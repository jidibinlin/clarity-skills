---
name: artifact-layout
description: Reference for Clarity's private artifact directories, filenames, ownership and local Git exclusion.
---

# Artifact Layout

This reference defines storage, not workflow. Stages govern execution; `review-records` defines review and repair records.

## Private workspace

Use `<repository-root>/.scratch/<work-slug>/` for one effort. Reuse established workspaces and link existing canonical documents rather than copying them. Installed skill directories are not output locations.

Before creating artifacts, resolve the repository and local exclusion file with `git rev-parse --show-toplevel` and `git rev-parse --git-path info/exclude`. Add `/.scratch/` to that local exclusion while preserving existing entries. Verify planned paths with `git check-ignore -v --no-index` and check for tracked artifacts with `git ls-files -- .scratch`, from the repository root. Report tracked paths instead of automatically untracking them.

Keep these artifacts private: do not include them in commits, publication or cleanup without permission. Git exclusion does not protect against other upload or packaging tools.

## Directory structure

Create only what the chosen route needs.

```text
.scratch/<work-slug>/
├── issue.md
├── wayfinder.md
├── requirements.md
├── architecture.md
├── technical.md
├── change.md
├── <object>.review-fix-decisions.log.md
├── issues/
│   ├── <NN>-<ticket>.md
│   └── <NN>-<ticket>.review-fix-decisions.log.md
├── requirements/
│   └── <NN>-<requirement>/
│       ├── issue.md
│       ├── requirements.md
│       ├── technical.md
│       └── <object>.review-fix-decisions.log.md
└── delivery.md
```

Standalone modeling uses root models. Heavyweight children use assigned `requirements/<NN>-<requirement>/` folders linking their parent; the root owns the effort index, ticket set and final delivery. A later change uses its own work folder and links the affected specifications.

## File responsibilities

| File | Responsibility |
| --- | --- |
| `issue.md` | Work definition and navigation: objective, scope, checkout, route and source links. A root ticket-set entry also holds planned coverage, dependencies and integration ownership. |
| Model files | Current integrated specifications, with rationale beside the decisions it explains. |
| `issues/<NN>-<ticket>.md` | Ticket specification and a separate compact block of current execution facts. |
| `<object>.review-fix-decisions.log.md` | Review reports, finding-linked repair decisions and approval evidence, using `review-records`. |
| `delivery.md` | Final implementation summary for the authorized scope. |

Log stems are `wayfinder`, `requirements`, `architecture`, `technical`, `change`, `tickets` for the plan, and `implementation` for the overall code result. Ticket code-review logs sit beside their tickets. Records for external canonical specifications remain in the private workspace.

Assign one writer per file; other participants return proposals or reports to that writer. Use relative artifact links and repository-relative code paths, naming other checkouts explicitly.

Keep models clean and records object-specific. Do not add progress diaries to `issue.md`, separate state files, candidate drafts or duplicate approval registries. Preserve review history when reorganizing private artifacts.
