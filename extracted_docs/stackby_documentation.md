---
title: "Node: Stackby"
slug: "node-stackby"
version: "1"
updated: "2025-11-13"
summary: "Read, write, and delete data in Stackby"
node_type: "regular"
group: "['transform']"
---

# Node: Stackby

**Purpose.** Read, write, and delete data in Stackby


---

## Node Details

- **Icon:** `file:stackby.png`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **stackbyApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `stackbyApi` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Append | `append` |  |
| Delete | `delete` |  |
| List | `list` |  |
| Read | `read` |  |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | append | ✗ | Operation to perform |  |

**Operation options:**

* **Append** (`append`)
* **Delete** (`delete`)
* **List** (`list`)
* **Read** (`read`)

---

### Append parameters (`append`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Columns | `columns` | string |  | ✓ | Comma-separated list of the properties which should used as columns for the new rows | e.g. id,name,description |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | ID of the record to return |  |

### List parameters (`list`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | True | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 1000 | ✗ | Max number of results to return | min:1, max:1000 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The name or ID of a view in the Stories table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| View | `view` | string |  | The name or ID of a view in the Stories table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view. |

</details>


### Read parameters (`read`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | ID of the record to return |  |

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
node: stackby
displayName: Stackby
description: Read, write, and delete data in Stackby
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: stackbyApi
  required: true
operations:
- id: append
  name: Append
  description: ''
  params:
  - id: columns
    name: Columns
    type: string
    default: ''
    required: true
    description: Comma-separated list of the properties which should used as columns
      for the new rows
    placeholder: id,name,description
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - append
    typeInfo:
      type: string
      displayName: Columns
      name: columns
- id: delete
  name: Delete
  description: ''
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: ID of the record to return
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - read
          - delete
    typeInfo: &id002
      type: string
      displayName: ID
      name: id
- id: list
  name: List
  description: ''
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
          - list
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 1000
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - list
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 1000
- id: read
  name: Read
  description: ''
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: ID of the record to return
    validation: *id001
    typeInfo: *id002
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: operation
    text: Action to perform
  - field: table
    text: Stories
  - field: additionalFields
    text: Add Field
  - field: columns
    text: id,name,description
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
  "$id": "https://n8n.io/schemas/nodes/stackby.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Stackby Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "append",
        "delete",
        "list",
        "read"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "append",
            "delete",
            "list",
            "read"
          ],
          "default": "append",
          "examples": [
            "Action to perform"
          ]
        },
        "stackId": {
          "description": "The ID of the stack to access",
          "type": "string",
          "default": ""
        },
        "table": {
          "description": "Enter Table Name",
          "type": "string",
          "default": "",
          "examples": [
            "Stories"
          ]
        },
        "id": {
          "description": "ID of the record to return",
          "type": "string",
          "default": ""
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": true
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 1000
        },
        "additionalFields": {
          "description": "The name or ID of a view in the Stories table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "columns": {
          "description": "Comma-separated list of the properties which should used as columns for the new rows",
          "type": "string",
          "default": "",
          "examples": [
            "id,name,description"
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
      "name": "stackbyApi",
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
