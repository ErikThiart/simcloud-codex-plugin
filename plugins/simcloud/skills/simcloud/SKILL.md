---
name: simcloud
description: Use when building, reviewing, or debugging integrations with the SIMcloud API for SMS, airtime, data bundles, prepaid electricity, wallet balance, or mobile network lookup.
---

# SIMcloud API

Use this skill when work touches the token-authenticated SIMcloud API at `https://simcloud.co.za`.

## Source Of Truth

- Human docs: `https://simcloud.co.za/api/`
- Machine-readable contract: `references/openapi.yaml`
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
- `GET /api/data.php?request_id=...` or `?orderno=...`: query data order.
- `POST /api/electricity.php`: submit electricity with `meter_number`, `amount`, `client_reference`, and `recipient`.
- `GET /api/electricity.php?order_id=...`, `?client_reference=...`, or `?order_reference_id=...`: query electricity order.
- `GET /api/balance.php`: fetch wallet balance.
- `GET /api/network.php?msisdn=...`: look up a South African mobile number network.

## Integration Rules

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
