---
title: "Autonomy Technical Contracts"
tags: []
version: "9.1"
last_updated: "2026-01-12"
---

# Autonomy Technical Contracts

**Purpose**: What the system guarantees at each paid level  
**Audience**: Enterprise buyers, auditors, platform team  
**Status**: Legal & technical specification

---

## The Contract Model

Each tier upgrades **4 contracts** — never all at once:

1. **Decision Authority Contract** (who decides)
2. **Execution Contract** (what runs automatically)
3. **Risk & Override Contract** (how failures are handled)
4. **Audit & Liability Contract** (who is accountable)

**This keeps buyers calm and lawyers quiet.**

---

## 🟩 LEVEL 1 — Visibility Automation

**Autonomy**: 10–15%  
**Promise**: "Nothing happens without you knowing."

### 1️⃣ Decision Authority Contract

```yaml
DecisionMode: OBSERVE_ONLY
```

- System **MAY NOT** make operational decisions
- System **MUST ONLY** observe, normalize, and report
- Humans remain sole decision-makers

### 2️⃣ Execution Contract

```yaml
execution:
  allowed_actions:
    - ingest
    - normalize
    - detect
  forbidden_actions:
    - mutate
    - submit
    - close
```

- Read-only ingestion (EDI, API, files)
- Deterministic normalization
- No write-backs to customer systems

### 3️⃣ Risk & Override Contract

```yaml
RiskProfile: NONE
```

- Zero operational risk
- No rollback required (no mutations)

### 4️⃣ Audit & Liability Contract

```yaml
Liability: CUSTOMER
AuditLevel: FULL_TRACE
```

- Immutable event logs
- Full traceability
- Liability stays entirely with customer

**💰 Why customers pay**: Insight without risk

---

## 🟨 LEVEL 2 — Assisted Execution

**Autonomy**: 25–35%  
**Promise**: "The system acts — but only with approval."

### 1️⃣ Decision Authority Contract

```yaml
DecisionMode: PROPOSE_WITH_APPROVAL
```

- AI may propose decisions
- Human must approve before execution

### 2️⃣ Execution Contract

```yaml
execution:
  requires_approval: true
  reversible: true
```

- Mutations allowed after approval
- Write-backs permitted (invoices, updates)
- Every action is explicitly consented

### 3️⃣ Risk & Override Contract

```yaml
OverrideWindow: OPEN
RollbackRequired: TRUE
```

- Mandatory rollback paths
- Humans can override before and after execution

### 4️⃣ Audit & Liability Contract

```yaml
Liability: SHARED
AuditLevel: DECISION_SIGNED
```

- Approval metadata required
- Signed decision records

**💰 Why customers upgrade**: Labor reduction with control

---

## 🟦 LEVEL 3 — Conditional Autonomy

**Autonomy**: 50–60%  
**Promise**: "It runs — unless something unusual happens."

### 1️⃣ Decision Authority Contract

```yaml
DecisionMode: AUTONOMOUS_WITH_THRESHOLDS
```

- AI executes within confidence thresholds
- Humans only intervene on anomalies

### 2️⃣ Execution Contract

```yaml
execution:
  confidence_threshold: configurable
  auto_execute: true
  anomaly_escalation: mandatory
```

- Auto-execution for known patterns
- Risk-scored decision engine
- Human escalation on outliers

### 3️⃣ Risk & Override Contract

```yaml
OverrideWindow: CONDITIONAL
Rollback: AUTOMATIC_ON_FAILURE
```

- Automatic rollback on confidence breach
- Overrides logged and versioned

### 4️⃣ Audit & Liability Contract

```yaml
Liability: CONDITIONAL_SHARED
AuditLevel: EXPLAINABLE_AI
```

- Explainable decision paths
- Confidence scores stored per action

**💰 Why customers pay more**: Headcount reduction + predictability

---

## 🟪 LEVEL 4 — Cross-Domain Autonomy

**Autonomy**: 70–80%  
**Promise**: "The system optimizes across the business."

### 1️⃣ Decision Authority Contract

```yaml
DecisionMode: MULTI_AGENT_OPTIMIZATION
```

- AI agents coordinate across domains
- Decisions optimized against policies (cost, SLA, risk)

### 2️⃣ Execution Contract

```yaml
execution:
  domains:
    - ops
    - finance
    - carrier
  optimization: enabled
```

- Cross-system mutations allowed
- Economic tradeoffs permitted
- Continuous optimization loops

### 3️⃣ Risk & Override Contract

```yaml
OverrideWindow: POLICY_ONLY
KillSwitch: GLOBAL
```

