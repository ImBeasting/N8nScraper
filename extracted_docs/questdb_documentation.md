---
title: "Node: QuestDB"
slug: "node-questdb"
version: "1"
updated: "2025-11-13"
summary: "Get, add and update data in QuestDB"
node_type: "regular"
group: "['input']"
---

# Node: QuestDB

**Purpose.** Get, add and update data in QuestDB


---

## Node Details

- **Icon:** `file:questdb.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **questDb**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `questDb` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Execute Query | `executeQuery` | Executes a SQL query |
| Insert | `insert` | Insert rows in database |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | insert | ✗ | Executes a SQL query |  |

**Operation options:**

* **Execute Query** (`executeQuery`) - Executes a SQL query
* **Insert** (`insert`) - Insert rows in database

---

### Execute Query parameters (`executeQuery`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Query | `query` | string |  | ✓ | The SQL query to execute. You can use n8n expressions or $1 and $2 in conjunction with query parameters. | e.g. SELECT id, name FROM product WHERE quantity > $1 AND price <= $2 |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Execute each query independently | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Mode | `mode` | options | independently | Execute each query independently |
| Query Parameters | `queryParams` | string |  | Comma-separated list of properties which should be used as query parameters |

</details>


### Insert parameters (`insert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Schema | `schema` | hidden |  | ✗ | Name of the schema the table belongs to |  |
| Table | `table` | string |  | ✓ | Name of the table in which to insert data to |  |
| Columns | `columns` | string |  | ✗ | Comma-separated list of the properties which should used as columns for the new rows | e.g. id,name,description |  |
| Return Fields | `returnFields` | string | * | ✗ | Comma-separated list of the fields that the operation will return |  |
| Additional Fields | `additionalFields` | hidden | {} | ✗ |  |  |

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
* Categories: Data & Storage, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: questDb
displayName: QuestDB
description: Get, add and update data in QuestDB
version: '1'
nodeType: regular
group:
- input
credentials:
- name: questDb
  required: true
operations:
- id: executeQuery
  name: Execute Query
  description: Executes a SQL query
  params:
  - id: query
    name: Query
    type: string
    default: ''
    required: true
    description: The SQL query to execute. You can use n8n expressions or $1 and $2
      in conjunction with query parameters.
    placeholder: SELECT id, name FROM product WHERE quantity > $1 AND price <= $2
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - executeQuery
    typeInfo:
      type: string
      displayName: Query
      name: query
- id: insert
  name: Insert
  description: Insert rows in database
  params:
  - id: schema
    name: Schema
    type: hidden
    default: ''
    required: false
    description: Name of the schema the table belongs to
    validation:
      displayOptions:
        show:
          operation:
          - insert
    typeInfo:
      type: hidden
      displayName: Schema
      name: schema
  - id: table
    name: Table
    type: string
    default: ''
    required: true
    description: Name of the table in which to insert data to
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - insert
    typeInfo:
      type: string
      displayName: Table
      name: table
  - id: columns
    name: Columns
    type: string
    default: ''
    required: false
    description: Comma-separated list of the properties which should used as columns
      for the new rows
    placeholder: id,name,description
    validation:
      displayOptions:
        show:
          operation:
          - insert
    typeInfo:
      type: string
      displayName: Columns
      name: columns
  - id: returnFields
    name: Return Fields
    type: string
    default: '*'
    required: false
    description: Comma-separated list of the fields that the operation will return
    validation:
      displayOptions:
        show:
          operation:
          - insert
    typeInfo:
      type: string
      displayName: Return Fields
      name: returnFields
  - id: additionalFields
    name: Additional Fields
    type: hidden
    default: {}
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - insert
    typeInfo:
      type: hidden
      displayName: Additional Fields
      name: additionalFields
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: query
    text: SELECT id, name FROM product WHERE quantity > $1 AND price <= $2
  - field: columns
    text: id,name,description
  - field: additionalFields
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
  "$id": "https://n8n.io/schemas/nodes/questDb.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "QuestDB Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "executeQuery",
        "insert"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Executes a SQL query",
          "type": "string",
          "enum": [
            "executeQuery",
            "insert"
          ],
          "default": "insert"
        },
        "query": {
          "description": "The SQL query to execute. You can use n8n expressions or $1 and $2 in conjunction with query parameters.",
          "type": "string",
          "default": "",
          "examples": [
            "SELECT id, name FROM product WHERE quantity > $1 AND price <= $2"
          ]
        },
        "schema": {
          "description": "Name of the schema the table belongs to",
          "type": "string",
          "default": ""
        },
        "table": {
          "description": "Name of the table in which to insert data to",
          "type": "string",
          "default": ""
        },
        "columns": {
          "description": "Comma-separated list of the properties which should used as columns for the new rows",
          "type": "string",
          "default": "",
          "examples": [
            "id,name,description"
          ]
        },
        "returnFields": {
          "description": "Comma-separated list of the fields that the operation will return",
          "type": "string",
          "default": "*"
        },
        "additionalFields": {
          "description": "",
          "type": "string",
          "default": {}
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
      "name": "questDb",
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
