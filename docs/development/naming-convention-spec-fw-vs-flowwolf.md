---
title: "Naming Convention Spec Fw Vs Flowwolf"
tags: []
version: "9.1"
last_updated: "2026-01-12"
---

# Naming Convention Spec: fw vs Flowwolf

**Version**: 9.4.2 (Frozen)  
**Authority**: Engineering Charter  
**Status**: 🔒 **IMMUTABLE RULE**

---

## 🏛️ The Golden Rule (Frozen)

> **Inside code = `fw`**  
> **Outside code = `Flowwolf`**  
> **Never mix within the same layer.**

---

## 📜 The Philosophy

### `fw` → Execution, Evolution, Adaptation
Where things **run**, **learn**, and **change**:
- Code modules
- Database tables
- API endpoints
- Service names
- Docker containers
- Internal functions

**Energy**: Dynamic, flowing, adaptive (the river)

### `Flowwolf` → Trust, Contracts, Authority
Where **decisions are made**, **contracts are signed**, **authority is exercised**:
- Company name
- Legal entities
- Customer-facing brand
- Governance DocTypes
- Decision Contracts
- Partner Agreements

**Energy**: Stable, authoritative, trustworthy (the mountain)

---

## 🎯 Frappe Naming Convention Spec

### 1. App Names (Internal Code = `fw_*`)

| Old Name (Deprecated) | New Name (Canonical) | Rationale |
|----------------------|---------------------|-----------|
| `cortex_ag_ai` | `fw_cortex` | The Brain (execution layer) |
| `fluent_ag_ai` | `fw_fluent` | The Translator (execution layer) |
| `motion_ag_ai` | `fw_motion` | The Body (execution layer) |

**Convention**: All Frappe apps use `fw_` prefix.

---

### 2. DocTypes (Split by Layer)

#### Execution Layer DocTypes (Code = `fw_*`)

| DocType Name | Table Name | Purpose |
|--------------|------------|---------|
| `FW Intent Instance` | `tabFW Intent Instance` | Runtime intent data |
| `FW Signal` | `tabFW Signal` | Raw signal storage |
| `FW Execution Result` | `tabFW Execution Result` | Agent execution outputs |
| `FW Circuit Breaker` | `tabFW Circuit Breaker` | Technical circuit state |

**Pattern**: `FW {NounPhrase}` (execution/runtime artifacts)

#### Authority Layer DocTypes (Brand = `Flowwolf *`)

| DocType Name | Table Name | Purpose |
|--------------|------------|---------|
| `Flowwolf Intent Definition` | `tabFlowwolf Intent Definition` | Canonical schema (immutable) |
| `Flowwolf Decision Contract` | `tabFlowwolf Decision Contract` | Governance policy (authority) |
| `Flowwolf Partner Agreement` | `tabFlowwolf Partner Agreement` | Legal contracts |
| `Flowwolf Shipment Load` | `tabFlowwolf Shipment Load` | Customer-facing load record |

**Pattern**: `Flowwolf {NounPhrase}` (authority/contract artifacts)

---

### 3. API Endpoints

#### Internal APIs (Execution = `/fw/`)

```
/api/fw/cortex/v1/intent/resolve
/api/fw/fluent/v2/ingest
/api/fw/motion/v1/load/execute
```

**Pattern**: `/api/fw/{app}/{version}/{resource}`

#### External APIs (Authority = `/flowwolf/`)

```
/api/flowwolf/v1/partner/onboard
/api/flowwolf/v1/contract/sign
/api/flowwolf/v1/decision/review
```

**Pattern**: `/api/flowwolf/{version}/{resource}`

---

### 4. Service Names (Docker/K8s)

#### Execution Services

```yaml
services:
  fw-cortex:
    image: flowwolf/fw-cortex:latest
  
  fw-fluent:
    image: flowwolf/fw-fluent:latest
  
  fw-motion:
    image: flowwolf/fw-motion:latest
```

#### Authority Services

```yaml
services:
  flowwolf-gateway:
    image: flowwolf/gateway:latest  # Customer-facing API gateway
  
  flowwolf-portal:
    image: flowwolf/portal:latest   # Partner portal (UI)
```

---

### 5. Python Modules/Packages

#### Execution Code

```python
# fw_cortex/fw_cortex/intent/library.py
from fw_cortex.intent.library import TenderLoad
from fw_cortex.governance.engine import GovernanceEngine

# fw_fluent/fw_fluent/plugins/x12.py
from fw_fluent.plugins.x12 import X12Plugin

# fw_motion/fw_motion/agents/booking.py
from fw_motion.agents.booking import ShipmentBookingAgent
```

#### Authority Code

```python
# Governance policies (authority layer)
from flowwolf.contracts import DecisionContract
from flowwolf.agreements import PartnerAgreement
```

---

### 6. Database Tables (Frappe Auto-Generated)

Frappe prepends `tab` automatically:

| DocType | Table Name | Layer |
|---------|------------|-------|
| `FW Intent Instance` | `tabFW Intent Instance` | Execution |
| `Flowwolf Decision Contract` | `tabFlowwolf Decision Contract` | Authority |

**Rule**: We control DocType name, Frappe controls table prefix.

---

