# Implementation Tickets: Authoring and Review Standard

## Purpose and stage boundary

Use this same standard while decomposing work, writing and repairing tickets, and independently reviewing the resulting set. The purpose is to keep each implementation task within a fresh context's comfortable reasoning scope while the whole set faithfully realizes the approved requirements and technical design.

Before authoring, resuming, or reviewing, read this complete standard and WORKFLOW-ARTIFACTS.md from the named skill `workflow-artifacts`. Apply that skill’s loading/resource and reference-only rules. This document owns ticket content and eligibility; the shared contract owns workspace, records, revision integrity, and resumption. Workflow order and handoff belong to [SKILL.md](SKILL.md).

A ticket is a work unit, not a code module or a new design document. The production structure, file ownership, objects, data definitions, interfaces, algorithms, concurrency model, and selected macro-flow tests come from the approved source basis defined below. Decomposition determines the work scope, prerequisites, sequence, and completion conditions; it does not finish or replace the design.

This stage produces a local ticket set and stops after review and final human approval. It does not implement code, execute the tickets, automatically publish issues, or prescribe the later implementation-stage TDD policy.

## Approved inputs and inspected baseline

Select and identify one authoritative requirements-and-technical source basis, with exact current paths, revisions, essential references, and approval evidence:

- **Flat requirements + technical route:** the current requirements and technical models, each with a passing independent review and final human approval. Verify that the technical model realizes the same approved requirements baseline.
- **Hierarchical route:** the root `issue.md` identifies the selected requirements package (shared and child requirements), overall architecture, complete applicable child technical models, and exact source identities under WORKFLOW-ARTIFACTS.md’s **Hierarchical source packages and handoffs**. Resolve review/human-approval evidence through the owning model metadata and object logs, not an entry-file approval index. Validate cross-child requirements consistency and that architecture and technical models realize that same current scope. Resolve supplied child entries back to this root; no flat sibling-file assumption. Gates cover this scope and real prerequisites, not every future map item. Architecture alone is not implementation-complete: shared realization, file and contract details must already be settled in the owning technical models, with applicable independent review and human approval.
- **Change route:** the `clarify-change` change model, its exact essential references, and synchronized affected sections of any existing canonical models. The current change package must have passed independent review and final human approval together. Its changed requirements and complete technical target supply the same authoritative basis as the original two models. Missing old separate requirements or technical documents, or missing historical approvals, are not blockers when scoped current evidence and the approved target are sufficient. Do not invent those documents or approvals as prerequisites.

Preserve the actual decisions, prohibitions, exceptions, and quantitative guarantees of the selected basis. A change basis must identify bounded scope, precise target owners, structure, definitions and contracts, dependencies and prerequisites, acceptance outcomes, and local and macro verification. Follow its explicit Changed/Unchanged/Unresolved dispositions for macro topology, data, concurrency and sequences; micro topology and sequences; file organization; and data/contracts. Exact essential references may supply unchanged definitions; an unresolved decision needed by a ticket is an upstream gap, not permission to invent it.

Use the approved change model’s evidence-backed routing decision. A change fitting one complete implementation unit goes directly to `implement`; decomposition here creates actual ticket sets, not synthetic bookkeeping tickets.

Inspect the relevant repository state, current callers, runtime evidence where available, and verification methods. Keep observed current behavior, confirmed requirements, and unknowns distinct. An observed legacy behavior is not an approved requirement or evidence that a bug should be preserved. Distinguish unchanged required behavior, work still required, and planned files or definitions. A future file does not have to exist now, but its role must resolve to the approved target. Existing code references must match inspected evidence rather than recollection.

Missing or conflicting source decisions return to their actual owners: `clarify-requirements` for business rules, `clarify-architecture` for hierarchical global guarantees, `clarify-technical-design` for local/shared realization, or `clarify-change` for an approved-model change package. Load routed skills by name only for an authorized stage; reference-only loading starts no workflow. Resume after affected review and human approval; preserve valid unaffected scopes with an impact basis. A child cannot override global architecture. Tickets cannot defer design to implementers or invent contracts. Keep context-proportional background and actual deciding rationale beside the work, not interview chronology.

