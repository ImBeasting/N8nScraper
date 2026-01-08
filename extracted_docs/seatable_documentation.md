---
title: "Node: SeaTable Trigger"
slug: "node-seatable"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when SeaTable events occur"
node_type: "trigger"
group: "['input']"
---

# Node: SeaTable Trigger

**Purpose.** Starts the workflow when SeaTable events occur
**Subtitle.** ={{$parameter["resource"] + ": " + $parameter["operation"]}}


---

## Node Details

- **Icon:** `file:seaTable.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **seaTableApi**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `seaTableApi` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a row |
| Delete | `delete` | Delete a row |
| Get | `get` | Get a row |
| Get Many | `getAll` | Get many rows |
| Update | `update` | Update a row |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | row | ✗ | Resource to operate on |  |

**Resource options:**

* **Row** (`row`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a row |  |

**Operation options:**

* **Create** (`create`) - Create a row
* **Delete** (`delete`) - Delete a row
* **Get** (`get`) - Get a row
* **Get Many** (`getAll`) - Get many rows
* **Update** (`update`) - Update a row

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Data to Send | `fieldsToSend` | options | defineBelow | ✗ | Use when node input properties match destination column names |  |

**Data to Send options:**

* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names
* **Define Below for Each Column** (`defineBelow`) - Set the value for each destination column

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Columns to Send | `columnsUi` | fixedCollection |  | ✗ | Choose from the list, or specify the name using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a> | e.g. Add Column |  |

<details>
<summary><strong>Columns to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Column | `columnValues` |  |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Row ID | `rowId` | string |  | ✗ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table ID | `tableId` | options |  | ✓ | The name of SeaTable table to access. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. ID of the table |  |
| Row ID | `rowId` | string |  | ✗ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | True | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Choose from the list, or specify an View Name using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a> | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| View Name | `view_name` | options |  | Choose from the list, or specify an View Name using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a> |

</details>

| Options | `options` | collection | {} | ✗ | Whether the ID of the linked row is returned in the link column (true). Otherwise, it return the name of the linked row (false). | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Convert Link ID | `convert_link_id` | boolean | False | Whether the ID of the linked row is returned in the link column (true). Otherwise, it return the name of the linked row (false). |
| Direction | `direction` | options | asc | The direction of the sort, ascending (asc) or descending (desc) |
| Order By Column | `order_by` | options |  | Choose from the list, or specify a Column using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a> |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Row ID | `rowId` | string |  | ✗ |  |  |
| Data to Send | `fieldsToSend` | options | defineBelow | ✗ | Use when node input properties match destination column names |  |

**Data to Send options:**

* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names
* **Define Below for Each Column** (`defineBelow`) - Set the value for each destination column

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Columns to Send | `columnsUi` | fixedCollection |  | ✗ | Choose from the list, or specify the name using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a> | e.g. Add Column |  |

<details>
<summary><strong>Columns to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Column | `columnValues` |  |  |  |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["resource"] + ": " + $parameter["operation"]}}`

---

## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |

---

## Notes & Caveats

* This node is part of n8n-nodes-base

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: seaTable
displayName: SeaTable Trigger
description: Starts the workflow when SeaTable events occur
version: '1'
nodeType: trigger
group:
- input
credentials:
- name: seaTableApi
  required: true
operations:
- id: create
  name: Create
  description: Create a row
  params:
  - id: fieldsToSend
    name: Data to Send
    type: options
    default: defineBelow
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
      name: fieldsToSend
      possibleValues:
      - value: autoMapInputData
        name: Auto-Map Input Data to Columns
        description: Use when node input properties match destination column names
      - value: defineBelow
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
          fieldsToSend:
          - autoMapInputData
    typeInfo: &id006
      type: string
      displayName: Inputs to Ignore
      name: inputsToIgnore
  - id: columnsUi
    name: Columns to Send
    type: fixedCollection
    default: ''
    required: false
    description: Choose from the list, or specify the name using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a>
    placeholder: Add Column
    validation: &id007
      displayOptions:
        show:
          operation:
          - create
          - update
          fieldsToSend:
          - defineBelow
    typeInfo: &id008
      type: fixedCollection
      displayName: Columns to Send
      name: columnsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: columnValues
        displayName: Column
        values:
        - displayName: Column Name
          name: columnName
          type: options
          description: Choose from the list, or specify the name using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getTableUpdateAbleColumns
        - displayName: Column Value
          name: columnValue
          type: string
          default: ''
- id: delete
  name: Delete
  description: Delete a row
  params:
  - id: rowId
    name: Row ID
    type: string
    default: ''
    required: false
    description: ''
    validation: &id001
      displayOptions:
        show:
          operation:
          - get
    typeInfo: &id002
      type: string
      displayName: Row ID
      name: rowId
- id: get
  name: Get
  description: Get a row
  params:
  - id: tableId
    name: Table ID
    type: options
    default: ''
    required: true
    description: The name of SeaTable table to access. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    placeholder: ID of the table
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - get
    typeInfo:
      type: options
      displayName: Table ID
      name: tableId
      typeOptions:
        loadOptionsMethod: getTableIds
      possibleValues: []
  - id: rowId
    name: Row ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many rows
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: true
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
  name: Update
  description: Update a row
  params:
  - id: rowId
    name: Row ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: fieldsToSend
    name: Data to Send
    type: options
    default: defineBelow
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
  - id: columnsUi
    name: Columns to Send
    type: fixedCollection
    default: ''
    required: false
    description: Choose from the list, or specify the name using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a>
    placeholder: Add Column
    validation: *id007
    typeInfo: *id008
common_expressions:
- '={{$parameter["resource"] + ": " + $parameter["operation"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: tableName
    text: Name of the table
  - field: tableId
    text: ID of the table
  - field: inputsToIgnore
    text: Enter properties...
  - field: columnsUi
    text: Add Column
  - field: filters
    text: Add Filter
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/seaTable.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SeaTable Trigger Node",
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
            "row"
          ],
          "default": "row"
        },
        "operation": {
          "description": "Create a row",
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
        "tableName": {
          "description": "The name of SeaTable table to access. Choose from the list, or specify the name using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "Name of the table"
          ]
        },
        "tableId": {
          "description": "The name of SeaTable table to access. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "ID of the table"
          ]
        },
        "rowId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "fieldsToSend": {
          "description": "Use when node input properties match destination column names",
          "type": "string",
          "enum": [
            "autoMapInputData",
            "defineBelow"
          ],
          "default": "defineBelow"
        },
        "inputsToIgnore": {
          "description": "List of input properties to avoid sending, separated by commas. Leave empty to send all properties.",
          "type": "string",
          "default": "",
          "examples": [
            "Enter properties..."
          ]
        },
        "columnsUi": {
          "description": "Choose from the list, or specify the name using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>",
          "type": "string",
          "default": "",
          "examples": [
            "Add Column"
          ]
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": true
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 50
        },
        "filters": {
          "description": "Choose from the list, or specify an View Name using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "options": {
          "description": "Whether the ID of the linked row is returned in the link column (true). Otherwise, it return the name of the linked row (false).",
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
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
    "version": "1"
  },
  "credentials": [
    {
      "name": "seaTableApi",
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
