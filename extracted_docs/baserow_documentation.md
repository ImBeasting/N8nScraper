---
title: "Node: Baserow"
slug: "node-baserow"
version: "1"
updated: "2026-01-08"
summary: "Consume the Baserow API"
node_type: "regular"
group: "['output']"
---

# Node: Baserow

**Purpose.** Consume the Baserow API
**Subtitle.** ={{$parameter["operation"] + ":" + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:baserow.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **baserowApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `baserowApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

---

## Operations

### Row Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a row |
| Delete | `delete` | Delete a row |
| Get | `get` | Retrieve a row |
| Get Many | `getAll` | Retrieve many rows |
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
| Operation | `operation` | options | getAll | ✗ | Create a row |  |

**Operation options:**

* **Create** (`create`) - Create a row
* **Delete** (`delete`) - Delete a row
* **Get** (`get`) - Retrieve a row
* **Get Many** (`getAll`) - Retrieve many rows
* **Update** (`update`) - Update a row

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Data to Send | `dataToSend` | options | defineBelow | ✗ | Use when node input properties match destination column names |  |

**Data to Send options:**

* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names
* **Define Below for Each Column** (`defineBelow`) - Set the value for each destination column

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Fields to Send | `fieldsUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `fieldValues` |  |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Row ID | `rowId` | string |  | ✓ | ID of the row to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Row ID | `rowId` | string |  | ✓ | ID of the row to return |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `additionalOptions` | collection | {} | ✗ | Filter rows based on comparison operators | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filters | `filters` | fixedCollection | {} | Filter rows based on comparison operators |
| Filter Type | `filterType` | options | AND | Indicates that the rows must match all the provided filters |
| Search Term | `search` | string |  | Text to match (can be in any column) |
| Sorting | `order` | fixedCollection | {} | Set the sort order of the result rows |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Row ID | `rowId` | string |  | ✓ | ID of the row to update |  |
| Data to Send | `dataToSend` | options | defineBelow | ✗ | Use when node input properties match destination column names |  |

**Data to Send options:**

* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names
* **Define Below for Each Column** (`defineBelow`) - Set the value for each destination column

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Fields to Send | `fieldsUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `fieldValues` |  |  |  |

</details>


---

## Load Options Methods

- `getDatabaseIds`

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
* Categories: Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: baserow
displayName: Baserow
description: Consume the Baserow API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: baserowApi
  required: true
operations:
- id: create
  name: Create
  description: Create a row
  params:
  - id: dataToSend
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
      name: dataToSend
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
          dataToSend:
          - autoMapInputData
    typeInfo: &id006
      type: string
      displayName: Inputs to Ignore
      name: inputsToIgnore
  - id: fieldsUi
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
          - defineBelow
    typeInfo: &id009
      type: fixedCollection
      displayName: Fields to Send
      name: fieldsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: fieldValues
        displayName: Field
        values:
        - displayName: Field Name or ID
          name: fieldId
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getTableFields
        - displayName: Field Value
          name: fieldValue
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
    required: true
    description: ID of the row to delete
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - delete
    typeInfo: &id002
      type: string
      displayName: Row ID
      name: rowId
- id: get
  name: Get
  description: Retrieve a row
  params:
  - id: rowId
    name: Row ID
    type: string
    default: ''
    required: true
    description: ID of the row to return
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Retrieve many rows
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
        maxValue: 100
- id: update
  name: Update
  description: Update a row
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
  - id: fieldsUi
    name: Fields to Send
    type: fixedCollection
    default: *id007
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Field
    validation: *id008
    typeInfo: *id009
common_expressions:
- ={{$parameter["operation"] + ":" + $parameter["resource"]}}
api_patterns:
  http_methods:
  - POST
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: inputsToIgnore
    text: Enter properties...
  - field: fieldsUi
    text: Add Field
  - field: additionalOptions
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
  "$id": "https://n8n.io/schemas/nodes/baserow.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Baserow Node",
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
          "default": "getAll"
        },
        "databaseId": {
          "description": "Database to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "tableId": {
          "description": "Table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "rowId": {
          "description": "ID of the row to delete",
          "type": "string",
          "default": ""
        },
        "dataToSend": {
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
        "fieldsUi": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
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
          "description": "Filter rows based on comparison operators",
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
      "name": "baserowApi",
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
