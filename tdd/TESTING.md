# Behavioral Testing Standard

These criteria guide test construction and independent review. SKILL.md supplies the author method.

## Test value

Tests establish meaningful behavior through the relevant public interface: results, state, invariants and errors. Keep tests that detect a real gap and remain useful when implementation details change. Expected outcomes need an independent basis in the contract, not a reproduction of the implementation.

Use real owned collaborators for the behavior under test. Keep setup deterministic and follow project conventions. Explain material substitutions and what they leave unverified; a substitute cannot establish the real interaction it replaces. Test boundaries, fixtures and conventional test files are implementation choices, not separate approval requests.

## Behavioral evidence

For new or changed behavior, red demonstrates the intended fault before implementation; green demonstrates the repair and relevant regressions. Setup failure is not behavioral red. Evidence describes what actually ran and what it proves.

Reuse meaningful coverage and existing failures. A user-supplied failure is already observed; verify the repair rather than rerunning solely to confirm the report. For behavior-preserving changes, exercise the changed path with before/after regressions instead of manufacturing red.

When reliable automation is infeasible, state the limitation and exercise a suitable direct scenario without claiming automated TDD. These alternatives do not waive verification assigned by the caller.
