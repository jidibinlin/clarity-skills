---
name: review-records
description: Reference for Clarity review submissions, reports, finding-linked repair decisions and approval records.
---

# Review Records

Use this format for an object's review-fix-decisions log. Read it when preparing or recovering review records, not to begin clarification. `artifact-layout` defines locations; the owning stage governs review, repair and approval.

The assigned writer preserves reports from the independent reviewer, decisions from the original author/implementer, and approvals from the human.

## Record identity

Identify the object and scope, with resumable author/reviewer handles in a compact header. Ticket role bindings stay in the ticket's execution block. Record actual replacements and the transferred context when a participant becomes unavailable.

Identify reviewed artifacts and governing sources by path and verifiable version. Code versions include relevant uncommitted work. Link evidence that lets a later reader understand what was reviewed and what changed.

## Admitted events

| Event | Contents |
| --- | --- |
| **Submission** | Scope, result and source versions, governing standards, applicable human confirmations, verification results and limits. |
| **Review result** | The reviewer's actual report, including failed or blocked reviews. |
| **Repair decision** | Finding IDs, chosen correction, necessary background and decisive rationale, consequences, conformity to the approved design, resulting changes and verification. Include confirmation for specification changes and the later reviewer disposition. |
| **Human approval or acceptance** | The explicit decision and reviewed scope/version, with a faithful quotation or durable reference. |

Use links to accessible evidence rather than copying it. Explain consequential autonomous repair choices so the human can understand what was decided. Distinguish planned checks from actual results and disclose substitutions or missing verification.

## Review report

Include:

- Scope, reviewer, reviewed version and governing sources/standards.
- Evidence supporting the assessment and its limitations.
- Verdict: `Pass`, `Changes required` or `Blocked`.
- Findings with stable IDs, violated criterion, location, evidence, significance and a clear closure condition.
- Disposition of prior findings, retaining their IDs.
- Blockers and what is needed to resolve them.

`Pass` means the applicable standard is satisfied without unresolved findings or blockers; it is not human approval. Findings describe demonstrated violations, not reviewer preferences. Missing evidence is a verification gap, not proof of a defect.

The reviewer closes findings. An author's repair remains awaiting review until that disposition. Preserve historical reports and decisions rather than rewriting past outcomes.

## Keep records factual and bounded

Record review events and finding-linked decisions, not routine development progress, interview transcripts, private reasoning or speculative proposals. A clean submission needs no invented repair entry. Specifications remain the authority for the design; logs cannot change them or substitute for human confirmation. Keep secrets out of records.
