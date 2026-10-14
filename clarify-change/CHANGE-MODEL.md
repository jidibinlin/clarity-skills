# Change Model: Authoring and Review Standard

Use these criteria to shape and review a transition from an evidenced existing system to a complete scoped target. The package includes changed requirements, preserved guarantees and technical decisions. Missing historical models do not require invented history or a heavyweight conversion.

## Purpose and governing design standard

Read these sections, including subsections, from registered `clarify-technical-design`'s `TECHNICAL-MODEL.md`:

- **Approved basis and decision rationale**.
- **Progressive design convergence**.
- **File organization and responsibility tree**.
- **Macro runtime and collaboration model**.
- **Micro object and collaboration model**.
- **Complete data-structure definitions**.
- **Complete interface contracts**.
- **Overall workflow integration test plan**.
- **Consistency, evidence, and clean integration**.

Resolve resources through their registered owners. When canonical architecture or map content is affected, read only these content sections, including subsections:

- From `clarify-architecture`'s `ARCHITECTURE-MODEL.md`: **Approved basis and global completeness**, **Global decisions versus owned child realization**, and **Overall workflow integration coverage**. Its referenced technical content is covered by the imports above.
- From `wayfinder`'s `WAYFINDER-MODEL.md`: **Destination and fidelity**, **Drillable boundaries and dependencies**, **Context and actual basis**, **Diagrams and visual evidence**, and **Review coverage**.

Apply these criteria to the affected canonical content. Change authors coordinate the updates and the change reviewer assesses the combined package under this stage's approval route.

## Evidenced baseline and scope

The baseline identifies the request, affected behavior, participants, source/code state and relevant external contracts. Reliable documents have been checked against the system; stale or missing affected content is reconstructed from code, callers, configuration, tests and runtime evidence.

Current behavior, confirmed intent and uncertainty are distinguishable. The reconstruction is sufficient to explain affected scenarios, macro collaboration, micro ownership, files and contracts without surveying unrelated scope. Existing code facts do not override an approved target.

## Requirements and decision rationale

Changed and preserved scenarios have clear rules, constraints, exclusions and observable acceptance outcomes. Technical-only changes still identify their preserved obligations.

Context and decisive rationale explain the transition, reuse and consequential tradeoffs. Concrete target views and definitions have been progressively agreed with the human or are supported by applicable unchanged references.

## Mandatory change assessment and complete targets

The current-to-target comparison addresses macro topology, dataflow/state authority, concurrency/completion, macro sequences, micro ownership/sequences, file organization, and data/interface contracts. Each has a justified **Changed** or **Unchanged** assessment. **Unresolved** identifies a decision still needed before readiness.

The complete target satisfies the imported technical criteria: file tree, macro and micro Mermaid topology and sequences, full structures and contracts. Checked unchanged references may supply retained content. Separate current and target views where combining them would obscure the transition.

## Reuse, consolidation, migration, and exit

The resulting concept set explains retained, moved, consolidated and replaced responsibilities. Migrations identify final owners, affected callers/data, transition constraints, cutover and obsolete-path exits. The target leaves one clear authority for each responsibility.

## Verification and execution readiness

The limited macro-flow plan covers changed behavior and consequential preserved collaboration using actual project facilities. Current checks cover the baseline-to-target mapping, referenced definitions, callers and migration feasibility. Every diagram has current rendering and visual-inspection evidence.

A **direct** change fits one coherent context for implementation, verification and repair, with settled owners, prerequisites and acceptance. **Decomposed** work needs meaningful separate increments or dependency coordination. The route has a scope-based rationale; a bounded direct change needs no synthetic tickets.

## Canonical synchronization and authority

Affected canonical requirements, architecture, technical and map sections contain the integrated target. The change model explains the transition and references those authorities; without older models, it supplies the scoped authority itself.

Impact identifies affected callers, dependent work, acceptance, approvals and verification evidence, with a basis for what remains valid. The change package includes enough surrounding and cross-child context to assess these effects together. Approval of the target does not establish code conformance.

## Authorization, continuity, and evidence validity

Specification writes require prior human confirmation of the exact displayed content. Independent review and final human approval are separate. Original change/canonical authors and the original independent change reviewer retain the work through repairs; evidence and approval apply only while their underlying result and sources remain applicable.

## Delivery criteria

The integrated package explains the affected baseline, complete agreed target, transition and downstream impact, supported by current checks and a justified execution route. Context, decisive rationale and acceptance outcomes accompany the decisions they explain.
