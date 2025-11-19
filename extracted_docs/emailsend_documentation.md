---
title: "Node: Send Email"
slug: "node-emailsend"
version: "['2', '2.1']"
updated: "2025-11-13"
summary: "Sends an email using SMTP protocol"
node_type: "regular"
group: "['output']"
---

# Node: Send Email

**Purpose.** Sends an email using SMTP protocol


---

## Node Details

- **Icon:** `fa:envelope`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **smtp**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `smtp` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` |  |
| Send and Wait for Response | `` |  |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | hidden | email | ✗ | Resource to operate on |  |
---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | send | ✗ | Operation to perform |  |

**Operation options:**

* **Send** (`send`) - Send an Email
* **Send and Wait for Response** (``) - Send message and wait for response

---

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Subject | `subject` | string |  | ✗ | Subject line of the email | e.g. My subject line |  |
| Email Format | `emailFormat` | options | html | ✗ | Send email as plain text | email |

**Email Format options:**

* **Text** (`text`) - Send email as plain text
* **HTML** (`html`) - Send email as HTML
* **Both** (`both`) - Send both formats, recipient's client selects version to display

| Email Format | `emailFormat` | options | text | ✗ |  | email |

**Email Format options:**

* **Text** (`text`)
* **HTML** (`html`)
* **Both** (`both`)

| Text | `text` | string |  | ✗ | Plain text message of email |  |
| HTML | `html` | string |  | ✗ | HTML text message of email |  |
| Options | `options` | collection | {} | ✗ | Whether to include the phrase “This email was sent automatically with n8n” to the end of the email | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `attachments` | string |  | Name of the binary properties that contain data to add to email as attachment. Multiple ones can be comma-separated. Reference embedded images or other content within the body of an email message, e.g. &lt;img src="cid:image_1"&gt; |
| CC Email | `ccEmail` | string |  | Email address of CC recipient |
| BCC Email | `bccEmail` | string |  | Email address of BCC recipient |
| Ignore SSL Issues (Insecure) | `allowUnauthorizedCerts` | boolean | False | Whether to connect even if SSL certificate validation is not possible |
| Reply To | `replyTo` | string |  | The email address to send the reply to |

</details>

| To Email | `toEmail` | string |  | ✓ | Email address of the recipient. You can also specify a name: Nathan Doe &lt;nate@n8n.io&gt;. | e.g. info@example.com | email |
| Append n8n Attribution | `appendAttribution` | boolean | True | ✗ |  |  |

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
node: emailSend
displayName: Send Email
description: Sends an email using SMTP protocol
version:
- '2'
- '2.1'
nodeType: regular
group:
- output
credentials:
- name: smtp
  required: true
operations:
- id: send
  name: Send
  description: ''
  params:
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
  - id: emailFormat
    name: Email Format
    type: options
    default: html
    required: false
    description: Send email as plain text
    validation: &id001
      format: email
      displayOptions:
        show: {}
    typeInfo: &id002
      type: options
      displayName: Email Format
      name: emailFormat
      possibleValues:
      - value: text
        name: Text
        description: ''
      - value: html
        name: HTML
        description: ''
      - value: both
        name: Both
        description: ''
  - id: emailFormat
    name: Email Format
    type: options
    default: text
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: text
    name: Text
    type: string
    default: ''
    required: false
    description: Plain text message of email
    validation:
      displayOptions:
        show:
          emailFormat:
          - text
          - both
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
    validation:
      displayOptions:
        show:
          emailFormat:
          - html
          - both
    typeInfo:
      type: string
      displayName: HTML
      name: html
      typeOptions:
        rows: 5
  - id: toEmail
    name: To Email
    type: string
    default: ''
    required: true
    description: 'Email address of the recipient. You can also specify a name: Nathan
      Doe &lt;nate@n8n.io&gt;.'
    placeholder: info@example.com
    validation:
      required: true
      format: email
    typeInfo:
      type: string
      displayName: To Email
      name: toEmail
  - id: appendAttribution
    name: Append n8n Attribution
    type: boolean
    default: true
    required: false
    description: ''
    typeInfo:
      type: boolean
      displayName: Append n8n Attribution
      name: appendAttribution
- id: ''
  name: Send and Wait for Response
  description: ''
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: subject
    text: My subject line
  - field: options
    text: Add option
  - field: toEmail
    text: info@example.com
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
  "$id": "https://n8n.io/schemas/nodes/emailSend.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Send Email Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "send",
        ""
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "default": "email"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "send",
            "Send and Wait for Response"
          ],
          "default": "send"
        },
        "default": {
          "description": "",
          "type": "string"
        },
        "subject": {
          "description": "Subject line of the email",
          "type": "string",
          "default": "",
          "examples": [
            "My subject line"
          ]
        },
        "emailFormat": {
          "description": "",
          "type": "string",
          "enum": [
            "text",
            "html",
            "both"
          ],
          "default": "text",
          "format": "email"
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
        "options": {
          "description": "Whether to include the phrase \u201cThis email was sent automatically with n8n\u201d to the end of the email",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "toEmail": {
          "description": "Email address of the recipient. You can also specify a name: Nathan Doe &lt;nate@n8n.io&gt;.",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "info@example.com"
          ]
        },
        "appendAttribution": {
          "description": "",
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
      "2",
      "2.1"
    ]
  },
  "credentials": [
    {
      "name": "smtp",
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
