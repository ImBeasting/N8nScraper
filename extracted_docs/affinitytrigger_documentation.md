---
title: "Node: Affinity Trigger"
slug: "node-affinitytrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle Affinity events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Affinity Trigger

**Purpose.** Handle Affinity events via webhooks


---

## Node Details

- **Icon:** `{'light': 'file:affinity.svg', 'dark': 'file:affinity.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **affinityApi**: N/A


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
| `affinityApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `events` | multiOptions | [] | ✓ | Webhook events that will be enabled for that endpoint |  |

**Events options:**

* **field_value.created** (`field_value.created`)
* **field_value.deleted** (`field_value.deleted`)
* **field_value.updated** (`field_value.updated`)
* **field.created** (`field.created`)
* **field.deleted** (`field.deleted`)
* **field.updated** (`field.updated`)
* **file.created** (`file.created`)
* **file.deleted** (`file.deleted`)
* **list_entry.created** (`list_entry.created`)
* **list_entry.deleted** (`list_entry.deleted`)
* **list.created** (`list.created`)
* **list.deleted** (`list.deleted`)
* **list.updated** (`list.updated`)
* **note.created** (`note.created`)
* **note.deleted** (`note.deleted`)
* **note.updated** (`note.updated`)
* **opportunity.created** (`opportunity.created`)
* **opportunity.deleted** (`opportunity.deleted`)
* **opportunity.updated** (`opportunity.updated`)
* **organization.created** (`organization.created`)
* **organization.deleted** (`organization.deleted`)
* **organization.updated** (`organization.updated`)
* **person.created** (`person.created`)
* **person.deleted** (`person.deleted`)
* **person.updated** (`person.updated`)


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
node: affinityTrigger
displayName: Affinity Trigger
description: Handle Affinity events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: affinityApi
  required: true
params:
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: Webhook events that will be enabled for that endpoint
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: field_value.created
      name: field_value.created
      description: ''
    - value: field_value.deleted
      name: field_value.deleted
      description: ''
    - value: field_value.updated
      name: field_value.updated
      description: ''
    - value: field.created
      name: field.created
      description: ''
    - value: field.deleted
      name: field.deleted
      description: ''
    - value: field.updated
      name: field.updated
      description: ''
    - value: file.created
      name: file.created
      description: ''
    - value: file.deleted
      name: file.deleted
      description: ''
    - value: list_entry.created
      name: list_entry.created
      description: ''
    - value: list_entry.deleted
      name: list_entry.deleted
      description: ''
    - value: list.created
      name: list.created
      description: ''
    - value: list.deleted
      name: list.deleted
      description: ''
    - value: list.updated
      name: list.updated
      description: ''
    - value: note.created
      name: note.created
      description: ''
    - value: note.deleted
      name: note.deleted
      description: ''
    - value: note.updated
      name: note.updated
      description: ''
    - value: opportunity.created
      name: opportunity.created
      description: ''
    - value: opportunity.deleted
      name: opportunity.deleted
      description: ''
    - value: opportunity.updated
      name: opportunity.updated
      description: ''
    - value: organization.created
      name: organization.created
      description: ''
    - value: organization.deleted
      name: organization.deleted
      description: ''
    - value: organization.updated
      name: organization.updated
      description: ''
    - value: person.created
      name: person.created
      description: ''
    - value: person.deleted
      name: person.deleted
      description: ''
    - value: person.updated
      name: person.updated
      description: ''
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
  "$id": "https://n8n.io/schemas/nodes/affinityTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Affinity Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "Webhook events that will be enabled for that endpoint",
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
      "name": "affinityApi",
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
