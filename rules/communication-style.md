# Communication Style

Help the receiver understand the subject and its implications.

## Do not use question or option-selection tools

Never use the harness's question or option-selection tools.
This ban applies to all human communication.
It is not limited to asking for decisions.

Use ordinary chat instead.
Let the human reply in their own words.

## Clarification guidance

### Establish shared context

A familiar topic does not mean a shared understanding of the problem.

Give enough context before proposing action or asking for a decision:
- What is the current situation?
- What is happening?
- What should happen instead?
- Why does the difference matter?
- Why does your recommendation fit this situation?

Explain unfamiliar concepts when needed.
Focus on the actual situation, not just general background.

Do not assume the receiver shares your understanding.
Do not leave essential context for them to uncover through repeated questions.

**Standard:** The receiver can understand the problem and why you recommend the proposed action.

### Explain with diagrams first

When a subject has structure, relationships, flow, sequence, state or other visual organization, prefer a diagram as the primary explanation. Use prose to provide context, rationale, implications and details that the diagram cannot convey.

Use Mermaid for these diagrams where it can express the required view. Use tables to compare alternatives.

| What to explain | Suggested view |
| --- | --- |
| Steps, conditions and branches | Mermaid `flowchart` |
| Call order, messages and asynchronous interaction | Mermaid `sequenceDiagram` |
| Lifecycles and state transitions | Mermaid `stateDiagram-v2` |
| Types, inheritance and composition | Mermaid `classDiagram` |
| Entity relationships and cardinality | Mermaid `erDiagram` |
| System structure, layers and topology | Mermaid `block-beta`; `flowchart` for simple node connections |
| Cloud services, resources and deployment groups | Mermaid `architecture-beta` |
| Benefits, costs and constraints | Comparison table |

Prefer the agent-provided Mermaid tool to render and validate diagrams. If unavailable, report the limit rather than looking for Chrome or a separate Mermaid MCP. Explain the key implications alongside the diagram.

## Ask when human judgment is needed

Apply the clarification guidance above when asking consequential questions. Make the options, tradeoffs, recommendation and decision needed clear.
