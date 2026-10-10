---
name: clarify-requirements
description: Clarify a bounded requirement or a heavyweight shared/child requirements package until independent review and explicit human approval. Use for standalone requirements, assigned child modeling, package consistency, or resumption. Also load reference-only for the requirements standard. Not for technical design, implementation planning, or coding.
---

# Clarify Requirements

Turn requirements into an understandable, durable model of intended behavior, not an interview transcript. Stop at requirements approval, before formal architecture or technical clarification.

## Entry mode and dependencies

For reference-only use, read the requested standard or reviewer contract and its required dependencies, then return to the consuming stage. Do not interview, create artifacts, dispatch reviewers, seek approval, or run the steps below merely because this skill was loaded. Execution retains every scope, review, and approval gate below.

Load the complete named dependency `workflow-artifacts` and read its entire `WORKFLOW-ARTIFACTS.md` before every role starts or resumes. Follow that skill's loading, supplied-content reuse, missing-dependency blocking, reference-only, and root-separation rules. Before investigation, questions, or drafting, read [REQUIREMENTS-MODEL.md](REQUIREMENTS-MODEL.md); apply these standards throughout authoring, repair, and review.
For substantive questions, load the named `ask-with-context` skill and read its complete SKILL.md. Apply its cognitive-alignment, representation, and answer-to-next-decision loop before questions and after every answer, within this stage's authorized scope. Maintain pending decisions in the assigned `issue.md` under the shared artifact rules. This stage retains its scope, artifacts, completeness checks, and approval gates.

Stage routes name separately installed complete skills: `clarify-architecture` after a heavyweight requirements package, `clarify-technical-design` after standalone requirements, or `clarify-change` for an authorized scoped-change route. Load a routed skill by name for execution only when that stage is authorized; mentioning it or approving this stage does not run it.

## 1. Establish the bounded change

Read the user's request and any supplied model, references, or inherited decisions. Establish the problem, intended outcome, and scope. Ask only for missing choices; do not repeat decisions already made.

Use the already-read REQUIREMENTS-MODEL.md to guide investigation before questioning or drafting. Inspect relevant project guidance, existing domain definitions, affected behavior, and tests to establish what is currently true. Follow references needed to interpret inherited constraints. Keep repository facts separate from proposed behavior. If evidence is inaccessible, identify the gap instead of pretending to have inspected it.

As author/controller, establish or reuse the verified private workspace under WORKFLOW-ARTIFACTS.md before writing. Standalone work uses `.scratch/<work-slug>/requirements.md`, with `issue.md` and `issue.log.md`. Heavyweight work reuses the effort root and explicitly assigned root or child model, entry, and log paths; never derive a new slug for a child. State the paths and writer. Apply the shared location rule to existing canonical models. Do not change production code or create `delivery.md`.

For heavyweight work, read **Shared and child requirements** in REQUIREMENTS-MODEL.md and the root entry’s current source package. Establish selected scope, actual dependencies, applicable inherited decisions, and root/child ownership. Shared and child drafts may co-evolve without either requiring the other’s prior final approval. A Wayfinder map supplies scope and hypotheses, not settled business rules or formal architecture.

Delegated authors write only assigned child artifacts and return shared-rule conflicts or proposed root updates to the root owner. Resolve accessible facts there and seek human choices only when material; do not silently override a parent or create another map.

## 2. Build and test the requirements model

Use REQUIREMENTS-MODEL.md as the authoring contract to expose gaps and organize each draft, not only to judge the finished document. Clarification is driven by gaps in understanding, not by an exhaustive decision tree or a questionnaire made from the standard. Challenge the account with relevant scenarios and ask only questions whose answers materially change it.

**Understand the problem before accepting a proposed solution.** Distinguish the user's actual difficulty and desired outcome from a suggested feature or mechanism. Use the context already supplied; ask about purpose only when that distinction is genuinely unclear. Start with a concrete situation: who acts, under what conditions, on what, toward which observable result. Derive and refine concepts and their relationships from that situation rather than requesting a dictionary of terms up front.

Use `ask-with-context` for unresolved business outcomes, scope, concept meanings/relationships, observable behavior, and material constraints. Leave implementation choices to technical clarification; an incidental convention must not decide disputed business behavior.

**Test the understanding with consequential scenarios.** Walk through the main behavior, then use examples or counterexamples suggested by actual rules, risks, or observed conflicts. For example, ask whether withdrawing an already-approved request reverses an effective outcome or whether withdrawal only applies before approval; explain why that distinction changes the meaning of withdrawal. Do not ask the user to work through generic lists of permissions, exceptions, concurrency, logging, or future extensions regardless of relevance. A small edge case still deserves a question when it changes correctness or scope.

As understanding changes, integrate outcomes through step 3. Conversational illustrations support clarification; they do not replace required model views, create extra approval gates, or become an append-only interview log.

