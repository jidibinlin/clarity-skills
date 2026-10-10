---
name: split-tickets
description: Use after a flat requirements/technical or hierarchical requirements/architecture/child-technical package has passed applicable review and human approval to split implementation work or revise its global ticket set; also use for an approved change package needing decomposition. Not for production design, coding, or executing tickets.
---

# Split Tickets

Turn the approved source basis into coherent implementation units that fit a fresh context through understanding, implementation, verification, and repair. Split the work, not the approved code structure.

Before starting or resuming, load `workflow-artifacts` by name and read its complete WORKFLOW-ARTIFACTS.md, then all of [TICKETS.md](TICKETS.md), **before investigation, questions, or planning**. They govern shared artifacts and substantive ticket criteria respectively. Apply `workflow-artifacts`' loading/resource and reference-only rules to every role; loading this skill for standards does not authorize its workflow. Read [reviewer-prompt.md](reviewer-prompt.md) at first review dispatch.

## 1. Establish the approved baseline

Select TICKETS.md's flat, hierarchical, or change-package basis. Resolve supplied effort/child paths through the root `issue.md`; read its selected scope, exact current source package, essential references, and applicable review/approval evidence rather than assuming sibling flat models. Validate route eligibility before decomposing: a bounded direct change goes to `implement`, with its root work entry but no synthetic tickets or ticket-set index.

Inspect relevant code, callers, repository guidance, and verification facilities using the already-read standard. Distinguish observed behavior, confirmed requirements, and unknowns. Production-design gaps return to the owning clarification stage under TICKETS.md; resume only after renewed source review and approval.

Reuse the resolved `.scratch/<work-slug>/` effort root. The author establishes the shared exclusion gate before writes, maintains its `issue.md` as the single entry/set index and root `issues/NN-<slug>.md` as tickets, and records planning in root `issue.log.md`. Child entries retain only scoped model recovery; they create no ticket pool. Recover existing state under WORKFLOW-ARTIFACTS.md rather than create a competing plan. New or repairing sets remain `Draft`.

## 2. Find coherent work units and real dependencies

Map approved obligations to meaningful intermediate results and their concrete prerequisite outputs. Apply TICKETS.md's dependency, atomic-cutover, and intermediate-state criteria; do not invent architecture to make units independent. Assign integration and every approved macro-flow test an implementation/execution owner with actual prerequisites.

## 3. Size for a fresh implementation context

For each candidate identify the necessary source sections, code relationships, concepts, and prerequisite outputs. Apply the standard's whole-cycle context-fit criteria. Split independent objectives; merge fragments that lack useful results or divide an inseparable change. Ask only consequential unresolved decomposition choices, presenting alternatives and a recommendation; recover repository facts yourself and retain settled source decisions. Working drafts may evolve during clarification.

## 4. Write the index and fresh-context tickets

Apply TICKETS.md's artifact organization: complete coverage and dependency/integration ownership in the index, bounded actionable work in each ticket, authoritative definitions upstream. Use stable identifiers and exact references rather than copied specifications. Integrate revisions into the current owning sections and synchronize the whole set; keep review/repair history in `issue.log.md`.

## 5. Rehearse the handoff and review the whole set

Walk the complete dependency order as an unfamiliar implementer: references resolve, inputs are available when needed, each increment is meaningful, and final composition covers the approved target. Perform all mandatory planning verification in TICKETS.md, including rendering and visually inspecting dependency diagrams. Correct known omissions and inconsistencies before independent review; return design gaps upstream rather than leave them for the reviewer.

Persist planning/repair decisions and current evidence in `issue.log.md`, then dispatch a **fresh independent read-only reviewer for every full-set round** using reviewer-prompt.md's complete input/output contract. Do not supply private author reasoning or substitute author self-review.

The author saves every returned report before repairs or gate advancement, following the shared finding lifecycle. Repair the canonical set, renew affected planning checks, and request another fresh full-set review, including regressions outside prior findings. Only reviewer-confirmed closure counts. Missing access, mandatory evidence, or an incomplete/stale report blocks advancement; no iteration count waives the gate. Update the work entry before a blocker or handoff.

## 6. Obtain final human approval and stop

A current independent `Pass` with no unresolved findings/blockers permits `Awaiting approval`. Present the complete reviewed index, objectives/granularity, dependencies, consequential tradeoffs, and macro-flow ownership; ask explicitly for final approval of this set for later implementation. Upstream or proposed-split approval is insufficient.

Integrate requested changes, renew full review, and ask for approval of the resulting set. Apply shared revision integrity and TICKETS.md's resumed-set gate: always review the full set before a resumed approved handoff; an unchanged set may retain its established human approval after that review. Use `Approved` only for the same currently passing, explicitly approved set.

Persist the actual decision in `issue.log.md` and update `issue.md` before returning the approved index and essential references. Otherwise return the draft with its exact blocker. Stop: no ticket execution, production/test code, later TDD policy, planning-only `delivery.md`, automatic remote publication, or commits.
