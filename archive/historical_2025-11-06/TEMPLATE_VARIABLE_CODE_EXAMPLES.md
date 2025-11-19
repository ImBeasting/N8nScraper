# Template Variable Issue - Code Examples

## Example 1: EGOI API Parameter

### Source Code (GenericFunctions.ts)
```typescript
export async function egoiApiRequest(
    this: IHookFunctions | IExecuteFunctions | ILoadOptionsFunctions,
    method: IHttpRequestMethods,
    endpoint: string,              // <-- Function parameter
    body: any = {},
    qs: IDataObject = {},
    _headers?: object,
): Promise<any> {
    const credentials = await this.getCredentials('egoiApi');
    
    const options: IRequestOptions = {
        headers: {
            accept: 'application/json',
        },
        qs,
        body,
        url: `https://api.egoiapp.com${endpoint}`,  // <-- Uses parameter
        json: true,
    };
    
    // ... rest of function
}
```

### Extracted Markdown (Current - Wrong)
```markdown
## API Patterns

**Common Endpoints:**
- `https://api.egoiapp.com${endpoint}`
```

### Issue
- `endpoint` is a **function parameter**, not a const declaration
- It gets its value from function calls like: `egoiApiRequest(..., '/lists', ...)`
- Cannot be resolved at extraction time
- Should be marked as a placeholder

### Extracted Markdown (Fixed - Option A)
```markdown
## API Patterns

**Common Endpoints:**
- `https://api.egoiapp.com<endpoint>`

*Note: `<endpoint>` is a dynamic parameter. Examples: `/lists`, `/contacts/{id}`, etc.*
```

### Extracted Markdown (Fixed - Option B)
```markdown
## API Patterns

**HTTP Methods:** GET, POST, PUT, DELETE, PATCH

**Common Endpoint Pattern:** `https://api.egoiapp.com/`

**Parameters:**
- `endpoint` - The specific API endpoint path (e.g., `/lists`, `/contacts/{id}`)
```

---

## Example 2: Twilio API Parameter

### Source Code (GenericFunctions.ts)
```typescript
export async function twilioApiRequest(
    this: IHookFunctions | IExecuteFunctions,
    method: IHttpRequestMethods,
    endpoint: string,                  // <-- Function parameter
    body: IDataObject,
    query?: IDataObject,
): Promise<any> {
    const credentials = await this.getCredentials<{
        accountSid: string;
        authType: 'authToken' | 'apiKey';
        authToken: string;
        apiKeySid: string;
        apiKeySecret: string;
    }>('twilioApi');
    
    const options: IHttpRequestOptions = {
        form: body,
        qs: query,
        uri: `https://api.twilio.com/2010-04-01/Accounts/${credentials.accountSid}${endpoint}`,
        json: true,
    };
    
    return await this.helpers.requestWithAuthentication.call(this, 'twilioApi', options);
}
```

### Extracted Markdown (Current - Wrong)
```markdown
## API Patterns

**Common Endpoints:**
- `https://events.twilio.com/v1/${endpoint}`
```

### Issue
- `endpoint` is a function parameter (like EGOI)
- Additional parameter `${credentials.accountSid}` in the actual URL
- Extractor only finds the second part of the URL
- Cannot resolve dynamic parameters

### Extracted Markdown (Fixed)
```markdown
## API Patterns

**Base URL:** `https://api.twilio.com/2010-04-01/Accounts/{accountSid}/`

**Endpoint Parameter:** The specific resource endpoint is passed as a parameter
- Examples: `/Messages`, `/Calls`, `/Addresses`

*Note: Actual endpoints depend on the operation being performed*
```

---

## Example 3: GitHub Function Reference

### Source Code (Github.node.ts)
```typescript
const waitingTooltip = (parameters: { operation: string }, resumeUrl: string) => {
    if (parameters?.operation === 'dispatchAndWait') {
        const message = 'Execution will continue when the following webhook URL is called: ';
        return `${message}<a href="${resumeUrl}" target="_blank">${resumeUrl}</a>`;
    }
    
    return '';
};

export class Github implements INodeType {
    description: INodeTypeDescription = {
        displayName: 'GitHub',
        name: 'github',
        // ... other fields ...
        defaults: {
            name: 'GitHub',
        },
        usableAsTool: true,
        inputs: [NodeConnectionTypes.Main],
        outputs: [NodeConnectionTypes.Main],
        waitingNodeTooltip: `={{ (${waitingTooltip})($parameter, $execution.resumeUrl) }}`,
        // ... more fields ...
    };
}
```

### Extracted Expression Pattern (Current - Wrong)
```markdown
## Common Expression Patterns

- `={{ (${waitingTooltip})($parameter, $execution.resumeUrl) }}`
```

### Issue
- `${waitingTooltip}` is a **function reference**, not a variable
- It's meant to be evaluated at runtime in n8n's expression system
- The expression calls the function with parameters
- Should not be extracted as a simple expression pattern
- This isn't a pattern to use, it's framework-internal logic

### Solution
Either **remove it entirely** (best), or **document what it does**:

```markdown
## Node Behavior

**Waiting Node Tooltip:**
The node displays a tooltip when waiting for webhook execution:
- For 'dispatchAndWait' operations: Shows the resume URL that must be called to continue
- For other operations: No special tooltip