**Stop clarifying when the model is ready to check.** Within the agreed scope, the main scenarios must be explainable, key concepts and rules consistent, consequential exceptions addressed, and no material business decision left for the implementer to guess. A fully specified request may need no clarification questions. Move to the delivery check and then document approval, not directly to implementation. If the scope cannot be bounded here, preserve the model and unresolved issues and surface the limitation rather than expanding the effort silently.

## 3. Maintain the model as understanding changes

As soon as there is substantive content, persist the model and keep it current throughout clarification. Use a visible status of `Draft`, `Awaiting approval`, or `Approved`; these describe the document, not whether individual interview answers were confirmed.

Organize the model around the requirement's concepts, relationships, behavior, and rules, following the delivery standard. Integrate answers where they belong. Do not append one section per interview round, leave a pile of definitions disconnected from behavior, or treat adding a diagram as a substitute for synthesis.

Separate established facts, confirmed decisions, proposals, assumptions, and unresolved questions. Supply background and actual rationale according to reader dependence. Keep the necessary knowledge in the model and its explicit references, not solely in session context.

Revise owning sections and synchronize dependent diagrams, scenarios, and rules under REQUIREMENTS-MODEL.md. Apply WORKFLOW-ARTIFACTS.md for revision identity, review/approval applicability, and historical records; keep only current approval metadata in the model.

On resumption, perform the shared recovery procedure and reuse settled requirements, but always run step 4 before an approved handoff. As controller, maintain `issue.md` and persist recovery state before blockers or handoffs. An inherited `Approved` label does not bypass review.

## 4. Verify, review, repair, and review again

Before dispatch, check the complete assigned model or selected composite package against REQUIREMENTS-MODEL.md. For a heavyweight handoff, the root controller checks the shared model and applicable children together, including cross-child meanings, flows, rules, and coverage; local Passes do not establish package consistency. This is the requirements review, not an additional generic review stage. Correct omissions and contradictions and resolve material decisions. Render and visually inspect all required Mermaid diagrams with current evidence. Missing required access, decisions, rendering, or inspection keeps `Draft`; author checks never replace independent review.

Dispatch a fresh independent, read-only reviewer for every round using [reviewer-prompt.md](reviewer-prompt.md), supplying its complete input package under the shared dispatch rules. If independence, required inputs, or verification are unavailable, retain `Draft` and report the blocker; self-review never substitutes.

The assigned record writer persists every returned review in the owning log before repair or advancement: child model records in the child log, root/package records in the root log. Use WORKFLOW-ARTIFACTS.md for record fields, finding closure, and snapshot applicability; request correction of stale, incomplete, or inconsistent reports.

For `Changes required`, repair owning sections and all dependent views. Recover evidence and settled answers before asking new questions. For `Blocked`, obtain missing inputs or verification. Persist repairs and fresh evidence before requesting another fresh **full-model or full-package** review, including prior findings and regressions. Save the independent disposition and update the assigned entry before advancing. Repeated attempts do not waive a gate.

Only a current independent `Pass`, with every applicable criterion satisfied, mandatory verification complete, and no unresolved finding or blocker, permits step 5. Changes to content, diagrams, or required references return to `Draft` and this loop; apply the shared metadata-only exception.

## 5. Obtain final human approval and stop

After the applicable review passes, set `Awaiting approval`. Present exact model/package paths and scope, its passing conclusion, main flows, and consequential decisions. Ask explicitly for approval of this reviewed basis: standalone requirements for technical clarification, or the selected heavyweight shared/child package for formal architecture. A child-only approval covers that child, not the composed package. Package approval may cover its identified shared and child sources together; do not require circular separate approvals first.

Wait. Agreement with interview answers, approval of a proposed correction, or approval given before the current model passed review is not final approval. If the human requests changes, return to clarification as needed, integrate the changes, run the review-and-repair loop again, and request approval of the resulting reviewed model.

Record `Approved` only for the same current model/package that passed review and received explicit final human approval. Persist the decision in its owning log and link current metadata and entries using WORKFLOW-ARTIFACTS.md. The root entry identifies the exact heavyweight package and applicable records, not a separate manifest. Source changes require impact assessment and renewed affected gates, preserving unrelated approvals only with an explicit basis. An unchanged resumed model may retain evidenced final approval after current review; a label alone is insufficient.

Return the assigned entry, approved model/package identities, applicable approval evidence, and essential references; child work returns to the root controller. If blocked, return the draft and persisted blocker, never an approved handoff. Stop: the next separately authorized stage is `clarify-architecture` for heavyweight packages or `clarify-technical-design` for standalone work. Do not generate architecture, technical models, tickets, code, or `delivery.md` here.

For scoped changes to an existing implemented system, route to `clarify-change`, loaded by name only when that stage is authorized, to reconstruct any missing baseline and clarify requirements with their technical consequences in one coordinated package. That route synchronizes affected canonical sections and obtains its own independent review and human approval; it does not silently retain this model's old approval for changed content. The full-model gate above remains the workflow when using clarify-requirements itself.
