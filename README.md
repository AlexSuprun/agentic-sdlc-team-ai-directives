# The team-ai-directives Repository

## The Central Library for Version-Controlled Agent Behavior

The team-ai-directives repository is the practical codification of **Factor XI: Directives as Code**. It is the central, version-controlled library that houses the collective AI-related intelligence of our engineering team. It serves as the single source of truth for all reusable components that guide our AI agents, consumed directly by **Agentic SDLC spec-kit CLI** and any **Orchestration Hub (MCP Server) implementation**.

## Core Philosophy

The repository's philosophy is centered on serving a central system, not individual developers.

1. **A Library for a Service:** This repository's sole purpose is to store the "what"—the canonical, version-controlled context modules. The "how" and "why" of a specific task—the Mission Brief—lives in our issue tracker and is orchestrated by the **spec-kit CLI (and any MCP server)**, which fetches the necessary modules from a **local clone of this library** on-demand.
2. **The System of Record for Guidance:** This repository stores the building blocks of agentic guidance. The CLI and MCP server assemble these blocks based on a Mission Brief to guide an agent. This separation is critical:
   * The **Repository** is for stable, reusable, versioned knowledge.
   * The **Orchestration Layer** (spec-kit CLI, MCP server, or other automation) is for dynamic, task-specific assembly and execution.
3. **Controlled Local Replication**: Each project maintains a local checkout (e.g., `.specify/memory/team-ai-directives` or a configured path exported via `SPECIFY_TEAM_DIRECTIVES`). Scripts and CLI commands pull from that checkout so every agent session—autonomous or human supervised—operates with identical directives.

## Repository Layout

```
team-ai-directives/
├── README.md
├── CONTRIBUTING.md
├── .mcp.json
└── context_modules/
    ├── constitution.md   # <-- The foundational principles for all AI behavior
    ├── examples/
    │   ├── testing/
    │   │   └── pytest_class_based.md
    │   └── …
    ├── personas/
    │   ├── senior_python_developer.md
    │   └── …
    ├── principles/
    │   ├── stateless_services.md
    │   ├── zero_trust_security_model.md
    │   └── …
    └── rules/
        ├── security/
        │   └── prevent_sql_injection.md
        └── style-guides/
            └── python_pep8_and_docstrings.md
```

## Directory Functions

* **/context_modules/:** The heart of the repository. This is the canonical source for the spec-kit CLI (and MCP server) pulls from when preparing specifications, plans, tasks, and implementations.
* **.mcp.json:** This file is a configuration manifest that acts as a service directory for the platform. It defines the approved autonomous agents and specialized tools the team can use, telling the spec-kit CLI and any orchestration server how to connect to them.
* **constitution.md:** The most important file in the repository. It contains the foundational, non-negotiable engineering principles that govern all AI behavior. It is injected by the CLI (and any MCP orchestration) as the base context for major planning tasks.
* **/examples/:** High-quality code **examples** that serve as a "gold standard" for the AI to follow.
* **/personas/:** Pre-defined AI personalities tailored for specific tasks (e.g., "senior python developer," "security expert").
* **/principles/:** Contains high-level, foundational engineering principles that can be imported into a project's constitution.md.
* **/rules/:** Explicit guidelines for style, security standards, and architectural patterns.
* **A Note on Versioning:** Treating our directives as a versioned library is non-negotiable. We use git tags (v1.0.0, v2.0.0, etc.) to manage breaking changes gracefully and support multiple standards across different projects.

## Usage

Point your Agentic SDLC Spec Kit or orchestration tooling at this repository to resolve `@team/...` references. Use git tags (v1.0.0, v2.0.0, etc.) when evolving personas, examples, or rules so downstream consumers can opt in to breaking changes safely.

## Governance and Contribution

This repository is a living asset, maintained by the **AI Development Guild**. It is treated with the same rigor as our production code.

* All changes must be submitted via a Pull Request.
* The PR process is defined in CONTRIBUTING.md and requires peer review.
* This structured process ensures that all contributions are high-quality, align with our team's standards, and are well-documented before becoming part of our official library, guaranteeing downstream automation (spec-kit CLI, MCP, IDE scripts) remains trustworthy.
