---
name: split-tickets
description: Use after requirements and technical models have passed independent review and final human approval to split implementation work or revise an existing ticket set; also use for an approved change package that needs decomposition instead of direct implementation. Not for production design, coding, or executing tickets.
---

# Split Tickets

**Entry mode:** When another stage or reviewer loads this skill only for its standards, use reference-only mode: read the requested resources and mandatory shared contract, then return without planning, writing artifacts, dispatching review, or requesting approval. Execute the numbered workflow only for authorized ticket planning; a dependency load does not authorize it.

Turn an approved requirements-and-technical basis into small, coherent implementation work units when decomposition is needed. Each ticket must be understandable, implementable, verifiable, and repairable in a fresh context without reconstructing the author's conversation. Split the work, not the approved code structure.

Before starting, resuming, or reviewing, load the registered skill `workflow-artifacts` by name using the Skill tool or the harness's equivalent named resource mechanism (omp: `skill://workflow-artifacts`), and read its WORKFLOW-ARTIFACTS.md. Then read [TICKETS.md](TICKETS.md). The shared contract governs private storage, records, recovery, and resource resolution; TICKETS.md governs ticket content and approval. Install this complete skill and its named dependency independently; they need not share a parent directory.

Resolve companions from their owning installed skill/document, not the product checkout or another skill. Reuse supplied complete current standards or verified readable resources with their owning skill identities; summaries do not suffice and intact inputs need no recursive load. Missing, ambiguous, or inaccessible dependencies block affected work: report the exact skill/resource and needed access, without guessing locations or auto-installing. Keep the read-only skill installation distinct from the target repository, where code, commands, and `.scratch/<work-slug>/` belong.

Stage routes name `clarify-requirements`, `clarify-technical-design`, `clarify-change`, `split-tickets`, and `implement`. Load a selected stage by name only when its reference is needed or execution is authorized; reference access never starts that stage or bypasses any stop or approval gate.

Stop after independent review and final human approval of the complete ticket set. Do not execute tickets, write production or test code, invent the later TDD policy, publish remote issues, or commit changes automatically.

## 1. Establish the approved baseline

Establish one of the two approved source routes defined in TICKETS.md: the current requirements and technical models, or the current change package from `clarify-change`. Read its exact essential references and independent-review and final-human-approval evidence. For the original route, confirm that the technical model realizes the same requirements baseline. For the change route, approval covers the change model and synchronized affected sections of existing canonical models together; absent old separate models or historical approvals are not missing prerequisites. A status label or agreement with an earlier proposal is insufficient.

On the change route, read the change model's direct-versus-decomposed routing decision and evidence. A bounded change that fits one complete implementation unit goes directly to `implement` with its approved change basis; do not manufacture a ticket or ticket-set index for it. Its root `issue.md` remains the required work entry. Continue here only when decomposition is needed.

Inspect the relevant existing code, callers, repository guidance, and verification facilities to distinguish observed current behavior from confirmed requirements and unknowns. Use the selected basis's target file assignments, object topology, data definitions, interface contracts, and macro-flow test plan as constraints, not suggestions to redesign or approval of legacy defects.

If an upstream decision is missing, contradictory, or no longer matches the approved baseline, return it to requirements or technical clarification for the original route, or to `clarify-change` for the change route. Do not force a change through the entire original two-stage pipeline or solve a production-design gap inside a ticket. Resume after the affected source package completes its own review and approval gate.

Reuse `.scratch/<work-slug>/` for this work. Before any artifact write, establish and verify local Git exclusion under WORKFLOW-ARTIFACTS.md, including worktree-aware exclusion resolution and tracked-file blocking. Use its `issue.md` as work entry and set index, `issues/NN-<slug>.md` for tickets, and same-stem `.log.md` files for their later execution records. Planning reviews, repairs, and approvals belong in root `issue.log.md`. Update the existing set rather than create a competing plan; begin new sets at `Draft`. On resumption read the entry, current sources/tickets, open findings, and applicable evidence; reconcile them with actual code and approvals.

## 2. Find coherent work units and real dependencies

Map the approved design to the changes needed in the inspected code. Identify useful intermediate results, their required inputs, and the responsibilities they realize. Prefer a narrow behavior or coherent structural change over a list of files to create. A ticket may touch several files, and several tickets may successively work on one file or object.

Keep a unit together where splitting it would break a contract, require a stub, or leave an invalid intermediate state. Not every ticket must complete the whole macro business flow; local work can precede integration when it has a meaningful verifiable result and declared prerequisites. Conversely, a small title does not make a large end-to-end change small.

Identify blocking dependencies from the outputs a ticket actually requires. Separate real prerequisites from a convenient reading order. Preserve the approved cutover: do not invent adapters, compatibility layers, temporary protocols, or new files solely to make tickets independent. If a valid bounded sequence needs a production-design change, return that problem to the selected route's upstream clarification.

Assign each approved macro-flow test to the ticket or tickets that will implement and run it once its real participants are available. Include the work that joins locally completed pieces into the full collaboration. A collection of locally passing tickets must not omit the final flow verification before release or handoff to joint integration.

## 3. Size for a fresh implementation context

