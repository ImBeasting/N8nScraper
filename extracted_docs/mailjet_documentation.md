---
title: "Node: Mailjet"
slug: "node-mailjet"
version: "1"
updated: "2026-01-08"
summary: "Consume Mailjet API"
node_type: "regular"
group: "['output']"
---

# Node: Mailjet

**Purpose.** Consume Mailjet API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:mailjet.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **mailjetEmailApi**: N/A
- **mailjetSmsApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `mailjetEmailApi` | ✓ | {'show': {'resource': ['email']}} |
| `mailjetSmsApi` | ✓ | {'show': {'resource': ['sms']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Email Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send a email |
| Send Template | `sendTemplate` | Send a email template |

### Sms Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send a sms |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | email | ✗ | Resource to operate on |  |

**Resource options:**

* **Email** (`email`)
* **SMS** (`sms`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | send | ✗ | Send a email |  |

**Operation options:**

* **Send** (`send`) - Send a email
* **Send Template** (`sendTemplate`) - Send a email template

---

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From Email | `fromEmail` | string |  | ✓ | The title for the email | e.g. admin@example.com | email |
| To Email | `toEmail` | string |  | ✓ | Email address of the recipient. Multiple ones can be separated by comma. | e.g. info@example.com | email |
| Text | `text` | string |  | ✗ | Plain text message of email |  |
| HTML | `html` | string |  | ✗ | HTML text message of email |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Bcc Email address of the recipient. Multiple ones can be separated by comma. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Bcc Email | `bccEmail` | string |  | Bcc Email address of the recipient. Multiple ones can be separated by comma. |
| Cc Addresses | `ccAddresses` | string |  | Cc Email address of the recipient. Multiple ones can be separated by comma. |
| From Name | `fromName` | string |  |  |
| Priority | `priority` | number | 2 |  |
| Reply To | `replyTo` | string |  | The reply-to email address. Multiple ones can be separated by comma. |
| Template Language | `templateLanguage` | boolean | False |  |
| Track Clicks | `trackClicks` | options | account_default | Use the values specified in the Mailjet account |
| Track Opens | `trackOpens` | options | account_default | Use the values specified in the Mailjet account |
| Custom Campaign | `customCampaign` | string |  |  |
| Deduplicate Campaign | `deduplicateCampaign` | boolean | False |  |

</details>

| Variables (JSON) | `variablesJson` | string |  | ✗ | HTML text message of email |  |
| Variables | `variablesUi` | fixedCollection | {} | ✗ | e.g. Add Variable |  |

<details>
<summary><strong>Variables sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Variable | `variablesValues` |  |  |  |

</details>

| From | `from` | string |  | ✓ | Customizable sender name. Should be between 3 and 11 characters in length, only alphanumeric characters are allowed. |  |
| To | `to` | string |  | ✓ | Message recipient. Should be between 3 and 15 characters in length. The number always starts with a plus sign followed by a country code, followed by the number. Phone numbers are expected to comply with the E.164 format. |  |
| Text | `text` | string |  | ✓ |  |  |

### Send Template parameters (`sendTemplate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From Email | `fromEmail` | string |  | ✓ | The title for the email | e.g. admin@example.com | email |
| To Email | `toEmail` | string |  | ✓ | Email address of the recipient. Multiple ones can be separated by comma. | e.g. info@example.com | email |
| Template Name or ID | `templateId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | BCC Recipients of the email separated by , | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Bcc Email | `bccEmail` | string |  | BCC Recipients of the email separated by , |
| Cc Email | `ccEmail` | string |  | Cc recipients of the email separated by , |
| From Name | `fromName` | string |  |  |
| Priority | `priority` | number | 2 |  |
| Reply To | `replyTo` | string |  | The reply-to email address. Multiple ones can be separated by comma. |
| Subject | `subject` | string |  |  |
| Template Language | `templateLanguage` | boolean | False |  |
| Track Clicks | `trackClicks` | string |  | Enable or disable open tracking on this message |
| Track Opens | `trackOpens` | string |  | Enable or disable open tracking on this message |
| Custom Campaign | `customCampaign` | string |  |  |
| Deduplicate Campaign | `deduplicateCampaign` | boolean | False |  |

</details>

| Variables | `variablesUi` | fixedCollection | {} | ✗ | e.g. Add Variable |  |

<details>
<summary><strong>Variables sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Variable | `variablesValues` |  |  |  |

</details>

| Variables (JSON) | `variablesJson` | string |  | ✗ | HTML text message of email |  |

---

## Load Options Methods

- `getTemplates`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ": " + $parameter["resource"]}}`

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
node: mailjet
displayName: Mailjet
description: Consume Mailjet API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: mailjetEmailApi
  required: true
- name: mailjetSmsApi
  required: true
operations:
- id: send
  name: Send
  description: Send a email
  params:
  - id: fromEmail
    name: From Email
    type: string
    default: ''
    required: true
    description: The title for the email
    placeholder: admin@example.com
    validation: &id003
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - email
          operation:
          - sendTemplate
    typeInfo: &id004
      type: string
      displayName: From Email
      name: fromEmail
  - id: toEmail
    name: To Email
    type: string
    default: ''
    required: true
    description: Email address of the recipient. Multiple ones can be separated by
      comma.
    placeholder: info@example.com
    validation: &id005
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - email
          operation:
          - sendTemplate
    typeInfo: &id006
      type: string
      displayName: To Email
      name: toEmail
  - id: text
    name: Text
    type: string
    default: ''
    required: false
    description: Plain text message of email
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - sms
          operation:
          - send
    typeInfo: &id002
      type: string
      displayName: Text
      name: text
  - id: html
    name: HTML
    type: string
    default: ''
    required: false
    description: HTML text message of email
    validation:
      displayOptions:
        show:
          resource:
          - email
          operation:
          - send
    typeInfo:
      type: string
      displayName: HTML
      name: html
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id007
      displayOptions:
        show:
          resource:
          - email
          operation:
          - sendTemplate
    typeInfo: &id008
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: variablesJson
    name: Variables (JSON)
    type: string
    default: ''
    required: false
    description: HTML text message of email
    validation: &id011
      displayOptions:
        show:
          resource:
          - email
          operation:
          - sendTemplate
          jsonParameters:
          - true
    typeInfo: &id012
      type: string
      displayName: Variables (JSON)
      name: variablesJson
  - id: variablesUi
    name: Variables
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Variable
    validation: &id009
      displayOptions:
        show:
          resource:
          - email
          operation:
          - sendTemplate
          jsonParameters:
          - false
    typeInfo: &id010
      type: fixedCollection
      displayName: Variables
      name: variablesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: variablesValues
        displayName: Variable
        values:
        - displayName: Name
          name: name
          type: string
          default: ''
        - displayName: Value
          name: value
          type: string
          default: ''
  - id: from
    name: From
    type: string
    default: ''
    required: true
    description: Customizable sender name. Should be between 3 and 11 characters in
      length, only alphanumeric characters are allowed.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - sms
          operation:
          - send
    typeInfo:
      type: string
      displayName: From
      name: from
  - id: to
    name: To
    type: string
    default: ''
    required: true
    description: Message recipient. Should be between 3 and 15 characters in length.
      The number always starts with a plus sign followed by a country code, followed
      by the number. Phone numbers are expected to comply with the E.164 format.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - sms
          operation:
          - send
    typeInfo:
      type: string
      displayName: To
      name: to
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
- id: sendTemplate
  name: Send Template
  description: Send a email template
  params:
  - id: fromEmail
    name: From Email
    type: string
    default: ''
    required: true
    description: The title for the email
    placeholder: admin@example.com
    validation: *id003
    typeInfo: *id004
  - id: toEmail
    name: To Email
    type: string
    default: ''
    required: true
    description: Email address of the recipient. Multiple ones can be separated by
      comma.
    placeholder: info@example.com
    validation: *id005
    typeInfo: *id006
  - id: templateId
    name: Template Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - email
          operation:
          - sendTemplate
    typeInfo:
      type: options
      displayName: Template Name or ID
      name: templateId
      typeOptions:
        loadOptionsMethod: getTemplates
      possibleValues: []
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: variablesUi
    name: Variables
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Variable
    validation: *id009
    typeInfo: *id010
  - id: variablesJson
    name: Variables (JSON)
    type: string
    default: ''
    required: false
    description: HTML text message of email
    validation: *id011
    typeInfo: *id012
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
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
  - field: fromEmail
    text: admin@example.com
  - field: toEmail
    text: info@example.com
  - field: subject
    text: My subject line
  - field: additionalFields
    text: Add Field
  - field: variablesUi
    text: Add Variable
  - field: fromEmail
    text: admin@example.com
  - field: toEmail
    text: info@example.com
  - field: additionalFields
    text: Add Field
  - field: variablesUi
    text: Add Variable
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
  "$id": "https://n8n.io/schemas/nodes/mailjet.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Mailjet Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "send",
        "sendTemplate"
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
          "enum": [
            "email",
            "sms"
          ],
          "default": "email"
        },
        "operation": {
          "description": "Send a sms",
          "type": "string",
          "enum": [
            "send"
          ],
          "default": "send"
        },
        "fromEmail": {
          "description": "The title for the email",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "admin@example.com"
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
        "subject": {
          "description": "Subject line of the email",
          "type": "string",
          "default": "",
          "examples": [
            "My subject line"
          ]
        },
        "text": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "html": {
          "description": "HTML text message of email",
          "type": "string",
          "default": ""
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "additionalFields": {
          "description": "BCC Recipients of the email separated by ,",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "variablesJson": {
          "description": "HTML text message of email",
          "type": "string",
          "default": ""
        },
        "variablesUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Variable"
          ]
        },
        "templateId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "from": {
          "description": "Customizable sender name. Should be between 3 and 11 characters in length, only alphanumeric characters are allowed.",
          "type": "string",
          "default": ""
        },
        "to": {
          "description": "Message recipient. Should be between 3 and 15 characters in length. The number always starts with a plus sign followed by a country code, followed by the number. Phone numbers are expected to comply with the E.164 format.",
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
      "name": "mailjetEmailApi",
      "required": true
    },
    {
      "name": "mailjetSmsApi",
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
