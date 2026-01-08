---
title: "Node: Mautic Trigger"
slug: "node-mautictrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle Mautic events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Mautic Trigger

**Purpose.** Handle Mautic events via webhooks


---

## Node Details

- **Icon:** `file:mautic.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **mauticApi**: N/A
- **mauticOAuth2Api**: N/A


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
| `mauticApi` | ✓ | {'show': {'authentication': ['credentials']}} |
| `mauticOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | credentials | ✗ |  |  |

**Authentication options:**

* **Credentials** (`credentials`)
* **OAuth2** (`oAuth2`)

| Event Names or IDs | `events` | multiOptions | [] | ✓ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Events Order | `eventsOrder` | options | ASC | ✗ | Order direction for queued events in one webhook. Can be “DESC” or “ASC”. |  |

**Events Order options:**

* **ASC** (`ASC`)
* **DESC** (`DESC`)


---

## Load Options Methods

- `getEvents`

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
node: mauticTrigger
displayName: Mautic Trigger
description: Handle Mautic events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: mauticApi
  required: true
- name: mauticOAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: credentials
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: credentials
      name: Credentials
      description: ''
    - value: oAuth2
      name: OAuth2
      description: ''
- id: events
  name: Event Names or IDs
  type: multiOptions
  default: []
  required: true
  description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Event Names or IDs
    name: events
    typeOptions:
      loadOptionsMethod: getEvents
    possibleValues: []
- id: eventsOrder
  name: Events Order
  type: options
  default: ASC
  required: false
  description: Order direction for queued events in one webhook. Can be “DESC” or
    “ASC”.
  typeInfo:
    type: options
    displayName: Events Order
    name: eventsOrder
    possibleValues:
    - value: ASC
      name: ASC
      description: ''
    - value: DESC
      name: DESC
      description: ''
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
  "$id": "https://n8n.io/schemas/nodes/mauticTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Mautic Trigger Node",
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
            "credentials",
            "oAuth2"
          ],
          "default": "credentials"
        },
        "events": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "eventsOrder": {
          "description": "Order direction for queued events in one webhook. Can be \u201cDESC\u201d or \u201cASC\u201d.",
          "type": "string",
          "enum": [
            "ASC",
            "DESC"
          ],
          "default": "ASC"
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
      "name": "mauticApi",
      "required": true
    },
    {
      "name": "mauticOAuth2Api",
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
