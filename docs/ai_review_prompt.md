# n8n Node Extraction - Quality Audit Protocol

**Mission:** Conduct a systematic quality audit of extracted node documentation by cross-referencing with source TypeScript files. Document findings using the multi-agent collaboration system.

**Target:** Find and document issues affecting extraction quality. Be thorough, specific, and evidence-based.

---

## Quick Start Guide

### Prerequisites Check
```bash
cd "/home/tyler/Projects/N8nScraper"
ls extracted_docs/*.json | wc -l  # Should show ~450 files
python3 validate_extraction.py    # Baseline metrics
```

### Your Workflow (Overview)
1. **Baseline** (5 min) - Run automated validation, review metrics
2. **Sample** (5 min) - Select 35+ nodes strategically
3. **Analyze** (30 min) - Deep cross-reference against source
4. **Document** (20 min) - Create detailed issue files
5. **Patterns** (10 min) - Identify recurring problems
6. **Report** (10 min) - Generate summary and recommendations

**Total Time:** ~80 minutes for thorough audit

---

## Phase 1: Baseline Assessment (5 minutes)

### Run Automated Validation
```bash
cd "/home/tyler/Projects/N8nScraper"
python3 validate_extraction.py
cat validation_report.json | jq '.stats'
```

### Document These Metrics
- Total data files extracted
- Nodes with zero properties (should be 1 - NoOp only)
- Nodes with null displayNames (should be 0)
- Duplicate file groups (should be 0)
- Missing metadata (inputs, outputs, group, icon)
- Unresolved template variables

### Quick Quality Check
```bash
# Check recent improvements
jq '.properties | length' extracted_docs/httprequest_data.json   # Should be 42
jq '.properties | length' extracted_docs/elasticsearch_data.json # Should be 35
jq '.properties | length' extracted_docs/slack_data.json        # Should be 111
```

---

## Phase 2: Strategic Sampling (5 minutes)

**Target Sample Size:** 35-50 nodes minimum

### A. Automated Problem Detection (25 nodes)
```bash
# Zero properties (5 nodes)
jq -r '.issues.zero_properties[0:5][]' validation_report.json

# Template variables (5 nodes)
jq -r '.issues.template_variables[0:5][].file' validation_report.json

# Missing outputs (3 nodes)
jq -r '.issues.missing_outputs[0:3][]' validation_report.json

# Random sample (12 nodes)
ls -1 extracted_docs/*_data.json | shuf -n 12
```

### B. Strategic High-Value Nodes (10 nodes)

**Popular Nodes** (users depend on these):
- Slack, HTTP Request, Google Sheets, Notion, Airtable

**Complex Nodes** (stress test extraction):
- Salesforce, HubSpot, GitLab, ActiveCampaign, ClickUp

**Recently Fixed** (verify fixes work):
- Check nodes affected by recent Issues #026, #027, #025

### C. Version-Aware Sampling (5 nodes)

**Versioned Nodes** (check v1/v2/V1/V2 handling):
```bash
# Find versioned nodes
find n8n/packages/nodes-base/nodes -type d -name "v[0-9]*" -o -name "V[0-9]*" | \
  sed 's|.*/nodes/\([^/]*\)/.*|\1|' | sort -u | head -5
```

---

## Phase 3: Deep Cross-Reference Analysis (30 minutes)

For EACH sampled node, perform this systematic audit.

### 3.1 Locate All Source Files

```bash
NODE_NAME="Slack"  # Replace with actual node name

# Main node file (entry point)
find n8n/packages/nodes-base/nodes -name "${NODE_NAME}.node.ts"

# Description files (property definitions)
find n8n/packages/nodes-base/nodes/${NODE_NAME} -name "*Description*.ts" -o -name "*description*.ts"

# Version-specific files (for versioned nodes)
find n8n/packages/nodes-base/nodes/${NODE_NAME}/v* -name "*.ts" 2>/dev/null
find n8n/packages/nodes-base/nodes/${NODE_NAME}/V* -name "*.ts" 2>/dev/null

# Resource/operation files (for multi-resource nodes)
find n8n/packages/nodes-base/nodes/${NODE_NAME} -path "*/actions/*" -name "*.ts" 2>/dev/null
```

