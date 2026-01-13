---
title: "Faq Common Questions"
tags: []
version: "9.1"
last_updated: "2026-01-12"
---

# Frequently Asked Questions (FAQ)

**Version**: 9.4 (Agentic Core)
**Last Updated**: 2026-01-08

---

## General Questions

### Q: What is Flowwolf Sentinel Flowwolf Sentinel?
**A**: An AI-native, Intent-driven logistics operating system layer that replaces traditional document processing with autonomous agents. Instead of mapping File A to File B, we extract business intent and execute it via governed agents.

### Q: How is this different from RPA (Robotic Process Automation)?
**A**: RPA mimics human mouse-clicks. Flowwolf understands Intent natively. RPA breaks when the UI changes; Flowwolf operates at the semantic layer (intent never changes, even if protocols do).

### Q: Can Flowwolf handle international freight (Ocean/Air)?
**A**: Yes. The `TenderLoad` Intent supports polymorphic payloads including:
- FTL (Full Truckload)
- LTL (Less than Truckload)
- Drayage
- Ocean FCL/LCL
- Air freight

See `18_INTENT_LIBRARY_DEFINITIONS.md` for full schema.

---

## Commercial Questions

### Q: How is pricing structured?
**A**: Pricing is based on **Autonomy Tiers** (not "per transaction"):

| Tier | Autonomy Ceiling | Base Fee | Per Intent | Per Execution |
|------|------------------|----------|------------|---------------|
| Assist | Level 1 | $500/mo | $0.10 | N/A |
| Co-Pilot | Level 2 | $2,000/mo | $0.05 | N/A |
| Autonomous Ops | Level 4 | $10,000/mo | $0.02 | $1.50 |
| Agentic Network | Level 5 | $50,000/mo | $0.01 | $0.50 |

Higher autonomy = lower per-unit costs (you earn automation).

### Q: Do I have to migrate all partners at once?
**A**: No. You can start with a single partner in "Assist" mode (Level 1) and gradually upgrade as trust builds. Hybrid mode supported (some partners on EDI, some on Flowwolf).

### Q: What happens if my partner's data quality drops?
**A**: The system automatically:
1. Lowers their autonomy ceiling (e.g., Level 4 → Level 2)
2. Sends them to manual review queue
3. Notifies your Account Manager

You stay in control.

---

## Technical Questions

### Q: Can I run this on-premise (data residency requirements)?
**A**: Yes. Frappe (the underlying framework) supports on-premise deployment. All data stays in your data center.

### Q: How do you prevent AI hallucinations?
**A**: Multiple layers:
1. **Pydantic validation** (type-checked schemas with constraints)
2. **Confidence thresholds** (low-confidence intents → human review)
3. **VCR cassette tests** (record/replay for regression detection)
4. **Property-based testing** (Hypothesis generates adversarial inputs)

See `tdd-manifesto.md` for details.

### Q: What happens if the AI model changes (GPT-4 → GPT-5)?
**A**: All AI calls are tagged with `model_version` in the audit log. We:
1. Run A/B tests on a sample of traffic
2. Compare outputs via trace replay
3. Only upgrade if regression tests pass

### Q: How long does Intent resolution take?
**A**: < 200ms (latency budget enforced by performance tests). If it exceeds this, the build fails.

---

## Integration Questions

### Q: Do I have to replace my existing TMS?
**A**: No. Flowwolf can run in parallel with your existing TMS. The `Motion` app can:
- Sync data to your legacy system via API
- Act as a "smart middleware" layer

### Q: Can I integrate with our existing EDI provider (Cleo, Kleinschmidt)?
**A**: Yes. We provide an "EDI Bridge" adapter:
1. Your EDI provider sends X12 files to Flowwolf
2. Flowwolf converts them to Intents
3. Intents execute autonomously (no manual mapping)

See `03_IMPLEMENTATION_PHASES.md` (Phase -1: Legacy Bridge).

### Q: What EDI standards do you support?
**A**: Currently:
- X12 (204, 214, 210, 990, 997)
- EDIFACT (planned for Q2 2026)
- Custom JSON/XML via API

