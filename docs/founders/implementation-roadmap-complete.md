# Implementation Roadmap - Complete (Granular Tasks + MVP→DEMO→PROD)

**Version**: 9.4 (Agentic Core)
**Methodology**: TDD + MVP→DEMO→PROD lifecycle gates

---

## Part 1: The Antigravity Lifecycle (MVP → DEMO → PROD)

Every capability must graduate through 3 stages. You cannot promote to the next stage without passing the **TDD Gate**.

| Stage | Goal | TDD Gate (Mandatory) |
| :--- | :--- | :--- |
| **MVP** | "It Works" (Happy Path) | Backend Unit Tests checks `output == expected`. |
| **DEMO** | "It Feels Right" (UX) | Frontend Tests (Jest/Cypress). The Demo Script *is* the E2E Test. |
| **PROD** | "It Survives" (Hardening) | Trace Replay, Performance Budget, circuit breakers. |

---

## Part 2: Phase-by-Phase Breakdown

### Phase 0: The Big Bang (Week 1)
**Goal**: Initialize infrastructure

**MVP Tasks**:
- [ ] Run `bench new-app cortex_ag_ai`
- [ ] Run `bench new-app fluent_ag_ai`
- [ ] Run `bench new-app motion_ag_ai`
- [ ] Install apps on development site
- [ ] Configure CI/CD (GitHub Actions)

**DEMO**: N/A (infrastructure)

**PROD Checklist**:
- [ ] CI passing (badge green)
- [ ] All 3 apps installable
- [ ] Basic smoke test passes

---

### Phase 1: The Brain (Cortex) - Weeks 2-4

#### 1.1 MVP: Intent Graph (Versioned)
**Tasks**:
- [ ] Create `IntentDefinition` DocType (immutable, versioned)
- [ ] Create `IntentInstance` DocType (runtime, mutable)
- [ ] Create `Intent` Pydantic schemas (TenderLoad, AcceptLoad, etc.)
- [ ] Create `EntityResolver` (mocked for MVP)

**TDD Gate**: `test_create_intent_node` → Assert Pydantic validation works

#### 1.2 DEMO: Intent Inspector UI
**Tasks**:
- [ ] Create `IntentGraph.vue` component
- [ ] Display nodes with confidence badges
- [ ] Display autonomy ceiling (red/green)
- [ ] Display governance status (Allowed/Blocked)

**TDD Gate**: `IntentGraph.spec.js` → Mount component, assert badges render

#### 1.3 PROD: Governance Enforcement
**Tasks**:
- [ ] Create `GovernanceEngine` class
- [ ] Create `DecisionContract` DocType
- [ ] Implement `calculate_autonomy_level(intent, partner)`
- [ ] Add circuit breakers

**TDD Gate**: `test_governance_block` → Feed "Banned Partner" signal, assert BLOCKED + audit log

#### 1.4 Entity Resolution (MVP Placeholder)
**Tasks**:
- [ ] Stub `EntityResolutionAgent` (returns mock data)
- [ ] Create `Location` Pydantic model
- [ ] Create `Carrier` Pydantic model

**TDD Gate**: `test_resolve_location_mocked` → Input "LAX" → Output Location(code="USLAX")

#### 1.5 Autonomy Governance Layer (v9.4)
**Tasks**:
- [ ] Create `Partner Signal Profile` DocType
- [ ] Add fields: `trust_score`, `autonomy_ceiling`, `data_quality_score`
- [ ] Implement `calculate_autonomy_level` in GovernanceEngine

**TDD Gate**: `test_autonomy_ceiling` → High-confidence intent + low-ceiling partner = BLOCKED

---

### Phase 2: Perception (Fluent) - Weeks 5-7

#### 2.1 MVP: Universal Ingest
**Tasks**:
- [ ] Create `/api/v2/ingest` endpoint
- [ ] Implement `NormalizedSignal` schema (idempotency key, trace ID)
- [ ] Create `PluginInterface` (abstract base for protocols)
- [ ] Implement X12 plugin (EDI 204 only for MVP)

