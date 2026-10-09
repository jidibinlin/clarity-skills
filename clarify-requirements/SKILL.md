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

## 2. Build and test the requirements model

Clarification is driven by gaps in understanding, not by an exhaustive decision tree. Build a coherent account of the requirement, challenge it with relevant scenarios, and ask only questions whose answers materially change that account.

**Understand the problem before accepting a proposed solution.** Distinguish the user's actual difficulty and desired outcome from a suggested feature or mechanism. Use the context already supplied; ask about purpose only when that distinction is genuinely unclear. Start with a concrete situation: who acts, under what conditions, on what, toward which observable result. Derive and refine concepts and their relationships from that situation rather than requesting a dictionary of terms up front.

**Make every question earn its interruption.** Before asking, identify what would change in the model depending on the answer: intended outcome, scope, concept meaning or relationship, observable behavior, or a material constraint. If nothing material changes, omit the question. Obtain accessible facts yourself, reuse confirmed answers and applicable conventions, and leave implementation choices to technical clarification. A convention can fill an incidental gap, but must not silently decide disputed business behavior. Do not invent a default for a material unknown merely to ask fewer questions.

**Choose the next useful question, not every available question.** Prioritize uncertainties that could invalidate the current understanding or determine other decisions. Ask a short round of related, independently answerable questions, or one focused question when that is enough. Defer dependent questions. Use plain language and provide the background and consequence needed to answer. Offer a recommendation with its actual basis when useful; do not manufacture alternatives or frame every choice as accepting the agent's preferred answer. Wait for the human's response.

**Test the understanding with consequential scenarios.** Walk through the main behavior, then use examples or counterexamples suggested by actual rules, risks, or observed conflicts. For example, ask whether withdrawing an already-approved request reverses an effective outcome or whether withdrawal only applies before approval; explain why that distinction changes the meaning of withdrawal. Do not ask the user to work through generic lists of permissions, exceptions, concurrency, logging, or future extensions regardless of relevance. A small edge case still deserves a question when it changes correctness or scope.

**Show how the understanding changed.** After resolving a coherent topic, briefly state what is now established, what previous interpretation changed, and any consequential question still open. Use a focused diagram when it makes a relationship or branch easier to judge. Persist the result through step 3 as the conversation proceeds; these updates are not separate approval gates or an append-only interview log.

**Stop clarifying when the model is ready to check.** Within the agreed scope, the main scenarios must be explainable, key concepts and rules consistent, consequential exceptions addressed, and no material business decision left for the implementer to guess. A fully specified request may need no clarification questions. Move to the delivery check and then document approval, not directly to implementation. If the scope cannot be bounded here, preserve the model and unresolved issues and surface the limitation rather than expanding the effort silently.

## 3. Maintain the model as understanding changes

As soon as there is substantive content, persist the model and keep it current throughout clarification. Use a visible status of `Draft`, `Awaiting approval`, or `Approved`; these describe the document, not whether individual interview answers were confirmed.

Organize the model around the requirement's concepts, relationships, behavior, and rules, following the delivery standard. Integrate answers where they belong. Do not append one section per interview round, leave a pile of definitions disconnected from behavior, or treat adding a diagram as a substitute for synthesis.

Separate established facts, confirmed decisions, proposals, assumptions, and unresolved questions. Supply background and actual rationale according to reader dependence. Keep the necessary knowledge in the model and its explicit references, not solely in session context.

Revise the owning sections in place and synchronize their diagrams, scenarios, and dependent rules. Enforce the delivery standard's prohibition on document patches and change logs, including when resuming inherited material that already contains them. Preserve agreed precision, exclusions, and necessary rationale while removing superseded text. Changes to reviewed content return the model to `Draft` for the review-and-repair loop and renewed final approval; keep only the current approval status and applicable note.

On resumption, read the model, its status, required references, and unresolved items. Reuse settled requirements rather than restarting the interview, but always run step 4 before an approved handoff. An inherited `Approved` status does not bypass review.

## 4. Review, repair, and review again

After requirements clarification is complete, act as the controller and dispatch an independent, read-only reviewer using [reviewer-prompt.md](reviewer-prompt.md). Read that contract and supply its required inputs: the complete current artifact and necessary references, REQUIREMENTS-MODEL.md, original requirement evidence, current verification evidence, and previous findings when applicable. Keep this review package in the task input, not in a new deliverable or an appendix. Provide the confirmed facts and decisions needed for comparison, not instructions to endorse your interpretation.

Use a fresh reviewer context for every round, without the author's working conversation or private reasoning. The same model may serve as reviewer; a role switch inside the author's conversation does not qualify. The reviewer only inspects and reports. You own writing, corrections, and human interaction. If an independent context or necessary input cannot be provided, retain `Draft` and report the specific blocker; do not substitute self-review or ask for final approval.

Render and inspect Mermaid diagrams and complete other required verification. Give the reviewer access to the current results and artifacts, or the read-only tools needed to check them. Missing mandatory verification blocks a pass; disclosure alone is insufficient.

Require the reviewer's result to follow the return contract and identify the current artifact. A stale, incomplete, or internally inconsistent response is not a pass: obtain a complete independent result, or report the review as blocked. Summarize findings and blockers in the conversation with their affected passages and criteria. Keep the model free of review logs, repair notes, and patch documents.

For `Changes required`, retain or return to `Draft`, correct findings in the owning sections, and synchronize diagrams, scenarios, and references. Recover missing details from available evidence first; ask the human only for genuinely unresolved requirements. For `Blocked`, retain `Draft` and obtain the missing evidence or verification. Then dispatch a fresh reviewer to perform another full review, checking previous findings and regressions outside them. A claimed fix is not a passing review. If the loop cannot progress, report the unresolved issue and the decision or access required; repeated attempts do not waive the gate.

Only an independent `Pass` for the current artifact with all applicable checks satisfied, no unresolved findings or blockers, and completed mandatory verification permits step 5. Confirm that the reviewed content and required references are still current before accepting the result. Any subsequent edit to requirement content, diagrams, or required references invalidates the review and returns to this loop. Updating approval metadata alone does not require another content review.

## 5. Obtain final human approval and stop

After the review passes, set the model to `Awaiting approval`. Present its path and the passing review conclusion, point the human to the main flow and consequential decisions, and ask explicitly whether they approve this reviewed model for technical clarification.

Wait. Agreement with interview answers, approval of a proposed correction, or approval given before the current model passed review is not final approval. If the human requests changes, return to clarification as needed, integrate the changes, run the review-and-repair loop again, and request approval of the resulting reviewed model.

Record `Approved` only when the same current model has both a passing review and explicit final human approval. Retain only its applicable approval note. On resumption, an unchanged model that passes the current review may retain its established final approval; a status label alone is not evidence that these conditions were met.

Return the approved model's path and essential references as the handoff. If blocked, return the draft path and blocker as a progress report, never as an approved handoff. Stop at this stage: approval permits separate technical clarification, not automatic execution of it. Do not generate technical models, implementation tickets, or code here.
