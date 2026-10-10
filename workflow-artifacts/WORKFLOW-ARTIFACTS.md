# Private Workflow Artifacts

Read this complete standard before starting/resuming any author, controller, implementer, or reviewer role. It owns storage, records, source identity, and transition integrity; stage standards own content quality and stage gates. Load it through the named `workflow-artifacts` skill under [SKILL.md](SKILL.md)'s resource rules. Missing access blocks affected work; neither memory nor another layout substitutes for it.

## Repository-local private workspace

Use `<repository-root>/.scratch/<work-slug>/` for one work identity across stages and sessions: a bounded standalone requirement/change, or an overall effort with scoped children under the heavyweight layout below. Inspect supplied paths and existing work before choosing a slug; state the path. Ask only when genuinely distinct efforts remain ambiguous. A new session does not create a new work identity.

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

### Heavyweight work: one effort, scoped models, one ticket set

For a Wayfinder-led effort, extend the same excluded work root; standalone lightweight work keeps the flat layout above:

```text
.scratch/<effort>/
├── issue.md
├── issue.log.md
├── wayfinder.md
├── requirements.md
├── architecture.md
├── requirements/
│   └── 01-<requirement>/
│       ├── issue.md
│       ├── issue.log.md
│       ├── requirements.md
│       └── technical.md
├── issues/
│   ├── 01-<ticket>.md
│   └── 01-<ticket>.log.md
└── delivery.md
```

The root entry is the sole whole-effort index and later implementation controller entry. It identifies the authorized scope, child entries, governing sources, applicable gates, dependencies, and next handoff. Child entries track scoped modeling/recovery and link their parent; they do not own separate ticket sets or implementation controllers. A requirement is a modeling boundary, not a code module or implementation ticket. Ticket scope follows complete, meaningful changes, including necessary atomic changes across children.

Document authority is explicit:

- `wayfinder.md`: coarse requirement decomposition, its rationale, tentative dependencies/topology, and unresolved exploration. Approval permits scoped clarification, not architecture or implementation. As formal models settle an estimate, replace it with a precise reference; the map is not a competing specification.
- Root `requirements.md`: shared domain meanings, cross-child rules and business flows, and exact child references. It composes the requirement model, rather than concatenating children.
- `architecture.md`: approved overall technical topology, shared constraints/contracts, and cross-child collaboration/verification requirements, authored through `clarify-architecture`.
- Child `requirements.md` and `technical.md`: complete scoped models under the existing respective standards. Cite applicable parent definitions, with one owner per decision; references must supply the actual required content, not conceal gaps.

Root `issue.log.md` holds root-model/package, ticket-set, and whole-implementation records; each child log holds its model-stage records. Actual implementation/repair records stay with root tickets. One controller owns shared root writes; a delegated model author writes only its assigned child artifacts and returns parent updates. All models remain clean and all records obey the shared lifecycle below. Create `change.md` only when needed at its governing work scope; later separately authorized changes keep their own work identity and reference affected original authorities.

Every dispatch/resume identifies the checkout, effort root, assigned entry/output paths, parent references, authorized stage/scope, and record writer. Child work must reuse that assignment, not derive another top-level slug. Read relevant current parent sections and essential dependencies without importing the entire effort history. Hierarchy never grants permission to write another owner's files or to publish private artifacts.

### Hierarchical source packages and handoffs

The root entry identifies each package's exact scope, source paths/sections and verifiable revisions, applicable review/approval records, and unresolved/excluded scope. This is index data, not another manifest file or a copy of source definitions. Store revision bindings in the entry/approval records; model links identify owning paths/sections rather than embedding mutually recursive digests. Child entries cite the relevant package and its sources. Apply the shared non-normative metadata convention to navigation/status-only updates; changed package membership, scope, or governing obligations are substantive changes, not exempt index edits.

For the authorized scope, the route is `wayfinder` → `clarify-requirements` (shared and child models) → `clarify-architecture` → `clarify-technical-design` (children) → `split-tickets` → `implement`/`implement-unit`. Modeling and ticket planning use their authoring standards, independent review and explicit applicable human approval. Implementation retains its unit-review and whole-scope acceptance gates, with no delegated-unit human gate. Loading or approving a stage does not execute the next one.

Shared and child requirements may be clarified iteratively against confirmed constraints and explicit hypotheses; do not create a parent/child approval deadlock. Before formal architecture, review/approve the current requirements package including cross-child consistency. Before child technical design, applicable requirements and overall architecture must pass their gates. Before ticketing, the package also needs the complete approved child technical designs and resolved shared realizations required by its scope. Local Passes alone do not establish package consistency. The requirements and ticket-set reviews assess their respective composition; do not add a duplicate generic package-review stage.

These gates apply to explicitly authorized scope and its real dependencies, not every future idea. Unresolved detail outside that scope may remain in the map; a needed prerequisite cannot be relabeled as future work to pass a gate. Detailed production design belongs in the applicable technical models before ticketing, not in Wayfinder and not in implementation. A valid scoped change package remains an alternative basis without fabricated historical approvals.

Conflicts return to the decision's owner: shared business rules to requirements, global technical guarantees to architecture, local realization to its technical model. A child cannot override a parent by exception notes. For approved-model changes use applicable change governance, synchronize current authorities and affected index links, and reassess affected descendants, tickets, and evidence before resuming. Preserve unrelated valid approvals with an explicit impact basis. Ordinary code nonconformance stays with the original implementation/review pair. Final combined verification, overall independent review and human acceptance belong to the root authorized delivery scope, not the sum of child statuses.

## Clean authority and current state

Models/tickets express the complete current intended result. Integrate revisions into owning sections, with necessary background and actual deciding rationale; remove superseded statements and synchronize diagrams/references. No interview chronology, normative patch files, changelogs, override appendices, review reports, or execution diaries belong in canonical artifacts. Process logs are not normative patches.

Curate current entry/status fields and link governing records instead of duplicating conclusions. A log cannot change requirements, interfaces, topology, file responsibilities, approvals, or dependencies. Design changes return to the owning modeling gate and regain applicable review/approval before execution. Historical decisions are not competing current specifications.

Keep known material pending decisions in `issue.md`, with their affected scope/model reference, missing human input or prerequisite, and next action or owning later stage. Reconcile this current list after each answer and before a pause/handoff; remove resolved or superseded entries while integrating conclusions into their owning models. Preserve unresolved parts of partial answers. This is recovery state, not an exhaustive questionnaire, a second specification, or a substitute for review findings. Apply `ask-with-context`'s continuation rules within the authorized stage.

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
