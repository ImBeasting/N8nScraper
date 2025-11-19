---
title: "Node: PostBin"
slug: "node-postbin"
version: "1"
updated: "2025-11-13"
summary: "Consume PostBin API"
node_type: "regular"
group: "['transform']"
---

# Node: PostBin

**Purpose.** Consume PostBin API
**Subtitle.** ={{ $parameter["operation"] + ": " + $parameter["resource"] }}


---

## Node Details

- **Icon:** `file:postbin.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Operations

### Bin Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Request Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | bin | ✓ | Resource to operate on |  |

**Resource options:**

* **Bin** (`bin`)
* **Request** (`request`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | bin | ✓ |  |  |

**Resource options:**

* **Bin** (`bin`)
* **Request** (`request`)

| Operation | `operation` | options | create | ✗ | Create bin |  |
| Bin ID | `binId` | string |  | ✓ | Unique identifier for each bin |  |
| Operation | `operation` | options | get | ✗ | Get a request |  |
| Bin ID | `binId` | string |  | ✓ | Unique identifier for each bin |  |
| Bin Content | `binContent` | string |  | ✗ |  |  |
| Request ID | `requestId` | string |  | ✓ | Unique identifier for each request |  |

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
* Categories: Development, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: postbin
displayName: PostBin
description: Consume PostBin API
version: '1'
nodeType: regular
group:
- transform
params:
- id: resource
  name: Resource
  type: options
  default: bin
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: bin
      name: Bin
      description: ''
    - value: request
      name: Request
      description: ''
- id: operation
  name: Operation
  type: options
  default: create
  required: false
  description: Create bin
  validation: &id001
    displayOptions:
      show:
        resource:
        - request
  typeInfo: &id002
    type: options
    displayName: Operation
    name: operation
    possibleValues: []
- id: binId
  name: Bin ID
  type: string
  default: ''
  required: true
  description: Unique identifier for each bin
  validation: &id003
    required: true
    displayOptions:
      show:
        resource:
        - request
        operation:
        - get
        - removeFirst
        - send
  typeInfo: &id004
    type: string
    displayName: Bin ID
    name: binId
- id: operation
  name: Operation
  type: options
  default: get
  required: false
  description: Get a request
  validation: *id001
  typeInfo: *id002
- id: binId
  name: Bin ID
  type: string
  default: ''
  required: true
  description: Unique identifier for each bin
  validation: *id003
  typeInfo: *id004
- id: binContent
  name: Bin Content
  type: string
  default: ''
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        resource:
        - request
        operation:
        - send
  typeInfo:
    type: string
    displayName: Bin Content
    name: binContent
    typeOptions:
      rows: 5
- id: requestId
  name: Request ID
  type: string
  default: ''
  required: true
  description: Unique identifier for each request
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - request
        operation:
        - get
  typeInfo:
    type: string
    displayName: Request ID
    name: requestId
common_expressions:
- '={{ $parameter["operation"] + ": " + $parameter["resource"] }}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders: []
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
  "$id": "https://n8n.io/schemas/nodes/postbin.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "PostBin Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "bin",
            "request"
          ],
          "default": "bin"
        },
        "operation": {
          "description": "Get a request",
          "type": "string",
          "default": "get"
        },
        "binId": {
          "description": "Unique identifier for each bin",
          "type": "string",
          "default": ""
        },
        "binContent": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "requestId": {
          "description": "Unique identifier for each request",
          "type": "string",
          "default": ""
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
