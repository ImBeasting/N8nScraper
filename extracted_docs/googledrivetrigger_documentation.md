---
title: "Node: Google Drive Trigger"
slug: "node-googledrivetrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Google Drive events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Google Drive Trigger

**Purpose.** Starts the workflow when Google Drive events occur
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:googleDrive.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **googleApi**: N/A
- **googleDriveOAuth2Api**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **asas** when triggerOn=['specificFolder']: Changes within subfolders won't trigger this node

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleApi` | ✓ | {'show': {'authentication': ['serviceAccount']}} |
| `googleDriveOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Credential Type | `authentication` | options | oAuth2 | ✗ |  |  |

**Credential Type options:**

* **OAuth2 (recommended)** (`oAuth2`)
* **Service Account** (`serviceAccount`)

| Trigger On | `triggerOn` | options |  | ✓ |  |  |

**Trigger On options:**

* **Changes to a Specific File** (`specificFile`)
* **Changes Involving a Specific Folder** (`specificFolder`)
* **Changes To Any File/Folder** (`anyFileFolder`)

| File | `fileToWatch` | resourceLocator |  | ✓ | e.g. Select a file... |  |
| Watch For | `event` | options | fileUpdated | ✓ | When to trigger this node |  |

**Watch For options:**

* **File Updated** (`fileUpdated`)

| Folder | `folderToWatch` | resourceLocator |  | ✓ | e.g. Select a folder... |  |
| Watch For | `event` | options |  | ✓ | When a file is created in the watched folder |  |

**Watch For options:**

* **File Created** (`fileCreated`) - When a file is created in the watched folder
* **File Updated** (`fileUpdated`) - When a file is updated in the watched folder
* **Folder Created** (`folderCreated`) - When a folder is created in the watched folder
* **Folder Updated** (`folderUpdated`) - When a folder is updated in the watched folder
* **Watch Folder Updated** (`watchFolderUpdated`) - When the watched folder itself is modified

| Drive To Watch | `driveToWatch` | options | root | ✓ | The drive to monitor. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Watch For | `event` | options | fileCreated | ✓ | When a file is created in the watched drive |  |

**Watch For options:**

* **File Created** (`fileCreated`) - When a file is created in the watched drive
* **File Updated** (`fileUpdated`) - When a file is updated in the watched drive
* **Folder Created** (`folderCreated`) - When a folder is created in the watched drive
* **Folder Updated** (`folderUpdated`) - When a folder is updated in the watched drive

| Options | `options` | collection | {} | ✗ | Triggers only when the file is this type | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Type | `fileType` | options | all | Triggers only when the file is this type |

</details>


---

## Load Options Methods

