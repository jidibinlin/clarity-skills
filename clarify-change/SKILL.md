---
name: clarify-change
description: Use to clarify and model a change to an existing system, including changed behavior, technical decisions, or structure, with reliable, stale, partial, or absent prior documentation. Produce an approved change model before direct implementation or necessary ticket decomposition; also load reference-only when another stage or reviewer needs its change standard; not for coding or implementation logging.
---

# Clarify Change

Establish what the existing system actually does, decide what must change and remain, and produce a complete scoped target design. This is a technical-first modeling workflow, not a shortcut around requirements decisions or design completeness. Do not require an ideal chain of historical documents and approvals that the project never had.

## Entry mode and dependencies

For reference-only use, read the requested standard or reviewer contract and its required dependencies, then return to the consuming stage. Do not investigate, clarify, create artifacts, dispatch reviewers, seek approval, or run the workflow below merely because this skill was loaded. Actual execution retains this route's full review and approval gates.

Load the complete named dependency `workflow-artifacts` and read its entire `WORKFLOW-ARTIFACTS.md` before every role starts or resumes. Follow that skill's loading, supplied-content reuse, missing-dependency blocking, reference-only, and root-separation rules. Before investigation, questions, or drafting, read [CHANGE-MODEL.md](CHANGE-MODEL.md), including the complete applicable TECHNICAL-MODEL.md sections it imports by loading `clarify-technical-design` by name in reference-only mode; apply these standards throughout authoring, repair, and review.

Stage routes name separately installed complete skills: `clarify-requirements` for an authorized scope change into broad requirements discovery, and `implement` or `split-tickets` for the approved next route. Load a routed skill by name for execution only when its stage is authorized. Reference loading and this stage's approval never auto-start the next stage.

Stop after independent model review and explicit human approval; do not implement, fabricate tickets, or create `delivery.md` during planning. As author/controller, establish or reuse the verified workspace under WORKFLOW-ARTIFACTS.md before writing. New work uses `.scratch/<work-slug>/change.md`, with `issue.md` and `issue.log.md`; state the paths and apply the shared location rule to existing canonical models. On resumption perform the shared recovery procedure.

## 1. Inspect the baseline before prescribing changes

Use the already-read CHANGE-MODEL.md and its imported technical-content sections to guide baseline investigation, consequential questions, and each target-model draft, not only later review. Identify the change objective and affected entry points. Inspect existing requirements/technical material if present, repository rules, actual code/callers, interfaces and data, configuration, tests, and relevant runtime facilities. Establish source identities and scope. Preserve existing user work.

Check whether documentation agrees with actual code and evidence. With stale or missing documents, reconstruct the affected current behavior, macro collaboration, micro ownership, file responsibilities, and interfaces from the actual system. Follow a concrete scenario through the involved boundaries, not merely a directory tree. Use targeted safe runtime investigation when behavior or a feasibility assumption cannot be established from existing evidence; do not claim a read-through proves runtime behavior.

Classify inspected facts, confirmed requirements, proposals, and unknowns. Existing behavior is not automatically intended behavior. Expose suspected bugs or accidental constraints without silently preserving them as requirements or changing them as cleanup. Never invent historical approval records. Missing documents alone do not block this workflow; unavailable evidence necessary to understand an affected guarantee does.

## 2. Grill the proposed change and its consequences

Start from the inspected behavior and a concrete proposed outcome. Ask only unresolved human choices that materially change requirements, scope, or technical tradeoffs; recover repository facts and reuse established decisions yourself. Present necessary background, the actual deciding evidence, alternatives where genuinely viable, the recommendation, and its consequences. Wait for a required answer before treating it as settled. Do not enumerate every possible decision or ask for low-value stylistic preferences.

Resolve behavior changes within this workflow alongside the technical consequences. Confirm what is preserved, corrected, replaced, or excluded, with observable acceptance outcomes. Return to the affected question when evidence contradicts a proposal. If the request expands into a separate broad requirement discovery problem, make that scope change explicit and use requirements clarification; do not routinely force a small change through the original two-stage pipeline.

Challenge concept reuse and retirement before proposing additional structure. Identify where an existing object can retain or absorb the responsibility, where concepts should be merged, and what a necessary replacement removes. A new requirement does not by itself justify a new layer or a second representation.

## 3. Model present-to-target behavior at both levels

Apply CHANGE-MODEL.md’s mandatory dimension assessment and imported technical completeness rules. Explain each change and provide the complete scoped target; an unexplained unchanged label or an omitted dimension is insufficient. Unresolved design cannot be approved.

