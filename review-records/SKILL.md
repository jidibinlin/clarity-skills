---
name: review-records
description: Use when preparing a Clarity review submission, returning a report, recording a finding-linked repair or recovering existing review records. Reference only; not required for initial clarification.
---

# Review Records

The contents of an object's review-fix-decisions log. This reference skill does not start review, bind roles or grant write permission: stage skills decide when review happens, who acts, how repair proceeds and when approval is valid. The separately registered `artifact-layout` skill defines filenames and locations; consult it when those are needed.

Read this format when preparing a submission, returning a review, recording a repair, or interpreting existing review records. It is not a prerequisite for initial clarification. The assigned record writer preserves attributable events; the reviewer produces the report, the original author/implementer supplies repair decisions, and the human supplies approval or acceptance.

## Record identity

Use one compact header for object/scope and actual resumable author/reviewer handles, or references to composite owners. Ticket role bindings remain in the ticket's execution block. An actual role replacement is represented in its submission by old/new handles, the recovery limitation and transferred evidence; the header does not authorize replacement or require a placeholder reviewer.

Identify artifacts by path plus digest or other verifiable local revision. Code identity includes checkout and relevant dirty/untracked content, not only HEAD. Sources have exact paths/sections and revisions without recursive digest links. State the reviewed-content boundary where non-normative status/approval metadata is excluded, or explain a metadata-only difference explicitly. Digests do not reconstruct historical content: identify preserved comparison evidence or disclose its absence.

## Admitted events

Only these four event types belong in the log. Reference accessible evidence instead of copying it. A clean first submission needs no invented finding or repair entry.

| Event | Required contents |
| --- | --- |
| **Submission** | Reviewed scope/result and exact identity; governing standards and source/approval references; original requirement evidence; concrete prior specification-write confirmations; actual verification, environment/participants, substitutions and limitations. |
| **Review result** | The actual report, including failed or blocked outcomes, in the report format below. Attribute it to the reviewer without rewriting its verdict. |
| **Repair decision** | Existing finding IDs and affected scope; chosen correction, necessary background and decisive rationale; consequences and whether it conforms to approved design; resulting changes, actual checks and evidence; subsequent reviewer disposition. Explain consequential autonomous decisions; trivial repairs need only concise rationale. Specification repairs include the prior exact-write confirmation. |
| **Human approval or acceptance** | The explicit decision, exact reviewed scope/result and applicable sources, with faithful quotation or a durable decision reference. Direction agreement and permission to write are not recorded as final approval. |

Distinguish planned, executed, failed and passed checks. State actual participant substitutions and verification limits. An upstream referral records the conflict and links its eventual approved resolution; it does not duplicate the design discussion. Until independent disposition, a repair is recorded as addressed/awaiting review, not author-declared closure.

## Review report

A report contains:

- Scope, round/date, reviewer, exact current result and governing sources/standards.
- Evidence-backed coverage of every applicable stage criterion: `Satisfied`, `Violated`, `Unverified` or justified `Not applicable`, with limitations.
- Verdict: `Changes required`, `Blocked` or `Pass`. The stage's review contract determines the verdict; `Pass` represents satisfied applicable obligations without unresolved findings/blockers, not human approval.
- Findings with stable IDs, violated obligation, location/behavior, evidence, necessary background/significance and observable closure conditions.
- Prior finding dispositions: resolved, unresolved, withdrawn with reason or unverified. Keep the original IDs and attribute the disposition to the reviewer.
- Blockers with affected checks and exact unblock conditions. Report `None` explicitly when findings or blockers are absent.

Preserve historical reports and dispositions rather than rewriting past outcomes when evidence changes. A finding records a demonstrated violation, not a reviewer preference or authority to invent a new design. Missing evidence is represented as a limitation/blocker, not a fabricated defect.

## Keep records factual and bounded

Record review evidence and finding-linked decisions, not routine investigation, development progress, interview transcripts, speculative proposals or private reasoning. No finding means no repair entry; ordinary human-requested design changes belong in the model and a later submission, not a manufactured fix history.

Records cannot override specifications or authorize an unseen specification write. Include attributable confirmation evidence, not remembered consent or fabricated retroactive approval. Keep credentials and secrets out. The stage presents consequential autonomous repair decisions to the human; this format makes them discoverable without turning the log into a work diary.
