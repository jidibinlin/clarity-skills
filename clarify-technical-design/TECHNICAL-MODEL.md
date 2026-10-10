# Technical Model: Authoring and Review Standard

This standard belongs to the `clarify-technical-design` skill. Load that skill by name in reference-only mode when another stage needs this resource; use its resolved companion location or complete current supplied content under the `workflow-artifacts` loading rules. Reading this standard does not start its author's workflow or require that workflow's execution prerequisites. The consuming stage determines the authorized scope and role; actual stage execution retains its existing gates.

## Purpose and completeness

This is the single authoritative content standard for producing and independently reviewing the technical realization of an approved requirements/domain model. Apply it while investigating, clarifying, writing, and repairing. Review uses these same requirements, not a separate quality rulebook.

Load `workflow-artifacts` by name through the Skill tool or the harness's equivalent registered resource mechanism and read its companion `WORKFLOW-ARTIFACTS.md` under its resource-resolution and supplied-content reuse rules before authoring, resuming, or reviewing. It governs private placement, exclusion, persistent records, revision identity, recovery, and transitions in addition to this content standard. New models use `.scratch/<work-slug>/technical.md` in the same work directory as `issue.md` and `issue.log.md`; existing authoritative project models may remain precisely referenced and synchronized under its location rule. The author/controller must establish and verify local Git exclusion before workflow writes, including worktree-aware exclusion resolution and tracked-file blocking. Never stage, commit, or publish workflow records; planning creates no `delivery.md`.

Use `issue.md` for current stage, scope/route, model and approval references, blockers, roles, and next action. Resume from it, applicable models, open findings, and latest evidence/decisions, reconciling actual sources before reuse. The controller (author in standalone mode) saves read-only reviewer reports in `issue.log.md`; reviewers do not write logs or exclusion rules. Record each round/reviewer, standards, exact source/model/code basis, verdict, category coverage, evidence/limits, stable finding IDs, and independent dispositions. Private files need path plus digest or another verifiable local revision; repository HEAD alone cannot identify ignored models or dirty/untracked code. Identify every relevant source and preserve enough evidence to compare current content without pretending logs are snapshots.

Persist reviews before repair or gate advancement; repair decisions, material rationale, addressed IDs and fresh evidence before new review; dispositions/current state before handoff; and recovery data before blockers or session/stage transitions. Author repairs are `addressed, awaiting review`, not self-closed findings; disputes remain open with counter-evidence until independent disposition. Save explicit human approval with exact scope/basis and a faithful short quotation or durable reference to the actual decision. Preserve prior outcomes and current applicability in the log, with only current approval metadata in the model. Apply the shared metadata-only revision rule. Task dispatches may carry review packages, but essential identities, decisions, findings, and evidence must persist locally.

The artifact must settle the scoped technical design before implementation. It describes the intended final system and code structure, not merely an implementation approach, a set of options, or a sequence of tickets. Do not reserve file organization, object decomposition, algorithms, data representation, interface details, coordination, or failure handling for the coding stage. Implementation translates the settled design into code; it does not complete the design.

"Complete" means complete for the approved change and its necessary interactions, not an inventory or redesign of the entire repository. Identify that scope explicitly. Reuse unchanged code and definitions through precise, accessible references. A reference must resolve the design question without guessing; a generic link to a package, an inaccessible definition, or an unspecified version of an external contract is not sufficient. Do not add speculative architecture to make a diagram or checklist look comprehensive.

The following are mandatory, including for small changes:

- A complete target file tree with file responsibilities and code ownership.
- Macro topology and macro sequence diagrams.
- Explicit data-flow direction and concurrency semantics.
- Micro topology and micro sequence diagrams.
- Complete data-structure definitions.
- Complete interface contracts.
- A project-grounded plan for a small set of overall workflow integration tests.
- A coherent account of the technical decisions connecting these views, with evidence and verification sufficient to review them.

Scale the size of each view to the actual system; do not omit a required view because the change is small. Do not invent processes, asynchronous messages, objects, or states merely to fill a view. Label the macro and micro views distinctly so neither is silently substituted for the other.

## Approved basis and decision rationale

Identify the approved requirements model and content revision, its scope and essential references, and evidence of its completed review and final approval. Preserve its terms, constraints, prohibitions, exceptions, quantitative bounds, and acceptance scenarios. The technical design must not quietly decide a missing business rule or replace the approved behavior with what existing code happens to support.

