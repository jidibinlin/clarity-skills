---
name: implement-unit
description: Complete one approved ticket or bounded direct change, including verification and independent review; continue its existing implementation or repair when present.
---

# Implement Unit

Own one implementation unit through Pass. The same implementer uses `tdd` for initial behavioral work and behavioral repairs; the independent reviewer uses `code-review`. These are working methods, not additional agents or stages.

Read [IMPLEMENTATION.md](IMPLEMENTATION.md). Use the `artifact-layout` skill. Use the `review-records` skill for review/repair records and the `ask-with-context` skill for substantive human questions. Resolve companion files relative to this skill and cross-skill resources through their registered owners.

## 1. Understand the assigned work

Read the authorized ticket or full direct-change basis. Connect its obligations to the approved owners, interfaces and acceptance outcomes; inspect the relevant caller paths, existing implementation/tests and prerequisites. Include the setup and participants needed for assigned macro flows.

Make ordinary implementation choices within that design. Return consequential design gaps to their source authority. If the unit already has work or findings, reconcile them with current code and continue with the original implementer/reviewer pair.

Standalone execution establishes its workspace and arranges an independent reviewer. Delegated execution uses the controller's assignment, writer and review-dispatch route.

## 2. Implement the unit using TDD

Use the registered `tdd` skill in this implementer's current context. Use the unit's agreed behavior, interfaces and design as its basis. Let that method drive behavior selection and the test/implementation cycles until the assigned behavior is complete; it is not a testing phase after writing the code.

Complete affected callers, documentation and the approved cutover as those cycles progress. For behavior-preserving work, use TDD's existing-evidence/regression approach.

Exercise the full unit with IMPLEMENTATION.md's required checks and real flows. Behavioral failures return to the same TDD method; setup or nonbehavioral problems receive the appropriate correction and verification. When blocked, finish reachable work and identify the missing decision, input or evidence.

If a specification must change, show the proposed patch and consequences, obtain explicit human confirmation and write the confirmed change against its agreed basis. Eligible execution facts use the standard's automatic exception.

## 3. Review and repair with the original pair

Record the submission and actual verification evidence. Give the independent reviewer registered `code-review` with the unit scope, approved sources, current code/tests, results and prior findings. The standards are IMPLEMENTATION.md and `tdd`'s TESTING.md; use `review-records` for the report. Identify whether this is a ticket-local result or the entire direct change. A delegated implementer returns this assignment to the controller for reviewer dispatch.

Preserve the report and return findings to the original implementer. Behavioral defects return to step 2's TDD cycle; other implementation repairs use suitable verification, and source-design issues return to their authority. Record finding-linked repair decisions and renewed evidence, then give the current result and prior findings to the **same reviewer**. Repeat until Pass without unresolved findings or blockers; the reviewer closes findings.

## 4. Hand off

Record Pass and update eligible execution facts through the assigned writer. Return the result, evidence, limits and repair decisions.

- **Delegated:** return to the controller without per-ticket human acceptance or a separate delivery. Ticket Pass is local; a full direct-change Pass covers that complete change.
- **Standalone:** write the standard's delivery summary, request final human acceptance of the reviewed scope and record the decision. Revisions return through the original pair.

Stop at the authorized boundary; further work or publication needs its own authorization.
