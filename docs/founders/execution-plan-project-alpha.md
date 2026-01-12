# Execution Plan: Project Alpha (The Build)

**Version**: 9.3 (Agentic Core)
**Context**: Executing the v9.0 "Karmic Completion" Architecture.  
**Phase**: Build & Launch (90 Days).

---

## 📅 The 90-Day Sprint Schedule

We are building the **Minimal Canonical Core** (Apps + Intent Graph + Governance).

### Sprint 1: The Trinity Setup (Weeks 1-2)
**Goal**: Initialize the 3 blank apps and the shared kernel.
*   [ ] Create App `cortex_ag_ai` (The Brain).
*   [ ] Create App `fluent_ag_ai` (The Translator).
*   [ ] Create App `motion_ag_ai` (The Body).
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
  /cortex_ag_ai   (git repo)
  /fluent_ag_ai   (git repo)
  /motion_ag_ai   (git repo)
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
`bench new-app cortex_ag_ai`
`bench new-app fluent_ag_ai`
`bench new-app motion_ag_ai`
