# Custom Skills

## Shared workflow principle

Every stage uses one authoritative standard for both producing its work and reviewing it. This applies to requirements modeling, technical modeling, and subsequent planning, implementation, and change workflows. Authors apply the stage's standard throughout the work, not only before delivery; independent reviewers judge the result against those same criteria.

Write criteria that can guide concrete decisions and be checked against observable content or evidence. A standard is neither a table of contents nor a collection of aspirations such as "use a reasonable architecture." Preserve the context and rationale needed to apply a criterion.

Skills define the workflow; standards define the required quality; reviewer contracts define independent review inputs, responsibilities, and results. Reference the authoritative criteria rather than maintaining a separate, potentially conflicting author checklist or reviewer rulebook. Review summaries may index those criteria but must not add, weaken, or replace them.

## Clarify Requirements

[clarify-requirements/SKILL.md](clarify-requirements/SKILL.md) is the entry point for the requirements stage of the lightweight workflow. It can also be called by a larger workflow with a bounded question and inherited constraints.

It investigates existing behavior, builds an understanding from concrete situations, and asks only questions whose answers materially affect the requirement. Relevant counterexamples test that understanding; an exhaustive decision tree or generic checklist does not drive the interview. A fully specified request can proceed to model review without clarification questions. The author maintains the model, dispatches a fresh independent reviewer for each full review, repairs findings, and repeats until the review passes, then waits for final human approval. It stops before technical design, implementation tickets, or production code.

The companion [delivery standard](clarify-requirements/REQUIREMENTS-MODEL.md) defines the content and review requirements, including background-dependent explanations, decision rationale, concept relationships, Mermaid diagrams, and non-chronological organization. The entry point requires reading it before beginning work. The [reviewer contract](clarify-requirements/reviewer-prompt.md) defines a read-only role, its evidence package, and its result: `Pass`, `Changes required`, or `Blocked`. The reviewer receives the complete current model, requirement sources, and verification evidence without inheriting the author's working context. Review results stay in the conversation or task result, never in the deliverable.

Produced models are maintained as clean, integrated documents. Revisions update the owning sections and remove superseded content; patch files, changelogs, revision logs, and override addenda are prohibited. Editing and cleanup commentary stays in the conversation, while version control preserves history.

### Use

Register or link the entire `clarify-requirements` directory using your agent harness's skill mechanism. These files have not been installed into any harness automatically. Keep both companion files with `SKILL.md`. The harness must provide a fresh independent reviewer context and access to the required inputs and verification evidence. The same model can perform both roles in separate contexts; switching roles in the author's conversation or relying on author self-review is not a substitute. If independence or required evidence is unavailable, the skill reports a blocker and retains `Draft`.

Then invoke `clarify-requirements` with a requirement, an existing model to resume, or a bounded question delegated by another workflow. For example:

> Use clarify-requirements to clarify employee withdrawal of pending expense claims. Read the existing claim behavior first. Save the model at docs/requirements/claim-withdrawal.md and stop for my approval before technical clarification.

The skill follows a supplied document path or the project's existing convention; otherwise it uses `docs/requirements/<short-name>.md`. Review the actual model, not just the closing message. Interview answers and approval of proposed fixes do not approve the finished document. Findings, missing independent review, or incomplete mandatory verification keep it in `Draft`; an independent `Pass` for the current artifact permits `Awaiting approval`; explicit final approval of that reviewed model permits `Approved`. Content changes return to a fresh full review. Resuming an approved model never skips independent review, but an unchanged model can retain its established final approval after passing.

## Clarify Technical Design

[clarify-technical-design/SKILL.md](clarify-technical-design/SKILL.md) is the next-stage entry point after the current requirements model has passed independent review and received final human approval. The skill itself requires reading and applying [TECHNICAL-MODEL.md](clarify-technical-design/TECHNICAL-MODEL.md) throughout authoring and repair and using that same standard for independent review; this README is not the execution gate.

Technical grilling and modeling form one loop: challenge candidate designs against concrete scenarios and inspected evidence, ask only consequential unresolved questions with grounded alternatives and a recommendation, wait for the necessary human choices, and integrate answers into the model. Macro choices precede dependent micro choices; contradictions found while modeling or reviewing return to the affected technical question. This is not an exhaustive decision-tree interview or a private design exercise followed by a request for approval.

The technical deliverable includes a complete file-responsibility tree, macro and micro topology and sequence diagrams, explicit data-flow and concurrency semantics, complete data definitions, and complete interface contracts. It settles the scoped technical decisions rather than leaving structure, algorithms, coordination, or contract details to implementation. The [technical reviewer contract](clarify-technical-design/reviewer-prompt.md) governs fresh read-only reviews and the review-and-repair loop.

Install the entire `clarify-technical-design` directory using the harness's skill mechanism; it has not been installed automatically. Invoke it with the approved requirements model and any existing technical model. It follows a supplied path or repository convention, otherwise using `docs/technical/<short-name>.md`. Independent `Pass` and final human approval are separate gates. Approval hands the model to a subsequent ticket-decomposition workflow; this skill neither splits tickets nor implements production code. The later post-implementation change-governance workflow remains outside this skill.
