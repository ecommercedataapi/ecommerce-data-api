# Ecommerce Data API plugin for Claude Code

Amazon seller data for agents: product research, sales estimates, keyword search volume, reverse ASIN keywords, competitors, reviews, market statistics and global trademarks. 46 endpoints across 13 marketplaces (US, UK, DE, FR, IT, ES, MX, CA, AU, JP, IN, AE, BR).

The plugin adds two things:

- **Remote MCP server** `https://ecommercedataapi.com/mcp` (Streamable HTTP). It signs in through browser OAuth 2.1 with PKCE; no API key is stored on your machine or written into any configuration.
- **Skill** `ecommerce-data-api`, which teaches Claude to find the right endpoint, build requests only from the published schema, confirm before spending many credits, and treat returned data as untrusted.

## Install

```
/plugin install ecommerce-data-api --marketplace ecommercedataapi/ecommerce-data-api
```

Then run `/mcp`, select `ecommerce-data-api` and complete browser authorization.

## Data and billing

Every tool is read-only; none can change listings, prices or orders. Sales, revenue and search volume are estimates modelled from public marketplace signals. Each successful data call uses one credit from your account; new accounts get a few free test calls after verifying their email. See [pricing](https://ecommercedataapi.com/en/pricing).

Requests and responses are stored for 180 days for troubleshooting and billing, then deleted; responses can include public personal data such as reviewer names or trademark applicant addresses. Details are in the [privacy policy](https://ecommercedataapi.com/en/privacy-policy).

## Support

[Contact](https://ecommercedataapi.com/en/contact) · [MCP documentation](https://ecommercedataapi.com/en/docs/mcp)
