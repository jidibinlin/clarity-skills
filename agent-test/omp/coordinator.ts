import { closeSync, constants, createReadStream, openSync, writeSync } from "node:fs";
import { readdir } from "node:fs/promises";
import { basename, join } from "node:path";
import { createInterface } from "node:readline";
import type { ExtensionAPI, ExtensionContext } from "@oh-my-pi/pi-coding-agent";
import { IDENTITY, NEW_TURN, TERMINAL_FAULT, pinnedModel, providerFailure, withoutThinking, type Fault } from "./main-session.ts";

type Subject = { run: string; model: string };
type MainIdentity = { session: string; sessionId: string; pid: number };

// Consume the native journal, not text from chat, directory mtimes, or a path chosen by the model.
// OMP stores child sessions under the workspace's session directory too. Only the main's own
// identity, the root header, and a settled error from its most recent turn can establish a fault.
async function inspectFile(session: string, peer: Subject): Promise<{ main: MainIdentity; fault?: Fault } | undefined> {
	let sessionId: string | undefined;
	let main: MainIdentity | undefined;
	let providerModel: string | undefined;
	let assistant: { id: string; failure?: Pick<Fault, "cause" | "http"> } | undefined;
	let fault: Fault | undefined;
	const stream = createReadStream(session, { encoding: "utf8" });
	try {
		for await (const line of createInterface({ input: stream, crlfDelay: Infinity })) {
			if (!line) continue;
			let r;
			try { r = JSON.parse(line); }
			catch { return; } // A concurrent writer may not have finished this record; never cite a partial journal.
			if (r.type === "session") {
				if (sessionId || typeof r.id !== "string" || !r.id || r.parentSession || r.cwd !== join(peer.run, "workspace")) return;
				sessionId = r.id;
			} else if (r.type === "custom" && r.customType === IDENTITY) {
				const d = r.data;
				if (!sessionId || d?.sessionId !== sessionId || d.role !== "subject" || d.run !== peer.run ||
					!Number.isSafeInteger(d.pid) || d.pid <= 0 || d.pid === process.pid || d.model !== peer.model ||
					(d.providerModel !== peer.model && d.providerModel !== withoutThinking(peer.model))) return;
				// Only the subject profile has the catalog that disambiguates a literal
				// ID ending in :low/:max/etc. The main-session guard binds it at startup.
				providerModel = d.providerModel;
				main = { pid: d.pid, sessionId, session };
			} else if (r.type === "custom" && r.customType === NEW_TURN) {
				assistant = undefined;
				fault = undefined;
			} else if (providerModel && r.type === "message" && r.message?.role === "assistant") {
				assistant = { id: r.id, failure: providerFailure(r.message, providerModel) };
				fault = undefined;
			} else if (providerModel && r.type === "custom" && r.customType === TERMINAL_FAULT) {
				const d = r.data;
				if (!d || d.role !== "subject" || d.model !== peer.model || typeof r.id !== "string") continue;
				if (d.cause !== "model_mismatch" && (!assistant?.failure || assistant.id !== d.source ||
					d.cause !== assistant.failure.cause || d.http !== assistant.failure.http)) continue;
				fault = { role: "subject", model: peer.model, cause: d.cause, http: d.http, session, entry: r.id };
			}
		}
	} catch (error) {
		if ((error as NodeJS.ErrnoException).code === "ENOENT") return;
		throw error;
	} finally {
		stream.destroy();
	}
	if (main) return { main, fault };
}

function result<T>(details: T) {
	return { content: [{ type: "text" as const, text: JSON.stringify(details) }], details };
}

