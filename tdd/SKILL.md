---
name: tdd
description: Use for test-first features, bug fixes, and behavioral integration tests. Independent reviewers read this skill's TESTING.md directly.
---

# Test-Driven Development

Use this method to implement or repair assigned behavior through its agreed interfaces. Read [TESTING.md](TESTING.md) before constructing tests. Work in the current implementer context; behavior selection and coding belong to the same loop.

## 1. Choose the next behavior

Inspect the repository's runner, nearby tests and fixtures. Follow an assigned requirement through its public interface and compare existing coverage with the outcome a caller needs. Select one meaningful uncovered behavior and an independent expected result. Choose the test boundary and fixtures yourself within the settled interfaces and assigned flows.

Reuse relevant existing evidence. For behavior-preserving work, use the regression approach in TESTING.md instead of inventing a failing test.

## 2. Run one vertical cycle

1. Write one test for the chosen behavior.
2. Run it before implementation and observe failure caused by that behavior, not broken setup.
3. Implement the behavior in its approved owner, using the existing collaboration and structure.
4. Run the test and relevant regressions for green; investigate and repair failures against the contract.
5. After green, make useful local cleanup and rerun affected checks. Cleanup is optional, not a ritual or a reason to redesign.
6. Compare the result with remaining obligations and choose the next actual gap.

Complete each test/implementation cycle before starting the next, rather than writing all tests first. Use engineering judgment to produce a complete implementation, not merely code that recognizes the test inputs.

## 3. Return the evidence

Return the covered behavior, actual check results, remaining gaps and material limits. The caller handles any broader verification, review and delivery.
