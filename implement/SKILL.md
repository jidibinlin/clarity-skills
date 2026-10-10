---
name: implement
description: Use to execute an approved ticket set or a bounded approved change directly, or resume execution, coordinating persistent implementer/reviewer pairs through current runtime evidence and final human acceptance. Not for deciding change design or releasing changes.
---

# Implement

Coordinate the whole authorized scope: an actual ticket set or one bounded direct change. One authorization covers ordinary execution and repairs; it does not require per-unit human gates.

Before starting/resuming or making scheduling choices, load `workflow-artifacts` by name and read its complete WORKFLOW-ARTIFACTS.md; load `implement-unit` by name in reference-only mode and read its entire IMPLEMENTATION.md; read all of [ORCHESTRATION.md](ORCHESTRATION.md). These own shared records, single-unit execution/original-pair lifecycle, and whole-work coordination respectively. Apply `workflow-artifacts`' loading/resource and reference-only rules to every role. A standards-only load does not execute this controller. Only dispatch-specific reviewer prompts may wait until their first actual use.

## 1. Establish the authorized route and execution basis

Apply IMPLEMENTATION.md's approved-basis and route-validation gates. Read the full set and its approved source basis, or the entire direct change package and bounded-fit evidence, plus current approvals and execution authorization. Both routes use `.scratch/<work-slug>/issue.md`; only a ticket set uses it as an index. A direct change's path/revision is its identity, without fabricated tickets or historical prerequisites.

Inspect actual code, repository rules, prerequisites, target coverage, and verification facilities. Route source/design conflicts and scope expansion under the unit standard before proceeding. Establish ORCHESTRATION.md's shared execution basis, preserving user work, and verify the harness can retain/resume independent original roles. Missing capability is a blocker, not permission to silently replace roles.

The controller establishes the shared exclusion gate before artifact writes and owns the work entry/root `issue.log.md`; ticket execution uses same-stem unit logs. Recover the current basis, evidence, prerequisites, and original roles under the shared contract and ORCHESTRATION.md before trusting saved progress.

## 2. Dispatch a ready unit to its bound implementer

Select only work meeting ORCHESTRATION.md's physical prerequisite/readiness criteria. Default to serial execution; a direct change has one full-scope unit. Continue ready authorized work without per-unit confirmation.

Create and bind the original implementer at first execution; resume it for repairs. Supply the initial author package defined in ORCHESTRATION.md, including the resolved `implement-unit` SKILL.md with explicit delegated execution, complete applicable standards, approved source, and controller return route. **The author receives and applies those standards and sources before evidence choices or code edits**, not only after review. Specify artifact-writing ownership; delegated execution must not create another controller or competing reviewer.

## 3. Run the persistent independent review loop

At the first review request, load `implement-unit`'s reviewer-prompt.md and create the unit's bound independent read-only reviewer with that contract's full initial package. Retain the original pair under IMPLEMENTATION.md; later rounds use its incremental package, and genuine role loss uses its explicit replacement procedure.

Persist the implementation/repair result and fresh evidence in the owning log before review. Save every returned report before routing repairs or advancing. Require a complete applicable verdict; return incomplete reports to the reviewer rather than reinterpret them.

Route demonstrated violations to the original implementer, then refreshed evidence to the original reviewer for complete current-unit reassessment. Follow ORCHESTRATION.md for blockers, stalled progress, and evidence invalidation. Only current `Pass` with no unresolved finding/blocker and usable incorporated output permits passed state or dependent scheduling. The controller checks applicability, not code conformance in place of independent review. Persist dispositions/current state before proceeding; no author self-closure or retry count waives a finding.

## 4. Establish final verification and independent Pass

Apply ORCHESTRATION.md's route-specific final gate:

- **Direct change:** check that the original reviewer's full-change Pass and final combined runtime/regression evidence cover the entire current target. Return gaps to that pair; do not create another overall reviewer or repeat unchanged verification for duplicate review.
- **Ticket set:** after all outputs are incorporated, establish complete composition and run current combined regression/macro-flow verification. Load [reviewer-prompt.md](reviewer-prompt.md) at first overall dispatch and send its full package to a separate independent overall reviewer. Retain that reviewer. Route integration repairs to original responsible implementers on current combined code, serialize repairs, renew affected unit reviews, then renew overall review. No catch-all cleanup author or aggregation of local Passes replaces this assessment.

## 5. Request final human acceptance and stop

After mandatory current verification and the route-appropriate final independent Pass, persist overall evidence/verdict in `issue.log.md`. The controller writes `.scratch/<work-slug>/delivery.md` under the shared summary contract, links it from `issue.md`, and asks for explicit acceptance of the reviewed whole result. Prior model/set approval and unit Passes are not human code acceptance.

Apply ORCHESTRATION.md's handoff gate for requested repairs, renewed evidence/review, and upstream design changes. Record the actual acceptance decision in `issue.log.md`, then update entry and summary. Until then report `Awaiting acceptance`. Retain the private records under the shared contract.

Stop at acceptance or an exact external blocker after all reachable authorized work. Do not automatically commit, merge, push, close remote issues, or release.
