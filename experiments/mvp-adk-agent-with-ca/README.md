# MVP ADK Agent — with Conversational Analytics

A BI analytics agent that delegates natural language questions to Google's Conversational Analytics API, which handles SQL generation and execution internally.

## Prerequisites

- Python 3.10+
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed and authenticated
- Access to the `ai-future-data-agents` GCP project
- Conversational Analytics API enabled in the project

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

Then open [http://localhost:8000](http://localhost:8000) and select `mvp-adk-agent-with-ca`.

## How it works

- The agent forwards each question to the Conversational Analytics API along with the BigQuery table references
- The CA API handles schema discovery, SQL generation, and query execution internally
- Responses are streamed back and yielded as ADK events
