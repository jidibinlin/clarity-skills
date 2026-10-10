# Implementation Tickets: Authoring and Review Standard

## Purpose and stage boundary

Use this same standard while decomposing work, writing and repairing tickets, and independently reviewing the resulting set. The purpose is to keep each implementation task within a fresh context's comfortable reasoning scope while the whole set faithfully realizes the approved requirements and technical design.

Before authoring, resumption, or review, load `workflow-artifacts` by registered name using the Skill tool or the harness's equivalent named mechanism (omp: `skill://workflow-artifacts`) and read its WORKFLOW-ARTIFACTS.md from that skill's resolved installed location. Its private-storage, pre-write exclusion, clean-authority, record, revision, and recovery contract is mandatory. Reuse a supplied complete current standard or verified readable resource with its owning skill identity without recursively loading it; a summary is not sufficient. Missing or inaccessible required standards block affected work; report the exact dependency, without guessing sibling paths or auto-installing.

This reference belongs to `split-tickets`; companion links resolve relative to that installed skill/document under [SKILL.md](SKILL.md). Consulting the standard does not start ticket planning or its review/approval workflow. Keep installed skill resources separate from the target checkout and private work directory. Upstream routes are `clarify-requirements`, `clarify-technical-design`, or `clarify-change`; implementation routes to `implement`. Load a required stage by name in reference-only mode for standards, or execute it only when authorized under its existing gates.

A ticket is a work unit, not a code module or a new design document. The production structure, file ownership, objects, data definitions, interfaces, algorithms, concurrency model, and selected macro-flow tests come from the approved source basis defined below. Decomposition determines the work scope, prerequisites, sequence, and completion conditions; it does not finish or replace the design.

This stage produces a local ticket set and stops after review and final human approval. It does not implement code, execute the tickets, automatically publish issues, or prescribe the later implementation-stage TDD policy.

## Approved inputs and inspected baseline

Select and identify one authoritative requirements-and-technical source basis, with exact current paths, revisions, essential references, and approval evidence:

- **Requirements + technical route:** the current requirements and technical models, each with a passing independent review and final human approval. Verify that the technical model realizes the same approved requirements baseline.
- **Change route:** the `clarify-change` change model, its exact essential references, and synchronized affected sections of any existing canonical models. The current change package must have passed independent review and final human approval together. Its changed requirements and complete technical target supply the same authoritative basis as the original two models. Missing old separate requirements or technical documents, or missing historical approvals, are not blockers when scoped current evidence and the approved target are sufficient. Do not invent those documents or approvals as prerequisites.

Preserve the actual decisions, prohibitions, exceptions, and quantitative guarantees of the selected basis. A change basis must identify bounded scope, precise target owners, structure, definitions and contracts, dependencies and prerequisites, acceptance outcomes, and local and macro verification. Follow its explicit Changed/Unchanged/Unresolved dispositions for macro topology, data, concurrency and sequences; micro topology and sequences; file organization; and data/contracts. Exact essential references may supply unchanged definitions; an unresolved decision needed by a ticket is an upstream gap, not permission to invent it.

On the change route, use the change model's direct-versus-decomposed decision and supporting scope/context evidence. If the entire change fits one direct implementation unit, leave it to `implement` using the approved change document path and revision as identity; create no synthetic ticket or ticket-set index. Its root `issue.md` remains the work entry and `issue.log.md` holds direct execution records. This route produces actual ticket sets only when the change needs decomposition.

Inspect the relevant repository state, current callers, runtime evidence where available, and verification methods. Keep observed current behavior, confirmed requirements, and unknowns distinct. An observed legacy behavior is not an approved requirement or evidence that a bug should be preserved. Distinguish unchanged required behavior, work still required, and planned files or definitions. A future file does not have to exist now, but its role must resolve to the approved target. Existing code references must match inspected evidence rather than recollection.

