---
name: orchestrate-implementation
description: Implement an approved ticket set or bounded direct change through independent review and final human acceptance; continue existing work when present.
---

# Orchestrate Implementation

Coordinate the whole requirement. `implement` runs each unit's implementation/review loop; its implementer uses `tdd`, and its independent reviewer uses `code-review`.

Read [ORCHESTRATION.md](ORCHESTRATION.md). Use the `artifact-layout` skill for storage, the `review-records` skill for review records and the `communication-style` skill for human communication. Resolve cross-skill resources through their registered owners.

## 1. Start from the approved work

Read the authorized requirements/design and ticket set, or the approved bounded change. Establish the requested scope, current code and usable prerequisites. Reading existing approvals does not require asking for them again; planning approval alone does not start execution.

Resolve child inputs to root `issue.md` and use one root ticket set. A bounded direct change is one full-scope unit without synthetic tickets. Existing code describes the starting point, while approved sources govern the target.

For new work, assign an implementer to each selected unit and bind an independent reviewer when review begins. If implementation is already underway, reconcile the current code, ticket facts and review records, then continue with the original implementers and reviewers.

## 2. Complete the ready units

Select work whose required outputs are incorporated and usable, with applicable prerequisite review/evidence. Choose an order that respects dependencies and shared work.

Dispatch the implementer through registered `implement` with its scope, approved references, current code, prerequisite outputs and verification responsibilities. Supply prior findings when continuing work.

When a delegated unit requests review, dispatch its independent reviewer through registered `code-review` with the unit's review assignment and return the report to the same implementer. Keep that pair through the unit's repair/re-review loop rather than starting a new pair each round.

After unit Pass, incorporate the result and preserve the report and dispositions. Continue ready dependent work without per-ticket human approval. For blocked work, identify the missing input or decision and continue other ready units; return source-design conflicts to their owning stage.

## 3. Verify and review the combined result

Follow the approved flows across incorporated outputs. Obtain the required combined regression and whole-flow evidence, reusing current evidence where it still proves the outcome.

For a **ticket set**, assign an independent overall reviewer using the `code-review` skill. Provide the complete scope and approved sources, combined code, unit reports, verification and prior findings. Give the reviewer ORCHESTRATION.md as the composition standard, with `review-records` as the report format. Review composition and cross-ticket behavior, not just individual Passes.

Route findings to the original responsible implementers through `implement`, renew affected unit reviews and return to the same overall reviewer until Pass. For a **direct change**, the original unit reviewer's full-change assessment is already the final independent review.

## 4. Obtain final acceptance

After final Pass and required verification, write the one root `delivery.md`. Present the reviewed whole result, evidence and consequential decisions for explicit human acceptance, and record the decision. Requested repairs retain the original owners and reviewers.

Stop after acceptance or an unresolved external blocker. Execution authority does not include automatic commits, publication or release.

## Applying specification writes

Show specification content or its exact patch and obtain explicit confirmation before writing; renew confirmation if the proposal or its basis changes. Keep unconfirmed proposals in conversation.
