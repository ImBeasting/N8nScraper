---
title: "Node: If"
slug: "node-if"
version: "['2', '2.1', '2.2', '2.3']"
updated: "2026-01-08"
summary: "Route items to different branches (true/false)"
node_type: "regular"
group: "['transform']"
---

# Node: If

**Purpose.** Route items to different branches (true/false)


---

## Node Details

- **Icon:** `fa:map-signs`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main', 'Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Conditions | `conditions` | filter | {} | ✗ | e.g. Add Condition |  |
| Options | `options` | collection | {} | ✗ | Whether to ignore letter case when evaluating conditions | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Ignore Case | `ignoreCase` | boolean | True | Whether to ignore letter case when evaluating conditions |

</details>

| Convert types where required | `looseTypeValidation` | boolean | True | ✗ | If the type of an expression doesn't match the type of the comparison, n8n will try to cast the expression to the required type. E.g. for booleans <code>"false"</code> or <code>0</code> will be cast to <code>false</code> |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{!$parameter.options.ignoreCase}}`
- `={{ $nodeVersion >= 2.3 ? 3 : $nodeVersion >= 2.2 ? 2 : 1 }}`

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
node: If
displayName: If
description: Route items to different branches (true/false)
version:
- '2'
- '2.1'
- '2.2'
- '2.3'
nodeType: regular
group:
- transform
params:
- id: conditions
  name: Conditions
  type: filter
  default: {}
  required: false
  description: ''
  placeholder: Add Condition
  typeInfo:
    type: filter
    displayName: Conditions
    name: conditions
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to ignore letter case when evaluating conditions
  placeholder: Add option
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Ignore Case
      name: ignoreCase
      type: boolean
      description: Whether to ignore letter case when evaluating conditions
      default: true
- id: looseTypeValidation
  name: Convert types where required
  type: boolean
  default: true
  required: false
  description: If the type of an expression doesn't match the type of the comparison,
    n8n will try to cast the expression to the required type. E.g. for booleans <code>"false"</code>
    or <code>0</code> will be cast to <code>false</code>
  typeInfo:
    type: boolean
    displayName: Convert types where required
    name: looseTypeValidation
common_expressions:
- ={{!$parameter.options.ignoreCase}}
- '={{ $nodeVersion >= 2.3 ? 3 : $nodeVersion >= 2.2 ? 2 : 1 }}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: conditions
    text: Add Condition
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/If.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "If Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "conditions": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Condition"
          ]
        },
        "options": {
          "description": "Whether to ignore letter case when evaluating conditions",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "looseTypeValidation": {
          "description": "If the type of an expression doesn't match the type of the comparison, n8n will try to cast the expression to the required type. E.g. for booleans <code>\"false\"</code> or <code>0</code> will be cast to <code>false</code>",
          "type": "boolean",
          "default": true
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
      "2.3"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2', '2.1', '2.2', '2.3'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
