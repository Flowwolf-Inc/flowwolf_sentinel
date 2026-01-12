# Contributing to Flowwolf Autonomous Antigravity

We welcome contributions to the world's first **Intent-Native Operating System** for logistics. This guide outlines our AI-native development workflow and the standards we follow.

## 🤖 AI-Native Development Principle
This project follows an **AI-First** development philosophy. We leverage AI (like Cursor, Claude, or GPT-4) to generate 100% of the code, documentation, and tests. Humans act as **Architects and Reviewers**, providing strategic direction and verifying quality (UAT).

## Getting the Code
```bash
# Install the app in your bench environment
bench get-app flowwolf_autonomous_antigravity
bench install-app flowwolf_autonomous_antigravity
```

## Development Workflow
1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Design with Intent** – Start by updating the relevant docs in `docs/` (e.g., architecture or features).
3. **AI-Driven Implementation** – Use your AI assistant to generate the code based on the updated design docs.
4. **TDD Compliance** – All logic must be backed by unit tests.
   ```bash
   bench --site your-site run-tests --app flowwolf_autonomous_antigravity
   ```
5. **Commit & Push**
   ```bash
   git add .
   git commit -m "feat: [AI-Generated] brief description"
   git push origin feature/your-feature-name
   ```

## Code Style & Standards
- **Python** – Follow PEP8, use `black` and `flake8` (via `pre-commit`).
- **Frappe Integration** – Follow the **3-App Triad** strategy (Domain Logic, UI/Page, API).
- **DocTypes** – Ensure all fields are semantically named and documentation-ready.

## 📚 Documentation
- All docs live in the `docs/` hierarchy (e.g., `docs/foundation/`, `docs/architecture/`).
- Use **kebab-case** for all new filenames.
- Ensure every new `.md` file has the standard YAML front-matter.

## License
This project is licensed under the MIT License – see `license.txt`.
