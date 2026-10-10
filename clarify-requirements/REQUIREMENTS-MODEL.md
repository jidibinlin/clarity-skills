# Requirements and Domain Model: Delivery Standard

This standard belongs to the `clarify-requirements` skill. Load that skill by name in reference-only mode when another stage needs this resource; use its resolved companion location or complete current supplied content under the `workflow-artifacts` loading rules. Reading this standard does not start its author's workflow or require that workflow's execution prerequisites. The consuming stage determines the authorized scope and role; actual stage execution retains its existing gates.

## Purpose and scope

Produce a requirements and domain model that both a human reviewer and an implementing agent can use without reconstructing the original conversation. It defines what behavior is correct before deciding how to implement it.

This is the shared authoring and review standard for the first stage of the lightweight workflow. Apply it throughout clarification and model construction, not just at the delivery gate. Independent review uses these same criteria. It also applies when a future heavyweight workflow delegates a bounded question with existing decisions and constraints. Reuse applicable prior decisions; clarify only what is missing, ambiguous, or contradictory.

The model covers one bounded requirement or change. Reference established project knowledge instead of redescribing the whole system. Domain modeling clarifies the requirement through concepts, relationships, rules, and examples; it is not limited to a glossary and does not require inventing a concept for every noun.

All skill instructions and companion standards are written in English. This language convention does not require the human conversation to be in English.

## Private location and persistent process records

Load `workflow-artifacts` by name through the Skill tool or the harness's equivalent registered resource mechanism and read its companion `WORKFLOW-ARTIFACTS.md` under its resource-resolution and supplied-content reuse rules before authoring, resuming, or reviewing. It governs private placement, exclusion, persistent records, revision identity, recovery, and transitions in addition to this content standard. New models use `.scratch/<work-slug>/requirements.md` in the same work directory as `issue.md` and `issue.log.md`; existing authoritative project models may remain precisely referenced and synchronized under its location rule. The author/controller must establish and verify local Git exclusion before workflow writes, including worktree-aware exclusion resolution and tracked-file blocking. Never stage, commit, or publish workflow records; planning creates no `delivery.md`.

Use `issue.md` for current stage, scope/route, model and approval references, blockers, roles, and next action. Resume from it, applicable models, open findings, and latest evidence/decisions, reconciling actual sources before reuse. The controller (author in standalone mode) saves read-only reviewer reports in `issue.log.md`; reviewers do not write logs or exclusion rules. Record each round/reviewer, standards, exact source/model/code basis, verdict, category coverage, evidence/limits, stable finding IDs, and independent dispositions. Private files need path plus digest or another verifiable local revision; repository HEAD alone cannot identify ignored models or dirty/untracked code. Identify every relevant source and preserve enough evidence to compare current content without pretending logs are snapshots.

Persist reviews before repair or gate advancement; repair decisions, material rationale, addressed IDs and fresh evidence before new review; dispositions/current state before handoff; and recovery data before blockers or session/stage transitions. Author repairs are `addressed, awaiting review`, not self-closed findings; disputes remain open with counter-evidence until independent disposition. Save explicit human approval with exact scope/basis and a faithful short quotation or durable reference to the actual decision. Preserve prior outcomes and current applicability in the log, with only current approval metadata in the model. Apply the shared metadata-only revision rule. Task dispatches may carry review packages, but essential identities, decisions, findings, and evidence must persist locally.

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

Update the model as conclusions emerge rather than reconstructing it from a long conversation at the end. The deliverable must remain one clean, integrated account of the current requirement.

**Hard rule: no normative document patches or model-embedded change logs.** Never append or create patch files, revision histories, dated update notes, override documents, or addenda that repair or supersede the main text. A reader must not combine a base document with later corrections to discover current rules. This applies during drafting and final delivery. The required `issue.log.md` is a process record, never a normative patch or a substitute for integrated model sections; private artifact history is not kept in Git.

Apply each change directly to the sections that own the affected concepts and rules. Update dependent scenarios, references, and diagrams in the same revision; remove obsolete or conflicting statements. If inherited material already contains patches or a change log, integrate the still-applicable decisions into the main text and remove the patch material. If their authority is unclear, ask about the specific conflict before choosing which rule to preserve.

Keep current proposals, assumptions, and unresolved questions distinct from confirmed conclusions. Necessary rationale, meaningful rejected alternatives, and descriptions of current versus desired behavior belong beside the relevant decision; they are not a license to preserve a chronological discussion or revision log. Maintain only the current approval status and applicable approval note, not an accumulating approval history. Apply the review and approval gate below whenever reviewed content changes; downstream work must not silently override confirmed decisions.

