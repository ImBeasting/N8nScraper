---
title: "Node: GetResponse Trigger"
slug: "node-getresponsetrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when GetResponse events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: GetResponse Trigger

**Purpose.** Starts the workflow when GetResponse events occur


---

## Node Details

- **Icon:** `file:getResponse.png`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **getResponseApi**: N/A
- **getResponseOAuth2Api**: N/A


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
| `getResponseApi` | ✓ | {'show': {'authentication': ['apiKey']}} |
| `getResponseOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | apiKey | ✗ |  |  |

**Authentication options:**

* **API Key** (`apiKey`)
* **OAuth2** (`oAuth2`)

| Events | `events` | multiOptions | [] | ✓ | Receive notifications when a customer is subscribed to a list |  |

**Events options:**

* **Customer Subscribed** (`subscribe`) - Receive notifications when a customer is subscribed to a list
* **Customer Unsubscribed** (`unsubscribe`) - Receive notifications when a customer is unsubscribed from a list
* **Email Clicked** (`click`) - Receive notifications when a email is clicked
* **Email Opened** (`open`) - Receive notifications when a email is opened
* **Survey Submitted** (`survey`) - Receive notifications when a survey is submitted

| List Names or IDs | `listIds` | multiOptions | [] | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Options | `options` | collection | {} | ✗ | Whether to delete the current subscription | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Delete Current Subscription | `delete` | boolean | False | Whether to delete the current subscription |

</details>


---

## Load Options Methods

- `getLists`
- `value`

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
* Categories: Communication, Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: getResponseTrigger
displayName: GetResponse Trigger
description: Starts the workflow when GetResponse events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: getResponseApi
  required: true
- name: getResponseOAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: apiKey
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: apiKey
      name: API Key
      description: ''
    - value: oAuth2
      name: OAuth2
      description: ''
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: Receive notifications when a customer is subscribed to a list
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: subscribe
      name: Customer Subscribed
      description: Receive notifications when a customer is subscribed to a list
    - value: unsubscribe
      name: Customer Unsubscribed
      description: Receive notifications when a customer is unsubscribed from a list
    - value: click
      name: Email Clicked
      description: Receive notifications when a email is clicked
    - value: open
      name: Email Opened
      description: Receive notifications when a email is opened
    - value: survey
      name: Survey Submitted
      description: Receive notifications when a survey is submitted
- id: listIds
  name: List Names or IDs
  type: multiOptions
  default: []
  required: false
  description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  typeInfo:
    type: multiOptions
    displayName: List Names or IDs
    name: listIds
    typeOptions:
      loadOptionsMethod: getLists
    possibleValues: []
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to delete the current subscription
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Delete Current Subscription
      name: delete
      type: boolean
      description: Whether to delete the current subscription
      default: false
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/getResponseTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GetResponse Trigger Node",
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
            "apiKey",
            "oAuth2"
          ],
          "default": "apiKey"
        },
        "events": {
          "description": "Receive notifications when a customer is subscribed to a list",
          "type": "string",
          "default": []
        },
        "listIds": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "options": {
          "description": "Whether to delete the current subscription",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
  },
  "credentials": [
    {
      "name": "getResponseApi",
      "required": true
    },
    {
      "name": "getResponseOAuth2Api",
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
