# API usage

## Native MCP first

When the current client exposes native MCP, use these tools in order:

1. `ecommerce_api_search` to discover APIs from the user's full intent.
2. `ecommerce_api_describe` to inspect the selected API schema and example.
3. `ecommerce_api_call` to execute a validated request.
4. `ecommerce_account` only when account or available Credits are needed.

If these tools are unavailable, use the equivalent `ecomdata api` CLI commands
below. The tools can come from the local stdio MCP or the public remote `/mcp`
server; never put an API key into either configuration.

## Discover

```bash
ecomdata api list --platform amazon --group products
ecomdata api search "reverse ASIN traffic keywords"
ecomdata api describe amazon.keywords.reverse-lookup
```

The live Catalog is authoritative. Do not rely on an endpoint list copied into
the Skill or model context.

## Call

```bash
ecomdata api call amazon.products.details \
  --json '{"marketplace":"US","asin":"B08CK5Z5Q1"}'
```

For larger JSON input, use:

```bash
ecomdata api call <api-code> --file request.json
```

## Repository integration

When the user asks to integrate Ecommerce Data API into code:

1. Inspect the repository's existing HTTP client and environment conventions.
2. Use the server-side `ECOMMERCE_DATA_API_KEY` environment variable.
3. Send `Authorization: Bearer <key>` or `X-API-Key: <key>`.
4. Implement types from the live Catalog or OpenAPI document.
5. Handle non-2xx responses, `request_id`, error codes, and HTTP 429.
6. Add focused tests without placing a real key in fixtures or snapshots.
7. Run a live request only when a key is already configured and network access
   is allowed.
