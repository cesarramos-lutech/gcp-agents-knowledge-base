# Configuring Claude Code ADK Expertise

> **Date:** 2026-03-18

> **Status:** Work in progress — additional configuration recommendations will be added over time.

---

## What this achieves

By default, Claude Code has general knowledge of Google ADK but cannot look up current documentation. This setup gives Claude Code two things:

- **Live ADK documentation access** — via an MCP server that indexes the official ADK docs in real time
- **Behavioral instructions** — via a `CLAUDE.md` that tells Claude to always consult those docs before implementing ADK patterns

The result: Claude Code defaults to correct, up-to-date ADK patterns instead of relying on potentially outdated training knowledge.

---

## Prerequisites

- Claude Code installed and working (`claude --version`)
- Python and `pip` available in your terminal

---

## Scope: user vs. project

This setup can be applied at two levels:

| Scope | MCP flag | `CLAUDE.md` location | When to use |
|:--|:--|:--|:--|
| **User (global)** | `--scope user` | `~/.claude/CLAUDE.md` | You work on ADK projects regularly and want the expertise available everywhere |
| **Project** | `--scope project` | `.claude/CLAUDE.md` in the project root | You want ADK expertise scoped to one specific project only |

The steps below are identical for both — just substitute the flag and `CLAUDE.md` location accordingly.

---

## Setup

### Step 1 — Install `uv`

```bash
pip install uv
```

**Why:** The ADK docs MCP server (`mcpdoc`) is run via `uvx`, a tool that ships with `uv`. `uvx` executes Python packages in temporary isolated environments — no permanent installation required, and your global Python environment stays clean.

---

### Step 2 — Register the ADK docs MCP server

**User (global):**
```bash
claude mcp add adk-docs --scope user --transport stdio -- uvx --from mcpdoc mcpdoc --urls AgentDevelopmentKit:https://google.github.io/adk-docs/llms.txt --transport stdio
```

**Project:**
```bash
claude mcp add adk-docs --scope project --transport stdio -- uvx --from mcpdoc mcpdoc --urls AgentDevelopmentKit:https://google.github.io/adk-docs/llms.txt --transport stdio
```

**Why each part matters:**

| Part | What it does |
|:--|:--|
| `adk-docs` | The name Claude Code uses to identify this MCP server |
| `--scope user` / `--scope project` | Controls availability — globally across all sessions, or only within the current project |
| `--transport stdio` | Tells Claude Code to communicate with the MCP server over standard I/O |
| `--` | Separator — everything after this is the command Claude Code will run to start the MCP server |
| `uvx --from mcpdoc mcpdoc` | Runs `mcpdoc` via `uvx` in an isolated environment |
| `--urls AgentDevelopmentKit:https://google.github.io/adk-docs/llms.txt` | Points `mcpdoc` at the official ADK docs. The `llms.txt` format is a standardized, LLM-optimized documentation index designed for programmatic consumption |
| `--transport stdio` | Tells `mcpdoc` itself to use stdio transport, as required by the MCP protocol |

---

### Step 3 — Add behavioral instructions to `CLAUDE.md`

Open (or create) the `CLAUDE.md` for your chosen scope and add:

```markdown
# Agent Projects
Always prioritize Google ADK for agent projects. Before implementing any pattern, consult the adk-docs MCP server to validate against the official docs.
```

**Why:** Claude Code reads `CLAUDE.md` at the start of every session. These instructions ensure Claude:

1. Defaults to ADK over other frameworks when building agents
2. Actively queries the `adk-docs` MCP server before implementing any pattern — preventing hallucinated or outdated API usage

---

### Step 4 — Verify

Start a **new** Claude Code session and ask:

> "Do you have access to adk-docs via MCP?"

**Why a new session:** MCP servers are loaded at startup. Changes made to MCP configuration do not apply to sessions that are already running.

**Expected response:** Claude confirms access to the `adk-docs` MCP server and can describe the available documentation sources.

---

## What gets configured

| Component | User scope | Project scope |
|:--|:--|:--|
| MCP server (`adk-docs`) | `~/.claude/` settings | `.claude/` settings in project root |
| Behavioral instruction | `~/.claude/CLAUDE.md` | `.claude/CLAUDE.md` in project root |

---

## Troubleshooting

- **Claude says it has no MCP access:** Confirm you used the correct scope flag and started a fresh session. If using `--scope project`, make sure you are running Claude Code from within the project directory — project-scoped MCP servers are only available when Claude Code is opened in that project.
- **`uvx` not found after installing `uv`:** Restart your terminal — the `uvx` binary may not be on `PATH` until the shell reloads.
- **Docs not loading:** Verify connectivity to `https://google.github.io/adk-docs/llms.txt` — `mcpdoc` fetches documentation at runtime.
