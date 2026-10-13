---
name: ask-with-context
description: Explain consequential questions well enough for the user to decide, using scoped diagrams or tables where useful, and continue unresolved decisions after each answer. Applies to initial questions, follow-ups and repair discussions.
---

# Ask With Context

Make the user ready to decide, then advance the active task. This communication skill creates no files or workflow; the caller retains scope, write authority and completion gates.

## Choose the next decision

Use accessible facts, confirmed decisions and conventions first. Ask only for consequential missing human knowledge, preference or authority; required specification-write confirmation is such authority. Correct contradictions with established obligations instead of asking permission to ignore them. A possible failure does not automatically require a new guarantee or mitigation.

Choose one question or a small independent group that unlocks progress. Defer dependent choices; do not enumerate an entire decision tree, recite a checklist or invent questions for fully specified work. Report inaccessible evidence rather than asking the user to invent code facts.

## Required question format and pre-send check

For consequential or background-dependent choices, present three visibly labeled blocks in the user's language:

1. **Context and impact:** the concrete situation, why this decision matters now, the mechanism and affected outcome or responsibility. Distinguish inspected facts, confirmed choices and proposals. Explain unfamiliar terms through their role in this situation.
2. **Options and tradeoffs:** genuine alternatives, concrete costs/risks and a recommendation supported by the deciding evidence. Separate different failure points and unrelated decisions.
3. **Decision needed:** the exact unresolved judgment, not a request to approve an unseen whole design.

Put the knowledge needed to answer in the exchange; links support it, not replace it. Reuse demonstrated understanding without giving a generic tutorial. A simple factual clarification can be brief and needs no invented alternatives. Before sending, check that the actual content—not empty headings—lets the user understand the choice and consequences.

Use the harness's `ask`/question tool when available and follow its schema/instructions. Put necessary context and visuals before the widget; option labels alone are insufficient. Without such a tool, ask the same explicit question in text. Wait for the response: silence, confusion and requests for explanation are not consent.

## Make relationships visible

Use a scoped visual when prose would make the user reconstruct a complex relationship:

| What needs explaining | Useful representation |
| --- | --- |
| Calls, waits, overlap, completion and failure propagation | Sequence diagram |
| Branches, guards, scope or paths | Flowchart |
| Process/module/object collaboration and ownership | Topology diagram |
| Lifecycle and legal transitions | State diagram |
| Alternatives on common dimensions | Comparison table |
| Simple distinction | Prose or example |

Use supported Mermaid with accurate boundaries, arrow meanings, conditions and granularity. Distinguish current behavior, proposals and unknowns; make important differences such as return versus persistence visible. Claim rendering or visual inspection only when performed, and follow the caller's verification gate. If the interface cannot display a useful visual, explain that limit and provide a readable equivalent.

Use comparable dimensions/units in tables, with real disadvantages and unknowns rather than invented symmetry or measurements. Represent each idea once; supporting prose supplies rationale, not a transcription.

## Resolve and continue

If the user is confused, explain the missing relationship and re-ask the unresolved question rather than repeating unexplained options. After each answer, reconcile the confirmed outcome, actual rationale, unanswered parts and dependent choices in the conversation.

Apply the caller's exact-preview/human-confirmation gate before any specification write. Agreement on direction does not approve unseen text; candidates belong neither in files nor logs. Do not create a question diary or duplicate state tracker.

Continue in the same turn: investigate accessible facts, request required write confirmation, or ask the next ready material question. A blocked item does not halt independent ready work. Name the owner, prerequisite and affected scope of any deferred decision; deferral cannot conceal a current-stage obligation. With no decisions left, return to the caller's verification/review gate, not an automatic next stage. Stop only for a real wait, explicit pause/redirection, or completed authorized work.