**TDD Gate**: `test_api_ingest` → Send POST with JSON → Assert 200 + trace_id returned

#### 2.2 DEMO: Drag & Drop UI
**Tasks**:
- [ ] Create `FileUploader.vue` component
- [ ] Add progress bar
- [ ] Display live preview (Intent name + confidence)
- [ ] Show JSON output

**TDD Gate**: **Cypress** → Drag fixture file → Assert "Parsing..." → Assert "Success" → Assert confidence score visible

#### 2.3 PROD: Circuit Breakers
**Tasks**:
- [ ] Implement `CircuitBreaker` utility class
- [ ] Add tenant-aware breakers (per partner)
- [ ] Configure thresholds (10 failures in 60s = OPEN)

**TDD Gate**: `test_circuit_trips` → Send 10 bad files → Assert 11th rejected with 429

---

### Phase 3: Execution (Motion) - Weeks 8-10

#### 3.1 MVP: Load Creation (via Agent)
**Tasks**:
- [ ] Create `ShipmentLoad` DocType
- [ ] Create `AgentContract` abstract base class
- [ ] Implement `ShipmentBookingAgent`
- [ ] Implement `execute(intent) →Load`

**TDD Gate**: `test_agent_execution` → `Agent.execute(intent)` → Assert Load created

#### 3.2 DEMO: Control Tower Dashboard
**Tasks**:
- [ ] Create `ControlTower.vue` (Kanban board)
- [ ] Show columns: "Intents Pending", "Loads Active", "Delivered"
- [ ] Add autonomy level badges

**TDD Gate**: `Kanban.spec.js` → Assert cards move columns when props change

#### 3.3 PROD: Autonomy Gating
**Tasks**:
- [ ] Implement `AutonomyEngine.can_execute(intent, partner)`
- [ ] Add confidence × trust × ceiling logic
- [ ] Block execution if ceiling exceeded

**TDD Gate**: `test_autonomy_ceiling` → Low-trust partner + auto-dispatch intent = DRAFT state

---

### Phase 4: Platform (Jupiter) - Weeks 11-14

#### 4.1 MVP: The SDK (`@skill`)
**Tasks**:
- [ ] Create `@skill` decorator
- [ ] Implement skill registry
- [ ] Write example skill (`calculate_shipping_cost`)

**TDD Gate**: `test_custom_skill` → Register skill → Execute intent → Assert skill called

#### 4.2 DEMO: Skill Marketplace UI
**Tasks**:
- [ ] Create `AppStore.vue` component
- [ ] List available skills
- [ ] Add "Install" button

**TDD Gate**: **Cypress** → Click "Install Customs Component" → Assert "Installed" badge

#### 4.3 PROD: Isolation Vault
**Tasks**:
- [ ] Implement tenant-key encryption
- [ ] Add per-tenant Redis namespaces
- [ ] Test cross-tenant isolation

**TDD Gate**: `test_tenant_isolation` → User A searches User B's data → Assert empty result

---

## Part 3: Deliverable Definition

The project is "Complete" only when:

1. **Backend Coverage** ≥ 100% on new/modified lines
2. **Frontend Coverage** ≥ 80% (components)
3. **Cypress Suite** runs nightly and passes (the sales demo is the test)
4. **Performance** < 200ms for Intent resolution
5. **All TDD Gates** pass

---

## Part 4: Task Tracking

Use this checklist to track progress:

- [ ] Phase 0 complete (apps initialized)
- [ ] Phase 1 MVP complete (Intent Graph works)
- [ ] Phase 1 DEMO complete (Intent Inspector UI)
- [ ] Phase 1 PROD complete (Governance hardened)
- [ ] Phase 2 MVP complete (API accepts signals)
- [ ] Phase 2 DEMO complete (Drag & drop works)
- [ ] Phase 2 PROD complete (Circuit breakers live)
- [ ] Phase 3 MVP complete (Loads created)
- [ ] Phase 3 DEMO complete (Dashboard live)
- [ ] Phase 3 PROD complete (Autonomy gating enforced)
- [ ] Phase 4 MVP complete (SDK functional)
- [ ] Phase 4 DEMO complete (Marketplace UI)
- [ ] Phase 4 PROD complete (Tenant isolation verified)

