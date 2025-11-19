---
title: "Node: WhatsApp Trigger"
slug: "node-whatsapptrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle WhatsApp events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: WhatsApp Trigger

**Purpose.** Handle WhatsApp events via webhooks
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:whatsapp.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **whatsAppTriggerApi**: N/A


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

- **whatsAppNotice**: Due to Facebook API limitations, you can use just one WhatsApp trigger for each Facebook App

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `whatsAppTriggerApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

**Common Endpoints:**
- `https://graph.facebook.com/v19.0/oauth/access_token`
- `https://graph.facebook.com/v19.0{resource}`
- `{phoneNumberId}/messages`

**Headers Used:** content-type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger On | `updates` | multiOptions | [] | ✓ |  |  |

**Trigger On options:**

* **Account Review Update** (`account_review_update`)
* **Account Update** (`account_update`)
* **Business Capability Update** (`business_capability_update`)
* **Message Template Quality Update** (`message_template_quality_update`)
* **Message Template Status Update** (`message_template_status_update`)
* **Messages** (`messages`)
* **Phone Number Name Update** (`phone_number_name_update`)
* **Phone Number Quality Update** (`phone_number_quality_update`)
* **Security** (`security`)
* **Template Category Update** (`template_category_update`)

| Options | `options` | collection | {} | ✗ | WhatsApp sends notifications to the Trigger when the status of a message changes (for example from Sent to Delivered and from Delivered to Read). To avoid multiple executions for one WhatsApp message, you can set the Trigger to execute only on selected message status updates. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Receive Message Status Updates | `messageStatusUpdates` | multiOptions |  | WhatsApp sends notifications to the Trigger when the status of a message changes (for example from Sent to Delivered and from Delivered to Read). To avoid multiple executions for one WhatsApp message, you can set the Trigger to execute only on selected message status updates. |

</details>


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
node: whatsAppTrigger
displayName: WhatsApp Trigger
description: Handle WhatsApp events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: whatsAppTriggerApi
  required: true
params:
- id: updates
  name: Trigger On
  type: multiOptions
  default: []
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Trigger On
    name: updates
    possibleValues:
    - value: account_review_update
      name: Account Review Update
      description: ''
    - value: account_update
      name: Account Update
      description: ''
    - value: business_capability_update
      name: Business Capability Update
      description: ''
    - value: message_template_quality_update
      name: Message Template Quality Update
      description: ''
    - value: message_template_status_update
      name: Message Template Status Update
      description: ''
    - value: messages
      name: Messages
      description: ''
    - value: phone_number_name_update
      name: Phone Number Name Update
      description: ''
    - value: phone_number_quality_update
      name: Phone Number Quality Update
      description: ''
    - value: security
      name: Security
      description: ''
    - value: template_category_update
      name: Template Category Update
      description: ''
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: WhatsApp sends notifications to the Trigger when the status of a message
    changes (for example from Sent to Delivered and from Delivered to Read). To avoid
    multiple executions for one WhatsApp message, you can set the Trigger to execute
    only on selected message status updates.
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Receive Message Status Updates
      name: messageStatusUpdates
      type: multiOptions
      description: WhatsApp sends notifications to the Trigger when the status of
        a message changes (for example from Sent to Delivered and from Delivered to
        Read). To avoid multiple executions for one WhatsApp message, you can set
        the Trigger to execute only on selected message status updates.
      value: all
      options:
      - name: All
        value: all
        displayName: All
      - name: Deleted
        value: deleted
        displayName: Deleted
      - name: Delivered
        value: delivered
        displayName: Delivered
      - name: Failed
        value: failed
        displayName: Failed
      - name: Read
        value: read
        displayName: Read
      - name: Sent
        value: sent
        displayName: Sent
common_expressions:
- ={{$parameter["event"]}}
api_patterns:
  http_methods:
  - POST
  endpoints:
  - https://graph.facebook.com/v19.0/oauth/access_token
  - https://graph.facebook.com/v19.0{resource}
  - '{phoneNumberId}/messages'
  headers:
  - content-type
  query_params: []
ui_elements:
  notices:
  - name: whatsAppNotice
    text: Due to Facebook API limitations, you can use just one WhatsApp trigger for
      each Facebook App
    conditions: null
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
  "$id": "https://n8n.io/schemas/nodes/whatsAppTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "WhatsApp Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "updates": {
          "description": "",
          "type": "string",
          "default": []
        },
        "options": {
          "description": "WhatsApp sends notifications to the Trigger when the status of a message changes (for example from Sent to Delivered and from Delivered to Read). To avoid multiple executions for one WhatsApp message, you can set the Trigger to execute only on selected message status updates.",
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
      "name": "whatsAppTriggerApi",
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
