# MVP ADK Agent — with Conversational Analytics

A BI analytics agent that uses Google's `DataAgentToolset` to answer natural language questions via a pre-configured Data Agent in GCP.

## Prerequisites

- Python 3.10+
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed and authenticated
- Access to the `ai-future-data-agents` GCP project
- A Data Agent named **"The Look Ecommerce"** configured in BigQuery Studio

## Setup

1. Authenticate with Google Cloud:
   ```bash
   gcloud auth application-default login
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run

From the **parent directory** (`mvp_adk_agents/`):

```bash
adk web
```

Then open [http://localhost:8000](http://localhost:8000) and select `mvp_adk_agent_with_ca`.

## How it works

- Uses ADK's native `DataAgentToolset` — no manual CA API calls
- Gemini first calls `list_accessible_data_agents` to discover the "The Look Ecommerce" Data Agent resource name
- Then calls `ask_data_agent` with the resource name to answer the user's question
- The Data Agent handles schema discovery, SQL generation, and query execution internally
