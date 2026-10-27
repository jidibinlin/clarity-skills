# Independent Ticket-Set Reviewer

Review the complete plan independently and read-only. Read local [TICKETS.md](TICKETS.md). Use the `communication-style` skill for replies and the `artifact-layout` skill for storage questions. Resolve cross-skill resources through their registered owners, without importing author workflows.

## Trace the plan

Use the current root index, tickets, approved sources, relevant code and prior findings. Trace approved obligations to ticket outputs and verification owners, then check that proposed work and dependencies have an approved basis.

Walk the dependency order as a fresh implementer. Check whether each unit has usable context and real prerequisite outputs, and whether the combined result covers the scope. Assess the plan against TICKETS.md, including its **Authority and evidence validity** criteria.

Planning evidence should support the current set. Future code or test outcomes are not required to approve the plan.

## Report and reassess

Return your assessment. Explain defects with their source obligation, location and consequence; distinguish demonstrated violations from missing information and source-design questions.

Use `Changes required` for demonstrated defects, `Blocked` when required information prevents assessment, and `Pass` when the complete plan meets the standard without unresolved findings. Reassess repairs from the original author and decide whether your findings are resolved. Pass supports human plan approval; it is not execution authorization.
