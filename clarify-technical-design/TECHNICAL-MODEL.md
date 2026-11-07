# Technical Model: Authoring and Review Standard

Use these criteria to author and review the technical model.

- The consuming skill supplies the working method; `artifact-layout` supplies artifact locations and ownership.
- Resolve this resource through the registered `clarify-technical-design` owner.
- Selective imports include named sections and their subsections, not the owner's workflow.

## Purpose and completeness

Settle consequential design choices within scope.
Leave ordinary implementation choices to the implementing model.

- Resolve structure, representations, algorithms, contracts, coordination and failure handling.
- Include a complete file-responsibility tree.
- Show macro and micro Mermaid topology and sequences, with concurrency semantics.
- Provide complete data definitions and interface contracts.
- Include a project-grounded macro-flow test plan.

## Approved basis and decision rationale

Explain the design's basis and key choices.
Make implementation constraints explicit.

- Identify governing requirements, approved decisions and scope. When code conflicts with approved decisions, the decisions take precedence.
- Explain the purpose, rationale, tradeoffs and consequences of key decisions.
- State ownership, invariants, collaboration and resource constraints, plus applicable repository conventions.

## Concrete design realization

The model describes the concrete design, not only technical direction:

- Topology and sequences.
- Declarations and interfaces.
- File responsibilities.

### Coherent macro-to-micro realization

Micro design realizes the macro topology and technical direction.

- Complete behavior spans state owners, foundational operations and consumers.
- Consequential interruption and recovery paths are defined.
- Data, interfaces and sequences are coherent under stated premises. Normal flows and decisive counterexamples support their consistency.
- Working assumptions are distinguishable from design decisions.

## File organization and responsibility tree

Describe the complete repository-relative target tree, not just changed files.

- Assign responsibilities to scoped production, contract, integration and test files.
- Map participating definitions and operations to their owners.
- Identify removals, relocations and migrated callers.

## Macro runtime and collaboration model

The model includes macro topology and sequence diagrams.

### Topology

- Topology diagrams show actual processes, contained modules, external participants and their responsibilities.
- Cross-boundary communication mechanisms and contracts are defined.

### Data flow and state authority

- Data ownership and flow are clear.
- Crossing representations and payload mappings are defined.

### Concurrency and ordering

- Execution contexts, allowed overlap, coordination mechanisms and ordering are explicit.
- Resource lifetime, capacity and failure behavior are defined where they affect scoped guarantees.

### Sequences

- Sequence diagrams cover distinct interaction patterns, including meaningful alternatives and failure paths.
- Participants, calls/messages, responses, completion and ordering agree with topology and contracts.

## Micro object and collaboration model

The model includes micro topology and sequence diagrams.
Micro views describe complete behavior within closed-loop groups.

### Topology and ownership

- Collaborating modules, objects and definitions have clear responsibilities and state ownership.
- Their relationships and mappings to files and macro participants are clear.

### Sequences and operations

- Sequences show concrete operations, data and state transitions that realize macro scenarios.
- Normal flows and consequential failure paths are described across collaborating owners.

## Complete data-structure definitions

Data definitions, including internal types, are presented in fenced code blocks.

- Key data structures, state semantics and creation/update/consumption lifecycles are clear.

## Complete interface contracts

Interfaces are presented as concrete callable signatures or native protocol declarations in fenced code blocks.

- Behavior for callers and implementers is clear, including preconditions, state effects, success and consequential errors.
- Inputs, results, ownership and lifetime are defined.
- Completion, concurrency and applicable compatibility or quantitative constraints are explicit.

## Test plans

The overall integration test plan covers complete requirement scenarios and interactions across closed-loop groups.

Each group's internal test plan covers its operations, state transitions and failure boundaries.

## Document integration and readability

Integrate the current design into canonical sections, readable without reconstructing a conversation or amendment diary.

- Keep context, decisive rationale and relevant acceptance outcomes beside the decisions they explain.
- Resolved choices are not presented as undecided.

References use file-level links. Identify specific functions or sections by name; do not use line numbers or line-based links.

### Anti-patterns

| Anti-pattern | Appropriate treatment |
| --- | --- |
| A "Current verification boundaries" chapter listing test names, PASS counts, durations, build or lint results | Omit the report from the model. Keep only findings that justify a current design choice, beside that choice with a concise evidence reference. |
| "Synced main, rebased, resolved conflicts, reran checks" | Keep repository operations out of the design. If an upstream contract changed, describe its current effect on the target instead. |
| "First inspected X, then ran probe Y, then found Z" | State the relevant baseline capability and its consequence for the chosen design, not the investigation chronology. |
| Repeated "not real RPC/database/end-to-end verification" disclaimers | Preserve actual guarantee limits or unresolved feasibility beside the affected contract, and substitutions beside the planned flow. Report limits of performed checks with the review evidence. |

## Delivery criteria

- No unresolved consequential design choice prevents implementation.