### 7. Frontend Components (Vue)

#### Execution Components

```
fw_cortex/fw_cortex/ui/IntentGraph.vue
fw_motion/fw_motion/ui/LoadBoard.vue
```

#### Authority Components

```
flowwolf_portal/flowwolf_portal/ui/ContractReview.vue
flowwolf_portal/flowwolf_portal/ui/PartnerOnboarding.vue
```

---

## 🔄 Migration Map (Old → New)

### Apps

```bash
# Old (deprecated)
cortex_ag_ai/
fluent_ag_ai/
motion_ag_ai/

# New (canonical)
fw_cortex/
fw_fluent/
fw_motion/
```

**Migration Command**:
```bash
bench rename-app cortex_ag_ai fw_cortex
bench rename-app fluent_ag_ai fw_fluent
bench rename-app motion_ag_ai fw_motion
```

### DocTypes

```python
# Migration script
DOCTYPE_MIGRATIONS = {
    # Execution layer (fw_*)
    "Intent Instance": "FW Intent Instance",
    "Signal": "FW Signal",
    "Circuit Breaker": "FW Circuit Breaker",
    "Execution Result": "FW Execution Result",
    
    # Authority layer (Flowwolf *)
    "Intent Definition": "Flowwolf Intent Definition",
    "Decision Contract": "Flowwolf Decision Contract",
    "Partner Signal Profile": "Flowwolf Partner Agreement",
    "Shipment Load": "Flowwolf Shipment Load",
}

for old, new in DOCTYPE_MIGRATIONS.items():
    frappe.rename_doc("DocType", old, new)
```

---

## 🎭 Layer Assignment Logic

**When naming something, ask**:

### Is it execution code? → `fw`
- Does it run/execute?
- Does it adapt/learn?
- Does it process data?
- Is it internal-only?

**Examples**: Intent resolution, signal parsing, circuit breaker state

### Is it authority/contract? → `Flowwolf`
- Does it represent a decision?
- Is it immutable (contract)?
- Is it customer-facing?
- Does it require governance?

**Examples**: Intent Definition (schema contract), Decision Contract (policy), Partner Agreement (trust)

---

## 📋 Quick Reference

| Artifact | Naming Pattern | Example |
|----------|----------------|---------|
| **Frappe App** | `fw_{name}` | `fw_cortex` |
| **Execution DocType** | `FW {Noun}` | `FW Intent Instance` |
| **Authority DocType** | `Flowwolf {Noun}` | `Flowwolf Decision Contract` |
| **Internal API** | `/api/fw/{resource}` | `/api/fw/cortex/v1/intent` |
| **External API** | `/api/flowwolf/{resource}` | `/api/flowwolf/v1/partner` |
| **Docker Service** | `fw-{name}` | `fw-cortex` |
| **Python Package** | `fw_{name}.module` | `fw_cortex.intent` |

---

## 🚫 Anti-Patterns (DO NOT DO)

❌ **Mixing in same layer**:
```python
# WRONG: Don't mix fw and Flowwolf in same module
from fw_cortex.intent import FlowwolfIntent  # ❌
```

❌ **Wrong layer assignment**:
```python
# WRONG: Runtime data should be fw, not Flowwolf
class FlowwolfIntentInstance(Document):  # ❌ Should be FW Intent Instance
    pass
```

❌ **Generic names without prefix**:
```python
# WRONG: Missing prefix
from cortex.intent import Intent  # ❌ Should be fw_cortex
```

---

## ✅ Correct Patterns

```python
# Execution layer (fw)
from fw_cortex.intent.library import TenderLoad
from fw_fluent.plugins.x12 import X12Plugin
from fw_motion.agents.booking import ShipmentBookingAgent

# Authority layer (Flowwolf)
contract = frappe.get_doc("Flowwolf Decision Contract", "contract-123")
definition = frappe.get_doc("Flowwolf Intent Definition", "TenderLoad:v4")
load = frappe.get_doc("Flowwolf Shipment Load", "LOAD-001")
```

---

## 🔒 Enforcement

This rule is **frozen** and must be enforced:

1. **Pre-commit hook**: Reject commits with wrong naming
2. **Code review**: Naming violations → PR blocked
3. **CI check**: Automated naming linter

```python
# .pre-commit-config.yaml
- repo: local
  hooks:
    - id: check-fw-naming
      name: Enforce fw vs Flowwolf naming
      entry: python scripts/check_naming_convention.py
      language: python
```

---

## 📖 Philosophical Alignment

### `fw` = The River (Heraclitus)
> "You cannot step into the same river twice."
- Code flows, changes, adapts
- Runtime execution is dynamic
- Never the same twice

### `Flowwolf` = The Mountain (Lao Tzu)
> "The mountain does not move."
- Contracts are immutable
- Authority is stable
- Governance is unchanging

**Together**: The river (execution) flows around the mountain (authority).

---

## 🎯 Summary

**One-Line Rule** (Frozen):
> Use `fw` where things execute, evolve, and adapt.  
> Use `Flowwolf` where trust, contracts, and authority matter.

**Status**: �� **IMMUTABLE** - This rule cannot be changed without board approval.

---

**"fw flows. Flowwolf governs."** 🌊⛰️