The tooltip is generated dynamically based on the operation type and resume URL.
```

---

## Example 4: Switch Node Configuration Reference

### Source Code
```typescript
// From some UI element or property
description: `${configuredOutputs}`  // or similar
```

### Issue
- `${configuredOutputs}` refers to a computed property from node configuration
- Not a const variable or function
- Its value depends on what the user has configured
- Cannot be resolved at extraction time

### Extracted Markdown (Current - Wrong)
```markdown
- `{{ $node["Switch"].json.configuredOutputs }}`
```

### Extracted Markdown (Fixed)
```markdown
This node dynamically creates outputs based on its configuration.
The number and names of outputs depend on the conditions you configure.
```

---

## Extractor Code Locations

### Problem Area 1: APIPatternExtractor (Lines 353-391)
```python
class APIPatternExtractor:
    @staticmethod
    def find_api_patterns(content: str) -> Dict[str, Any]:
        """Find API patterns in node code"""
        patterns = {
            'http_methods': set(),
            'endpoints': [],      # <-- Raw URLs added here
            'headers': set(),
            'query_params': set()
        }
        
        # Find URL patterns - extracts with ${...} as-is
        urls = re.findall(r'url:\s*[\'"`]([^\'"`]+)[\'"`]', content)
        patterns['endpoints'].extend(urls)  # <-- No template resolution
        
        return patterns
```

### Problem Area 2: Markdown Output (Lines 2440-2454)
```python
if self.api_patterns.get('endpoints'):
    md.append("**Common Endpoints:**")
    for endpoint in self.api_patterns['endpoints'][:5]:
        md.append(f"- `{endpoint}`")  # <-- Writes ${...} as-is
```

### Problem Area 3: Template Resolution (Lines 745-796)
```python
@staticmethod
def resolve_template_variables(text: str, content: str) -> str:
    """Resolve ${VARIABLE} template references"""
    # ... code ...
    
    is_simple = re.match(r'^\w+$', inner_expr)  # <-- Only word characters
    
    if is_simple:
        # Try to resolve as const
        # Patterns only match: const VAR = 'value'
    else:
        # Everything else marked as unresolvable
        text = text.replace(full_expr, f'(template: {inner_expr})')
```

---

## Fix Implementation Example

### Quick Fix (10 minutes)
```python
# Add this to APIPatternExtractor.find_api_patterns()

# Process URLs to replace parameter placeholders
processed_urls = []
for url in urls:
    # Replace ${param} with <param> to indicate it's a placeholder
    url = re.sub(r'\$\{(\w+)\}', r'<\1>', url)
    processed_urls.append(url)

patterns['endpoints'] = processed_urls
```

### Better Fix (30 minutes)
```python
# In APIPatternExtractor
@staticmethod
def find_api_patterns(content: str) -> Dict[str, Any]:
    """Find API patterns in node code"""
    patterns = {
        'http_methods': set(),
        'endpoints': [],
        'headers': set(),
        'query_params': set(),
        'dynamic_params': set()  # <-- NEW: Track dynamic parameters
    }
    
    # Find URL patterns
    urls = re.findall(r'url:\s*[\'"`]([^\'"`]+)[\'"`]', content)
    
    for url in urls:
        # Extract template variables
        templates = re.findall(r'\$\{(\w+)\}', url)
        patterns['dynamic_params'].update(templates)
        
        # Replace with placeholders
        clean_url = re.sub(r'\$\{(\w+)\}', r'<\1>', url)
        patterns['endpoints'].append(clean_url)
    
    # ... rest of function ...
    return patterns
```

---

## Before/After Comparison

| Node | Before | After |
|------|--------|-------|
| **EGOI** | `https://api.egoiapp.com${endpoint}` | `https://api.egoiapp.com<endpoint>` |
| **Twilio** | `https://events.twilio.com/v1/${endpoint}` | `https://events.twilio.com/v1/<endpoint>` |
| **GitHub (expressions)** | `` ={{ (${waitingTooltip})($parameter, ...) }}`` | *Removed - not a valid pattern* |
| **Switch** | `{{ ${configuredOutputs} }}` | *Documented as dynamic output* |

---

## Summary of Issues by Category

### Cannot Resolve - Function Parameters
- `endpoint` in URL strings
- `rootUrl`, `path`, `phoneNumberId` in endpoint templates
- **Action:** Replace with `<param>` format or filter out

### Cannot Resolve - Function References  
- `waitingTooltip` - function that returns HTML
- `configuredOutputs` - computed property
- `prettifyOperation` - utility function
- **Action:** Remove from expressions or document functionality

### Cannot Resolve - Complex Expressions
- `${pagination.completeExpression.trim().slice(3, -2)}`
- Method chains and function calls
- **Action:** These should be filtered out during extraction

---

## Validation Test Cases

After implementing fix, test these cases:

### Test 1: Simple Parameter Replacement
```typescript
url: `https://api.example.com${endpoint}`
```
Expected output: `https://api.example.com<endpoint>`

### Test 2: Multiple Parameters
```typescript
url: `https://api.example.com/${accountId}${endpoint}`
```
Expected output: `https://api.example.com/<accountId><endpoint>`

### Test 3: Function Reference (Should be Filtered)
```typescript
description: `{{ ${functionName}() }}`
```
Expected: Filtered out (not in endpoints list)

### Test 4: Complex Expression (Should be Filtered)
```typescript
value: `${obj.method().field}`
```
Expected: Filtered out (not a simple parameter)

---

**Related Documentation:**
- `/media/tyler/fastraid/Projects/n8n Node Scrapper/TEMPLATE_VARIABLE_INVESTIGATION.md` - Full analysis
- `/media/tyler/fastraid/Projects/n8n Node Scrapper/TEMPLATE_VARIABLE_SUMMARY.md` - Quick summary
- `validation_report.json` - List of 23 affected files
- `n8n_node_extractor.py` - Source code (lines 353-391, 745-796, 2440-2454)
