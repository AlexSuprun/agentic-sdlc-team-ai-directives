#!/usr/bin/env python3
"""Smoke test for the GitHub MCP configuration in .mcp.json."""

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
MCP_FILE = ROOT_DIR / ".mcp.json"

REQUIRED_GITHUB_FIELDS = {
    "type": "github",
    "tokenEnv": "GITHUB_TOKEN",
    "baseUrl": "https://api.github.com",
}


def fail(message: str) -> None:
    print(f"❌ {message}", file=sys.stderr)
    sys.exit(1)


def check_mcp_config() -> None:
    if not MCP_FILE.exists():
        fail(f".mcp.json not found at: {MCP_FILE}")

    print("Checking .mcp.json GitHub tool configuration...")

    with MCP_FILE.open(encoding="utf-8") as f:
        data = json.load(f)

    github = (data.get("tools") or {}).get("github") or {}

    missing = [k for k in REQUIRED_GITHUB_FIELDS if k not in github]
    if missing:
        fail(f"Missing GitHub MCP fields: {', '.join(missing)}")

    mismatched = [k for k, v in REQUIRED_GITHUB_FIELDS.items() if github.get(k) != v]
    if mismatched:
        details = ", ".join(f"{k}={github.get(k)!r}" for k in mismatched)
        fail(f"Invalid GitHub MCP field values: {details}")

    if not github.get("owner") or not github.get("repo"):
        fail("GitHub MCP config requires non-empty 'owner' and 'repo'.")

    print("✅ GitHub MCP config shape looks valid.")


def check_github_token() -> None:
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        fail(
            "GITHUB_TOKEN is not set.\n"
            "   Export it and retry: export GITHUB_TOKEN=..."
        )

    print("Checking GitHub token against API...")

    req = urllib.request.Request(
        "https://api.github.com/user",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        },
    )

    try:
        with urllib.request.urlopen(req) as resp:
            payload = json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        try:
            payload = json.loads(exc.read().decode())
        except (json.JSONDecodeError, AttributeError):
            fail(f"GitHub API request failed with HTTP {exc.code}.")
            return  # unreachable, keeps type checker happy

    if payload.get("message") == "Bad credentials":
        fail("GITHUB_TOKEN is invalid (Bad credentials).")

    if "login" not in payload:
        message = payload.get("message", "unknown error")
        fail(f"GitHub API auth failed: {message}")

    print(f"✅ GitHub token is valid for user: {payload['login']}")
    print("✅ GitHub MCP smoke test passed.")


if __name__ == "__main__":
    check_mcp_config()
    check_github_token()
