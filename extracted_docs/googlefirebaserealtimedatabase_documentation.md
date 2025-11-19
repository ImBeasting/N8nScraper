---
title: "Node: Google Cloud Realtime Database"
slug: "node-googlefirebaserealtimedatabase"
version: "1"
updated: "2025-11-13"
summary: "Interact with Google Firebase - Realtime Database API"
node_type: "regular"
group: "['input']"
---

# Node: Google Cloud Realtime Database

**Purpose.** Interact with Google Firebase - Realtime Database API
**Subtitle.** ={{$parameter["operation"]}}


---

## Node Details

- **Icon:** `file:googleFirebaseRealtimeDatabase.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleFirebaseRealtimeDatabaseOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleFirebaseRealtimeDatabaseOAuth2Api` | Optional | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Write data to a database |
| Delete | `delete` | Delete data from a database |
| Get | `get` | Get a record from a database |
| Push | `push` | Append to a list of data |
| Update | `update` | Update item on a database |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✓ | Write data to a database |  |

**Operation options:**

* **Create** (`create`) - Write data to a database
* **Delete** (`delete`) - Delete data from a database
* **Get** (`get`) - Get a record from a database
* **Push** (`push`) - Append to a list of data
* **Update** (`update`) - Update item on a database

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Columns / Attributes | `attributes` | string |  | ✓ | Attributes to save | e.g. age, name, city |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Object Path | `path` | string |  | ✗ | Object path on database. Do not append .json. | e.g. e.g. /app/users |  |

### Push parameters (`push`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Columns / Attributes | `attributes` | string |  | ✓ | Attributes to save | e.g. age, name, city |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Columns / Attributes | `attributes` | string |  | ✓ | Attributes to save | e.g. age, name, city |  |

---

## Load Options Methods

- `getProjects`

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
node: googleFirebaseRealtimeDatabase
displayName: Google Cloud Realtime Database
description: Interact with Google Firebase - Realtime Database API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: googleFirebaseRealtimeDatabaseOAuth2Api
  required: false
operations:
- id: create
  name: Create
  description: Write data to a database
  params:
  - id: attributes
    name: Columns / Attributes
    type: string
    default: ''
    required: true
    description: Attributes to save
    placeholder: age, name, city
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - create
          - push
          - update
    typeInfo: &id002
      type: string
      displayName: Columns / Attributes
      name: attributes
- id: delete
  name: Delete
  description: Delete data from a database
- id: get
  name: Get
  description: Get a record from a database
  params:
  - id: path
    name: Object Path
    type: string
    default: ''
    required: false
    description: Object path on database. Do not append .json.
    hint: Leave blank to get a whole database object
    placeholder: e.g. /app/users
    validation:
      displayOptions:
        show:
          operation:
          - get
    typeInfo:
      type: string
      displayName: Object Path
      name: path
- id: push
  name: Push
  description: Append to a list of data
  params:
  - id: attributes
    name: Columns / Attributes
    type: string
    default: ''
    required: true
    description: Attributes to save
    placeholder: age, name, city
    validation: *id001
    typeInfo: *id002
- id: update
  name: Update
  description: Update item on a database
  params:
  - id: attributes
    name: Columns / Attributes
    type: string
    default: ''
    required: true
    description: Attributes to save
    placeholder: age, name, city
    validation: *id001
    typeInfo: *id002
common_expressions:
- ={{$parameter["operation"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: path
    text: e.g. /app/users
  - field: path
    text: e.g. /app/users
  - field: attributes
    text: age, name, city
  hints:
  - field: path
    text: Leave blank to get a whole database object
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
  "$id": "https://n8n.io/schemas/nodes/googleFirebaseRealtimeDatabase.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Cloud Realtime Database Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "get",
        "push",
        "update"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "projectId": {
          "description": "As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "operation": {
          "description": "Write data to a database",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "push",
            "update"
          ],
          "default": "create"
        },
        "path": {
          "description": "Object path on database. Do not append .json.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. /app/users"
          ]
        },
        "attributes": {
          "description": "Attributes to save",
          "type": "string",
          "default": "",
          "examples": [
            "age, name, city"
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
      "name": "googleFirebaseRealtimeDatabaseOAuth2Api",
      "required": false
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
