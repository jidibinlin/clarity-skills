# Custom Skills

## Shared workflow principle

Every stage uses one authoritative standard for both producing its work and reviewing it. This applies to requirements modeling, technical modeling, and subsequent planning, implementation, and change workflows. Authors apply the stage's standard throughout the work, not only before delivery; independent reviewers judge the result against those same criteria.

Write criteria that can guide concrete decisions and be checked against observable content or evidence. A standard is neither a table of contents nor a collection of aspirations such as "use a reasonable architecture." Preserve the context and rationale needed to apply a criterion.

Skills define the workflow; standards define the required quality; reviewer contracts define independent review inputs, responsibilities, and results. Reference the authoritative criteria rather than maintaining a separate, potentially conflicting author checklist or reviewer rulebook. Review summaries may index those criteria but must not add, weaken, or replace them.

## Private workflow workspace

Every entry point and reviewer loads the model-invoked [workflow-artifacts](workflow-artifacts/SKILL.md) reference skill and reads its companion [WORKFLOW-ARTIFACTS.md](workflow-artifacts/WORKFLOW-ARTIFACTS.md). The SKILL steps, not this README alone, enforce storage, transition recording, and handoff. The reference does not itself execute a stage or create project files.

Install complete skill directories through the harness and resolve dependencies by registered skill name, not their position in a source checkout or a shared installation parent. Same-skill companion links resolve from the owning installed skill/document. Cross-skill references use the Skill tool, or the harness's equivalent named mechanism; omp provides `skill://<name>` and `skill://<name>/<resource>`. A reference-only load reads the requested standard or reviewer contract without running that stage. Missing dependencies block affected work; installing one skill does not imply automatic dependency installation.

| Skill | Required reference dependencies |
| --- | --- |
| `workflow-artifacts` | None; install its complete directory. |
| `clarify-requirements` | `workflow-artifacts` |
| `clarify-technical-design` | `workflow-artifacts` |
| `clarify-change` | `workflow-artifacts`, `clarify-technical-design` for its design-content standard |
| `split-tickets` | `workflow-artifacts` |
| `implement` | `workflow-artifacts`, `implement-unit` for execution/review resources |
| `implement-unit` | `workflow-artifacts`; delegated execution is driven by a separately authorized `implement` controller |

Skill resources are read-only installation inputs; the target repository is the separate working/output root. Loading a global skill never means writing `.scratch` under the global configuration directory or changing the product working directory. Dispatches provide actual resolved resources (or complete current content), their owning skill identities, and the target checkout. Workflow handoffs name the next skill but do not install it, start it, or bypass its authorization gates.

All new workflow artifacts live in the repository-local `.scratch/<work-slug>/`, excluded through the actual local Git exclusion file located with `git rev-parse --git-path info/exclude`. Verify effective exclusion and absence of tracked workflow files before writing. Preserve existing rules; do not edit `.gitignore`, force-add, commit, publish, or automatically delete these materials. Existing authoritative project documentation stays at its owning location and is synchronized within approved scope. Git exclusion is not a packaging or upload security boundary.

`issue.md` is the work entry/recovery map and, when needed, ticket-set index. Models use `requirements.md`, `technical.md`, or `change.md`; tickets use `issues/<NN>-<slug>.md`. Clean specifications remain separate from `issue.log.md` and same-stem ticket `.log.md` files. Logs preserve review rounds, stable findings, repair decisions with necessary background/key rationale, actual verification, source/code identities, and approval evidence. Current states point to those records rather than becoming a diary.

Implementation produces a clean `delivery.md` after required verification and independent Pass, before requesting final human acceptance. It records delivered scope, final design references, consequential decisions, verification/limits, maintenance needs and acceptance state; it is not a chronological changelog. Delegated units return their records to the controller rather than claim whole-work delivery. All files, including the summary, remain local and excluded; only create artifacts needed by the route.

## Clarify Requirements

[clarify-requirements/SKILL.md](clarify-requirements/SKILL.md) is the entry point for the requirements stage of the lightweight workflow. It can also be called by a larger workflow with a bounded question and inherited constraints.

It investigates existing behavior, builds an understanding from concrete situations, and asks only questions whose answers materially affect the requirement. Relevant counterexamples test that understanding; an exhaustive decision tree or generic checklist does not drive the interview. A fully specified request can proceed to model review without clarification questions. The author maintains the model, dispatches a fresh independent reviewer for each full review, repairs findings, and repeats until the review passes, then waits for final human approval. It stops before technical design, implementation tickets, or production code.

The companion [delivery standard](clarify-requirements/REQUIREMENTS-MODEL.md) defines content and review requirements, including background-dependent explanations, decision rationale, concept relationships, Mermaid diagrams, and non-chronological organization. The entry point requires reading it before beginning work. The [reviewer contract](clarify-requirements/reviewer-prompt.md) defines a read-only role, its evidence package, and `Pass`, `Changes required`, or `Blocked`. Reviewers receive current sources and evidence without the author's working context. The controller persists each result in `issue.log.md` before advancing, never in the canonical model.

