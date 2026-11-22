"""Turn one resolved Git commit into the private inputs of one run."""

import json
import os
import re
import shutil
import subprocess
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

import yaml


class SubmissionError(Exception):
    """A diagnostic safe to print (never include subprocess output or parsed secrets)."""


def nix_environment():
    # Nix's client may need host store/registry settings and transport auth;
    # it does not need the submitter's OMP profile or provider credentials.
    allowed = {
        "PATH",
        "HOME",
        "USER",
        "LOGNAME",
        "TMPDIR",
        "LANG",
        "LC_ALL",
        "SSL_CERT_FILE",
        "SSL_CERT_DIR",
        "SSH_AUTH_SOCK",
        "http_proxy",
        "https_proxy",
        "no_proxy",
        "HTTP_PROXY",
        "HTTPS_PROXY",
        "NO_PROXY",
    }
    return {
        k: v
        for k, v in os.environ.items()
        if k in allowed or k.startswith(("NIX_", "XDG_"))
    }


def command(argv, failure, *, cwd=None):
    if argv[0] in ("nix", "nix-instantiate"):
        env = nix_environment()
    else:
        # A submit launched from a Git hook must still operate on *project*,
        # not the calling hook's index, objects or forced worktree. Likewise
        # a caller's TAR_OPTIONS must not change what gets archived.
        ignored = {
            "GIT_DIR",
            "GIT_COMMON_DIR",
            "GIT_WORK_TREE",
            "GIT_INDEX_FILE",
            "GIT_OBJECT_DIRECTORY",
            "GIT_ALTERNATE_OBJECT_DIRECTORIES",
            "GIT_NAMESPACE",
            "GIT_REPLACE_REF_BASE",
            "TAR_OPTIONS",
        }
        env = {k: v for k, v in os.environ.items() if k not in ignored}
    try:
        result = subprocess.run(
            argv,
            cwd=cwd,
            env=env,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            check=False,
        )
    except OSError as error:
        raise SubmissionError(f"{failure}: could not execute {argv[0]}") from error
    if result.returncode:
        raise SubmissionError(f"{failure} ({argv[0]} exit {result.returncode})")
    return result.stdout


@contextmanager
def selected_worktree(project, branch, revision):
    if revision is not None and branch is None:
        raise SubmissionError("--commit requires --branch")
    git = ["git", "-C", project]
    root = command(
        [*git, "rev-parse", "--show-toplevel"], "project is not a Git worktree"
    )
    if Path(root.rstrip(b"\n").decode()).resolve() != project:
        raise SubmissionError("project must be the Git worktree root")
    ref = "HEAD"
    if branch is not None:
        ref = f"refs/heads/{branch}"
        command([*git, "check-ref-format", ref], "invalid branch name")
    resolve = [*git, "rev-parse", "--verify", "--end-of-options"]
    tip = (
        command([*resolve, ref + "^{commit}"], "branch or HEAD has no such commit")
        .decode()
        .strip()
    )
    commit = tip
    if revision is not None:
        commit = (
            command(
                [*resolve, revision + "^{commit}"], "cannot resolve requested commit"
            )
            .decode()
            .strip()
        )
        command(
            [*git, "merge-base", "--is-ancestor", commit, tip],
            "commit is not on requested branch",
        )
    with tempfile.TemporaryDirectory(prefix="agent-test-source-") as temp:
        # Git names its worktree registration after this directory's basename.
        tree = Path(temp).resolve()
        try:
            command(
                [*git, "worktree", "add", "--detach", "--", tree, commit],
                "cannot check out selected commit",
            )
            yield tree, commit
        finally:
            # A checkout hook can generate ignored files, or fail *after* Git
            # registered the worktree. Remove just our registration and files.
            if (tree / ".git").is_file():
                command(
                    [*git, "worktree", "remove", "--force", "--", tree],
                    "cannot remove temporary worktree",
                )


