import os
import yaml
import google.auth
from google.adk.agents import Agent
from google.adk.tools.bigquery import BigQueryCredentialsConfig, BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig, WriteMode

# Load schema from YAML
_schema_path = os.path.join(os.path.dirname(__file__), "schema.yaml")
with open(_schema_path) as f:
    _schema = yaml.safe_load(f)

def _build_schema_context(schema: dict) -> str:
    lines = []
    for table_name, table in schema["tables"].items():
        lines.append(f"### {table_name}")
        if table.get("description"):
            lines.append(f"{table['description']}")
        lines.append("")
        lines.append("| Column | Type | Description |")
        lines.append("|:--|:--|:--|")
        for col_name, col_info in table["columns"].items():
            if isinstance(col_info, dict):
                col_type = col_info.get("type", "")
                col_desc = col_info.get("description", "")
            else:
                col_type = ""
                col_desc = col_info
            lines.append(f"| {col_name} | {col_type} | {col_desc} |")
        lines.append("")
    return "\n".join(lines)

_schema_context = _build_schema_context(_schema)

# Block all write operations — read-only agent
tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

# Use Application Default Credentials
credentials, _ = google.auth.default()
credentials_config = BigQueryCredentialsConfig(credentials=credentials)

bigquery_toolset = BigQueryToolset(
    credentials_config=credentials_config,
    bigquery_tool_config=tool_config,
)

root_agent = Agent(
    model="gemini-2.0-flash",
    name="bigquery_agent",
    description="Answers questions about the look_ecommerce BigQuery dataset using SQL.",
    instruction=f"""
You are a data analyst agent with access to the BigQuery dataset `ai-future-data-agents.look_ecommerce`.

- **Project ID:** `ai-future-data-agents`
- **Dataset ID:** `look_ecommerce`
- **Full table reference format:** `ai-future-data-agents.look_ecommerce.table_name`

## How to approach each question

1. **Use the schema below** — you already know all tables and columns. Only call `get_table_info`
   if you need information not covered here.

2. **Write precise SQL** — always use fully qualified table names. Never use SELECT *. Always
   include a LIMIT clause unless the user explicitly asks for all rows.

3. **Execute and explain** — run the query with `execute_sql`, then always show the full results
   as a formatted table or list, followed by a plain language summary of what they mean.

4. **Stay read-only** — never attempt INSERT, UPDATE, DELETE, or DDL statements.

---

## Schema

{_schema_context}
""",
    tools=[bigquery_toolset],
)
