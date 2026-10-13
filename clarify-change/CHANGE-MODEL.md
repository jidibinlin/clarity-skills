# Change Model: Authoring and Review Standard

Content and evidence for a transition from an evidenced system to a completely decided scoped target, including changed requirements and technical decisions. Small scope reduces volume, not precision. The consuming stage owns execution, write permission and approval validity; `artifact-layout` owns artifact paths, names, purposes and ownership. Record-schema loading is controlled by the stage's actual record gate, not this content standard.

## Purpose and governing design standard

Read these sections, with subsections, directly from registered `clarify-technical-design`'s `TECHNICAL-MODEL.md` before constructing or reviewing the target:

- **Approved basis and decision rationale**.
- **File organization and responsibility tree**.
- **Macro runtime and collaboration model**.
- **Micro object and collaboration model**.
- **Complete data-structure definitions**.
- **Complete interface contracts**.
- **Overall workflow integration test plan**.
- **Consistency, evidence, and clean integration**.

They supply technical completeness, concrete-confirmation evidence, dependency reasoning, first-pass constraints, limited flow planning, and current verification. When existing architecture governs affected work, also read applicable `ARCHITECTURE-MODEL.md` criteria from registered `clarify-architecture`; for affected decomposition in `wayfinder.md`, read applicable `WAYFINDER-MODEL.md` criteria from registered `wayfinder`. Tentative estimates remain subordinate to formal models. These conditional imports do not apply merely because the skills exist.

Resolve resources relative to their registered owners or reuse intact current supplied content. Imports do not load owner SKILLs, workflows, or historical prerequisites. Missing necessary sources/evidence block work; missing historical models do not. This package may supply confirmed requirements and the complete target directly, with current review and human approval, without retrospective approvals or mandatory heavyweight conversion. Existing applicable authority still constrains it.

## Evidenced baseline and scope

Identify the request, affected behavior/participants, source/code identities (including dirty/untracked changes), external contracts, and investigation/change boundaries. Existing effort/child references resolve through their governing root. Inspect applicable models/map references, repository rules, code/callers, data/interfaces, configuration, tests, and runtime paths; include necessary interactions and preserved guarantees, not automatic whole-project redesign.

| Prior documentation | Required evidence |
| --- | --- |
| Reliable | Affected content checked against the system; exact references for applicable unchanged definitions/views. |
| Partial or stale | Concrete divergence and reconstruction of missing/unreliable affected content; neither document nor code automatically wins an intent dispute. |
| Absent | Sufficient reconstructed current behavior, macro collaboration, micro ownership, files, and contracts in this package; no empty stand-ins or unrelated models. |

Trace concrete scenarios across boundaries rather than inferring behavior from directories. Attribute claims to inspection, execution, external contracts, or human decisions. A read-through is not runtime observation; test source is not a passing run. Supplied failures are evidence, not a reason to rerun for confirmation. Necessary uncertain behavior/feasibility needs safe permitted investigation, not speculation.

Historical defects and incidental constraints are not automatically target requirements. State what is preserved, corrected, replaced, or excluded, without silent unrelated repairs. Identify any inaccessible evidence necessary to establish affected behavior, ownership, contracts, or feasibility and its consequence.

## Requirements and decision rationale

Define desired scenarios, rules, constraints, exclusions, and observable acceptance outcomes, distinguishing changed requirements from preserved guarantees, including meaningful failures and concurrency. A technical-only change still identifies unchanged obligations and evidence. Ordinary bounded behavior clarification belongs in this package, not an invented historical requirements stage.

Apply imported decision rationale and concrete-convergence evidence. Explain changed/failed premises; valid settled decisions need not be re-interrogated. Existing behavior is evidence, not automatic intent. Affected macro decisions precede dependent micro design, which follows affected module foundations upward. Valid unchanged foundations need not be redesigned. Concrete structures, interfaces, topology, and sequences require their own applicable confirmation/reuse basis.

## Mandatory change assessment and complete targets

Every dimension below is assessed as **Changed**, **Unchanged**, or **Unresolved**, with concrete scope and basis. Changed identifies transformation and complete target. Unchanged identifies a verified target reference/description and preservation rationale. Unresolved remains conversational and blocks readiness; it is not a placeholder row admitted to the model. Written assessments need exact human confirmation under the stage's write gate.

