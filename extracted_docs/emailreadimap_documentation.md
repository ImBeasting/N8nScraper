---
title: "Node: Email Trigger (IMAP)"
slug: "node-emailreadimap"
version: "['2', '2.1']"
updated: "2025-11-13"
summary: "Triggers the workflow when a new email is received"
node_type: "trigger"
group: "['trigger']"
---

# Node: Email Trigger (IMAP)

**Purpose.** Triggers the workflow when a new email is received


---

## Node Details

- **Icon:** `fa:inbox`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **imap**: N/A


---

## Trigger Properties

- **Event Trigger Description:** Waiting for you to receive an email
- **Activation Message:** 
- **Supports CORS:** False
- **Trigger Panel:**
```json
{
  "executionsHelp": "{\n\t\t\tinactive:\n\t\t\t\t\"<b>While building your workflow</b>, click the 'execute step' button, then send an email to make an event happen. This will trigger an execution, which will show up in this editor.<br /> <br /><b>Once you're happy with your workflow</b>, <a data-key='activate'>activate</a> it. Then every time an email is received, the workflow will execute. These executions will show up in the <a data-key='executions'>executions list</a>, but not in the editor.\",\n\t\t\tactive:\n\t\t\t\t\"<b>While building your workflow</b>, click the 'execute step' button, then send an email to make an event happen. This will trigger an execution, which will show up in this editor.<br /> <br /><b>Your workflow will also execute automatically</b>, since it's activated. Every time an email is received, this node will trigger an execution. These executions will show up in the <a data-key='executions'>executions list</a>, but not in the editor.\",\n\t\t}",
  "activationHint": "Once you\u2019ve finished building your workflow, <a data-key="
}
```

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `imap` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Mailbox Name | `mailbox` | string | INBOX | ✗ |  |  |
| Action | `postProcessAction` | options | read | ✗ | What to do after the email has been received. If "nothing" gets selected it will be processed multiple times. |  |

**Action options:**

* **Mark as Read** (`read`)
* **Nothing** (`nothing`)

| Download Attachments | `downloadAttachments` | boolean | False | ✗ | Whether attachments of emails should be downloaded. Only set if needed as it increases processing. |  |
| Format | `format` | options | simple | ✗ | Returns the full email message data with body content in the raw field as a base64url encoded string; the payload field is not used |  |

**Format options:**

* **RAW** (`raw`) - Returns the full email message data with body content in the raw field as a base64url encoded string; the payload field is not used
* **Resolved** (`resolved`) - Returns the full email with all data resolved and attachments saved as binary data
* **Simple** (`simple`) - Returns the full email; do not use if you wish to gather inline attachments

| Property Prefix Name | `dataPropertyAttachmentsPrefixName` | string | attachment_ | ✗ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" |  |
| Property Prefix Name | `dataPropertyAttachmentsPrefixName` | string | attachment_ | ✗ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" |  |
| Options | `options` | collection | {} | ✗ | Custom email fetching rules. See <a href="https://github.com/mscdex/node-imap">node-imap</a>'s search function for more details. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Email Rules | `customEmailConfig` | string | [ | Custom email fetching rules. See <a href="https://github.com/mscdex/node-imap">node-imap</a>'s search function for more details. |
| Force Reconnect Every Minutes | `forceReconnect` | number | 60 | Sets an interval (in minutes) to force a reconnection |
| Fetch Only New Emails | `trackLastMessageId` | boolean | True | Whether to fetch only new emails since the last run, or all emails that match the "Custom Email Rules" (["UNSEEN"] by default) |

</details>


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
node: emailReadImap
displayName: Email Trigger (IMAP)
description: Triggers the workflow when a new email is received
version:
- '2'
- '2.1'
nodeType: trigger
group:
- trigger
credentials:
- name: imap
  required: true
params:
- id: mailbox
  name: Mailbox Name
  type: string
  default: INBOX
  required: false
  description: ''
  typeInfo:
    type: string
    displayName: Mailbox Name
    name: mailbox
