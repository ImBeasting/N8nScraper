---
title: "Node: SSE Trigger"
slug: "node-ssetrigger"
version: "1"
updated: "2025-11-13"
summary: "Triggers the workflow when Server-Sent Events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: SSE Trigger

**Purpose.** Triggers the workflow when Server-Sent Events occur


---

## Node Details

- **Icon:** `fa:cloud-download-alt`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** You can now make calls to your SSE URL to trigger executions.
- **Supports CORS:** False
- **Trigger Panel:**
```json
{
  "executionsHelp": "{\n\t\t\t\tinactive:\n\t\t\t\t\t\"<b>While building your workflow</b>, click the 'execute step' button, then trigger an SSE event. This will trigger an execution, which will show up in this editor.<br /> <br /><b>Once you're happy with your workflow</b>, <a data-key='activate'>activate</a> it. Then every time a change is detected, the workflow will execute. These executions will show up in the <a data-key='executions'>executions list</a>, but not in the editor.\",\n\t\t\t\tactive:\n\t\t\t\t\t\"<b>While building your workflow</b>, click the 'execute step' button, then trigger an SSE event. This will trigger an execution, which will show up in this editor.<br /> <br /><b>Your workflow will also execute automatically</b>, since it's activated. Every time a change is detected, this node will trigger an execution. These executions will show up in the <a data-key='executions'>executions list</a>, but not in the editor.\",\n\t\t\t}",
  "activationHint": "Once you\u2019ve finished building your workflow, <a data-key="
}
```

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| URL | `url` | string |  | ✓ | The URL to receive the SSE from | e.g. http://example.com | url |

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
* Categories: Development, Core Nodes

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: sseTrigger
displayName: SSE Trigger
description: Triggers the workflow when Server-Sent Events occur
version: '1'
nodeType: trigger
group:
- trigger
params:
- id: url
  name: URL
  type: string
  default: ''
  required: true
  description: The URL to receive the SSE from
  placeholder: http://example.com
  validation:
    required: true
    format: url
  typeInfo:
    type: string
    displayName: URL
    name: url
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: url
    text: http://example.com
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
  "$id": "https://n8n.io/schemas/nodes/sseTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SSE Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "url": {
          "description": "The URL to receive the SSE from",
          "type": "string",
          "default": "",
          "format": "url",
          "examples": [
            "http://example.com"
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
