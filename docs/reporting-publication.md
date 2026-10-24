# SIMcloud reporting plugin publication

The public package is `plugins/simcloud-reporting`, version 1.0.2. It is separate from the existing full-access Codex plugin. Its display name is SIMcloud and its subtitle is “Account reports and status”.

Build the submission archive with:

```sh
python3 scripts/package_reporting.py
```

The ZIP contains only the portable plugin manifest, MCP configuration, reporting skill and square SVG icon. No application source, API token, reviewer credential, customer export or full-access OpenAPI reference belongs in it. The portable MCP configuration follows OpenAI’s documented `extensions.com.openai.auth` convention. OpenAI’s portal accepted the package and displayed the expected DCR, reporting resource and reporting-scope settings. The standalone upstream Agent Plugins MCP schema does not describe this OpenAI extension.

## Hosted requirements

- MCP: https://simcloud.co.za/api/reporting-mcp.php
- Protected resource metadata: https://simcloud.co.za/.well-known/oauth-protected-resource-reporting.php
- Standard metadata discovery: https://simcloud.co.za/.well-known/oauth-protected-resource/api/reporting-mcp.php
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
- Publisher identity: verified individual identity selected in the owning OpenAI organization. Do not pay for API credits merely because the dashboard shows an Add credits link; the public submission guide does not list a submission fee.
- Dedicated reviewer account: a new, isolated account was created at the owner’s requested review email. Its credentials and OTP instructions are saved only in the secure OpenAI form and owner-only local configuration. A read-only check confirmed zero balance, empty history and account-scoped not-found responses for absent airtime, data, SMS, VAS and electricity records. The review cases explicitly describe those results; populated-history and successful-order examples are not claimed.
- Live ChatGPT evaluation: still required using that account. Run all five positive and three negative cases before submission; the current cases expect empty history and missing-order responses, with no seeded orders.
- Video walkthrough: prepared and saved in OpenAI's review form at https://simcloud.co.za/chatgpt-reporting-review.php. It shows actual reporting MCP requests and responses from the dedicated account, with the client and testing limitations disclosed. It does not claim a ChatGPT conversation or interactive login demonstration.
- Domain proof: verified. The exact portal challenge is deployed at `https://simcloud.co.za/.well-known/openai-apps-challenge` and passed byte-for-byte compare-back and HTTP verification. Preserve this proof while the plugin uses the domain.
- Submit only after automated findings and required review materials are complete. Approval and Publish are separate steps.

Reviewer login details go in the secure dashboard fields. Do not commit them or place them in the ZIP. The package deliberately omits a demo video URL until a real recording exists.

## Official references

