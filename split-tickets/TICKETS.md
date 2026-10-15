# Implementation Tickets: Content and Review Standard

These criteria guide both ticket generation and review. SKILL.md supplies the planning method; `artifact-layout` and `review-records` define storage and records.

## Approved basis

The plan implements an approved source package:

- **Flat:** requirements and the technical design that realizes them.
- **Heavyweight:** selected shared/child requirements, overall architecture and the applicable technical designs, approved in that order.
- **Change:** the complete change model and synchronized affected canonical sections. A bounded direct change needs no synthetic ticket set.

The root identifies the selected scope and authoritative sources. Approved design governs production decisions; observed legacy behavior is not a substitute. Required unresolved design blocks the affected planning work.

## Useful increments and whole-cycle context fit

A ticket has one coherent objective and a usable resulting state. Its context leaves room for understanding, implementation, verification and repair. A fresh implementer can find the necessary source/code sections and prerequisite outputs without reconstructing prior chat.

Boundaries follow useful work, not modules or file counts. Inseparable contract changes and caller updates belong together unless the approved design provides a staged transition. Non-obvious splits and joins have a clear rationale.

## Dependencies and composition

Dependencies name concrete required outputs and their reasons. They form an acyclic graph consistent with the tickets. The set covers the whole selected scope, including integration, caller changes and selected whole-flow verification.

A factual execution blocker describes a current obstacle. Clearing it does not remove the planned dependency or its required output.

## Root index and ticket content

There is one root index and ticket set, using `issue.md` and `issues/NN-<slug>.md` under `artifact-layout`.

The index identifies the approved basis, scope, ticket map, coverage and dependency graph. It is navigation and definition, not an execution diary.

Each ticket provides:

- Stable identity, objective, scope and exclusions.
- Necessary context and precise approved-source/code references.
- Prerequisites and the usable resulting state.
- Acceptance conditions and local verification, with later-owned whole-flow checks identified.
- An execution block for current status, factual blocker, actual implementer/reviewer handles and evidence references.

## Authority and evidence validity

Specification content, including the initial execution block and later plan changes, is shown and explicitly confirmed before writing. Final plan approval is distinct from permission to write. Candidate specification files are not a substitute for confirmation.

Review and approval apply to the actual current set and sources. Material changes require reassessment of affected conclusions. Records preserve findings and decisions, not a progress diary.

## Verification criteria

Every increment has meaningful completion checks. Selected whole-flow tests have real owners and prerequisites. Planning establishes this coverage without claiming future test results or requiring implementation/TDD execution.

References resolve, and the dependency diagram agrees with the declared output dependencies. The plan is usable in dependency order and complete as a whole.

## Whole-set coverage

A satisfactory plan preserves the approved design, divides it into context-fit usable increments, supplies fresh-context handoffs and accounts for integration and verification. Independent review assesses that complete set; human approval precedes separately authorized implementation.
