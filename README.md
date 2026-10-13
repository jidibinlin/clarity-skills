# Clarity Skills

Human-led requirements and technical design, bounded ticket planning, and implementation against approved models. Content standards guide construction and independent review; review is not a substitute for settling the design.

## Workflows

| Skill | Outcome | Content standard |
| --- | --- | --- |
| [wayfinder](wayfinder/SKILL.md) | Coarse decomposition guided by tentative topology, not technical approval | [WAYFINDER-MODEL.md](wayfinder/WAYFINDER-MODEL.md) |
| [clarify-requirements](clarify-requirements/SKILL.md) | Bounded requirements or a composed shared/child package | [REQUIREMENTS-MODEL.md](clarify-requirements/REQUIREMENTS-MODEL.md) |
| [clarify-architecture](clarify-architecture/SKILL.md) | Overall heavyweight architecture and shared guarantees | [ARCHITECTURE-MODEL.md](clarify-architecture/ARCHITECTURE-MODEL.md) |
| [clarify-technical-design](clarify-technical-design/SKILL.md) | Complete scoped files, topology, flows, data and contracts | [TECHNICAL-MODEL.md](clarify-technical-design/TECHNICAL-MODEL.md) |
| [clarify-change](clarify-change/SKILL.md) | Evidenced baseline and complete scoped change, including legacy projects | [CHANGE-MODEL.md](clarify-change/CHANGE-MODEL.md) |
| [split-tickets](split-tickets/SKILL.md) | Context-fit usable increments covering the approved target | [TICKETS.md](split-tickets/TICKETS.md) |
| [implement](implement/SKILL.md) | Whole ticket set or bounded direct change through human code acceptance | [ORCHESTRATION.md](implement/ORCHESTRATION.md) |
| [implement-unit](implement-unit/SKILL.md) | One ticket or full bounded direct change | [IMPLEMENTATION.md](implement-unit/IMPLEMENTATION.md) |

Lightweight: requirements → technical design → tickets → implementation. Heavyweight: Wayfinder → shared/child requirements → overall architecture → child technical designs → one root ticket set → implementation. A sufficiently bounded approved change may go directly to implementation. Stage approval permits downstream use; it does not start the next stage.

## Responsibilities and reading

- **Stage SKILL.md** owns its inputs, progression, retained author/reviewer loop and approval/stop gate.
- **Content standards** define the result's substantive completeness and quality. Read them before construction, not just before review.
- **Reviewer prompts** define the independent review task against those same standards.
- [artifact-layout](artifact-layout/SKILL.md) defines private directories, names and file responsibilities. [review-records](review-records/SKILL.md) defines admitted review/repair evidence and its format. Each is a reference-only skill whose SKILL.md contains the complete specification; neither starts a workflow.
- [ask-with-context](ask-with-context/SKILL.md) prepares decision-ready questions and continues open decisions; it also works outside these workflows.

Load reference skills by registered name through the harness. Authors read their complete content standard and `artifact-layout` before construction; load `review-records` when preparing review, repairing a finding or recovering existing records, not just to begin clarification. Reviewers read their prompt, content standard and `review-records` without importing the author workflow. Other content-standard references load their named owner's resource directly, not its execution prerequisites. Reuse complete current supplied content. Judge simplification by the applicable reading path and execution rules, not shorter entry files or repository-wide deduplication.

## Installation

Register complete skill directories and their declared dependencies in the agent harness. Every stage depends on `artifact-layout` and `review-records`; questioning additionally uses `ask-with-context`. Reference skills are resolved by their registered names, and stage-local companion files relative to their actual owner. OMP supports `skill://artifact-layout`, `skill://review-records` and `skill://<stage>/<resource>`; other harnesses use their native skill discovery/loading mechanism. Missing dependencies block affected work rather than authorizing guessed paths or automatic installation.

The reference skills each contain one self-contained SKILL.md. Ordinary directory copying is sufficient; no shared-resource symlinks, generated copies, special packaging step or installation-manager-specific layout is required. Installed skills need not be siblings or retain this repository's tree.

Keep installed instructions separate from the target checkout. This repository does not auto-install skills or change global instructions. Register this suite's `wayfinder` unambiguously rather than alongside the upstream namesake.

## Private artifacts

[artifact-layout](artifact-layout/SKILL.md) defines the excluded `.scratch/<work-slug>/` workspace. `issue.md` is definition/navigation, ticket metadata holds compact execution state, and object-specific logs follow [review-records](review-records/SKILL.md). Models remain clean specifications, not diaries; no separate state files or candidate sidecars.

Stage skills require an exact preview and explicit human confirmation for every specification write, including repairs and metadata. Code conformance repairs retain their execution authorization. Human acceptance grants no permission to publish, commit or delete private artifacts.

Example after installation:

> Use clarify-requirements for employee withdrawal of pending expense claims. Inspect existing behavior, use .scratch/claim-withdrawal/ after verifying exclusion, and stop at requirements approval.
