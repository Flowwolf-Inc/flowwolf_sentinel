# App Skeleton Template (fw Naming)

**Version**: 9.4.2 (Frozen)  
**Naming Convention**: `fw_*` for all apps (see `33_NAMING_CONVENTION_SPEC`)  
**Purpose**: Standard directory structure

---

## App 1: fw_cortex (The Brain)

```
fw_cortex/
├── fw_cortex/
│   ├── intent/library.py            # Intent schemas (TenderLoad, etc.)
│   ├── governance/engine.py         # GovernanceEngine
│   ├── agents/base.py               # AgentContract ABC
│   ├── core/doctype/
│   │   ├── fw_intent_instance/      # Runtime intent data
│   │   ├── flowwolf_intent_definition/  # Authority (schema contract)
│   │   ├── flowwolf_decision_contract/  # Authority (policy)
│   │   └── flowwolf_partner_agreement/  # Authority (trust contract)
│   ├── tests/
│   └── fixtures/vcr_cassettes/
```

## App 2: fw_fluent (The Translator)

```
fw_fluent/
├── fw_fluent/
│   ├── plugins/                     # X12, EDIFACT, JSON, Email
│   ├── ingest/normalizer.py         # Signal normalization
│   ├── api/v1/ingest.py             # /api/fw/fluent/v1/ingest
│   ├── core/doctype/
│   │   ├── fw_signal/               # Execution (raw signal storage)
│   │   └── fw_circuit_breaker/      # Execution (circuit state)
│   └── tests/
```

## App 3: fw_motion (The Body)

```
fw_motion/
├── fw_motion/
│   ├── agents/shipment_booking.py
│   ├── core/doctype/
│   │   ├── flowwolf_shipment_load/  # Authority (customer-facing)
│   │   ├── fw_stop/                 # Execution (runtime state)
│   │   └── fw_execution_result/     # Execution (agent output)
│   ├── ui/IntentGraph.vue
│   └── tests/
```

---

## Init Commands (Updated Names)

```bash
# Create apps with fw_ prefix
bench new-app fw_cortex
bench new-app fw_fluent
bench new-app fw_motion

# Install apps
bench --site development.localhost install-app fw_cortex
bench --site development.localhost install-app fw_fluent
bench --site development.localhost install-app fw_motion
```

---

## DocType Naming (Layer-Aware)

### Execution Layer (`FW *`)
- `FW Intent Instance` - Runtime intent data
- `FW Signal` - Raw signal storage
- `FW Circuit Breaker` - Circuit state
- `FW Execution Result` - Agent outputs
- `FW Stop` - Runtime stop data

### Authority Layer (`Flowwolf *`)
- `Flowwolf Intent Definition` - Canonical schema (immutable)
- `Flowwolf Decision Contract` - Governance policy
- `Flowwolf Partner Agreement` - Trust contract
- `Flowwolf Shipment Load` - Customer-facing load

---

**See**: `33_NAMING_CONVENTION_SPEC_FW_VS_FLOWWOLF.md` for full naming rules.
