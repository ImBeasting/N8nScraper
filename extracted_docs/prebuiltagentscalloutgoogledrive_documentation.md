---
title: "Node: Retrieve, analyze, and answer questions using your Google Drive documents with our pre-built"
slug: "node-prebuiltagentscalloutgoogledrive"
version: "3"
updated: "2026-01-08"
summary: "Access data on Google Drive"
node_type: "regular"
group: "['input']"
---

# Node: Retrieve, analyze, and answer questions using your Google Drive documents with our pre-built

**Purpose.** Access data on Google Drive
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `bot`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleApi**: N/A
- **googleDriveOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleApi` | ✓ | {'show': {'authentication': ['serviceAccount']}} |
| `googleDriveOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Drive Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a shared drive |
| Delete | `deleteDrive` | Permanently delete a shared drive |
| Get | `get` | Get a shared drive |
| Get Many | `list` | Get the list of shared drives |
| Update | `update` | Update a shared drive |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Copy | `copy` | Create a copy of an existing file |
| Create From Text | `createFromText` | Create a file from a provided text |
| Delete | `deleteFile` | Permanently delete a file |
| Download | `download` | Download a file |
| Move | `move` | Move a file to another folder |
| Share | `share` | Add sharing permissions to a file |
| Update | `update` | Update a file |
| Upload | `upload` | Upload an existing file to Google Drive |

### Filefolder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Search | `search` | Search or list files and folders |

### Folder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a folder |
| Delete | `deleteFolder` | Permanently delete a folder |
| Share | `share` | Add sharing permissions to a folder |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | file | ✗ | Resource to operate on |  |

**Resource options:**

* **File** (`file`)
* **File/Folder** (`fileFolder`)
* **Folder** (`folder`)
* **Shared Drive** (`drive`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a shared drive |  |

**Operation options:**

* **Create** (`create`) - Create a shared drive
* **Delete** (`deleteDrive`) - Permanently delete a shared drive
* **Get** (`get`) - Get a shared drive
* **Get Many** (`list`) - Get the list of shared drives
* **Update** (`update`) - Update a shared drive

---

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: preBuiltAgentsCalloutGoogleDrive
displayName: Retrieve, analyze, and answer questions using your Google Drive documents
  with our pre-built
description: Access data on Google Drive
version: '3'
nodeType: regular
group:
- input
credentials:
- name: googleApi
  required: true
- name: googleDriveOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a shared drive
- id: deleteDrive
  name: Delete
  description: Permanently delete a shared drive
- id: get
  name: Get
  description: Get a shared drive
- id: list
  name: Get Many
  description: Get the list of shared drives
- id: update
  name: Update
  description: Update a shared drive
- id: copy
  name: Copy
  description: Create a copy of an existing file
- id: createFromText
  name: Create From Text
  description: Create a file from a provided text
- id: deleteFile
  name: Delete
  description: Permanently delete a file
- id: download
  name: Download
  description: Download a file
- id: move
  name: Move
  description: Move a file to another folder
- id: share
  name: Share
  description: Add sharing permissions to a file
- id: upload
  name: Upload
  description: Upload an existing file to Google Drive
- id: search
  name: Search
  description: Search or list files and folders
- id: deleteFolder
  name: Delete
  description: Permanently delete a folder
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders: []
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
  "$id": "https://n8n.io/schemas/nodes/preBuiltAgentsCalloutGoogleDrive.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Retrieve, analyze, and answer questions using your Google Drive documents with our pre-built Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "deleteDrive",
        "get",
        "list",
        "update",
        "copy",
        "createFromText",
        "deleteFile",
        "download",
        "move",
        "share",
        "upload",
        "search",
        "deleteFolder"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "oAuth2",
            "serviceAccount"
          ],
          "default": "oAuth2"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "file",
            "fileFolder",
            "folder",
            "drive"
          ],
          "default": "file"
        },
        "operation": {
          "description": "Create a folder",
          "type": "string",
          "enum": [
            "create",
            "deleteFolder",
            "share"
          ],
          "default": "create"
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
    "version": "3"
  },
  "credentials": [
    {
      "name": "googleApi",
      "required": true
    },
    {
      "name": "googleDriveOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 3 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
