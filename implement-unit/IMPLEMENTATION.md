# Unit Implementation Standard

This standard guides implementation and independent review. SKILL.md supplies the unit workflow; registered `code-review` supplies the reviewer method. Read TESTING.md from registered `tdd` for shared test criteria. Registered `implement`'s ORCHESTRATION.md covers whole-work composition; `artifact-layout` and `review-records` own storage and records.

## Executable basis

Implementation requires explicit execution authorization and a current reviewed, human-approved basis:

- **Ticket:** one ticket from the approved root set, its applicable requirements/design or change package, and usable prerequisites. Its scope includes assigned verification and respects later-owned work.
- **Direct change:** the entire approved bounded change and its essential references. One implementer/reviewer pair must be able to complete the target, including combined verification. It needs no synthetic tickets.

Use the selected root package and relevant shared contracts for cross-child work. The basis must settle the behavior, production structure, interfaces, ownership and acceptance needed for execution. Ordinary engineering choices within that design are autonomous; models need not prescribe statements line by line. A concrete design contradiction or missing consequential decision returns to its source authority, with approved-source changes handled through `clarify-change`.

## Execution facts exception

During authorized implementation, the assigned execution writer may automatically update four kinds of facts inside an existing approved ticket's execution block: **current status, factual blocker, actual implementer/reviewer handles, and evidence references**.

Support these facts with actual dispatch/execution evidence, citing the owning log where applicable. Initial implementing status and actual handles need no fabricated log event. Updates retain the original-pair rules; recording a handle does not appoint a replacement. A passing status requires the saved independent Pass and current mandatory evidence, not an author's claim that findings are closed.

This exception does not change the approved scope, design, acceptance, verification, dependencies or source selection. Separate facts from specification changes in a mixed patch. Once the evidence-backed handoff and actual prerequisites are satisfied, the controller may continue authorized dependent work without per-ticket human approval.

## Authorization and evidence validity

Specification changes require explicit human confirmation of the displayed change **before writing**. Confirmation applies to that content and basis, not unseen follow-on decisions. Execution facts above and ordinary code repairs do not require another confirmation. Final human acceptance is a separate decision about the reviewed result.

Evidence must identify the current source/code and actual result, with material environment or verification limits. Renew affected evidence when the implementation or approved basis changes; preserve evidence that remains applicable.

Review is independent and belongs to the original reviewer, with repairs by the original implementer. If a role is genuinely unavailable, recover or replace that role with its context and findings preserved. Findings remain open until the reviewer resolves them. Pass requires current mandatory evidence and no unresolved findings or blockers.

## Implementation and verification quality

The result conforms to the approved behavior and production design, follows repository conventions and preserves unrelated user work. Complete the authorized cutover across affected owners, callers, tests and documentation. Local cleanup and test organization are engineering choices; changes to approved structure, interfaces or ownership require an approved basis.

Run applicable project static checks, behavioral/regression tests and required suites. Exercise the actual changed surface and every assigned macro flow with the required participants. Compilation or isolated mocks cannot establish unexercised runtime behavior. Tickets own their assigned flows; direct changes own the complete combined result.

Report actual outcomes and limits, distinguishing pre-existing failures from regressions. Missing mandatory verification blocks Pass. Evidence already exercising the required real flow can be reused; duplicate runs and permanent low-value tests are unnecessary.

## Review coverage

Assess the current scope and relevant surrounding code across the executable basis, structural and behavioral conformance, test value/execution, runtime/integration evidence and complete handoff. Findings connect an obligation to an observed defect and consequence, not reviewer preference.

Distinguish **implementation violations**, **upstream defects** and **unavailable evidence** so the response reaches the right owner. Ticket Pass is local; direct full-change Pass is final independent review, not human acceptance.

## Delivery content and storage

After verification and independent Pass, the controller or standalone author writes the root `delivery.md`. It describes delivered scope, authoritative design, consequential decisions, actual checks and limits, operational guidance and acceptance status. Delegated units return evidence to the controller rather than creating separate deliveries.

Final acceptance is explicit and recorded for the reviewed scope. A standalone ticket claims only its authorized scope. Delivery or acceptance does not itself authorize publication, commit, merge or release.
