---
name: clarify-change
description: Clarify or resume changes to an existing system, including projects with missing or stale models, for bounded direct implementation or decomposition.
---

# Clarify Change

Recover the affected baseline, co-design the complete target, synchronize its authorities and obtain independent review plus human approval. This route can supply requirements and design together without inventing historical stages.

## Establish scope and baseline

Read [CHANGE-MODEL.md](CHANGE-MODEL.md) and its named technical imports before designing. Read its conditional architecture/map content sections when those authorities are affected. Use the `artifact-layout` skill for locations/ownership and the `communication-style` skill for human communication, including its Ask when human judgment is needed section for consequential questions. Resolve skills by registered name and resources through their installed owners.

Reuse the existing effort/root and canonical owners, or establish the change workspace through `artifact-layout`. Follow requested scenarios through current entry points, processes/modules, state owners, callers and outcomes. Compare documents with code, configuration, tests and runtime evidence. Retain reliable references and reconstruct missing affected behavior, ownership, files and contracts; bound investigation by the change and its necessary interactions.

Distinguish observed or inspected behavior from confirmed target intent and remaining uncertainty. Existing code does not override an approved target. Discuss unresolved intent with the human using the evidence you found.

## Compare current and target

Clarify changed and preserved scenarios, constraints and acceptance outcomes. Compare current and target across macro collaboration, dataflow/state, concurrency/completion, micro ownership, files and contracts. Explain both changes and the basis for unchanged claims.

Compare retaining, moving or consolidating responsibilities with new collaborators. Settle affected macro topology, sequences and overall guarantees before dependent local realization. Show concrete views in bounded groups, with context, meaningful alternatives and decisive rationale.

Use `Macro views` from registered `clarify-technical-design` for diagram guidance, without starting its workflow.

Then follow actual module dependencies from foundational configuration, representations, interfaces and basic operations to their consumers. Reuse applicable unchanged foundations. Start with data/declarations when their meaning is stable; use sequence-first or coupled decisions when lifecycle, ownership or completion determines representation.

For each bounded behavior, present brief context, complete target-language declarations and operation signatures with file/owner locations, and matching topology and sequences together in the main response. Use the code and diagram presentation requirements from registered `clarify-technical-design`'s `Micro design: closed-loop groups`, without starting its workflow. Explain decisive tradeoffs beside the definitions, confirm the concrete group, and reconcile the answer across the target before dependent decisions. Settle consequential design while leaving ordinary implementation choices to the implementing model.

Complete the target file tree, definitions/contracts, migrations and obsolete-path exits. Inspect actual integration-test facilities and select a few changed/preserved macro flows with setup, invocation and limits; detailed TDD belongs to implementation.

## Agree the route and synchronize authority

Choose **direct** when implementation, verification and repair fit one coherent context with settled owners, prerequisites and acceptance. Choose **decomposed** when meaningful separate increments or dependencies need coordination. Explain and confirm the route; a bounded direct change needs no synthetic tickets. Reconsider the route if its scope grows.

Locate the canonical authorities for changed concepts and return their integrated updates to the original authors. Keep root/shared navigation with the root owner. The change model explains the transition and references synchronized targets; without older models, it supplies the complete scoped target itself.

Trace impact through callers, dependent work, acceptance, approvals and verification evidence. Identify what must be reconsidered and why the remainder remains valid. Assess the change model and affected canonical sections together as one coordinated package, not a replay of initial architecture/technical stages.

## Write agreed specifications

Before every specification write, the owning author shows the exact proposed content or patch and destination in the main response, carrying forward the confirmed definitions and matching flows. Question-tool previews supplement that content. Explain material consequences and obtain explicit human confirmation. Apply only that confirmed content; confirm again if the proposal or basis changes. Keep unconfirmed proposals in conversation, not candidate files. Integrate decisions and their context into current owning sections rather than amendment diaries.

## Check, review and approve

Walk changed and preserved scenarios through the complete target and transition. Check referenced definitions, callers and migration feasibility. Render every diagram and visually inspect its current result, resolving cross-view conflicts before submission.

Use the `review-records` skill to prepare the submission and preserve review/repair evidence. Supply [reviewer-prompt.md](reviewer-prompt.md) with the coordinated package, baseline, governing sources, confirmations, actual checks and previous findings. Retain original change/canonical authors and the original independent change reviewer: report, original-author repairs with required write confirmation, then the same reviewer reassesses the package and findings. Repeat until Pass without unresolved findings or blockers.

Present the reviewed target, impacts, route and limits for explicit final human approval, separate from write consent. Human revisions return through the same loop.

Return approved model/source references, baseline, impacts, prerequisites, acceptance and review/approval evidence. Separately authorized direct execution goes to `implement` with one full-scope implementer/reviewer pair. Decomposed work goes to `split-tickets`; heavyweight children return to one governing root set. New consequential design choices during execution return to the original authors and change reviewer, then back to the originating implementation review; ordinary code-conformance repairs stay with implementation.

Stop here. Approval does not automatically launch ticketing or execution.
