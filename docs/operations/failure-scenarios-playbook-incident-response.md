---
title: "Failure Scenarios Playbook Incident Response"
tags: []
version: "9.1"
last_updated: "2026-01-12"
---

# Failure Scenarios & Recovery Playbook

**Version**: 9.4 (Agentic Core)
**Owner**: DevOps + Engineering
**Purpose**: Production incident response procedures

---

## Scenario 1: Circuit Breaker Triggered

**Symptoms**:
- HTTP 429 "Too Many Requests" errors
- Partner signals being rejected
- Alert: "Circuit breaker OPEN for partner P12345"

**Root Cause**: Partner sending malformed/duplicate signals too frequently

**Recovery Steps**:

1. **Identify the partner**:
   ```bash
   bench console
   >>> from fw_cortex.governance import CircuitBreakerRegistry
   >>> registry = CircuitBreakerRegistry()
   >>> registry.get_open_breakers()
   ['P12345']
   ```

2. **Check error rate**:
   ```bash
   >>> breaker = registry.get('P12345')
   >>> breaker.failure_count
   15  # Exceeded threshold of 10
   ```

3. **Contact partner** (escalate to Account Manager):
   > "Your integration is sending malformed signals. Please fix X12 segment ABC."

4. **Manually reset circuit breaker** (after partner confirms fix):
   ```bash
   >>> breaker.reset()
   >>> breaker.state
   'CLOSED'
   ```

**Prevention**: Add partner to weekly data-quality review list.

---

## Scenario 2: AI Hallucination Detected

**Symptoms**:
- Intent created with impossible values (e.g., weight = -50 lbs)
- Confidence score is high (> 0.9) but validation fails
- Alert: "Hallucination detected in IntentInstance #123"

**Root Cause**: LLM generated invalid data not caught by Pydantic schema

**Recovery Steps**:

1. **Tag the Intent as FAILED**:
   ```python
   intent = frappe.get_doc("Intent Instance", "uuid-123")
   intent.state = "FAILED"
   intent.error_reason = "Hallucination: negative weight"
   intent.save()
   ```

2. **Capture as VCR test case**:
   ```bash
   # Export the raw signal + expected output
   bench execute fw_cortex.tests.export_hallucination_case \
     --args "['uuid-123', 'fixtures/hallucinations/negative_weight.yaml']"
   ```

3. **Add property-based test** to catch future cases:
   ```python
   # tests/test_intent_validation.py
   from hypothesis import given, strategies as st
   
   @given(weight=st.floats(min_value=-1000, max_value=0))
   def test_negative_weight_rejected(weight):
       with pytest.raises(ValidationError):
           TenderLoad(weight=weight, ...)
   ```

4. **Deploy schema fix**:
   ```python
   class TenderLoad(BaseIntent):
       weight: confloat(gt=0)  # Must be positive
   ```

**Prevention**: All Pydantic models must use constrained types (`confloat`, `conint`).

---

## Scenario 3: Partner Data Quality Drop

**Symptoms**:
- Partner P45678's trust_score drops below 0.80
- Increasing number of PARTIAL intents (missing required fields)
- Alert: "Partner P45678 trust score: 0.75 (was 0.92)"

**Root Cause**: Partner changed their EDI format without notice

**Recovery Steps**:

1. **Auto-downgrade autonomy tier**:
   ```python
   partner = frappe.get_doc("Partner Signal Profile", "P45678")
   if partner.trust_score < 0.80:
       partner.autonomy_ceiling = max(partner.autonomy_ceiling - 1, 1)
       partner.save()
   ```

2. **Enable manual review mode**:
   ```python
   # All signals from this partner now go to human review
   partner.require_human_review = True
   partner.save()
   ```

3. **Analyze recent signals**:
   ```bash
   bench execute fw_cortex.analytics.analyze_partner_signals \
     --args "['P45678', '2026-01-01', '2026-01-08']"
   # Output: "Missing field 'pickup_time' in 85% of signals"
   ```

4. **Contact partner**:
   > "We noticed your EDI 204s are missing the pickup time. Can you restore this field?"

5. **Re-enable autonomy** (after partner fixes + 7-day probation):
   ```python
   partner.require_human_review = False
   partner.autonomy_ceiling = 2  # Gradual upgrade
   partner.save()
   ```

**Prevention**: Weekly automated partner scorecard emails.

---

## Scenario 4: Database Failover

**Symptoms**:
- Primary MySQL instance unreachable
- Alert: "Database connection lost"
- All API requests return 500 errors

**Root Cause**: Primary DB instance crashed

**Recovery Steps**:

1. **Automatic failover** (RDS handles this):
   - Replica promoted to PRIMARY (2-minute RPO)
   - DNS updated automatically

