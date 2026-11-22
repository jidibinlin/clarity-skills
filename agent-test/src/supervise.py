#!/usr/bin/env python3
"""Private Linux worker, entered once inside the selected Nix environment."""

import ctypes
import errno
import fcntl
import json
import os
import re
import selectors
import signal
import stat
import struct
import subprocess
import sys
import termios
from datetime import datetime, timezone
from pathlib import Path
from time import monotonic

import yaml

ROLES = ("subject", "coordinator")
SHARE = Path(__file__).resolve().parents[2] / "share/agent-test"
FAULTS = {
    "model_mismatch",
    "provider_auth_rejected",
    "provider_error",
    "discovery_timeout",
}
FINAL_CHECK = (
    b"The subject process has exited. Check the delivery already received; if it "
    b"establishes the scenario outcome, report it with finish_run now. Do not "
    b"wait for another reply or classify process exit itself as a scenario error.\r"
)


def emit(stream, **record):
    stream.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
    stream.flush()


def log_event(log, event, **fields):
    emit(log, event=event, timestamp=datetime.now(timezone.utc).isoformat(), **fields)


def own_descendants():
    # The per-HOME daemon and OMP tool jobs may double-fork or call setsid().
    # A new session alone cannot reclaim them. Adopt *only* this run's orphans.
    libc = ctypes.CDLL(None, use_errno=True)
    if libc.prctl(36, 1, 0, 0, 0) != 0:  # PR_SET_CHILD_SUBREAPER
        code = ctypes.get_errno()
        raise OSError(code, os.strerror(code))
    return Path(f"/proc/self/task/{os.getpid()}/children")


def sessions(run, role):
    return run / "home/.omp/profiles" / role / "agent/sessions"


def native_path(run, role, value):
    if not isinstance(value, str):
        return None
    path = Path(value)
    if not path.is_absolute() or path.suffix != ".jsonl":
        return None
    path = path.resolve()
    return path if path.is_relative_to(sessions(run, role)) else None


class Evidence:
    """Tail only the coordinator main file bound by its private session event."""

    def __init__(self, run):
        self.run = run
        self.path = None
        self.identity = None
        self.offset = 0
        self.header_offset = 0
        self.header_ok = False
        self.intact = True
        self.report = None

    def bind(self, path):
        if self.path is None:
            self.path = native_path(self.run, "coordinator", path)

    def scan(self, final=False):
        if self.path is None:
            return False
        try:
            fd = os.open(self.path, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW)
            with os.fdopen(fd, "rb") as stream:
                info = os.fstat(stream.fileno())
                if not stat.S_ISREG(info.st_mode):
                    return False
                identity = (info.st_dev, info.st_ino)
                if final or identity != self.identity or info.st_size < self.offset:
                    self.offset = 0
                    self.header_offset = 0
                    self.identity = identity
                    self.header_ok = False
                    self.intact = True
                stream.seek(self.offset)
                while line := stream.readline():
                    if not line.endswith(b"\n"):
                        if final:
                            self.intact = False
                        break  # The writer has not finished this entry yet.
                    start = self.offset
                    self.offset += len(line)
                    try:
                        entry = json.loads(line)
                        if not isinstance(entry, dict):
                            raise TypeError
                    except (TypeError, ValueError, UnicodeError):
                        self.intact = False
                        continue
                    # OMP's optional v1 title slot precedes the native header.
                    # No other record can move the expected header position.
                    if (
                        start == 0
                        and entry.get("type") == "title"
                        and entry.get("v") == 1
                        and all(
                            isinstance(entry.get(k), str)
                            for k in ("title", "updatedAt", "pad")
                        )
                        and (
                            "source" not in entry or entry["source"] in ("auto", "user")
                        )
                    ):
                        self.header_offset = self.offset
                        continue
                    if start == self.header_offset:
                        self.header_ok = (
                            entry.get("type") == "session"
                            and isinstance(entry.get("id"), str)
                            and self.path.stem.endswith("_" + entry["id"])
                            and not entry.get("parentSession")
                            and entry.get("cwd") == str(self.run / "workspace")
                        )
                    elif self.header_ok and self.report is None:
                        self.accept(entry)
        except OSError:
            return False
        return self.header_ok and self.intact

    def accept(self, entry):
        msg = entry.get("message")
        if (
            entry.get("type") != "message"
            or not isinstance(msg, dict)
            or msg.get("role") != "toolResult"
            or msg.get("toolName") != "finish_run"
            or msg.get("isError") is not False
        ):
            return
        details = msg.get("details")
        if not isinstance(details, dict):
            return
        outcome, reason = details.get("outcome"), details.get("reason")
        if (
            outcome in ("completed", "scenario_error")
            and isinstance(reason, str)
            and (outcome == "completed" or reason.strip())
        ):
            self.report = (outcome, reason)


