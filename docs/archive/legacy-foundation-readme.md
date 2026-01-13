---
title: "Legacy Foundation Readme"
tags: []
version: "9.1"
last_updated: "2026-01-12"
---

# Flowwolf: The Intent-Native Operating System for Logistics

> Built on an AI-native core and progressing safely toward autonomy.

**Version**: 9.4.2 (Positioning Locked)  
**Status**: ✅ **READY FOR IMPLEMENTATION**  
**Documentation**: 28 documents, ~5,000 lines

---

## 🚀 Quick Start

| I want to... | Go here... |
|--------------|------------|
| **Understand the vision** | [02_VISION_AND_STRATEGY](VISION_AND_STRATEGY_AUTONOMY_TIERS.md) |
| **Start building** | [11_DEVELOPER_QUICK_START](DEVELOPER_QUICK_START_5_MINUTE_SETUP.md) 🚀 |
| **Get answers** | [17_FAQ](FAQ_COMMON_QUESTIONS.md) |
| **Read by role** | [00_READING_ORDER](READING_ORDER.md) |

---

## 🔒 Governed By

This project is governed by the [Engineering Constitution](ENGINEERING_CONSTITUTION.md).

**The Three Laws**:
1. If it runs → `fw`
2. If it governs → `flowwolf`
3. If it describes → tooling (metadata only)

See: [33_NAMING_CONVENTION_SPEC_FW_VS_FLOWWOLF.md](NAMING_CONVENTION_SPEC_FW_VS_FLOWWOLF.md)

---


## 💡 What is Flowwolf?

Flowwolf is the **Intent-Native Operating System** for logistics coordination.

### The Paradigm Shift

**Legacy Systems** (Protocol-Centric):
```
EDI 204 → Manual Mapping → EDI 990
```

**Flowwolf** (Intent-Native):
```
Any Signal → Intent Extraction → Autonomous Execution
```

### Why "Operating System"?

Just like **Linux** is the OS that applications run on:

- **Flowwolf** = The OS for logistics coordination
- **TMS/WMS** = Applications that execute loads  
- **EDI/API** = Input/output protocols (like TCP/IP)

We sit **above** your existing systems, orchestrating decisions autonomously.

---

## 🎯 Core Differentiators

### 1. Intent-Native (Not Protocol-Bound)

We extract business intent from **any** signal type:
- ✅ EDI (X12, EDIFACT)
- ✅ Email (unstructured text)
- ✅ API (JSON, XML)
- ✅ Voice (transcribed calls)

All become **Intent nodes** in our graph.

### 2. Progressively Autonomous (Not All-or-Nothing)

We don't deploy "full AI" on day one. You **earn** autonomy via trust:

| Tier | Level | What Happens |
|------|-------|--------------|
| **Assist** | 1 | AI suggests, human confirms |
| **Co-Pilot** | 2 | AI drafts, human approves |
| **Autonomous** | 4 | AI executes, human monitors |
| **Agentic** | 5 | Agent-to-agent negotiation |

### 3. AI-Native Core (Not Bolted-On)

Built on LLMs from day one:
- **Constrained generation** (Pydantic schemas prevent hallucinations)
- **VCR pattern** (deterministic AI tests)
- **Trace replay** (production debugging)

---

## 🏗️ The 3-App Architecture

```
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│  fw_cortex   │ ───> │  fw_fluent   │ ───> │  fw_motion   │
│   (The Brain)   │      │ (The Translator)│      │   (The Body)    │
└─────────────────┘      └─────────────────┘      └─────────────────┘
       │                         │                         │
       v                         v                         v
  Intent Graph            Signal Ingestion           Load Execution
  Entity Resolution       Protocol Adapters          TMS Business Logic
  Governance Engine       Universal Ingestor         Shipment DocTypes
```

See: [12_FRAPPE_APP_DESIGN_3_APP_TRIAD](FRAPPE_APP_DESIGN_3_APP_TRIAD.md)

---