- `getDrives`
- `name`
- `value`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["event"]}}`

---

## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |

---

## Notes & Caveats

* This node is part of n8n-nodes-base
* Categories: Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleDriveTrigger
displayName: Google Drive Trigger
description: Starts the workflow when Google Drive events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: googleApi
  required: true
- name: googleDriveOAuth2Api
  required: true
params:
- id: authentication
  name: Credential Type
  type: options
  default: oAuth2
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Credential Type
    name: authentication
    possibleValues:
    - value: oAuth2
      name: OAuth2 (recommended)
      description: ''
    - value: serviceAccount
      name: Service Account
      description: ''
- id: triggerOn
  name: Trigger On
  type: options
  default: ''
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Trigger On
    name: triggerOn
    possibleValues:
    - value: specificFile
      name: Changes to a Specific File
      description: ''
    - value: specificFolder
      name: Changes Involving a Specific Folder
      description: ''
    - value: anyFileFolder
      name: Changes To Any File/Folder
      description: ''
- id: fileToWatch
  name: File
  type: resourceLocator
  default: ''
  required: true
  description: ''
  placeholder: Select a file...
  validation:
    required: true
    displayOptions:
      show:
        triggerOn:
        - specificFile
  typeInfo:
    type: resourceLocator
    displayName: File
    name: fileToWatch
- id: event
  name: Watch For
  type: options
  default: fileUpdated
  required: true
  description: When to trigger this node
  validation: &id001
    required: true
    displayOptions:
      show:
        triggerOn:
        - anyFileFolder
  typeInfo: &id002
    type: options
    displayName: Watch For
    name: event
    possibleValues:
    - value: fileCreated
      name: File Created
      description: When a file is created in the watched drive
    - value: fileUpdated
      name: File Updated
      description: When a file is updated in the watched drive
    - value: folderCreated
      name: Folder Created
      description: When a folder is created in the watched drive
    - value: folderUpdated
      name: Folder Updated
      description: When a folder is updated in the watched drive
- id: folderToWatch
  name: Folder
  type: resourceLocator
  default: ''
  required: true
  description: ''
  placeholder: Select a folder...
  validation:
    required: true
    displayOptions:
      show:
        triggerOn:
        - specificFolder
  typeInfo:
    type: resourceLocator
    displayName: Folder
    name: folderToWatch
- id: event
  name: Watch For
  type: options
  default: ''
  required: true
  description: When a file is created in the watched folder
  validation: *id001
  typeInfo: *id002
- id: driveToWatch
  name: Drive To Watch
  type: options
  default: root
  required: true
  description: The drive to monitor. Choose from the list, or specify an ID using
    an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation:
    required: true
    displayOptions:
      show:
        triggerOn:
        - anyFileFolder
  typeInfo:
    type: options
    displayName: Drive To Watch
    name: driveToWatch
    typeOptions:
      loadOptionsMethod: getDrives
    possibleValues: []
- id: event
  name: Watch For
  type: options
  default: fileCreated
  required: true
  description: When a file is created in the watched drive
  validation: *id001
  typeInfo: *id002
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Triggers only when the file is this type
  placeholder: Add option
  validation:
    displayOptions:
      show:
        event:
        - fileCreated
        - fileUpdated
      hide:
        triggerOn:
        - specificFile
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: File Type
      name: fileType
      type: options
      description: Triggers only when the file is this type
      value: all
      default: all
      options:
      - name: '[All]'
        value: all
        displayName: '[all]'
      - name: Audio
        value: application/vnd.google-apps.audio
        displayName: Audio
      - name: Google Docs
        value: application/vnd.google-apps.document
        displayName: Google Docs
      - name: Google Drawings
        value: application/vnd.google-apps.drawing
        displayName: Google Drawings
      - name: Google Slides
        value: application/vnd.google-apps.presentation
        displayName: Google Slides
      - name: Google Spreadsheets
        value: application/vnd.google-apps.spreadsheet
        displayName: Google Spreadsheets
      - name: Photos and Images
        value: application/vnd.google-apps.photo
        displayName: Photos And Images
      - name: Videos
        value: application/vnd.google-apps.video
        displayName: Videos
common_expressions:
- ={{$parameter["event"]}}
ui_elements:
  notices:
  - name: asas
    text: Changes within subfolders won't trigger this node
    conditions:
      show:
        triggerOn:
        - specificFolder
      hide:
        event:
        - watchFolderUpdated
  tooltips: []
  placeholders:
  - field: fileToWatch
    text: Select a file...
  - field: folderToWatch
    text: Select a folder...
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/googleDriveTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Drive Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
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
        "triggerOn": {
          "description": "",
          "type": "string",
          "enum": [
            "specificFile",
            "specificFolder",
            "anyFileFolder"
          ],
          "default": ""
        },
        "fileToWatch": {
          "description": "",
          "type": "string",
          "examples": [
            "Select a file..."
          ]
        },
        "event": {
          "description": "When a file is created in the watched drive",
          "type": "string",
          "enum": [
            "fileCreated",
            "fileUpdated",
            "folderCreated",
            "folderUpdated"
          ],
          "default": "fileCreated"
        },
        "folderToWatch": {
          "description": "",
          "type": "string",
          "examples": [
            "Select a folder..."
          ]
        },
        "driveToWatch": {
          "description": "The drive to monitor. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": "root"
        },
        "options": {
          "description": "Triggers only when the file is this type",
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
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
    "version": "1"
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
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
