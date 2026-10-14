---
name: clarify-requirements
description: Clarify or resume standalone, child, or composite requirements through independent review and human approval. Not technical design, ticketing, or coding.
---

# Clarify Requirements

Explain the intended behavior and domain meaning well enough for the next modeling stage. Stop at requirements approval.

## 1. Recover the scope and working basis

Read [REQUIREMENTS-MODEL.md](REQUIREMENTS-MODEL.md) before modeling; it guides both construction and review. Use the registered `artifact-layout` skill for workspace and ownership conventions. Resolve resources through their installed skill owners, not assumed neighboring directories.

Read the original request, confirmed decisions, relevant project knowledge and current behavior. Establish the selected scope and whether the assignment is standalone, child-only or composite. On resume, recover the current models and review state. Code establishes current facts; confirmed requirements govern the target.

Keep the original author and a separate independent reviewer for each object through its repair loop. Root and child authors retain their assigned files.

## 2. Reconstruct behavior with scenarios

Walk an actor through the initiating event, starting state, action or decision, resulting state and observable outcome. Contrast current and intended behavior. Identify what is existing/preserved, new, changed, external or excluded where it affects the flow.

Vary the scenario at consequential boundaries and failures to expose the business rules. Investigate accessible facts before asking the human. Continue until the selected behavior and the decisions still needed are clear.

## 3. Derive the concepts that explain those scenarios

Identify distinctions that change ownership, permission, lifecycle or outcomes. Give them consistent domain names and explain their relationships. Retell the scenarios using those concepts: retain distinctions that explain behavior, and use ordinary prose where a separate concept adds nothing.

Keep imposed technical constraints when they affect requirements; leave realization choices to technical modeling.

## 4. Ask the next ready material question

Use registered `ask-with-context`, including its **Required question format and pre-send check**. Choose the question whose answer most usefully resolves the selected behavior or scope and whose prerequisites are understood. Work from upstream business choices toward their consequences, rather than conducting an exhaustive low-level interview.

After each answer, reconcile affected scenarios and concepts and continue with the next ready material question. A fully specified request needs no interview. Keep unresolved proposals in conversation; confirmed groups can progress while other groups remain open.

## 5. Integrate a confirmed group and authorize its write

Organize the group in its owning domain flow, joining concepts, rules and outcomes. Make existing/new/changed behavior explicit. Add visibly labeled **Acceptance criteria** beside each substantive requirement, and include the background and actual rationale needed to understand consequential choices.

Before writing specification content, show the concrete proposed text or patch and its destination, explain material consequences, and obtain human confirmation. Apply the confirmed content; if the proposal changes, confirm it again. Keep candidate specifications in conversation rather than draft files.

Integrate refinements into the current owning sections, updating related acceptance and views. The model explains current authority; `issue.md` provides definition and navigation, not an interview diary.

## 6. Compose the package and make its views inspectable

Use Mermaid views to make material flows, relationships and scope understandable. Choose the forms that fit the domain, render them and visually inspect their agreement with the prose. Retain the rendered output and inspection evidence.

For composite work, follow **Shared and child requirements** in the standard. Root owns shared meanings and end-to-end flows; children own complete scoped detail. Walk selected outcomes across those boundaries, resolve conflicting rules with their owners and link the actual source sections. Root and children may co-evolve; the complete selected package needs composition review and approval before architecture.

## 7. Review, repair, obtain approval and stop

Load registered `review-records` for recording the review and repair loop, using the locations from `artifact-layout`.

1. Submit the complete current model or selected package, its source basis, human confirmations and diagram evidence to the original independent reviewer using [reviewer-prompt.md](reviewer-prompt.md).
2. Record the findings. Return repairs to the original authors, recording repair decisions, including those made autonomously within the confirmed scope. Confirm specification changes through step 5, then return the current result to the same reviewer. Continue until `Pass`; the reviewer assesses finding closure and regressions.
3. Present the reviewed result and consequential decisions for final human approval, separate from permission to write. Human revisions return through the same author/reviewer loop. Review and approval must apply to the current result.
4. Record approval and return the artifact paths, reviewed scope and remaining limitations. Child work returns to root.

Stop. A separately authorized standalone next step is `clarify-technical-design`; an approved heavyweight requirements package proceeds to `clarify-architecture`. Approval here does not launch either stage.
