---
title: "Node: Box Trigger"
slug: "node-boxtrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when Box events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Box Trigger

**Purpose.** Starts the workflow when Box events occur


---

## Node Details

- **Icon:** `file:box.png`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **boxOAuth2Api**: N/A


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
| `boxOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `events` | multiOptions | [] | ✓ | A collaboration has been accepted |  |

**Events options:**

* **Collaboration Accepted** (`COLLABORATION.ACCEPTED`) - A collaboration has been accepted
* **Collaboration Created** (`COLLABORATION.CREATED`) - A collaboration is created
* **Collaboration Rejected** (`COLLABORATION.REJECTED`) - A collaboration has been rejected
* **Collaboration Removed** (`COLLABORATION.REMOVED`) - A collaboration has been removed
* **Collaboration Updated** (`COLLABORATION.UPDATED`) - A collaboration has been updated
* **Comment Created** (`COMMENT.CREATED`) - A comment object is created
* **Comment Deleted** (`COMMENT.DELETED`) - A comment object is removed
* **Comment Updated** (`COMMENT.UPDATED`) - A comment object is edited
* **File Copied** (`FILE.COPIED`) - A file is copied
* **File Deleted** (`FILE.DELETED`) - A file is moved to the trash
* **File Downloaded** (`FILE.DOWNLOADED`) - A file is downloaded
* **File Locked** (`FILE.LOCKED`) - A file is locked
* **File Moved** (`FILE.MOVED`) - A file is moved from one folder to another
* **File Previewed** (`FILE.PREVIEWED`) - A file is previewed
* **File Renamed** (`FILE.RENAMED`) - A file was renamed
* **File Restored** (`FILE.RESTORED`) - A file is restored from the trash
* **File Trashed** (`FILE.TRASHED`) - A file is moved to the trash
* **File Unlocked** (`FILE.UNLOCKED`) - A file is unlocked
* **File Uploaded** (`FILE.UPLOADED`) - A file is uploaded to or moved to this folder
* **Folder Copied** (`FOLDER.COPIED`) - A copy of a folder is made
* **Folder Created** (`FOLDER.CREATED`) - A folder is created
* **Folder Deleted** (`FOLDER.DELETED`) - A folder is permanently removed
* **Folder Downloaded** (`FOLDER.DOWNLOADED`) - A folder is downloaded
* **Folder Moved** (`FOLDER.MOVED`) - A folder is moved to a different folder
* **Folder Renamed** (`FOLDER.RENAMED`) - A folder was renamed
* **Folder Restored** (`FOLDER.RESTORED`) - A folder is restored from the trash
* **Folder Trashed** (`FOLDER.TRASHED`) - A folder is moved to the trash
* **Metadata Instance Created** (`METADATA_INSTANCE.CREATED`) - A new metadata template instance is associated with a file or folder
* **Metadata Instance Deleted** (`METADATA_INSTANCE.DELETED`) - An existing metadata template instance associated with a file or folder is deleted
* **Metadata Instance Updated** (`METADATA_INSTANCE.UPDATED`) - An attribute (value) is updated/deleted for an existing metadata template instance associated with a file or folder
* **Sharedlink Created** (`SHARED_LINK.CREATED`) - A shared link was created
* **Sharedlink Deleted** (`SHARED_LINK.DELETED`) - A shared link was deleted
* **Sharedlink Updated** (`SHARED_LINK.UPDATED`) - A shared link was updated
* **Task Assignment Created** (`TASK_ASSIGNMENT.CREATED`) - A task is created
* **Task Assignment Updated** (`TASK_ASSIGNMENT.UPDATED`) - A task is updated
* **Webhook Deleted** (`WEBHOOK.DELETED`) - When a webhook is deleted

| Target Type | `targetType` | options |  | ✗ | The type of item to trigger a webhook |  |

**Target Type options:**

* **File** (`file`)
* **Folder** (`folder`)

| Target ID | `targetId` | string |  | ✗ | The ID of the item to trigger a webhook |  |

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
node: boxTrigger
displayName: Box Trigger
description: Starts the workflow when Box events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: boxOAuth2Api
  required: true
params:
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: A collaboration has been accepted
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: COLLABORATION.ACCEPTED
      name: Collaboration Accepted
      description: A collaboration has been accepted
    - value: COLLABORATION.CREATED
      name: Collaboration Created
      description: A collaboration is created
    - value: COLLABORATION.REJECTED
      name: Collaboration Rejected
      description: A collaboration has been rejected
    - value: COLLABORATION.REMOVED
      name: Collaboration Removed
      description: A collaboration has been removed
    - value: COLLABORATION.UPDATED
      name: Collaboration Updated
      description: A collaboration has been updated
    - value: COMMENT.CREATED
      name: Comment Created
      description: A comment object is created
    - value: COMMENT.DELETED
      name: Comment Deleted
      description: A comment object is removed
    - value: COMMENT.UPDATED
      name: Comment Updated
      description: A comment object is edited
    - value: FILE.COPIED
      name: File Copied
      description: A file is copied
    - value: FILE.DELETED
      name: File Deleted
      description: A file is moved to the trash
    - value: FILE.DOWNLOADED
      name: File Downloaded
      description: A file is downloaded
    - value: FILE.LOCKED
      name: File Locked
      description: A file is locked
    - value: FILE.MOVED
      name: File Moved
      description: A file is moved from one folder to another
    - value: FILE.PREVIEWED
      name: File Previewed
      description: A file is previewed
    - value: FILE.RENAMED
      name: File Renamed
      description: A file was renamed
    - value: FILE.RESTORED
      name: File Restored
      description: A file is restored from the trash
    - value: FILE.TRASHED
      name: File Trashed
      description: A file is moved to the trash
    - value: FILE.UNLOCKED
      name: File Unlocked
      description: A file is unlocked
    - value: FILE.UPLOADED
      name: File Uploaded
      description: A file is uploaded to or moved to this folder
    - value: FOLDER.COPIED
      name: Folder Copied
      description: A copy of a folder is made
    - value: FOLDER.CREATED
      name: Folder Created
      description: A folder is created
    - value: FOLDER.DELETED
      name: Folder Deleted
      description: A folder is permanently removed
    - value: FOLDER.DOWNLOADED
      name: Folder Downloaded
      description: A folder is downloaded
    - value: FOLDER.MOVED
      name: Folder Moved
      description: A folder is moved to a different folder
    - value: FOLDER.RENAMED
      name: Folder Renamed
      description: A folder was renamed
    - value: FOLDER.RESTORED
      name: Folder Restored
      description: A folder is restored from the trash
    - value: FOLDER.TRASHED
      name: Folder Trashed
      description: A folder is moved to the trash
    - value: METADATA_INSTANCE.CREATED
      name: Metadata Instance Created
      description: A new metadata template instance is associated with a file or folder
    - value: METADATA_INSTANCE.DELETED
      name: Metadata Instance Deleted
      description: An existing metadata template instance associated with a file or
        folder is deleted
    - value: METADATA_INSTANCE.UPDATED
      name: Metadata Instance Updated
      description: An attribute (value) is updated/deleted for an existing metadata
        template instance associated with a file or folder
    - value: SHARED_LINK.CREATED
      name: Sharedlink Created
      description: A shared link was created
    - value: SHARED_LINK.DELETED
      name: Sharedlink Deleted
      description: A shared link was deleted
    - value: SHARED_LINK.UPDATED
      name: Sharedlink Updated
      description: A shared link was updated
    - value: TASK_ASSIGNMENT.CREATED
      name: Task Assignment Created
      description: A task is created
    - value: TASK_ASSIGNMENT.UPDATED
      name: Task Assignment Updated
      description: A task is updated
    - value: WEBHOOK.DELETED
      name: Webhook Deleted
      description: When a webhook is deleted
- id: targetType
  name: Target Type
  type: options
  default: ''
  required: false
  description: The type of item to trigger a webhook
  typeInfo:
    type: options
    displayName: Target Type
    name: targetType
    possibleValues:
    - value: file
      name: File
      description: ''
    - value: folder
      name: Folder
      description: ''
- id: targetId
  name: Target ID
  type: string
  default: ''
  required: false
  description: The ID of the item to trigger a webhook
  typeInfo:
    type: string
    displayName: Target ID
    name: targetId
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/boxTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Box Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "A collaboration has been accepted",
          "type": "string",
          "default": []
        },
        "targetType": {
          "description": "The type of item to trigger a webhook",
          "type": "string",
          "enum": [
            "file",
            "folder"
          ],
          "default": ""
        },
        "targetId": {
          "description": "The ID of the item to trigger a webhook",
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
      "name": "boxOAuth2Api",
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
