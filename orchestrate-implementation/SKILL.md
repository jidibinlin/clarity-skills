---
name: orchestrate-implementation
description: Implement an approved scope through independent review and final human acceptance; continue existing work when present.
---

# Orchestrate Implementation

Coordinate the whole requirement. `implement` runs each unit's implementation/review loop, using `tdd` and `code-review` in the implementer's context.

Read [ORCHESTRATION.md](ORCHESTRATION.md). Use the `artifact-layout` skill for storage and the `communication-style` skill for communication. Resolve cross-skill resources through their registered owners.

## 1. Start from the approved work

Read the authorized requirements/design or approved bounded change. Establish the requested scope, current code and usable prerequisites. Reading existing approvals does not require asking for them again.

Resolve child inputs to root `issue.md`. A bounded direct change is one full-scope unit. Existing code describes the starting point, while approved sources govern the target.

For new work, assign implementers and independent reviewers to the selected units. On resume, use the current code, progress and prior review results to continue with the original participants.

## 2. Complete the ready units

Select work whose required outputs are incorporated and usable, with applicable prerequisite review/evidence. Choose an order that respects dependencies and shared work.

Dispatch the implementer through registered `implement` with its scope, approved references, current code, prerequisite outputs and verification responsibilities. Supply prior findings when continuing work.

Let the unit's implementer invoke `code-review` in its current context.

After unit Pass, incorporate the result. Continue ready dependent work without per-unit human approval. For blocked work, identify the missing input or decision and continue other ready units; return source-design conflicts to their owning stage.

## 3. Verify and review the combined result

Follow the approved flows across incorporated outputs. Obtain the required combined regression and whole-flow evidence, reusing current evidence where it still proves the outcome.

For **multiple units**, use `code-review` in the coordinator's current context to dispatch independent overall Spec and Standards reviewers. Provide the complete scope, approved sources, combined code, unit reviews, verification and prior findings. Supply ORCHESTRATION.md as the composition standard. Review composition and cross-unit behavior, not just individual Passes.

If a review report is unclear, ask the original reviewer for clarification. Return fixes to the original responsible implementers through `implement`, renew affected unit reviews and return to the same overall reviewers until Pass. For a **single unit**, the original unit reviewers' full-change assessments are already the final independent review.

## 4. Obtain final acceptance

After final Pass and required verification, write the one root `delivery.md`. Present the reviewed whole result, evidence and consequential decisions for explicit human acceptance. Requested repairs retain the original owners and reviewers.

Stop after acceptance or an unresolved external blocker. Execution authority does not include automatic commits, publication or release.

## Applying specification writes

Show specification content or its exact patch and obtain explicit confirmation before writing; renew confirmation if the proposal or its basis changes. Keep unconfirmed proposals in conversation.
