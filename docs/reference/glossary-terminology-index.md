---
title: "Glossary Terminology Index"
tags: []
version: "9.1"
last_updated: "2026-01-12"
---

# Glossary of Terms

**Version**: 9.4 (Agentic Core)
**Purpose**: Canonical definitions of all Antigravity Flowwolf Autonomous terminology

---

## Core Concepts

### Agent Contract
An interface that executes Intents with governance. All writes to the Motion database must go through an AgentContract (never directly from an Intent).

```python
class AgentContract(ABC):
    async def execute(self, intent: IntentInstance) -> ExecutionResult
    def can_execute(self, intent: IntentInstance, partner: Partner) -> bool
```

### Autonomy Ceiling
Maximum automation level (0-5) allowed for a specific partner. Defined in the Partner Signal Profile.

| Level | Name | Description |
|-------|------|-------------|
| 0 | Observe | Read-only, no writes |
| 1 | Extract | Parse to Draft (human must save) |
| 2 | Suggest | Create draft logic (human must submit) |
| 3 | Auto-Confirm | Execute if confidence > 99% |
| 4 | Auto-Execute | Execute if confidence > 90% |
| 5 | Negotiate | Agent-to-Agent negotiation allowed |

### Autonomy Tier
Commercial pricing tier corresponding to autonomy ceiling:
- **Assist** (L1) = Standard SaaS pricing
- **Co-Pilot** (L2) = Per-seat + usage fee
- **Autonomous Ops** (L4) = Platform fee + autonomy surcharge
- **Agentic Network** (L5) = Network access fee

---

## Architecture Components

### Circuit Breaker
A protective mechanism that stops processing signals from a misbehaving partner after N failures within a time window. Prevents one bad partner from affecting the entire system.

### Cortex_AG_AI
The "Brain" app. Contains:
- Intent Graph (DAG of Intent nodes)
- Entity Resolution (location/carrier matching)
- Governance Engine (policy enforcement)

### Decision Contract
A policy rule that governs whether an Intent can be executed. Example:
```json
{
  "rule_id": "no_hazmat_auto_dispatch",
  "condition": "intent.payload.hazmat == true",
  "action": "BLOCK"
}
```

### Fluent_AG_AI
The "Translator" app. Handles:
- Signal Ingestion (EDI, Email, API, Phone)
- Protocol Adapters (X12, EDIFACT, JSON)
- Signal Normalization (idempotency keys, trace IDs)

### Motion_AG_AI
The "Body" app. Contains:
- TMS business logic
- Shipment Load DocType
- Execution workflows

---

## Data Model

### Intent Definition
The immutable schema/rules for an Intent type (versioned, append-only).

```python
{
  "name": "TenderLoad",
  "version": 4,
  "schema": { /* JSON Schema */ },
  "created_at": "2026-01-01T00:00:00Z"
}
```

### Intent Instance
Runtime data for a specific Intent (mutable state).

```python
{
  "id": "uuid-123",
  "definition_id": "TenderLoad:v4",
  "state": "CONFIRMED",  # DRAFT, PARTIAL, CONFIRMED, EXECUTING, DONE, FAILED
  "payload": { "origin": "LAX", "destination": "SFO" },
  "confidence": 0.95,
  "trace_id": "trace-456"
}
```

### Intent Graph
A directed acyclic graph (DAG) of Intent nodes showing dependencies. Example: `TenderLoad` → `AcceptLoad` → `Dispatch` → `UpdateStatus`.

---

## Governance & Trust

### Partner Signal Profile
A behavioral contract defining how to interact with a specific partner.

| Field | Type | Description |
|-------|------|-------------|
| `trust_score` | float (0-1) | Historical accuracy of signals |
| `data_quality_score` | float (0-1) | % of signals with all required fields |
| `autonomy_ceiling` | int (0-5) | Max automation level allowed |
| `preferred_channel` | string | EDI 204, Email PDF, API, etc. |

### Trace ID
A UUID that identifies a single request as it flows through the system (Signal → Intent → Agent → Load). Used for debugging and audit trails.

Format: `trace-<uuid>` (e.g., `trace-12345678-abcd-1234-5678-abcdef012345`)

---

## Testing & Quality

### Cassette (VCR)
A recorded snapshot of an AI model's response, used to replay tests deterministically without calling the live model.

```yaml
# fixtures/vcr_cassettes/test_extract_ftl.yaml
request:
  prompt: "Extract origin and destination from: Pickup LAX deliver SFO"
response:
  origin: "LAX"
  destination: "SFO"
  confidence: 0.95
```

