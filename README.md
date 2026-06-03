# SIMcloud Codex Plugin

Use SIMcloud inside Codex through the live SIMcloud MCP server.

This plugin is intended for Codex users who want Codex to work with the full SIMcloud API surface that is currently exposed through the SIMcloud MCP endpoint:

- wallet balance
- network lookup
- SMS
- airtime
- data
- prepaid electricity

Each user authenticates with their own SIMcloud account. The plugin does not use a shared API token.

## What This Repo Contains

- `plugins/simcloud/.codex-plugin/plugin.json`
  The Codex plugin manifest.
- `plugins/simcloud/.mcp.json`
  Points Codex at the live SIMcloud MCP endpoint.
- `plugins/simcloud/skills/simcloud/SKILL.md`
  Workflow guidance for Codex when building or debugging SIMcloud integrations.
- `.agents/plugins/marketplace.json`
  A repo-local marketplace entry so the plugin can be installed from this repo.

## SIMcloud Endpoints

- AI guide: `https://simcloud.co.za/api/ai.html`
- MCP endpoint: `https://simcloud.co.za/api/mcp.php`
- OpenAPI spec: `https://simcloud.co.za/api/openapi.yaml`
- Protected resource metadata: `https://simcloud.co.za/.well-known/oauth-protected-resource`
- Authorization server metadata: `https://simcloud.co.za/.well-known/oauth-authorization-server`

## Install In Codex

1. Clone this repo somewhere local:

```bash
git clone https://github.com/ErikThiart/simcloud-codex-plugin.git
cd simcloud-codex-plugin
```

2. Add the repo-local marketplace to Codex:

```bash
codex plugin marketplace add /absolute/path/to/simcloud-codex-plugin
```

3. Install the plugin from that marketplace:

```bash
codex plugin add simcloud@simcloud
```

4. Start a new Codex thread after installation so Codex picks up the plugin and MCP server.

## Authentication

The live SIMcloud MCP server uses OAuth.

- Users authenticate with their own SIMcloud account.
- PKCE with `S256` is required.
- The MCP server maps the OAuth access token to the user's SIMcloud API token internally.

## Example Prompts

```text
Connect my SIMcloud account and check my wallet balance.
```

```text
Use SIMcloud to send an SMS to +27821234567 and then check the delivery status.
```

```text
Create a SIMcloud airtime, data, or electricity order using my connected account.
```

## Notes

- The plugin is designed to use the live SIMcloud MCP server rather than bundling a separate local server.
- REST request and field details are documented in the published OpenAPI spec.
- The human-readable AI integration guide is at `https://simcloud.co.za/api/ai.html`.
