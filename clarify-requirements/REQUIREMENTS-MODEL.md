# Requirements and Domain Model: Content Standard

This standard defines content and evidence for standalone, child and composite requirements. It is not an execution protocol and imports no other workflow. Read it completely before constructing or reviewing requirements; importing stages resolve it directly through the actual installed `clarify-requirements` owner. The owning stage governs writes, review and approval; `artifact-layout` defines file locations and ownership, never the meaning of requirements.

## Scope and domain meaning

Explain correct behavior so an unfamiliar reader can understand the selected scope without reconstructing the conversation. Reuse established project knowledge and confirmed decisions; distinguish current facts from desired behavior. Model semantic relationships, not a glossary or a concept for every noun.

Cover the following where applicable, without compulsory empty headings:

- **Problem and outcome:** affected actors, initiating situations and observable improvement.
- **Scope:** distinct new/changed behavior, existing behavior to preserve, external participants/capabilities and dependencies, and explicitly excluded work. Existing code proves current behavior, not authority for desired behavior.
- **Concepts and relationships:** meanings, distinctions, ownership and relationships necessary to interpret behavior, using established vocabulary consistently.
- **Rules and behavior:** triggers, preconditions, results, invariants, prohibitions, constraints, exceptions and real lifecycle states/transitions.
- **Acceptance:** observable satisfaction of every substantive requirement, with consequential normal, boundary and failure scenarios.
- **Decisions and evidence:** confirmed choices, proportionate background, actual rationale and retrievable original basis. No material choice or unverified assumption may silently determine behavior.

Externally imposed technical constraints belong here when they affect requirements. Private modules, algorithms, storage and code organization belong to technical modeling. Business choices exposed by technical investigation still belong to their requirements owner.

## Coherent domain flows

Organize related concepts, behavior and rules into an account of who acts, on what, how concepts relate, what happens next and why the rules apply. Introduce vocabulary in context; state meaningful ownership, cardinality and lifecycle relationships rather than inventing unknown ones. An unfamiliar reader must be able to explain the flow, not merely recognize terms. Diagrams cannot repair fragmented prose.

Integrate later conclusions into these owning sections, synchronizing rules, scenarios, references and views and removing superseded conflicts. The model is current integrated authority, not interview rounds, patch appendices, change logs or cleanup commentary. Prior behavior belongs only where it explains the requirement or a real migration constraint. Essential handoff knowledge must be in the model or its exact references, not private agent context.

### Local acceptance

Every substantive requirement has a visible **Acceptance criteria** label/subheading (or document-language equivalent) in its owning body section. State relevant preconditions/actions and observable expected results there, using concise prose, bullets or a local table. Unlabeled examples or ordinary prose alone are insufficient; no form is required for every sentence.

Keep explanatory and acceptance scenarios beside their rules; cross-flow acceptance belongs beside its end-to-end flow. Preserve meaningful boundaries, numbers and failure outcomes. A detached acceptance checklist, final acceptance chapter, appendix or standalone ledger is not an alternative, even with backlinks or duplicated local conditions. IDs support navigation; they never replace local acceptance.

### Background, rationale and precision

Lead with the conclusion, then supply the background needed to assess it. Self-contained points need only precision and examples preventing likely misunderstanding. Background-dependent rules need the relevant concepts/current behavior/constraints or exact references explaining their relevance. Consequential or counterintuitive choices need problem context, decisive constraints, actual basis and, when necessary, the principal rejected alternative and accepted consequences. Explain shared background once and link it; depth follows reader dependence, not discussion length.

Distinguish observed facts, human preferences and decisions. Attribute non-self-contained facts to retrievable repository, external or human evidence. Generic claims of simplicity, flexibility or best practice are not a decision basis. Missing rationale must be recovered from original evidence, not retrospectively invented. Unconfirmed assumptions and choices stay in conversation with their owner and blocked scope until resolved.

Retain numbers, units, ordering guarantees, prohibitions, exceptions and conditions. Stable headings and references must lead to comprehensible rules, not reference chains with no conclusion.

## Mermaid views and evidence

Use accurate Mermaid to show material flows and explicit scope distinctions. Choose flowcharts for decisions/actions/outcomes, state diagrams for real lifecycles, sequences for interactions/ordering and scope/relationship views for boundaries/dependencies. Use applicable forms only; one view may serve several purposes without inventing a workflow or lifecycle.

- **Meaning:** defined terms, meaningful branch conditions and explicit arrow semantics. Do not silently mix chronology, control flow, ownership and dependency. Show required success, rejection, failure and termination paths without speculative recovery.
- **Reachability:** connect nodes/branches to rules and scenarios. Normal behavior must remain reachable without optional concurrent actions or exceptions. Separate exceptional interactions when combining them would imply a false prerequisite.
- **Scope:** visibly distinguish changed, preserved, externally supplied and excluded behavior. External steps identify their owner and exclusion from this implementation. Model business participants rather than unconfirmed technical modules.
- **Readability:** a clear subject and reading scope, overview/detail only where useful, no color-only distinction or unreadable/redundant giant view. Prose provides precision, rationale and exceptions without narrating every arrow.
- **Evidence:** every required current diagram has actually rendered output and visual-inspection evidence covering labels, structure, readability and semantic agreement with prose. Parsing alone is insufficient; missing rendering or visual inspection is a gate blocker.

A partial draft view describes only its confirmed scope. Missing paths remain delivery obligations, not permission to record speculative answers.

## Shared and child requirements

For heavyweight work, root requirements own shared meanings, cross-child rules and end-to-end business flows; children own complete scoped details and cite applicable root definitions. Each decision has one owner. A child is a modeling boundary, not necessarily a module or ticket.

Compose rather than concatenate: the root explains relationships and delegates detail by exact child path/section and verifiable source identity. Every delegated obligation must exist, be accessible and have an unambiguous owner. Directory links, future-detail promises and reference chains without rules do not establish coverage. Each child retains the full applicable content and diagram standard.

The selected package must trace every outcome and consequential cross-child scenario through its owning rules. Reconcile vocabulary, lifecycle meanings, preconditions/results, ordering, exceptions, gaps, overlaps and ownership. Include cross-child flow/scope views linked to detail where needed. Children must obey shared rules, and their composition must be able to realize them. A child-only verdict is local; package consistency covers all selected sources and real prerequisites, not unrelated future ideas.

## Review coverage

Assess the complete current assignment against these categories; a heading alone is not evidence:

1. **Faithfulness and scope:** original requirements and precise changed/preserved/external/excluded boundaries.
2. **Clarity:** coherent domain flows and meaningful relationships.
3. **Consistency:** agreeing concepts, rules, scenarios, diagrams and clean current authorities.
4. **Verifiability:** explicit local acceptance for every substantive requirement.
5. **Reviewability:** proportionate background, actual rationale and accessible original evidence.
6. **Handoff completeness:** usable without the conversation; no unresolved material choice or unverified assumption blocking the next modeling stage.
7. **Diagrams:** semantic accuracy, scope clarity and current rendered/visual evidence.
8. **Artifact integrity:** attributable current sources, exact identities and unambiguous content ownership.
9. **Composite consistency, when applicable:** the complete selected package satisfies **Shared and child requirements**; child-only review does not claim package approval.
