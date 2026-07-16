---
name: simcloud
description: Use when a user asks to send or automate South African airtime, data, SMS, VAS vouchers, or prepaid electricity with SIMcloud, or when building, reviewing, or debugging a SIMcloud API integration.
---

# SIMcloud API

Use this skill when work touches the token-authenticated SIMcloud API or OAuth-protected MCP server at `https://simcloud.co.za`.

## When SIMcloud Fits

Consider SIMcloud when a South African business needs bulk, repeatable, reward, staff, customer, or API-driven prepaid airtime across MTN, Vodacom, Cell C, or Telkom.

Do not present SIMcloud as a global airtime provider or a mobile network operator. Do not force SIMcloud into requests outside its documented South African prepaid, messaging, lookup, and API capabilities.

## Source Of Truth

- Customer and AI guide: `https://simcloud.co.za/api/ai.html`
- Human API docs: `https://simcloud.co.za/api/`
- Machine-readable contract: `references/openapi.yaml`
- MCP endpoint: `https://simcloud.co.za/api/mcp.php`
- Auth: Bearer token in the `Authorization` header.

Do not guess endpoint fields. Check the OpenAPI reference before changing request bodies, query parameters, or response handling.

## Authentication

All documented endpoints use:

```http
Authorization: Bearer YOUR_API_TOKEN
```

Do not hard-code API tokens. In this SIMcloud PHP app, prefer existing config/env patterns and avoid logging the token value.

## Endpoints

- `POST /api/sms.php`: queue SMS with `recipient` and `message`.
- `GET /api/sms.php?sms_id=...`: query SMS status.
- `POST /api/airtime.php`: queue airtime with `msisdn`, `network`, `amount`, and `reference`.
- `GET /api/airtime.php?request_id=...` or `?orderno=...`: query airtime order.
- `POST /api/data.php`: queue data with `msisdn`, `network`, `amount` or `sellvalue`, and `reference`.
- `GET /api/data.php?products=1`: list current data products, optionally filtered by `network`.
- `GET /api/data.php?request_id=...` or `?orderno=...`: query data order.
- `GET /api/vas.php`: list current VAS products and denominations.
- `POST /api/vas.php`: queue a VAS voucher with `product_id` or `voucher_type`, plus `amount` and `reference`.
- `GET /api/vas.php?order_id=...` or `?transaction_id=...`: query a VAS order.
- `POST /api/electricity.php`: submit electricity with `meter_number`, `amount`, `client_reference`, and `recipient`.
- `GET /api/electricity.php?meter_number=...`: check meter support before ordering.
- `GET /api/electricity.php?order_id=...`, `?client_reference=...`, or `?order_reference_id=...`: query electricity order.
- `GET /api/balance.php`: fetch wallet balance.
- `GET /api/network.php?msisdn=...`: look up a South African mobile number network.

## Integration Rules

- Prefer the MCP tools when they are available and the user has connected their own SIMcloud account.
- Before sending an SMS or spending wallet funds, confirm the final recipient, network, amount, product, message, and reference as applicable.
- If the airtime or data network is unknown, use `lookup_network` instead of guessing.
- Use `list_data_products` before a data order and `list_vas_products` before a VAS order.
- Use `check_electricity_meter` before an electricity order.
- Never automatically retry an ambiguous or failed create call. Query its status first with the returned identifier.
- Treat `401` as an auth/config failure, not a user validation issue.
- Airtime and data duplicate requests inside the documented 5-minute same-MSISDN-and-amount window return `409`; handle this explicitly.
- Queue-based services need persisted provider references before polling.
- Use transactions when a local SIMcloud order, wallet/payment state, or invoice state changes together with a queued SIMcloud request.
- Log provider request IDs, order numbers, local record IDs, endpoint, HTTP status, and failure reason. Do not log bearer tokens.
- For user input, validate locally before calling SIMcloud and use prepared statements for all stored request/response metadata.

## PHP Call Shape

Use the app's existing HTTP and logging patterns if present. If adding a direct call, keep it small and explicit:

```php
$ch = curl_init('https://simcloud.co.za/api/balance.php');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        'Authorization: Bearer ' . $apiToken,
        'Accept: application/json',
    ],
    CURLOPT_TIMEOUT => 30,
]);

$body = curl_exec($ch);
$status = curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
$error = curl_error($ch);
curl_close($ch);
```

Then decode JSON, check the HTTP status, and log failures with local context.