### Q: Can we send Intents via email?
**A**: Yes. The `Fluent` app has an email parser that extracts Intents from unstructured text (e.g., "Pickup 5 pallets tomorrow at LAX, deliver to SFO").

---

## Security & Compliance Questions

### Q: Is this SOC-2 compliant?
**A**: Yes. See `governance.md` for compliance matrix (SOC-2, ISO-27001, GDPR).

### Q: How is tenant data isolated?
**A**: Each partner has:
1. **Tenant-Key Encryption** (data encrypted with partner-specific key)
2. **Circuit Breakers** (one partner's failures don't affect others)
3. **Separate Redis namespaces** (no cross-contamination)

### Q: Can I audit every decision the AI makes?
**A**: Yes. Every Intent has:
- `trace_id` (follow it through logs)
- `confidence` score
- `execution_decision` (with reasoning)
- Complete audit trail

See `25_FAILURE_SCENARIOS_PLAYBOOK.md` for trace replay.

---

## Governance Questions

### Q: Can the AI auto-dispatch my high-value loads?
**A**: Only if:
1. Your **Autonomy Ceiling** ≥ Level 4
2. Your **Trust Score** ≥ 0.90
3. Intent **Confidence** ≥ 0.90
4. No **Decision Contracts** block it (e.g., "No hazmat auto-dispatch")

The system is designed to be conservative.

### Q: Who controls the Autonomy Ceiling?
**A**: You do. It's set in the Partner Signal Profile (editable by Account Managers). We recommend starting at Level 2 and upgrading gradually.

### Q: What is a "Decision Contract"?
**A**: A policy rule that governs execution. Example:
```json
{
  "rule_id": "require_insurance_for_high_value",
  "condition": "intent.payload.value > 100000",
  "action": "REQUIRE_MANUAL_REVIEW"
}
```

You define these in the Governance UI.

---

## Development Questions

### Q: What tech stack is this built on?
**A**: 
- **Backend**: Python 3.11, Frappe v15, Pydantic
- **AI**: OpenAI API (configurable), `instructor` library
- **Frontend**: Vue 3, Tailwind (optional)
- **Database**: MariaDB, Redis
- **Testing**: Pytest, Hypothesis, VCRpy, Cypress

See `05_FRAMEWORK_SELECTION_ANALYSIS.md` for rationale.

### Q: Can I extend the system with custom agents?
**A**: Yes. Use the `@skill` decorator:
```python
from fw_cortex.sdk import skill

@skill(name="custom_shipping_cost")
def calculate_cost(intent: Intent) -> float:
    # your logic here
    return 0.0
```

See `architecture.md` for SDK documentation.

### Q: How do I run the tests locally?
**A**: 
```bash
bench run-tests --app fw_cortex
```

See `24_DEVELOPER_QUICK_START.md` for setup.

---

## Roadmap Questions

### Q: When will Agent-to-Agent negotiation (Level 5) be available?
**A**: Q3 2026 (Phase 4 - Jupiter). See `07_10_YEAR_EVOLUTION_MAP.md`.

### Q: Will you support drone delivery?
**A**: Yes, planned for Year 3. The polymorphic payload architecture makes adding new modes straightforward (no migration required).

### Q: What about blockchain integration?
**A**: Not planned. The Intent Graph + Audit Trail already provides immutability and traceability without blockchain overhead.

---

## Troubleshooting

### Q: My Intent is stuck in "PARTIAL" state. What does that mean?
**A**: The signal was missing required fields (e.g., weight, pickup date). This is normal for low-quality EDI. The Intent waits in the "Needs Clarification" queue for a human to fill in the gaps.

### Q: I'm getting "Circuit breaker OPEN" errors. How do I fix it?
**A**: Your partner is sending too many malformed signals. See `25_FAILURE_SCENARIOS_PLAYBOOK.md` (Scenario 1) for recovery steps.

### Q: The AI is hallucinating. What do I do?
**A**: Tag the Intent as FAILED, export it as a test case, and add property-based tests. See `25_FAILURE_SCENARIOS_PLAYBOOK.md` (Scenario 2).

