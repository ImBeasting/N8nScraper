---
title: "Node: E2E Test"
slug: "node-e2etest"
version: "1"
updated: "2025-11-13"
summary: "Dummy node used for e2e testing"
node_type: "regular"
group: "['output']"
---

# Node: E2E Test

**Purpose.** Dummy node used for e2e testing
**Subtitle.** ={{$parameter["operation"]}}


---

## Node Details

- **Icon:** `fa:play`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Remote Options | `remoteOptions` |  |
| Resource Locator | `resourceLocator` |  |
| Resource Mapping Component | `resourceMapper` |  |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | remoteOptions | ✗ | Operation to perform |  |

**Operation options:**

* **Remote Options** (`remoteOptions`)
* **Resource Locator** (`resourceLocator`)
* **Resource Mapping Component** (`resourceMapper`)

---

### Remote Options parameters (`remoteOptions`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Remote Options Name or ID | `remoteOptions` | options | [] | ✓ | Remote options to load. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Resource Locator parameters (`resourceLocator`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource Locator | `rlc` | resourceLocator |  | ✓ | e.g. https://example.com/user/a4071e98-7d40-41fb-8911-ce3e7bf94fb2 |  |

### Resource Mapping Component parameters (`resourceMapper`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource Mapping Component | `resourceMapper` | resourceMapper |  | ✓ |  |  |

---

## Load Options Methods

- `getOptions`

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
* Categories: Core Nodes

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: e2eTest
displayName: E2E Test
description: Dummy node used for e2e testing
version: '1'
nodeType: regular
group:
- output
operations:
- id: remoteOptions
  name: Remote Options
  description: ''
  params:
  - id: remoteOptions
    name: Remote Options Name or ID
    type: options
    default: []
    required: true
    description: Remote options to load. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - remoteOptions
    typeInfo:
      type: options
      displayName: Remote Options Name or ID
      name: remoteOptions
      typeOptions:
        loadOptionsMethod: getOptions
      possibleValues: []
- id: resourceLocator
  name: Resource Locator
  description: ''
  params:
  - id: rlc
    name: Resource Locator
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: https://example.com/user/a4071e98-7d40-41fb-8911-ce3e7bf94fb2
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - resourceLocator
    typeInfo:
      type: resourceLocator
      displayName: Resource Locator
      name: rlc
- id: resourceMapper
  name: Resource Mapping Component
  description: ''
  params:
  - id: resourceMapper
    name: Resource Mapping Component
    type: resourceMapper
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - resourceMapper
    typeInfo:
      type: resourceMapper
      displayName: Resource Mapping Component
      name: resourceMapper
common_expressions:
- ={{$parameter["operation"]}}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: rlc
    text: https://example.com/user/a4071e98-7d40-41fb-8911-ce3e7bf94fb2
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
  "$id": "https://n8n.io/schemas/nodes/e2eTest.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "E2E Test Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "remoteOptions",
        "resourceLocator",
        "resourceMapper"
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
            "remoteOptions",
            "resourceLocator",
            "resourceMapper"
          ],
          "default": "remoteOptions"
        },
        "fieldId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "remoteOptions": {
          "description": "Remote options to load. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "rlc": {
          "description": "",
          "type": "string",
          "examples": [
            "https://example.com/user/a4071e98-7d40-41fb-8911-ce3e7bf94fb2"
          ]
        },
        "resourceMapper": {
          "description": "",
          "type": "string"
        },
        "otherField": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "Resource 1": {
          "description": "",
          "type": "string"
        },
        "Resource 2": {
          "description": "",
          "type": "string"
        },
        "Resource 3": {
          "description": "",
          "type": "string"
        },
        "Hello World": {
          "description": "",
          "type": "string"
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
