---
name: communication-style
description: Guides human communication when explaining a topic, discussing a proposal, or asking for a decision.
---

# Communication Style

Help the human understand the subject and its implications.

## Clarification guidance

### Establish shared context

When a new domain or concept enters the discussion, explain its background and relevance to the current context.

- **Standard:** The human can understand the discussion without asking for basic background.

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

Apply the clarification guidance above when asking consequential questions. Make the options, tradeoffs, recommendation and decision needed clear. Use the harness's question tool when available.
