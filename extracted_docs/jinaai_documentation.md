---
title: "Node: Jina AI"
slug: "node-jinaai"
version: "1"
updated: "2026-01-08"
summary: "Interact with Jina AI API"
node_type: "regular"
group: "['transform']"
---

# Node: Jina AI

**Purpose.** Interact with Jina AI API
**Subtitle.** ={{ $parameter["operation"] + ": " + $parameter["resource"] }}


---

## Node Details

- **Icon:** `{'light': 'file:jinaAi.svg', 'dark': 'file:jinaAi.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **jinaAiApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `jinaAiApi` | ✓ | - |

---

## Operations

### Reader Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Research Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | reader | ✗ | Resource to operate on |  |

**Resource options:**

* **Reader** (`reader`)
* **Research** (`research`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | reader | ✗ |  |  |

**Resource options:**

* **Reader** (`reader`)
* **Research** (`research`)

| Operation | `operation` | options | read | ✗ | Fetches content from a URL and converts it to clean, LLM-friendly formats |  |
| Operation | `operation` | options | deepResearch | ✗ | Research a topic and generate a structured research report |  |
| URL | `url` | string |  | ✓ | The URL to fetch content from | e.g. https://jina.ai/ | url |
| Simplify | `simplify` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Specify desired output format | e.g. Add Option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Output Format | `outputFormat` | options |  | Specify desired output format |
| Target CSS Selector | `targetSelector` | string |  | CSS selector to focus on specific page elements |
| Exclude CSS Selector | `excludeSelector` | string |  | CSS selector for elements to exclude |
| Enable Image Captioning | `enableImageCaptioning` | boolean | False | Whether to generate captions for images within the content |
| Wait for CSS Selector | `waitForSelector` | string |  | Wait for a specific element to appear before extracting content (for dynamic pages) |

</details>

| Search Query | `searchQuery` | string |  | ✓ | e.g. e.g. Jina AI |  |
| Simplify | `simplify` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Specify desired output format | e.g. Add Option | min:1, max:∞ |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Output Format | `outputFormat` | options |  | Specify desired output format |
| Site Filter | `siteFilter` | string |  | Restrict search to specific websites |
| Page Number | `pageNumber` | number |  | The page number of the search results to retrieve |

</details>

| Research Query | `researchQuery` | string |  | ✓ | The topic or question for the AI to research | e.g. e.g. Analyze the impact of renewable energy sources on climate change mitigation |  |
| Simplify | `simplify` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | The maximum number of URLs to include in the final answer | e.g. Add Option | min:1, max:∞ |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Max Returned Sources | `maxReturnedSources` | number |  | The maximum number of URLs to include in the final answer |
| Prioritize Sources | `prioritizeSources` | string |  | A list of domains that are given a higher priority for content retrieval |
| Exclude Sources | `excludeSources` | string |  | A list of domains to be strictly excluded from content retrieval |
| Site Filter | `siteFilter` | string |  | Restrict search to specific websites |

</details>


---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: No options

**From workflow:** Jina AI -> Reader -> Search

**Parameters:**
```json
{
  "operation": "search",
  "searchQuery": "Jina AI",
  "simplify": false,
  "options": {},
  "requestOptions": {}
}
```

**Credentials:**
- jinaAiApi: `Jina AI account`

### Example 2: With options

**From workflow:** Jina AI -> Reader -> Search

**Parameters:**
```json
{
  "operation": "search",
  "searchQuery": "Jina AI",
  "simplify": false,
  "options": {
    "outputFormat": "markdown",
    "siteFilter": "jina.ai",
    "pageNumber": 2
  },
  "requestOptions": {}
}
```

**Credentials:**
- jinaAiApi: `Jina AI account`

### Example 3: Simplified

**From workflow:** Jina AI -> Reader -> Search

**Parameters:**
```json
{
  "operation": "search",
  "searchQuery": "Jina AI",
  "options": {},
  "requestOptions": {}
}
```

**Credentials:**
- jinaAiApi: `Jina AI account`

### Example 4: No options

**From workflow:** Jina AI -> Reader -> Read

**Parameters:**
```json
{
  "url": "https://first.com/some/path",
  "simplify": false,
  "options": {},
  "requestOptions": {}
}
```

**Credentials:**
- jinaAiApi: `Jina AI account`

### Example 5: With options

**From workflow:** Jina AI -> Reader -> Read

**Parameters:**
```json
{
  "url": "https://second.com/other?foo=bar",
  "simplify": false,
  "options": {
    "outputFormat": "markdown",
    "targetSelector": "article",
    "excludeSelector": ".ad",
    "enableImageCaptioning": true,
    "waitForSelector": "#posts"
  },
  "requestOptions": {}
}
```

**Credentials:**
- jinaAiApi: `Jina AI account`


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter["searchQuery"] }}`
- `={{ $responseItem["choices"][0]["message"]["content"] }}`
- `={{ $parameter["operation"] + ": " + $parameter["resource"] }}`
- `={{ $parameter["options"]["enableImageCaptioning"] }}`
- `={{ $responseItem["usage"] }}`
- `={{ $parameter["options"]["siteFilter"] }}`
- `={{ $parameter["options"]["pageNumber"] }}`
- `={{ $parameter["options"]["excludeSources"].split(/,\\s*/) }}`
- `={{ $responseItem["choices"][0]["message"]["annotations"] }}`
- `={{ $parameter["options"]["waitForSelector"] }}`

