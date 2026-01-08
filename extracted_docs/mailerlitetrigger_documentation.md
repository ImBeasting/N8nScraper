---
title: "Node: MailerLite"
slug: "node-mailerlitetrigger"
version: "['2']"
updated: "2026-01-08"
summary: "Consume MailerLite API"
node_type: "regular"
group: "['input']"
---

# Node: MailerLite

**Purpose.** Consume MailerLite API
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:MailerLite.svg`
- **Group:** `['input']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **mailerLiteApi**: N/A


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

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |
| Always Output Data | `alwaysOutputData` | boolean | False | If active, will output a single, empty item when the output would have been empty. Use to prevent the workflow finishing on this node |
| Execute Once | `executeOnce` | boolean | False | If active, the node executes only once, with data from the first item it receives |
| Retry On Fail | `retryOnFail` | boolean | False | If active, the node tries to execute again when it fails |
| Max. Tries | `maxTries` | number | 3 | Number of times to attempt to execute the node before failing the execution *(Only visible when 'Retry On Fail' is enabled)* (min: 2, max: 5) |
| Wait Between Tries (ms) | `waitBetweenTries` | number | 1000 | How long to wait between each attempt (in milliseconds) *(Only visible when 'Retry On Fail' is enabled)* (min: 0, max: 5000) |
| On Error | `onError` | options | stopWorkflow | Action to take when the node execution fails |

**On Error Options:**

* **Stop Workflow** (`stopWorkflow`) — Halt execution and fail workflow
* **Continue** (`continueRegularOutput`) — Pass error message as item in regular output
* **Continue (using error output)** (`continueErrorOutput`) — Pass item to an extra `error` output

---

## Notes & Caveats

* This node is part of n8n-nodes-base

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: mailerLiteTrigger
displayName: MailerLite
description: Consume MailerLite API
version:
- '2'
nodeType: regular
group:
- input
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
  executable:
    alwaysOutputData:
      name: Always Output Data
      field_id: alwaysOutputData
      type: boolean
      default: false
      description: If active, will output a single, empty item when the output would
        have been empty. Use to prevent the workflow finishing on this node
    executeOnce:
      name: Execute Once
      field_id: executeOnce
      type: boolean
      default: false
      description: If active, the node executes only once, with data from the first
        item it receives
    retryOnFail:
      name: Retry On Fail
      field_id: retryOnFail
      type: boolean
      default: false
      description: If active, the node tries to execute again when it fails
    maxTries:
      name: Max. Tries
      field_id: maxTries
      type: number
      default: 3
      min: 2
      max: 5
      description: Number of times to attempt to execute the node before failing the
        execution
      displayOptions:
        show:
          retryOnFail:
          - true
    waitBetweenTries:
      name: Wait Between Tries (ms)
      field_id: waitBetweenTries
      type: number
      default: 1000
      min: 0
      max: 5000
      description: How long to wait between each attempt (in milliseconds)
      displayOptions:
        show:
          retryOnFail:
          - true
    onError:
      name: On Error
      field_id: onError
      type: options
      default: stopWorkflow
      description: Action to take when the node execution fails
      options:
      - name: Stop Workflow
        value: stopWorkflow
        description: Halt execution and fail workflow
      - name: Continue
        value: continueRegularOutput
        description: Pass error message as item in regular output
      - name: Continue (using error output)
        value: continueErrorOutput
        description: Pass item to an extra `error` output
  note: Executable nodes have both common and executable settings

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/mailerLiteTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MailerLite Node",
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
        },
        "alwaysOutputData": {
          "type": "boolean",
          "default": false,
          "description": "If active, will output a single, empty item when the output would have been empty. Use to prevent the workflow finishing on this node"
        },
        "executeOnce": {
          "type": "boolean",
          "default": false,
          "description": "If active, the node executes only once, with data from the first item it receives"
        },
        "retryOnFail": {
          "type": "boolean",
          "default": false,
          "description": "If active, the node tries to execute again when it fails"
        },
        "maxTries": {
          "type": "number",
          "default": 3,
          "description": "Number of times to attempt to execute the node before failing the execution",
          "minimum": 2,
          "maximum": 5
        },
        "waitBetweenTries": {
          "type": "number",
          "default": 1000,
          "description": "How long to wait between each attempt (in milliseconds)",
          "minimum": 0,
          "maximum": 5000
        },
        "onError": {
          "type": "options",
          "default": "stopWorkflow",
          "description": "Action to take when the node execution fails",
          "enum": [
            "stopWorkflow",
            "continueRegularOutput",
            "continueErrorOutput"
          ]
        }
      }
    }
  },
  "metadata": {
    "nodeType": "regular",
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
| ['2'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