Inspect the relevant existing code before proposing new concepts. Identify reusable processes, modules, objects, types, and contracts with repository references. Describe the affected current structure only as needed to explain the target design, compatibility, or a real transition constraint. Explain why a proposed new abstraction is necessary, why an existing one cannot take the responsibility, and whether a superseded abstraction or duplicate representation must disappear.

Lead with the decision, then provide the background and actual decisive basis needed by an unfamiliar human or agent. Give consequential tradeoffs their relevant constraints, alternatives, and accepted consequences; do not repeat empty background/rationale headings for self-explanatory facts. Distinguish inspected facts, imposed constraints, confirmed choices, proposals, and unverified assumptions. Generic claims such as "best practice," "flexible," or "clean architecture" do not establish a decision's basis.

### Constraints for first-pass implementation

The approved technical model is the normative basis for later implementation and code-conformance review. Settle consequential quality constraints here, before coding: canonical state and invariant owners, reuse of existing concepts, responsibility locality, allowed collaboration, error and resource ownership, and retirement of replaced paths. Integrate each constraint and its actual rationale into the owning design section; do not create a parallel quality checklist or prescribe every local statement. Reference applicable repository rules precisely and resolve conflicts before approval.

Make these constraints concrete enough to guide the first implementation, rather than planning to repair its structure during code review. Local expression choices may remain with the implementer when they preserve the specified structure, contracts, algorithms, and guarantees. A later reviewer must tie required corrections to this approved design, its requirements basis, applicable repository rules, or the shared implementation/verification standard, not introduce a preferred architecture or an unstated style rule. If evidence exposes a defective or incomplete design, return it to clarification and renewed approval; neither silently implement a different design nor approve incorrect behavior merely because the code follows the document.

## File organization and responsibility tree

Provide a repository-relative file tree of the intended final organization. Every file participating in the scoped design must have an identified responsibility, either annotated in the tree or linked directly to a responsibility description. Include the concrete locations of new and modified code, definitions and contracts, and the unchanged files necessary to explain integration. Identify the verification/test locations needed by the design without turning them into implementation tickets. Explicitly exclude unrelated repository areas rather than using an incomplete tree to conceal missing design.

For each participating file, establish:

- The responsibility it owns and the objects, definitions, or operations assigned to it.
- Which existing role is preserved, changed, or replaced, when that distinction is necessary to understand the design.
- Its relationship to the runtime or module responsibilities shown in the diagrams.

Show the disposition of replaced or relocated code separately from the target tree, so removed files are not mistaken for part of the final structure. Name the final owner of migrated responsibilities and affected callers; do not leave a new implementation alongside an undefined obsolete path. This describes the structural cutover, not a chronological change log or task list.

A layer label such as "business logic" is not a file assignment. A proposed helper with no location or responsibility is unfinished design. Keep closely related state, behavior, and invariants together. If an object's implementation spans files, explain the actual reason and the responsibility of each part; do not split methods mechanically or create pass-through files without a role. Follow the repository's language and organization conventions unless a concrete requirement justifies changing them.

## Macro runtime and collaboration model

### Topology

Provide a complete Mermaid topology view of the scoped business collaboration. Identify processes and their boundaries, participating modules within them, external participants, and the communication or dependency relationships relevant to the change. Distinguish an object or module from a separately running process; a box named "worker" must not leave its execution location ambiguous.

Label nodes with their responsibilities and relationships with their meaning. State which participants are existing, changed, new, or outside the implementation scope where that distinction matters. Define the selected communication mechanism and interaction contract at each crossing. For a single-process design, show that actual boundary and its participants rather than omitting the view or inventing distributed infrastructure.

### Data flow and state authority

Show where each relevant data item originates, how it is transformed, where it goes, and which result or state change consumes it. This may be carried by the topology if direction and edge semantics remain unambiguous; otherwise supply a focused flow view.

Identify authoritative state, ownership of writes, and whether a crossing carries a reference, copied value, message, or persisted representation. Map payloads and transformations to the complete definitions below. Distinguish data movement from control flow and dependency; an unlabeled arrow must not stand for all three. Do not imply that replicas or cached values are authoritative, or that a call automatically synchronizes all state.

### Concurrency and ordering

Define the execution model: processes, threads, event loops, tasks, or other actual execution contexts; what can run concurrently; what must be serialized; and who schedules or coordinates the work. State who may modify shared state and the selected mechanism and scope of any required mutual exclusion, ordering, or consistency guarantee.

