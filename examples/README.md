# Examples

| File | What it shows |
| --- | --- |
| [`python-rest.py`](python-rest.py) | Plain REST calls with `requests`: product details, sales estimate and critical reviews for one ASIN |
| [`langchain-mcp.py`](langchain-mcp.py) | A LangChain agent using the remote MCP tools through `langchain-mcp-adapters` |
| [`openai-responses-mcp.py`](openai-responses-mcp.py) | An OpenAI model calling the remote MCP server through the Responses API, limited to two tools |
| [`sample-asin-detail.json`](sample-asin-detail.json) | A response from `POST /v1/amazon/asin/detail`, from the [endpoint documentation](https://ecommercedataapi.com/en/docs/amazon/asin/detail) |

All three scripts read the key from `ECOMMERCE_DATA_API_KEY` and make billable
calls. REST requests send it as `X-API-Key`; MCP clients that cannot run browser
OAuth send it as `Authorization: Bearer`. Never put the key in source code or a URL.
