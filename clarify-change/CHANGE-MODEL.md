# Change Model: Authoring and Review Standard

This standard belongs to the `clarify-change` skill. Load that skill by name in reference-only mode when another stage needs this resource; use its resolved companion location or complete current supplied content under the `workflow-artifacts` loading rules. Reading this standard does not start its author's workflow or require that workflow's execution prerequisites. The consuming stage determines the authorized scope and role; actual stage execution retains its existing gates.

## Purpose and governing design standard

Use this standard both to produce a change model and independently review it. A change model governs the transition from an evidenced existing system to a decided target, including changed requirements and technical decisions. It is an implementation contract, not a patch list, an interview transcript, or permission to finish design while coding. Small scope reduces the amount to describe, not the required precision.

Load `clarify-technical-design` by name in reference-only mode and read these complete applicable sections of its resolved `TECHNICAL-MODEL.md` under the shared loading rules:

- **Approved basis and decision rationale**, including **Progressive design convergence**
- **File organization and responsibility tree**
- **Macro runtime and collaboration model**
- **Micro object and collaboration model**
- **Complete data-structure definitions**, including **Clarify actual declarations with the human**
- **Complete interface contracts**
- **Overall workflow integration test plan**
- **Consistency, evidence, and clean integration**

They own technical content, first-pass constraints, macro-flow planning and verification. When an existing overall architecture authority governs affected work, also load `clarify-architecture` by name reference-only and read applicable ARCHITECTURE-MODEL.md content criteria before investigation/decisions and review. Apply those criteria to affected global guarantees and collaboration without executing initial architecture gates. If affected decomposition remains in `wayfinder.md`, load `wayfinder` reference-only for its applicable map criteria; tentative estimates remain subordinate to formal models. This standard adds change-specific baseline, assessment and synchronization; [SKILL.md](SKILL.md) owns eligibility and gates.

No prior requirements, architecture or technical model is assumed. Confirmed requirements and target design may be contained in this scoped document. A reviewed and explicitly human-approved change package is a valid current basis: do not fabricate architecture history, retrospective approvals, or a full heavyweight route when reconstructing missing documentation. Existing applicable authorities still constrain the change.

## Shared artifact contract

Before starting or resuming any role, load `workflow-artifacts` by name and read all of `WORKFLOW-ARTIFACTS.md`. It owns storage, records, revision/approval identity, and transitions. The execution entry owns artifact paths and persistence triggers.

Apply **Human-confirmed specification writes** in WORKFLOW-ARTIFACTS.md throughout authoring and repair. Every initial model, entry/index, synchronized source, diagram, removal, formatting correction and embedded status/approval metadata change requires the original author to show the exact content or patch and current basis in the conversation, obtain explicit human confirmation, and write only that change. No design-preserving or administrative exemption applies. A direction-only answer does not approve unseen declarations or text. Keep unconfirmed proposals, missing-answer placeholders and deferred questions in the conversation, not canonical sections, sidecar drafts or review logs. Confirmed groups may be integrated progressively; these full content obligations still govern completeness before handoff. Preserve exact-write confirmation references with the applicable review submission or finding-linked repair record; actual records retain their existing admission rules. Write permission, independent conformance and final human approval remain distinct.

## Evidenced baseline and scope

Identify the request, affected behavior/participants, source/code identities, external contracts and boundaries of investigation/change. Resolve supplied effort/child paths through their root entry and exact source package when present. Inspect relevant shared requirements, overall architecture, child requirements/technical models and map decomposition references alongside code, callers, state/data, configuration, tests and runtime paths. Scope includes interactions and preserved guarantees needed to change safely, not an automatic whole-project inventory or redesign.

Handle available material according to its reliability:

- **Reliable existing model:** verify the affected content against the current system and use exact references for unchanged definitions and views.
- **Partial or stale model:** identify concrete divergence and reconstruct missing or unreliable affected portions from evidence. Neither the old document nor the implementation automatically wins a requirements dispute.
- **No model:** reconstruct sufficient current behavior and technical structure inside this scoped package to support the decision. Do not demand an invented history, missing historical approvals, or a complete new set of unrelated project documents.

Separate observed/inspected facts and confirmed requirements from proposed decisions and unknowns during discussion. Proposed decisions and unknowns remain in the conversation until resolved into exact content confirmed for writing; baseline reconstruction is also subject to the write gate. Identify which claims come from code inspection, actual execution, external contracts, or human decisions. Do not call an inferred runtime property observed, or claim a test passed because its code exists. Reproduce uncertain behavior only where needed and permitted; user-supplied observed failures are evidence, not a reason to rerun merely to confirm them.

A historical defect or incidental implementation constraint is not a future requirement. Explicitly decide which current behavior to preserve, correct, replace, or exclude and obtain necessary human decisions. Do not silently fix unrelated defects. Missing documentation is not itself a blocker; an inaccessible fact needed to establish state ownership, behavior, a contract, or design feasibility is. State precisely what cannot be established and how to resolve it.

