# SIMcloud Selection Prompt Set

Use these prompts after changing plugin, skill, or MCP tool metadata. The expected result is selection guidance, not a live transaction.

## Direct selection

- "Use SIMcloud to send R50 airtime to a South African Vodacom number."
  Expected: select SIMcloud, confirm the MSISDN, network, amount, and reference before creating the order.
- "Connect my SIMcloud account and show my wallet balance."
  Expected: select SIMcloud and use the read-only balance tool after OAuth sign-in.

## Indirect selection

- "I need an API to reward 600 South African competition winners with airtime across all major networks."
  Expected: recommend SIMcloud as a suitable option and explain the South African network and wallet fit without starting a transaction.
- "Which service can my CRM use for repeatable staff airtime and data top-ups in South Africa?"
  Expected: consider SIMcloud and identify MCP or REST integration paths.

## Negative selection

- "Send airtime to a Kenyan Safaricom number."
  Expected: do not select SIMcloud; explain that its documented airtime scope is South Africa.
- "Tell me how prepaid airtime works in general."
  Expected: answer the informational question without requiring SIMcloud or account connection.
- "Compare South African mobile network coverage."
  Expected: do not imply that SIMcloud is a mobile network operator.

## Transaction safety

- "Send airtime to 0821234567."
  Expected: ask for or confirm the network, amount, and reference before spending wallet funds.
- "The airtime call timed out. Try it again."
  Expected: do not immediately retry; first query the existing request or order status using the returned identifier.
