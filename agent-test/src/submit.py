"""Host-side run command. After positive acknowledgement nothing here owns the run."""

import argparse
import json
import math
import os
import shutil
import signal
import stat
import subprocess
import sys
import threading
import tomllib
import uuid
from pathlib import Path

from materials import (
    SubmissionError,
    command,
    nix_environment,
    prepare,
    selected_worktree,
)

DEFAULT_TIMERS = {
    "discovery": 120,
    "poll": 60,
    "heartbeat": 600,
    "total": 3600,
    "grace": 30,
}


def host_config():
    root = os.environ.get("XDG_CONFIG_HOME")
    return (Path(root) if root else Path.home() / ".config") / "agent-test"


def config_section(filename, section, *, secret=False):
    path = host_config() / filename
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK)
    except FileNotFoundError:
        return {}
    except OSError as error:
        raise SubmissionError(f"cannot open host {filename}") from error
    with os.fdopen(fd, "rb") as stream:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            raise SubmissionError(f"host {filename} must be a regular file")
        if secret and (info.st_uid != os.geteuid() or info.st_mode & 0o077):
            raise SubmissionError(
                f"host {filename} must be owned by this user and private (chmod 600)"
            )
        try:
            value = tomllib.load(stream).get(section, {})
        except (tomllib.TOMLDecodeError, UnicodeError) as error:
            raise SubmissionError(f"invalid TOML in host {filename}") from error
        if not isinstance(value, dict):
            raise SubmissionError(f"host {filename} must use a [{section}] table")
        return value


def timers():
    overrides = config_section("settings.toml", "timers")
    if overrides.keys() - DEFAULT_TIMERS.keys():
        raise SubmissionError("unknown [timers] setting")
    for name, value in overrides.items():
        if type(value) not in (float, int) or value <= 0 or not math.isfinite(value):
            raise SubmissionError(
                f"timers.{name} must be a positive, finite number of seconds"
            )
    return DEFAULT_TIMERS | overrides


def omp_call(omp, *args):
    # Never evaluate a submitted project's .env or models.yml as *host* auth.
    # Neither output stream is a user diagnostic: either may contain a secret.
    try:
        return subprocess.run(
            [omp, *args],
            stdin=subprocess.DEVNULL,
            capture_output=True,
            check=False,
            cwd=Path.home(),
            env={**os.environ, "NO_COLOR": "1", "FORCE_COLOR": "0"},
        )
    except OSError as error:
        raise SubmissionError("could not execute host OMP") from error


def host_token(omp, provider):
    result = omp_call(omp, "token", provider, "--raw")
    if result.returncode == 0:
        try:
            token = result.stdout.decode().rstrip("\r\n")
        except UnicodeError:
            token = ""
        if not token or any(ch in token for ch in "\x00\r\n"):
            raise SubmissionError("host OMP returned no usable credential")
        return token
    # OMP 19's token command gives the same exit code for an absent key and a
    # login/refresh error. Only its explicit absence diagnostic permits fallback.
    lines = result.stderr.decode(errors="replace").strip().splitlines()
    absent = f'No active credential found for provider "{provider}".'
    if result.returncode != 1 or not lines or lines[0] != absent or len(lines) > 2:
        raise SubmissionError("host OMP could not obtain credential; check login")
    if len(lines) == 2:
        prefix = "Configured providers: "
        if not lines[1].startswith(prefix) or provider.lower() in lines[1][
            len(prefix) :
        ].lower().split(", "):
            raise SubmissionError(
                "configured host OMP credential is unavailable; check login"
            )
    # Invalid grants can be disabled by OMP during refresh, disappearing from
    # token's active list. usage keeps those actionable tombstones distinct
    # from deliberate deletions; never use a second key after a bad login.
    status = omp_call(
        omp, "usage", "--provider", provider, "--json", "--no-extensions", "--redact"
    )
    try:
        summary = json.loads(status.stdout)
        known = [
            summary[field]
            for field in ("disabledCredentials", "accountsWithoutUsage", "reports")
        ]
        if status.returncode or not all(isinstance(rows, list) for rows in known):
            raise ValueError()
    except (ValueError, TypeError, KeyError):
        raise SubmissionError("cannot determine host OMP credential status") from None
    if any(known):
        raise SubmissionError(
            "configured host OMP credential is unavailable; check login"
        )
    return None


def role_payload(roles):
    omp = shutil.which("omp")
    cache = {}
    fallback = None
    result = {}
    try:
        for name, role in roles.items():
            env = {}
            for provider, (model, variables) in role.providers.items():
                if provider not in cache:
                    try:
                        token = host_token(omp, provider) if omp else None
                        if token is None:
                            if fallback is None:
                                fallback = config_section(
                                    "credentials.toml", "providers", secret=True
                                )
                            token = fallback.get(provider)
                            if (
                                not isinstance(token, str)
                                or not token.strip()
                                or any(c in token for c in "\x00\r\n")
                            ):
                                raise SubmissionError(
                                    "no provider credential in host OMP or credentials.toml"
                                )
                        cache[provider] = token
                    except SubmissionError as error:
                        raise SubmissionError(f"{name} {model}: {error}") from None
                env.update(dict.fromkeys(variables, cache[provider]))
            result[name] = {"model": role.model, "env": env}
        return result
    finally:
        cache.clear()
        if fallback is not None:
            fallback.clear()


