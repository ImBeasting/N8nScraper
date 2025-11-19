---
title: "Node: Microsoft Outlook Trigger"
slug: "node-microsoftoutlooktrigger"
version: "1"
updated: "2025-11-13"
summary: "Fetches emails from Microsoft Outlook and starts the workflow on specified polling intervals."
node_type: "trigger"
group: "['trigger']"
---

# Node: Microsoft Outlook Trigger

**Purpose.** Fetches emails from Microsoft Outlook and starts the workflow on specified polling intervals.
**Subtitle.** ={{"Microsoft Outlook Trigger"}}


---

## Node Details

- **Icon:** `file:outlook.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftOutlookOAuth2Api**: N/A


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
| `microsoftOutlookOAuth2Api` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger On | `event` | options | messageReceived | ✗ |  |  |

**Trigger On options:**

* **Message Received** (`messageReceived`)


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{"Microsoft Outlook Trigger"}}`

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
* Aliases: email

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: microsoftOutlookTrigger
displayName: Microsoft Outlook Trigger
description: Fetches emails from Microsoft Outlook and starts the workflow on specified
  polling intervals.
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: microsoftOutlookOAuth2Api
  required: true
params:
- id: event
  name: Trigger On
  type: options
  default: messageReceived
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Trigger On
    name: event
    possibleValues:
    - value: messageReceived
      name: Message Received
      description: ''
common_expressions:
- ={{"Microsoft Outlook Trigger"}}
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
  "$id": "https://n8n.io/schemas/nodes/microsoftOutlookTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft Outlook Trigger Node",
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
            "messageReceived"
          ],
          "default": "messageReceived"
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
      "name": "microsoftOutlookOAuth2Api",
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
