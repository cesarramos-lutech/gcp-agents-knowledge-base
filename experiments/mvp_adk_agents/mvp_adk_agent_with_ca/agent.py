"""BI Analytics Agent — DataAgentToolset + Google ADK."""

import google.auth
from google.adk.agents import Agent
from google.adk.tools.data_agent.config import DataAgentToolConfig
from google.adk.tools.data_agent.credentials import DataAgentCredentialsConfig
from google.adk.tools.data_agent.data_agent_toolset import DataAgentToolset

credentials, _ = google.auth.default()

da_toolset = DataAgentToolset(
    credentials_config=DataAgentCredentialsConfig(credentials=credentials),
    data_agent_tool_config=DataAgentToolConfig(max_query_result_rows=100),
    tool_filter=["list_accessible_data_agents", "ask_data_agent"],
)

root_agent = Agent(
    name="ca_analytics_agent",
    model="gemini-2.0-flash",
    description="BI Analytics Assistant powered by the Conversational Analytics Data Agent.",
    instruction=(
        "You are a BI Analytics Assistant for an ecommerce company. "
        "Use 'list_accessible_data_agents' with project 'ai-future-data-agents' to find the data agent named 'The Look Ecommerce', "
        "then use 'ask_data_agent' with its full resource name to answer the user's question. "
        "Always present results clearly with insights, not just raw numbers."
    ),
    tools=[da_toolset],
)
