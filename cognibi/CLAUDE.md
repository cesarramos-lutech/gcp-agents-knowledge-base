# CLAUDE.md — CogniBI Playbook

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

## Estado actual del plan de trabajo

| Sesión | Nombre | Estado | Fecha |
|--------|--------|--------|-------|
| S1 | Product Brief | ✅ COMPLETADO | 24 Feb 2026 |
| S1.5 | Competitive Landscape | ⏳ **SIGUIENTE** | 26 Feb 2026 |
| S2 | Asset Analysis | ⏳ pendiente | 2 Mar 2026 |
| S3 | Agent Deliverable Spec | ⏳ pendiente | 4 Mar 2026 |
| S4 | Metodología | ⏳ pendiente | 6 Mar 2026 |
| S5 | Arquitectura Template | ⏳ pendiente | 9 Mar 2026 |
| S6 | Build: Template v0.1 | ⏳ pendiente | 11 Mar 2026 |
| S7 | Build: Client Onboarding | ⏳ pendiente | 13 Mar 2026 |
| S8 | Build: Claude Code Automation | ⏳ pendiente | 16 Mar 2026 |
| S9 | Demo + Pitch | ⏳ pendiente | 18 Mar 2026 |
| S10 | Review + Package | ⏳ pendiente | 20 Mar 2026 |
| S11 | Smoke Test E2E (GA4 + Ads) | ⏳ pendiente | 23 Mar 2026 |
| S12 | Governance & Ops Layer | ⏳ pendiente | 25 Mar 2026 |
| S13 | Market Validation & Battle Cards | ⏳ pendiente | 27 Mar 2026 |

**Última sesión:** S1 — Product Brief (24 Feb 2026)
**Próxima sesión:** S1.5 — Competitive Landscape (26 Feb 2026)

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
- Retainer mensual: €1k–€3k/mes, que incluye:
  - **Operaciones:** monitorización interna del agente (system health, SQL correctness, costes de inferencia)
  - **Business Value Report:** informe mensual al cliente con métricas de ROI (time-to-insight, adoption, % queries exitosas)
  - **Mantenimiento evolutivo:** actualizaciones de schema, glosario, upgrades de modelo

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

## Metodología especial para S1.5: Competitive Landscape

S1.5 valida el posicionamiento estratégico de CogniBI **antes de construir nada**. Es un checkpoint de estrategia para asegurarse de que hay un hueco real en el mercado antes de invertir en S2–S12.

### Preguntas clave a responder
- ¿Para qué segmento CogniBI gana claramente? ¿Hay un hueco real no cubierto?
- ¿Cuál es el moat real frente a cada competidor?
- ¿Hay algún red flag que deba cambiar el diseño del producto antes de S3?

### Competidores a analizar (6)
1. Databricks Genie
2. Looker Conversational Analytics (Google)
3. Power BI Copilot / Tableau Pulse
4. ThoughtSpot / Sigma
5. MicroStrategy Mosaic + Strategy AI Agents
6. DIY: LangChain/LlamaIndex + BigQuery (la alternativa que los técnicos intentan en casa)

### Dimensiones de comparación (7)
- **Precio / modelo de negocio**
- **ICP al que va** (enterprise vs midmarket vs startup)
- **Stack técnico requerido** (¿lock-in a qué plataforma?)
- **Capacidades NL2SQL / viz / contexto de negocio**
- **Deployment** (SaaS vs self-hosted vs managed)
- **Madurez / adoption**
- **Lo que NO hace bien** (gaps que CogniBI puede explotar)

### Paso a paso para ejecutar S1.5

1. **Preguntar a César** qué competidores conoce bien y si hay alguno a priorizar o descartar
2. **Lanzar research en paralelo** — WebSearch por competidor (6 búsquedas paralelas), focalizando en pricing, ICP, stack y gaps documentados
3. **Presentar hallazgos a César** antes de sintetizar — ¿refleja lo que él ve en el mercado?
4. **Generar `01b-competitive-landscape.md`** con tabla comparativa + mapa de posicionamiento + positioning statement refinado + red flags

