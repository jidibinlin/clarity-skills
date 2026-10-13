# Technical Model: Authoring and Review Standard

Content and evidence criteria for a complete scoped production design. Read this resource directly from the actual installed `clarify-technical-design` owner; an import does not load its SKILL, workflow, or prerequisites. The consuming stage owns execution and artifact permissions; `artifact-layout` defines file locations and ownership.

## Purpose and completeness

The target settles structure, object decomposition, algorithms, representations, contracts, coordination, resources, and failure handling before coding. Implementation translates it; it does not finish production design. Scope includes necessary interactions, not an unrelated repository inventory or speculative redesign.

Every scoped target includes a complete file-responsibility tree, distinctly labeled macro and micro Mermaid topology and sequence views, dataflow/concurrency semantics, complete data and interface definitions, and a project-grounded overall-flow test plan. Scale views to reality without omitting them or inventing infrastructure. Exact accessible unchanged definitions may be referenced after checking applicability, including external contract versions; a package link is not a definition.

## Heavyweight child realization

Initial child design identifies the root's approved shared/child requirements package and architecture, with current review/approval evidence. This does not impose heavyweight history on standalone work or coordinated change.

Connect every local view to inherited global guarantees by exact owner/path/section and verified revision. Each concrete shared definition, interface realization, and code responsibility has exactly one child technical owner; consumers reference that complete authority. Architecture approval does not complete child design. Requirements, modules, children, and tickets need not map one-to-one.

Trace guarantees to local operations, mechanisms, state owners, and integration participation. Inherit global flows by exact reference and add only necessary local coverage. Dependent children need compatible settled definitions, not circular prerequisites demanding that each be approved first: mutually dependent designs may constitute one explicitly scoped review/approval package assessing every child's full criteria. All applicable child/shared realizations must be complete and approved before the single root ticket set.

## Approved basis and decision rationale

Identify governing requirements, exact identities, scope, essential references, and decision authority. Preserve terminology, constraints, prohibitions, exceptions, quantitative bounds, and acceptance scenarios. Initial standalone design realizes approved requirements; initial heavyweight design also realizes approved architecture; coordinated change may establish confirmed requirements in its own package. Code limitations and technical preferences do not decide business rules.

Ground concepts in inspected processes, modules, objects, types, contracts, and callers. Cite reusable owners; justify each new abstraction by the need existing owners cannot serve. Identify displaced concepts and duplicate representations to retire. Lead each consequential decision with its background, decisive evidence/constraint, credible alternatives, and accepted consequences. Distinguish facts, constraints, confirmed choices, proposals, and assumptions; generic virtues are not rationale.

### Progressive design convergence

A reviewable design has concrete human-confirmation evidence for its consequential groups, not merely agreement on a direction followed by a privately completed blueprint. Evidence identifies the actual topology, sequences, declarations, file responsibilities, and contracts shown, the agreed scope, and its current applicability. Coupled views may form one group; no fixed round count or question per field is required.

Inspected exact unchanged reuse and previously confirmed concrete design remain valid while their structure, semantics, and governing basis remain applicable. Changed ownership, meaning, invariants, or use contracts invalidate that basis even when shape is unchanged. Direction agreement, silence, and permission given before seeing the proposal do not confirm concrete detail. Keep concise confirmation/reuse provenance beside the owning content, without a separate ledger or interview chronology.

#### Macro-first, dependency-led micro design

Macro decisions establish process/module topology, responsibility/state boundaries, dataflow/concurrency guarantees, and consequential mechanisms from approved scenarios. Their confirmed or validly reused basis precedes dependent micro detail; technology names alone explain no mechanism.

Micro design follows actual module dependencies from foundations upward: required configuration, stored/state representations, interfaces, and basic operations precede collaborations consuming them. Approved scenarios and coarse consumer needs bound these foundations; generic infrastructure is not a prerequisite by default. This is design dependency order, not call-stack, file, implementation, or ticket order.

Within a module, data, interfaces, topology, and sequences inform one another. Data/declaration-first is a heuristic: sequence-first is appropriate when lifecycle, ownership, or completion determines representation; coupled choices can be one bounded group. The rationale explains the actual dependency. Micro detail must realize macro guarantees; a changed premise requires a revised authoritative decision, not a silently weakened guarantee.

### Constraints for first-pass implementation