def material(tree, relative, label, *, directory=False):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise SubmissionError(f"{label} must be a project-relative path")
    path = (tree / relative).resolve()
    if not path.is_relative_to(tree):
        raise SubmissionError(f"{label} falls outside the selected worktree")
    if not (path.is_dir() if directory else path.is_file()):
        raise SubmissionError(
            f"{label}: missing {'directory' if directory else 'file'} {relative!r}"
        )
    return path


def mapping(value, label):
    if not isinstance(value, dict):
        raise SubmissionError(f"{label} must be a mapping")
    return value


def yaml_map(path, label):
    try:
        with path.open("rb") as src:
            return mapping(yaml.safe_load(src), label)
    except (yaml.YAMLError, UnicodeError) as error:
        raise SubmissionError(f"{label} is not valid YAML") from error


@dataclass
class Role:
    model: str
    # provider -> (representative declared model for diagnostics, env references)
    providers: dict[str, tuple[str, set[str]]]


def credential_variable(value):
    # OMP's models.yml also accepts literals and !commands; neither is a
    # host credential reference. Don't let one replace process control state.
    return (
        isinstance(value, str)
        and re.fullmatch(r"[A-Z][A-Z0-9_]*", value)
        and not value.startswith(
            (
                "AGENT_TEST_",
                "OMP_",
                "PI_",
                "XDG_",
                "NIX_",
                "LD_",
                "DYLD_",
                "BASH_",
                "PYTHON",
                "BUN_",
                "NODE_",
                "LC_",
                "GIT_",
                "OPENSSL_",
                "SSL_CERT_",
            )
        )
        and value
        not in {
            "HOME",
            "PATH",
            "PWD",
            "OLDPWD",
            "USER",
            "LOGNAME",
            "TERM",
            "LANG",
            "TZ",
            "TMPDIR",
            "TMP",
            "TEMP",
            "SHELL",
            "ENV",
            "IFS",
            "SHLVL",
            "PS1",
            "PS4",
            "CDPATH",
        }
    )


AUTH_FIELD = re.compile(
    r"(?:^|[-_])(?:auth|authorization|authentication|cookie|api[-_]?key|access[-_]?key|token|secret|password)(?:$|[-_])|^key$",
    re.IGNORECASE,
)


def provider_references(definition, name):
    refs = []
    if "apiKey" in definition:
        refs.append(definition["apiKey"])
    models = definition.get("models", [])
    overrides = mapping(definition.get("modelOverrides", {}), f"{name} modelOverrides")
    if not isinstance(models, list):
        raise SubmissionError(f"{name} provider models must be a list")
    for node in (definition, *models, *overrides.values()):
        node = mapping(node, f"{name} model definition")
        url = node.get("baseUrl")
        if isinstance(url, str):
            location = urlsplit(url)
            if location.username is not None or any(
                AUTH_FIELD.search(k) for k, _ in parse_qsl(location.query)
            ):
                raise SubmissionError(
                    f"{name} models.yml must not embed credentials in a URL"
                )
        for header, value in mapping(
            node.get("headers", {}), f"{name} headers"
        ).items():
            if isinstance(header, str) and AUTH_FIELD.search(header):
                refs.append(value)
    if not all(credential_variable(ref) for ref in refs):
        raise SubmissionError(
            f"{name} models.yml credential fields must reference environment variables"
        )
    return set(refs)


