---
title: "Intent Library Definitions The Core Schema"
tags: []
version: "9.1"
last_updated: "2026-01-12"
---

# Intent Library: The Language of Autonomous Logistics

**Version**: 9.3 (Agentic Core)
**Context**: The Canonical Taxonomy of Intent Types.

---

## 🏗️ The Polymorphic "TenderLoad" (Universal)

The `TenderLoad` intent uses a **Stop-Based Architecture** and supports **Global Forwarding**.

### Base Structure
*   `intent_id`: UUID
*   `mode`: Enum (FTL, LTL, DRAYAGE, OCEAN_FCL, OCEAN_LCL, AIR)
*   `incoterms`: Enum (FOB, EXW, CIF, DDP, DAP) **(Critical for Intl)**
*   `stops`: List[Stop]
*   `payload`: Polymorphic Details

---

### 🚛 Domestic Variants (Surface)

#### Variant A: FTL (Full Truckload)
*   **Focus**: Equipment, Temp, Team Driver.
*   **Schema**: `equipment_type`, `temp_control`, `driver_assist`.

#### Variant B: LTL (Less Than Truckload)
*   **Focus**: NMFC, Accessorials.
*   **Schema**: `freight_class`, `liftgate`, `inside_delivery`.

#### Variant C: Drayage (Port Moves)
*   **Focus**: Container Constraints.
*   **Schema**: `container_no`, `chassis_type`, `cut_off_date`.

---

### ✈️ International Variants (Forwarding)

#### Variant D: Ocean FCL (Full Container Load)
*   **Focus**: Container & Booking.
*   **Schema**:
    *   `booking_number`: String (SSL Booking)
    *   `mbl_number`: String (Master Bill of Lading)
    *   `container_type`: "40HQ", "20GP", "45REEFER"
    *   `vessel_voyage`: "Maersk Kensington / 213W"

#### Variant E: Ocean LCL (Less Than Container)
*   **Focus**: Consolidation.
*   **Schema**:
    *   `hbl_number`: String (House Bill of Lading)
    *   `cbm`: Float (Cubic Meters)
    *   `cfs_location`: String (Container Freight Station)

#### Variant F: Air Freight
*   **Focus**: Speed & Chargeable Weight.
*   **Schema**:
    *   `awb_number`: String (MAWB / HAWB)
    *   `service_level`: "Next Flight Out", "Deferred", "Consol"
    *   `uld_type`: "LD3", "Loose"
    *   `screening_required`: Boolean (TSA/KSMS)

---

## 📋 The Updated "Intent Schema" (Pydantic Base)

```python
class BaseIntent(BaseModel):
    intent_id: UUID
    intent_type: str
    
    # Global Context
    incoterms: Optional[Incoterm]  # e.g., "FOB"
    commercial_invoice_value: Optional[Money]
    
    # The Route
    stops: List[Stop]
    
    # The Payload (Polymorphic Union)
    payload: Union[
        FTLTender, LTLTender, DrayageTender,
        OceanFCLTender, OceanLCLTender, AirTender
    ]
```

**Verdict**: The system covers domestic surface (FTL/LTL) and global forwarding (Air/Ocean), unifying them under a single `TenderLoad` intent with polymorphic payloads.

## 🌍 Global Party Definitions (v9.1 Patch)

International freight requires defining parties beyond "Sender/Receiver".

### The `involved_parties` List
Every BaseIntent includes dynamic parties:
*   **Customs Broker**: (Critical for DDP/DAP)
*   **Notify Party**: (Who gets the arrival notice?)
*   **Bill To**: (Who pays the freight?)

```python
class InvolvedParty(BaseModel):
    role: Literal["CUSTOMS_BROKER", "NOTIFY_PARTY", "BILL_TO", "CONSOLIDATOR"]
    entity_id: EntityID
```

**Verdict**: This ensures that when an Ocean shipment arrives, we know who to call for Customs Clearance.

## 🤖 Autonomous Asset Definitions (v9.1 Patch)

To support Level 4/5 Autonomous Trucks (AVs), we must define asset capability.

### FTL Variant Update
*   `autonomous_level`: Enum (NONE, HUMAN_ASSIST, HIGHWAY_AUTONOMY, FULL_AUTONOMY)
*   **Implication**:
    *   If `HIGHWAY_AUTONOMY`: System looks for "Transfer Hub" stops.
    *   If `FULL_AUTONOMY`: System ignores "Driver Sleep" constraints in scheduling.