- id: postProcessAction
  name: Action
  type: options
  default: read
  required: false
  description: What to do after the email has been received. If "nothing" gets selected
    it will be processed multiple times.
  typeInfo:
    type: options
    displayName: Action
    name: postProcessAction
    possibleValues:
    - value: read
      name: Mark as Read
      description: ''
    - value: nothing
      name: Nothing
      description: ''
- id: downloadAttachments
  name: Download Attachments
  type: boolean
  default: false
  required: false
  description: Whether attachments of emails should be downloaded. Only set if needed
    as it increases processing.
  validation:
    displayOptions:
      show:
        format:
        - simple
  typeInfo:
    type: boolean
    displayName: Download Attachments
    name: downloadAttachments
- id: format
  name: Format
  type: options
  default: simple
  required: false
  description: Returns the full email message data with body content in the raw field
    as a base64url encoded string; the payload field is not used
  typeInfo:
    type: options
    displayName: Format
    name: format
    possibleValues:
    - value: raw
      name: RAW
      description: Returns the full email message data with body content in the raw
        field as a base64url encoded string; the payload field is not used
    - value: resolved
      name: Resolved
      description: Returns the full email with all data resolved and attachments saved
        as binary data
    - value: simple
      name: Simple
      description: Returns the full email; do not use if you wish to gather inline
        attachments
- id: dataPropertyAttachmentsPrefixName
  name: Property Prefix Name
  type: string
  default: attachment_
  required: false
  description: Prefix for name of the binary property to which to write the attachments.
    An index starting with 0 will be added. So if name is "attachment_" the first
    attachment is saved to "attachment_0"
  validation: &id001
    displayOptions:
      show:
        format:
        - simple
        downloadAttachments:
        - true
  typeInfo: &id002
    type: string
    displayName: Property Prefix Name
    name: dataPropertyAttachmentsPrefixName
- id: dataPropertyAttachmentsPrefixName
  name: Property Prefix Name
  type: string
  default: attachment_
  required: false
  description: Prefix for name of the binary property to which to write the attachments.
    An index starting with 0 will be added. So if name is "attachment_" the first
    attachment is saved to "attachment_0"
  validation: *id001
  typeInfo: *id002
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Custom email fetching rules. See <a href="https://github.com/mscdex/node-imap">node-imap</a>'s
    search function for more details.
  placeholder: Add option
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Custom Email Rules
      name: customEmailConfig
      type: string
      description: Custom email fetching rules. See <a href="https://github.com/mscdex/node-imap">node-imap</a>'s
        search function for more details.
      default: '['
    - displayName: Force Reconnect Every Minutes
      name: forceReconnect
      type: number
      description: Sets an interval (in minutes) to force a reconnection
      default: 60
    - displayName: Fetch Only New Emails
      name: trackLastMessageId
      type: boolean
      description: Whether to fetch only new emails since the last run, or all emails
        that match the "Custom Email Rules" (["UNSEEN"] by default)
      default: true
      displayOptions:
        show: {}
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
  "$id": "https://n8n.io/schemas/nodes/emailReadImap.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Email Trigger (IMAP) Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "mailbox": {
          "description": "",
          "type": "string",
          "default": "INBOX"
        },
        "postProcessAction": {
          "description": "What to do after the email has been received. If \"nothing\" gets selected it will be processed multiple times.",
          "type": "string",
          "enum": [
            "read",
            "nothing"
          ],
          "default": "read"
        },
        "downloadAttachments": {
          "description": "Whether attachments of emails should be downloaded. Only set if needed as it increases processing.",
          "type": "boolean",
          "default": false
        },
        "format": {
          "description": "Returns the full email message data with body content in the raw field as a base64url encoded string; the payload field is not used",
          "type": "string",
          "enum": [
            "raw",
            "resolved",
            "simple"
          ],
          "default": "simple"
        },
        "dataPropertyAttachmentsPrefixName": {
          "description": "Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is \"attachment_\" the first attachment is saved to \"attachment_0\"",
          "type": "string",
          "default": "attachment_"
        },
        "options": {
          "description": "Custom email fetching rules. See <a href=\"https://github.com/mscdex/node-imap\">node-imap</a>'s search function for more details.",
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
    "version": [
      "2",
      "2.1"
    ]
  },
  "credentials": [
    {
      "name": "imap",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2', '2.1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
