---
title: "Node: Help Scout Trigger"
slug: "node-helpscouttrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Help Scout events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Help Scout Trigger

**Purpose.** Starts the workflow when Help Scout events occur


---

## Node Details

- **Icon:** `file:helpScout.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **helpScoutOAuth2Api**: N/A


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
| `helpScoutOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `events` | multiOptions | [] | ✓ |  |  |

**Events options:**

* **Conversation - Assigned** (`convo.assigned`)
* **Conversation - Created** (`convo.created`)
* **Conversation - Deleted** (`convo.deleted`)
* **Conversation - Merged** (`convo.merged`)
* **Conversation - Moved** (`convo.moved`)
* **Conversation - Status** (`convo.status`)
* **Conversation - Tags** (`convo.tags`)
* **Conversation Agent Reply - Created** (`convo.agent.reply.created`)
* **Conversation Customer Reply - Created** (`convo.customer.reply.created`)
* **Conversation Note - Created** (`convo.note.created`)
* **Customer - Created** (`customer.created`)
* **Rating - Received** (`satisfaction.ratings`)


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
node: helpScoutTrigger
displayName: Help Scout Trigger
description: Starts the workflow when Help Scout events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: helpScoutOAuth2Api
  required: true
params:
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: convo.assigned
      name: Conversation - Assigned
      description: ''
    - value: convo.created
      name: Conversation - Created
      description: ''
    - value: convo.deleted
      name: Conversation - Deleted
      description: ''
    - value: convo.merged
      name: Conversation - Merged
      description: ''
    - value: convo.moved
      name: Conversation - Moved
      description: ''
    - value: convo.status
      name: Conversation - Status
      description: ''
    - value: convo.tags
      name: Conversation - Tags
      description: ''
    - value: convo.agent.reply.created
      name: Conversation Agent Reply - Created
      description: ''
    - value: convo.customer.reply.created
      name: Conversation Customer Reply - Created
      description: ''
    - value: convo.note.created
      name: Conversation Note - Created
      description: ''
    - value: customer.created
      name: Customer - Created
      description: ''
    - value: satisfaction.ratings
      name: Rating - Received
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
  "$id": "https://n8n.io/schemas/nodes/helpScoutTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Help Scout Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "",
          "type": "string",
          "default": []
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
      "name": "helpScoutOAuth2Api",
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
