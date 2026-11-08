# Architecture Model: Authoring and Review Standard

Use these criteria to shape and review the selected effort's global technical design. Architecture settles the guarantees and shared responsibilities needed for compatible technical realization; technical models supply local detail.

## Selective technical content

Read these sections, including subsections, from registered `clarify-technical-design`'s `TECHNICAL-MODEL.md`:

- **Approved basis and decision rationale**.
- **Macro runtime and collaboration model**.
- **Test plans** (overall integration testing).
- **Document integration and readability**.

Resolve the resource through its registered owner and import the content, not its workflow. Apply it at global resolution: macro responsibilities connect to realization assignments. File trees, micro views and local declarations belong to technical design.

## Approved basis and global completeness

The basis is the independently reviewed and human-approved requirements, with their dependencies and exclusions.

The design is grounded in approved scenarios and inspected runtime/code boundaries. It explains reuse, changed responsibilities and decisive choices. Existing implementation facts do not override the approved target.

Complete scoped Mermaid topology and sequences show process/module responsibilities, dataflow, state authority, collaboration and concurrency mechanisms. Every scenario reaches an observable outcome through accountable owners. The global choices needed for technical design have been concretely agreed with the human or are applicable unchanged reuse.

## Global decisions versus local realization

Cross-boundary contracts define purpose, inputs/results, state effects, completion/errors, ordering and ownership. Payload or protocol details are fixed wherever compatible technical design depends on them. The selected mechanisms explain how these guarantees hold.

Every shared definition, interface realization and code responsibility has one owning technical-model location, with consumers, fixed obligations and design dependencies. Remaining local detail cannot change another scope's basis. The architecture distinguishes these assignments from definitions already completed in technical models.

## Overall workflow integration coverage

The imported limited macro-flow plan identifies meaningful cross-boundary flows using actual project test facilities. Each flow has a coverage owner and describes required cooperation. Technical models reference the global flow and complete their participation.

Current evidence includes scenario/reference checks, necessary feasibility investigation, and actual rendering plus visual inspection of every diagram. Future integration coverage remains a plan, not a claim that tests have run.

## Authorization, continuity, and evidence validity

Specification writes require prior human confirmation of the exact displayed content. Independent review and final human approval are separate. The original author and original independent reviewer retain the work through repairs; evidence and approval apply only while their underlying result and sources remain applicable.

## Delivery criteria

The integrated global model provides a compatible basis for technical design, with settled guarantees, unique realization ownership, meaningful coverage and current evidence. Architecture approval is not completion of technical design or implementation.
