# Clarity Skills

## Workflow and standards

These skills turn bounded requirements, scoped changes, or large efforts into reviewed models and conforming implementation. Each stage reads its complete applicable standard before investigation and generation. The standard guides the author and the independent reviewer; review does not finish an intentionally incomplete design.

The executable rules live in the skills, not this README:

- **SKILL.md:** entry conditions, ordered work, branches, pre-review checks, and handoff/stop gates.
- **Stage standard:** substantive quality, completeness, and evidence requirements.
- **Reviewer contract:** independent role, inputs, assessment, and return contract against that same standard.
- **workflow-artifacts:** shared resource loading, private workspace, durable records, source identity, and delivery summaries.

## Shared questioning

[ask-with-context](ask-with-context/SKILL.md) is a self-contained communication skill with a mandatory per-question protocol. Background-dependent decisions visibly connect context and impact, genuine options and tradeoffs, and the exact decision needed, using focused diagrams, comparable tables, or prose. Simple factual questions remain concise. After each answer, its continuation loop advances remaining material decisions rather than ending at an acknowledgement. It introduces no artifact layout or approval process and can be used outside engineering workflows. The five clarification stages require its pre-send check for initial questions, follow-ups, resumed work, and repairs; their scope and gates remain authoritative.

Its model-facing description permits discovery after registration; it does not guarantee always-on activation. Explicit caller references provide the suite-level requirement. This repository does not install it, change global instructions, or enable it by default in the harness.

## Entry points

| Skill | Authorized work | Governing standard | Reviewer contract |
| --- | --- | --- | --- |
| [wayfinder](wayfinder/SKILL.md) | Explore and coarsely split a large requirement; tentative topology tests the split, not a technical approval. | [WAYFINDER-MODEL.md](wayfinder/WAYFINDER-MODEL.md) | [Map review](wayfinder/reviewer-prompt.md) |
| [clarify-requirements](clarify-requirements/SKILL.md) | Clarify a bounded requirement or shared/child requirement package; stop at final model approval. | [REQUIREMENTS-MODEL.md](clarify-requirements/REQUIREMENTS-MODEL.md) | [Model review](clarify-requirements/reviewer-prompt.md) |
| [clarify-architecture](clarify-architecture/SKILL.md) | Establish formal overall architecture from clarified approved requirements before child technical designs. | [ARCHITECTURE-MODEL.md](clarify-architecture/ARCHITECTURE-MODEL.md) | [Architecture review](clarify-architecture/reviewer-prompt.md) |
| [clarify-technical-design](clarify-technical-design/SKILL.md) | Realize an approved requirements model as a complete scoped technical design. | [TECHNICAL-MODEL.md](clarify-technical-design/TECHNICAL-MODEL.md) | [Technical review](clarify-technical-design/reviewer-prompt.md) |
| [clarify-change](clarify-change/SKILL.md) | Reconstruct an existing system's affected baseline and decide a scoped target, including when historical models are absent/stale. | [CHANGE-MODEL.md](clarify-change/CHANGE-MODEL.md) | [Change-package review](clarify-change/reviewer-prompt.md) |
| [split-tickets](split-tickets/SKILL.md) | Decompose an approved source package into bounded, meaningful implementation units without redesigning production structure. | [TICKETS.md](split-tickets/TICKETS.md) | [Whole-set review](split-tickets/reviewer-prompt.md) |
| [implement](implement/SKILL.md) | Coordinate an authorized ticket set or one bounded approved change through final human acceptance. | [ORCHESTRATION.md](implement/ORCHESTRATION.md), plus the unit standard | [Overall ticket-set review](implement/reviewer-prompt.md) |
| [implement-unit](implement-unit/SKILL.md) | Implement one ticket or an entire bounded approved change, standalone or delegated. | [IMPLEMENTATION.md](implement-unit/IMPLEMENTATION.md) | [Unit/full-change review](implement-unit/reviewer-prompt.md) |

The lightweight initial route remains requirements modeling, technical modeling, ticket planning, then implementation. The heavyweight route adds `wayfinder` before shared/child requirements clarification, and `clarify-architecture` before child technical designs; approved designs feed one root ticket set and implementation controller. A child requirement is a modeling scope, not a module, ticket, or separate controller. Stage approval and execution authorization remain distinct.

Scoped changes use `clarify-change`: its approved package can go directly to `implement` if bounded, or through `split-tickets` when decomposition is needed. It assesses affected shared requirements, architecture, child models and downstream evidence when present, without inventing missing historical models or approvals. Direct changes create no synthetic ticket or state artifact; `issue.md` defines and links the work, while change modeling and implementation retain separate review records.

Technical, architecture and scoped-change modeling converge with the human through bounded concrete design groups at each stage’s authorized resolution. Show actual topology/sequence diagrams, data declarations and other relevant views, resolve the response, then refine dependent groups; do not complete the whole blueprint after a direction interview and ask only once at the end, even under a Draft label. Partial agreement closes only its stated scope, and changed premises reopen only affected choices. Applicable concrete confirmations and inspected unchanged reuse avoid repeat questions. Authors and independent reviewers apply **Progressive design convergence** in TECHNICAL-MODEL.md, including its mandatory declaration clarification, without adding a confirmation or state artifact.

