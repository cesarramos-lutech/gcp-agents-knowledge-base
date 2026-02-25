# GCP Agents Knowledge Base

A shared team knowledge base for **AI agents on Google Cloud** -- ADK, Conversational Analytics API, multi-agent orchestration, and related topics.

---

## Structure

| Folder | Purpose |
|:--|:--|
| `comparisons/` | Side-by-side comparisons of tools, approaches, and architectures |
| `concepts/` | Core concepts explained -- what things are and how they work |
| `experiments/` | Notes and learnings from hands-on experiments and prototypes |
| `decisions/` | Decision frameworks -- when to use what, trade-offs, recommendations |
| `_templates/` | Blank templates for each entry type -- copy to the right folder to create a new entry |

---

## Index

### Comparisons

- [Conversational Analytics API vs. ADK SQL Tools](comparisons/conversational-analytics-vs-adk-sql.md) -- Managed NL-to-data pipeline vs. custom agent-built pipeline

### Concepts

*Coming soon*

### Experiments

*Coming soon*

### Decisions

*Coming soon*

---

## How to contribute

Push entries directly to `main`. No PR required — just keep quality high.

To add an entry:

1. Pick the right template from `_templates/`
2. Copy it to the correct folder with a descriptive slug (e.g. `experiments/nl2sql-self-correction-loop.md`)
3. Fill in all sections — replace HTML comment instructions with real content
4. Add it to the Index in this README
5. Push

If you're unsure where something fits:
- Comparing two things → `comparisons/`
- Explaining a mechanism → `concepts/`
- Documenting an empirical result → `experiments/`
- Justifying a choice with trade-offs → `decisions/`

Over time, this becomes a searchable, version-controlled second brain for the GCP agents domain.

---

## Topics to explore

- [ ] ADK fundamentals (agents, tools, sessions, state)
- [ ] Multi-agent orchestration patterns (sequential, parallel, loop)
- [ ] Semantic layers and why they matter for NL2SQL accuracy
- [ ] BigQuery ML (BQML) agents for forecasting and anomaly detection
- [ ] Agent Engine (Vertex AI) for managed deployment
- [ ] MCP (Model Context Protocol) and tool interoperability
- [ ] Evaluation and testing strategies for agents
- [ ] Cost optimization for LLM-heavy agent pipelines

---

*Built while learning. Maintained by the team.*
