# Ecommerce Data API — MCP server and Agent Skill

Amazon seller data for AI agents: product research, sales estimates, keyword research and search volume, reverse ASIN keywords, competitors, reviews, market statistics and global trademarks. 46 endpoints across 13 marketplaces (US, UK, DE, FR, IT, ES, MX, CA, AU, JP, IN, AE, BR).

This repository holds the public connection details and the Agent Skill. The service itself runs at [ecommercedataapi.com](https://ecommercedataapi.com/en).

## Remote MCP

```
https://ecommercedataapi.com/mcp
```

Streamable HTTP with OAuth 2.1 (PKCE). The client opens a browser to sign in; no API key goes into the configuration.

**Claude Code**

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

Every endpoint is also exposed as its own tool, for example `amazon_product_research`, `amazon_sales_prediction_asin`, `amazon_traffic_keyword` (reverse ASIN), `amazon_asin_competitor`, `amazon_keyword_research` and `amazon_review`. The full list is in the [API catalog](https://ecommercedataapi.com/en/docs/api-catalog).

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

## What the data is

Sales, revenue and search volume figures are **estimates** modelled from public marketplace signals such as Best Sellers Rank. They are for comparing products and tracking direction, not accounting. The API cannot return another seller's orders, conversion rate or ad spend.

## Pricing

New accounts get 5 free test calls once the email is verified, valid for 24 hours. After that, calls are billed from one-time credit packs starting at 50 calls; there is no subscription. See [pricing](https://ecommercedataapi.com/en/pricing).

## Links

- Documentation: https://ecommercedataapi.com/en/docs
- REST quick start: https://ecommercedataapi.com/en/docs/getting-started
- Privacy policy: https://ecommercedataapi.com/en/privacy-policy
- Machine-readable summary: https://ecommercedataapi.com/llms.txt

---

## 中文说明

面向 AI Agent 的 Amazon 卖家数据：选品、销量估算、关键词搜索量、反查 ASIN、竞品、评论、市场统计和全球商标，共 46 个接口，覆盖 13 个站点。

- 远程 MCP 地址：`https://ecommercedataapi.com/mcp`，浏览器 OAuth 登录，配置里不需要写 API Key。
- Claude Code：`claude mcp add --transport http ecommerce-data-api https://ecommercedataapi.com/mcp`
- Skill 安装：`npx skills add ecommercedataapi/ecommerce-data-api --skill ecommerce-data-api`
- 新账号验证邮箱后送 5 次测试调用（24 小时内有效），之后按一次性调用包计费。
- 文档：https://ecommercedataapi.com/docs