**Pro Tip:** Open 2-3 key source files in your analysis. Don't just grep - actually read the structure.

---

### 3.2 Systematic Quality Checks

Use this checklist for EVERY sampled node:

#### ✅ Metadata Validation

**Check node_info section:**

```bash
NODE="slack"  # lowercase for filename
jq '.node_info' extracted_docs/${NODE}_data.json
```

| Field | What to Verify | Common Issues |
|-------|----------------|---------------|
| displayName | Matches source exactly | Null, generic name, template variable |
| name | Lowercase identifier matches | Wrong case, missing |
| icon | Correct path or object {light, dark} | Empty string, object not parsed |
| group | Array with all values | Missing, wrong type (string not array) |
| version | All versions present as array | Missing versions, wrong format |
| inputs | Converted from NodeConnectionTypes | Missing (triggers=expected), wrong values |
| outputs | Converted from NodeConnectionTypes | Missing, not converted |
| subtitle | Expression preserved exactly | Missing, mangled |
| description | Complete sentence | Truncated, missing |
| defaults | Object not string | Empty, wrong type |

**Quick Command:**
```bash
# Compare quickly
jq -r '.node_info | "Display: \(.displayName)\nName: \(.name)\nIcon: \(.icon)\nGroup: \(.group)\nVersions: \(.version)"' \
  extracted_docs/${NODE}_data.json
```

---

#### ✅ Credentials Validation

**Source Pattern:**
```typescript
credentials: [
  {
    name: 'slackApi',
    required: true,
    displayOptions: { show: { authentication: ['accessToken'] } }
  }
]
```

**Check extracted data:**
```bash
jq '.credentials' extracted_docs/${NODE}_data.json
```

**What to Look For:**
- ❌ Empty objects `{}` in credentials array (parsing failure)
- ❌ Missing credential entries (count mismatch)
- ❌ Missing `displayOptions` (conditional auth broken)
- ❌ Missing `required` field or wrong type
- ❌ Name mismatch vs source

**Evidence to Collect:**
```bash
# Count in source
grep -c "name: '" n8n/packages/nodes-base/nodes/${NODE_NAME}/*.node.ts | grep credentials

# Count extracted
jq '.credentials | length' extracted_docs/${NODE}_data.json

# Show names
jq -r '.credentials[].name' extracted_docs/${NODE}_data.json
```

---

#### ✅ Properties Count Verification

**THE MOST IMPORTANT CHECK** - Property count reveals extraction completeness.

**Step 1: Count in extracted JSON**
```bash
jq '.properties | length' extracted_docs/${NODE}_data.json
```

**Step 2: Estimate count in source**

For simple nodes:
```bash
grep -c "displayName:" n8n/packages/nodes-base/nodes/${NODE_NAME}/*Description*.ts
```

For versioned nodes (v2/V2/versionDescription):
```bash
grep -c "displayName:" n8n/packages/nodes-base/nodes/${NODE_NAME}/v*/actions/versionDescription.ts
grep -c "displayName:" n8n/packages/nodes-base/nodes/${NODE_NAME}/v*/*Description*.ts
```

For multi-resource nodes with spreads:
```bash
# Count main properties
grep -c "displayName:" n8n/packages/nodes-base/nodes/${NODE_NAME}/v*/actions/versionDescription.ts

# Count operation files
find n8n/packages/nodes-base/nodes/${NODE_NAME} -path "*/actions/*" -name "*.operation.ts" -exec grep -c "displayName:" {} +

# Add them up (approximately)
```

**Step 3: Compare**
- If extracted < 50% of source: 🚨 **CRITICAL ISSUE**
- If extracted < 80% of source: ⚠️ **HIGH ISSUE**
- If extracted < 95% of source: ⚡ **MEDIUM ISSUE**

