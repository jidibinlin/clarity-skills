---
name: implement-unit
description: Use to execute one approved ticket or bounded approved change, standalone or delegated by implement, and resume or repair it with the original implementer and independent reviewer. Not for deciding change design, decomposing work, or releasing changes.
---

# Implement Unit

Implement one approved unit directly in its agreed structure; independent review checks conformance, not a planned rough-code-then-redesign phase.

Before starting/resuming, load `workflow-artifacts` by name and read its complete WORKFLOW-ARTIFACTS.md, then all of [IMPLEMENTATION.md](IMPLEMENTATION.md), **before investigation, evidence choices, or code edits**. These own shared records and unit source/code/test/runtime criteria plus the original-pair lifecycle. Apply `workflow-artifacts`' loading/resource and reference-only rules to every role. A standards-only load starts no implementation or reviewer pair. Read [reviewer-prompt.md](reviewer-prompt.md) at first review dispatch; no external TDD/review rulebook replaces these standards.

Establish invocation mode under IMPLEMENTATION.md. Standalone: the current author implements and retains an independent reviewer. Delegated: the existing controller binds both roles; send intermediate review requests/blockers and the eventual passed result to it. Do not recursively invoke `implement`, spawn competing roles, or request per-unit human approval.

## 1. Establish the executable work unit

Apply IMPLEMENTATION.md’s approved-basis and bounded-direct-fit gates. Resolve supplied effort/child sources through the root entry; read the route-appropriate exact source revisions, applicable scope/review/human approvals and execution authorization. Load this unit’s precise shared/architecture/child references and necessary cross-child dependencies, not unrelated history. Inspect affected code/callers, repository rules, facilities, and existing user changes; establish the current code basis and **actual usable prerequisite outputs**, not predecessor status alone.

Use the resolved effort root’s `issue.md` for definition/navigation on either route; a child modeling entry does not establish a separate implementation unit or controller. The standalone author establishes the shared exclusion gate before writing; delegated workers use the controller’s verified workspace and report failures. Resume or cut over current sources, ticket status where applicable, evidence, findings and original roles under the shared contract. A ticket carries its compact non-normative execution block and uses `issues/NN-<slug>.review-fix-decisions.log.md`, even standalone. Direct execution uses the single `implementation.review-fix-decisions.log.md`, separate from change-model review, with a compact work/role identity header for its original pair. Create no state file, fabricated ticket, duplicate controller record, checklist or recovery snapshot. Assign one writer per ticket or review log; reviewers remain read-only.

Return missing decisions, contradictions, stale required evidence, or unmet prerequisites through IMPLEMENTATION.md's design-boundary routes. Resume only on a valid renewed basis. Do not reopen settled choices, ask for recoverable repository facts, or shrink a direct change to force bounded fit.

## 2. Choose evidence for this unit's behavior

Apply IMPLEMENTATION.md's test-value criteria using the actual runner, nearby tests, fixtures, commands, and approved interfaces. Reuse adequate coverage; identify real versus substituted interactions and assigned macro flows. Ask only consequential unresolved choices affecting behavior, production structure, or authorized verification constraints. Testing inconvenience does not authorize new production abstractions.

## 3. Implement each behavior in the approved structure

Follow IMPLEMENTATION.md's TDD path for uncovered behavior and its existing-test/behavior-preserving alternatives. Diagnose setup failures separately from behavioral red evidence. Implement directly in the approved owners and collaboration from the first increment; minimal means no speculative work, not temporary design violations.

Preserve unrelated user changes; update affected callers, tests, and documentation and complete the unit's approved cutover. Correct known defects as encountered. Return necessary upstream decisions instead of inventing designs. Canonical models/tickets stay clean descriptions, not execution history.

Update current status, blocker, original role handles and applicable evidence references in the existing ticket’s compact non-normative execution block when a ticket exists; do not repeat planned tasks or chronological progress. Direct work uses approved change, actual code and reviews, with role identity only in its existing review-log header. Prepare an identified review submission with actual verification in the owning review log; an initial clean implementation records submission and evidence, not ordinary progress or invented findings. For repairs, record the existing finding IDs, chosen correction, rationale/consequences and fresh evidence under the shared contract. Delegated authors supply updates to the assigned writer unless they exclusively own the ticket or log; reviewers remain read-only.

## 4. Exercise the completed increment

Run all applicable static, behavioral, regression, required project-suite, and actual-runtime checks in IMPLEMENTATION.md, including assigned macro flows with approved real participants. A direct unit completes its entire target and final combined evidence now; a ticket may leave only explicitly later-owned flows outside its local claim. Mandatory unavailable verification blocks Pass.

Preflight the complete result against the same standard, approved target, repository rules, and acceptance conditions. Correct known conformance defects and renew affected evidence before review; self-check does not replace independent assessment. Persist the review submission or finding-linked repair decision and fresh code-bound evidence in the owning review log before requesting review.

## 5. Obtain independent conformance review

Use reviewer-prompt.md's complete initial package and IMPLEMENTATION.md's original-pair lifecycle. Standalone, dispatch the bound read-only reviewer; delegated, send the request to the controller. Never substitute a role switch in the author's context or transmit private author reasoning as reviewer instructions.

The assigned writer saves every returned report before repairs or gate advancement. Return violations to the original implementer and current changes/evidence to the original reviewer for full-scope reassessment, using incremental rather than repeated initial packages. Only reviewer-confirmed closure and a complete current `Pass` without unresolved findings/blockers permit handoff. Continue ordinary repairs automatically; route genuine upstream/capability blockers without lowering the gate. Before blockers, replacements or handoffs, persist dispositions and reconcile ticket metadata where applicable, actual code, evidence and bound roles; carry the missing conditions and role handoff basis without a recovery file.

## 6. Hand off the reviewed result and stop

Persist the applicable Pass and update the existing ticket’s execution status where applicable; return scope, code/source basis, actual verification/limits, consequential autonomous repair decisions, and ticket/review-record references. For direct work return the approved change and implementation review references, not a substitute status artifact.

- **Delegated:** return to the supplied controller without per-unit human approval or whole-work `delivery.md`. It owns continuation and final acceptance under ORCHESTRATION.md. Ticket-local Pass is not whole-set completion; direct full-change Pass already supplies final independent review, without a duplicate overall reviewer.
- **Standalone:** after mandatory verification and Pass, write `.scratch/<work-slug>/delivery.md` under the shared summary contract and request explicit acceptance, surfacing significant autonomous repair decisions with record links. A standalone ticket identifies only its reviewed scope and preserves a broader existing summary. Persist the actual scoped user decision and reviewed code/source basis in the owning review log, then update the summary’s acceptance and evidence link, not approval navigation in `issue.md`.

Retain the original pair for conformance repairs. Reconcile current code and intervening user/ticket changes before edits; renew affected evidence and full-scope review, then integrate the summary before renewed acceptance. Genuine role loss follows IMPLEMENTATION.md; shared revision rules distinguish substantive changes from metadata-only updates.

Stop at this unit's authorized handoff or precise external blocker. Do not start another unit or automatically commit, merge, push, close remote issues, or release. Retain excluded records. Post-delivery design questions follow the unit standard's upstream route.
