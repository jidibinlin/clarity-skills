---
name: implement
description: Complete one approved ticket or bounded direct change, including verification and independent review; continue its existing implementation or repair when present.
---

# Implement

```mermaid
flowchart TD
    Implement["Implement with TDD"] --> Verify["Verify implementation"]
    Verify --> Commit["Commit task changes"]
    Commit --> Delegate["Use code-review in current context<br/>Skill dispatches independent reviewers"]
    Delegate --> Spec["Spec review"]
    Delegate --> Standards["Standards review"]
    Spec --> Reports["Separate reports"]
    Standards --> Reports
    Reports --> Pass{"Both axes Pass?"}
    Pass -->|Yes| Return["Return result"]
    Pass -->|No| Fix["Fix implementation"]
    Fix --> Reverify["Verify fixes"]
    Reverify --> FixCommit["Commit this round's changes"]
    FixCommit --> Resubmit["Send commit and evidence directly<br/>to original reviewers"]
    Resubmit --> Spec
    Resubmit --> Standards
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

Use the code-review skill in the current context.
If a review report is unclear, ask the original reviewer for clarification.

If issues are found:
- Fix the implementation.
- Verify the fixes.
- Commit only this round's changes.
- Send the new commit and verification evidence back to the same reviewers through their supported conversation channels.

Repeat the repair–verification–review loop until both axes Pass.
Return the completed result to the caller.
