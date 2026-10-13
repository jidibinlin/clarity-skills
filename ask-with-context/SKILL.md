---
name: ask-with-context
description: Use before asking a user for a consequential decision or clarification, or when they need background to answer a question. Establish shared understanding and use focused diagrams, comparison tables, or prose before asking. Usable independently or as a communication reference for another skill.
---

# Ask With Context

Make the user ready to decide before asking them to decide. The user should not need several follow-up turns to recover the background, decode terms, or discover consequences that the agent already knows.

This self-contained skill owns question preparation and communication, not a workflow stage. It needs no other skill, repository, artifact directory, reviewer, or approval process. Apply it within the active task's authorization and language. Reference-only loading provides guidance without starting an interview. Consuming skills retain their scope, investigation, recording, verification, and approval rules; an answer to a question does not approve a later artifact or authorize execution. Applying steps 1–4 is mandatory before every substantive question, including follow-ups, resumed work, and questions after repairs; apply step 5 after each answer. Having loaded this skill is not evidence that a question complies.

## 1. Decide whether to ask

Identify the unresolved decision and what different answers would materially change. Use accessible evidence, confirmed answers, and applicable conventions first; do not ask the user to rediscover repository facts or choose incidental details. Disclose inaccessible evidence rather than inventing it. Ask when missing human knowledge, preference, or authority actually changes the answer. A contradiction with an established obligation calls for correction, not a vote to ignore it. Distinguish a risk from an agreed guarantee and a possible mitigation from a required mechanism: identifying a failure possibility does not authorize adding recovery capabilities or expanding scope. Establish the required outcome before asking how to achieve it. Required document-write confirmation is authority, not an incidental design question: do not skip it because the answer or correction seems obvious.

Prioritize uncertainty that changes the current understanding or enables other decisions. Ask one focused question or a short group of independently answerable questions; defer dependent choices. Do not enumerate a decision tree or turn a completeness checklist into a questionnaire. A sufficiently specified request may need no questions.

## 2. Establish the knowledge needed to answer

Build the shared causal explanation before presenting the choice. According to the decision's dependence on background, explain:

- The concrete situation, relevant current behavior or confirmed constraints, and why this question arises now.
- The mechanism or relationship needed to understand it. Explain unfamiliar terms where they matter, in terms of behavior or responsibility, not a detached glossary.
- What is already settled, what remains undecided, and how the unresolved choice affects observable outcomes, ownership, risk, or cost.

Distinguish inspected facts, user constraints, assumptions, and proposals. Do not present a candidate design as existing behavior or a hypothesis as an approved constraint. Include the decisive context in this exchange; references support it but do not send the user away to reconstruct the explanation.

Scale depth to the actual knowledge gap, not a fixed sentence count or assumed expertise. Reuse demonstrated shared understanding and explain only the missing or changed relationships; neither a terse premise nor a general tutorial is the target. Do not require the user to confirm “I understand” before every decision.

## 3. Choose the clearest representation

Use a diagram proactively when a consequential structure or interaction is complex enough that prose makes the user reconstruct it mentally. Use a table when comparison across common dimensions or mappings is the comprehension problem. Simple questions need neither. Select for the relationship being explained, not to fill a presentation template:

| Understanding needed | Useful representation |
| --- | --- |
| Order, calls, waiting, overlap, completion, failure propagation | Sequence diagram |
| Branches, conditions, paths, scope boundaries | Flowchart |
| Object, module, or process collaboration; state and responsibility ownership | Topology diagram |
| Legal transitions, lifecycle, completion states | State diagram |
| Alternatives along shared criteria, before/after differences, responsibilities or contracts mapped consistently | Table |
| A small distinction or rationale with no useful structural comparison | Prose or a concrete example |

Use Mermaid where supported for the relevant diagram types. Keep only the participants and surrounding context needed to understand the current decision; a whole-system diagram that makes the user hunt for the issue is not alignment. Show decision-sensitive points such as return versus persistence, ownership boundaries, or failure branches explicitly. Label current facts, candidates, and unknowns; keep names, scope and visual granularity consistent across alternatives. Check directions, labels, branches and consistency with the explanation. Do not claim rendering or visual inspection unless actually performed; the caller's mandatory artifact-verification rules still apply.

