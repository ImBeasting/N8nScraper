---
title: "Node: LoneScale Trigger"
slug: "node-lonescaletrigger"
version: "1"
updated: "2026-01-08"
summary: "Trigger LoneScale Workflow"
node_type: "trigger"
group: "['trigger']"
---

# Node: LoneScale Trigger

**Purpose.** Trigger LoneScale Workflow


---

## Node Details

- **Icon:** `{'light': 'file:loneScale.svg', 'dark': 'file:loneScale.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **loneScaleApi**: N/A


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
| `loneScaleApi` | ✓ | - |

---

## API Patterns

**Headers Used:** X-API-KEY, Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workflow Name | `workflow` | options |  | ✓ | Select one workflow. Choose from the list |  |

---

## Load Options Methods

- `getWorkflows`
- `return`

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
node: lonescaleTrigger
displayName: LoneScale Trigger
description: Trigger LoneScale Workflow
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: loneScaleApi
  required: true
params:
- id: workflow
  name: Workflow Name
  type: options
  default: ''
  required: true
  description: Select one workflow. Choose from the list
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Workflow Name
    name: workflow
    typeOptions:
      loadOptionsMethod: getWorkflows
    possibleValues: []
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - X-API-KEY
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
  "$id": "https://n8n.io/schemas/nodes/lonescaleTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "LoneScale Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "workflow": {
          "description": "Select one workflow. Choose from the list",
          "type": "string",
          "default": ""
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
      "name": "loneScaleApi",
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
