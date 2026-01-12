# Changelog

All notable changes to the Antigravity Flowwolf Autonomous documentation and architecture.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---



## [9.4.2] - 2026-01-08 - Canonical Positioning Locked

### Changed
- **LOCKED CANONICAL POSITIONING**: "Flowwolf is the Intent-Native Operating System for logistics—built on an AI-native core and progressing safely toward autonomy."
- Updated Master Manifest with "Operating System" framing
- Updated README with OS analogy (Flowwolf:Logistics :: Linux:Servers)
- Clarified competitive positioning (OS layer vs Application layer)

### Why "Operating System"?
- Positions above TMS/WMS (we orchestrate, they execute)
- Implies foundational infrastructure (like Linux for servers)
- Differentiates from "platform" (too generic)

### The Three-Part Formula
1. **Intent-Native** = Core differentiator (Intent-Native (protocol-agnostic))
2. **Operating System** = Positioning (we're the OS layer)
3. **Safely toward autonomy** = Risk mitigation (progressive tiers)


## [9.4.1] - 2026-01-08 - Terminology Refinement

### Changed
- **BREAKING POSITIONING CHANGE**: Reframed from "AI-Native EDI Platform" to "**Intent-Native Logistics Operating System Layer**"
- Updated all strategic positioning language to emphasize Intent over Protocol
- Clarified: We are NOT an EDI platform (we're Intent-Native (protocol-agnostic))
- Updated Problem Statement to "The Intent Gap" (was focused on EDI)
- Added "What We Are NOT" section to Vision document

### Why This Matters
The "EDI Platform" framing was legacy language from our initial prototype. The architecture evolved to be Intent-Native (protocol-agnostic) (handles EDI, Email, API, Voice equally). The new positioning accurately reflects that we:
- **Extract intent** from any signal type
- **Execute via agents**, not protocol mappings  
- **Replace** traditional EDI systems, not improve them

### Technical Notes
- EDI terminology preserved where technically accurate (e.g., "EDI 204 protocol", "X12 standards")
- Strategic positioning now says "Intent-Native Operating System Layer"
- Competitive framing updated: "vs EDI platforms" instead of "better EDI platform"

## [9.4.0] - 2026-01-08 - Agentic Core (CURRENT)

### Added
- **Developer Quick Start Guide** (`24_DEVELOPER_QUICK_START.md`) - 5-minute setup for new engineers
- **Failure Scenarios Playbook** (`25_FAILURE_SCENARIOS_PLAYBOOK.md`) - Production incident response procedures
- **Glossary** (`26_GLOSSARY.md`) - Canonical definitions of all terminology
- **FAQ** (`27_FAQ.md`) - Answers to common questions from all stakeholders
- **Changelog** (`28_CHANGELOG.md`) - This file
- **Final Gap Analysis** (`23_FINAL_GAP_ANALYSIS_v9.4.md`) - Comprehensive review from fresh LLM perspective
- **Pricing Calculator** in `01_VISION_AND_STRATEGY.md` - Actual dollar amounts for Autonomy Tiers
- **Partner Signal Profile** definition in `18_INTENT_LIBRARY_DEFINITIONS.md` - Full schema with JSON example
- **Compliance Matrix** in `06_GOVERNANCE_FRAMEWORK.md` - SOC-2, ISO-27001, GDPR status
- **Execution Intermediaries** rule in `06_GOVERNANCE_FRAMEWORK.md` - No raw writes, agent-mediated execution
- **CI Badge** in `00_MASTER_MANIFEST.md` - GitHub Actions status
- **SDK Decorator Signature** in `04_FRAPPE_APP_DESIGN.md` - `@skill` interface example
- **ERD Diagram** in `02_ARCHITECTURE_DESIGN.md` - Entity relationships visualization
- **Normalized Signal Spec** in `04_FRAPPE_APP_DESIGN.md` - X-Idempotency-Key, X-Trace-ID headers
- **PR Checklist** in `24_DEVELOPER_QUICK_START.md` - Code review requirements

### Changed
- **Global Version** from 9.3 to 9.4 across all documents
- **AgentContract Interface** formalized in `02_ARCHITECTURE_DESIGN.md` - Abstract base class defined
- **Intent Definition vs Instance** separation clarified - Schema vs Runtime split documented
- **Trace ID Propagation** mechanism specified - All DocTypes get `trace_id` field

### Fixed
- Version inconsistencies across stakeholder review documents
- Missing TAM (Total Addressable Market) in `01_VISION_AND_STRATEGY.md` - Now $30B by 2030
- Missing RPO/RTO in `06_ARCHITECTURE_TOPOLOGY.md` - Now 2 min / 2 hours
- Missing performance budgets in `16_ANTIGRAVITY_ENGINEERING_GUIDELINES.md` - Now < 200ms for Intent resolution

---

## [9.3.0] - 2026-01-08 - Agentic Core (Operational Reality)

### Added
- **Normalized Signal** with idempotency keys and trace IDs
- **Agent-mediated execution** (no raw writes to database)
- **Split Intent Architecture** (IntentDefinition vs IntentInstance)
- **Idempotency Key** support in Fluent API (X-Idempotency-Key header)
- **Trace ID** propagation (X-Trace-ID header)

### Changed
- Updated `04_FRAPPE_APP_DESIGN.md` to include Normalized Signal Specs
- Updated `06_GOVERNANCE_FRAMEWORK.md` to define "No Raw Writes" policy

---

## [9.2.0] - 2026-01-08 - AI-Native TDD Aligned

### Added
- **Engineering Guidelines v2.0** - AI-native testing requirements
- **Latency Budgets** - < 200ms for Intent resolution, < 1s for chat
- **Trace-Based Tests** - Replay production traces in CI
- **Incompleteness Handling** - First-class support for PARTIAL intents
- **Autonomy Gating Tests** - Test-gated autonomy upgrades
- **VCR Pattern** - Record/replay for deterministic AI tests
- **Property-Based Testing** - Hypothesis for adversarial input generation

### Changed
- Updated `16_ANTIGRAVITY_ENGINEERING_GUIDELINES.md` with new testing pyramid
- Added "Performance & Latency Budgets" section
- Added "Conversational & Multi-Channel Testing" requirements

---

## [9.1.0] - 2026-01-08 - Canonical & Commercial

### Added
- **Autonomy Ceiling** concept - Partner-specific automation limits (0-5)
- **Partner Signal Profile** - Behavioral contract (trust_score, autonomy_ceiling, data_quality_score)
- **Commercial Autonomy Strategy** - Autonomy-Tier pricing model
- **Partner Scorecard** - Sales onboarding tool
- **Execution Formula** - `Decision = Confidence × Trust × Ceiling`
- **Autonomy Governance Layer** in roadmap

### Changed
- Updated `01_VISION_AND_STRATEGY.md` with Autonomy Tiers pricing
- Updated `06_GOVERNANCE_FRAMEWORK.md` with Autonomy Ceiling enforcement
- Updated `11_STAKEHOLDER_REVIEW_SALES.md` with Partner Scorecard

---

## [9.0.0] - 2026-01-07 - Karmic Completion

### Added
- **Core Freezing** - Cortex, Fluent, Motion declared immutable
- **Extension Seams** - Plugin points for extending functionality
- **Constitutional Protection** - Governance for core changes
- **Code-First Entity Resolution** - UN/LOCODE, IATA codes prioritized
- **Mode-Aware Governance** - Decision Contracts filter by transport mode
- **Autonomous Asset Support** - `autonomous_level` field for AVs
- **Polymorphic Storage Strategy** - JSON + indexed columns for Intent payloads

### Changed
- Updated Intent Library to v4.0 (Global Forwarding)
- Added HANDOFF stop type for AV-human transitions
- Updated 10-Year Evolution Map with autonomous trucks

---

## [8.0.0] - 2026-01-06 - Jupiter Maturity (Scale & Ecosystem)

### Added
- **External Developer SDKs** - `@skill` interface
- **Partner Nodes** (Satellite Mode) - Federated mesh support
- **Economic Primitives** - Decision Meter billing
- **Skill Marketplace** - Revenue sharing for third-party agents
- **Multi-Tenant Isolation** - Tenant-Key Encryption

---

## [7.0.0] - 2026-01-05 - Mercury + Jupiter Expansion

### Added
- **Agent-to-Agent (A2A) Protocols** - PROPOSE/ACCEPT/COUNTER negotiation
- **Policy-Driven Decision Layer** - Business rules in DocTypes (no code deployment)
- **Symmetric Overrides** - AI can block humans (Safety Mode)
- **Intent Life-Cycle States** - DRAFT, PROPOSED, NEGOTIATING, CONTRACTED, EXECUTED

---

## [6.0.0] - 2026-01-04 - Saturn Refinement (Stability & Contracts)

### Added
- **Schema Contracts** - Strict Pydantic enforcement at agent boundaries
- **Event Versioning** - Upcasting strategy for backward compatibility
- **Circuit Breakers** - Tenant-aware isolation for failing integrations
- **Immutable Traceability** - Cryptographic audit trails
- **Time Travel Replay** - Re-process past events with new logic
- **Dead Letter Jail** - For signals that fail processing

---

## [5.0.0] - 2026-01-03 - Stakeholder Aligned

### Added
- **Tiered Autonomy Subscription** - Pricing model
- **Data Privacy Protocol** - GDPR compliance
- **Redis Caching** for Entity Resolution
- **Deterministic Test Mode** - VCR pattern
- **Explicit Feedback** - Teacher UI for AI training

### Changed
- Integrated stakeholder feedback (Investor, Customer, Sales, Architect, Developer, QA)

---

## [4.0.0] - 2026-01-02 - Networked Intelligence

### Added
- **Federated Knowledge** - Global Entity Graph
- **Hybrid Entity Resolution** - Exact → Redis → Vector → Human
- **Constrained Generation** - Pydantic-constrained LLM outputs
- **Network Effects** - Cross-tenant learning (privacy-preserving)

---

## [3.0.0] - 2026-01-01 - Intent Graph Core

### Added
- **Intent Graph** - Canonical, Intent-Native (protocol-agnostic) intent representation
- **Governance Engine** - Decision Contracts for policy enforcement
- **IntentParser** - Extract intent from any signal

---

## [2.0.0] - 2025-12-31 - Cognitive Intent Hub

### Added
- **3-App Architecture** - Cortex, Fluent, Motion separation
- **Intent-First Design** - Shift from documents to intents
- **Governance Framework** - Progressive Trust Model

---

## [1.0.0] - 2025-12-30 - Vision Foundation

### Added
- **Problem Statement** - The "Intent Gap" in intent-native logistics
- **Vision & Strategy** - From documents to intent
- **10-Year Evolution Map** - Long-term roadmap

---

## Version Naming Convention

- **Major versions** (X.0.0) = Architectural paradigm shifts
- **Minor versions** (9.X.0) = Feature additions, new capabilities
- **Patch versions** (9.4.X) = Bug fixes, documentation updates

---

## Future Versions (Planned)

### [10.0.0] - Q2 2026 - Agent Marketplace
- Public SDK release
- Skill marketplace launch
- Revenue sharing model

### [11.0.0] - Q3 2026 - Agent-to-Agent Negotiation
- Level 5 Autonomy (Agentic Network)
- Cross-company agent collaboration
- Federated partner nodes

### [12.0.0] - Q4 2026 - Global Expansion
- EDIFACT support
- Multi-language UI
- Regional data centers

---

**How to Update This File**:
1. Add new entry under "Unreleased" during development
2. On release, move to new version section
3. Follow "Added/Changed/Deprecated/Removed/Fixed/Security" categories
