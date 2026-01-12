---
title: "Engineering Guidelines Tdd Manifesto"
tags: []
version: "9.1"
last_updated: "2026-01-12"
---

# Antigravity Engineering Guidelines: Zero Gravity, Zero Defects

**Version**: 9.3 (Agentic Core)
**Context**: The "Physics" of developing Flowwolf Autonomous.
**Mandate**: 100% Code Coverage via Strict TDD.

## 0. Review Summary

The existing guidelines establish an **exceptionally strong software-TDD culture**.
This update extends them into a **complete AI-native + logistics-native TDD system**.

Key upgrades:
- Explicit testing for **partial intents**
- Confidence- and trust-aware automation guardrails
- Autonomy ceiling enforcement via tests
- Chat-native and multi-channel test requirements
- Performance and latency budgets as correctness criteria

This document is **additive**, not a rewrite.

## 1. Prime Directive (Reaffirmed)

> **Test First, or Don’t Type**

Writing implementation code without a failing test remains a **Safety Violation**.

This applies equally to:
- Core logic
- AI agents
- Prompt templates
- Parsers
- Workflows
- Governance rules

No exceptions.

## 2. The TDD Loop (Red → Green → Refactor)

1. **Red** — Write a failing test.
2. **Green** — Write the minimum code to pass.
3. **Refactor** — Clean up without breaking tests.

**New Clarification:**  
Refactors must not change:
- Intent state transitions
- Confidence thresholds
- Autonomy guard behavior

## 3. Coverage Pact (Clarified)

- **Requirement:** 100% coverage on *new or modified lines*
- **Tooling:** coverage.py enforced in CI
- **Scope Expansion:**  
  - Agent orchestration logic
  - Confidence scoring logic
  - Autonomy decision paths
  - Chat handling branches

> “It’s just AI logic” is not an excuse.  
> If it can fail, it must be tested.

## 4. Testing Pyramid (Extended for AI Systems)

### Level 1 — Unit Tests (≈70%)
- Speed: <10ms
- Scope: Single function/class
- DB: Mocked
- AI: Mocked or cassette-replayed

**New Mandatory Unit Tests**
- Intent state transitions
- Confidence scoring math
- Autonomy gating logic

Example:
```python
def test_intent_enters_partial_state_when_required_field_missing():
    intent = resolve(signal_missing_weight)
    assert intent.state == "PARTIAL"
```

### Level 2 — Integration Tests (≈20%)
- Speed: <1s
- Real DB
- FRA_TEST_MODE=1 (no live LLM calls)

**New Required Coverage**
- Signal → Intent → Governance → Execution flow
- Partner-specific behavior via Signal Profiles
- Channel-specific ingestion differences

Example:
```python
def test_partner_autonomy_ceiling_blocks_auto_execution():
    partner.autonomy_ceiling = LEVEL_2
    result = executor.try_execute(intent, partner)
    assert result.executed is False
```

### Level 3 — Trace-Based Tests (≈10%)

**This remains a cornerstone capability.**

Enhancements:
- Trace replay must assert:
  - Output equality
  - Intent state
  - Confidence values
  - Execution decision

Example:
```python
def test_trace_replay_matches_production_decision():
    replay = replay_trace(trace_id)
    assert replay.execution_decision == "HUMAN_REVIEW"
```

## 5. Intent State & Incompleteness Testing (New Section)

Logistics data is frequently incomplete.

**This is normal — not an error.**

Required intent states:
- DRAFT
- PARTIAL
- CONFIRMED
- EXECUTING

Required tests:
```python
def test_partial_intent_never_executes():
    assert executor.can_execute(intent_partial) is False
```

## 6. Confidence, Trust & Autonomy Guardrails (New Section)

Execution decisions must always satisfy:

```
Intent Confidence × Partner Trust × Autonomy Ceiling
→ Execution Allowed?
```

Required tests:
```python
def test_low_confidence_blocks_execution_even_for_high_trust_partner():
    intent.confidence = 0.55
    partner.trust_score = 0.9
    partner.autonomy_ceiling = LEVEL_4
    assert executor.can_execute(intent, partner) is False
```

