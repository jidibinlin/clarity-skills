---
name: clarify-technical-design
description: Use after a requirements/domain model has passed independent review and received final human approval, to clarify and model its technical realization, or to resume an existing technical model. Also load reference-only when another stage or reviewer needs its technical standard. Not for requirements discovery, ticket decomposition, or production implementation.
---

# Clarify Technical Design

Interrogate the proposed technical realization of an approved requirements model and turn the clarified decisions into a complete technical model whose implementation does not require further design decisions. Technical grilling and modeling are one iterative process, not a private design exercise followed by a request for approval. Stop at the technical-model approval gate. Do not create implementation tickets or production code.

## Entry mode and dependencies

For reference-only use, read the requested standard or reviewer contract and its required dependencies, then return to the consuming stage. Do not start the approved-requirements prerequisite check, investigation, questions, artifact creation, reviewer dispatch, or approval workflow below. Reading an exported standard does not require an approved requirements model; executing this technical-modeling stage still does.

Load the complete named dependency `workflow-artifacts` and read its entire `WORKFLOW-ARTIFACTS.md` before every role starts or resumes. Follow that skill's loading, supplied-content reuse, missing-dependency blocking, reference-only, and root-separation rules. Before investigation, questions, or drafting, read [TECHNICAL-MODEL.md](TECHNICAL-MODEL.md); apply these standards throughout authoring, repair, and review.

Stage routes name separately installed complete skills: `clarify-requirements` for unresolved requirements, `split-tickets` for authorized subsequent decomposition, and `clarify-change` for an authorized scoped-change route. Load a routed skill by name for execution only when that stage is authorized; loading a reference or approving this stage does not execute another stage.

The required views and completeness bar are defined in TECHNICAL-MODEL.md. Settle the scoped production design before coding; a plausible approach with design decisions left to implementation is not a complete model.

## 1. Establish the approved input and inspect the actual system

Read the current requirements model, its essential references, and evidence of its passing review and final human approval. Identify the exact approved content being realized. An approval label alone is not evidence of these conditions. If the input is missing, changed since approval, or still unresolved, report the specific prerequisite and return it to requirements clarification; do not invent requirements to proceed.

Use the already-read TECHNICAL-MODEL.md as the authoring contract for investigation, technical grilling, and each draft, not only later review. Inspect the relevant repository guidance, existing processes, modules, objects, types, interfaces, callers, and tests. Follow the behavior across actual runtime and code boundaries. Establish what can be reused and what must change before proposing new abstractions. Keep inspected facts, proposed changes, and imposed constraints distinct. If essential evidence is inaccessible, preserve the gap as a blocker rather than assuming the existing design.

Investigate the project testing means under **Overall workflow integration test plan** in TECHNICAL-MODEL.md before selecting flows in step 3.

As author/controller, reuse the requirements work’s `.scratch/<work-slug>/` and establish its verified workspace under WORKFLOW-ARTIFACTS.md before writing. New technical models use `technical.md`, with the same `issue.md` and `issue.log.md`; apply the shared location rule to existing canonical models. Reference the approved requirements path/revision and persist substantive conclusions as `Draft`. On resumption perform the shared recovery procedure. Planning creates no `delivery.md`.

## 2. Grill the technical design, not the human for repository facts

Challenge both the human's proposed approach and your own. Start from an approved concrete scenario, inspected existing behavior, and a candidate design. Identify the unresolved decision or contradiction that could change the resulting structure or behavior. Use TECHNICAL-MODEL.md to expose missing decisions, not as a questionnaire to read aloud. An exhaustive decision tree, generic infrastructure checklist, or request to choose every name is not technical grilling.

**Work from macro choices to their micro consequences.** First test runtime boundaries, collaboration, state authority, data movement, ordering, and concurrency. Then test whether concrete objects, file assignments, data definitions, and contracts can realize those choices. Do not settle a dependent interface or object split while the upstream choice remains open. Independent questions may be grouped in a small round; questions whose answers depend on another answer must wait.

**Make each question reviewable.** Give the relevant inspected fact or approved constraint, the specific uncertainty or counterexample, the viable alternatives and their actual consequences, and your recommendation with its basis. Ask for the unresolved choice, not general feedback on a finished design. State which file responsibilities, interactions, types, or contracts the answer will affect. Do not manufacture alternatives when the issue is a missing fact or a direct contradiction.

Resolve accessible facts yourself. Reuse already confirmed choices and established conventions where they settle the issue. Ask only when materially different viable designs remain and the choice needs the human's preference or authority, or a missing human constraint changes the answer. Wait for that answer before treating your recommendation as a decision. Do not infer confirmation from silence or finish the dependent design under an unapproved assumption. Missing repository access is a blocker, not a question asking the human to invent system facts.

**Stress-test with consequential counterexamples.** Trace an actual approved scenario through the candidate design: can two execution contexts update the same state, does ownership survive a boundary crossing, does an operation's stated result match its completion point, or does one rule require edits across unrelated objects and files? Use only cases relevant to this change. A counterexample that contradicts the approved requirement requires a design correction, not a question about whether to permit the contradiction. If several compliant corrections have consequential tradeoffs, present that real choice. Check whether a new abstraction is necessary, whether an existing one already serves its purpose, and whether its introduction leaves redundant responsibilities behind.

