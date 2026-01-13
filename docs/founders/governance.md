---
title: "Governance Framework"
tags: []
version: "9.1"
last_updated: "2026-01-13"
---

# Governance Framework: The Constitution of Autonomy

**Version**: 9.3 (Agentic Core)
**Context**: Defining the "Safety Rails" for Flowwolf Autonomous.

## 1. The Necessity of Governance
You cannot sell "Autonomous AI" to an enterprise without "Guaranteed Safety".
An AI that auto-accepts a $1M load because it "hallucinated" a low rate is a liability.
**Governance is not a constraint; it is a feature.**

## 2. Decision Contracts (The "Laws")

A **Decision Contract** is a DocType that explicitly defines the boundaries of an autonomous agent's power.

### Structure
*   **Scope**: "Carrier Onboarding" OR "Load Tendering".
*   **Partner Group**: "Trusted Tier 1", "New / Probation".
*   **Constraints**:
    *   `max_transaction_value`: e.g., $2,000.
    *   `min_confidence_score`: e.g., 95%.
    *   `required_entities`: ["Shipper", "Consignee", "Rate"].
*   **Action**: "Auto-Approve", "Hold for Review", "Reject".

### Example Contract: "Tier 1 Automatic Tender"
> *If Partner is 'Tier 1' AND Load Value < $1500 AND Confidence > 98% -> AUTO APPROVE.*

## 3. The Progressive Trust Model (The "Career Path")

Agents (and Partners) must earn their autonomy.

1.  **Level 1: Sandbox (Shadow Mode)**
    *   AI processes the document but takes NO action.
    *   Result is logged as "Simulation".
    *   Human does the work manually.
    *   System compares AI vs Human to grade accuracy.

2.  **Level 2: Copilot (Assisted Mode)**
    *   AI prepares the draft.
    *   Human reviews and clicks "Submit".
    *   System learns from any edits.

3.  **Level 3: Conditional Autonomy**
    *   AI executes automatically IF within "Safe" Decision Contracts.
    *   Outliers go to Human.

4.  **Level 4: High Autonomy**
    *   AI executes 95% of traffic.
    *   AI auto-negotiates minor exceptions (e.g., date shifts).

## 4. The Audit Trail (Decision Narrative)

Every autonomous action generates an immutable **Decision Narrative** log:
*   **Trigger**: "Received 204 from Walmart".
*   **Evidence**: "Confidence 99% based on history".
*   **Contract**: "Matched Contract #T1-Auto".
*   **Outcome**: "Created Load #L-1001".

This enables "Forensic Debugging": *Why did the AI do that?*

---
**Summary**: Governance builds Trust. Trust enables Autonomy. Autonomy creates Value.

---

## 5. Data Privacy & Federation Protocol

To address Enterprise concerns about the "Global Graph", we implement specific Privacy Seals.

### A. The "Private by Default" Rule
*   All data stays in `Local Memory` (Tenant Isolated) by default.
*   No "Customer Specific" data (Rates, Volumes, Partner Names) is EVER shared.

### B. The "Public Fact" Promotion Protocol
Information is ONLY promoted to `Global Memory` if:
1.  It is a **Public Entity** (e.g., "Amazon Warehouse CLT4").
2.  It has been independently verified by **5 Separate Tenants**.
3.  It passes the **PII Scrubber** (No names, phones, emails).

### C. The Opt-Out Clause
*   Tenants can check "Isolation Mode" in settings. They will read from Global Graph but contribute nothing. (Freeloader penalty: Lower Trust Score).

---

## 6. Saturn Reliability Hooks (v9.1)

Safety isn't just about stopping bad actions; it's about *surviving* them and *proving* what happened.

### A. Immutable Traceability (The Black Box Recorder)
Every Database Transaction in `Motion` must link back to a `Governance Trace ID`.
*   **Trace Chain**: `D-Transaction` -> `D-Decision Contract` -> `D-Intent` -> `D-Raw Signal`.
*   **Audit Promise**: "Show me every decision regarding Load #1001" -> Returns the exact EDI Segment, the Vector Search score, and the Policy Check result.
*   **Tech**: Stored in a dedicated immutable `Audit Log` DocType (or specializedAppend-Only DB).

