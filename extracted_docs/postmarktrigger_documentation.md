---
title: "Node: Postmark Trigger"
slug: "node-postmarktrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when Postmark events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Postmark Trigger

**Purpose.** Starts the workflow when Postmark events occur


---

## Node Details

- **Icon:** `file:postmark.png`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **postmarkApi**: N/A


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
| `postmarkApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `events` | multiOptions | [] | ✓ | Trigger on bounce |  |

**Events options:**

* **Bounce** (`bounce`) - Trigger on bounce
* **Click** (`click`) - Trigger on click
* **Delivery** (`delivery`) - Trigger on delivery
* **Open** (`open`) - Trigger webhook on open
* **Spam Complaint** (`spamComplaint`) - Trigger on spam complaint
* **Subscription Change** (`subscriptionChange`) - Trigger on subscription change

| First Open | `firstOpen` | boolean | False | ✗ | Only fires on first open for event "Open" |  |
| Include Content | `includeContent` | boolean | False | ✗ | Whether to include message content for events "Bounce" and "Spam Complaint" |  |

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
node: postmarkTrigger
displayName: Postmark Trigger
description: Starts the workflow when Postmark events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: postmarkApi
  required: true
params:
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: Trigger on bounce
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: bounce
      name: Bounce
      description: Trigger on bounce
    - value: click
      name: Click
      description: Trigger on click
    - value: delivery
      name: Delivery
      description: Trigger on delivery
    - value: open
      name: Open
      description: Trigger webhook on open
    - value: spamComplaint
      name: Spam Complaint
      description: Trigger on spam complaint
    - value: subscriptionChange
      name: Subscription Change
      description: Trigger on subscription change
- id: firstOpen
  name: First Open
  type: boolean
  default: false
  required: false
  description: Only fires on first open for event "Open"
  validation:
    displayOptions:
      show:
        events:
        - open
  typeInfo:
    type: boolean
    displayName: First Open
    name: firstOpen
- id: includeContent
  name: Include Content
  type: boolean
  default: false
  required: false
  description: Whether to include message content for events "Bounce" and "Spam Complaint"
  validation:
    displayOptions:
      show:
        events:
        - bounce
        - spamComplaint
  typeInfo:
    type: boolean
    displayName: Include Content
    name: includeContent
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
  "$id": "https://n8n.io/schemas/nodes/postmarkTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Postmark Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "Trigger on bounce",
          "type": "string",
          "default": []
        },
        "firstOpen": {
          "description": "Only fires on first open for event \"Open\"",
          "type": "boolean",
          "default": false
        },
        "includeContent": {
          "description": "Whether to include message content for events \"Bounce\" and \"Spam Complaint\"",
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
      "name": "postmarkApi",
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
