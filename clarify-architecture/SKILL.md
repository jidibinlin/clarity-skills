---
name: clarify-architecture
description: Clarify formal overall architecture after a heavyweight requirements package passes independent review and explicit human approval, or resume that architecture. Also load reference-only for architecture content rules. Not for tentative Wayfinder topology, child implementation-detail design, ticketing, or coding.
---

# Clarify Architecture

Settle the selected effort's global technical decisions and cross-child guarantees before children design their complete realizations. Stop at architecture approval; this stage neither finishes child technical models nor authorizes coding.

## Entry mode and dependencies

For reference-only use, read the requested standard/contract and its required dependencies, then return without executing prerequisites, investigation, drafting, review dispatch, or approval. Consuming routes determine their own authorized scope and gates.

Before every role starts or resumes, load `workflow-artifacts` by name and read its entire WORKFLOW-ARTIFACTS.md. Follow its loading, supplied-content reuse, missing-dependency, reference-only, and root-separation rules. Before decisions or drafting, read [ARCHITECTURE-MODEL.md](ARCHITECTURE-MODEL.md) and its named `clarify-technical-design` content dependencies. Apply the same standards during authoring, repair, and independent review.
For every substantive question, load the named `ask-with-context` skill and read its complete SKILL.md under the shared loading rules. Its **Required question format and pre-send check** is mandatory at the point of asking, including follow-ups, resumed work, and repair questions; it is not optional reference advice. Apply its answer-to-next-decision loop after every answer. Keep unresolved decisions beside their affected canonical rules, identify any deferred decision's owner and blocked scope, and integrate settled answers with their necessary rationale and evidence there. Reconcile remaining decisions after every answer and before handoff; maintain no separate queue or interview log. This stage retains its authorized scope, artifacts, completeness checks, and approval gates.

Routes name separately installed skills: `clarify-requirements` for business-rule conflicts, `clarify-technical-design` for subsequently authorized child realization, and `clarify-change` for approved-model changes under applicable change governance. Reference loading and approval never execute another stage.

Before assigning architecture work or writing, apply **Persistent author/reviewer lifecycle** in WORKFLOW-ARTIFACTS.md: bind or resume the original architecture author/repair owner; bind the independent reviewer at first review and retain that pair through final review, human revisions, and source reassessment. Use the architecture review log's identity header and the shared recovery/replacement rules, not new role state.

## 1. Establish approved scope and inspect reality

Read the root entry's exact requirements package: shared requirements, selected child requirements, and necessary dependencies, with current identities; resolve composite independent Pass and explicit human approval evidence through the requirements models and their review logs. Follow the authoritative sources, not just their index labels. Wayfinder approval permits clarification only; tentative topology and a collection of child-local Passes are not architecture prerequisites. Missing, changed, or unapproved applicable requirements return to their owning gate. Do not require future map ideas outside the authorized scope.

Inspect actual runtime boundaries, code responsibilities, authoritative state, interfaces, callers, repository guidance, and relevant tests. Establish reusable capabilities and necessary changes before proposing topology. Investigate actual integration-test guidance, runners/configuration, representative tests, fixtures/environment and commands under the imported **Overall workflow integration test plan** before selecting flows. Inaccessible essential facts are blockers, not questions asking the human to invent repository facts.

Reuse the verified excluded `.scratch/<effort>/` root. The root author/controller owns `architecture.md`, `architecture.review-fix-decisions.log.md`, and definition/source-package/navigation updates to root `issue.md`; use precisely referenced existing model authority instead where applicable. State paths, selected scope, source identities, and writer. On resumption reconcile the entry, current models, source identities and applicable review/approval evidence. Keep unresolved decisions current in their owning sections before blockers or handoffs; report other execution blockers in the handoff. Create only needed artifacts; no child technical models, tickets, production code, or `delivery.md`.

## 2. Grill consequential global choices while modeling

Work top-down from approved cross-child scenarios and inspected system behavior to the global process/module topology, boundaries and responsibility allocation, then the solution directions needed for consequential technical problems. Explain how selected mechanisms establish data/state authority, movement, ordering/concurrency and completion/failure guarantees; naming technologies is insufficient. Trace relevant counterexamples and prefer an existing owner when it can satisfy the role. Apply the macro part of **Macro-first, dependency-led micro design**; child technical stages later develop their concrete module foundations and collaboration bottom-up, not here.

