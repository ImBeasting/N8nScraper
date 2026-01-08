---
title: "Node: Brevo Trigger"
slug: "node-brevotrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when Brevo events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Brevo Trigger

**Purpose.** Starts the workflow when Brevo events occur


---

## Node Details

- **Icon:** `file:brevo.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **sendInBlueApi**: N/A


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
| `sendInBlueApi` | ✓ | {'show': {}} |

---

## API Patterns

**HTTP Methods:** DELETE, GET, POST

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `type` | options | transactional | ✓ |  |  |

**Resource options:**

* **Inbound** (`inbound`)
* **Marketing** (`marketing`)
* **Transactional** (`transactional`)

| Trigger On | `events` | multiOptions | [] | ✓ | Triggers when transactional email is blocked | e.g. Add Event |  |

**Trigger On options:**

* **Email Blocked** (`blocked`) - Triggers when transactional email is blocked
* **Email Clicked** (`click`) - Triggers when transactional email is clicked
* **Email Deferred** (`deferred`) - Triggers when transactional email is deferred
* **Email Delivered** (`delivered`) - Triggers when transactional email is delivered
* **Email Hard Bounce** (`hardBounce`) - Triggers when transactional email is hard bounced
* **Email Invalid** (`invalid`) - Triggers when transactional email is invalid
* **Email Marked Spam** (`spam`) - Triggers when transactional email is set to spam
* **Email Opened** (`opened`) - Triggers when transactional email is opened
* **Email Sent** (`request`) - Triggers when transactional email is sent
* **Email Soft-Bounce** (`softBounce`) - Triggers when transactional email is soft bounced
* **Email Unique Open** (`uniqueOpened`) - Triggers when transactional email is unique opened
* **Email Unsubscribed** (`unsubscribed`) - Triggers when transactional email is unsubscribed

| Trigger On | `events` | multiOptions | [] | ✓ | Triggers when marketing email is clicked | e.g. Add Event |  |

**Trigger On options:**

* **Marketing Email Clicked** (`click`) - Triggers when marketing email is clicked
* **Marketing Email Delivered** (`delivered`) - Triggers when marketing email is delivered
* **Marketing Email Hard Bounce** (`hardBounce`) - Triggers when marketing email is hard bounced
* **Marketing Email List Addition** (`listAddition`) - Triggers when marketing email is clicked
* **Marketing Email Opened** (`opened`) - Triggers when marketing email is opened
* **Marketing Email Soft Bounce** (`softBounce`) - Triggers when marketing email is soft bounced
* **Marketing Email Spam** (`spam`) - Triggers when marketing email is spam
* **Marketing Email Unsubscribed** (`unsubscribed`) - Triggers when marketing email is unsubscribed

| Trigger On | `events` | multiOptions | [] | ✓ | Triggers when inbound email is processed | e.g. Add Event |  |

**Trigger On options:**

* **Inbound Email Processed** (`inboundEmailProcessed`) - Triggers when inbound email is processed


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
* Categories: Marketing, Communication
* Aliases: sendinblue

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: brevoTrigger
displayName: Brevo Trigger
description: Starts the workflow when Brevo events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: sendInBlueApi
  required: true
params:
- id: type
  name: Resource
  type: options
  default: transactional
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Resource
    name: type
    possibleValues:
    - value: inbound
      name: Inbound
      description: ''
    - value: marketing
      name: Marketing
      description: ''
    - value: transactional
      name: Transactional
      description: ''
- id: events
  name: Trigger On
  type: multiOptions
  default: []
  required: true
  description: Triggers when transactional email is blocked
  placeholder: Add Event
  validation: &id001
    required: true
    displayOptions:
      show:
        type:
        - inbound
  typeInfo: &id002
    type: multiOptions
    displayName: Trigger On
    name: events
    possibleValues:
    - value: inboundEmailProcessed
      name: Inbound Email Processed
      description: Triggers when inbound email is processed
- id: events
  name: Trigger On
  type: multiOptions
  default: []
  required: true
  description: Triggers when marketing email is clicked
  placeholder: Add Event
  validation: *id001
  typeInfo: *id002
- id: events
  name: Trigger On
  type: multiOptions
  default: []
  required: true
  description: Triggers when inbound email is processed
  placeholder: Add Event
  validation: *id001
  typeInfo: *id002
api_patterns:
  http_methods:
  - DELETE
  - GET
  - POST
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: events
    text: Add Event
  - field: events
    text: Add Event
  - field: events
    text: Add Event
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
  "$id": "https://n8n.io/schemas/nodes/brevoTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Brevo Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "type": {
          "description": "",
          "type": "string",
          "enum": [
            "inbound",
            "marketing",
            "transactional"
          ],
          "default": "transactional"
        },
        "events": {
          "description": "Triggers when inbound email is processed",
          "type": "string",
          "default": [],
          "examples": [
            "Add Event"
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
      "name": "sendInBlueApi",
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
