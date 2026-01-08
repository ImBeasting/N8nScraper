---
title: "Node: Compression"
slug: "node-compression"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Compress and decompress files"
node_type: "regular"
group: "['transform']"
---

# Node: Compression

**Purpose.** Compress and decompress files
**Subtitle.** ={{$parameter["operation"]}}


---

## Node Details

- **Icon:** `fa:file-archive`
- **Group:** `['transform']`
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
| Compress | `compress` | Compress files into a zip or gzip archive |
| Decompress | `decompress` | Decompress zip or gzip archives |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | decompress | ✗ | Compress files into a zip or gzip archive |  |

**Operation options:**

* **Compress** (`compress`) - Compress files into a zip or gzip archive
* **Decompress** (`decompress`) - Decompress zip or gzip archives

---

### Compress parameters (`compress`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Input Binary Field(s) | `binaryPropertyName` | string | data | ✓ | To process more than one file, use a comma-separated list of the binary fields names | e.g. e.g. data,data2,data3 |  |
| Output Format | `outputFormat` | options |  | ✗ | Format of the output |  |

**Output Format options:**

* **Gzip** (`gzip`)
* **Zip** (`zip`)

| Output Format | `outputFormat` | options | zip | ✗ | Format of the output |  |

**Output Format options:**

* **Gzip** (`gzip`)
* **Zip** (`zip`)

| File Name | `fileName` | string |  | ✓ | Name of the output file | e.g. e.g. data.zip |  |
| Put Output File in Field | `binaryPropertyOutput` | string | data | ✗ | e.g. The name of the output binary field to put the file in |  |
| File Name | `fileName` | string |  | ✗ | Name of the output file | e.g. e.g. data.txt |  |
| Put Output File in Field | `binaryPropertyOutput` | string | data | ✗ | e.g. The name of the output binary field to put the file in |  |
| Output File Prefix | `outputPrefix` | string | data | ✓ | Prefix to add to the gzip file |  |

### Decompress parameters (`decompress`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Input Binary Field(s) | `binaryPropertyName` | string | data | ✓ | To process more than one file, use a comma-separated list of the binary fields names | e.g. e.g. data |  |
| Output Prefix | `outputPrefix` | string | file_ | ✓ | Prefix to add to the decompressed files |  |

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
* Categories: Core Nodes, Data & Storage
* Aliases: Zip, Gzip, uncompress, compress, decompress, archive, unarchive, Binary, Files, File

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: compression
displayName: Compression
description: Compress and decompress files
version:
- '1'
- '1.1'
nodeType: regular
group:
- transform
operations:
- id: compress
  name: Compress
  description: Compress files into a zip or gzip archive
  params:
  - id: binaryPropertyName
    name: Input Binary Field(s)
    type: string
    default: data
    required: true
    description: To process more than one file, use a comma-separated list of the
      binary fields names
    hint: The name of the input binary field(s) containing the file(s) to be compressed
    placeholder: e.g. data,data2,data3
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - decompress
    typeInfo: &id008
      type: string
      displayName: Input Binary Field(s)
      name: binaryPropertyName
  - id: outputFormat
    name: Output Format
    type: options
    default: ''
    required: false
    description: Format of the output
    validation: &id001
      displayOptions:
        show:
          operation:
          - compress
        hide: {}
    typeInfo: &id002
      type: options
      displayName: Output Format
      name: outputFormat
      possibleValues:
      - value: gzip
        name: Gzip
        description: ''
      - value: zip
        name: Zip
        description: ''
  - id: outputFormat
    name: Output Format
    type: options
    default: zip
    required: false
    description: Format of the output
    validation: *id001
    typeInfo: *id002
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: true
    description: Name of the output file
    placeholder: e.g. data.zip
    validation: &id003
      displayOptions:
        show:
          operation:
          - compress
          outputFormat:
          - gzip
        hide: {}
    typeInfo: &id004
      type: string
      displayName: File Name
      name: fileName
  - id: binaryPropertyOutput
    name: Put Output File in Field
    type: string
    default: data
    required: false
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id005
      displayOptions:
        show:
          outputFormat:
          - gzip
          operation:
          - compress
        hide: {}
    typeInfo: &id006
      type: string
      displayName: Put Output File in Field
      name: binaryPropertyOutput
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: false
    description: Name of the output file
    placeholder: e.g. data.txt
    validation: *id003
    typeInfo: *id004
  - id: binaryPropertyOutput
    name: Put Output File in Field
    type: string
    default: data
    required: false
    description: ''
    hint: The name of the output binary field to put the file in
    validation: *id005
    typeInfo: *id006
  - id: outputPrefix
    name: Output File Prefix
    type: string
    default: data
    required: true
    description: Prefix to add to the gzip file
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - decompress
    typeInfo: &id010
      type: string
      displayName: Output Prefix
      name: outputPrefix
- id: decompress
  name: Decompress
  description: Decompress zip or gzip archives
  params:
  - id: binaryPropertyName
    name: Input Binary Field(s)
    type: string
    default: data
    required: true
    description: To process more than one file, use a comma-separated list of the
      binary fields names
    hint: The name of the input binary field(s) containing the file(s) to decompress
    placeholder: e.g. data
    validation: *id007
    typeInfo: *id008
  - id: outputPrefix
    name: Output Prefix
    type: string
    default: file_
    required: true
    description: Prefix to add to the decompressed files
    validation: *id009
    typeInfo: *id010
common_expressions:
- ={{$parameter["operation"]}}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: binaryPropertyName
    text: e.g. data,data2,data3
  - field: binaryPropertyName
    text: e.g. data
  - field: fileName
    text: e.g. data.zip
  - field: fileName
    text: e.g. data.txt
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field(s) containing the file(s) to be compressed
  - field: binaryPropertyName
    text: The name of the input binary field(s) containing the file(s) to decompress
  - field: binaryPropertyOutput
    text: The name of the output binary field to put the file in
  - field: binaryPropertyOutput
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/compression.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Compression Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "compress",
        "decompress"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Compress files into a zip or gzip archive",
          "type": "string",
          "enum": [
            "compress",
            "decompress"
          ],
          "default": "decompress"
        },
        "binaryPropertyName": {
          "description": "To process more than one file, use a comma-separated list of the binary fields names",
          "type": "string",
          "default": "data",
          "examples": [
            "e.g. data"
          ]
        },
        "outputFormat": {
          "description": "Format of the output",
          "type": "string",
          "enum": [
            "gzip",
            "zip"
          ],
          "default": "zip"
        },
        "fileName": {
          "description": "Name of the output file",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. data.txt"
          ]
        },
        "binaryPropertyOutput": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "outputPrefix": {
          "description": "Prefix to add to the decompressed files",
          "type": "string",
          "default": "file_"
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