**Model while grilling.** Steps 2 and 3 form a loop. Use draft topology, sequences, file assignments, and declarations to make choices concrete, and update their owning sections after each clarification. Mark tentative designs and unresolved choices explicitly. Preserve the answer and its actual rationale in the integrated model, not an interview log. A new contradiction found while detailing objects or contracts returns to the affected technical question; do not silently change an earlier decision.

Use targeted, disposable investigation when existing evidence cannot establish a necessary feasibility fact. Report what was actually exercised; do not invent results or make exploratory code part of production. If a technical issue exposes an undecided or conflicting business rule, return it to requirements clarification instead of deciding it here. Refresh the input after that requirement completes its own review and approval gate.

**Completion criterion:** every production-design choice needed for the scoped realization is resolved from evidence, an applicable established decision, or the human's answer; consequential counterexamples are addressed; and those decisions and their basis are captured in the model. No production-design decision is reserved for coding. The testing deliverable is limited to the overall workflow plan described below; detailed testing remains with the later TDD stage. A fully specified input can need no new human questions, but it still undergoes this technical challenge and the complete modeling, verification, and independent review steps. Answers during grilling are not final approval of the finished technical model.

## 3. Model runtime collaboration, then its concrete realization

Build the macro collaboration first, then its concrete micro realization using TECHNICAL-MODEL.md. Connect both levels to the scoped file-responsibility tree, complete definitions, and contracts. Walk approved scenarios through the views; if the micro design cannot satisfy a macro guarantee, revisit that decision rather than preserve contradictory views.

Apply the standard's first-pass implementation constraints in their owning sections. Resolve consequential quality choices now; distinguish permissible local expression choices from design changes requiring renewed approval.

Using the project evidence from step 1, produce the plan required by **Overall workflow integration test plan** in TECHNICAL-MODEL.md. Clarify any necessary capability gap; leave detailed testing/TDD to implementation.

## 4. Integrate and verify the complete model

Integrate conclusions in the canonical model under TECHNICAL-MODEL.md. As controller, maintain `issue.md` and persist process records and recovery state in `issue.log.md` under WORKFLOW-ARTIFACTS.md before blockers or handoffs.

Complete all standard-mandated current design checks, including rendering and visually inspecting every Mermaid diagram. Parsing alone is insufficient. Check the declarations, referenced definitions, repository integration, scenario traces, and whether the selected overall workflow tests are grounded in the project's actual testing methods. Perform feasibility checks needed to support the production design's execution assumptions. Distinguish planned flow tests from existing checks or disposable probes actually run. Do not implement a permanent test suite or demand a complete test matrix here. Keep current verification evidence tied to the content; if a mandatory current check cannot be performed, report the blocker and retain `Draft`.

Do not advance while a production-design choice is deferred to implementation, a required definition or diagram is incomplete, or the views disagree. The implementer must be able to translate the settled system design into code, not finish designing it. The document defines the target structure, behavior, and limited overall workflow test plan, not a chronological implementation plan, exhaustive test strategy, or ticket list.

## 5. Obtain an independent review and repair until passing

Dispatch a fresh independent, read-only reviewer every round using [reviewer-prompt.md](reviewer-prompt.md) and its complete input contract. Missing independence, input, or mandatory verification keeps `Draft`; self-review cannot substitute.

As controller (author in standalone mode), save every returned review in `issue.log.md` before repair or advancement, following the shared record and finding-lifecycle rules. Request correction of stale, incomplete, or inconsistent reports.

For `Changes required`, repair the canonical model and dependent views/evidence; recover settled answers first and return unresolved tradeoffs to grilling. For `Blocked`, obtain missing inputs or verification. Persist repairs and fresh evidence before dispatching another fresh **full-model** review of all criteria, prior findings, and regressions. Save its disposition and update `issue.md` before advancing. Only a current independent `Pass` with all applicable criteria satisfied, mandatory verification complete, and no unresolved finding or blocker permits step 6. Repeated attempts do not waive the gate.

Verify that the artifact, approved requirements, and necessary references still match what was reviewed. Changes invalidate the result and return the document to `Draft`; approval-metadata updates alone do not invalidate content review. On resumption, always run this review before an approved handoff, even if the model is labeled `Approved`.

## 6. Obtain final human approval and stop

Only after the current model independently passes, set `Awaiting approval`. Present the document path, passing conclusion, macro and micro design, selected overall flow tests and existing project methods, and consequential decisions. Ask whether the human approves this reviewed technical model for subsequent ticket decomposition.

Wait for explicit approval of that current artifact. Agreement with earlier choices, approval of a proposed repair, or approval before the independent review passed is not final approval. Requested changes return to clarification as needed, integrated repair, fresh full review, and renewed final approval.

Set `Approved` only when both gates hold for the same current artifact. Persist human approval in `issue.log.md` and link current model metadata and `issue.md` using WORKFLOW-ARTIFACTS.md. An unchanged resumed model may retain evidenced final approval after current review; a label alone is insufficient.

Return `issue.md`, the approved technical model path/revision, its approved requirements input, and essential references. If blocked, return the draft and persisted blocker, not an approved handoff. Stop before ticket decomposition, implementation, or `delivery.md`. For subsequent scoped system changes, `clarify-change` (load by name only when that stage is authorized) combines evidenced baseline reconstruction, requirements/technical decisions, canonical updates and its own review/approval gate. It retains technical rigor without demanding absent historical documents or mandatory tickets for a bounded change.
