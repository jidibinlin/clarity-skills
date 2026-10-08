# Requirements and Domain Model: Delivery Standard

## Purpose and scope

Produce a requirements and domain model that both a human reviewer and an implementing agent can use without reconstructing the original conversation. It defines what behavior is correct before deciding how to implement it.

This is the delivery standard for the first stage of the lightweight workflow. It is also intended to apply when a future heavyweight workflow delegates a bounded question with existing decisions and constraints. Reuse applicable prior decisions; clarify only what is missing, ambiguous, or contradictory.

The model covers one bounded requirement or change. Reference established project knowledge instead of redescribing the whole system. Domain modeling clarifies the requirement through concepts, relationships, rules, and examples; it is not limited to a glossary and does not require inventing a concept for every noun.

All skill instructions and companion standards are written in English. This language convention does not require the human conversation to be in English.

## Required coverage

Cover the following wherever they apply. These are coverage obligations, not mandatory headings or a form to fill with invented content.

- **Problem and outcome:** who encounters the problem, in what situation, and what observable improvement is needed.
- **Scope:** what this change includes and excludes, what existing behavior must remain unchanged, and which external participants or capabilities it depends on.
- **Concepts and relationships:** the meanings, distinctions, relationships, and ownership needed to interpret the requirement. Reuse established terms with the same meaning.
- **Behavior and rules:** triggers, preconditions, expected results, constraints, invariants, exceptions, and prohibited behavior. Include states and transitions where the requirement has a lifecycle.
- **Concrete scenarios:** examples that establish the expected behavior, including relevant normal, boundary, and failure cases. Scenarios must make important rules verifiable, not merely restate that the feature works.
- **Decisions and unresolved questions:** confirmed choices, their necessary rationale, and the facts or choices still missing. Explain the effect of an unresolved question on the rest of the model.

Separate observed current behavior from required future behavior. The existing code is evidence of the former, not automatic authority for the latter. Investigate facts available in the repository or other accessible sources rather than asking the human to retrieve them.

Keep this model independent of the implementation proposal. Record externally imposed technical constraints when they affect the requirement, but leave choices of modules, algorithms, storage structures, and private code organization to technical modeling. When technical investigation exposes an unresolved business choice, return that choice to requirements clarification.

## Writing for review and implementation

### Organize by the requirement, not by the conversation

Write a coherent model of the current requirement, not meeting minutes, a chronological decision log, or a succession of question-and-answer summaries. Organize the explanation around the problem, related concepts, behavior, and rules. Integrate later clarifications into the relevant explanation instead of appending another round of notes.

The reader must be able to identify who acts, what they act on, how the relevant concepts relate, what happens next, and which rules govern that behavior without reverse-engineering a list of terms. Explain each material concept through its role and relationships; a glossary of isolated definitions is not sufficient. State ownership, cardinality, or lifecycle relationships when they matter and are known, but leave unknown relationships explicit rather than inventing them.

Introduce necessary vocabulary where readers can understand it. Reuse a precise existing term; add a new term only when it names a meaningful distinction. A cluster of unexplained nouns is not a model. Keep each rule and its essential context together, with links for genuinely shared background.

Mermaid diagrams expose this structure; they do not excuse fragmented prose. During review, check that a reader can explain the main flow and concept relationships from the model, not merely recognize individual terms or follow a record of what was discussed. Preserve the rationale needed to assess a decision, not the chronology of how the conversation reached it.

### Scale explanation to background dependence

Lead with the rule, conclusion, or decision. Then supply the background needed to understand it and the key basis needed to evaluate it. Determine explanation depth from the perspective of the intended reader who did not attend the discussion, not from what the current agent remembers.

| Background dependence | Required treatment |
| --- | --- |
| Low: understandable on its own | State the point precisely. Add an example if it prevents a likely misunderstanding. |
| Medium: depends on other concepts, existing behavior, or constraints | Explain or link the necessary background and show how it affects this point. |
| High: counterintuitive, crosses several concepts, or involves a consequential tradeoff | Explain the problem context, decisive constraints, chosen conclusion, and key basis. Include the principal rejected alternative and accepted consequences when needed to judge the choice. |

Do not mechanically attach three empty headings to every point. A short statement can be sufficient; a longer explanation earns its place by making the point understandable and reviewable.

Background should establish why the problem arises, what is currently true, and which concepts or limitations matter. Include the information whose absence would cause a reader to misinterpret the point, not the entire history of the discussion.

Explain shared background once and link to it from dependent points. Readers must be able to follow those references without searching the original chat.

### Preserve the actual basis for decisions

For a decision requiring explanation, identify the concrete requirement, constraint, evidence, or explicit human preference that drove it. Where alternatives matter, explain why the chosen option wins and what cost or limitation it accepts.

Generic claims such as "for simplicity," "for flexibility," or "best practice" are not sufficient unless connected to the actual choice and its consequences.

Distinguish the following in the prose:

- **Fact:** identify a retrievable source when the fact is not established in the model itself. Sources can include repository locations, external references, and explicitly attributed human-provided constraints.
- **Decision:** record what was chosen and the real basis for choosing it. A stated human preference is a valid basis; do not manufacture objective evidence for it.
- **Assumption:** mark it as unverified and explain what depends on it.
- **Unresolved question:** state what information or choice is missing. Do not turn it into a default decision to complete a section.

When a decision's rationale is missing, consult the discussion or available evidence first. If the gap still prevents meaningful review, ask the human. Never invent retrospective justification.

