---
title: "Node: n8n Trigger"
slug: "node-n8ntrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle events and perform actions on your n8n instance"
node_type: "trigger"
group: "['trigger']"
---

# Node: n8n Trigger

**Purpose.** Handle events and perform actions on your n8n instance


---

## Node Details

- **Icon:** `file:n8nTrigger.svg`
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
| Events | `events` | multiOptions | [] | ✓ | Specifies under which conditions an execution should happen:
				<ul>
					<li><b>Active Workflow Updated</b>: Triggers when this workflow is updated</li>
					<li><b>Instance Started</b>:  Triggers when this n8n instance is started or re-started</li>
					<li><b>Workflow Activated</b>: Triggers when this workflow is activated</li>
				</ul> |  |

**Events options:**

* **Active Workflow Updated** (`update`) - Triggers when this workflow is updated
* **Instance Started** (`init`) - Triggers when this n8n instance is started or re-started
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
node: n8nTrigger
displayName: n8n Trigger
description: Handle events and perform actions on your n8n instance
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
    \t\t<ul>\n\t\t\t\t\t<li><b>Active Workflow Updated</b>: Triggers when this workflow\
    \ is updated</li>\n\t\t\t\t\t<li><b>Instance Started</b>:  Triggers when this\
    \ n8n instance is started or re-started</li>\n\t\t\t\t\t<li><b>Workflow Activated</b>:\
    \ Triggers when this workflow is activated</li>\n\t\t\t\t</ul>"
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
    - value: init
      name: Instance Started
      description: Triggers when this n8n instance is started or re-started
    - value: activate
      name: Workflow Activated
      description: Triggers when this workflow is activated
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
  "$id": "https://n8n.io/schemas/nodes/n8nTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "n8n Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "Specifies under which conditions an execution should happen:\n\t\t\t\t<ul>\n\t\t\t\t\t<li><b>Active Workflow Updated</b>: Triggers when this workflow is updated</li>\n\t\t\t\t\t<li><b>Instance Started</b>:  Triggers when this n8n instance is started or re-started</li>\n\t\t\t\t\t<li><b>Workflow Activated</b>: Triggers when this workflow is activated</li>\n\t\t\t\t</ul>",
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
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