### B. The "Time Travel" Replay
*   **Concept**: Since we store `Raw Signal` and `Software Version` (Commit Hash), we can re-run any past event.
*   **Use Case**: A bug in v9.1 caused a wrong mapping.
    1.  Fix bug in v9.1.
    2.  Select all affected Intents.
    3.  **Replay Integration**: Re-process Raw Signal -> Intent using v9.1 logic.
    4.  Auto-correct the downstream data.

### C. Dead Letter Jail
*   **Policy**: No data is ever deleted.
*   **Mechanism**: If a signal fails parsing/validation 3 times, it moves to `Dead Letter Jail`.
    *   It does NOT clog the queue.
    *   It alerts a human "Warden".
    *   Human can "Fix & Flush" (edit raw -> retry) or "Ignite" (delete).

---

## 7. Autonomy Enablement (v9.1)

### A. The Intent Life-Cycle
The `Intent Graph` tracks the state of every desire:
1.  **Draft**: Raw signal parsed.
2.  **Proposed**: Agent suggests a plan.
3.  **Negotiating**: A2A protocol active (Counter-offers).
4.  **Contracted**: Locked by Decision Contract.
5.  **Executed**: Written to `Motion` database.

### B. The "Safety Mode" (AI Override)
Just as a Tesla creates a "Force Field" preventing a driver from steering into a wall, `Cortex` creates a Safety Field around `Motion`.
*   **Mechanism**: Before *any* write to `Motion`, the `Policy Engine` runs a final check.
*   **Result**: It is mathematically impossible for a user (Human OR AI) to violate a Critical Policy (e.g., "Review Required").

### C. Transparency Reports for Investors
*   **Metric**: "Autonomous Miles".
*   **Definition**: % of Shipment Lifecycle steps managed without human touch.
*   **Dashboard**: Real-time view of `Sandbox` vs `Autonomous` volume to prove the "Ramping Trust" curve.

---

## 8. Economic Primitives (v9.1)

To monetize Autonomy (as requested by Sales/Investors), we need to meter "Value", not "Volume".

### A. The "Decision Meter"
*   **Metric**: `autonomous_decisions`.
*   **Definition**: A count of every time an Agent executes an Intent *without* human intervention.
*   **Pricing**: $0.10 per Decision.

### B. The "Skill Marketplace"
*   **Concept**: If a 3rd party dev builds a "Customs Skill", they can charge for it.
*   **Mechanism**:
    *   `Skill Usage` is tracked in the Ledger.
    *   RevShare: 70% to Dev, 30% to Platform.

### C. Isolation Guarantees (The "Vault")
*   **Promise**: "Your data trains YOUR Personal Agent, and anonymized patterns train the GLOBAL Agent. But Competitor X never sees your data."
*   **Tech**: **Tenant-Key Encryption**. Every tenant's Vector Store partition is encrypted with a unique key.

---

## 9. The Constitutional Protection (v9.1)

This framework is the "Constitution" of the system.
**It cannot be changed by Engineering.** It can only be amended by the **Governance Committee** (CTO + Head of Trust).

### The Prime Directive: "Do No Harm"
*   If an Agent's action violates a Decision Contract, the action is blocked.
*   If the Network is down, the system defaults to "Safety Mode" (Manual Only).
*   If an Extension Plugin crashes, the Core isolates it and continues.

### The Code Freeze Pact
*   **Core Logic (`Cortex`)** changes require:
    1.  RFC (Request for Comments).
    2.  Red Team Review.
    3.  Formal Governance Vote.
    4.  Audited Deployment.

---

## 10. Mode-Aware Governance (v9.1 Patch)

Decision Contracts must be granular enough to handle different Transport Modes.

### The "Mode" Selector
Every `Decision Contract` DocType has a `mode_filter` field.
*   **Example 1**: "Auto-Approve FTL"
    *   `mode_filter`: ["FTL", "LTL"]
    *   `max_value`: $2,000
    *   `action`: APPROVE
*   **Example 2**: "Review Air Freight"
    *   `mode_filter`: ["AIR"]
    *   `max_value`: $0 (Review All)
    *   `action`: REVIEW

**Why**: Air Freight is "Premium/Emergency". It almost always requires human eyes, whereas LTL is routine.

## 11. Operational Autonomy Governance (v9.1 Upgrade)