---

## Migration Questions

### Q: How long does migration from Cleo/Kleinschmidt take?
**A**: Typical timeline:
- Week 1-2: Legacy Bridge setup (parallel run)
- Week 3-4: Train AI on your historical EDI files
- Week 5-8: Onboard first 3 partners in "Assist" mode
- Month 3+: Gradual autonomy升级

### Q: Will I lose my historical EDI data?
**A**: No. The Intent Graph is append-only. Old EDI files are preserved in the `Signal` table as immutable records.

---

## Support

### Q: How do I get help?
**A**: 
- **Documentation**: `master-manifest.md` (start here)
- **Glossary**: `26_GLOSSARY.md`
- **Developer Guide**: `24_DEVELOPER_QUICK_START.md`
- **Slack**: #antigravity-support
- **Email**: support@antigravity.ai

---

**Have a question not answered here?** Create a GitHub Discussion or Slack message in #antigravity-questions.

---

## Future Roadmap FAQs (Nice-to-Have Gaps)

### Q: Will you support non-English signals? (GAP-N1)
**A**: Multi-language support is planned for Year 3 (2028). Our LLM-based extraction can handle any language, but we're prioritizing North American TAM first (English/Spanish). Chinese and European languages will be added when we expand globally.

**Roadmap**: Phase 6 (Global Scale)

---

### Q: Is there a mobile app for approving intents on-the-go? (GAP-N2)
**A**: Mobile apps (iOS/Android) are planned for Phase 4 (Jupiter). For now, the web UI is fully responsive and works on mobile browsers. Native apps will be added once we launch the Partner SDK.

**Roadmap**: Phase 4 (Jupiter - External Developer SDKs)

---

### Q: Do you use blockchain for immutability? (GAP-N3)
**A**: No. We achieve immutability via **append-only Intent Graphs** + cryptographic audit trails, which provide the same guarantees without blockchain's overhead and complexity. Our approach is faster, cheaper, and simpler to audit.

**Technical Details**:
- Each Intent has a cryptographic hash of its payload
- Audit log is append-only (never modified)
- Trace replay can reconstruct any historical decision

---

### Q: Can I call in a load tender over thephone? (GAP-N4)
**A**: Voice-to-Intent is planned for Phase 2 (Fluent PROD). We'll integrate with Twilio for phone call transcription → Intent extraction. For MVP, focus is on EDI/Email/API (90% of signals).

**Roadmap**: Phase 2.3 (Fluent PROD - Voice Plugin)

---

### Q: How many intents/second can the system handle? (GAP-N5)
**A**: Capacity planning will be documented after Phase 1 load tests. Early estimates: 
- Single Cortex instance: ~500 intents/sec
- Horizontal scaling: 10K+ intents/sec (via load balancer)

We'll publish official capacity guidelines after production deployment.

**Roadmap**: Post-Phase 1 (after load testing)

---

### Q: What's your backup and disaster recovery strategy? (GAP-N6)
**A**: 
- **RPO**: 2 minutes (continuous replication)
- **RTO**: 2 hours (automated failover)
- **Backup Frequency**: Real-time replication + daily snapshots
- **Retention**: 90 days

Full DR runbook will be finalized during infrastructure setup.

**Roadmap**: Phase 0 (Infrastructure Setup)

---

### Q: Can customers request data deletion (GDPR)? (GAP-N7)
**A**: GDPR "Right to Delete" will be implemented in Phase 3 (Motion PROD). Since most partners are companies (B2B), individual PII deletion is rare. We'll add "Archive & Purge" workflow for compliance.

**Roadmap**: Phase 3.3 (Motion PROD - Compliance Features)

---

### Q: How do you handle scale to millions of partners? (GAP-N8)
**A**: Multi-tenancy sharding strategy will be finalized in Year 5 (Global Scale phase). Current architecture (single DB + tenant-key encryption) supports up to 10K partners. Beyond that, we'll implement horizontal database sharding.

**Roadmap**: Year 5 (10-Year Evolution Map)

---

**Status**: All nice-to-have gaps documented in roadmap.
