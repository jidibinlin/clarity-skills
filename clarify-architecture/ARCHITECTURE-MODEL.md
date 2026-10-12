# Architecture Model: Authoring and Review Standard

This standard belongs to `clarify-architecture`. Load that skill by name in reference-only mode when another stage needs it; use the resolved companion location or complete current supplied content under `workflow-artifacts` loading rules. Reading content does not execute architecture prerequisites or approval steps. [SKILL.md](SKILL.md) owns execution; this document owns architecture content and evidence.

## Shared rules and selective technical reuse

Before every role starts or resumes, load `workflow-artifacts` and read its entire WORKFLOW-ARTIFACTS.md. It owns privacy, hierarchy, writer ownership, source identity, records, scoped approvals, and impact propagation. Architecture is the clean root global technical authority, not a second requirement model or an expanded Wayfinder estimate.

Before investigation, decisions, drafting, or review, load `clarify-technical-design` by name in **reference-only** mode and read these TECHNICAL-MODEL.md sections completely:

- **Approved basis and decision rationale**, including **Progressive design convergence** and **Constraints for first-pass implementation**: progressively discussed concrete global proposals, evidence-grounded reuse, consequential quality choices, proportional background, actual deciding rationale, and distinct facts/proposals/decisions.
- **Macro runtime and collaboration model**, all subsections: complete relevant topology, data movement/state authority, actual concurrency/ordering, and macro sequences.
- **Overall workflow integration test plan**: project investigation before selection, few meaningful overall flows, actual collaboration versus substitutions, planned tests versus current evidence.
- **Consistency, evidence, and clean integration**: scenario traces, accurate rendered and visually inspected diagrams, checked references, feasibility evidence, and integrated current authority.

Apply those content rules to the architecture scope below. Importing them neither starts technical-stage execution nor demands a completed child micro model at architecture approval. In imported cross-view rules, trace macro responsibilities to the explicit child realization assignments; complete child file trees, micro diagrams, data declarations, and implementation interfaces are delivered at child technical gates. This scope boundary does not permit deferring a cross-child decision needed to design those children.

## Approved basis and global completeness

Use the root entry to identify the selected shared/child requirements package, exact current sources/sections/revisions and real prerequisites. Resolve applicable composite review and explicit human approval through the models and their object review logs, not approval-record navigation in the entry. Preserve approved behavior, quantitative bounds, exceptions, and exclusions. Map approval, rough topology, code's current limitations, and local child Passes are not substitutes. Initial architecture requires actually approved clarified requirements; an authorized coordinated scoped-change route may import this content standard under its own gates without inventing historical approvals.

Explain relevant current runtime/code structure and reusable owners with repository evidence. Settle the target global organization and meaningful cutovers, including displaced responsibilities and affected callers. Model the selected scope and necessary interactions, not every future map idea or the whole repository. A business requirement boundary need not be a module, process, code owner, or ticket boundary.

The architecture must contain:

- **Macro topology:** all relevant actual processes, modules and external participants, their responsibilities and boundaries, selected communication mechanisms, and existing/new/changed/external scope distinctions. A single-process design still has an explicit runtime boundary; do not invent distribution.
- **Dataflow and state authority:** origins, transformations, destinations, representations at crossings, authoritative writes and invariant owners; distinguish dependency, control, and data arrows.
- **Concurrency and macro sequences:** real execution contexts, permitted overlap, selected coordination mechanisms and their scope, ordering, lifetime/completion, and relevant capacity/error/termination behavior. Cover every distinct approved cross-child interaction pattern and consequential alternatives without false prerequisites or speculative recovery features.
- **Shared technical guarantees and boundary contracts:** the obligations children can rely on and must preserve, with responsibility ownership as specified below.
- **Overall integration-flow plan:** the small project-grounded set below, not a detailed TDD strategy.

Use the imported macro semantic and Mermaid requirements in full. Provide complete relevant topology and sequence diagrams, plus a separate dataflow view when one topology cannot express it clearly. Split complex views for readability without losing necessary paths, boundaries, or cross-view consistency.

## Global decisions versus owned child realization

Architecture settles every global choice and caller-visible cross-boundary guarantee needed to design children. For each shared responsibility or crossing, specify its owning runtime/module, participating children, purpose, semantic inputs/results/state effects, invariants, completion and failure/rejection propagation, ordering/concurrency, ownership/lifetime, and applicable compatibility or quantitative constraints. Define the chosen mechanism and why it establishes the guarantee. Include exact payload, protocol, or representation details here when children need them to design compatible behavior; a label such as “shared API later” is not a contract.

