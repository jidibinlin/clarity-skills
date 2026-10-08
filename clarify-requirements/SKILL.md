---
name: clarify-requirements
description: Clarify a bounded requirement and maintain a reviewable requirements/domain model until explicit human approval. Use for the requirements stage of a lightweight change, to resume an existing requirements model, or when a larger workflow delegates a bounded requirements question with inherited constraints. Not for technical design, implementation planning, or coding.
---

# Clarify Requirements

Turn a requirement into an understandable, durable model of the intended behavior, not a transcript of the interview. The work ends at the first human approval gate, before technical clarification.

Before interviewing or writing, read [REQUIREMENTS-MODEL.md](REQUIREMENTS-MODEL.md). It defines the mandatory content, background and rationale requirements, Mermaid rules, and delivery checks. Apply the entire standard, not just its headings. This skill is self-contained; it does not require Matt Pocock's skills to be installed.

## 1. Establish the bounded change

Read the user's request and any supplied model, references, or inherited decisions. Establish the problem, intended outcome, and scope. Ask only for missing choices; do not repeat decisions already made.

Inspect relevant project guidance, existing domain definitions, affected behavior, and tests to establish what is currently true. Follow references needed to interpret inherited constraints. Keep repository facts separate from proposed behavior. If evidence is inaccessible, identify the gap instead of pretending to have inspected it.

Choose one persistent model document. Use a supplied path or the project's existing requirements-document convention; otherwise use `docs/requirements/<short-name>.md`. State the chosen location. Update an existing model for the same change instead of creating a competing account. Do not publish remote issues or change production code as part of this skill.

For delegated work, stay within the supplied scope. If a necessary decision conflicts with an inherited constraint or belongs to the parent effort, return that conflict for human resolution rather than silently changing the parent model. Do not create a heavyweight map here.

## 2. Clarify material questions

Identify uncertainties that affect behavior, scope, or the meaning and relationships of concepts. Investigate facts with available tools; reserve questions for human intent and genuine tradeoffs.

Work in short rounds of independent, currently answerable questions. For each, explain the concrete uncertainty, why it matters, and a recommendation with its key basis where one is supportable. Wait for the human's answers. Defer dependent questions until their prerequisites are settled, and never supply the human's answer yourself.

Use concrete examples and counterexamples to expose ambiguity. Check relevant exceptions, negative requirements, ordering, boundaries, and failure outcomes without manufacturing hypothetical features. Challenge conflicting terms and rules with evidence, not an unexplained preference for another name.

Continue until material questions are resolved. If the change cannot be bounded for this workflow, surface that limitation and preserve the current model and open questions; do not silently expand the effort or claim it is ready.

## 3. Maintain the model as understanding changes

As soon as there is substantive content, persist the model and keep it current throughout clarification. Use a visible status of `Draft`, `Awaiting approval`, or `Approved`; these describe the document, not whether individual interview answers were confirmed.

Organize the model around the requirement's concepts, relationships, behavior, and rules, following the delivery standard. Integrate answers where they belong. Do not append one section per interview round, leave a pile of definitions disconnected from behavior, or treat adding a diagram as a substitute for synthesis.

Separate established facts, confirmed decisions, proposals, assumptions, and unresolved questions. Supply background and actual rationale according to reader dependence. Keep the necessary knowledge in the model and its explicit references, not solely in session context.

Update diagrams, scenarios, and dependent rules when a conclusion changes. Preserve agreed precision and exclusions. A material revision to an approved model returns it to `Draft` and requires renewed approval of the affected model. Keep decision rationale, not a running discussion log.

On resumption, read the model, its status, required references, and unresolved items before choosing the next question. If it is already approved and no material change is requested, return its handoff instead of reopening settled questions.

## 4. Check the deliverable

Apply every delivery check in REQUIREMENTS-MODEL.md against the actual discussion, inherited constraints, and inspected evidence. Repair omissions from available context before asking another question.

Check specifically that an unfamiliar reader can explain the main flow and relationships between the relevant concepts, not merely recite the terminology. Consolidate scattered rules and remove superseded or duplicative prose without losing meaningful constraints or rationale.

Render and inspect the Mermaid diagrams as required by the standard. Disclose any unavailable verification instead of reporting a pass. If a material question still blocks technical modeling, retain `Draft` and ask the blocking question rather than requesting approval of an incomplete model.

## 5. Request approval and stop

When the model is ready for review, set its status to `Awaiting approval`. Present its path, point the human to the main flow and consequential decisions, and report any verification limitations. Ask explicitly whether the human approves this requirements/domain model for technical clarification.

Wait. Confirmation of interview answers is not approval of the model. If the human requests changes, return to the relevant clarification or delivery check and present the revised model for approval. Record `Approved` only after explicit approval of the current model, and retain a concise approval note tied to that confirmation.

Return the model's path, approval status, essential inherited references, and any disclosed verification limitations as the handoff. Stop at this stage: approval permits a separate technical-clarification stage, not automatic execution of it. Do not generate technical models, implementation tickets, or code here.
