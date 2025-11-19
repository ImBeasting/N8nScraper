---
title: "Node: Cron"
slug: "node-cron"
version: "1"
updated: "2025-11-13"
summary: "Triggers the workflow at a specific time"
node_type: "trigger"
group: "['trigger', 'schedule']"
---

# Node: Cron

**Purpose.** Triggers the workflow at a specific time


---

## Node Details

- **Icon:** `fa:clock`
- **Group:** `['trigger', 'schedule']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** Your cron trigger will now trigger executions on the schedule you have defined.
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice**: This workflow will run on the schedule you define here once you <a data-key="activate">activate</a> it.<br><br>For testing, you can also trigger it manually: by going back to the canvas and clicking 'execute workflow'

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger Times | `triggerTimes` | fixedCollection | {} | ✗ | Triggers for the workflow | e.g. Add Cron Time |  |

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
* Aliases: Time, Scheduler, Polling, Cron, Interval

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: cron
displayName: Cron
description: Triggers the workflow at a specific time
version: '1'
nodeType: trigger
group:
- trigger
- schedule
params:
- id: triggerTimes
  name: Trigger Times
  type: fixedCollection
  default: {}
  required: false
  description: Triggers for the workflow
  placeholder: Add Cron Time
  typeInfo:
    type: fixedCollection
    displayName: Trigger Times
    name: triggerTimes
    typeOptions:
      multipleValues: true
    subProperties: []
ui_elements:
  notices:
  - name: notice
    text: 'This workflow will run on the schedule you define here once you <a data-key="activate">activate</a>
      it.<br><br>For testing, you can also trigger it manually: by going back to the
      canvas and clicking ''execute workflow'''
    conditions: null
  tooltips: []
  placeholders:
  - field: triggerTimes
    text: Add Cron Time
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
  "$id": "https://n8n.io/schemas/nodes/cron.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Cron Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "triggerTimes": {
          "description": "Triggers for the workflow",
          "type": "string",
          "default": {},
          "examples": [
            "Add Cron Time"
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