Distinguish these settled global decisions from later **child implementation-detail design**. For each necessary shared concrete definition, interface realization, or code responsibility not fully specified here, assign exactly one owning child technical-model path/section, identify consumers and design dependencies, and state the fixed contract it must realize and the detail still to specify. The assignment is a design obligation, not a fake existing source reference or a ticket. A child may own shared code serving multiple business requirements; do not create duplicate definitions in each child or infer ownership from directory names.

Only detail that cannot change a settled global guarantee or another child's design basis may remain for that owner. If a prospective child cannot design correctly without a missing boundary choice, resolve it here before approval. Local objects, algorithms, full declarations, file assignments and operation contracts are still mandatory in applicable child technical models; they must be fully specified and compatibly reviewed/approved before global tickets. No production-design choice remains for coding. Once a concrete definition is settled, reference its single authority precisely rather than copying it into consumers or maintaining competing versions here.

Route conflicts to their owning requirements, architecture, or child technical model, with synchronized affected references and renewed applicable gates under WORKFLOW-ARTIFACTS.md. Record actual design revisions and their review in the owning upstream model and object log; the originating review record only links the referral and approved resolution. Keep unresolved choices beside their affected canonical rules, with their owners and effects on the current scope; integrate settled answers and necessary rationale/evidence there without a duplicate queue. Neither local exception notes nor review records override authority. Use current source identities and an explicit impact basis to distinguish affected dependents from unrelated valid approvals.

## Overall workflow integration coverage

Apply the imported **Overall workflow integration test plan** without expanding it. Inspect existing project means first; select a few representative end-to-end flows across the actual participating children/runtime owners, tied to approved scenarios and macro sequences. Name starting conditions, entry/action, real participants and substituted dependencies, expected observable outcomes, intended test locations and existing invocation/setup, plus the owning child design responsibility for realizing the flow and any necessary collaboration.

Resolve an actual capability gap through the minimal justified technical choice; do not invent a harness from a framework name. Children inherit these overall flows by exact reference and complete their scoped participation rather than duplicating a global suite. Detailed fixtures/assertions, unit cases and exhaustive boundary matrices belong to later implementation/TDD. The plan is not proof of execution, and future unwritten tests are not failed current architecture verification.

## Delivery criteria

Author from these criteria and assess the same complete current model on every independent review round. Coverage headings index the content rules, not replace them:

1. **Approved basis and scope:** exact applicable requirements package, composite review/human approval evidence, real prerequisites and exclusions; no map-as-approval or invented business decisions.
2. **Existing-system fit, rationale and convergence:** inspected runtime/code/testing facts ground reuse, changes, cutovers and consequential choices, with sufficient background and actual deciding basis; progressive convergence works top-down from scoped global topology and boundaries to the solution directions needed for consequential technical problems, with applicable concrete confirmation or reuse evidence. Technology labels or direction agreement followed by a finished architecture awaiting final confirmation are insufficient. Child bottom-up micro design remains at its assigned technical gate.
3. **Macro completeness:** complete relevant topology and sequences, explicit dataflow/state authority and concrete concurrency/ordering mechanisms, consistent with approved scenarios.
4. **Shared guarantees and ownership:** clear cross-child boundary contracts and invariant/responsibility owners; every global decision needed to design children is settled.
5. **Realization boundary and closure:** exactly one child design owner per shared concrete realization, explicit consumers/dependencies and remaining child detail, no missing prerequisite disguised as local detail or design deferred to coding.
6. **Overall integration coverage:** project means investigated first; a few meaningful overall flows with real/substituted collaboration, outcomes, locations, invocation and scoped realization ownership.
7. **Consistency and verification:** scenarios trace through consistent views; references and necessary feasibility assumptions have evidence; every Mermaid diagram has current rendering and visual-inspection evidence. Missing required access/rendering/inspection blocks the gate honestly.
8. **Clean, reviewable handoff and records:** integrated current authority with precise accessible references, proportional background and actual rationale; shared record/source/ownership rules satisfied for records due now, not the review report or approval still to occur.

Pass concerns this selected architecture, not whole-effort delivery. Final child design, global ticket planning, combined implementation verification, overall independent review and human acceptance retain their own gates.
