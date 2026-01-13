---
title: "Sales Tools Package"
tags: []
version: "9.1"
last_updated: "2026-01-12"
---

# Sales Tools Package

**Purpose**: Enable sales from day 1  
**Contents**: Pricing calculator, FDP outreach, objection handling  
**Status**: Ready to use

---

## Tool 1: Pricing Calculator (GAP-S2 Fix)

### Interactive Calculator (Google Sheet)

**Sheet URL**: `https://docs.google.com/spreadsheets/d/FLOWWOLF_PRICING_CALC`

**Tab 1: Quick Quote**
```
┌─────────────────────────────────────────────┐
│  Flowwolf Pricing Calculator v9.1            │
│─────────────────────────────────────────────│
│                                             │
│  Company Name: [_______________________]    │
│  Monthly Load Volume: [_______] loads       │
│                                             │
│  Intent Types (check all):                  │
│  ☑ Invoice Processing                       │
│  ☑ Load Planning                            │
│  ☐ Tracking Updates                         │
│  ☐ Claims & Disputes                        │
│                                             │
│  Desired Autonomy Level:                    │
│  ○ L1 - Visibility Only                     │
│  ● L2 - Assisted Execution                  │
│  ○ L3 - Conditional Autonomy                │
│                                             │
│───────────────────────────────────────────│
│  MONTHLY PRICING                            │
│───────────────────────────────────────────│
│  Platform Base:           $200              │
│  Invoice Processing (L2): $600              │
│  Load Planning (L2):      $800              │
│───────────────────────────────────────────│
│  Total Flowwolf Cost:     $1,600/month      │
│                                             │
│  Current EDI Cost:        $8,000/month      │
│  (2 FTE × $4,000)                           │
│                                             │
│  Monthly Savings:         $6,400 (80%)      │
│  Annual Savings:          $76,800           │
│  Breakeven Period:        < 1 month         │
│───────────────────────────────────────────│
│  [Generate PDF Quote] [Email to Prospect]  │
└─────────────────────────────────────────────┘
```

**Formula Logic**:
```
Platform Base = $200-$500 (based on volume)

Per Intent = Volume Metric × Autonomy Multiplier × Base Rate

Base Rates:
- Invoice Processing: $0.30/transaction
- Load Planning: $0.50/load
- Tracking: $0.10/update
- Claims: $2.00/claim

Autonomy Multipliers:
- L1: 1.0×
- L2: 2.0×
- L3: 4.0×
- L4: 7.0×
- L5: 12.0×

Example (1,000 loads/month at L2):
  Platform Base: $200
  Invoice (1000 × $0.30 × 2.0): $600
  Load Planning (1000 × $0.50 × 2.0): $1,000
  Total: $1,800/month
```

---

### Embedded Calculator (Website Widget)

