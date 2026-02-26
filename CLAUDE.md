# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

This is a **knowledge repository**, not a software application. It contains version-controlled AI agent directives (Markdown files) implementing Factor XI ("Directives as Code") from the Twelve-Factor Agentic SDLC. There is no build step, no compiled code, and no application runtime.

## Repository Architecture

### Three-Layer Loading Order

All AI agent behavior follows this strict loading sequence defined in `AGENTS.md`:

1. **Constitution** (`context_modules/constitution.md`) — 11 non-negotiable principles, always loaded first
2. **Persona** (`context_modules/personas/`) — role-specific identity loaded based on task context
3. **Skill** (`skills/*/SKILL.md`) — self-contained capabilities triggered on-demand

Key architectural rule: **Skills are self-contained** and never use `@rule:` or `@example:` references. Rules are accessed through personas, not directly from skills.

### Cross-Referencing Syntax

Use structured references when linking between content:
- `@rule:relative_path` — reference a rule file
- `@example:relative_path` — reference an example file
- `@persona:name` — reference a persona

### Skills Registry

`.skills.json` is the **single source of truth** for skill discovery and policy. Every skill must be registered there. Skills have policy levels: `required`, `recommended`, or `blocked`.

Each skill's `SKILL.md` must have YAML frontmatter with `name` and `description` fields.

## Validation

The only test script is `scripts/test_github_mcp.py` (Python 3, no dependencies):
```
python3 scripts/test_github_mcp.py
```
It validates `.mcp.json` GitHub tool configuration and checks `GITHUB_TOKEN` authentication.

## MCP Configuration

`.mcp.json` configures two servers:
- **Context7**: documentation lookup via `@upstash/context7-mcp`
- **GitHub tool**: requires `GITHUB_TOKEN`, `GITHUB_OWNER`, and `GITHUB_REPO` environment variables

## Contributing Conventions

- All changes via Pull Request, reviewed by AI Development Guild
- Branch naming: `feature/<slug>` or `docs/<slug>`
- Commit prefixes: `docs:`, `feat:`, `fix:`, `refactor:`
- Markdown must render cleanly; use anonymized examples (no secrets)
- Incremental git tags for material changes
- Skills must have YAML frontmatter and be registered in `.skills.json`
- See `CONTRIBUTING.md` for full guidelines including the `/levelup` contribution process

## Key Files

| File | Purpose |
|---|---|
| `AGENTS.md` | Agent instructions and loading order |
| `context_modules/constitution.md` | 11 core principles governing all AI behavior |
| `.skills.json` | Skills registry and policy (single source of truth) |
| `.mcp.json` | MCP server configuration |
| `CONTRIBUTING.md` | PR workflow, skill contribution rules |
| `docs/skills.md` | Skills system deep-dive |
| `docs/personas.md` | Personas system deep-dive |