Use `ask-with-context` and the imported **Progressive design convergence** rule for each bounded global decision group: propose and actually show the relevant macro topology/dataflow/sequence and guarantees, obtain confirmation or corrections, then refine the next dependent group. Direction agreement alone does not approve the topology. Keep look-ahead coarse; do not privately finish the whole architecture and ask only for final approval, even with a Draft label. Keep child micro decisions out of this stage; fully specified input needs no questions only when concrete current designs have applicable confirmation or inspected unchanged-reuse evidence.

Model inside that loop, integrating each answer, its attributable evidence and deciding rationale in the owning section before proceeding. Reconcile affected views and reopen only decisions whose premises change; do not silently override them. Business-rule conflicts return to requirements. Use targeted disposable feasibility investigation when needed, preserving actual evidence for review rather than a process diary. Keep unverified assumptions and unresolved decisions explicit beside the affected rules.

Completion means the global boundary has converged with the human through actual scoped proposals, all cross-boundary guarantees needed to design children are settled, and every later concrete realization has an explicit child design owner. Complete architecture views in step 3 as part of this loop, not as autonomous design after questions end. Child detail remains a later modeling obligation, never a coding decision.

## 3. Complete the architecture and current evidence

Apply ARCHITECTURE-MODEL.md to the clean integrated model: complete relevant macro views, shared guarantees/contracts, responsibility ownership, exact requirement traces, explicit realization assignments, and a small project-grounded overall integration-flow plan. Preserve necessary background and deciding rationale without duplicating child details or turning the document into tickets.

Walk the approved scenarios through all views, check referenced definitions against the repository, and obtain evidence for feasibility-sensitive assumptions. Actually render and visually inspect every Mermaid diagram; retain current renderings and inspection evidence for review. Parsing is insufficient. Planned integration flows are not executed tests. Missing renderer, visual inspection, source access, required decision, or feasibility evidence keeps `Draft` and blocks the affected gate honestly.

## 4. Independently review, repair, and fully re-review

Record the submission and current evidence in `architecture.review-fix-decisions.log.md`, then send it to the bound independent read-only reviewer using [reviewer-prompt.md](reviewer-prompt.md). Supply its initial package at first review and incremental follow-ups under the shared lifecycle thereafter, keeping all current sources accessible. Author checks never replace this gate; unavailable independence or required inputs keep `Draft`.

The root controller saves every returned report in `architecture.review-fix-decisions.log.md` before repair or advancement under WORKFLOW-ARTIFACTS.md. Return incomplete, stale, or inconsistent reports to the same reviewer for correction. For `Changes required`, return findings to the original architecture author to repair owning sections and dependent views, returning material unresolved choices to grilling. For `Blocked`, recover the missing evidence/access. Route upstream defects to their owning stage's bound author/reviewer, then return current approved results and evidence to the originating architecture reviewer. Persist finding-linked repair decisions and current verification before returning to that same reviewer for **full-architecture** assessment, including prior findings and regressions. Only an applicable independent disposition closes findings; save it before advancing.

A current `Pass` with all applicable criteria satisfied, required verification present, and no unresolved findings/blockers permits the human gate. Source changes trigger the shared impact procedure and renewed affected gates through their original roles; neither status labels nor stale reviews authorize dependent work. On resumption, restore the bound pair and run this review with the same reviewer before an approved handoff, preserving evidenced human approval only if its unchanged basis remains applicable.

## 5. Obtain explicit human approval and stop

After Pass, set `Awaiting approval`. Present the model path/revision, selected scope and requirements basis, passing conclusion, global topology and consequential choices, cross-child guarantees and realization owners, and the limited overall integration plan. Ask explicitly whether the human approves this reviewed architecture for child technical modeling. Wait; agreement with individual choices or an earlier map is not final approval.

Requested changes return to the original author for clarification, integrated repair and current verification, then to the same reviewer for full independent review before renewed approval. Record `Approved` only for the same current architecture and source basis that passed review and received explicit human approval; persist decision evidence in `architecture.review-fix-decisions.log.md` and link approval from model metadata under WORKFLOW-ARTIFACTS.md. The root entry retains exact package scope, source paths/sections and revisions, not approval-record navigation.

Return the root entry, architecture and governing requirements identities, applicable review/approval records, child design assignments, and essential references. If blocked, return the draft, its inline unresolved decisions, and any remaining review or execution blockers, never an approved handoff. Stop. Separately authorized `clarify-technical-design` may now complete applicable children; architecture approval does not create tickets, start implementation, or close the effort.
