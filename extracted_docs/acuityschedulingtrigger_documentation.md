---
title: "Node: Acuity Scheduling Trigger"
slug: "node-acuityschedulingtrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle Acuity Scheduling events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Acuity Scheduling Trigger

**Purpose.** Handle Acuity Scheduling events via webhooks


---

## Node Details

- **Icon:** `file:acuityScheduling.png`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **acuitySchedulingApi**: N/A
- **acuitySchedulingOAuth2Api**: N/A


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
| `acuitySchedulingApi` | ✓ | {'show': {'authentication': ['apiKey']}} |
| `acuitySchedulingOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | apiKey | ✗ |  |  |

**Authentication options:**

* **API Key** (`apiKey`)
* **OAuth2** (`oAuth2`)

| Event | `event` | options |  | ✓ | Is called whenever an appointment is canceled |  |

**Event options:**

* **appointment.canceled** (`appointment.canceled`) - Is called whenever an appointment is canceled
* **appointment.changed** (`appointment.changed`) - Is called when the appointment is changed in any way
* **appointment.rescheduled** (`appointment.rescheduled`) - Is called when the appointment is rescheduled to a new time
* **appointment.scheduled** (`appointment.scheduled`) - Is called once when an appointment is initially booked
* **order.completed** (`order.completed`) - Is called when an order is completed

| Resolve Data | `resolveData` | boolean | True | ✗ | By default does the webhook-data only contain the ID of the object. If this option gets activated, it will resolve the data automatically. |  |

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
node: acuitySchedulingTrigger
displayName: Acuity Scheduling Trigger
description: Handle Acuity Scheduling events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: acuitySchedulingApi
  required: true
- name: acuitySchedulingOAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: apiKey
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: apiKey
      name: API Key
      description: ''
    - value: oAuth2
      name: OAuth2
      description: ''
- id: event
  name: Event
  type: options
  default: ''
  required: true
  description: Is called whenever an appointment is canceled
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: appointment.canceled
      name: appointment.canceled
      description: Is called whenever an appointment is canceled
    - value: appointment.changed
      name: appointment.changed
      description: Is called when the appointment is changed in any way
    - value: appointment.rescheduled
      name: appointment.rescheduled
      description: Is called when the appointment is rescheduled to a new time
    - value: appointment.scheduled
      name: appointment.scheduled
      description: Is called once when an appointment is initially booked
    - value: order.completed
      name: order.completed
      description: Is called when an order is completed
- id: resolveData
  name: Resolve Data
  type: boolean
  default: true
  required: false
  description: By default does the webhook-data only contain the ID of the object.
    If this option gets activated, it will resolve the data automatically.
  typeInfo:
    type: boolean
    displayName: Resolve Data
    name: resolveData
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
  "$id": "https://n8n.io/schemas/nodes/acuitySchedulingTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Acuity Scheduling Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "apiKey",
            "oAuth2"
          ],
          "default": "apiKey"
        },
        "event": {
          "description": "Is called whenever an appointment is canceled",
          "type": "string",
          "enum": [
            "appointment.canceled",
            "appointment.changed",
            "appointment.rescheduled",
            "appointment.scheduled",
            "order.completed"
          ],
          "default": ""
        },
        "resolveData": {
          "description": "By default does the webhook-data only contain the ID of the object. If this option gets activated, it will resolve the data automatically.",
          "type": "boolean",
          "default": true
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
      "name": "acuitySchedulingApi",
      "required": true
    },
    {
      "name": "acuitySchedulingOAuth2Api",
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
