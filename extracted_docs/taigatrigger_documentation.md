---
title: "Node: Taiga Trigger"
slug: "node-taigatrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle Taiga events via webhook"
node_type: "trigger"
group: "['trigger']"
---

# Node: Taiga Trigger

**Purpose.** Handle Taiga events via webhook
**Subtitle.** ={{"project:" + $parameter["projectSlug"]}}


---

## Node Details

- **Icon:** `file:taiga.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **taigaApi**: N/A


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
| `taigaApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `projectId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Resources | `resources` | multiOptions |  | ✓ | Resources to listen to |  |

**Resources options:**

* **All** (`all`)
* **Issue** (`issue`)
* **Milestone (Sprint)** (`milestone`)
* **Task** (`task`)
* **User Story** (`userstory`)
* **Wikipage** (`wikipage`)

| Operations | `operations` | multiOptions |  | ✓ | Operations to listen to |  |

**Operations options:**

* **All** (`all`)
* **Create** (`create`)
* **Delete** (`delete`)
* **Update** (`change`)


---

## Load Options Methods

- `getUserProjects`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{"project:" + $parameter["projectSlug"]}}`

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
* Categories: Development, Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: taigaTrigger
displayName: Taiga Trigger
description: Handle Taiga events via webhook
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: taigaApi
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
      loadOptionsMethod: getUserProjects
    possibleValues: []
- id: resources
  name: Resources
  type: multiOptions
  default: ''
  required: true
  description: Resources to listen to
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Resources
    name: resources
    possibleValues:
    - value: all
      name: All
      description: ''
    - value: issue
      name: Issue
      description: ''
    - value: milestone
      name: Milestone (Sprint)
      description: ''
    - value: task
      name: Task
      description: ''
    - value: userstory
      name: User Story
      description: ''
    - value: wikipage
      name: Wikipage
      description: ''
- id: operations
  name: Operations
  type: multiOptions
  default: ''
  required: true
  description: Operations to listen to
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Operations
    name: operations
    possibleValues:
    - value: all
      name: All
      description: ''
    - value: create
      name: Create
      description: ''
    - value: delete
      name: Delete
      description: ''
    - value: change
      name: Update
      description: ''
common_expressions:
- ={{"project:" + $parameter["projectSlug"]}}
api_patterns:
  http_methods:
  - POST
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
  "$id": "https://n8n.io/schemas/nodes/taigaTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Taiga Trigger Node",
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
        "resources": {
          "description": "Resources to listen to",
          "type": "string"
        },
        "operations": {
          "description": "Operations to listen to",
          "type": "string"
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
      "name": "taigaApi",
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
