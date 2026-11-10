---
name: clarify-architecture
description: Clarify or resume global architecture for independently reviewed and human-approved requirements.
---

# Clarify Architecture

Co-design the selected effort's global topology, guarantees and shared realization owners. Finish with independent review and human approval.

## Establish the basis

Read [ARCHITECTURE-MODEL.md](ARCHITECTURE-MODEL.md) and its selective technical imports before designing. Use the `artifact-layout` skill for locations/ownership. Resolve skills through their registered names and resources through their installed owners; importing a standard does not invoke its author's workflow.

Read the selected requirements, dependencies and exclusions. The requirements must have independent Pass and human approval. Inspect relevant runtime/code boundaries, state owners, interfaces, callers and repository guidance. Resume from current models and prior decisions, not just status labels.

## Trace scenarios and compare collaboration

Follow approved scenarios from entry to observable outcome through processes, modules and state owners. Identify the guarantees at each crossing and the owner capable of enforcing them. Compare reuse or redistribution of existing responsibilities with introducing new collaborators. Treat existing code as evidence, while preserving the approved target's authority.

Start with macro topology and state boundaries. Walk core sequences through them to resolve dataflow, concurrency, completion and failure behavior. Compare mechanisms against the required guarantees and investigate consequential uncertainty as needed.

Use `Macro views` from registered `clarify-technical-design` for diagram guidance, without starting its workflow.

## Converge with the human

Present bounded groups of actual topology, sequences, dataflow and boundary contracts, with context, decisive alternatives and consequences. Confirm the concrete choices progressively before building dependent detail. Reconcile each answer across the views and continue with the next ready decision; reuse settled content while its basis remains applicable.

Settle all global choices needed for technical design, including representations where compatibility depends on them. Then assign each shared realization one owner, its consumers and design dependencies. Leave local objects and algorithms to technical design within those guarantees.

Inspect the project's integration-test facilities and select a few meaningful cross-boundary flows with coverage owners and cooperation needs. Keep this a practical macro-flow plan rather than future detailed TDD.

## Write the agreed model

Before every specification write, show the exact proposed content or patch and its destination, explain material consequences, and obtain explicit human confirmation. Apply only that confirmed content; if the proposal or basis changes, confirm the revision first. Keep unconfirmed proposals in conversation, not candidate files.

Integrate agreed content into the canonical architecture and work navigation through their assigned writer. Return requirement conflicts to their owner in `clarify-requirements`; revise affected architectural decisions here and realizations in `clarify-technical-design`.

## Check, review and approve

Walk scenarios through the complete global model and realization assignments. Render every diagram and visually inspect the result against the intended boundaries, paths and ordering. Resolve contradictions and gather necessary feasibility evidence, distinguishing actual checks from planned integration tests.

Give [reviewer-prompt.md](reviewer-prompt.md) the current model, approved sources, confirmations, checks and prior findings. Keep the original author and a separate original independent reviewer through the loop: original-author repair with any required write confirmation, then the same reviewer reassesses the current model and findings. Ask the original reviewer if feedback is unclear. Continue until Pass without unresolved findings or blockers.

Present the reviewed architecture, consequential choices, assignments and limits for explicit final human approval. Human revisions return through the same loop. This approval is separate from consent to write.

Return the approved model and source references, review result, human approval, evidence references and realization assignments. Stop here; do not automatically launch technical design or execution.
