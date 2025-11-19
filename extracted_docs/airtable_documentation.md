---
title: "Node: Airtable"
slug: "node-airtable"
version: "['2', '2.1']"
updated: "2025-11-13"
summary: "Read, update, write and delete data from Airtable"
node_type: "regular"
group: "['input']"
---

# Node: Airtable

**Purpose.** Read, update, write and delete data from Airtable
**Subtitle.** ={{ $parameter["operation"] + ": " + $parameter["resource"] }}


---

## Node Details

- **Icon:** `file:airtable.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **airtableTokenApi**: N/A
- **airtableOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `airtableTokenApi` | ✓ | {'show': {'authentication': ['airtableTokenApi']}} |
| `airtableOAuth2Api` | ✓ | {'show': {'authentication': ['airtableOAuth2Api']}} |

---

## Operations

### Record Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new record in a table |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `deleteRecord` | Delete a record from a table |
| Get | `get` | Retrieve a record from a table |
| Search | `search` | Search for specific records or list all |
| Update | `update` | Update a record in a table |

### Base Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getMany` | List all the bases |
| Get Schema | `getSchema` | Get the schema of the tables in a base |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | record | ✗ | Resource to operate on |  |

**Resource options:**

* **Base** (`base`)
* **Record** (`record`)
* **Table** (`table`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Create a new record in a table |  |

**Operation options:**

* **Create** (`create`) - Create a new record in a table
* **Create or Update** (`upsert`) - Create a new record, or update the current one if it already exists (upsert)
* **Delete** (`deleteRecord`) - Delete a record from a table
* **Get** (`get`) - Retrieve a record from a table
* **Search** (`search`) - Search for specific records or list all
* **Update** (`update`) - Update a record in a table

---

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter["operation"] + ": " + $parameter["resource"] }}`

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
node: airtable
displayName: Airtable
description: Read, update, write and delete data from Airtable
version:
- '2'
- '2.1'
nodeType: regular
group:
- input
credentials:
- name: airtableTokenApi
  required: true
- name: airtableOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a new record in a table
- id: upsert
  name: Create or Update
  description: Create a new record, or update the current one if it already exists
    (upsert)
- id: deleteRecord
  name: Delete
  description: Delete a record from a table
- id: get
  name: Get
  description: Retrieve a record from a table
- id: search
  name: Search
  description: Search for specific records or list all
- id: update
  name: Update
  description: Update a record in a table
- id: getMany
  name: Get Many
  description: List all the bases
- id: getSchema
  name: Get Schema
  description: Get the schema of the tables in a base
common_expressions:
- '={{ $parameter["operation"] + ": " + $parameter["resource"] }}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: base
    text: e.g. https://airtable.com/app12DiScdfes/tbl9WvGeEPa6lZyVq/viwHdfasdfeieg5p
  - field: table
    text: https://airtable.com/app12DiScdfes/tblAAAAAAAAAAAAA/viwHdfasdfeieg5p
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
  "$id": "https://n8n.io/schemas/nodes/airtable.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Airtable Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "upsert",
        "deleteRecord",
        "get",
        "search",
        "update",
        "getMany",
        "getSchema"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "airtableTokenApi",
            "airtableOAuth2Api"
          ],
          "default": "airtableTokenApi"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "base",
            "record",
            "table"
          ],
          "default": "record"
        },
        "operation": {
          "description": "List all the bases",
          "type": "string",
          "enum": [
            "getMany",
            "getSchema"
          ],
          "default": "getMany"
        },
        "base": {
          "description": "The Airtable Base in which to operate on",
          "type": "string",
          "examples": [
            "e.g. https://airtable.com/app12DiScdfes/tbl9WvGeEPa6lZyVq/viwHdfasdfeieg5p"
          ]
        },
        "table": {
          "description": "",
          "type": "string",
          "examples": [
            "https://airtable.com/app12DiScdfes/tblAAAAAAAAAAAAA/viwHdfasdfeieg5p"
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
      "2.1"
    ]
  },
  "credentials": [
    {
      "name": "airtableTokenApi",
      "required": true
    },
    {
      "name": "airtableOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2', '2.1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