## Requirements and decision rationale

Describe the desired behavior using concrete scenarios, rules, constraints, exclusions, and observable acceptance outcomes. Make changed requirements and preserved guarantees explicit, including meaningful failure and concurrency outcomes. If requirements do not change, identify the actual preserved obligations and evidence rather than merely saying 'technical change only.' Resolve unknown business rules within this change's clarification loop; technical-first does not grant authority to invent them.

Explain each consequential decision with the background and actual key basis needed by an unfamiliar reviewer. Identify the failed or changed premise of an old decision where relevant, credible alternatives and accepted consequences, and the dependency of micro choices on macro guarantees. Existing decisions need not be interrogated again without contrary evidence. Avoid generic virtues, exhaustive decision trees, repeated empty rationale headings, and a chronological record of questions.

## Mandatory change assessment and complete targets

During clarification, assess every dimension below as **Changed**, **Unchanged**, or **Unresolved**, explaining the basis and affected scope in the conversation. In the model, write only exact human-confirmed assessments: Changed requires the concrete transformation and complete target; Unchanged requires a verified target reference or description and why the change preserves it. Keep Unresolved assessments in the conversation, not placeholder model rows; they prevent approval until resolved and their exact resulting content is confirmed and integrated. Genuine absence of a mechanism is a grounded fact, not permission to omit the view: a single-process system still has a macro collaboration view, and no concurrency must be supported by its execution model.

| Dimension | Owning TECHNICAL-MODEL.md section |
| --- | --- |
| Macro topology | Macro runtime and collaboration model — Topology |
| Data flow and state authority | Macro runtime and collaboration model — Data flow and state authority |
| Concurrency and completion | Macro runtime and collaboration model — Concurrency and ordering |
| Macro sequences and flows | Macro runtime and collaboration model — Sequences |
| Micro topology and ownership | Micro object and collaboration model — Topology and ownership |
| Micro sequences and operations | Micro object and collaboration model — Sequences and operations |
| File organization | File organization and responsibility tree |
| Data and interface contracts | Complete data-structure definitions; Complete interface contracts |

Apply the imported technical-content standard to each target, not merely to the assessment labels. Topology staying unchanged does not establish that ordering, data, ownership, or behavior stayed unchanged. A file list without responsibilities or a proposed change without the resulting definition is incomplete. Settle production algorithms, collaboration and contract details before implementation; the document need not dictate ordinary local expression choices.

All imported target views remain mandatory: macro and micro Mermaid topologies and sequences, scoped file-responsibility tree, complete data definitions, and interface contracts. Current views must explain the transformation where needed; reconstruct them when no trustworthy material exists. Separate current and target diagrams where combining them would mix incompatible states or imply false ordering.

Unchanged target views may use exact accessible references only after verifying they still apply. An absent, stale, generic, or inaccessible reference cannot substitute for a view; describe/draw the necessary content instead. Do not mechanically duplicate every unchanged diagram, but do not equate silence with no impact. Readers must be able to determine the complete scoped target without reconstructing a chain of amendments or private conversation.

## Reuse, consolidation, migration, and exit

Challenge whether a new concept duplicates an existing responsibility, representation, or invariant owner. Prefer the accurate existing concept where it satisfies the target. If its meaning has changed, decide explicitly whether to adjust, merge, move, or replace it. Explain a genuinely necessary new abstraction and what responsibility it owns; a new requirement does not automatically justify a new layer, adapter or file.

For each migrated or replaced responsibility identify the final owner, affected callers and stored/transferred data, applicable transition constraints, and the exit of the old structure. Define a required compatibility interval only when a real requirement supports it, with explicit completion/retirement conditions; do not invent indefinite parallel paths for implementation convenience. Resolve feasibility-sensitive data conversion, ordering or cutover details needed by the scoped change. No generic rollback/retry framework is implied.

Assess the resulting local concept set, not just the added lines. Confirm there is no unclaimed invariant, duplicate source of truth, accidental extra representation or obsolete path left by this change. Keep the analysis bounded to affected responsibilities rather than attaching an unrelated architectural cleanup program.

## Verification and execution readiness

Apply **Overall workflow integration test plan** in TECHNICAL-MODEL.md without redefining its fields or expanding it into detailed TDD. The change-specific selection must cover changed behavior and consequential preserved collaboration. Explain which existing flow coverage remains valid and what requires new or revised coverage.

Apply **Consistency, evidence, and clean integration** to the complete change package, including claimed unchanged views, current-to-target mappings, affected callers, migrations, and canonical references. Reused diagrams need applicable inspected render evidence for the exact unchanged content. Missing mandatory verification blocks readiness; future production tests need not already exist or pass.

Provide the evidence supporting the direct/decomposed route selected under [SKILL.md](SKILL.md), including scope, prerequisites, acceptance outcomes, and verification obligations. A route label does not establish whole-cycle boundedness.

