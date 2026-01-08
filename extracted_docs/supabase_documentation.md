---
title: "Node: Supabase"
slug: "node-supabase"
version: "1"
updated: "2026-01-08"
summary: "Add, get, delete and update data in a table"
node_type: "regular"
group: "['input']"
---

# Node: Supabase

**Purpose.** Add, get, delete and update data in a table
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:supabase.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **supabaseApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `supabaseApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** GET

---

## Operations

### Row Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new row |
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
| Operation | `operation` | options | create | ✗ | Create a new row |  |

**Operation options:**

* **Create** (`create`) - Create a new row
* **Delete** (`delete`) - Delete a row
* **Get** (`get`) - Get a row
* **Get Many** (`getAll`) - Get many rows
* **Update** (`update`) - Update a row

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table Name or ID | `tableId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
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
| Table Name or ID | `tableId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table Name or ID | `tableId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Select Conditions | `filters` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Condition |  |

<details>
<summary><strong>Select Conditions sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conditions | `conditions` |  |  |  |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table Name or ID | `tableId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table Name or ID | `tableId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
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

- `getTables`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ": " + $parameter["resource"]}}`
- `={{ $rawParameter.schema?.startsWith("=") && $input.all().length > 1 }}`

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
node: supabase
displayName: Supabase
description: Add, get, delete and update data in a table
version: '1'
nodeType: regular
group:
- input
credentials:
- name: supabaseApi
  required: true
operations:
- id: create
  name: Create
  description: Create a new row
  params:
  - id: tableId
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - row
          operation:
          - create
          - delete
          - get
          - getAll
          - update
    typeInfo: &id002
      type: options
      displayName: Table Name or ID
      name: tableId
      typeOptions:
        loadOptionsMethod: getTables
      possibleValues: []
  - id: dataToSend
    name: Data to Send
    type: options
    default: defineBelow
    required: false
    description: Use when node input properties match destination column names
    validation: &id003
      displayOptions:
        show:
          resource:
          - row
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
          resource:
          - row
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
          resource:
          - row
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
            loadOptionsMethod: getTableColumns
        - displayName: Field Value
          name: fieldValue
          type: string
          default: ''
- id: delete
  name: Delete
  description: Delete a row
  params:
  - id: tableId
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
- id: get
  name: Get
  description: Get a row
  params:
  - id: tableId
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: filters
    name: Select Conditions
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Condition
    validation:
      displayOptions:
        show:
          resource:
          - row
          operation:
          - get
    typeInfo:
      type: fixedCollection
      displayName: Select Conditions
      name: filters
      typeOptions:
        multipleValues: true
      subProperties:
      - name: conditions
        displayName: Conditions
        values:
        - displayName: Name or ID
          name: keyName
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getTableColumns
        - displayName: Value
          name: keyValue
          type: string
          default: ''
- id: getAll
  name: Get Many
  description: Get many rows
  params:
  - id: tableId
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
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
          - row
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
          - row
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
  - id: tableId
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
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
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
- ={{ $rawParameter.schema?.startsWith("=") && $input.all().length > 1 }}
api_patterns:
  http_methods:
  - GET
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
  - field: filters
    text: Add Condition
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
  "$id": "https://n8n.io/schemas/nodes/supabase.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Supabase Node",
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
        "useCustomSchema": {
          "description": "Whether to use a database schema different from the default \"public\" schema (requires schema exposure in the <a href=\"https://supabase.com/docs/guides/api/using-custom-schemas?queryGroups=language&language=curl#exposing-custom-schemas\">Supabase API</a>)",
          "type": "boolean",
          "default": false
        },
        "schema": {
          "description": "Name of database schema to use for table",
          "type": "string",
          "default": "public"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "row"
          ],
          "default": "row"
        },
        "operation": {
          "description": "Create a new row",
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
        "tableId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "Any Select Condition": {
          "description": "",
          "type": "string"
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
        "filters": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Condition"
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
      "name": "supabaseApi",
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
