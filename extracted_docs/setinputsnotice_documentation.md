---
title: "Node: For adding columns from your dataset to the evaluation results. Anything you add here will be displayed in the ‘evaluations’ tab, not on the Google Sheet or Data table."
slug: "node-setinputsnotice"
version: "1.0"
updated: "2025-11-13"
summary: "The expected output defined in your evaluation dataset, used as ground truth"
node_type: "regular"
---

# Node: For adding columns from your dataset to the evaluation results. Anything you add here will be displayed in the ‘evaluations’ tab, not on the Google Sheet or Data table.

**Purpose.** The expected output defined in your evaluation dataset, used as ground truth


---

## Node Details

- **Icon:** ``
- **Group:** `[]`
- **Inputs:** `[]`
- **Outputs:** `[]`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **setInputsNotice** when operation=['setInputs']: For adding columns from your dataset to the evaluation results. Anything you add here will be displayed in the ‘evaluations’ tab, not on the Google Sheet or Data table.

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Inputs | `inputs` | fixedCollection | {} | ✗ | e.g. Add Input |  |

<details>
<summary><strong>Inputs sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filter | `values` |  |  |  |

</details>


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
node: setInputsNotice
displayName: For adding columns from your dataset to the evaluation results. Anything
  you add here will be displayed in the ‘evaluations’ tab, not on the Google Sheet
  or Data table.
description: The expected output defined in your evaluation dataset, used as ground
  truth
version: '1.0'
nodeType: regular
params:
- id: inputs
  name: Inputs
  type: fixedCollection
  default: {}
  required: false
  description: ''
  placeholder: Add Input
  validation:
    displayOptions:
      show:
        operation:
        - setInputs
  typeInfo:
    type: fixedCollection
    displayName: Inputs
    name: inputs
    typeOptions:
      multipleValues: true
    subProperties:
    - name: values
      displayName: Filter
      values:
      - displayName: Name
        name: inputName
        type: string
        default: ''
      - displayName: Value
        name: inputValue
        type: string
        default: ''
ui_elements:
  notices:
  - name: setInputsNotice
    text: For adding columns from your dataset to the evaluation results. Anything
      you add here will be displayed in the ‘evaluations’ tab, not on the Google Sheet
      or Data table.
    conditions:
      show:
        operation:
        - setInputs
  tooltips: []
  placeholders:
  - field: inputs
    text: Add Input
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
  "$id": "https://n8n.io/schemas/nodes/setInputsNotice.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "For adding columns from your dataset to the evaluation results. Anything you add here will be displayed in the \u2018evaluations\u2019 tab, not on the Google Sheet or Data table. Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "inputs": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Input"
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
    "version": "1.0"
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1.0 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
