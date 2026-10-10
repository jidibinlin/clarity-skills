---
name: clarify-architecture
description: Clarify formal overall architecture after a heavyweight requirements package passes independent review and explicit human approval, or resume that architecture. Also load reference-only for architecture content rules. Not for tentative Wayfinder topology, child implementation-detail design, ticketing, or coding.
---

# Clarify Architecture

Settle the selected effort's global technical decisions and cross-child guarantees before children design their complete realizations. Stop at architecture approval; this stage neither finishes child technical models nor authorizes coding.

## Entry mode and dependencies

For reference-only use, read the requested standard/contract and its required dependencies, then return without executing prerequisites, investigation, drafting, review dispatch, or approval. Consuming routes determine their own authorized scope and gates.

Before every role starts or resumes, load `workflow-artifacts` by name and read its entire WORKFLOW-ARTIFACTS.md. Follow its loading, supplied-content reuse, missing-dependency, reference-only, and root-separation rules. Before decisions or drafting, read [ARCHITECTURE-MODEL.md](ARCHITECTURE-MODEL.md) and its named `clarify-technical-design` content dependencies. Apply the same standards during authoring, repair, and independent review.

Routes name separately installed skills: `clarify-requirements` for business-rule conflicts, `clarify-technical-design` for subsequently authorized child realization, and `clarify-change` for approved-model changes under applicable change governance. Reference loading and approval never execute another stage.

## 1. Establish approved scope and inspect reality

Read the root entry's exact requirements package: shared requirements, selected child requirements, and necessary dependencies, with current identities and evidence of the composite independent Pass and explicit human approval. Follow the authoritative sources, not just their index labels. Wayfinder approval permits clarification only; tentative topology and a collection of child-local Passes are not architecture prerequisites. Missing, changed, or unapproved applicable requirements return to their owning gate. Do not require future map ideas outside the authorized scope.

Inspect actual runtime boundaries, code responsibilities, authoritative state, interfaces, callers, repository guidance, and relevant tests. Establish reusable capabilities and necessary changes before proposing topology. Investigate actual integration-test guidance, runners/configuration, representative tests, fixtures/environment and commands under the imported **Overall workflow integration test plan** before selecting flows. Inaccessible essential facts are blockers, not questions asking the human to invent repository facts.

Reuse the verified excluded effort root. The root author/controller owns `architecture.md`, root `issue.md` updates, and root `issue.log.md`; use precisely referenced existing authority instead where applicable. State paths, selected scope, source identities, and writer. Perform shared recovery on resumption. Create only needed artifacts; no child technical models, tickets, production code, or `delivery.md`.

## 2. Grill consequential global choices while modeling

Start with an approved cross-child scenario, inspected system behavior, and a candidate global design. Challenge runtime boundaries, state authority, data movement, ordering/concurrency, completion/failure semantics, and responsibility allocation. Trace consequential counterexamples, including overlap or partial completion when relevant; test whether the proposed mechanism actually establishes each required guarantee and whether a reusable existing owner avoids a new abstraction.

Resolve accessible facts and reuse confirmed constraints yourself. Ask only when materially different compliant choices need human authority/preference or a missing human constraint changes the result. Give the inspected background, actual uncertainty, viable alternatives and consequences, recommendation with its real basis, and affected guarantees/children. Ask a focused question or small independent round, wait for the answer, and do not treat a proposal or silence as a decision. Dependent choices wait for their prerequisites; a fully specified input may require no questions.

Use draft topology, dataflow and macro sequences to make choices concrete. Integrate each answer and its actual deciding rationale into the owning model section. Business-rule conflicts return to requirements; do not redefine the product here. Use targeted disposable feasibility investigation when needed, recording only what was actually exercised. Keep unverified assumptions and unresolved decisions visible.

Completion means the architecture standard's global decision boundary is fully settled, all cross-boundary guarantees needed to design children are clear, and every permissible later concrete realization has an explicit child design owner. Child detail is a later modeling obligation, never an instruction for coding to decide production design.

## 3. Complete the architecture and current evidence

Apply ARCHITECTURE-MODEL.md to the clean integrated model: complete relevant macro views, shared guarantees/contracts, responsibility ownership, exact requirement traces, explicit realization assignments, and a small project-grounded overall integration-flow plan. Preserve necessary background and deciding rationale without duplicating child details or turning the document into tickets.

Walk the approved scenarios through all views, check referenced definitions against the repository, and obtain evidence for feasibility-sensitive assumptions. Actually render and visually inspect every Mermaid diagram; retain current renderings and inspection evidence for review. Parsing is insufficient. Planned integration flows are not executed tests. Missing renderer, visual inspection, source access, required decision, or feasibility evidence keeps `Draft` and blocks the affected gate honestly.

## 4. Independently review, repair, and fully re-review

Dispatch a fresh independent read-only reviewer every round using [reviewer-prompt.md](reviewer-prompt.md) and its complete input package. Author checks never replace this gate; unavailable independence or required inputs keep `Draft`.

The root controller saves every returned report in the root log before repair or advancement under WORKFLOW-ARTIFACTS.md. Request correction of incomplete, stale, or inconsistent reports. For `Changes required`, repair owning sections and all dependent views, returning material unresolved choices to grilling. For `Blocked`, recover the missing evidence/access. Persist repairs and current verification before another fresh **full-architecture** review, including prior findings and regressions. Only an applicable independent disposition closes findings.

A current `Pass` with all applicable criteria satisfied, required verification present, and no unresolved findings/blockers permits the human gate. Source changes trigger the shared impact procedure and renewed affected gates; neither status labels nor stale reviews authorize dependent work. On resumption, run this review before an approved handoff, preserving evidenced human approval only if its unchanged basis remains applicable.

## 5. Obtain explicit human approval and stop

After Pass, set `Awaiting approval`. Present the model path/revision, selected scope and requirements basis, passing conclusion, global topology and consequential choices, cross-child guarantees and realization owners, and the limited overall integration plan. Ask explicitly whether the human approves this reviewed architecture for child technical modeling. Wait; agreement with individual choices or an earlier map is not final approval.

Requested changes return to clarification, integrated repair, current verification and fresh full independent review before renewed approval. Record `Approved` only for the same current architecture and source basis that passed review and received explicit human approval; persist decision evidence and update root source-package/index links under WORKFLOW-ARTIFACTS.md.

Return the root entry, architecture and governing requirements identities, applicable review/approval records, child design assignments, and essential references. If blocked, return the persisted draft/blocker, never an approved handoff. Stop. Separately authorized `clarify-technical-design` may now complete applicable children; architecture approval does not create tickets, start implementation, or close the effort.