---

## Execution Settings

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |
| Always Output Data | `alwaysOutputData` | boolean | False | If active, will output a single, empty item when the output would have been empty. Use to prevent the workflow finishing on this node |
| Execute Once | `executeOnce` | boolean | False | If active, the node executes only once, with data from the first item it receives |
| Retry On Fail | `retryOnFail` | boolean | False | If active, the node tries to execute again when it fails |
| Max. Tries | `maxTries` | number | 3 | Number of times to attempt to execute the node before failing the execution *(Only visible when 'Retry On Fail' is enabled)* (min: 2, max: 5) |
| Wait Between Tries (ms) | `waitBetweenTries` | number | 1000 | How long to wait between each attempt (in milliseconds) *(Only visible when 'Retry On Fail' is enabled)* (min: 0, max: 5000) |
| On Error | `onError` | options | stopWorkflow | Action to take when the node execution fails |

**On Error Options:**

* **Stop Workflow** (`stopWorkflow`) — Halt execution and fail workflow
* **Continue** (`continueRegularOutput`) — Pass error message as item in regular output
* **Continue (using error output)** (`continueErrorOutput`) — Pass item to an extra `error` output

---

## Notes & Caveats

* This node is part of n8n-nodes-base
* Categories: Miscellaneous

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: jinaAi
displayName: Jina AI
description: Interact with Jina AI API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: jinaAiApi
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: reader
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: reader
      name: Reader
      description: ''
    - value: research
      name: Research
      description: ''
- id: operation
  name: Operation
  type: options
  default: read
  required: false
  description: Fetches content from a URL and converts it to clean, LLM-friendly formats
  validation: &id001
    displayOptions:
      show:
        resource:
        - research
  typeInfo: &id002
    type: options
    displayName: Operation
    name: operation
    possibleValues: []
- id: operation
  name: Operation
  type: options
  default: deepResearch
  required: false
  description: Research a topic and generate a structured research report
  validation: *id001
  typeInfo: *id002
- id: url
  name: URL
  type: string
  default: ''
  required: true
  description: The URL to fetch content from
  placeholder: https://jina.ai/
  validation:
    required: true
    format: url
    displayOptions:
      show:
        resource:
        - reader
        operation:
        - read
  typeInfo:
    type: string
    displayName: URL
    name: url