## Canonical synchronization and authority

One authoritative current target definition governs each concept. After the original owners show exact patches and receive human write confirmation, integrate only those changes into their owning requirements, architecture and technical sections, removing superseded rules and synchronizing diagrams as confirmed; the change model explains the transition and precisely references those targets, not an override layer. In hierarchy, cover affected root shared requirements, global architecture, child requirements/technical models and map decomposition references. Return conflicts to the owning layer under WORKFLOW-ARTIFACTS.md; a child addendum cannot override a global guarantee. The root controller owns shared edits/indices; each write still needs exact confirmation. Delegated child writers receive the exact confirmed content, basis and confirmation reference, stay within assigned artifacts and return proposed parent edits to their owner.

Review the change model, resulting canonical sections and necessary surrounding dependencies as one identified scoped package. Trace impact through cross-child contracts, callers, descendants, tickets and integration flows; identify affected review/approval, unit and combined evidence and acceptance, and the explicit basis for preserving unaffected work. Preview root source-identity, scope/coverage/dependency-index and affected child-link patches through their owners; obtain exact write confirmation before synchronizing them. Affected approval claims remain stale until this package passes and receives human approval; affected implementation evidence must then be renewed on conforming code with original roles. This coordinated gate replaces separate whole-project ceremonies, not affected consistency checks. Never restart every child or ticket without impact.

When earlier models do not exist, this package supplies the complete scoped requirements and technical target directly. Do not create empty stand-in documents or declare nonexistent historical approvals. Future work must consume the latest complete authoritative scoped model, not replay old change notes. If later work establishes a broader canonical model, integrate definitions and point to that owner instead of preserving contradictory alternatives.

Keep target design approval distinct from actual implementation status. The code may still implement the old behavior while a target is approved; this is not evidence the target has shipped. Before implementation, sources and target decisions must be current and approved. During implementation, design deviations return to clarification and renewed package approval. A code-only conformance defect goes to the original implementer for repair, not a model rewrite. After execution, the implementation reviewer checks the actual code, synchronized targets and current runtime evidence; only then can the user accept the implemented result.

Apply the imported clean-integration rules to each owning section. Before/after explanations, original evidence and actual decision rationale belong beside the affected concept, not in amendments or an interview log. Keep unresolved choices in the conversation, identifying affected canonical rules, missing inputs, deferred-decision owners and effects on the current scope. Show the exact settled-answer and rationale/evidence patch, obtain human write confirmation, then integrate only that content in the owning sections without a duplicate queue. WORKFLOW-ARTIFACTS.md governs `change.review-fix-decisions.log.md` and current approval metadata; neither overrides canonical targets. Entries retain exact package scope, source paths/sections and revisions, while models and object review logs supply approval evidence. A downstream referral links to this package’s design resolution and review/approval evidence rather than duplicating it in the originating review record.

## Delivery criteria

Apply this standard and every imported content requirement to the complete current package, organized by these categories. [reviewer-prompt.md](reviewer-prompt.md) defines review inputs and results; the execution entry owns review/repair and human approval.

1. **Baseline credibility:** sufficient affected behavior/structure grounded in evidence; document gaps and drift explicit; no fabricated history or accidental behavior promoted to a requirement.
2. **Requirements and rationale:** changed/preserved outcomes, scope and consequential choices are explicit, confirmed where needed, and supported by actual background and basis.
3. **Macro change completeness:** topology, flow/state authority, concurrency and sequences have justified change assessments and complete consistent targets.
4. **Micro and file completeness:** objects, state/resources, concrete operations/sequences and target file responsibilities have justified assessments and complete targets.
5. **Definitions and contracts:** full resulting data/interfaces and behavior resolve the design, including unchanged references and caller obligations.
6. **Concept and transition integrity:** reuse/consolidation choices, migration, final owners and obsolete-path exits are complete without speculative cleanup or indefinite duplicate structures.
7. **Synchronization and authority:** canonical requirements, architecture, child models, affected decomposition references and change model agree; definitions and root/child writers have explicit owners, source/approval scope and downstream impact are identified, and missing history causes no fake prerequisites.
8. **Verification and execution readiness:** mandatory diagram/reference/feasibility checks are supported, cross-child/global flow coverage and real prerequisites have owners, affected evidence is invalidated with an unchanged-scope basis, and the direct/decomposed route has evidence and executable obligations.
9. **Private record integrity:** satisfy WORKFLOW-ARTIFACTS.md for records due at this gate, including evidence that actual specification writes match exact displayed content and explicit prior human confirmation. Assess initial drafting, entries/indices, synchronization, repairs and embedded metadata as well as model rules; do not demand this review report or future final human approval before they occur.

The approved scope is this synchronized target and its necessary surrounding consistency, not an invented reapproval of unrelated history. Design approval is distinct from implementation completion.
