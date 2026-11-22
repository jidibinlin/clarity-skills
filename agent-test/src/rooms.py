"""Discover view-only links via the run's own OMP 19 collab CLI."""

import json
import os
import signal
import stat
import subprocess
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from time import monotonic


@contextmanager
def _defer_cancellation():
    # Never interrupt a spawn before we own the process, or interrupt teardown
    # after removing it from pending. The commands are killed with SIGKILL.
    old = signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGINT, signal.SIGTERM, signal.SIGHUP})
    try:
        yield
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, old)


@dataclass
class _Query:
    proc: subprocess.Popen
    output: int
    deadline: float
    main: dict
    host: dict | None

    def close(self):
        # poll()/wait() would reap the leader and allow its PID to be reused.
        # Leave it waitable until its dedicated group (including wrappers'
        # children) has been signalled. Never touch either OMP session group.
        try:
            os.killpg(self.proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        finally:
            os.close(self.output)
        try:
            self.proc.wait(timeout=0.5)
        except subprocess.TimeoutExpired:
            pass  # SIGKILL is already pending, including for a stuck syscall.

    def receive(self, now):
        state = os.waitid(os.P_PID, self.proc.pid, os.WEXITED | os.WNOHANG | os.WNOWAIT)
        if not state:
            return None if now < self.deadline else {}
        if state.si_code == os.CLD_EXITED and state.si_status == 0:
            try:
                value = json.loads(os.pread(self.output, 1024 * 1024, 0))
                if isinstance(value, dict) and value.get("version") == 1:
                    return value
            except (OSError, ValueError, RecursionError):
                pass
        return {}


class ViewRooms:
    def __init__(self, run: Path):
        self.run = run
        self.pending = {}
        self.retry_at = {}

    def _main(self, role):
        # The startup extension writes once (0600) from the main process,
        # not the launcher's PTY wrapper or a delegated OMP helper.
        try:
            fd = os.open(self.run / f"{role}-view.json", os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
            with os.fdopen(fd, "rb") as stream:
                info = os.fstat(fd)
                if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077:
                    return None
                main = json.loads(stream.read(256 * 1024))
            if (isinstance(main, dict) and type(main.get("pid")) is int and main["pid"] > 0
                    and isinstance(main.get("sessionId"), str) and main["sessionId"]
                    and isinstance(main.get("cli"), str) and os.path.isabs(main["cli"])
                    and isinstance(main.get("path"), str)):
                return main
        except (OSError, ValueError, RecursionError):
            pass  # Includes startup races; don't remember an unavailable identity.
        return None

    def _start(self, role, main, host=None):
        args = ["list"] if host is None else ["link", str(main["pid"]), "--view"]
        # A private memory file avoids both pipe backpressure while the watcher
        # sleeps and writing the CLI's bearer URL to a named file or common log.
        fd = os.memfd_create("omp-collab")
        try:
            proc = subprocess.Popen(
                [main["cli"], "collab", *args, "--json"], cwd=self.run / "home",
                env={"HOME": str(self.run / "home"), "PATH": main["path"], "TMPDIR": str(self.run),
                     "LANG": "C.UTF-8", "PI_SKIP_VERSION_CHECK": "1"},
                stdin=subprocess.DEVNULL, stdout=fd, stderr=subprocess.DEVNULL, start_new_session=True,
            )
        except BaseException:
            os.close(fd)
            raise
        self.pending[role] = _Query(proc, fd, monotonic() + 4, main, host)

    @staticmethod
    def _match(main, hosts):
        if not isinstance(hosts, list):
            return None
        matches = [h for h in hosts if isinstance(h, dict) and h.get("pid") == main["pid"]]
        if len(matches) != 1:
            return None
        host = matches[0]
        if (host.get("sessionId") != main["sessionId"]
                or host.get("access") != "view" or host.get("relayConnected") is not True
                or not isinstance(host.get("instanceId"), str) or not host["instanceId"]
                or type(host.get("generation")) is not int or host["generation"] < 1):
            return None
        return host

    def _advance(self, role, now):
        query = self.pending.get(role)
        if query is None:
            if now >= self.retry_at.get(role, 0):
                self.retry_at[role] = now + 0.5
                if (main := self._main(role)) is not None:
                    self._start(role, main)
            return None

        result = query.receive(now)
        if result is None:
            return None  # still running; never block the other role or terminal
        del self.pending[role]
        query.close()
        self.retry_at[role] = now + 0.5
        if query.host is None:
            host = self._match(query.main, result.get("hosts"))
            if host is not None:
                self._start(role, query.main, host)
        # The official link command re-lists internally. A rotated generation
        # must be re-identified before any of its new capabilities are returned.
        elif (result.get("access") == "view" and result.get("instanceId") == query.host["instanceId"]
              and result.get("generation") == query.host["generation"] and isinstance(result.get("url"), str)
              and result["url"].startswith(("https://", "http://"))):
            self.retry_at[role] = now + 5
            return result["url"]
        return None

    def ready(self, wanted: set[str]) -> dict[str, str]:
        now = monotonic()
        ready = {}
        with _defer_cancellation():
            for role in wanted & {"subject", "coordinator"}:
                try:
                    if url := self._advance(role, now):
                        ready[role] = url
                except (OSError, ValueError, subprocess.SubprocessError):
                    self.retry_at[role] = now + 0.5
        return ready

    def close(self):
        with _defer_cancellation():
            while self.pending:
                _, query = self.pending.popitem()
                query.close()
