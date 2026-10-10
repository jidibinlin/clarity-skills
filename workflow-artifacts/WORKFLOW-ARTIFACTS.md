# Private Workflow Artifacts

Mandatory for every author, controller, implementer, and independent reviewer in this suite. Read before starting or resuming work and before creating artifacts. This is the shared authoring, recording, handoff, and review standard for storage and record integrity; each stage's existing content and approval standard still applies. It belongs to the `workflow-artifacts` skill: load that skill by name and read this companion from its actual installed location under the resource-resolution rules in [SKILL.md](SKILL.md). Install the complete skill directory, not a standalone file in a common parent. Loading this reference does not execute a product workflow or change the target working directory. Missing access blocks artifact-producing work; do not substitute another layout from memory.

## Repository-local private workspace

Use `<repository-root>/.scratch/<work-slug>/` for one bounded requirement or change. Reuse its stable identity across stages and sessions. Inspect supplied paths and existing work first; do not create another directory for the same work merely because a session or agent changed. Name a new slug from the work and state the chosen path. Ask only when genuinely distinct existing efforts cannot be disambiguated from available evidence.

New workflow artifacts belong here, not under `docs/`, `docs/records/`, a separate personal directory, or a remote issue tracker. Explicit user changes to this policy require clarification; an inherited convention or an old example is not authorization to change it. Existing authoritative project documents may remain at their established locations: cite and, within approved scope, synchronize their owning sections rather than copy competing definitions. Do not relocate or untrack existing user files automatically. Approved product-documentation edits are distinct from these private workflow records.

### Establish exclusion before writing

The author/controller owns setup; delegated workers use its verified workspace and report problems rather than concurrently editing exclusion rules. Reviewers inspect evidence read-only.

1. Locate the actual repository root using `git rev-parse --show-toplevel` and locate the local exclusion file using `git rev-parse --git-path info/exclude`, resolving returned paths relative to the command's working directory. `.git` can be a file in a worktree; never assume `.git/info/exclude` is the physical path. In a worktree this exclusion file can be shared with other worktrees: preserve all existing content.
2. Inspect the exclusion file and append the root-anchored rule `/.scratch/` only if absent. Preserve existing rules, comments, and newline boundaries. Create the local file if legitimately absent; do not edit `.gitignore`, global Git configuration, or initialize another Git repository. Do not create workflow content before setup succeeds.
3. Check `git ls-files -- .scratch` from the repository root. Existing tracked workflow material cannot be made private by exclusion. Stop the affected write and report the concrete paths; do not run `git rm --cached`, rewrite history, or claim they are now untracked without user authorization.
4. Verify with `git check-ignore -v --no-index -- <planned-path>` that the intended artifact paths are actually ignored. A matching negation is not successful exclusion; inspect the effective pattern. Check actual paths again when introducing a path affected by different nested rules. The rule alone is not proof when another rule overrides it. Resolve local setup failures or report the blocker instead of falling back to public storage.

Never force-add, stage, commit, push, publish, upload, or automatically copy workflow artifacts into tracked project documentation. Do not require a commit to identify a private model revision. Exclusion prevents ordinary Git discovery, not force-add, packaging, backup, synchronization, or upload: inspect actual publication inputs if asked to release anything. Using a cloud agent may still send read content to its provider; do not describe this arrangement as offline secrecy.

## Layout and ownership

Create only files needed by the selected route and current stage:

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

