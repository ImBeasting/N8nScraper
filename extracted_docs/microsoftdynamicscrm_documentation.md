---
title: "Node: Microsoft Dynamics CRM"
slug: "node-microsoftdynamicscrm"
version: "1"
updated: "2026-01-08"
summary: "Consume Microsoft Dynamics CRM API"
node_type: "regular"
group: "['input']"
---

# Node: Microsoft Dynamics CRM

**Purpose.** Consume Microsoft Dynamics CRM API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:microsoftDynamicsCrm.svg', 'dark': 'file:microsoftDynamicsCrm.dark.svg'}`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftDynamicsOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `microsoftDynamicsOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Account Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an account |
| Delete | `delete` | Delete an account |
| Get | `get` | Get an account |
| Get Many | `getAll` | Get many accounts |
| Update | `update` | Update an account |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | account | ✗ | Resource to operate on |  |

**Resource options:**

* **Account** (`account`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create an account
* **Delete** (`delete`) - Delete an account
* **Get** (`get`) - Get an account
* **Get Many** (`getAll`) - Get many accounts
* **Update** (`update`) - Update an account

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Company or business name |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Options | `options` | collection | {} | ✗ | Fields the response will include. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Return Field Names or IDs | `returnFields` | multiOptions | [] | Fields the response will include. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Account ID | `accountId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Account ID | `accountId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Return Field Names or IDs | `returnFields` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Expand Field Names or IDs | `expandFields` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Options | `options` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Return Field Names or IDs | `returnFields` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Expand Field Names or IDs | `expandFields` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Filters | `filters` | collection | {} | ✗ | Query to filter the results. Check <a href="https://docs.microsoft.com/en-us/powerapps/developer/data-platform/webapi/query-data-web-api#filter-results" target="_blank">filters</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | Query to filter the results. Check <a href="https://docs.microsoft.com/en-us/powerapps/developer/data-platform/webapi/query-data-web-api#filter-results" target="_blank">filters</a>. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Account ID | `accountId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |
| Options | `options` | collection | {} | ✗ | Fields the response will include. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Return Field Names or IDs | `returnFields` | multiOptions | [] | Fields the response will include. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


---

## Load Options Methods

- `getAccountCategories`

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
* Categories: Marketing, Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: microsoftDynamicsCrm
displayName: Microsoft Dynamics CRM
description: Consume Microsoft Dynamics CRM API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: microsoftDynamicsOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Company or business name
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - account
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
- id: delete
  name: Delete
  description: ''
  params:
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - account
          operation:
          - delete
          - get
          - update
    typeInfo: &id002
      type: string
      displayName: Account ID
      name: accountId
- id: get
  name: Get
  description: ''
  params:
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: ''
  params:
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
          - account
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          resource:
          - account
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
        maxValue: 10
- id: update
  name: Update
  description: ''
  params:
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add option
  - field: filters
    text: Add Filter
  - field: updateFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/microsoftDynamicsCrm.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft Dynamics CRM Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "get",
        "getAll",
        "update"
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
            "account"
          ],
          "default": "account"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "name": {
          "description": "Company or business name",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "accountId": {
          "description": "",
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
          "default": 5
        },
        "options": {
          "description": "Fields the response will include. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "filters": {
          "description": "Query to filter the results. Check <a href=\"https://docs.microsoft.com/en-us/powerapps/developer/data-platform/webapi/query-data-web-api#filter-results\" target=\"_blank\">filters</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "updateFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
      "name": "microsoftDynamicsOAuth2Api",
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
