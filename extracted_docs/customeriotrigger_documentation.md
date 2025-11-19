---
title: "Node: Customer.io Trigger"
slug: "node-customeriotrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow on a Customer.io update (Beta)"
node_type: "trigger"
group: "['trigger']"
---

# Node: Customer.io Trigger

**Purpose.** Starts the workflow on a Customer.io update (Beta)


---

## Node Details

- **Icon:** `{'light': 'file:customerio.svg', 'dark': 'file:customerio.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **customerIoApi**: N/A


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
| `customerIoApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `events` | multiOptions | [] | ✓ | The events that can trigger the webhook and whether they are enabled |  |

**Events options:**

* **Customer Subscribed** (`customer.subscribed`) - Whether the webhook is triggered when a list subscriber is added
* **Customer Unsubscribe** (`customer.unsubscribed`) - Whether the webhook is triggered when a list member unsubscribes
* **Email Attempted** (`email.attempted`) - Whether the webhook is triggered when a list member unsubscribes
* **Email Bounced** (`email.bounced`) - Whether the webhook is triggered when a list member unsubscribes
* **Email Clicked** (`email.clicked`) - Whether the webhook is triggered when a list member unsubscribes
* **Email Converted** (`email.converted`) - Whether the webhook is triggered when a list member unsubscribes
* **Email Delivered** (`email.delivered`) - Whether the webhook is triggered when a list member unsubscribes
* **Email Drafted** (`email.drafted`) - Whether the webhook is triggered when a list member unsubscribes
* **Email Failed** (`email.failed`) - Whether the webhook is triggered when a list member unsubscribes
* **Email Opened** (`email.opened`) - Whether the webhook is triggered when a list member unsubscribes
* **Email Sent** (`email.sent`) - Whether the webhook is triggered when a list member unsubscribes
* **Email Spammed** (`email.spammed`) - Whether the webhook is triggered when a list member unsubscribes
* **Push Attempted** (`push.attempted`) - Whether the webhook is triggered when a list member unsubscribes
* **Push Bounced** (`push.bounced`) - Whether the webhook is triggered when a list member unsubscribes
* **Push Clicked** (`push.clicked`) - Whether the webhook is triggered when a list member unsubscribes
* **Push Delivered** (`push.delivered`) - Whether the webhook is triggered when a list member unsubscribes
* **Push Drafted** (`push.drafted`) - Whether the webhook is triggered when a list member unsubscribes
* **Push Failed** (`push.failed`) - Whether the webhook is triggered when a list member unsubscribes
* **Push Opened** (`push.opened`) - Whether the webhook is triggered when a list member unsubscribes
* **Push Sent** (`push.sent`) - Whether the webhook is triggered when a list member unsubscribes
* **Slack Attempted** (`slack.attempted`) - Whether the webhook is triggered when a list member unsubscribes
* **Slack Clicked** (`slack.clicked`) - Whether the webhook is triggered when a list member unsubscribes
* **Slack Drafted** (`slack.drafted`) - Whether the webhook is triggered when a list member unsubscribes
* **Slack Failed** (`slack.failed`) - Whether the webhook is triggered when a list member unsubscribes
* **Slack Sent** (`slack.sent`) - Whether the webhook is triggered when a list member unsubscribes
* **SMS Attempted** (`sms.attempted`) - Whether the webhook is triggered when a list member unsubscribes
* **SMS Bounced** (`sms.bounced`) - Whether the webhook is triggered when a list member unsubscribes
* **SMS Clicked** (`sms.clicked`) - Whether the webhook is triggered when a list member unsubscribes
* **SMS Delivered** (`sms.delivered`) - Whether the webhook is triggered when a list member unsubscribes
* **SMS Drafted** (`sms.drafted`) - Whether the webhook is triggered when a list member unsubscribes
* **SMS Failed** (`sms.failed`) - Whether the webhook is triggered when a list member unsubscribes
* **SMS Sent** (`sms.sent`) - Whether the webhook is triggered when a list member unsubscribes


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
* Categories: Communication, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: customerIoTrigger
displayName: Customer.io Trigger
description: Starts the workflow on a Customer.io update (Beta)
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: customerIoApi
  required: true
params:
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: The events that can trigger the webhook and whether they are enabled
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: customer.subscribed
      name: Customer Subscribed
      description: Whether the webhook is triggered when a list subscriber is added
    - value: customer.unsubscribed
      name: Customer Unsubscribe
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: email.attempted
      name: Email Attempted
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: email.bounced
      name: Email Bounced
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: email.clicked
      name: Email Clicked
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: email.converted
      name: Email Converted
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: email.delivered
      name: Email Delivered
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: email.drafted
      name: Email Drafted
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: email.failed
      name: Email Failed
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: email.opened
      name: Email Opened
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: email.sent
      name: Email Sent
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: email.spammed
      name: Email Spammed
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: push.attempted
      name: Push Attempted
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: push.bounced
      name: Push Bounced
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: push.clicked
      name: Push Clicked
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: push.delivered
      name: Push Delivered
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: push.drafted
      name: Push Drafted
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: push.failed
      name: Push Failed
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: push.opened
      name: Push Opened
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: push.sent
      name: Push Sent
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: slack.attempted
      name: Slack Attempted
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: slack.clicked
      name: Slack Clicked
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: slack.drafted
      name: Slack Drafted
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: slack.failed
      name: Slack Failed
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: slack.sent
      name: Slack Sent
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: sms.attempted
      name: SMS Attempted
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: sms.bounced
      name: SMS Bounced
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: sms.clicked
      name: SMS Clicked
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: sms.delivered
      name: SMS Delivered
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: sms.drafted
      name: SMS Drafted
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: sms.failed
      name: SMS Failed
      description: Whether the webhook is triggered when a list member unsubscribes
    - value: sms.sent
      name: SMS Sent
      description: Whether the webhook is triggered when a list member unsubscribes
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
  "$id": "https://n8n.io/schemas/nodes/customerIoTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Customer.io Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "The events that can trigger the webhook and whether they are enabled",
          "type": "string",
          "default": []
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
      "name": "customerIoApi",
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
