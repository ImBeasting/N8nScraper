---
title: "Node: Microsoft SQL"
slug: "node-microsoftsql"
version: "['1', '1.1']"
updated: "2025-11-13"
summary: "Get, add and update data in Microsoft SQL"
node_type: "regular"
group: "['input']"
---

# Node: Microsoft SQL

**Purpose.** Get, add and update data in Microsoft SQL


---

## Node Details

- **Icon:** `file:mssql.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftSql**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `microsoftSql` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Execute Query | `executeQuery` | Execute an SQL query |
| Insert | `insert` | Insert rows in database |
| Update | `update` | Update rows in database |
| Delete | `delete` | Delete rows in database |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | insert | ✗ | Execute an SQL query |  |

**Operation options:**

* **Execute Query** (`executeQuery`) - Execute an SQL query
* **Insert** (`insert`) - Insert rows in database
* **Update** (`update`) - Update rows in database
* **Delete** (`delete`) - Delete rows in database

---

### Execute Query parameters (`executeQuery`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Query | `query` | string |  | ✓ | The SQL query to execute | e.g. SELECT id, name FROM product WHERE id < 40 |  |

### Insert parameters (`insert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table | `table` | string |  | ✓ | Name of the table in which to insert data to |  |
| Columns | `columns` | string |  | ✗ | Comma-separated list of the properties which should used as columns for the new rows | e.g. id,name,description |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table | `table` | string |  | ✓ | Name of the table in which to update data in |  |
| Update Key | `updateKey` | string | id | ✓ | Name of the property which decides which rows in the database should be updated. Normally that would be "id". |  |
| Columns | `columns` | string |  | ✗ | Comma-separated list of the properties which should used as columns for rows to update | e.g. name,description |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table | `table` | string |  | ✓ | Name of the table in which to delete data |  |
| Delete Key | `deleteKey` | string | id | ✓ | Name of the property which decides which rows in the database should be deleted. Normally that would be "id". |  |

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
* Categories: Development, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: microsoftSql
displayName: Microsoft SQL
description: Get, add and update data in Microsoft SQL
version:
- '1'
- '1.1'
nodeType: regular
group:
- input
credentials:
- name: microsoftSql
  required: true
operations:
- id: executeQuery
  name: Execute Query
  description: Execute an SQL query
  params:
  - id: query
    name: Query
    type: string
    default: ''
    required: true
    description: The SQL query to execute
    placeholder: SELECT id, name FROM product WHERE id < 40
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
  - id: table
    name: Table
    type: string
    default: ''
    required: true
    description: Name of the table in which to insert data to
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - delete
    typeInfo: &id002
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
    validation: &id003
      displayOptions:
        show:
          operation:
          - update
    typeInfo: &id004
      type: string
      displayName: Columns
      name: columns
- id: update
  name: Update
  description: Update rows in database
  params:
  - id: table
    name: Table
    type: string
    default: ''
    required: true
    description: Name of the table in which to update data in
    validation: *id001
    typeInfo: *id002
  - id: updateKey
    name: Update Key
    type: string
    default: id
    required: true
    description: Name of the property which decides which rows in the database should
      be updated. Normally that would be "id".
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - update
    typeInfo:
      type: string
      displayName: Update Key
      name: updateKey
  - id: columns
    name: Columns
    type: string
    default: ''
    required: false
    description: Comma-separated list of the properties which should used as columns
      for rows to update
    placeholder: name,description
    validation: *id003
    typeInfo: *id004
- id: delete
  name: Delete
  description: Delete rows in database
  params:
  - id: table
    name: Table
    type: string
    default: ''
    required: true
    description: Name of the table in which to delete data
    validation: *id001
    typeInfo: *id002
  - id: deleteKey
    name: Delete Key
    type: string
    default: id
    required: true
    description: Name of the property which decides which rows in the database should
      be deleted. Normally that would be "id".
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - delete
    typeInfo:
      type: string
      displayName: Delete Key
      name: deleteKey
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: query
    text: SELECT id, name FROM product WHERE id < 40
  - field: columns
    text: id,name,description
  - field: columns
    text: name,description
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
  "$id": "https://n8n.io/schemas/nodes/microsoftSql.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft SQL Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "executeQuery",
        "insert",
        "update",
        "delete"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Execute an SQL query",
          "type": "string",
          "enum": [
            "executeQuery",
            "insert",
            "update",
            "delete"
          ],
          "default": "insert"
        },
        "query": {
          "description": "The SQL query to execute",
          "type": "string",
          "default": "",
          "examples": [
            "SELECT id, name FROM product WHERE id < 40"
          ]
        },
        "table": {
          "description": "Name of the table in which to delete data",
          "type": "string",
          "default": ""
        },
        "columns": {
          "description": "Comma-separated list of the properties which should used as columns for rows to update",
          "type": "string",
          "default": "",
          "examples": [
            "name,description"
          ]
        },
        "updateKey": {
          "description": "Name of the property which decides which rows in the database should be updated. Normally that would be \"id\".",
          "type": "string",
          "default": "id"
        },
        "deleteKey": {
          "description": "Name of the property which decides which rows in the database should be deleted. Normally that would be \"id\".",
          "type": "string",
          "default": "id"
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
    "version": [
      "1",
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "microsoftSql",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
