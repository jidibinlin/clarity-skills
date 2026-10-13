# Clarity Skills

Human-led requirements and technical design, followed by implementation against approved models. Skills provide goals, useful methods and key decision boundaries; the model chooses ordinary investigation and implementation details.

## Workflows

| Skill | Outcome | Content standard |
| --- | --- | --- |
| [wayfinder](wayfinder/SKILL.md) | Coarse decomposition guided by tentative topology | [WAYFINDER-MODEL.md](wayfinder/WAYFINDER-MODEL.md) |
| [clarify-requirements](clarify-requirements/SKILL.md) | Requirements or a composed shared/child package | [REQUIREMENTS-MODEL.md](clarify-requirements/REQUIREMENTS-MODEL.md) |
| [clarify-architecture](clarify-architecture/SKILL.md) | Overall heavyweight architecture | [ARCHITECTURE-MODEL.md](clarify-architecture/ARCHITECTURE-MODEL.md) |
| [clarify-technical-design](clarify-technical-design/SKILL.md) | Concrete files, topology, flows, data and contracts | [TECHNICAL-MODEL.md](clarify-technical-design/TECHNICAL-MODEL.md) |
| [clarify-change](clarify-change/SKILL.md) | Current baseline and agreed target change | [CHANGE-MODEL.md](clarify-change/CHANGE-MODEL.md) |
| [split-tickets](split-tickets/SKILL.md) | Context-fit usable increments | [TICKETS.md](split-tickets/TICKETS.md) |
| [implement](implement/SKILL.md) | Whole-work implementation and human acceptance | [ORCHESTRATION.md](implement/ORCHESTRATION.md) |
| [implement-unit](implement-unit/SKILL.md) | One ticket or bounded direct change | [IMPLEMENTATION.md](implement-unit/IMPLEMENTATION.md) |

Lightweight: requirements → technical design → tickets → implementation. Heavyweight: Wayfinder → shared/child requirements → overall architecture → child technical designs → one root ticket set → implementation. A bounded approved change can go directly to implementation. Stage approval does not automatically launch the next stage.

`implement` starts from the approved work and coordinates ready units through `implement-unit`. The original implementer uses `tdd` for initial behavior and behavioral repairs; the independent reviewer uses `code-review`. Existing progress is continued when present, not required to start.

## Responsibilities and reading

- **SKILL.md:** the working method and key human/agent handoffs.
- **Content standard:** read before authoring; the same criteria guide generation and independent review.
- **Reviewer prompts:** scope modeling and ticket-planning reviews. Code review uses the shared method below with unit or whole-result criteria.
- [ask-with-context](ask-with-context/SKILL.md): decision-ready questions and continued clarification.
- [tdd](tdd/SKILL.md): the implementer's behavioral loop, including repair. [TESTING.md](tdd/TESTING.md) supplies shared test-quality criteria.
- [code-review](code-review/SKILL.md): the independent reviewer's method for conformance, engineering quality and verification evidence. It does not dispatch another review team or repair code.
- [artifact-layout](artifact-layout/SKILL.md): private directories and file responsibilities.
- [review-records](review-records/SKILL.md): review reports and finding-linked decisions; needed when preparing or recovering records.

Keep guidance focused on this workflow's choices, not exhaustive policies or generic engineering instruction. Assess the complete reading path: moving restrictions into referenced files is not simplification.

## Installation

Register complete skill directories and their dependencies in the agent harness. Stages use `artifact-layout` and `review-records`; questions use `ask-with-context`; implementation uses `tdd` and `code-review`. Code reviewers read `tdd`'s TESTING.md directly. Resolve cross-skill resources through their registered owner and companion files relative to the installed skill. Reading a reference does not start its owner's workflow.

Ordinary directory copying is sufficient; no source symlinks or installation-manager-specific packaging is required. Installed skills need not be siblings. OMP supports `skill://<name>` and `skill://<name>/<resource>`; other harnesses use native discovery. Register `wayfinder`, `tdd` and `code-review` unambiguously alongside any upstream skills. This repository does not auto-install or change global instructions.

## Private artifacts and decisions

Use the locally excluded `.scratch/<work-slug>/` layout. `issue.md` defines and links the work; models hold the current specification; ticket blocks hold execution facts; object-specific logs preserve review and repair decisions.

Show specification changes and obtain confirmation before writing them. Authorized implementation proceeds autonomously within the approved design, including the bounded [Execution facts exception](implement-unit/IMPLEMENTATION.md#execution-facts-exception). Preserve the original implementer/reviewer pair through repairs and obtain final human approval or acceptance for the stage result. These approvals do not authorize publication of private artifacts.
