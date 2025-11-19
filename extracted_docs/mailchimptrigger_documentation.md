---
title: "Node: Mailchimp Trigger"
slug: "node-mailchimptrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle Mailchimp events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Mailchimp Trigger

**Purpose.** Handle Mailchimp events via webhooks


---

## Node Details

- **Icon:** `{'light': 'file:mailchimp.svg', 'dark': 'file:mailchimp.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **mailchimpApi**: N/A
- **mailchimpOAuth2Api**: N/A


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
| `mailchimpApi` | ✓ | {'show': {'authentication': ['apiKey']}} |
| `mailchimpOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**HTTP Methods:** GET

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | apiKey | ✗ |  |  |

**Authentication options:**

* **API Key** (`apiKey`)
* **OAuth2** (`oAuth2`)

| List Name or ID | `list` | options |  | ✓ | The list that is gonna fire the event. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Events | `events` | multiOptions | [] | ✓ | The events that can trigger the webhook and whether they are enabled |  |

**Events options:**

* **Campaign Sent** (`campaign`) - Whether the webhook is triggered when a campaign is sent or cancelled
* **Cleaned** (`cleaned`) - Whether the webhook is triggered when a subscriber's email address is cleaned from the list
* **Email Address Updated** (`upemail`) - Whether the webhook is triggered when a subscriber's email address is changed
* **Profile Updated** (`profile`) - Whether the webhook is triggered when a subscriber's profile is updated
* **Subscribe** (`subscribe`) - Whether the webhook is triggered when a list subscriber is added
* **Unsubscribe** (`unsubscribe`) - Whether the webhook is triggered when a list member unsubscribes

| Sources | `sources` | multiOptions | [] | ✓ | The possible sources of any events that can trigger the webhook and whether they are enabled |  |

**Sources options:**

* **User** (`user`) - Whether the webhook is triggered by subscriber-initiated actions
* **Admin** (`admin`) - Whether the webhook is triggered by admin-initiated actions in the web interface
* **API** (`api`) - Whether the webhook is triggered by actions initiated via the API


---

## Load Options Methods

- `getLists`
- `for`
- `name`
- `value`

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: mailchimpTrigger
displayName: Mailchimp Trigger
description: Handle Mailchimp events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: mailchimpApi
  required: true
- name: mailchimpOAuth2Api
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
- id: list
  name: List Name or ID
  type: options
  default: ''
  required: true
  description: The list that is gonna fire the event. Choose from the list, or specify
    an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation:
    required: true
  typeInfo:
    type: options
    displayName: List Name or ID
    name: list
    typeOptions:
      loadOptionsMethod: getLists
    possibleValues: []
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: The events that can trigger the webhook and whether they are enabled
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: campaign
      name: Campaign Sent
      description: Whether the webhook is triggered when a campaign is sent or cancelled
    - value: cleaned
      name: Cleaned
      description: Whether the webhook is triggered when a subscriber's email address
        is cleaned from the list
    - value: upemail
      name: Email Address Updated
      description: Whether the webhook is triggered when a subscriber's email address
        is changed
    - value: profile
      name: Profile Updated
      description: Whether the webhook is triggered when a subscriber's profile is
        updated
    - value: subscribe
      name: Subscribe
      description: Whether the webhook is triggered when a list subscriber is added
    - value: unsubscribe
      name: Unsubscribe
      description: Whether the webhook is triggered when a list member unsubscribes
- id: sources
  name: Sources
  type: multiOptions
  default: []
  required: true
  description: The possible sources of any events that can trigger the webhook and
    whether they are enabled
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Sources
    name: sources
    possibleValues:
    - value: user
      name: User
      description: Whether the webhook is triggered by subscriber-initiated actions
    - value: admin
      name: Admin
      description: Whether the webhook is triggered by admin-initiated actions in
        the web interface
    - value: api
      name: API
      description: Whether the webhook is triggered by actions initiated via the API
api_patterns:
  http_methods:
  - GET
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
  "$id": "https://n8n.io/schemas/nodes/mailchimpTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Mailchimp Trigger Node",
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
        "list": {
          "description": "The list that is gonna fire the event. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "events": {
          "description": "The events that can trigger the webhook and whether they are enabled",
          "type": "string",
          "default": []
        },
        "sources": {
          "description": "The possible sources of any events that can trigger the webhook and whether they are enabled",
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
      "name": "mailchimpApi",
      "required": true
    },
    {
      "name": "mailchimpOAuth2Api",
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
