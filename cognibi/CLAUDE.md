# CLAUDE.md — CogniBI Sprint

> Este fichero es el punto de arranque para cualquier sesión.
> Léelo antes de empezar. Actualízalo al terminar cada sesión.

---

## ▶ Cómo arrancar una sesión

```
"Lee el CLAUDE.md en gcp-agents-knowledge-base/cognibi/ y arranca la sesión S[N] de CogniBI"
```

Claude Code leerá este fichero y empezará con el contexto completo, sin necesidad de repetir nada.

---

## ⚠️ REGLAS IMPERATIVAS DE SESIÓN

### 1. Las sesiones requieren el input de César — NO son autónomas

Claude Code **NO debe ejecutar tareas de manera autónoma**. Cada paso importante dentro de una sesión requiere confirmación explícita del usuario antes de proceder.

**Protocolo obligatorio:**
- Al arrancar: presentar el plan de la sesión y preguntar si César quiere empezar, modificar el alcance, o priorizar algo diferente
- Ante cada tarea o entrega: usar `AskUserQuestion` para confirmar dirección antes de generar output
- Ante decisiones de diseño: presentar opciones y esperar elección, no decidir unilateralmente
- Ante dudas: preguntar, no asumir

**Ejemplo correcto:**
> "La sesión S2 tiene estas 5 tareas. ¿Empezamos por el análisis de data-science-agent o prefieres otro orden?"

**Ejemplo incorrecto:**
> [Claude ejecuta las 5 tareas sin preguntar y presenta el documento terminado]

### 2. Las sesiones del calendario son flexibles

El calendario es una guía, no un contrato. Las sesiones pueden:
- **Moverse** a otro día según la agenda de César
- **Dividirse** en sub-sesiones si una tarea es más grande de lo esperado
- **Fusionarse** si el trabajo va más rápido
- **Reordenarse** si cambian las prioridades
- **Añadir sesiones nuevas** para tareas no previstas inicialmente

Cuando esto ocurra: actualizar este CLAUDE.md y, si aplica, los eventos del calendario.

### 3. IMPERATIVO: Guardar la foto al terminar cada sesión

**Al finalizar cualquier sesión** (o si se interrumpe), Claude Code DEBE actualizar este fichero con:
- El estado actualizado de la tabla de sesiones (✅ / ⏳ / 🚧 en curso)
- Una nota en "Notas por sesión" con: qué se hizo, qué quedó pendiente, decisiones tomadas
- Las "Decisiones abiertas" actualizadas
- La sesión SIGUIENTE marcada como **SIGUIENTE**

Esto garantiza que en cualquier sesión futura, partimos con contexto completo aunque no haya memoria de conversaciones anteriores.

---

## Estado actual del sprint

| Sesión | Nombre | Estado | Fecha |
|--------|--------|--------|-------|
| S1 | Product Brief | ✅ COMPLETADO | 18 Feb 2026 |
| S2 | Asset Analysis | ⏳ **SIGUIENTE** | 24 Feb 2026 |
| S3 | Agent Deliverable Spec | ⏳ pendiente | 25 Feb 2026 |
| S4 | Metodología | ⏳ pendiente | 26 Feb 2026 |
| S5 | Arquitectura Template | ⏳ pendiente | 27 Feb 2026 |
| S6 | Build: Template v0.1 | ⏳ pendiente | 2 Mar 2026 |
| S7 | Build: Client Onboarding | ⏳ pendiente | 3 Mar 2026 |
| S8 | Build: Claude Code Automation | ⏳ pendiente | 4 Mar 2026 |
| S9 | Demo + Pitch | ⏳ pendiente | 5 Mar 2026 |
| S10 | Review + Package | ⏳ pendiente | 6 Mar 2026 |

**Última sesión:** S1 — Product Brief (18 Feb 2026)
**Próxima sesión:** S2 — Asset Analysis

---

## Contexto del producto

**CogniBI** = acelerador de consultoría de BI para entregar **agentes conversacionales sobre datos** en empresas medianas.

### El problema
- **Cliente final:** datos existen pero no son accesibles — cualquier pregunta nueva requiere esperar al analista
- **Consultor:** 70% del proyecto es trabajo repetitivo que CogniBI + Claude Code automatiza

### El deliverable al cliente
Agente conversacional deployado en GCP con:
- NL2SQL (pregunta en español → SQL → resultado)
- Visualizaciones automáticas (Vega-Lite)
- UI web (Streamlit o React)
- API (FastAPI + WebSocket)
- Contexto de negocio embebido (KPIs, glosario, relaciones de tablas)
- Deployment: Cloud Run + Firestore (sesiones) + GCS (artefactos)

