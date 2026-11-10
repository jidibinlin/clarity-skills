# Independent Requirements Reviewer

Review read-only. Return findings to the original authors rather than rewriting their models.

## 1. Assemble the current assignment

Read [REQUIREMENTS-MODEL.md](REQUIREMENTS-MODEL.md). Resolve resources through their installed owners; use the `artifact-layout` skill for artifact conventions.

Receive the complete current model, original requirements and confirmed decisions, relevant source references, human confirmations, rendered views and relevant prior review conversations.

## 2. Reconstruct authorization and evidence chronology

Check **Authorization and evidence validity** against the supplied confirmations and review conversations. Establish that the result matches the confirmed content, that review remains independent, and that prior findings and repair responses describe the current work. Report missing evidence that prevents an assessment without reconstructing an administrative history unrelated to the result.

## 3. Trace behavior against the content standard

Trace intended outcomes from the original request through domain flows, rules and local acceptance. Walk the normal scenario and consequential variations; identify where the model leaves an outcome ambiguous or conflicts with confirmed intent. Follow source references when the decision depends on them.

Inspect the rendered views against the prose.

## 4. Reassess repairs and return evidence

Reassess the current scope, prior findings and regressions after repairs. Explain which findings are resolved and which remain.

Ground each finding in a content-standard obligation, the actual location and its consequence. Return `Changes required` for defects, `Blocked` when missing information prevents judgment, or `Pass` when the selected scope is sound with no unresolved findings or blockers. Return the assessment to the review initiator; final human approval follows separately.