| Dimension | Owning technical section |
| --- | --- |
| Macro topology | Macro runtime and collaboration model — Topology |
| Data flow and state authority | Macro runtime and collaboration model — Data flow and state authority |
| Concurrency and completion | Macro runtime and collaboration model — Concurrency and ordering |
| Macro sequences and flows | Macro runtime and collaboration model — Sequences |
| Micro topology and ownership | Micro object and collaboration model — Topology and ownership |
| Micro sequences and operations | Micro object and collaboration model — Sequences and operations |
| File organization | File organization and responsibility tree |
| Data and interface contracts | Complete data-structure definitions; Complete interface contracts |

Apply full content criteria to every target, not merely its label. Macro/micro Mermaid topologies and sequences, complete target file tree, data definitions, and contracts remain mandatory. Unchanged topology proves nothing alone about ordering, ownership, payloads, or behavior. A mechanism's absence is an evidenced fact, not an omitted view; a single process or no-concurrency claim still needs a concrete execution model.

Current views explain the transformation and are reconstructed when reliable sources are absent. Separate current and target when mixing them implies incompatible states or false ordering. Checked exact unchanged references avoid mechanical redraws; silence is not evidence of no impact. An unfamiliar reader must recover the complete scoped target without replaying amendments or conversation.

## Reuse, consolidation, migration, and exit

Assess the resulting concept set, not just added lines. Explain whether affected concepts retain, absorb, merge, move, or replace responsibilities. New requirements alone do not justify layers, adapters, files, or second representations.

Migrations/replacements identify final owners, affected callers and stored/transferred data, transition constraints, conversion/ordering/cutover feasibility, and obsolete-path exit. A compatibility interval needs a real requirement and explicit retirement/completion conditions, not indefinite parallel paths. No generic rollback/retry framework is implied.

No affected invariant is unclaimed, truth duplicated, or obsolete path left without an exit. Keep this bounded to the authorized change rather than unrelated structural cleanup.

## Verification and execution readiness

The imported flow plan covers changed behavior and consequential preserved collaboration using inspected real project means. Identify valid existing coverage and necessary revisions/additions; do not introduce another test standard or exhaustive TDD design.

Current verification covers unchanged claims, baseline-to-target mappings, callers, migrations, and canonical references as well as changed views. Reused diagrams need rendering and visual-inspection evidence applicable to their exact content. Missing mandatory evidence blocks readiness; future production tests need not already exist or pass.

Route rationale covers the whole understanding, implementation, verification, and repair scope, with settled owners, prerequisites, observable acceptance outcomes, and local/macro verification. A direct change fits one coherent implementation context; independent meaningful increments, real dependencies, or excessive combined reasoning require decomposition. Patch size or a route label alone establishes neither.

## Canonical synchronization and authority

Each target concept has one current authority. Existing canonical requirements, architecture, technical models, and decomposition references contain integrated confirmed changes with superseded rules removed and views/references synchronized. The change model explains transition and precisely references resulting targets; it is not an override layer. Necessary surrounding and cross-child context accompanies affected sections in one coordinated scoped package.

Impact is explicit across contracts, callers, descendants, tickets, integration flows, approvals, unit/combined evidence, and acceptance. Source identities, scope, coverage, dependencies, and links remain consistent. Preservation of unaffected work has an actual basis; impact does not automatically restart every child/ticket. Changed premises invalidate affected evidence semantically even if metadata has not yet caught up. Target approval does not make existing code conforming or renew implementation evidence.

Without older models, this package is the complete scoped authority. Future work consumes the latest integrated target, not a chain of change notes. A later broader canonical model absorbs definitions and becomes their referenced authority instead of adding competing targets.

Before/after explanations, factual evidence, and decisive rationale accompany affected concepts. Entries provide source navigation, not approval or progress registries. Review records identify decisions and approvals, not competing design authority. An approved unimplemented target may coexist with old code; a code conformance defect is not a reason to change the specification to excuse it.

## Delivery criteria

Apply all local/imported obligations; these categories index coverage:

1. Evidenced affected baseline, explicit drift/gaps, no invented history or accidental requirement promotion.
2. Changed/preserved outcomes, bounded scope, decisive rationale, and concrete confirmation/reuse evidence.
3. Justified macro assessments and complete topology, flow/state, concurrency, and sequence targets.
4. Justified micro/file assessments and complete ownership, operation/sequence, and responsibility targets.
5. Complete resulting data/interfaces, semantics, callers, and checked unchanged references.
6. Justified concept reuse/consolidation, migrations/final owners, and obsolete-path exits.
7. One synchronized authoritative target with current source scope and precise downstream impact.
8. Current mandatory verification, owned flow coverage/prerequisites, scoped invalidation, and justified executable route.
9. Attributable current source and confirmation/reuse evidence.

Approval of this target is neither historical approval nor completed implementation.
