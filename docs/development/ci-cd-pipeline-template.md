---
title: "Ci Cd Pipeline Template"
tags: []
version: "9.1"
last_updated: "2026-01-12"
---

# CI/CD Pipeline Configuration

**Version**: 9.4.2  
**Purpose**: Automated testing and coverage enforcement  
**Fixes**: GAP-C2

---

## GitHub Actions Workflow

Create `.github/workflows/ci.yml` in each app:

```yaml
name: Antigravity CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      mariadb:
        image: mariadb:10.6
        env:
          MYSQL_ROOT_PASSWORD: root
        ports:
          - 3306:3306
      
      redis:
        image: redis:7
        ports:
          - 6379:6379
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install Frappe Bench
        run: |
          pip install frappe-bench
          bench init --frappe-branch version-15 frappe-bench
          cd frappe-bench
      
      - name: Install App
        run: |
          cd frappe-bench
          bench get-app ${{ github.workspace }}
          bench new-site test.localhost --admin-password admin
          bench --site test.localhost install-app $(basename ${{ github.workspace }})
      
      - name: Run Tests
        run: |
          cd frappe-bench
          bench run-tests --app $(basename ${{ github.workspace }}) --coverage
      
      - name: Check Coverage
        run: |
          cd frappe-bench
          bench coverage --app $(basename ${{ github.workspace }}) --fail-under=100
      
      - name: Upload Coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./frappe-bench/coverage.xml
```

---

## Pre-Commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.0
    hooks:
      - id: black
        language_version: python3.11
  
  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        args: ['--max-line-length=88']
  
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v9.1
    hooks:
      - id: mypy
        additional_dependencies: [pydantic]
```

---

## Local Test Commands

```bash
# Run all tests
bench run-tests --app fw_cortex

# Run with coverage
bench run-tests --app fw_cortex --coverage

# Run specific test file
bench run-tests --app fw_cortex --module tests.test_intent_graph

# Check coverage threshold
bench coverage --app fw_cortex --fail-under=100

# Run type checking
mypy apps/fw_cortex

# Format code
black apps/fw_cortex
```

---

## Performance Tests (Latency Budget)

Create `.github/workflows/performance.yml`:

```yaml
name: Performance Tests

on:
  push:
    branches: [ main ]

jobs:
  latency:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Latency Tests
        run: |
          bench run-tests --app fw_cortex --module tests.performance.test_latency_budget
      
      - name: Fail if budget exceeded
        run: |
          # Assert Intent resolution < 200ms
          # Assert Chat response < 1s
          # Assert Execution decision < 100ms
```

---

**Status**: CI/CD pipeline template ready for deployment.
