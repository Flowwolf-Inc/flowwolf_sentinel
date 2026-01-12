# Demo Infrastructure Specification

**Purpose**: Week 1 deliverable - The demo that sells  
**Deadline**: January 11, 2026  
**Status**: Implementation spec ready

---

## Demo Scenario

**Story**: "ABC Logistics receives EDI 204 from Walmart"

**Persona**: Operations Manager at mid-size 3PL  
**Pain**: Manual EDI processing, 2 FTE needed, error-prone  
**Promise**: Flowwolf reduces to $0.10/load, 95% automated

---

## Demo Environment Setup

### Infrastructure

```yaml
# demo-stack.yml
version: '3.8'
services:
  flowwolf-demo:
    image: frappe/frappe:v15
    environment:
      - SITE_NAME=demo.flowwolf.ai
      - DB_HOST=demo-db
      - REDIS_CACHE=demo-redis:6379
    ports:
      - "8080:8000"
    volumes:
      - ./apps/fw_cortex:/home/frappe/frappe-bench/apps/fw_cortex
      - ./apps/fw_fluent:/home/frappe/frappe-bench/apps/fw_fluent
      - ./apps/fw_motion:/home/frappe/frappe-bench/apps/fw_motion
  
  demo-db:
    image: mariadb:10.6
    environment:
      - MYSQL_ROOT_PASSWORD=demo123
      - MYSQL_DATABASE=flowwolf_demo
  
  demo-redis:
    image: redis:alpine
```

**Deployment**:
```bash
docker-compose -f demo-stack.yml up -d
bench --site demo.flowwolf.ai install-app fw_cortex
bench --site demo.flowwolf.ai install-app fw_fluent
bench --site demo.flowwolf.ai install-app fw_motion
./scripts/seed_demo_data.sh
```

---

## Demo Data (Pre-Loaded)

### Test Partner: ABC Logistics

```python
# scripts/seed_demo_data.sh
#!/bin/bash

bench --site demo.flowwolf.ai run-script << 'PYTHON'
import frappe

# Create demo partner
partner = frappe.get_doc({
    "doctype": "Partner",
    "partner_name": "ABC Logistics",
    "partner_id": "DEMO-ABC-001",
    "email": "ops@abclogistics.demo",
    "autonomy_level": "L1",  # Start at visibility
    "trust_score": 0.5,  # New partner
})
partner.insert()

# Create autonomy contract
contract = frappe.get_doc({
    "doctype": "Flowwolf Autonomy Contract",
    "partner": partner.name,
    "autonomy_level": "L1",
    "decision_mode": "OBSERVE_ONLY",
    "pricing_tier": "Entry",
    "monthly_fee": 500
})
contract.insert()

frappe.db.commit()
print("✅ Demo partner created")
PYTHON
```

### Sample EDI Files

**File 1: FTL Load (Simple)**
```
# demo_data/edi/204_ftl_walmart.edi
ISA*00*          *00*          *ZZ*WALMART        *ZZ*ABC_LOGISTICS  *260108*0945*U*00401*000000001*0*P*>~
GS*SM*WALMART*ABC_LOGISTICS*20260108*0945*1*X*004010~
ST*204*0001~
B2**PP**WALMART~
B2A*04*STANDARD~
MS3*ABC_LOGISTICS*XX*123456~
NTE*GEN*Palletized freight, fragile items~
N1*SH*Walmart DC 6012*93*006012~
N3*1000 Walmart Way~
N4*Bentonville*AR*72712~
G62*86*20260115~
N1*CN*Target Store 1849*93*001849~
N3*500 Main Street~
N4*Chicago*IL*60601~
G62*17*20260117~
SE*15*0001~
GE*1*1~
IEA*1*000000001~
```

**File 2: LTL Load (Complex)**
```
# demo_data/edi/204_ltl_multi_stop.edi
[Similar structure, 3 stops, 5 pallets]
```

**File 3: Ocean Load (International)**
```
# demo_data/edi/204_ocean_container.edi
[Container load, customs info, SCAC codes]
```

---

## Demo Flow (Step-by-Step)

### Step 1: Upload EDI (10 seconds)

**UI**: Drag-and-drop widget
```
┌─────────────────────────────────────┐
│  📄 Upload EDI File                 │
│                                     │
│  [Drag file here or click to browse]│
│                                     │
│  ✅ Supported: EDI 204, 990, 214   │
└─────────────────────────────────────┘
```

**Backend**:
```python
@frappe.whitelist()
def upload_edi_demo(file_content):
    """Demo upload handler"""
    signal = frappe.get_doc({
        "doctype": "FW Signal",
        "partner": "ABC Logistics",
        "signal_type": "EDI_204",
        "raw_content": file_content,
        "trace_id": f"trace-{uuid.uuid4()}"
    })
    signal.insert()
    
    # Trigger Intent extraction (async)
    enqueue("fw_cortex.intent.extract", signal=signal.name)
    
    return {"signal_id": signal.name, "trace_id": signal.trace_id}
```