### ICP (cliente ideal)
Empresa mediana B2B, 50–500 empleados, sector SaaS/retail/fintech/logística, datos ya en BigQuery o Salesforce, sin equipo de IA propio, presupuesto €15k–€50k.

### Modelo de negocio
- Fee implementación: €15k–€40k por proyecto
- Retainer mensual: €1k–€3k/mes

### Decisiones abiertas (confirmar con César)
- [ ] ¿El nombre "CogniBI" es definitivo?
- [ ] ¿Solo GCP/Gemini o hay que soportar otros LLMs?
- [ ] ¿UI Streamlit (MVP rápido) o React (look enterprise)?

---

## Base técnica existente

### `data-science-agent` — base principal del template
**Path:** `gcp-data-agents/data-science-agent/`
- ADK v1.14+, Gemini 2.5 Pro
- BigQuery (NL2SQL con CHASE-SQL) + AlloyDB (MCP Toolbox) + Python analytics + BQML
- Root agent → 4 sub-agentes (BQ, AlloyDB, Analytics, BQML)
- Config dataset: `flights_dataset_config.json` → define datasets + relaciones FK
- Deployment: ADK local / Vertex AI Agent Engine / Cloud Run
- **Generalizar:** eliminar "flights/demo", parametrizar datasets por cliente

### `crm-data-agent-cesar` — patrón BI para usuario de negocio
**Path:** `gcp-data-agents/crm-data-agent-cesar/`
- ADK v1.3.x, Gemini 2.5 Pro (root/BA/DE/BI) + Gemini 2.0 Flash (evaluador visual)
- BigQuery + Salesforce Data Cloud + Vega-Lite + Streamlit + FastAPI
- Root agent → 3 tools: CRM Business Analyst (LlmAgent), Data Engineer (FunctionTool), BI Engineer (FunctionTool)
- Loop de calidad de charts con modelo vision (hasta 5 iteraciones)
- Self-correction SQL hasta 32 intentos con re-inyección de schema
- Metadata: `sfdc_metadata.json` (~470KB) en contexto
- **Generalizar:** reemplazar sfdc_metadata por formato genérico, parametrizar prompts por dominio

### Patrón arquitectónico común (el "CogniBI pattern")
```
Root Agent (orquestador)
  ├── Business Analyst (LlmAgent) → interpreta la pregunta de negocio
  ├── Data Engineer (FunctionTool) → NL2SQL + self-correction loop
  └── BI Engineer (FunctionTool) → ejecuta SQL + genera viz + evalúa calidad
```

### Otros repos de referencia
- `ca-demos-and-tools-CESAR/` — ejemplos ADK públicos (streaming, Prism ORM, React frontend, CA API)
- `ca-api-quickstarts-CESAR/` — quickstarts ADK con Streamlit

---

## Herramientas disponibles en Claude Code para este proyecto

### Skill: `google-adk`

Claude Code tiene una **skill especializada en Google ADK** que actúa como experto en el framework.

**Cómo invocarla:**
```
/google-adk
```

**Qué puede hacer:**
- Responder preguntas sobre arquitectura de agentes ADK (LlmAgent, FunctionTool, AgentTool, etc.)
- Revisar código ADK y detectar antipatrones
- Comparar implementaciones contra las best practices oficiales
- Guiar decisiones de diseño: cuándo usar sub-agentes vs tools, cómo gestionar estado, cómo hacer deploy en Vertex AI Agent Engine vs Cloud Run
- Contrastar lo que tenemos construido vs lo que el framework recomienda

**Cuándo usarla:** siempre que haya una decisión de arquitectura ADK, especialmente en S2 (análisis), S5 (diseño del template) y S6-S8 (construcción).

### Agentes paralelos (Task tool)

Claude Code puede lanzar **múltiples agentes en paralelo** usando el Task tool interno. Esto permite analizar varios repos simultáneamente y luego sintetizar los resultados — lo que se llama enfoque **agent-as-a-judge**.

**Cuándo usarlo:** S2 — Asset Analysis (ver metodología específica más abajo).

---

## Estructura objetivo del template (borrador S5)

```
gcp-data-agents/cognibi-template/    ← se crea en S6
├── cognibi/
│   ├── agent.py                     # Root orchestrator genérico
│   ├── prompts.py                   # Instrucciones base parametrizables
│   └── sub_agents/
│       ├── business_analyst/
│       ├── data_engineer/
│       └── bi_engineer/
├── setup/
│   ├── onboard_client.py            # S7: script de onboarding
│   └── client_config.yaml          # S7: config por cliente
├── schemas/
│   └── schema_template.json        # Formato genérico de metadata BQ
├── docs/
│   └── claude-playbook.md          # S8: playbook de prompts
├── demo/                            # S9: demo script
├── CLAUDE.md                        # S8: instrucciones para Claude Code
└── README.md
```

