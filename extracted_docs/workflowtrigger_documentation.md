---
title: "Node: Workflow Trigger"
slug: "node-workflowtrigger"
version: "1"
updated: "2026-01-08"
summary: "Triggers based on various lifecycle events, like when a workflow is activated"
node_type: "trigger"
group: "['trigger']"
---

# Node: Workflow Trigger

**Purpose.** Triggers based on various lifecycle events, like when a workflow is activated


---

## Node Details

- **Icon:** `fa:network-wired`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** Your workflow will now trigger executions on the event you have defined.
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **oldVersionNotice**: This node is deprecated and would not be updated in the future. Please use 'n8n Trigger' node instead.

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `events` | multiOptions | [] | ✓ | Specifies under which conditions an execution should happen:
					<ul>
						<li><b>Active Workflow Updated</b>: Triggers when this workflow is updated</li>
						<li><b>Workflow Activated</b>: Triggers when this workflow is activated</li>
					</ul> |  |

**Events options:**

* **Active Workflow Updated** (`update`) - Triggers when this workflow is updated
* **Workflow Activated** (`activate`) - Triggers when this workflow is activated


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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: WorkflowTrigger
displayName: Workflow Trigger
description: Triggers based on various lifecycle events, like when a workflow is activated
version: '1'
nodeType: trigger
group:
- trigger
params:
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: "Specifies under which conditions an execution should happen:\n\t\t\
    \t\t\t<ul>\n\t\t\t\t\t\t<li><b>Active Workflow Updated</b>: Triggers when this\
    \ workflow is updated</li>\n\t\t\t\t\t\t<li><b>Workflow Activated</b>: Triggers\
    \ when this workflow is activated</li>\n\t\t\t\t\t</ul>"
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: update
      name: Active Workflow Updated
      description: Triggers when this workflow is updated
    - value: activate
      name: Workflow Activated
      description: Triggers when this workflow is activated
ui_elements:
  notices:
  - name: oldVersionNotice
    text: This node is deprecated and would not be updated in the future. Please use
      'n8n Trigger' node instead.
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
  "$id": "https://n8n.io/schemas/nodes/WorkflowTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Workflow Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "Specifies under which conditions an execution should happen:\n\t\t\t\t\t<ul>\n\t\t\t\t\t\t<li><b>Active Workflow Updated</b>: Triggers when this workflow is updated</li>\n\t\t\t\t\t\t<li><b>Workflow Activated</b>: Triggers when this workflow is activated</li>\n\t\t\t\t\t</ul>",
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