Show current and target views separately where needed to avoid ambiguity. Supply or precisely reference complete target macro and micro topologies and sequences, the file-responsibility tree, definitions, and contracts. Reconstruct missing current views needed to justify the change. Keep unchanged references verified and accessible; do not redraw every project diagram or infer that unchanged topology means unchanged sequence. Explain migration and exit of old responsibilities, representations, files, and callers in the owning sections.

Investigate project integration-test means before selecting coverage under the imported **Overall workflow integration test plan**. Apply CHANGE-MODEL.md’s changed/preserved assessment; detailed TDD remains with implementation.

Choose the execution route using the whole understanding/implementation/verification/repair scope, not patch size:

- **Direct:** one coherent change fits one implementation context with settled owners, prerequisites, acceptance outcomes, and local/macro verification. The approved model is sufficient authority; no ticket or ticket-set index is required.
- **Decomposed:** independently meaningful results, real dependencies, or excessive combined reasoning scope require tickets derived from the same design.

Record the actual reason. If scope grows beyond direct fit, return to this decision and obtain approved decomposition before continuing; never silently invent tickets.

## 4. Integrate canonical models and verify the package

Apply the synchronization rules in CHANGE-MODEL.md. Update affected existing requirements/technical definitions and diagrams in their owning canonical locations, together with the change model. Include the exact resulting sections and their necessary context in the review package. Preserve unaffected decisions. If no earlier models exist, make this scoped change model self-contained enough to govern implementation; do not fabricate a full historical documentation suite.

Keep one authoritative target definition per changed concept under CHANGE-MODEL.md. As controller, maintain `issue.md` and persist process records and recovery state in `issue.log.md` under WORKFLOW-ARTIFACTS.md before blockers or handoffs. Documentation approval is not implementation completion.

Check the complete package against CHANGE-MODEL.md and its imported technical-content requirements, including source references, claimed unchanged views, current-to-target mappings, callers, migrations, contract completeness and execution prerequisites. Correct known omissions and inconsistencies before independent review; return unsettled decisions to clarification rather than delegating them to review or implementation. Render and visually inspect the required diagrams; reused renderings must still apply to the referenced unchanged content. Perform necessary design-feasibility probes. Required unavailable verification is a blocker, not permission to mark the model ready. Future production tests need not already exist or pass.

## 5. Review, repair, and obtain human approval

Dispatch a fresh independent, read-only reviewer every round using [reviewer-prompt.md](reviewer-prompt.md) and its complete package contract. Missing independence, required input, or mandatory verification blocks approval; author self-review cannot substitute.

As controller (author in standalone mode), save every returned review in `issue.log.md` before repair or advancement, following shared record and finding-lifecycle rules. Request correction of stale, incomplete, or inconsistent reports. Repair owning sections and dependent views; return unsettled choices to grilling and obtain missing evidence. Persist repairs and fresh verification before another fresh **full-package** review of all criteria, previous findings, and regressions. Save its disposition and update `issue.md` before advancing. Later implementation retains its original implementer/reviewer; these model-review rounds do not.

Use Draft while clarifying, repairing, or blocked. Current independent Pass with no unresolved issue permits Awaiting approval. Present the target behavior/design, consequential changed/unchanged decisions, synchronized canonical scope, verification and limits, and direct-versus-decomposed route. Ask for explicit approval of this exact package. Earlier answers or old model approvals do not approve it.

Use `Approved` only after explicit human approval of that same current package, persisted and linked from current model metadata and `issue.md` under WORKFLOW-ARTIFACTS.md. Human-requested changes return to clarification, repair, fresh full-package review, and final approval. Content, relevant baseline, or essential-reference changes invalidate affected review/approval under the shared applicability and metadata-only rules. Always obtain a current complete-package review on resumption before handoff; unchanged evidenced final approval may remain applicable after `Pass`.

## 6. Hand off without inventing another planning stage

Return `issue.md`, the approved model path/revision, exact synchronized target references, code baseline, acceptance/verification obligations, prerequisites, and approved route. For a bounded change, the model itself is the implementation basis: load `implement` by name and hand it the approved basis only when execution is authorized, without a ticket, ticket-set index, synthetic ticket ID, or absent historical models. The required `issue.md` work entry is recovery state, not another planning authority or ticket index on this route. For decomposed work, load `split-tickets` by name only when decomposition is authorized and hand it the same approved basis; its own set approval remains required before execution.

If implementation exposes a new behavior/structure decision, clarify it here and reapprove affected content before resuming. A defect against a settled obligation remains an implementation repair, not grounds to rewrite the design to match bad code. Neither route authorizes automatic commits, tracker actions, or release. Preserve the private workspace and logs for implementation; only that later stage creates `delivery.md` after its required verification and independent review.
