---
name: code-review
description: Review code against requirements, technical design and project standards, for an implementation unit, combined result or standalone code review.
---

# Code Review

Work as the assigned independent reviewer. This is your inspection method, not a dispatcher for additional reviewers. Return an assessment; the implementation workflow handles repairs and records.

## 1. Establish the scope and basis

Read the requested scope, governing requirements/design, applicable project and review standards, current code, verification evidence and any prior findings. Include relevant uncommitted work. Use the supplied comparison point or diff to locate changes, then follow their callers and surrounding implementation.

For standalone review, use the available request and project contracts as the basis. Identify missing information that affects the assessment rather than inventing requirements.

## 2. Trace behavior and inspect the implementation

Follow the required behavior from real entry points through state owners and collaborators to observable outcomes. Compare the result with the intended behavior and technical design: look for missing or additional behavior, incorrect contracts and structural drift.

Assess engineering quality against project conventions and applicable standards as well as functional conformance. Investigate concrete maintainability or correctness problems in their surrounding code; explain their consequence rather than prescribing a preferred style. Treat a defect in the approved design as a source-design issue, not permission to redesign the implementation silently.

## 3. Assess tests and runtime evidence

Read `TESTING.md` directly from registered `tdd` when assessing tests; this does not run the author's TDD method. Examine the behaviors and real interactions the tests establish, together with their execution results.

Check assigned runtime and whole-flow obligations against actual participants and outcomes. Reuse applicable evidence and run focused checks when needed. State material gaps and substitutions; local tests alone do not establish a combined result.

## 4. Report and reassess

Use the caller's reporting format; Clarity implementation assignments supply `review-records`. Tie findings to the affected code, governing obligation or quality criterion, evidence and consequence. Distinguish implementation defects, source-design issues and missing verification.

On re-review, follow the repairs and their impact on the current assigned result, including regressions. Keep prior finding IDs and state their dispositions. Return the report to the assigned writer; leave code changes to the original implementer. A passing review is not human acceptance.
