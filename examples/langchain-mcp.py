"""Give a LangChain agent the remote MCP tools.

    pip install langchain langchain-mcp-adapters langchain-anthropic
    export ECOMMERCE_DATA_API_KEY="your_api_key"
    export ANTHROPIC_API_KEY="..."
    python langchain-mcp.py

Any LangChain chat model works; swap the model string for your provider.
Each tool call the agent makes is a billable data query.
"""

import asyncio
import os

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    client = MultiServerMCPClient(
        {
            "ecommerce-data-api": {
                "transport": "streamable_http",
                "url": "https://ecommercedataapi.com/mcp",
                "headers": {"Authorization": f"Bearer {os.environ['ECOMMERCE_DATA_API_KEY']}"},
            }
        }
    )
    tools = await client.get_tools()

    agent = create_agent("anthropic:claude-sonnet-5-5", tools)
    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Look up Amazon US ASIN B08CK5Z5Q1: price, rating, BSR and estimated "
                        "monthly sales. Then summarise the main complaints in its 1- and 2-star "
                        "reviews. Label every estimate as an estimate."
                    ),
                }
            ]
        }
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
