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

## Phase 3: The "Network" Sprint (Critical v4.0 Upgrade)
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
