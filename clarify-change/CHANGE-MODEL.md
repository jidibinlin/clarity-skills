# Change Model: Authoring and Review Standard

This standard belongs to the `clarify-change` skill. Load that skill by name in reference-only mode when another stage needs this resource; use its resolved companion location or complete current supplied content under the `workflow-artifacts` loading rules. Reading this standard does not start its author's workflow or require that workflow's execution prerequisites. The consuming stage determines the authorized scope and role; actual stage execution retains its existing gates.

## Purpose and governing design standard

Use this standard both to produce a change model and independently review it. A change model governs the transition from an evidenced existing system to a decided target, including changed requirements and technical decisions. It is an implementation contract, not a patch list, an interview transcript, or permission to finish design while coding. Small scope reduces the amount to describe, not the required precision.

Load `clarify-technical-design` by name in reference-only mode under the shared resource-resolution and supplied-content reuse rules, then read and apply only these sections of its resolved companion `TECHNICAL-MODEL.md`: **Approved basis and decision rationale** for reuse, rationale and first-pass constraints; **File organization and responsibility tree**; **Macro runtime and collaboration model**; **Micro object and collaboration model**; **Complete data-structure definitions**; **Complete interface contracts**; **Overall workflow integration test plan**; and **Consistency, evidence, and clean integration** for cross-view coherence and verification. These are the shared design-content requirements, not a second weaker checklist. This standard governs change-specific inputs, baseline reconstruction, change assessment, synchronization, approval, and routing instead of importing the original workflow's requirement for a separately approved prior requirements document or mandatory subsequent tickets.

No prior requirements or technical model is assumed to exist. The change's confirmed requirements and target design may be contained in this one document. An independently reviewed and explicitly human-approved change package is a valid current design basis; historical approval records must not be fabricated to make it fit an initial-project workflow.

## Private location and persistent process records

Load `workflow-artifacts` by name through the Skill tool or the harness's equivalent registered resource mechanism and read its companion `WORKFLOW-ARTIFACTS.md` under its resource-resolution and supplied-content reuse rules before authoring, resuming, or reviewing. It governs private placement, exclusion, persistent records, revision identity, recovery, and transitions in addition to this content standard. New models use `.scratch/<work-slug>/change.md` in the same work directory as `issue.md` and `issue.log.md`; existing authoritative project models may remain precisely referenced and synchronized under its location rule. The author/controller must establish and verify local Git exclusion before workflow writes, including worktree-aware exclusion resolution and tracked-file blocking. Never stage, commit, or publish workflow records; planning creates no `delivery.md`.

Use `issue.md` for current stage, scope/route, model and approval references, blockers, roles, and next action. Resume from it, applicable models, open findings, and latest evidence/decisions, reconciling actual sources before reuse. The controller (author in standalone mode) saves read-only reviewer reports in `issue.log.md`; reviewers do not write logs or exclusion rules. Record each round/reviewer, standards, exact source/model/code basis, verdict, category coverage, evidence/limits, stable finding IDs, and independent dispositions. Private files need path plus digest or another verifiable local revision; repository HEAD alone cannot identify ignored models or dirty/untracked code. Identify every relevant source and preserve enough evidence to compare current content without pretending logs are snapshots.

Persist reviews before repair or gate advancement; repair decisions, material rationale, addressed IDs and fresh evidence before new review; dispositions/current state before handoff; and recovery data before blockers or session/stage transitions. Author repairs are `addressed, awaiting review`, not self-closed findings; disputes remain open with counter-evidence until independent disposition. Save explicit human approval with exact scope/basis and a faithful short quotation or durable reference to the actual decision. Preserve prior outcomes and current applicability in the log, with only current approval metadata in the model. Apply the shared metadata-only revision rule. Task dispatches may carry review packages, but essential identities, decisions, findings, and evidence must persist locally.

## Evidenced baseline and scope

Identify the request, affected existing behavior and participants, source/code identities, necessary external contracts, and the boundaries of investigation and change. Inspect code, callers, state, data, configuration, tests and relevant runtime paths before proposing structure. Scope includes the interactions and preserved guarantees needed to change safely, not an automatic inventory or redesign of the whole repository.

