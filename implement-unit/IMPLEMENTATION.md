# Unit Implementation: Conformance and Evidence Standard

Approved sources—not reviewer taste—own production design. This standard defines source validity, code/test/runtime quality and delivery content. SKILL.md owns the unit's retained-pair execution loop. `artifact-layout` owns artifact paths, names, purposes and ownership; SKILL.md owns write permission and approval validity. Record-schema loading is controlled by the stage's actual record gate, not this content standard. Controller-only composition criteria live in registered `implement`'s ORCHESTRATION.md; reading this standard does not import that owner's workflow.

## Executable basis

A unit has one authorized route:

- **Ticket:** one ticket from an independently passing, finally human-approved root set, with relevant index baseline/dependency/coverage entries and exact applicable approved sources. The basis is flat requirements plus complete technical design, a complete heavyweight package, or an approved change package. A ticket cannot supply missing design.
- **Direct change:** the entire independently passing, finally human-approved change model and essential references, including synchronized affected canonical sections approved together. Its path/revision identifies the unit. Root `issue.md` remains necessary; synthetic tickets, ticket indices and set approvals do not.

For heavyweight work, resolve children to the root-selected package: shared/child requirements composed and approved before architecture, approved architecture before child technical designs, and all complete approved technical models for selected scope and real prerequisites before the single root ticket set. Read applicable cross-child contracts and settled shared realization/ownership, not unrelated future map scope. Separate child Passes or architecture alone cannot prove composition; child entries never create independent ticket pools/controllers/deliveries.

A change basis provides changed requirements and a complete scoped technical target: scope, owners, structure, definitions/contracts, prerequisites, acceptance and local/macro verification. Respect Changed/Unchanged/Unresolved dispositions across macro topology/data/concurrency/sequences, micro topology/sequences, file organization and data/contracts. Unchanged claims require exact readable references or evidenced scoped reconstruction; necessary unresolved decisions block execution. Distinguish observed legacy behavior, confirmed requirements and unknowns. Complete approved current change evidence requires no invented historical models or approvals.

**Bounded direct fit:** one pair can implement and assess the entire target through verification and repair in a bounded context, with actual physical prerequisites, identified affected owners/callers/cutovers and executable acceptance, local, macro-flow and final-conformance obligations. Multiple behavioral increments are fine; unowned remainder or imagined future tickets are not. Separately scheduled dependent units or scope growth return to `clarify-change` for a renewed reviewed/human-approved route, then `split-tickets` if needed. Never narrow scope or fabricate tickets to force fit.

Execution authorization is separate from planning approval. Required evidence includes current source review/approval, repository rules, identified code including dirty/untracked content, and usable incorporated prerequisites. Preserve pre-existing user work; missing applicable evidence blocks work, route-inapplicable absent documents do not. Source identities/selection belong in root definition/navigation and records, not an approval registry. Ticket records use the existing execution block and ticket log defined by `artifact-layout`; direct work uses its sole implementation log, shared with its controller through one assigned writer. Logs or metadata cannot amend specifications.

## First-pass conformance and decision boundary

Implement directly in approved file organization, collaboration, state ownership, definitions, interfaces, algorithms, concurrency and cutover. Preserve reuse, invariant locality, error/resource ownership, quantitative guarantees and factual rationale. Several tests or units may modify one object without inventing extra production files. Minimal means no speculative work—not rough code awaiting redesign, fake results or hard-coded examples.

Local naming, control-flow expression and non-semantic simplification are engineering choices only where the approved responsibilities, behavior and constraints remain intact. New/moved responsibilities, objects, files, design-bearing operations, representations, coordination or compatibility mechanisms require an approved basis. Inspect existing equivalents and actual contracts before adding concepts; missed reuse or incompatible duplication is an upstream design issue.

Business rules go to `clarify-requirements`, global guarantees to `clarify-architecture`, local/shared realization to `clarify-technical-design`, decomposition to `split-tickets`. Changes to approved models, change-basis conflicts and post-delivery design go through `clarify-change`'s coordinated package, not fictitious replay of the original pipeline. These destinations require stage authorization; children cannot override parent authority. Renew affected review/approval and synchronize canonical sources/indices/tickets through confirmed writes before relying on the new basis. Originating findings link the resolution instead of copying design discussions.

Honor the approved usable intermediate state, update required callers and remove paths obsolete under this unit's atomic cutover. Internal increments need not be independently deployed or expose the whole feature. Preserve later-owned work and unrelated user changes; direct changes complete their entire target.

## Tests that earn their maintenance cost

Inspect project guidance, runner, nearby tests, fixtures and environment; reuse established means and locations. Test behavior through approved interfaces at the scope able to detect the fault—an object operation can be the interface, not just an HTTP endpoint.

Every permanent test needs a plausible consumer-visible failure, an expected outcome independent of implementation and a gap in existing coverage. Prefer distinct behaviors, consequential boundaries, invariants, transitions and specified errors. No coverage/method quotas, exhaustive matrices or tests for every mechanical edit. Control inputs/state and cleanup for deterministic isolation without mocking away the collaboration under test.

Assert promised results, permitted state or meaningful effects. Incidental wiring, private structure, arbitrary call counts, incidental snapshots, source-text checks, copied constants, mock echoes and expectations repeating implementation logic do not earn maintenance. Interaction/ordering assertions are useful only when contractually observable. Remove tautological or implementation-coupled tests rather than refreshing their incidental expectations; replace with meaningful coverage where needed.