Missing or conflicting source decisions return to requirements or technical clarification on the original route, or to `clarify-change` on the change route. Re-review and obtain human approval of the affected source package before resuming; the change route does not require rerunning the entire original two-stage pipeline. Do not fill the gap with "implementer decides," an extra design ticket, or a locally invented contract. Background and rationale belong beside the work they explain, scaled to what a reader unfamiliar with the conversation needs; do not invent reasons or repeat the interview chronology.

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

Do not equate one ticket with one file, object, method, or architectural layer. A coherent change can span files; successive tickets can work on the same file or object. Small work units must not introduce fragmentation into the approved production structure.

## Dependencies and intermediate states

A ticket is executable once its declared prerequisites are satisfied, not necessarily independently of every other ticket. For each blocker, name the concrete result it must supply and why this ticket cannot start without it. Use stable identifiers and links, not only vague references to "the previous step." A numbered order alone does not establish a dependency.

The dependency graph must be acyclic and agree with every ticket's declared blockers. Use genuine prerequisites; do not hide a missing dependency or manufacture a full serial chain without a reason. Conversely, absence of a blocking edge is not proof that simultaneous execution is safe: shared changes or incompatible intermediate states can still require coordination. This plan need not define an execution scheduler.

Describe the meaningful post-ticket state and the verification that establishes it. Preserve existing required behavior and a usable integration state at each step. A ticket need not make the entire new feature available, but it must not claim completion with broken existing callers, production stubs, or unverified fake behavior. An internal operation or planned migration can be a valid unit when its result is concrete and independently verifiable once dependencies are met.

Keep an atomic contract change and necessary caller updates together when separating them would break the design. If a valid atomic unit cannot be made context-bounded, return the problem to the selected route's upstream clarification for an approved cutover approach. Do not invent temporary APIs, compatibility shims, feature flags, extra abstractions, or file splits as a scheduling convenience. Carry out an explicitly approved transition when one already exists; ticket decomposition cannot create that architecture on its own.

## Artifact organization

Use `.scratch/<work-slug>/issue.md` as the work entry and set index, and `issues/NN-<slug>.md` for each ticket. Before writing, the author/controller must complete WORKFLOW-ARTIFACTS.md exclusion setup: resolve the actual Git root and local exclusion path, preserve existing rules, block tracked workflow paths, and verify effective exclusion. No project convention or old example bypasses this gate. Reuse the stable work directory; create only needed files. Each ticket has a same-stem `NN-<slug>.log.md` for later unit records; planning and whole-set records use root `issue.log.md`. Keep identifiers stable while revising a set; make changed dependencies explicit rather than relying on filenames as execution instructions.

### Set index

The parent `issue.md` is the current work/recovery map, not an execution diary or a separate index file. Alongside the shared contract's checkout identity, stage, roles, blockers, and next action, include:

- **Basis and scope:** the selected source route and exact approved source package with identifiable revisions, essential shared constraints, bounded objective, and exclusions. On the change route, include the change model, essential references and affected synchronized canonical sections, plus evidence that this current package passed independent review and final human approval together. Record the set's current approval status and applicable approval note here.
- **Ticket map:** stable identifier, descriptive title, link, intended result, and blockers for every ticket. Detailed work belongs in the ticket, not repeated in the index.
- **Coverage:** map every in-scope requirement, target technical obligation, cutover/caller migration or obsolete-path removal, and selected macro-flow test to the tickets that implement, integrate, or verify it. Use precise source headings or existing identifiers; do not require a new upstream identification scheme. On the change route, map the changed requirements and target technical sections, including retained invariants and referenced unchanged obligations, rather than treating the change as a prose patch to unavailable old models. If inspected existing code already satisfies an obligation, identify that evidence and any required preservation verification instead of inventing work or silently omitting it.
- **Dependencies and integration:** when blockers exist, provide an accurate Mermaid dependency graph with a stated arrow direction. When no dependencies exist, say so explicitly; do not draw a decorative graph. Identify where local results are joined, ownership and prerequisites for the approved cutover, and the owners of final macro-flow implementation and execution.

### Each ticket

Include the following information, organized clearly rather than as a chronological task log:

