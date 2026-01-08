---
title: "Node: Simulate"
slug: "node-simulate"
version: "1"
updated: "2026-01-08"
summary: "Simulate a node"
node_type: "regular"
group: "['organization']"
---

# Node: Simulate

**Purpose.** Simulate a node
**Subtitle.** ={{$parameter.subtitle || undefined}}


---

## Node Details

- **Icon:** `fa:arrow-right`
- **Group:** `['organization']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Output | `output` | options | all | ✗ |  |  |

**Output options:**

* **Returns all input items** (`all`)
* **Specify how many of input items to return** (`specify`)
* **Specify output as JSON** (`custom`)

| Number of Items | `numberOfItems` | number | 1 | ✗ | Number input of items to return, if greater then input length all items will be returned | min:1, max:∞ |
| Icon to Display on Canvas | `icon` | options | n8n-nodes-base.noOp | ✗ | Select a type of node to show corresponding icon |  |
| Subtitle | `subtitle` | string |  | ✗ | e.g. e.g. 'record: read' |  |
| JSON | `jsonOutput` | json | [\n  {\n   | ✗ |  |  |
| Execution Duration (MS) | `executionDuration` | number | 150 | ✗ | Execution duration in milliseconds | min:0, max:∞ |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `{{$parameter.subtitle || undefined}}`
- `={{$parameter.subtitle || undefined}}`

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
* Aliases: placeholder, stub, dummy

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: simulate
displayName: Simulate
description: Simulate a node
version: '1'
nodeType: regular
group:
- organization
params:
- id: output
  name: Output
  type: options
  default: all
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Output
    name: output
    possibleValues:
    - value: all
      name: Returns all input items
      description: ''
    - value: specify
      name: Specify how many of input items to return
      description: ''
    - value: custom
      name: Specify output as JSON
      description: ''
- id: numberOfItems
  name: Number of Items
  type: number
  default: 1
  required: false
  description: Number input of items to return, if greater then input length all items
    will be returned
  validation:
    displayOptions:
      show:
        output:
        - specify
  typeInfo:
    type: number
    displayName: Number of Items
    name: numberOfItems
    typeOptions:
      minValue: 1
- id: icon
  name: Icon to Display on Canvas
  type: options
  default: n8n-nodes-base.noOp
  required: false
  description: Select a type of node to show corresponding icon
  typeInfo:
    type: options
    displayName: Icon to Display on Canvas
    name: icon
    typeOptions:
      loadOptionsMethod: getNodeTypes
    possibleValues: []
- id: subtitle
  name: Subtitle
  type: string
  default: ''
  required: false
  description: ''
  placeholder: 'e.g. ''record: read'''
  typeInfo:
    type: string
    displayName: Subtitle
    name: subtitle
- id: jsonOutput
  name: JSON
  type: json
  default: '[\n  {\n  '
  required: false
  description: ''
  typeInfo:
    type: json
    displayName: JSON
    name: jsonOutput
    typeOptions:
      rows: 5
- id: executionDuration
  name: Execution Duration (MS)
  type: number
  default: 150
  required: false
  description: Execution duration in milliseconds
  typeInfo:
    type: number
    displayName: Execution Duration (MS)
    name: executionDuration
    typeOptions:
      minValue: 0
common_expressions:
- '{{$parameter.subtitle || undefined}}'
- ={{$parameter.subtitle || undefined}}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: subtitle
    text: 'e.g. ''record: read'''
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
  "$id": "https://n8n.io/schemas/nodes/simulate.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Simulate Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "output": {
          "description": "",
          "type": "string",
          "enum": [
            "all",
            "specify",
            "custom"
          ],
          "default": "all"
        },
        "numberOfItems": {
          "description": "Number input of items to return, if greater then input length all items will be returned",
          "type": "number",
          "default": 1
        },
        "icon": {
          "description": "Select a type of node to show corresponding icon",
          "type": "string",
          "default": "n8n-nodes-base.noOp"
        },
        "subtitle": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. 'record: read'"
          ]
        },
        "jsonOutput": {
          "description": "",
          "type": "string",
          "default": "[\\n  {\\n  "
        },
        "executionDuration": {
          "description": "Execution duration in milliseconds",
          "type": "number",
          "default": 150
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
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
