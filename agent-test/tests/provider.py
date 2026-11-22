"""Script the model side of OpenAI chat completions. OMP executes every tool call.

Each Provider represents one independently authenticated endpoint. The script
uses only the conversation sent by the client: in particular it cannot deliver
an IRC message, discover a PID, inspect a session, or write a run artifact.
"""

import json
import re
import secrets
import threading
import time
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


@dataclass(frozen=True)
class Reply:
    action: str
    data: str | dict | None = None


def read_tool(path):
    return Reply("read", {"i": "Reading scenario context", "path": path})


def send(pid, message):
    return Reply(
        "write",
        {
            "i": "Contacting repair partner",
            "path": f"agent://{pid}",
            "content": message,
        },
    )


def finish(outcome, reason):
    return Reply("finish_run", {"outcome": outcome, "reason": reason})


def content(message):
    value = message.get("content")
    if isinstance(value, list):
        return "\n".join(part["text"] for part in value if part.get("type") == "text")
    return value or ""


class Dialogue:
    """Pair the model's calls with actual tool responses, not assistant prose."""

    def __init__(self, request):
        self.tools = {
            tool["function"]["name"]
            for tool in request.get("tools", [])
            if "function" in tool
        }
        self.inputs = []
        self.incoming = []
        self.results = []
        self.turn_start = -1
        self.verified_peer = None
        pending_roster = None
        calls = {}
        for index, message in enumerate(request["messages"]):
            role, text = message["role"], content(message)
            if role == "assistant":
                for call in message.get("tool_calls", []):
                    fn = call["function"]
                    calls[call["id"]] = fn["name"], json.loads(fn["arguments"])
            elif role == "tool" and message.get("tool_call_id") in calls:
                name, args = calls[message["tool_call_id"]]
                self.results.append((index, name, args, text))
                pending_roster = text if name == "read" and args.get("path") == "agent://peers" else None
                if pending_roster is not None:
                    self.verified_peer = None
            elif role in ("user", "developer", "system"):
                self.inputs.append(text)
                # OMP emits hook additionalContext as a separate developer
                # message after the tool result (user on compatible endpoints
                # without developer roles), not as part of the native roster.
                if pending_roster is not None and role in ("developer", "user"):
                    verified = VERIFIED.search(text)
                    if verified and verified[1] in PEER.findall(pending_roster):
                        self.verified_peer = verified[1]
                        pending_roster = None
                        continue
                    if "No verified subject main yet." in text:
                        pending_roster = None
                        continue
                pending_roster = None
                if role == "user":
                    self.turn_start = index
                for match in re.finditer(
                    r"Incoming IRC message from agent `(\d+)`[^:\n]*:\s*\n([^\n]+)",
                    text,
                ):
                    self.incoming.append(match.groups())

    def results_for(self, name, *, path=None, this_turn=False):
        return [
            text
            for index, tool, args, text in self.results
            if tool == name
            and (path is None or args.get("path") == path)
            and (not this_turn or index > self.turn_start)
        ]

    def sent(self, prefix):
        return any(
            tool == "write"
            and args["content"].startswith(prefix)
            and "Delivered to" in text
            for _, tool, args, text in self.results
        )


PROMPT = re.compile(r'(/[^\n`"<>]*?/coordinator-prompt\.md)')
PEER = re.compile(r"^\s*-\s*agent://(\d+)\s+\(", re.MULTILINE)
VERIFIED = re.compile(r"^Verified subject main: agent://(\d+)\. Use this address for the scenario\.$", re.MULTILINE)
WAITING = Reply("text", "Waiting for the repair desk.")
HELPED = "The replacement filament has been fitted."
QUESTION = "Which detail is available for "
SYMPTOM = "The lamp flickers; "
NO_SERIAL = "No serial number is available; "
DELIVERY = "The lamp is repaired; receipt "
BLOCKED = "Dispatch is blocked before booking; "