## Ticket size and fresh-context fit

A good ticket has one coherent objective and a meaningful resulting state. Its context must accommodate the entire implementation cycle: understanding, code reading, implementation, verification, failure investigation, and repair. A ticket that consumes the available reasoning scope just loading its prerequisites is too large even if its code change is short.

Assess fit from the actual work, not an arbitrary token, line, or file limit:

- The objective and completion conditions are concrete and bounded.
- The required concepts, invariants, states, interfaces, and code relationships form a coherent set that can be reasoned about together.
- Relevant source sections and code locations can be identified without requiring a new agent to reconstruct the whole project or a long earlier conversation.
- Prerequisite outputs are explicit; no hidden design decision or unresolved handoff must be solved during the ticket.
- Verification and likely failure investigation remain local enough to complete the task, not a separate unplanned project.

Document the material reason for a non-obvious split or merge; do not add speculative token estimates to every ticket. "Fits a context window" is a judgment supported by the bounded read set and objective, not a guarantee of model quality at a fixed token count.

Split multiple unrelated objectives or independent results when doing so reduces simultaneous reasoning. Merge fragments that offer no meaningful result, require repeated reconstruction of the same indivisible context, or leave an invalid half-change. Creating an empty class, directory, placeholder, fake implementation, or pass-through layer solely to report progress is not a useful work unit.

Do not equate a child requirement, code module, or ticket: these are different boundaries. A coherent change can span children and files; successive tickets can work on the same file or object. Small work units must not fragment the approved production structure.

## Dependencies and intermediate states

A ticket is executable once its declared prerequisites are satisfied, not necessarily independently of every other ticket. For each blocker, name the concrete result it must supply and why this ticket cannot start without it. Use stable identifiers and links, not only vague references to "the previous step." A numbered order alone does not establish a dependency.

The dependency graph must be acyclic and agree with every ticket's declared blockers. Use genuine prerequisites; do not hide a missing dependency or manufacture a full serial chain without a reason. Conversely, absence of a blocking edge is not proof that simultaneous execution is safe: shared changes or incompatible intermediate states can still require coordination. This plan need not define an execution scheduler.

Describe the meaningful post-ticket state and the verification that establishes it. Preserve existing required behavior and a usable integration state at each step. A ticket need not make the entire new feature available, but it must not claim completion with broken existing callers, production stubs, or unverified fake behavior. An internal operation or planned migration can be a valid unit when its result is concrete and independently verifiable once dependencies are met.

Keep an atomic contract change and necessary caller updates together when separating them would break the design. If a valid atomic unit cannot be made context-bounded, return the problem to the selected route's upstream clarification for an approved cutover approach. Do not invent temporary APIs, compatibility shims, feature flags, extra abstractions, or file splits as a scheduling convenience. Carry out an explicitly approved transition when one already exists; ticket decomposition cannot create that architecture on its own.

## Artifact organization

Use the resolved effort root’s `issue.md` as the one set definition/index and root `issues/NN-<slug>.md` for all ticket specifications. Planning uses `tickets.review-fix-decisions.log.md`, not a synthetic `tickets.md` or any state file. Execution later updates a compact non-normative block in each existing ticket and uses its own review log. No substitute progress/checklist files, child ticket pools, child implementation controllers, or child delivery summaries. The author/controller completes the shared exclusion gate before writes and assigns one writer per ticket or review log; reviewers remain read-only. Apply WORKFLOW-ARTIFACTS.md for storage, ownership, resumption and legacy cutover; preserve stable ticket IDs when revising dependencies.

### Set index

The parent `issue.md` is the clean work definition and navigation entry, not current execution state. Alongside its checkout and route, include:

- **Basis and scope:** the selected source route and exact approved source package with identifiable revisions, essential shared constraints, bounded objective, and exclusions. Hierarchical packages include root and child source sections and their owning entries; the map records decomposition, not implementation authority. Change packages include synchronized canonical sections approved together. The entry links specifications, package revisions and ticket definitions, not approval records. Resolve source approval through model metadata and owning logs, and set approval through `tickets.review-fix-decisions.log.md`; no separate approval index or planning-status ledger.
- **Ticket map:** stable identifier, descriptive title, specification link, intended result, and planned prerequisites for every ticket. Detailed work and compact execution status belong in the ticket; the controller derives runtime readiness from ticket status, dependencies, actual incorporated code and applicable evidence.
- **Coverage:** map every in-scope requirement, target technical obligation, cutover/caller migration or obsolete-path removal, and selected macro-flow test to the tickets that implement, integrate, or verify it. Use precise source headings or existing identifiers; do not require a new upstream identification scheme. On the change route, map the changed requirements and target technical sections, including retained invariants and referenced unchanged obligations, rather than treating the change as a prose patch to unavailable old models. If inspected existing code already satisfies an obligation, identify that evidence and any required preservation verification instead of inventing work or silently omitting it.
- **Dependencies and integration:** when planned dependencies exist, provide an accurate Mermaid dependency graph with a stated arrow direction. When none exist, say so explicitly; do not draw a decorative graph. Identify where local results are joined, ownership and prerequisites for the approved cutover, and the owners of final macro-flow implementation and execution.

### Each ticket

Include the following information, organized clearly rather than as a chronological task log:

| Information | Required content |
| --- | --- |
| Identity and objective | Stable identifier, title, and one coherent implementation result. |
| Necessary context | Background and the actual reason for this unit where needed to understand or review it. |
| Authoritative references | Link to the root index’s selected baseline and precise applicable requirements/technical sections: flat models, hierarchical shared requirements/architecture/child models, or the change package’s affected authorities. Include required cross-child contracts and dependencies, not the whole effort archive. Identify definitions, constraints, and code locations needed for this work without copying upstream specifications. |
| Scope and exclusions | The concrete changes this ticket owns, their already-approved code locations, and what it deliberately leaves to other tickets or outside the change. |
| Prerequisites | The selected approved source basis, blocking ticket links and the outputs they must provide, and any existing environmental prerequisite. Do not add absent historical documents or approvals to the change route. |
| Resulting state | What is true after this ticket, what later work can rely on, and how that differs from full-feature completion. |
| Acceptance | Observable conditions that establish the objective while preserving the relevant upstream rules. |
| Verification | The appropriate check or scenario, expected outcome, and relevant existing project method; identify later whole-flow verification where it cannot yet run. |
| Execution metadata | One compact non-normative block for current status, current blocker if any, original implementer/reviewer handles when assigned, and applicable review/evidence references, including this ticket’s `NN-<slug>.review-fix-decisions.log.md`. Update fields in place during execution; do not repeat planned tasks, add a step checklist or chronological progress, or create empty future records. Keep execution status distinct from ticket-specification approval. |

An agent starting with a ticket can read the small necessary part of the index, follow the cited source sections and prerequisite outputs, and begin without the author's chat. Do not require it to read every unrelated ticket or copy the complete source package into every ticket. References must resolve the work, not merely say "see the design." Summaries can explain relevance but cannot redefine an upstream type or contract.

## Verification responsibilities

Each ticket needs a way to establish its own meaningful result after prerequisites are met. This may be an existing check, a targeted behavior scenario, or a suitable local verification of the completed increment. It is not necessarily a full macro business-flow test. Do not force every ticket to traverse every layer if that makes the unit too large or fabricates unrelated work.

For new behavior, identify the acceptance outcome and relevant verification scope, not a full unit-test or boundary-case matrix. Detailed tests, fixtures, assertion code, and their red/green execution belong to the later implementation-stage TDD instructions. Do not move that entire test-design burden into the tickets or leave product behavior undecided under the name of TDD.

The selected macro-flow tests from the approved source package remain mandatory on every source route. Assign who will implement and run them after required participants are available, including cross-child flows owned by shared requirements/architecture, and identify their real prerequisites. They can belong to an integration ticket or to the ticket completing the collaboration; a separate final-test ticket is not required by default. Do not defer all verification to a final ticket while intermediate tickets lack completion evidence.

The resulting implementation must run those macro flows before release or handoff to joint integration. Compilation and individually passing module tests do not establish that the full collaboration works. Decomposition must account for this work, but does not execute it or claim future results. New production behavior or integration mechanisms needed to make a test possible must already be covered by the technical design, not invented in a ticket.