def role_environment(run, credential_names):
    # Keep the project's Nix toolchain and declared build variables, not paths
    # selecting a different OMP home, profile, session directory or daemon.
    env = {
        k: v
        for k, v in os.environ.items()
        if k not in credential_names
        and not k.startswith(("PI_", "OMP_", "AGENT_TEST_", "XDG_"))
    }
    home = run / "home"
    # OMP stops ancestor discovery before os.tmpdir(). Without that ceiling,
    # launching from another Git repository imports its AGENTS.md and skills.
    env.update(
        HOME=str(home),
        PWD=str(run / "workspace"),
        TMPDIR=str(run),
        TMP=str(run),
        TEMP=str(run),
        GIT_CEILING_DIRECTORIES=str(run),
        TERM="xterm-256color",
        AGENT_TEST_RUN=str(run),
    )
    return env


def controlling_terminal():
    # Popen starts a new session before calling this hook. This supervisor is
    # single-threaded; no Python threads or locks survive the fork.
    fcntl.ioctl(0, termios.TIOCSCTTY, 0)


class Supervisor:
    def __init__(self, run, payload, log, children_file):
        self.run = run
        self.log = log
        self.children_file = children_file
        self.policy = payload["policy"]
        self.observe = payload.get("observe", True)
        self.models = {r: payload["roles"][r]["model"] for r in ROLES}
        self.procs = {}
        self.ptys = {}
        self.startup_output = {r: bytearray() for r in ROLES}
        self.sel = selectors.DefaultSelector()
        self.control = bytearray()
        self.evidence = Evidence(run)
        self.fault = None
        self.interrupt = None
        self.last_beat = None
        self.until = None

    def on_signal(self, signum, _frame):
        if self.interrupt is None:
            self.interrupt = signal.Signals(signum).name

    def role_overlay(self, role):
        # Preserve the content of the submitted profile, but pin its declared
        # model roles above workspace settings, as --model does for default.
        # OMP deep-merges --config: an omitted role remains project/native.
        profile = sessions(self.run, role).parent
        with (profile / "config.yml").open(encoding="utf-8") as stream:
            models = yaml.safe_load(stream)["modelRoles"]
        overlay = profile.parent / "run-role.yml"
        with overlay.open("x", encoding="utf-8") as stream:
            # --config also takes precedence over workspace/profile auto-control.
            # Keep the project's relay, browser URL and other collab settings.
            yaml.safe_dump({
                "modelRoles": models,
                "collab": {"autoStart": "view" if self.observe else "off"},
            }, stream)
        return overlay

    def spawn(self, role, env, overlay, fd=None):
        model = self.models[role]
        work = self.run / "workspace"
        env.update(AGENT_TEST_ROLE=role, AGENT_TEST_MODEL=model,
                   AGENT_TEST_OBSERVE="1" if self.observe else "0")
        args = [
            "omp",
            "--profile",
            role,
            "--cwd",
            str(work),
            "--model",
            model,
            "--config",
            str(SHARE / "locked.yml"),
            "--config",
            str(overlay),
            "--no-title",
        ]
        if role == "coordinator":
            env.update(
                AGENT_TEST_FD=str(fd),
                AGENT_TEST_SUBJECT_MODEL=self.models["subject"],
                AGENT_TEST_POLL=str(self.policy["poll"]),
                AGENT_TEST_DISCOVERY=str(self.policy["discovery"]),
            )
            args.extend(["-e", str(SHARE / "coordinator.ts")])
        args.extend(["-e", str(SHARE / "main-session.ts")])
        if role == "coordinator":
            args.extend(
                [
                    "--",
                    (
                        f"Read {self.run / 'coordinator-prompt.md'} for your scenario. "
                        "Follow your coordinator instructions to find and converse with the subject."
                    ),
                ]
            )
        master, slave = os.openpty()
        try:
            fcntl.ioctl(slave, termios.TIOCSWINSZ, struct.pack("HHHH", 40, 132, 0, 0))
            os.set_blocking(master, False)
            proc = subprocess.Popen(
                args,
                cwd=work,
                env=env,
                stdin=slave,
                stdout=slave,
                stderr=slave,
                close_fds=True,
                pass_fds=(() if fd is None else (fd,)),
                start_new_session=True,
                preexec_fn=controlling_terminal,  # noqa: PLW1509 — single-threaded Linux worker
            )
            self.procs[role] = proc
            self.ptys[role] = master
            self.sel.register(master, selectors.EVENT_READ, role)
        except BaseException:
            os.close(master)
            raise
        finally:
            os.close(slave)
            env.clear()
        if role == "coordinator":
            self.last_beat = monotonic()
        log_event(self.log, "started", role=role, model=model, pid=proc.pid)

    def launch(self, roles):
        role = "subject"
        try:
            base = role_environment(
                self.run, {key for cfg in roles.values() for key in cfg["env"]}
            )
            self.spawn(role, base | roles[role].pop("env"), self.role_overlay(role))
            if self.interrupt:
                return "interrupted", {"signal": self.interrupt}
            role = "coordinator"
            reader, writer = os.pipe()
            try:
                os.set_blocking(reader, False)
                self.sel.register(reader, selectors.EVENT_READ, "control")
                self.spawn(role, base | roles[role].pop("env"), self.role_overlay(role), writer)
            finally:
                os.close(writer)
        except (OSError, subprocess.SubprocessError, ValueError) as exc:
            cause = (
                errno.errorcode.get(exc.errno, "os_error")
                if isinstance(exc, OSError)
                else type(exc).__name__
            )
            return "startup_failure", {
                "role": role,
                "model": self.models[role],
                "step": "launch_omp",
                "cause": cause,
            }
        finally:
            roles.clear()  # Popen does not retain its environment.
        return None

    def control_message(self, data):
        try:
            msg = json.loads(data)
        except (ValueError, UnicodeError):
            return
        if not isinstance(msg, dict):
            return
        kind = msg.get("type")
        if kind == "session":
            self.evidence.bind(msg.get("path"))
        elif kind == "heartbeat":
            self.last_beat = monotonic()
        elif kind == "fault" and self.fault is None:
            role, cause = msg.get("role"), msg.get("cause")
            if (
                role not in ROLES
                or cause not in FAULTS
                or msg.get("model") != self.models[role]
            ):
                return
            detail = {"role": role, "model": self.models[role], "cause": cause}
            if cause != "discovery_timeout":
                path = native_path(self.run, role, msg.get("session"))
                entry = msg.get("entry")
                if (
                    not path
                    or not isinstance(entry, str)
                    or not re.fullmatch(r"[\w-]+", entry)
                ):
                    return
                detail.update(session=str(path), entry=entry)
            elif role != "coordinator":
                return
            http = msg.get("http")
            if type(http) is int and 100 <= http <= 599:
                detail["http"] = http
            self.fault = detail
            log_event(self.log, "fault", **detail)

    def drain(self, delay):
        for key, _ in self.sel.select(delay):
            try:
                data = os.read(key.fd, 65536)
            except BlockingIOError:
                continue
            except OSError as exc:
                if exc.errno != errno.EIO:  # PTY slave closed on Linux
                    raise
                data = b""
            if not data:
                self.sel.unregister(key.fd)
                os.close(key.fd)
                self.ptys.pop(key.data, None)
            elif key.data == "control":
                self.control.extend(data)
                lines = self.control.split(b"\n")
                self.control = lines.pop()
                for line in lines:
                    self.control_message(line)
            else:
                # Do not log terminal output. Keep only the initial CLI frame
                # to recognize OMP's explicit model-resolution error on exit.
                buf = self.startup_output[key.data]
                buf.extend(data[: 8192 - len(buf)])

    def exit_fact(self, role):
        code = self.procs[role].returncode
        model = self.models[role]
        detail = {"role": role, "model": model, "code": code}
        if code == 78:
            return "provider_fault", detail | {"cause": "model_mismatch"}
        if (
            code != 0
            and f'Model "{model}" not found.'.encode() in self.startup_output[role]
        ):
            return "startup_failure", detail | {
                "step": "resolve_model",
                "cause": "model_not_found",
            }
        return "process_exit", detail

    def monitor(self):
        grace = self.policy["grace"]
        report_until = review_until = subject_exit = None
        while True:
            self.drain(0)
            self.evidence.scan()
            now = monotonic()
            coord = self.procs["coordinator"].poll()
            subject = self.procs["subject"].poll()
            if self.interrupt:
                return "interrupted", {"signal": self.interrupt}
            if self.fault:
                # If discovery failed because a process died first, preserve
                # the actual process failure rather than claiming invisibility.
                cause = self.fault["cause"]
                if cause != "discovery_timeout" or (subject is None and coord is None):
                    return (
                        "discovery_timeout"
                        if cause == "discovery_timeout"
                        else "provider_fault"
                    ), self.fault
            if now >= self.until:
                return "run_timeout", {}
            if self.evidence.report and report_until is None:
                report_until = now + grace
            if coord is not None:
                if subject_exit:
                    return subject_exit
                if self.evidence.report and coord == 0:
                    return "reported", {}
                return self.exit_fact("coordinator")
            if subject is not None and subject_exit is None:
                subject_exit = self.exit_fact("subject")
                fd = self.ptys.get("coordinator")
                if (
                    subject_exit[0] != "process_exit"
                    or report_until
                    or fd is None
                    or not self.evidence.path
                ):
                    return subject_exit
                # One bounded opportunity to identify *already delivered* work.
                try:
                    os.write(fd, FINAL_CHECK)
                except OSError:
                    return subject_exit
                review_until = now + grace
                log_event(self.log, "final_check", **subject_exit[1])
            if review_until and (now >= review_until or self.evidence.report):
                return subject_exit
            if report_until and now >= report_until:
                return "exit_grace_timeout", {}
            beat_until = self.last_beat + self.policy["heartbeat"]
            if not report_until and now >= beat_until:
                return subject_exit or (
                    "heartbeat_timeout",
                    {"role": "coordinator", "model": self.models["coordinator"]},
                )
            wake = min(
                t
                for t in (
                    self.until,
                    review_until,
                    report_until,
                    None if report_until else beat_until,
                )
                if t is not None
            )
            self.drain(min(0.1, max(0, wake - monotonic())))

    def reap(self):
        """Capture actual role statuses and reap adopted descendants, without blocking."""
        while True:
            try:
                pid, status = os.waitpid(-1, os.WNOHANG)
            except ChildProcessError:
                return True
            if not pid:
                return False
            for proc in self.procs.values():
                if proc.pid == pid:
                    proc.returncode = os.waitstatus_to_exitcode(status)

    def cleanup(self):
        for sig, seconds in ((signal.SIGTERM, 2), (signal.SIGKILL, 3)):
            deadline = monotonic() + seconds
            signaled = set()
            while not self.reap():
                # Each pid is our own direct (possibly adopted) child. Only this
                # thread reaps it, so its numeric pid cannot be reused mid-pass.
                for pid in map(int, self.children_file.read_text().split()):
                    if pid in signaled:
                        continue
                    try:
                        if any(
                            p.pid == pid and p.returncode is None
                            for p in self.procs.values()
                        ):
                            os.killpg(pid, sig)
                        else:
                            os.kill(pid, sig)
                        signaled.add(pid)
                    except ProcessLookupError:
                        pass
                if monotonic() >= deadline:
                    break
                self.drain(0.05)
            else:
                return True
        return self.reap()

    def finish(self, reason, detail):
        alive = {r: r in self.procs and self.procs[r].poll() is None for r in ROLES}
        clean = False
        try:
            clean = self.cleanup()
        finally:
            # Read control frames queued immediately before exit (including the
            # identity frame), then re-open the native file after writers stop.
            drain_until = monotonic() + 0.5
            while monotonic() < drain_until and self.sel.select(0):
                self.drain(0)
            for key in list(self.sel.get_map().values()):
                os.close(key.fd)
            self.sel.close()
            intact = self.evidence.scan(final=True)
            scene, scene_reason = self.evidence.report or (None, None)
            if (
                scene
                and reason == "process_exit"
                and detail["role"] == "coordinator"
                and detail["code"] == 0
            ):
                # The last result can reach disk between the live scan and waitpid.
                reason, detail = "reported", {}
            exits = {
                r: self.procs[r].returncode if r in self.procs else None for r in ROLES
            }
            log_event(
                self.log,
                "terminal",
                scene=scene,
                sceneReason=scene_reason,
                reason=reason,
                detail=detail,
                aliveAtStop=alive,
                exits=exits,
                cleanup="complete" if clean else "incomplete",
                evidence="complete" if clean and intact else "incomplete",
            )