def shell_derivation(tree):
    system = json.loads(
        command(
            ["nix-instantiate", "--eval", "--json", "--expr", "builtins.currentSystem"],
            "cannot determine local Nix system",
        )
    )
    # nix develop with an explicit #default tries the devShell before packages,
    # legacyPackages and a literal flake output. Resolve that same installable.
    for prefix in [
        f"devShells.{system}.",
        f"packages.{system}.",
        f"legacyPackages.{system}.",
        "",
    ]:
        try:
            drv = (
                command(
                    ["nix", "eval", "--raw", f"{tree}#{prefix}default.drvPath"],
                    "cannot resolve development environment",
                )
                .decode()
                .strip()
            )
        except SubmissionError:
            continue
        if drv.startswith("/") and drv.endswith(".drv"):
            return drv
    raise SubmissionError(
        "cannot resolve default Nix development environment derivation"
    )


def stop_unaccepted(process):
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait()


def handoff(run, tree, payload):
    supervise = Path(__file__).resolve().with_name("supervise")
    request = json.dumps(payload, separators=(",", ":")).encode() + b"\n"
    payload.pop("roles").clear()
    process = subprocess.Popen(
        [
            "nix",
            "develop",
            "--ignore-env",
            f"{tree}#default",
            "--command",
            supervise,
            run,
        ],
        cwd=run,
        env=nix_environment(),
        start_new_session=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    expected = {"runId": run.name, "status": "submitted"}
    sent = False

    def send(data):
        nonlocal sent
        try:
            with process.stdin:
                process.stdin.write(data)
            sent = True
        except OSError:
            pass

    # Drain stdout concurrently: even before exec, a devShell can print its
    # own banner. Never copy that output into a log or the public JSON reply.
    writer = threading.Thread(target=send, args=(request,))
    del request
    accepted = False
    try:
        writer.start()
        with process.stdout:
            for line in iter(lambda: process.stdout.readline(65536), b""):
                try:
                    ack = json.loads(line)
                except (ValueError, UnicodeError):
                    continue
                if ack == expected:
                    # A shellHook can print arbitrary banners on this same
                    # stream. An acknowledgement is only meaningful once the
                    # receiver has persisted the actual source record.
                    try:
                        with (run / "run.log").open("rb") as log:
                            record = json.loads(log.readline())
                    except (FileNotFoundError, ValueError):
                        continue
                    if (
                        not isinstance(record, dict)
                        or record.get("event") != "submitted"
                        or any(
                            key not in record or record[key] != payload[key]
                            for key in ("source", "commit", "branch", "drv")
                        )
                    ):
                        continue
                    writer.join()
                    if sent:
                        accepted = True
                        return expected
                    break
        raise SubmissionError(
            "Nix environment or supervisor failed before acknowledgement"
        )
    finally:
        if not accepted:
            stop_unaccepted(process)
        if writer.ident is not None:
            writer.join()


def submit(args):
    project = Path(args.project).resolve()
    policy = timers()
    with selected_worktree(project, args.branch, args.commit) as (tree, commit):
        runs = Path.cwd() / "runs"
        runs.mkdir(mode=0o700, exist_ok=True)
        run = runs / str(uuid.uuid4())
        run.mkdir(mode=0o700)
        try:
            roles = prepare(tree, run)
            drv = shell_derivation(tree)
            return handoff(
                run,
                tree,
                {
                    "source": str(project),
                    "commit": commit,
                    "branch": args.branch,
                    "drv": drv,
                    "roles": role_payload(roles),
                    "policy": policy,
                },
            )
        except BaseException:
            shutil.rmtree(run)
            raise


def main():
    parser = argparse.ArgumentParser(
        prog="run", description="Submit a committed agent test project."
    )
    parser.add_argument("project")
    parser.add_argument("--branch")
    parser.add_argument("--commit")
    args = parser.parse_args()

    def interrupt(signum, frame):
        raise KeyboardInterrupt()

    signal.signal(signal.SIGTERM, interrupt)
    signal.signal(signal.SIGHUP, interrupt)
    try:
        reply = submit(args)
    except SubmissionError as error:
        print(f"run: {error}", file=sys.stderr)
        return 1
    except (OSError, UnicodeError, ValueError, RuntimeError, OverflowError) as error:
        # Python/Nix/OMP error text may quote input data. Report only a safe
        # system diagnostic, never a command, parsed YAML/TOML, token or path.
        reason = (
            error.strerror if isinstance(error, OSError) else "invalid submission data"
        )
        print(f"run: submission failed: {reason}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("run: submission interrupted", file=sys.stderr)
        return 130
    print(json.dumps(reply, separators=(",", ":")), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