def coordinator(d, case):
    if case == "owner_denied":
        return Reply("denied")
    if case == "owner_hang" or (case == "final_hang" and d.results_for("finish_run")):
        return Reply("hang")
    if d.results_for("finish_run") or d.results_for("report_run_fault"):
        return Reply("text", "Report submitted.")

    # Read the actual retained prompt before acting. Use the caller's run ID
    # for the first ticket; the desk learns our PID only from a real delivery.
    prompt = next(
        (match[1] for text in reversed(d.inputs) if (match := PROMPT.search(text))),
        None,
    )
    if prompt is None:
        return Reply("text", "I have not received a scenario prompt path.")
    brief = d.results_for("read", path=prompt)
    if not brief:
        return read_tool(prompt)
    if "lamp" not in brief[-1].lower():
        return Reply("text", "I have not received a lamp repair brief.")
    peer = d.verified_peer
    if not peer:
        if d.results_for("read", path="agent://peers", this_turn=True):
            return WAITING  # let the discovery wake arrive before trying again
        return read_tool("agent://peers")
    if not d.sent("Repair ticket "):
        return send(
            peer, f"Repair ticket {prompt.split('/')[-2]}: please repair the lamp."
        )

    # Only an actual message from the discovered peer counts as a question or
    # delivery. A progress summary or our own earlier tool input does not.
    last = next((msg for sender, msg in reversed(d.incoming) if sender == peer), "")
    if last.startswith(QUESTION):
        ticket = re.search(r"\brepair-\d+\b", last)
        answer = NO_SERIAL if case == "material" else SYMPTOM
        if ticket and not d.sent(answer):
            return send(peer, answer + ticket[0] + ".")
    if last.startswith(BLOCKED):
        return finish(
            "scenario_error",
            "Dispatch stopped before booking: the required device serial number is missing.",
        )
    delivered = last.startswith(DELIVERY)
    if delivered and case != "after_delivery":
        return finish("completed", last)

    # After delivery in the 401 race, deliberately let the desk finish its
    # failed turn before reporting the already received receipt. No cross-
    # endpoint signal or fixed sleep is needed to order these events.
    due = "inspection due" in d.inputs[-1].lower() if d.inputs else False
    if due or delivered:
        path = f"agent://{peer}"
        if not d.results_for("read", path=path, this_turn=True):
            return read_tool(path)
        inspections = d.results_for("inspect_subject", this_turn=True)
        if not inspections:
            return Reply("inspect_subject", {})
        evidence = json.loads(inspections[-1])
        if evidence.get("session") and evidence.get("entry"):
            if delivered:
                return finish("completed", last)
            return Reply(
                "report_run_fault", {k: evidence[k] for k in ("session", "entry")}
            )
    return WAITING


def subject(d, case, endpoint):
    if case == "denied" or (case == "after_delivery" and d.sent(DELIVERY)):
        return Reply("denied")
    if case == "endless":
        return Reply("hang")
    if not d.incoming:
        return Reply("text", "Waiting for a repair request.")
    owner, last = d.incoming[-1]
    ticket = f"repair-{owner}"
    if last.startswith("Repair ticket ") and not d.sent(QUESTION):
        detail = (
            "the device serial number" if case == "material" else "the fault symptom"
        )
        return send(owner, QUESTION + ticket + "? I need " + detail + ".")
    if last.startswith(NO_SERIAL) and not d.sent(BLOCKED):
        return send(owner, BLOCKED + ticket + " has no device serial number.")
    if not last.startswith(SYMPTOM) or ticket not in last or d.sent(DELIVERY):
        return Reply("text", "Awaiting instructions.")

    if case == "helper":
        if not d.results_for("task"):
            return Reply(
                "task",
                {
                    "i": "Assigning lamp repair",
                    "context": "A flickering lamp needs a repair.",
                    "tasks": [
                        {
                            "name": "Electrician",
                            "task": "Replace the faulty lamp filament and report the repair.",
                            "solutionSpace": "One repair: replace the faulty filament.",
                        }
                    ],
                },
            )
        if not any(
            HELPED in text
            for text in d.inputs + d.results_for("task") + d.results_for("wait")
        ):
            return (
                Reply("wait", {"i": "Awaiting electrician result"})
                if "wait" in d.tools
                else WAITING
            )

    receipts = d.results_for("bash")
    if not receipts:
        cmd = (
            f"printf '%s\\n' \"$LAMP_ENV_VERSION\" > environment.txt && "
            'printf \'%s\\n\' "${ALPHA_KEY:+alpha}" "${BETA_KEY:+beta}" > credential-scope.txt && '
            f"printf '%s\\n' '{ticket}' > {ticket}.txt && "
        )
        if case == "normal" and endpoint.edits_material(owner):
            cmd += f"if test -f material.txt; then printf '%s\\n' '{ticket}' >> material.txt; fi && "
        return Reply(
            "bash",
            {"i": "Saving repair receipt", "command": cmd + "echo RECEIPT_SAVED"},
        )
    if "RECEIPT_SAVED" not in receipts[-1]:
        return Reply("text", "I could not save the repair receipt.")
    return send(owner, DELIVERY + ticket + ".")