- id: simplify
  name: Simplify
  type: boolean
  default: true
  required: false
  description: Whether to return a simplified version of the response instead of the
    raw data
  validation: &id003
    displayOptions:
      show:
        resource:
        - research
        operation:
        - deepResearch
  typeInfo: &id004
    type: boolean
    displayName: Simplify
    name: simplify
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Specify desired output format
  placeholder: Add Option
  validation: &id005
    displayOptions:
      show:
        resource:
        - research
        operation:
        - deepResearch
  typeInfo: &id006
    type: collection
    displayName: Options
    name: options
    typeOptions:
      minValue: 1
      numberPrecision: 0
    subProperties:
    - displayName: Max Returned Sources
      name: maxReturnedSources
      type: number
      description: The maximum number of URLs to include in the final answer
      placeholder: e.g. 5
      default: ''
      typeOptions:
        minValue: 1
        numberPrecision: 0
    - displayName: Prioritize Sources
      name: prioritizeSources
      type: string
      description: A list of domains that are given a higher priority for content
        retrieval
      placeholder: e.g. jina.ai, github.com
      default: ''
    - displayName: Exclude Sources
      name: excludeSources
      type: string
      description: A list of domains to be strictly excluded from content retrieval
      placeholder: e.g. jina.ai, github.com
      default: ''
    - displayName: Site Filter
      name: siteFilter
      type: string
      description: Restrict search to specific websites
      placeholder: e.g. jina.ai, github.com
      default: ''
- id: searchQuery
  name: Search Query
  type: string
  default: ''
  required: true
  description: ''
  placeholder: e.g. Jina AI
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - reader
        operation:
        - search
  typeInfo:
    type: string
    displayName: Search Query
    name: searchQuery
- id: simplify
  name: Simplify
  type: boolean
  default: true
  required: false
  description: Whether to return a simplified version of the response instead of the
    raw data
  validation: *id003
  typeInfo: *id004
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Specify desired output format
  placeholder: Add Option
  validation: *id005
  typeInfo: *id006
- id: researchQuery
  name: Research Query
  type: string
  default: ''
  required: true
  description: The topic or question for the AI to research
  placeholder: e.g. Analyze the impact of renewable energy sources on climate change
    mitigation
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - research
        operation:
        - deepResearch
  typeInfo:
    type: string
    displayName: Research Query
    name: researchQuery
    typeOptions:
      rows: 2
- id: simplify
  name: Simplify
  type: boolean
  default: true
  required: false
  description: Whether to return a simplified version of the response instead of the
    raw data
  validation: *id003
  typeInfo: *id004
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: The maximum number of URLs to include in the final answer
  placeholder: Add Option
  validation: *id005
  typeInfo: *id006
examples:
- name: No options
  parameters:
    operation: search
    searchQuery: Jina AI
    simplify: false
    options: {}
    requestOptions: {}
  workflow: Jina AI -> Reader -> Search
- name: With options
  parameters:
    operation: search
    searchQuery: Jina AI
    simplify: false
    options:
      outputFormat: markdown
      siteFilter: jina.ai
      pageNumber: 2
    requestOptions: {}
  workflow: Jina AI -> Reader -> Search
- name: Simplified
  parameters:
    operation: search
    searchQuery: Jina AI
    options: {}
    requestOptions: {}
  workflow: Jina AI -> Reader -> Search
common_expressions:
- ={{ $parameter["searchQuery"] }}
- ={{ $responseItem["choices"][0]["message"]["content"] }}
- '={{ $parameter["operation"] + ": " + $parameter["resource"] }}'
- ={{ $parameter["options"]["enableImageCaptioning"] }}
- ={{ $responseItem["usage"] }}
- ={{ $parameter["options"]["siteFilter"] }}
- ={{ $parameter["options"]["pageNumber"] }}
- ={{ $parameter["options"]["excludeSources"].split(/,\\s*/) }}
- ={{ $responseItem["choices"][0]["message"]["annotations"] }}
- ={{ $parameter["options"]["waitForSelector"] }}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: url
    text: https://jina.ai/
  - field: options
    text: Add Option
  - field: searchQuery
    text: e.g. Jina AI
  - field: options
    text: Add Option
  - field: researchQuery
    text: e.g. Analyze the impact of renewable energy sources on climate change mitigation
  - field: options
    text: Add Option
  hints: []
