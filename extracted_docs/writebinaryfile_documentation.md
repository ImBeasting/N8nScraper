---
title: "Node: Write Binary File"
slug: "node-writebinaryfile"
version: "1"
updated: "2026-01-08"
summary: "Writes a binary file to disk"
node_type: "regular"
group: "['output']"
---

# Node: Write Binary File

**Purpose.** Writes a binary file to disk


---

## Node Details

- **Icon:** `fa:file-export`
- **Group:** `['output']`
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
| File Name | `fileName` | string |  | ✓ | Path to which the file should be written | e.g. /data/example.jpg |  |
| Property Name | `dataPropertyName` | string | data | ✓ | Name of the binary property which contains the data for the file to be written |  |
| Options | `options` | collection | {} | ✗ | Whether to append to an existing file | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Append | `append` | boolean | False | Whether to append to an existing file |

</details>


---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Write Binary File

**From workflow:** Write Binary File unit test

**Parameters:**
```json
{
  "fileName": "C:\\Test\\image-written.jpg",
  "options": {}
}
```


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
* Aliases: Text, Save, Export

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: writeBinaryFile
displayName: Write Binary File
description: Writes a binary file to disk
version: '1'
nodeType: regular
group:
- output
params:
- id: fileName
  name: File Name
  type: string
  default: ''
  required: true
  description: Path to which the file should be written
  placeholder: /data/example.jpg
  validation:
    required: true
  typeInfo:
    type: string
    displayName: File Name
    name: fileName
- id: dataPropertyName
  name: Property Name
  type: string
  default: data
  required: true
  description: Name of the binary property which contains the data for the file to
    be written
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Property Name
    name: dataPropertyName
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to append to an existing file
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Append
      name: append
      type: boolean
      description: Whether to append to an existing file
      default: false
examples:
- name: Write Binary File
  parameters:
    fileName: C:\Test\image-written.jpg
    options: {}
  workflow: Write Binary File unit test
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: fileName
    text: /data/example.jpg
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
  "$id": "https://n8n.io/schemas/nodes/writeBinaryFile.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Write Binary File Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "fileName": {
          "description": "Path to which the file should be written",
          "type": "string",
          "default": "",
          "examples": [
            "/data/example.jpg"
          ]
        },
        "dataPropertyName": {
          "description": "Name of the binary property which contains the data for the file to be written",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "Whether to append to an existing file",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
  "examples": [
    {
      "description": "Write Binary File",
      "value": {
        "fileName": "C:\\Test\\image-written.jpg",
        "options": {}
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
