---
name: implement
description: Use to execute an approved ticket set or a bounded approved change directly, or resume execution, coordinating persistent implementer/reviewer pairs through current runtime evidence and final human acceptance. Not for deciding change design or releasing changes.
---

# Implement

Coordinate the whole authorized scope: an actual ticket set or one bounded direct change. Execution authorization covers ordinary code work and repairs, not specification writes; it introduces no per-unit code-acceptance gate.

Before starting/resuming or making scheduling choices, load `workflow-artifacts` by name and read its complete WORKFLOW-ARTIFACTS.md; load `implement-unit` by name in reference-only mode and read its entire IMPLEMENTATION.md; read all of [ORCHESTRATION.md](ORCHESTRATION.md). These own shared records/persistent author-reviewer lifecycle, single-unit execution, and whole-work coordination respectively. Apply `workflow-artifacts`' loading/resource and reference-only rules to every role. A standards-only load does not execute this controller. Only dispatch-specific reviewer prompts may wait until their first actual use.

## 1. Establish the authorized route and execution basis

Apply IMPLEMENTATION.md’s approved-basis and route-validation gates. Resolve supplied effort/child entries to the governing root `issue.md`; read the full global set and its selected flat/hierarchical/change source package, or the entire bounded direct change package. Resolve current scoped review/approval evidence through model metadata and owning object logs, and establish execution authorization. Hierarchy uses one root controller and ticket set; child entries define models, not new controllers or recovery files. A direct change’s path/revision is its source identity, without fabricated tickets or historical prerequisites.

Inspect actual code, repository rules, prerequisites, target coverage, and verification facilities. Route source/design conflicts and scope expansion under the unit standard before proceeding. Establish ORCHESTRATION.md's shared execution basis, preserving user work, and verify the harness can retain/resume independent original roles. Missing capability is a blocker, not permission to silently replace roles.

The controller establishes the shared exclusion gate before artifact writes, maintains definition/navigation in `issue.md`, and owns `implementation.review-fix-decisions.log.md`. Each existing ticket carries its compact non-normative execution block and has its own review log under explicit single-writer assignments. Direct work shares one implementation review log with its full-scope pair; its compact identity header binds the original roles without progress, blockers or next actions. Create no state file, scheduler ledger, duplicate checklist or recovery snapshot. Resume or cut over artifacts, current basis/evidence, prerequisites and original roles under the shared contract and ORCHESTRATION.md before trusting saved status. Apply **Human-confirmed specification writes** before changing any entry, model or ticket, including its embedded execution/role/status metadata: show exact content and wait for explicit confirmation. Scope authorization or no-design-change judgments never waive this.

## 2. Dispatch a ready unit to its bound implementer

Select only work meeting ORCHESTRATION.md's physical prerequisite/readiness criteria. Default to serial execution; a direct change has one full-scope unit. Continue ready authorized work without per-unit code acceptance; document writes still wait for their exact confirmation.

Create and bind the original implementer at first execution; resume it for repairs. Supply the initial author package defined in ORCHESTRATION.md, including the resolved `implement-unit` SKILL.md with explicit delegated execution, complete applicable standards, approved source, and controller return route. **The author receives and applies those standards and sources before evidence choices or code edits**, not only after review. Specify artifact-writing ownership and supply exact confirmed patches, current basis and confirmation references for any delegated specification writes; delegated execution must not create another controller or competing reviewer.

## 3. Run the persistent independent review loop

At the first review request, load `implement-unit`'s reviewer-prompt.md and create the unit's bound independent read-only reviewer with that contract's full initial package. Retain the original pair under WORKFLOW-ARTIFACTS.md’s **Persistent author/reviewer lifecycle**; later rounds use its incremental package, and genuine role loss uses its explicit replacement procedure.

Persist the identified review submission and verification, or finding-linked repair decisions and fresh evidence, in the owning review log before review. Save every returned report before routing repairs or advancing. Require a complete applicable verdict; return incomplete reports to the reviewer rather than reinterpret them.

Route demonstrated violations to the original implementer, then refreshed evidence to the original reviewer for complete current-unit reassessment. Follow ORCHESTRATION.md for blockers, stalled progress, and evidence invalidation. Only current `Pass` with no unresolved finding/blocker and usable incorporated output permits a passed ticket status or dependent scheduling. The controller checks applicability, not code conformance in place of independent review. Persist dispositions and obtain confirmation of the exact ticket-execution-block update before writing it and proceeding; direct work uses its actual code and review evidence. No author self-closure or retry count waives a finding.

## 4. Establish final verification and independent Pass

Apply ORCHESTRATION.md's route-specific final gate:

- **Direct change:** check that the original reviewer's full-change Pass and final combined runtime/regression evidence cover the entire current target. Return gaps to that pair; do not create another overall reviewer or repeat unchanged verification for duplicate review.
- **Ticket set:** after all outputs are incorporated, establish complete composition against the root selected scope and run current combined regression/macro-flow verification, including shared and cross-child obligations. Load [reviewer-prompt.md](reviewer-prompt.md) at first overall dispatch and send its full package to a separate independent overall reviewer. Retain that reviewer. Route integration repairs to original responsible implementers on current combined code, serialize repairs, renew affected unit reviews, then renew overall review. No catch-all cleanup author or aggregation of child/unit Passes replaces this assessment.

## 5. Request final human acceptance and stop

After mandatory current verification and the route-appropriate final independent Pass, preserve the overall submission/evidence and verdict in `implementation.review-fix-decisions.log.md`; direct work already uses this same record. The controller writes `.scratch/<work-slug>/delivery.md` under the shared summary contract, obtains confirmation of the exact `issue.md` navigation patch before linking the summary, explicitly surfaces significant autonomous repair decisions with record links, and asks for acceptance of the reviewed whole result. Prior model/set approval and unit Passes are not human code acceptance. Keep `issue.md` for specification navigation, not acceptance-record links.

Apply ORCHESTRATION.md’s handoff gate for requested repairs, renewed evidence/review, and upstream design changes. Record the actual acceptance decision with exact scope/code/source basis in `implementation.review-fix-decisions.log.md`, then update the delivery summary with its acceptance-evidence link. Until then report `Awaiting acceptance`. Retain the private records under the shared contract.

Stop at acceptance or an exact external blocker after all reachable authorized work. Do not automatically commit, merge, push, close remote issues, or release.
