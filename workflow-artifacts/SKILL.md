---
name: workflow-artifacts
description: Shared reference for private workflow storage, records, recovery, and delivery summaries. Load for authoring, coordinating, reviewing, or resuming this suite's work; loading it does not execute a workflow.
---

# Workflow Artifacts

Every role must read the complete [WORKFLOW-ARTIFACTS.md](WORKFLOW-ARTIFACTS.md) before starting or resuming its work. Authors use this and the applicable stage standard to guide generation; reviewers use the same criteria. This reference owns no execution: workspace setup, writing, dispatch, and approval belong to the authorized consuming stage. Reviewers remain read-only.

## Loading skills and their resources

Install each skill and its declared dependencies as complete directories through the harness. Dependencies need not be siblings and are not assumed to install automatically. This skill needs only its own directory.

Load dependencies by registered name through the Skill tool or the harness's equivalent mechanism; omp uses `skill://<name>` and `skill://<name>/<resource>`. Use the resolved installed owner, not guessed configuration paths, source-checkout paths, or `../` traversal. Resolve companion links relative to their owning skill/document. Mentioning a slash command is not loading it.

When only a standard or reviewer contract is needed, load **reference-only**: read the requested material and its mandatory dependencies, then return without executing that skill's steps or prerequisites. A dependency load never authorizes another stage.

Reuse complete current supplied standards, or read verified resource locations identified by their owning skill. Intact supplied content needs no recursive reload; a summary or remembered version is insufficient. Missing, ambiguous, or inaccessible dependencies block affected work. Report the exact resource/access need; do not auto-install or substitute another skill.

## Keep installation and project roots separate

The **skill root** contains read-only instructions, including when globally installed, symlinked, or cached. The **project root** is the actual target checkout: resolve code, commands, project links, Git exclusion, and `.scratch/<work-slug>/` there. Loading skills does not change the working directory or authorize writing into their installation. Reconcile both roots on resumption.

Each dispatch supplies the target checkout/work identity, governing skill owners, complete current required content or verified readable locations, and the authorized role and execution/reference-only mode. Fresh contexts must not infer paths, inherit an assumed working directory, or treat access as write permission. Applicable authoring standards must reach the worker before its decisions and edits, not only its reviewer.
