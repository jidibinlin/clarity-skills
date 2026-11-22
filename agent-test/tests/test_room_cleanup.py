"""A watch cancellation must reclaim just its own in-flight CLI process group."""

import json
import os
import select
import signal
import sys
import tempfile
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from rooms import ViewRooms


class RoomCleanupTests(unittest.TestCase):
    def test_close_reclaims_hung_cli_and_its_child(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp)
            (run / "home").mkdir()
            cli = run / "hung-omp"
            cli.write_text(f"#!{sys.executable}\n" + '''
import os, signal, subprocess, sys
from pathlib import Path
child = subprocess.Popen([sys.executable, '-c', 'import signal; signal.pause()'])
Path('started').write_text(f'{os.getpid()} {child.pid}')
signal.pause()
''')
            cli.chmod(0o700)
            identity = run / "subject-view.json"
            identity.write_text(json.dumps({"cli": str(cli), "path": os.defpath,
                                            "pid": os.getpid(), "sessionId": "main"}))
            identity.chmod(0o600)
            rooms = ViewRooms(run)
            marker = run / "home/started"
            deadline = time.monotonic() + 3
            try:
                rooms.ready({"subject"})
                while time.monotonic() < deadline and not (marker.exists() and marker.stat().st_size):
                    time.sleep(0.01)
                self.assertTrue(marker.exists(), "test CLI did not start")
                leader, child = map(int, marker.read_text().split())
                fds = [os.pidfd_open(leader), os.pidfd_open(child)]
                try:
                    rooms.close()
                    for fd in fds:
                        self.assertTrue(select.select([fd], [], [], 2)[0], "lookup survived watcher close")
                finally:
                    for fd in fds:
                        # Do not leak our fixture processes on a failed assertion.
                        try:
                            signal.pidfd_send_signal(fd, signal.SIGKILL)
                        except ProcessLookupError:
                            pass
                        os.close(fd)
            finally:
                rooms.close()


if __name__ == "__main__":
    unittest.main()
