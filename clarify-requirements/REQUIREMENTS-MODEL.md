# Requirements and Domain Model: Content Standard

These criteria guide both construction and review of standalone, child and composite requirements. Import this resource through the installed `clarify-requirements` owner without invoking its workflow.

## Scope and domain meaning

The model explains the problem, affected actors, intended outcomes and selected scope. Existing/preserved, new and changed behavior are distinguishable, along with external responsibilities and exclusions. Confirmed target decisions take precedence over observed legacy behavior.

Concepts and relationships explain the rules: ownership, meaningful distinctions, relevant states and transitions. Behavior has clear triggers, conditions and observable outcomes, including consequential boundaries and failures. Material business choices are resolved rather than left for an implementer to guess.

Imposed technical constraints belong here when they affect the requirements; acknowledging a project constraint does not require specification of every implementation detail.

## Coherent domain flows

Related concepts, behavior and rules form a coherent account of who acts, what happens and why. Confirmed refinements are integrated into their owning sections. The model is a clean current account, not accumulated interview rounds or patch notes, and is understandable without the conversation.

### Local acceptance

Each substantive requirement has visibly labeled **Acceptance criteria** in its owning section. They state observable results under the relevant conditions, preserving meaningful boundaries and failure outcomes. Cross-flow acceptance belongs with the end-to-end flow; a detached checklist does not replace local acceptance.

### Background, rationale and precision

Background and rationale are proportionate to what the reader needs to understand the decision. Consequential choices have their actual basis and relevant constraints, with accessible source references where needed. Facts, preferences and decisions are distinguishable. Numbers, conditions and exceptions retain their intended meaning.

## Mermaid views and evidence

Mermaid views explain material flows, relationships and scope. They agree with the prose, distinguish changed and preserved behavior, and make external responsibilities clear. Branches and arrows have understandable meanings; normal and exceptional paths reflect the actual rules.

Required views have current rendered output and visual-inspection evidence. Readable, semantically accurate diagrams matter, not merely valid syntax.

## Shared and child requirements

Root requirements own shared meanings, cross-child rules and end-to-end flows. Children own complete scoped detail and reference applicable root definitions. Each decision has a clear owner; a requirements boundary need not match a module or ticket.

The selected package links actual root/child source sections and explains how they compose. Its outcomes can be followed across child boundaries without gaps or conflicting rules. Each child meets the applicable content standard. A local child verdict does not establish package consistency.

## Authorization and evidence validity

Specification content has human confirmation before it is written; candidate content remains in conversation. The original author and independent original reviewer carry repairs through to Pass. Findings and repair decisions are recorded using `review-records`.

Review and final human approval concern the current result. Final approval is distinct from write consent and does not authorize the next stage. `artifact-layout` owns workspace and artifact conventions.

## Review coverage

The whole selected scope is faithful to confirmed intent, coherent, verifiable through local acceptance, and usable for the next modeling stage. Its diagrams and decision basis support that account. Composite review includes the shared rules and cross-child behavior, not just individual child quality.
