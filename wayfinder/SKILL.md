---
name: wayfinder
description: Coarsely split a large requirement into drillable clarification scopes, or resume its map. Tentative topology tests boundaries; this is not formal architecture, ticketing, or coding.
---

# Wayfinder

Make a large requirement navigable. Use LOW-resolution tentative topology to challenge the decomposition, not to approve a technical solution.

## 1. Establish the destination and evidence

Read [WAYFINDER-MODEL.md](WAYFINDER-MODEL.md) before modeling; it guides both construction and review. Use the registered `artifact-layout` skill for the effort root and artifact ownership. Resolve resources through their installed skill owners, not assumed neighboring directories.

Read the original request, confirmed decisions and relevant domain/repository evidence. Establish the practical problem, intended outcomes and selected scope. Separate current facts from the confirmed target. On resume, recover the current map and review state, including formal decisions that supersede its estimates.

Retain the original map author and a separate independent reviewer through repairs. If the work is already bounded for standalone requirements clarification, return that handoff instead of creating a hierarchy.

## 2. Walk scenarios before naming children

Walk an actor through an initiating event, starting state, decisions and observable outcome. Contrast current and intended behavior, identifying existing/preserved, new, changed, external and excluded scope. Follow variations where they expose different responsibilities or dependencies.

Group related rules and outcomes into candidate requirements slices. Test whether each slice can be understood without deciding its neighbors' rules. Assign shared meanings and cross-child flows to the future root requirements owner. The goal is independent clarification, not independent deployment.

## 3. Challenge the split with LOW-resolution topology

Sketch the participants, broad responsibility/state ownership and collaboration directions needed to expose coupling. Distinguish tentative estimates from established facts and imposed constraints.

For each connection, ask what rule or information crosses the boundary and which unresolved answer another slice needs. Revise or merge boundaries when scenarios reveal hidden coupling. Stop refining when further detail would choose a technical realization rather than improve the split.

Keep business relationships, tentative collaboration and clarification prerequisites distinguishable. Explain what each prerequisite supplies and why it matters. Even a human-confirmed topology estimate remains tentative until formal architecture is developed from detailed requirements.

## 4. Resolve the next material boundary question

Use registered `communication-style` for human communication, including its **Ask when human judgment is needed** section for consequential questions. Investigate accessible facts first, then choose a ready question that materially changes the scope, boundary or prerequisite.

Resolve the coarse choices needed to begin useful requirements clarification. Leave later detailed choices with their owners rather than trying to solve the whole system here. After each answer, reconcile the affected scenarios and split and continue with the next ready material question. Keep candidate maps and unresolved proposals in conversation.

## 5. Integrate the map and authorize its write

Organize confirmed conclusions around the overall journey and its scopes. Explain each scope's purpose, boundaries, outcomes and dependencies, with the background and actual rationale needed for consequential decisions. Integrate refinements into their owning sections rather than accumulating discussion history.

Before writing specification content, show the concrete proposed text or patch and its destination, explain material consequences, and obtain human confirmation. Apply the confirmed content; if the proposal changes, confirm it again. Do not persist candidate specifications.

Use Mermaid to explain business flow and scope, including tentative collaboration when it influenced the split. Render the views and visually inspect them against the narrative; retain the output and inspection evidence.

## 6. Make the heavyweight handoff navigable

Use root `issue.md` to identify the selected sources, scope and dependencies. Preserve the route:

1. `clarify-requirements` develops shared and child requirements. Root owns shared meanings and cross-child flows; children own scoped detail. They may co-evolve, but the selected composed package needs review and human approval before architecture.
2. `clarify-architecture` establishes overall architecture from that approved requirements package.
3. `clarify-technical-design` develops scoped realizations from applicable approved requirements and architecture.
4. `split-tickets` builds one root ticket set from the complete approved technical scope, followed by root-controlled implementation and one delivery summary.

Children retain their assigned model ownership and return to root; they do not create separate ticket sets or whole-work summaries. Return conflicts to the owning stage. Map approval establishes a useful requirements handoff, not approval of these later stages.

## 7. Review, repair, obtain approval and stop

Load registered `review-records` for recording the review and repair loop, using the locations from `artifact-layout`.

1. Submit the complete current map, original requirements, confirmed decisions, source basis, human confirmations and diagram evidence to the original independent reviewer using [reviewer-prompt.md](reviewer-prompt.md).
2. Record findings and return repairs to the original author. Record repair decisions, including those made autonomously within the confirmed scope. Confirm specification changes through step 5, then return the result to the same reviewer. Continue until `Pass`; the reviewer assesses closure and regressions.
3. Present the reviewed map, consequential boundaries and coarse-stage limits for final human approval, separate from permission to write. Human revisions return through the same author/reviewer loop. Review and approval must apply to the current result.
4. Record approval and return the map, selected next requirements scope, inherited constraints and owned later questions. State any remaining blockers plainly.

Stop. Only separately authorized `clarify-requirements` begins the next stage; naming or approving the route does not launch it.
