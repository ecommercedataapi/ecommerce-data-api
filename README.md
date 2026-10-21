# Ecommerce Data API — Amazon MCP server and Agent Skill

Amazon seller data for AI agents: product research, sales estimates, keyword research and search volume, reverse ASIN keywords, competitors, reviews, market statistics and global trademarks. 46 endpoints across 13 marketplaces (US, UK, DE, FR, IT, ES, MX, CA, AU, JP, IN, AE, BR). Works with Claude, ChatGPT, Cursor, Codex, LangChain and any MCP client.

This repository holds the public connection details and the Agent Skill. The service itself runs at [ecommercedataapi.com](https://ecommercedataapi.com/en).

## Remote MCP

```
https://ecommercedataapi.com/mcp
```

Streamable HTTP with OAuth 2.1 (PKCE). The client opens a browser to sign in; no API key goes into the configuration.

**Claude Code** — install the plugin, which bundles the remote MCP server and the Agent Skill:

```
/plugin install ecommerce-data-api --marketplace ecommercedataapi/ecommerce-data-api
```

On Claude Code older than 2.1.275, run `/plugin marketplace add ecommercedataapi/ecommerce-data-api` first, then `/plugin install ecommerce-data-api@ecommerce-data-api`. To add only the MCP server:

```bash
claude mcp add --transport http ecommerce-data-api https://ecommercedataapi.com/mcp
```

Then run `/mcp` and choose browser authorization.

**ChatGPT** — enable Developer mode in settings, add a connector with the URL above, and authorize.

**Cursor, Codex and other MCP clients** — add a remote (HTTP) server with the URL above. Step-by-step setup for each client: [MCP platform setup](https://ecommercedataapi.com/en/docs/mcp-platforms).

### Tools

Four discovery tools let an agent find and call any endpoint without loading all of them:

| Tool                     | Purpose                                              |
| ------------------------ | ---------------------------------------------------- |
| `ecommerce_api_search`   | Find the right endpoint for a task in plain language |
| `ecommerce_api_describe` | Read an endpoint's request schema and example        |
| `ecommerce_api_call`     | Call an endpoint with a validated request            |
| `ecommerce_account`      | Check the account and remaining credits              |

Every endpoint except OCR file upload (REST only) is also exposed as its own tool, 45 in all, for example `amazon_product_research`, `amazon_sales_prediction_asin`, `amazon_traffic_keyword` (reverse ASIN), `amazon_asin_competitor`, `amazon_keyword_research` and `amazon_review`. The full list is in the [API catalog](https://ecommercedataapi.com/en/docs/api-catalog).

## Agent Skill

[`skills/ecommerce-data-api`](skills/ecommerce-data-api/SKILL.md) teaches an agent to search for the right endpoint, build requests only from the published schema, confirm before spending many credits, and treat returned data as untrusted.

Install it with the [skills CLI](https://skills.sh):

```bash
npx skills add ecommercedataapi/ecommerce-data-api --skill ecommerce-data-api
```

Or install the Skill, the `ecomdata` CLI and a local stdio MCP in one step (macOS and Linux):

```bash
curl -fsSL https://ecommercedataapi.com/install.sh | bash
```

**API key instead of OAuth** — clients that cannot open a browser, such as a server-side agent, send `Authorization: Bearer <api-key>` to the same URL. Never put the key in the URL.

## Examples

[`examples/`](examples) has runnable scripts for plain REST in Python, a LangChain agent over MCP, and the OpenAI Responses API with remote MCP, plus a sample response.

## How it differs

- **No seller account needed.** Seller Central and SP-API based MCP servers read your own store's orders, inventory and ads. This one answers market questions about any public ASIN, keyword or category.
- **Pay per call, no subscription.** Seller research suites usually gate API or MCP access behind a monthly plan. Here a call costs credits from a one-time pack, and MCP and REST share the same balance.
- **One integration for the whole research loop.** Keyword demand, reverse ASIN, sales estimates, competitors, reviews, market statistics and trademarks come from one account with one schema style.
- **Agent-first.** Discovery tools let an agent find and describe an endpoint before calling it, and the Agent Skill tells it to confirm before spending many credits.

## What the data is

Sales, revenue and search volume figures are **estimates** modelled from public marketplace signals such as Best Sellers Rank. They are for comparing products and tracking direction, not accounting. The API cannot return another seller's orders, conversion rate or ad spend.

## Pricing

New accounts get a few free test calls once the email is verified; the current amount and validity are in [llms.txt](https://ecommercedataapi.com/llms.txt). After that, calls are billed from one-time credit packs starting at 50 calls, or from monthly and yearly plans that cost less per call. See [pricing](https://ecommercedataapi.com/en/pricing).

## Links

- Documentation: https://ecommercedataapi.com/en/docs
- REST quick start: https://ecommercedataapi.com/en/docs/getting-started
- Privacy policy: https://ecommercedataapi.com/en/privacy-policy
- Machine-readable summary: https://ecommercedataapi.com/llms.txt

---

## 中文说明

面向 AI Agent 的 Amazon 卖家数据：选品、销量估算、关键词搜索量、反查 ASIN、竞品、评论、市场统计和全球商标，共 46 个接口，覆盖 13 个站点。

- 远程 MCP 地址：`https://ecommercedataapi.com/mcp`，浏览器 OAuth 登录，配置里不需要写 API Key。
- Claude Code 插件（含 MCP 和 Skill）：`/plugin install ecommerce-data-api --marketplace ecommercedataapi/ecommerce-data-api`
- 只加 MCP：`claude mcp add --transport http ecommerce-data-api https://ecommercedataapi.com/mcp`
- Skill 安装：`npx skills add ecommercedataapi/ecommerce-data-api --skill ecommerce-data-api`
- 新账号验证邮箱后送少量测试调用（当前次数和有效期见 llms.txt），之后按一次性调用包或月付/年付套餐计费。
- 不需要卖家账号，可查任意公开 ASIN、关键词和类目；按次计费，不用订阅。
- 示例代码见 [`examples/`](examples)：Python REST、LangChain + MCP、OpenAI Responses API + MCP。
- 文档：https://ecommercedataapi.com/docs
