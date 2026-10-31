# Clarity Skills

Human-led requirements and technical design, followed by implementation against approved models. Skills provide goals, useful methods and key decision boundaries; the model chooses ordinary investigation and implementation details.

## Workflows

| Skill | Outcome | Content standard |
| --- | --- | --- |
| [wayfinder](wayfinder/SKILL.md) | Coarse decomposition guided by tentative topology | [WAYFINDER-MODEL.md](wayfinder/WAYFINDER-MODEL.md) |
| [clarify-requirements](clarify-requirements/SKILL.md) | Requirements or a composed shared/child package | [REQUIREMENTS-MODEL.md](clarify-requirements/REQUIREMENTS-MODEL.md) |
| [clarify-architecture](clarify-architecture/SKILL.md) | Overall heavyweight architecture | [ARCHITECTURE-MODEL.md](clarify-architecture/ARCHITECTURE-MODEL.md) |
| [clarify-technical-design](clarify-technical-design/SKILL.md) | Coordinated technical realization: files, topology, flows, data and contracts | [TECHNICAL-MODEL.md](clarify-technical-design/TECHNICAL-MODEL.md) |
| [orchestrate-implementation](orchestrate-implementation/SKILL.md) | Whole-work implementation and human acceptance | [ORCHESTRATION.md](orchestrate-implementation/ORCHESTRATION.md) |
| [implement](implement/SKILL.md) | One bounded implementation unit | — |

Lightweight: requirements → technical design → implementation. Heavyweight: Wayfinder → shared/child requirements → overall architecture → child technical designs → implementation. Stage approval does not automatically launch the next stage.

`orchestrate-implementation` starts from the approved work and coordinates ready units through `implement`. The original implementer uses `tdd` for initial behavior and behavioral repairs, then uses `code-review` in the current context to dispatch independent Spec and Standards reviewers. Repair rounds return directly to those same reviewers. Existing progress is continued when present, not required to start.

`clarify-technical-design` coordinates the whole technical scope and assigns `technical-design-author` to scoped decision-makers. Authors use `technical-clarification` for macro-to-micro methods, confirm concrete proposals with the human and write canonical model content themselves. The coordinator shares survey collaborators, reconciles dependencies and arranges independent whole-model review and final approval. One author remains valid; parallel groups can use linked design parts with one writer per file.

## Responsibilities and reading