This prevents unsafe automation.

## 7. AI Determinism & Quality Controls (Extended)

### A. VCR Pattern (Reaffirmed)
- First run records
- Subsequent runs replay

### B. AI Output Contract Tests (New)

AI outputs must satisfy invariants:
- No hallucinated required fields
- Confidence < threshold if inferred

Example:
```python
def test_ai_does_not_hallucinate_weight():
    result = extractor.run(signal)
    assert result.weight is None or result.weight_confidence < 0.6
```

## 8. Conversational & Multi-Channel Testing (New)

Chat is a **first-class input**, not an edge case.

Required tests:
- Ambiguous messages
- Clarification loops
- Multi-turn context

Example:
```python
def test_chat_requires_clarification_for_missing_date():
    response = chat_agent.process("Pickup tomorrow LAX to SFO")
    assert response.requires_clarification is True
```

## 9. Performance & Latency Budgets (New)

For autonomous systems, **latency is correctness**.

Mandatory constraints:
- Intent resolution < 200ms
- Chat response < 1s
- Execution decision < 100ms

Example:
```python
def test_intent_resolution_latency():
    start = time.time()
    resolve(signal)
    assert time.time() - start < 0.2
```

## 10. Frappe-Specific Rules (Reaffirmed + Clarified)

- No raw SQL (`frappe.db.sql`) in business logic
- Hooks over core overrides
- Explicit atomic transactions when spanning DocTypes

**New:**  
All background workers must be testable without Redis/SQS running.

## 11. Autonomy Upgrade Tests (Critical)

Autonomy level increases must be **test-gated**.

Example:
```python
def test_partner_not_eligible_for_level_3_with_recent_disputes():
    assert autonomy_engine.can_upgrade(partner) is False
```

No test = no autonomy upgrade.

## 12. Architecture Coverage Matrix (New)

| Platform Layer | Test Coverage Required |
|--------------|-----------------------|
| Signal Ingestion | Unit + Integration |
| Intent Resolution | Unit + Integration |
| Partner Signal Profile | Integration |
| Confidence Engine | Unit |
| Autonomy Enforcement | Unit + Integration |
| Agent Runtime | Trace Tests |
| Governance Engine | Unit + Trace |
## Executive Summary (v9.1)
Antigravity Flowwolf Next is engineered to **prove safety** before automation. All code follows a strict TDD lifecycle, AI outputs are deterministic via VCR, and autonomy is gated by trust and ceiling.

## Performance & Latency Budgets (v9.1)
- **Intent resolution**: < 200 ms
- **Chat response**: < 1 s
- **Execution decision**: < 100 ms

## Feature‑Benefit Table (v9.1)
| Feature | Business Benefit |
| :--- | :--- |
| VCR‑capped AI calls | Predictable costs, no hallucinations |
| Autonomy Ceiling | Risk‑controlled scaling, clear pricing |
| Partner Signal Profile | Data‑quality driven trust, better SLA |
| Trace‑Based Tests | Auditable rollback, compliance evidence |

---

## 🔒 Naming Convention Charter (Immutable)

**Authority**: Engineering frozen rule  
**Source**: `33_NAMING_CONVENTION_SPEC_FW_VS_FLOWWOLF.md`

### The Golden Rule

> **Inside code = `fw`**  
> **Outside code = `Flowwolf`**  
> **Never mix within the same layer.**

### Quick Reference

| Layer | Pattern | Example |
|-------|---------|---------|
| **Execution** | `fw_*` | `fw_cortex`, `FW Intent Instance` |
| **Authority** | `Flowwolf *` | `Flowwolf Decision Contract` |

### Philosophy

- **`fw`** = Where things execute, evolve, and adapt (the river)
- **`Flowwolf`** = Where trust, contracts, and authority matter (the mountain)

**Enforcement**: Pre-commit hooks + CI linter mandatory.

See full spec: `33_NAMING_CONVENTION_SPEC_FW_VS_FLOWWOLF.md`

---

**Status**: Naming convention integrated into engineering charter.
