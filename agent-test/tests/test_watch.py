"""Read-only watch consumers, using actual on-disk supervisor log records."""

import fcntl
import json
import os
import select
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path


RUN_ID = "c104ee8e-d93e-493e-83c1-e588039bf694"
SUBMITTED = {
    "event": "submitted", "source": "/project", "commit": "d" * 40,
    "branch": None, "drv": "/nix/store/example.drv",
}
TERMINAL = {
    "event": "terminal", "scene": "scenario_error", "sceneReason": "no supplies",
    "reason": "exit_grace_timeout", "detail": {},
    "aliveAtStop": {"subject": True, "coordinator": True},
    "exits": {"subject": -15, "coordinator": -15},
    "cleanup": "complete", "evidence": "complete",
}


def watch_fixture(mode, library):
    # The native provider owns rotation/timing, not the watcher. Drive just
    # that boundary deterministically while exercising the real log and PID.
    sys.path.insert(0, library)
    import watch
    from unittest.mock import patch

    if mode == "busy":
        class BusyRooms(watch.ViewRooms):
            # The subject is available immediately while the coordinator's
            # real query launcher is still waiting for the fixture command.
            def ready(self, wanted):
                return super().ready(wanted) | {"subject": "first"}

        with patch.object(watch, "ViewRooms", BusyRooms):
            return watch.watch(RUN_ID)

    class ScriptedRooms:
        def __init__(self, run):
            self.run = run
            self.lease = run / "active-lookup"
            self.lease.touch()
            self.urls = iter(["first", "first", None, "first", "replacement"])

        def ready(self, wanted):
            url = "first" if mode == "steady" else next(self.urls, "stale")
            if url == "stale":
                # Supervisor finishes while the lookup is returning a stale URL.
                with (self.run / "run.log").open("a") as log:
                    print(json.dumps(TERMINAL), file=log)
            return {"subject": url} if url and "subject" in wanted else {}

        def close(self):
            self.lease.unlink()

    with patch.object(watch, "ViewRooms", ScriptedRooms):
        return watch.watch(RUN_ID)


class WatchTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.run_dir = self.root / "runs" / RUN_ID
        (self.run_dir / "workspace").mkdir(parents=True)
        self.log = self.run_dir / "run.log"
        exe = os.environ.get("AGENT_TEST_BIN")
        self.command = [exe] if exe else [
            sys.executable, "-B", str(Path(__file__).resolve().parents[1] / "src/submit.py")
        ]

    def watch(self, run_id=RUN_ID):
        return subprocess.run([*self.command, "--watch", run_id], cwd=self.root,
                              timeout=5, capture_output=True, text=True)

    def expect_terminal(self, stdout):
        self.assertEqual([json.loads(line) for line in stdout.splitlines()], [{
            **TERMINAL, "runId": RUN_ID, "runDir": str(self.run_dir),
            "unavailableViews": ["coordinator", "subject"],
        }])

    def test_reattaching_after_exit_replays_only_the_durable_terminal(self):
        self.log.write_text(json.dumps(SUBMITTED | {"pid": 2147483647}) + "\n" +
                            json.dumps(TERMINAL) + "\n")
        result = self.watch()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.expect_terminal(result.stdout)

    def test_partial_terminal_waits_for_commit_even_when_rooms_are_unavailable(self):
        # This writer stands in for the accepted supervisor. It retains its open
        # run.log exactly as supervise does; no actual model or native daemon.
        with self.log.open("w", buffering=1) as log:
            print(json.dumps(SUBMITTED | {"pid": os.getpid()}), file=log)
            encoded = json.dumps(TERMINAL)
            log.write(encoded[:20])
            log.flush()
            proc = subprocess.Popen([*self.command, "--watch", RUN_ID], cwd=self.root,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                ready, _, _ = select.select([proc.stderr], [], [], 5)
                self.assertTrue(ready, "watch did not announce missing live rooms")
                pending = proc.stderr.readline().decode()
                for role in ("coordinator", "subject"):
                    self.assertIn(role, pending)
                self.assertIsNone(proc.poll())
                print(encoded[20:], file=log)
                stdout, stderr = proc.communicate(timeout=5)
                self.assertEqual(proc.returncode, 0, stderr)
                self.expect_terminal(stdout.decode())
            finally:
                proc.kill()
                proc.communicate()

    def test_recycled_pid_is_not_the_supervisor_even_if_it_reads_this_log(self):
        self.log.write_text(json.dumps(SUBMITTED | {"pid": os.getpid()}) + "\n")
        with self.log.open():
            result = self.watch()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("supervisor", result.stderr.lower())
        self.assertIn("terminal", result.stderr.lower())

    def test_zombie_supervisor_without_terminal_is_an_observation_error(self):
        with subprocess.Popen([sys.executable, "-c", "pass"]) as child:
            os.waitid(os.P_PID, child.pid, os.WEXITED | os.WNOWAIT)
            self.log.write_text(json.dumps(SUBMITTED | {"pid": child.pid}) + "\n")
            result = self.watch()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("supervisor", result.stderr.lower())
        self.assertIn("terminal", result.stderr.lower())

    def fixture_command(self, mode):
        exe = os.environ.get("AGENT_TEST_BIN")
        library = Path(exe).resolve().parent if exe else Path(__file__).resolve().parents[1] / "src"
        return [sys.executable, "-B", str(Path(__file__).resolve()), "--fixture", mode, str(library)]

    def test_changed_view_replaces_only_that_roles_link_before_terminal(self):
        with self.log.open("w", buffering=1) as log:
            print(json.dumps(SUBMITTED | {"pid": os.getpid()}), file=log)
            result = subprocess.run(self.fixture_command("rotate"), cwd=self.root,
                                    timeout=5, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([json.loads(line) for line in result.stdout.splitlines()], [
            {"event": "view", "role": "subject", "runId": RUN_ID, "url": "first"},
            {"event": "view", "role": "subject", "runId": RUN_ID, "url": "replacement"},
            TERMINAL | {"runDir": str(self.run_dir), "runId": RUN_ID,
                        "unavailableViews": ["coordinator"]},
        ])
        self.assertFalse((self.run_dir / "active-lookup").exists())

    def test_disconnect_signals_release_room_lookup_without_a_terminal(self):
        for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):
            with self.subTest(sig=sig), self.log.open("w", buffering=1) as log:
                submitted = json.dumps(SUBMITTED | {"pid": os.getpid()})
                print(submitted, file=log)
                proc = subprocess.Popen(self.fixture_command("steady"), cwd=self.root,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    ready, _, _ = select.select([proc.stdout], [], [], 5)
                    self.assertTrue(ready, "watch did not announce the live room")
                    self.assertEqual(json.loads(proc.stdout.readline())["url"], "first")
                    proc.send_signal(sig)
                    stdout, _ = proc.communicate(timeout=5)
                    self.assertEqual(stdout, b"")
                    self.assertFalse((self.run_dir / "active-lookup").exists())
                    self.assertEqual(self.log.read_text(), submitted + "\n")
                finally:
                    proc.kill()
                    proc.communicate()

    def test_termination_while_output_is_full_reaps_inflight_lookup(self):
        (self.run_dir / "home").mkdir()
        cli = self.run_dir / "cli"
        cli.write_text("#!/bin/sh\necho $$ > ../lookup.pid\nexec sleep 10\n")
        cli.chmod(0o700)
        binding = self.run_dir / "coordinator-view.json"
        binding.write_text(json.dumps({"pid": os.getpid(), "sessionId": "main",
                                       "cli": str(cli), "path": os.environ["PATH"]}))
        binding.chmod(0o600)
        lookup = self.run_dir / "lookup.pid"
        with self.log.open("w", buffering=1) as log:
            print(json.dumps(SUBMITTED | {"pid": os.getpid()}), file=log)
            for fd in (1, 2):
                with self.subTest(fd=fd):
                    lookup.unlink(missing_ok=True)
                    reader, writer = os.pipe()
                    try:
                        os.write(writer, b"x" * fcntl.fcntl(writer, fcntl.F_GETPIPE_SZ))
                        proc = subprocess.Popen(
                            self.fixture_command("busy"), cwd=self.root,
                            stdout=writer if fd == 1 else subprocess.DEVNULL,
                            stderr=writer if fd == 2 else subprocess.DEVNULL,
                        )
                        try:
                            # Observe the blocked write, rather than guessing a
                            # delay. Leave the full pipe open and never drain it.
                            deadline = time.monotonic() + 5
                            while time.monotonic() < deadline:
                                call = Path(f"/proc/{proc.pid}/syscall").read_text().split()
                                if lookup.exists() and call[1:2] == [hex(fd)]:
                                    break
                                time.sleep(0.01)
                            else:
                                self.fail("watch never blocked while a lookup was in flight")
                            lookup_pid = int(lookup.read_text())
                            proc.terminate()
                            proc.wait(timeout=2)
                            self.assertFalse(Path(f"/proc/{lookup_pid}").exists())
                        finally:
                            proc.kill()
                            proc.wait()
                    finally:
                        os.close(writer)
                        os.close(reader)

    def test_run_id_is_not_a_path_or_alternate_spelling(self):
        self.log.write_text(json.dumps(SUBMITTED | {"pid": os.getpid()}) + "\n" +
                            json.dumps(TERMINAL) + "\n")
        for alias in (str(self.run_dir), f"../runs/{RUN_ID}", RUN_ID.upper(),
                      RUN_ID.replace("-", "")):
            with self.subTest(alias=alias):
                result = self.watch(alias)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn("runid", result.stderr.lower())


if __name__ == "__main__":
    if sys.argv[1:2] == ["--fixture"]:
        sys.exit(watch_fixture(*sys.argv[2:]))
    unittest.main()
