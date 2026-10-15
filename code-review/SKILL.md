---
name: code-review
description: Review changes against requirements, technical design and repository standards through independent Spec and Standards subagents. Return both reports separately with their reviewer references.
---

# Code Review

Two-axis review of the supplied changes:

- **Standards:** Does the code follow repository standards and sound engineering practices?
- **Spec:** Does the code correctly implement the requirements and technical design?

Run the axes in parallel subagents so they form independent judgments.
Return their reports separately to the caller.

## Process

### 1. Pin the review range

Use the comparison point or commit range supplied by the caller.
Resolve ambiguous scope from the task and repository before asking the caller.

Capture the chosen diff command and commit list once.

For an explicit base/head range:

```bash
git diff <base>..<head>
git log <base>..<head> --oneline
```

For a fixed-point comparison against the merge-base:

```bash
git diff <fixed-point>...HEAD
git log <fixed-point>..HEAD --oneline
```

Confirm that the references resolve and the diff is non-empty before dispatching reviewers.
Report an invalid reference or empty scope before starting subagents.

### 2. Identify the Spec sources

Find the governing sources in this order:

1. Approved requirements, technical design and subsequent confirmed changes supplied by the caller.
2. Governing documents referenced by the task or commits.
3. Relevant requirements/design documents in the repository.

If the sources cannot be located, ask the caller where they are.
Do not invent requirements or substitute an unconfirmed proposal.

If no Spec basis exists, skip the Spec subagent and report
"Cannot assess — no Spec basis available", not Pass.

### 3. Identify the Standards sources

Find the repository's documented coding standards, such as
CODING_STANDARDS.md, CONTRIBUTING.md and applicable project instructions.

Use TESTING.md from registered tdd as an additional test-quality standard.

The Standards axis also carries the Fowler code-smell baseline below
(Refactoring, chapter 3), even when the repository documents no standards.

Two rules govern this baseline:

- **Repository standards override it.** Suppress a smell where a documented project standard endorses the pattern.
- **Smells are judgment calls.** Label them as possible problems, not automatic violations.

Skip checks already enforced by tooling.

Each smell describes a recognition signal and a possible improvement:

- **Mysterious Name:** A function, variable or type whose name does not reveal what it does or holds. → Rename it; difficulty finding an honest name may indicate an unclear design.
- **Duplicated Code:** The same logic shape appears in multiple changed locations. → Extract the shared logic and reuse it.
- **Feature Envy:** A method reaches into another object's data more than its own. → Move the behavior toward the data it operates on.
- **Data Clumps:** The same fields or parameters repeatedly travel together. → Represent the related values as one type.
- **Primitive Obsession:** A primitive or string stands in for a domain concept that deserves its own type. → Introduce an appropriate domain type.
- **Repeated Switches:** The same branching on a type recurs across the change. → Consider polymorphism or a shared dispatch map.
- **Shotgun Surgery:** One logical change requires scattered edits across many files. → Gather the parts that change together.
- **Divergent Change:** One module changes for several unrelated reasons. → Separate responsibilities that change independently.
- **Speculative Generality:** Abstractions, parameters or hooks serve needs absent from the Spec. → Remove the unnecessary generality.
- **Message Chains:** Callers depend on long navigation chains through collaborators. → Hide that navigation behind an appropriate interface.
- **Middle Man:** A class or function mainly forwards calls without adding responsibility. → Remove unnecessary indirection.
- **Refused Bequest:** A subtype ignores or overrides much of its inherited behavior. → Reconsider the inheritance and consider composition.

Judge these improvements in the repository's context.
Explain the concrete consequence of any smell reported.

### 4. Dispatch both review subagents in parallel

Give both reviewers the same change range and commit list.
Include the shared evidence and assessment requirements below in each prompt.

**Standards subagent inputs:**

- The full diff command and commit list.
- The applicable standards-source files.
- The registered tdd TESTING.md reference.
- The complete smell baseline above, pasted in full; the subagent does not inherit the caller's context.

**Standards brief:**

> Report, per file or hunk where relevant:
> (a) violations of documented standards, citing the source file and rule;
> (b) possible baseline smells, naming the smell and quoting the affected code.
> Distinguish documented-standard violations from judgment calls.
> Repository standards override the generic baseline.
> Skip checks already enforced by tooling.
> Explain why each finding matters in this codebase.
> Keep the report under 400 words.

**Spec subagent inputs:**

- The full diff command and commit list.
- The requirements and technical-design paths or contents.
- Subsequent confirmed changes that affect this review.

**Spec brief:**

> Report:
> (a) requirements that are missing or only partially implemented;
> (b) behavior that was not requested;
> (c) requirements that appear implemented but are implemented incorrectly.
> Cite the governing requirement or design section for each finding.
> Allow ordinary implementation choices within the intended behavior,
> contracts and binding design decisions.
> Distinguish source-design problems from implementation defects.
> Keep the report under 400 words.

**Shared evidence and assessment requirements:**

- Ground findings in inspected code and relevant collaborators, not only the implementer's report.
- Assess verification claims against applicable test and runtime evidence.
- State material gaps and limits. Isolated tests do not establish an end-to-end result.
- Give findings IDs, severity, code locations, governing criteria, evidence and impact.
- Separate blocking findings from optional suggestions.
- Return a verdict: Pass, Needs changes or Cannot assess.
- Do not claim Pass when missing basis or evidence prevents assessment.

Reviewers inspect and report; they do not change the implementation.

### 5. Return the reports

Present the reports under separate ## Standards and ## Spec headings.
Return them verbatim or lightly cleaned.

Do not merge or rerank findings across axes.

End with a short summary for each axis:
- Verdict.
- Total findings.
- The most severe issue within that axis, if any.

Return the corresponding reviewer agent references with the reports.
If an axis was skipped, state why; do not represent it as passed.

The caller owns subsequent actions.

## Why two axes

A change can pass one axis and fail the other:

- Code follows every standard but implements the wrong thing:
  Standards pass, Spec fail.
- Code implements the requested behavior but violates project standards:
  Spec pass, Standards fail.

Separate reports prevent one axis from masking the other.