---

### Step 2: Intent Extraction (10 seconds)

**UI**: Real-time progress
```
┌─────────────────────────────────────┐
│  🧠 Extracting Intent...            │
│                                     │
│  ████████████░░░░░░ 75%            │
│                                     │
│  ✓ Parsed EDI structure            │
│  ✓ Identified TenderLoad intent    │
│  ⏳ Validating coordinates...      │
└─────────────────────────────────────┘
```

**Backend** (Simulated for demo):
```python
def extract_intent_demo(signal):
    """Demo: Pre-computed result for speed"""
    # In real system: Call OpenAI, run Pydantic validation
    # In demo: Return pre-baked result
    
    intent = frappe.get_doc({
        "doctype": "FW Intent Instance",
        "signal": signal.name,
        "intent_type": "TenderLoad",
        "confidence": 0.94,  # High confidence
        "payload": json.dumps({
            "origin": {
                "name": "Walmart DC 6012",
                "city": "Bentonville",
                "state": "AR",
                "zip": "72712"
            },
            "destination": {
                "name": "Target Store 1849",
                "city": "Chicago",
                "state": "IL",
                "zip": "60601"
            },
            "pickup_date": "2026-01-15",
            "delivery_date": "2026-01-17",
            "weight": 20000,
            "pieces": 20
        }),
        "state": "PARTIAL"  # Needs approval (L1 partner)
    })
    intent.insert()
    return intent
```

---

### Step 3: Display Intent + Confidence (5 seconds)

**UI**: Intent card
```
┌─────────────────────────────────────────────┐
│  ✅ Intent Extracted: TenderLoad             │
│                                             │
│  Confidence: ███████████░ 94%               │
│                                             │
│  📍 Origin:                                 │
│     Walmart DC 6012                         │
│     Bentonville, AR 72712                   │
│                                             │
│  📍 Destination:                            │
│     Target Store 1849                       │
│     Chicago, IL 60601                       │
│                                             │
│  📅 Pickup: Jan 15, 2026                    │
│  📅 Delivery: Jan 17, 2026                  │
│                                             │
│  📦 Weight: 20,000 lbs (20 pieces)          │
│                                             │
│  🤖 Autonomy Recommendation: L2             │
│     (Needs approval - partner at L1)        │
│                                             │
│  [Approve & Create Load] [Reject] [Edit]   │
└─────────────────────────────────────────────┘
```

---

### Step 4: Autonomy Level Explanation (5 seconds)

**UI**: Educational overlay
```
┌─────────────────────────────────────────────┐
│  🪜 Your Autonomy Journey                    │
│                                             │
│  Current Level: L1 (Visibility)             │
│  ✓ We extract intents                      │
│  ✓ You approve all actions                 │
│                                             │
│  Next Level: L2 (Assisted Execution)        │
│  ↑ Unlock after 30 days, 95% accuracy      │
│  💰 Price: $500 → $1,000/month             │
│  💡 Value: 50% time savings                │
│                                             │
│  [See Upgrade Path] [Not Now]              │
└─────────────────────────────────────────────┘
```

---

### Step 5: Approve → Load Created (5 seconds)

**User Action**: Click "Approve & Create Load"

**Backend**:
```python
@frappe.whitelist()
def approve_intent_demo(intent_id):
    """Demo approval flow"""
    intent = frappe.get_doc("FW Intent Instance", intent_id)
    
    # Create load in Motion
    load = frappe.get_doc({
        "doctype": "Flowwolf Shipment Load",
        "load_id": f"LOAD-{datetime.now().strftime('%Y%m%d')}-001",
        "partner": intent.partner,
        "origin_city": "Bentonville",
        "origin_state": "AR",
        "destination_city": "Chicago",
        "destination_state": "IL",
        "pickup_date": "2026-01-15",
        "delivery_date": "2026-01-17",
        "status": "Tendered",
        "trace_id": intent.trace_id
    })
    load.insert()
    
    # Update intent
    intent.state = "EXECUTED"
    intent.execution_result = load.name
    intent.save()
    
    return {"load_id": load.name, "success": True}
```

**UI**: Success message
```
┌─────────────────────────────────────────────┐
│  ✅ Load Created Successfully!               │
│                                             │
│  Load ID: LOAD-20260108-001                 │
│  Status: Tendered                           │
│                                             │
│  ⏱️  Process Time: 25 seconds                │
│  💰 Cost: $0.10 (vs $2.00 manual)           │
│                                             │
│  [View Load Details] [Process Another]     │
└─────────────────────────────────────────────┘
```

