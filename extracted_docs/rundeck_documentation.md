---
title: "Node: Rundeck"
slug: "node-rundeck"
version: "1"
updated: "2025-11-13"
summary: "Manage Rundeck API"
node_type: "regular"
group: "['transform']"
---

# Node: Rundeck

**Purpose.** Manage Rundeck API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:rundeck.png`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **rundeckApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `rundeckApi` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Execute | `execute` | Execute a job |
| Get Metadata | `getMetadata` | Get metadata of a job |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | job | ✗ | Resource to operate on |  |

**Resource options:**

* **Job** (`job`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | execute | ✗ | Execute a job |  |

**Operation options:**

* **Execute** (`execute`) - Execute a job
* **Get Metadata** (`getMetadata`) - Get metadata of a job

---

### Execute parameters (`execute`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Job ID | `jobid` | string |  | ✓ | The job ID to execute | e.g. Rundeck Job ID |  |
| Arguments | `arguments` | fixedCollection | {} | ✗ | e.g. Add Argument |  |

<details>
<summary><strong>Arguments sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Arguments | `arguments` |  |  |  |

</details>

| Filter | `filter` | string |  | ✗ | Filter Rundeck nodes by name | e.g. Add Filters |  |

### Get Metadata parameters (`getMetadata`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Job ID | `jobid` | string |  | ✓ | The job ID to get metadata off | e.g. Rundeck Job ID |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ": " + $parameter["resource"]}}`

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
* Categories: Communication, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: rundeck
displayName: Rundeck
description: Manage Rundeck API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: rundeckApi
  required: true
operations:
- id: execute
  name: Execute
  description: Execute a job
  params:
  - id: jobid
    name: Job ID
    type: string
    default: ''
    required: true
    description: The job ID to execute
    placeholder: Rundeck Job ID
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - getMetadata
          resource:
          - job
    typeInfo: &id002
      type: string
      displayName: Job ID
      name: jobid
  - id: arguments
    name: Arguments
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Argument
    validation:
      displayOptions:
        show:
          operation:
          - execute
          resource:
          - job
    typeInfo:
      type: fixedCollection
      displayName: Arguments
      name: arguments
      typeOptions:
        multipleValues: true
      subProperties:
      - name: arguments
        displayName: Arguments
        values:
        - displayName: Name
          name: name
          type: string
          default: ''
        - displayName: Value
          name: value
          type: string
          default: ''
  - id: filter
    name: Filter
    type: string
    default: ''
    required: false
    description: Filter Rundeck nodes by name
    placeholder: Add Filters
    validation:
      displayOptions:
        show:
          operation:
          - execute
          resource:
          - job
    typeInfo:
      type: string
      displayName: Filter
      name: filter
- id: getMetadata
  name: Get Metadata
  description: Get metadata of a job
  params:
  - id: jobid
    name: Job ID
    type: string
    default: ''
    required: true
    description: The job ID to get metadata off
    placeholder: Rundeck Job ID
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: jobid
    text: Rundeck Job ID
  - field: arguments
    text: Add Argument
  - field: filter
    text: Add Filters
  - field: jobid
    text: Rundeck Job ID
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
  "$id": "https://n8n.io/schemas/nodes/rundeck.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Rundeck Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "execute",
        "getMetadata"
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
            "job"
          ],
          "default": "job"
        },
        "operation": {
          "description": "Execute a job",
          "type": "string",
          "enum": [
            "execute",
            "getMetadata"
          ],
          "default": "execute"
        },
        "jobid": {
          "description": "The job ID to get metadata off",
          "type": "string",
          "default": "",
          "examples": [
            "Rundeck Job ID"
          ]
        },
        "arguments": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Argument"
          ]
        },
        "filter": {
          "description": "Filter Rundeck nodes by name",
          "type": "string",
          "default": "",
          "examples": [
            "Add Filters"
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
      "name": "rundeckApi",
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
