---
title: "Node: Keap Trigger"
slug: "node-keaptrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when Infusionsoft events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Keap Trigger

**Purpose.** Starts the workflow when Infusionsoft events occur
**Subtitle.** ={{$parameter["eventId"]}}


---

## Node Details

- **Icon:** `file:keap.png`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **keapOAuth2Api**: N/A


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
| `keapOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event Name or ID | `eventId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| RAW Data | `rawData` | boolean | False | ✗ | Whether to return the data exactly in the way it got received from the API |  |

---

## Load Options Methods

- `getEvents`
- `for`
- `name`
- `value`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["eventId"]}}`

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
* Categories: Sales, Communication
* Aliases: Infusionsoft

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: keapTrigger
displayName: Keap Trigger
description: Starts the workflow when Infusionsoft events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: keapOAuth2Api
  required: true
params:
- id: eventId
  name: Event Name or ID
  type: options
  default: ''
  required: true
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event Name or ID
    name: eventId
    typeOptions:
      loadOptionsMethod: getEvents
    possibleValues: []
- id: rawData
  name: RAW Data
  type: boolean
  default: false
  required: false
  description: Whether to return the data exactly in the way it got received from
    the API
  typeInfo:
    type: boolean
    displayName: RAW Data
    name: rawData
common_expressions:
- ={{$parameter["eventId"]}}
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
  "$id": "https://n8n.io/schemas/nodes/keapTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Keap Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "eventId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "rawData": {
          "description": "Whether to return the data exactly in the way it got received from the API",
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
      "name": "keapOAuth2Api",
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