Keep editing instructions and cleanup commentary out of the model: no patch-deletion lists, rewrite narratives, or accounts of invalidated approvals. Record material maintenance decisions and review applicability in `issue.log.md`, not conversation alone. Show current approval status and remove obsolete approval notes from the model while preserving historical outcomes in the log. Mention previous behavior only when necessary to understand the requirement or a real migration constraint.

Essential knowledge for the next stage must not exist only in the current agent's context. At a handoff, the model and its explicit references must carry that knowledge.

## Delivery check and first approval gate

This gate governs full requirements-model authoring through clarify-requirements. For scoped changes to an existing system, the `clarify-change` skill (load by name in reference-only mode to consult its standard; execute only when that route is authorized) governs the coordinated change-package route: integrate affected requirements and technical targets in their canonical sections and review/approve that package together with necessary surrounding consistency. Prior approval does not cover changed content, but this route does not require separate repeated whole-project requirements and technical ceremonies or nonexistent historical approvals. Unaffected content is not falsely reapproved.

Before asking for approval, an independent reviewer in a fresh context must check the complete current model against the confirmed discussion, inherited constraints, and inspected evidence. The author supplies evidence and repairs findings; author self-review cannot satisfy this gate. Use [reviewer-prompt.md](reviewer-prompt.md) for the review input and return contract. Apply these criteria:

1. **Faithfulness:** important confirmed requirements are neither omitted, weakened, nor expanded without agreement. Pay particular attention to numbers, ordering, prohibitions, and exceptions.
2. **Clarity and structure:** different implementers should not have to guess at material business choices or infer them from vague wording. The model makes the main flow and concept relationships understandable, with connected explanations rather than terminology piles or a chronological discussion log.
3. **Consistency and clean integration:** concepts, rules, scenarios, and diagrams agree. Current facts and desired changes are distinguishable. The canonical text incorporates every applicable correction; no patch, changelog, revision log, override addendum, or obsolete conflicting rule remains in the deliverable.
4. **Verifiability:** concrete scenarios or observable conditions can establish whether the key rules hold.
5. **Reviewability:** background-dependent points contain enough context and actual rationale for a human to assess them. Sources and inherited decisions are accessible where needed.
6. **Handoff completeness:** an agent unfamiliar with the conversation can understand the requirement from the model and its explicit references.
7. **Diagram verification:** Mermaid diagrams have been rendered and inspected, and their conditions, paths, terminology, and scope match the prose. Report any verification limitation.
8. **Open questions:** no unresolved question or unverified assumption silently determines a material behavior. Questions that prevent technical modeling from proceeding must be resolved before this stage is complete.
9. **Private record integrity:** required location and verified exclusion, recovery entry, source/revision identities, persistent review/repair/evidence records, stable finding dispositions, and applicable approval evidence satisfy WORKFLOW-ARTIFACTS.md. Assess records available at this gate; do not require the current review result or future human approval before they occur.

Fix findings in the canonical model, persist repairs and fresh evidence in `issue.log.md`, then dispatch a fresh independent reviewer to assess all applicable checks, previous findings, and regressions. Save each result before advancing. Recover omitted information from available discussion/evidence before asking new questions. Keep findings and repair reports in the sidecar log, not the clean model or conversation alone.

A review passes only with an independent `Pass` for the current artifact: all applicable criteria are satisfied, no findings remain unresolved, and required verification has actually been completed. `Changes required` and `Blocked` do not permit approval. An unavailable independent reviewer, necessary evidence, or mandatory check is a blocker, not a waived criterion. Disclosing a limitation or receiving early human approval does not turn an incomplete review into a pass.

Use `Draft` while clarifying, repairing, or blocked on review or verification. Use `Awaiting approval` only after the current model passes review. Use `Approved` only after the human explicitly approves that reviewed model. Agreement with interview answers or proposed fixes does not satisfy the final approval gate.

An edit to requirement content, diagrams, or required references invalidates the previous review and final approval for that artifact. Return to `Draft`, review and repair until passing, and obtain approval of the resulting model. Approval-metadata updates alone do not invalidate a content review. A resumed document must be reviewed against this standard even if it already says `Approved`; an unchanged document may retain its established final approval after passing that review. Never infer review success from its status label.

Do not begin technical clarification or present an approved handoff until both review and final human confirmation have succeeded for the current model. If blocked, report the draft and its specific blocker instead.

The initial lightweight modeling/planning workflow has separate human approval gates for requirements, technical design, and tickets; approval at one gate does not approve later artifacts or code. The scoped change-package route above can instead hand a complete approved bounded change directly to implementation without tickets. Both routes still require independent review and explicit human approval of their current governing design.
