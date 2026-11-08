---
name: artifact-layout
description: Reference for Clarity's private artifact directories, filenames, ownership and local Git exclusion.
---

# Artifact Layout

This reference defines storage, not workflow. Stages govern execution.

## Private workspace

Use `<repository-root>/.scratch/<work-slug>/` for one effort. Reuse established workspaces and link existing canonical documents rather than copying them. Installed skill directories are not output locations.

Before creating artifacts, resolve the repository and local exclusion file with `git rev-parse --show-toplevel` and `git rev-parse --git-path info/exclude`. Add `/.scratch/` to that local exclusion while preserving existing entries. Verify planned paths with `git check-ignore -v --no-index` and check for tracked artifacts with `git ls-files -- .scratch`, from the repository root. Report tracked paths instead of automatically untracking them.

Keep these artifacts private: do not include them in commits, publication or cleanup without permission. Git exclusion does not protect against other upload or packaging tools.

## Directory structure

Create only what the chosen route needs.

```text
.scratch/<work-slug>/
├── issue.md
├── requirements.md
├── architecture.md
├── technical.md
└── technical/
    └── <group>.md
```

A later change uses its own work folder and links the affected specifications.

A technical scope may use linked `technical/<group>.md` parts when groups need separate writing responsibility. These and the coordinating `technical.md` form one canonical model; parts are named by design scope, not agent identity.

## File responsibilities

| File | Responsibility |
| --- | --- |
| `issue.md` | Work definition and navigation: objective, scope, checkout, route and source links. Holds the Design Alignment Roadmap when present. |
| Model files | Current integrated specifications, with rationale beside the decisions it explains. |

Assign one writer per file at a time; other participants return proposals or reports to that writer. Use relative artifact links and repository-relative code paths, naming other checkouts explicitly.

Keep models clean. Do not add progress diaries to `issue.md`, separate state files, candidate drafts or duplicate approval registries. Preserve existing historical artifacts when reorganizing private workspaces.