## Whole-set consistency and clean maintenance

Assess the root set as a whole against its selected authorized scope, not each child or ticket in isolation. Trace shared and child obligations, cross-child contracts/callers, real prerequisite outputs and macro flows to explicit implementation/integration/verification owners. Check consistent shared realization and file ownership across technical models; competing definitions or unowned design return upstream. Walk dependency order and confirm meaningful intermediate states and complete final composition. An atomic contract and caller cutover may cross children in one ticket; local model Passes cannot prove this composition.

Resolve current document links and distinguish references to inspected code from proposed locations in the approved technical basis. Validate future ticket review-log paths without creating empty files. Render and inspect any dependency diagram, checking it against the ticket blockers and arrow semantics. A parse-only check or a visually plausible graph does not prove correct dependencies. Unavailable required planning verification is a blocker. Do not require not-yet-implemented ticket code or future tests to pass at this stage.

Maintain one clean current index and set under WORKFLOW-ARTIFACTS.md’s clean-authority and revision rules. Splits, merges, and repairs update owning sections, coverage, references, and dependencies together; remove superseded proposed work. Keep unresolved decomposition choices beside the affected ticket or index definitions; integrate settled choices and original evidence there. Preserve review submissions, full reviewer reports, finding-linked repair decisions/evidence, and scoped human approvals in `tickets.review-fix-decisions.log.md` under the shared lifecycle. Upstream design decisions stay in their owning models and review records; a ticket-plan finding links its referral and approved resolution rather than duplicating that discussion.

## Delivery checks and ticket-set approval gate

The independent reviewer uses these categories to apply the full standard, not as a reduced replacement for it:

1. **Approved basis and fidelity:** the route’s approved inputs and inspected-baseline criteria.
2. **Coherent, bounded work:** ticket size and whole-cycle fresh-context fit.
3. **Fresh-context handoff:** complete actionable ticket content and exact references.
4. **Structural fidelity:** approved production organization and cutover, without ticket-created design.
5. **Dependency and intermediate-state correctness:** real acyclic blockers and meaningful usable results.
6. **Local and macro verification:** the full verification-responsibility criteria, with later TDD boundaries.
7. **Complete composition:** whole-set coverage, ownership, and integration.
8. **Reviewability and verified plan:** clean consistent artifacts, rationale, checked references and rendered/visually inspected diagrams, truthful evidence, and shared artifact integrity.

Use [reviewer-prompt.md](reviewer-prompt.md) for the independent role, complete input package, and report contract. Every full-set round uses a fresh independent reviewer, including repaired sets. Author self-check cannot supply this gate; mandatory planning verification or reviewer-access gaps block it.

A set remains a draft while decomposing, repairing, or blocked. An independent `Pass` for the complete current set with no unresolved finding or blocker permits requesting approval. Only explicit final human approval of that reviewed set permits calling it approved; derive that disposition from the current set and its review/approval evidence, not a planning-state file. Neither upstream approval nor approval of a proposed split is approval of the finished set.

Changing a ticket specification, the index's substantive content, or a relevant approved baseline invalidates review and final approval for that set. Return to review and repair, then obtain final approval of the resulting set. Exclude the compact non-normative ticket execution block from ticket-specification review revisions under the shared metadata convention; changes only to status, blocker, bound-role handles or evidence references do not invalidate specification approval or authorize normative changes. Approval-metadata changes alone likewise do not invalidate content review. On resumption, review the whole set before an approved handoff; an unchanged set can retain established final human approval after passing that review.

Set approval is permission for subsequent implementation under the applicable implementation workflow, not proof that any ticket ran or completed. Do not mark every ticket immediately runnable regardless of its blockers or auto-start execution. Keep this planning approval distinct from the execution lifecycle that later instructions will govern.

Planning-only work creates no `delivery.md`. Before handoff the author/controller persists scoped final approval with the exact reviewed set/source basis in `tickets.review-fix-decisions.log.md`. Keep the entry’s specification references current without adding approval links or a status ledger. Surface consequential autonomous repair decisions and their records when requesting approval. Approval does not authorize execution, publication, or commits.
