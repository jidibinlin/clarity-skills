# Custom Skills

## Clarify Requirements

[clarify-requirements/SKILL.md](clarify-requirements/SKILL.md) is the entry point for the requirements stage of the lightweight workflow. It can also be called by a larger workflow with a bounded question and inherited constraints.

It investigates existing behavior, clarifies material questions with the human, maintains a requirements/domain model, checks the deliverable, and stops at explicit human approval. It does not perform technical design, generate implementation tickets, or write production code.

The companion [delivery standard](clarify-requirements/REQUIREMENTS-MODEL.md) defines the content and review requirements, including background-dependent explanations, decision rationale, concept relationships, Mermaid diagrams, and non-chronological organization. The entry point requires reading it before beginning work.

### Use

Register or link the entire `clarify-requirements` directory using your agent harness's skill mechanism. These files have not been installed into any harness automatically. Keep the companion standard with `SKILL.md` when installing or copying the skill.

Then invoke `clarify-requirements` with a requirement, an existing model to resume, or a bounded question delegated by another workflow. For example:

> Use clarify-requirements to clarify employee withdrawal of pending expense claims. Read the existing claim behavior first. Save the model at docs/requirements/claim-withdrawal.md and stop for my approval before technical clarification.

The skill follows a supplied document path or the project's existing convention; otherwise it uses `docs/requirements/<short-name>.md`. Review the actual model, not just the closing message. Interview answers do not approve the document. A request to revise it returns to clarification; explicit approval ends this stage with a handoff.
