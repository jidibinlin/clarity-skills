# Clarity Skills

Human-led requirements and technical design, followed by implementation against approved models. Skills provide goals, useful methods and key decision boundaries; the model chooses ordinary investigation and implementation details.

## Workflows

| Skill | Outcome | Content standard |
| --- | --- | --- |
| [clarify-requirements](clarify-requirements/SKILL.md) | Requirements and domain behavior | [REQUIREMENTS-MODEL.md](clarify-requirements/REQUIREMENTS-MODEL.md) |
| [clarify-architecture](clarify-architecture/SKILL.md) | Global architecture | [ARCHITECTURE-MODEL.md](clarify-architecture/ARCHITECTURE-MODEL.md) |
| [clarify-technical-design](clarify-technical-design/SKILL.md) | Concrete files, topology, flows, data and contracts | [TECHNICAL-MODEL.md](clarify-technical-design/TECHNICAL-MODEL.md) |
| [implement](implement/SKILL.md) | One bounded implementation unit | — |

Requirements → technical design → implementation. Stage approval does not automatically launch the next stage.

The original implementer uses `tdd` for initial behavior and behavioral repairs, then uses `code-review` in the current context to dispatch independent Spec and Standards reviewers. Repair rounds return directly to those same reviewers. Existing progress is continued when present, not required to start.

`clarify-technical-design` remains one skill for the leader, closed-loop designers and their scouts. Designers clarify and write their assigned local models with the human. The leader takes over affected model revisions during coordination and whole-model review. Shared definitions have one authoritative location, and the complete model may include linked parts with one active writer per file. Whole-model review and final human approval remain distinct from local confirmation.

`Roles and collaboration` separates local human–designer clarification from human–leader coordination. The human initiates cross-group coordination and progression. Assignments name the role and require reading the complete skill and its authoring standard. Loading or re-reading does not expand the assignment.

## Responsibilities and reading

- **SKILL.md:** the working method and key human/agent handoffs.
- **Content standard:** read before authoring; the same criteria guide generation and independent review. Cross-stage imports name applicable content sections; the consuming stage owns its method, role routing and approval route.
- **Reviewer prompts:** scope modeling reviews. Code review uses the shared method below with unit or whole-result criteria.
- [communication-style](rules/communication-style.md): session-wide rules for shared context, clear explanations, Mermaid diagrams and consequential questions.
- [tdd](tdd/SKILL.md): the implementer's behavioral loop, including repair. [writing-good-tests.md](tdd/writing-good-tests.md) provides test-writing guidance, copied unchanged from [Superpowers `bb92a77`](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/test-driven-development/writing-good-tests.md) under its [MIT license](tdd/LICENSE.superpowers). [TESTING.md](tdd/TESTING.md) supplies shared test-quality criteria.
- [code-review](code-review/SKILL.md): Spec and Standards review criteria and independent subagent dispatch. Returns separate reports; `implement` owns repairs and re-review with the same reviewers, asking for clarification when needed.
  Adapted from [Matt Pocock v1.3.1](https://github.com/mattpocock/skills/blob/v1.3.1/skills/engineering/code-review/SKILL.md) under its [MIT license](code-review/LICENSE.mattpocock).
- [artifact-layout](artifact-layout/SKILL.md): private directories and file responsibilities.
- [collaboration-guidance](collaboration-guidance/SKILL.md): reusable factual scouts, scope and naming, preparation and consultation. Technical clarification owns its design coordination, writing and approval flow.

Keep guidance focused on this workflow's choices, not exhaustive policies or generic engineering instruction. Assess the complete reading path: moving restrictions into referenced files is not simplification.

Micro technical proposals and document drafts present concrete definitions with their operations and flows. Use target-language declarations for program types, native/dynamic schemas where appropriate, and precise references for unchanged definitions; prose explains rather than replaces them.

## Installation

Register complete skill directories and their dependencies in the agent harness. Stages use `artifact-layout`; implementation uses `tdd` and `code-review`. Code reviewers read `tdd`'s TESTING.md directly. Resolve cross-skill resources through their registered owner and companion files relative to the installed skill. Reading a reference does not start its owner's workflow.

Technical clarification also uses `collaboration-guidance`. Its role-specific flow is contained in the existing `clarify-technical-design` skill; no separate author or methodology skill is required.

Ordinary directory copying is sufficient; no source symlinks or installation-manager-specific packaging is required. Installed skills need not be siblings. OMP supports `skill://<name>` and `skill://<name>/<resource>`; other harnesses use native discovery. Register `tdd` and `code-review` unambiguously alongside any upstream skills. Installing skill directories alone does not change global instructions.

### Communication rules

Install [rules/communication-style.md](rules/communication-style.md) as session-wide instructions, not a skill. The OMP and OpenCode plugins add these rules to the existing system prompt. Codex uses its global `AGENTS.md`. These rules do not select or start other Clarity workflows.

`rules/communication-style.md` is the single source. Building embeds its body into two standalone JavaScript plugins; installed plugins do not read the checkout or need companion assets. Rebuild and reinstall when the rule changes. Remove the old `communication-style` skill registration when migrating.

From the repository root, with Bun installed:

```sh
bun plugins/build.mjs
(cd plugins && bun run test)
install -Dm644 plugins/dist/omp.js ~/.omp/agent/extensions/clarity.js
install -Dm644 plugins/dist/opencode.js ~/.config/opencode/plugins/clarity.js
```

Restart the runners after installation. For custom OMP profiles or OpenCode configuration directories, use their active extension/plugin directories instead. Install only one copy per runner.

For Codex without Home Manager, merge the rule body into `$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`), preserving existing instructions. Do not replace the file or set `model_instructions_file`. If `AGENTS.override.md` exists there, Codex uses it instead; reconcile that file before relying on this installation. Project instructions remain separate.

#### Home Manager

Pass this repository's non-flake input as `clarity-skills` through `extraSpecialArgs`, then add to your home module:

```nix
{ clarity-skills, ... }:
{
  imports = [ "${clarity-skills}/plugins/home-manager.nix" ];
  programs.clarityPlugins.enable = true;
}
```

The option is disabled by default. Enabling it builds and tests both plugins with Nix, installs them at the two default paths above, and appends the rule to Home Manager's `home.file.".codex/AGENTS.md".text` using `lib.mkAfter`. Other text definitions are retained; the module does not force-overwrite existing unmanaged files. Bring such files under Home Manager while preserving their content before activation.

Update the pinned repository input, apply your Home Manager configuration, and start new sessions. Custom profiles and `CODEX_HOME` need the same rules installed in their active configuration locations. The plugin package is also available through `pkgs.callPackage "${clarity-skills}/plugins" { }`.

The plugins preserve existing system blocks. A build-time source fingerprint prevents duplicate insertion when the same guidance is inherited or merged, even if the runner normalizes its whitespace. They check each prepared policy rather than remember a session flag, so rebuilt contexts receive the guidance again. OpenCode's system-transform hook is experimental; recheck compatibility when upgrading the runner.

## Private artifacts and decisions

Use the locally excluded `.scratch/<work-slug>/` layout. `issue.md` defines and links the work; models hold the current specification.

Show specification changes and obtain confirmation before writing them. Authorized implementation proceeds autonomously within the approved design. Preserve the original implementer/reviewer pair through repairs and obtain final human approval or acceptance for the stage result. These approvals do not authorize publication of private artifacts.
