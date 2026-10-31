---
name: technical-clarification-collaboration
description: Opt-in pilot for technical clarification with shared existing-material survey owners and bounded clarification owners; coordinate macro understanding, dependencies and cross-topic decisions without centralizing all detailed reasoning.
---

# Technical Clarification Collaboration

Use when the human chooses this collaboration pilot for technical clarification. It does not establish suitability for requirements, architecture or other clarification workflows.

This skill supplies responsibilities and a default collaboration path, not a new stage or approval process. Continue using `clarify-technical-design` for stage coordination, its content standard and final review/approval; clarification owners use `technical-design-author` for confirmation, document writes and repairs, and `technical-clarification` for the clarification method. Use `communication-style` for human discussion. Resolve these through registered skills. Reading this skill alone does not start a formal clarification workflow.

## Two layers of work

- **Existing facts and explanations:** what code actually does, what documents state, how existing mechanisms behave, their limits and inconsistencies. Evidenced inference such as tracing execution order belongs here.
- **Goal-directed reasoning and decisions:** what those facts mean for the current objective, whether existing behavior satisfies it, what to change and which tradeoffs to accept. Main and clarification owners hold this responsibility with the human.

A documented decision, its current authority and the implemented behavior are distinct. Report disagreements rather than treating a document as proof of implementation. Follow the governing stage's decision authority; evidence about today's implementation does not silently override approved target behavior.

## Responsibilities, not fixed positions

Roles may be combined. One clarification owner can work with several survey owners; do not split clarification merely to populate a team.

### Main model — macro understanding and coordination

Establish and maintain the macro technical model: overall mechanisms, constraints, coupling and responsibility boundaries. Reuse survey owners' explanations rather than repeatedly reading and summarizing the same materials. Inspect a source when needed to resolve a concrete uncertainty, not as routine re-investigation of delegated work.

Decide which topics can advance independently, give them the applicable basis and boundaries, and keep their owners and contact routes discoverable. Update the macro model and assignments as new dependencies emerge. Hold enough understanding to coordinate and reconcile the whole, without re-deriving every local proposal.

Main can also be the only clarification owner. Delegating a topic transfers continuing clarification responsibility, not just preparation of a report.

### Shared survey owner — 调研负责人

Maintain an evidence-backed understanding of a bounded area of existing code and documents. Serve Main and relevant clarification owners directly; this capability is shared, not private to one topic.

Explain sources, observed behavior, evidence-backed inference, uncertainty and applicability. Distinguish unknown from absent, and a historical note from current code or an effective approved decision. Choose the useful response and evidence detail for the question; no fixed report template is required.

Keep callers' hypothetical designs separate from existing facts. If asked to select a new design, provide the relevant facts and limits and return the choice to the clarification owner. Familiarity with the implementation does not confer design or approval authority.

When new evidence changes an explanation, correct it and notify the consumers known to rely on it. Surface material changes of investigation direction, scope or shared constraints to Main so it can coordinate. This role need not track every design decision or create a separate knowledge system.

### Clarification owner — 澄清负责人

Continuously own a bounded technical decision loop: understand the applicable basis, consult shared survey owners directly, develop the proposal and clarify it with the human. Retain local reasoning and revise the proposal already discussed instead of restarting it on each response.

On taking ownership, briefly tell Main the intended direction and known research dependencies before developing the full proposal; do not wait for a reply to proceed. Thereafter, proactively surface material direction or scope changes, shared-premise changes and cross-topic disagreements, including their effect on the proposal. Direction synchronization is not a request for permission before every inquiry or local action.

Know the current survey contacts and their scope; ask Main to resolve a missing or ambiguous owner rather than silently duplicating an existing investigation. Reuse answers within their evidence and applicability; return to the original owner when they need clarification or revision.

### Expanded clarification lead — a temporary responsibility

For a cross-topic question, Main may designate an existing clarification owner to take a broader scope. The lead owns the common question, gathers constraints directly from affected peers and continues the human-facing clarification. Other owners retain unaffected topics and assess the common proposal's impact on their areas. Survey owners remain shared evidence providers.

This expands responsibility, not rank. It does not authorize overriding confirmed choices, approving a proposal for the human or absorbing unrelated topics. Main defines the affected boundary; adjust it again if the problem proves different.

## Basic collaboration path

1. Main establishes macro understanding with survey support and identifies useful clarification boundaries. Preserve the governing stage's confirmation before dependent design.
2. Clarification owners advance with the human and consult existing survey owners directly. Keep material direction and dependencies visible; do not forward every exchange or require periodic status reports.
3. When topics intersect, assess what needs joint treatment. A direct exchange may suffice; Main can change boundaries or sequence work, convene joint clarification, or designate an expanded lead. Do not mechanically escalate every disagreement.
4. The responsible owner brings a coherent proposal and consequential unresolved choices to the human. Follow the existing stage's confirmation unit, not independent approvals for fragments of a coupled design.
5. Feed confirmed outcomes, applicable premises and cross-topic effects back into the overall model and affected topics. Reuse the existing canonical artifacts and their assigned writers; do not create a second approval registry or knowledge repository.

If evidence invalidates a shared premise, separate the affected guarantees from still-valid local work. Notify the relevant owners, revisit dependent decisions with the human as needed, and let Main coordinate the shared issue without taking all local reasoning back.

## Human contact and integration

Make clear which owner continues each topic and how the human can reach it using the available harness. Do not invent cross-tab routing or assume a background worker has a user-facing channel.

Where direct human contact is available, the owner uses it. Otherwise Main may relay the owner's human-facing proposal and the human's reply, preserving the owner's context and responsibility. The owner still explains options, revises the proposal and resolves follow-up questions; do not stop at “Main should clarify this with the human.” Relaying a message does not make Main the new author or confer approval.

Main integrates confirmed outcomes and checks shared consistency without routinely asking the human to confirm unchanged local decisions again. Preserve final whole-model review and approval required by the technical clarification stage. Where confirmed choices conflict or premises change, surface the specific issue rather than silently choosing a winner.

Keep the arrangement proportional. Fixed staffing, mandatory report forms, extra gates and a new team infrastructure are not prerequisites for this pilot.
