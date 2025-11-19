---
title: "Node: Grist"
slug: "node-grist"
version: "1"
updated: "2025-11-13"
summary: "Consume the Grist API"
node_type: "regular"
group: "['input']"
---

# Node: Grist

**Purpose.** Consume the Grist API
**Subtitle.** ={{$parameter["operation"]}}


---

## Node Details

- **Icon:** `file:grist.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **gristApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `gristApi` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create Row | `create` | Create rows in a table |
| Delete Row | `delete` | Delete rows from a table |
| Get Many Rows | `getAll` | Read rows from a table |
| Update Row | `update` | Update rows in a table |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Create rows in a table |  |

**Operation options:**

* **Create Row** (`create`) - Create rows in a table
* **Delete Row** (`delete`) - Delete rows from a table
* **Get Many Rows** (`getAll`) - Read rows from a table
* **Update Row** (`update`) - Update rows in a table

---

### Create Row parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Data to Send | `dataToSend` | options | defineInNode | ✗ | Use when node input properties match destination column names |  |

**Data to Send options:**

* **Auto-Map Input Data to Columns** (`autoMapInputs`) - Use when node input properties match destination column names
* **Define Below for Each Column** (`defineInNode`) - Set the value for each destination column

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Fields to Send | `fieldsToSend` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Properties | `properties` |  |  |  |

</details>


### Delete Row parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Row ID | `rowId` | string |  | ✓ | ID of the row to delete, or comma-separated list of row IDs to delete |  |

### Get Many Rows parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Additional Options | `additionalOptions` | collection | {} | ✓ | Only return rows matching all of the given filters. For complex filters, create a formula column and filter for the value "true". | e.g. Add option |  |

<details>
<summary><strong>Additional Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filter | `filter` | fixedCollection | {} | Only return rows matching all of the given filters. For complex filters, create a formula column and filter for the value "true". |
| Sort Order | `sort` | fixedCollection | {} | Column to sort on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Update Row parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Row ID | `rowId` | string |  | ✓ | ID of the row to update |  |
| Data to Send | `dataToSend` | options | defineInNode | ✗ | Use when node input properties match destination column names |  |

**Data to Send options:**

* **Auto-Map Input Data to Columns** (`autoMapInputs`) - Use when node input properties match destination column names
* **Define Below for Each Column** (`defineInNode`) - Set the value for each destination column

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Fields to Send | `fieldsToSend` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Properties | `properties` |  |  |  |

</details>


---

## Load Options Methods

- `getTableColumns`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"]}}`

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
* Categories: Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: grist
displayName: Grist
description: Consume the Grist API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: gristApi
  required: true
operations:
- id: create
  name: Create Row
  description: Create rows in a table
  params:
  - id: dataToSend
    name: Data to Send
    type: options
    default: defineInNode
    required: false
    description: Use when node input properties match destination column names
    validation: &id003
      displayOptions:
        show:
          operation:
          - create
          - update
    typeInfo: &id004
      type: options
      displayName: Data to Send
      name: dataToSend
      possibleValues:
      - value: autoMapInputs
        name: Auto-Map Input Data to Columns
        description: Use when node input properties match destination column names
      - value: defineInNode
        name: Define Below for Each Column
        description: Set the value for each destination column
  - id: inputsToIgnore
    name: Inputs to Ignore
    type: string
    default: ''
    required: false
    description: List of input properties to avoid sending, separated by commas. Leave
      empty to send all properties.
    placeholder: Enter properties...
    validation: &id005
      displayOptions:
        show:
          operation:
          - create
          - update
          dataToSend:
          - autoMapInputs
    typeInfo: &id006
      type: string
      displayName: Inputs to Ignore
      name: inputsToIgnore
  - id: fieldsToSend
    name: Fields to Send
    type: fixedCollection
    default: &id007 {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Field
    validation: &id008
      displayOptions:
        show:
          operation:
          - create
          - update
          dataToSend:
          - defineInNode
    typeInfo: &id009
      type: fixedCollection
      displayName: Fields to Send
      name: fieldsToSend
      typeOptions:
        multipleValues: true
      subProperties:
      - name: properties
        displayName: Properties
        values:
        - displayName: Column Name or ID
          name: fieldId
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getTableColumns
        - displayName: Field Value
          name: fieldValue
          type: string
          default: ''
- id: delete
  name: Delete Row
  description: Delete rows from a table
  params:
  - id: rowId
    name: Row ID
    type: string
    default: ''
    required: true
    description: ID of the row to delete, or comma-separated list of row IDs to delete
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: Row ID
      name: rowId
- id: getAll
  name: Get Many Rows
  description: Read rows from a table
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
- id: update
  name: Update Row
  description: Update rows in a table
  params:
  - id: rowId
    name: Row ID
    type: string
    default: ''
    required: true
    description: ID of the row to update
    validation: *id001
    typeInfo: *id002
  - id: dataToSend
    name: Data to Send
    type: options
    default: defineInNode
    required: false
    description: Use when node input properties match destination column names
    validation: *id003
    typeInfo: *id004
  - id: inputsToIgnore
    name: Inputs to Ignore
    type: string
    default: ''
    required: false
    description: List of input properties to avoid sending, separated by commas. Leave
      empty to send all properties.
    placeholder: Enter properties...
    validation: *id005
    typeInfo: *id006
  - id: fieldsToSend
    name: Fields to Send
    type: fixedCollection
    default: *id007
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Field
    validation: *id008
    typeInfo: *id009
common_expressions:
- ={{$parameter["operation"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalOptions
    text: Add option
  - field: inputsToIgnore
    text: Enter properties...
  - field: fieldsToSend
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/grist.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Grist Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "getAll",
        "update"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Create rows in a table",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "getAll",
            "update"
          ],
          "default": "getAll"
        },
        "docId": {
          "description": "In your document, click your profile icon, then Document Settings, then copy the value under \"This document's ID\"",
          "type": "string",
          "default": ""
        },
        "tableId": {
          "description": "ID of table to operate on. If unsure, look at the Code View.",
          "type": "string",
          "default": ""
        },
        "rowId": {
          "description": "ID of the row to update",
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
        "additionalOptions": {
          "description": "Only return rows matching all of the given filters. For complex filters, create a formula column and filter for the value \"true\".",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "dataToSend": {
          "description": "Use when node input properties match destination column names",
          "type": "string",
          "enum": [
            "autoMapInputs",
            "defineInNode"
          ],
          "default": "defineInNode"
        },
        "inputsToIgnore": {
          "description": "List of input properties to avoid sending, separated by commas. Leave empty to send all properties.",
          "type": "string",
          "default": "",
          "examples": [
            "Enter properties..."
          ]
        },
        "fieldsToSend": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
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
      "name": "gristApi",
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
