---
name: clarify-technical-design
description: Clarify or resume technical realization of approved requirements; heavyweight child design also realizes approved architecture.
---

# Clarify Technical Design

Co-design the technical model **top-down from macro to micro**. Within micro design, work **bottom-up along foundational dependencies**, using complete behavior as the unit of discussion. Finish with independent review and final human approval.

## Establish the basis

Read [TECHNICAL-MODEL.md](TECHNICAL-MODEL.md) before designing. Use the `artifact-layout` skill for locations/ownership and the `communication-style` skill for human communication, including its Ask when human judgment is needed section for consequential questions. Resolve skills through their registered names and resources through their installed owners; a standard import does not invoke its author's workflow.

Read the approved requirements, original context and applicable review/approval evidence. Inspect relevant repository guidance, runtime boundaries, owners, types, interfaces, callers and tests. Recover current work and prior decisions when resuming.

For a heavyweight child, read the root's approved requirements package and architecture document. Inherit its guarantees, boundary contracts, shared realization assignments and relevant child dependencies; refine the scoped macro design within that basis. Return conflicts to the owning authority rather than changing a global premise locally.

## 1. Macro design: settle topology and technical direction

Trace approved scenarios from entry to observable outcome through processes, modules and state owners, including consequential alternatives. Compare existing concepts and collaboration with what the target needs; reuse capable owners before introducing new abstractions. Existing code explains the baseline, not a reason to override approved intent.

Propose actual macro topology, responsibility boundaries, technical approaches, state/dataflow, concurrency mechanisms and core sequences. Walk the scenarios through these views to expose ownership, completion and boundary-contract choices. Discuss concrete groups with context, alternatives and decisive rationale; obtain human confirmation of the macro basis before its dependent micro design.

## 2. Micro design: co-design complete behavior

1. Choose a bounded behavior, including the collaborating modules needed to complete it. Restore its confirmed macro guarantees and prior decisions. Work from foundational state and operations toward their consumers; use the whole flow to test those foundations.
2. Develop an end-to-end proposal before asking for decisions. Connect state owners, triggers, computation, consumers and outcomes, including consequential interruption/recovery paths. Use declarations first when their meaning is stable; let lifecycle and sequences lead when they determine representation. Keep working assumptions explicit in conversation; if a missing human premise blocks the design, ask about that premise and its impact.
3. Walk the normal flow and decisive counterexamples, reconciling data, interfaces and sequences before presentation. Inspect existing implementations to establish reuse and necessary changes against the target, rather than reopen confirmed intent.
4. Present one coherent micro-design group in the main response: brief context, complete target-language declarations and operation signatures with their file/owner locations, matching topology and sequences, then the remaining tradeoffs. Use the standard's representation rules for protocol and dynamic data. Keep rationale beside the definitions it explains. Confirm the concrete group, propagate the answer across affected views, then advance to dependent behavior. Reference unchanged approved definitions precisely.

Build the complete scoped file tree from the owners, including integration/test locations and retired paths. Trace macro guarantees into concrete micro operations and mechanisms. Settle consequential design while leaving ordinary implementation choices to the implementing model.

Inspect the project's test facilities and choose a few meaningful macro flows from entry to observable outcome. Identify participants, setup, invocation and limits; heavyweight children inherit global flow references and complete their participation. Detailed future TDD stays with implementation.

## Integrate confirmed groups throughout the design

Before every specification write, show the exact proposed content or patch and destination in the main response, explain material consequences, and obtain explicit human confirmation. Carry the confirmed definitions and matching flows into that content; question-tool previews supplement it rather than carry the only copy. One answer can approve the design and its write when both were fully displayed. Apply only the confirmed content; a changed proposal or basis needs renewed confirmation. Keep unconfirmed proposals conversational, not in candidate files.

Integrate agreed content by revising its owning sections and reconciling affected decisions, references and remaining open scope, so the model expresses the current design rather than accumulated amendments. Heavyweight children write their assigned realizations and return root navigation changes to the root owner. Mutually dependent children can be reviewed as one coordinated package.

## 3. Check, review and approve

Walk the scenarios across requirements, files, macro/micro views, declarations and contracts. Render every diagram and visually inspect its actual result. Resolve conflicts and substantiate consequential feasibility claims; distinguish current checks from the future flow plan.

Use the `review-records` skill to prepare the submission and preserve review/repair evidence. Supply [reviewer-prompt.md](reviewer-prompt.md) with the current model, governing sources, confirmations, checks and prior findings. Retain the original author and separate original independent reviewer: report, original-author repair with required write confirmation, then the same reviewer reassesses the complete current design and findings. Repeat until Pass without unresolved findings or blockers.

Present the reviewed design and limits for explicit final human approval, separate from write consent. Human revisions return through the same loop.

Return the approved model/source references and review/approval evidence. A heavyweight child returns to the root: all scoped realizations must be complete and approved before one root ticket set, controller and delivery. Stop before ticketing or coding; do not automatically launch the next stage.
