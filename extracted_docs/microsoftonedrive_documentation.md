---
title: "Node: Microsoft OneDrive"
slug: "node-microsoftonedrive"
version: "1"
updated: "2025-11-13"
summary: "Consume Microsoft OneDrive API"
node_type: "regular"
group: "['input']"
---

# Node: Microsoft OneDrive

**Purpose.** Consume Microsoft OneDrive API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:oneDrive.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftOneDriveOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `microsoftOneDriveOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Copy | `copy` | Copy a file |
| Delete | `delete` | Delete a file |
| Download | `download` | Download a file |
| Get | `get` | Get a file |
| Rename | `rename` | Rename a file |
| Search | `search` | Search a file |
| Share | `share` | Share a file |
| Upload | `upload` | Upload a file up to 4MB in size |

### Folder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a folder |
| Delete | `delete` | Delete a folder |
| Get Children | `getChildren` | Get items inside a folder |
| Rename | `rename` | Rename a folder |
| Search | `search` | Search a folder |
| Share | `share` | Share a folder |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | file | ✗ | Resource to operate on |  |

**Resource options:**

* **File** (`file`)
* **Folder** (`folder`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | upload | ✗ | Copy a file |  |

**Operation options:**

* **Copy** (`copy`) - Copy a file
* **Delete** (`delete`) - Delete a file
* **Download** (`download`) - Download a file
* **Get** (`get`) - Get a file
* **Rename** (`rename`) - Rename a file
* **Search** (`search`) - Search a file
* **Share** (`share`) - Share a file
* **Upload** (`upload`) - Upload a file up to 4MB in size

---

### Copy parameters (`copy`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File ID | `fileId` | string |  | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The new name for the copy. If this isn't provided, the same name will be used as the original. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | The new name for the copy. If this isn't provided, the same name will be used as the original. |

</details>

| Parent Reference | `parentReference` | collection | {} | ✗ | Reference to the parent item the copy will be created in <a href="https://docs.microsoft.com/en-us/onedrive/developer/rest-api/resources/itemreference?view=odsp-graph-online"> Details </a> | e.g. Add Parent Reference |  |

<details>
<summary><strong>Parent Reference sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Drive ID | `driveId` | string |  | Identifier of the drive instance that contains the item |
| Drive Type | `driveType` | string |  | Identifies the type of drive |
| ID | `id` | string |  | Identifier of the item in the drive |
| List ID | `listId` | string |  | Identifier of the list |
| Name | `name` | string |  | The name of the item being referenced |
| Path | `path` | string |  | Path that can be used to navigate to the item |
| Share ID | `shareId` | string |  | Identifier for a shared resource that can be accessed via the Shares API |
| Site ID | `siteId` | string |  | Identifier of the site |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File ID | `fileId` | string |  | ✗ | Field ID |  |
| Folder ID | `folderId` | string |  | ✗ |  |  |

### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File ID | `fileId` | string |  | ✗ |  |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File ID | `fileId` | string |  | ✗ | Field ID |  |

### Rename parameters (`rename`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Item ID | `itemId` | string |  | ✗ | ID of the file |  |
| New Name | `newName` | string |  | ✗ | New name for file |  |
| Item ID | `itemId` | string |  | ✗ | ID of the folder |  |
| New Name | `newName` | string |  | ✗ | New name for folder |  |

### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Query | `query` | string |  | ✗ | The query text used to search for items. Values may be matched across several fields including filename, metadata, and file content. |  |
| Query | `query` | string |  | ✗ | The query text used to search for items. Values may be matched across several fields including filename, metadata, and file content. |  |

### Share parameters (`share`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File ID | `fileId` | string |  | ✗ |  |  |
| Type | `type` | options |  | ✗ | The type of sharing link to create |  |

**Type options:**

* **View** (`view`)
* **Edit** (`edit`)
* **Embed** (`embed`)

| Scope | `scope` | options |  | ✗ | The type of sharing link to create |  |

**Scope options:**

* **Anonymous** (`anonymous`)
* **Organization** (`organization`)

| Folder ID | `folderId` | string |  | ✗ | File ID |  |
| Type | `type` | options |  | ✗ | The type of sharing link to create |  |

**Type options:**

* **View** (`view`)
* **Edit** (`edit`)
* **Embed** (`embed`)

| Scope | `scope` | options |  | ✗ | The type of sharing link to create |  |

**Scope options:**

* **Anonymous** (`anonymous`)
* **Organization** (`organization`)


### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Name | `fileName` | string |  | ✗ | The name the file should be saved as |  |
| Parent ID | `parentId` | string |  | ✓ | ID of the parent folder that will contain the file |  |
| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| File Content | `fileContent` | string |  | ✓ | The text content of the file |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be written |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | The name or path of the folder | e.g. /Pictures/2021 |  |
| Options | `options` | collection | {} | ✗ | ID of the folder you want to crate the new folder in | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Parent Folder ID | `parentFolderId` | string |  | ID of the folder you want to crate the new folder in |

</details>


### Get Children parameters (`getChildren`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Folder ID | `folderId` | string |  | ✗ |  |  |

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
node: microsoftOneDrive
displayName: Microsoft OneDrive
description: Consume Microsoft OneDrive API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: microsoftOneDriveOAuth2Api
  required: true
operations:
- id: copy
  name: Copy
  description: Copy a file
  params:
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: false
    description: ''
    validation: &id001
      displayOptions:
        show:
          operation:
          - share
          resource:
          - file
    typeInfo: &id002
      type: string
      displayName: File ID
      name: fileId
- id: delete
  name: Delete
  description: Delete a file
  params:
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: false
    description: Field ID
    validation: *id001
    typeInfo: *id002
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: false
    description: ''
    validation: &id009
      displayOptions:
        show:
          operation:
          - share
          resource:
          - folder
    typeInfo: &id010
      type: string
      displayName: Folder ID
      name: folderId
- id: download
  name: Download
  description: Download a file
  params:
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id015
      required: true
      displayOptions:
        show:
          binaryData:
          - true
          operation:
          - upload
          resource:
          - file
    typeInfo: &id016
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
- id: get
  name: Get
  description: Get a file
  params:
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: false
    description: Field ID
    validation: *id001
    typeInfo: *id002
- id: rename
  name: Rename
  description: Rename a file
  params:
  - id: itemId
    name: Item ID
    type: string
    default: ''
    required: false
    description: ID of the file
    validation: &id003
      displayOptions:
        show:
          operation:
          - rename
          resource:
          - folder
    typeInfo: &id004
      type: string
      displayName: Item ID
      name: itemId
  - id: newName
    name: New Name
    type: string
    default: ''
    required: false
    description: New name for file
    validation: &id005
      displayOptions:
        show:
          operation:
          - rename
          resource:
          - folder
    typeInfo: &id006
      type: string
      displayName: New Name
      name: newName
  - id: itemId
    name: Item ID
    type: string
    default: ''
    required: false
    description: ID of the folder
    validation: *id003
    typeInfo: *id004
  - id: newName
    name: New Name
    type: string
    default: ''
    required: false
    description: New name for folder
    validation: *id005
    typeInfo: *id006
- id: search
  name: Search
  description: Search a file
  params:
  - id: query
    name: Query
    type: string
    default: ''
    required: false
    description: The query text used to search for items. Values may be matched across
      several fields including filename, metadata, and file content.
    validation: &id007
      displayOptions:
        show:
          operation:
          - search
          resource:
          - folder
    typeInfo: &id008
      type: string
      displayName: Query
      name: query
  - id: query
    name: Query
    type: string
    default: ''
    required: false
    description: The query text used to search for items. Values may be matched across
      several fields including filename, metadata, and file content.
    validation: *id007
    typeInfo: *id008
- id: share
  name: Share
  description: Share a file
  params:
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: type
    name: Type
    type: options
    default: ''
    required: false
    description: The type of sharing link to create
    validation: &id011
      displayOptions:
        show:
          operation:
          - share
          resource:
          - folder
    typeInfo: &id012
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: view
        name: View
        description: ''
      - value: edit
        name: Edit
        description: ''
      - value: embed
        name: Embed
        description: ''
  - id: scope
    name: Scope
    type: options
    default: ''
    required: false
    description: The type of sharing link to create
    validation: &id013
      displayOptions:
        show:
          operation:
          - share
          resource:
          - folder
    typeInfo: &id014
      type: options
      displayName: Scope
      name: scope
      possibleValues:
      - value: anonymous
        name: Anonymous
        description: ''
      - value: organization
        name: Organization
        description: ''
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: false
    description: File ID
    validation: *id009
    typeInfo: *id010
  - id: type
    name: Type
    type: options
    default: ''
    required: false
    description: The type of sharing link to create
    validation: *id011
    typeInfo: *id012
  - id: scope
    name: Scope
    type: options
    default: ''
    required: false
    description: The type of sharing link to create
    validation: *id013
    typeInfo: *id014
- id: upload
  name: Upload
  description: Upload a file up to 4MB in size
  params:
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: false
    description: The name the file should be saved as
    validation:
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
    typeInfo:
      type: string
      displayName: File Name
      name: fileName
  - id: parentId
    name: Parent ID
    type: string
    default: ''
    required: true
    description: ID of the parent folder that will contain the file
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
    typeInfo:
      type: string
      displayName: Parent ID
      name: parentId
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
    validation:
      required: true
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
    required: true
    description: The text content of the file
    validation:
      required: true
      displayOptions:
        show:
          binaryData:
          - false
          operation:
          - upload
          resource:
          - file
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
    hint: The name of the input binary field containing the file to be written
    validation: *id015
    typeInfo: *id016
- id: create
  name: Create
  description: Create a folder
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name or path of the folder
    placeholder: /Pictures/2021
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - folder
    typeInfo:
      type: string
      displayName: Name
      name: name
- id: getChildren
  name: Get Children
  description: Get items inside a folder
  params:
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id009
    typeInfo: *id010
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: parentReference
    text: Add Parent Reference
  - field: name
    text: /Pictures/2021
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
  "$id": "https://n8n.io/schemas/nodes/microsoftOneDrive.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft OneDrive Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "copy",
        "delete",
        "download",
        "get",
        "rename",
        "search",
        "share",
        "upload",
        "create",
        "getChildren"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "file",
            "folder"
          ],
          "default": "file"
        },
        "operation": {
          "description": "Create a folder",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "getChildren",
            "rename",
            "search",
            "share"
          ],
          "default": "getChildren"
        },
        "fileId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The new name for the copy. If this isn't provided, the same name will be used as the original.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "parentReference": {
          "description": "Reference to the parent item the copy will be created in <a href=\"https://docs.microsoft.com/en-us/onedrive/developer/rest-api/resources/itemreference?view=odsp-graph-online\"> Details </a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Parent Reference"
          ]
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "itemId": {
          "description": "ID of the folder",
          "type": "string",
          "default": ""
        },
        "newName": {
          "description": "New name for folder",
          "type": "string",
          "default": ""
        },
        "query": {
          "description": "The query text used to search for items. Values may be matched across several fields including filename, metadata, and file content.",
          "type": "string",
          "default": ""
        },
        "type": {
          "description": "The type of sharing link to create",
          "type": "string",
          "enum": [
            "view",
            "edit",
            "embed"
          ],
          "default": ""
        },
        "scope": {
          "description": "The type of sharing link to create",
          "type": "string",
          "enum": [
            "anonymous",
            "organization"
          ],
          "default": ""
        },
        "fileName": {
          "description": "The name the file should be saved as",
          "type": "string",
          "default": ""
        },
        "parentId": {
          "description": "ID of the parent folder that will contain the file",
          "type": "string",
          "default": ""
        },
        "binaryData": {
          "description": "Whether the data to upload should be taken from binary field",
          "type": "boolean",
          "default": false
        },
        "fileContent": {
          "description": "The text content of the file",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "The name or path of the folder",
          "type": "string",
          "default": "",
          "examples": [
            "/Pictures/2021"
          ]
        },
        "options": {
          "description": "ID of the folder you want to crate the new folder in",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "folderId": {
          "description": "File ID",
          "type": "string",
          "default": ""
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
      "name": "microsoftOneDriveOAuth2Api",
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
