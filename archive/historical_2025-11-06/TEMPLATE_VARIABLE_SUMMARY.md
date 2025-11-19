# Template Variable Issue - Quick Summary

## The Issue in 30 Seconds

23 markdown documentation files contain template variables that weren't resolved:

```
Before:  https://api.egoiapp.com${endpoint}
After:   https://api.egoiapp.com<endpoint>  (or better documentation)
```

## What's Affected

### By Node Type:
- **EGOI** - `${endpoint}` in API endpoints
- **Twilio** - `${endpoint}` in API endpoints  
- **GitHub** - `${waitingTooltip}` in expressions
- **... 20 more nodes** (see full report)

### By Variable Type:
| Type | Count | Examples |
|------|-------|----------|
| URL Parameters | ~13 | `${endpoint}`, `${rootUrl}`, `${path}` |
| Function References | ~7 | `${waitingTooltip}`, `${configuredOutputs}` |
| Complex Expressions | ~3 | Function calls, method chains |

## Why It Happens

The extractor captures template syntax from 3 sources:

1. **API GenericFunctions.ts** - Function parameters like:
   ```typescript
   url: `https://api.example.com${endpoint}`  // endpoint is a parameter
   ```

2. **Expression Patterns** - Function references like:
   ```typescript
   waitingNodeTooltip: `={{ (${waitingTooltip})($parameter, ...) }}`
   ```

3. **UI Elements** - Dynamic values:
   ```typescript
   description: `${configuredOutputs}`  // Computed from node config
   ```

## Root Cause

The `resolve_template_variables()` function (line 745) only:
- ✓ Resolves simple variable names: `const x = 'value'`
- ✗ Doesn't handle function parameters: `${endpoint}`
- ✗ Doesn't handle function references: `${waitingTooltip}`
- ✗ Never called on API patterns or expressions

**Result:** Template variables appear unresolved in markdown output

## Impact

| Aspect | Status |
|--------|--------|
| **JSON Data** | ✓ Clean (unaffected) |
| **API Training** | ✓ Works fine (parameter structure clear) |
| **Markdown Readability** | ✗ Shows `${...}` instead of proper format |
| **Severity** | Low - cosmetic issue only |

## The Fix

### Quick Fix (10 minutes)
Replace `${param}` with `<param>` in endpoints:
```python
# In APIPatternExtractor.find_api_patterns()
url = re.sub(r'\$\{(\w+)\}', r'<\1>', url)
```

### Better Fix (30 minutes)
1. Convert parameters to `<param>` format
2. Filter out function reference expressions
3. Add documentation note about placeholders

### Code Locations
- **API Extraction:** `n8n_node_extractor.py` lines 353-391
- **Markdown Output:** `n8n_node_extractor.py` lines 2440-2454
- **Template Resolution:** `n8n_node_extractor.py` lines 745-796

## Examples

### EGOI Node
```
Current:  https://api.egoiapp.com${endpoint}
Fixed:    https://api.egoiapp.com<endpoint>

(endpoint is a dynamic parameter passed at runtime)
```

### Twilio Node
```
Current:  https://events.twilio.com/v1/${endpoint}
Fixed:    https://events.twilio.com/v1/<endpoint>

(endpoint is a dynamic parameter passed at runtime)
```

### GitHub Node
```
Current:  ={{ (${waitingTooltip})($parameter, $execution.resumeUrl) }}
Fixed:    (Removed - this is a function call, not a valid expression pattern)

or

Fixed:    A tooltip function that displays webhook URL for dispatchAndWait operations
```

## Next Steps

1. ✓ **Investigation complete** - Full report in `TEMPLATE_VARIABLE_INVESTIGATION.md`
2. → **Decide approach** - Quick fix vs. Better fix
3. → **Implement fix** - ~30 minutes work
4. → **Test** - Re-extract 3 nodes and validate
5. → **Regenerate** - Run full extraction with fix applied

## Files Involved

- Source: `/media/tyler/fastraid/Projects/n8n Node Scrapper/n8n_node_extractor.py`
- Analysis: `/media/tyler/fastraid/Projects/n8n Node Scrapper/TEMPLATE_VARIABLE_INVESTIGATION.md`
- Affected: 23 files in `extracted_docs/` (see validation report)

---

**Priority:** Low (cosmetic) | **Effort:** 30 min | **Complexity:** Low
