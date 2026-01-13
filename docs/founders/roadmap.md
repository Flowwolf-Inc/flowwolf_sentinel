---
title: "Master Roadmap"
tags: []
version: "9.1"
last_updated: "2026-01-13"
---

# Master Roadmap

---

**Intent**: Revenue now → Industry dominance later  
**Start Date**: Monday, January 12, 2026  
**Start Time**: 9:14 AM PST  
**Current Phase**: v9.1 (Sales-Led Autonomy)  
**Final Destiny**: v9.1 (Industry Standard)

---

## 🎯 The Strategic Arc

```
v9.1                v9.1              v9.1              v9.1
Sales-Led ────────> Market-Fit ────> Scale-Ready ────> Industry Standard
(Revenue now)       (Validated)       (Growing)         (Dominance)
```

---

## Phase 1: v9.1 (Sales-Led Autonomy) - Revenue NOW

**Timeline**: Jan 12 - Mar 31, 2026 (11 weeks)  
**Goal**: First paying customers + proven ROI  
**Success Metric**: $50K MRR by end of Q1

### What We Build (Minimum Sellable Product)

#### Week 1-2: The Demo That Sells
**Priority**: Make it TANGIBLE
- ✅ Live EDI 204 → Intent extraction demo
- ✅ Partner Scorecard visualization
- ✅ Autonomy Level progression (visual)
- ✅ "Before/After" ROI calculator

**Output**: Repeatable 30-minute demo that closes deals

#### Week 3-4: The Core That Works
**Priority**: Deliver on the promise
- ✅ fw_fluent: X12 EDI parsing (204, 990 only)
- ✅ fw_cortex: Intent extraction (TenderLoad only)
- ✅ fw_motion: Load creation (basic fields)
- ✅ Email alerts (no fancy UI yet)

**Output**: A broker can replace 1 manual EDI person

#### Week 5-8: The Safety That Sells
**Priority**: Trust = revenue
- ✅ Autonomy Ceiling (Levels 1-2 only)
- ✅ Human approval workflow
- ✅ Audit trail (every decision logged)
- ✅ Error handling (graceful degradation)

**Output**: CFO signs off on autonomy

#### Week 9-11: The Scale That Convinces
**Priority**: Prove it's not a toy
- ✅ 100 loads/day throughput
- ✅ 3 partners onboarded
- ✅ 95% accuracy (5% needs human review)
- ✅ Case study: "$10K/month saved"

**Output**: Reference customer for next sale

---

## Phase 2: v9.1 (Market-Fit Validated) - Q2 2026

**Timeline**: Apr 1 - Jun 30, 2026  
**Goal**: Product-market fit proven  
**Success Metric**: $250K MRR, 10 customers

### What We Add (Competitive Moat)

#### The Differentiators
- ✅ Multi-modal support (Ocean, Air, not just FTL/LTL)
- ✅ Email → Intent (not just EDI)
- ✅ Autonomy Level 3 (co-pilot mode)
- ✅ Partner ecosystem (3+ TMS integrations)

#### The Scalers
- ✅ API for external systems
- ✅ Batch processing (1000+ loads/day)
- ✅ Multi-tenant (5+ companies on same instance)

**Output**: Pricing power (can charge $5K/month per customer)

---

## Phase 3: v9.1 (Scale-Ready) - Q3-Q4 2026

**Timeline**: Jul 1 - Dec 31, 2026  
**Goal**: Series A ready  
**Success Metric**: $1M ARR, 50 customers

### What We Perfect (The Platform)

#### The Enterprise Features
- ✅ SSO (Okta, Azure AD)
- ✅ SOC-2 compliance
- ✅ 99.9% uptime SLA
- ✅ Dedicated support (enterprise tier)

#### The Network Effects
- ✅ Carrier marketplace (carriers bid on loads)
- ✅ Agent-to-agent negotiation (early Level 5)
- ✅ Skill marketplace (3rd-party plugins)

**Output**: Fundable story ($10M Series A)

---

## Phase 4: v9.1 (Industry Standard) - 2027+

**Timeline**: Jan 2027 onwards  
**Goal**: Category king  
**Success Metric**: $10M ARR, 500+ customers

### What We Become (The Standard)

- ✅ "Flowwolf-compatible" becomes industry term
- ✅ Competitors integrate with us (not vice versa)
- ✅ Intent schemas = de facto standard
- ✅ Agent protocols = logistics TCP/IP

