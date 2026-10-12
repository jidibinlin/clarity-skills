---
name: split-tickets
description: Use after a flat requirements/technical or hierarchical requirements/architecture/child-technical package has passed applicable review and human approval to split implementation work or revise its global ticket set; also use for an approved change package needing decomposition. Not for production design, coding, or executing tickets.
---

# Split Tickets

Turn the approved source basis into coherent implementation units that fit a fresh context through understanding, implementation, verification, and repair. Split the work, not the approved code structure.

Before starting or resuming, load `workflow-artifacts` by name and read its complete WORKFLOW-ARTIFACTS.md, then all of [TICKETS.md](TICKETS.md), **before investigation, questions, or planning**. They govern shared artifacts and substantive ticket criteria respectively. Apply `workflow-artifacts`' loading/resource and reference-only rules to every role; loading this skill for standards does not authorize its workflow. Read [reviewer-prompt.md](reviewer-prompt.md) at first review dispatch.

## 1. Establish the approved baseline

Select TICKETS.md's flat, hierarchical, or change-package basis. Resolve supplied effort/child paths through the root `issue.md`; read its selected scope, exact current source package and essential references, then resolve applicable review/approval evidence through model metadata and owning review logs rather than assuming sibling flat models. Validate route eligibility before decomposing: a bounded direct change goes to `implement`, with its root work entry but no synthetic tickets or ticket-set index.

Inspect relevant code, callers, repository guidance, and verification facilities using the already-read standard. Distinguish observed behavior, confirmed requirements, and unknowns. Production-design gaps return to the owning clarification stage and its original author/reviewer under TICKETS.md and the shared lifecycle; resume the same ticket-plan pair only after renewed source review and approval.

Reuse the resolved `.scratch/<work-slug>/` effort root. The author establishes the shared exclusion gate before writes, maintains `issue.md` as the definition/set index and root `issues/NN-<slug>.md` as tickets, and owns `tickets.review-fix-decisions.log.md`. Child entries define scoped models, with no child ticket pool. Resume or cut over existing artifacts under WORKFLOW-ARTIFACTS.md rather than create a competing plan. Planning creates no state file or substitute checklist; unresolved choices remain beside affected definitions.

Before writing or resuming plan edits, bind/resume the original ticket-plan author under **Persistent author/reviewer lifecycle** in WORKFLOW-ARTIFACTS.md, using the identity header of `tickets.review-fix-decisions.log.md`; bind its independent reviewer at first review. Retain this pair through repairs, final whole-set assessment, human revisions, upstream returns, and resumption; shared recovery and genuine-loss replacement rules apply. This plan pair is distinct from the implementation pairs later bound per ticket in execution metadata.

## 2. Find coherent work units and real dependencies

Map approved obligations to meaningful intermediate results and their concrete prerequisite outputs. Apply TICKETS.md's dependency, atomic-cutover, and intermediate-state criteria; do not invent architecture to make units independent. Assign integration and every approved macro-flow test an implementation/execution owner with actual prerequisites.

## 3. Size for a fresh implementation context

For each candidate identify the necessary source sections, code relationships, concepts, and prerequisite outputs. Apply the standard's whole-cycle context-fit criteria. Split independent objectives; merge fragments that lack useful results or divide an inseparable change. Ask only consequential unresolved decomposition choices, presenting alternatives and a recommendation; recover repository facts yourself and retain settled source decisions. Working drafts may evolve during clarification.

## 4. Write the index and fresh-context tickets

Apply TICKETS.md's artifact organization: complete coverage and planned dependency/integration ownership in the index, bounded actionable work in each ticket, authoritative definitions upstream. Use stable identifiers and exact references rather than copied specifications. Keep pending decomposition choices beside the affected definitions and integrate settled decisions and original evidence there; review submissions and finding-linked repairs belong in `tickets.review-fix-decisions.log.md`.

## 5. Rehearse the handoff and review the whole set

Walk the complete dependency order as an unfamiliar implementer: references resolve, inputs are available when needed, each increment is meaningful, and final composition covers the approved target. Perform all mandatory planning verification in TICKETS.md, including rendering and visually inspecting dependency diagrams. Correct known omissions and inconsistencies before independent review; return design gaps upstream rather than leave them for the reviewer.

Persist the identified review submission and current planning evidence, or finding-linked repair decisions and renewed evidence, in `tickets.review-fix-decisions.log.md`, then dispatch the bound independent read-only ticket-plan reviewer using reviewer-prompt.md's input/output contract. Supply the full initial package at first assignment or genuine replacement; later messages follow the shared incremental-input rules with the complete current set and sources accessible. Do not supply private author reasoning or substitute author self-review.

The assigned writer saves every returned report before repairs or gate advancement, following the shared finding lifecycle. Return findings to the original plan author to repair the canonical set and renew affected planning checks, then return the current set to the same reviewer for full-set assessment, including regressions outside prior findings. Upstream defects retain their owning author/reviewer; return approved source corrections and renewed evidence to this original plan reviewer. Only reviewer-confirmed closure counts. Missing access, mandatory evidence, or an incomplete/stale report blocks advancement; return defective reports to the same reviewer for correction. No iteration count waives the gate. Before a blocker or handoff, reconcile unresolved choices in their owning definitions and carry the exact missing evidence or decision in the handoff.

## 6. Obtain final human approval and stop

A current independent `Pass` with no unresolved findings/blockers permits requesting human approval. Present the complete reviewed index, objectives/granularity, dependencies, consequential tradeoffs, significant autonomous repair decisions with record links, and macro-flow ownership; ask explicitly for final approval of this set for later implementation. Upstream or proposed-split approval is insufficient.

The original plan author integrates human-requested changes, then returns the set to the same reviewer for full assessment before asking for approval of the resulting set. Apply shared revision integrity and TICKETS.md's resumed-set gate: resume these same roles and always review the full set before a resumed approved handoff; an unchanged set may retain its established human approval after that review. Use `Approved` only for the same currently passing, explicitly approved set.

Persist the actual scoped decision and reviewed source/set identities in `tickets.review-fix-decisions.log.md` before returning the approved index and essential references. Keep `issue.md` limited to specification navigation, not approval-record links. Otherwise return the draft with its exact blocker. Stop: no ticket execution, production/test code, later TDD policy, planning-only `delivery.md`, automatic remote publication, or commits.
