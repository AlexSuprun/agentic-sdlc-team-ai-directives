# GitHub MCP Guide

This guide explains what the Model Context Protocol (MCP) is, how to configure the GitHub MCP in this repo, and how to get an AI agent to use it effectively.

---

## Table of Contents

1. [What is an MCP?](#1-what-is-an-mcp)
2. [How to Configure the GitHub MCP](#2-how-to-configure-the-github-mcp)
3. [How the GitHub MCP Can Be Used](#3-how-the-github-mcp-can-be-used)
4. [Getting an Agent to Use the GitHub MCP](#4-getting-an-agent-to-use-the-github-mcp)

---

## 1. What is an MCP?

**MCP** stands for **Model Context Protocol**. Think of it as a standardized plug-in system that lets AI agents talk to external tools and services — like GitHub, Linear, or a database — without you having to write custom integration code each time.

Without MCP, an AI agent can only work with text you paste into the conversation. With MCP, the agent gains live, structured access to real systems.

### Analogy

Imagine a highly skilled contractor who can only work with the blueprints you hand them. MCP is like giving that contractor a badge that lets them walk into the building, read the plans on-site, open pull requests, and file issues — in real time.

### Key concepts

| Term | What it means |
| --- | --- | --- |
| **MCP server** | A small process that wraps an external tool (GitHub, a database, etc.) and exposes its actions over a standard protocol |
| **MCP client** | The AI agent or IDE extension that connects to MCP servers and calls their actions |
| **`.mcp.json`** | The config file that tells your AI client which MCP servers to start and how to reach them |
| **Tool / action** | A specific capability an MCP server exposes, e.g. "create a pull request" or "list open issues" |

---

## 2. How to Configure the GitHub MCP

### Prerequisites

- A GitHub account with a [Personal Access Token (PAT)](https://github.com/settings/tokens) that has `repo` scope (or fine-grained permissions for the repos you need).
- Node.js 18+ installed (used to run MCP servers via `npx`).

### Step 1 — Export your token

```bash
export GITHUB_TOKEN=ghp_your_token_here
```

Add this to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.) so it persists across sessions. Alternatively, use `.envrc` files with [direnv](https://direnv.net/) to automatically load project-specific environment variables.

### Step 2 — Edit `.mcp.json`

At the root of this repo there is a `.mcp.json` file. Update it with your organization and repository:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  },
  "tools": {
    "github": {
      "type": "github",
      "tokenEnv": "GITHUB_TOKEN",
      "owner": "YOUR_ORG_OR_USERNAME",
      "repo": "YOUR_REPO_NAME",
      "baseUrl": "https://api.github.com"
    }
  }
}
```

Replace `YOUR_ORG_OR_USERNAME` and `YOUR_REPO_NAME` with your actual values.

> **GitHub Enterprise users:** Change `baseUrl` to your enterprise API endpoint, e.g. `https://github.example.com/api/v3`.

### Step 3 — Verify the MCP configuration

```bash
python3 scripts/test_github_mcp.py
```

---

## 3. How the GitHub MCP Can Be Used

Once configured, the GitHub MCP gives your AI agent real-time, read/write access to GitHub. Here is a sample of what it can do:

### Reading & discovery

- List open issues and pull requests
- Read file contents from any branch or commit
- Search for code, issues, or commits across a repository
- Fetch PR review comments and CI status checks

### Writing & collaboration

- Create issues with labels, assignees, and milestones
- Open pull requests from a source branch to a target branch
- Post review comments on a specific PR
- Merge a pull request (when conditions are met)

### Workflow automation

- Trigger GitHub Actions workflows via the API
- Query commit history and blame information
- Create or update files directly in a branch

This makes the agent a first-class participant in your engineering workflow rather than a passive code-suggestion tool.

---

## 4. Getting an Agent to Use the GitHub MCP

The GitHub MCP is available automatically once `.mcp.json` is configured and your IDE or agent runtime is connected. You interact with it through natural language — the agent decides which MCP tool to call based on your request.

### Example prompts and what the agent does

---

**Reading the current state of a repository**

> "What are the open pull requests in this repo?"

The agent calls the GitHub MCP to list open PRs and returns a summary with titles, authors, and links.

---

**Creating an issue**

> "Create a GitHub issue titled 'Add retry logic to the payment service'. Label it `enhancement` and assign it to @alice."

The agent calls the MCP `create_issue` action with the supplied fields and returns the new issue URL.

---

**Reviewing a pull request**

> "Summarize PR #42 and tell me if there are any unresolved review comments."

The agent fetches the PR diff and all review threads via the MCP, then gives you a plain-English summary.

---

**Automating a full feature cycle**

> "I've just finished the feature on branch `feature/retry-logic`. Open a PR against `main`, write a description based on the commit history, and request review from @bob."

The agent:
1. Reads the commit log on `feature/retry-logic` via the MCP.
2. Generates a PR description.
3. Calls `create_pull_request` with the generated title and description.
4. Requests a review from `@bob`.

---

**Searching for context before coding**

> "Before I add the new endpoint, check if there are any open issues or TODOs related to rate limiting in this repo."

The agent searches issues and code simultaneously and returns a consolidated answer before you write a single line.

---

**Incorporating the GitHub MCP into a directive**

You can bake GitHub MCP usage into an agent directive or skill so the agent uses it automatically without being asked each time. For example, in a skill file:

```markdown
## Instructions

1. Before writing any code, search for related open issues using the GitHub MCP.
2. After completing a task, create a GitHub issue summarizing what was done and any follow-up items.
3. If the user asks you to "ship it", open a pull request against `main` with a generated description.
```

This turns the GitHub MCP from a one-off tool into a consistent part of your team's development workflow.

---

## 5. Working with Multiple Repos

### The MCP is not limited to one repo

The `owner` and `repo` fields in `.mcp.json` set a **default context hint** for the agent — they are not an API-level restriction. Every GitHub MCP tool (`get_file_contents`, `search_code`, `create_issue`, etc.) accepts `owner` and `repo` as parameters on each individual call. As long as your `GITHUB_TOKEN` has access to a repository, the agent can read from and write to it.

One GitHub MCP server instance handles all repos the token can reach. You do not need a separate MCP server entry per repository.

### Using this repo as a reference while working in another

This directives repo is a *knowledge source*, not a workspace. A common and powerful pattern is to:

- Set your **active project** as the default `owner`/`repo` in `.mcp.json`
- Reference this directives repo (or any other standards/runbook repo) **explicitly in skills or prompts**

Example skill directive:

```markdown
## Instructions

1. Before writing any code, check `my-org/agentic-sdlc-team-ai-directives` for
   relevant patterns, personas, or rules.
2. Open all pull requests and issues against `my-org/current-project`.
```

This gives the agent a clean separation: one repo for knowledge, one repo for work.

### Example cross-repo prompts

**Using a shared standards repo for reference**

> "Before writing the Helm chart, check `my-org/platform-standards` for any existing chart templates or naming conventions."

**Working across a monorepo and a separate config repo**

> "Read the service contract from `my-org/api-contracts` and implement the client in `my-org/backend`."

**Pulling runbooks during incident response**

> "Search `my-org/runbooks` for any procedures related to database failover, then create a tracking issue in `my-org/incidents`."

### Token permissions

When working across multiple repos:

- A **classic PAT** with `repo` scope works across all repos the account can access.
- A **fine-grained PAT** must explicitly list each repo it is allowed to access — scope it to only the repos your agent needs.
- For organization repos, ensure the token has been granted SSO authorization if your org enforces SAML SSO.