2. **Verify failover**:
   ```bash
   bench console
   >>> frappe.db.get_value("Intent Instance", {"name": "test-intent"}, "state")
   'CONFIRMED'  # Data intact
   ```

3. **Check for lost transactions** (last 2 minutes):
   ```sql
   SELECT COUNT(*) FROM `tabIntent Instance`
   WHERE creation > (NOW() - INTERVAL 2 MINUTE);
   ```

4. **Notify affected partners**:
   > "We experienced a brief outage. Please resend any signals from the last 2 minutes."

**RPO/RTO**:
- **RPO**: 2 minutes (continuous replication)
- **RTO**: 5 minutes (automated failover + DNS propagation)

---

## Scenario 5: Agent Execution Timeout

**Symptoms**:
- Intent stuck in "EXECUTING" state for > 5 minutes
- Alert: "AgentContract timeout for Intent #789"
- No Load created in Motion

**Root Cause**: Agent hit an infinite loop or external API timeout

**Recovery Steps**:

1. **Kill the stuck task**:
   ```bash
   # Find the worker process
   ps aux | grep "execute_intent"
   kill -9 <PID>
   ```

2. **Mark Intent as FAILED**:
   ```python
   intent = frappe.get_doc("Intent Instance", "uuid-789")
   intent.state = "FAILED"
   intent.error_reason = "Agent timeout after 300s"
   intent.save()
   ```

3. **Check agent logs**:
   ```bash
   tail -f logs/worker.log | grep "uuid-789"
   # Look for stack trace
   ```

4. **Add timeout guard** to agent:
   ```python
   import asyncio
   
   async def execute(self, intent):
       try:
           result = await asyncio.wait_for(
               self._execute_internal(intent),
               timeout=60.0  # 60 second max
           )
       except asyncio.TimeoutError:
           return ExecutionResult(success=False, error="Timeout")
   ```

**Prevention**: All agent methods must have timeout guards.

---

## Scenario 6: Trace Replay Regression

**Symptoms**:
- CI failing with "Trace replay mismatch"
- Production trace #12345 now produces different output
- Alert: "Regression detected in trace test"

**Root Cause**: Code change altered behavior of Intent resolution

**Recovery Steps**:

1. **Identify the change**:
   ```bash
   git log --oneline --since="1 week ago" -- fw_cortex/intent/
   ```

2. **Compare outputs**:
   ```bash
   bench execute fw_cortex.tests.compare_trace_outputs \
     --args "['trace-12345', 'HEAD', 'HEAD~1']"
   # Shows diff between old and new behavior
   ```

3. **Decide if regression is acceptable**:
   - **Breaking change**: Revert the commit
   - **Intentional improvement**: Update trace fixture

4. **Update trace fixture** (if intentional):
   ```bash
   bench execute fw_cortex.tests.refresh_trace_fixture \
     --args "['trace-12345']"
   ```

**Prevention**: All PRs must pass trace-replay tests before merge.

---

## Scenario 7: Redis OOM (Out of Memory)

**Symptoms**:
- Redis evicting idempotency keys prematurely
- Duplicate signals being processed
- Alert: "Redis memory usage > 90%"

**Root Cause**: Too many idempotency keys cached (TTL too long)

**Recovery Steps**:

1. **Check Redis memory**:
   ```bash
   redis-cli info memory
   # used_memory_human:5.2G
   # maxmemory:6G
   ```

2. **Reduce TTL** for idempotency keys:
   ```python
   # fw_fluent/api/ingest.py
   IDEMPOTENCY_TTL = 12 * 3600  # Reduce from 24h to 12h
   ```

3. **Flush old keys**:
   ```bash
   redis-cli --scan --pattern "idempotency:*" | \
     xargs redis-cli del
   ```

4. **Scale Redis** (increase max memory):
   ```bash
   # Update Redis config
   redis-cli CONFIG SET maxmemory 12gb
   ```

**Prevention**: Monitor Redis memory weekly, auto-scale at 80% threshold.

---

## Emergency Contacts

| Scenario | Contact | Slack | Phone |
|----------|---------|-------|-------|
| Circuit Breaker | DevOps Lead | #oncall-devops | +1-555-0100 |
| Hallucination | AI Engineering Lead | #oncall-ai | +1-555-0101 |
| Database Failover | DBA | #oncall-db | +1-555-0102 |
| Agent Timeout | Backend Lead | #oncall-backend | +1-555-0103 |

---

## Post-Incident Review Template

After any incident, create a doc with:

1. **Timeline**: What happened when
2. **Root Cause**: Why it happened
3. **Resolution**: How we fixed it
4. **Prevention**: What we'll do to prevent recurrence
5. **Action Items**: Tickets created (with assignees + deadlines)

---

**Status**: Living document. Update after every incident.
