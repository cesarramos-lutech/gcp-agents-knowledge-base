# CLAUDE.md — GCP Agents Knowledge Base

> This file defines how Claude Code works in this repo.
> Read it before adding, modifying, or indexing any knowledge entry.

---

## Purpose

Shared team knowledge base on **GCP data agents** — ADK, Conversational Analytics API, BigQuery, multi-agent orchestration, and related topics.

---

## Capture criterion

**Is an entry worth creating?**

> Yes, if it would save any team member 30+ minutes of rediscovering something.

Signals that something deserves an entry:
- An ADK pattern was implemented for the first time and it wasn't obvious how to do it
- A choice was made between two tools/approaches with explicit reasoning
- An experiment produced an unexpected result (success or failure)
- An architecture conclusion was reached that changes a project's design

---

## Folder structure

| Folder | What goes here | When to use it |
|--------|----------------|----------------|
| `comparisons/` | Side-by-side between two tools, APIs, or approaches | When comparing alternatives and reaching a conclusion |
| `concepts/` | Explanations of how something works | When understanding a new mechanism (e.g. how ADK state works) |
| `experiments/` | Results of what was tried — successes AND failures | When an experiment has a clear outcome |
| `decisions/` | Architecture decisions with reasoning | When choosing between options with consequences |
| `_templates/` | Blank templates for each entry type | Reference only — don't create entries directly here |

**Not sure where something goes?**
- If it compares two things → `comparisons/`
- If it explains a mechanism → `concepts/`
- If it documents an empirical result → `experiments/`
- If it justifies a choice → `decisions/`

---

## How to add an entry

### 1. Pick the right template

```
_templates/adk-pattern.md           → ADK implementation patterns
_templates/architecture-decision.md → design decisions with alternatives
_templates/tool-comparison.md       → comparisons between tools
_templates/experiment.md            → experiment results
```

### 2. Naming convention

```
{folder}/{descriptive-slug}.md
```

Correct examples:
```
concepts/adk-session-state-vs-context.md
experiments/nl2sql-self-correction-loop.md
decisions/streamlit-vs-react-for-data-app-ui.md
comparisons/agent-engine-vs-cloud-run-deployment.md
```

Slug rules:
- All lowercase, words separated by hyphens
- Descriptive: the topic should be clear from the filename alone
- No dates in the name (date goes inside the document)

### 3. Fill in the template

Copy the template to the new location and fill in all sections. HTML comment sections (`<!-- -->`) are instructions — replace them with real content.

### 4. Update the index

Always update `README.md` after creating an entry — add it to the corresponding section of the index. Don't leave entries unindexed.

---

## Language

- **Documentation:** English
- **Code snippets:** English (variable names, function names, code comments)

---

## What this repo is NOT

- Not product documentation — that belongs in project-specific repos
- Not code — that belongs in the corresponding code repos
- Not session notes — those belong in project-specific playbooks
- Not a blog — every entry must be dense with practical value, not narrative