Handle available material according to its reliability:

- **Reliable existing model:** verify the affected content against the current system and use exact references for unchanged definitions and views.
- **Partial or stale model:** identify concrete divergence and reconstruct missing or unreliable affected portions from evidence. Neither the old document nor the implementation automatically wins a requirements dispute.
- **No model:** reconstruct sufficient current behavior and technical structure inside this scoped package to support the decision. Do not demand an invented history, missing historical approvals, or a complete new set of unrelated project documents.

Separate observed/inspected facts, confirmed requirements, proposed decisions, and unknowns. Identify which claims come from code inspection, actual execution, external contracts, or human decisions. Do not call an inferred runtime property observed, or claim a test passed because its code exists. Reproduce uncertain behavior only where needed and permitted; user-supplied observed failures are evidence, not a reason to rerun merely to confirm them.

A historical defect or incidental implementation constraint is not a future requirement. Explicitly decide which current behavior to preserve, correct, replace, or exclude and obtain necessary human decisions. Do not silently fix unrelated defects. Missing documentation is not itself a blocker; an inaccessible fact needed to establish state ownership, behavior, a contract, or design feasibility is. State precisely what cannot be established and how to resolve it.

## Requirements and decision rationale

Describe the desired behavior using concrete scenarios, rules, constraints, exclusions, and observable acceptance outcomes. Make changed requirements and preserved guarantees explicit, including meaningful failure and concurrency outcomes. If requirements do not change, identify the actual preserved obligations and evidence rather than merely saying 'technical change only.' Resolve unknown business rules within this change's clarification loop; technical-first does not grant authority to invent them.

Explain each consequential decision with the background and actual key basis needed by an unfamiliar reviewer. Identify the failed or changed premise of an old decision where relevant, credible alternatives and accepted consequences, and the dependency of micro choices on macro guarantees. Existing decisions need not be interrogated again without contrary evidence. Avoid generic virtues, exhaustive decision trees, repeated empty rationale headings, and a chronological record of questions.

## Mandatory change assessment and complete targets

For every dimension below state **Changed**, **Unchanged**, or **Unresolved**. Explain the basis and affected scope. Changed requires the concrete transformation and complete target; Unchanged requires a verified target reference or description and why the change preserves it; Unresolved prevents approval. Genuine absence of a mechanism is a grounded fact, not permission to omit the view: a single-process system still has a macro collaboration view, and no concurrency must be supported by its execution model.

| Dimension | Required account |
| --- | --- |
| Macro topology | Current and target processes, modules, external participants, responsibility/execution boundaries and actual communication mechanisms. |
| Data flow and state authority | Sources, transformations, direction, representations, authoritative state and write ownership across crossings; distinguish data, control and dependencies. |
| Concurrency and completion | Execution contexts, scheduling, ordering, atomicity/consistency, relevant lifetimes and error/cancellation/shutdown behavior; identify the actual enforcing mechanism and scope. |
| Macro sequences and flows | Entry-to-outcome interactions, participants, ordering, branches and relevant failures; show exactly how changed and preserved scenarios run after the change. |
| Micro topology and ownership | Concrete objects/modules/types, their responsibilities, creation, multiplicity, references, owned state/resources and relationships to macro participants. |
| Micro sequences and operations | Exact collaborating operations, algorithms, transitions, data and error propagation realizing macro guarantees; no unnamed helper hiding a decision. |
| File organization | Complete scoped target file-responsibility tree, assigned objects/definitions, affected unchanged integration files, relocations, removed locations and callers. |
| Data and interface contracts | Complete resulting types/representations and exact operations, owners/locations, pre/postconditions, errors, side effects, lifetime and concurrency semantics, with precise references for unchanged definitions. |

Apply the imported technical-content standard to each target, not merely to the assessment labels. Topology staying unchanged does not establish that ordering, data, ownership, or behavior stayed unchanged. A file list without responsibilities or a proposed change without the resulting definition is incomplete. Settle production algorithms, collaboration and contract details before implementation; the document need not dictate ordinary local expression choices.