settings:
  common:
    notes:
      name: Notes
      field_id: notes
      type: string
      default: ''
      description: Optional note to save with the node
    notesInFlow:
      name: Display Note in Flow?
      field_id: notesInFlow
      type: boolean
      default: false
      description: If active, the note above will display in the flow as a subtitle
  executable:
    alwaysOutputData:
      name: Always Output Data
      field_id: alwaysOutputData
      type: boolean
      default: false
      description: If active, will output a single, empty item when the output would
        have been empty. Use to prevent the workflow finishing on this node
    executeOnce:
      name: Execute Once
      field_id: executeOnce
      type: boolean
      default: false
      description: If active, the node executes only once, with data from the first
        item it receives
    retryOnFail:
      name: Retry On Fail
      field_id: retryOnFail
      type: boolean
      default: false
      description: If active, the node tries to execute again when it fails
    maxTries:
      name: Max. Tries
      field_id: maxTries
      type: number
      default: 3
      min: 2
      max: 5
      description: Number of times to attempt to execute the node before failing the
        execution
      displayOptions:
        show:
          retryOnFail:
          - true
    waitBetweenTries:
      name: Wait Between Tries (ms)
      field_id: waitBetweenTries
      type: number
      default: 1000
      min: 0
      max: 5000
      description: How long to wait between each attempt (in milliseconds)
      displayOptions:
        show:
          retryOnFail:
          - true
    onError:
      name: On Error
      field_id: onError
      type: options
      default: stopWorkflow
      description: Action to take when the node execution fails
      options:
      - name: Stop Workflow
        value: stopWorkflow
        description: Halt execution and fail workflow
      - name: Continue
        value: continueRegularOutput
        description: Pass error message as item in regular output
      - name: Continue (using error output)
        value: continueErrorOutput
        description: Pass item to an extra `error` output
  note: Executable nodes have both common and executable settings

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/jinaAi.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Jina AI Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "reader",
            "research"
          ],
          "default": "reader"
        },
        "operation": {
          "description": "Research a topic and generate a structured research report",
          "type": "string",
          "default": "deepResearch"
        },
        "url": {
          "description": "The URL to fetch content from",
          "type": "string",
          "default": "",
          "format": "url",
          "examples": [
            "https://jina.ai/"
          ]
        },
        "simplify": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "options": {
          "description": "The maximum number of URLs to include in the final answer",
          "type": "string",
          "default": {},
          "examples": [
            "Add Option"
          ]
        },
        "searchQuery": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Jina AI"
          ]
        },
        "researchQuery": {
          "description": "The topic or question for the AI to research",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Analyze the impact of renewable energy sources on climate change mitigation"
          ]
        }
      }
    },
    "settings": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "notes": {
          "type": "string",
          "default": "",
          "description": "Optional note to save with the node"
        },
        "notesInFlow": {
          "type": "boolean",
          "default": false,
          "description": "If active, the note above will display in the flow as a subtitle"
        },
        "alwaysOutputData": {
          "type": "boolean",
          "default": false,
          "description": "If active, will output a single, empty item when the output would have been empty. Use to prevent the workflow finishing on this node"
        },
        "executeOnce": {
          "type": "boolean",
          "default": false,
          "description": "If active, the node executes only once, with data from the first item it receives"
        },
        "retryOnFail": {
          "type": "boolean",
          "default": false,
          "description": "If active, the node tries to execute again when it fails"
        },
        "maxTries": {
          "type": "number",
          "default": 3,
          "description": "Number of times to attempt to execute the node before failing the execution",
          "minimum": 2,
          "maximum": 5
        },
        "waitBetweenTries": {
          "type": "number",
          "default": 1000,
          "description": "How long to wait between each attempt (in milliseconds)",
          "minimum": 0,
          "maximum": 5000
        },
        "onError": {
          "type": "options",
          "default": "stopWorkflow",
          "description": "Action to take when the node execution fails",
          "enum": [
            "stopWorkflow",
            "continueRegularOutput",
            "continueErrorOutput"
          ]
        }
      }
    }
  },
  "metadata": {
    "nodeType": "regular",
    "version": "1"
  },
  "credentials": [
    {
      "name": "jinaAiApi",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "No options",
      "value": {
        "operation": "search",
        "searchQuery": "Jina AI",
        "simplify": false,
        "options": {},
        "requestOptions": {}
      }
    },
    {
      "description": "With options",
      "value": {
        "operation": "search",
        "searchQuery": "Jina AI",
        "simplify": false,
        "options": {
          "outputFormat": "markdown",
          "siteFilter": "jina.ai",
          "pageNumber": 2
        },
        "requestOptions": {}
      }
    },
    {
      "description": "Simplified",
      "value": {
        "operation": "search",
        "searchQuery": "Jina AI",
        "options": {},
        "requestOptions": {}
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
