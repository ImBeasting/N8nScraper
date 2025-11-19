# Template Variable Issue - Action Plan

## Quick Reference

| Item | Details |
|------|---------|
| **Issue** | 23 markdown files contain unresolved template variables (${...}) |
| **Root Cause** | API patterns and expressions extracted with placeholders, not resolved |
| **Severity** | Low - cosmetic only, JSON data is clean |
| **Fix Effort** | 10-30 minutes (depends on approach) |
| **Impact** | Markdown readability improvement only |

---

## The 23 Affected Files

All in `extracted_docs/` directory:

### URL Parameter Issues (13 files)
- `egoi_documentation.md` - ${endpoint}
- `twilio_documentation.md` - ${endpoint}
- `twiliotrigger_documentation.md` - ${endpoint}
- `wisetrigger_documentation.md` - ${rootUrl}, ${endpoint}
- `wise_documentation.md` - ${rootUrl}, ${endpoint}
- `formiotrigger_documentation.md` - ${base}, ${endpoint}
- `whatsapptrigger_documentation.md` - ${phoneNumberId}, ${resource}
- `whatsapp_documentation.md` - ${phoneNumberId}, ${resource}
- `seatable_trigger_documentation.md` - ${resolveBaseUri(ctx)}
- `seatabletrigger_documentation.md` - ${resolveBaseUri(ctx)}
- `unleashedsoftware_documentation.md` - ${paginatedPath}
- `pushover_documentation.md` - ${path}
- `posthog_documentation.md` - ${path}, ${base}

### Function Reference Issues (7 files)
- `github_documentation.md` - ${waitingTooltip}
- `wait_documentation.md` - ${waitingTooltip}
- `switch_documentation.md` - ${configuredOutputs}
- `webhook_documentation.md` - ${configuredOutputs}
- `mistralai_documentation.md` - ${resource}
- `jwt_documentation.md` - ${prettifyOperation}
- `respondtowebhook_documentation.md` - ${configuredOutputs}