**HTML/JavaScript** (for flowwolf.ai/calculator):

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flowwolf Pricing Calculator</title>
    <style>
        .calculator {
            max-width: 600px;
            margin: 50px auto;
            padding: 30px;
            border: 2px solid #2563eb;
            border-radius: 10px;
            font-family: Inter, sans-serif;
        }
        .result {
            background: #f0f9ff;
            padding: 20px;
            margin-top: 20px;
            border-radius: 5px;
        }
        .savings {
            color: #16a34a;
            font-size: 24px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h2>Calculate Your Savings</h2>
        
        <label>Monthly Load Volume:</label>
        <input type="number" id="volume" value="1000" min="100">
        
        <label>Current EDI Team Size:</label>
        <input type="number" id="team_size" value="2" min="0">
        
        <label>Avg Salary per Person:</label>
        <input type="number" id="salary" value="4000" min="3000">
        
        <button onclick="calculate()">Calculate Savings</button>
        
        <div class="result" id="result" style="display:none;">
            <h3>Your Numbers</h3>
            <p>Current Monthly Cost: $<span id="current_cost"></span></p>
            <p>Flowwolf Monthly Cost: $<span id="flowwolf_cost"></span></p>
            <p class="savings">Monthly Savings: $<span id="savings"></span></p>
            <p>Annual Savings: $<span id="annual_savings"></span></p>
            <p>ROI: <span id="roi"></span>%</p>
        </div>
    </div>
    
    <script>
        function calculate() {
            const volume = parseInt(document.getElementById('volume').value);
            const teamSize = parseInt(document.getElementById('team_size').value);
            const salary = parseInt(document.getElementById('salary').value);
            
            // Current cost
            const currentCost = teamSize * salary;
            
            // Flowwolf cost (L2 pricing)
            const platformBase = 200;
            const perLoadCost = 0.80; // Average across intents
            const flowwolfCost = platformBase + (volume * perLoadCost);
            
            // Savings
            const monthlySavings = currentCost - flowwolfCost;
            const annualSavings = monthlySavings * 12;
            const roi = ((monthlySavings / flowwolfCost) * 100).toFixed(0);
            
            // Display
            document.getElementById('current_cost').textContent = currentCost.toLocaleString();
            document.getElementById('flowwolf_cost').textContent = Math.round(flowwolfCost).toLocaleString();
            document.getElementById('savings').textContent = Math.round(monthlySavings).toLocaleString();
            document.getElementById('annual_savings').textContent = Math.round(annualSavings).toLocaleString();
            document.getElementById('roi').textContent = roi;
            document.getElementById('result').style.display = 'block';
        }
    </script>
</body>
</html>
```

---

## Tool 2: FDP Outreach Script (GAP-S3 Fix)

### Email Template 1: Cold Outreach

**Subject**: Replace your EDI team with AI (first 10 get price lock)

```
Hi [First Name],

Quick question: How much do you spend on EDI processing each month?

Most 3PLs we talk to: $4K-$8K/month (1-2 people doing manual data entry).

We're Flowwolf — AI that replaces your EDI team.

Think: EDI 204 comes in → AI extracts the load → Creates it in your TMS.
Cost: $0.10/load (vs $2.00 manual).

We're offering the first 10 brokers:
✅ 3-year price lock ($1K-$2K/month, guaranteed)
✅ Faster autonomy (earn Level 3 in half the time)
✅ Exit protection (90-day export, no vendor lock-in)

Interested in a 15-minute demo?

[Book time here]

Best,
[Your Name]
Flowwolf Sentinel
```

---

### Email Template 2: Warm Introduction

**Subject**: [Mutual Contact] suggested we connect

```
Hi [First Name],

[Mutual Contact] at [Company] mentioned you're frustrated with EDI costs.

We just helped them cut EDI processing from $8K/month to $1.2K/month.

How? AI that learns your business. Replaces manual EDI entry with autonomous intent extraction.

They're one of our Founding Design Partners — 3-year price lock, strategic input.

We have 7 FDP slots left. Want one?

15-minute demo: [Calendar link]

Cheers,
[Your Name]
```

---

### Email Template 3: Follow-Up (No Response)

**Subject**: Still spending $8K/month on EDI?

```
[First Name],

Circling back—did you see my note about Flowwolf?

If EDI costs aren't a priority, no worries.

But if you're curious: We're saving brokers $6K-$10K/month.

Last call for FDP pricing (3-year lock, ends Jan 31).

Want a 10-minute overview?

[Book here]

Thanks,
[Your Name]
```

---

### LinkedIn InMail Template

```
Hi [First Name],

Saw you're at [Company]. Quick question:

How many people handle EDI processing at [Company]?

We're Flowwolf — AI that replaces EDI teams.

Brokers are saving $5K-$10K/month with us.

First 10 get 3-year price lock + strategic input.

15-min demo? [Link]

Best,
[Your Name]
```

---

### Phone Script (If you call)

**Opening** (15 seconds):
> "Hi [Name], this is [Your Name] from Flowwolf.  
> Do you have 30 seconds?  
> 
> We help brokers replace their EDI teams with AI.  
> Companies like [Reference Customer] cut EDI costs 80%.  
> 
> Are you open to a 15-minute demo this week?"

**If "Not interested"**:
> "No problem. Quick question before I let you go:  
> What do you currently spend on EDI processing?  
> [They answer]  
> Got it. If that ever becomes a priority, reach out.  
> Thanks for your time."

**If "Maybe, send info"**:
> "Sure. What's the best email?  
> I'll send a 2-minute video + calendar link.  
> Fair?"

---

## Tool 3: FDP Qualification Criteria

### ✅ Good FDP Indicators

**Company Profile**:
- 500-5,000 loads/month (sweet spot)
- Current EDI team (1-3 people)
- Using modern TMS (McLeod, TMW, proprietary)
- Growth-oriented (hiring, expanding)

**Decision Maker**:
- VP Ops or CEO (budget authority)
- Frustrated with current EDI (pain acknowledged)
- Open to new tech (not "we've always done it this way")

**Engagement**:
- Responds to emails within 48 hours
- Books demo within 1 week
- Brings team to demo (Ops, IT, Finance)

---

### ❌ Bad FDP Indicators (Disqualify)

**Company Profile**:
- < 100 loads/month (too small, not economical)
- No current EDI (not feeling pain)
- Resisting tech ("We like manual control")
- Distressed financially (can't pay)

**Decision Maker**:
- "Need to talk to my board" (no authority)
- Ghostsafter initial interest (not serious)
- Asks for 90-day free trial (wants free stuff)

**Engagement**:
- Delays demo 3+ times (not priority)
- Sends junior person to demo (not executive buy-in)
- Asks "Can you do X, Y, Z first?" (feature creep)

---

## Tool 4: Objection Handling

### Objection 1: "Price is too high"

**Response**:
> "I hear you. Let's look at ROI.  
> 
> You're spending $[X]/month on EDI now.  
> Flowwolf costs $[Y]/month.  
> Savings: $[X-Y]/month.  
> 
> The real question: Can you afford NOT to save $[Savings]?  
> 
> Plus, FDPs get 3-year price lock. Rates never go up."

---

### Objection 2: "We need to think about it"

**Response**:
> "Totally fair. What specifically do you need to think about?  
> [They explain]  
> 
> Got it. Here's what I'll do:  
> Send you a PDF with [their concern] addressed.  
> 
> Can we schedule 15 minutes next week to discuss?  
> That way you're not figuring this out alone."

---

### Objection 3: "What if AI makes a mistake?"

**Response**:
> "Great question. That's why we start at Level 1.  
> 
> Level 1 = You approve every action. Zero risk.  
> 
> You only move to Level 2 (auto-draft) after 30 days of proof.  
> And Level 3 (auto-execute) only after 90 days + executive signoff.  
> 
> Trust is earned, not given. We build autonomy progressively."

---

### Objection 4: "We're locked into [Current EDI Provider]"

**Response**:
> "When does that contract end?  
> [They tell you]  
> 
> Perfect. Let's get you set up now, run in parallel for 30 days.  
> 
> If Flowwolf saves you money (it will), you switch when contract ends.  
> If not, you cancel—no penalty.  
> 
> FDPs get exit protection. We're confident you'll stay."

---

### Objection 5: "Our IT team is slammed"

**Response**:
> "That's exactly why we built this.  
> 
> Integration = 1 week, we handle 90%.  
> Your IT gives us API credentials, we do the rest.  
> 
> Total IT time: 8 hours over 2 weeks.  
> 
> Compare that to hiring another EDI person (months to recruit, train).  
> 
> Which is easier?"

---

## Tool 5: Demo Follow-Up Sequence

### Email 1: Immediately After Demo

**Subject**: [Company Name] — Flowwolf Demo Follow-Up

```
Hi [Name],

Thanks for the demo today!

As discussed:
- Your volume: [X] loads/month
- Estimated savings: $[Y]/month
- FDP pricing: $[Z]/month (3-year lock)

Next steps:
1. Review attached PDF (pricing, case study)
2. Intro us to your CFO/CEO (if not you)
3. Pick pilot start date (suggest Feb 1)

Questions? Hit reply or call me: [Phone]

Best,
[Your Name]

P.S. FDP slots filling fast (4 left as of today).
```

---

### Email 2: 3 Days Later (No Response)

**Subject**: Following up — any questions?

```
[Name],

Quick check-in. Did you get a chance to review the Flowwolf proposal?

Any blockers I can help with?

If timing isn't right, totally understand.

Let me know!

[Your Name]
```

---

### Email 3: 7 Days Later (Final)

**Subject**: Last call for FDP pricing

```
[Name],

Last note from me.

We're closing FDP enrollment Jan 31.

After that, pricing goes to standard rates (20% higher).

If you want the 3-year lock, let me know by Friday.

If not, no worries—maybe we connect down the road.

Best,
[Your Name]
```

---

## Tool 6: Sales Metrics Dashboard

### Track These

**Pipeline Metrics**:
- Outbound emails sent: [___]
- Responses received: [___]
- Demos scheduled: [___]
- Demos completed: [___]
- Pilots started: [___]
- FDPs closed: [___]

**Conversion Rates**:
- Email → Response: Target 15%
- Response → Demo: Target 50%
- Demo → Pilot: Target 40%
- Pilot → FDP: Target 70%
- Overall: Email → FDP = 4% (15% × 50% × 40% × 70%)

**Example**:
- Send 250 emails
- Get 38 responses (15%)
- Book 19 demos (50% of responses)
- Start 8 pilots (40% of demos)
- Close 5 FDPs (70% of pilots)

**Implication**: Need 50 emails per FDP closed.

---

## Success Criteria

**Tool is successful if**:
- ✅ Sales can run calculator without engineering help
- ✅ Email templates get 15%+ response rate
- ✅ Objection handling reduces "think about it" by 50%
- ✅ 10 FDPs signed by March 31

---

**Status**: All sales tools ready.  
**Owner**: Sales/CEO  
**Next**: Execute outbound campaign.

**"Sales tools turn conversations into contracts."** 📧💰
