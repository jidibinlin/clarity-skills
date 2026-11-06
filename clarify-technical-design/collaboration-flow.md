# Multi-designer Collaboration

This example has two independent groups, A and B.
Group C depends on their confirmed designs.
The roadmap marks a coordination point requiring both A and B before group C starts.

The leader develops the Design Alignment Roadmap with the human and records it in `issue.md`.
Each designer is a separate AI agent with its own human-facing conversation.
Each designer clarifies directly with the human and writes confirmed content.
The human chooses the alignment order and initiates coordination.
The leader then reads and revises the affected models directly with the human.

```mermaid
sequenceDiagram
    actor H as Human
    participant L as Leader
    participant A as Designer A
    participant B as Designer B
    participant C as Designer C
    participant R as Reviewer

    L->>H: Clarify macro design, groups and dependencies
    L->>H: Present the Design Alignment Roadmap
    H->>L: Confirm macro basis and roadmap for writing
    L->>L: Write the roadmap into issue.md

    Note over H,B: A and B may prepare independently<br/>The human chooses the alignment order

    H->>L: Start groups A and B
    L->>A: Create human-facing agent and assign group A
    L->>B: Create human-facing agent and assign group B

    loop Until group A's design is complete
        A->>H: Present the proposal and open questions
        H->>A: Give feedback and adjustments
    end
    A->>H: Present the complete proposal for writing
    H->>A: Confirm and authorize writing
    A->>A: Write the group A model

    loop Until group B's design is complete
        B->>H: Present the proposal and open questions
        H->>B: Give feedback and adjustments
    end
    B->>H: Present the complete proposal for writing
    H->>B: Confirm and authorize writing
    B->>B: Write the group B model

    H->>L: Check the roadmap for ready coordination points
    L->>L: Check the required group designs
    Note over L,B: A and B are complete, confirmed and written<br/>The leader takes over coordination revisions
    L->>L: Read A and B models<br/>Identify conflicts and coupling

    opt Cross-group changes are needed
        loop Until coordinated changes are clear
            L->>H: Present conflicts and proposed changes
            H->>L: Give feedback and adjustments
        end
        L->>H: Show exact changes and target files
        H->>L: Confirm and authorize writing
        L->>L: Update affected group models<br/>Reconcile global content and references
    end

    opt Clarification dependencies change
        L->>H: Present the revised Design Alignment Roadmap
        H->>L: Confirm the revised roadmap for writing
        L->>L: Update the roadmap in issue.md
    end

    L->>L: Check integration and downstream prerequisites
    Note over L,C: C's prerequisites are confirmed and written<br/>Blocking issues are resolved

    H->>L: Start group C
    L->>C: Create human-facing agent with upstream models

    loop Until group C's design is complete
        C->>H: Present the proposal and open questions
        H->>C: Give feedback and adjustments
    end
    C->>H: Present the complete proposal for writing
    H->>C: Confirm and authorize writing
    C->>C: Write the group C model

    H->>L: Complete whole-model coordination
    L->>L: Read required models<br/>Resolve remaining changes with the human

    L->>R: Submit the complete model
    loop While changes are required
        R->>L: Return findings
        L->>H: Present repairs and target files
        H->>L: Confirm and authorize writing
        L->>L: Repair the affected model files
        L->>R: Submit the revised complete model
    end
    R->>L: Pass
    L->>H: Request whole-model approval
    H->>L: Approve the complete technical model
```

Designers do not report completion to the leader.
The human initiates coordination; the leader revises affected models after confirmation.
Scouts remain available to their creators for factual consultation throughout the process.
