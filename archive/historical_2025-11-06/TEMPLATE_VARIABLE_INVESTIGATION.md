# Template Variable Investigation Report

## Summary
23 extracted markdown files contain unresolved template variables (${...}) that should be resolved before documentation is finalized. These are in API endpoint URLs and expression patterns that contain function references and variable interpolations.

## Root Cause Analysis

### The Problem
Template variables appear in two contexts:

1. **API Pattern Endpoints** - Extracted from GenericFunctions.ts files, containing parameter placeholders like `${endpoint}`
2. **Expression Patterns** - Extracted from node descriptions, containing function references like `${waitingTooltip}`

The current `resolve_template_variables()` function in the extractor:
- Only handles simple variables (word characters only)
- Marks complex expressions as "(template: ...)"
- Never processes variables found in extracted API patterns
- Never processes variables found in common expression patterns

### Current Implementation

**Location:** `n8n_node_extractor.py` lines 745-796

```python
def resolve_template_variables(text: str, content: str) -> str:
    """Resolve ${VARIABLE} template references by finding const declarations"""
    if not text or '${' not in text:
        return text

    template_pattern = r'\$\{([^}]+)\}'
    matches = re.finditer(template_pattern, text)

    for match in matches:
        full_expr = match.group(0)  # ${...}
        inner_expr = match.group(1)  # Content inside ${}

        # Check if it's a simple variable (only word characters) or complex expression
        is_simple = re.match(r'^\w+$', inner_expr)

        if is_simple:
            # Try to resolve simple variable
            # ... patterns for const VAR = 'value' ...
        else:
            # Complex expression (has ., (, [, etc.) - mark as unresolvable template
            text = text.replace(full_expr, f'(template: {inner_expr})')

    return text
```

**Key Limitation:** The function only resolves simple identifiers. All 23 cases involve:
1. Function references (`${waitingTooltip}`)
2. URL parameters (`${endpoint}`)
3. Complex expressions

## Detailed Findings

### Node 1: EGOI

**File:** `extracted_docs/egoi_documentation.md`

**Unresolved Variable:** `${endpoint}`

**Where Found:**
```markdown
## API Patterns

**Common Endpoints:**
- `https://api.egoiapp.com${endpoint}`
```

**What It Should Be:**
The `endpoint` is a **parameter**, not a constant. From `GenericFunctions.ts`:

```typescript
export async function egoiApiRequest(
    this: IHookFunctions | IExecuteFunctions | ILoadOptionsFunctions,
    method: IHttpRequestMethods,
    endpoint: string,  // <-- Parameter passed at call time
    body: any = {},
    qs: IDataObject = {},
    _headers?: object,
): Promise<any> {
    // ...
    url: `https://api.egoiapp.com${endpoint}`,  // <-- Used in string interpolation
}
```

**Root Cause:**
- The extractor finds the URL string: `https://api.egoiapp.com${endpoint}`
- It attempts to resolve `${endpoint}` as a constant variable
- `endpoint` is a function parameter, not a const declaration
- Should be marked as a parameter placeholder, not left as a template variable

**Should Resolve To:**
One of these approaches:
1. Remove: Just show `https://api.egoiapp.com/[endpoint]` or similar
2. Document: `https://api.egoiapp.com/<endpoint>` - making it clear it's a parameter
3. List examples: Show actual endpoints like `/lists`, `/contacts/{id}` etc.

---

### Node 2: Twilio

**File:** `extracted_docs/twilio_documentation.md`

**Unresolved Variable:** `${endpoint}`

**Where Found:**
```markdown
## API Patterns

**Common Endpoints:**
- `https://events.twilio.com/v1/${endpoint}`
```

**What It Should Be:**
Same as EGOI - `endpoint` is a parameter in `GenericFunctions.ts`:

```typescript
export async function twilioApiRequest(
    this: IHookFunctions | IExecuteFunctions,
    method: IHttpRequestMethods,
    endpoint: string,  // <-- Parameter
    body: IDataObject,
    query?: IDataObject,
): Promise<any> {
    // ...
    uri: `https://api.twilio.com/2010-04-01/Accounts/${credentials.accountSid}${endpoint}`,
}
```

**Root Cause:**
Same as EGOI - function parameter, not a const.

---

### Node 3: GitHub

**File:** `extracted_docs/github_documentation.md`

**Unresolved Variable:** `${waitingTooltip}`

**Where Found:**
```markdown
## Common Expression Patterns

