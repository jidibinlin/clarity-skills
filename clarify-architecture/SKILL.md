---
name: clarify-architecture
description: Clarify or resume global architecture for an independently reviewed and human-approved heavyweight requirements package.
---

# Clarify Architecture

Co-design the selected effort's global topology, guarantees and shared realization owners. Finish with independent review and human approval, then return child technical-design assignments.

## Establish the basis

Read [ARCHITECTURE-MODEL.md](ARCHITECTURE-MODEL.md) and its selective technical imports before designing. Use the `artifact-layout` skill for locations/ownership and the `communication-style` skill for human communication, including its Ask when human judgment is needed section for consequential questions. Resolve skills through their registered names and resources through their installed owners; importing a standard does not invoke its author's workflow.

Resolve the root entry's selected shared/child requirements, dependencies and exclusions. The package must have independent composite Pass and human approval. Inspect relevant runtime/code boundaries, state owners, interfaces, callers and repository guidance. Resume from current models and prior decisions, not just status labels.

## Trace scenarios and compare collaboration

Follow approved cross-child scenarios from entry to observable outcome through processes, modules and state owners. Identify the guarantees at each crossing and the owner capable of enforcing them. Compare reuse or redistribution of existing responsibilities with introducing new collaborators. Treat existing code as evidence, while preserving the approved target's authority.

Start with macro topology and state boundaries. Walk core sequences through them to resolve dataflow, concurrency, completion and failure behavior. Compare mechanisms against the required guarantees and investigate consequential uncertainty as needed.

Use `Macro views` from registered `clarify-technical-design` for diagram guidance, without starting its workflow.

## Converge with the human

Present bounded groups of actual topology, sequences, dataflow and boundary contracts, with context, decisive alternatives and consequences. Confirm the concrete choices progressively before building dependent detail. Reconcile each answer across the views and continue with the next ready decision; reuse settled content while its basis remains applicable.

Settle all global choices needed by children, including representations where cross-child compatibility depends on them. Then assign each shared realization one child technical owner, its consumers and design dependencies. Leave local objects and algorithms to child technical design within those guarantees.

Inspect the project's integration-test facilities and select a few meaningful cross-child flows with coverage owners and cooperation needs. Keep this a practical macro-flow plan rather than future detailed TDD.

## Write the agreed model

Before every specification write, show the exact proposed content or patch and its destination, explain material consequences, and obtain explicit human confirmation. Apply only that confirmed content; if the proposal or basis changes, confirm the revision first. Keep unconfirmed proposals in conversation, not candidate files.

Integrate agreed content into the canonical architecture and root navigation through their assigned writer. Return requirement conflicts to their owner in `clarify-requirements`; revise affected architectural decisions here and realizations in `clarify-technical-design`.

## Check, review and approve

Walk scenarios through the complete global model and child assignments. Render every diagram and visually inspect the result against the intended boundaries, paths and ordering. Resolve contradictions and gather necessary feasibility evidence, distinguishing actual checks from planned integration tests.

Give [reviewer-prompt.md](reviewer-prompt.md) the current model, approved sources, confirmations, checks and prior findings. Keep the original author and a separate original independent reviewer through the loop: original-author repair with any required write confirmation, then the same reviewer reassesses the current model and findings. Ask the original reviewer if feedback is unclear. Continue until Pass without unresolved findings or blockers.

Present the reviewed architecture, consequential choices, assignments and limits for explicit final human approval. Human revisions return through the same loop. This approval is separate from consent to write.

Return the root entry, approved model and source references, review result, human approval, evidence references and child assignments. Child realizations must all be complete and approved before one root ticket set, controller and delivery. Stop here; do not automatically launch child design or execution.
