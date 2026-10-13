---
name: artifact-layout
description: Use when establishing or checking Clarity artifact directories, filenames, ownership and local Git exclusion. Reference only; does not start a workflow.
---

# Artifact Layout

Directory structure, naming, file responsibilities and local exclusion for Clarity work. This reference skill does not start a stage, create files on loading or grant write permission. Stage skills own execution and approval; the separately registered `review-records` skill owns record contents and is needed only for record work.

## Private workspace

Use `<repository-root>/.scratch/<work-slug>/` for one authorized effort. Reuse its established identity; existing canonical project documents may stay in place with precise references. Installed skills are instructions, not output locations.

Establish exclusion before creating artifacts:

1. Resolve the repository root with `git rev-parse --show-toplevel` and local exclusion file with `git rev-parse --git-path info/exclude`. Resolve relative output from the command's cwd; `.git` may be a worktree file.
2. Preserve existing content and newline boundaries; append `/.scratch/` if absent. Create a legitimately missing local exclusion file, not a repository or global ignore setting.
3. From the resolved repository root, run `git ls-files -- .scratch`. Tracked artifact paths block affected writes; report them rather than automatically untracking files.
4. From that root, run `git check-ignore -v --no-index -- <planned-path>` and verify effective exclusion, not a matching negation. Recheck where nested rules could change the result.

A failed exclusion check is not permission to use public storage. These artifacts are not automatically staged, committed, published or deleted. Inspect packaging/upload inputs when publication is separately authorized: Git exclusion is not an upload policy, and cloud agents may transmit read content to providers.

## Directory structure

Create only the files required by the authorized route; this tree is a location map, not a checklist of required deliverables.

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

Standalone requirements/design use root models. Heavyweight child modeling uses the assigned `requirements/<NN>-<requirement>/` folder, whose entry links its parent; the root owns the effort index, ticket set and final delivery. A later separately authorized change has its own work folder and links affected authorities. These locations do not prescribe stage prerequisites.

## File responsibilities

| File | Responsibility |
| --- | --- |
| `issue.md` | Work definition and navigation: objective, exclusions, checkout, route and authoritative sources. A root ticket-set entry also owns planned coverage/dependencies and integration/verification ownership. Not an approval index or progress diary. |
| `wayfinder.md`, `requirements.md`, `architecture.md`, `technical.md`, `change.md` | Current specifications at their respective resolutions; not transcripts, changelogs or normative patch appendices. |
| `issues/<NN>-<ticket>.md` | Ticket specification and its compact in-place execution block; not chronological work history. |
| `<object>.review-fix-decisions.log.md` | The reviewed object's review, repair and approval evidence, in the separate record format. Not a general investigation or implementation log. |
| `delivery.md` | Final implementation summary at the authorized scope, not a planning document. |

Log stems are `wayfinder`, `requirements`, `architecture`, `technical`, `change`, `tickets` for the ticket plan, and `implementation` for the whole-set or direct code result. Ticket code-review logs sit beside their tickets. External canonical specifications keep review records in the assigned private workspace.

Each file has one assigned writer; other roles return proposed changes or reports to that writer. Use relative artifact links and checkout-relative code paths, identifying other checkouts explicitly. Root and child files retain their respective owners.

There are no separate state files, candidate sidecars, question diaries, per-round files or duplicate approval registries. Preserve existing private history during an authorized reorganization instead of copying mixed diaries into current specifications or keeping competing active locations; evidence must not disappear as a side effect of renaming files.
