# Wayfinder Model: Authoring and Review Standard

Use this complete standard to guide exploration and first-pass authoring, then assess the same criteria independently. Before either role starts/resumes, load the complete shared WORKFLOW-ARTIFACTS.md through named skill `workflow-artifacts`. It owns storage, records, authority, recovery, and hierarchical handoffs; [SKILL.md](SKILL.md) owns this stage's execution and approval loop.

## Purpose and fidelity

The map decides what large requirement is being explored and how to take it into detailed requirements modeling. It is a coherent explanation of the current coarse understanding, not a transcript, glossary dump, technical specification, or list of implementation tasks. Its approval says the selected scope can be clarified in bounded parts; it does not say those parts can already be implemented independently.

A rough macro-topology estimate is a decomposition aid. It may identify likely participants, responsibility boundaries, state owners, and directions of collaboration when these affect the split. Label it explicitly tentative. Do not require or freeze process counts, technologies, file trees, concrete objects, full data structures, protocols, or concurrency design here. Existing verified architectural facts and actual imposed constraints retain their distinct authority; a diagram cannot turn a guess into one.

## Destination, scope, and original basis

Explain the practical problem, affected actors, intended observable outcomes, and exclusions. Distinguish the current clarification/delivery scope from the wider effort; reference the actual human decisions and inspected facts supporting it. Do not treat an interesting future extension as in scope or hide a necessary prerequisite among exclusions.

Describe the overall business journey before enumerating parts. A reader should understand why the parts exist and how they contribute to the outcome without replaying the conversation. Use stable business names in prose and meaningful link labels; internal IDs supplement rather than replace them.

## Coarse decomposition and collaboration

For each candidate child requirement, identify its purpose, main initiating situation and outcome, boundary with adjacent requirements, relevant known constraints, and why this is a useful clarification scope. Record only the principal concepts needed to understand that boundary; detailed domain definitions belong to requirements modeling.

Expose shared business meanings/rules and cross-child flows that need an overall requirements owner. Do not clone them into every child. Separate:

- Business relationships: which outcomes or rules interact, regardless of implementation.
- Tentative collaboration estimates: how existing or plausible responsibilities might cooperate, used only to test boundaries.
- Prerequisites for clarification: what confirmed answer/evidence must be available before a dependent question can be resolved.

For a material dependency, state what is needed and why; numbering and arrows without a meaning do not establish readiness. A candidate topology should reveal suspicious coupling, not dictate a module per requirement. Test the split against representative end-to-end scenarios and likely shared ownership: can each part be clarified coherently without privately deciding another part's business rule? Preserve necessary collaboration. Do not manufacture interfaces, adapters, or extra concepts to make a poor split look independent.

## Background and deciding rationale

Place a consequential boundary or scope decision beside the context and evidence needed to judge it. Explain the actual decisive reason, especially when an apparent alternative would create hidden coupling or omit part of the outcome. Straightforward decisions need short explanations; unfamiliar constraints need sufficient background for a new human or agent reader. Avoid generic benefits, exhaustive rejected-option histories, and private reasoning traces.

Keep confirmed decisions, observed facts, and assumptions visibly distinct. A recommendation does not become confirmed because the human has not objected. If a coarse business choice determines the next scope, resolve it before that scope's handoff. Uncertainty that belongs to later detailed requirements or technical design remains explicit there, not silently settled here.

## Diagrams and narrative

Use accurate Mermaid to show the overall business flow and scope boundaries. Include a low-resolution collaboration/topology view for the estimates that actually influence decomposition; it may share a diagram with the flow only when business relationships and speculative technical relationships remain unmistakable. Avoid redundant views and decorative architecture.

Name participants consistently with the prose; label arrow meaning/direction and distinguish tentative estimates from confirmed scope or existing facts. Explain relevant external participants and excluded behavior at boundaries. The views must agree with each other and with the text, but must not imply detail or guarantees not yet decided.

Render and visually inspect every current diagram. Verify labels, branching, crossings, and boundary readability as well as syntax. Record actual rendering/inspection evidence under the shared artifact rules. Unavailable tools or inspection prevent a verified Pass; never invent render results.

## Unresolved areas and handoff

Keep unresolved material in its owning map section: the question if it can be stated, or the area still too vague, its relevance, what would clarify it, and the responsible next stage/scope. Distinguish a blocker to the current handoff from an explicitly later decision. Unknown future work need not be artificially decomposed or fully resolved.

The handoff to `clarify-requirements` identifies the selected scope, its map/source revision, confirmed inherited constraints separately from hypotheses, relevant scenario/dependency references, and unresolved business questions to deepen. The root entry owns assignment, child paths, progress, and records; the map owns the explanation of the split. Children are modeling scopes, not implementation tickets. The root shared requirements model will own cross-child business rules; the eventual formal architecture must derive from clarified approved requirements rather than simply approving this sketch.

When formal models supersede an estimate, integrate references to their current owning sections. Preserve a clean map; process logs retain history. A change contradicting an approved downstream model returns to that model's governance, not to an overriding map note.

## Delivery categories

Authors check, and reviewers report coverage of, every category:

1. **Destination and faithfulness:** original problem/outcomes, scope/exclusions, inspected evidence and actual human decisions are accurately represented.
2. **Coherent decomposition:** understandable child purposes/boundaries, shared meanings and complete representative cross-child journeys, without fictitious implementation independence.
3. **Low-resolution topology:** relevant estimates test the split, clearly separated from facts and binding architecture; no premature detailed design.
4. **Reviewable decisions:** proportional background and actual deciding rationale, rather than chronology or unsupported defaults.
5. **Diagrams and evidence:** consistent, accurately labeled, currently rendered and visually inspected views.
6. **Uncertainty and handoff:** explicit dependencies and next clarification scope; current blockers resolved without pretending later details are settled.
7. **Authority and recovery:** clean canonical content, precise references and source identity, correct private workspace/record ownership, and no downstream authorization inferred from map approval.

No category is satisfied by its heading alone. `Not applicable` requires a scope-specific reason; missing mandatory evidence is unverified, not an optional improvement. The stage may pass with explicitly owned later unknowns, but not with an unanswered decision that prevents the selected requirements handoff.
