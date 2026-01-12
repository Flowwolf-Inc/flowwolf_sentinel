# High-Level Architecture & Design: The Frappe Intent Stack

**Version**: 9.3 (Agentic Core)
**Pattern**: Agentic Micro-Monolith with Governance

## 1. System Topology

We utilize Frappe's natively integrated stack to deliver a seamless AI experience.

| Layer | Component | Role |
| :--- | :--- | :--- |
| **Interface** | **Frappe UI** | Client Portal & Admin Desk |
| **Logic (Apps)** | **Cortex / Fluent / Motion** | Segregated Brain / Perceptor / Actor |
| **Governance** | **Decision Contracts** | The "Constitution" for the AI Agents |
| **Memory** | **ChromaDB + MariaDB** | Vector Semantic + Relational Transactional |

---

## 2. The Application Triad (Detailed Design)

### App 1: `Cortex_AG_AI` (The Brain)
*   **Role**: Cognition & Governance.
*   **Key Logic**:
    *   `IntentParser`: Extracts meaning from signals.
    *   `GovernanceEngine`: Checks `Decision Contracts` before allowing execution.

### App 2: `Fluent_AG_AI` (The Translator)
*   **Role**: Perception.
*   **Key Logic**:
    *   `UniversalIngestor`: Detects signal type (X12 vs Email) and routes it.

### App 3: `Motion_AG_AI` (The Body)
*   **Role**: Execution.
*   **Key Logic**:
    *   `WorkflowEngine`: Creates the actual loads/invoices in the database.

---

## 3. The Data Flow Pipeline (The "Intent Loop")

```mermaid
sequenceDiagram
    participant Partner
    participant Fluent
    participant Cortex
    participant Motion
    participant DB

    Partner->>Fluent: Sends Signal (EDI/Email)
    Fluent->>Cortex: Request: "Extract Intent"
    
    activate Cortex
    Cortex->>DB: Load "Intent Graph" & "Partner Memory"
    Cortex->>Cortex: Parse Intent (ShipGoods)
    Cortex->>Cortex: Resolve Entities (Fuzzy Match)
    Cortex->>Cortex: CHECK GOVERNANCE (Contract OK?)
    Cortex-->>Motion: "Approved Intent: ShipGoods"
    deactivate Cortex
    
    Motion->>DB: Execute (Create Load)
```

## 4. Why This Wins

1.  **Safety First**: The `GovernanceEngine` ensures no AI hallucination can bankrupt the company.
2.  **Protocol Agnostic**: Swapping EDI for API requires ZERO changes to the `Cortex` or `Motion` layers.
3.  **Unified Memory**: History informs every decision.