### Output: `01b-competitive-landscape.md`
- Tabla comparativa 7 dimensiones × 6 competidores + CogniBI
- Mapa de posicionamiento 2×2 (precio vs complejidad técnica)
- Positioning statement refinado de CogniBI
- Red flags o ajustes a incorporar antes de S3

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

## Metodología especial para S11: Smoke Test E2E con datos sintéticos

S11 valida el sistema CogniBI completo simulando un engagement real con un cliente de marketing digital. El objetivo no es solo que el agente funcione — es validar que el **workflow completo consultor + Claude Code** (vibe coding) permite construir el modelo, los pipelines y el agente de manera acelerada.

### Dominio del smoke test
- **Fuente de datos:** GA4 export + Google Ads export (esquema estándar BigQuery)
- **Nivel de datos:** mínimo viable — esquema realista + ~100–500 filas sintéticas por tabla clave
- **Pregunta de negocio de ejemplo:** "¿Cuál es el coste por sesión por campaña este mes?" / "¿Qué canal convierte mejor?"

### Las 3 fases del smoke test

**Fase 1 — Modelo de datos + datos sintéticos**
Usando Claude Code en modo vibe coding:
- Definir el esquema BigQuery de GA4 + Ads (tablas estándar del export)
- Generar script Python de datos sintéticos (volumetría mínima viable)
- Cargar en BigQuery (dataset de test)
- Output: `smoke-test/schema/` + `smoke-test/seed_data.py`

**Fase 2 — Data pipelines**
Usando Claude Code en modo vibe coding:
- Definir las transformaciones mínimas necesarias (views o tablas agregadas) para que el agente pueda responder las preguntas de negocio sin SQL complejo
- Implementar como SQL scripts o dbt models ligeros
- Output: `smoke-test/pipelines/`

**Fase 3 — Agente CogniBI sobre ese modelo**
Usando el template CogniBI construido en S6–S8:
- Onboarding del cliente "demo_ga4_ads" (script S7)
- Configurar `client_config.yaml` con el schema sintético
- Ejecutar el agente y hacer 5–10 preguntas de negocio reales
- Documentar: ¿funcionó? ¿qué falló? ¿qué hay que corregir?
- Output: `smoke-test/results.md` con evidencia (queries generadas, charts, errores)

### Dependencias de S11

**S11 no puede ejecutarse sin que estén completadas:**
- ✅ S6 — Build: Template v0.1 (el template genérico existe y funciona en local)
- ✅ S7 — Build: Client Onboarding (el script `onboard_client.py` y `client_config.yaml` están operativos)
- ✅ S8 — Build: Claude Code Automation (el playbook de prompts y el CLAUDE.md del template están listos)

**Si alguna de estas sesiones se retrasa**, S11 se mueve automáticamente. No tiene sentido hacer el smoke test sobre un template incompleto.

### Lo que S11 valida
- El **template es genérico** de verdad (no hardcodeado a flights o SFDC)
- El **workflow de onboarding** funciona con un cliente nuevo
- El **vibe coding con Claude Code** es el método de trabajo para la fase de delivery
- Los **gaps reales** del sistema antes de venderlo a un cliente

---

## Metodología especial para S12: Governance & Ops Layer

S12 diseña la capa de operaciones post-entrega del CogniBI Framework. No es solo
documentación — es el fundamento que justifica el retainer y hace el producto sostenible.

### Dos capas con audiencias distintas

**Capa 1 — Interna (el consultor / César)**

Herramientas y procesos que usa el consultor para operar el agente del cliente:
- **System health:** Cloud Run uptime, latencia p50/p95/p99
- **SQL correctness monitoring:** % queries con retry, errores por tipo, fallback rate
- **Cost tracker:** tokens Gemini + BQ slots por cliente/mes, alertas de budget
- **Incident log:** qué falló, cuándo, cómo se resolvió
- **Runbook:** guía paso a paso para detectar y resolver los fallos más comunes

**Capa 2 — Visible al cliente (business value)**