### The "Transfer Hub" Stop Type
*   New `StopType`: **HANDOFF**
*   **Logic**: A dedicated stop where the trailer is swapped from an AV Tractor to a Human Day-Cab.
*   **Intent**: `TenderLoad` must support splitting one shipment into 3 legs (Human -> AV -> Human).
## Partner Signal Profile (v9.1)

The **Partner Signal Profile** captures behavioral contracts for each partner.

| Field | Type | Description |
| :--- | :--- | :--- |
| `trust_score` | float (0‑1) | Dynamic trust based on historical accuracy. |
| `data_quality_score` | float (0‑1) | Quality of signals sent by the partner. |
| `autonomy_ceiling` | int (0‑5) | Maximum automation level allowed. |
| `preferred_channel` | string | Preferred ingestion channel (e.g., "EDI 204", "Email PDF"). |
| `preferred_format` | string | JSON, XML, PDF, etc. |

### Example JSON
```json
{
  "partner_id": "P12345",
  "trust_score": 0.92,
  "data_quality_score": 0.87,
  "autonomy_ceiling": 4,
  "preferred_channel": "EDI 204",
  "preferred_format": "X12"
}
```

---

## Intent Versioning & Upcasting (GAP-I1 Fix)

### Version Strategy

**Intent Definitions are immutable and versioned**:
- Each change creates a new version (v4 → v5)
- Old versions remain readable (never deleted)
- Upcasting functions convert old → new

### Upcasting Interface

```python
from abc import ABC, abstractmethod
from typing import Dict

class IntentUpcaster(ABC):
    """
    Converts old Intent payloads to new schema versions.
    
    Example: TenderLoad v3 → v4 adds 'special_instructions' field.
    """
    
    @abstractmethod
    def upcast(self, old_payload: Dict, from_version: int, to_version: int) -> Dict:
        """
        Convert payload from old version to new version.
        
        Args:
            old_payload: The v3 payload
            from_version: Source version (e.g., 3)
            to_version: Target version (e.g., 4)
        
        Returns:
            Dict: The v4 payload with new fields added
        
        Example:
            >>> upcaster = TenderLoadUpcaster()
            >>> v3_payload = {"origin": "LAX", "destination": "SFO"}
            >>> v4_payload = upcaster.upcast(v3_payload, 3, 4)
            >>> assert "special_instructions" in v4_payload
        """
        pass

class TenderLoadUpcaster(IntentUpcaster):
    """Upcast TenderLoad from any version to latest."""
    
    def upcast(self, old_payload: Dict, from_version: int, to_version: int) -> Dict:
        """Convert TenderLoad v3 → v4."""
        if from_version == 3 and to_version == 4:
            # v4 adds 'special_instructions' field
            return {
                **old_payload,
                "special_instructions": None  # Default for upgraded intents
            }
        elif from_version == 4 and to_version == 5:
            # Future: v5 might add 'priority' field
            return {
                **old_payload,
                "priority": "STANDARD"
            }
        else:
            raise ValueError(f"No upcaster for {from_version} → {to_version}")
```

### Migration Workflow

When you upgrade an Intent schema:

1. **Create new IntentDefinition** (v4)
   ```python
   new_def = frappe.get_doc({
       "doctype": "Intent Definition",
       "name": "TenderLoad",
       "version": 4,
       "schema": {...},  # New schema with 'special_instructions'
       "created_at": now()
   })
   new_def.insert()
   ```

2. **Register Upcaster**
   ```python
   from cortex_ag_ai.intent.versioning import register_upcaster
   register_upcaster("TenderLoad", TenderLoadUpcaster())
   ```

3. **Old Intents Are Auto-Upgraded on Read**
   ```python
   # When you load a v3 Intent...
   intent = frappe.get_doc("Intent Instance", "old-intent-123")
   
   # System detects version mismatch
   if intent.definition_version < CURRENT_VERSION:
       upcaster = get_upcaster(intent.intent_name)
       intent.payload = upcaster.upcast(
           intent.payload,
           from_version=intent.definition_version,
           to_version=CURRENT_VERSION
       )
       intent.definition_version = CURRENT_VERSION
       intent.save()  # Persist the upgrade
   ```

### Backward Compatibility Rules

1. **Old intents are never invalidated** (append-only)
2. **Upcasters must be idempotent** (can run multiple times safely)
3. **New fields must have sensible defaults** (None, null, or inferred)
4. **Breaking changes are NOT allowed** (fork to new Intent type instead)

---

**Status**: Intent versioning strategy defined.
