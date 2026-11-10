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

When a new domain or concept enters the discussion, explain its background and relevance to the current context.

- **Standard:** The receiver can understand the discussion without asking for basic background.

### Explain with diagrams where appropriate

Use diagrams when they make the subject easier to understand; use tables to compare alternatives.

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
