---
title: "Node: Figma Trigger (Beta)"
slug: "node-figmatrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Figma events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Figma Trigger (Beta)

**Purpose.** Starts the workflow when Figma events occur
**Subtitle.** ={{$parameter["triggerOn"]}}


---

## Node Details

- **Icon:** `file:figma.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **figmaApi**: N/A


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
| `figmaApi` | ✓ | - |

---

## API Patterns

**Headers Used:** X-FIGMA-TOKEN

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team ID | `teamId` | string |  | ✓ | Trigger will monitor this Figma Team for changes. Team ID can be found in the URL of a Figma Team page when viewed in a web browser: figma.com/files/team/{TEAM-ID}/. |  |
| Trigger On | `triggerOn` | options |  | ✓ | Triggers when someone comments on a file |  |

**Trigger On options:**

* **File Commented** (`fileComment`) - Triggers when someone comments on a file
* **File Deleted** (`fileDelete`) - Triggers whenever a file has been deleted. Does not trigger on all files within a folder, if the folder is deleted.
* **File Updated** (`fileUpdate`) - Triggers whenever a file saves or is deleted. This occurs whenever a file is closed or within 30 seconds after changes have been made.
* **File Version Updated** (`fileVersionUpdate`) - Triggers whenever a named version is created in the version history of a file
* **Library Publish** (`libraryPublish`) - Triggers whenever a library file is published


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["triggerOn"]}}`

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
* Categories: Miscellaneous

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: figmaTrigger
displayName: Figma Trigger (Beta)
description: Starts the workflow when Figma events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: figmaApi
  required: true
params:
- id: teamId
  name: Team ID
  type: string
  default: ''
  required: true
  description: 'Trigger will monitor this Figma Team for changes. Team ID can be found
    in the URL of a Figma Team page when viewed in a web browser: figma.com/files/team/{TEAM-ID}/.'
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Team ID
    name: teamId
- id: triggerOn
  name: Trigger On
  type: options
  default: ''
  required: true
  description: Triggers when someone comments on a file
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Trigger On
    name: triggerOn
    possibleValues:
    - value: fileComment
      name: File Commented
      description: Triggers when someone comments on a file
    - value: fileDelete
      name: File Deleted
      description: Triggers whenever a file has been deleted. Does not trigger on
        all files within a folder, if the folder is deleted.
    - value: fileUpdate
      name: File Updated
      description: Triggers whenever a file saves or is deleted. This occurs whenever
        a file is closed or within 30 seconds after changes have been made.
    - value: fileVersionUpdate
      name: File Version Updated
      description: Triggers whenever a named version is created in the version history
        of a file
    - value: libraryPublish
      name: Library Publish
      description: Triggers whenever a library file is published
common_expressions:
- ={{$parameter["triggerOn"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - X-FIGMA-TOKEN
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
  "$id": "https://n8n.io/schemas/nodes/figmaTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Figma Trigger (Beta) Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "teamId": {
          "description": "Trigger will monitor this Figma Team for changes. Team ID can be found in the URL of a Figma Team page when viewed in a web browser: figma.com/files/team/{TEAM-ID}/.",
          "type": "string",
          "default": ""
        },
        "triggerOn": {
          "description": "Triggers when someone comments on a file",
          "type": "string",
          "enum": [
            "fileComment",
            "fileDelete",
            "fileUpdate",
            "fileVersionUpdate",
            "libraryPublish"
          ],
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
      "name": "figmaApi",
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
