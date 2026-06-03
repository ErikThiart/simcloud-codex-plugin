# SIMcloud Codex Plugin

Connect [SIMcloud](https://simcloud.co.za) to Codex and use AI to work with **SMS, airtime, data bundles, prepaid electricity, wallet balance, and network lookup** through your own authenticated SIMcloud account.

This repository provides a **public Codex plugin** for the live SIMcloud MCP server. It is designed for both:

- **non-technical users** who want Codex to help them use SIMcloud
- **developers and SaaS builders** who want Codex to understand the SIMcloud API and integration model

## What Is This?

The SIMcloud Codex Plugin helps Codex connect to the live SIMcloud platform so it can assist with real SIMcloud tasks such as:

- checking SIMcloud wallet balance
- looking up South African mobile networks
- sending SMS messages
- creating airtime recharges
- creating data bundle recharges
- creating prepaid electricity orders
- checking the status of existing SMS and order requests

Each user connects with **their own SIMcloud account**. This is not a shared token or shared wallet setup.

## Why This Matters

Instead of logging into a portal and clicking through multiple screens, a user can ask Codex to help with SIMcloud tasks in plain language.

Examples:

- “Check my SIMcloud balance.”
- “Send an SMS to this customer and confirm the status.”
- “Recharge this number with airtime.”
- “Help me build a SaaS feature that uses the SIMcloud API.”

## What Codex Can Do With This Plugin

Once installed and connected, Codex can help users and teams:

- use SIMcloud from inside Codex
- understand the SIMcloud API without guessing fields
- connect through the live OAuth-protected MCP endpoint
- generate code against the published OpenAPI contract
- help build internal tools, automations, dashboards, and SaaS applications on top of SIMcloud

## SIMcloud Features Covered

The current plugin is designed around the SIMcloud capabilities exposed through the live MCP and API surface:

- **Wallet Balance**
- **Network Lookup**
- **SMS**
- **Airtime**
- **Data**
- **Prepaid Electricity**

## Who This Is For

### Non-technical users

If you want Codex to help you use SIMcloud without learning the raw API, this plugin gives Codex the context it needs.

### Developers

If you are integrating SIMcloud into a website, mobile app, admin portal, CRM workflow, customer support flow, or SaaS product, this plugin gives Codex a structured starting point.

### SaaS builders

If you want Codex to help you build a software product on top of SIMcloud, this repo is meant to make that easier by pointing Codex at:

- the live MCP server
- the OAuth metadata endpoints
- the OpenAPI specification
- the human-readable SIMcloud AI integration guide

## How It Works

This plugin uses the live SIMcloud MCP server and published SIMcloud API documentation.

At a high level:

1. The user connects their SIMcloud account with OAuth.
2. Codex uses the SIMcloud MCP endpoint where supported.
3. SIMcloud maps the OAuth token to the user’s own SIMcloud API token internally.
4. Tool calls run against that user’s own SIMcloud wallet, permissions, and account context.

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/ErikThiart/simcloud-codex-plugin.git
cd simcloud-codex-plugin
```

### 2. Add the marketplace to Codex

```bash
codex plugin marketplace add /absolute/path/to/simcloud-codex-plugin
```

### 3. Install the SIMcloud plugin

```bash
codex plugin add simcloud@simcloud
```

### 4. Start a new Codex thread

Start a new thread after installation so Codex picks up the plugin, skill, and MCP configuration.

## Authentication

The live SIMcloud integration uses OAuth.

- users authenticate with their own SIMcloud account
- PKCE is required
- use `code_challenge_method=S256`
- the plugin uses the live SIMcloud MCP endpoint rather than bundling a local server

## Example Prompts

### For everyday users

```text
Connect my SIMcloud account and check my wallet balance.
```

```text
Use SIMcloud to send an SMS to +27821234567 and then check the delivery status.
```

```text
Create a SIMcloud airtime, data, or electricity order using my connected account.
```

### For developers

```text
Read the SIMcloud plugin and help me build a SaaS feature that uses SIMcloud SMS, airtime, data, and electricity APIs.
```

```text
Use the SIMcloud OpenAPI and MCP setup to scaffold a SIMcloud integration for my app.
```

## Important Endpoints

### Human-readable guide

- AI integration guide: [https://simcloud.co.za/api/ai.html](https://simcloud.co.za/api/ai.html)

### MCP

- MCP endpoint: [https://simcloud.co.za/api/mcp.php](https://simcloud.co.za/api/mcp.php)

### OpenAPI

- OpenAPI spec: [https://simcloud.co.za/api/openapi.yaml](https://simcloud.co.za/api/openapi.yaml)

### OAuth discovery

- Protected resource metadata: [https://simcloud.co.za/.well-known/oauth-protected-resource](https://simcloud.co.za/.well-known/oauth-protected-resource)
- Authorization server metadata: [https://simcloud.co.za/.well-known/oauth-authorization-server](https://simcloud.co.za/.well-known/oauth-authorization-server)
- Authorization endpoint: [https://simcloud.co.za/oauth/authorize.php](https://simcloud.co.za/oauth/authorize.php)
- Token endpoint: [https://simcloud.co.za/oauth/token.php](https://simcloud.co.za/oauth/token.php)
- Dynamic client registration: [https://simcloud.co.za/oauth/register.php](https://simcloud.co.za/oauth/register.php)

## Repository Structure

- `plugins/simcloud/.codex-plugin/plugin.json`
  The Codex plugin manifest.
- `plugins/simcloud/.mcp.json`
  The MCP server configuration for the live SIMcloud MCP endpoint.
- `plugins/simcloud/skills/simcloud/SKILL.md`
  The Codex skill that teaches Codex how to work with SIMcloud.
- `plugins/simcloud/skills/simcloud/references/openapi.yaml`
  The machine-readable SIMcloud API contract used as a reference.
- `.agents/plugins/marketplace.json`
  Repo-local marketplace definition for plugin installation.

## Built For Real SIMcloud Use Cases

This plugin is meant to support practical SIMcloud workflows, including:

- SIMcloud SMS automation
- prepaid airtime integration
- prepaid data bundle workflows
- prepaid electricity ordering
- wallet balance checks
- South African mobile network lookups
- AI-assisted customer support flows
- Codex-assisted SaaS development on top of SIMcloud

## Notes For Developers

- Use the MCP endpoint first when Codex can access MCP tools.
- Use the OpenAPI spec as the REST source of truth.
- Do not assume shared credentials.
- Handle duplicate airtime and data requests correctly.
- Handle insufficient balance, validation failures, and asynchronous order flows explicitly.

## Support

- SIMcloud website: [https://simcloud.co.za](https://simcloud.co.za)
- AI integration guide: [https://simcloud.co.za/api/ai.html](https://simcloud.co.za/api/ai.html)
- Contact: `customercare@freepaid.co.za`

## License

This project is released under the MIT License. See [LICENSE](LICENSE).
