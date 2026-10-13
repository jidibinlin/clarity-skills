---
name: clarify-technical-design
description: Clarify or resume technical realization of approved requirements; heavyweight child design also realizes approved architecture.
---

# Clarify Technical Design

Co-design a complete scoped production realization, independently review it, obtain human approval, then hand it back for the next authorized stage.

## Establish the basis

Read [TECHNICAL-MODEL.md](TECHNICAL-MODEL.md) before designing. Load `artifact-layout` for locations/ownership and `ask-with-context` for substantive questions, including its Required question format and pre-send check. Resolve skills through their registered names and resources through their installed owners; a standard import does not invoke its author's workflow.

Read the approved requirements, original context and applicable review/approval evidence. Inspect relevant repository guidance, runtime boundaries, owners, types, interfaces, callers and tests. Recover current work and prior decisions when resuming.

For a heavyweight child, also resolve the root's approved requirements package and architecture, and read registered `clarify-architecture`'s `ARCHITECTURE-MODEL.md` for inherited guarantees and shared realization assignments. Return conflicts to the owning authority rather than changing a global premise locally.

## Settle macro collaboration

Trace approved scenarios from entry to observable outcome through processes, modules and state owners, including consequential alternatives. Compare existing concepts and collaboration with what the target needs; reuse capable owners before introducing new abstractions. Existing code explains the baseline, not a reason to override approved intent.

Propose actual macro topology, state/dataflow, concurrency mechanisms and core sequences. Walk the scenarios through these views to expose ownership, completion and boundary-contract choices. Show the human bounded concrete groups with context, alternatives and decisive rationale, and settle them before dependent local detail.

## Refine through foundational dependencies

Identify what consuming collaborations need from their foundations: configuration, owned/state representations, interfaces and basic operations. Design along those actual dependencies rather than directory or call-stack order.

Within a module, use data/declaration-first as a heuristic. When lifecycle, ownership or completion determines representation, work through the sequence first or decide the coupled views together.

Progressively show complete declarations or schemas, concrete interfaces, object topology, sequences and file responsibilities. Confirm these actual decisions with the human instead of revealing a completed blueprint after broad direction agreement. Reconcile answers across views, replay the scenario and continue to the next ready decision. Applicable unchanged definitions can be referenced without redesigning them.

Build the complete scoped file tree from the owners, including integration/test locations and retired paths. Trace macro guarantees into concrete micro operations and mechanisms. Settle consequential design while leaving ordinary implementation choices to the implementing model.

Inspect the project's test facilities and choose a few meaningful macro flows from entry to observable outcome. Identify participants, setup, invocation and limits; heavyweight children inherit global flow references and complete their participation. Detailed future TDD stays with implementation.

## Write the agreed model

Before every specification write, show the exact proposed content or patch and destination, explain material consequences, and obtain explicit human confirmation. Apply only the confirmed content; a changed proposal or basis needs renewed confirmation. Keep unconfirmed proposals conversational, not in candidate files.

Integrate agreed content in canonical sections. Heavyweight children write their assigned realizations and return root navigation changes to the root owner. Mutually dependent children can be reviewed as one coordinated package.

## Check, review and approve

Walk the scenarios across requirements, files, macro/micro views, declarations and contracts. Render every diagram and visually inspect its actual result. Resolve conflicts and substantiate consequential feasibility claims; distinguish current checks from the future flow plan.

Read `review-records` to prepare the submission and preserve review/repair evidence. Supply [reviewer-prompt.md](reviewer-prompt.md) with the current model, governing sources, confirmations, checks and prior findings. Retain the original author and separate original independent reviewer: report, original-author repair with required write confirmation, then the same reviewer reassesses the complete current design and findings. Repeat until Pass without unresolved findings or blockers.

Present the reviewed design and limits for explicit final human approval, separate from write consent. Human revisions return through the same loop.

Return the approved model/source references and review/approval evidence. A heavyweight child returns to the root: all scoped realizations must be complete and approved before one root ticket set, controller and delivery. Stop before ticketing or coding; do not automatically launch the next stage.