**Output**: Industry standard, IPO trajectory

---

## 🔥 The v9.1 Launch Plan (Jan 12, 2026)

### Day 1 (Monday, Jan 12, 9:14 AM PST)

**9:14 AM**: Kickoff meeting
- ✅ Review this strategic plan
- ✅ Assign Week 1-2 tasks
- ✅ Set first demo date (Jan 26)

**10:00 AM**: Begin Phase 0 execution
```bash
bench new-app fw_cortex
bench new-app fw_fluent
bench new-app fw_motion
```

**2:00 PM**: First commit
- ✅ App skeletons created
- ✅ CI/CD pipeline running
- ✅ First test passing

**5:00 PM**: Day 1 standup
- ✅ Blockers identified
- ✅ Tomorrow's goals clear

### Week 1 Goal
**Output**: Live demo of EDI 204 → Intent extraction

**Demo Script**:
1. Upload sample EDI 204 file
2. Show Intent extraction (10 seconds)
3. Show confidence score (92%)
4. Show autonomy recommendation (Level 2 - Needs approval)
5. Click "Approve" → Load created
6. Show before/after ROI ($2/load → $0.10/load)

**Sales Pitch**: "Replace your EDI team with Flowwolf Sentinel"

---

## 💰 Pricing Strategy (v9.1)

### Tier 1: Assist ($500/month)
- **What**: Human reviews every load
- **Who**: New customers, trial period
- **Value**: Still 50% cheaper than EDI team

### Tier 2: Co-Pilot ($2,000/month)
- **What**: AI drafts, human approves
- **Who**: Established brokers, 100+ loads/month
- **Value**: 80% time savings

### Tier 3: Autonomous ($5,000/month) - v9.1+
- **What**: AI executes, human monitors
- **Who**: High-trust partners, 500+ loads/month
- **Value**: 95% touchless

**Revenue Model**: Monthly recurring + per-load fees

---

## 📊 Success Metrics (v9.1)

### Week 2: Demo Ready
- ✅ 30-minute demo script polished
- ✅ Sample data realistic
- ✅ Error handling graceful

### Week 4: First Pilot
- ✅ 1 customer signed (even if free trial)
- ✅ 10 loads processed successfully
- ✅ 1 "wow" moment captured (testimonial)

### Week 8: Repeatability
- ✅ 3 customers using daily
- ✅ 100 loads/day throughput
- ✅ 95% accuracy maintained

### Week 11: Revenue
- ✅ $10K MRR (2 paying customers)
- ✅ 1 case study published
- ✅ Pipeline: 5 qualified leads

---

## 🚫 What We DON'T Build (v9.1)

To ship fast, we defer:

❌ Multi-language support (English only)  
❌ Mobile app (web only)  
❌ Voice input (EDI/Email only)  
❌ Advanced reporting (basic metrics only)  
❌ Custom workflows (standard flow only)  
❌ White-labeling (Flowwolf brand only)  

**Rationale**: Revenue first, features later

---

## 🎯 The North Star

**v9.1 Vision**: "Flowwolf Sentinel replaces your EDI team"  
**v9.1 Vision**: "Flowwolf Sentinel is how modern brokers operate"  
**v9.1 Vision**: "Flowwolf Sentinel is the logistics operating system"  
**v9.1 Vision**: "Flowwolf Sentinel IS the logistics industry standard"

---

## ✅ Alignment with Technical v9.1

**Technical v9.1** (the docs we just completed) = The destination  
**Sales v9.1** (this plan) = The path to get there

**Bridge**:
- Technical docs = "What we'll become"
- Sales plan = "How we get revenue to fund it"
- Both true, different timelines

---

**Start**: Monday, Jan 12, 2026, 9:14 AM PST  
**First Milestone**: Demo ready by Jan 26  
**First Revenue**: By March 31  
**Industry Standard**: By 2027

**Let's build.** 🚀

---

---

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
- [ ] Run `bench new-app fw_cortex`
- [ ] Run `bench new-app fw_fluent`
- [ ] Run `bench new-app fw_motion`
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

#### 1.5 Autonomy Governance Layer (v9.1)
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
from fw_cortex.intent.library import TenderLoad
from fw_cortex.governance.engine import GovernanceEngine

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