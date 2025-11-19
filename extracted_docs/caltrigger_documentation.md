---
title: "Node: Cal.com Trigger"
slug: "node-caltrigger"
version: "['1', '2']"
updated: "2025-11-13"
summary: "Handle Cal.com events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Cal.com Trigger

**Purpose.** Handle Cal.com events via webhooks
**Subtitle.** =Events: {{$parameter["events"].join(", ")}}


---

## Node Details

- **Icon:** `{'light': 'file:cal.svg', 'dark': 'file:cal.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **calApi**: N/A


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
| `calApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `events` | multiOptions | [] | ✓ | Receive notifications when a Cal event is canceled |  |

**Events options:**

* **Booking Cancelled** (`BOOKING_CANCELLED`) - Receive notifications when a Cal event is canceled
* **Booking Created** (`BOOKING_CREATED`) - Receive notifications when a new Cal event is created
* **Booking Rescheduled** (`BOOKING_RESCHEDULED`) - Receive notifications when a Cal event is rescheduled
* **Meeting Ended** (`MEETING_ENDED`) - Receive notifications when a Cal event or meeting has ended

| API Version | `version` | options | 1 | ✗ |  |  |

**API Version options:**

* **Before v2.0** (``)
* **v2.0 Onwards** (``)

| Options | `options` | collection | {} | ✗ | The ID of the App to monitor | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| App ID | `appId` | string |  | The ID of the App to monitor |
| EventType Name or ID | `eventTypeId` | options |  | The EventType to monitor. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Payload Template | `payloadTemplate` | string |  | Template to customize the webhook payload |

</details>


---

## Load Options Methods

- `getEventTypes`

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
* Categories: Productivity, Utility

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: calTrigger
displayName: Cal.com Trigger
description: Handle Cal.com events via webhooks
version:
- '1'
- '2'
nodeType: trigger
group:
- trigger
credentials:
- name: calApi
  required: true
params:
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: Receive notifications when a Cal event is canceled
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: BOOKING_CANCELLED
      name: Booking Cancelled
      description: Receive notifications when a Cal event is canceled
    - value: BOOKING_CREATED
      name: Booking Created
      description: Receive notifications when a new Cal event is created
    - value: BOOKING_RESCHEDULED
      name: Booking Rescheduled
      description: Receive notifications when a Cal event is rescheduled
    - value: MEETING_ENDED
      name: Meeting Ended
      description: Receive notifications when a Cal event or meeting has ended
- id: version
  name: API Version
  type: options
  default: 1
  required: false
  description: ''
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: options
    displayName: API Version
    name: version
    possibleValues:
    - value: Before v2.0
      name: Before v2.0
      description: ''
    - value: v2.0 Onwards
      name: v2.0 Onwards
      description: ''
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: The ID of the App to monitor
  placeholder: Add Field
  typeInfo:
    type: collection
    displayName: Options
    name: options
    typeOptions:
      loadOptionsMethod: getEventTypes
    subProperties:
    - displayName: App ID
      name: appId
      type: string
      description: The ID of the App to monitor
      default: ''
    - displayName: EventType Name or ID
      name: eventTypeId
      type: options
      description: The EventType to monitor. Choose from the list, or specify an ID
        using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
      default: ''
      typeOptions:
        loadOptionsMethod: getEventTypes
    - displayName: Payload Template
      name: payloadTemplate
      type: string
      description: Template to customize the webhook payload
      default: ''
      typeOptions:
        rows: 4
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: options
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/calTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Cal.com Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "Receive notifications when a Cal event is canceled",
          "type": "string",
          "default": []
        },
        "version": {
          "description": "",
          "type": "string",
          "enum": [
            "Before v2.0",
            "v2.0 Onwards"
          ],
          "default": 1
        },
        "options": {
          "description": "The ID of the App to monitor",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
    "version": [
      "1",
      "2"
    ]
  },
  "credentials": [
    {
      "name": "calApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
