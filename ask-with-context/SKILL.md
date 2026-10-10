---
name: ask-with-context
description: Use before asking a user for a consequential decision or clarification, or when they need background to answer a question. Establish shared understanding and use focused diagrams, comparison tables, or prose before asking. Usable independently or as a communication reference for another skill.
---

# Ask With Context

Make the user ready to decide before asking them to decide. The user should not need several follow-up turns to recover the background, decode terms, or discover consequences that the agent already knows.

This self-contained skill owns question preparation and communication, not a workflow stage. It needs no other skill, repository, artifact directory, reviewer, or approval process. Apply it within the active task's authorization and language. Reference-only loading provides guidance without starting an interview. Consuming skills retain their scope, investigation, recording, verification, and approval rules; an answer to a question does not approve a later artifact or authorize execution.

## 1. Decide whether to ask

Identify the unresolved decision and what different answers would materially change. Use accessible evidence, confirmed answers, and applicable conventions first; do not ask the user to rediscover repository facts or choose incidental details. Disclose inaccessible evidence rather than inventing it. Ask when missing human knowledge, preference, or authority actually changes the answer. A contradiction with an established obligation calls for correction, not a vote to ignore it.

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

## 4. Ask the decision, not for a vague reaction

Offer genuine alternatives with concrete consequences when alternatives exist. Recommend one only with its actual deciding evidence or constraint; expose the tradeoff rather than steering through loaded labels or omitted costs. A missing fact may need a direct question instead of fabricated choices. Ask exactly what human judgment is needed, not whether the whole explanation “looks good.”

Before sending, check whether a user who has not read the agent's source material or participated in its private deliberation can understand why the question exists, what it decides, and the main consequences from this explanation and established shared context. Repair missing causal links before asking. This is an author check, not a separate user gate or mandatory set of headings.

If using a structured question/choice widget, present necessary context and visuals before it; short option labels do not replace the explanation. Wait for the answer. A request for explanation is not a selection, and silence is not consent.

## 5. Repair understanding and hand back

If the user asks for missing background, address that gap and restate the still-open decision using the corrected explanation. Do not repeat the unexplained options or respond with disconnected fragments. Correct affected diagrams/tables as understanding changes, and distinguish new facts from a changed decision.

After an answer, briefly clarify its effect when useful and return the decision, necessary background, and actual rationale to the active task. The owning workflow integrates them into its current model and records under its own rules. Do not create a separate questioning log, transcript artifact, approval ceremony, or automatic next stage. Stop asking when the current decision is sufficiently resolved; the caller determines overall stage completeness.