## ❤️ The Heart: Intent Library

**[08_INTENT_LIBRARY_DEFINITIONS_THE_CORE_SCHEMA](INTENT_LIBRARY_DEFINITIONS_THE_CORE_SCHEMA.md)**

This defines the canonical schemas (TenderLoad, AcceptLoad, UpdateStatus, etc.).  
Everything else exists to support these schemas.

---

## 🔥 What's Different?

### vs EDI Platforms (Cleo, Kleinschmidt)
- **They**: Protocol-centric (X12 ↔ EDIFACT)
- **We**: Intent-native (Any Signal → Intent)

### vs TMS (SAP, Oracle)
- **They**: Application layer (execute loads)
- **We**: Operating system layer (orchestrate decisions)

### vs RPA (UiPath)
- **They**: UI automation (brittle)
- **We**: Intent understanding (robust)

---

## 📖 Documentation Navigator

### By Role

| I am a... | Start Here | Then Read |
|-----------|------------|-----------|
| **CEO/Investor** | [02_VISION](VISION_AND_STRATEGY_AUTONOMY_TIERS.md) | 01, 07, 18 |
| **Architect** | [04_ARCHITECTURE](ARCHITECTURE_DESIGN_CORE_COMPONENTS.md) | 03, 05, 06, 08 |
| **Developer** | [11_QUICK_START](DEVELOPER_QUICK_START_5_MINUTE_SETUP.md) 🚀 | 12, 14, 09 |
| **Sales** | [18_STAKEHOLDER_REVIEWS](STAKEHOLDER_REVIEWS_COMPREHENSIVE.md) | 02, 17 |
| **Customer** | [17_FAQ](FAQ_COMMON_QUESTIONS.md) | 02, 24 |
| **DevOps** | [24_PLAYBOOK](FAILURE_SCENARIOS_PLAYBOOK_INCIDENT_RESPONSE.md) 🚨 | 05, 16 |

### By Intent

| I want to... | Document |
|--------------|----------|
| Understand the problem | [01_PROBLEM_STATEMENT](PROBLEM_STATEMENT_THE_INTENT_GAP.md) |
| See the big picture | [00_DOCUMENT_MAP](DOCUMENT_MAP.md) |
| Learn the architecture | [04_ARCHITECTURE_DESIGN](ARCHITECTURE_DESIGN_CORE_COMPONENTS.md) |
| Build the system | [11_DEVELOPER_QUICK_START](DEVELOPER_QUICK_START_5_MINUTE_SETUP.md) |
| Understand pricing | [02_VISION (Section 5)](VISION_AND_STRATEGY_AUTONOMY_TIERS.md) |
| Debug an issue | [24_PLAYBOOK](FAILURE_SCENARIOS_PLAYBOOK_INCIDENT_RESPONSE.md) |

---

## 📊 Stats

- **Documents**: 28 (optimized from 34)
- **Lines**: ~5,000
- **Version**: 9.4.2 (Positioning Locked)
- **Status**: Frozen (changes require governance)

---

## 🚨 Quick Links

- **Production Emergency?** → [24_PLAYBOOK](FAILURE_SCENARIOS_PLAYBOOK_INCIDENT_RESPONSE.md) 🚨
- **Have a Question?** → [17_FAQ](FAQ_COMMON_QUESTIONS.md)
- **Unknown Term?** → [16_GLOSSARY](GLOSSARY_TERMINOLOGY_INDEX.md)

---

## ✅ Status

✅ **Positioning Locked** - "Intent-Native Operating System for Logistics"  
✅ **Architecturally Complete** - All designs documented  
✅ **Commercially Aligned** - Pricing, sales, messaging consistent  
✅ **Operationally Prepared** - Runbooks ready  
✅ **Developer-Friendly** - 5-minute setup guide  

---

**Next Step**: Execute Phase 0 - Initialize the 3 Frappe apps.

**Welcome to the Intent-Native Operating System for Logistics.** 🚀