export default function coordinator(pi: ExtensionAPI) {
	if (process.env.AGENT_TEST_ROLE !== "coordinator") return;
	const z = pi.zod;
	let owner: ExtensionContext | undefined;
	let ownerId: string;
	let fd: number;
	let peer: Subject;
	let ownModel: string;
	let ownProviderModel: string;
	let peerDir: string;
	let subjectMain: MainIdentity | undefined;
	let discoveryStarted = false;
	let discovery: Timer | undefined;
	let wake: Timer | undefined;
	let pollMs: number;
	let discoveryMs: number;
	let finished = false;
	let faultSent = false;

	function isOwner(ctx: ExtensionContext) {
		return ctx.agent.kind === "main" && ctx.sessionManager.getSessionId() === ownerId;
	}
	function active(ctx: ExtensionContext) {
		if (!isOwner(ctx) || finished || faultSent) throw new Error("Not the active coordinator main session.");
	}
	function notify(event: object) {
		writeSync(fd, JSON.stringify(event) + "\n");
	}
	function cancelWake() {
		if (wake) owner!.clearTimer(wake);
		wake = undefined;
	}
	function cancelTimers() {
		cancelWake();
		if (discovery) owner!.clearTimer(discovery);
		discovery = undefined;
	}
	function report(facts: Fault | { role: "coordinator"; model: string; cause: "discovery_timeout" }) {
		if (faultSent || finished) return;
		notify({ type: "fault", ...facts });
		faultSent = true;
		cancelTimers();
	}
	function armWake() {
		if (wake || faultSent || finished || !discoveryStarted) return;
		wake = owner!.setTimeout(() => {
			wake = undefined;
			if (finished || faultSent || !owner!.isIdle() || owner!.hasPendingMessages()) return;
			pi.sendMessage({ customType: "agent-test/inspection", display: true, content:
				"Agent-test inspection due. " + (subjectMain
					? `Handle any delivered peer message first; otherwise read agent://${subjectMain.pid} and inspect_subject if needed. Do not send a nudge.`
					: "Read agent://peers again; send the scenario as soon as the subject is identified.")
			}, { triggerTurn: true });
		}, pollMs);
	}

	async function evidence() {
		if (!subjectMain) throw new Error("No discovered subject main session.");
		const snapshot = await inspectFile(subjectMain.session, peer);
		if (snapshot?.main.sessionId !== subjectMain.sessionId || snapshot.main.pid !== subjectMain.pid) {
			throw new Error("Subject identity or journal unavailable; no fault verified.");
		}
		return snapshot.fault;
	}

	async function matchPeer(visible: Set<number>) {
		// Sibling profiles use the same OMP-encoded cwd directory name, chosen by OMP itself.
		let files;
		try { files = await readdir(peerDir, { withFileTypes: true }); }
		catch (error) {
			if ((error as NodeJS.ErrnoException).code === "ENOENT") return;
			throw error;
		}
		let bound: MainIdentity | undefined;
		for (const file of files) {
			if (!file.isFile() || !file.name.endsWith(".jsonl")) continue;
			const path = join(peerDir, file.name);
			const candidate = await inspectFile(path, peer);
			if (!candidate || !visible.has(candidate.main.pid)) continue;
			if (bound) return; // Ambiguous: wait for a unique corroborated native identity.
			bound = candidate.main;
		}
		return bound;
	}

	pi.on("session_start", async (_, ctx) => {
		if (ctx.agent.kind !== "main" || owner) return;
		owner = ctx;
		ownerId = ctx.sessionManager.getSessionId();
		peer = { model: process.env.AGENT_TEST_SUBJECT_MODEL!, run: process.env.AGENT_TEST_RUN! };
		ownModel = process.env.AGENT_TEST_MODEL!;
		ownProviderModel = pinnedModel(ctx, ownModel);
		pollMs = Number(process.env.AGENT_TEST_POLL) * 1000;
		discoveryMs = Number(process.env.AGENT_TEST_DISCOVERY) * 1000;
		const session = ctx.sessionManager.getSessionFile();
		const inherited = Number(process.env.AGENT_TEST_FD);
		delete process.env.AGENT_TEST_FD;
		try {
			if (!session || !Number.isSafeInteger(inherited) || inherited < 3 || !peer.run || !peer.model ||
				!(pollMs > 0) || !(discoveryMs > 0)) throw Error();
			// Reopen the anonymous pipe CLOEXEC and remove its inherited handle before business tools run.
			fd = openSync(`/dev/fd/${inherited}`, constants.O_WRONLY | constants.O_NONBLOCK);
			closeSync(inherited);
			await ctx.sessionManager.ensureOnDisk();
			notify({ type: "session", path: session });
		} catch {
			// A missing control channel is a startup fault, not an unsupervised test run.
			process.exit(70);
		}
		peerDir = join(peer.run, "home/.omp/profiles/subject/agent/sessions", basename(ctx.sessionManager.getSessionDir()));
		pi.events.on(TERMINAL_FAULT, (data: unknown) => {
			const f = data as Fault;
			if (f?.role === "coordinator" && f.model === ownModel && f.session === session) report(f);
		});

		// Register only in the main session; check the actual caller too (advisor tools can share a runner).
		pi.registerTool({ name: "inspect_subject", label: "Inspect subject", loadMode: "essential", approval: "read",
			description: "Read the current subject main session for a settled machine fault. Silence or running is not a fault.",
			parameters: z.object({}), async execute(_id, _args, _signal, _update, caller) {
				active(caller);
				return result(await evidence() ?? { fault: null });
			} });
		pi.registerTool({ name: "report_run_fault", label: "Report verified fault", loadMode: "essential",
			description: "If a verified terminal subject fault prevents a still-required delivery, cite the session and entry from inspect_subject. Never cite conversation text.",
			parameters: z.object({ session: z.string(), entry: z.string() }), async execute(_id, args, _signal, _update, caller) {
				active(caller);
				const f = await evidence();
				if (!f || args.session !== f.session || args.entry !== f.entry) throw new Error("No matching current terminal fault in this subject main session.");
				active(caller);
				report(f);
				return result({ reported: true });
			} });
		pi.registerTool({ name: "finish_run", label: "Finish scenario", loadMode: "essential",
			description: "Report the achieved scenario outcome, not a judgment about the tested skill. For scenario_error explain where and why the scenario cannot proceed.",
			parameters: z.object({ outcome: z.enum(["completed", "scenario_error"]), reason: z.string() }),
			async execute(_id, { outcome, reason }, _signal, _update, caller) {
				active(caller);
				if (!subjectMain) throw new Error("The scenario has not started: first discover the subject main session.");
				if (outcome === "scenario_error" && !reason.trim()) throw new Error("Explain the blocked step and its cause.");
				finished = true;
				cancelTimers();
				return result({ outcome, reason });
			} });
	});

	pi.on("before_agent_start", (event, ctx) => {
		if (!isOwner(ctx)) return;
		return { systemPrompt: [...event.systemPrompt, `You are the scenario coordinator (agent://${process.pid}). Read the submitter's coordinator-prompt.md at the supplied path; play the user, do not do the subject's work. First read agent://peers. Only use the peer explicitly confirmed as the verified subject by the framework after cross-checking the native peer list with the subject main session. An empty list or a visible but unconfirmed PID is not a failure: end your turn and re-query on the discovery wake. Use native write to the verified subject address to send the first task immediately upon discovery and to answer actual questions. The subject receives your return address in native IRC. Decide the next message from actual replies and the submitter's instructions, never a fixed script.
When awaiting an answer, END your turn; do not call wait, sleep or create polling jobs. Peer messages wake you directly. On “Agent-test inspection due.” process messages already delivered first; if there is none, read the verified subject's agent:// address, then inspect_subject({}) if its summary is insufficient. Do not send reminders or ask the subject for heartbeats. If still waiting, end your turn. A current terminal fault from inspect_subject can be cited via report_run_fault({session,entry}) ONLY if it blocks a still-required delivery. Silence, progress or an empty peer list is not a terminal fault. A fault after delivery does not undo the delivery.
Use finish_run({outcome:"completed",reason}) when the actual delivery meets the goal. If the materials/scenario make it impossible to continue, use finish_run({outcome:"scenario_error",reason}) giving the blocked step and why. After a successful report finish your final reply without starting new work.`] };
	});
	pi.on("tool_call", (event, ctx) => {
		if (!isOwner(ctx)) return;
		if (event.toolName === "write" && typeof event.input.path === "string") {
			// write accepts a pasted [path#TAG] as well as a raw path. Recognize the
			// remote PID before any display selector; only authorize a plain main
			// recipient, not a path that could normalize to a different recipient.
			const raw = event.input.path.trim();
			const target = raw.startsWith("[") && raw.endsWith("]")
				? raw.slice(1, -1).replace(/#[\da-f]{4}$/i, "") : raw;
			const address = /^agent:\/\/([^/:?#]+)/i.exec(target);
			if (address) {
				let host = address[1];
				try { host = decodeURIComponent(host); } catch { /* OMP keeps the raw host. */ }
				if (/^\d+$/.test(host) && Number(host) !== process.pid) {
					const recipient = target.slice(address[0].length).split(/[?#]/, 1)[0];
					const main = recipient === "" || recipient === "/" || recipient === "/Main" || recipient === "/Main/";
					if (faultSent || finished || Number(host) !== subjectMain?.pid || !main) {
						return { block: true, reason: "Only message the verified remote main session. Re-query agent://peers while awaiting discovery." };
					}
				}
			}
		}
		if (faultSent || finished) return;
		if (event.toolName === "read" && event.input.path === "agent://peers" && !discoveryStarted) {
			discoveryStarted = true;
			discovery = ctx.setTimeout(() => { if (!subjectMain) report({ role: "coordinator", model: ownModel, cause: "discovery_timeout" }); }, discoveryMs);
		}
	});
	pi.on("tool_result", async (event, ctx) => {
		if (!isOwner(ctx) || event.isError || event.toolName !== "read" || event.input.path !== "agent://peers") return;
		if (!subjectMain && !faultSent && !finished) {
			const visible = new Set<number>();
			for (const part of event.content) {
				if (part.type !== "text") continue;
				for (const match of part.text.matchAll(/^\s*-\s+agent:\/\/(\d+)(?=\s|$)/gm)) visible.add(Number(match[1]));
			}
			const found = visible.size ? await matchPeer(visible) : undefined;
			if (found && !faultSent && !finished) {
				subjectMain = found;
				if (discovery) ctx.clearTimer(discovery);
				discovery = undefined;
			}
		}
		// Preserve OMP's unmodified native roster. The model receives only a corroborated
		// address in the extension-authored instruction, never an inferred launcher PID.
		return { additionalContext: subjectMain
			? `Verified subject main: agent://${subjectMain.pid}. Use this address for the scenario.`
			: "No verified subject main yet. End your turn and read agent://peers on the next inspection wake." };
	});
	pi.on("message_end", ({ message }, ctx) => {
		if (!isOwner(ctx) || faultSent || message.role !== "assistant" || `${message.provider}/${message.model}` !== ownProviderModel) return;
		if (message.stopReason !== "error" && message.stopReason !== "aborted" && message.content.some(c =>
			c.type === "toolCall" || (c.type === "text" && c.text.trim().length > 0))) notify({ type: "heartbeat" });
	});
	pi.on("agent_start", (_, ctx) => { if (isOwner(ctx)) cancelWake(); });
	pi.on("agent_end", (event, ctx) => {
		if (!isOwner(ctx)) return;
		if (finished) { ctx.shutdown(); return; }
		if (!event.willContinue || event.awaitingAsyncWork) armWake();
	});
	pi.on("session_shutdown", (_, ctx) => { if (isOwner(ctx)) cancelTimers(); });
}
