# Engineering Constitution

**Status**: 🔒 **SUPREME LAW** - Immutable  
**Authority**: Board of Directors + Chief Architect  
**Version**: 1.0 (Ratified 2026-01-08)  
**Amendments**: Require unanimous board approval

---

## Preamble

We, the engineering team of Flowwolf, in order to establish consistency, ensure maintainability, and uphold the integrity of the Intent-Native Operating System for Logistics, do hereby establish this Constitution as the supreme law governing all technical decisions.

---

## Article I: Identity Separation

### Section 1: The Three Identities

This Constitution recognizes three distinct identities, each with separate jurisdiction:

1. **`fw`** - The Execution Identity
2. **`flowwolf`** - The Platform Identity  
3. **Tooling** - Metadata Only (No Identity)

### Section 2: Execution Identity (`fw`)

**Definition**: `fw` is the identity of all code that **executes, adapts, and flows**.

**Jurisdiction**: `fw` shall govern:
- Application code (Python, JavaScript)
- Runtime DocTypes (mutable state)
- Internal APIs
- Service containers
- Database tables (execution layer)
- Worker processes
- Agent implementations

**Canonical Form**:
- Frappe apps: `fw_{name}` (e.g., `fw_cortex`)
- DocTypes: `FW {NounPhrase}` (e.g., `FW Intent Instance`)
- APIs: `/api/fw/{resource}`
- Containers: `fw-{name}`

**Constitutional Guarantee**: No law shall mix `fw` identity with `flowwolf` identity within the same artifact.

### Section 3: Platform Identity (`flowwolf`)

**Definition**: `flowwolf` is the identity of all **authority, contracts, and governance**.

**Jurisdiction**: `flowwolf` shall govern:
- Company legal name
- Customer-facing brand
- Immutable schemas (Intent Definitions)
- Governance policies (Decision Contracts)
- Partner agreements (trust contracts)
- Customer-facing DocTypes
- External APIs
- Marketing materials

**Canonical Form**:
- Company: "Flowwolf, Inc."
- DocTypes: `Flowwolf {NounPhrase}` (e.g., `Flowwolf Decision Contract`)
- APIs: `/api/flowwolf/{resource}`
- Brand: "Flowwolf" (never "FW" in customer communications)

**Constitutional Guarantee**: No law shall diminish the authority of `flowwolf` identity in customer-facing contexts.

### Section 4: Tooling (Metadata Only)

**Definition**: Tooling exists to **annotate and describe**, not to execute or govern.

**Jurisdiction**: Tooling shall be limited to:
- Type hints (`# type: ignore`)
- Linter configs (`.pylintrc`, `.flake8`)
- IDE metadata (`.vscode/`, `.idea/`)
- Build scripts (`setup.py`, `package.json`)
- CI/CD configs (`.github/workflows/`)

**Constitutional Principle**: Tooling shall **never** create runtime behavior. Tooling is descriptive, not prescriptive.

**Example Violations**:
- ❌ Type hints that enforce runtime checks (use Pydantic instead)
- ❌ Linter rules that generate code (use templates instead)

---

## Article II: Separation of Powers

### Section 1: The Three-Layer Architecture

This Constitution establishes three layers of authority:

```
┌─────────────────────────────────────┐
│  Layer 3: flowwolf (Authority)      │ ← Immutable, Governance
├─────────────────────────────────────┤
│  Layer 2: fw (Execution)            │ ← Mutable, Adaptive
├─────────────────────────────────────┤
│  Layer 1: Tooling (Metadata)        │ ← Descriptive Only
└─────────────────────────────────────┘
```

### Section 2: Non-Interference Clause

No layer shall interfere with the jurisdiction of another layer.

**Violation Examples**:
- ❌ Execution layer (`fw`) creating governance rules (belongs to `flowwolf`)
- ❌ Authority layer (`flowwolf`) executing business logic (belongs to `fw`)
- ❌ Tooling generating runtime behavior (belongs to `fw`)

### Section 3: Clear Boundaries

| Decision | Layer | Identity |
|----------|-------|----------|
| "What intent schema to use?" | Authority | `flowwolf` (Intent Definition) |
| "How to extract intent from signal?" | Execution | `fw` (Intent Parser) |
| "What type hint to add?" | Metadata | Tooling (`.pyi` stub) |

---

## Article III: Naming Convention Law

### Section 1: Mandatory Prefixes

All artifacts shall declare their identity via mandatory prefixes:

| Identity | Prefix Pattern | Example |
|----------|----------------|---------|
| Execution | `fw_*` or `FW *` | `fw_cortex`, `FW Signal` |
| Authority | `flowwolf` or `Flowwolf *` | `Flowwolf Decision Contract` |
| Tooling | No prefix (tool-specific) | `.pylintrc`, `mypy.ini` |

### Section 2: Prohibition of Mixing

**Constitutional Ban**: Mixing identities within the same artifact is **prohibited**.