- `={{ (${waitingTooltip})($parameter, $execution.resumeUrl) }}`
```

**What It Should Be:**
`waitingTooltip` is a **function** defined in `Github.node.ts`:

```typescript
const waitingTooltip = (parameters: { operation: string }, resumeUrl: string) => {
    if (parameters?.operation === 'dispatchAndWait') {
        const message = 'Execution will continue when the following webhook URL is called: ';
        return `${message}<a href="${resumeUrl}" target="_blank">${resumeUrl}</a>`;
    }
    return '';
};
```

**How It's Used:**
```typescript
waitingNodeTooltip: `={{ (${waitingTooltip})($parameter, $execution.resumeUrl) }}`,
```

**Root Cause:**
- The function reference is captured in the expression pattern
- When resolving `${waitingTooltip}`, the extractor can't find it as a simple const
- It's a const arrow function, not a string constant
- Complex expression (contains parentheses and is a function call)

**Should Resolve To:**
Either:
1. Skip it entirely - expressions with function calls shouldn't be captured as-is
2. Document the function behavior: "Returns a tooltip for dispatchAndWait operations"
3. Show the resolved expression: Would evaluate to HTML string with resumeUrl

---

## The 23 Affected Files

From `validation_report.json`:

| File | Variable(s) | Type |
|------|-------------|------|
| egoi_documentation.md | `${endpoint}` | URL Parameter |
| twilio_documentation.md | `${endpoint}` | URL Parameter |
| github_documentation.md | `${waitingTooltip}` | Function Reference |
| twiliotrigger_documentation.md | `${endpoint}` | URL Parameter |
| wait_documentation.md | `${waitingTooltip}` | Function Reference |
| switch_documentation.md | `${configuredOutputs}` | Function/Variable |
| webhook_documentation.md | `${configuredOutputs}` | Function/Variable |
| ... (17 more) | ... | ... |

### Variable Types Breakdown

**URL Parameters** (e.g., `${endpoint}`):
- Found in API pattern extraction
- Are function parameters, not constants
- Should be documented differently

**Function References** (e.g., `${waitingTooltip}`):
- Found in expression patterns
- Are JavaScript functions, not string values
- Should not be captured as simple expressions

**Configuration References** (e.g., `${configuredOutputs}`):
- Found in UI elements
- Are computed values from node configuration
- Should not be statically resolved

## Where the Problem Occurs in the Extractor

### 1. API Pattern Extraction (Lines 353-391)

**File:** `n8n_node_extractor.py`, class `APIPatternExtractor`

```python
@staticmethod
def find_api_patterns(content: str) -> Dict[str, Any]:
    """Find API patterns in node code"""
    patterns = {
        'http_methods': set(),
        'endpoints': [],      # <-- URLs with ${...} are added here
        'headers': set(),
        'query_params': set()
    }
    
    # Find URL patterns
    urls = re.findall(r'url:\s*[\'"`]([^\'"`]+)[\'"`]', content)
    patterns['endpoints'].extend(urls)  # <-- ${endpoint} ends up here
    
    return patterns
```

**Issue:** No template variable resolution happens here. URLs are extracted as-is.

### 2. Markdown Generation (Lines 2440-2454)

**File:** `n8n_node_extractor.py`

```python
if self.api_patterns.get('endpoints'):
    md.append("**Common Endpoints:**")
    for endpoint in self.api_patterns['endpoints'][:5]:  # <-- Raw URLs written
        md.append(f"- `{endpoint}`")
```

**Issue:** The endpoints containing `${...}` are written directly without resolution.

### 3. Expression Pattern Extraction (Lines 191-282)

**File:** `n8n_node_extractor.py`, class `ExpressionExtractor`

The extractor detects patterns but doesn't realize they contain function references that shouldn't be resolved.

### 4. Template Variable Resolution (Lines 745-796)

**File:** `n8n_node_extractor.py`, function `resolve_template_variables()`

```python
if is_simple:
    # Try to resolve simple variable
    # Patterns only match: const VAR = 'value'
else:
    # Complex expression - marked as unresolvable
    text = text.replace(full_expr, f'(template: {inner_expr})')
