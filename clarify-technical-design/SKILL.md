---
name: clarify-technical-design
description: Use after a requirements/domain model has passed independent review and received final human approval, to clarify and model its technical realization, or to resume an existing technical model. Not for requirements discovery, ticket decomposition, or production implementation.
---

# Clarify Technical Design

Interrogate the proposed technical realization of an approved requirements model and turn the clarified decisions into a complete technical model whose implementation does not require further design decisions. Technical grilling and modeling are one iterative process, not a private design exercise followed by a request for approval. Stop at the technical-model approval gate. Do not create implementation tickets or production code.

Before investigation, questions, or writing, read [TECHNICAL-MODEL.md](TECHNICAL-MODEL.md). It is the single authoritative standard for both producing this model and independently reviewing it. Apply the entire standard throughout investigation, clarification, modeling, and repair, not just before delivery. Give the reviewer this same standard; do not replace it with a separate or weaker checklist. This skill is self-contained; install its entire directory, including both companion files.

**Required deliverable:** a complete file-responsibility tree; macro topology and sequence diagrams with data flow and concurrency semantics; micro topology and sequence diagrams; complete data-structure definitions; and complete interface contracts. Settle the technical decisions connecting them. A plausible implementation approach or a promise to decide the details while coding is not a completed technical model.

## 1. Establish the approved input and inspect the actual system

Read the current requirements model, its essential references, and evidence of its passing review and final human approval. Identify the exact approved content being realized. An approval label alone is not evidence of these conditions. If the input is missing, changed since approval, or still unresolved, report the specific prerequisite and return it to requirements clarification; do not invent requirements to proceed.

Inspect the relevant repository guidance, existing processes, modules, objects, types, interfaces, callers, and tests. Follow the behavior across actual runtime and code boundaries. Establish what can be reused and what must change before proposing new abstractions. Keep inspected facts, proposed changes, and imposed constraints distinct. If essential evidence is inaccessible, preserve the gap as a blocker rather than assuming the existing design.

Choose one canonical technical document. Use the supplied path or established project convention; otherwise use `docs/technical/<short-name>.md`. Maintain an existing model for the same change instead of creating another account. Reference the approved requirements model explicitly. Persist substantive conclusions as they emerge, initially with status `Draft`.

## 2. Grill the technical design, not the human for repository facts

Challenge both the human's proposed approach and your own. Start from an approved concrete scenario, inspected existing behavior, and a candidate design. Identify the unresolved decision or contradiction that could change the resulting structure or behavior. Use TECHNICAL-MODEL.md to expose missing decisions, not as a questionnaire to read aloud. An exhaustive decision tree, generic infrastructure checklist, or request to choose every name is not technical grilling.

**Work from macro choices to their micro consequences.** First test runtime boundaries, collaboration, state authority, data movement, ordering, and concurrency. Then test whether concrete objects, file assignments, data definitions, and contracts can realize those choices. Do not settle a dependent interface or object split while the upstream choice remains open. Independent questions may be grouped in a small round; questions whose answers depend on another answer must wait.

**Make each question reviewable.** Give the relevant inspected fact or approved constraint, the specific uncertainty or counterexample, the viable alternatives and their actual consequences, and your recommendation with its basis. Ask for the unresolved choice, not general feedback on a finished design. State which file responsibilities, interactions, types, or contracts the answer will affect. Do not manufacture alternatives when the issue is a missing fact or a direct contradiction.

Resolve accessible facts yourself. Reuse already confirmed choices and established conventions where they settle the issue. Ask only when materially different viable designs remain and the choice needs the human's preference or authority, or a missing human constraint changes the answer. Wait for that answer before treating your recommendation as a decision. Do not infer confirmation from silence or finish the dependent design under an unapproved assumption. Missing repository access is a blocker, not a question asking the human to invent system facts.

**Stress-test with consequential counterexamples.** Trace an actual approved scenario through the candidate design: can two execution contexts update the same state, does ownership survive a boundary crossing, does an operation's stated result match its completion point, or does one rule require edits across unrelated objects and files? Use only cases relevant to this change. A counterexample that contradicts the approved requirement requires a design correction, not a question about whether to permit the contradiction. If several compliant corrections have consequential tradeoffs, present that real choice. Check whether a new abstraction is necessary, whether an existing one already serves its purpose, and whether its introduction leaves redundant responsibilities behind.

**Model while grilling.** Steps 2 and 3 form a loop. Use draft topology, sequences, file assignments, and declarations to make choices concrete, and update their owning sections after each clarification. Mark tentative designs and unresolved choices explicitly. Preserve the answer and its actual rationale in the integrated model, not an interview log. A new contradiction found while detailing objects or contracts returns to the affected technical question; do not silently change an earlier decision.

Use targeted, disposable investigation when existing evidence cannot establish a necessary feasibility fact. Report what was actually exercised; do not invent results or make exploratory code part of production. If a technical issue exposes an undecided or conflicting business rule, return it to requirements clarification instead of deciding it here. Refresh the input after that requirement completes its own review and approval gate.