Define the lifetime and completion semantics needed by the scoped collaboration. Where the design uses queues, shared resources, overlapping requests, or asynchronous work, resolve their capacity, ownership, scheduling, and completion/error behavior rather than leaving them as generic boxes. Cover cancellation, shutdown, contention, or backpressure when they arise from the chosen design or approved requirements; do not invent new product behavior or generic recovery features just to populate a checklist.

Terms such as "async," "thread-safe," or "eventual consistency" alone are not a concurrency model. A process-local lock does not establish cross-process serialization. Explain how the actual selected mechanisms establish the stated guarantees and what outcomes are permitted when operations overlap.

### Sequences

Provide Mermaid sequence diagrams for the macro interactions that realize the approved scenarios. Show real participants, boundary crossings, direction, initiation, responses or completion notifications, and the selected synchronous or asynchronous semantics. Account for applicable success, rejection, failure, termination, and concurrent paths. Use separate diagrams or clearly scoped alternatives when combining them would imply false ordering or prerequisites.

Cover every distinct interaction pattern required by the approved behavior. Several scenarios may share one diagram if their guards and outcomes are explicit and can be traced through it; do not duplicate a diagram for every input value. The macro sequences must agree with the topology, data-flow direction, concurrency rules, and interface contracts.

## Micro object and collaboration model

### Topology and ownership

Provide a complete Mermaid topology view of the concrete modules, objects, and definitions implementing the scoped macro responsibilities. Map them to their files and macro participants. Define each object's responsibility and owned state; distinguish creation, ownership, reference holding, dependency, and invocation rather than representing them with indistinguishable arrows.

Resolve instantiation, instance multiplicity, lifetime, and disposal where the design has state or resources. Identify shared versus per-request/per-operation instances and who may access or mutate them. Reuse existing abstractions by their actual role and contract. Explain necessary splits and merges; do not add a class for every noun or distribute one invariant across uncoordinated objects.

### Sequences and operations

Provide Mermaid sequence diagrams showing how concrete objects and operations carry out the macro scenarios, including their required alternatives and failure paths. Use the actual operation names from the contracts. Show the relevant data passed, state transitions, side effects, and completion/error propagation. A participant named "helper" or "implementation detail" cannot hide undecided work.

Resolve the algorithms, transformations, coordination operations, and resource handling required to realize these sequences. Define internal operations as well as public entry points when they carry part of that design. Use precise prose, pseudocode, or declarations as appropriate, without making the document a transcript of production code. "Implement normally," "choose an algorithm later," and an unspecified collaborator do not settle a technical decision.

Trace each macro interaction and guarantee to its concrete realization. A macro serialization rule, for example, needs an actual coordinating owner and an interface/operation sequence whose scope enforces it. If the micro design cannot realize the macro rule, repair the design rather than silently weakening the rule.

## Complete data-structure definitions

Define all data structures needed by the scoped design: owned state, operation inputs and results, messages, and stored or transferred representations that it uses. Existing unchanged structures may be referenced exactly; new or changed structures must be fully defined. Show a complete resulting definition, not a patch containing only new fields.

For every definition, provide its canonical name and code location, complete fields or variants and their types, and the semantics needed to use it correctly. Resolve identifiers, units, nullability/optionality, defaults, valid ranges or states, relationships, ownership, mutability, and invariants wherever relevant. For collections, define element and key meaning and any relied-upon ordering or uniqueness. If layout, encoding, or representation affects the design, define it rather than leaving the choice to implementation.

For transformations between representations, identify the mapping, information preserved or discarded, and handling of invalid input required by the approved behavior. Establish where each invariant is enforced and who can perform a state transition. A field declaration alone is not a semantic definition; an informal concept description alone is not a complete type.

Do not use ellipses, "other fields," unbounded generic payloads, or example-only schemas to conceal unresolved definitions. Opaque values are acceptable only when opacity is an intentional, fully specified contract, not a missing design. Avoid multiple competing definitions of the same concept; reference one canonical definition and explicitly model a different representation only where necessary.

## Complete interface contracts

Define every interface needed for the scoped collaboration, including module/object interfaces used by other code and process or external protocol crossings. Also define the internal operations that the selected micro design relies on. "External" does not mean HTTP only.

Each operation must have an exact name, owner and code location, signature or protocol shape, inputs and outputs tied to the complete data definitions, and specified behavior. Resolve:

- Preconditions and the operation's responsibility for checking them.
- Postconditions, state transitions, invariants preserved, and observable side effects.
- Success, rejection, and error outcomes, including their concrete representation and propagation.
- Ownership/lifetime of arguments, results, and resources where relevant.
- Synchronous/asynchronous completion, ordering, and concurrency/reentrancy guarantees needed by callers.
- Any existing compatibility, configuration, or quantitative performance constraint on correct use.

State genuine non-applicability where needed instead of inventing error cases or infrastructure. An exact signature without behavioral obligations is incomplete, as is a behavioral description whose types, errors, or owner are unspecified. Resolve contract-affecting details now; do not instruct implementation to choose an error type, payload, method split, or synchronization policy later.

## Overall workflow integration test plan

**Inspect the project before selecting tests.** Read the existing integration-test guidance, runner/configuration, representative tests, fixture or environment setup, and relevant local/CI commands. Establish how this project actually exercises integrated behavior, what it can reuse, and its limitations. Cite the relevant repository evidence; do not infer capabilities from a framework name or prescribe a new harness before this investigation. If the evidence is inaccessible, report that gap rather than asking the human to invent repository facts.

Use those findings to select a small set of representative macro-level business flows, tied to the macro topology and sequence diagrams. Their purpose is to prevent a change being released or handed to joint integration before its basic collaboration works: exercise the path from the real entry through the participating processes or modules to the final observable outcome. Cover the main path and only consequential alternatives or failures, not a case for every interface, field, boundary value, state combination, or concurrency interleaving. Individually working modules do not establish that the macro flow works.

For each selected flow, record:

- The approved scenario and why this flow needs integration coverage.
- The existing testing method and entry point, the participating modules or processes, and the material limits of what is actually exercised.
- The starting situation, the high-level action sequence, and the observable overall result expected from the approved requirement and interface contracts.
- The intended test location and how the existing project setup and invocation will support it; reference existing conventions rather than redescribing the harness.

Preserve the distinction between real collaboration and replaced dependencies. An existing setup that substitutes an external system can still exercise a useful workflow, but cannot establish that external system's real behavior. Do not claim cross-process or persistence guarantees from a setup that replaces those interactions. If existing means cannot exercise a necessary overall flow, explain the gap and resolve the minimal approach through technical clarification instead of silently inventing infrastructure or expanding the test scope.

This stage defines overall integration coverage, not the complete testing strategy. Unit tests, fine-grained contract and boundary cases, detailed fixture construction, assertion code, additional test files, and other testing techniques belong to the later implementation-stage TDD instructions. Do not design that future TDD policy here or block technical approval because those details are absent. The requirement to settle production structure, data definitions, and interface behavior remains unchanged; this limited test plan does not reopen them.

The deliverable at this technical stage is a plan, not an executable test suite. The selected macro flows are to be implemented and exercised in the later implementation stage before release or handoff to joint integration; do not leave the first attempt to run them until after that handoff. A plan, successful compilation, or passing isolated tests is not evidence that these flows ran successfully. Distinguish planned flow tests from checks or disposable feasibility probes actually run. Unwritten future tests are not failed current design verification. Final human approval includes the selected macro flows and project-grounded testing approach, not an exhaustive test matrix.

## Consistency, evidence, and clean integration

Keep stable names and references across the requirements mapping, file tree, macro and micro views, definitions, and contracts. Every scoped responsibility has a concrete owner; each interaction has a contract; every payload and state has a defined representation. Walk approved normal, boundary, failure, and relevant concurrency scenarios through the entire design. A scenario must not work only in one view. These design walkthroughs do not require a separately specified integration test for every scenario.

Render and visually inspect all Mermaid diagrams. Check for misleading boundaries, arrow meanings, ordering, guards, concurrency, and missing paths as well as rendering errors. Parsing alone does not prove correctness. Keep verification results and artifacts available to the reviewer and tied to the current content. An unavailable renderer or necessary inspection capability blocks delivery rather than making diagrams optional.

Verify referenced code and definitions against the inspected repository. Support feasibility-sensitive execution assumptions with existing evidence or a targeted disposable probe. Distinguish observations from expectations; do not claim future production tests have already run. Check that the selected overall workflow tests use investigated project capabilities and have meaningful observable outcomes. Their implementation and detailed test strategy belong to the later implementation/TDD stage. An unresolved assumption on which the production design depends still prevents approval.

