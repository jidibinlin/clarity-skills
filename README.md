# Custom Skills

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
