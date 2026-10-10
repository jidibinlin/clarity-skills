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

Separate definitions, ticket progress, and review evidence. Create only artifacts needed by the authorized route and current work; no empty stage files or per-session, per-agent, or per-review-round files.

- `issue.md` is the work definition and navigation entry: objective, exclusions, checkout, route, authoritative model/source-package references, and final delivery-summary navigation. For a ticket set it also owns stable ticket links, coverage, planned dependencies, and integration/verification responsibilities under TICKETS.md. Change it when this definition or navigation changes, not after execution steps. No approval-record index, active stage/step, pending interview questions, runtime blockers, role handles, progress, investigation notes, or repair history belongs here. Child entries have the same boundary and link their parent.
- Models and tickets contain the clean current specification. Unresolved modeling decisions remain explicit beside their affected rules; settled answers replace them in place. Tickets also carry a compact, non-normative execution status under **Progress and resumption** below. Keep document approval metadata distinct from execution status.
- There are no standalone state files or substitute progress/checklist artifacts. Models already express clarification progress; tickets already define implementation work.
- `<object>.review-fix-decisions.log.md` contains only that object's review submissions, actual review outcomes, finding-linked repair decisions/evidence, and corresponding human approvals or acceptance. Follow **Review records and finding lifecycle** and **Review submissions and fix decisions** below. It is not a general process log.
- `delivery.md` summarizes verified, independently reviewed implementation before final human acceptance. Planning creates none. Delegated units do not create whole-work summaries; standalone tickets summarize only their reviewed scope and preserve any broader summary.

Use these object stems within the assigned private work directory; append `.review-fix-decisions.log.md`, not the model’s `.md` extension:

| Object | Stem | Specification / review scope |
| --- | --- | --- |
| Coarse decomposition | `wayfinder` | `wayfinder.md` |
| Requirements | `requirements` | Assigned `requirements.md`, or the root's identified composite package |
| Overall architecture | `architecture` | `architecture.md` |
| Technical design | `technical` | Assigned `technical.md` |
| Scoped change | `change` | `change.md` and its identified synchronized sources |
| Ticket planning | `tickets` | Root `issue.md` set definition and `issues/<NN>-<slug>.md` specifications; no synthetic `tickets.md` |
| Whole/direct implementation | `implementation` | Whole ticket-set result, or the entire approved direct change |
| One implementation ticket | `issues/<NN>-<slug>` | That ticket's code result, not ticket-plan approval |

Thus requirements use `requirements.review-fix-decisions.log.md`; a ticket uses `issues/01-<slug>.review-fix-decisions.log.md`. A direct change has distinct change-model and implementation reviews, but no artificial ticket or state artifact. Its full-scope pair and controller share one assigned implementation review-record writer, not duplicate direct-unit records. A standalone ticket uses only its ticket and review log, not an artificial whole-set controller. Referenced canonical models may remain outside the private directory; their review records remain in the assigned private workspace.

The author/controller assigns one writer per ticket or review-record file. Delegated authors may write explicitly assigned exclusive object files or return updates to their writer; reviewers remain read-only and return reports. Each writer records its own facts; cross-object effects travel through explicit handoffs, not concurrent edits to a shared catch-all file.

Use relative artifact links and stable heading/finding anchors. Code paths are checkout-relative; identify different checkouts explicitly. Essential decisions and review evidence must be durable, not just temporary tool output/agent handles. Exclude secrets, credentials, private reasoning traces, and raw conversation dumps.

### Heavyweight work: one effort, scoped models, one ticket set

For a Wayfinder-led effort, extend the same excluded root. The tree below shows specification placement; each reviewed object uses its own review log from the stem table above, at the same assigned work scope. Do not create every possible review file in advance.

```text
.scratch/<effort>/
├── issue.md
├── wayfinder.md
├── requirements.md
├── architecture.md
├── requirements/
│   └── 01-<requirement>/
│       ├── issue.md
│       ├── requirements.md
│       └── technical.md
├── issues/
│   └── 01-<ticket>.md
└── delivery.md
```

The root entry is the sole whole-effort definition/index and implementation navigation entry. It identifies scope, child entries, governing sources and planned dependencies, not approval-record navigation, live scheduling or next actions. Child entries define scoped modeling and link their parent; their requirements and technical reviews have separate logs within that child directory. They own no separate ticket set, implementation controller, or delivery summary. A requirement is a modeling boundary, not a code module or implementation ticket. Ticket scope follows complete, meaningful changes, including necessary atomic changes across children.

Document authority is explicit:

