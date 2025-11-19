---
title: "Node: Pushcut Trigger"
slug: "node-pushcuttrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Pushcut events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Pushcut Trigger

**Purpose.** Starts the workflow when Pushcut events occur


---

## Node Details

- **Icon:** `file:pushcut.png`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **pushcutApi**: N/A


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
| `pushcutApi` | ✓ | - |

---

## API Patterns

**Headers Used:** API-Key

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Action Name | `actionName` | string |  | ✗ | Choose any name you would like. It will show up as a server action in the app. |  |

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
* Categories: Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: pushcutTrigger
displayName: Pushcut Trigger
description: Starts the workflow when Pushcut events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: pushcutApi
  required: true
params:
- id: actionName
  name: Action Name
  type: string
  default: ''
  required: false
  description: Choose any name you would like. It will show up as a server action
    in the app.
  typeInfo:
    type: string
    displayName: Action Name
    name: actionName
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - API-Key
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
  "$id": "https://n8n.io/schemas/nodes/pushcutTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Pushcut Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "actionName": {
          "description": "Choose any name you would like. It will show up as a server action in the app.",
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
      "name": "pushcutApi",
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
