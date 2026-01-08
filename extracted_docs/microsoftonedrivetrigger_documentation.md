---
title: "Node: Microsoft OneDrive Trigger"
slug: "node-microsoftonedrivetrigger"
version: "1"
updated: "2026-01-08"
summary: "Trigger for Microsoft OneDrive API."
node_type: "trigger"
group: "['trigger']"
---

# Node: Microsoft OneDrive Trigger

**Purpose.** Trigger for Microsoft OneDrive API.
**Subtitle.** ={{($parameter["event"])}}


---

## Node Details

- **Icon:** `file:oneDrive.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftOneDriveOAuth2Api**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

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

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger On | `event` | options | fileCreated | ✗ | When a new file is created |  |

**Trigger On options:**

* **File Created** (`fileCreated`) - When a new file is created
* **File Updated** (`fileUpdated`) - When an existing file is modified
* **Folder Created** (`folderCreated`) - When a new folder is created
* **Folder Updated** (`folderUpdated`) - When an existing folder is modified

| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Watch Folder | `watchFolder` | boolean | False | ✗ | Whether to watch for the created file in a given folder, rather than the entire OneDrive |  |
| Watch | `watch` | options | anyFile | ✗ | How to select which file to watch |  |

**Watch options:**

* **Any File** (`anyFile`) - Watch for updated files in the entire OneDrive
* **Inside a Folder** (`selectedFolder`) - Watch for updated files inside a selected folder
* **A Selected File** (`selectedFile`) - Watch a specific file for updates

| Watch Folder | `watchFolder` | boolean | False | ✗ | Whether to watch for the created folder in a given folder, rather than the entire OneDrive |  |
| Watch | `watch` | options | anyFolder | ✗ | How to select which folder to watch |  |

**Watch options:**

* **Any Folder** (`anyFolder`) - Watch for updated folders in the entire OneDrive
* **Inside a Folder** (`selectedFolder`) - Watch for updated folders inside a selected folder
* **A Selected Folder** (`oneSelectedFolder`) - Watch a specific folder for updates

| Options | `options` | collection | {} | ✗ | Whether to look for modified files/folders in all nested folders, rather than only direct descendants | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Watch Nested Folders | `folderChild` | boolean | False | Whether to look for modified files/folders in all nested folders, rather than only direct descendants |

</details>

| Options | `options` | collection | {} | ✗ | Whether to look for modified files/folders in all nested folders, rather than only direct descendants | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Watch Nested Folders | `folderChild` | boolean | False | Whether to look for modified files/folders in all nested folders, rather than only direct descendants |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{($parameter["event"])}}`

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
node: microsoftOneDriveTrigger
displayName: Microsoft OneDrive Trigger
description: Trigger for Microsoft OneDrive API.
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: microsoftOneDriveOAuth2Api
  required: true
params:
- id: event
  name: Trigger On
  type: options
  default: fileCreated
  required: false
  description: When a new file is created
  typeInfo:
    type: options
    displayName: Trigger On
    name: event
    possibleValues:
    - value: fileCreated
      name: File Created
      description: When a new file is created
    - value: fileUpdated
      name: File Updated
      description: When an existing file is modified
    - value: folderCreated
      name: Folder Created
      description: When a new folder is created
    - value: folderUpdated
      name: Folder Updated
      description: When an existing folder is modified
- id: simple
  name: Simplify
  type: boolean
  default: true
  required: false
  description: Whether to return a simplified version of the response instead of the
    raw data
  typeInfo:
    type: boolean
    displayName: Simplify
    name: simple
- id: watchFolder
  name: Watch Folder
  type: boolean
  default: false
  required: false
  description: Whether to watch for the created file in a given folder, rather than
    the entire OneDrive
  validation: &id001
    displayOptions:
      show:
        event:
        - folderCreated
  typeInfo: &id002
    type: boolean
    displayName: Watch Folder
    name: watchFolder
- id: watch
  name: Watch
  type: options
  default: anyFile
  required: false
  description: How to select which file to watch
  validation: &id003
    displayOptions:
      show:
        event:
        - folderUpdated
  typeInfo: &id004
    type: options
    displayName: Watch
    name: watch
    possibleValues:
    - value: anyFolder
      name: Any Folder
      description: Watch for updated folders in the entire OneDrive
    - value: selectedFolder
      name: Inside a Folder
      description: Watch for updated folders inside a selected folder
    - value: oneSelectedFolder
      name: A Selected Folder
      description: Watch a specific folder for updates
- id: watchFolder
  name: Watch Folder
  type: boolean
  default: false
  required: false
  description: Whether to watch for the created folder in a given folder, rather than
    the entire OneDrive
  validation: *id001
  typeInfo: *id002
- id: watch
  name: Watch
  type: options
  default: anyFolder
  required: false
  description: How to select which folder to watch
  validation: *id003
  typeInfo: *id004
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to look for modified files/folders in all nested folders, rather
    than only direct descendants
  placeholder: Add option
  validation: &id005
    displayOptions:
      show:
        watchFolder:
        - true
  typeInfo: &id006
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Watch Nested Folders
      name: folderChild
      type: boolean
      description: Whether to look for modified files/folders in all nested folders,
        rather than only direct descendants
      default: false
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to look for modified files/folders in all nested folders, rather
    than only direct descendants
  placeholder: Add option
  validation: *id005
  typeInfo: *id006
common_expressions:
- ={{($parameter["event"])}}
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
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/microsoftOneDriveTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft OneDrive Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "event": {
          "description": "When a new file is created",
          "type": "string",
          "enum": [
            "fileCreated",
            "fileUpdated",
            "folderCreated",
            "folderUpdated"
          ],
          "default": "fileCreated"
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "watchFolder": {
          "description": "Whether to watch for the created folder in a given folder, rather than the entire OneDrive",
          "type": "boolean",
          "default": false
        },
        "watch": {
          "description": "How to select which folder to watch",
          "type": "string",
          "enum": [
            "anyFolder",
            "selectedFolder",
            "oneSelectedFolder"
          ],
          "default": "anyFolder"
        },
        "options": {
          "description": "Whether to look for modified files/folders in all nested folders, rather than only direct descendants",
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
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
