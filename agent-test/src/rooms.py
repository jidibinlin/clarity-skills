"""Discover view-only links via the run's own OMP 19 collab CLI."""

import json
import os
import stat
import subprocess
from pathlib import Path
from queue import Empty, SimpleQueue
from threading import Thread
from time import monotonic


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

    def _cli(self, main, *args):
        # Never discover omp on the watcher's PATH or inherit its HOME, OMP_*,
        # XDG_*, provider keys, etc. `collab` is a CLI query, not a new session.
        proc = subprocess.run(
            [main["cli"], "collab", *args, "--json"], cwd=self.run / "home",
            env={"HOME": str(self.run / "home"), "PATH": main["path"], "TMPDIR": str(self.run),
                 "LANG": "C.UTF-8", "PI_SKIP_VERSION_CHECK": "1"},
            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            timeout=4, check=False,
        )
        if proc.returncode == 0:
            result = json.loads(proc.stdout)
            if isinstance(result, dict) and result.get("version") == 1:
                return result
        return {}

    def _link(self, main):
        hosts = self._cli(main, "list").get("hosts")
        if not isinstance(hosts, list):
            return None
        matches = [h for h in hosts if isinstance(h, dict) and h.get("pid") == main["pid"]]
        if len(matches) != 1:
            return None
        host = matches[0]
        if (host.get("sessionId") != main["sessionId"] or host.get("cwd") != str(self.run / "workspace")
                or host.get("access") != "view" or host.get("relayConnected") is not True
                or not isinstance(host.get("instanceId"), str) or not host["instanceId"]
                or type(host.get("generation")) is not int or host["generation"] < 1):
            return None
        # The official command re-lists internally. Discard a room that rotated
        # between commands even if it belongs to the very same live OMP PID.
        link = self._cli(main, "link", str(main["pid"]), "--view")
        if (link.get("access") == "view" and link.get("instanceId") == host["instanceId"]
                and link.get("generation") == host["generation"] and isinstance(link.get("url"), str)
                and link["url"].startswith(("https://", "http://"))):
            return link["url"]
        return None

    def _lookup(self, main, result):
        try:
            url = self._link(main)
        except (OSError, ValueError, RecursionError, subprocess.SubprocessError):
            url = None
        result.put(url)

    def ready(self, wanted: set[str]) -> dict[str, str]:
        # Each role has at most one bounded lookup. Neither an unresponsive
        # registry nor a delayed subject blocks the other role or terminal.
        ready = {}
        for role in wanted & {"subject", "coordinator"}:
            if role in self.pending:
                try:
                    url = self.pending[role].get_nowait()
                except Empty:
                    continue
                del self.pending[role]
                if url:
                    ready[role] = url
                    continue
                self.retry_at[role] = monotonic() + 0.5
            if monotonic() < self.retry_at.get(role, 0):
                continue
            if (main := self._main(role)) is not None:
                result = SimpleQueue()
                self.pending[role] = result
                # Short-lived watcher-owned work; must never hold open a watch
                # that already found terminal, or become a supervisor input.
                Thread(target=self._lookup, args=(main, result), daemon=True).start()
        return ready
