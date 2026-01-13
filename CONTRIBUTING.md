---
title: "Contributing"
tags: []
version: "9.1"
last_updated: "2026-01-12"
---

# Contributing to Flowwolf Sentinel

We welcome contributions to the world's first **Intent-Native Operating System** for logistics. This guide outlines our AI-native development workflow and the standards we follow.

## 🤖 AI-Native Development Principle
This project follows an **AI-First** development philosophy. We leverage AI to generate 100% of the code, documentation, and tests. Humans act as **Architects and Reviewers**, providing strategic direction and verifying quality (UAT).

## Getting the Code
```bash
# Install the app in your bench environment
bench get-app flowwolf_sentinel
bench install-app flowwolf_sentinel
```

## Development Workflow
1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Design with Intent** – Start by updating the relevant docs in `docs/` (e.g., `docs/founders/` or `docs/architecture/`).
3. **AI-Driven Implementation** – Use your AI assistant to generate the code based on the updated design docs.
4. **TDD Compliance** – All logic must be backed by unit tests. **Test First, or Don’t Type.**
   ```bash
   bench --site your-site run-tests --app flowwolf_sentinel
   ```
5. **Commit & Push**
   ```bash
   git add .
   git commit -m "feat: [AI-Generated] brief description"
   git push origin feature/your-feature-name
   ```

## Code Style & Standards
- **Python** – Follow PEP8, use Type Hints, and adhere to the **Engineering Constitution**.
- **Frappe Integration** – Follow the **3-App Triad** strategy (`fw_cortex`, `fw_fluent`, `fw_motion`).
- **DocTypes** – Use the `fw` prefix for execution and `Flowwolf` for authority.

## 📚 Documentation
- All docs live in the `docs/` hierarchy (e.g., `docs/founders/`, `docs/architecture/`).
- Use **kebab-case** for all filenames.
- Ensure every new `.md` file has the standard YAML front-matter and is versioned at `9.1`.

## License
This project is licensed under the MIT License – see `license.txt`.