Maintain a clean canonical model throughout clarification and repair. Integrate corrections into owning sections and synchronize dependent views. No normative patch files, model-embedded changelogs/revision histories, override addenda, interview records, review reports, or cleanup commentary belong in the model. Necessary rationale and current-versus-target explanations remain beside the decision. Persist material review/repair/approval history and evidence in the shared work directory's `issue.log.md`, not Git history or conversation alone; this sidecar never overrides the integrated model.

## Delivery checks and second approval gate

The gate below governs full initial technical modeling through clarify-technical-design. Scoped changes to existing systems use the `clarify-change` skill (load by name in reference-only mode to consult its standard; execute only when that route is authorized), which imports this standard's design-content requirements while supplying its own baseline reconstruction, coordinated canonical updates, review and approval gate. That route may start without prior models and approve a complete bounded change for direct implementation; it does not invent historical approvals or waive target completeness. Its approval covers the exact affected target sections and necessary consistency, not unrelated historical content.

The author uses the requirements above throughout the work. A fresh independent reviewer applies the same standard to the complete current artifact and evidence, reporting these categories:

1. **Approved basis and faithfulness:** the current requirements input passed its own review and final approval; the technical model preserves it and has not invented business decisions.
2. **Existing-design fit and rationale:** inspected code grounds reuse, changes, new abstractions, and necessary cutovers; consequential choices and first-pass implementation constraints have their actual basis and can guide later conformance review.
3. **File organization:** the complete scoped target tree assigns every responsibility and definition to a concrete file and explains any relevant relocation or retirement.
4. **Macro completeness:** topology and sequence diagrams, data flow, state authority, and the actual concurrency/ordering model are complete and agree.
5. **Micro completeness:** topology and sequence diagrams resolve concrete ownership, collaboration, algorithms, and lifetimes and realize the macro model.
6. **Data completeness:** complete resulting definitions and semantics exist for all required state, payloads, inputs, outputs, and representations.
7. **Contract completeness:** every required interaction has a defined owner, exact interface, and complete caller-relevant behavior; internal operations do not hide undecided work.
8. **Cross-view consistency and decision closure:** approved scenarios can be traced through consistent views; no technical decision or necessary assumption remains for implementation to settle.
9. **Overall workflow integration coverage:** the project's existing integration-test methods were investigated before selecting a small set of relevant overall flows. The plan identifies the chosen method, entry, real collaboration and limits, expected outcome, and test location. An exhaustive interface-test matrix or detailed TDD test design is not required here.
10. **Verification:** every diagram was rendered and inspected, references were checked, and required feasibility evidence is available for the current content. Planned acceptance tests are not misrepresented as completed verification.
11. **Reviewability and clean handoff:** an unfamiliar reader can understand and evaluate the complete design from the model and explicit references, without interview history, patches, or an implementation ticket list.
12. **Private record integrity:** required location and verified exclusion, recovery entry, source/revision identities, persistent review/repair/evidence records, stable finding dispositions, and applicable approval evidence satisfy WORKFLOW-ARTIFACTS.md. Assess records available at this gate; do not demand the current report or future human approval before they occur.

These categories index the full standard, not a reduced replacement for it. Use [reviewer-prompt.md](reviewer-prompt.md) for independent-review inputs and results. Author self-review cannot satisfy this gate. Repair findings in place and obtain a new independent full review, including regressions outside previous findings. Missing independent review, necessary evidence, or mandatory verification is a blocker, not a waived requirement.

Retain `Draft` during clarification, repair, or blocked assessment. Only an independent `Pass` for the complete current artifact, with no unresolved findings or blockers, permits `Awaiting approval`. Only explicit final human approval of that reviewed artifact permits `Approved`. Early agreement, an author's claimed fix, and an old status label do not satisfy either gate.

Changes to the model's content, its approved requirements input, or essential references invalidate review and final approval for the affected artifact. Return to `Draft` and repeat review, repair, and final approval. Approval-metadata updates alone do not invalidate a content review. Always review resumed material before an approved handoff; an unchanged model may retain its established final approval after passing the new review.

Approval through this initial technical-model workflow authorizes subsequent ticket decomposition, not immediate implementation. The scoped change route identified above may instead authorize direct implementation of its independently reviewed, human-approved change package. Design changes outside an existing approved execution basis return to the applicable modeling route; code-conformance repairs remain in implementation.