- **SKILL.md:** the working method and key human/agent handoffs.
- **Content standard:** read before authoring; the same criteria guide generation and independent review. Cross-stage imports name applicable content sections; the consuming stage owns its method, role routing and approval route.
- **Reviewer prompts:** scope modeling reviews. Code review uses the shared method below with unit or whole-result criteria.
- [communication-style](communication-style/SKILL.md): shared context, clear explanations, Mermaid diagrams and consequential questions.
- [tdd](tdd/SKILL.md): the implementer's behavioral loop, including repair. [writing-good-tests.md](tdd/writing-good-tests.md) provides test-writing guidance, copied unchanged from [Superpowers `bb92a77`](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/test-driven-development/writing-good-tests.md) under its [MIT license](tdd/LICENSE.superpowers). [TESTING.md](tdd/TESTING.md) supplies shared test-quality criteria.
- [code-review](code-review/SKILL.md): Spec and Standards review criteria and independent subagent dispatch. Returns separate reports; `implement` owns repairs and re-review with the same reviewers, asking for clarification when needed.
  Adapted from [Matt Pocock v1.3.1](https://github.com/mattpocock/skills/blob/v1.3.1/skills/engineering/code-review/SKILL.md) under its [MIT license](code-review/LICENSE.mattpocock).
- [artifact-layout](artifact-layout/SKILL.md): private directories and file responsibilities.
- [technical-clarification](technical-clarification/SKILL.md): reusable macro-to-micro clarification, draft-based iteration and whole-group confirmation within an assigned technical scope. The consuming role supplies document-writing responsibilities and the approval route.
- [technical-design-author](technical-design-author/SKILL.md): assigned-scope decision-making, human confirmation, canonical document writes and original-author repairs. Uses the common technical model standard rather than defining a second one.
- [technical-clarification-collaboration](technical-clarification-collaboration/SKILL.md): opt-in technical clarification pilot. Main owns macro understanding and coordination; shared survey owners explain existing code/documents; clarification owners retain bounded human-facing decision loops. Cross-topic questions may expand an existing owner's scope. Single-clarifier work remains valid; this does not replace the technical stage's confirmation, writing or review rules, or establish suitability for other clarification stages.
- [collaboration-guidance](collaboration-guidance/SKILL.md): reusable factual investigation and decision-conflict escalation. Technical design uses it for early survey preparation, shared survey contacts and peer conflict escalation; the stage and author roles retain their confirmation, writing and approval responsibilities. The two collaboration methods remain independently usable.

Keep guidance focused on this workflow's choices, not exhaustive policies or generic engineering instruction. Assess the complete reading path: moving restrictions into referenced files is not simplification.

Micro technical proposals and document drafts present concrete definitions with their operations and flows. Use target-language declarations for program types, native/dynamic schemas where appropriate, and precise references for unchanged definitions; prose explains rather than replaces them.

## Installation

Register complete skill directories and their dependencies in the agent harness. Stages use `artifact-layout`; communication uses `communication-style`; implementation uses `tdd` and `code-review`. Code reviewers read `tdd`'s TESTING.md directly. Resolve cross-skill resources through their registered owner and companion files relative to the installed skill. Reading a reference does not start its owner's workflow.

Technical design requires `technical-clarification`, `technical-design-author` and `collaboration-guidance` alongside the stage, artifact and communication skills. Architecture's selective `Macro views` import resolves through `technical-clarification`; its content-standard imports still resolve through `clarify-technical-design`.

Ordinary directory copying is sufficient; no source symlinks or installation-manager-specific packaging is required. Installed skills need not be siblings. OMP supports `skill://<name>` and `skill://<name>/<resource>`; other harnesses use native discovery. Register `wayfinder`, `tdd` and `code-review` unambiguously alongside any upstream skills. Installing skill directories alone does not change global instructions.

The earlier collaboration pilot is selected explicitly, not automatically enabled by installation. If trying it, register its complete directory alongside the technical-design dependencies above. The technical stage's role-based flow does not require this pilot; no plugin or global instruction changes are required.

### Optional communication bootstrap

The OMP and OpenCode plugins preload `communication-style` into the system prompt without a separate skill invocation. They do not select or start other Clarity workflows. Codex is not included.

`communication-style/SKILL.md` is the single source. Building removes its frontmatter and embeds its body into two standalone JavaScript files; installed plugins do not read the checkout or need companion assets. Rebuild and reinstall when the skill changes.

From the repository root, with Bun installed:

```sh
bun plugins/build.mjs
(cd plugins && bun run test)
install -Dm644 plugins/dist/omp.js ~/.omp/agent/extensions/clarity.js
install -Dm644 plugins/dist/opencode.js ~/.config/opencode/plugins/clarity.js
```

Restart the runners after installation. For custom OMP profiles or OpenCode configuration directories, use their active extension/plugin directories instead. Install only one copy per runner.

#### Home Manager

Pass this repository's non-flake input as `clarity-skills` through `extraSpecialArgs`, then add to your home module:

```nix
{ clarity-skills, ... }:
{
  imports = [ "${clarity-skills}/plugins/home-manager.nix" ];
  programs.clarityPlugins.enable = true;
}
```

The option is disabled by default. Enabling it builds and tests both plugins with Nix, then installs them at the two default paths above. Apply your Home Manager configuration and restart the runners. Update the pinned repository input before rebuilding to pick up newer guidance. The package is also available through `pkgs.callPackage "${clarity-skills}/plugins" { }`.

The plugins preserve existing system blocks. A build-time source fingerprint prevents duplicate insertion when the same guidance is inherited or merged, even if the runner normalizes its whitespace. They check each prepared policy rather than remember a session flag, so rebuilt contexts receive the guidance again. OpenCode's system-transform hook is experimental; recheck compatibility when upgrading the runner.

## Private artifacts and decisions

Use the locally excluded `.scratch/<work-slug>/` layout. `issue.md` defines and links the work; models hold the current specification.

Show specification changes and obtain confirmation before writing them. Authorized implementation proceeds autonomously within the approved design. Preserve the original implementer/reviewer pair through repairs and obtain final human approval or acceptance for the stage result. These approvals do not authorize publication of private artifacts.