**Common Root Causes When Count is Low:**
1. **Spread operators not resolved** - `...arrayName` in properties array
2. **Imports not followed** - `import { fields } from './Description'`
3. **Collections not recursed** - Nested options in collection/fixedCollection types
4. **Version file not used** - Extracting from base wrapper instead of v2/NotionV2.node.ts
5. **Resource spreads missed** - `...record.description` not expanded
6. **Map transformations lost** - `...array.map(x => ...)` not resolved

---

#### ✅ Property Quality Check (Sample 10 properties)

**Pick 10 random properties to inspect:**
```bash
jq '.properties[0:10][] | {displayName, name, type, default, required}' extracted_docs/${NODE}_data.json
```

**What to Verify:**

| Field | Expected | Red Flags |
|-------|----------|-----------|
| displayName | Non-null string | `null`, empty string, template ${...} |
| name | Camelcase identifier | Missing, wrong format |
| type | Valid type | Wrong type, missing |
| default | Correct type for field | Wrong type (string instead of number) |
| description | Complete text | Missing, truncated, `undefined` |
| options | Array of {name, value} | Missing `value` field (common bug!) |
| options[].value | Present in ALL options | Missing in some but not others |
| typeOptions | Object if complex | Missing loadOptionsMethod, minValue, etc |
| displayOptions | Object with show/hide | Missing, causing fields to show incorrectly |
| placeholder | String if exists in source | Missing when it should be there |
| hint | String if exists in source | Missing when it should be there |

**Critical Bug to Check - Missing option values:**
```bash
# Check if ANY option is missing 'value' field
jq '.properties[] | select(.type == "options") | .options[]? | select(.value == null) | {name, VALUE_MISSING: true}' \
  extracted_docs/${NODE}_data.json
```

---

#### ✅ Collections/FixedCollections (Nested Options)

Collections are the #1 place extraction fails due to complexity.

**Check for nested options:**
```bash
# Count collections
jq '[.properties[] | select(.type == "collection" or .type == "fixedCollection")] | length' \
  extracted_docs/${NODE}_data.json

# Check if nested options are extracted
jq '.properties[] | select(.type == "collection") | {name, nested_count: (.options | length)}' \
  extracted_docs/${NODE}_data.json

# Look for empty nested options (BUG indicator)
jq '.properties[] | select(.type == "collection" and (.options | length) == 0) | .name' \
  extracted_docs/${NODE}_data.json
```

**What to Look For:**
- Collection exists but `options: []` is empty (extraction failed)
- Collection has options but missing nested fields
- FixedCollection with `values: []` empty

**This was Issue #026** - now fixed, but verify on your samples.

---

#### ✅ Operations Validation

For multi-resource nodes (Slack, Salesforce, HubSpot, etc.):

```bash
# Check operations count
jq '.operations | length' extracted_docs/${NODE}_data.json
jq '.operations_by_resource | keys' extracted_docs/${NODE}_data.json

# Show operation details
jq '.operations[] | {name, value, description, action}' extracted_docs/${NODE}_data.json
```

**What to Verify:**
- All resources detected? (e.g., Slack should have: channel, message, reaction, star, user, userGroup)
- All operations per resource extracted?
- Operations properly grouped in `operations_by_resource`?
- Each operation has `action` field? (e.g., "Create a channel")

**Count verification:**
```bash
# Source: count operation definitions
find n8n/packages/nodes-base/nodes/${NODE_NAME} -path "*/actions/*" -name "*.resource.ts" -exec cat {} \; | grep -c "name:"

# Extracted
jq '.operations | length' extracted_docs/${NODE}_data.json
```

---

#### ✅ Methods Validation (loadOptions, listSearch)

**Source Pattern:**
```typescript
methods = {
  loadOptions: {
    getUsers: async function() {...},
    getChannels: async function() {...}
  },
  listSearch: {
    searchChannels: async function() {...}
  }
}
```