Specify consequential quality constraints where owned: canonical invariant/state owners, concept reuse, responsibility locality, allowed collaboration, error/resource ownership, and retirement of replaced paths. Cite applicable repository rules and resolve conflicts. These guide the first implementation, not a later structural cleanup.

Local expression choices remain with implementers only when structure, algorithms, contracts, and guarantees stay intact. Conformance findings need a basis in the design, requirements, repository rules, or applicable implementation/verification standard, not a preferred architecture. An incomplete or defective design needs clarification; neither silent redesign nor faithful implementation of known incorrect behavior is acceptable.

## File organization and responsibility tree

Provide the complete repository-relative target tree for scoped code, contracts, unchanged integration files, and needed verification/test locations. Assign every participating file its responsibility, objects/definitions/operations, and macro/micro relationships. Explicitly exclude unrelated areas.

Describe removals/relocations separately from the final tree, with final owners, migrated callers, and obsolete-path exits. Keep related state, behavior, and invariants together. Explain real reasons for multi-file objects and each part's role; a layer label, unlocated helper, pass-through file, or mechanical method split is not ownership. Follow repository conventions unless a concrete requirement justifies departure.

## Macro runtime and collaboration model

### Topology

Show complete scoped Mermaid topology: actual processes/boundaries, contained modules, external participants, responsibilities, and communications/dependencies. Distinguish modules/objects from independently running processes. Label crossings with mechanisms and contracts, and distinguish existing/new/changed/out-of-scope participants where material. A single process still has a real boundary.

### Data flow and state authority

For relevant data show origin, transformations, destination, and observable result/state change. Use topology when unambiguous, otherwise a focused flow view. Identify authoritative state/write owners, crossing representations (reference, copy, message, persistence), and exact payload/mapping definitions. Distinguish data movement, control, and dependency: calls do not imply synchronized state; caches do not imply authority.

### Concurrency and ordering

Specify actual processes, threads, event loops, tasks, or other execution contexts; permitted overlap, serialization, scheduling/coordinating owners, and mutation authority. Define the selected mechanism and scope establishing mutual exclusion, ordering, or consistency and the permitted overlapping outcomes. Labels such as async/thread-safe or process-local locks cannot establish unstated cross-process guarantees.

Resolve resource lifetime and completion. Queues, shared resources, overlapping requests, and asynchronous work need capacity, ownership, scheduling, completion, and errors. Include cancellation, shutdown, contention, and backpressure where required by this design, not as generic recovery infrastructure or invented behavior.

### Sequences

Provide macro Mermaid sequences for every distinct interaction pattern realizing approved scenarios: actual participants, initiation, direction, crossings, responses/completion, and synchronous/asynchronous semantics. Cover applicable success, rejection, failure, termination, and concurrency with explicit guards/alternatives or separate diagrams when combined paths would imply false ordering. Scenarios differing only in inputs may share a diagram. All sequences agree with topology, state/dataflow, concurrency, and contracts.

## Micro object and collaboration model

### Topology and ownership

Show complete Mermaid topology of concrete modules, objects, and definitions, mapped to files and macro participants. Specify responsibilities/state; distinguish creation, ownership, reference holding, dependency, and invocation. Resolve instantiation, multiplicity, lifetime/disposal, shared versus per-request/per-operation instances, and access/mutation ownership. Justify splits/merges; one class per noun or fragmented invariants is not decomposition.

### Sequences and operations

Concrete Mermaid sequences realize macro scenarios and required alternatives/failures using contract operation names. Show data, state transitions, effects, completion, and error propagation. Settle algorithms, transformations, coordination, and resource handling, including internal operations carrying design responsibility, through precise prose, pseudocode, or declarations rather than production-code transcription. An unspecified helper or algorithm left to coding is missing design.

Every macro interaction/guarantee traces to a concrete owner and mechanism: serialization, for example, needs a coordinating owner and operation sequence with sufficient scope.

## Complete data-structure definitions

Fully define owned state, collections, inputs/results, messages, and stored/transferred representations. New/changed structures require complete resulting definitions, not added-field patches. Unchanged definitions need exact checked references.

Specify canonical name/location, every field/variant/type, and applicable identifiers, units, optionality/nullability, defaults, valid states/ranges, relationships, ownership, mutability, and invariants. Define collection elements/keys, relied-upon ordering/uniqueness, consequential layout/encoding, transformations, retained/discarded information, invalid-input behavior, and invariant/transition authority.

