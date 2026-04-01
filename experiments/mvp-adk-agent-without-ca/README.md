# MVP ADK Agent — without Conversational Analytics

A BI analytics agent that uses Gemini to write and execute BigQuery SQL based on natural language questions.

## Prerequisites

- Python 3.10+
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed and authenticated
- Access to the `ai-future-data-agents` GCP project with BigQuery permissions

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

From the **parent directory** (`mvp_adk-agents/`):

```bash
adk web
```

Then open [http://localhost:8000](http://localhost:8000) and select `mvp-adk-agent-without-ca`.

## How it works

- Gemini reads the table schema from `schema.yaml` upfront
- For each question it writes a BigQuery SQL query and executes it via the native `BigQueryToolset`
- Write operations are blocked — the agent is read-only