---

**Status**: Ready for Phase 0 execution.

---

## Performance Test Suite (GAP-I5 Fix)

### Latency Budget Tests

Create `tests/performance/test_latency_budget.py`:

```python
import time
import pytest
from cortex_ag_ai.intent.library import TenderLoad
from cortex_ag_ai.governance.engine import GovernanceEngine

class TestLatencyBudgets:
    """Enforce latency budgets from Engineering Guidelines."""
    
    def test_intent_resolution_under_200ms(self):
        """Intent resolution must complete in < 200ms."""
        signal = load_fixture("sample_edi_204.json")
        
        start = time.time()
        intent = extract_intent(signal)
        elapsed_ms = (time.time() - start) * 1000
        
        assert elapsed_ms < 200, f"Intent resolution took {elapsed_ms}ms (budget: 200ms)"
        assert intent.confidence > 0.8
    
    def test_chat_response_under_1s(self):
        """Chat responses must complete in < 1s."""
        user_message = "I need to ship 5 pallets from LAX to SFO tomorrow"
        
        start = time.time()
        response = chatbot.respond(user_message)
        elapsed_ms = (time.time() - start) * 1000
        
        assert elapsed_ms < 1000, f"Chat response took {elapsed_ms}ms (budget: 1000ms)"
        assert response.intent_extracted
    
    def test_execution_decision_under_100ms(self):
        """Governance decisions must complete in < 100ms."""
        intent = TenderLoad(origin="USLAX", destination="USSFO")
        partner = load_partner("P12345")
        
        start = time.time()
        decision = GovernanceEngine().can_execute(intent, partner)
        elapsed_ms = (time.time() - start) * 1000
        
        assert elapsed_ms < 100, f"Execution decision took {elapsed_ms}ms (budget: 100ms)"
    
    def test_p95_latency_under_budget(self):
        """95th percentile must meet budget (load test)."""
        latencies = []
        
        for _ in range(100):
            start = time.time()
            intent = extract_intent(random_signal())
            latencies.append((time.time() - start) * 1000)
        
        p95 = sorted(latencies)[94]  # 95th percentile
        assert p95 < 250, f"P95 latency {p95}ms exceeds budget (250ms)"
```

### Throughput Tests

```python
def test_throughput_1000_intents_per_second():
    """System must handle 1000 intents/sec sustained."""
    import asyncio
    
    async def process_batch(batch_size=1000):
        tasks = [extract_intent_async(random_signal()) for _ in range(batch_size)]
        start = time.time()
        await asyncio.gather(*tasks)
        duration = time.time() - start
        return batch_size / duration  # intents/sec
    
    throughput = asyncio.run(process_batch())
    assert throughput >= 1000, f"Throughput {throughput:.0f}/s < 1000/s"
```

### Memory Tests

```python
def test_memory_leak_after_10k_intents():
    """Memory must not grow beyond 10MB after 10K intents."""
    import tracemalloc
    
    tracemalloc.start()
    baseline = tracemalloc.get_traced_memory()[0]
    
    # Process 10K intents
    for _ in range(10000):
        intent = extract_intent(random_signal())
    
    current, peak = tracemalloc.get_traced_memory()
    growth_mb = (current - baseline) / 1024 / 1024
    
    assert growth_mb < 10, f"Memory leaked {growth_mb:.1f}MB (budget: 10MB)"
```

### CI Integration

Add to `.github/workflows/performance.yml`:

```yaml
- name: Run Performance Tests
  run: |
    pytest tests/performance/ -v --benchmark-only
    
- name: Fail if budget exceeded
  run: |
    pytest tests/performance/test_latency_budget.py --strict
```

---

**Status**: Performance test suite defined and ready for implementation.
