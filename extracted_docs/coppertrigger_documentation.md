---
title: "Node: Copper Trigger"
slug: "node-coppertrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle Copper events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Copper Trigger

**Purpose.** Handle Copper events via webhooks


---

## Node Details

- **Icon:** `file:copper.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **copperApi**: N/A


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
| `copperApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options |  | ✓ | The resource which will fire the event |  |

**Resource options:**

* **Company** (`company`)
* **Lead** (`lead`)
* **Opportunity** (`opportunity`)
* **Person** (`person`)
* **Project** (`project`)
* **Task** (`task`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options |  | ✓ | The resource which will fire the event |  |

**Resource options:**

* **Company** (`company`)
* **Lead** (`lead`)
* **Opportunity** (`opportunity`)
* **Person** (`person`)
* **Project** (`project`)
* **Task** (`task`)

| Event | `event` | options |  | ✓ | An existing record is removed |  |

**Event options:**

* **Delete** (`delete`) - An existing record is removed
* **New** (`new`) - A new record is created
* **Update** (`update`) - Any field in the existing entity record is changed


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
node: copperTrigger
displayName: Copper Trigger
description: Handle Copper events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: copperApi
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: ''
  required: true
  description: The resource which will fire the event
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: company
      name: Company
      description: ''
    - value: lead
      name: Lead
      description: ''
    - value: opportunity
      name: Opportunity
      description: ''
    - value: person
      name: Person
      description: ''
    - value: project
      name: Project
      description: ''
    - value: task
      name: Task
      description: ''
- id: event
  name: Event
  type: options
  default: ''
  required: true
  description: An existing record is removed
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: delete
      name: Delete
      description: An existing record is removed
    - value: new
      name: New
      description: A new record is created
    - value: update
      name: Update
      description: Any field in the existing entity record is changed
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
  "$id": "https://n8n.io/schemas/nodes/copperTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Copper Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "The resource which will fire the event",
          "type": "string",
          "enum": [
            "company",
            "lead",
            "opportunity",
            "person",
            "project",
            "task"
          ],
          "default": ""
        },
        "event": {
          "description": "An existing record is removed",
          "type": "string",
          "enum": [
            "delete",
            "new",
            "update"
          ],
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
      "name": "copperApi",
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
