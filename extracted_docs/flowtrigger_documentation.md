---
title: "Node: Flow Trigger"
slug: "node-flowtrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle Flow events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Flow Trigger

**Purpose.** Handle Flow events via webhooks


---

## Node Details

- **Icon:** `file:flow.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **flowApi**: N/A


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
| `flowApi` | ✓ | - |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options |  | ✗ | Resource that triggers the webhook |  |

**Resource options:**

* **Project** (`list`)
* **Task** (`task`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options |  | ✗ | Resource that triggers the webhook |  |

**Resource options:**

* **Project** (`list`)
* **Task** (`task`)

| Project ID | `listIds` | string |  | ✓ | Lists IDs, perhaps known better as "Projects" separated by a comma (,) |  |
| Task ID | `taskIds` | string |  | ✓ | Task IDs separated by a comma (,) |  |

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
node: flowTrigger
displayName: Flow Trigger
description: Handle Flow events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: flowApi
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: ''
  required: false
  description: Resource that triggers the webhook
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: list
      name: Project
      description: ''
    - value: task
      name: Task
      description: ''
- id: listIds
  name: Project ID
  type: string
  default: ''
  required: true
  description: Lists IDs, perhaps known better as "Projects" separated by a comma
    (,)
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - list
      hide:
        resource:
        - task
  typeInfo:
    type: string
    displayName: Project ID
    name: listIds
- id: taskIds
  name: Task ID
  type: string
  default: ''
  required: true
  description: Task IDs separated by a comma (,)
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - task
      hide:
        resource:
        - list
  typeInfo:
    type: string
    displayName: Task ID
    name: taskIds
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
  "$id": "https://n8n.io/schemas/nodes/flowTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Flow Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Resource that triggers the webhook",
          "type": "string",
          "enum": [
            "list",
            "task"
          ],
          "default": ""
        },
        "listIds": {
          "description": "Lists IDs, perhaps known better as \"Projects\" separated by a comma (,)",
          "type": "string",
          "default": ""
        },
        "taskIds": {
          "description": "Task IDs separated by a comma (,)",
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
      "name": "flowApi",
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