The technical questioning baseline is macro-first: converge top-down on topology, boundaries and needed solution directions, then design micro capabilities bottom-up by module dependencies. Start with the configuration, stored/state definitions, interfaces and basic flows that actual consumers need. Data-first is a default, not a rigid pass order; choose sequence-first or a joint group when it resolves prerequisite uncertainty. This governs design decisions, not implementation or ticket ordering.

Every reviewed object retains its original author/repair owner and independent reviewer through repairs, re-review, final full-scope assessment and human revisions under WORKFLOW-ARTIFACTS.md’s **Persistent author/reviewer lifecycle**. First assignments receive complete inputs; later messages refresh changed inputs without narrowing review criteria. Persist resumable bindings in existing object review-log headers or implementation-ticket metadata; replace only genuinely lost roles through the shared recovery/handoff procedure. Composite and overall findings return to their original owning authors, not a new catch-all fixer.

Delegated units have no per-ticket human acceptance gate. Ticket sets need combined verification and a retained overall independent reviewer; a direct change’s full-scope unit Pass is its final independent review, without another reviewer. Neither review Pass nor model approval is final human acceptance of code.

## Installation and resource access

Register complete skill directories through the harness. They have not been installed automatically by this repository. Keep companion files with their owning SKILL.md and install the declared reference dependencies:

| Skill | Required reference dependencies |
| --- | --- |
| `workflow-artifacts` | None outside its own directory. |
| `ask-with-context` | None outside its own directory. |
| `wayfinder` | `workflow-artifacts`; `ask-with-context` before substantive questions |
| `clarify-requirements` | `workflow-artifacts`; `ask-with-context` before substantive questions |
| `clarify-architecture` | `workflow-artifacts`, `clarify-technical-design` for applicable design-content rules; `ask-with-context` before substantive questions |
| `clarify-technical-design` | `workflow-artifacts`; `ask-with-context` before substantive questions; heavyweight child design also loads `clarify-architecture` reference-only |
| `clarify-change` | `workflow-artifacts`, `clarify-technical-design` for design-content rules; `ask-with-context` before substantive questions; `clarify-architecture` or `wayfinder` reference-only when their existing authorities are affected |
| `split-tickets` | `workflow-artifacts` |
| `implement` | `workflow-artifacts`, `implement-unit` |
| `implement-unit` | `workflow-artifacts`; delegated use has a separately authorized `implement` controller |

Cross-skill resources use registered names, not installation-directory adjacency. See [workflow-artifacts/SKILL.md](workflow-artifacts/SKILL.md) for the Skill tool/omp mechanisms, owner-relative links, supplied-content reuse, missing-dependency handling, and reference-only loading. Reference-only access does not execute another stage. Skill resources are read-only; the target checkout remains the separate working/output root. Source links in this README are navigation, not installed-path assumptions. Register this suite's `wayfinder` unambiguously: it replaces, rather than co-registers with, the upstream skill of the same name.

## Private work and invocation

Every role reads [WORKFLOW-ARTIFACTS.md](workflow-artifacts/WORKFLOW-ARTIFACTS.md). New work lives under repository-local `.scratch/<work-slug>/`, after the author/controller establishes and verifies local Git exclusion. Its heavyweight layout adds root map/shared-requirements/architecture models and scoped `requirements/NN-<slug>/` modeling entries; implementation tickets and final delivery remain at the root. The shared standard owns the exact tree, hierarchical source identities, record ownership, and cross-layer handoffs. Existing authoritative project models can remain precisely referenced at their owning locations.

`issue.md` contains only work definition/navigation and, when applicable, the ticket-set specification/index—not progress or an approval registry. Unresolved decisions and settled answers belong in their canonical model sections. Implementation progress belongs in the existing ticket’s compact execution metadata; no separate state files, duplicate execution checklists, or global status ledger are created. Each reviewed object uses `<object>.review-fix-decisions.log.md` for submissions/outcomes, finding-linked repair decisions/evidence, and corresponding human approvals. Consumers resolve approvals through the owning models and review records. Direct work resumes from its approved change, actual code, and review evidence, without a synthetic ticket. Significant autonomous repair decisions must be visible at handoff. Existing mixed records undergo classification-based cutover, not wholesale renaming or history deletion. All artifacts stay local and excluded unless publication is separately authorized.

Example invocation after installation:

> Use clarify-requirements to clarify employee withdrawal of pending expense claims. Inspect existing behavior first, use .scratch/claim-withdrawal/ after verifying local Git exclusion, and stop for my approval before technical clarification.

Review the actual artifact, not only the closing message. If required inputs, independent contexts, or verification are unavailable, the skill must report the specific blocker rather than claim completion.
