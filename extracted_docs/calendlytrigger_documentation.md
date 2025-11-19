---
title: "Node: Calendly Trigger"
slug: "node-calendlytrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Calendly events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Calendly Trigger

**Purpose.** Starts the workflow when Calendly events occur


---

## Node Details

- **Icon:** `file:calendly.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **calendlyApi**: N/A
- **calendlyOAuth2Api**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **deprecationNotice** when authentication=['apiKey']: Action required: Calendly will discontinue API Key authentication on May 31, 2025. Update node to use OAuth2 authentication now to ensure your workflows continue to work.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `calendlyApi` | ✓ | {'show': {'authentication': ['apiKey']}} |
| `calendlyOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | apiKey | ✗ |  |  |

**Authentication options:**

* **OAuth2 (recommended)** (`oAuth2`)
* **API Key or Personal Access Token** (`apiKey`)

| Scope | `scope` | options | user | ✓ | Triggers the webhook for all subscribed events within the organization | e.g. Ignored if you are using an API Key |  |

**Scope options:**

* **Organization** (`organization`) - Triggers the webhook for all subscribed events within the organization
* **User** (`user`) - Triggers the webhook for subscribed events that belong to the current user

| Events | `events` | multiOptions | [] | ✓ | Receive notifications when a new Calendly event is created |  |

**Events options:**

* **Event Created** (`invitee.created`) - Receive notifications when a new Calendly event is created
* **Event Canceled** (`invitee.canceled`) - Receive notifications when a Calendly event is canceled


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
node: calendlyTrigger
displayName: Calendly Trigger
description: Starts the workflow when Calendly events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: calendlyApi
  required: true
- name: calendlyOAuth2Api
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
    - value: oAuth2
      name: OAuth2 (recommended)
      description: ''
    - value: apiKey
      name: API Key or Personal Access Token
      description: ''
- id: scope
  name: Scope
  type: options
  default: user
  required: true
  description: Triggers the webhook for all subscribed events within the organization
  hint: Ignored if you are using an API Key
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Scope
    name: scope
    possibleValues:
    - value: organization
      name: Organization
      description: Triggers the webhook for all subscribed events within the organization
    - value: user
      name: User
      description: Triggers the webhook for subscribed events that belong to the current
        user
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: Receive notifications when a new Calendly event is created
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: invitee.created
      name: Event Created
      description: Receive notifications when a new Calendly event is created
    - value: invitee.canceled
      name: Event Canceled
      description: Receive notifications when a Calendly event is canceled
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: deprecationNotice
    text: 'Action required: Calendly will discontinue API Key authentication on May
      31, 2025. Update node to use OAuth2 authentication now to ensure your workflows
      continue to work.'
    conditions:
      show:
        authentication:
        - apiKey
  tooltips: []
  placeholders: []
  hints:
  - field: scope
    text: Ignored if you are using an API Key
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
  "$id": "https://n8n.io/schemas/nodes/calendlyTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Calendly Trigger Node",
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
            "oAuth2",
            "apiKey"
          ],
          "default": "apiKey"
        },
        "scope": {
          "description": "Triggers the webhook for all subscribed events within the organization",
          "type": "string",
          "enum": [
            "organization",
            "user"
          ],
          "default": "user"
        },
        "events": {
          "description": "Receive notifications when a new Calendly event is created",
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
      "name": "calendlyApi",
      "required": true
    },
    {
      "name": "calendlyOAuth2Api",
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
