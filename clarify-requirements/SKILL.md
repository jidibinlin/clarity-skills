---
name: clarify-requirements
description: Clarify a bounded requirement and maintain a reviewable requirements/domain model until explicit human approval. Use for the requirements stage of a lightweight change, to resume an existing requirements model, or when a larger workflow delegates a bounded requirements question with inherited constraints. Also load reference-only when another stage or reviewer needs its requirements standard. Not for technical design, implementation planning, or coding.
---

# Clarify Requirements

Turn a requirement into an understandable, durable model of the intended behavior, not a transcript of the interview. The work ends at the first human approval gate, before technical clarification.

## Entry mode and dependencies

For reference-only use, read the requested standard or reviewer contract and its required dependencies, then return to the consuming stage. Do not interview, create artifacts, dispatch reviewers, seek approval, or run the steps below merely because this skill was loaded. Execution retains every scope, review, and approval gate below.

Install this complete skill and the complete model-loadable `workflow-artifacts` dependency. Before consuming its standards, interviewing, starting/resuming work, or writing, load `workflow-artifacts` by name through the Skill tool or the harness's equivalent registered resource mechanism, and read its companion `WORKFLOW-ARTIFACTS.md`; then read [REQUIREMENTS-MODEL.md](REQUIREMENTS-MODEL.md). Follow that shared skill's resource-resolution, supplied-content reuse, missing-dependency blocking, and skill-root/project-root rules. Apply both standards throughout clarification, writing, repair, and review. No external skill collection is required.

Stage routes name separately installed complete skills: `clarify-technical-design` for an authorized subsequent technical stage, or `clarify-change` for an authorized scoped-change route. Load a routed skill by name for execution only when that stage is authorized; mentioning it or approving this stage does not run it.

## 1. Establish the bounded change

Read the user's request and any supplied model, references, or inherited decisions. Establish the problem, intended outcome, and scope. Ask only for missing choices; do not repeat decisions already made.

Inspect relevant project guidance, existing domain definitions, affected behavior, and tests to establish what is currently true. Follow references needed to interpret inherited constraints. Keep repository facts separate from proposed behavior. If evidence is inaccessible, identify the gap instead of pretending to have inspected it.

Resolve the repository and existing work identity before choosing or reusing `.scratch/<work-slug>/`. As author/controller, complete the shared pre-write exclusion procedure: resolve `info/exclude` with Git (including worktrees), preserve its contents, establish `/.scratch/`, block writes to tracked workflow material, and verify effective exclusion for planned paths. Do this before writing workflow content; never stage, commit, or publish it.

Create the new model at `.scratch/<work-slug>/requirements.md`, with `issue.md` as the work entry/recovery map and `issue.log.md` for process records in the same directory. Existing authoritative project models may stay at established paths under the shared reference/synchronization rule; do not duplicate or relocate them automatically. State the work and model paths. Do not change production code or create `delivery.md` at this planning stage.

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

Revise owning sections and synchronize diagrams, scenarios, and dependent rules. Enforce the prohibition on normative patches and model-embedded change logs, including inherited material. Preserve agreed precision, exclusions, and rationale while removing superseded text. Changes to reviewed content return the model to `Draft` for review and renewed final approval. Keep only current approval metadata in the model; preserve prior outcomes and their applicability in `issue.log.md`, not Git history or conversation alone.

On resumption, read `issue.md`, applicable models/references, open findings, and the latest evidence/decisions; reconcile their identities, approvals, and actual sources before reuse. Reuse settled requirements, but always run step 4 before an approved handoff. Keep `issue.md` current with stage, basis, approval links, blockers, roles, and next action; persist recovery information before blockers or session/stage handoffs. An inherited `Approved` status does not bypass review.

## 4. Review, repair, and review again