Métricas que el cliente ve cada mes para demostrar ROI:
- **Time-to-insight:** antes (esperar al analista) vs después (respuesta del agente en segundos)
- **Adoption dashboard:** usuarios activos, queries/día, tendencia
- **Query success rate:** % preguntas respondidas satisfactoriamente
- **ROI estimado:** horas de analista ahorradas × coste hora del cliente
- **Report mensual automático** → el entregable que justifica el retainer

### Dependencias de S12

**S12 no puede ejecutarse sin:**
- ✅ S6, S7, S8 completadas (el template y su arquitectura existen)
- ✅ S11 completada (el smoke test ha revelado qué hay que monitorizar en la práctica)

### Output de S12
- `12-governance-ops.md` — especificación completa de ambas capas
- Integración en `cognibi-template/`: estructura de logging y métricas a añadir al template

---

## Metodología especial para S13: Market Validation & Battle Cards

S13 evalúa el producto CogniBI **terminado** contra la competencia con evidencia real del smoke test (S11) y el sistema de operaciones (S12). Es la validación final antes de salir a vender.

### Objetivo
Confirmar que CogniBI tiene posicionamiento defendible con un producto real funcionando, y que el equipo comercial (César) tiene los argumentarios necesarios para cerrar deals.

### Prerequisito
**S13 no puede ejecutarse sin que estén completadas:**
- ✅ S6–S12 completadas (el producto existe, funciona y tiene capa de ops)
- ✅ S11 completada (el smoke test ha revelado los puntos fuertes y débiles reales)
- ✅ S1.5 completada (tenemos la línea base del análisis competitivo inicial)

### Las 3 fases de S13

**Fase 1 — Battle cards por competidor**
Para cada uno de los 6 competidores analizados en S1.5:
- ¿Cuándo gana CogniBI claramente?
- ¿Cuándo pierde (y qué decir en ese caso)?
- Cómo responder las 3 objeciones más comunes de ese competidor
- Evidencia del smoke test que respalda los argumentos

**Fase 2 — Análisis de supervivencia (Future-proofing)**
- ¿CogniBI tiene sentido en 2027 cuando los LLMs sean aún más capaces?
- ¿Cuál es el moat a largo plazo? (stack especializado GCP, expertise de implementación, base de clientes, datos propietarios del cliente)
- Escenarios: ¿qué pasa si Google lanza una versión gratuita de Looker Conversational para PyMEs?

**Fase 3 — Go-to-market readiness**
- ¿Está el producto listo para ser vendido? ¿Qué falta?
- Checklist de materiales de venta: deck, one-pager, demo en vivo, pricing sheet, caso de uso de referencia
- Primeros 3 clientes objetivo: perfil, canal de entrada, propuesta de valor específica

### Output: `13-market-validation.md`
- Battle cards (1 por competidor, formato estandarizado)
- Sección "Future-proofing": escenarios y moat analysis
- Checklist go-to-market con estado de cada ítem
- Resumen ejecutivo: ¿CogniBI está listo para vender? ¿Qué hacer primero?

---

## Reglas de trabajo para Claude Code

- Documentación → esta carpeta (`gcp-agents-knowledge-base/cognibi/`)
- Código del template → `gcp-data-agents/cognibi-template/` (se crea en S6)
- **Al terminar cada sesión:** actualizar este `CLAUDE.md` (tabla de estado + notas) y el `README.md` — SIEMPRE, sin excepción
- **Antes de cada tarea:** usar `AskUserQuestion` para confirmar con César — SIEMPRE
- **Al modificar el plan de trabajo (añadir, mover, fusionar o eliminar sesiones):** (1) consultar primero el Google Calendar de César (cesar.ramos@lutech-sweeft.es) para ver las fechas reales de todos los eventos CogniBI existentes, (2) calcular el nuevo orden respetando siempre un día de gap entre sesiones y saltando fines de semana a la siguiente semana, (3) actualizar o crear los eventos de Calendar consecuentemente. SIEMPRE, sin excepción. No asumir fechas sin consultar el calendario real.
- Stack fijo: Google ADK + Gemini + BigQuery + GCP. No proponer alternativas salvo que César lo indique.
- Idioma de documentación: español. Código: inglés.