Use real owned collaborators for collaboration under test. Explain justified external substitutes and their limits: a mocked store does not prove persistence or cross-process atomicity. Mocking convenience cannot authorize production abstractions, dependencies or ownership changes; necessary production-design changes return upstream.

## Behavioral red/green and alternatives

For uncovered new/changed behavior, select one meaningful contract test, run it before implementation and observe a failure attributable to the target behavior; implement in approved owners, then run it and relevant nearby checks for green. Choose subsequent behaviors from actual gaps, not a speculative full matrix. Fixture/service/unrelated compilation failures are not behavioral red. A missing declaration can explain initial compile failure, but establish assertion sensitivity once the interface is exercisable; compile-only scaffolding is not a completed increment.

Reuse existing failing tests. User-supplied failures are already observed evidence and need not be rerun solely for confirmation. For behavior-preserving work, use meaningful before/after regressions and exercise the changed path without inventing a failure for unchanged behavior. If reliable automation is infeasible, state the concrete limitation and exercise a suitable direct scenario without claiming automated TDD. Mandatory tests/flows are still mandatory. Green proves its assertions, not design conformance or unrelated behavior.

## Runtime and regression evidence

Use project commands for changed behavior, contracts and callers: applicable static, meaningful targeted/regression checks and the normal suite required by project guidance at handoff. Missing mandatory portions block Pass; narrow substitutes do not waive them. Distinguish evidenced pre-existing failures from change-caused failures, state limits and preserve unrelated code. Do not suppress failures to manufacture success.

Exercise the actual changed surface: a real CLI invocation/output/state, interaction with the actual UI, or a library caller/integration scenario. Compilation and isolated mocks are insufficient. Existing real-flow tests may supply evidence without duplicate runs. Disposable probes may fill gaps without permanent low-value tests; retain observations and remove probes. Mandatory unverified visual/runtime outcomes block Pass.

Implement and execute every assigned macro-flow test with prescribed real participants and substitution limits, including cross-child collaboration. Missing participants/setup blocks Pass. Tickets exclude only explicitly later-owned flows; direct units own every selected flow and final combined conformance across owners, contracts, callers, state/resources and cutovers. A sum of local Passes cannot establish whole-set conformance.

Bind actual evidence to source/code identity and environment. After repairs renew affected checks; prior evidence remains applicable only with explicit unchanged relevant code, configuration, participants and environment. Changed contracts/callers/state/integration invalidate affected unit and combined evidence immediately, including while a metadata correction waits for confirmation. Preserve unaffected evidence with a reasoned impact basis, not blanket reruns or stale status labels.

## Review coverage

Assess complete current changes and sufficient surrounding implementations/callers, not only a diff or prior failing lines. Necessary interactions matter; an unrelated repository-wide architecture audit does not. Findings require an approved obligation, repository rule, acceptance condition or execution criterion here, plus actual location/evidence and consequence—not personal design/style taste.

Classify findings as **implementation violation** (usable basis, nonconforming result), **upstream defect** (contradictory, incomplete or insufficient source/ticket) or **unavailable evidence** (specific missing check/input and unblock condition). Review reports cover:

1. **Approved executable basis:** route, authorization/approvals, repository rules, code identity and incorporated prerequisites.
2. **Structural conformance:** organization, ownership, reuse/locality, collaboration and cutover.
3. **Behavioral conformance:** definitions/contracts, algorithms, errors/resources, concurrency and outcomes.
4. **Test value and execution:** meaningful tests, red/green or justified alternatives, isolation and substitution limits.
5. **Runtime and integration evidence:** required runtime/regressions and correct ticket-local/full-change scope.
6. **Complete reviewable handoff:** current callers/tests/documentation, retired obsolete paths/probes, evidence identities and artifact integrity. Required diagrams in affected specifications must actually be rendered and visually inspected; source validity and complete content cannot be inferred from parsing or status labels.

The same criteria govern construction and review. A direct full-change Pass is final independent review; it does not need another overall reviewer. A ticket Pass remains local. Human acceptance is separate from either verdict.

## Delivery content and storage

The whole-work controller, or standalone unit author, writes one root `delivery.md` **after** mandatory verification and the applicable independent Pass. Its absence before Pass is not a defect. Delegated units and children return evidence to the controller without separate summaries or per-unit acceptance gates. A standalone ticket states only its reviewed scope and preserves any broader existing summary.

The clean current summary contains:

- Delivered scope and exclusions; actual final design with authoritative source links.
- Maintenance-relevant decisions and basis, explicitly surfacing consequential autonomous repair decisions with finding/record links.
- Actual checks and independent review against exact source/code identities, real/substituted participants, environment and limits.
- Necessary operational, configuration and migration guidance.
- `Awaiting acceptance`, or the evidenced explicit final human acceptance with exact reviewed scope/basis and owning record reference.

Acceptance records belong in the owning implementation log; summary links may navigate to them, but `issue.md` remains definition/navigation and links only the delivery. An exact root navigation patch still requires prior human confirmation. Any normative specification change embedded in delivery also uses that gate; delivery is not a way to invent or override design.

Necessary existing documentation is updated in place, with specification writes confirmed; disposable probes are removed and private evidence retained. Conformance repairs renew affected evidence/review and update the summary before renewed acceptance. Later separately authorized changes have their own work identity/summary while synchronized canonical models remain authoritative. Keep artifacts local and excluded. Acceptance alone authorizes no deletion, publication, commit, merge, push, tracker closure or release; external publication needs explicit content and destination authorization.
