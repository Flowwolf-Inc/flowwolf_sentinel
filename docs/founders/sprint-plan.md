---
title: "Sprint Plan"
tags: []
version: "9.1"
last_updated: "2026-01-13"
---

# Sprint Plan & Project Alpha

# Implementation Phases: The Road to Networked Autonomy

**Version**: 9.3 (Agentic Core)
**Timeline**: [Q1 2026] - [Q4 2026]

## Phase 1: The Foundation (Completed)
**Goal**: Operational Stability. (X12 Parser, Basic Agents).

---

## Phase 2: The "Intent" Upgrade (Immediate)
**Goal**: Decouple Protocol from Logic.
**Duration**: 4 Weeks.

### Objectives:
1.  **Build the `Intent Node`**: Refactor `Fluent` to output Intent, not EDI Documents.
2.  **Build the `Governance Engine`**: Implement `Decision Contract` DocType.

### Deliverable:
*   Unified processing path for EDI + Email.
*   "Safe" Autonomy via Contracts.

---

## Phase 3: The "Network" Sprint (Critical v9.1 Upgrade)
**Goal**: Solve the "Cold Start" Problem via Federation.
**Duration**: 6 Weeks.

### Objectives:
1.  **Build `Global Graph`**:
    *   Shared `Global Entity` DocType (anonymized).
    *   Sync Logic: If `Entity` has >5 confirmations -> Promote to Global.
2.  **Upgrade `Resolution Agent`**:
    *   Implement Hybrid Waterfall: Exact -> Geo -> Global Vector -> Local Vector.

### Deliverable:
*   New Tenants start with "Pre-Loaded" knowledge of top 100 Retailers/Carriers.

---

## Phase 4: The "Teacher" Sprint
**Goal**: Explicit Feedback Loops.
**Duration**: 4 Weeks.

### Objectives:
1.  **Build "Reasoning Capture" UI**:
    *   Interceptor Modal on Form Save: "Why did you change this? (One-off / New Rule)".
2.  **Build `OptimizationAgent`**:
    *   Process explicit feedback to update `Local Graph`.

### Deliverable:
*   AI stops making the same mistake twice.

---

## Phase 5: The "Generative" Sprint (Onboarding)
**Goal**: Zero-Config Onboarding.
**Duration**: 6 Weeks.

### Objectives:
1.  **Build `ArchitectAgent`**:
    *   LLM with **Pydantic Constraints** to generate valid `Intent Maps` from PDFs.

### Deliverable:
*   2-Hour Onboarding.

---

## Phase 6: The "Confidence" Sprint (QA & Reliability)
**Goal**: Deterministic Testing & Tooling.
**Duration**: 4 Weeks.

### Objectives:
1.  **Build "Deterministic Mode"**:
    *   Flag `FRA_TEST_MODE=1`. When set, `Cortex` bypasses LLMs and returns cached/mocked JSONs. Use `VCR.py` pattern for embedding calls.
2.  **Build "Intent Replay"**:
    *   Tool to export a Production Intent and inject it into the Test Runner.
3.  **Build "Pydantic Generator"**:
    *   CLI tool `bench generate-pydantic` that reads DocType JSONs and writes `models.py`.

### Deliverable:
*   Flaky Tests reduced to 0%. Developer Boilerplate reduced by 80%.

---

# Execution Plan: Project Alpha (The Build)

**Version**: 9.3 (Agentic Core)
**Context**: Executing the v9.1 "Karmic Completion" Architecture.  
**Phase**: Build & Launch (90 Days).

---

## 📅 The 90-Day Sprint Schedule

We are building the **Minimal Canonical Core** (Apps + Intent Graph + Governance).

### Sprint 1: The Trinity Setup (Weeks 1-2)
**Goal**: Initialize the 3 blank apps and the shared kernel.
*   [ ] Create App `fw_cortex` (The Brain).
*   [ ] Create App `fw_fluent` (The Translator).
*   [ ] Create App `fw_motion` (The Body).
*   [ ] Setup `frappe-bench` with specific sites for `sandbox` and `dev`.
*   [ ] Define the **Shared Kernel** (Common Utilities).

### Sprint 2: The Intent Graph (Weeks 3-4)
**Goal**: Build the data structures that hold "Meaning".
*   [ ] **Cortex**: Create `Intent Node`, `Intent Type` (SemVer enabled).
*   [ ] **Cortex**: Create `Entity Resolution Agent` (Mocked).
*   [ ] **Fluent**: Create `Exchange Document` and `Intent Mapper`.
*   [ ] **Test**: Feed a JSON into `Fluent` and see an `Intent Node` appear in `Cortex`.

### Sprint 3: The Governance Engine (Weeks 5-6)
**Goal**: Build the "Constitution".
*   [ ] **Cortex**: Create `Decision Contract` DocType.
*   [ ] **Cortex**: Implement `GovernanceEngine` Python class.
*   [ ] **Test**: Write a Contract "Max Value $500". submit an Intent for $600. Verify Rejection.

### Sprint 4: The Perception Layer (Weeks 7-8)
**Goal**: Connect to Reality (X12).
*   [ ] **Fluent**: Port the X12 Parsing Logic from `flowwolf_edi` (Legacy) into a `Fluent Plugin`.
*   [ ] **Fluent**: Implement the `Universal Ingestor` (Route X12 -> Plugin -> Intent).
*   [ ] **Test**: End-to-End: Raw EDI 204 file -> `Intent Node` (ShipGoods).

### Sprint 5: The Execution Layer (Weeks 9-10)
**Goal**: Create Business Value.
*   [ ] **Motion**: Create `Shipment Load` DocType.
*   [ ] **Motion**: Implement `WorkflowEngine`.
*   [ ] **Integration**: `Cortex` ("Approved Intent") -> `Motion` ("Create Load").

### Sprint 6: The "Saturn" Hardening (Weeks 11-12)
**Goal**: Stability & Launch.
*   [ ] **Cortex**: Implement `Schema Registry` (Pydantic Validation).
*   [ ] **System**: Implement `Circuit Breakers`.
*   [ ] **Launch**: Deploy to Staging.

---

## 🛠️ Technical Primitives (The "How")

### 1. The Repo Structure
We will use a Monorepo approach for convenience within the `frappe-bench`, but treat them as separate git repos eventually.
```
/apps
  /fw_cortex   (git repo)
  /fw_fluent   (git repo)
  /fw_motion   (git repo)
```

### 2. The Development Standard
*   **Strict Pydantic**: No loose dicts passed between Apps.
*   **Test Driven**: Write the `Decision Contract` test case *before* writing the Engine code.

## 👥 Resourcing Plan

*   **Principal Engineer (You)**: Focus on `Cortex` (Governance/Intent).
*   **Senior Backend**: Focus on `Fluent` (X12 Parsing/Plugins).
*   **Full Stack**: Focus on `Motion` (UI/Workflows).

## 🚦 Immediate Next Action
**Initialize the 3 Apps.**
`bench new-app fw_cortex`
`bench new-app fw_fluent`
`bench new-app fw_motion`