---
title: "Node: Eventbrite Trigger"
slug: "node-eventbritetrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle Eventbrite events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Eventbrite Trigger

**Purpose.** Handle Eventbrite events via webhooks
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:eventbrite.png`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **eventbriteApi**: N/A
- **eventbriteOAuth2Api**: N/A


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
| `eventbriteApi` | ✓ | {'show': {'authentication': ['privateKey']}} |
| `eventbriteOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | privateKey | ✗ |  |  |

**Authentication options:**

* **Private Key** (`privateKey`)
* **OAuth2** (`oAuth2`)

| Organization Name or ID | `organization` | options |  | ✓ | The Eventbrite Organization to work on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Event Name or ID | `event` | options |  | ✓ | Limit the triggers to this event. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Actions | `actions` | multiOptions | [] | ✓ | One or more action to subscribe to |  |

**Actions options:**

* **attendee.checked_in** (`attendee.checked_in`)
* **attendee.checked_out** (`attendee.checked_out`)
* **attendee.updated** (`attendee.updated`)
* **event.created** (`event.created`)
* **event.published** (`event.published`)
* **event.unpublished** (`event.unpublished`)
* **event.updated** (`event.updated`)
* **order.placed** (`order.placed`)
* **order.refunded** (`order.refunded`)
* **order.updated** (`order.updated`)
* **organizer.updated** (`organizer.updated`)
* **ticket_class.created** (`ticket_class.created`)
* **ticket_class.deleted** (`ticket_class.deleted`)
* **ticket_class.updated** (`ticket_class.updated`)
* **venue.updated** (`venue.updated`)

| Resolve Data | `resolveData` | boolean | True | ✗ | By default does the webhook-data only contain the URL to receive the object data manually. If this option gets activated, it will resolve the data automatically. |  |

---

## Load Options Methods

- `getOrganizations`
- `for`
- `name`
- `value`

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
* Categories: Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: eventbriteTrigger
displayName: Eventbrite Trigger
description: Handle Eventbrite events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: eventbriteApi
  required: true
- name: eventbriteOAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: privateKey
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: privateKey
      name: Private Key
      description: ''
    - value: oAuth2
      name: OAuth2
      description: ''
- id: organization
  name: Organization Name or ID
  type: options
  default: ''
  required: true
  description: The Eventbrite Organization to work on. Choose from the list, or specify
    an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Organization Name or ID
    name: organization
    typeOptions:
      loadOptionsMethod: getOrganizations
    possibleValues: []
- id: event
  name: Event Name or ID
  type: options
  default: ''
  required: true
  description: Limit the triggers to this event. Choose from the list, or specify
    an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event Name or ID
    name: event
    typeOptions:
      loadOptionsMethod: getEvents
    possibleValues: []
- id: actions
  name: Actions
  type: multiOptions
  default: []
  required: true
  description: One or more action to subscribe to
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Actions
    name: actions
    possibleValues:
    - value: attendee.checked_in
      name: attendee.checked_in
      description: ''
    - value: attendee.checked_out
      name: attendee.checked_out
      description: ''
    - value: attendee.updated
      name: attendee.updated
      description: ''
    - value: event.created
      name: event.created
      description: ''
    - value: event.published
      name: event.published
      description: ''
    - value: event.unpublished
      name: event.unpublished
      description: ''
    - value: event.updated
      name: event.updated
      description: ''
    - value: order.placed
      name: order.placed
      description: ''
    - value: order.refunded
      name: order.refunded
      description: ''
    - value: order.updated
      name: order.updated
      description: ''
    - value: organizer.updated
      name: organizer.updated
      description: ''
    - value: ticket_class.created
      name: ticket_class.created
      description: ''
    - value: ticket_class.deleted
      name: ticket_class.deleted
      description: ''
    - value: ticket_class.updated
      name: ticket_class.updated
      description: ''
    - value: venue.updated
      name: venue.updated
      description: ''
- id: resolveData
  name: Resolve Data
  type: boolean
  default: true
  required: false
  description: By default does the webhook-data only contain the URL to receive the
    object data manually. If this option gets activated, it will resolve the data
    automatically.
  typeInfo:
    type: boolean
    displayName: Resolve Data
    name: resolveData
common_expressions:
- ={{$parameter["event"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
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
  "$id": "https://n8n.io/schemas/nodes/eventbriteTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Eventbrite Trigger Node",
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
            "privateKey",
            "oAuth2"
          ],
          "default": "privateKey"
        },
        "organization": {
          "description": "The Eventbrite Organization to work on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "event": {
          "description": "Limit the triggers to this event. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "actions": {
          "description": "One or more action to subscribe to",
          "type": "string",
          "default": []
        },
        "resolveData": {
          "description": "By default does the webhook-data only contain the URL to receive the object data manually. If this option gets activated, it will resolve the data automatically.",
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
      "name": "eventbriteApi",
      "required": true
    },
    {
      "name": "eventbriteOAuth2Api",
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
