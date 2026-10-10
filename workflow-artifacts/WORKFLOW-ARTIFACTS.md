# Private Workflow Artifacts

Read this complete standard before starting/resuming any author, controller, implementer, or reviewer role. It owns storage, records, source identity, and transition integrity; stage standards own content quality and stage gates. Load it through the named `workflow-artifacts` skill under [SKILL.md](SKILL.md)'s resource rules. Missing access blocks affected work; neither memory nor another layout substitutes for it.

## Repository-local private workspace

Use `<repository-root>/.scratch/<work-slug>/` for one bounded requirement/change across stages and sessions. Inspect supplied paths and existing work before choosing a slug; state the path. Ask only when genuinely distinct efforts remain ambiguous. A new session does not create a new work identity.

New workflow artifacts belong here, not in `docs/`, personal folders, or remote trackers. Changing this policy requires explicit user direction, not an inherited example. Existing authoritative project documents may stay in their owning locations: reference and synchronize approved sections rather than duplicate, relocate, or untrack them. Approved product-documentation changes are distinct from private records.

### Establish exclusion before writing

The author/controller sets up exclusion; delegated workers use its verified workspace and report problems. Reviewers inspect evidence read-only.

1. Resolve the repository with `git rev-parse --show-toplevel` and exclusion file with `git rev-parse --git-path info/exclude`; resolve returned relative paths from the command's working directory. Do not assume `.git` is a directory. Worktrees can share exclusion files.
2. Preserve existing content, comments, and newline boundaries. Append root-anchored `/.scratch/` only if absent; create the local exclusion file if legitimately missing. Do not edit `.gitignore`, global Git settings, or initialize another repository.
3. From the repository root, run `git ls-files -- .scratch`. Tracked workflow material blocks affected writes: report exact paths. Exclusion does not untrack files; do not untrack or rewrite history without authorization.
4. Verify planned paths with `git check-ignore -v --no-index -- <planned-path>`. Check the effective pattern: a matching negation is not successful exclusion. Recheck when nested rules can affect a new path. Resolve setup failure or report it; do not write workflow content first or fall back to public storage.

Never force-add, stage, commit, push, publish, upload, or automatically copy these artifacts into tracked documentation. Git exclusion is not protection from packaging, backups, synchronization, or uploads; inspect publication inputs if release is separately requested. Cloud agents may transmit read content to providers: this is not offline secrecy.

## Layout and ownership

Create only files needed by the route and current stage:

```text
.scratch/<work-slug>/
├── issue.md
├── requirements.md
├── technical.md
├── change.md
├── issue.log.md
├── issues/
│   ├── 01-<slug>.md
│   └── 01-<slug>.log.md
└── delivery.md
```

- `issue.md`: current objective/exclusions, checkout, route, models and applicable approvals, stage, blockers, next action, original role handles/recovery. On the ticket route, also the TICKETS.md set index: stable ticket links, coverage, dependencies, integration/verification ownership, and set approval. Keep planning approval, code conformance, and human acceptance distinct; no separate `STATE.md` or `INDEX.md`.
- `requirements.md`, `technical.md`, `change.md`: clean stage models. Create only applicable models; precisely referenced existing authorities need no copy, and missing history needs no placeholders.
- `issues/<NN>-<slug>.md`: clean ticket specification/current status. IDs are stable; numbering is not dependency order. Its same-stem `.log.md` holds unit results, reviews, repairs, evidence, and handoffs—not separate files per round/finding/agent/session.
- `issue.log.md`: document-stage reviews/repairs/approvals and overall implementation review/acceptance. Direct changes also keep implementation and full-change review here; their identity is the approved change model path/revision, with no artificial ticket or `issues/` directory.
- `delivery.md`: implementation summary after required verification and independent Pass, before final human acceptance. Delegated units return to their controller without whole-work summaries. Standalone tickets summarize only their reviewed scope and preserve any broader summary. Planning produces no delivery summary.

Use relative artifact links and stable heading/finding anchors. Code paths are checkout-relative; identify different checkouts explicitly. Temporary tool output/agent handles cannot replace durable essential content. Exclude secrets, credentials, private reasoning traces, and raw conversation dumps.

## Clean authority and current state

Models/tickets express the complete current intended result. Integrate revisions into owning sections, with necessary background and actual deciding rationale; remove superseded statements and synchronize diagrams/references. No interview chronology, normative patch files, changelogs, override appendices, review reports, or execution diaries belong in canonical artifacts. Process logs are not normative patches.

Curate current entry/status fields and link governing records instead of duplicating conclusions. A log cannot change requirements, interfaces, topology, file responsibilities, approvals, or dependencies. Design changes return to the owning modeling gate and regain applicable review/approval before execution. Historical decisions are not competing current specifications.

On resumption, read `issue.md`, relevant current models/tickets, open findings, and latest applicable decisions/evidence; consult older history only as needed. Reconcile actual checkout/code, approvals, prerequisites, and role availability. Stored status or retained context is not proof. Restore implementation roles under IMPLEMENTATION.md; model reviewers remain fresh per round.

## Review records and finding lifecycle

