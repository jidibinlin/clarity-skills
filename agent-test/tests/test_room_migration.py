"""Follow an actual OMP write-conflict continuation, not an arbitrary session switch."""

import json
import select
import subprocess
import unittest

import test_rooms
import test_run


class MigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_run.RunTests.setUpClass()

    def test_subject_view_follows_its_replaced_journal(self):
        fixture = test_rooms.NativeRoomsTests()
        self.addCleanup(fixture.doCleanups)
        fixture.setUp()
        h = fixture.h
        fixture.project("owner_hang")
        h.timers(heartbeat=60, total=90, discovery=60)
        # OMP's append fast path does not check file size. Its full rewrite
        # does: drive that real storage operation after replacing the file.
        h.put("scene/.omp/config.yml", 'extensions: ["./trigger-migration.ts"]\n')
        h.put("scene/trigger-migration.ts", '''
import { existsSync } from "node:fs";
export default function(pi) {
  pi.on("session_start", (_, ctx) => {
    if (ctx.agent.kind !== "main" || process.env.AGENT_TEST_ROLE !== "subject") return;
    const timer = ctx.setInterval(async () => {
      if (!existsSync("trigger-migration")) return;
      ctx.clearTimer(timer);
      await ctx.sessionManager.rewriteEntries();
    }, 100);
  });
}
''')
        h.git("add", "scene")
        h.git("commit", "-qm", "trigger one subject journal write")
        run = h.submit(observe=True)
        first = None
        with subprocess.Popen([h.exe, "--watch", run.name], cwd=h.launch, env=h.env,
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=0) as watch:
            try:
                while True:
                    self.assertTrue(select.select([watch.stdout], [], [], 25)[0],
                                    "missing replacement subject room" if first else "missing initial subject room")
                    line = watch.stdout.readline()
                    self.assertTrue(line, "watch ended without publishing the continuation")
                    event = json.loads(line)
                    self.assertEqual(event["event"], "view")
                    if event["role"] != "subject":
                        continue
                    if first is not None:
                        self.assertTrue(event["url"] != first, "old subject room replayed")
                        break
                    first = event["url"]
                    original, = h.sessions(run, "subject")
                    header = next(r for r in test_run.json_lines(original) if r.get("type") == "session")
                    original.write_text('{"type":"session","id":"different-session"}\n')
                    (run / "workspace/trigger-migration").touch()
            finally:
                watch.terminate()
                watch.wait(timeout=5)
        self.assertTrue(any(r.get("type") == "session" and r.get("continuationOf") == header["id"]
                            for file in h.sessions(run, "subject") for r in test_run.json_lines(file)))


if __name__ == "__main__":
    unittest.main()
