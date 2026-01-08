---
title: "Node: Interval"
slug: "node-interval"
version: "1"
updated: "2026-01-08"
summary: "Triggers the workflow in a given interval"
node_type: "trigger"
group: "['trigger', 'schedule']"
---

# Node: Interval

**Purpose.** Triggers the workflow in a given interval


---

## Node Details

- **Icon:** `fa:hourglass`
- **Group:** `['trigger', 'schedule']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** Your interval trigger will now trigger executions on the schedule you have defined.
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice**: This workflow will run on the schedule you define here once you publish it.<br><br>For testing, you can also trigger it manually: by going back to the canvas and clicking 'execute workflow'

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Interval | `interval` | number | 1 | ✗ | Interval value | min:1, max:∞ |
| Unit | `unit` | options | seconds | ✗ | Unit of the interval value |  |

**Unit options:**

* **Seconds** (`seconds`)
* **Minutes** (`minutes`)
* **Hours** (`hours`)


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
* Aliases: Time, Scheduler, Polling

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: interval
displayName: Interval
description: Triggers the workflow in a given interval
version: '1'
nodeType: trigger
group:
- trigger
- schedule
params:
- id: interval
  name: Interval
  type: number
  default: 1
  required: false
  description: Interval value
  typeInfo:
    type: number
    displayName: Interval
    name: interval
    typeOptions:
      minValue: 1
- id: unit
  name: Unit
  type: options
  default: seconds
  required: false
  description: Unit of the interval value
  typeInfo:
    type: options
    displayName: Unit
    name: unit
    possibleValues:
    - value: seconds
      name: Seconds
      description: ''
    - value: minutes
      name: Minutes
      description: ''
    - value: hours
      name: Hours
      description: ''
ui_elements:
  notices:
  - name: notice
    text: 'This workflow will run on the schedule you define here once you publish
      it.<br><br>For testing, you can also trigger it manually: by going back to the
      canvas and clicking ''execute workflow'''
    conditions: null
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
  "$id": "https://n8n.io/schemas/nodes/interval.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Interval Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "interval": {
          "description": "Interval value",
          "type": "number",
          "default": 1
        },
        "unit": {
          "description": "Unit of the interval value",
          "type": "string",
          "enum": [
            "seconds",
            "minutes",
            "hours"
          ],
          "default": "seconds"
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
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