- `issue.md` is the current work entry and recovery map: bounded objective and exclusions, project/checkout identity, route, model links and applicable approvals, current stage, blockers, next action, and original role handles/recovery information. On the ticket route it also owns the set index required by TICKETS.md: stable ticket identities/links, complete coverage, dependencies, integration/verification ownership, and set approval. Keep planning approval, implementation conformance, and final human acceptance distinct. Do not create a separate `STATE.md` or `INDEX.md`.
- `requirements.md`, `technical.md`, and `change.md` are clean current models governed by their stage standards. Create only the applicable models; missing historical models do not require placeholders. Existing authoritative models can instead be precisely referenced under the location rule above.
- `issues/<NN>-<slug>.md` is one ticket's clean specification and current status. Use stable identifiers and explicit dependencies, not numbering as execution order. Keep its neighboring `<NN>-<slug>.log.md` for its implementation, reviews, repair decisions, evidence, and necessary handoffs. Do not create one file per round, finding, agent, or session.
- `issue.log.md` holds document-stage reviews/repairs/approvals and overall ticket-set review/acceptance. A direct change also keeps its implementation and full-change code review here; it creates no ticket or `issues/` directory merely for bookkeeping. Its identity remains the approved change model path/revision, not a synthetic ticket.
- `delivery.md` is the final implementation summary, not an execution diary or another design authority. It is created after the authorized implementation scope has passed the required independent review and verification, before requesting final user acceptance. A delegated unit returns to the controller rather than creating a whole-work summary. A standalone ticket may summarize only its explicitly identified reviewed scope, never claim whole-set delivery; preserve any existing broader summary rather than overwrite it with a subset. Planning-only skills do not create a delivery summary.

Use relative artifact links and stable heading/finding anchors where possible. Code paths are relative to the identified repository root; record a different checkout explicitly. Agent handles or temporary tool output locations can supplement, but never replace, durable essential content. Do not add secrets, credentials, private reasoning traces, or raw conversation dumps.

## Clean authority and current state

Models and ticket specifications describe the complete current intended result. Integrate revisions into their owning sections with necessary background and key decision basis; remove superseded statements and synchronize diagrams and references. Keep chronological interviews, patch files, changelogs, override appendices, review reports, and implementation diaries outside these canonical artifacts. The logs below are process records, not normative patches.

The current entry and status fields are curated state, not an append-only timeline. Link to their governing records rather than duplicate conclusions everywhere. A log entry cannot silently change a requirement, interface, topology, file responsibility, approval, or ticket dependency. Design changes return to the appropriate modeling gate, update authoritative sections, and regain applicable review/approval before execution proceeds. An obsolete historical decision remains historical, not an alternative current specification.

On resumption read `issue.md`, relevant current models/tickets, open findings, and the latest applicable evidence/decisions. Follow older entries only when needed; do not load every completed ticket's history into each worker. Reconcile actual code, checkout, source approvals, prerequisites, and role availability with the record. Retained context or a stored status is not proof of current validity. Restore original implementation roles according to IMPLEMENTATION.md; model reviewers remain fresh per round.

## Review records and finding lifecycle

Record each independent review under its stage/unit and round in the owning log. Preserve its actual verdict, scope, findings, limitations, and verification coverage without rewriting a failed review into a pass. The controller saves a read-only reviewer's report; in standalone mode the author performs that recording duty. Request a corrected report when incomplete. Shared work-level logs have one controller writer; delegated implementers provide entries to it or write only their assigned unit log under an explicit exclusive assignment.

Each review record identifies:

- Stage/unit, round, date, reviewer identity, and exact reviewed artifact/code basis.
- Governing standards and applicable approved source references.
- `Pass`, `Changes required`, or `Blocked`, with category coverage required by the stage's reviewer contract, actual evidence/limits, and every finding or blocker.
- Prior finding dispositions and whether earlier Pass/evidence remains applicable. Do not hide regression or invalidation by starting a new session or numbering scheme.

Give each finding a stable ID scoped to its stage/unit, such as `technical-F01` or `01-F01`. Reuse it across rounds. Include its precise violated obligation, actual location/behavior, why it matters with background proportional to reader dependence, and an observable closure condition. Do not turn a closure condition into an unapproved design prescription. The repair record cites this ID and the later reviewer records the disposition.

An implementer/author can report `addressed, awaiting review`, not self-close an independent finding. A disputed finding remains open with the actual counter-evidence until the reviewer confirms correction or withdrawal. Genuine upstream design disputes return to modeling. Only the current applicable independent assessment can establish closure; Pass requires no unresolved findings/blockers under the stage's existing gate. Preserve historical results and mark their current applicability; new evidence may reopen an issue. Reviewer Pass is not human approval or acceptance.

## Implementation and repair records

Use the same unit log (or `issue.log.md` for direct work), not a separate repairs file or implementation diary. Organize entries by meaningful implemented result or repair batch; keep a finding, its handling, evidence, and later review connected by IDs and links. Record:

