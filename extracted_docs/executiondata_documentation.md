---
title: "Node: Execution Data"
slug: "node-executiondata"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Add execution data for search"
node_type: "regular"
group: "['input']"
---

# Node: Execution Data

**Purpose.** Add execution data for search


---

## Node Details

- **Icon:** `fa:tasks`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice**: Save important data using this node. It will be displayed on each execution for easy reference and you can filter by it.<br />Filtering is available on Pro and Enterprise plans. <a href='https://n8n.io/pricing/' target='_blank'>More Info</a>

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Save Highlight Data (for Search/review) | `save` |  |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | save | ✗ | Operation to perform |  |

**Operation options:**

* **Save Highlight Data (for Search/review)** (`save`) - Save Highlight Data (for search/review)

---

### Save Highlight Data (for Search/review) parameters (`save`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Data to Save | `dataToSave` | fixedCollection | {} | ✗ | e.g. Add Saved Field |  |

<details>
<summary><strong>Data to Save sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Values | `values` |  |  |  |

</details>


---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Execution Data

**From workflow:** [TEST] Execution Data

**Parameters:**
```json
{
  "dataToSave": {
    "values": [
      {
        "key": "id",
        "value": "={{ $json.id }}"
      }
    ]
  }
}
```


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter.dataToSave.values.some((x) => x.key.length > 50) }}`
- `{{ $parameter.dataToSave.values.some((x) => x.key.length > 50) }}`
- `={{ $parameter.dataToSave.values.some((x) => x.value.length > 512) }}`
- `{{ $parameter.dataToSave.values.some((x) => x.value.length > 512) }}`

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
* Categories: Development, Core Nodes
* Aliases: Filter, _Set, Data

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: executionData
displayName: Execution Data
description: Add execution data for search
version:
- '1'
- '1.1'
nodeType: regular
group:
- input
operations:
- id: save
  name: Save Highlight Data (for Search/review)
  description: ''
  params:
  - id: dataToSave
    name: Data to Save
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Saved Field
    validation:
      displayOptions:
        show:
          operation:
          - save
    typeInfo:
      type: fixedCollection
      displayName: Data to Save
      name: dataToSave
      typeOptions:
        multipleValues: true
      subProperties:
      - name: values
        displayName: Values
        values:
        - displayName: Key
          name: key
          type: string
          placeholder: e.g. myKey
          default: ''
        - displayName: Value
          name: value
          type: string
          placeholder: e.g. myValue
          default: ''
examples:
- name: Execution Data
  parameters:
    dataToSave:
      values:
      - key: id
        value: ={{ $json.id }}
  workflow: '[TEST] Execution Data'
common_expressions:
- ={{ $parameter.dataToSave.values.some((x) => x.key.length > 50) }}
- '{{ $parameter.dataToSave.values.some((x) => x.key.length > 50) }}'
- ={{ $parameter.dataToSave.values.some((x) => x.value.length > 512) }}
- '{{ $parameter.dataToSave.values.some((x) => x.value.length > 512) }}'
ui_elements:
  notices:
  - name: notice
    text: Save important data using this node. It will be displayed on each execution
      for easy reference and you can filter by it.<br />Filtering is available on
      Pro and Enterprise plans. <a href='https://n8n.io/pricing/' target='_blank'>More
      Info</a>
    conditions: null
  tooltips: []
  placeholders:
  - field: dataToSave
    text: Add Saved Field
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
  "$id": "https://n8n.io/schemas/nodes/executionData.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Execution Data Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "save"
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
            "save"
          ],
          "default": "save"
        },
        "dataToSave": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Saved Field"
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
  },
  "examples": [
    {
      "description": "Execution Data",
      "value": {
        "dataToSave": {
          "values": [
            {
              "key": "id",
              "value": "={{ $json.id }}"
            }
          ]
        }
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
