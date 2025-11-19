---
title: "Node: MailerLite Trigger"
slug: "node-mailerlitetrigger"
version: "['2']"
updated: "2025-11-13"
summary: "Starts the workflow when MailerLite events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: MailerLite Trigger

**Purpose.** Starts the workflow when MailerLite events occur


---

## Node Details

- **Icon:** `file:MailerLite.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **mailerLiteApi**: N/A


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
| `mailerLiteApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `events` | multiOptions | [] | ✓ | Fired when campaign is sent |  |

**Events options:**

* **Campaign Sent** (`campaign.sent`) - Fired when campaign is sent
* **Subscriber Added to Group** (`subscriber.added_to_group`) - Fired when a subscriber is added to a group
* **Subscriber Automation Completed** (`subscriber.automation_completed`) - Fired when subscriber finishes automation
* **Subscriber Automation Triggered** (`subscriber.automation_triggered`) - Fired when subscriber starts automation
* **Subscriber Bounced** (`subscriber.bounced`) - Fired when an email address bounces
* **Subscriber Created** (`subscriber.created`) - Fired when a new subscriber is added to an account
* **Subscriber Removed From Group** (`subscriber.removed_from_group`) - Fired when a subscriber is removed from a group
* **Subscriber Spam Reported** (`subscriber.spam_reported`) - Fired when subscriber marks a campaign as a spam
* **Subscriber Unsubscribe** (`subscriber.unsubscribed`) - Fired when a subscriber becomes unsubscribed
* **Subscriber Updated** (`subscriber.updated`) - Fired when any of the subscriber's custom fields are updated


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
node: mailerLiteTrigger
displayName: MailerLite Trigger
description: Starts the workflow when MailerLite events occur
version:
- '2'
nodeType: trigger
group:
- trigger
credentials:
- name: mailerLiteApi
  required: true
params:
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: Fired when campaign is sent
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: campaign.sent
      name: Campaign Sent
      description: Fired when campaign is sent
    - value: subscriber.added_to_group
      name: Subscriber Added to Group
      description: Fired when a subscriber is added to a group
    - value: subscriber.automation_completed
      name: Subscriber Automation Completed
      description: Fired when subscriber finishes automation
    - value: subscriber.automation_triggered
      name: Subscriber Automation Triggered
      description: Fired when subscriber starts automation
    - value: subscriber.bounced
      name: Subscriber Bounced
      description: Fired when an email address bounces
    - value: subscriber.created
      name: Subscriber Created
      description: Fired when a new subscriber is added to an account
    - value: subscriber.removed_from_group
      name: Subscriber Removed From Group
      description: Fired when a subscriber is removed from a group
    - value: subscriber.spam_reported
      name: Subscriber Spam Reported
      description: Fired when subscriber marks a campaign as a spam
    - value: subscriber.unsubscribed
      name: Subscriber Unsubscribe
      description: Fired when a subscriber becomes unsubscribed
    - value: subscriber.updated
      name: Subscriber Updated
      description: Fired when any of the subscriber's custom fields are updated
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
  "$id": "https://n8n.io/schemas/nodes/mailerLiteTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MailerLite Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "Fired when campaign is sent",
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
    "version": [
      "2"
    ]
  },
  "credentials": [
    {
      "name": "mailerLiteApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
