# Technical Model: Authoring and Review Standard

Use these criteria to shape the design and review it. The consuming skill supplies the working method; `artifact-layout` supplies artifact locations and ownership. Resolve this resource through the registered `clarify-technical-design` owner. Selective imports include the named sections and their subsections, not the owner's workflow.

## Purpose and completeness

A complete scoped design settles consequential structure, representations, algorithms, contracts, coordination and failure handling. Ordinary implementation choices remain with the implementing model.

The target includes a complete file-responsibility tree, macro and micro Mermaid topology and sequences, dataflow and concurrency semantics, full data definitions and interface contracts, and a project-grounded macro-flow test plan. Applicable unchanged definitions may be referenced precisely rather than copied.

## Heavyweight child realization

A child realizes the root's approved requirements package and architecture. Its local owners and operations implement the inherited guarantees, and each shared realization has one child authority referenced by consumers. Mutually dependent children may form one coordinated technical review package. All scoped child realizations must be complete and approved before one root ticket set.

## Approved basis and decision rationale

The model identifies its governing requirements, scope and constraints. Heavyweight work also identifies its approved architecture; a change package may establish its own confirmed requirements. Existing code is evidence about the system, not authority to override an approved target.

Decisions carry enough context to explain their purpose, decisive constraints, meaningful alternatives and consequences. Reuse existing concepts where they fit; explain new or displaced responsibilities in terms of the actual scenarios and owners.

### Progressive design convergence

Concrete topology, sequences, declarations, interfaces and file responsibilities have been progressively agreed with the human or are applicable unchanged reuse. Agreement on direction alone does not establish agreement on the completed design.

#### Macro-first, dependency-led micro design

The confirmed macro topology and technical direction ground micro design. Discussion groups realize bounded behavior across its participants, connecting foundational state and operations to consumers and outcomes, including consequential interruption/recovery paths. Each proposed design is coherent under its stated premises across data, interfaces and sequences, supported by normal flows and decisive counterexamples. Concrete human agreement covers the resulting group; working assumptions remain distinguishable from confirmed decisions. Data-first or sequence-first reasoning follows dependencies, not a field-by-field approval order; design order does not prescribe implementation order.

### Constraints for first-pass implementation

Consequential ownership, invariants, collaboration and resource constraints are explicit where they belong, together with applicable repository conventions. These guide implementation without prescribing every local expression or helper.

## File organization and responsibility tree

The complete repository-relative target tree assigns responsibilities to scoped production, contract, integration and test files. It maps participating definitions and operations to their owners and identifies removals, relocations and migrated callers. The tree describes the final organization, not just changed files.

## Macro runtime and collaboration model

### Topology

Mermaid topology shows the actual processes, contained modules, external participants and their responsibilities. Crossings identify communication mechanisms and contracts.

### Data flow and state authority

Data paths identify origins, transformations, destinations, state changes and authoritative owners. Crossing representations and payload mappings are defined. A separate flow view supplements topology when needed for clarity.

### Concurrency and ordering

The model identifies execution contexts, allowed overlap, coordination mechanisms, mutation authority and completion. Resource lifetime, capacity and failure behavior are resolved where they affect the scoped guarantees.

### Sequences

Macro Mermaid sequences realize the distinct scenario interaction patterns, including meaningful alternative and failure paths. They show participants, calls/messages, responses, completion and ordering consistent with topology and contracts.

## Micro object and collaboration model

### Topology and ownership

Mermaid topology shows concrete modules, objects and definitions mapped to files and macro participants. Responsibilities, state, ownership, multiplicity and lifetime make their collaboration understandable.

### Sequences and operations

Micro Mermaid sequences realize macro scenarios using concrete operation names, data and state transitions. Consequential algorithms, transformations, coordination and resource handling are specified through declarations, precise prose or pseudocode. Each macro guarantee reaches a concrete owner and mechanism.

## Complete data-structure definitions

Owned state, inputs/results, collections, messages and stored/transferred representations have complete target-language declarations or precise schemas. Changed structures show the full resulting definition; unchanged structures have applicable references.

Definitions include all fields, variants and types, with the semantics needed to use them correctly: defaults, optionality, units, valid states, relationships, ownership, mutability and invariants. Collection and encoding rules, transformations and invalid-input behavior are included where consequential. Each concept has a canonical definition.

### Clarify actual declarations with the human

Agreement covers the actual declarations and their meaning, including internal structures that carry design responsibility. Creation, update and consumption agree with the sequences; a relationship diagram alone is not a data definition.

## Complete interface contracts

Interfaces cover module/object operations, process/external crossings and internal operations relied on by the design. Each has an owner, concrete signature or protocol, and inputs/results linked to full definitions.

Contracts explain behavior, preconditions, state effects, success and errors, ownership/lifetime, completion and concurrency, plus applicable compatibility and quantitative constraints. They are sufficient for callers and implementers to agree on the same behavior.

## Overall workflow integration test plan

The plan uses inspected project guidance, runner/configuration, representative tests, setup and invocation. It selects a few meaningful business flows from real entry through collaborating modules/processes to observable outcome, including consequential alternatives.

Each flow identifies its scenario, participants, starting conditions, actions, expected result, intended test location and how to run it. Substitutions and coverage limits are clear. This is a limited macro-flow plan; detailed TDD cases, fixtures and assertions belong to implementation. Planned tests are distinct from checks already performed.

## Consistency, evidence, and clean integration

Requirements, files, macro/micro views, definitions and contracts agree. Scenario traces connect them, and referenced code or targeted investigation supports consequential feasibility claims.

Every diagram has been rendered and visually inspected against its current source. The evidence reports what was actually checked and any remaining limits.

The model is integrated current content in canonical sections, with context, decisive rationale and relevant acceptance outcomes beside the decisions they explain. Related decisions, references and remaining open scope reflect the same current design; resolved choices are no longer presented as undecided. It is readable without reconstructing a conversation or amendment diary.

## Authorization, continuity, and evidence validity

Specification writes require prior human confirmation of the exact displayed content. Independent review and final human approval are separate. The original author and original independent reviewer retain the work through repairs; evidence and approval apply only while their underlying result and sources remain applicable.

## Delivery criteria

The scoped target is complete, coherent, concretely agreed and supported by current checks. No unresolved consequential design choice prevents implementation, while ordinary implementation judgment remains available.
