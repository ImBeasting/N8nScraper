---
title: "Node: MySQL"
slug: "node-mysql"
version: "['2', '2.1', '2.2', '2.3', '2.4', '2.5']"
updated: "2026-01-08"
summary: "Get, add and update data in MySQL"
node_type: "regular"
group: "['input']"
---

# Node: MySQL

**Purpose.** Get, add and update data in MySQL
**Subtitle.** ={{ $parameter["operation"] }}


---

## Node Details

- **Icon:** `{'light': 'file:mysql.svg', 'dark': 'file:mysql.dark.svg'}`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **mySql**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `mySql` | ✓ | - |

---

## Operations

### Database Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `deleteTable` | Delete an entire table or rows in a table |
| Execute SQL | `executeQuery` | Execute an SQL query |
| Insert | `insert` | Insert rows in a table |
| Insert or Update | `upsert` | Insert or update rows in a table |
| Select | `select` | Select rows from a table |
| Update | `update` | Update rows in a table |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | hidden | database | ✗ | Resource to operate on |  |
---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | insert | ✗ | Delete an entire table or rows in a table |  |

**Operation options:**

* **Delete** (`deleteTable`) - Delete an entire table or rows in a table
* **Execute SQL** (`executeQuery`) - Execute an SQL query
* **Insert** (`insert`) - Insert rows in a table
* **Insert or Update** (`upsert`) - Insert or update rows in a table
* **Select** (`select`) - Select rows from a table
* **Update** (`update`) - Update rows in a table

---

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter["operation"] }}`

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: mySql
displayName: MySQL
description: Get, add and update data in MySQL
version:
- '2'
- '2.1'
- '2.2'
- '2.3'
- '2.4'
- '2.5'
nodeType: regular
group:
- input
credentials:
- name: mySql
  required: true
operations:
- id: deleteTable
  name: Delete
  description: Delete an entire table or rows in a table
- id: executeQuery
  name: Execute SQL
  description: Execute an SQL query
- id: insert
  name: Insert
  description: Insert rows in a table
- id: upsert
  name: Insert or Update
  description: Insert or update rows in a table
- id: select
  name: Select
  description: Select rows from a table
- id: update
  name: Update
  description: Update rows in a table
common_expressions:
- ={{ $parameter["operation"] }}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: table
    text: Select a Table...
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
  "$id": "https://n8n.io/schemas/nodes/mySql.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MySQL Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "deleteTable",
        "executeQuery",
        "insert",
        "upsert",
        "select",
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
          "default": "database"
        },
        "operation": {
          "description": "Delete an entire table or rows in a table",
          "type": "string",
          "enum": [
            "deleteTable",
            "executeQuery",
            "insert",
            "upsert",
            "select",
            "update"
          ],
          "default": "insert"
        },
        "table": {
          "description": "The table you want to work on",
          "type": "string",
          "examples": [
            "Select a Table..."
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
    "version": [
      "2",
      "2.1",
      "2.2",
      "2.3",
      "2.4",
      "2.5"
    ]
  },
  "credentials": [
    {
      "name": "mySql",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2', '2.1', '2.2', '2.3', '2.4', '2.5'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
