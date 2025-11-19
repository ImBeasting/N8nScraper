# Validation Summary - openai_codex
Date: 2025-11-06
Agent: openai_codex
Sample Size: 35 nodes

## Statistics
- Total nodes sampled: 35
- Issues found: 6
- Critical: 0
- High: 3
- Medium: 2
- Low: 1

## Top Issues
1. [_openai_codex_issue_002] Object defaults serialized as strings for 2,908 properties – wipes structured defaults across Slack, ActiveCampaign, WhatsApp.
2. [_openai_codex_issue_001] `listSearchMethods` arrays polluted with tokens (`for`, `call`) and missing actual helpers (`getUsers`, `searchCards`).
3. [_openai_codex_issue_003] Branching nodes (If, Switch) lose `outputNames`, hiding true/false routing semantics.

## Patterns Discovered
- Versioned nodes remain gutted: zero properties and missing base metadata persist in PostgresV2, MicrosoftOutlookV2, GoogleDriveV2, etc., reaffirming `_claude_issue_009` and `_claude_issue_020`.
- Options/options-like schemas continue to miss `value` fields and nested types (Slack, Salesforce, ClickUp), reinforcing `_gemini_issue_001` and `_claude_issue_001`.
- Resource locator definitions and collections show cascading metadata loss (modes trimmed, typeOptions blank), compounding `_claude_issue_004` and our new default serialization bug.

## Sample Quality Examples
### Excellent Extractions
- Autopilot Trigger (`extracted_docs/autopilottrigger_data.json`): metadata, authentication, and webhook definitions align with `n8n/packages/nodes-base/nodes/Autopilot/AutopilotTrigger.node.ts`.
- AWS Rekognition (`extracted_docs/awsrekognition_data.json`): operation list and credentials mirror the TypeScript source with minimal drift beyond known options/value bug.

### Poor Extractions
- PostgresV2 (`extracted_docs/PostgresV2_data.json`): zero properties and empty metadata despite rich `versionDescription` spread (see `n8n/packages/nodes-base/nodes/Postgres/v2/actions/versionDescription.ts`).
- HTTP Request (`extracted_docs/httpRequest_data.json`): 0 properties plus missing `usableAsTool` object from `V3/HttpRequestV3.node.ts`, leaving core schema unusable.

## Recommendations
1. Prioritise `_openai_codex_issue_002` so collection defaults regain object form; re-extract Slack, ActiveCampaign, WhatsApp to validate fixes.
2. Address `_openai_codex_issue_001` and `_openai_codex_issue_003` to restore list search metadata and branch labels before revisiting existing spread/import fixes.
# End of Summary