### A. The "Partner Signal Profile" (Behavioral Contract)
The Intent Library defines *what* is extracted. The **Signal Profile** defines *how* we treat the sender.
*   **Attached To**: `Partner` (CRM).
*   **Fields**:
    *   `trust_score`: 0-100 (Dynamic).
    *   `data_quality_score`: 0-100 (Historical accuracy).
    *   `preferred_channel`: e.g., "EDI 204", "Email PDF".
    *   **`autonomy_ceiling`**: Enum (0-5). Max allowed level.

### B. The Execution Formula
A standard `Decision Contract` is static. The new formula encompasses dynamic trust:

> **Execution Decision** = `Intent Confidence` × `Partner Trust` × `Autonomy Ceiling`

**Logic**:
*   If `Autonomy Ceiling` < `Intent Level`: **DOWNGRADE** to Manual Review.
*   If `Partner Trust` < 80%: **BLOCK** Level 4 Execution.

### C. The Autonomy Levels
| Level | Capability | Constraint |
| :--- | :--- | :--- |
| **0** | Observe | Read-Only. No updates. |
| **1** | Extract | Parse to Draft. Human must Save. |
| **2** | Suggest | Parse & Draft Logic. Human must Submit. |
| **3** | Auto-Confirm | Executed if Confidence > 99%. |
| **4** | Auto-Execute | Executed if Confidence > 90%. |
| **5** | Negotiate | A2A Counter-offers allowed. |

**Verdict**: This ensures high-trust partners scale fast, while low-trust signals (like random emails) are naturally gated.

## 12. Execution Intermediaries (v9.1 Patch)

### The "No Raw Writes" Policy
*   **Rule**: A raw `Intent` instance cannot write to the `Motion` database.
*   **Mechanism**: The Intent must "Hire" an Agent.
    *   `Intent(#123)` -> `Calls` -> `AgentContract(ShipmentBookingAgent)`
    *   The **Agent** holds the Write Permission. The **Intent** holds the Instruction.
*   **Benefit**: If we need to rollback a transaction, we reverse the *Agent's Actions*, which are auditable.
## Compliance Matrix (v9.1)
| Standard | Status |
| :--- | :--- |
| SOC‑2 | ✅ |
| ISO‑27001 | ✅ |
| GDPR | ✅ |

## Execution Intermediaries (No Raw Writes)
* **Rule**: A raw `Intent` instance cannot write directly to the `Motion` database.
* **Mechanism**: The Intent must *hire* an `AgentContract` which holds write permissions.
* **Benefit**: Enables audit‑able rollbacks and guarantees that all writes are mediated by an agent.

---

## Partner Signal Profile - Default Values (GAP-I2 Fix)

### Default Profile (New Partners)

When a new partner is onboarded, initialize with conservative defaults:

```python
DEFAULT_PARTNER_SIGNAL_PROFILE = {
    "trust_score": 0.50,           # Neutral (50%)
    "data_quality_score": 0.50,    # Neutral (50%)
    "autonomy_ceiling": 1,          # Level 1 (Assist) - most conservative
    "preferred_channel": "API",     # Modern default
    "preferred_format": "JSON",     # Modern default
    "require_human_review": True,   # Manual review required initially
    "circuit_breaker_threshold": 10 # Trip after 10 failures
}
```

### Bootstrapping Strategy

**Option 1: Conservative Start** (Recommended)
- Start all partners at Level 1
- Require 30 days of clean history to upgrade to Level 2
- Require 90 days to reach Level 3+

**Option 2: Historical Data Bootstrap**
- If migrating from legacy EDI system with history:
  ```python
  def bootstrap_from_history(partner_edi_logs):
      """Analyze historical EDI to set initial trust score."""
      total = len(partner_edi_logs)
      errors = count_errors(partner_edi_logs)
      error_rate = errors / total
      
      if error_rate < 0.01:  # < 1% errors
          return {"trust_score": 0.90, "autonomy_ceiling": 3}
      elif error_rate < 0.05:  # < 5% errors
          return {"trust_score": 0.75, "autonomy_ceiling": 2}
      else:
          return DEFAULT_PARTNER_SIGNAL_PROFILE
  ```

### Trust Score Decay

Trust degrades if partner stops sending signals (inactivity):

```python
def apply_decay(profile: PartnerSignalProfile):
    """Decay trust_score for inactive partners."""
    days_since_last_signal = (now() - profile.last_signal_at).days
    
    if days_since_last_signal > 90:
        profile.trust_score *= 0.9   # 10% decay after 90 days
        profile.save()
```

---

**Status**: Partner Signal Profile defaults defined.