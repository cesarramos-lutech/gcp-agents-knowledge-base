# CLAUDE.md — GCP Agents Knowledge Base

> Este fichero define cómo Claude Code trabaja en este repo.
> Léelo antes de añadir, modificar o indexar cualquier entrada de conocimiento.

---

## Propósito del repo

Base de conocimiento personal sobre **agentes de datos en GCP** — ADK, Conversational Analytics API, BigQuery, multi-agent orchestration, y temas relacionados. El conocimiento aquí capturado proviene principalmente del proyecto CogniBI y del estudio del stack GCP.

---

## Criterio de captura

**¿Vale la pena crear una entrada?**

> Sí, si le ahorraría a César-futuro 30+ minutos de redescubrir algo.

Señales de que algo merece capturarse:
- Se implementó un patrón ADK por primera vez y no era obvio cómo hacerlo
- Se eligió entre dos herramientas/enfoques con razonamiento explícito
- Un experimento produjo un resultado inesperado (éxito o fallo)
- Se llegó a una conclusión de arquitectura que cambia algo del diseño de CogniBI

---

## Estructura de carpetas

| Carpeta | Qué va aquí | Cuándo usarla |
|---------|-------------|---------------|
| `comparisons/` | Side-by-side entre dos herramientas, APIs o enfoques | Cuando se comparan alternativas y se llega a una conclusión |
| `concepts/` | Explicaciones de cómo funciona algo | Cuando se entiende un mecanismo nuevo (ej: cómo funciona el state en ADK) |
| `experiments/` | Resultados de lo que se probó — éxitos Y fallos | Cuando se hace un experimento con resultado claro |
| `decisions/` | Decisiones de arquitectura con razonamiento | Cuando se elige entre opciones con consecuencias |
| `_templates/` | Plantillas vacías para cada tipo de entrada | Solo como referencia — no crear entradas directamente aquí |

**Duda de dónde poner algo:**
- Si compara dos cosas → `comparisons/`
- Si explica un mecanismo → `concepts/`
- Si documenta un resultado empírico → `experiments/`
- Si justifica una elección → `decisions/`

---

## Cómo añadir una entrada

### 1. Elegir el template correcto

```
_templates/adk-pattern.md          → patrones de implementación ADK
_templates/architecture-decision.md → decisiones de diseño con alternativas
_templates/tool-comparison.md       → comparaciones entre herramientas
_templates/experiment.md            → resultados de experimentos
```

### 2. Naming convention

```
{carpeta}/{slug-descriptivo}.md
```

Ejemplos correctos:
```
concepts/adk-session-state-vs-context.md
experiments/nl2sql-self-correction-loop.md
decisions/streamlit-vs-react-for-cognibi-ui.md
comparisons/agent-engine-vs-cloud-run-deployment.md
```

Reglas del slug:
- Todo en minúsculas, palabras separadas por guión
- Descriptivo: que al leer el nombre se entienda el tema
- Sin fechas en el nombre (la fecha va dentro del documento)

### 3. Rellenar el template

Copiar el template a la nueva ubicación y rellenar todas las secciones. Las secciones en comentarios HTML (`<!-- -->`) son instrucciones — reemplazarlas con contenido real.

### 4. Actualizar el índice

Siempre actualizar `README.md` después de crear una entrada — añadirla en la sección correspondiente del índice. No dejar entradas sin indexar.

---

## Idioma

- **Documentación:** español
- **Code snippets:** inglés (variable names, function names, comments en código)

---

## Lo que este repo NO es

- No es documentación de producto de CogniBI → eso va en `cognibi-playbook/`
- No es código → eso va en `cognibi-template/`
- No es notas de sesión → eso va en `cognibi-playbook/CLAUDE.md`
- No es un blog — cada entrada debe ser densa en valor práctico, no narrativa
