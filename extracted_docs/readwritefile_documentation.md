---
title: "Node: Read/Write Files from Disk"
slug: "node-readwritefile"
version: "1"
updated: "2025-11-13"
summary: "Read or write files from the computer that runs n8n"
node_type: "regular"
group: "['input']"
---

# Node: Read/Write Files from Disk

**Purpose.** Read or write files from the computer that runs n8n


---

## Node Details

- **Icon:** `file:readWriteFile.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **info**: Use this node to read and write files on the same computer running n8n. To handle files between different computers please use other nodes (e.g. FTP, HTTP Request, AWS).

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Read File(s) From Disk | `read` | Retrieve one or more files from the computer that runs n8n |
| Write File to Disk | `write` | Create a binary file on the computer that runs n8n |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | read | ✗ | Retrieve one or more files from the computer that runs n8n |  |

**Operation options:**

* **Read File(s) From Disk** (`read`) - Retrieve one or more files from the computer that runs n8n
* **Write File to Disk** (`write`) - Create a binary file on the computer that runs n8n

---

### Read File(s) From Disk parameters (`read`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File(s) Selector | `fileSelector` | string |  | ✓ | Specify a file's path or path pattern to read multiple files. Always use forward-slashes for path separator even on Windows. | e.g. e.g. /home/user/Pictures/**/*.png |  |
| Options | `options` | collection | {} | ✗ | Extension of the file in the output binary | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Extension | `fileExtension` | string |  | Extension of the file in the output binary |
| File Name | `fileName` | string |  | Name of the file in the output binary |
| Mime Type | `mimeType` | string |  | Mime type of the file in the output binary |
| Put Output File in Field | `dataPropertyName` | string | data | By default 'data' is used |

</details>


### Write File to Disk parameters (`write`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Path and Name | `fileName` | string |  | ✓ | Path and name of the file that should be written. Also include the file extension. | e.g. e.g. /data/example.jpg |  |
| Input Binary Field | `dataPropertyName` | string | data | ✓ | e.g. e.g. data |  |

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Read from Disk

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "fileSelector": "C:/Test/image.jpg",
  "options": {}
}
```

### Example 2: Write to Disk

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "operation": "write",
  "fileName": "C:/Test/image-written.jpg",
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
* Aliases: Binary, File, Text, Open, Import, Save, Export, Disk, Transfer

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: readWriteFile
displayName: Read/Write Files from Disk
description: Read or write files from the computer that runs n8n
version: '1'
nodeType: regular
group:
- input
operations:
- id: read
  name: Read File(s) From Disk
  description: Retrieve one or more files from the computer that runs n8n
  params:
  - id: fileSelector
    name: File(s) Selector
    type: string
    default: ''
    required: true
    description: Specify a file's path or path pattern to read multiple files. Always
      use forward-slashes for path separator even on Windows.
    hint: Supports patterns, learn more <a href="https://github.com/micromatch/picomatch#basic-globbing"
      target="_blank">here</a>
    placeholder: e.g. /home/user/Pictures/**/*.png
    validation:
      required: true
    typeInfo:
      type: string
      displayName: File(s) Selector
      name: fileSelector
- id: write
  name: Write File to Disk
  description: Create a binary file on the computer that runs n8n
  params:
  - id: fileName
    name: File Path and Name
    type: string
    default: ''
    required: true
    description: Path and name of the file that should be written. Also include the
      file extension.
    placeholder: e.g. /data/example.jpg
    validation:
      required: true
    typeInfo:
      type: string
      displayName: File Path and Name
      name: fileName
  - id: dataPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be written
    placeholder: e.g. data
    validation:
      required: true
    typeInfo:
      type: string
      displayName: Input Binary Field
      name: dataPropertyName
examples:
- name: Read from Disk
  parameters:
    fileSelector: C:/Test/image.jpg
    options: {}
  workflow: Unnamed workflow
- name: Write to Disk
  parameters:
    operation: write
    fileName: C:/Test/image-written.jpg
    options: {}
  workflow: Unnamed workflow
ui_elements:
  notices:
  - name: info
    text: Use this node to read and write files on the same computer running n8n.
      To handle files between different computers please use other nodes (e.g. FTP,
      HTTP Request, AWS).
    conditions: null
  tooltips: []
  placeholders:
  - field: fileSelector
    text: e.g. /home/user/Pictures/**/*.png
  - field: options
    text: Add option
  - field: fileName
    text: e.g. /data/example.jpg
  - field: dataPropertyName
    text: e.g. data
  hints:
  - field: fileSelector
    text: Supports patterns, learn more <a href="https://github.com/micromatch/picomatch#basic-globbing"
      target="_blank">here</a>
  - field: options
    text: The name of the output binary field to put the file in
  - field: dataPropertyName
    text: The name of the input binary field containing the file to be written
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
  "$id": "https://n8n.io/schemas/nodes/readWriteFile.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Read/Write Files from Disk Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "read",
        "write"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Retrieve one or more files from the computer that runs n8n",
          "type": "string",
          "enum": [
            "read",
            "write"
          ],
          "default": "read"
        },
        "fileSelector": {
          "description": "Specify a file's path or path pattern to read multiple files. Always use forward-slashes for path separator even on Windows.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. /home/user/Pictures/**/*.png"
          ]
        },
        "options": {
          "description": "Extension of the file in the output binary",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "fileName": {
          "description": "Path and name of the file that should be written. Also include the file extension.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. /data/example.jpg"
          ]
        },
        "dataPropertyName": {
          "description": "",
          "type": "string",
          "default": "data",
          "examples": [
            "e.g. data"
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
      "description": "Read from Disk",
      "value": {
        "fileSelector": "C:/Test/image.jpg",
        "options": {}
      }
    },
    {
      "description": "Write to Disk",
      "value": {
        "operation": "write",
        "fileName": "C:/Test/image-written.jpg",
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
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