| Information | Required content |
| --- | --- |
| Identity and objective | Stable identifier, title, and one coherent implementation result. |
| Necessary context | Background and the actual reason for this unit where needed to understand or review it. |
| Authoritative references | Link to the index's selected source baseline and precise relevant requirements and target technical sections: both models on the original route, or the change model and its essential references/affected canonical sections on the change route. Identify the definitions, contracts, constraints, and repository locations needed for this work. |
| Scope and exclusions | The concrete changes this ticket owns, their already-approved code locations, and what it deliberately leaves to other tickets or outside the change. |
| Prerequisites | The selected approved source basis, blocking ticket links and the outputs they must provide, and any existing environmental prerequisite. Do not add absent historical documents or approvals to the change route. |
| Resulting state | What is true after this ticket, what later work can rely on, and how that differs from full-feature completion. |
| Acceptance | Observable conditions that establish the objective while preserving the relevant upstream rules. |
| Verification | The appropriate check or scenario, expected outcome, and relevant existing project method; identify later whole-flow verification where it cannot yet run. |
| Current state and record | Current ticket status, distinct from set planning approval, and the relative same-stem log reference when execution begins. Keep findings and evidence in the log, not in the specification. |

An agent starting with a ticket can read the small necessary part of the index, follow the cited source sections and prerequisite outputs, and begin without the author's chat. Do not require it to read every unrelated ticket or copy the complete source package into every ticket. References must resolve the work, not merely say "see the design." Summaries can explain relevance but cannot redefine an upstream type or contract.

## Verification responsibilities

Each ticket needs a way to establish its own meaningful result after prerequisites are met. This may be an existing check, a targeted behavior scenario, or a suitable local verification of the completed increment. It is not necessarily a full macro business-flow test. Do not force every ticket to traverse every layer if that makes the unit too large or fabricates unrelated work.

For new behavior, identify the acceptance outcome and relevant verification scope, not a full unit-test or boundary-case matrix. Detailed tests, fixtures, assertion code, and their red/green execution belong to the later implementation-stage TDD instructions. Do not move that entire test-design burden into the tickets or leave product behavior undecided under the name of TDD.

The selected macro-flow tests from the approved technical basis remain mandatory work on either route. Assign who will implement and run them after the required participants are available, and identify which prerequisites make that possible. They can belong to an integration ticket or to the ticket that completes the collaboration; a separate final-test ticket is not required by default. Do not defer every kind of verification to a final ticket while intermediate tickets have no completion evidence.

The resulting implementation must run those macro flows before release or handoff to joint integration. Compilation and individually passing module tests do not establish that the full collaboration works. Decomposition must account for this work, but does not execute it or claim future results. New production behavior or integration mechanisms needed to make a test possible must already be covered by the technical design, not invented in a ticket.

## Whole-set consistency and clean maintenance

Assess the set as a whole, not only each ticket in isolation. The required work must have clear ownership without omissions, conflicting implementations, duplicated responsibilities, or unclaimed integration. Follow the dependency order and confirm that prerequisite outputs exist when needed and that the final combined state is the approved target, not a collection of disconnected local successes.

Resolve document links and distinguish references to inspected code from proposed locations in the approved technical basis. Render and inspect any dependency diagram, checking it against the ticket blockers and arrow semantics. A parse-only check or a visually plausible graph does not prove correct dependencies. Unavailable required planning verification is a blocker. Do not require not-yet-implemented ticket code or future tests to pass at this stage.

Maintain one clean current `issue.md` and ticket set. Update owning sections and all affected references when splitting, merging, or correcting work; remove superseded proposed content. No interview logs, patches, changelogs, revision histories, override addenda, review reports, or cleanup narration belong in these canonical sections. Save process records in `issue.log.md`; ignored artifacts have no Git history to rely on. Necessary rationale is not a license to preserve old competing plans.