def prepare_role(tree, run, name, declaration):
    role_dir = material(
        tree, declaration.get("ompConfigDir"), f"{name}.ompConfigDir", directory=True
    )
    relative = role_dir.relative_to(tree)
    config = material(tree, str(relative / "config.yml"), f"{name} config.yml")
    config_data = yaml_map(config, f"{name} config.yml")
    models = mapping(config_data.get("modelRoles"), f"{name} modelRoles")
    if "default" not in models:
        raise SubmissionError(f"{name} modelRoles.default is required")
    needed = {}
    for role_id in ["default", *(key for key in models if key != "default")]:
        model = models[role_id]
        if not isinstance(model, str) or not re.fullmatch(
            r"[a-zA-Z0-9][a-zA-Z0-9._-]*/[^\s\x00-\x1f\x7f]+", model
        ):
            raise SubmissionError(
                f"{name} modelRoles entries must name an exact provider/model"
            )
        needed.setdefault(model.partition("/")[0], model)

    destination = run / "home/.omp/profiles" / name / "agent"
    destination.mkdir(parents=True)
    raw_models = role_dir / "models.yml"
    submitted_models = None
    model_data = {}
    if raw_models.exists() or raw_models.is_symlink():
        submitted_models = material(
            tree, str(relative / "models.yml"), f"{name} models.yml"
        )
        model_data = yaml_map(submitted_models, f"{name} models.yml")
    providers = mapping(
        model_data.setdefault("providers", {}), f"{name} models.yml providers"
    )
    variables = {}
    references = {}
    for provider, definition in providers.items():
        refs = provider_references(
            mapping(definition, f"{name} provider definition"), name
        )
        for key in refs:
            if key in variables and variables[key] != provider:
                raise SubmissionError(
                    f"{name} models.yml must not share a credential variable between providers"
                )
            variables[key] = provider
        references[provider] = refs

    bindings = {}
    implicit = False
    for index, (provider, model) in enumerate(needed.items()):
        definition = providers.get(provider, {})
        variable = definition.get("apiKey")
        if variable is None:
            # No table of built-in provider aliases: this works for OAuth as
            # well as providers with no native OMP environment variable.
            variable = f"AGENT_TEST_CREDENTIAL_{index}"
            # Don't mutate a definition shared by YAML anchors with other providers.
            providers[provider] = {**definition, "apiKey": variable}
            implicit = True
        bindings[provider] = (model, references.get(provider, set()) | {variable})
    if implicit:
        if submitted_models is not None:
            shutil.copyfile(submitted_models, destination / "submitted-models.yml")
        with (destination / "models.yml").open("w") as f:
            yaml.safe_dump(model_data, f, sort_keys=False)
    else:
        shutil.copyfile(submitted_models, destination / "models.yml")
    shutil.copyfile(config, destination / "config.yml")
    skills = role_dir / "skills"
    if skills.exists() or skills.is_symlink():
        skills = material(
            tree, str(relative / "skills"), f"{name} skills", directory=True
        )
        shutil.copytree(skills, destination / "skills", symlinks=True)
    return Role(models["default"], bindings)


def prepare(tree, run):
    material(tree, "flake.nix", "development environment")
    description = material(tree, "test.nix", "test description")
    raw = command(
        ["nix-instantiate", "--eval", "--strict", "--json", description],
        "cannot evaluate test.nix",
        cwd=tree,
    )
    try:
        spec = mapping(json.loads(raw), "test.nix")
    except ValueError as error:
        raise SubmissionError("test.nix did not evaluate to a JSON object") from error
    roles = {}
    for name in ("subject", "coordinator"):
        declaration = mapping(spec.get(name), f"test.nix {name}")
        roles[name] = prepare_role(tree, run, name, declaration)
    prompt = material(tree, spec["coordinator"].get("prompt"), "coordinator.prompt")
    shutil.copyfile(prompt, run / "coordinator-prompt.md")
    # OMP walks ancestors for AGENTS.md and project skills using its own
    # nearest-.git check, not Git's environment or the process temp directory.
    # Keep that boundary outside workspace, even for an empty-input scenario.
    command(
        ["git", "init", "--quiet", "--template=", run],
        "cannot isolate OMP project discovery",
    )
    command(
        ["git", "-C", run, "config", "--local", "core.hooksPath", os.devnull],
        "cannot disable hooks in the discovery boundary",
    )
    workspace = run / "workspace"
    workspace.mkdir()
    if "workspaceSource" in spec:
        source = material(
            tree, spec["workspaceSource"], "workspaceSource", directory=True
        )
        archive = run / "start.tar.gz"
        command(
            ["tar", "-czf", archive, "--exclude=.git", "-C", source, "."],
            "cannot archive workspaceSource",
        )
        command(
            ["tar", "-xzf", archive, "--no-same-owner", "-C", workspace],
            "cannot initialize workspace",
        )
    return roles
