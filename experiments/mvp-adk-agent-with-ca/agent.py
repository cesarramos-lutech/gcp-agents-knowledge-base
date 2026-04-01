"""BI Analytics Agent — Conversational Analytics API + Google ADK."""

import os
from typing import AsyncGenerator

from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.cloud import geminidataanalytics_v1beta as ca
from google.genai import types
from typing import override

PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
DATASET = "look_ecommerce"
TABLES = [
    "orders",
    "order_items",
    "products",
    "users",
    "inventory_items",
    "events",
    "distribution_centers",
]

_CLIENT = ca.DataChatServiceAsyncClient()

_INLINE_CONTEXT = ca.Context(
    datasource_references=ca.DatasourceReferences(
        bq=ca.BigQueryTableReferences(
            table_references=[
                ca.BigQueryTableReference(
                    project_id=PROJECT,
                    dataset_id=DATASET,
                    table_id=table,
                )
                for table in TABLES
            ]
        )
    )
)


class ConversationalAnalyticsAgent(BaseAgent):
    """ADK agent that delegates NL2SQL to the Conversational Analytics API."""

    @override
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        question = ""
        if ctx.user_content and ctx.user_content.parts:
            question = " ".join(
                p.text for p in ctx.user_content.parts if getattr(p, "text", None)
            ).strip()

        if not question:
            yield Event(
                author=self.name,
                invocation_id=ctx.invocation_id,
                content=types.Content(
                    role="model",
                    parts=[types.Part(text="Please ask a question about your ecommerce data.")],
                ),
                turn_complete=True,
            )
            return

        request = ca.ChatRequest(
            parent=f"projects/{PROJECT}/locations/global",
            messages=[ca.Message(user_message=ca.UserMessage(text=question))],
            inline_context=_INLINE_CONTEXT,
        )

        stream = await _CLIENT.chat(request=request)

        async for response in stream:
            msg = response.system_message
            if not msg:
                continue

            text = ""
            if msg.text and msg.text.parts:
                text = getattr(msg.text.parts[0], "text", "").strip()

            if not text and msg.data:
                rows = getattr(msg.data.result, "data", None) or getattr(msg.data.result, "formatted_data", None)
                if rows:
                    text = f"Query returned {len(rows)} row(s)."

            if text:
                yield Event(
                    author=self.name,
                    invocation_id=ctx.invocation_id,
                    content=types.Content(
                        role="model",
                        parts=[types.Part(text=text)],
                    ),
                    turn_complete=False,
                )

        yield Event(
            author=self.name,
            invocation_id=ctx.invocation_id,
            turn_complete=True,
        )


root_agent = ConversationalAnalyticsAgent(
    name="ca_analytics_agent",
    description="BI Analytics Assistant powered by the Conversational Analytics API",
)
