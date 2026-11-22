"""End-to-end acceptance: real Git, Nix, PTYs and OMP; only the provider is local."""

import json
import os
import shutil
import signal
import subprocess
import tarfile
import tempfile
import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from contextlib import ExitStack
from pathlib import Path

from provider import Provider

PACKAGE = Path(__file__).resolve().parents[1]


def output(argv, **kwargs):
    result = subprocess.run(argv, text=True, capture_output=True, check=False, **kwargs)
    if result.returncode:
        raise RuntimeError(
            f"{argv[0]} failed ({result.returncode}): {result.stderr.strip()}"
        )
    return result.stdout.strip()


def json_lines(path):
    # A live writer may still be appending the last line.
    with path.open("rb") as stream:
        return [json.loads(line) for line in stream if line.endswith(b"\n")]


class RunTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.omp = Path(shutil.which("omp") or "").resolve(strict=True)
        if not cls.omp.is_file() or not cls.omp.is_relative_to("/nix/store"):
            raise RuntimeError("Integration tests require a Nix-installed omp on PATH")
        cls.pkgs = Path(output(["nix-instantiate", "--find-file", "nixpkgs"])).resolve()
        cls.system = json.loads(
            output(
                [
                    "nix-instantiate",
                    "--eval",
                    "--json",
                    "--expr",
                    "builtins.currentSystem",
                ]
            )
        )
        selected = os.environ.get("AGENT_TEST_BIN")
        if selected:
            cls.exe = str(Path(selected).resolve(strict=True))
        else:
            expr = f"let pkgs = import <nixpkgs> {{}}; in pkgs.callPackage (builtins.toPath {json.dumps(str(PACKAGE))}) {{}}"
            cls.exe = str(
                Path(output(["nix-build", "--no-out-link", "-E", expr])) / "bin/run"
            )

    def setUp(self):
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.root = Path(
            self.stack.enter_context(tempfile.TemporaryDirectory(prefix="agent-test-"))
        )
        self.a = self.stack.enter_context(Provider())
        self.b = self.stack.enter_context(Provider())
        self.home = self.root / "submit-home"
        self.repo = self.root / "test-project"
        self.launch = self.root / "submit-here"
        self.repo.mkdir()
        self.launch.mkdir()
        config = self.home / ".config/agent-test"
        config.mkdir(parents=True, mode=0o700)
        self.config = config
        credentials = config / "credentials.toml"
        credentials.write_text(
            f"[providers]\nalpha = {json.dumps(self.a.key)}\nbeta = {json.dumps(self.b.key)}\n"
        )
        credentials.chmod(0o600)
        self.env = {
            "HOME": str(self.home),
            "PATH": os.environ["PATH"],
            "NIX_PATH": f"nixpkgs={self.pkgs}",
            "NIX_CONFIG": "experimental-features = nix-command flakes",
            "LANG": "C.UTF-8",
            "TERM": "xterm-256color",
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
        }
        for key in (
            "USER",
            "LOGNAME",
            "NIX_REMOTE",
            "SSL_CERT_FILE",
            "NIX_SSL_CERT_FILE",
        ):
            if key in os.environ:
                self.env[key] = os.environ[key]
        self.timers()
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@invalid")
        self.put(
            "test.nix",
            '{ workspaceSource = "scene"; subject.ompConfigDir = "roles/subject"; coordinator = { ompConfigDir = "roles/coordinator"; prompt = "owner.md"; }; }\n',
        )
        self.put(
            "owner.md",
            "You are the user. Ask the subject to repair the lamp; continue through delivery. If required information is unavailable, explain why the scenario cannot proceed.\n",
        )
        self.put(
            "scene/.agents/skills/lamp/SKILL.md",
            "---\nname: lamp\ndescription: How to repair the sample lamp.\n---\nNotify the requester after the repair.\n",
        )
        self.put(".gitignore", "*.private\n")
        self.runs = []
        self.stack.callback(self.stop_leftovers)

    def timers(self, heartbeat=10, total=40, grace=2, poll=0.5):
        (self.config / "settings.toml").write_text(
            f"[timers]\ndiscovery=10\npoll={poll}\nheartbeat={heartbeat}\ntotal={total}\ngrace={grace}\n"
        )

    def git(self, *args):
        return output(["git", "-C", str(self.repo), *args], env=self.env)

    def put(self, name, text):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def version(
        self,
        case="normal",
        tag="v1",
        *,
        unavailable=None,
        thinking=False,
        workspace=True,
        delay_subject=False,
    ):
        # Use the OMP already installed in the Nix store, not host PATH or credentials.
        path = str(self.omp.parent)
        if delay_subject:
            self.put(
                "delay.sh",
                f"""if [ "$AGENT_TEST_ROLE" = subject ]; then
  until test -f "{self.root}/release-subject"; do sleep 0.1; done
  {self.omp} "$@"
  status=$?
  exit "$status"
fi
exec {self.omp} "$@"
""",
            )
            path = '${p.writeShellScriptBin "omp" (builtins.readFile ./delay.sh)}/bin'
        self.put(
            "flake.nix",
            f'''{{ inputs.nixpkgs.url = "path:{self.pkgs}";
          outputs = {{nixpkgs,...}}: let p=nixpkgs.legacyPackages.{self.system}; in {{
            devShells.{self.system}.default = p.mkShellNoCC {{
              LAMP_ENV_VERSION = "{tag}";
              shellHook = ''export PATH={path}:$PATH'';
            }}; }}; }}\n''',
        )
        self.put("scene/material.txt", tag + "\n")
        if not workspace:
            self.put(
                "test.nix",
                '{ subject.ompConfigDir="roles/subject"; coordinator.ompConfigDir="roles/coordinator"; coordinator.prompt="owner.md"; }',
            )
        for role, provider, endpoint, name in [
            ("coordinator", "alpha", self.a, "owner"),
            ("subject", "beta", self.b, "desk"),
        ]:
            model = f"{name}-{case}"
            cfg = {
                "modelRoles": {
                    "default": provider + "/" + model + (":low" if thinking else "")
                },
                "task": {"crossInstance": True},
                "startup": {"checkUpdate": False},
                "tools": {"approvalMode": "yolo"},
            }
            if case == "helper" and role == "subject":
                cfg["modelRoles"]["task"] = "alpha/helper"
            ids = ["other"] if role == unavailable else [model]

            def service(p, ep, models):
                return {
                    "api": "openai-completions",
                    "baseUrl": ep.url,
                    "apiKey": p.upper() + "_KEY",
                    "models": [{"id": x, "name": x} for x in models],
                }

            providers = {provider: service(provider, endpoint, ids)}
            if case == "helper" and role == "subject":
                providers["alpha"] = service("alpha", self.a, ["helper"])
            self.put(f"roles/{role}/config.yml", json.dumps(cfg))
            self.put(f"roles/{role}/models.yml", json.dumps({"providers": providers}))
        if case == "helper":
            # Project defaults may fill omitted roles, never replace explicit
            # role choices. The alternative model has a valid local credential.
            self.put(
                "scene/.omp/config.yml",
                json.dumps({"modelRoles": {"task": "beta/desk-helper"}}),
            )
        self.git("add", "--all")
        if not (self.repo / "flake.lock").exists():
            output(["nix", "flake", "lock", "--offline", str(self.repo)], env=self.env)
            self.git("add", "flake.lock")
        self.git("commit", "-qm", case + " " + tag)
        return self.git("rev-parse", "HEAD")

    def call(self, *args):
        return subprocess.run(
            [self.exe, str(self.repo), *args],
            env=self.env,
            cwd=self.launch,
            text=True,
            capture_output=True,
            check=False,
            timeout=90,
        )

    def submit(self, *args):
        r = self.call(*args)
        self.assertEqual(r.returncode, 0, (r.stdout, r.stderr))
        reply = json.loads(r.stdout)
        self.assertEqual(reply["status"], "submitted")
        run = self.launch / "runs" / reply["runId"]
        self.runs.append(run)
        self.assertTrue((run / "run.log").is_file())
        return run

    def terminal(self, run, timeout=55):
        cutoff = time.monotonic() + timeout
        while time.monotonic() < cutoff:
            records = json_lines(run / "run.log")
            ends = [r for r in records if r.get("event") == "terminal"]
            if ends:
                self.assertEqual(len(ends), 1)
                end = ends[0]
                self.assertEqual(end["cleanup"], "complete", end)
                return end
            time.sleep(0.1)
        self.fail(f"No terminal for {run.name}: {records}")

    def sessions(self, run, role):
        return list(
            (run / "home/.omp/profiles" / role / "agent/sessions").rglob("*.jsonl")
        )

    def assert_normal_teardown(self, run, end):
        self.assertEqual(end["reason"], "reported", end)
        self.assertEqual(end["exits"]["coordinator"], 0, end)
        self.assertIsInstance(end["exits"]["subject"], int)
        self.assertEqual(end["evidence"], "complete", end)
        self.assertTrue((run / "workspace").is_dir())
        for role in ("coordinator", "subject"):
            self.assertTrue(
                any(
                    entry.get("type") == "session" and not entry.get("parentSession")
                    for path in self.sessions(run, role)
                    for entry in json_lines(path)
                ),
                role,
            )

    def stop_leftovers(self):
        for run in self.runs:
            records = json_lines(run / "run.log")
            first = next((x for x in records if x.get("event") == "submitted"), {})
            if not any(x.get("event") == "terminal" for x in records) and first.get(
                "pid"
            ):
                try:
                    os.kill(first["pid"], signal.SIGTERM)
                except ProcessLookupError:
                    pass
                else:
                    deadline = time.monotonic() + 5
                    while time.monotonic() < deadline and not any(
                        x.get("event") == "terminal"
                        for x in json_lines(run / "run.log")
                    ):
                        time.sleep(0.1)

    def test_external_commit_selects_matching_environment_and_material(self):
        first = self.version(tag="v1")
        second = self.version(tag="v2")
        self.put("scene/material.txt", "uncommitted")
        self.put("scene/no.private", "local-only")
        a = self.submit("--branch", "main", "--commit", first)
        b = self.submit("--branch", "main")
        drv = []
        for run, tag, commit in [(a, "v1", first), (b, "v2", second)]:
            end = self.terminal(run)
            self.assertEqual(end["scene"], "completed", end)
            start = json_lines(run / "run.log")[0]
            self.assertEqual((start["branch"], start["commit"]), ("main", commit))
            drv.append(start["drv"])
            with tarfile.open(run / "start.tar.gz") as archive:
                names = {m.name.removeprefix("./"): m for m in archive.getmembers()}
                self.assertNotIn("no.private", names)
                self.assertEqual(
                    archive.extractfile(names["material.txt"]).read().decode().strip(),
                    tag,
                )
            self.assertEqual(
                (run / "workspace/environment.txt").read_text().strip(), tag
            )
            self.assertEqual(
                (run / "workspace/credential-scope.txt").read_text().split(), ["beta"]
            )
        self.assertNotEqual(*drv)
        self.assertTrue(all(x.endswith(".drv") for x in drv))
        self.assertEqual((self.repo / "scene/material.txt").read_text(), "uncommitted")

    def assert_no_credentials(self, run):
        secrets = [endpoint.key.encode() for endpoint in (self.a, self.b)]
        for path in run.rglob("*"):
            if path.is_file() and not path.is_symlink():
                data = path.read_bytes()
                self.assertFalse(any(key in data for key in secrets), path)

    def test_enclosing_project_does_not_supply_role_instructions_or_skills(self):
        outer = "host-only-instruction-a0cb"
        inner = "submitted-workspace-instruction-ca03"
        subject_skill = "subject-only-lamp-guide"
        outer_skill = "host-only-skill-b226"
        output(["git", "init", "-q", str(self.launch)], env=self.env)
        (self.launch / "AGENTS.md").write_text(outer)
        skill = self.launch / ".agents/skills" / outer_skill / "SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text(
            f"---\nname: {outer_skill}\ndescription: Host-only skill.\n---\nDo not load.\n"
        )
        self.put("scene/AGENTS.md", inner)
        self.put(
            f"roles/subject/skills/{subject_skill}/SKILL.md",
            f"---\nname: {subject_skill}\ndescription: A role-specific repair method.\n---\nCheck the filament.\n",
        )
        for endpoint in (self.a, self.b):
            endpoint.context_markers = {outer, outer_skill, inner, subject_skill}
        self.version()
        end = self.terminal(self.submit())
        self.assertEqual(end["scene"], "completed", end)
        for endpoint, expected in [(self.a, {inner}), (self.b, {inner, subject_skill})]:
            supplied = set().union(
                *(c["markers"] for c in endpoint.calls if c["kind"] == "agent")
            )
            self.assertEqual(supplied, expected)

    def test_simultaneous_submissions_of_same_commit_do_not_share_state(self):
        self.version()
        with ThreadPoolExecutor(max_workers=2) as pool:
            a, b = list(pool.map(lambda _: self.submit(), range(2)))
        self.assertNotEqual(a, b)
        artifacts = []
        transcripts = []
        for run in (a, b):
            end = self.terminal(run)
            self.assertEqual(end["scene"], "completed", end)
            files = list((run / "workspace").glob("repair-*.txt"))
            self.assertEqual(len(files), 1)
            artifacts.append(files[0].stem)
            records = [p.read_text() for p in self.sessions(run, "subject")]
            self.assertTrue(records)
            transcripts.append("".join(records))
            self.assert_no_credentials(run)
        self.assertNotEqual(*artifacts)
        final_materials = [(r / "workspace/material.txt").read_text() for r in (a, b)]
        self.assertCountEqual([len(x.splitlines()) for x in final_materials], [1, 2])
        for i in (0, 1):
            self.assertIn(artifacts[i], transcripts[i])
            self.assertNotIn(artifacts[1 - i], transcripts[i])
            self.assertFalse(
                ((a, b)[i] / "workspace" / (artifacts[1 - i] + ".txt")).exists()
            )
        self.assertEqual((self.repo / "scene/material.txt").read_text(), "v1\n")

    def test_missing_committed_material_does_not_read_dirty_copy(self):
        self.version()
        self.put(
            "test.nix",
            '{subject.ompConfigDir="roles/subject"; coordinator.ompConfigDir="roles/coordinator"; coordinator.prompt="local.md";}',
        )
        self.git("add", "test.nix")
        self.git("commit", "-qm", "missing")
        self.put("local.md", "local only")
        failed = self.call()
        self.assertNotEqual(failed.returncode, 0)
        self.assertIn("local.md", failed.stderr)
        self.assertNotIn("submitted", failed.stdout)

    def test_invalid_version_is_not_silently_replaced_by_head(self):
        tip = self.version()
        self.git("branch", "old", tip)
        newer = self.version(tag="newer")
        for args, diagnostic in [
            (("--commit", tip), "--commit requires --branch"),
            (("--branch", "no-such-branch"), "branch"),
            (("--branch", "old", "--commit", newer), "not on requested branch"),
        ]:
            with self.subTest(args=args):
                r = self.call(*args)
                self.assertNotEqual(r.returncode, 0)
                self.assertNotIn("submitted", r.stdout)
                self.assertIn(diagnostic, r.stderr)

    def test_material_generated_by_project_checkout_is_part_of_start(self):
        commit = self.version()
        hook = self.repo / ".git/hooks/post-checkout"
        hook.write_text('#!/bin/sh\nprintf "%s\\n" "$2" > scene/generated.private\n')
        hook.chmod(0o700)
        self.put("scene/generated.private", "dirty source, not the selected checkout")
        run = self.submit()
        self.assertEqual(self.terminal(run)["scene"], "completed")
        with tarfile.open(run / "start.tar.gz") as archive:
            self.assertEqual(
                archive.extractfile("./generated.private").read().decode().strip(),
                commit,
            )
        self.assertEqual(
            (run / "workspace/generated.private").read_text().strip(), commit
        )

    def test_delayed_peer_is_discovered_before_work_begins(self):
        self.version(delay_subject=True)
        run = self.submit()
        deadline = time.monotonic() + 15
        while not self.a.observed_peer_list:
            if time.monotonic() >= deadline:
                self.fail("Coordinator never received its native peers read result")
            time.sleep(0.05)
        (self.root / "release-subject").touch()
        end = self.terminal(run)
        self.assertEqual(end["scene"], "completed", end)
        self.assertTrue(list((run / "workspace").glob("repair-*.txt")))

    def test_native_model_can_start_without_an_exact_catalog_row(self):
        # OMP constructs this exact Bedrock model from an inference profile ARN.
        # The coordinator stays silent, so no AWS credentials or call are needed.
        self.version(case="owner_hang")
        self.timers(heartbeat=45, total=60)
        arn = "arn:aws:bedrock:us-east-1:123456789012:inference-profile/fixture-v1"
        provider = "amazon-bedrock"
        model = provider + "/" + arn
        config_path = "roles/subject/config.yml"
        config = json.loads((self.repo / config_path).read_text())
        config["modelRoles"]["default"] = model
        self.put(config_path, json.dumps(config))
        self.put(
            "roles/subject/models.yml",
            json.dumps(
                {
                    "providers": {
                        provider: {
                            "apiKey": "BEDROCK_FIXTURE_TOKEN",
                            "baseUrl": self.b.url,
                            "api": "bedrock-converse-stream",
                            "models": [{"id": "template", "name": "Template"}],
                        }
                    }
                }
            ),
        )
        with (self.config / "credentials.toml").open("a") as stream:
            stream.write(f"\n{provider} = {json.dumps(self.b.key)}\n")
        self.git("add", "roles/subject")
        self.git("commit", "-qm", "Select a native non-catalog inference profile")
        run = self.submit()
        deadline = time.monotonic() + 40
        while not any(
            e.get("type") == "model_change" and e.get("model") == model
            for p in self.sessions(run, "subject")
            for e in json_lines(p)
        ):
            records = json_lines(run / "run.log")
            if (
                any(r["event"] == "terminal" for r in records)
                or time.monotonic() >= deadline
            ):
                self.fail(f"Native non-catalog model did not start: {records}")
            time.sleep(0.1)
        os.kill(json_lines(run / "run.log")[0]["pid"], signal.SIGTERM)
        end = self.terminal(run)
        self.assertEqual(end["reason"], "interrupted", end)

    def test_host_login_precedes_config_and_missing_credentials_reject_submission(self):
        self.version()
        path = "roles/coordinator/models.yml"
        models = json.loads((self.repo / path).read_text())
        models["providers"]["alpha"]["apiKey"] = "gatewayToken"
        self.put(path, json.dumps(models))
        self.git("add", path)
        self.git("commit", "-qm", "Use a mixed-case gateway credential reference")
        entry = {
            "provider": "alpha",
            "credential": {"type": "api_key", "key": self.a.key, "source": "login"},
        }
        output(
            [str(self.omp), "auth", "import", "-"],
            env=self.env,
            input=json.dumps({"version": 1, "credentials": [entry]}),
        )
        credentials = self.config / "credentials.toml"
        credentials.write_text(
            f'[providers]\nalpha="wrong-account"\nbeta={json.dumps(self.b.key)}\n'
        )
        run = self.submit()
        end = self.terminal(run)
        self.assertEqual(end["scene"], "completed", end)
        self.assert_normal_teardown(run, end)
        self.assertTrue(
            any(c["authorized"] and c["model"] == "owner-normal" for c in self.a.calls)
        )
        credentials.write_text('[providers]\nalpha="wrong-account"\n')
        failed = self.call()
        self.assertNotEqual(failed.returncode, 0)
        self.assertNotIn("submitted", failed.stdout)
        self.assertIn("beta", failed.stderr)

    def test_empty_workspace_and_material_blocker_preserve_native_reason(self):
        self.version(case="material", workspace=False)
        run = self.submit()
        end = self.terminal(run)
        self.assertEqual(end["scene"], "scenario_error", end)
        self.assert_normal_teardown(run, end)
        self.assertTrue(end["sceneReason"])
        self.assertFalse((run / "start.tar.gz").exists())
        self.assertFalse((run / "workspace/material.txt").exists())
        messages = [
            e["message"]
            for f in self.sessions(run, "coordinator")
            for e in json_lines(f)
            if e.get("message", {}).get("toolName") == "finish_run"
            and not e["message"].get("isError")
        ]
        self.assertEqual(messages[0]["details"]["reason"], end["sceneReason"])

    def test_failure_origin_does_not_turn_into_scene_or_wrong_account(self):
        for case, role in [("denied", "subject"), ("owner_denied", "coordinator")]:
            with self.subTest(case=case):
                self.version(case=case)
                run = self.submit()
                end = self.terminal(run)
                self.assertIsNone(end["scene"], end)
                self.assertEqual(end["reason"], "provider_fault", end)
                self.assertEqual(end["detail"]["role"], role)
                self.assertEqual(end["detail"]["http"], 401)
                self.assertTrue(end["detail"]["model"].endswith(case))

    def test_auth_failure_after_delivery_does_not_revoke_scene(self):
        self.version(case="after_delivery")
        run = self.submit()
        end = self.terminal(run)
        self.assertEqual(end["scene"], "completed", end)
        self.assertTrue(
            any(
                e.get("message", {}).get("errorStatus") == 401
                for f in self.sessions(run, "subject")
                for e in json_lines(f)
            )
        )

    def test_oauth_access_uses_role_binding_without_copying_the_login_store(self):
        self.version()
        provider = "openai-codex"
        refresh = "private-refresh-" + self.a.key
        login = {
            "provider": provider,
            "credential": {
                "type": "oauth",
                "access": self.a.key,
                "refresh": refresh,
                "expires": int(time.time() * 1000) + 3_600_000,
            },
        }
        output(
            [str(self.omp), "auth", "import", "-"],
            env=self.env,
            input=json.dumps({"version": 1, "credentials": [login]}),
        )
        # Keep the fixture on loopback: use only OMP's real OAuth storage and token
        # export here, not the live ChatGPT service or its proprietary wire API.
        config_path = "roles/coordinator/config.yml"
        config = json.loads((self.repo / config_path).read_text())
        config["modelRoles"]["default"] = provider + "/owner-normal"
        self.put(config_path, json.dumps(config))
        models_path = "roles/coordinator/models.yml"
        service = json.loads((self.repo / models_path).read_text())["providers"][
            "alpha"
        ]
        del service["apiKey"]
        self.put(models_path, json.dumps({"providers": {provider: service}}))
        self.git("add", config_path, models_path)
        self.git(
            "commit", "-qm", "Use host OAuth and a role-local credential reference"
        )
        run = self.submit()
        end = self.terminal(run)
        self.assertEqual(end["scene"], "completed", end)
        self.assertTrue(
            any(c["authorized"] and c["model"] == "owner-normal" for c in self.a.calls)
        )
        self.assert_no_credentials(run)

    def test_missing_model_never_uses_other_available_model(self):
        for role, expected, endpoint in [
            ("subject", "beta/desk-normal", self.b),
            ("coordinator", "alpha/owner-normal", self.a),
        ]:
            with self.subTest(role=role):
                self.version(unavailable=role)
                run = self.submit()
                end = self.terminal(run)
                self.assertIsNone(end["scene"], end)
                self.assertEqual(
                    (end["detail"].get("role"), end["detail"].get("model")),
                    (role, expected),
                    end,
                )
                self.assertNotIn(
                    end["reason"],
                    {"discovery_timeout", "heartbeat_timeout", "run_timeout"},
                )
                self.assertFalse(
                    any(
                        c["model"] == "other" and c["kind"] == "agent"
                        for c in endpoint.calls
                    )
                )

    def test_native_reasoning_suffix_keeps_the_selected_model(self):
        self.version(thinking=True)
        end = self.terminal(self.submit())
        self.assertEqual(end["scene"], "completed", end)
        for endpoint, model in [(self.a, "owner-normal"), (self.b, "desk-normal")]:
            self.assertEqual(
                {c["model"] for c in endpoint.calls if c["kind"] == "agent"}, {model}
            )

    def test_owner_hang_and_healthy_indefinite_wait_have_different_bounds(self):
        for case, timeout, reason in [
            ("owner_hang", 25, "heartbeat_timeout"),
            ("endless", 12, "run_timeout"),
        ]:
            with self.subTest(case=case):
                self.timers(heartbeat=6, total=timeout)
                self.version(case=case)
                run = self.submit()
                end = self.terminal(run)
                self.assertIsNone(end["scene"], end)
                self.assertEqual(end["reason"], reason, end)

    def test_success_record_survives_timeout_during_final_model_request(self):
        self.version(case="final_hang")
        run = self.submit()
        end = self.terminal(run)
        self.assertEqual(
            (end["scene"], end["reason"]), ("completed", "exit_grace_timeout"), end
        )

    def test_interrupt_preserves_report_already_in_native_session(self):
        self.timers(grace=15)
        self.version(case="final_hang")
        run = self.submit()
        supervisor = json_lines(run / "run.log")[0]["pid"]
        deadline = time.monotonic() + 30
        while not any(
            entry.get("message", {}).get("toolName") == "finish_run"
            and entry["message"].get("details", {}).get("outcome") == "completed"
            for path in self.sessions(run, "coordinator")
            for entry in json_lines(path)
        ):
            if time.monotonic() >= deadline:
                self.fail(f"No native report; run log: {json_lines(run / 'run.log')}")
            time.sleep(0.05)
        os.kill(supervisor, signal.SIGTERM)
        end = self.terminal(run)
        self.assertEqual((end["scene"], end["reason"]), ("completed", "interrupted"))

    def test_configured_helper_calls_its_provider_from_subject_session(self):
        self.version(case="helper")
        run = self.submit()
        end = self.terminal(run)
        self.assertEqual(end["scene"], "completed", end)
        self.assertTrue(
            any(c["model"] == "helper" and c["authorized"] for c in self.a.calls)
        )
        self.assertFalse(any(c["model"] == "helper" for c in self.b.calls))
        sessions = {
            path: e
            for path in self.sessions(run, "subject")
            for e in json_lines(path)
            if e.get("type") == "session"
        }
        (main,) = [
            str(path) for path, e in sessions.items() if not e.get("parentSession")
        ]
        self.assertEqual(
            [e["parentSession"] for e in sessions.values() if e.get("parentSession")],
            [main],
        )
        self.assertEqual(
            set((run / "workspace/credential-scope.txt").read_text().split()),
            {"alpha", "beta"},
        )


if __name__ == "__main__":
    unittest.main()