Produced models remain clean, integrated documents. Revisions update owning sections and remove superseded content; patch files, changelogs, revision logs and override addenda are prohibited in them. Private sidecar logs retain meaningful process evidence without relying on Git history or conversation memory.

### Use

Register or link the entire `clarify-requirements` directory and its required `workflow-artifacts` reference skill through the harness. These files have not been installed into any harness automatically. Keep both companion files with `SKILL.md`. The harness must provide a fresh independent reviewer context and access to the required inputs and verification evidence. The same model can perform both roles in separate contexts; switching roles in the author's conversation or relying on author self-review is not a substitute. If independence or required evidence is unavailable, the skill reports a blocker and retains `Draft`.

Then invoke `clarify-requirements` with a requirement, an existing model to resume, or a bounded question delegated by another workflow. For example:

> Use clarify-requirements to clarify employee withdrawal of pending expense claims. Read the existing claim behavior first. Use .scratch/claim-withdrawal/requirements.md after verifying local Git exclusion, and stop for my approval before technical clarification.

New requirements models use `.scratch/<work-slug>/requirements.md` under the shared workspace standard. Review the actual model, not just the closing message. Interview answers and approval of proposed fixes do not approve the finished document. Findings, missing independent review, or incomplete mandatory verification keep it in `Draft`; an independent `Pass` for the current artifact permits `Awaiting approval`; explicit final approval of that reviewed model permits `Approved`. Content changes return to a fresh full review. Resuming an approved model never skips independent review, but an unchanged model can retain its established final approval after passing.

## Clarify Technical Design

[clarify-technical-design/SKILL.md](clarify-technical-design/SKILL.md) is the next-stage entry point after the current requirements model has passed independent review and received final human approval. The skill itself requires reading and applying [TECHNICAL-MODEL.md](clarify-technical-design/TECHNICAL-MODEL.md) throughout authoring and repair and using that same standard for independent review; this README is not the execution gate.

Technical grilling and modeling form one loop: challenge candidate designs against concrete scenarios and inspected evidence, ask only consequential unresolved questions with grounded alternatives and a recommendation, wait for the necessary human choices, and integrate answers into the model. Macro choices precede dependent micro choices; contradictions found while modeling or reviewing return to the affected technical question. This is not an exhaustive decision-tree interview or a private design exercise followed by a request for approval.

