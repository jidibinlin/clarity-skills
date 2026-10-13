---
name: ask-with-context
description: Prepare consequential questions with enough context for the user to decide, then continue unresolved decisions.
---

# Ask With Context

Help the user make the next useful decision. Adapt the explanation to their demonstrated understanding.

## Find the next decision

Start from the task, confirmed choices and remaining uncertainty. Inspect accessible repository facts yourself. Treat existing code as the current implementation, not authority over an approved target.

Ask about choices that change the requirement, design or a meaningful tradeoff. Use project conventions and your judgment for ordinary execution details. Choose a question whose prerequisites are settled; independent questions can be grouped.

## Required question format and pre-send check

Make three things clear before asking:

- **Context and impact:** the concrete situation, relevant facts and confirmed choices, and why the remaining choice matters.
- **Options and tradeoffs:** viable alternatives, their consequences and your recommendation.
- **Decision needed:** the specific judgment needed to proceed.

Use the user's language. Supply enough background to decide without another round of basic explanation; keep familiar, simple choices brief.

Use the harness's `ask`/question tool when available, following its instructions. Put supporting explanation and visuals before the question widget. Otherwise ask in text.

## Make relationships visible

Use diagrams when flow, timing, ownership or topology is easier to understand visually; use tables to compare alternatives. Keep the view focused on the decision and check Mermaid with available tooling. Explain the deciding rationale rather than repeating the visual.

## Incorporate the answer and continue

Apply the answer, update dependent choices and continue with the next ready question or investigation in the same turn. Revisit settled decisions when their basis changes, not merely because old code differs.

A request for explanation leaves the decision open. Keep unconfirmed proposals in conversation; the owning workflow handles confirmation and document writes. When decisions are settled, return to that workflow's next step. Pause for a real dependency, a user-requested pause or completed work—not simply because one question was answered.
