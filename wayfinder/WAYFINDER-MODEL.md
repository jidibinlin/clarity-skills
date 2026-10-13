# Wayfinder Model: Content Standard

This standard defines map content and evidence, not execution. Read it completely before constructing or reviewing a map. Importing stages resolve it directly through the actual installed `wayfinder` owner; it imports no other workflow. The owning stage governs writes, review and approval; `artifact-layout` defines file locations and ownership.

## Destination and fidelity

Explain the practical problem, actors, observable outcomes and selected scope before enumerating parts, so an unfamiliar reader understands the overall business journey. Distinguish the selected clarification/delivery scope from the wider effort, explicitly identifying exclusions and real prerequisites. Future extensions are not implicit scope; prerequisites cannot be disguised as exclusions. Use original human decisions and inspected facts, stable business names and meaningful reference labels.

The map is a coherent coarse decomposition into bounded requirements-modeling scopes, not detailed requirements, architecture or implementation tasks. Approval means the parts can be clarified, not implemented or deployed independently.

A low-resolution topology estimate is useful only when it tests the split: participants, responsibility boundaries, state owners and collaboration directions that affect decomposition. Distinguish tentative estimates from verified architectural facts and imposed constraints. Even a human-confirmed estimate is not committed architecture: it does not freeze process counts, technologies, file trees, concrete objects, data structures, protocols or concurrency design.

## Drillable boundaries and dependencies

Each candidate child explains its purpose, initiating situation/outcome, boundary with adjacent requirements, relevant known constraints and why it is independently understandable for clarification. Include only concepts necessary to explain those boundaries; detailed definitions belong to requirements modeling.

Expose shared meanings/rules and cross-child flows needing an overall requirements owner. Keep three different relationships legible:

- Business relationships between outcomes or rules, independent of implementation.
- Tentative collaboration estimates testing the split.
- Clarification prerequisites: answers or evidence needed to resolve dependent questions.

Every material dependency states what is needed and why; ordering numbers/arrows alone do not establish readiness. Representative end-to-end scenarios must remain coherent across children without private decisions about one another's rules. Revise or merge weak boundaries instead of inventing interfaces, adapters or concepts to simulate independence. Neither one module per requirement nor independent deployment is necessary.

## Context and actual basis

Place consequential scope/boundary decisions beside their background and original evidence. Give the decisive reason, meaningful alternatives and accepted consequences where needed to judge the choice, especially when an attractive split hides coupling or omits an outcome. Scale explanation to an unfamiliar reader's dependence. Generic benefits and exhaustive discussion histories are not rationale.

Distinguish confirmed decisions, observed facts and hypotheses. Silence is not confirmation. Resolve coarse business choices that determine the next scope; later detailed-requirements/technical choices remain explicitly owned rather than silently settled. Unconfirmed exploration, candidate answers and missing inputs stay in conversation with their relevance, owner and blocked scope. Only exact human-confirmed coarse descriptions of later unknowns may enter the map, without prefilling their answers.

Maintain a clean current account, integrating confirmed refinements into owning sections rather than patch appendices or a chronological diary. As formal models supersede estimates, use precise references to those authorities. An approved downstream decision cannot be overridden by a map note.

## Diagrams and visual evidence

Use accurate Mermaid for overall business flow and scope boundaries. Include a low-resolution collaboration/topology view when an estimate influences decomposition. Combine views only if business relationships and tentative technical relationships remain unmistakable; omit decorative architecture and redundant views.

Names agree with prose; arrow meanings/directions are clear; estimates, confirmed scope and existing facts are distinct. Explain external participants and excluded behavior at boundaries. Views agree with one another and with the narrative without implying undecided detail or guarantees.

Every required current view has actual rendered output and visual-inspection evidence covering syntax, labels, branching, crossings, boundary readability and semantic agreement. Parsing alone is insufficient. Missing rendering or visual inspection blocks a verified Pass.

## Requirements handoff

A usable handoff identifies selected scope, exact map/source revision, inherited confirmed constraints separately from hypotheses, scenario/dependency references and owned questions to deepen. Current blockers are distinct from later choices; future unknown work need not be artificially decomposed or resolved.

The map explains the split; root `issue.md` defines package selection, source identities and assigned navigation. The root shared requirements model will own cross-child rules; children will own full scoped detail, not tickets. Formal architecture derives from the approved clarified requirements, not automatic promotion of the sketch. The map must not claim approval of those later stages.

## Review coverage

Assess the complete current map against each category:

1. **Destination and faithfulness:** original problem/outcomes, selected scope, exclusions and prerequisites.
2. **Coherent decomposition:** drillable child boundaries, shared meanings and representative cross-child journeys.
3. **Low-resolution topology:** useful estimates without premature design commitments.
4. **Reviewable decisions:** proportionate background, actual rationale and accessible original evidence.
5. **Diagrams:** semantic agreement, readable boundaries and current rendered/visual evidence.
6. **Uncertainty and handoff:** real readiness of the selected next scope, with later choices owned rather than guessed.
7. **Artifact integrity:** attributable current sources, exact identities and unambiguous content ownership.

A heading alone establishes nothing. Explicitly owned later unknowns may remain; unanswered business choices blocking the selected requirements handoff cannot pass.
