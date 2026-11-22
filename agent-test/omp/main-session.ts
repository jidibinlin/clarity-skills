import { writeFileSync } from "node:fs";
import { join } from "node:path";
import type { ExtensionAPI, ExtensionContext } from "@oh-my-pi/pi-coding-agent";

export const IDENTITY = "agent-test/main";
export const NEW_TURN = "agent-test/turn";
export const TERMINAL_FAULT = "agent-test/fault";

export type Fault = {
	role: "subject" | "coordinator";
	model: string;
	cause: "model_mismatch" | "provider_auth_rejected" | "provider_error";
	http?: number;
	session: string; // Native JSONL filename, not the session UUID.
	entry: string;   // OMP's ID of the terminal marker in that file.
};

type Assistant = { role: string; provider?: string; model?: string; stopReason?: string; errorStatus?: number };

// OMP 19.0.1 model-selector: :auto is exact; concrete efforts (including
// inherit/off) also allow an unambiguous prefix of at least two characters.
const efforts = ["inherit", "off", "minimal", "low", "medium", "high", "xhigh", "max"];
export function withoutThinking(selector: string) {
	const colon = selector.lastIndexOf(":");
	if (colon <= selector.indexOf("/")) return selector;
	const level = selector.slice(colon + 1);
	// These concrete levels all have distinct two-letter prefixes.
	if (level === "auto" || (level.length >= 2 && efforts.some(e => e.startsWith(level)))) {
		return selector.slice(0, colon);
	}
	return selector;
}

export function pinnedModel(ctx: ExtensionContext, selector: string) {
	const base = withoutThinking(selector);
	if (base === selector) return selector;
	// The CLI tries the entire qualified literal ID before parsing the suffix.
	// Never use the fuzzy model resolver here: it may accept an unrelated model.
	const slash = selector.indexOf("/");
	const literal = ctx.modelRegistry.find(selector.slice(0, slash), selector.slice(slash + 1));
	return literal && `${literal.provider}/${literal.id}` === selector ? selector : base;
}

export function providerFailure(message: Assistant | undefined, expected: string) {
	if (message?.role !== "assistant" || message.stopReason !== "error" ||
		`${message.provider}/${message.model}` !== expected) return;
	// Only the provider's machine field, never chat, stderr, or the provider's free-text body.
	const http = message.errorStatus;
	const cause = http === 401 || http === 403 ? "provider_auth_rejected" : "provider_error";
	return { cause, ...(Number.isInteger(http) && http! >= 100 && http! <= 599 ? { http } : {}) } as const;
}

export default function mainSession(pi: ExtensionAPI) {
	const role = process.env.AGENT_TEST_ROLE;
	const model = process.env.AGENT_TEST_MODEL;
	const run = process.env.AGENT_TEST_RUN;
	if ((role !== "subject" && role !== "coordinator") || !model || !run) return;
	let owner: ExtensionContext | undefined;
	let providerModel: string;

	function marker(ctx: ExtensionContext, facts: Pick<Fault, "cause" | "http"> & { source?: string }) {
		const session = ctx.sessionManager.getSessionFile();
		pi.appendEntry(TERMINAL_FAULT, { role, model, ...facts });
		const entry = ctx.sessionManager.getLeafId();
		if (role === "coordinator" && session && entry) {
			pi.events.emit(TERMINAL_FAULT, { role, model, session, entry, cause: facts.cause, http: facts.http });
		}
	}

	async function guard(ctx: ExtensionContext) {
		if (ctx.agent.kind !== "main" || !owner) return;
		// `before_provider_request` also runs for advisors and side requests. Its ctx.model
		// is the REQUEST model; the startup context reads the live SESSION selection.
		const actual = owner.models.current();
		if (actual && `${actual.provider}/${actual.id}` === providerModel) return;
		try {
			marker(owner, { cause: "model_mismatch" });
			await owner.sessionManager.ensureOnDisk();
		} finally {
			// OMP treats thrown extension errors as diagnostics and would still send the
			// request. Do not return control to the request path on a mismatched model.
			process.exit(78);
		}
	}

	pi.on("session_start", async (_, ctx) => {
		if (ctx.agent.kind !== "main") return;
		owner = ctx;
		providerModel = pinnedModel(ctx, model);
		const sessionId = ctx.sessionManager.getSessionId();
		if (process.env.AGENT_TEST_OBSERVE === "1") {
			// Launcher PIDs can belong to shell wrappers. Only the native main can
			// identify its own OMP process and the session its room must mirror.
			try {
				const cli = Bun.which("omp");
				if (cli) writeFileSync(join(run, `${role}-view.json`),
					JSON.stringify({ pid: process.pid, sessionId, cli, path: process.env.PATH }),
					{ flag: "wx", mode: 0o600 });
			} catch { /* Observation is optional and never affects the model run. */ }
		}
		pi.appendEntry(IDENTITY, { role, model, providerModel, run, pid: process.pid, sessionId });
		await guard(ctx);
		await ctx.sessionManager.ensureOnDisk();
	});
	pi.on("before_agent_start", (_, ctx) => guard(ctx));
	pi.on("before_provider_request", (_, ctx) => guard(ctx));
	pi.on("agent_start", (_, ctx) => {
		if (ctx.agent.kind === "main") pi.appendEntry(NEW_TURN);
	});
	pi.on("agent_end", (event, ctx) => {
		if (ctx.agent.kind !== "main" || event.willContinue) return;
		// Unlike message_end, this is AFTER OMP's recovery, continuations and queued work.
		const last = event.messages.findLast(m => m.role === "assistant");
		if (last?.role !== "assistant") return;
		const failure = providerFailure(last, providerModel);
		if (!failure) return;
		const native = ctx.sessionManager.getBranch().findLast(e => e.type === "message" && e.message.role === "assistant");
		if (native?.type !== "message" || native.message.role !== "assistant" ||
			native.message.timestamp !== last.timestamp || !providerFailure(native.message, providerModel)) return;
		marker(ctx, { ...failure, source: native.id });
	});
}
