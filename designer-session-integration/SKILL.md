---
name: designer-session-integration
description: Use when writing, adapting or testing a start-designer-session skill for a user's harness and client.
---

# Designer Session Integration

Register the user's implementation as `start-designer-session`. The leader calls that skill, not this guide, when assigning a group.

## Implement the handoff

- **Input:** Accept the group name, workspace and existing assignment from the leader. Start the designer in that workspace with the assignment; the launcher does not choose groups or make design decisions.
- **Ready:** Verify that the designer received the assignment and that the human's chosen client provides a writable entry to that same live session. Return the group name and where to enter it. The designer must stay online after the launch returns, including while waiting for a reply or while the human works with another group.
- **Blocked:** Identify the group and the blocker. Distinguish “not started” from “started, but access could not be verified.” A saved conversation, a read-only view or messages relayed by the leader do not complete the handoff.

## Test from the human's client

Start two independent groups. After the launcher returns, reply directly to A, switch to B and reply there, then return to A. Check that each designer received its own reply and that A is still the original live session; reopening a transcript in a new process is not a pass.

Exercise an unavailable host and an unreachable entry after launch. The reported outcome should distinguish those failures without claiming either group is ready.