### Preserve precision

Retain meaningful numbers, units, ordering guarantees, negative requirements, exceptions, and conditions. Do not weaken a precise requirement into general intent while summarizing it.

Use stable headings or references so diagrams, scenarios, and future implementation tickets can identify the relevant rules. References complement the explanation; they must not become a trail of links with no understandable conclusion.

## Mermaid requirements

Use Mermaid to make requirement flows and scope accurately visible. Choose the diagram form that represents the relationship being described:

- **Flowchart:** triggers, actions, decisions, branches, and outcomes.
- **State diagram:** lifecycle states, transition triggers or guards, and allowed transitions.
- **Sequence diagram:** interactions between participants and relevant ordering.
- **Scope or relationship diagram:** what changes, what remains unchanged, which external participants or dependencies are involved, and what is explicitly excluded. Use clear grouping and labels.

A document does not need every diagram type. Show material flows rather than making readers reconstruct them from prose, and make scope distinctions explicit in an appropriate diagram. One diagram may serve both purposes when it remains clear. Do not invent a lifecycle or workflow for a requirement that has none.

### Semantic accuracy

- Use the same defined terms in diagrams and prose.
- Give decision branches meaningful conditions rather than vague labels such as "check" or "process."
- Make the meaning of arrows clear. Do not silently mix control flow, chronological order, ownership, and dependency.
- Include the success, rejection, failure, and termination paths that the requirement actually calls for. Do not add speculative recovery behavior merely to make a diagram look complete.
- Mark unresolved behavior on the affected path or exclude that path explicitly from the diagram's stated scope. A detached uncertainty note must not leave a path that appears decided.
- Relate key nodes and branches to the corresponding rules, scenarios, or decisions. Walk each concrete scenario through the diagram: ordinary behavior must remain reachable without an optional concurrent action or exception, and a missing answer is not permission to complete a branch. Show exceptional interactions separately when combining them would imply a false prerequisite.

### Scope accuracy

Distinguish new or changed behavior from existing behavior that remains unchanged, externally provided capabilities, and work explicitly excluded from this change. These are different categories, not a single "out of scope" bucket.

External steps may appear when needed to understand the requirement, but their ownership and exclusion from this implementation must be clear. Use business behavior and participants at this stage, not unconfirmed technical modules.

### Readability and consistency

Give each diagram a clear subject and reading scope. Use an overview and focused detail only when complexity warrants it. Avoid both unreadable giant diagrams and redundant diagrams of the same idea. Do not rely on color alone to convey status or scope.

Diagrams explain structure. Prose defines precise rules, background, rationale, and exceptions. Do not narrate every arrow again, and do not treat a diagram label as a complete rule definition.

Whenever a requirement changes, update affected diagrams and prose together. Before delivery, actually render the Mermaid diagrams with an available renderer and inspect them for both rendering errors and misleading structure or labels. Successful parsing alone does not establish semantic correctness. If rendering is unavailable, explicitly report that verification gap rather than claiming the diagrams are verified.

## Maintain the model during clarification

Update the model as conclusions emerge rather than reconstructing it from a long conversation at the end. Preserve the current, coherent understanding, not a transcript or an append-only stream of contradictory decisions.

Keep proposals, assumptions, and unresolved questions distinct from confirmed conclusions. When a conclusion changes, revise affected rules, scenarios, references, and diagrams. Surface a change to an already approved material decision for renewed human confirmation; downstream work must not silently override it.

Essential knowledge for the next stage must not exist only in the current agent's context. At a handoff, the model and its explicit references must carry that knowledge.

## Delivery check and first approval gate

Before asking for approval, check the model against the confirmed discussion, inherited constraints, and inspected evidence:

1. **Faithfulness:** important confirmed requirements are neither omitted, weakened, nor expanded without agreement. Pay particular attention to numbers, ordering, prohibitions, and exceptions.
2. **Clarity and structure:** different implementers should not have to guess at material business choices or infer them from vague wording. The model makes the main flow and concept relationships understandable, with connected explanations rather than terminology piles or a chronological discussion log.
3. **Consistency:** concepts, rules, scenarios, and diagrams agree. Current facts and desired changes are distinguishable.
4. **Verifiability:** concrete scenarios or observable conditions can establish whether the key rules hold.
5. **Reviewability:** background-dependent points contain enough context and actual rationale for a human to assess them. Sources and inherited decisions are accessible where needed.
6. **Handoff completeness:** an agent unfamiliar with the conversation can understand the requirement from the model and its explicit references.
7. **Diagram verification:** Mermaid diagrams have been rendered and inspected, and their conditions, paths, terminology, and scope match the prose. Report any verification limitation.
8. **Open questions:** no unresolved question or unverified assumption silently determines a material behavior. Questions that prevent technical modeling from proceeding must be resolved before this stage is complete.

Fix omissions using existing discussion and evidence before asking new questions. Return to the human only for genuinely missing information or decisions.

Present the model for explicit human confirmation after the delivery check. Answering the interview questions, finishing the document, or the agent declaring it complete is not approval. Do not begin technical clarification until the human confirms this model. If a blocking gap remains, present the model as a draft and identify the gap instead of treating it as an approved handoff.

The lightweight workflow has three separate human approval gates: this requirements/domain model, the technical model, and the implementation tickets. Approval at one gate authorizes the next stage only, not all later stages. This document defines the first gate; the technical-model and ticket delivery standards are separate decisions.
