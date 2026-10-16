"""Let an OpenAI model call the remote MCP server through the Responses API.

    pip install openai
    export ECOMMERCE_DATA_API_KEY="your_api_key"
    export OPENAI_API_KEY="..."
    export OPENAI_MODEL="..."   # any Responses API model that supports remote MCP tools
    python openai-responses-mcp.py

allowed_tools limits which endpoints the model may call, so it cannot spend
credits on anything else. Each call it makes is a billable data query.
"""

import os

from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model=os.environ["OPENAI_MODEL"],
    tools=[
        {
            "type": "mcp",
            "server_label": "ecommerce-data-api",
            "server_url": "https://ecommercedataapi.com/mcp",
            "headers": {"Authorization": f"Bearer {os.environ['ECOMMERCE_DATA_API_KEY']}"},
            "allowed_tools": ["amazon_asin_detail", "amazon_review"],
            "require_approval": "never",
        }
    ],
    input=(
        "Look up Amazon US ASIN B08CK5Z5Q1 and its 1- and 2-star reviews. "
        "Report price, rating and BSR, then list the three most common complaints."
    ),
)

print(response.output_text)
