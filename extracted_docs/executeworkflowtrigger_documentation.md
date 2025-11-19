---
title: "Node: Execute Workflow Trigger"
slug: "node-executeworkflowtrigger"
version: "['1', '1.1']"
updated: "2025-11-13"
summary: "Helpers for calling other n8n workflows. Used for designing modular, microservice-like workflows."
node_type: "trigger"
group: "['trigger']"
---

# Node: Execute Workflow Trigger

**Purpose.** Helpers for calling other n8n workflows. Used for designing modular, microservice-like workflows.


---

## Node Details

- **Icon:** `fa:sign-out-alt`
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

**Node-Specific Tips:**

- **notice**: When an ‘execute workflow’ node calls this workflow, the execution starts here. Any data passed into the 'execute workflow' node will be output by this node.
- **outdatedVersionWarning**: This node is out of date. Please upgrade by removing it and adding a new one
- **(template: JSON_EXAMPLE)_notice**: Provide an example object to infer fields and their types.<br>To allow any type for a given field, set the value to null.

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `events` | hidden | worklfow_call | ✗ | When executed by another workflow using Execute Workflow Trigger |  |
| Input data mode | `Define using fields below` | options |  | ✗ | Provide input fields via UI |  |

**Input data mode options:**

* **Define using fields below** (``) - Provide input fields via UI
* **Define using JSON example** (``) - Generate a schema from an example JSON object
* **Accept all data** (``) - Use all incoming data from the parent workflow

| Workflow Input Schema | `name` | fixedCollection | {} | ✓ | Define expected input fields. If no inputs are provided, all data from the calling workflow will be passed through. | e.g. Add field |  |

<details>
<summary><strong>Workflow Input Schema sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Values | `name` |  |  |  |

</details>


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
node: executeWorkflowTrigger
displayName: Execute Workflow Trigger
description: Helpers for calling other n8n workflows. Used for designing modular,
  microservice-like workflows.
version:
- '1'
- '1.1'
nodeType: trigger
group:
- trigger
params:
- id: events
  name: Events
  type: hidden
  default: worklfow_call
  required: false
  description: When executed by another workflow using Execute Workflow Trigger
  typeInfo:
    type: hidden
    displayName: Events
    name: events
- id: Define using fields below
  name: Input data mode
  type: options
  default: ''
  required: false
  description: Provide input fields via UI
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: options
    displayName: Input data mode
    name: Define using fields below
    possibleValues:
    - value: Define using fields below
      name: Define using fields below
      description: Provide input fields via UI
    - value: Define using JSON example
      name: Define using JSON example
      description: Generate a schema from an example JSON object
    - value: Accept all data
      name: Accept all data
      description: Use all incoming data from the parent workflow
- id: name
  name: Workflow Input Schema
  type: fixedCollection
  default: {}
  required: true
  description: Define expected input fields. If no inputs are provided, all data from
    the calling workflow will be passed through.
  placeholder: Add field
  validation:
    required: true
    displayOptions:
      show: {}
  typeInfo:
    type: fixedCollection
    displayName: Workflow Input Schema
    name: name
    typeOptions:
      multipleValues: true
    subProperties:
    - name: name
      displayName: Values
      values:
      - displayName: Name
        name: name
        type: string
        description: A unique name for this workflow input, used to reference it from
          another workflows
        placeholder: e.g. fieldName
        default: ''
        required: true
        noDataExpression: true
      - displayName: Type
        name: type
        type: options
        description: Expected data type for this input value. Determines how this
          field's values are stored, validated, and displayed.
        default: string
        required: true
        noDataExpression: true
ui_elements:
  notices:
  - name: notice
    text: When an ‘execute workflow’ node calls this workflow, the execution starts
      here. Any data passed into the 'execute workflow' node will be output by this
      node.
    conditions:
      show: {}
  - name: outdatedVersionWarning
    text: This node is out of date. Please upgrade by removing it and adding a new
      one
    conditions:
      show: {}
  - name: '(template: JSON_EXAMPLE)_notice'
    text: Provide an example object to infer fields and their types.<br>To allow any
      type for a given field, set the value to null.
    conditions:
      show: {}
  tooltips: []
  placeholders:
  - field: name
    text: Add field
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
  "$id": "https://n8n.io/schemas/nodes/executeWorkflowTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Execute Workflow Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "When executed by another workflow using Execute Workflow Trigger",
          "type": "string",
          "default": "worklfow_call"
        },
        "Define using fields below": {
          "description": "Provide input fields via UI",
          "type": "string",
          "enum": [
            "Define using fields below",
            "Define using JSON example",
            "Accept all data"
          ]
        },
        "name": {
          "description": "Define expected input fields. If no inputs are provided, all data from the calling workflow will be passed through.",
          "type": "string",
          "default": {},
          "examples": [
            "Add field"
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
    "version": [
      "1",
      "1.1"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
