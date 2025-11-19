---
title: "Node: Dropbox"
slug: "node-dropbox"
version: "1"
updated: "2025-11-13"
summary: "Access data on Dropbox"
node_type: "regular"
group: "['input']"
---

# Node: Dropbox

**Purpose.** Access data on Dropbox
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:dropbox.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **dropboxApi**: N/A
- **dropboxOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `dropboxApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `dropboxOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Copy | `copy` | Copy a file |
| Delete | `delete` | Delete a file |
| Download | `download` | Download a file |
| Move | `move` | Move a file |
| Upload | `upload` | Upload a file |

### Folder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Copy | `copy` | Copy a folder |
| Create | `create` | Create a folder |
| Delete | `delete` | Delete a folder |
| List | `list` | Return the files and folders in a given folder |
| Move | `move` | Move a folder |

### Search Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Query | `query` | Query |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | file | ✗ | Resource to operate on |  |

**Resource options:**

* **File** (`file`)
* **Folder** (`folder`)
* **Search** (`search`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | upload | ✗ | Copy a file |  |

**Operation options:**

* **Copy** (`copy`) - Copy a file
* **Delete** (`delete`) - Delete a file
* **Download** (`download`) - Download a file
* **Move** (`move`) - Move a file
* **Upload** (`upload`) - Upload a file

---

### Copy parameters (`copy`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From Path | `path` | string |  | ✓ | The path of file or folder to copy | e.g. /invoices/original.txt |  |
| To Path | `toPath` | string |  | ✓ | The destination path of file or folder | e.g. /invoices/copy.txt |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Delete Path | `path` | string |  | ✓ | The path to delete. Can be a single file or a whole folder. | e.g. /invoices/2019/invoice_1.pdf |  |

### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Path | `path` | string |  | ✓ | The file path of the file to download. Has to contain the full path. | e.g. /invoices/2019/invoice_1.pdf |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |

### Move parameters (`move`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From Path | `path` | string |  | ✓ | The path of file or folder to move | e.g. /invoices/old_name.txt |  |
| To Path | `toPath` | string |  | ✓ | The new path of file or folder | e.g. /invoices/new_name.txt |  |

### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Path | `path` | string |  | ✓ | The file path of the file to upload. Has to contain the full path. The parent folder has to exist. Existing files get overwritten. | e.g. /invoices/2019/invoice_1.pdf |  |
| Binary File | `binaryData` | boolean | False | ✗ | Whether the data to upload should be taken from binary field |  |
| File Content | `fileContent` | string |  | ✗ | The text content of the file to upload |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Folder | `path` | string |  | ✓ | The folder to create. The parent folder has to exist. | e.g. /invoices/2019 |  |

### List parameters (`list`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Folder Path | `path` | string |  | ✗ | The path of which to list the content | e.g. /invoices/2019/ |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Whether the results will include entries for files and folders that used to exist but were deleted. The default for this field is False. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Deleted | `include_deleted` | boolean | False | Whether the results will include entries for files and folders that used to exist but were deleted. The default for this field is False. |
| Include Shared Members | `include_has_explicit_shared_members` | boolean | False | Whether the results will include a flag for each file indicating whether or not that file has any explicit members. The default for this field is False. |
| Include Mounted Folders | `include_mounted_folders` | boolean | True | Whether the results will include entries under mounted folders which includes app folder, shared folder and team folder. The default for this field is True. |
| Include Non Downloadable Files | `include_non_downloadable_files` | boolean | True | Whether to include files that are not downloadable, i.e. Google Docs. The default for this field is True. |
| Recursive | `recursive` | boolean | False | Whether the list folder operation will be applied recursively to all subfolders and the response will contain contents of all subfolders. The default for this field is False. |

</details>


### Query parameters (`query`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Query | `query` | string |  | ✓ | The string to search for. May match across multiple fields based on the request arguments. |  |
| File Status | `fileStatus` | options | active | ✗ | The string to search for. May match across multiple fields based on the request arguments. |  |

**File Status options:**

* **Active** (`active`)
* **Deleted** (`deleted`)

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:∞ |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Filters | `filters` | collection | {} | ✗ | Multiple file extensions can be set separated by comma. Example: jpg,pdf. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Categories | `file_categories` | multiOptions | [] |  |
| File Extensions | `file_extensions` | string |  | Multiple file extensions can be set separated by comma. Example: jpg,pdf. |
| Folder | `path` | string |  | If this field is not specified, this module searches the entire Dropbox |

</details>


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
* Categories: Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: dropbox
displayName: Dropbox
description: Access data on Dropbox
version: '1'
nodeType: regular
group:
- input
credentials:
- name: dropboxApi
  required: true
- name: dropboxOAuth2Api
  required: true
operations:
- id: copy
  name: Copy
  description: Copy a file
  params:
  - id: path
    name: From Path
    type: string
    default: ''
    required: true
    description: The path of file or folder to copy
    placeholder: /invoices/original.txt
    validation: &id001
      displayOptions:
        show:
          operation:
          - list
          resource:
          - folder
    typeInfo: &id002
      type: string
      displayName: Folder Path
      name: path
  - id: toPath
    name: To Path
    type: string
    default: ''
    required: true
    description: The destination path of file or folder
    placeholder: /invoices/copy.txt
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - move
          resource:
          - file
          - folder
    typeInfo: &id004
      type: string
      displayName: To Path
      name: toPath
- id: delete
  name: Delete
  description: Delete a file
  params:
  - id: path
    name: Delete Path
    type: string
    default: ''
    required: true
    description: The path to delete. Can be a single file or a whole folder.
    placeholder: /invoices/2019/invoice_1.pdf
    validation: *id001
    typeInfo: *id002
- id: download
  name: Download
  description: Download a file
  params:
  - id: path
    name: File Path
    type: string
    default: ''
    required: true
    description: The file path of the file to download. Has to contain the full path.
    placeholder: /invoices/2019/invoice_1.pdf
    validation: *id001
    typeInfo: *id002
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
          binaryData:
          - true
    typeInfo: &id006
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
- id: move
  name: Move
  description: Move a file
  params:
  - id: path
    name: From Path
    type: string
    default: ''
    required: true
    description: The path of file or folder to move
    placeholder: /invoices/old_name.txt
    validation: *id001
    typeInfo: *id002
  - id: toPath
    name: To Path
    type: string
    default: ''
    required: true
    description: The new path of file or folder
    placeholder: /invoices/new_name.txt
    validation: *id003
    typeInfo: *id004
- id: upload
  name: Upload
  description: Upload a file
  params:
  - id: path
    name: File Path
    type: string
    default: ''
    required: true
    description: The file path of the file to upload. Has to contain the full path.
      The parent folder has to exist. Existing files get overwritten.
    placeholder: /invoices/2019/invoice_1.pdf
    validation: *id001
    typeInfo: *id002
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: false
    description: Whether the data to upload should be taken from binary field
    validation:
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
    typeInfo:
      type: boolean
      displayName: Binary File
      name: binaryData
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
          resource:
          - file
          binaryData:
          - false
    typeInfo:
      type: string
      displayName: File Content
      name: fileContent
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be uploaded
    validation: *id005
    typeInfo: *id006
- id: create
  name: Create
  description: Create a folder
  params:
  - id: path
    name: Folder
    type: string
    default: ''
    required: true
    description: The folder to create. The parent folder has to exist.
    placeholder: /invoices/2019
    validation: *id001
    typeInfo: *id002
- id: list
  name: List
  description: Return the files and folders in a given folder
  params:
  - id: path
    name: Folder Path
    type: string
    default: ''
    required: false
    description: The path of which to list the content
    placeholder: /invoices/2019/
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id007
      displayOptions:
        show:
          operation:
          - list
          resource:
          - folder
    typeInfo: &id008
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id009
      displayOptions:
        show:
          resource:
          - folder
          operation:
          - list
          returnAll:
          - false
    typeInfo: &id010
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
- id: query
  name: Query
  description: ''
  params:
  - id: query
    name: Query
    type: string
    default: ''
    required: true
    description: The string to search for. May match across multiple fields based
      on the request arguments.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - query
          resource:
          - search
    typeInfo:
      type: string
      displayName: Query
      name: query
  - id: fileStatus
    name: File Status
    type: options
    default: active
    required: false
    description: The string to search for. May match across multiple fields based
      on the request arguments.
    validation:
      displayOptions:
        show:
          operation:
          - query
          resource:
          - search
    typeInfo:
      type: options
      displayName: File Status
      name: fileStatus
      possibleValues:
      - value: active
        name: Active
        description: ''
      - value: deleted
        name: Deleted
        description: ''
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id007
    typeInfo: *id008
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation:
      displayOptions:
        show:
          operation:
          - query
          resource:
          - search
    typeInfo:
      type: boolean
      displayName: Simplify
      name: simple
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: path
    text: /invoices/original.txt
  - field: toPath
    text: /invoices/copy.txt
  - field: path
    text: /invoices/2019/invoice_1.pdf
  - field: path
    text: /invoices/old_name.txt
  - field: toPath
    text: /invoices/new_name.txt
  - field: path
    text: /invoices/2019/invoice_1.pdf
  - field: path
    text: /invoices/2019/invoice_1.pdf
  - field: filters
    text: Add Filter
  - field: path
    text: /invoices/2019
  - field: path
    text: /invoices/2019/
  - field: filters
    text: Add Filter
  hints:
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be uploaded
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
  "$id": "https://n8n.io/schemas/nodes/dropbox.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Dropbox Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "copy",
        "delete",
        "download",
        "move",
        "upload",
        "create",
        "list",
        "query"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "Means of authenticating with the service",
          "type": "string",
          "enum": [
            "accessToken",
            "oAuth2"
          ],
          "default": "accessToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "file",
            "folder",
            "search"
          ],
          "default": "file"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "query"
          ],
          "default": "query"
        },
        "path": {
          "description": "The path of which to list the content",
          "type": "string",
          "default": "",
          "examples": [
            "/invoices/2019/"
          ]
        },
        "toPath": {
          "description": "The new path of file or folder",
          "type": "string",
          "default": "",
          "examples": [
            "/invoices/new_name.txt"
          ]
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "binaryData": {
          "description": "Whether the data to upload should be taken from binary field",
          "type": "boolean",
          "default": false
        },
        "fileContent": {
          "description": "The text content of the file to upload",
          "type": "string",
          "default": ""
        },
        "query": {
          "description": "The string to search for. May match across multiple fields based on the request arguments.",
          "type": "string",
          "default": ""
        },
        "fileStatus": {
          "description": "The string to search for. May match across multiple fields based on the request arguments.",
          "type": "string",
          "enum": [
            "active",
            "deleted"
          ],
          "default": "active"
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "filters": {
          "description": "Whether the results will include entries for files and folders that used to exist but were deleted. The default for this field is False.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
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
      "name": "dropboxApi",
      "required": true
    },
    {
      "name": "dropboxOAuth2Api",
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