Apply the context-fit criteria in TICKETS.md to the entire cycle: understanding the references, reading relevant code, implementing, verifying, investigating failures, and repairing. Do not size by ticket prose, line count, file count, or an invented universal token threshold.

For each candidate, identify the minimum source sections, code relationships, concepts, and prerequisite outputs the implementer must keep in view. Split unrelated objectives or independently verifiable results when that reduces simultaneous reasoning. Merge fragments that only create empty structures or spread one inseparable change across tickets. Do not alter the agreed architecture to obtain smaller work units.

Ask the human only about consequential decomposition choices, such as priorities or granularity tradeoffs not settled by the inputs. Present the affected result, alternatives, and recommendation. Recover facts from the repository and reuse settled decisions; do not reopen business or technical choices merely because a ticket needs them.

## 4. Write the index and fresh-context tickets

Use the artifact contract in TICKETS.md. Give every ticket a concrete objective, necessary background, precise model and code references, bounded work and exclusions, prerequisite outputs, acceptance outcomes, and the verification needed for this increment. Keep definitions authoritative in the upstream models; do not copy entire documents or turn the ticket into a new technical specification.

The index carries the selected source route and exact approved baseline, links to all tickets, coverage of requirements and target technical obligations, dependency relationships, and ownership of cutover and macro-flow verification. On the change route, cite the precise change requirements and target technical sections, including essential references and affected canonical sections, rather than requiring two separate source models. Use stable ticket identifiers and explicit links. Initial numbering may follow dependency order, but a number is not a dependency. Render and inspect a Mermaid dependency graph when dependencies exist; state independence explicitly when they do not.

Maintain a clean current plan. Integrate changes into the owning `issue.md` entries and ticket sections, synchronize references and dependencies, and remove superseded proposed work. Keep interview chronology, patches, changelogs, override addenda, review reports, and cleanup commentary out of these canonical sections. Preserve review/repair decisions and essential evidence in `issue.log.md`, not Git history or conversation-only records.

## 5. Rehearse the handoff and review the whole set

Check the plan without implementing it. Resolve the source references, distinguish planned code locations from existing code, and walk the dependency order. At each ticket, can an unfamiliar implementer obtain its required context and inputs, know what to change under the approved design, and determine completion without a hidden decision? Can the intermediate result support the next ticket? Does the whole set cover the approved change and its macro-flow verification?

Read [reviewer-prompt.md](reviewer-prompt.md) and dispatch a fresh independent read-only reviewer. Supply the complete index and every ticket at an identifiable snapshot, TICKETS.md, the selected approved source package and its approval evidence, relevant repository evidence, current planning-verification results, and previous findings when applicable. Do not pass the author's working conversation, private reasoning, or instructions to endorse the split. A role switch in the author's context is not independent review.

Include the target repository/checkout and work identity, governing owners `split-tickets` and `workflow-artifacts`, and complete current standards/reviewer instructions or their verified resolved installed locations. Mark skill loading reference-only and the assignment independent read-only review, not ticket planning. Include WORKFLOW-ARTIFACTS.md, the current entry/log references, exact source/set identities, and applicable exclusion evidence. Before dispatch, persist planning or repair decisions and fresh evidence in `issue.log.md`; never postpone records until approval.

Require a complete `Pass`, `Changes required`, or `Blocked` result identifying the current set. Missing reviewer access or evidence, a stale report, or an inconsistent result is not a pass. Retain `Draft` and obtain the necessary independent assessment rather than substituting author self-review.

Persist every returned report in `issue.log.md` before repairs or gate changes, with stable finding IDs, actual verdict and category coverage, exact reviewed source/set revisions, and prior dispositions. Authors record addressed findings as awaiting review; only the reviewer confirms closure or withdrawal. Update `issue.md` before a blocker or handoff with current basis, open findings, evidence, roles, and next action.

Repair findings in the canonical tickets and index. Return any exposed production-design gap upstream rather than hiding it in a repair. Then dispatch a fresh full-set review, including regressions outside the original findings. Repeat until all applicable criteria pass with no unresolved findings or blockers. If progress stalls, report the unresolved decision or access need; iteration count does not waive the standard.

## 6. Obtain final human approval and stop

An independent `Pass` for the unchanged current set permits `Awaiting approval`. Present the index, ticket objectives and granularity, dependencies, necessary decomposition tradeoffs, and macro-flow verification ownership. Ask explicitly whether the human approves this reviewed set for later implementation.

Wait. Approval of the upstream source package, a proposed split, or a repair is not final approval of the reviewed ticket set. Integrate requested changes, repeat full independent review, and ask for final approval of the resulting set.

Use `Approved` only when the same current set has both a passing review and explicit final human approval. Content or relevant baseline changes invalidate those approvals; approval-metadata updates alone do not. On resumption, always review the complete set before an approved handoff; an unchanged set may retain its established final human approval after passing the current review.

Persist explicit final human approval with its exact scope/basis and faithful decision evidence in `issue.log.md`; update `issue.md` before handoff. Return that approved index and essential references, then stop. Set approval is not ticket execution or completion, and a ticket's prerequisites still determine when it can start. If blocked, return the draft and its precise blocker, not an approved handoff. Planning-only work creates no `delivery.md`. Do not design or run the later implementation/TDD or post-implementation change-governance workflow here.
