---
title: "Node: Autopilot Trigger"
slug: "node-autopilottrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle Autopilot events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Autopilot Trigger

**Purpose.** Handle Autopilot events via webhooks
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:autopilot.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **autopilotApi**: N/A


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
| `autopilotApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event | `event` | options |  | ✓ |  |  |

**Event options:**

* **Contact Added** (`contactAdded`)
* **Contact Added To List** (`contactAddedToList`)
* **Contact Entered Segment** (`contactEnteredSegment`)
* **Contact Left Segment** (`contactLeftSegment`)
* **Contact Removed From List** (`contactRemovedFromList`)
* **Contact Unsubscribed** (`contactUnsubscribed`)
* **Contact Updated** (`contactUpdated`)


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
* Categories: Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: autopilotTrigger
displayName: Autopilot Trigger
description: Handle Autopilot events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: autopilotApi
  required: true
params:
- id: event
  name: Event
  type: options
  default: ''
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: contactAdded
      name: Contact Added
      description: ''
    - value: contactAddedToList
      name: Contact Added To List
      description: ''
    - value: contactEnteredSegment
      name: Contact Entered Segment
      description: ''
    - value: contactLeftSegment
      name: Contact Left Segment
      description: ''
    - value: contactRemovedFromList
      name: Contact Removed From List
      description: ''
    - value: contactUnsubscribed
      name: Contact Unsubscribed
      description: ''
    - value: contactUpdated
      name: Contact Updated
      description: ''
common_expressions:
- ={{$parameter["event"]}}
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
  "$id": "https://n8n.io/schemas/nodes/autopilotTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Autopilot Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "event": {
          "description": "",
          "type": "string",
          "enum": [
            "contactAdded",
            "contactAddedToList",
            "contactEnteredSegment",
            "contactLeftSegment",
            "contactRemovedFromList",
            "contactUnsubscribed",
            "contactUpdated"
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
      "name": "autopilotApi",
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