- [Package format and OAuth configuration](https://developers.openai.com/plugins/build/plugins)
- [Submission and publication](https://developers.openai.com/plugins/deploy/submission)
- [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines)

## Deployment and validation checkpoint - 24 October 2026

The reporting runtime and public support/privacy pages are deployed. The nine-file production manifest passed byte-for-byte compare-back verification. A subsequent one-file deployment corrected empty input-schema properties and passed compare-back too.

- Application commits: `0ae2f471` and `485c7a3c`, pushed to `ErikThiart/simcloud`.
- All nine changed runtime PHP files passed syntax checks with PHP 8.4.17. The five isolated HTTP/OAuth regression tests passed. PHP 8.5 was not available as a local test binary; the touched cURL path no longer calls deprecated `curl_close()`.
- Live reporting discovery advertises exactly seven tools, each with valid input and output JSON schemas, read-only annotations and `reports:read` security metadata.
- Live direct calls to all ten excluded full-access tool names were rejected. An unauthenticated balance request returned a reporting OAuth challenge. These checks used no account credentials and did not purchase products or change account data.
- The existing full endpoint still advertises 17 tools with valid JSON schemas.
- Support, privacy and OAuth metadata URLs return HTTP 200. The privacy policy contains the publisher-provided three-year record/log retention period.
- The original upload block was cleared after identity verification. Version 1.0.1 is uploaded as a draft. The initial Business category was rejected; Productivity removed the blocking category finding, and the later 1.0.2 upload cleared the remaining metadata recommendation. Domain ownership is verified. Review submission and publication have not occurred.

An owner-authorized live OAuth connection completed successfully in the OpenAI portal. This establishes authorization and discovery setup; the five positive/three negative ChatGPT scenarios and reviewer-account readiness remain unverified. No paid OpenAI API calls, API credit purchase or submission payment was made during this work.

## OpenAI draft

- [Manage the SIMcloud draft](https://platform.openai.com/plugins/manage/plugin_asdk_app_6adcde772fe48191b7e5a2f01340ec2d)
- Plugin ID: `plugin_asdk_app_6adcde772fe48191b7e5a2f01340ec2d`.
- Associated MCP app ID: `asdk_app_6adcde772fe48191b7e5a2f01340ec2d`.
- Draft package version: 1.0.2, uploaded.
- Publisher verification is individual, not business verification.
- Dedicated reviewer credentials and OTP sign-in instructions are saved privately. OTPs go to the designated review email, with the owner’s supplied contact for assistance. Live ChatGPT scenarios and the walkthrough recording remain outstanding. Never mark draft upload, domain verification or an in-progress automated check as review approval or publication.

The live connection used the owner’s signed-in account only after explicit authorization. The owner’s password was not placed in the reviewer fields, package or repository. The original test-account email settings were not changed; the newly created reviewer account uses the owner-specified review email. The database OTP check confirmed a one-way password hash rather than a plaintext code; no OTP protection or challenge record was altered.

The OpenAI portal completed discovery of all seven reporting tools and marked the MCP configuration Configured. The latest MCP scan reported no findings, and the bundled skill checks passed. Version 1.0.2 shows no metadata findings; the earlier non-blocking category recommendation cleared. Review status is Not submitted and publication is Not published.

Version 1.0.2 aligns the review scenarios with the actual dedicated account: zero balance, empty history, filtered empty history, and account-scoped not-found status responses. No synthetic production financial or provider records were created to populate the account. Successful delivery and populated account-history examples remain unverified in this review account.

The new dedicated reviewer account was created through the normal registration API after the owner supplied the review email and explicitly requested an invented test login number. Local duplication checks ran before registration. The provider returned HTTP 201 with `existing=false`. Read-only API checks then confirmed R0, empty history and HTTP 404 for absent status identifiers across all five status services. No wallet funding, purchase or SMS sending occurred. Account identifiers, passwords and API credentials remain outside this public repository.

The secure reviewer instructions contain the new username/password, the designated OTP mailbox and the owner-provided assistance contact, without naming another integration. No registration step is requested from reviewers. The final portal blocker is Supporting content: `Demo recording URL is required`. Live ChatGPT scenario evaluation and an actual walkthrough recording remain outstanding; no review submission or publication has been made.

That initial video blocker is now resolved. A 110-second walkthrough was assembled from screens captured while a local MCP test client executed real requests against the deployed reporting endpoint. All five positive protocol cases and three server boundary cases passed on the dedicated review account. A privately verified existing request belonging to another account returned HTTP 404; its identifier is omitted from the recording. The video, hosted page and private review context distinguish these protocol checks from conversational testing in ChatGPT, which remains unverified.

The walkthrough used a temporary, reporting-only authorization for the dedicated review account. The token was revoked and its temporary client disabled after capture; a live request verified rejection of the revoked token, and the local bearer file was removed. Account login and OTP settings were unchanged. No production financial records or purchases were created.

Application commit `0095696e` adds the review page and video. PHP lint, full video decoding, production byte-for-byte compare-back, HTTP video range requests and browser playback metadata checks passed. OpenAI saved the video URL and cleared the incomplete-review-information finding. Final submission still requires the displayed legal and policy attestations, followed by review approval before publication.

The browser's custom MCP setup reported that automatic OAuth discovery failed. A subsequent creation attempt with explicit reporting-only OAuth settings returned: "A service needed to create the app is temporarily unavailable." This is separate from the publishing portal's successful OAuth authorization and MCP scan. No live ChatGPT test result or video is claimed from those setup attempts.

Application commit `de3532ba` adds the standard path-specific reporting metadata URL and the `error` / `error_description` fields required by ChatGPT's tool-level OAuth challenge. Both changed runtime files passed lint, the five isolated regression tests passed, and production compare-back passed. Live checks confirmed the new metadata URL returns the reporting resource and scope, the existing full-resource metadata still works, and unauthenticated reporting calls include the expected challenge fields. A browser discovery retry after deployment still returned "Couldn't discover OAuth settings"; the server fix does not establish a working ChatGPT test connection. No generated cPanel configuration was changed.