def main():
    os.umask(0o077)
    run = Path(sys.argv[1]).resolve(strict=True)
    os.chdir(run / "workspace")
    children_file = own_descendants()
    children_file.read_text()  # Fail before acceptance if isolated cleanup is unavailable.
    payload = json.load(sys.stdin)
    with (
        open(os.devnull, "r+b", buffering=0) as detached,
        (run / "run.log").open("x", encoding="utf-8") as log,
    ):
        os.dup2(detached.fileno(), 0)  # Immediately release the anonymous secret pipe.
        worker = Supervisor(run, payload, log, children_file)
        for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):
            signal.signal(sig, worker.on_signal)
        worker.until = monotonic() + payload["policy"]["total"]
        log_event(
            log,
            "submitted",
            pid=os.getpid(),
            **{k: payload[k] for k in ("source", "commit", "branch", "drv")},
        )
        emit(sys.stdout, runId=run.name, status="submitted")
        os.dup2(detached.fileno(), 1)
        os.dup2(detached.fileno(), 2)
        reason, detail = "supervision_failure", {"step": "monitor"}
        try:
            stop = worker.launch(payload.pop("roles"))
            reason, detail = stop if stop is not None else worker.monitor()
        except Exception as exc:
            # Do not serialize a command, environment, or raw OMP output.
            detail["cause"] = type(exc).__name__
            raise
        finally:
            worker.finish(reason, detail)


if __name__ == "__main__":
    main()