### Hypothesis (Property-Based Testing)
A library that generates random test inputs to verify invariants. Example:
```python
from hypothesis import given, strategies as st

@given(weight=st.floats(min_value=0.1, max_value=100000))
def test_weight_always_positive(weight):
    intent = TenderLoad(weight=weight, ...)
    assert intent.weight > 0
```

### Trace Replay Test
A test that replays a production trace (given a trace_id) and asserts the output matches the original result. Used for regression testing.

```python
def test_trace_replay_12345():
    result = replay_trace("trace-12345")
    assert result.execution_decision == "HUMAN_REVIEW"
```

---

## Signal Processing

### Idempotency Key
A unique identifier (UUID) sent in `X-Idempotency-Key` header to prevent duplicate processing of the same signal. TTL = 24 hours in Redis.

### Normalized Signal
The standard format that all incoming signals (EDI, Email, API) are converted to before processing.

```python
{
  "idempotency_key": "uuid-abc",
  "trace_id": "trace-def",
  "content_type": "application/json",
  "payload": { /* raw signal data */ },
  "partner_id": "P12345"
}
```

### Signal
Any input to the system: EDI file, email, API call, phone transcript, etc.

---

## Execution & Workflow

### Execution Result
The output of an AgentContract's `execute()` method.

```python
{
  "success": true,
  "load_id": "LOAD-001",
  "error": null,
  "audit_trail": [ /* list of actions taken */ ]
}
```

### Polymorphic Payload
The `TenderLoad` Intent supports multiple transport modes (FTL, LTL, Ocean, Air) via a discriminated union:

```python
payload: Union[FTLPayload, LTLPayload, OceanFCLPayload, AirPayload]
```

---

## Commercial Terms

### Decision Meter
A billing metric that counts autonomous decisions made by the system (used for "per-execution" pricing).

### Network Effect
The value increase of the OS as more partners join (shared Global Entity Graph improves resolution quality for everyone).

### Skill Marketplace
A future feature where third-party developers can publish custom agents (e.g., "Customs Clearance Agent") and earn revenue share.

---

## Acronyms

- **A2A**: Agent-to-Agent (negotiation protocol)
- **DAG**: Directed Acyclic Graph
- **EDI**: Electronic Data Interchange
- **ERD**: Entity Relationship Diagram
- **FCL**: Full Container Load (ocean freight)
- **FTL**: Full Truckload
- **LCL**: Less than Container Load
- **LTL**: Less than Truckload
- **RPO**: Recovery Point Objective (max acceptable data loss)
- **RTO**: Recovery Time Objective (max acceptable downtime)
- **TAM**: Total Addressable Market
- **TDD**: Test-Driven Development
- **TMS**: Transportation Management System
- **VCR**: Video Cassette Recorder (pattern name for recording/replaying API calls)

---

**Status**: Living document. Update when new terms are introduced.

---

## Trace ID Specification (GAP-I4 Fix)

### Standard Format

**Format**: `trace-{uuid4}`  
**Example**: `trace-550e8400-e29b-41d4-a716-446655440000`  
**Generation**: Python's `uuid.uuid4()`

### Usage

```python
import uuid

def generate_trace_id() -> str:
    """Generate a new trace ID for request tracking."""
    return f"trace-{uuid.uuid4()}"

# Example
trace_id = generate_trace_id()
# Output: "trace-a1b2c3d4-e5f6-7890-abcd-ef1234567890"
```

### Propagation Rules

1. **HTTP Headers**: `X-Trace-ID: trace-{uuid}`
2. **DocType Field**: All Intent/Signal/Load docs have `trace_id` (Data, indexed)
3. **Logs**: All log statements include `trace_id` in structured logging
   ```python
   logger.info("Processing intent", extra={"trace_id": trace_id})
   ```

### Trace Lifecycle

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Signal    │ ───> │   Intent    │ ───> │    Load     │
│ (trace-123) │      │ (trace-123) │      │ (trace-123) │
└─────────────┘      └─────────────┘      └─────────────┘
```

Same `trace_id` flows through entire pipeline for correlation.

### Querying by Trace ID

```python
# Find all objects in a trace
signals = frappe.get_all("Signal", filters={"trace_id": "trace-123"})
intents = frappe.get_all("Intent Instance", filters={"trace_id": "trace-123"})
loads = frappe.get_all("Shipment Load", filters={"trace_id": "trace-123"})

# Reconstruct entire flow
print(f"Trace {trace_id}: {len(signals)} signals → {len(intents)} intents → {len(loads)} loads")
```

---

**Status**: Trace ID format standardized.