After requirements clarification, act as controller and dispatch an independent, read-only reviewer using [reviewer-prompt.md](reviewer-prompt.md). Supply the complete current artifact/references, REQUIREMENTS-MODEL.md and WORKFLOW-ARTIFACTS.md, original requirement evidence, current verification, workspace/exclusion evidence, and previous findings. The package may remain in task input, but its essential source identities, decisions, findings, and evidence must persist in `issue.log.md`. Identify private models by path plus digest or another verifiable local revision, not HEAD alone; identify every relevant source and any dirty/untracked code basis under the shared contract. Provide facts and decisions, not endorsement instructions. Supply the target repository/checkout, work identity, governing skill names, and complete current standards/reviewer contract or verified readable resource locations with their owning skills under the shared dispatch rules. State reference-only use and the read-only reviewer role; do not assume the reviewer inherits a working directory or sibling skill layout.

Use a fresh reviewer context for every round, without the author's working conversation or private reasoning. The same model may serve as reviewer; a role switch inside the author's conversation does not qualify. The reviewer only inspects and reports. You own writing, corrections, and human interaction. If an independent context or necessary input cannot be provided, retain `Draft` and report the specific blocker; do not substitute self-review or ask for final approval.

Render and inspect Mermaid diagrams and complete other required verification. Give the reviewer access to the current results and artifacts, or the read-only tools needed to check them. Missing mandatory verification blocks a pass; disclosure alone is insufficient.

Require the exact reviewed basis and complete return contract. A stale, incomplete, or inconsistent response is not a pass: request correction or report the blocker. As sole controller writer (the author in standalone mode), save every returned review, including failed/blocked outcomes, in `issue.log.md` before repair or gate advancement. Preserve round/reviewer identity, standards, basis, coverage, evidence/limits, and stable finding IDs with closure conditions. Keep the model free of review logs and repair notes.

For `Changes required`, retain or return to `Draft`, correct findings in owning sections, and synchronize diagrams, scenarios, and references. Recover evidence first; ask only for genuinely unresolved requirements. For `Blocked`, retain `Draft` and obtain missing evidence or verification. Before requesting a fresh full review, record repair decisions, actual rationale, addressed finding IDs, revised basis, fresh verification, and remaining blockers in `issue.log.md`. Mark author repairs `addressed, awaiting review`; disputes remain open with counter-evidence until independent disposition. The fresh reviewer checks prior findings and regressions across the complete model. Save that disposition and update `issue.md` before advancing. Repeated attempts do not waive the gate; persist recovery information when blocked.

Only an independent `Pass` for the current artifact with all applicable checks satisfied, no unresolved findings or blockers, and completed mandatory verification permits step 5. Confirm that the reviewed content and required references are still current before accepting the result. Any subsequent edit to requirement content, diagrams, or required references invalidates the review and returns to this loop. Updating approval metadata alone does not require another content review.

## 5. Obtain final human approval and stop

After the review passes, set the model to `Awaiting approval`. Present its path and the passing review conclusion, point the human to the main flow and consequential decisions, and ask explicitly whether they approve this reviewed model for technical clarification.

Wait. Agreement with interview answers, approval of a proposed correction, or approval given before the current model passed review is not final approval. If the human requests changes, return to clarification as needed, integrate the changes, run the review-and-repair loop again, and request approval of the resulting reviewed model.

Record `Approved` only when the same current model has both a passing review and explicit final human approval. Persist exact approved scope/basis and a faithful short quotation or durable reference to the actual user decision in `issue.log.md`; link it from current model metadata and `issue.md`. Handle metadata-only identity changes under the shared contract. An unchanged resumed model may retain its evidenced final approval after current review; a status label alone is insufficient.

Return `issue.md`, the approved model path/revision, and essential references as the handoff. If blocked, return the draft path and persisted blocker, never an approved handoff. Stop at this stage: approval permits separate technical clarification, not automatic execution. Do not generate technical models, implementation tickets, code, or `delivery.md` here.

For scoped changes to an existing implemented system, route to `clarify-change`, loaded by name only when that stage is authorized, to reconstruct any missing baseline and clarify requirements with their technical consequences in one coordinated package. That route synchronizes affected canonical sections and obtains its own independent review and human approval; it does not silently retain this model's old approval for changed content. The full-model gate above remains the workflow when using clarify-requirements itself.
