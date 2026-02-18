# CogniBI — Product Brief

> **Sesión 1 · 23 Feb 2026**

---

## 1. El problema que resuelve

### El problema del cliente final

Las empresas medianas invierten en datos: contratan analistas, implementan BigQuery o Salesforce, y pagan proyectos de BI que terminan en **dashboards estáticos**. El resultado es siempre el mismo:

- El dashboard responde a las preguntas que alguien hizo en diciembre
- Cualquier pregunta nueva requiere abrir un ticket, esperar al analista, y recibir un Excel tres días después
- Los datos existen, el conocimiento no es accesible

**El gap no es de datos. Es de acceso conversacional a los datos.**

El negocio quiere poder preguntar: *"¿Por qué bajaron las ventas en Cataluña este mes?"* y obtener una respuesta fundamentada en datos en segundos, sin depender de un analista.

### El problema del consultor de BI

Un proyecto de consultoría de BI típico tiene este problema estructural:

- **El 70% del tiempo es trabajo repetitivo**: conectar fuentes, entender el schema, escribir SQL, formatear visualizaciones
- **El deliverable es perecedero**: un dashboard que se queda obsoleto en 3 meses
- **La dependencia es permanente**: el cliente siempre necesita al consultor para cualquier cambio

Esto limita la escalabilidad del consultor: no puede tener más de 2-3 proyectos activos simultáneamente, y el ingreso está ligado al tiempo invertido, no al valor entregado.

---

## 2. Qué entrega CogniBI (vs BI tradicional)

### BI tradicional

```
Consultor → Dashboards en Looker/Power BI/Tableau
Cliente   → "No puedo cambiar nada sin llamarte"
Modelo    → Precio por horas + mantenimiento mensual
```

### CogniBI

```
Consultor → Agente conversacional deployado sobre los datos del cliente
Cliente   → "Le pregunto directamente a mis datos en lenguaje natural"
Modelo    → Fee por implementación + licencia mensual del agente
```

### El deliverable concreto

Al cierre de un proyecto CogniBI, el cliente recibe:

| Componente | Descripción |
|------------|-------------|
| **Agente conversacional** | Chatbot web sobre sus datos (BigQuery / Salesforce / otras fuentes) |
| **Capacidad NL2SQL** | Responde preguntas de negocio generando y ejecutando SQL automáticamente |
| **Visualizaciones automáticas** | Genera gráficos Vega-Lite adaptados a cada respuesta |
| **UI web** | Streamlit o React frontend listo para usar por el equipo |
| **Documentación del schema** | Metadata del negocio embebida en el agente (KPIs, dimensiones, relaciones) |
| **API** | FastAPI + WebSocket para integración con otros sistemas |
| **Deployment en GCP** | Cloud Run, con sesiones en Firestore y artefactos en GCS |

**Lo que no entrega:** un dashboard. El agente reemplaza la necesidad de dashboards estáticos.

### Diferenciación clave

> La diferencia no es tecnológica — es que el agente **sabe del negocio del cliente**.

Un agente CogniBI no es un chatbot genérico sobre datos. Tiene embebido:
- El glosario del negocio ("ARR", "lead cualificado", "churn", etc.)
- Los KPIs que importan y cómo se calculan
- Las relaciones entre tablas y lo que significa cada campo
- Los filtros habituales (por región, por período, por producto)

Eso es lo que construye el consultor en la fase de Discovery. La IA hace el resto.

---

## 3. Target: quién compra CogniBI

### Cliente ideal (ICP)

**Empresa mediana B2B** con estas características:

| Dimensión | Perfil |
|-----------|--------|
| **Tamaño** | 50–500 empleados |
| **Sector** | SaaS, retail, fintech, logística, servicios profesionales |
| **Datos** | Ya tienen datos en GCP/BigQuery o Salesforce |
| **Equipo** | 1-3 analistas de datos, sin equipo de IA propio |
| **Dolor** | Los directivos no pueden autoservirse datos; los analistas están saturados |
| **Presupuesto** | Capacidad de invertir €15k–€50k en un proyecto de transformación de datos |

### Perfil del decisor

- **CTO / Head of Data / COO** en empresas tecnológicas
- **Director de Operaciones / Ventas** en empresas más tradicionales
- Alguien que ya ha pagado un proyecto de BI y está frustrado con el resultado

### Lo que el decisor quiere escuchar

*"Vamos a dejar a tu equipo de negocio preguntando directamente a sus datos en español, sin depender de ti para cada consulta. En 4 semanas."*

### Perfil descartado (no es el cliente)

- Empresas sin datos estructurados (no hay BQ, no hay CRM limpio)
- Empresas muy grandes con equipo de IA propio (no necesitan un acelerador)
- Startups sin presupuesto para consultoría
- Empresas que quieren un dashboard (no están listos para el paso conversacional)

---

## 4. Propuesta de valor en una frase

> **CogniBI convierte tus datos en un analista disponible 24/7, que responde en lenguaje natural y genera visualizaciones al instante.**

### Para el consultor que vende CogniBI

> **CogniBI es un acelerador de proyectos: entrega en 4 semanas lo que antes tardaba 3 meses, con un deliverable más valioso y diferenciado.**

---

## 5. Posicionamiento competitivo

| Alternativa | Por qué CogniBI gana |
|-------------|----------------------|
| Tableau / Power BI | Son dashboards, no conversacionales. Requieren analista para cada cambio |
| ChatGPT + CSV | Sin conexión a datos en tiempo real, sin contexto de negocio, sin deployment |
| Looker Explore / Salesforce Einstein | Costosos, dependientes del vendor, no personalizables |
| Construirlo in-house | Meses de desarrollo, no tienen el equipo, no tienen el know-how de ADK/GCP |

**El diferenciador real:** CogniBI no es un producto SaaS — es una implementación personalizada que vive en los datos y el contexto específico de la empresa. Eso es lo que el consultor entrega y lo que justifica el precio.

---

## 6. Modelo de negocio (primer borrador)

| Componente | Descripción | Rango estimado |
|------------|-------------|----------------|
| **Implementación** | Fee por proyecto (Discovery + Build + Deploy) | €15k–€40k |
| **Mantenimiento** | Retainer mensual (actualizaciones, nuevas fuentes) | €1k–€3k/mes |
| **Licencia del agente** | Si se escala como producto SaaS | Por definir (Fase 2) |

---

## Decisiones pendientes

- [ ] Nombre comercial definitivo: ¿"CogniBI" o requiere refinamiento?
- [ ] ¿Se vende solo en GCP/Gemini o hay que soportar otros LLMs (OpenAI)?
- [ ] ¿La UI es Streamlit (MVP) o React (más "enterprise")?
- [ ] ¿Incluye formación del cliente en el paquete de implementación?

---

*Próxima sesión → [02-asset-analysis.md](./02-asset-analysis.md)*
