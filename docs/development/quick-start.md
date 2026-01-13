---
title: "Quick Start Guide"
tags: []
version: "9.1"
last_updated: "2026-01-13"
---

# Developer Quick Start Guide

**Version**: 9.4 (Agentic Core)
**Target Audience**: New developers joining the Antigravity Flowwolf Sentinel project
**Time to Complete**: 30 minutes

---

## Prerequisites

Before you begin, ensure you have:

- **Python 3.11+** installed (`python --version`)
- **Node.js 18+** installed (`node --version`)
- **Redis** installed and running (`redis-cli ping`)
- **MariaDB 10.6+** installed
- **Git** configured with SSH keys
- **VS Code** (recommended) with Python extension

---

## 5-Minute Local Setup

### Step 1: Initialize Frappe Bench

```bash
# Install bench CLI
pip install frappe-bench

# Initialize bench (development mode)
bench init --frappe-branch version-15 frappe-bench
cd frappe-bench

# Create site
bench new-site development.localhost --admin-password admin
bench use development.localhost
```

### Step 2: Install the 3 Apps

```bash
# Install Cortex (The Brain)
bench new-app fw_cortex
bench --site development.localhost install-app fw_cortex

# Install Fluent (The Translator)
bench new-app fw_fluent
bench --site development.localhost install-app fw_fluent

# Install Motion (The Body)
bench new-app fw_motion
bench --site development.localhost install-app fw_motion
```

### Step 3: Run Your First Test

```bash
# Run unit tests for Cortex
bench run-tests --app fw_cortex

# Expected output: All tests pass ✅
```

### Step 4: Start Development Server

```bash
# Start bench (auto-reload enabled)
bench start
```

### Step 5: Access the System

- **Frontend**: http://development.localhost:8000
- **Login**: Administrator / admin
- **API Docs**: http://development.localhost:8000/api/docs

---

##Architecture Overview

```
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│  fw_cortex   │ ───> │  fw_fluent   │ ───> │  fw_motion   │
│   (The Brain)   │      │ (The Translator)│      │   (The Body)    │
└─────────────────┘      └─────────────────┘      └─────────────────┘
       │                         │                         │
       v                         v                         v
  Intent Graph            Signal Ingestion           Load Execution
  Entity Resolution       Protocol Adapters          TMS Business Logic
  Governance Engine       Universal Ingestor         Shipment DocTypes
```

**Data Flow**:
1. **Signal** (EDI/Email/API) arrives at `Fluent`
2. `Fluent` normalizes → sends to `Cortex`
3. `Cortex` creates **Intent** → checks **Governance**
4. If approved → `Cortex` calls **AgentContract** in `Motion`
5. `Motion` creates **Load** → executes business logic

---

## PR Checklist

Before submitting a PR, ensure:

- [ ] All new functions have **type hints**
- [ ] Coverage ≥ **100%** on modified lines
- [ ] No `frappe.db.sql` in business logic
- [ ] Pydantic models for all DTOs
- [ ] **Trace ID** propagated through function calls
- [ ] Performance test if latency-sensitive (< 200ms budget)

---

## Useful Commands

```bash
# Run all tests
bench run-tests

# Run tests for one app
bench run-tests --app fw_cortex

# Check coverage
bench coverage --app fw_cortex

# Format code
black apps/fw_cortex

# Type check
mypy apps/fw_cortex

# Start interactive Python shell
bench console
```

---

## Getting Help

- **Documentation**: `/docs/Antigravity_Flowwolf_Autonomous/00_MASTER_MANIFEST.md`
- **Glossary**: `26_GLOSSARY.md`
- **FAQ**: `27_FAQ.md`

Welcome to Antigravity! 🚀