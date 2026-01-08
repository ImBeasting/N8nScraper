---
title: "Node: n8n Form Trigger"
slug: "node-formtrigger"
version: "1"
updated: "2026-01-08"
summary: "Generate webforms in n8n and pass their responses to the workflow"
node_type: "trigger"
group: "['trigger']"
---

# Node: n8n Form Trigger

**Purpose.** Generate webforms in n8n and pass their responses to the workflow


---

## Node Details

- **Icon:** `file:form.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`


---

## Trigger Properties

- **Event Trigger Description:** Waiting for you to submit the form
- **Activation Message:** You can now make calls to your production Form URL.
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
| Options | `options` | collection | {} | ✗ | The text displayed to users after they filled the form | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Form Submitted Text | `formSubmittedText` | string | Your response has been recorded | The text displayed to users after they filled the form |

</details>

| Form Path | `path` | string |  | ✓ | The final segment of the form's URL, both for test and production | e.g. webhook |  |
| Form Title | `formTitle` | string |  | ✓ | Shown at the top of the form | e.g. e.g. Contact us |  |
| Form Description | `formDescription` | string |  | ✗ | Shown underneath the Form Title. Can be used to prompt the user on how to complete the form. Accepts HTML. | e.g. e.g. We'll get back to you soon |  |
| Form Elements | `formFields` | fixedCollection | {} | ✗ | e.g. Add Form Element |  |
| Respond When | `responseMode` | options | onReceived | ✗ | As soon as this node receives the form submission |  |

**Respond When options:**

* **Form Is Submitted** (`onReceived`) - As soon as this node receives the form submission
* **Workflow Finishes** (`lastNode`) - When the last node of the workflow is executed
* **Using 'Respond to Webhook' Node** (`responseNode`) - When the 'Respond to Webhook' node is executed


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["path"]}}`
- `={{$parameter["responseMode"]}}`
- `={{$parameter["responseMode"] === "lastNode" ? "noData" : undefined}}`

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: formTrigger
displayName: n8n Form Trigger
description: Generate webforms in n8n and pass their responses to the workflow
version: '1'
nodeType: trigger
group:
- trigger
params:
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: The text displayed to users after they filled the form
  placeholder: Add option
  validation:
    displayOptions:
      hide:
        responseMode:
        - responseNode
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Form Submitted Text
      name: formSubmittedText
      type: string
      description: The text displayed to users after they filled the form
      default: Your response has been recorded
- id: path
  name: Form Path
  type: string
  default: ''
  required: true
  description: The final segment of the form's URL, both for test and production
  placeholder: webhook
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Form Path
    name: path
- id: formTitle
  name: Form Title
  type: string
  default: ''
  required: true
  description: Shown at the top of the form
  placeholder: e.g. Contact us
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Form Title
    name: formTitle
- id: formDescription
  name: Form Description
  type: string
  default: ''
  required: false
  description: Shown underneath the Form Title. Can be used to prompt the user on
    how to complete the form. Accepts HTML.
  placeholder: e.g. We'll get back to you soon
  typeInfo:
    type: string
    displayName: Form Description
    name: formDescription
    typeOptions:
      rows: 2
- id: formFields
  name: Form Elements
  type: fixedCollection
  default: {}
  required: false
  description: ''
  placeholder: Add Form Element
  typeInfo:
    type: fixedCollection
    displayName: Form Elements
    name: formFields
    typeOptions:
      multipleValues: true
    subProperties: []
- id: responseMode
  name: Respond When
  type: options
  default: onReceived
  required: false
  description: As soon as this node receives the form submission
  typeInfo:
    type: options
    displayName: Respond When
    name: responseMode
    possibleValues:
    - value: onReceived
      name: Form Is Submitted
      description: As soon as this node receives the form submission
    - value: lastNode
      name: Workflow Finishes
      description: When the last node of the workflow is executed
    - value: responseNode
      name: Using 'Respond to Webhook' Node
      description: When the 'Respond to Webhook' node is executed
common_expressions:
- ={{$parameter["path"]}}
- ={{$parameter["responseMode"]}}
- '={{$parameter["responseMode"] === "lastNode" ? "noData" : undefined}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  - field: path
    text: webhook
  - field: formTitle
    text: e.g. Contact us
  - field: formDescription
    text: e.g. We'll get back to you soon
  - field: formFields
    text: Add Form Element
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
  "$id": "https://n8n.io/schemas/nodes/formTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "n8n Form Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "options": {
          "description": "The text displayed to users after they filled the form",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "path": {
          "description": "The final segment of the form's URL, both for test and production",
          "type": "string",
          "default": "",
          "examples": [
            "webhook"
          ]
        },
        "formTitle": {
          "description": "Shown at the top of the form",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Contact us"
          ]
        },
        "formDescription": {
          "description": "Shown underneath the Form Title. Can be used to prompt the user on how to complete the form. Accepts HTML.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. We'll get back to you soon"
          ]
        },
        "formFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Form Element"
          ]
        },
        "responseMode": {
          "description": "As soon as this node receives the form submission",
          "type": "string",
          "enum": [
            "onReceived",
            "lastNode",
            "responseNode"
          ],
          "default": "onReceived"
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
