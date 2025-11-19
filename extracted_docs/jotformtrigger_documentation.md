---
title: "Node: Jotform Trigger"
slug: "node-jotformtrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle Jotform events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Jotform Trigger

**Purpose.** Handle Jotform events via webhooks


---

## Node Details

- **Icon:** `{'light': 'file:jotform.svg', 'dark': 'file:jotform.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **jotFormApi**: N/A


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
| `jotFormApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Name or ID | `form` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Resolve Data | `resolveData` | boolean | True | ✗ | By default does the webhook-data use internal keys instead of the names. If this option gets activated, it will resolve the keys automatically to the actual names. |  |
| Only Answers | `onlyAnswers` | boolean | True | ✗ | Whether to return only the answers of the form and not any of the other data |  |

---

## Load Options Methods

- `getForms`
- `limit`

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
* Categories: Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: jotFormTrigger
displayName: Jotform Trigger
description: Handle Jotform events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: jotFormApi
  required: true
params:
- id: form
  name: Form Name or ID
  type: options
  default: ''
  required: true
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Form Name or ID
    name: form
    typeOptions:
      loadOptionsMethod: getForms
    possibleValues: []
- id: resolveData
  name: Resolve Data
  type: boolean
  default: true
  required: false
  description: By default does the webhook-data use internal keys instead of the names.
    If this option gets activated, it will resolve the keys automatically to the actual
    names.
  typeInfo:
    type: boolean
    displayName: Resolve Data
    name: resolveData
- id: onlyAnswers
  name: Only Answers
  type: boolean
  default: true
  required: false
  description: Whether to return only the answers of the form and not any of the other
    data
  typeInfo:
    type: boolean
    displayName: Only Answers
    name: onlyAnswers
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
  "$id": "https://n8n.io/schemas/nodes/jotFormTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Jotform Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "form": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "resolveData": {
          "description": "By default does the webhook-data use internal keys instead of the names. If this option gets activated, it will resolve the keys automatically to the actual names.",
          "type": "boolean",
          "default": true
        },
        "onlyAnswers": {
          "description": "Whether to return only the answers of the form and not any of the other data",
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
      "name": "jotFormApi",
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
