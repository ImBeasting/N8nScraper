---
title: "Node: ActiveCampaign Trigger"
slug: "node-activecampaigntrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle ActiveCampaign events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: ActiveCampaign Trigger

**Purpose.** Handle ActiveCampaign events via webhooks


---

## Node Details

- **Icon:** `{'light': 'file:activeCampaign.svg', 'dark': 'file:activeCampaign.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **activeCampaignApi**: N/A


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
| `activeCampaignApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event Names or IDs | `events` | multiOptions | [] | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Source | `sources` | multiOptions | [] | ✗ | Run the hooks when a contact triggers the action |  |

**Source options:**

* **Public** (`public`) - Run the hooks when a contact triggers the action
* **Admin** (`admin`) - Run the hooks when an admin user triggers the action
* **Api** (`api`) - Run the hooks when an API call triggers the action
* **System** (`system`) - Run the hooks when automated systems triggers the action


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
* Categories: Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: activeCampaignTrigger
displayName: ActiveCampaign Trigger
description: Handle ActiveCampaign events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: activeCampaignApi
  required: true
params:
- id: events
  name: Event Names or IDs
  type: multiOptions
  default: []
  required: false
  description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  typeInfo:
    type: multiOptions
    displayName: Event Names or IDs
    name: events
    typeOptions:
      loadOptionsMethod: getEvents
    possibleValues: []
- id: sources
  name: Source
  type: multiOptions
  default: []
  required: false
  description: Run the hooks when a contact triggers the action
  typeInfo:
    type: multiOptions
    displayName: Source
    name: sources
    possibleValues:
    - value: public
      name: Public
      description: Run the hooks when a contact triggers the action
    - value: admin
      name: Admin
      description: Run the hooks when an admin user triggers the action
    - value: api
      name: Api
      description: Run the hooks when an API call triggers the action
    - value: system
      name: System
      description: Run the hooks when automated systems triggers the action
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
  "$id": "https://n8n.io/schemas/nodes/activeCampaignTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ActiveCampaign Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "sources": {
          "description": "Run the hooks when a contact triggers the action",
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
      "name": "activeCampaignApi",
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