### Complex Expression Issues (3 files)
- `httprequest_documentation.md` - ${pagination.completeExpression.trim().slice(3, -2)}
- `http_request_documentation.md` - ${pagination.completeExpression.trim().slice(3, -2)}
- `elasticsearch_documentation.md` - ${baseUrl.replace(/\\/$/, '\n  - ...)}

---

## Implementation Roadmap

### Step 1: Understand the Problem (Done)
- Read: `TEMPLATE_VARIABLE_INVESTIGATION.md` (comprehensive analysis)
- Read: `TEMPLATE_VARIABLE_SUMMARY.md` (quick overview)
- Read: `TEMPLATE_VARIABLE_CODE_EXAMPLES.md` (side-by-side examples)

### Step 2: Choose Implementation Approach

**Option A: Quick Fix (10 minutes)**
- Just replace `${param}` with `<param>` in endpoints
- Minimal change, immediate improvement
- Best for: "just make it look better"

**Option B: Better Fix (30 minutes)**
- Replace parameters with `<param>` format
- Filter out function reference expressions
- Add documentation notes
- Best for: "do it right"

**Option C: Comprehensive Fix (1 hour)**
- Include parameter tracking in API patterns
- Document parameter usage
- Update expression filtering
- Add validation
- Best for: "production quality"

### Step 3: Implementation

#### If choosing Option A (Quick Fix):
1. Open `n8n_node_extractor.py`
2. Find `APIPatternExtractor.find_api_patterns()` (line 353)
3. Add this after line 372:
   ```python
   # Replace ${param} with <param>
   processed_urls = []
   for url in urls:
       url = re.sub(r'\$\{(\w+)\}', r'<\1>', url)
       processed_urls.append(url)
   patterns['endpoints'] = processed_urls
   ```
4. Test with: `python3 n8n_node_extractor.py extract egoi`
5. Verify: Check extracted_docs/egoi_documentation.md has `<endpoint>` not `${endpoint}`

#### If choosing Option B (Better Fix):
1. Same as Option A, plus:
2. Find `ExpressionExtractor.find_expressions()` (line 191)
3. Add filter: Skip patterns with `(` or `)` (function calls)
4. Add note to markdown output about placeholders
5. Test with 3 nodes from each category
6. Regenerate all docs: `python3 n8n_node_extractor.py extract-all`

#### If choosing Option C (Comprehensive):
1. Create new function: `resolve_api_parameters()`
2. Track parameter usage in APIPatternExtractor
3. Output parameter documentation
4. Add validation tests
5. Full extraction and validation

### Step 4: Testing

After implementation, test:

```bash
# Test single node extraction
python3 n8n_node_extractor.py extract Egoi

# Check the output
grep -n "\${" extracted_docs/egoi_documentation.md
# Should show 0 results (variables resolved)

# Test other nodes
python3 n8n_node_extractor.py extract Twilio
python3 n8n_node_extractor.py extract Github

# Validate all
python3 validate_extraction.py

# Check template variable count decreased
jq '.stats.template_variables' validation_report.json
```

### Step 5: Regenerate Documentation

After fix is working:

```bash
# Full extraction with fix
python3 n8n_node_extractor.py extract-all

# Validate
python3 validate_extraction.py

# Check results
jq '.stats' validation_report.json
```

Expected: `"template_variables": 0` (or significant reduction)

---

## File Locations Reference

### Source File to Modify
```
/media/tyler/fastraid/Projects/n8n Node Scrapper/n8n_node_extractor.py
```

**Key Functions:**
- `APIPatternExtractor.find_api_patterns()` - Line 353-391
- `ExpressionExtractor.find_expressions()` - Line 191-282
- Markdown output - Line 2440-2454
- Template resolution - Line 745-796

### Documentation Generated
```
TEMPLATE_VARIABLE_INVESTIGATION.md      - Comprehensive analysis
TEMPLATE_VARIABLE_SUMMARY.md             - Quick reference
TEMPLATE_VARIABLE_CODE_EXAMPLES.md       - Code side-by-side
TEMPLATE_VARIABLE_ACTION_PLAN.md         - This file
```

### Affected Output Files
```
extracted_docs/egoi_documentation.md
extracted_docs/twilio_documentation.md
extracted_docs/github_documentation.md
... (20 more files)
```

### Validation Reports
```
validation_report.json                   - Current state (23 issues)
```

---

## Code Changes Checklist

- [ ] Backup original file: `cp n8n_node_extractor.py n8n_node_extractor.py.backup`
- [ ] Choose implementation approach (A, B, or C)
- [ ] Make code changes
- [ ] Test single node extraction
- [ ] Fix any issues
- [ ] Test multiple nodes from different categories
- [ ] Run full extraction: `extract-all`
- [ ] Run validation: `validate_extraction.py`
- [ ] Review validation_report.json
- [ ] Verify template_variables count decreased
- [ ] Git commit: `git add -A && git commit -m "Fix template variable resolution in API patterns"`

---

## Success Criteria

### Option A (Quick Fix)
✓ `${param}` converted to `<param>` in all endpoints
✓ Markdown files now show `<endpoint>` instead of `${endpoint}`
✓ validation_report.json shows reduced template_variable count

### Option B (Better Fix)
✓ All from Option A, plus:
✓ Function reference expressions removed
✓ Documentation note added about placeholders
✓ All 23 files have resolved variables
✓ validation_report.json shows 0 template_variables (or close)

### Option C (Comprehensive)
✓ All from Option B, plus:
✓ Parameter tracking in API patterns
✓ Parameter documentation in markdown
✓ Validation test cases pass
✓ Code review ready

---

## Decision Matrix

| Need | Approach | Time | Complexity | Quality |
|------|----------|------|-----------|---------|
| Quick improvement | A | 10 min | Low | Good |
| Proper fix | B | 30 min | Medium | Excellent |
| Production ready | C | 1 hour | High | Production |

**Recommendation:** Option B (Better Fix)
- Takes 30 minutes
- Fixes root issues properly
- Improves documentation quality
- Cleanest solution

---

## Next Steps

1. **Decide** which approach to use
2. **Read** the relevant example file (`TEMPLATE_VARIABLE_CODE_EXAMPLES.md`)
3. **Backup** the original file
4. **Implement** the fix
5. **Test** with sample nodes
6. **Validate** the extraction
7. **Commit** the changes
8. **Document** what was fixed (update this file)

---

## Questions & Answers

**Q: Why is this a problem?**
A: It's not a critical problem - the JSON data is fine. It just makes the markdown documentation look unpolished when someone reads it.

**Q: Will this break anything?**
A: No. The fix is additive - we're just improving how template variables are displayed, not changing the core extraction logic.

**Q: How much impact?**
A: Low impact - only affects markdown readability. JSON used for AI training is unaffected.

**Q: How many files affected?**
A: 23 files out of 450 (5% of extracted documentation).

**Q: Can it wait?**
A: Yes, it's low priority. But it's a quick fix, so might as well do it.

**Q: What if I break something?**
A: Backup the file first. Also, you can just revert with: `git checkout n8n_node_extractor.py`

---

## Quick Start for Implementation

### Quick Fix (Recommended if pressed for time)
```bash
# 1. Backup
cp n8n_node_extractor.py n8n_node_extractor.py.backup

# 2. Edit file (add 5 lines in APIPatternExtractor.find_api_patterns)
# See TEMPLATE_VARIABLE_CODE_EXAMPLES.md for exact code

# 3. Test
python3 n8n_node_extractor.py extract Egoi

# 4. Verify
grep "\${" extracted_docs/egoi_documentation.md  # Should be empty

# 5. Full extraction
python3 n8n_node_extractor.py extract-all

# 6. Validate
python3 validate_extraction.py
jq '.stats.template_variables' validation_report.json

# 7. Commit
git add -A && git commit -m "Fix: Replace template variable placeholders with <param> format"
```

---

**Status:** Ready for implementation
**Last Updated:** 2025-11-07
**Documentation:** Complete and comprehensive