---

### Step 6: ROI Calculator (5 seconds)

**UI**: Savings widget
```
┌─────────────────────────────────────────────┐
│  💰 Your Potential Savings                   │
│                                             │
│  Current Process:                           │
│  • Manual EDI processing: 2 FTE             │
│  • Cost per load: $2.00                     │
│  • Monthly volume: 1,000 loads              │
│  • Total cost: $2,000/month (labor only)    │
│                                             │
│  With Flowwolf (L2):                        │
│  • Automated: 95%                           │
│  • Cost per load: $0.10                     │
│  • Monthly cost: $100 + $1,000 platform     │
│  • Total cost: $1,100/month                 │
│                                             │
│  💵 Monthly Savings: $900 (45%)             │
│  📈 Annual Savings: $10,800                 │
│  ⏰ Breakeven: 1.1 months                   │
│                                             │
│  [📊 See Detailed ROI] [📧 Email Quote]     │
└─────────────────────────────────────────────┘
```

---

## Demo Script (Presenter Notes)

### Opening (30 seconds)

> "Thanks for joining. I'm [Name] from Flowwolf.  
> 
> You're probably spending $4,000-$8,000/month on EDI teams.  
> What if AI could handle 95% of that?  
> 
> Let me show you. This is a real EDI 204 from Walmart..."

### Upload (15 seconds)

> "Watch this. I'm uploading an EDI file.  
> [Drag file]  
> In legacy systems, someone would manually key this into your TMS.  
> That person costs you $2 per load.  
> 
> Flowwolf extracts the intent automatically..."

### Extraction (20 seconds)

> "See this? 94% confidence.  
> That means our AI is sure this is a load tender.  
> Origin: Bentonville. Destination: Chicago.  
> All the details extracted perfectly.  
> 
> Now here's the key difference..."

### Autonomy Levels (45 seconds)

> "Notice it says 'Needs Approval'?  
> That's because this is a Level 1 account — visibility only.  
> 
> At Level 2, we'd auto-draft this for you.  
> At Level 3, we'd auto-execute within confidence thresholds.  
> 
> You earn higher levels over time. Trust is built, not given.  
> 
> For now, you approve. Click."

### Approval (15 seconds)

> "[Click Approve]  
> Done. 25 seconds total.  
> Cost: 10 cents.  
> 
> Your current process? 5 minutes, $2per load.  
> That's 20× faster, 95% cheaper."

### ROI (45 seconds)

> "Let's talk numbers.  
> If you process 1,000 loads/month...  
> [Show calculator]  
> 
> Current cost: $2,000 in labor.  
> Flowwolf cost: $1,100 (platform + per-load).  
> 
> You save $900/month, $10,800/year.  
> 
> And that's at Level 2. At Level 3, savings double.  
> 
> Questions?"

---

## Fallback Scenarios

### What if demo breaks?

**Backup Plan 1**: Pre-recorded video (2 minutes)
**Backup Plan 2**: Screenshots + narrative
**Backup Plan 3**: Live coding (show code, explain flow)

### What if prospect asks "What about my TMS?"

> "Great question. Flowwolf integrates with McLeod, TMW, and 15+ others.  
> We provide the API, you give us credentials.  
> Setup takes 1 week, we handle it."

### What if they say "Too expensive"?

> "Let's recalculate. How many loads/month?  
> [Adjust calculator]  
> If you're below 100 loads/month, you're right—not economical yet.  
> But at 500+, you're leaving $5K/month on the table."

---

## Success Metrics

**Demo is successful if**:
- ✅ Prospect stays for full 30 minutes
- ✅ Asks "How do we get started?" (buying signal)
- ✅ Books follow-up call within 7 days
- ✅ Introduces us to CFO/CEO (budget holder)

**Demo fails if**:
- ❌ Prospect leaves after 10 minutes (not engaged)
- ❌ Says "Interesting, we'll think about it" (no commitment)
- ❌ Asks for proposal (sending to procurement = dead)

---

## Implementation Checklist

**By Jan 10**:
- [ ] Spin up demo.flowwolf.ai (Docker Compose)
- [ ] Install 3 apps (fw_cortex, fw_fluent, fw_motion)
- [ ] Seed ABC Logistics partner
- [ ] Upload 3 sample EDI files
- [ ] Test full flow 5 times (catch bugs)

**By Jan 11**:
- [ ] Rehearse demo (CEO + Engineer)
- [ ] Time each step (should be < 5 min total)
- [ ] Record backup video (in case live fails)
- [ ] Create demo PDF (email to prospects after)

---

**Status**: Spec complete. Ready for implementation.  
**Owner**: Engineering + Sales  
**Deadline**: Jan 11, 2026 (Sunday)

---

**"The demo that sells is the demo that works."** 🎬
