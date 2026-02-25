# Skills

Skills are self-contained, reusable AI agent capabilities. Each skill packages a domain's instructions, context, and optional automation so an AI agent can reliably apply it on demand without requiring the user to supply background knowledge each time.

---

## Table of Contents

1. [How Skills Work](#1-how-skills-work)
2. [Skill Folder Structure](#2-skill-folder-structure)
3. [The `.skills.json` Manifest](#3-the-skillsjson-manifest)
4. [Configuring Skills](#4-configuring-skills)
5. [Creating a New Skill](#5-creating-a-new-skill)
6. [Using Skills as an Agent](#6-using-skills-as-an-agent)
7. [External Skills](#7-external-skills)
8. [Policy Settings](#8-policy-settings)

---

## 1. How Skills Work

When a user makes a request, an agent:

1. Reads `.skills.json` to discover available skills.
2. Matches the user's intent against each skill's `description` and trigger phrases.
3. Loads the relevant `SKILL.md` to obtain domain-specific instructions.
4. Optionally loads files from `references/` for deeper context.
5. Applies the skill while completing the task.

Skills are loaded **on-demand** — only the skills relevant to the current request are activated. Required skills defined in `.skills.json` are always available to the agent.

---

## 2. Skill Folder Structure

All internal skills live under `skills/{skill-name}/`:

```
skills/
└── my-skill/
    ├── SKILL.md          # Required — primary instructions for the agent
    ├── references/       # Optional — supplementary reference documents
    │   ├── guide.md
    │   └── patterns.md
    └── scripts/          # Optional — automation scripts for the skill
        └── setup.sh
```

### `SKILL.md`

The entry point for every skill. It uses a YAML front matter block to declare metadata, followed by Markdown instructions:

```yaml
---
name: my-skill
description: >
  Short description of the skill's purpose.
  Use when [trigger phrases that describe when to activate this skill].
---

# My Skill

## What This Skill Provides
...

## When to Use This Skill
...

## Core Patterns
...
```

The `description` field is critical — it tells the agent **when** to activate the skill. Write it in natural language and include representative phrases a user might say.

### `references/`

Supporting Markdown documents loaded on-demand when the agent needs deeper detail on a subtopic. Reference files should be focused and independently readable. Link to them from `SKILL.md` using relative paths (e.g., `See references/guide.md`).

### `scripts/`

Optional shell or Python scripts that automate tasks the skill describes. Include a comment header in each script explaining its purpose and usage.

---

## 3. The `.skills.json` Manifest

`.skills.json` is the single source of truth for skill discovery and policy. It defines which skills are required, recommended, internal, blocked, or available in the registry.

```json
{
  "version": "1.0.0",
  "source": "team-ai-directives",
  "description": "Team skills manifest for the Skills Package Manager.",
  "skills": {
    "required": { ... },
    "recommended": { ... },
    "internal": { ... },
    "blocked": [ ... ]
  },
  "registry": {
    "description": "Additional skills available for manual discovery.",
    "skills": { ... }
  },
  "policy": { ... }
}
```

### Skill Categories in `.skills.json`

| Category | Meaning |
|---|---|
| `required` | Always loaded by the agent; auto-installed if `auto_install_required` is `true` |
| `recommended` | Suggested skills; surfaced to the agent but not mandatory |
| `internal` | Skills hosted locally in this repository |
| `blocked` | Skills explicitly prohibited; the agent must refuse to use them |
| `registry` | Additional skills available for on-demand discovery and installation |

### Skill Entry Format

Each skill entry in the manifest uses a URI as its key:

- **Local skill**: `"local:./skills/my-skill"`
- **External skill**: `"github:org/repo/skill-name"`

```json
"local:./skills/my-skill": {
  "version": "*",
  "description": "Human-readable description of what the skill does.",
  "categories": ["tag1", "tag2"]
}
```

External skills add `source` and `url` fields pointing to the raw `SKILL.md`:

```json
"github:org/repo/skill-name": {
  "version": "^1.0.0",
  "description": "...",
  "categories": ["..."],
  "source": "https://github.com/org/repo",
  "url": "https://raw.githubusercontent.com/org/repo/main/skills/skill-name/SKILL.md"
}
```

---

## 4. Configuring Skills

### Adding a Local Skill

1. Create the skill folder and `SKILL.md` (see [Creating a New Skill](#5-creating-a-new-skill)).
2. Register the skill in `.skills.json` under the appropriate category:

```json
"skills": {
  "required": {
    "local:./skills/my-skill": {
      "version": "*",
      "description": "What my skill does.",
      "categories": ["my-category"]
    }
  }
}
```

### Adding an External Skill

External skills are fetched from a URL at runtime. Add them to `recommended` or `registry`:

```json
"recommended": {
  "github:org/repo/skill-name": {
    "version": "^1.0.0",
    "description": "Short description with trigger phrases.",
    "categories": ["relevant", "tags"],
    "source": "https://github.com/org/repo",
    "url": "https://raw.githubusercontent.com/org/repo/main/skills/skill-name/SKILL.md"
  }
}
```

### Blocking a Skill

To prevent an agent from using a specific skill (e.g., a deprecated or insecure external skill), add it to the `blocked` list:

```json
"blocked": [
  {
    "id": "github:unsafe-org/deprecated-skill",
    "reason": "Security vulnerability - deprecated by maintainer"
  }
]
```

---

## 5. Creating a New Skill

```bash
mkdir -p skills/my-skill/references
```

Create `skills/my-skill/SKILL.md`:

```yaml
---
name: my-skill
description: >
  Describe what the skill does. Use when the user asks to [action],
  [another action], or [trigger phrase].
---

# My Skill

## What This Skill Provides

Brief overview of the domain knowledge and capabilities this skill covers.

## When to Use This Skill

- Scenario 1
- Scenario 2

## Core Patterns

### Pattern Name

**Rule**: State the rule clearly.

**Implementation**:
- Step or detail
- Step or detail

**References**: See references/guide.md
```

Then register it in `.skills.json` (see [Configuring Skills](#4-configuring-skills)).

---

## 6. Using Skills as an Agent

When processing a request, an agent resolves skills in this order:

1. **Constitution** — `context_modules/constitution.md` (always loaded).
2. **Persona** — relevant file from `context_modules/personas/` based on task context.
3. **Skill** — triggered by matching the user's intent to a skill description.

To activate a skill manually, tell the agent which skill to use:

> "Using the `github-actions` skill, create a reusable workflow for deploying to Kubernetes."

The agent will read `skills/github-actions/SKILL.md` and any referenced rule files before responding.

### Example: dbt Template Skill

The `dbt-template` skill is activated when a user asks to:
- Create a new dbt project
- Run data transformation pipelines
- Set up analytics engineering workflows

It is registered as `required`, so it is always available.

### Example: GitHub Actions Skill

The `github-actions` skill is activated when a user asks about:
- Writing or reviewing GitHub Actions workflow files
- Setting up reusable or organization-level shared workflows
- Configuring OIDC for AWS, GCP, or Azure authentication

It is registered as `recommended` and internally hosted. Trigger it with:

> "Write a reusable GitHub Actions workflow that builds a Docker image and pushes to GHCR."

### Example: Helm Charts Skill

The `helm-charts` skill is activated when a user asks about:
- Creating or reviewing Helm charts
- Building chart library abstractions or wrapper charts
- Packaging and publishing charts to an OCI registry

Trigger it with:

> "Design a Helm chart library for our Kubernetes platform with shared templates for Deployment and Service resources."

### Example: External Secrets Skill

The `external-secrets` skill is activated when a user asks about:
- Configuring External Secrets Operator with AWS Secrets Manager or GCP Secret Manager
- Designing a DRY secrets management strategy across namespaces
- Implementing secret rotation without pod restarts

Trigger it with:

> "Set up an ExternalSecret that pulls database credentials from GCP Secret Manager into a Kubernetes namespace."

### How Personas and Skills Work Together

A persona and one or more skills are loaded at the same time. They complement rather than duplicate each other.

For example, a DevOps Engineer session might look like:

1. **Constitution** — foundational team principles always apply
2. **Persona**: `devops_engineer.md` — sets the role identity, collaboration preferences, and tool context
3. **Skill**: `github-actions` — activated when the user asks about CI/CD pipelines
4. **Skill**: `helm-charts` — activated when the user asks about packaging for Kubernetes

The persona tells the agent *who it is*. The skills tell it *how to execute* specific tasks.

---

## 7. External Skills

External skills are fetched at runtime from their `url` field in `.skills.json`. They are not stored locally in this repository.

To discover registry skills, ask your AI agent:

> "What skills are available in the registry?"

The agent will read `.skills.json`, list the `registry` entries, and describe when each is useful. To use one, the agent fetches the `SKILL.md` from the provided `url`.

Currently available registry skills (see [`.skills.json`](../.skills.json) for full details):

| Skill | Description |
|---|---|
| `react-best-practices` | React and Next.js performance optimization, 40+ rules |
| `web-design-guidelines` | Accessibility, performance, and UX audits, 100+ rules |
| `composition-patterns` | React compound component and composition patterns |
| `react-native-guidelines` | React Native and Expo best practices |
| `vercel-deploy-claimable` | Deploy to Vercel directly from a conversation |

---

## 8. Policy Settings

The `policy` section of `.skills.json` controls agent behavior:

```json
"policy": {
  "auto_install_required": true,
  "enforce_blocked": true,
  "allow_project_override": true
}
```

| Setting | Default | Description |
| --- | --- | --- |
| `auto_install_required` | `true` | Required skills are automatically loaded without user prompting |
| `enforce_blocked` | `true` | The agent refuses to use any skill in the `blocked` list |
| `allow_project_override` | `true` | Individual projects can override manifest settings locally |
