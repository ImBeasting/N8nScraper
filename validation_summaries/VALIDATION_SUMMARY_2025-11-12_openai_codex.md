# Validation Summary - openai_codex
Date: 2025-11-12
Agent: openai_codex
Sample Size: 35 nodes

## Statistics
- Total nodes sampled: 35 (problem categories + 10 random)
- Issues found: 5
- Critical: 1 (`_openai_codex_issue_007`)
- High: 1 (`_openai_codex_issue_010`)
- Medium: 2 (`_openai_codex_issue_008`, `_openai_codex_issue_009`)
- Low: 1 (`_openai_codex_issue_011`)

## Top Issues
1. [_openai_codex_issue_007] Namespace spread descriptors skipped – Google Sheets, Airtable, Postgres, SeaTable lose >80% of their properties.
2. [_openai_codex_issue_010] Notion credentials parsed from commented code, creating a phantom OAuth2 requirement with garbage displayOptions.
3. [_openai_codex_issue_008] Subtitle expressions truncated to `={{$parameter[` across 292 nodes, wiping context tooltips.

## Patterns Discovered
- **Namespace import spreads not resolved:** Any `...module.description` spread is ignored, affecting every VersionedNodeType that organizes resources under namespaced modules (Google Sheets, Airtable, Postgres, SeaTable, ConvertToFile, SeaTable Trigger, etc.).
- **Metadata helpers corrupted:** `loadOptionsMethods`/`listSearchMethods` arrays capture tokens from inside function bodies (`for`, `limit`, `q`) instead of the helper names (`getChannels`, `getUsers`, `getSpaces`, ...), leaving documentation unusable for Slack, Salesforce, ClickUp, ActiveCampaign.
- **Subtitle literals clipped:** 292 JSON files show `\"subtitle\": \"={{$parameter[` because the extractor stops at the first embedded quote in expressions like `={{$parameter[\"operation\"] + \": \" + $parameter[\"resource\"]}}`.

## Sample Quality Examples
### Excellent Extractions
- **Freshservice** (`extracted_docs/freshservice_data.json`): 158 properties with full resource/operation coverage match `n8n/packages/nodes-base/nodes/Freshservice` descriptions; credentials and operations_by_resource align with TypeScript.
- **Reddit** (`extracted_docs/reddit_data.json`): Credentials and property defaults mirror `Reddit.node.ts`, with 46 properties covering post/comment/profile operations; no discrepancies beyond known metadata gaps.

### Poor Extractions
- **Google Sheets** (`extracted_docs/googlesheets_data.json`): Only 23 properties extracted even though `versionDescription.ts` spreads ~100 description entries from `sheet` and `spreadsheet` modules (issue `_openai_codex_issue_007`).
- **Postgres** (`extracted_docs/postgres_data.json`): Just four selectors survive while `database.description` contains 30+ field definitions; operations still reference non-existent parameters (issue `_openai_codex_issue_007`).

## Recommendations
1. Prioritize `_openai_codex_issue_007` to restore namespace-spread properties (Google Sheets, Airtable, Postgres, SeaTable). This single fix recovers hundreds of parameters.
2. Address `_openai_codex_issue_010` so credential metadata ignores commented code—otherwise Notion docs remain misleading and automation will request invalid OAuth2 creds.
3. Fix `_openai_codex_issue_009` and `_openai_codex_issue_008` to clean metadata (helper lists + subtitles) before adding new validation rules; both issues affect hundreds of nodes.
