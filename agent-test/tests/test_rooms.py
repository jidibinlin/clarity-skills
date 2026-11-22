"""Exercise OMP's real host registry and public collab CLI, without a public relay."""

import base64
import hashlib
import json
import select
import subprocess
import threading
import unittest
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import test_run  # Reuse the real package, PTY, Git, Nix and local-provider fixture.


@contextmanager
def host_relay():
    # No guest joins these tests: OMP publishes its room after the host WebSocket
    # upgrades. Hold it open; do not receive or record conversation data.
    stop = threading.Event()
    hosts = []

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def do_GET(self):
            if not self.path.startswith("/r/") or "role=host" not in self.path:
                self.send_error(404)
                return
            key = self.headers["Sec-WebSocket-Key"] + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
            self.send_response(101)
            self.send_header("Upgrade", "websocket")
            self.send_header("Connection", "Upgrade")
            self.send_header("Sec-WebSocket-Accept", base64.b64encode(hashlib.sha1(key.encode()).digest()).decode())
            self.end_headers()
            hosts.append(True)
            stop.wait()
            self.close_connection = True

        def log_message(self, *args):
            pass

    with ThreadingHTTPServer(("127.0.0.1", 0), Handler) as server:
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            yield server.server_port, hosts
        finally:
            stop.set()
            server.shutdown()
            worker.join()


class NativeRoomsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_run.RunTests.setUpClass()

    def setUp(self):
        self.h = test_run.RunTests()
        self.addCleanup(self.h.doCleanups)
        self.h.setUp()
        self.port, self.hosts = self.h.stack.enter_context(host_relay())

    def project(self, case, **options):
        self.h.version(case, **options)
        for role in ("subject", "coordinator"):
            file = self.h.repo / f"roles/{role}/config.yml"
            config = json.loads(file.read_bytes())
            config["collab"] = {
                "relayUrl": f"ws://127.0.0.1:{self.port}",
                "webUrl": f"http://127.0.0.1:{self.port}/{role}",
            }
            if role == "subject":
                config["collab"]["autoStart"] = "control"  # must never win
            file.write_text(json.dumps(config))
        self.h.git("commit", "-qam", "select offline collaboration relay")

    def test_default_discovers_only_view_rooms_attributed_to_native_main_roles(self):
        self.project("owner_hang", delay_subject=True)
        self.h.timers(heartbeat=30, total=80, discovery=60)
        volume = self.h.root / "artifact-volume"
        volume.mkdir()
        (self.h.launch / "runs").symlink_to(volume, target_is_directory=True)
        run = self.h.submit(observe=True)
        found = {}
        with subprocess.Popen(
            [self.h.exe, "--watch", run.name], cwd=self.h.launch, env=self.h.env,
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=0,
        ) as watcher:
            try:
                for role in ("coordinator", "subject"):
                    self.assertTrue(select.select([watcher.stdout], [], [], 25)[0], role)
                    line = watcher.stdout.readline()
                    self.assertTrue(line, f"watch ended before {role}'s link")
                    event = json.loads(line)
                    self.assertEqual((event["event"], event["role"], event["runId"]),
                                     ("view", role, run.name))
                    url = event["url"]
                    self.assertTrue(url.startswith(f"http://127.0.0.1:{self.port}/{role}/#"), role)
                    found[role] = url
                    if role == "coordinator":
                        (self.h.root / "release-subject").touch()
            finally:
                watcher.terminate()
                watcher.wait(timeout=5)
        self.assertTrue(all(url not in (run / 'run.log').read_text() for url in found.values()))
        cli = subprocess.run(
            [self.h.omp, "collab", "list", "--json"], capture_output=True, check=True,
            env={"HOME": str(run / "home"), "PATH": str(self.h.omp.parent)}, timeout=5,
        )
        published = json.loads(cli.stdout)["hosts"]
        self.assertEqual([host["access"] for host in published], ["view", "view"])

    def test_opt_out_prevents_native_auto_host_even_when_project_requests_control(self):
        self.project("normal")
        run = self.h.submit()  # the standard offline fixture always passes --no-observe
        self.assertEqual(self.h.terminal(run)["scene"], "completed")
        self.assertFalse(self.hosts)


if __name__ == "__main__":
    unittest.main()
