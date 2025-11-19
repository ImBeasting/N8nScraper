---
title: "Node: Gmail Trigger"
slug: "node-gmailtrigger"
version: "['1', '1.1', '1.2', '1.3']"
updated: "2025-11-13"
summary: "Fetches emails from Gmail and starts the workflow on specified polling intervals."
node_type: "trigger"
group: "['trigger']"
---

# Node: Gmail Trigger

**Purpose.** Fetches emails from Gmail and starts the workflow on specified polling intervals.
**Subtitle.** ={{"Gmail Trigger"}}


---

## Node Details

- **Icon:** `file:gmail.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **googleApi**: N/A
- **gmailOAuth2**: N/A


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
| `googleApi` | ✓ | {'show': {'authentication': ['serviceAccount']}} |
| `gmailOAuth2` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | oAuth2 | ✗ |  |  |

**Authentication options:**

* **OAuth2 (recommended)** (`oAuth2`)
* **Service Account** (`serviceAccount`)

| Event | `event` | options | messageReceived | ✗ |  |  |

**Event options:**

* **Message Received** (`messageReceived`)

| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Filters | `filters` | collection | {} | ✗ | Whether to include messages from SPAM and TRASH in the results | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Spam and Trash | `includeSpamTrash` | boolean | False | Whether to include messages from SPAM and TRASH in the results |
| Include Drafts | `includeDrafts` | boolean | False | Whether to include email drafts in the results |
| Label Names or IDs | `labelIds` | multiOptions | [] | Only return messages with labels that match all of the specified label IDs. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Search | `q` | string |  | Only return messages matching the specified query |
| Read Status | `readStatus` | options | unread |  |
| Sender | `sender` | string |  | Sender name or email to filter by |

</details>

| Options | `options` | collection | {} | ✗ | Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is 'attachment_' the first attachment is saved to 'attachment_0'. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is 'attachment_' the first attachment is saved to 'attachment_0'. |
| Download Attachments | `downloadAttachments` | boolean | False | Whether the email's attachments will be downloaded |

</details>


---

## Load Options Methods

- `getLabels`
- `for`
- `name`
- `value`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{"Gmail Trigger"}}`

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
node: gmailTrigger
displayName: Gmail Trigger
description: Fetches emails from Gmail and starts the workflow on specified polling
  intervals.
version:
- '1'
- '1.1'
- '1.2'
- '1.3'
nodeType: trigger
group:
- trigger
credentials:
- name: googleApi
  required: true
- name: gmailOAuth2
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: oAuth2
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: oAuth2
      name: OAuth2 (recommended)
      description: ''
    - value: serviceAccount
      name: Service Account
      description: ''
- id: event
  name: Event
  type: options
  default: messageReceived
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: messageReceived
      name: Message Received
      description: ''
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
- id: filters
  name: Filters
  type: collection
  default: {}
  required: false
  description: Whether to include messages from SPAM and TRASH in the results
  hint: Use the same format as in the Gmail search box. <a href="https://support.google.com/mail/answer/7190?hl=en">More
    info</a>.
  placeholder: Add Filter
  typeInfo:
    type: collection
    displayName: Filters
    name: filters
    typeOptions:
      loadOptionsMethod: getLabels
    subProperties:
    - displayName: Include Spam and Trash
      name: includeSpamTrash
      type: boolean
      description: Whether to include messages from SPAM and TRASH in the results
      default: false
    - displayName: Include Drafts
      name: includeDrafts
      type: boolean
      description: Whether to include email drafts in the results
      default: false
    - displayName: Label Names or IDs
      name: labelIds
      type: multiOptions
      description: Only return messages with labels that match all of the specified
        label IDs. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
      default: []
      typeOptions:
        loadOptionsMethod: getLabels
    - displayName: Search
      name: q
      type: string
      description: Only return messages matching the specified query
      placeholder: has:attachment
      hint: Use the same format as in the Gmail search box. <a href="https://support.google.com/mail/answer/7190?hl=en">More
        info</a>.
      default: ''
    - displayName: Read Status
      name: readStatus
      type: options
      hint: Filter emails by whether they have been read or not
      value: both
      default: unread
      options:
      - name: Unread and read emails
        value: both
        displayName: Unread And Read Emails
      - name: Unread emails only
        value: unread
        displayName: Unread Emails Only
      - name: Read emails only
        value: read
        displayName: Read Emails Only
    - displayName: Sender
      name: sender
      type: string
      description: Sender name or email to filter by
      hint: Enter an email or part of a sender name
      default: ''
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Prefix for name of the binary property to which to write the attachment.
    An index starting with 0 will be added. So if name is 'attachment_' the first
    attachment is saved to 'attachment_0'.
  placeholder: Add option
  validation:
    displayOptions:
      hide:
        simple:
        - true
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Attachment Prefix
      name: dataPropertyAttachmentsPrefixName
      type: string
      description: Prefix for name of the binary property to which to write the attachment.
        An index starting with 0 will be added. So if name is 'attachment_' the first
        attachment is saved to 'attachment_0'.
      default: attachment_
    - displayName: Download Attachments
      name: downloadAttachments
      type: boolean
      description: Whether the email's attachments will be downloaded
      default: false
common_expressions:
- ={{"Gmail Trigger"}}
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
  - field: filters
    text: Add Filter
  - field: options
    text: Add option
  hints:
  - field: filters
    text: Use the same format as in the Gmail search box. <a href="https://support.google.com/mail/answer/7190?hl=en">More
      info</a>.
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
  "$id": "https://n8n.io/schemas/nodes/gmailTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Gmail Trigger Node",
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
            "oAuth2",
            "serviceAccount"
          ],
          "default": "oAuth2"
        },
        "event": {
          "description": "",
          "type": "string",
          "enum": [
            "messageReceived"
          ],
          "default": "messageReceived"
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "filters": {
          "description": "Whether to include messages from SPAM and TRASH in the results",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "options": {
          "description": "Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is 'attachment_' the first attachment is saved to 'attachment_0'.",
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
      "1",
      "1.1",
      "1.2",
      "1.3"
    ]
  },
  "credentials": [
    {
      "name": "googleApi",
      "required": true
    },
    {
      "name": "gmailOAuth2",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1', '1.2', '1.3'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
