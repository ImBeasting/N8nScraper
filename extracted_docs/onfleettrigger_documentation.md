---
title: "Node: Onfleet Trigger"
slug: "node-onfleettrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when Onfleet events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Onfleet Trigger

**Purpose.** Starts the workflow when Onfleet events occur
**Subtitle.** ={{$parameter["triggerOn"]}}


---

## Node Details

- **Icon:** `file:Onfleet.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **onfleetApi**: N/A


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
| `onfleetApi` | ✓ | - |

---

## API Patterns

**Headers Used:** User-Agent, Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger On | `triggerOn` | options | [] | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | A name for the webhook for identification | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | A name for the webhook for identification |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["triggerOn"]}}`

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
* Categories: Miscellaneous

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: onfleetTrigger
displayName: Onfleet Trigger
description: Starts the workflow when Onfleet events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: onfleetApi
  required: true
params:
- id: triggerOn
  name: Trigger On
  type: options
  default: []
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Trigger On
    name: triggerOn
    possibleValues: []
- id: additionalFields
  name: Additional Fields
  type: collection
  default: {}
  required: false
  description: A name for the webhook for identification
  placeholder: Add Field
  typeInfo:
    type: collection
    displayName: Additional Fields
    name: additionalFields
    subProperties:
    - displayName: Name
      name: name
      type: string
      description: A name for the webhook for identification
      default: ''
common_expressions:
- ={{$parameter["triggerOn"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - User-Agent
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
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
  "$id": "https://n8n.io/schemas/nodes/onfleetTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Onfleet Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "triggerOn": {
          "description": "",
          "type": "string",
          "default": []
        },
        "additionalFields": {
          "description": "A name for the webhook for identification",
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
    "version": "1"
  },
  "credentials": [
    {
      "name": "onfleetApi",
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
