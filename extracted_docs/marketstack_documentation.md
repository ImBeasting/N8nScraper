---
title: "Node: Marketstack"
slug: "node-marketstack"
version: "1"
updated: "2025-11-13"
summary: "Consume Marketstack API"
node_type: "regular"
group: "['transform']"
---

# Node: Marketstack

**Purpose.** Consume Marketstack API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:marketstack.svg', 'dark': 'file:marketstack.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **marketstackApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `marketstackApi` | ✓ | - |

---

## Operations

### Exchange Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get an exchange |

### Endofdaydata Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many EoD data |

### Ticker Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a ticker |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | endOfDayData | ✓ | Stock market closing data |  |

**Resource options:**

* **End-of-Day Data** (`endOfDayData`) - Stock market closing data
* **Exchange** (`exchange`) - Stock market exchange
* **Ticker** (`ticker`) - Stock market symbol

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Get** (`get`) - Get an exchange

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Exchange | `exchange` | string |  | ✓ | Stock exchange to retrieve, specified by <a href="https://en.wikipedia.org/wiki/Market_Identifier_Code">Market Identifier Code</a>, e.g. <code>XNAS</code> |  |
| Ticker | `symbol` | string |  | ✓ | Stock symbol (ticker) to retrieve, e.g. <code>AAPL</code> |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Ticker | `symbols` | string |  | ✓ | One or multiple comma-separated stock symbols (tickers) to retrieve, e.g. <code>AAPL</code> or <code>AAPL,MSFT</code> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Stock exchange to filter results by, specified by <a href="https://en.wikipedia.org/wiki/Market_Identifier_Code">Market Identifier Code</a>, e.g. <code>XNAS</code> | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exchange | `exchange` | string |  | Stock exchange to filter results by, specified by <a href="https://en.wikipedia.org/wiki/Market_Identifier_Code">Market Identifier Code</a>, e.g. <code>XNAS</code> |
| Latest | `latest` | boolean | False | Whether to fetch the most recent stock market data |
| Sort Order | `sort` | options | DESC | Order to sort results in |
| Specific Date | `specificDate` | dateTime |  | Date in YYYY-MM-DD format, e.g. <code>2020-01-01</code>, or in ISO-8601 date format, e.g. <code>2020-05-21T00:00:00+0000</code> |
| Timeframe Start Date | `dateFrom` | dateTime |  | Timeframe start date in YYYY-MM-DD format, e.g. <code>2020-01-01</code>, or in ISO-8601 date format, e.g. <code>2020-05-21T00:00:00+0000</code> |
| Timeframe End Date | `dateTo` | dateTime |  | Timeframe end date in YYYY-MM-DD format, e.g. <code>2020-01-01</code>, or in ISO-8601 date format, e.g. <code>2020-05-21T00:00:00+0000</code> |

</details>


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
* Categories: Analytics, Finance & Accounting

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: marketstack
displayName: Marketstack
description: Consume Marketstack API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: marketstackApi
  required: true
operations:
- id: get
  name: Get
  description: ''
  params:
  - id: exchange
    name: Exchange
    type: string
    default: ''
    required: true
    description: Stock exchange to retrieve, specified by <a href="https://en.wikipedia.org/wiki/Market_Identifier_Code">Market
      Identifier Code</a>, e.g. <code>XNAS</code>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - exchange
          operation:
          - get
    typeInfo:
      type: string
      displayName: Exchange
      name: exchange
  - id: symbol
    name: Ticker
    type: string
    default: ''
    required: true
    description: Stock symbol (ticker) to retrieve, e.g. <code>AAPL</code>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - ticker
          operation:
          - get
    typeInfo:
      type: string
      displayName: Ticker
      name: symbol
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: symbols
    name: Ticker
    type: string
    default: ''
    required: true
    description: One or multiple comma-separated stock symbols (tickers) to retrieve,
      e.g. <code>AAPL</code> or <code>AAPL,MSFT</code>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - endOfDayData
          operation:
          - getAll
    typeInfo:
      type: string
      displayName: Ticker
      name: symbols
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          resource:
          - endOfDayData
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          resource:
          - endOfDayData
          operation:
          - getAll
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
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
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/marketstack.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Marketstack Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Stock market closing data",
          "type": "string",
          "enum": [
            "endOfDayData",
            "exchange",
            "ticker"
          ],
          "default": "endOfDayData"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "get"
          ],
          "default": "get"
        },
        "exchange": {
          "description": "Stock exchange to retrieve, specified by <a href=\"https://en.wikipedia.org/wiki/Market_Identifier_Code\">Market Identifier Code</a>, e.g. <code>XNAS</code>",
          "type": "string",
          "default": ""
        },
        "symbols": {
          "description": "One or multiple comma-separated stock symbols (tickers) to retrieve, e.g. <code>AAPL</code> or <code>AAPL,MSFT</code>",
          "type": "string",
          "default": ""
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 50
        },
        "filters": {
          "description": "Stock exchange to filter results by, specified by <a href=\"https://en.wikipedia.org/wiki/Market_Identifier_Code\">Market Identifier Code</a>, e.g. <code>XNAS</code>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "symbol": {
          "description": "Stock symbol (ticker) to retrieve, e.g. <code>AAPL</code>",
          "type": "string",
          "default": ""
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
      "name": "marketstackApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