class Provider:
    def __init__(self):
        self.key = secrets.token_urlsafe(32)
        self._lock = threading.Lock()
        self._calls = []
        self.context_markers = set()
        self._first_writer = None
        self.closed = threading.Event()

    @property
    def observed_peer_list(self):
        return any(c.get("readPeers") for c in self.calls)

    def __enter__(self):
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
        self.server.fixture = self
        self.url = f"http://127.0.0.1:{self.server.server_port}/v1"
        self.thread = threading.Thread(
            target=self.server.serve_forever,
            kwargs={"poll_interval": 0.05},
            daemon=True,
        )
        self.thread.start()
        return self

    def __exit__(self, *exc):
        self.closed.set()  # release all deliberately hanging requests
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    @property
    def calls(self):
        with self._lock:
            return self._calls.copy()

    def edits_material(self, owner):
        with self._lock:
            if self._first_writer is None:
                self._first_writer = owner
            return self._first_writer == owner

    def respond(self, request, authorized):
        model = request["model"]
        d = Dialogue(request)
        agent = {"read", "write"} <= d.tools
        if not authorized:
            reply = Reply("denied")
        elif not agent:
            reply = Reply("text", "Lamp repair")  # title or other auxiliary prompt
        elif model == "helper":
            reply = Reply("text", HELPED)
        elif model.startswith("owner-"):
            reply = coordinator(d, model.removeprefix("owner-"))
        elif model.startswith("desk-"):
            reply = subject(d, model.removeprefix("desk-"), self)
        else:
            reply = Reply("text", "No repair scenario assigned.")
        record = {
            "model": model,
            "authorized": authorized,
            "kind": "agent" if agent else "auxiliary",
            "action": reply.action,
        }
        if agent and model.startswith("owner-"):
            record["readPeers"] = bool(d.results_for("read", path="agent://peers"))
        if self.context_markers and agent:
            prompt = json.dumps(request["messages"])
            record["markers"] = {
                marker for marker in self.context_markers if marker in prompt
            }
        with self._lock:
            self._calls.append(record)
        return reply


class _Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        # Do not print headers, request bodies, or access logs during tests.
        pass

    def do_POST(self):
        if self.path != "/v1/chat/completions":
            self.send_error(404)
            return
        request = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        provider = self.server.fixture
        authorized = self.headers.get("Authorization") == "Bearer " + provider.key
        reply = provider.respond(request, authorized)
        if reply.action == "hang":
            provider.closed.wait()
            return
        if reply.action == "denied":
            self.respond(
                401,
                "application/json",
                json.dumps(
                    {
                        "error": {
                            "type": "authentication_error",
                            "code": "invalid_api_key",
                            "message": "Model access denied.",
                        }
                    }
                ).encode(),
            )
            return
        response = {
            "id": "chatcmpl-" + secrets.token_hex(8),
            "created": int(time.time()),
            "model": request["model"],
        }
        message = {"role": "assistant"}
        if reply.action == "text":
            message["content"] = reply.data
            finish_reason = "stop"
        else:
            call = {
                "id": "call_" + secrets.token_hex(8),
                "type": "function",
                "function": {"name": reply.action, "arguments": json.dumps(reply.data)},
            }
            message["tool_calls"] = [call]
            finish_reason = "tool_calls"
        if request.get("stream"):
            if "tool_calls" in message:
                message["tool_calls"][0]["index"] = 0
            response["object"] = "chat.completion.chunk"

            def chunk(delta, reason):
                return (
                    "data: "
                    + json.dumps(
                        {
                            **response,
                            "choices": [
                                {"index": 0, "delta": delta, "finish_reason": reason}
                            ],
                        }
                    )
                    + "\n\n"
                )

            self.respond(
                200,
                "text/event-stream",
                (
                    chunk(message, None) + chunk({}, finish_reason) + "data: [DONE]\n\n"
                ).encode(),
            )
        else:
            response.update(
                object="chat.completion",
                choices=[
                    {"index": 0, "message": message, "finish_reason": finish_reason}
                ],
            )
            self.respond(200, "application/json", json.dumps(response).encode())

    def respond(self, status, mime, data):
        try:
            self.send_response(status)
            self.send_header("Content-Type", mime)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except (BrokenPipeError, ConnectionResetError):
            # The real supervisor may stop OMP while a response is in flight.
            pass