Declarations without semantics and concepts without types are incomplete. Ellipses, example-only schemas, unspecified fields, or generic payloads cannot hide design. Intentional opacity needs a complete contract. Each concept has one canonical definition; other representations need a real purpose.

### Clarify actual declarations with the human

Confirmation evidence covers actual complete target-language declarations or precise schemas for every introduced/changed structure, including ordinary, internal, and anonymous ones. It identifies the resulting definition and baseline difference, purposes/types, stored versus derived values, keys/relationships, defaults/units/optionality, ownership/mutability, and invariants, with creation/update/consumption traced through sequences. Tables and relationship diagrams supplement declarations, not replace them.

Architecture, sequence, or risk agreement alone does not confirm declarations and semantics. Valid reuse follows **Progressive design convergence**; proposed choices reflect genuine tradeoffs, not blank-page questions or fabricated alternatives.

## Complete interface contracts

Define necessary module/object interfaces, process/external crossings, and internal operations relied on by micro design. External interfaces are not limited to HTTP. Every operation has an exact name, owner/location, signature/protocol, inputs/results linked to complete definitions, and applicable:

- Preconditions/checking owner, postconditions, state transitions, invariants, and observable effects.
- Success, rejection, errors, concrete representation, and propagation.
- Argument/result/resource ownership and lifetime.
- Synchronous/asynchronous completion, ordering, concurrency, and reentrancy.
- Compatibility, configuration, and quantitative performance constraints.

Explain genuine non-applicability. A signature alone or behavior without types/errors/owner is incomplete; consequential payloads, method splits, error types, and synchronization cannot be left to coding.

## Overall workflow integration test plan

Selection rests on inspected project integration-test guidance, runner/configuration, representative tests, fixtures/environment, and local/CI commands. Cite actual capabilities, reuse, and limitations; a framework name is not evidence. Missing necessary repository facts are blockers, not questions asking the human to invent capabilities.

Select a small set of representative macro business flows tied to scenarios and topology/sequences, from real entry through participating modules/processes to observable result. Include the main path and consequential alternatives/failures, not every field, boundary, combination, or interleaving. Isolated working modules do not prove collaboration.

Each flow identifies scenario/coverage reason, existing method/entry and actual participants, starting situation/actions/expected observable outcome, intended test location and setup/invocation, and material limits or substitutions. Substituted systems cannot prove real external behavior, cross-process coordination, or persistence guarantees. Necessary coverage beyond existing means needs a minimal justified approach, not a silently expanded harness.

This is a plan, not a suite or exhaustive test design. Detailed TDD cases, fixtures, assertions, and additional test files belong to implementation; their absence does not reopen settled production design. Implementation must exercise selected flows before release or joint-integration handoff. Distinguish that future obligation from checks and disposable probes actually run now.

## Consistency, evidence, and clean integration

Names, owners, references, representations, and contracts agree across requirements, tree, macro/micro views, data, and interfaces. Trace normal, boundary, failure, and relevant concurrency scenarios across views; this walkthrough does not require a test per scenario.

Every Mermaid diagram has actual current-content rendering and visual-inspection evidence checking boundaries, arrows, ordering, guards, concurrency, missing paths, and rendering errors. Parsing alone is insufficient; missing rendering/inspection capability blocks readiness. Checked referenced code/definitions and existing evidence or targeted disposable probes support feasibility-sensitive assumptions. Report actual exercise, keep exploratory code out of production, and distinguish future tests from current checks. Unresolved production assumptions block readiness.

The result is current integrated content in canonical owning sections, understandable without interviews, normative patches, override appendices, alternate drafts, or review diaries. Evidence and decisive rationale accompany the concepts they support.

## Delivery criteria

Apply all obligations above; these categories index coverage:

1. Governing basis and faithfulness.
2. Existing-design fit, rationale, reuse/cutovers, and first-pass constraints.
3. Complete file organization and final ownership.
4. Macro topology, sequences, dataflow/state authority, and concurrency.
5. Micro ownership, algorithms, collaboration, and lifetimes realizing macro guarantees.
6. Complete data definitions/semantics and concrete confirmation or valid reuse.
7. Complete interfaces, owners, and caller-relevant contracts.
8. Cross-view consistency, scenario traces, and dependency-led concrete decision closure.
9. Inspected project means and limited meaningful overall-flow coverage.
10. Current rendering, visual inspection, references, and necessary feasibility evidence.
11. Complete integrated target recoverable by an unfamiliar reader.
12. Attributable current source and confirmation/reuse evidence.
