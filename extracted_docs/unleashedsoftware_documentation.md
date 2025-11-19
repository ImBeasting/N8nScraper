---
title: "Node: Unleashed Software"
slug: "node-unleashedsoftware"
version: "1"
updated: "2025-11-13"
summary: "Consume Unleashed Software API"
node_type: "regular"
group: "['transform']"
---

# Node: Unleashed Software

**Purpose.** Consume Unleashed Software API
**Subtitle.** ={{$parameter["operation"] + ":" + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:unleashedSoftware.png`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **unleashedSoftwareApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `unleashedSoftwareApi` | ✓ | - |

---

## API Patterns

**Common Endpoints:**
- `https://api.unleashedsoftware.com/{paginatedPath}`

**Headers Used:** Content-Type

---

## Operations

### Salesorder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many sales orders |

### Stockonhand Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a stock on hand |
| Get Many | `getAll` | Get many stocks on hand |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | salesOrder | ✗ | Resource to operate on |  |

**Resource options:**

* **Sales Order** (`salesOrder`)
* **Stock On Hand** (`stockOnHand`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Get many sales orders |  |

**Operation options:**

* **Get Many** (`getAll`) - Get many sales orders

---

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | Only returns orders for a specified Customer GUID. The CustomerId can be specified as a list of comma-separated GUIDs. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Customer ID | `customerId` | string |  | Only returns orders for a specified Customer GUID. The CustomerId can be specified as a list of comma-separated GUIDs. |
| Customer Code | `customerCode` | string |  | Returns orders that start with the specific customer code |
| End Date | `endDate` | dateTime |  | Returns orders with order date before the specified date. UTC. |
| Modified Since | `modifiedSince` | dateTime |  | Returns orders created or edited after a specified date, must be UTC format |
| Order Number | `orderNumber` | string |  | Returns a single order with the specified order number. If set, it overrides all other filters. |
| Order Status | `orderStatus` | multiOptions | [] | Returns orders with the specified status. If no orderStatus filter is specified, then we exclude "Deleted" by default. |
| Start Date | `startDate` | dateTime |  | Returns orders with order date after the specified date. UTC. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | Returns the stock on hand for a specific date | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| As at Date | `asAtDate` | dateTime |  | Returns the stock on hand for a specific date |
| Is Assembled | `IsAssembled` | boolean | False | Whether the AvailableQty will also include the quantity that can be assembled |
| Modified Since | `modifiedSince` | dateTime |  | Returns stock on hand values modified after a specific date |
| Order By | `orderBy` | string |  | Orders the list by a specific column, by default the list is ordered by productCode |
| Product ID | `productId` | string |  | Returns products with the specific Product Guid. You can enter multiple product IDs separated by commas. |
| Warehouse Code | `warehouseCode` | string |  | Returns stock on hand for a specific warehouse code |
| Warehouse Name | `warehouseName` | string |  | Returns stock on hand for a specific warehouse name |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Product ID | `productId` | string |  | ✗ |  |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ":" + $parameter["resource"]}}`

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
* Categories: Sales, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: unleashedSoftware
displayName: Unleashed Software
description: Consume Unleashed Software API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: unleashedSoftwareApi
  required: true
operations:
- id: getAll
  name: Get Many
  description: Get many sales orders
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id001
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - stockOnHand
    typeInfo: &id002
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id003
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - stockOnHand
          returnAll:
          - false
    typeInfo: &id004
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 1000
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
- id: get
  name: Get
  description: Get a stock on hand
  params:
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - get
          resource:
          - stockOnHand
    typeInfo:
      type: string
      displayName: Product ID
      name: productId
common_expressions:
- ={{$parameter["operation"] + ":" + $parameter["resource"]}}
api_patterns:
  http_methods: []
  endpoints:
  - https://api.unleashedsoftware.com/{paginatedPath}
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/unleashedSoftware.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Unleashed Software Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "getAll",
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
            "salesOrder",
            "stockOnHand"
          ],
          "default": "salesOrder"
        },
        "operation": {
          "description": "Get a stock on hand",
          "type": "string",
          "enum": [
            "get",
            "getAll"
          ],
          "default": "getAll"
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
        },
        "filters": {
          "description": "Returns the stock on hand for a specific date",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "productId": {
          "description": "",
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
      "name": "unleashedSoftwareApi",
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
