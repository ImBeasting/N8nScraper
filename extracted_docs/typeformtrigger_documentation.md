---
title: "Node: Typeform Trigger"
slug: "node-typeformtrigger"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Starts the workflow on a Typeform form submission"
node_type: "trigger"
group: "['trigger']"
---

# Node: Typeform Trigger

**Purpose.** Starts the workflow on a Typeform form submission
**Subtitle.** =Form ID: {{$parameter["formId"]}}


---

## Node Details

- **Icon:** `{'light': 'file:typeform.svg', 'dark': 'file:typeform.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **typeformApi**: N/A
- **typeformOAuth2Api**: N/A


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
| `typeformApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `typeformOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | accessToken | ✗ |  |  |

**Authentication options:**

* **Access Token** (`accessToken`)
* **OAuth2** (`oAuth2`)

| Form Name or ID | `formId` | options |  | ✓ | Form which should trigger workflow on submission. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Simplify Answers | `simplifyAnswers` | boolean | True | ✗ | Whether to convert the answers to a key:value pair ("FIELD_TITLE":"USER_ANSER") to be easily processable |  |
| Only Answers | `onlyAnswers` | boolean | True | ✗ | Whether to return only the answers of the form and not any of the other data |  |

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
* Aliases: Form

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: typeformTrigger
displayName: Typeform Trigger
description: Starts the workflow on a Typeform form submission
version:
- '1'
- '1.1'
nodeType: trigger
group:
- trigger
credentials:
- name: typeformApi
  required: true
- name: typeformOAuth2Api
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
  description: Form which should trigger workflow on submission. Choose from the list,
    or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Form Name or ID
    name: formId
    typeOptions:
      loadOptionsMethod: getForms
    possibleValues: []
- id: simplifyAnswers
  name: Simplify Answers
  type: boolean
  default: true
  required: false
  description: Whether to convert the answers to a key:value pair ("FIELD_TITLE":"USER_ANSER")
    to be easily processable
  typeInfo:
    type: boolean
    displayName: Simplify Answers
    name: simplifyAnswers
- id: onlyAnswers
  name: Only Answers
  type: boolean
  default: true
  required: false
  description: Whether to return only the answers of the form and not any of the other
    data
  typeInfo:
    type: boolean
    displayName: Only Answers
    name: onlyAnswers
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
  "$id": "https://n8n.io/schemas/nodes/typeformTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Typeform Trigger Node",
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
          "description": "Form which should trigger workflow on submission. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "simplifyAnswers": {
          "description": "Whether to convert the answers to a key:value pair (\"FIELD_TITLE\":\"USER_ANSER\") to be easily processable",
          "type": "boolean",
          "default": true
        },
        "onlyAnswers": {
          "description": "Whether to return only the answers of the form and not any of the other data",
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
    "version": [
      "1",
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "typeformApi",
      "required": true
    },
    {
      "name": "typeformOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
