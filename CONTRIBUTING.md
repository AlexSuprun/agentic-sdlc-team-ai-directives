# Contributing to team-ai-directives

This repository is a living asset, maintained by the **AI Development Guild**. It is treated with the same rigor as our production code—each change shapes how our agents behave and impacts downstream automation.

## Governance Overview

All changes must be submitted via a Pull Request. The PR process requires peer review by at least one member of the AI Development Guild. This structured process ensures that all contributions are high-quality, align with our team's standards, and are well-documented before becoming part of our official library, guaranteeing downstream automation (spec-kit CLI, MCP, IDE scripts) remains trustworthy.

## Workflow

1. **Pull Latest Directives** – Before starting work, pull the latest changes from the team-ai-directives repository to ensure you are using the team's most current standards.
2. **Fork and Branch** – create feature branches named `feature/<slug>` or `docs/<slug>`.
3. **Add or Update Modules** – follow the directory conventions under `context_modules/`. Use standardized templates from the library for common tasks (e.g., reference existing examples or rules).
4. **Validate** – run linting or schema checks if provided, and ensure markdown renders cleanly.
5. **Document Impact** – note which projects or workflows need to update their references.
6. **Open a Pull Request** – include:
    - Summary of changes
    - Rationale and intended benefits
    - Any migration steps (e.g., "projects can checkout the v1.0.0 tag for old structure, new projects should use latest")".
7. **Guild Review** – at least one member of the AI Development Guild must approve before merge.
8. **Contribute Back via /levelup** – If you develop a highly effective new prompt or a "golden" example during your work, formalize it and submit back to this repository using the /levelup process to build the team's shared knowledge base.

## Guidelines

- Maintain a high signal-to-noise ratio: each directive should be actionable and unambiguous.
- Avoid leaking secrets or sensitive data; use anonymized examples.
- Prefer incremental git tags (v2.0.0, v3.0.0) when guidance changes materially.
- Keep examples up to date with current best practices and ensure they run or lint cleanly.
- Use structured references for cross-linking: `@rule:relative_path` (relative to rules/ directory), `@example:relative_path`, `@persona:name` to reduce duplication and enable tooling.
- Share learnings: After completing complex tasks, share your workflow, successful prompts, or challenges with the team in the AI Development Guild forum.

Thank you for helping keep our shared knowledge base sharp and reliable!
