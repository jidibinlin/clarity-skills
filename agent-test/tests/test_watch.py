"""Read-only watch consumers, using actual on-disk supervisor log records."""

import json
import os
import select
import subprocess
import sys
import tempfile
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
    unittest.main()
