"""Follow one accepted run. Only the supervisor writes the outcome."""

import json
import os
import select
import signal
import sys
import uuid
from contextlib import ExitStack
from pathlib import Path

from rooms import ViewRooms


ROLES = {"subject", "coordinator"}


class ObservationError(Exception):
    """Safe diagnostic: never include the contents of logs or room records."""


def _emit(record):
    print(json.dumps(record, ensure_ascii=False, separators=(",", ":")), flush=True)


def _record(log):
    start = log.tell()
    line = log.readline()
    if not line.endswith(b"\n"):
        if line:
            log.seek(start)  # The writer may still be appending this record.
        return None
    try:
        record = json.loads(line)
    except (ValueError, UnicodeError):
        raise ObservationError("invalid record in run.log") from None
    if not isinstance(record, dict):
        raise ObservationError("invalid record in run.log")
    return record


def _terminal(log):
    while (record := _record(log)) is not None:
        if record.get("event") == "terminal":
            return record
    return None


def _final_read(log):
    # The writer could have committed its final line after our last read and
    # before we noticed its exit. Once it is gone, this read is conclusive.
    terminal = _terminal(log)
    if terminal is None:
        raise ObservationError("accepted supervisor is gone without a terminal record")
    return terminal


def _owns_log(pid, log):
    # submitted.pid alone does not identify a process on a later attachment.
    # The accepted worker keeps its exclusive run.log open for writing until
    # it has flushed terminal. An unrelated reader is not that worker.
    expected = os.fstat(log.fileno())
    proc = Path("/proc") / str(pid)
    try:
        for descriptor in (proc / "fd").iterdir():
            try:
                if os.path.samestat(descriptor.stat(), expected):
                    with (proc / "fdinfo" / descriptor.name).open() as info:
                        for line in info:
                            if line.startswith("flags:"):
                                if int(line.split()[1], 8) & os.O_ACCMODE:
                                    return True
                                break
            except (FileNotFoundError, ProcessLookupError):
                continue  # An unrelated descriptor can close during enumeration.
    except (FileNotFoundError, ProcessLookupError):
        pass
    return False


def _follow(run, log, pid, latest):
    try:
        pidfd = os.pidfd_open(pid)
    except ProcessLookupError:
        return _final_read(log)
    with ExitStack() as resources:
        resources.callback(os.close, pidfd)
        # Pin the PID before identifying its log. pidfd becomes readable on
        # exit (including zombies), and cannot be retargeted through PID reuse.
        exited = select.poll()
        exited.register(pidfd, select.POLLIN)
        if exited.poll(0):
            return _final_read(log)
        try:
            owns_log = _owns_log(pid, log)
        except PermissionError:
            # procfs may deny access once exit has started. Its terminal, if
            # any, was flushed before kernel teardown of the worker's files.
            terminal = _terminal(log)
            if terminal is not None:
                return terminal
            if exited.poll(0):
                return _final_read(log)
            raise
        if not owns_log or exited.poll(0):
            return _final_read(log)
        stopping = False

        def disconnect(signum, frame):
            # Unwind at the next poll, not midway through starting or closing
            # a lookup. The supervisor is independent of this command.
            nonlocal stopping
            stopping = True

        for sig in (signal.SIGTERM, signal.SIGHUP, signal.SIGINT):
            previous = signal.signal(sig, disconnect)
            resources.callback(signal.signal, sig, previous)
        rooms = ViewRooms(run)
        resources.callback(rooms.close)
        first_poll = True
        while not stopping:
            views = rooms.ready(ROLES)
            terminal = _terminal(log)
            if terminal is not None:
                return terminal
            if exited.poll(0):
                return _final_read(log)
            for role, url in views.items():
                if role in ROLES and url != latest.get(role):
                    _emit({"event": "view", "runId": run.name, "role": role, "url": url})
                    latest[role] = url
            if first_poll:
                pending = ROLES.difference(latest)
                if pending:
                    print("run: watch: no view available yet for " + ", ".join(sorted(pending)),
                          file=sys.stderr, flush=True)
                first_poll = False
            if exited.poll(250):
                return _final_read(log)
        raise KeyboardInterrupt


def watch(run_id: str) -> int:
    try:
        try:
            canonical = str(uuid.UUID(run_id))
        except ValueError:
            canonical = None
        if canonical != run_id:
            raise ObservationError("runId must be a canonical UUID")
        run = Path.cwd() / "runs" / run_id
        latest = {}
        with (run / "run.log").open("rb") as log:
            accepted = _record(log)
            if accepted is None or accepted.get("event") != "submitted":
                raise ObservationError("no accepted submission in run.log")
            terminal = _terminal(log)
            if terminal is None:
                pid = accepted.get("pid")
                if type(pid) is not int or not 0 < pid < 2**31:
                    raise ObservationError("invalid supervisor PID in run.log")
                terminal = _follow(run, log, pid, latest)
        _emit(terminal | {"runId": run_id, "runDir": str(run),
                          "unavailableViews": sorted(ROLES.difference(latest))})
        return 0
    except BrokenPipeError:
        # The consumer went away. Suppress interpreter shutdown's second flush.
        with open(os.devnull, "wb") as sink:
            os.dup2(sink.fileno(), sys.stdout.fileno())
        return 1
    except KeyboardInterrupt:
        return 130
    except (ObservationError, OSError) as error:
        detail = error.strerror if isinstance(error, OSError) else str(error)
        print(f"run: watch failed: {detail}", file=sys.stderr)
        return 1
