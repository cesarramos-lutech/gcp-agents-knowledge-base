# CogniBI Framework — Playbook

> Automatizar casi al 100% proyectos de consultoría de BI donde el deliverable final al cliente es un **agente de datos conversacional**.

**Tres capas del framework:**
- **CogniBI** — el acelerador / template reutilizable (lo que se entrega al cliente)
- **CogniBI Playbook** — esta carpeta: metodología, roadmap y documentación de trabajo
- **CogniBI Ops Layer** — gobernanza, monitorización y demostración de ROI post-entrega (S12)

## Índice de documentos

| # | Documento | Sesión | Estado |
|---|-----------|--------|--------|
| 01 | [Product Brief](./01-product-brief.md) | S1 — 18 Feb | ✅ Completado |
| 02 | [Asset Analysis](./02-asset-analysis.md) | S2 — 24 Feb | ⏳ Pendiente |
| 03 | [Agent Deliverable Spec](./03-agent-deliverable-spec.md) | S3 — 25 Feb | ⏳ Pendiente |
| 04 | [Methodology](./04-methodology.md) | S4 — 26 Feb | ⏳ Pendiente |
| 05 | [Template Architecture](./05-template-architecture.md) | S5 — 27 Feb | ⏳ Pendiente |
| 06 | [Build Log: Template v0.1](./06-build-template.md) | S6 — 2 Mar | ⏳ Pendiente |
| 07 | [Build Log: Client Onboarding](./07-client-onboarding.md) | S7 — 3 Mar | ⏳ Pendiente |
| 08 | [Build Log: Claude Code Automation](./08-claude-automation.md) | S8 — 4 Mar | ⏳ Pendiente |
| 09 | [Pitch Narrative](./09-pitch-narrative.md) | S9 — 5 Mar | ⏳ Pendiente |
| 10 | [Review & Next Steps](./10-review-next-steps.md) | S10 — 6 Mar | ⏳ Pendiente |
| 11 | [Smoke Test E2E: GA4 + Google Ads](./11-smoke-test.md) | S11 — 7 Mar | ⏳ Pendiente |
| 12 | [Governance & Ops Layer](./12-governance-ops.md) | S12 — 10 Mar | ⏳ Pendiente |

## Contexto del plan de trabajo

**Horizonte:** flexible — las sesiones pueden moverse, fusionarse o añadirse según prioridades
**Sesiones previstas:** 12 × ~2h = ~24h
**Horario orientativo:** Lunes a Viernes, 15:00–17:00 (Europe/Madrid)
**Semana 1 inicio:** 23 Feb 2026
**Semana 2 inicio:** 2 Mar 2026
**S11 (smoke test):** 7 Mar 2026 — depende de S6, S7 y S8 completadas
**S12 (governance/ops):** 10 Mar 2026 — depende de S6, S7, S8 y S11 completadas

## Activos existentes (base de partida)

- `gcp-data-agents/data-science-agent/` — base del template (ADK, BQ, BQML, AlloyDB)
- `gcp-data-agents/crm-data-agent-cesar/` — patrones multi-tool (Salesforce/BQ)
- `gcp-data-agents/ca-demos-and-tools-CESAR/` — ejemplos públicos ADK
- `gcp-data-agents/ca-api-quickstarts-CESAR/` — quickstarts con Streamlit

## Output final del plan de trabajo

- `gcp-data-agents/cognibi-template/` — acelerador reutilizable para nuevos proyectos
- `gcp-data-agents/cognibi-template/smoke-test/` — ejemplo real con datos sintéticos GA4 + Google Ads (S11)
- Esta carpeta `cognibi/` — metodología, playbook y documentación completa
- `cognibi/12-governance-ops.md` — especificación de la capa de operaciones y monitoring (S12)