The author/controller records every review round and actual verdict before repair or gate advancement, using stable finding IDs and precise source/set revisions. Record each planning repair's decision, rationale, changes, and fresh evidence before re-review. Only the independent reviewer confirms closure/withdrawal; disputed findings remain open with counter-evidence. Record explicit human approval with actual decision evidence and scope/basis before handoff. Update the current entry before blockers or session/stage handoffs. Recover from it plus relevant sources, open findings and applicable evidence, not conversation memory.

Apply WORKFLOW-ARTIFACTS.md revision integrity: paths plus digests or another verifiable local mechanism identify private source/set bodies; HEAD alone does not. Identify every relevant source revision and consistently distinguish metadata-only updates from substantive changes. Existing authoritative project models may remain at their approved locations with precise references and synchronized owning sections. Logs never authorize target changes or reconstruct unavailable historical bodies.

## Delivery checks and ticket-set approval gate

The independent reviewer uses these categories to apply the full standard, not as a reduced replacement for it:

1. **Approved basis and fidelity:** the selected source package meets its route's current review and human-approval prerequisites; exact requirements and target technical references resolve, and the set preserves their decisions and required macro-flow verification. A change route is not blocked solely by absent old separate models or historical approvals.
2. **Coherent, bounded work:** each ticket has a useful objective, a manageable read/reasoning scope for implementation through repair, and no empty scaffolding or artificial file-sized split.
3. **Fresh-context handoff:** the ticket's necessary context, exact source references, code scope, and prerequisite outputs let an unfamiliar agent proceed without hidden history or design work.
4. **Structural fidelity:** the work respects the approved file organization, objects, data, contracts, and cutover; decomposition has not introduced a new architecture or compatibility path.
5. **Dependency and intermediate-state correctness:** blockers are concrete, accurate and acyclic; each ticket can reach its stated usable result when prerequisites are met.
6. **Local and macro verification:** every unit has meaningful completion evidence; whole-flow test work has explicit ownership and prerequisites; detailed TDD policy is not prematurely prescribed.
7. **Complete composition:** coverage and integration account for the whole approved change without gaps, conflicting ownership, or misleading claims that partial results finish the feature.
8. **Reviewability and verified plan:** rationale, links, coverage, ticket declarations, and any rendered dependency diagram agree; the set is clean and current, and planned execution is not presented as observed evidence. Shared artifact requirements are satisfied: private paths/exclusion evidence, recoverable current state, stable findings and repair records, exact source/review identities, and no log-based normative overrides.

Use [reviewer-prompt.md](reviewer-prompt.md) for the independent input and report contract. Author self-review cannot supply this gate. Repair findings, synchronize the entire set, and obtain a fresh full-set review, including effects outside the original finding. Missing necessary evidence, independent reviewer access, or mandatory planning verification is a blocker, not a waived criterion.

Give every reviewer the target repository/checkout and work identity, governing owners `split-tickets` and `workflow-artifacts`, and complete current standards/reviewer instructions or verified resolved installed resource locations. Explicitly assign read-only review with reference-only skill loading; do not require a fresh reviewer to reconstruct installation paths or start planning.

Use `Draft` while decomposing, repairing, or blocked. An independent `Pass` for the complete current set with no unresolved finding or blocker permits `Awaiting approval`. Only explicit final human approval of that reviewed set permits `Approved`. Neither upstream approval nor approval of a proposed split is approval of the finished set.

Changing a ticket, the index's substantive content, or a relevant approved baseline invalidates review and final approval for that set. Return to review and repair, then obtain final approval of the resulting set. Approval-metadata changes alone do not invalidate content review. On resumption, review the whole set before an approved handoff; an unchanged set can retain established final human approval after passing that review.

Set approval is permission for subsequent implementation under the applicable implementation workflow, not proof that any ticket ran or completed. Do not mark every ticket immediately runnable regardless of its blockers or auto-start execution. Keep this planning approval distinct from the execution lifecycle that later instructions will govern.

Persist planning approval and handoff in the work records, but do not create `delivery.md`: final implementation delivery belongs to the later implementation controller after verification and independent Pass. Keep the private workspace excluded; no approval authorizes publishing or committing it.