- Objective/acceptance obligation or finding IDs addressed.
- Actual resulting behavior/structure and relevant changed owners, not an inventory of tool calls.
- The handling decision and material background/key rationale. Trivial conformance repairs need only a concise explanation; non-obvious repairs need enough context for an unfamiliar reviewer. Record engineering decisions, not private step-by-step thinking.
- Whether the work stays within approved design; if not, the blocker and subsequent approved upstream decision reference. A repair note itself grants no authorization.
- Exact verification commands/scenarios, actual outcomes, relevant environment/participants/substitutions, and the code basis to which they apply. Distinguish planned, executed, failed, and passed. Keep important observed output/assertions and limitations locally; a vanished terminal or agent link alone is insufficient. Retain large raw artifacts only when necessary, in the work directory with an explicit reference and appropriate redaction.
- Remaining findings/blockers, pending review, and a necessary next action/handoff.

Do not transcribe every read/edit/test invocation, duplicate source definitions, invent evidence, or postpone all recording until the final summary. Completed clean implementation still records its meaningful result and verification even when review finds no issues.

## Revision, approval, and transition integrity

Identify private artifacts with path plus a content digest or another verifiable local revision mechanism; do not pretend an ignored file is identified by the repository HEAD. For a multi-document package identify every relevant source revision. Define any exclusion of non-normative status/approval metadata consistently so metadata-only updates do not invalidate unchanged content, or retain the reviewed digest with an explicit metadata-only change explanation. For code, a commit alone is insufficient when dirty/untracked code participates: identify the checkout and relevant modified/new file content as well. Keep the evidence needed to compare current content; hashes identify a basis but do not recreate missing content.

Review input packages can remain in task dispatches, but their essential source identities, findings, decisions, and verification must be recoverable from the private artifacts. Logs are not Git history or complete snapshots. If an old body cannot be recovered, say so; do not fabricate its content or reapply an unverifiable approval.

Persist at these transitions, before advancing:

1. Save a returned review, including failed or blocked outcomes, before dispatching repair or advancing a gate.
2. Save the implementation/repair decision and fresh evidence before requesting review.
3. Save the new review disposition and update current state before scheduling dependents or handing off.
4. Before a blocker, role replacement, or session/stage handoff, update the recovery entry with current basis, open issues, evidence pointers, roles, and next action.
5. Record explicit human approval/acceptance with its exact scope/basis and a faithful short quotation or durable reference to the actual user decision. An agent must not invent user consent. Approval of an idea, repair proposal, or upstream model is not approval of an unreviewed downstream result.

Source/code changes invalidate affected evidence, reviews, and acceptance under the existing stage standards. Update current applicability without erasing previous outcomes. Do not aggregate ticket Passes into the independent overall verdict. A direct full-change Pass already supplies its final independent review; logging must not introduce a duplicate review or a per-ticket human gate.

## Final delivery summary and retention

After implementation verification and applicable independent Pass, author `delivery.md` as a clean account of the final result:

- **Delivered scope:** observable completed outcomes and explicit exclusions; identify any standalone partial scope.
- **Final design landing:** concise orientation to actual code owners/collaboration/contracts with precise links to synchronized authoritative models, not duplicate definitions.
- **Consequential decisions:** background and actual key basis that a later maintainer needs, with references; not the chronological repair history.
- **Verification and review:** actual checks/results, code/source basis, applicable independent verdicts, participants/substitution limits, and any remaining coverage limits. Unresolved mandatory evidence blocks completion rather than becoming a footnote.
- **Use and maintenance:** necessary configuration, migration, operation, or maintenance instructions, only where applicable.
- **Acceptance:** clearly distinguish `Awaiting acceptance` from explicit acceptance of this result and link its evidence. Update after the human decides; do not infer consent from silence.

On an ordinary conformance repair before acceptance, renew the affected review/evidence and integrate the summary. A later separately authorized change has its own work identity; its delivery summary describes that delivery while synchronized canonical models remain the current authority. Do not treat old summaries as normative overrides.

Keep all artifacts local and excluded, including the summary. A final summary does not authorize deleting process records. Do not automatically delete, move out, publish, or commit the workspace on completion. If the user requests external documentation, separately identify the approved content and destination instead of publishing private records wholesale. No version-control or release action follows merely from a planning approval, Pass, or acceptance.