**Violation Examples**:
- ❌ `from fw_cortex import FlowwolfIntent` (mixed identities)
- ❌ `class FW_Flowwolf_Signal` (double identity)
- ❌ Using "Flowwolf" in variable names within `fw` code

**Permitted Exceptions**: None.

### Section 3: Enforcement Mechanisms

- **Pre-commit hooks**: Shall reject commits violating naming conventions
- **CI linter**: Shall fail builds with identity violations
- **Code review**: Maintainers shall block PRs with violations

---

## Article IV: The Constitutional Principles

### Principle 1: Identity Reflects Purpose

> **`fw` is what runs. `flowwolf` is what decides. Tooling is what describes.**

Every artifact shall be named according to its **essential purpose**, not its implementation details.

### Principle 2: Immutability of Authority

> **Authority identities (`flowwolf`) are immutable. Execution identities (`fw`) are mutable.**

- `Flowwolf Intent Definition` v4 → Cannot be modified (create v5 instead)
- `FW Intent Instance` → Can be updated (runtime state)

### Principle 3: Tooling Has No Runtime

> **Tooling is metadata. Metadata does not execute.**

If it executes, it is not tooling—it is `fw` code.

**Example**:
- ✅ Type hints in `.pyi` files → Tooling (metadata)
- ❌ Pydantic schema validation → Execution (`fw` code)

### Principle 4: Customer Sees Flowwolf, Code Sees fw

> **External identity is `flowwolf`. Internal identity is `fw`.**

- Customer-facing: "Welcome to **Flowwolf**, the Intent-Native OS"
- Developer-facing: "Import `fw_cortex.intent.library`"
- Never expose `fw` branding to customers

---

## Article V: Amendment Process

### Section 1: Amendment Threshold

Amendments to this Constitution require:
1. **Unanimous approval** of the Engineering Leadership Team
2. **Board of Directors** signoff
3. **60-day notice** period before enforcement

### Section 2: Prohibited Amendments

The following principles are **unamendable**:

1. The three-identity system (`fw`, `flowwolf`, tooling)
2. The separation of execution vs authority
3. The prohibition of mixing identities

**Rationale**: These are foundational to system coherence.

### Section 3: Emergency Override

In case of **critical production incident**, the Chief Architect may temporarily waive naming conventions. Such waivers:
- Must be documented in post-incident review
- Expire after 7 days
- Require retroactive board approval

---

## Article VI: Supremacy Clause

### Section 1: Constitutional Supremacy

This Constitution is the **supreme law** of the Flowwolf engineering organization.

In case of conflict between this Constitution and:
- Engineering Guidelines → Constitution prevails
- Code review comments → Constitution prevails
- Personal preferences → Constitution prevails
- Legacy code → Legacy code must be migrated

### Section 2: Severability

If any provision of this Constitution is found invalid, the remainder shall continue in full force.

### Section 3: Grandfathering (Legacy Code)

Code written before ratification (2026-01-08) has **12 months** to comply. After 2027-01-08, all violations are **unconstitutional**.

---

## Article VII: Ratification

This Constitution was ratified on **2026-01-08** by:

- [X] Chief Architect
- [X] Engineering Lead
- [X] Product Lead
- [X] Board of Directors

**Effective Date**: 2026-01-08 00:00:00 UTC

---

## Appendix A: Quick Reference

### The Three Laws (Simplified)

1. **Execution Law**: If it runs → `fw`
2. **Authority Law**: If it governs → `flowwolf`
3. **Tooling Law**: If it describes → no identity prefix

### Decision Tree

```
Does this artifact execute code or store runtime state?
├─ YES → fw identity
└─ NO → Is it customer-facing or immutable governance?
    ├─ YES → flowwolf identity
    └─ NO → Tooling (metadata only)
```

---

## Appendix B: Constitutional Violations (Examples)

| Violation | Reason | Correct Form |
|-----------|--------|--------------|
| `from cortex import Intent` | Missing `fw_` prefix | `from fw_cortex.intent import Intent` |
| `class FlowwolfSignal` | Authority identity for execution data | `class FWSignal` |
| `fw-marketing-site` | `fw` in customer-facing service | `flowwolf-portal` |
| `Flowwolf Intent Instance` | Authority identity for mutable state | `FW Intent Instance` |

---

## Appendix C: Enforcement Checklist

Before merging any PR, verify:

- [ ] All apps use `fw_` prefix
- [ ] Execution DocTypes use `FW *` prefix
- [ ] Authority DocTypes use `Flowwolf *` prefix
- [ ] No mixed identities in same file
- [ ] Customer-facing materials say "Flowwolf" (never "FW")
- [ ] Internal code uses `fw_*` imports

---

## Closing Statement

> **"We hold these truths to be self-evident: that `fw` flows, `flowwolf` governs, and tooling merely observes."**

This Constitution shall endure as long as the Intent-Native Operating System for Logistics exists.

**Ratified**: 2026-01-08  
**In force**: Perpetually  
**Amendments**: Prohibited (see Article V, Section 2)

---

**🔒 END OF CONSTITUTION 🔒**
