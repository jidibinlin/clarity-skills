---
name: implement
description: Complete one approved ticket or bounded direct change, including verification and independent review; continue its existing implementation or repair when present.
---

# Implement

```mermaid
flowchart TD
    Implement["Implement with TDD"] --> Verify["Verify implementation"]
    Verify --> Commit["Commit task changes"]
    Commit --> Delegate["Delegate independent subagent<br/>Use code-review skill"]
    Delegate --> Review["Review current result"]
    Review --> Pass{"Pass?"}
    Pass -->|Yes| Return["Return result"]
    Pass -->|No| Fix["Fix implementation"]
    Fix --> Reverify["Verify fixes"]
    Reverify --> FixCommit["Commit this round's changes"]
    FixCommit -->|"Same review subagent"| Review
```

Read the assigned requirements, design and relevant code.

Use `tdd` in the current context to implement the work.
Follow repository conventions.
Complete affected callers, tests and documentation.

Apply engineering judgment within the intended behavior and design.
Resolve ordinary implementation details independently.
Discuss consequential changes to behavior, contracts or architecture.

Run relevant project checks and the full test suite.
Exercise the actual changed behavior.
Report actual results and material limits.

Complete implementation and verification.
Commit only this task's changes before the first review.

Delegate review to an independent subagent.
Have the subagent use the `code-review` skill.

If issues are found:
- Fix the implementation.
- Verify the fixes.
- Commit only this round's changes.
- Resubmit the new commit to the same review subagent.

Repeat the repair–verification–review loop until Pass.
Return the completed result to the caller.
