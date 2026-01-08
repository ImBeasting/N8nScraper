---
title: "Node: FTP"
slug: "node-ftp"
version: "1"
updated: "2026-01-08"
summary: "Transfer files via FTP or SFTP"
node_type: "regular"
group: "['input']"
---

# Node: FTP

**Purpose.** Transfer files via FTP or SFTP
**Subtitle.** ={{$parameter["protocol"] + ": " + $parameter["operation"]}}


---

## Node Details

- **Icon:** `fa:server`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **ftp**: N/A
- **sftp**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `ftp` | ✓ | {'show': {'protocol': ['ftp']}} |
| `sftp` | ✓ | {'show': {'protocol': ['sftp']}} |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a file/folder |
| Download | `download` | Download a file |
| List | `list` | List folder content |
| Rename | `rename` | Rename/move oldPath to newPath |
| Upload | `upload` | Upload a file |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | download | ✗ | Delete a file/folder |  |

**Operation options:**

* **Delete** (`delete`) - Delete a file/folder
* **Download** (`download`) - Download a file
* **List** (`list`) - List folder content
* **Rename** (`rename`) - Rename/move oldPath to newPath
* **Upload** (`upload`) - Upload a file

---

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Path | `path` | string |  | ✓ | The file path of the file to delete. Has to contain the full path. | e.g. e.g. /public/documents/file-to-delete.txt |  |
| Options | `options` | collection | {} | ✗ | Whether folders can be deleted | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Folder | `folder` | boolean | False | Whether folders can be deleted |
| Recursive | `recursive` | boolean | False | Whether to remove all files and directories in target directory |

</details>


### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Path | `path` | string |  | ✓ | The file path of the file to download. Has to contain the full path. | e.g. e.g. /public/documents/file-to-download.txt |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| Options | `options` | collection | {} | ✗ | Whether to enable concurrent reads for downloading files | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Enable Concurrent Reads | `enableConcurrentReads` | boolean | False | Whether to enable concurrent reads for downloading files |
| Max Concurrent Reads | `maxConcurrentReads` | number | 5 |  |
| Chunk Size | `chunkSize` | number | 64 | Size of each chunk in KB to download, Not all servers support this |

</details>


### List parameters (`list`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Path | `path` | string | / | ✓ | Path of directory to list contents of | e.g. e.g. /public/folder |  |
| Recursive | `recursive` | boolean | False | ✓ | Whether to return object representing all directories / objects recursively found within SFTP server |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

### Rename parameters (`rename`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Old Path | `oldPath` | string |  | ✓ | e.g. e.g. /public/documents/old-file.txt |  |
| New Path | `newPath` | string |  | ✓ | e.g. e.g. /public/documents/new-file.txt |  |
| Options | `options` | collection | {} | ✗ | Whether to recursively create destination directory when renaming an existing file or folder | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Create Directories | `createDirectories` | boolean | False | Whether to recursively create destination directory when renaming an existing file or folder |

</details>


### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Path | `path` | string |  | ✓ | The file path of the file to upload. Has to contain the full path. | e.g. e.g. /public/documents/file-to-upload.txt |  |
| Binary File | `binaryData` | boolean | True | ✗ | The text content of the file to upload |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be written |  |
| File Content | `fileContent` | string |  | ✗ | The text content of the file to upload |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["protocol"] + ": " + $parameter["operation"]}}`

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
* Categories: Core Nodes, Data & Storage, Development, Utility
* Aliases: SFTP, FTP, Binary, File, Transfer

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: ftp
displayName: FTP
description: Transfer files via FTP or SFTP
version: '1'
nodeType: regular
group:
- input
credentials:
- name: ftp
  required: true
- name: sftp
  required: true
operations:
- id: delete
  name: Delete
  description: Delete a file/folder
  params:
  - id: path
    name: Path
    type: string
    default: ''
    required: true
    description: The file path of the file to delete. Has to contain the full path.
    placeholder: e.g. /public/documents/file-to-delete.txt
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - list
    typeInfo: &id002
      type: string
      displayName: Path
      name: path
- id: download
  name: Download
  description: Download a file
  params:
  - id: path
    name: Path
    type: string
    default: ''
    required: true
    description: The file path of the file to download. Has to contain the full path.
    placeholder: e.g. /public/documents/file-to-download.txt
    validation: *id001
    typeInfo: *id002
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - upload
          binaryData:
          - true
    typeInfo: &id004
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
- id: list
  name: List
  description: List folder content
  params:
  - id: path
    name: Path
    type: string
    default: /
    required: true
    description: Path of directory to list contents of
    placeholder: e.g. /public/folder
    validation: *id001
    typeInfo: *id002
  - id: recursive
    name: Recursive
    type: boolean
    default: false
    required: true
    description: Whether to return object representing all directories / objects recursively
      found within SFTP server
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - list
    typeInfo:
      type: boolean
      displayName: Recursive
      name: recursive
- id: rename
  name: Rename
  description: Rename/move oldPath to newPath
  params:
  - id: oldPath
    name: Old Path
    type: string
    default: ''
    required: true
    description: ''
    placeholder: e.g. /public/documents/old-file.txt
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - rename
    typeInfo:
      type: string
      displayName: Old Path
      name: oldPath
  - id: newPath
    name: New Path
    type: string
    default: ''
    required: true
    description: ''
    placeholder: e.g. /public/documents/new-file.txt
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - rename
    typeInfo:
      type: string
      displayName: New Path
      name: newPath
- id: upload
  name: Upload
  description: Upload a file
  params:
  - id: path
    name: Path
    type: string
    default: ''
    required: true
    description: The file path of the file to upload. Has to contain the full path.
    placeholder: e.g. /public/documents/file-to-upload.txt
    validation: *id001
    typeInfo: *id002
  - id: binaryData
    name: Binary File
    type: boolean
    default: true
    required: false
    description: The text content of the file to upload
    validation:
      displayOptions:
        show:
          operation:
          - upload
    typeInfo:
      type: boolean
      displayName: Binary File
      name: binaryData
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be written
    validation: *id003
    typeInfo: *id004
  - id: fileContent
    name: File Content
    type: string
    default: ''
    required: false
    description: The text content of the file to upload
    validation:
      displayOptions:
        show:
          operation:
          - upload
          binaryData:
          - false
    typeInfo:
      type: string
      displayName: File Content
      name: fileContent
common_expressions:
- '={{$parameter["protocol"] + ": " + $parameter["operation"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: path
    text: e.g. /public/documents/file-to-delete.txt
  - field: options
    text: Add option
  - field: path
    text: e.g. /public/documents/file-to-download.txt
  - field: options
    text: Add Field
  - field: oldPath
    text: e.g. /public/documents/old-file.txt
  - field: newPath
    text: e.g. /public/documents/new-file.txt
  - field: options
    text: Add Field
  - field: path
    text: e.g. /public/documents/file-to-upload.txt
  - field: options
    text: Add Field
  - field: path
    text: e.g. /public/folder
  - field: options
    text: Add Field
  hints:
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
  - field: binaryPropertyName
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
  "$id": "https://n8n.io/schemas/nodes/ftp.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "FTP Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "delete",
        "download",
        "list",
        "rename",
        "upload"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "protocol": {
          "description": "File transfer protocol",
          "type": "string",
          "enum": [
            "ftp",
            "sftp"
          ],
          "default": "ftp"
        },
        "operation": {
          "description": "Delete a file/folder",
          "type": "string",
          "enum": [
            "delete",
            "download",
            "list",
            "rename",
            "upload"
          ],
          "default": "download"
        },
        "path": {
          "description": "Path of directory to list contents of",
          "type": "string",
          "default": "/",
          "examples": [
            "e.g. /public/folder"
          ]
        },
        "options": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "oldPath": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. /public/documents/old-file.txt"
          ]
        },
        "newPath": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. /public/documents/new-file.txt"
          ]
        },
        "binaryData": {
          "description": "The text content of the file to upload",
          "type": "boolean",
          "default": true
        },
        "fileContent": {
          "description": "The text content of the file to upload",
          "type": "string",
          "default": ""
        },
        "recursive": {
          "description": "Whether to return object representing all directories / objects recursively found within SFTP server",
          "type": "boolean",
          "default": false
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
      "name": "ftp",
      "required": true
    },
    {
      "name": "sftp",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
