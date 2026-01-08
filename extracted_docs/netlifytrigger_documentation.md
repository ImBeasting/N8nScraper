---
title: "Node: Netlify Trigger"
slug: "node-netlifytrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle netlify events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Netlify Trigger

**Purpose.** Handle netlify events via webhooks
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:netlify.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **netlifyApi**: N/A


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
| `netlifyApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Site Name or ID | `siteId` | options |  | ✓ | Select the Site ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Event | `event` | options |  | ✓ |  |  |

**Event options:**

* **Deploy Building** (`deployBuilding`)
* **Deploy Failed** (`deployFailed`)
* **Deploy Created** (`deployCreated`)
* **Form Submitted** (`submissionCreated`)

| Form Name or ID | `formId` | options |  | ✓ | Select a form. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

---

## Load Options Methods

- `getSites`
- `for`
- `name`
- `value`

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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: netlifyTrigger
displayName: Netlify Trigger
description: Handle netlify events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: netlifyApi
  required: true
params:
- id: siteId
  name: Site Name or ID
  type: options
  default: ''
  required: true
  description: Select the Site ID. Choose from the list, or specify an ID using an
    <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Site Name or ID
    name: siteId
    typeOptions:
      loadOptionsMethod: getSites
    possibleValues: []
- id: event
  name: Event
  type: options
  default: ''
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: deployBuilding
      name: Deploy Building
      description: ''
    - value: deployFailed
      name: Deploy Failed
      description: ''
    - value: deployCreated
      name: Deploy Created
      description: ''
    - value: submissionCreated
      name: Form Submitted
      description: ''
- id: formId
  name: Form Name or ID
  type: options
  default: ''
  required: true
  description: Select a form. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation:
    required: true
    displayOptions:
      show:
        event:
        - submissionCreated
  typeInfo:
    type: options
    displayName: Form Name or ID
    name: formId
    typeOptions:
      loadOptionsMethod: getForms
    possibleValues: []
- id: simple
  name: Simplify
  type: boolean
  default: true
  required: false
  description: Whether to return a simplified version of the response instead of the
    raw data
  validation:
    displayOptions:
      show:
        event:
        - submissionCreated
  typeInfo:
    type: boolean
    displayName: Simplify
    name: simple
common_expressions:
- ={{$parameter["event"]}}
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
  "$id": "https://n8n.io/schemas/nodes/netlifyTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Netlify Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "siteId": {
          "description": "Select the Site ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "event": {
          "description": "",
          "type": "string",
          "enum": [
            "deployBuilding",
            "deployFailed",
            "deployCreated",
            "submissionCreated"
          ],
          "default": ""
        },
        "formId": {
          "description": "Select a form. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
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
      "name": "netlifyApi",
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
