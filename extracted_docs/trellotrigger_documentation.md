---
title: "Node: Trello Trigger"
slug: "node-trellotrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Trello events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Trello Trigger

**Purpose.** Starts the workflow when Trello events occur


---

## Node Details

- **Icon:** `file:trello.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **trelloApi**: N/A


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
| `trelloApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Model ID | `id` | string |  | ✓ | ID of the model of which to subscribe to events | e.g. 4d5ea62fd76aa1136000000c |  |

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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: trelloTrigger
displayName: Trello Trigger
description: Starts the workflow when Trello events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: trelloApi
  required: true
params:
- id: id
  name: Model ID
  type: string
  default: ''
  required: true
  description: ID of the model of which to subscribe to events
  placeholder: 4d5ea62fd76aa1136000000c
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Model ID
    name: id
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: id
    text: 4d5ea62fd76aa1136000000c
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
  "$id": "https://n8n.io/schemas/nodes/trelloTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Trello Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "id": {
          "description": "ID of the model of which to subscribe to events",
          "type": "string",
          "default": "",
          "examples": [
            "4d5ea62fd76aa1136000000c"
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
      "name": "trelloApi",
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
