---
title: "Node: Mailjet Trigger"
slug: "node-mailjettrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle Mailjet events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Mailjet Trigger

**Purpose.** Handle Mailjet events via webhooks


---

## Node Details

- **Icon:** `file:mailjet.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **mailjetEmailApi**: N/A


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
| `mailjetEmailApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event | `event` | options | open | ✓ | Determines which resource events the webhook is triggered for |  |

**Event options:**

* **email.blocked** (`blocked`)
* **email.bounce** (`bounce`)
* **email.open** (`open`)
* **email.sent** (`sent`)
* **email.spam** (`spam`)
* **email.unsub** (`unsub`)


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
* Categories: Communication, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: mailjetTrigger
displayName: Mailjet Trigger
description: Handle Mailjet events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: mailjetEmailApi
  required: true
params:
- id: event
  name: Event
  type: options
  default: open
  required: true
  description: Determines which resource events the webhook is triggered for
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: blocked
      name: email.blocked
      description: ''
    - value: bounce
      name: email.bounce
      description: ''
    - value: open
      name: email.open
      description: ''
    - value: sent
      name: email.sent
      description: ''
    - value: spam
      name: email.spam
      description: ''
    - value: unsub
      name: email.unsub
      description: ''
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
  "$id": "https://n8n.io/schemas/nodes/mailjetTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Mailjet Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "event": {
          "description": "Determines which resource events the webhook is triggered for",
          "type": "string",
          "enum": [
            "blocked",
            "bounce",
            "open",
            "sent",
            "spam",
            "unsub"
          ],
          "default": "open"
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
      "name": "mailjetEmailApi",
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
