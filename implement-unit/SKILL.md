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

Use the resolved effort root’s `issue.md` for either route; a child modeling entry does not establish a separate implementation unit or controller. The standalone author establishes the shared exclusion gate before writing; delegated workers use the controller’s verified workspace and report failures. Recover current sources, evidence, findings, and original roles under the shared contract. A direct change uses its document path/revision, with no fabricated ticket/index or historical approvals.

Return missing decisions, contradictions, stale required evidence, or unmet prerequisites through IMPLEMENTATION.md's design-boundary routes. Resume only on a valid renewed basis. Do not reopen settled choices, ask for recoverable repository facts, or shrink a direct change to force bounded fit.

## 2. Choose evidence for this unit's behavior

Apply IMPLEMENTATION.md's test-value criteria using the actual runner, nearby tests, fixtures, commands, and approved interfaces. Reuse adequate coverage; identify real versus substituted interactions and assigned macro flows. Ask only consequential unresolved choices affecting behavior, production structure, or authorized verification constraints. Testing inconvenience does not authorize new production abstractions.

## 3. Implement each behavior in the approved structure

Follow IMPLEMENTATION.md's TDD path for uncovered behavior and its existing-test/behavior-preserving alternatives. Diagnose setup failures separately from behavioral red evidence. Implement directly in the approved owners and collaboration from the first increment; minimal means no speculative work, not temporary design violations.

Preserve unrelated user changes; update affected callers, tests, and documentation and complete the unit's approved cutover. Correct known defects as encountered. Return necessary upstream decisions instead of inventing designs. Canonical models/tickets stay clean descriptions, not execution history.

Record meaningful results/repairs under the shared contract in the ticket's same-stem `issues/NN-<slug>.log.md`, or root `issue.log.md` for direct work. A delegated author supplies entries to the controller unless assigned exclusive unit-log ownership. Clean implementation still needs a result record.

## 4. Exercise the completed increment

Run all applicable static, behavioral, regression, required project-suite, and actual-runtime checks in IMPLEMENTATION.md, including assigned macro flows with approved real participants. A direct unit completes its entire target and final combined evidence now; a ticket may leave only explicitly later-owned flows outside its local claim. Mandatory unavailable verification blocks Pass.

Preflight the complete result against the same standard, approved target, repository rules, and acceptance conditions. Correct known conformance defects and renew affected evidence before review; self-check does not replace independent assessment. Persist the result/repair decision and fresh code-bound evidence in the owning log before requesting review.

## 5. Obtain independent conformance review

Use reviewer-prompt.md's complete initial package and IMPLEMENTATION.md's original-pair lifecycle. Standalone, dispatch the bound read-only reviewer; delegated, send the request to the controller. Never substitute a role switch in the author's context or transmit private author reasoning as reviewer instructions.

The recorder saves every returned report before repairs or gate advancement. Return violations to the original implementer and current changes/evidence to the original reviewer for full-scope reassessment, using incremental rather than repeated initial packages. Only reviewer-confirmed closure and a complete current `Pass` without unresolved findings/blockers permit handoff. Continue ordinary repairs automatically; route genuine upstream/capability blockers without lowering the gate. Persist dispositions and update the entry through its owner before blockers, replacements, or handoffs.

## 6. Hand off the reviewed result and stop

Persist the applicable Pass/current state and return scope, code/source basis, actual verification/limits, and record links.

- **Delegated:** return to the supplied controller without per-unit human approval or whole-work `delivery.md`. It owns continuation and final acceptance under ORCHESTRATION.md. Ticket-local Pass is not whole-set completion; direct full-change Pass already supplies final independent review, without a duplicate overall reviewer.
- **Standalone:** after mandatory verification and Pass, write `.scratch/<work-slug>/delivery.md` under the shared summary contract and request explicit acceptance. A standalone ticket identifies only its reviewed scope and preserves a broader existing summary. Persist the actual user decision in the owning log, then update entry/summary.

Retain the original pair for conformance repairs. Reconcile current code and intervening user/ticket changes before edits; renew affected evidence and full-scope review, then integrate the summary before renewed acceptance. Genuine role loss follows IMPLEMENTATION.md; shared revision rules distinguish substantive changes from metadata-only updates.

Stop at this unit's authorized handoff or precise external blocker. Do not start another unit or automatically commit, merge, push, close remote issues, or release. Retain excluded records. Post-delivery design questions follow the unit standard's upstream route.
