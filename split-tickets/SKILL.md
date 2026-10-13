---
name: split-tickets
description: Use to decompose an approved design or change package into implementation tickets, or revise its global ticket set. Not for production design or execution.
---

# Split Tickets

Turn the approved scope into useful increments that a fresh implementer can understand, implement, verify and repair within one working context.

Read [TICKETS.md](TICKETS.md) for generation and review criteria, and registered `artifact-layout` for storage. Load `review-records` when recording or recovering review work and `ask-with-context` for substantive human questions. Resolve references through their registered owners and local files relative to this skill.

## 1. Recover the approved basis

Resolve child inputs to root `issue.md`. Read the selected approved package and inspect relevant code, callers and verification facilities. Distinguish completed obligations, remaining work and unresolved design. Existing code informs planning; it does not override approved requirements or design.

Keep one root ticket set, including cross-child work. A bounded whole-change direct route goes to `implement` without artificial tickets. Return missing design to its owning stage rather than deciding it in the plan.

## 2. Derive increments and dependencies

Follow the approved owner/caller paths. Group changes into useful resulting states, keeping inseparable contract changes and caller updates together. Split independent objectives when that reduces the reasoning needed for each unit.

For each increment, identify the source/code context, concrete outputs it consumes, what it makes usable and how completion will be checked. Size the ticket for the whole implementation-and-repair cycle, not a file or token quota. Assign integration and every selected whole-flow test to the ticket that establishes the necessary collaboration.

Map each dependency to a required output and reason. Rehearse the dependency order: at every step, ask whether the implementer has enough context and whether the prerequisite outputs really support the next result.

## 3. Confirm, write and rehearse the set

Prepare the root index and tickets using TICKETS.md. Before writing specification content, show the exact proposed content or patch and obtain explicit human confirmation. If the proposal or its basis changes, renew that confirmation. Keep unconfirmed proposals in conversation, not candidate files.

Write the confirmed set, resolve its references and inspect the dependency diagram against the actual prerequisites. Walk the set again as a fresh implementer and check that the final composition covers the approved scope. Planning assigns future implementation and testing; it does not require executing them.

When resuming a set with implementation-owned fact updates, use TICKETS.md's **Authority and evidence validity** criteria to separate those facts from plan changes.

## 4. Review, repair and approve

Use [reviewer-prompt.md](reviewer-prompt.md) with the complete set, approved sources and planning evidence. Retain the original author and independent reviewer through repairs. Record findings, repair decisions and review outcomes under `review-records`; the reviewer determines whether findings are resolved.

The original author repairs plan defects through the same confirmation gate, then returns the current set to the same reviewer. Resolve missing inputs or refer source-design defects upstream. Repeat until Pass, then present the reviewed plan for explicit human approval.

Return the approved root index and essential references. Plan approval does not itself authorize implementation, commits or release.