- Policy-based constraints
- Emergency kill switch
- Strategic overrides only

### 4️⃣ Audit & Liability Contract

```yaml
Liability: PLATFORM_GOVERNED
AuditLevel: POLICY_COMPLIANT
```

- Policy compliance logs
- Governance board review capability

**💰 Why this is platform pricing**: Structural advantage

---

## 🟥 LEVEL 5 — Full Autonomous Operations

**Autonomy**: 90%+  
**Promise**: "We operate logistics — you govern intent."

### 1️⃣ Decision Authority Contract

```yaml
DecisionMode: FULL_AUTONOMY_WITH_GOVERNANCE
```

- AI operates end-to-end
- Humans define intent & constraints, not actions

### 2️⃣ Execution Contract

```yaml
execution:
  self_healing: true
  human_approval: false
```

- Self-healing workflows
- Agent-to-agent negotiation
- No human approvals required

### 3️⃣ Risk & Override Contract

```yaml
OverrideWindow: GOVERNANCE_ONLY
```

- Governance-only overrides
- Ethics & compliance escalation
- No tactical intervention

### 4️⃣ Audit & Liability Contract

```yaml
Liability: SHARED_INFRASTRUCTURE
AuditLevel: REGULATORY_READY
```

- Constitutional logs
- Shared economic & operational liability
- Regulatory-grade compliance

**💰 Why this becomes industry standard**:  
At this level, you are infrastructure, not software.

---

## Why This Contract Model Wins

1. **Buyers can start small** → Low risk entry
2. **Legal teams stay comfortable** → Clear contracts
3. **Trust compounds per tier** → Natural progression
4. **Autonomy is earned, not forced** → No trust jumps
5. **Architecture aligns with revenue** → Clean scaling

---

## 🔒 Founder Rule (Critical)

**Never increase decision authority without upgrading the audit contract.**

**This is how trillion-dollar systems survive scrutiny.**

---

## Technical Implementation (fw Framework)

### Frappe DocType: `Flowwolf Autonomy Contract`

```python
class FlowwolfAutonomyContract(Document):
    # Core fields
    partner = Link("Partner")
    autonomy_level = Select(["L1", "L2", "L3", "L4", "L5"])
    
    # Decision Authority
    decision_mode = Select([
        "OBSERVE_ONLY",
        "PROPOSE_WITH_APPROVAL",
        "AUTONOMOUS_WITH_THRESHOLDS",
        "MULTI_AGENT_OPTIMIZATION",
        "FULL_AUTONOMY_WITH_GOVERNANCE"
    ])
    
    # Execution Constraints
    allowed_actions = Small Text  # JSON list
    forbidden_actions = Small Text  # JSON list
    requires_approval = Check
    confidence_threshold = Float  # 0.0-1.0
    
    # Risk & Override
    override_window = Select(["OPEN", "CONDITIONAL", "POLICY_ONLY", "GOVERNANCE_ONLY"])
    rollback_required = Check
    kill_switch_enabled = Check
    
    # Audit & Liability
    liability = Select(["CUSTOMER", "SHARED", "CONDITIONAL_SHARED", "PLATFORM_GOVERNED", "SHARED_INFRASTRUCTURE"])
    audit_level = Select(["FULL_TRACE", "DECISION_SIGNED", "EXPLAINABLE_AI", "POLICY_COMPLIANT", "REGULATORY_READY"])
    
    # Commercial
    pricing_tier = Link("Pricing Tier")
    monthly_fee = Currency
    per_transaction_fee = Currency
```

### Usage in Governance Engine

```python
def can_execute_autonomously(intent, partner):
    contract = frappe.get_doc("Flowwolf Autonomy Contract", 
                               {"partner": partner.name})
    
    if contract.decision_mode == "OBSERVE_ONLY":
        return False  # Must go to human
    
    if contract.decision_mode == "PROPOSE_WITH_APPROVAL":
        create_approval_request(intent)
        return False  # Wait for approval
    
    if contract.decision_mode == "AUTONOMOUS_WITH_THRESHOLDS":
        if intent.confidence < contract.confidence_threshold:
            escalate_to_human(intent, "Low confidence")
            return False
        return True  # Auto-execute
    
    # Higher levels...
```

---

## See Also

- **37_THE_PAID_AUTONOMY_LADDER.md** - Commercial framework
- **06_GOVERNANCE_FRAMEWORK.md** - Governance engine design
- **00_STRATEGIC_EXECUTION_PLAN.md** - Revenue roadmap

---

**"Contracts create trust. Trust creates revenue."** 📜💰
