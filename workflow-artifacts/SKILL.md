---
name: workflow-artifacts
description: Shared reference for this suite's private issue workspace, local Git exclusion, review and repair records, source identities, recovery, and delivery summaries. Load when another workflow or reviewer needs these rules, including after installation or resumption. This is a reference to consult, not a separate workflow to execute.
---

# Workflow Artifacts

Read [WORKFLOW-ARTIFACTS.md](WORKFLOW-ARTIFACTS.md) before producing, coordinating, or reviewing this suite's artifacts. Apply the same rules to authors and reviewers. Loading this skill supplies the standard; it does not itself create a workspace, edit Git exclusion, write logs, run implementation, dispatch reviewers, or approve anything. Those actions belong to the authorized consuming stage and role. Read-only reviewers remain read-only.

## Loading skills and their resources

Install this whole directory as the model-loadable skill `workflow-artifacts`; no file outside this directory is required for this reference. Keep the companion standard with this entry. Install each consuming skill and its declared skill dependencies as complete units, using the harness's supported installation mechanism. Do not assume a single-skill installer automatically installs dependencies or that different skills share a filesystem parent.

To obtain another skill's resources, call the Skill tool with its registered name. If the harness exposes a different named skill-loading/resource mechanism instead of a Skill tool, use that mechanism; for example, omp exposes `skill://<name>` and `skill://<name>/<resource>`. Use the actual registered skill location returned by the harness, not a guessed configuration path, a sibling-directory traversal, or a path into the source checkout. A bare slash-name mention is not a completed load.

Resolve every companion-document link relative to its owning installed skill/document, never relative to the product working directory or the consuming skill. Load another skill in **reference-only mode** when only its standard or reviewer contract is needed: read the requested resources without starting that skill's execution steps or approval workflow. Loading a dependency is not user authorization to run another stage.

If a caller/reviewer already supplies the complete current required standard, or a verified readable resource location with its owning skill identity, use it without recursively reloading the same skill. Do not substitute a summary or remembered version for missing required content. Missing, ambiguous, or inaccessible registered dependencies block the affected work; report the exact name/resource and needed installation/access. Do not silently fetch, install, fall back to another skill of similar name, or assume an absolute source path on the author's machine.

## Keep installation and project roots separate

The **skill root** locates installed instructions and companion resources. Treat these as read-only while executing a product workflow; an installation can be global, copied, symlinked, read-only, or stored in a plugin cache.

The **project root** is the target repository identified from the user's work and actual checkout. Resolve `.scratch/<work-slug>/`, Git exclusion, product code, commands, and project-document links against that repository, not the skill installation. Loading global skills must not change the product working directory. Inspect both identities when resuming; do not initialize a work directory under a global skill installation merely because instructions were loaded there.

Before dispatching a worker/reviewer, provide the target repository/checkout, work identity, governing skill names, and complete required content or verified resolved resource locations. State reference-only versus executable use and the authorized role. A fresh context must not reconstruct paths from the source repository layout or inherit an assumed current directory. Resource resolution does not grant write permission or relax existing review/approval gates.
