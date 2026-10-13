# Implementation Tickets: Content and Review Standard

A ticket is a bounded work unit, not a module or design document. Approved sources own production structure, files, objects, data, interfaces, algorithms, concurrency and selected macro-flow tests. Decomposition determines scope, prerequisites, sequence and completion—not missing design. This standard defines plan quality; SKILL.md owns authoring/review order, write permission and approval validity. `artifact-layout` owns artifact paths, names, purposes and ownership. Record-schema loading is controlled by the stage's actual record gate, not this content standard.

## Approved inputs

Identify the authoritative basis by exact paths/sections, verifiable revisions, essential references and current scoped review/human-approval evidence:

- **Flat:** approved requirements and complete technical design realizing the same requirements baseline.
- **Heavyweight:** a root-selected composed package of shared and child requirements approved before overall architecture; approved architecture before child technical design; all complete approved technical models needed for selected scope and real prerequisites before ticketing. Shared realization, ownership, contracts and cross-child consistency must be settled. Architecture or separate child Passes alone are insufficient. There is one global root ticket set, controller and delivery; children return to the root, not separate execution pools. Unrelated future map items are not prerequisites.
- **Change:** approved complete change model, essential references and synchronized affected canonical sections approved together. Its changed requirements and scoped technical target can replace absent historical models/approvals. Validate scope, owners/structure/definitions/contracts, prerequisites, acceptance and local/macro verification. Honor Changed/Unchanged/Unresolved dispositions across macro topology/data/concurrency/sequences, micro topology/sequences, file organization and data/contracts. Precise references or evidenced reconstruction can supply unchanged definitions; necessary unresolved decisions block ticketing. A complete bounded direct change follows its approved route to `implement`, without a bookkeeping ticket.

Root `issue.md` defines package selection and identities; approval evidence stays in owning logs or model metadata, not an approval registry or new manifest. Preserve actual decisions, prohibitions, exceptions and quantitative guarantees. Inspect relevant code, callers and verification facilities. Distinguish observed legacy behavior from confirmed requirements and unknowns; identify satisfied obligations, remaining work and approved future locations.

Business-rule gaps belong to `clarify-requirements`, global guarantees to `clarify-architecture`, local/shared realization to `clarify-technical-design`, and approved-model change packages to `clarify-change`. Source conflicts return to their authority, never child/local overrides. These are referral destinations, not workflow imports or authorization to execute them.

## Whole-cycle context fit

Each ticket has one coherent objective and a meaningful resulting state. Its bounded read set must leave room for understanding, code reading, implementation, verification, failure investigation and repair. Assess actual concepts, invariants, states, interfaces and relationships—not token, line or file quotas.

A fresh implementer must find precise source/code sections and explicit prerequisite outputs without reconstructing the project or prior chat. No hidden design decision or unplanned verification project may remain. Explain non-obvious splits/merges with their actual rationale.

Split independent objectives when that reduces simultaneous reasoning. Merge fragments that repeat indivisible context, leave an invalid half-change or lack useful results. Empty classes/directories, placeholders, fake behavior and pass-through layers made only as progress are not units. Requirements, modules and tickets are different boundaries; a ticket may span children or revisit a file.

## Dependencies and usable increments

Every blocker names a stable ticket ID, concrete required output and reason. The graph is acyclic and agrees with ticket blockers; ordering numbers are not dependencies, and independent units need no invented serial chain. Missing edges do not establish parallel safety where files, state or contracts overlap.

Describe what becomes usable and how to verify it after prerequisites. An internal operation or migration is a useful increment without independent deployment or full-feature exposure. Preserve required existing behavior and callers; stubs, broken callers and fake/unverified behavior are not usable increments.

Keep atomic contract changes and required caller updates together. If they cannot fit a context, return upstream for an approved cutover. Ticketing cannot invent temporary APIs, compatibility shims, flags, abstractions or file splits for scheduling convenience; an already-approved transition remains valid.

## Root index and tickets

