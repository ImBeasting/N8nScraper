---
title: "Node: Formstack Trigger"
slug: "node-formstacktrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow on a Formstack form submission."
node_type: "trigger"
group: "['trigger']"
---

# Node: Formstack Trigger

**Purpose.** Starts the workflow on a Formstack form submission.
**Subtitle.** =Form ID: {{$parameter["formId"]}}


---

## Node Details

- **Icon:** `file:formstack.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **formstackApi**: N/A
- **formstackOAuth2Api**: N/A


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
| `formstackApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `formstackOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | accessToken | ✗ |  |  |

**Authentication options:**

* **Access Token** (`accessToken`)
* **OAuth2** (`oAuth2`)

| Form Name or ID | `formId` | options |  | ✓ | The Formstack form to monitor for new submissions. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

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
node: formstackTrigger
displayName: Formstack Trigger
description: Starts the workflow on a Formstack form submission.
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: formstackApi
  required: true
- name: formstackOAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: accessToken
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: accessToken
      name: Access Token
      description: ''
    - value: oAuth2
      name: OAuth2
      description: ''
- id: formId
  name: Form Name or ID
  type: options
  default: ''
  required: true
  description: The Formstack form to monitor for new submissions. Choose from the
    list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation:
    required: true
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
  typeInfo:
    type: boolean
    displayName: Simplify
    name: simple
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
  "$id": "https://n8n.io/schemas/nodes/formstackTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Formstack Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "accessToken",
            "oAuth2"
          ],
          "default": "accessToken"
        },
        "formId": {
          "description": "The Formstack form to monitor for new submissions. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
      "name": "formstackApi",
      "required": true
    },
    {
      "name": "formstackOAuth2Api",
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
