---
title: "Node: ProfitWell"
slug: "node-profitwell"
version: "1"
updated: "2026-01-08"
summary: "Consume ProfitWell API"
node_type: "regular"
group: "['output']"
---

# Node: ProfitWell

**Purpose.** Consume ProfitWell API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:profitwell.svg', 'dark': 'file:profitwell.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **profitWellApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `profitWellApi` | ✓ | - |

---

## Operations

### Company Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Settings | `getSetting` | Get your company's ProfitWell account settings |

### Metric Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve financial metric broken down by day for either the current month or the last |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | metric | ✗ | Resource to operate on |  |

**Resource options:**

* **Company** (`company`)
* **Metric** (`metric`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getSetting | ✗ | Get your company's ProfitWell account settings |  |

**Operation options:**

* **Get Settings** (`getSetting`) - Get your company's ProfitWell account settings

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Type | `type` | options |  | ✓ | Retrieve financial metric broken down by day for either the current month or the last |  |

**Type options:**

* **Daily** (`daily`) - Retrieve financial metric broken down by day for either the current month or the last
* **Monthly** (`monthly`) - Retrieve all monthly financial metric for your company

| Month | `month` | string |  | ✓ | Can only be the current or previous month. Format should be YYYY-MM. | e.g. YYYY-MM |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Only return the metric for this Plan ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Plan Name or ID | `plan_id` | options |  | Only return the metric for this Plan ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Metrics | `dailyMetrics` | multiOptions | [] | Number of paying customers |
| Metrics | `monthlyMetrics` | multiOptions | [] | Number of paying customers |

</details>


---

## Load Options Methods

- `getPlanIds`
- `for`
- `name`
- `value`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ": " + $parameter["resource"]}}`

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
* Categories: Analytics

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: profitWell
displayName: ProfitWell
description: Consume ProfitWell API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: profitWellApi
  required: true
operations:
- id: getSetting
  name: Get Settings
  description: Get your company's ProfitWell account settings
- id: get
  name: Get
  description: Retrieve financial metric broken down by day for either the current
    month or the last
  params:
  - id: type
    name: Type
    type: options
    default: ''
    required: true
    description: Retrieve financial metric broken down by day for either the current
      month or the last
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - metric
          operation:
          - get
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: daily
        name: Daily
        description: Retrieve financial metric broken down by day for either the current
          month or the last
      - value: monthly
        name: Monthly
        description: Retrieve all monthly financial metric for your company
  - id: month
    name: Month
    type: string
    default: ''
    required: true
    description: Can only be the current or previous month. Format should be YYYY-MM.
    placeholder: YYYY-MM
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - metric
          operation:
          - get
          type:
          - daily
    typeInfo:
      type: string
      displayName: Month
      name: month
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation:
      displayOptions:
        show:
          resource:
          - metric
          operation:
          - get
    typeInfo:
      type: boolean
      displayName: Simplify
      name: simple
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: month
    text: YYYY-MM
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/profitWell.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ProfitWell Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "getSetting",
        "get"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "company",
            "metric"
          ],
          "default": "metric"
        },
        "operation": {
          "description": "Retrieve financial metric broken down by day for either the current month or the last",
          "type": "string",
          "enum": [
            "get"
          ],
          "default": "get"
        },
        "type": {
          "description": "Retrieve financial metric broken down by day for either the current month or the last",
          "type": "string",
          "enum": [
            "daily",
            "monthly"
          ],
          "default": ""
        },
        "month": {
          "description": "Can only be the current or previous month. Format should be YYYY-MM.",
          "type": "string",
          "default": "",
          "examples": [
            "YYYY-MM"
          ]
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "options": {
          "description": "Only return the metric for this Plan ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
      "name": "profitWellApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