Use the root entry, stable ticket specifications and ticket-plan review log defined by `artifact-layout` (`issue.md`, `issues/NN-<slug>.md` and `tickets.review-fix-decisions.log.md`). The index is definition/navigation, not approvals, execution status or a diary. No synthetic `tickets.md`, state files, child pools or duplicate checklists.

The index contains:

- **Basis and scope:** checkout, route, objective/exclusions, exact approved package identities, authoritative links and shared constraints; selected root/child sections or synchronized change sections where applicable.
- **Ticket map:** stable ID, title, specification link, intended result and planned prerequisites.
- **Coverage:** an implementation/integration/verification owner for every in-scope requirement, technical obligation, caller migration, cutover, obsolete-path removal and selected macro flow. Cite existing source headings/IDs. Include retained change invariants; satisfied obligations need inspected evidence and preservation checks, not fake work.
- **Dependencies and integration:** accurate Mermaid for actual dependencies, with arrow direction stated; explicitly say when there are none. Identify joins, cutover ownership/prerequisites and final macro-flow owners.

Each ticket contains:

| Field | Required content |
| --- | --- |
| Identity and objective | Stable ID, title, one coherent implementation result. |
| Necessary context | Background and deciding rationale needed for this unit. |
| Authoritative references | Precise applicable source sections, root baseline, cross-child contracts and inspected code locations; citations rather than copied definitions. |
| Scope and exclusions | Owned changes/approved locations and work belonging elsewhere. |
| Prerequisites | Blocker links and concrete outputs, approved basis and environmental requirements. |
| Resulting state | Usable output and what later work may rely on, distinct from feature completion. |
| Acceptance | Observable objective and preserved upstream obligations. |
| Verification | Suitable project check/scenario, expected outcome and explicitly later-owned whole-flow checks. |
| Execution block | Compact current status, blocker, real implementer/reviewer handles and evidence references under `artifact-layout` file-ownership rules; no progress history or speculative role placeholders. |

Relevant index sections, exact references and prerequisite outputs must suffice without unrelated tickets or chat. “See the design” alone is not actionable. All ticket/index changes, including metadata, require prior exact human confirmation. Keep one clean current set; coordinated splits/merges update coverage, references, blockers and deletions together. Logs cannot redefine the plan.

## Verification and review coverage

Each unit needs local completion evidence after prerequisites; it need not traverse every layer or own a full business flow. Define acceptance and verification scope, not exhaustive fixture/assertion matrices or detailed TDD policy. Undecided product behavior cannot be deferred to tests.

Every approved macro-flow test remains mandatory, including shared/cross-child flows. Assign its implementation and execution to an integration ticket or the ticket completing collaboration, with real prerequisites; no separate final-test ticket is required by default. Final code must execute those flows before release or joint-integration handoff. Planning assigns this work but neither executes it nor claims future results. Production mechanisms needed for verification must already be designed.

Review the complete set through these categories:

1. **Approved basis and fidelity:** valid sources, preserved obligations and inspected baseline.
2. **Coherent bounded work:** useful objectives and whole-cycle context fit.
3. **Fresh-context handoff:** actionable content and precise references.
4. **Structural fidelity:** approved organization and atomic cutover without invented design.
5. **Dependencies and intermediate states:** real acyclic blockers and usable increments.
6. **Local and macro verification:** appropriate evidence owners and later-TDD boundary.
7. **Complete composition:** whole-set coverage, shared ownership and final integration.
8. **Reviewable verified plan:** meaningful rationale, consistent artifacts, resolved links, rendered and visually inspected diagrams, truthful evidence and exact write confirmations.

Walk the complete dependency order and final composition, not isolated tickets. Resolve current links; distinguish inspected existing code from approved future locations. Validate future log paths without creating empty logs. Actually render and visually inspect each dependency diagram for correct arrow semantics and agreement with blockers; parsing or visual appearance alone cannot establish correct edges. Missing mandatory planning evidence blocks approval; future implementation results are not planning prerequisites.

Substantive source/set changes invalidate affected approval/evidence immediately, even while metadata correction awaits confirmation; unaffected scopes need an explicit impact basis. Set approval permits a later authorized implementation stage, not execution itself or a claim that blocked tickets are ready.
