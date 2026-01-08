---
title: "Node: Data table"
slug: "node-datatable"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Permanently save data across workflow executions in a table"
node_type: "regular"
group: "['input', 'transform']"
---

# Node: Data table

**Purpose.** Permanently save data across workflow executions in a table
**Subtitle.** ={{$parameter["action"]}}


---

## Node Details

- **Icon:** `fa:table`
- **Group:** `['input', 'transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **deleteWarning**: This will permanently delete the data table and all its data. This action cannot be undone.

---

## Operations

### Row Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `` | Delete row(s) |
| Get | `` | Get row(s) |
| If Row Exists | `` | Match input items that are in the data table |
| If Row Does Not Exist | `` | Match input items that are not in the data table |
| Insert | `` | Insert a new row |
| Update | `` | Update row(s) matching certain fields |
| Upsert | `` | Update row(s), or insert if there is no match |

### Table Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `` | Create a new data table |
| Delete | `` | Delete a data table |
| List | `` | List all data tables |
| Update | `` | Update a data table name |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | row | ✗ | Resource to operate on |  |

**Resource options:**

* **Row** (`row`)
* **Table** (`table`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | insert | ✗ | Delete row(s) |  |

**Operation options:**

* **Delete** (``) - Delete row(s)
* **Get** (``) - Get row(s)
* **If Row Exists** (``) - Match input items that are in the data table
* **If Row Does Not Exist** (``) - Match input items that are not in the data table
* **Insert** (``) - Insert a new row
* **Update** (``) - Update row(s) matching certain fields
* **Upsert** (``) - Update row(s), or insert if there is no match

---

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["action"]}}`
- `={{ $parameter.dataTableId !== "" && $parameter?.columns?.mappingMode === "defineBelow" && !$parameter?.columns?.schema?.length }}`
- `{{ $parameter.dataTableId !== "" && $parameter?.columns?.mappingMode === "defineBelow" && !$parameter?.columns?.schema?.length }}`

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
* Categories: Core Nodes, Development
* Aliases: data, table, knowledge, data table, table, sheet, database, data base, mysql, postgres, postgresql, airtable, supabase, noco, notion

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: dataTable
displayName: Data table
description: Permanently save data across workflow executions in a table
version:
- '1'
- '1.1'
nodeType: regular
group:
- input
- transform
operations:
- id: ''
  name: Delete
  description: Delete row(s)
- id: ''
  name: Get
  description: Get row(s)
- id: ''
  name: If Row Exists
  description: Match input items that are in the data table
- id: ''
  name: If Row Does Not Exist
  description: Match input items that are not in the data table
- id: ''
  name: Insert
  description: Insert a new row
- id: ''
  name: Update
  description: Update row(s) matching certain fields
- id: ''
  name: Upsert
  description: Update row(s), or insert if there is no match
- id: ''
  name: Create
  description: Create a new data table
- id: ''
  name: List
  description: List all data tables
common_expressions:
- ={{$parameter["action"]}}
- ={{ $parameter.dataTableId !== "" && $parameter?.columns?.mappingMode === "defineBelow"
  && !$parameter?.columns?.schema?.length }}
- '{{ $parameter.dataTableId !== "" && $parameter?.columns?.mappingMode === "defineBelow"
  && !$parameter?.columns?.schema?.length }}'
ui_elements:
  notices:
  - name: deleteWarning
    text: This will permanently delete the data table and all its data. This action
      cannot be undone.
    conditions: null
  tooltips: []
  placeholders:
  - field: list
    text: e.g. My Table
  - field: options
    text: Add option
  - field: tableName
    text: e.g. My Data Table
  - field: columns
    text: Add Column
  - field: newName
    text: e.g. Renamed Data Table
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
  "$id": "https://n8n.io/schemas/nodes/dataTable.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Data table Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
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
            "row",
            "table"
          ],
          "default": "row"
        },
        "operation": {
          "description": "Create a new data table",
          "type": "string",
          "enum": [
            "Create",
            "Delete",
            "List",
            "Update"
          ],
          "default": "list"
        },
        "list": {
          "description": "",
          "type": "string",
          "examples": [
            "e.g. My Table"
          ]
        },
        "options": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number"
        },
        "tableName": {
          "description": "The name of the data table to create",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. My Data Table"
          ]
        },
        "columns": {
          "description": "The columns to create in the data table",
          "type": "string",
          "default": {},
          "examples": [
            "Add Column"
          ]
        },
        "newName": {
          "description": "The new name for the data table",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Renamed Data Table"
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
      "1",
      "1.1"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
