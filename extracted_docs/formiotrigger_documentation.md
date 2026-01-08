---
title: "Node: Form.io Trigger"
slug: "node-formiotrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle form.io events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Form.io Trigger

**Purpose.** Handle form.io events via webhooks
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:formio.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **formIoApi**: N/A


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
| `formIoApi` | ✓ | - |

---

## API Patterns

**Common Endpoints:**
- `{base}{endpoint}`

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `projectId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Form Name or ID | `formId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Trigger Events | `events` | multiOptions | [] | ✓ |  |  |

**Trigger Events options:**

* **Submission Created** (`create`)
* **Submission Updated** (`update`)

| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

---

## Load Options Methods

- `getProjects`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["event"]}}`

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
node: formIoTrigger
displayName: Form.io Trigger
description: Handle form.io events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: formIoApi
  required: true
params:
- id: projectId
  name: Project Name or ID
  type: options
  default: ''
  required: true
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Project Name or ID
    name: projectId
    typeOptions:
      loadOptionsMethod: getProjects
    possibleValues: []
- id: formId
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
    name: formId
    typeOptions:
      loadOptionsMethod: getForms
    possibleValues: []
- id: events
  name: Trigger Events
  type: multiOptions
  default: []
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Trigger Events
    name: events
    possibleValues:
    - value: create
      name: Submission Created
      description: ''
    - value: update
      name: Submission Updated
      description: ''
- id: simple
  name: Simplify
  type: boolean
  default: true
  required: false
  description: Whether to return a simplified version of the response instead of the
    raw data
  typeInfo:
    type: boolean
    displayName: Simplify
    name: simple
common_expressions:
- ={{$parameter["event"]}}
api_patterns:
  http_methods: []
  endpoints:
  - '{base}{endpoint}'
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
  "$id": "https://n8n.io/schemas/nodes/formIoTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Form.io Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "projectId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "formId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "events": {
          "description": "",
          "type": "string",
          "default": []
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
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
      "name": "formIoApi",
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
