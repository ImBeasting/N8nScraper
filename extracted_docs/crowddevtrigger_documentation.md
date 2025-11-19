---
title: "Node: crowd.dev Trigger"
slug: "node-crowddevtrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when crowd.dev events occur."
node_type: "trigger"
group: "['trigger']"
---

# Node: crowd.dev Trigger

**Purpose.** Starts the workflow when crowd.dev events occur.


---

## Node Details

- **Icon:** `{'light': 'file:crowdDev.svg', 'dark': 'file:crowdDev.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **crowdDevApi**: N/A


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
| `crowdDevApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger | `trigger` | options | new_activity | ✓ | What will trigger an automation |  |

**Trigger options:**

* **New Activity** (`new_activity`)
* **New Member** (`new_member`)


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
node: crowdDevTrigger
displayName: crowd.dev Trigger
description: Starts the workflow when crowd.dev events occur.
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: crowdDevApi
  required: true
params:
- id: trigger
  name: Trigger
  type: options
  default: new_activity
  required: true
  description: What will trigger an automation
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Trigger
    name: trigger
    possibleValues:
    - value: new_activity
      name: New Activity
      description: ''
    - value: new_member
      name: New Member
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
  "$id": "https://n8n.io/schemas/nodes/crowdDevTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "crowd.dev Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "trigger": {
          "description": "What will trigger an automation",
          "type": "string",
          "enum": [
            "new_activity",
            "new_member"
          ],
          "default": "new_activity"
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
      "name": "crowdDevApi",
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
