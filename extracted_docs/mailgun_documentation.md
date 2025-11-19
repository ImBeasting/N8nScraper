---
title: "Node: Mailgun"
slug: "node-mailgun"
version: "1"
updated: "2025-11-13"
summary: "Sends an email via Mailgun"
node_type: "regular"
group: "['output']"
---

# Node: Mailgun

**Purpose.** Sends an email via Mailgun


---

## Node Details

- **Icon:** `file:mailgun.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **mailgunApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `mailgunApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From Email | `fromEmail` | string |  | ✓ | Email address of the sender optional with name | e.g. Admin <admin@example.com> | email |
| To Email | `toEmail` | string |  | ✓ | Email address of the recipient. Multiple ones can be separated by comma. | e.g. info@example.com | email |
| Cc Email | `ccEmail` | string |  | ✗ | Cc Email address of the recipient. Multiple ones can be separated by comma. | email |
| Bcc Email | `bccEmail` | string |  | ✗ | Bcc Email address of the recipient. Multiple ones can be separated by comma. | email |
| Subject | `subject` | string |  | ✗ | Subject line of the email | e.g. My subject line |  |
| Text | `text` | string |  | ✗ | Plain text message of email |  |
| HTML | `html` | string |  | ✗ | HTML text message of email |  |
| Attachments | `attachments` | string |  | ✗ | Name of the binary properties which contain data which should be added to email as attachment. Multiple ones can be comma-separated. |  |

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
* Categories: Communication, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: mailgun
displayName: Mailgun
description: Sends an email via Mailgun
version: '1'
nodeType: regular
group:
- output
credentials:
- name: mailgunApi
  required: true
params:
- id: fromEmail
  name: From Email
  type: string
  default: ''
  required: true
  description: Email address of the sender optional with name
  placeholder: Admin <admin@example.com>
  validation:
    required: true
    format: email
  typeInfo:
    type: string
    displayName: From Email
    name: fromEmail
- id: toEmail
  name: To Email
  type: string
  default: ''
  required: true
  description: Email address of the recipient. Multiple ones can be separated by comma.
  placeholder: info@example.com
  validation:
    required: true
    format: email
  typeInfo:
    type: string
    displayName: To Email
    name: toEmail
- id: ccEmail
  name: Cc Email
  type: string
  default: ''
  required: false
  description: Cc Email address of the recipient. Multiple ones can be separated by
    comma.
  validation:
    format: email
  typeInfo:
    type: string
    displayName: Cc Email
    name: ccEmail
- id: bccEmail
  name: Bcc Email
  type: string
  default: ''
  required: false
  description: Bcc Email address of the recipient. Multiple ones can be separated
    by comma.
  validation:
    format: email
  typeInfo:
    type: string
    displayName: Bcc Email
    name: bccEmail
- id: subject
  name: Subject
  type: string
  default: ''
  required: false
  description: Subject line of the email
  placeholder: My subject line
  typeInfo:
    type: string
    displayName: Subject
    name: subject
- id: text
  name: Text
  type: string
  default: ''
  required: false
  description: Plain text message of email
  typeInfo:
    type: string
    displayName: Text
    name: text
    typeOptions:
      rows: 5
- id: html
  name: HTML
  type: string
  default: ''
  required: false
  description: HTML text message of email
  typeInfo:
    type: string
    displayName: HTML
    name: html
    typeOptions:
      rows: 5
- id: attachments
  name: Attachments
  type: string
  default: ''
  required: false
  description: Name of the binary properties which contain data which should be added
    to email as attachment. Multiple ones can be comma-separated.
  typeInfo:
    type: string
    displayName: Attachments
    name: attachments
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: fromEmail
    text: Admin <admin@example.com>
  - field: toEmail
    text: info@example.com
  - field: subject
    text: My subject line
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
  "$id": "https://n8n.io/schemas/nodes/mailgun.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Mailgun Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "fromEmail": {
          "description": "Email address of the sender optional with name",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "Admin <admin@example.com>"
          ]
        },
        "toEmail": {
          "description": "Email address of the recipient. Multiple ones can be separated by comma.",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "info@example.com"
          ]
        },
        "ccEmail": {
          "description": "Cc Email address of the recipient. Multiple ones can be separated by comma.",
          "type": "string",
          "default": "",
          "format": "email"
        },
        "bccEmail": {
          "description": "Bcc Email address of the recipient. Multiple ones can be separated by comma.",
          "type": "string",
          "default": "",
          "format": "email"
        },
        "subject": {
          "description": "Subject line of the email",
          "type": "string",
          "default": "",
          "examples": [
            "My subject line"
          ]
        },
        "text": {
          "description": "Plain text message of email",
          "type": "string",
          "default": ""
        },
        "html": {
          "description": "HTML text message of email",
          "type": "string",
          "default": ""
        },
        "attachments": {
          "description": "Name of the binary properties which contain data which should be added to email as attachment. Multiple ones can be comma-separated.",
          "type": "string",
          "default": ""
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
    "version": "1"
  },
  "credentials": [
    {
      "name": "mailgunApi",
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