- `wayfinder.md`: coarse requirement decomposition, its rationale, tentative dependencies/topology, and unresolved exploration. Approval permits scoped clarification, not architecture or implementation. As formal models settle an estimate, replace it with a precise reference; the map is not a competing specification.
- Root `requirements.md`: shared domain meanings, cross-child rules and business flows, and exact child references. It composes the requirement model, rather than concatenating children.
- `architecture.md`: approved overall technical topology, shared constraints/contracts, and cross-child collaboration/verification requirements, authored through `clarify-architecture`.
- Child `requirements.md` and `technical.md`: complete scoped models under the existing respective standards. Cite applicable parent definitions, with one owner per decision; references must supply the actual required content, not conceal gaps.

Root model/package reviews stay with their respective root object, child model reviews with that child's respective object, ticket-plan reviews with root `tickets.review-fix-decisions.log.md`, and whole implementation reviews with root `implementation.review-fix-decisions.log.md`. Actual single-ticket repairs stay with that root ticket's review log. One controller owns root definition writes; delegated model authors write only assigned child artifacts and return proposed parent changes. Create `change.md` only at its governing work scope; later separately authorized changes keep their own work identity and reference affected original authorities.

Every dispatch/resume identifies the checkout, effort root, assigned definition/model or ticket, review-record paths, parent references, authorized stage/scope, and each writer. Child work reuses that assignment, not another top-level slug. Read applicable parent sections and essential dependencies, not the whole effort history. Hierarchy grants neither another owner’s write permission nor publication permission.

### Hierarchical source packages and handoffs

The root entry identifies each package’s exact scope, source paths/sections and verifiable revisions, and unresolved/excluded scope. This is specification index data, not another manifest or an approval registry. Approval evidence belongs to the reviewed object’s log and, where applicable, model metadata; consumers resolve it through the object mapping above, not a second entry-file index. Store source revision bindings in the entry and the applicable review records; model links identify owning paths/sections rather than embedding mutually recursive digests. Child entries cite the relevant package and its sources. Apply the shared non-normative metadata convention to navigation/status-only updates; changed package membership, scope, or governing obligations are substantive changes, not exempt index edits.

For the authorized scope, the route is `wayfinder` → `clarify-requirements` (shared and child models) → `clarify-architecture` → `clarify-technical-design` (children) → `split-tickets` → `implement`/`implement-unit`. Modeling and ticket planning use their authoring standards, independent review and explicit applicable human approval. Implementation retains its unit-review and whole-scope acceptance gates, with no delegated-unit human gate. Loading or approving a stage does not execute the next one.

Shared and child requirements may be clarified iteratively against confirmed constraints and explicit hypotheses; do not create a parent/child approval deadlock. Before formal architecture, review/approve the current requirements package including cross-child consistency. Before child technical design, applicable requirements and overall architecture must pass their gates. Before ticketing, the package also needs the complete approved child technical designs and resolved shared realizations required by its scope. Local Passes alone do not establish package consistency. The requirements and ticket-set reviews assess their respective composition; do not add a duplicate generic package-review stage.

These gates apply to explicitly authorized scope and its real dependencies, not every future idea. Unresolved detail outside that scope may remain in the map; a needed prerequisite cannot be relabeled as future work to pass a gate. Detailed production design belongs in the applicable technical models before ticketing, not in Wayfinder and not in implementation. A valid scoped change package remains an alternative basis without fabricated historical approvals.

Conflicts return to the decision's owner: shared business rules to requirements, global technical guarantees to architecture, local realization to its technical model. A child cannot override a parent by exception notes. For approved-model changes use applicable change governance, synchronize current authorities and affected index links, and reassess affected descendants, tickets, and evidence before resuming. Preserve unrelated valid approvals with an explicit impact basis. Ordinary code nonconformance stays with the original implementation/review pair. Final combined verification, overall independent review and human acceptance belong to the root authorized delivery scope, not the sum of child statuses.

## Clean authority and progress

Models/tickets express the complete current intended result. Integrate conclusions, necessary background, original requirement evidence and actual rationale into owning sections; synchronize diagrams/references and remove superseded rules. Ordinary clarification answers belong here, not as interview entries in a review log. Preserve necessary attributed human quotations or other retrievable original evidence alongside the relevant rule without dumping the conversation. No normative patches, changelogs, override appendices, review reports, or execution diaries belong in canonical artifacts.

Definition entries link authoritative specifications, not approval records or copies of model conclusions. Neither ticket execution metadata nor review records may change requirements, interfaces, topology, file responsibilities, or planned dependencies. Return design changes to their owning modeling gate and regain applicable review/approval before execution. Historical decisions are not competing specifications.