**Check extracted:**
```bash
jq '.methods' extracted_docs/${NODE}_data.json
```

**Red Flags:**
- `loadOptionsMethods: ["call", "for", "push"]` ← PARSING BUG (extracted wrong identifiers)
- `loadOptionsMethods: []` when source has methods
- Missing methods that exist in source

**Correct extraction looks like:**
```json
{
  "loadOptionsMethods": ["getUsers", "getChannels", "getTables"],
  "listSearchMethods": ["searchChannels"]
}
```

---

#### ✅ Advanced Checks (For Complex Nodes)

**1. Workflow Examples**
```bash
jq '.workflow_examples | length' extracted_docs/${NODE}_data.json
```
- Should have 1+ real examples from test files
- Examples should have complete parameters, not just `{}`

**2. Dynamic Outputs**
```bash
jq '.outputs' extracted_docs/${NODE}_data.json
```
- Branching nodes (Switch, If, Merge) should show multiple outputs
- Missing outputs was a bug (now mostly fixed)

**3. Expression Patterns**
```bash
jq '.unique_expressions' extracted_docs/${NODE}_data.json
```
- Should capture real expressions from subtitle, default values
- Not just generic `={{...}}`

**4. API Information**
```bash
jq '.api_info' extracted_docs/${NODE}_data.json
```
- Base URLs extracted?
- Headers documented?
- Query params noted?

---

## Phase 4: Issue Documentation (20 minutes)

When you find a discrepancy, document it immediately.

### Issue Severity Guidelines

| Severity | Impact | Examples |
|----------|--------|----------|
| **CRITICAL** | Node completely unusable | 0 properties extracted, all credentials missing, wrong node entirely |
| **HIGH** | Major functionality lost | 50%+ properties missing, wrong types, missing entire resources |
| **MEDIUM** | Quality degraded | 20-50% properties missing, some null fields, missing metadata |
| **LOW** | Minor issues | Missing icon, missing tooltip, cosmetic problems |

### Create Issue File

**1. Determine your issue number:**
```bash
AGENT="your_agent_name"  # claude_code, gemini_cli, openai_codex
NEXT_NUM=$(printf "%03d" $(($(ls -1 issues/*/_${AGENT}_issue_*.json 2>/dev/null | wc -l) + 1)))
echo "Your next issue: _${AGENT}_issue_${NEXT_NUM}"
```

**2. Create issue file using this template:**

**File:** `issues/<severity>/_<agent>_issue_<nnn>_<short_description>.json`

```json
{
  "issue_id": "_<agent>_issue_<nnn>",
  "title": "Specific, clear title - include node name and specific problem",
  "severity": "critical|high|medium|low",
  "status": "new",
  "priority": 1,
  "metadata": {
    "created_at": "2025-11-13T16:00:00Z",
    "created_by": "<your_agent>",
    "affected_nodes": "NodeName (specify) or count (e.g., '15 versioned nodes')",
    "validation_session": "comprehensive_audit_2025-11-13",
    "related_issues": "Link to related issues if applicable"
  },
  "description": {
    "problem": "One clear sentence stating what's wrong",
    "impact": "QUANTIFIED impact with percentages/counts (e.g., 'HIGH - 25/50 properties missing (50% loss), node unusable for 3 main operations')",
    "root_cause": "Technical explanation of WHY this happens in the extraction code. Be specific about which function/pattern is failing.",
    "evidence": [
      "Line 1: Source file location and what it contains",
      "Line 2: Actual TypeScript snippet showing expected data",
      "Line 3: Extracted JSON showing actual data",
      "Line 4: Command used to verify: jq '.properties | length' ...",
      "Line 5: Quantified comparison: Expected 50, got 25",
      "Line 6: Pattern identified: All nodes with X structure affected"
    ],
    "fix_approach": "Specific technical fix with steps:\n1. Modify function _parse_properties() to handle X pattern\n2. Add detection for Y case\n3. Test with affected nodes: [list]\n4. Expected result: property count increases from 25 to 50\n5. Validation command: jq '.properties | length' after fix"
  },
  "ownership": {
    "assigned_to": null,
    "locked_by": null,
    "lock_acquired_at": null,
    "lock_expires_at": null,
    "claimed_at": null
  }
}
```