Provide complete scoped target macro topology and sequence/flow views and micro topology and sequence views in Mermaid, plus the target file tree and full definitions/contracts. Current views must explain the evidence and transformation where needed; reconstruct them if no trustworthy material exists. Use separate current/target diagrams where one diagram would mix incompatible states or imply false ordering. Small diagrams are acceptable; invented participants or generic boxes are not.

Unchanged target views may use exact accessible references only after verifying they still apply. An absent, stale, generic, or inaccessible reference cannot substitute for a view; describe/draw the necessary content instead. Do not mechanically duplicate every unchanged diagram, but do not equate silence with no impact. Readers must be able to determine the complete scoped target without reconstructing a chain of amendments or private conversation.

## Reuse, consolidation, migration, and exit

Challenge whether a new concept duplicates an existing responsibility, representation, or invariant owner. Prefer the accurate existing concept where it satisfies the target. If its meaning has changed, decide explicitly whether to adjust, merge, move, or replace it. Explain a genuinely necessary new abstraction and what responsibility it owns; a new requirement does not automatically justify a new layer, adapter or file.

For each migrated or replaced responsibility identify the final owner, affected callers and stored/transferred data, applicable transition constraints, and the exit of the old structure. Define a required compatibility interval only when a real requirement supports it, with explicit completion/retirement conditions; do not invent indefinite parallel paths for implementation convenience. Resolve feasibility-sensitive data conversion, ordering or cutover details needed by the scoped change. No generic rollback/retry framework is implied.

Assess the resulting local concept set, not just the added lines. Confirm there is no unclaimed invariant, duplicate source of truth, accidental extra representation or obsolete path left by this change. Keep the analysis bounded to affected responsibilities rather than attaching an unrelated architectural cleanup program.

## Verification and direct-execution fit

Inspect existing integration-test guidance, runner/configuration, representative tests, fixtures/environment and actual invocation before selecting flow coverage. Plan a small set of macro flows showing changed behavior and consequential preserved collaboration. Tie each to the target diagrams, real entry and participants, starting condition, high-level actions, expected observable result, location/invocation and actual substitution limits. Do not demand an exhaustive boundary matrix or write detailed TDD fixtures/assertions at this stage.

Render and visually inspect required diagrams for both graphical and semantic correctness. Reused diagrams require applicable inspected render evidence for the exact unchanged content. Check definitions, references, unchanged claims, scenario traces, source consistency and necessary feasibility facts. If required evidence or rendering is unavailable, retain Draft and report the blocker. Planning approval does not require future production tests to exist or pass, but future macro-flow execution before delivery remains mandatory.

The execution route is a deliberate conclusion:

- **Direct:** one coherent bounded change can be understood, implemented, verified and repaired in one implementation context, with settled target files/owners, prerequisites, acceptance outcomes, and all required local and macro verification. The model is the work authority, identified by its path/revision. No ticket, ticket-set index, or synthetic ticket ID is required. The mandatory `issue.md` recovery entry is not another planning authority or ticket index; direct-work records use `issue.log.md` without creating an `issues/` directory.
- **Decomposed:** several independently meaningful results, real dependencies, or excessive combined reasoning scope require tickets. Supply this same approved package to split-tickets; preserve the target structure and obligations rather than inventing abstractions to ease splitting.

Judge fit using the full reasoning/verification cycle, not age of project, number of changed lines, or a fixed token threshold. If scope grows during execution, return to this route decision and appropriate approved decomposition before continuing; do not squeeze an unsafe large change into 'direct' or silently create unapproved tickets.

## Canonical synchronization and authority

One authoritative current target definition governs each affected concept. A change model explains the decision and transition; it must not become an override layer on top of contradictory canonical requirements/technical models. Where those models exist, integrate changed requirements, definitions, file responsibilities and diagrams into their owning sections and remove superseded rules. Reference exact updated targets from the change model rather than maintain competing definitions.

