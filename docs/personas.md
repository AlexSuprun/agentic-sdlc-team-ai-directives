# Personas

Personas define the role, expertise, preferences, and rule references that shape how an AI agent behaves for a given engineering context. Loading a persona tells the agent _who_ it is for this session — its values, collaboration style, and which domain-specific rules to apply.

---

## Table of Contents

1. [How Personas Work](#1-how-personas-work)
2. [Persona Folder Structure](#2-persona-folder-structure)
3. [Persona File Anatomy](#3-persona-file-anatomy)
4. [Built-In Personas](#4-built-in-personas)
5. [Creating a Custom Persona](#5-creating-a-custom-persona)
6. [Using Personas](#6-using-personas)
7. [Personas vs. Skills](#7-personas-vs-skills)

---

## 1. How Personas Work

When an agent begins a session, it loads context in this order:

1. **Constitution** (`context_modules/constitution.md`) — non-negotiable team principles applied to every interaction.
2. **Persona** (`context_modules/personas/*.md`) — role-specific defaults, rules, and collaboration style.
3. **Skills** (`skills/*/SKILL.md`) — on-demand capabilities triggered by the user's request.

A persona sits between the universal constitution and the task-specific skill. It tells the agent:
- What domain knowledge to prioritize
- Which rule files are relevant to its role
- How to collaborate (communication style, review preferences, workflow assumptions)
- Agent-specific guidance (e.g., always propose infra changes as code)

Personas are **passive by default** — they don't activate automatically unless your tooling or prompt instructs the agent to load one. You attach a persona to an agent through your IDE settings, a system prompt, or a prompt prefix (see [Using Personas](#6-using-personas)).

---

## 2. Persona Folder Structure

All personas live in `context_modules/personas/`:

```
context_modules/
└── personas/
    ├── cloud_native_platform_architect.md
    ├── data_analyst.md
    ├── devops_engineer.md
    ├── senior_java_developer.md
    └── senior_python_developer.md
```

Each persona is a single Markdown file. There is no sub-folder nesting — one file per role.

---

## 3. Persona File Anatomy

A well-formed persona file contains some or all of the following sections:

### `# Persona: <Name>` (required)

The heading names the persona. Agents use this as the persona identifier.

```markdown
# Persona: DevOps Engineer
```

---

### `## Summary` (required)

Describes the persona's **motivation**, **pain points**, and **success criteria**. This is the first context an agent reads to understand its role.

```markdown
## Summary
- **Motivation**: Enable reliable, scalable, and secure software delivery through automation, IaC, and observability.
- **Pain Points**: Manual deployments, configuration drift, lack of visibility.
- **Success Criteria**: Fully automated CI/CD pipelines, declarative infrastructure, secure secret management.
```

For simpler personas, this can be a plain bullet list of responsibilities instead of the structured sub-keys.

---

### `## Rule References` (recommended)

Links the persona to domain-specific rule files using the `@rule:<path>` syntax. Agents resolve these paths relative to `context_modules/rules/`.

```markdown
## Rule References
- CI/CD Pipelines: @rule:devops/github_actions.md
- Secrets Management: @rule:devops/external_secrets_operator.md, @rule:devops/secrets_management_dry.md
- Testing: @rule:testing/python_testing.md
```

Rules are loaded on-demand when the agent determines they are relevant to the task. A persona can reference many rules; not all will be loaded every time.

---

### `## Collaboration Preferences` (recommended)

Describes how the persona prefers to work: communication style, review expectations, workflow assumptions, and advocacy positions.

```markdown
## Collaboration Preferences
- Prefers infrastructure changes reviewed through pull requests with clear descriptions
- Values declarative configurations over imperative scripts
- Expects "everything as code" — infrastructure, configs, and pipelines in version control
```

---

### `## Tool Context` (optional)

Lists the tooling ecosystem this persona operates in. Helps agents make appropriate technology choices without asking the user every time.

```markdown
## Tool Context
- CI: GitHub Actions, GitLab CI
- CD/GitOps: ArgoCD, Flux
- IaC: Terraform, Crossplane
- Secrets: HashiCorp Vault, AWS Secrets Manager
```

---

### `## Guidance for Agents` (optional)

Explicit behavioral instructions for agents taking actions on behalf of this persona.

```markdown
## Guidance for Agents
- Always propose infrastructure changes as code, never manual operations
- When working with secrets, always use secret management services — never hardcode or commit secrets
- Always consider disaster recovery, backup strategies, and rollback procedures
```

---

### `## Core Philosophy` (optional)

For senior or architect-level personas, this section captures overarching design principles that inform every decision. These are applied before domain rules are consulted.

```markdown
## Core Philosophy
- GitOps as the Source of Truth: If it isn't in Git, it doesn't exist.
- DRY: Use templates and compositions to eliminate duplication.
- Security-Shift-Left: Integrate scanning and least-privilege access by default.
```

---

### `## The Interaction Protocol` (optional, advanced)

For complex personas (e.g., architects), this section defines a **context-switching framework** — a structured step-by-step process the agent follows to identify which domain it's working in and which rules to activate.

```markdown
## The Interaction Protocol

Before providing a solution, identify the Domain Context:
1. CI Domain, 2. Packaging Domain, 3. GitOps Domain, 4. IaC Domain

Step 1: Identify Domain Context (ask clarifying questions if needed)
Step 2: Activate the relevant rule file
Step 3: Provide Architectural Reasoning → Code → Verification
```

---

## 4. Built-In Personas

| File | Persona | Primary Domain |
|---|---|---|
| `senior_python_developer.md` | Senior Python Developer | Python, PEP 8, testing, CI/CD |
| `senior_java_developer.md` | Senior Java Developer | Java, Spring Boot, JUnit 5, Google Style |
| `devops_engineer.md` | DevOps Engineer | CI/CD, Helm, IaC, secrets management, GitOps |
| `cloud_native_platform_architect.md` | Cloud-Native Platform Architect | Kubernetes, Crossplane, ArgoCD, platform engineering |
| `data_analyst.md` | Data Analyst | SQL, dashboards, reproducible reporting, large datasets |

Each built-in persona is self-contained and production-ready. Fork and adjust them to match your team's specific tooling and standards.

---

## 5. Creating a Custom Persona

1. Create a new file in `context_modules/personas/`:

   ```bash
   touch context_modules/personas/my_role.md
   ```

2. Add the following template and fill it in:

   ```markdown
   # Persona: My Role

   ## Summary
   - **Motivation**: [What drives this role]
   - **Pain Points**: [What slows them down]
   - **Success Criteria**: [What good looks like]

   ## Rule References
   - [Domain]: @rule:[domain]/[rule-file].md

   ## Collaboration Preferences
   - [How this persona prefers to work]

   ## Tool Context
   - [Tools and platforms this persona uses]

   ## Guidance for Agents
   - [Behavioral instructions for autonomous actions]
   ```

3. Reference any applicable rule files from `context_modules/rules/`. Browse the available rules:

   ```
   context_modules/rules/
   ├── devops/
   ├── framework/
   ├── orchestration/
   ├── security/
   ├── style-guides/
   └── testing/
   ```

4. Attach the persona in your agent configuration (see [Using Personas](#6-using-personas)).

---

## 6. Using Personas

### Option A: IDE Custom Instructions (GitHub Copilot)

In VS Code with GitHub Copilot, add the persona content directly to a `.github/copilot-instructions.md` file or reference it in your workspace settings:

```json
// .vscode/settings.json
{
  "github.copilot.chat.codeGeneration.instructions": [
    { "file": "context_modules/personas/devops_engineer.md" }
  ]
}
```

This makes the DevOps Engineer persona active for all code-generation requests in the workspace. The persona automatically references the right rule files (`@rule:devops/github_actions.md`, etc.) so the agent knows its standards without you repeating them each session.

### Option B: System Prompt Prefix

Prepend the persona content to your agent's system prompt:

```
[Load persona: context_modules/personas/devops_engineer.md]

User request: ...
```

### Option C: Prompt Reference at Session Start

Tell the agent explicitly which persona to adopt at the start of a conversation:

```
You are acting as the DevOps Engineer persona defined in
context_modules/personas/devops_engineer.md. Load that file
and apply it to all responses in this session.
```

### Option D: AGENTS.md Loading Order

The [AGENTS.md](../AGENTS.md) file documents the canonical loading order agents should follow when bootstrapping:

1. Constitution → 2. Persona → 3. Skill

Agents that read `AGENTS.md` on startup will automatically know to load a persona before activating skills.

---

## 7. Personas vs. Skills

| | Persona | Skill |
|---|---|---|
| **Purpose** | Defines _who_ the agent is | Defines _what_ the agent can do |
| **Scope** | Entire session | Triggered per task |
| **Location** | `context_modules/personas/` | `skills/*/SKILL.md` |
| **Activation** | Loaded at session start | Loaded on-demand by trigger phrases |
| **Registered in `.skills.json`?** | No | Yes |
| **Contains rules?** | References rules via `@rule:` | May embed rules inline |

A persona provides the stable identity and preferences for a session. Skills provide the domain-specific execution instructions for individual tasks. They complement each other and are both loaded alongside the constitution.

### Real-World Example: DevOps Engineer + Tool Skills

The `devops_engineer` persona defines the *role*: motivation, collaboration style, tool philosophy, and which rule families apply. It does **not** duplicate the content of those rules.

The tool-specific skills define the *how* for each domain:

| Persona | Triggered Skills | When the skill activates |
| --- | --- | --- |
| `devops_engineer.md` | `github-actions` | User asks to write or review a CI/CD pipeline |
| `devops_engineer.md` | `helm-charts` | User asks to create or package a Helm chart |
| `devops_engineer.md` | `crossplane` | User asks to write an infrastructure Composition or XRD |
| `devops_engineer.md` | `external-secrets` | User asks about secret management in Kubernetes |
| `devops_engineer.md` | `gke-workload-identity` | User asks about GCP authentication from GKE pods |

A task like _"Write a GitHub Actions workflow that builds our app and pushes to GKE"_ would activate:
1. **Persona** `devops_engineer.md` — already loaded as session identity
2. **Skill** `github-actions` — triggered by "GitHub Actions workflow"
3. **Skill** `gke-workload-identity` — triggered by "pushes to GKE" (OIDC auth pattern)

`devops-engineer` as a skill would have been wrong because it had no clear trigger phrase — it was a role, not a task.

See [docs/skills.md](skills.md) for full documentation on skills.
