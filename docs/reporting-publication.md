# SIMcloud reporting plugin publication

The public package is `plugins/simcloud-reporting`, version 1.0.0. It is separate from the existing full-access Codex plugin. Its display name is SIMcloud and its subtitle is “Account reports and status”.

Build the submission archive with:

```sh
python3 scripts/package_reporting.py
```

The ZIP contains only the portable plugin manifest, MCP configuration, reporting skill and square SVG icon. No application source, API token, reviewer credential, customer export or full-access OpenAPI reference belongs in it. The portable MCP configuration follows OpenAI’s documented `extensions.com.openai.auth` convention. The upstream Agent Plugins MCP schema currently rejects that extension; validate the base transport fields against that schema and use the OpenAI portal for final extension validation.

## Hosted requirements

- MCP: https://simcloud.co.za/api/reporting-mcp.php
- Protected resource metadata: https://simcloud.co.za/.well-known/oauth-protected-resource-reporting.php
- OAuth authorization server: https://simcloud.co.za/.well-known/oauth-authorization-server
- Permission: `reports:read`
- Product and support: https://simcloud.co.za/chatgpt-reporting.php
- Privacy: https://simcloud.co.za/chatgpt-reporting-privacy.php
- Terms: https://simcloud.co.za/legal.php

The server advertises and permits only `get_wallet_balance`, `get_transaction_history`, `get_sms_status`, `get_airtime_order`, `get_data_order`, `get_vas_order` and `get_electricity_order`. Direct calls to other tool names fail before forwarding to the API. Reporting OAuth tokens are bound to the reporting resource and cannot authorize the full MCP endpoint. VAS redemption codes and electricity recharge PINs are excluded.

The account/transaction and operational-log retention period supplied by the publisher is three years. This release documents that policy; it does not introduce or alter automated retention jobs.

## Review status and remaining work

- Package and review scenarios: prepared. Five positive and three negative cases are embedded in the manifest.
- Local security/OAuth regression: uses disposable synthetic accounts and a local stub API. It does not prove a live ChatGPT connection or reviewer account works.
- Publisher identity: must be verified in the OpenAI organization that owns the submission. Do not pay for API credits merely because the dashboard shows an Add credits link; the public submission guide does not list a submission fee.
- Dedicated reviewer account: still required. It must contain sample account history and existing order/SMS records corresponding to the review cases, without real customer data. Do not insert synthetic records into production wallet, payment, invoice or provider queues just to populate a demo. A suitable existing isolated test account or properly separated test dataset is needed.
- Live ChatGPT evaluation: still required using that account. Supply the actual seeded order identifiers in the secure reviewer instructions, and run all five positive and three negative cases before submission.
- Video walkthrough: still required. Record the working account connection and reporting cases after live evaluation. Do not substitute a mocked test recording for evidence of the live ChatGPT workflow.
- Domain proof: host the exact token shown by the portal at the exact challenge URL. Do not invent a token or replace a proof used by another plugin.
- Submit only after automated findings and required review materials are complete. Approval and Publish are separate steps.

Reviewer login details go in the secure dashboard fields. Do not commit them or place them in the ZIP. The package deliberately omits a demo video URL until a real recording exists.

## Official references

- [Package format and OAuth configuration](https://developers.openai.com/plugins/build/plugins)
- [Submission and publication](https://developers.openai.com/plugins/deploy/submission)
- [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines)