### Issue Quality Checklist

Before saving, verify your issue has:
- ✅ Quantified impact (numbers, percentages)
- ✅ Specific evidence (file paths, commands, snippets)
- ✅ Technical root cause (why extraction fails)
- ✅ Actionable fix approach (how to fix it)
- ✅ Test nodes listed (how to verify fix)
- ✅ Correct severity based on impact

### Example: High-Quality Issue

```json
{
  "issue_id": "_gemini_issue_015",
  "title": "Slack node missing 18 properties from Message resource create operation",
  "severity": "high",
  "status": "new",
  "priority": 2,
  "metadata": {
    "created_at": "2025-11-13T16:30:00Z",
    "created_by": "gemini_cli",
    "affected_nodes": "Slack (potentially other multi-resource nodes)",
    "validation_session": "comprehensive_audit_2025-11-13"
  },
  "description": {
    "problem": "Slack Message resource 'create' operation missing 18 properties including attachments, blocks, thread_ts, and other critical messaging fields",
    "impact": "HIGH - 18/43 properties missing (42% loss). Users cannot see documentation for advanced message formatting, threading, or file attachments. Reduces node usability significantly.",
    "root_cause": "Operation-specific spreads not fully resolved. The create.operation.ts exports 'description = updateDisplayOptions(displayOptions, properties)' but the extraction only captures the base properties array, not the operation-specific additions from updateDisplayOptions wrapper.",
    "evidence": [
      "Source: n8n/packages/nodes-base/nodes/Slack/v2/actions/message/create.operation.ts",
      "Source shows: const properties: INodeProperties[] = [25 property objects]",
      "Source also has: export const description = updateDisplayOptions(displayOptions, properties)",
      "Extracted: jq '.properties[] | select(.displayOptions.show.operation[] == \"create\")' slack_data.json | jq -s 'length'",
      "Result: 7 properties (expected 25)",
      "Missing properties: attachments, blocks, thread_ts, link_names, parse, reply_broadcast, unfurl_links, unfurl_media, mrkdwn, icon_emoji, icon_url, username, as_user, blocks_ui, attachments_ui, plus 3 more",
      "Grep count: grep -c 'displayName:' create.operation.ts = 25",
      "Pattern: All Slack operations affected (update, search, delete also missing properties)"
    ],
    "fix_approach": "1. Enhance _resolve_spreads() to follow updateDisplayOptions() wrapper function pattern\n2. When encountering 'export const description = updateDisplayOptions(X, properties)', parse the properties array\n3. Ensure displayOptions from the wrapper are merged with property definitions\n4. Test with: Slack (message/create), Slack (message/update), other operations\n5. Validation: jq '.properties | map(select(.displayOptions.show.operation[]? == \"create\")) | length' should show 25 not 7\n6. Expand test to other Slack resources (channel, user, etc.) to verify pattern fix works broadly"
  },
  "ownership": {
    "assigned_to": null,
    "locked_by": null,
    "lock_acquired_at": null,
    "lock_expires_at": null,
    "claimed_at": null
  }
}
```

---

## Phase 5: Pattern Analysis (10 minutes)

Look for PATTERNS across multiple nodes - these are high-impact issues.

### Pattern Identification

**Question to ask:** "Are 5+ nodes failing in the SAME way?"

Common patterns to look for:

1. **All versioned nodes missing properties**
   - Pattern: Nodes with v1/, v2/, V1/, V2/ directories
   - Check: Are properties extracted from base wrapper instead of version file?

