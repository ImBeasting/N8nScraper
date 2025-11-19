---
title: "Node: Simulate Trigger"
slug: "node-simulatetrigger"
version: "1"
updated: "2025-11-13"
summary: "Simulate a trigger node"
node_type: "trigger"
group: "['trigger']"
---

# Node: Simulate Trigger

**Purpose.** Simulate a trigger node
**Subtitle.** ={{$parameter.subtitle || undefined}}


---

## Node Details

- **Icon:** `fa:arrow-right`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`


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

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Icon to Display on Canvas | `icon` | options | n8n-nodes-base.noOp | ✗ | Select a type of node to show corresponding icon |  |
| Subtitle | `subtitle` | string |  | ✗ | e.g. e.g. 'record: read' |  |
| JSON | `jsonOutput` | json | [\n  {\n   | ✗ |  |  |
| Execution Duration (MS) | `executionDuration` | number | 150 | ✗ | Execution duration in milliseconds | min:0, max:∞ |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `{{$parameter.subtitle || undefined}}`
- `={{$parameter.subtitle || undefined}}`

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
* Categories: Core Nodes
* Aliases: placeholder, stub, dummy

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: simulateTrigger
displayName: Simulate Trigger
description: Simulate a trigger node
version: '1'
nodeType: trigger
group:
- trigger
params:
- id: icon
  name: Icon to Display on Canvas
  type: options
  default: n8n-nodes-base.noOp
  required: false
  description: Select a type of node to show corresponding icon
  typeInfo:
    type: options
    displayName: Icon to Display on Canvas
    name: icon
    typeOptions:
      loadOptionsMethod: getNodeTypes
    possibleValues: []
- id: subtitle
  name: Subtitle
  type: string
  default: ''
  required: false
  description: ''
  placeholder: 'e.g. ''record: read'''
  typeInfo:
    type: string
    displayName: Subtitle
    name: subtitle
- id: jsonOutput
  name: JSON
  type: json
  default: '[\n  {\n  '
  required: false
  description: ''
  typeInfo:
    type: json
    displayName: JSON
    name: jsonOutput
    typeOptions:
      rows: 5
- id: executionDuration
  name: Execution Duration (MS)
  type: number
  default: 150
  required: false
  description: Execution duration in milliseconds
  typeInfo:
    type: number
    displayName: Execution Duration (MS)
    name: executionDuration
    typeOptions:
      minValue: 0
common_expressions:
- '{{$parameter.subtitle || undefined}}'
- ={{$parameter.subtitle || undefined}}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: subtitle
    text: 'e.g. ''record: read'''
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
  "$id": "https://n8n.io/schemas/nodes/simulateTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Simulate Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "icon": {
          "description": "Select a type of node to show corresponding icon",
          "type": "string",
          "default": "n8n-nodes-base.noOp"
        },
        "subtitle": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. 'record: read'"
          ]
        },
        "jsonOutput": {
          "description": "",
          "type": "string",
          "default": "[\\n  {\\n  "
        },
        "executionDuration": {
          "description": "Execution duration in milliseconds",
          "type": "number",
          "default": 150
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