Review the change model, these resulting canonical sections, and all surrounding dependencies needed for consistency as one identified change package. The approval applies to this complete scoped target and its synchronized references, not an invented reapproval of unrelated historical content. Substantive canonical edits invalidate their affected prior approval claims until this package passes and the human approves it. The change route's coordinated review replaces repeating two separate whole-project clarification workflows; it does not waive affected consistency or evidence.

When earlier models do not exist, this package supplies the complete scoped requirements and technical target directly. Do not create empty stand-in documents or declare nonexistent historical approvals. Future work must consume the latest complete authoritative scoped model, not replay old change notes. If later work establishes a broader canonical model, integrate definitions and point to that owner instead of preserving contradictory alternatives.

Keep target design approval distinct from actual implementation status. The code may still implement the old behavior while a target is approved; this is not evidence the target has shipped. Before implementation, sources and target decisions must be current and approved. During implementation, design deviations return to clarification and renewed package approval. A code-only conformance defect goes to the original implementer for repair, not a model rewrite. After execution, the implementation reviewer checks the actual code, synchronized targets and current runtime evidence; only then can the user accept the implemented result.

Revisions integrate into owning sections with necessary background and decision basis. No normative patches, model-embedded changelogs, override addenda, review reports, implementation diaries, or chronological Q&A belong in canonical artifacts. The required sidecar `issue.log.md` preserves review/repair/approval records and essential evidence under WORKFLOW-ARTIFACTS.md; it never overrides canonical targets. Keep existing authoritative documents in place when appropriate and use the shared exact paths for new private artifacts.

## Independent review and approval

A fresh independent read-only model reviewer receives the complete current package, WORKFLOW-ARTIFACTS.md, this standard and imported content rules, original request and confirmed decisions, actual baseline evidence and documentation gaps, verification artifacts, workspace/exclusion evidence, and previous findings. Do not supply private author reasoning as instructions. Apply every requirement, organized by:

1. **Baseline credibility:** sufficient affected behavior/structure grounded in evidence; document gaps and drift explicit; no fabricated history or accidental behavior promoted to a requirement.
2. **Requirements and rationale:** changed/preserved outcomes, scope and consequential choices are explicit, confirmed where needed, and supported by actual background and basis.
3. **Macro change completeness:** topology, flow/state authority, concurrency and sequences have justified change assessments and complete consistent targets.
4. **Micro and file completeness:** objects, state/resources, concrete operations/sequences and target file responsibilities have justified assessments and complete targets.
5. **Definitions and contracts:** full resulting data/interfaces and behavior resolve the design, including unchanged references and caller obligations.
6. **Concept and transition integrity:** reuse/consolidation choices, migration, final owners and obsolete-path exits are complete without speculative cleanup or indefinite duplicate structures.
7. **Synchronization and authority:** canonical targets and change model agree, each definition has one owner, approval scope is identifiable, and missing original documents do not cause fake prerequisites.
8. **Verification and execution readiness:** mandated current diagram/reference/feasibility checks are supported, future macro coverage is project-grounded, and the direct/decomposed route has evidence and executable obligations.
9. **Private record integrity:** required location and verified exclusion, recovery entry, source/revision identities, persistent review/repair/evidence records, stable finding dispositions, and applicable approval evidence satisfy WORKFLOW-ARTIFACTS.md. Assess records available at this gate; do not require the current report or future human approval before they occur.

Use reviewer-prompt.md for the report contract. Known violations yield Changes required, with additional blockers reported separately. If no violation is demonstrated but required evidence is inaccessible, use Blocked. Pass requires all applicable obligations satisfied without unresolved findings/blockers. Repair then obtain a fresh full-package review, not only a check of prior finding locations. A reviewer cannot approve on the human's behalf or redesign the target according to personal preference.

Draft applies during clarification, repair or blocked assessment. Current independent Pass permits Awaiting approval; explicit human approval of that exact package permits Approved. Changed model content, essential references or relevant baseline assumptions invalidate affected approval and require renewed verification and review; metadata-only updates do not. Resumed material requires a current complete-package assessment before handoff; unchanged established human approval may remain applicable after Pass. Approval authorizes the chosen next stage but does not auto-execute, commit, publish or release anything.