2. **All multi-resource nodes missing operations**
   - Pattern: Nodes with actions/ directory structure
   - Check: Are operation spreads resolved?

3. **All collection fields have empty options**
   - Pattern: Any property with `type: "collection"`
   - Check: Is nested option extraction working? (Issue #026 - now fixed)

4. **All nodes missing specific metadata field**
   - Pattern: Every node or most nodes
   - Check: Is field extraction implemented for that metadata type?

### Creating Pattern Issues

When you find a pattern affecting 5+ nodes:

**Title format:** `"PATTERN: <Description affecting node category>"`

**Example:**
```
"PATTERN: All versioned nodes (20+ nodes) with v2 directories extract 0-5 properties instead of 50+"
```

**Evidence format:**
- List all affected nodes (or sample 10 if >10 affected)
- Show pattern in source structure (they all have X)
- Show pattern in extraction failure (they all result in Y)
- Estimate total impact (nodes affected × avg properties lost)

**Fix approach:**
- Should fix root cause that affects the pattern
- Should include regression test across all affected nodes

---

## Phase 6: Generate Reports (5 minutes)

After documenting all issues:

```bash
# Regenerate reports with your new issues
python3 generate_reports.py

# Verify your issues appear in reports
cat reports/EXTRACTION_ERRORS_REPORT.md | grep -A 5 "_<your_agent>_issue"

# Check issue index
cat issues/index.json | jq '.by_agent.<your_agent>'

# Log your session
python3 agent_start.py --agent <your_agent>
```

---

## Phase 7: Create Validation Summary (10 minutes)

Create file: `validation_summaries/VALIDATION_SUMMARY_<date>_<your_agent>.md`

**Note:** All validation summaries are organized in the `validation_summaries/` directory to keep the project root clean.

### Template

```markdown
# Validation Summary - <Agent Name>

**Date:** 2025-11-13
**Agent:** <your_agent>
**Session Duration:** <time>
**Sample Size:** <number> nodes analyzed

---

## Executive Summary

- **Nodes Sampled:** X nodes (Y% of total 450)
- **Issues Found:** Z issues total
  - Critical: A issues
  - High: B issues
  - Medium: C issues
  - Low: D issues
- **Patterns Identified:** P patterns affecting M+ nodes each
- **Estimated Overall Quality:** <percentage>% based on sample

---

## Top 5 Critical Findings

1. **[Issue #NNN]** Title - Affects X nodes, Y% property loss
2. **[Issue #NNN]** Title - Affects X nodes, breaks Z functionality
3. **[Issue #NNN]** Title - Pattern affecting X node category
4. **[Issue #NNN]** Title - Affects X nodes, Y impact
5. **[Issue #NNN]** Title - Affects X nodes, Y impact

---

## Patterns Discovered

### Pattern 1: <Name>
- **Affects:** X nodes
- **Symptom:** Y
- **Root Cause:** Z
- **Impact:** Quantified impact
- **Issue Reference:** #NNN

### Pattern 2: <Name>
...

---

## Sample Quality Distribution

### Excellent Extractions (>95% complete)
- **Node Name:** Property count X/X (100%), all metadata complete
- **Node Name:** Property count Y/Y (100%), complex collections handled correctly
...

### Good Extractions (80-95% complete)
- **Node Name:** Property count X/Y (Z%), minor issues only
...

### Poor Extractions (<80% complete)
- **Node Name:** Property count X/Y (Z%), major issues - [Issue #NNN]
...

### Failed Extractions (<50% complete)
- **Node Name:** Property count X/Y (Z%), critical issues - [Issue #NNN]
...

---

## Verification of Recent Fixes

### Issue #026 - Collection Nesting (Status: Fixed ✅)
- **Tested Nodes:** HttpRequest, Elasticsearch, Slack
- **Result:** All nested options extracted correctly
- **Evidence:** HttpRequest has 10 nested options (was 0)

### Issue #027 - .map() Transformations (Status: Fixed ✅)
- **Tested Nodes:** HttpRequest
- **Result:** All transformed properties extracted with correct displayOptions
- **Evidence:** HttpRequest has 10 AI properties with @tool flag (was 0)

### Issue #025 - Versioned Nodes (Status: Partial ⚠️)
- **Tested Nodes:** Notion (works), Airtable (partial), Discord (partial)
- **Result:** Mixed - some versioned nodes work, others don't
- **Evidence:** Further investigation needed

---

## Detailed Findings by Node

### Node: Slack
- **Property Count:** 111/115 (96%)
- **Operations:** 32/32 (100%)
- **Collections:** 20 collections, all with nested options ✅
- **Issues:** None found
- **Quality:** Excellent

### Node: HttpRequest
- **Property Count:** 42/44 (95%)
- **Operations:** 0 (not applicable for this node)
- **Collections:** 6 collections with 15 total nested options ✅
- **Issues:** 2 properties missing (minor)
- **Quality:** Excellent
- **Fix Verified:** Issue #026 (collections) ✅, Issue #027 (.map()) ✅

... (repeat for all sampled nodes)

---

## Recommendations

### Priority 1 (Critical - Fix Immediately)
1. **[Issue #NNN]** - Affects X nodes, Y% of extraction
   - **Why:** High impact, many nodes affected
   - **Fix Complexity:** Medium
   - **Expected Result:** Z improvement

### Priority 2 (High - Fix Soon)
...

### Priority 3 (Medium - Fix When Possible)
...

---

## Testing Commands Used

### Validation Commands
```bash
# Baseline
python3 validate_extraction.py

# Property counts
for node in slack httprequest elasticsearch; do
  echo "$node: $(jq '.properties | length' extracted_docs/${node}_data.json)"
done

# Collection nesting check
jq '.properties[] | select(.type == "collection") | {name, nested: (.options | length)}' \
  extracted_docs/httprequest_data.json
```

### Source Analysis Commands
```bash
# Find versioned nodes
find n8n/packages/nodes-base/nodes -type d -name "v[0-9]*" | head -10

# Count properties in source
grep -c "displayName:" n8n/packages/nodes-base/nodes/Slack/v2/actions/versionDescription.ts

# Compare with extracted
jq '.properties | length' extracted_docs/slack_data.json
```

---

## Statistics

- **Analysis Time:** X hours
- **Files Read:** Y source files
- **Commands Executed:** ~Z commands
- **Issues Created:** A issues
- **Evidence Snippets:** B code snippets collected
- **Cross-References:** C source-to-extraction comparisons

---

## Conclusion

Overall extraction quality is <percentage>% based on this <sample_size>-node sample. The main areas for improvement are:

1. <Top issue category>
2. <Second issue category>
3. <Third issue category>

Recent fixes (Issues #026, #027) are working well and show measurable improvement. Recommend prioritizing [specific issues] for maximum impact.

---

**Validation conducted by:** <Agent Name>
**Next recommended action:** Review and prioritize issues for fixing
```

---

## Success Criteria

Your validation is **complete** when you can answer YES to all:

- ✅ Sampled at least 35 nodes (diverse mix)?
- ✅ Cross-referenced extracted data with source TypeScript for each?
- ✅ Created issues for ALL discrepancies found (not just some)?
- ✅ Each issue has quantified impact + evidence + proposed fix?
- ✅ Identified patterns affecting multiple nodes?
- ✅ Generated reports with `python3 generate_reports.py`?
- ✅ Created validation summary document?
- ✅ Can clearly state top 3-5 problems and their impact?

---

## Pro Tips for Better Results

### 1. Use Parallel Analysis
Open multiple terminals:
- Terminal 1: Source file viewing
- Terminal 2: Extracted data inspection
- Terminal 3: Command execution

### 2. Create Helper Scripts
```bash
# Quick node analysis script
function analyze_node() {
  NODE=$1
  echo "=== $NODE ==="
  echo "Properties: $(jq '.properties | length' extracted_docs/${NODE}_data.json)"
  echo "Operations: $(jq '.operations | length' extracted_docs/${NODE}_data.json)"
  echo "Credentials: $(jq '.credentials | length' extracted_docs/${NODE}_data.json)"
}

# Use it
analyze_node slack
analyze_node httprequest
```

### 3. Evidence Collection Template
Keep a running document with:
```
Node: Slack
Source File: n8n/packages/nodes-base/nodes/Slack/v2/SlackV2.node.ts
Expected Properties: 115 (grep count)
Extracted Properties: 111 (jq count)
Discrepancy: 4 properties missing (3.5% loss)
Analysis: [notes]
Issue Created: #NNN
```

### 4. Don't Skip "Working" Nodes
Even nodes that look good may have subtle issues:
- Missing tooltips/hints
- Wrong default values
- Missing displayOptions
- Incomplete options arrays

### 5. Compare Similar Nodes
If Node A works perfectly but Node B (similar structure) fails, you've found a specific failure pattern.

---

## Common Pitfalls to Avoid

❌ **Don't:** Just count properties without checking quality
✅ **Do:** Sample individual properties for field-level issues

❌ **Don't:** Create vague issues like "some properties missing"
✅ **Do:** Quantify exactly: "18/43 properties missing (42% loss)"

❌ **Don't:** Skip source file verification
✅ **Do:** Always compare against actual TypeScript source

❌ **Don't:** Assume validation report is complete
✅ **Do:** Manual cross-reference catches issues automation misses

❌ **Don't:** Document issues without evidence
✅ **Do:** Include commands, file paths, and snippets

❌ **Don't:** Ignore patterns across multiple nodes
✅ **Do:** Create pattern issues for systemic problems

---

## Quick Reference: Essential Commands

```bash
# Navigate to project
cd "/home/tyler/Projects/N8nScraper"

# Run validation
python3 validate_extraction.py

# View validation stats
cat validation_report.json | jq '.stats'

# Count properties in extracted node
jq '.properties | length' extracted_docs/<node>_data.json

# Count properties in source
grep -c "displayName:" n8n/packages/nodes-base/nodes/<Node>/*Description*.ts

# Find node source files
find n8n/packages/nodes-base/nodes/<Node> -name "*.ts"

# Check for empty collections
jq '.properties[] | select(.type == "collection" and (.options | length) == 0) | .name' \
  extracted_docs/<node>_data.json

# Sample random nodes
ls -1 extracted_docs/*_data.json | shuf -n 10

# Generate reports
python3 generate_reports.py

# Check your issues
ls -1 issues/*/_<your_agent>_issue_*.json

# View issue details
cat issues/<severity>/_<your_agent>_issue_<nnn>_*.json | jq '.'
```

---

## Questions to Guide Your Analysis

As you analyze each node, ask:

1. **Completeness:** Does the extraction include all data from the source?
2. **Correctness:** Is the extracted data accurate and properly typed?
3. **Usability:** Would someone using this documentation understand the node?
4. **Patterns:** Have I seen this problem before in other nodes?
5. **Impact:** How many users/workflows does this issue affect?

---

## Final Checklist Before Submission

Before you consider your validation complete:

- [ ] Created 5-20+ issues (depending on findings)
- [ ] All issues saved to correct severity directories
- [ ] All issues have complete evidence sections
- [ ] All issues have quantified impact
- [ ] All issues have proposed fix approaches
- [ ] Identified 2-5 patterns affecting multiple nodes
- [ ] Ran `python3 generate_reports.py`
- [ ] Created validation summary document
- [ ] Can list top 3 problems and their root causes
- [ ] Verified recent fixes are working (Issues #026, #027)

---

**Ready? Begin your validation audit now.**

**Report back with:**
1. Number of issues found
2. Top 3 critical problems
3. Overall quality assessment
4. Recommendations for fixes