---

## Metodología especial para S2: Agent-as-a-Judge

S2 no es una sesión de análisis lineal. Usa un enfoque multi-agente en paralelo:

```
┌─────────────────────────────────────────────────────────────┐
│              ORQUESTADOR (Claude Code principal)             │
│         Experto en arquitecturas agénticas                   │
└──────┬──────────┬──────────┬──────────┬──────────┬──────────┘
       │          │          │          │          │
       ▼          ▼          ▼          ▼          ▼
  [Agente 1]  [Agente 2]  [Agente 3]  [Agente 4]  [Agente 5]
  data-sci-   crm-data-   ca-demos-   ca-api-     /google-adk
  agent       agent       and-tools   quickstarts  skill
  (Explore)   (Explore)   (Explore)   (Explore)   (ADK canon)
       │          │          │          │          │
       └──────────┴──────────┴──────────┴──────────┘
                            │
                            ▼
                   SÍNTESIS / JUICIO
              ¿Qué es reutilizable? ¿Qué
              va contra ADK best practices?
              ¿Qué falta para CogniBI?
```

**Paso a paso para ejecutar S2:**

1. **Preguntar a César** qué quiere priorizar / si hay algo que ya conoce bien y no hace falta analizar en profundidad
2. **Lanzar 5 agentes en paralelo** (un Task/Explore por repo + invocar /google-adk para el contexto canónico de ADK)
3. **Recoger los 5 outputs** y presentar un resumen a César antes de sintetizar
4. **Preguntar a César** si el análisis refleja lo que él ve / si hay matices a corregir
5. **Generar `02-asset-analysis.md`** con la síntesis final + tabla de reutilización + gaps

**El "juez"** es el orquestador (Claude Code principal) que contrasta los 4 repos entre sí y contra lo que dice ADK. No es un agente separado — es Claude Code usando los resultados de los sub-agentes como evidencia.

**Nota sobre el "agente experto en arquitecturas agénticas":** por ahora este rol lo cubre Claude Code principal + la skill `/google-adk`. Si en el futuro se quiere un agente especializado persistente, se puede crear un custom agent con instrucciones específicas en `cognibi-template/CLAUDE.md` (S8).

---

## Notas por sesión

### Sesión de setup del sprint ✅ (18 Feb 2026)
Todo lo siguiente ocurrió en la misma sesión antes/durante S1:
- Creada estructura `gcp-agents-knowledge-base/cognibi/` con `README.md` y este `CLAUDE.md`
- Creados 10 eventos en Google Calendar (cesar.ramos@lutech-sweeft.es), 15:00–17:00, lunes a viernes, semanas del 23 Feb y 2 Mar 2026
- Todos los eventos actualizados con contexto de arranque (prompt exacto + tareas + output esperado)
- Definidas las 3 reglas imperativas de sesión (input de César, calendario flexible, guardar foto)
- Añadida documentación de la skill `/google-adk` y la metodología agent-as-a-judge para S2
- Evento S2 en Calendar actualizado con el enfoque de 5 agentes en paralelo

### S1 — Product Brief ✅ (18 Feb 2026)
- ⚠️ Ejecutada de manera demasiado autónoma (sin pedir input a César en cada paso) — corregido en las reglas
- Explorados `data-science-agent` y `crm-data-agent-cesar` en profundidad via agente Explore
- Definido: problema, deliverable concreto, ICP, modelo de negocio, posicionamiento competitivo
- Output: `gcp-agents-knowledge-base/cognibi/01-product-brief.md`
- Decisiones abiertas pendientes de confirmar con César:
  - ¿El nombre "CogniBI" es definitivo?
  - ¿Solo GCP/Gemini o hay que soportar otros LLMs?
  - ¿UI Streamlit (MVP) o React (enterprise)?

---

## Reglas de trabajo para Claude Code

- Documentación → esta carpeta (`gcp-agents-knowledge-base/cognibi/`)
- Código del template → `gcp-data-agents/cognibi-template/` (se crea en S6)
- **Al terminar cada sesión:** actualizar este `CLAUDE.md` (tabla de estado + notas) y el `README.md` — SIEMPRE, sin excepción
- **Antes de cada tarea:** usar `AskUserQuestion` para confirmar con César — SIEMPRE
- Stack fijo: Google ADK + Gemini + BigQuery + GCP. No proponer alternativas salvo que César lo indique.
- Idioma de documentación: español. Código: inglés.