**Completion criterion:** every technical choice needed for the scoped realization is resolved from evidence, an applicable established decision, or the human's answer; consequential counterexamples are addressed; and those decisions and their basis are captured in the model. No technical decision is reserved for coding. A fully specified input can need no new human questions, but it still undergoes this technical challenge and the complete modeling, verification, and independent review steps. Answers during grilling are not final approval of the finished technical model.

## 3. Model runtime collaboration, then its concrete realization

Build the macro model first: participating processes and modules, responsibility and communication boundaries, data direction and state authority, ordering, and concurrency. Produce complete macro topology and sequence diagrams for the scoped behavior. A single-process design still needs an explicit macro view; do not invent extra processes to fill it.

Translate that model into the micro design: concrete objects, state ownership, dependencies, collaboration sequences, exact data definitions, and exact interface contracts. Produce complete micro topology and sequence diagrams. Map each responsibility and definition to its actual file in the target file tree. An unnamed helper, a generic layer label, or an undefined payload cannot hide an unresolved design decision.

Use the detailed coverage and completeness rules in TECHNICAL-MODEL.md. Include the technical decisions behind algorithms, representations, object creation and lifetime, coordination, and failure behavior where the scoped implementation needs them. Reuse exact existing definitions by accessible, identified reference; do not duplicate or casually redefine them. If a new abstraction is needed, explain why the existing one cannot carry the responsibility and what old structure it replaces, if any.

Walk every approved scenario through both levels. Show that actual object interactions, data structures, and interfaces realize the macro behavior, including its concurrency guarantees. Revisit the macro model when the concrete design cannot satisfy it; do not preserve contradictory views.

## 4. Integrate and verify the complete model

Maintain one clean explanation of the intended final structure. Update the owning sections, diagrams, definitions, and file tree together. Remove superseded designs. Do not add patches, changelogs, revision histories, override addenda, interview logs, or cleanup commentary to the deliverable; keep maintenance discussion in the conversation and history in version control.

Complete all standard-mandated checks, including rendering and visually inspecting every Mermaid diagram. Parsing alone is insufficient. Check the actual declarations, referenced definitions, repository integration, and scenario traces; perform the feasibility checks needed to support the design's execution assumptions. Keep evidence tied to the current content. If a required check cannot be performed, report the blocker and retain `Draft`.

Do not advance while a technical choice is deferred to implementation, a required definition or diagram is incomplete, or the views disagree. The implementer must be able to translate the settled design into code, not finish designing it. The document defines the target structure and behavior, not a chronological implementation plan or ticket list.

## 5. Obtain an independent review and repair until passing

Read [reviewer-prompt.md](reviewer-prompt.md) and dispatch a fresh, read-only reviewer context for every round. Supply the complete current artifact and required references, this same TECHNICAL-MODEL.md, approved requirements and source evidence, relevant inspected repository evidence, current verification artifacts, and any previous findings. Keep this package in the task input, not in an additional deliverable. Do not pass the author's working conversation or private reasoning, or instructions to endorse the design. The same underlying model may review; a role switch in the author's conversation is not independence.

The reviewer reports; you own repairs and human interaction. Require the exact reviewed snapshot and a complete `Pass`, `Changes required`, or `Blocked` result under the reviewer contract. A stale, incomplete, or internally inconsistent response is not a pass. If an independent reviewer or necessary input is unavailable, retain `Draft` and report what is needed; do not substitute author self-review.

For `Changes required`, repair the canonical model and all affected views and evidence. If a finding exposes an unresolved technical tradeoff or invalidates a settled choice, return to the technical-grilling loop before selecting a repair; recover facts and settled answers from existing sources first. For `Blocked`, obtain the missing input or verification. Then dispatch a fresh full review, not merely a review of the fix. Repeat until an independent `Pass` establishes that every applicable criterion is satisfied and no finding or blocker remains. If progress stalls, surface the unresolved decision or access requirement; exhausting review attempts does not waive the standard.

Verify that the artifact, approved requirements, and necessary references still match what was reviewed. Changes invalidate the result and return the document to `Draft`; approval-metadata updates alone do not invalidate content review. On resumption, always run this review before an approved handoff, even if the model is labeled `Approved`.

## 6. Obtain final human approval and stop

Only after the current model independently passes, set `Awaiting approval`. Present the document path, passing conclusion, macro and micro design, and consequential decisions. Ask whether the human approves this reviewed technical model for subsequent ticket decomposition.

Wait for explicit approval of that current artifact. Agreement with earlier choices, approval of a proposed repair, or approval before the independent review passed is not final approval. Requested changes return to clarification as needed, integrated repair, fresh full review, and renewed final approval.

Set `Approved` only when both gates are satisfied for the same current artifact. An unchanged resumed model may retain its established final approval after passing the current review; a status label alone is insufficient. Keep only the current status and applicable approval note, not approval history.

Return the approved technical model, its approved requirements input, and essential references. If blocked, return the draft and specific blocker as a progress report, not an approved handoff. Ticket decomposition is a separate subsequent workflow: do not split tickets or begin implementation here. This skill does not define the later post-implementation change-governance process.