### Progress and resumption

Modeling and ticket planning create no state file. Keep material unresolved decisions beside their affected model rules or ticket-definition sections; integrate each settled answer and its necessary rationale/evidence there. Reconcile remaining decisions after every answer and before handoff under `ask-with-context`, without an exhaustive questionnaire, interview diary, or duplicate decision queue. A deferred decision identifies its owner and where it blocks the current scope.

Implementation progress belongs to the existing ticket, in one compact non-normative execution block: current status, current blocker if any, bound implementation/reviewer handles, and applicable review/evidence references. Use the project’s status vocabulary or distinguish pending, implementing, in review, passed, and blocked. Update these fields in place; keep completed tickets, not a second step checklist or chronological history. Passed means current independent conformance, not source approval, whole-result acceptance, or a replacement for actual verification.

The controller reads ticket status, planned dependencies, actual incorporated code, and applicable verification/review evidence to determine readiness. It maintains no duplicate global status ledger. Direct implementation has no synthetic ticket or state record: use the approved change package, actual code, and its implementation review evidence. Session-local todos may guide execution, but do not become another durable artifact or completion authority.

Bind original implementation/reviewer roles using ticket execution metadata and the harness’s resumable context. When no ticket exists, the existing implementation review log may carry a compact identity header for its work scope and bound roles; this is review ownership metadata, not a fifth log event or a place for progress, next actions, or blockers. Record later authorized role replacement with the affected review submission and basis. No new role registry is needed.

On resumption, use `issue.md` for specification navigation, then the governing models/tickets and applicable review records. Reconcile unresolved decisions, actual checkout/code, approvals, prerequisites, evidence and role availability; stored status is not proof. Restore implementation roles under IMPLEMENTATION.md; model reviewers remain fresh per round. Reconstruct only from available evidence, report what is missing, and never infer completion from lost context. A blocker is made explicit in its owning model, ticket or actual review report as applicable; report other execution blockers in the handoff without inventing a persistence file.

## Review records and finding lifecycle

The reviewer returns the core fields below plus its stage contract's coverage/verdict requirements. The assigned writer preserves every actual report in the reviewed object's `.review-fix-decisions.log.md` before repair or advancement. A log accepts only four event types: review submission with its basis/evidence, reviewer outcome, finding-linked repair decision/evidence, and corresponding explicit human approval/acceptance. No routine investigation, interview, implementation progress, or miscellaneous decision entries. Follow the object mapping and single-writer rule above.

Every reviewer report identifies:

- Stage/unit, round, date, reviewer, and exact reviewed artifact/code basis.
- Governing standards and applicable approved sources.
- `Pass`, `Changes required`, or `Blocked`; required category coverage, actual evidence/limits, and every finding/blocker.
- Prior finding dispositions: resolved, unresolved, withdrawn with reason, or unverified, with applicability of previous Pass/evidence. New sessions or numbering must not hide regressions.

Each finding has a stable stage/unit ID (for example `technical-F01`), the violated obligation, actual location/behavior and supporting evidence, significance with necessary background, and an observable closure condition—not an unauthorized design prescription. Repairs and subsequent disposition cite the same ID.

For every blocker, identify the affected checks and the evidence, access, or decision needed to unblock them. Explicitly report `None` when findings or blockers are absent; omission is not a clean result.

Authors mark repairs `addressed, awaiting review`, never self-close findings. Disputes stay open with counter-evidence until independent correction/withdrawal; genuine upstream design disputes return to modeling. Only an applicable independent assessment establishes closure. Preserve historical outcomes and update applicability; new evidence may reopen findings. Pass requires no unresolved findings/blockers and is not human approval/acceptance. Obtain correction of incomplete, stale, or inconsistent reports rather than rewriting them into Pass.

## Review submissions and fix decisions

Before review, preserve the identified submitted result, governing sources and applicable approved basis, original requirement evidence, and actual verification/evidence limits in the object's review log. An initial clean implementation still has a review submission and outcome; it does not need invented findings or a development diary. Later repair submissions cite the affected finding IDs and fresh evidence. Reuse durable evidence by exact reference rather than copying it across objects.

Every repair decision records:

- The existing finding ID(s), violated obligation, and affected scope.
- The author's chosen correction, necessary background, decisive rationale, and material consequences/tradeoffs. Explain meaningful autonomous decisions so the human can assess them; trivial conformance corrections need only a concise explanation.
- Whether the correction conforms to the approved design. If not, record the conflict and owning upstream referral, then await the applicable approved resolution; do not authorize redesign in the log.
- The resulting change and exact checks/scenarios, actual outcomes, environment/participants/substitutions, and code/source basis. Distinguish planned, executed, failed and passed; preserve important evidence locally and link large necessary redacted artifacts.
- The subsequent reviewer disposition, tied to the same finding and reviewed basis. Until that exists the correction remains `addressed, awaiting review`.

No repair entry without an existing review finding: ordinary implementation progress belongs nowhere in this log. Ticket progress stays in the ticket; unresolved modeling decisions, settled design and rationale stay in their owning canonical sections. If a finding requires an upstream change, keep its originating conflict/referral here and the actual design revision/review in the upstream object’s records; link the approved resolution back rather than copying the discussion. A human-requested model change with no existing review finding follows modeling and a new review submission, not an invented repair finding.

When presenting a reviewed result, explicitly surface consequential autonomous repair decisions and link their records; merely saying `Pass` or burying decisions in a long file does not make them visible to the human. Do not introduce per-ticket human gates into delegated implementation.

## Revision, approval, and transition integrity

Identify private artifacts by path plus content digest or another verifiable local revision—not repository HEAD. Identify every relevant source in a multi-document package. Consistently exclude non-normative approval/status metadata from revision calculation, or retain the reviewed digest with an explicit metadata-only explanation. Identify the checkout and relevant dirty/untracked content as well as commits for code. Preserve evidence needed to compare current content; hashes cannot recreate missing bodies.

Dispatch packages need not be copied wholesale, but essential source identities, findings, decisions, and verification must survive in private records. Logs are neither Git history nor full snapshots. Disclose unrecoverable old content; do not fabricate it or reuse unverifiable approval.

Persist before advancing:

1. Save every returned review, including failed/blocked outcomes, before repair or gate advancement.
2. Save the review submission's result and evidence, or finding-linked repair decisions and fresh evidence, before requesting review.
3. Save reviewer disposition and update the ticket’s execution status, when a ticket exists, before scheduling dependents or handing off.
4. Before a blocker or session/stage handoff, ensure the owning model’s unresolved decisions, ticket status, and actual review findings are current where applicable. Carry the relevant basis, blocker and bound-role references in the handoff; create no recovery snapshot or work diary.
5. Save explicit human approval/acceptance in the corresponding object’s review log, with exact scope/basis and a faithful quotation or durable decision reference. Link it from model metadata or the delivery summary where applicable, not from `issue.md`. Never invent consent or treat approval of an idea, proposed fix, or upstream model as approval of an unreviewed downstream result.

Source/code changes invalidate affected evidence, review, and acceptance under the stage standard; retain history and update applicability. Ticket Passes do not constitute an independent overall verdict. A direct full-change Pass is already its final independent review: recording introduces neither duplicate review nor per-ticket human approval.

## Existing workspace cutover

When resuming a workspace with mixed `issue.md`, `issue.log.md`, generic unit `.log.md`, or legacy global/object state files, inspect before writing. Classify existing content by owner: specification navigation stays in the entry; current ticket execution facts move into the ticket’s metadata; unresolved modeling decisions and applicable normative answers integrate into their owning sections under existing approval rules; original review reports, finding-linked repair decisions, verification submissions and approvals move to the respective review logs. Recover no-ticket role bindings in the existing implementation review identity header. Other obsolete progress stays read-only legacy material, not a new active file. Remove approval navigation from the entry only after its evidence remains accessible through the owning model metadata or object review log. Do not rename a mixed log or state file wholesale, or turn its investigation/interview diary into new log entries.

Preserve original finding IDs, rounds, actual verdicts, reviewed identities, approval scope and necessary evidence/provenance; map old references to the new owned records and verify links before switching active readers/writers. Unknown ownership, missing evidence or conflicting authority blocks only the affected migration/approval, never justifies fabricated closure. Do not assume a substantive model/index rewrite is metadata-only or retain an approval for a changed basis without assessment.

Stop writing legacy catch-all files after cutover; retain no compatibility aliases or dual-write paths. Before rewriting a mixed entry, preserve its original bytes in the excluded workspace at `legacy/<source-digest>/<original-relative-path>` when otherwise-unmigrated history or approval evidence would be lost; never overwrite a different original snapshot. These are read-only migration sources, not active records or competing authority. Keep unmigrated historical material read-only until necessary evidence is preserved and deletion is authorized. Migration does not authorize deleting private history, silently rewriting old reports, or changing unrelated workspaces. No new migration diary is required.

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