The technical deliverable includes a complete file-responsibility tree, macro and micro topology and sequence diagrams, explicit data-flow and concurrency semantics, complete data definitions, complete interface contracts, and an [overall workflow integration test plan](clarify-technical-design/TECHNICAL-MODEL.md#overall-workflow-integration-test-plan). The skill first investigates the project's existing integration-test methods, then selects a small set of overall flows with meaningful observable outcomes. Detailed test strategies, unit and boundary cases, fixture implementation, and assertion code belong to the later implementation-stage TDD instructions, not this stage. The [technical reviewer contract](clarify-technical-design/reviewer-prompt.md) applies that same scope and standard during independent review.

Install the complete `clarify-technical-design` and `workflow-artifacts` skills through the harness; they have not been installed automatically and need not share a parent directory. Invoke technical clarification with the approved requirements model and any existing technical model. New technical output is `.scratch/<work-slug>/technical.md` in the same work directory. Independent `Pass` and final human approval are separate gates. Approval hands the model to subsequent ticket decomposition; this skill neither splits tickets nor implements production code.

The approved technical model also carries concrete first-pass implementation constraints and their rationale in the owning design sections. It is the basis for later code-conformance review, not a loose approach to be redesigned while coding or reviewing. Local expression choices remain with implementation only where they preserve those constraints.

## Clarify Change

[clarify-change/SKILL.md](clarify-change/SKILL.md) models scoped changes directly from an existing system, including projects with stale, partial, or absent prior documents. Its [CHANGE-MODEL.md](clarify-change/CHANGE-MODEL.md) is the shared authoring and independent-review standard and imports the technical model's design-content rules without imposing its historical input/approval prerequisites. Install the complete `clarify-change`, `workflow-artifacts`, and `clarify-technical-design` skills. Load the technical skill by name in reference-only mode for its requested content standard, not to start the original technical workflow. None has been installed automatically.

The workflow reconstructs affected current behavior from evidence, distinguishes observed behavior from confirmed requirements and unknowns, and clarifies changed/preserved outcomes with the technical consequences. Every macro/micro topology, flow, concurrency, sequence, file-organization and data/interface dimension has an explicit Changed/Unchanged/Unresolved assessment and a complete scoped target or verified reference. Missing documents do not justify missing design, and legacy bugs are not automatically requirements.

Changed canonical requirements/technical sections are integrated and reviewed with the change model as one package; no amendment chain or fabricated historical approval is required. Without old models, the change package supplies the complete scoped basis. A [fresh independent model reviewer](clarify-change/reviewer-prompt.md) checks the whole current package after every repair, followed by explicit human approval. This model gate is distinct from retained implementation-role review loops.

A bounded approved change goes directly to `implement` without a ticket or ticket-set index; its `issue.md` remains the work entry. A change needing decomposition uses `split-tickets` with the same approved basis. Both retain runtime/macro verification and final human implementation acceptance. New change models use `.scratch/<work-slug>/change.md`; all reviews, decisions and approvals follow the shared private-record standard.

## Split Tickets

[split-tickets/SKILL.md](split-tickets/SKILL.md) decomposes an approved requirements/technical basis or an approved change package when multiple bounded units are necessary. It requires [TICKETS.md](split-tickets/TICKETS.md) as the shared authoring and review standard. Ticket size includes understanding, code reading, implementation, verification and repair, not just prose length or a fixed token limit. A bounded direct change bypasses this stage rather than receiving a synthetic ticket.

Split the work, not the approved production structure. Each ticket has a coherent result, precise source/code references, concrete prerequisites, and meaningful completion evidence. It need not finish the whole macro flow, but the complete set must own the integration and macro-flow verification required before release or handoff to joint integration. Detailed test strategies remain with the later implementation-stage TDD instructions.

The output is the work directory's `issue.md` as the set index plus `issues/<NN>-<slug>.md` per ticket. The index records the source baseline, ticket map, coverage and dependencies. The [reviewer contract](split-tickets/reviewer-prompt.md) requires a fresh independent review of the entire set, repair and full re-review, then separate final human approval. Set approval does not execute tickets or satisfy their individual blockers. Planning reviews and approval evidence persist in `issue.log.md`.

Install the entire `split-tickets` directory and required `workflow-artifacts` skill through the harness; neither is installed automatically. Invoke it with the approved source package and any existing ticket set. Change-derived tickets cite the change requirements, complete target design and synchronized affected canonical references, without requiring absent historical models. The skill stops after its own set review and human approval; it does not implement or publish issues.

## Implement

[implement/SKILL.md](implement/SKILL.md) executes an authorized approved ticket set or one bounded approved change directly. [ORCHESTRATION.md](implement/ORCHESTRATION.md) governs coordination, actual prerequisites, shared code basis, evidence validity and final acceptance. Its execution/review dependency is the named `implement-unit` skill, whose [IMPLEMENTATION.md](implement-unit/IMPLEMENTATION.md) is the common standard. Install complete `implement`, `implement-unit`, and `workflow-artifacts` skills through the harness. Load unit resources in reference-only mode for orchestration; dispatch authorized delegated execution separately with actual resolved resource locations. Source-browser links here are navigation, not installed-directory assumptions.

Execution is serial by default. Each unit has its original implementer and independent reviewer retained through automatic repair/re-review until the current result passes. Ticket sets use separate bounded pairs per ticket; a direct change uses one pair for the complete approved change. Later messages carry changed code, finding dispositions and renewed evidence. Role loss requires explicit handoff rather than erased findings. The controller preserves real prerequisites and user work and does not ask for per-unit human confirmation.

Ticket sets require final combined regression/macro-flow evidence and the [overall reviewer](implement/reviewer-prompt.md); local Passes do not prove composition. Direct changes place all final combined evidence and target coverage in their original unit reviewer's full-change Pass, with no duplicate overall review. Both routes end with explicit human acceptance of the current reviewed implementation. No automatic commit, merge, push, remote issue closure or release is implied. New change-design decisions return to `clarify-change`.

## Implement Unit

[implement-unit/SKILL.md](implement-unit/SKILL.md) executes one ticket or one entire bounded approved change, standalone or delegated by the named `implement` controller. Its [IMPLEMENTATION.md](implement-unit/IMPLEMENTATION.md) is the common execution/review standard. Direct identity is the change document path and revision; it needs no ticket, ticket-set index, old separate model or historical approval when the approved current change package supplies the complete basis. Standalone use needs the complete `implement-unit` and `workflow-artifacts` skills; delegated orchestration additionally needs the separately authorized `implement` controller, not a guessed sibling path.

Implementation follows approved ownership, contracts, collaboration and cutover from the first pass, without a rough-code-then-refactor phase. TDD uses useful behavior checks and existing facilities, not extra production abstractions for mocking. Runtime verification exercises the actual changed surface, and direct changes own every required macro flow immediately rather than deferring it to an imaginary ticket.

The original implementer repairs findings and the original [independent reviewer](implement-unit/reviewer-prompt.md) reassesses the full current scope until Pass. Retained context does not preserve stale approval. A delegated Pass returns to the controller without a per-unit human gate; standalone invocation requests human acceptance of its explicitly scoped reviewed result. Requirements, technical, change-model and ticket-plan authoring retain fresh-reviewer-per-round gates. All roles apply the shared workspace/record standard; implementation summaries do not replace persistent repair evidence.