```

**Issues:**
- Only called on some text (line 846), not on API patterns or expressions
- Only handles simple const declarations, not function declarations
- Can't resolve parameters or computed values
- Never called on `api_patterns['endpoints']` or `common_expressions`

## Why This Happens: Context Matters

The template variables serve different purposes:

| Context | Type | Should Resolve? | Reason |
|---------|------|-----------------|--------|
| `const x = '${var}'` | Literal string | Yes | It's a value that should be known at extraction time |
| `url: '${endpoint}'` in function | Function parameter | No | It's dynamic, set at runtime by callers |
| `${waitingTooltip}` in expression | Function reference | No | It's runtime JavaScript code |
| `${configuredOutputs}` in UI | Dynamic config | No | Depends on user's node configuration |

**The current code doesn't distinguish between these contexts.**

## Proposed Fix Approach

### Option 1: Smart Template Resolution (Recommended)

1. **Identify context** before resolution:
   - Is it in a function parameter? Skip it
   - Is it in a URL inside function? Mark as `<parameter>`
   - Is it a function reference? Skip it or document as `[function_name]`

2. **Update `APIPatternExtractor`**:
   ```python
   @staticmethod
   def find_api_patterns(content: str) -> Dict[str, Any]:
       # ... existing code ...
       # Find URL patterns
       urls = re.findall(r'url:\s*[\'"`]([^\'"`]+)[\'"`]', content)
       
       # Process URLs to replace parameter placeholders
       processed_urls = []
       for url in urls:
           # Replace ${param} with <param> to indicate it's a placeholder
           url = re.sub(r'\$\{(\w+)\}', r'<\1>', url)
           processed_urls.append(url)
       
       patterns['endpoints'] = processed_urls
   ```

3. **Update expression pattern handling**:
   Skip expressions that contain function calls (have `(` or `)`)

### Option 2: Documentation Approach

Add a note in the extracted documentation explaining template variables:
```markdown
**Note:** API endpoints shown above use template parameters (shown as `<param>`).
The actual endpoint depends on the specific operation being performed.
Common operations include: `/lists`, `/contacts/{id}`, etc.
```

### Option 3: Filter Out Bad Patterns

During extraction, don't include URLs that have unresolvable template variables:
```python
if '${' in url and not can_resolve_template(url):
    continue  # Skip URLs with unresolvable parameters
```

## Impact Assessment

**Current State:**
- 23 files with cosmetic template variable issues
- JSON data is clean (only markdown is affected)
- Does not impact API training (the parameter structure is still clear)
- Only affects human-readability of generated documentation

**Severity:** Low
- These are in documentation generated for humans
- The underlying JSON data is correct and can be used for AI training
- The template syntax in markdown is recognizable even unresolved

**User Impact:**
- Markdown documentation shows `${endpoint}` instead of `<endpoint>`
- Would be confusing to someone reading the docs
- But doesn't break functionality or training

## Recommended Implementation

**Priority:** Low (cosmetic issue)

**Best Approach:** Option 1 - Smart Template Resolution

**Changes Needed:**

1. **In `APIPatternExtractor.find_api_patterns()`**:
   - Add post-processing to convert `${paramName}` to `<paramName>`
   - This makes it clear these are placeholders, not variables

2. **In expression pattern handling**:
   - Filter out patterns containing function calls: `(...)` or `[...]`
   - These aren't useful extracted patterns

3. **Optional documentation**:
   - Add explanation of parameter placeholders in generated markdown

**Code Location:** `n8n_node_extractor.py` lines 353-391 and 2440-2454

**Estimated Effort:** 30 minutes to implement and test

## Examples of Fixed Output

### Before (Current)
```
**Common Endpoints:**
- `https://api.egoiapp.com${endpoint}`
```

### After (Proposed)
```
**Common Endpoints:**
- `https://api.egoiapp.com<endpoint>`
```

### Documentation (Optional)
```
**Note:** API endpoints use placeholders like `<endpoint>` for dynamic parameters
determined by the specific operation being performed.
```

## Summary

- **23 files affected** - validation report shows exact list
- **Two main causes:**
  1. Function parameters in URL strings aren't resolvable
  2. Function references in expressions shouldn't be extracted
- **Root cause:** Context-insensitive template resolution
- **Impact:** Low - cosmetic markdown issue, JSON data is correct
- **Fix:** 30-line code change in `APIPatternExtractor`