Tables must compare genuinely comparable options using consistent dimensions, conditions, units, and definitions. Include material disadvantages and unknowns; do not invent measurements, precise estimates, scores, or symmetric alternatives to fill cells. A long text dump in cells is not a useful comparison.

A diagram may explain an interaction while a table compares its consequences, but each must contribute something distinct. Put each idea in its clearest form once. Text supplies missing context, non-obvious consequences, decisive rationale, and the question—not a line-by-line transcription of the visual. If the interface cannot display a useful visual, provide an equivalent readable explanation and disclose the limitation rather than relying on an unseen image.

## 4. Required question format and pre-send check

For a decision that depends on background or involves consequential alternatives, use visibly labeled blocks in the user's language, in this order:

- **Context and impact:** present the concrete situation and causal explanation from step 2, with the representation chosen in step 3. When proposing a change, make current behavior, the candidate change, and its observable consequences explicit. Explain what changes hands, moves, or completes differently instead of naming a mechanism and expecting the user to infer its meaning.
- **Options and tradeoffs:** compare genuine alternatives by their concrete outcomes and costs. Recommend one only with its actual deciding evidence or constraint. Distinguish different failure points or ownership boundaries before discussing their remedies; do not bundle unrelated problems into one implementation choice.
- **Decision needed:** ask exactly which unresolved judgment is needed now. Defer dependent choices; do not ask for a vague reaction to the whole design.

A simple factual clarification can use concise prose. Omit the alternatives block when asking for a missing fact, rather than fabricating options; necessary context and a precise question still apply. Visible structure must carry the explanation, not empty headings, jargon, or a mandatory tutorial.

Before sending, check the actual outgoing question, not your private understanding: can the user explain the situation, the specific decision, and the main consequences using this message and demonstrated shared context? Are facts distinguishable from candidates, separate problems distinguishable from each other, and the needed diagram or comparison present? If not, rewrite before asking. This is a mandatory author check, not a request for the user to approve the explanation. If the user reports confusion, repair the missing relationship under step 5 instead of repeating the options or claiming that the skill was followed.

If using a structured question/choice widget, present necessary context and visuals before it; short option labels do not replace the explanation. Wait for the answer. A request for explanation is not a selection, and silence is not consent.

## 5. Resolve the question and continue the active task

If the user asks for missing background, address that gap and restate the still-open decision using the corrected explanation. Do not repeat the unexplained options or respond with disconnected fragments. Correct affected diagrams/tables as understanding changes, and distinguish new facts from a changed decision.

After an answer, reconcile its effect, necessary background and actual rationale in the conversation first. An answer about direction does not approve unwitnessed document content. Follow the caller's write gate: show exact proposed content/patch and destination, obtain explicit confirmation, then write only it. No candidate, Draft label, placeholder, wording cleanup or review fix bypasses that gate. Retain unanswered parts and dependent choices in the conversation, revisit affected assumptions and remove superseded questions with their reason; resolving one question does not finish the interview.

Continue from that reconciled state in the same turn:

- Resolve accessible evidence and incidental design details yourself, without treating that as permission to write documents. If a document write needs confirmation, present the exact proposed update; otherwise ask the next ready material question using steps 1–4. Do not end with an acknowledgement or offer to continue while actionable work remains.
- A blocked or deferred item does not stop independent ready items. Preserve its missing prerequisite or owning later stage; deferral must respect the agreed scope, not hide an unmet current-stage obligation.
- When no material choice remains for this stage, return to its required modeling, verification, and review steps without inventing more questions. The caller determines stage completeness; an interview answer is not artifact approval or authorization for another stage.
- If only genuinely blocked work remains, state unresolved items and their unblock conditions in the conversation. Honor an explicit pause or redirection; do not create unapproved document placeholders for the unresolved items.

Use the caller's existing canonical destinations only after its write gate; create no separate draft, state file, decision queue or questioning log. Standalone communication needs no artifact. The suite's `issue.md` is definition/navigation, not interview progress. This communication skill never waives the caller's required write confirmations, review or final approval.
