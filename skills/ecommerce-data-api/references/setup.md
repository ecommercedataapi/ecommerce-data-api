# Setup and diagnostics

## Commands

```bash
ecomdata login
ecomdata account
ecomdata doctor
ecomdata update --check
ecomdata update
ecomdata logout
ecomdata uninstall
ecomdata mcp serve
ecomdata mcp install --client codex
ecomdata mcp status
ecomdata mcp uninstall --client codex
```

`ecomdata login` displays the API key creation page and requests the key through
a secure local prompt. Never ask the user to send the key in chat.

The default installer installs the Skill, CLI, and local MCP configuration for
the selected supported client. Use `--skip-mcp` on macOS/Linux or `-SkipMcp` on
Windows only when MCP should not be configured. The installer's MCP runs as a
local stdio process and calls the cloud REST API. Clients that support remote
MCP can instead add `https://ecommercedataapi.com/mcp`, which signs in through
browser OAuth and needs no API key. An API key must never be placed in an MCP
URL or configuration.

`ecomdata mcp status` checks local MCP configuration without revealing the API
key. `ecomdata mcp install --client <client>` adds it after a skipped install;
`ecomdata mcp uninstall --client <client>` removes only that configuration; and
`ecomdata mcp serve` is the local stdio server command used by the configured
client.

On macOS, interactive login stores the key in Keychain. Linux uses Secret
Service when available. Automated `--api-key-stdin` login may use a private file
with mode `0600`.

## Recovery

| Error                  | Action                                                                                                                                             |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `API_KEY_REQUIRED`     | Ask the user to run `ecomdata login`.                                                                                                              |
| `INVALID_API_KEY`      | Ask the user to create a new key, then run `ecomdata login`.                                                                                       |
| `API_KEY_EXPIRED`      | Ask the user to create a replacement key.                                                                                                          |
| `INSUFFICIENT_CREDITS` | Report the required action without retrying.                                                                                                       |
| `NETWORK_ERROR`        | Run `ecomdata doctor`, then retry once.                                                                                                            |
| `REQUEST_TIMEOUT`      | Retry once for a single call; confirm before retrying a batch.                                                                                     |
| `API_NOT_FOUND`        | Search again using the user's complete intent. Do not guess codes.                                                                                 |
| MCP tools unavailable  | Run `ecomdata mcp status`, start a new client session, then run `ecomdata mcp install --client <client>` if the selected client is not configured. |

Do not expose raw stack traces unless the user explicitly requests debugging
details and `ECOMDATA_DEBUG=1` is appropriate.