The reviewer returns the core fields below plus the stage reviewer contract's coverage and verdict requirements. The controller preserves each actual report in the owning log; standalone authors perform this duty. Shared work-level records have one controller writer. Delegated implementers supply entries or write only an explicitly assigned exclusive unit log.

Every report/record identifies:

- Stage/unit, round, date, reviewer, and exact reviewed artifact/code basis.
- Governing standards and applicable approved sources.
- `Pass`, `Changes required`, or `Blocked`; required category coverage, actual evidence/limits, and every finding/blocker.
- Prior finding dispositions: resolved, unresolved, withdrawn with reason, or unverified, with applicability of previous Pass/evidence. New sessions or numbering must not hide regressions.

Each finding has a stable stage/unit ID (for example `technical-F01`), the violated obligation, actual location/behavior and supporting evidence, significance with necessary background, and an observable closure condition—not an unauthorized design prescription. Repairs and subsequent disposition cite the same ID.

For every blocker, identify the affected checks and the evidence, access, or decision needed to unblock them. Explicitly report `None` when findings or blockers are absent; omission is not a clean result.

Authors mark repairs `addressed, awaiting review`, never self-close findings. Disputes stay open with counter-evidence until independent correction/withdrawal; genuine upstream design disputes return to modeling. Only an applicable independent assessment establishes closure. Preserve historical outcomes and update applicability; new evidence may reopen findings. Pass requires no unresolved findings/blockers and is not human approval/acceptance. Obtain correction of incomplete, stale, or inconsistent reports rather than rewriting them into Pass.

## Implementation and repair records

In the existing unit log, or root log for direct work, record meaningful implementation results and repair batches with:

- Objective/acceptance obligations or finding IDs.
- Resulting behavior/structure and changed owners, not tool-call inventories.
- Handling decision, necessary background, and key rationale. Trivial conformance repairs need only a concise explanation; non-obvious ones need enough context for an unfamiliar reviewer, not private reasoning.
- Whether the work stays within approved design; otherwise the blocker and subsequent approved upstream decision. A repair record grants no authority.
- Exact checks/scenarios, actual outcomes, environment/participants/substitutions, and applicable code basis. Distinguish planned, executed, failed, and passed. Preserve important output/assertions and limits locally; retain large raw artifacts only when necessary, referenced and redacted in the work directory.
- Remaining issues, pending review, and next action/handoff.

Link findings, handling, evidence, and disposition. Do not duplicate definitions, invent evidence, transcribe every tool call, or defer records until delivery. Clean implementation still records its result and verification even without findings.

## Revision, approval, and transition integrity

Identify private artifacts by path plus content digest or another verifiable local revision—not repository HEAD. Identify every relevant source in a multi-document package. Consistently exclude non-normative approval/status metadata from revision calculation, or retain the reviewed digest with an explicit metadata-only explanation. Identify the checkout and relevant dirty/untracked content as well as commits for code. Preserve evidence needed to compare current content; hashes cannot recreate missing bodies.

Dispatch packages need not be copied wholesale, but essential source identities, findings, decisions, and verification must survive in private records. Logs are neither Git history nor full snapshots. Disclose unrecoverable old content; do not fabricate it or reuse unverifiable approval.

Persist before advancing:

1. Save every returned review, including failed/blocked outcomes, before repair or gate advancement.
2. Save implementation/repair decisions and fresh evidence before requesting review.
3. Save reviewer disposition and update state before scheduling dependents or handing off.
4. Before blockers, role replacement, or session/stage handoff, update recovery basis, open issues, evidence, roles, and next action.
5. Save explicit human approval/acceptance with exact scope/basis and a faithful quotation or durable decision reference. Never invent consent or treat approval of an idea, proposed fix, or upstream model as approval of an unreviewed downstream result.

Source/code changes invalidate affected evidence, review, and acceptance under the stage standard; retain history and update applicability. Ticket Passes do not constitute an independent overall verdict. A direct full-change Pass is already its final independent review: recording introduces neither duplicate review nor per-ticket human approval.

## Final delivery summary and retention

After implementation verification and applicable independent Pass, write a clean `delivery.md` containing:

- **Delivered scope:** observable outcomes, exclusions, and any standalone partial scope.
- **Final design landing:** actual owners/collaboration/contracts with authoritative model links, not duplicate definitions.
- **Consequential decisions:** maintenance-relevant background and actual key basis, not repair chronology.
- **Verification and review:** actual checks/results, code/source basis, applicable verdicts, participants/substitutions, and limits. Missing mandatory evidence blocks completion, not merely a footnote.
- **Use and maintenance:** applicable configuration, migration, operational, or maintenance instructions.
- **Acceptance:** `Awaiting acceptance` versus explicit acceptance of this result, linked to decision evidence; silence is not consent.

Before an ordinary conformance-repair handoff, renew affected evidence/review and integrate the summary. A later separately authorized change has its own work identity and summary; synchronized canonical models remain current authority, not old summaries.

Keep all artifacts local and excluded. Delivery does not authorize deleting records, moving them out, publishing, or committing them. A request for external documentation requires separately identified content and destination, not wholesale publication. Planning approval, Pass, or acceptance never implies version-control or release action.
