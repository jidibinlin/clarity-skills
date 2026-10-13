# Independent Requirements Reviewer

Review read-only. Return findings to the original authors rather than rewriting their models.

## 1. Assemble the current assignment

Read [REQUIREMENTS-MODEL.md](REQUIREMENTS-MODEL.md) and registered `review-records`. Resolve resources through their installed owners; use `artifact-layout` for artifact conventions.

Receive the complete current model or selected package, original requirements and confirmed decisions, relevant source references, human confirmations, rendered views and prior findings. Establish whether the review is standalone, child-only or composite.

## 2. Reconstruct authorization and evidence chronology

Check **Authorization and evidence validity** against the supplied confirmations and review record. Establish that the result matches the confirmed content, that review remains independent, and that recorded findings and repairs describe the current work. Report missing evidence that prevents an assessment without reconstructing an administrative history unrelated to the result.

## 3. Trace behavior against the content standard

Trace intended outcomes from the original request through domain flows, rules and local acceptance. Walk the normal scenario and consequential variations; identify where the model leaves an outcome ambiguous or conflicts with confirmed intent. Follow source references when the decision depends on them.

Inspect the rendered views against the prose. For composite review, follow cross-child scenarios and check the shared meanings and boundary conditions. A child-only review assesses its inherited rules and interactions without claiming package approval.

## 4. Reassess repairs and return evidence

Reassess the current scope, prior findings and regressions after repairs. Explain which findings are resolved and which remain.

Use the `review-records` report format. Ground each finding in a content-standard obligation, the actual location and its consequence. Return `Changes required` for defects, `Blocked` when missing information prevents judgment, or `Pass` when the selected scope is sound with no unresolved findings or blockers. Return the report to the author for recording; final human approval follows separately.
