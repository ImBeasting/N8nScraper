---
title: "Node: Mandrill"
slug: "node-mandrill"
version: "1"
updated: "2025-11-13"
summary: "Consume Mandrill API"
node_type: "regular"
group: "['output']"
---

# Node: Mandrill

**Purpose.** Consume Mandrill API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:mandrill.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **mandrillApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `mandrillApi` | ✓ | - |

---

## Operations

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send Template | `sendTemplate` | Send message based on template |
| Send HTML | `sendHtml` | Send message based on HTML |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✗ | Send a message |  |

**Resource options:**

* **Message** (`message`) - Send a message

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | sendTemplate | ✗ | Send message based on template |  |

**Operation options:**

* **Send Template** (`sendTemplate`) - Send message based on template
* **Send HTML** (`sendHtml`) - Send message based on HTML

---

### Send Template parameters (`sendTemplate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Template Name or ID | `template` | options |  | ✓ | The template you want to send. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| From Email | `fromEmail` | string |  | ✓ | Email address of the sender optional with name | e.g. Admin <example@yourdomain.com> | email |
| To Email | `toEmail` | string |  | ✓ | Email address of the recipient. Multiple ones can be separated by comma. | e.g. info@example.com | email |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | Whether to enable a background sending mode that is optimized for bulk sending. In async mode, messages/send will immediately return a status of "queued" for every recipient. To handle rejections when sending in async mode, set up a webhook for the 'reject' event. Defaults to false for messages with no more than 10 recipients; messages with more than 10 recipients are always sent asynchronously, regardless of the value of async. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Async | `async` | boolean | False | Whether to enable a background sending mode that is optimized for bulk sending. In async mode, messages/send will immediately return a status of "queued" for every recipient. To handle rejections when sending in async mode, set up a webhook for the 'reject' event. Defaults to false for messages with no more than 10 recipients; messages with more than 10 recipients are always sent asynchronously, regardless of the value of async. |
| Auto Text | `autoText` | boolean | False | Whether or not to automatically generate a text part for messages that are not given text |
| Auto HTML | `autoHtml` | boolean | False | Whether or not to automatically generate an HTML part for messages that are not given HTML |
| BCC Address | `bccAddress` | string |  | An optional address to receive an exact copy of each recipient's email |
| From Name | `fromName` | string |  | Optional from name to be used |
| Google Analytics Campaign | `googleAnalyticsCampaign` | string |  | Optional string indicating the value to set for the utm_campaign tracking parameter. If this isn't provided the email's from address will be used instead. |
| Google Analytics Domains | `googleAnalyticsDomains` | string |  | An array of strings separated by a comma (,) indicating for which any matching URLs will automatically have Google Analytics parameters appended to their query string automatically |
| HTML | `html` | string |  | The html you want to send |
| Important | `important` | boolean | False | Whether or not this message is important, and should be delivered ahead of non-important messages |
| Inline CSS | `inlineCss` | boolean | False | Whether or not to automatically inline all CSS styles provided in the message HTML - only for HTML documents less than 256KB in size |
| Ip Pool | `ipPool` | string |  | The name of the dedicated ip pool that should be used to send the message. If you do not have any dedicated IPs, this parameter has no effect. If you specify a pool that does not exist, your default pool will be used instead. |
| Preserve Recipients | `preserveRecipients` | boolean | False | Whether or not to expose all recipients in to "To" header for each email |
| Return Path Domain | `returnPathDomain` | string |  | A custom domain to use for the messages's return-path |
| Sent At | `sendAt` | dateTime |  | When this message should be sent as a UTC timestamp in YYYY-MM-DD HH:MM:SS format. If you specify a time in the past, the message will be sent immediately. An additional fee applies for scheduled email, and this feature is only available to accounts with a positive balance. |
| Signing Domain | `signingDomain` | string |  | A custom domain to use for SPF/DKIM signing instead of mandrill(for "via" or "on behalf of" in email clients) |
| Subaccount | `subAccount` | string |  | The unique ID of a subaccount for this message - must already exist or will fail with an error |
| Subject | `subject` | string |  | Subject line of the email |
| Tags | `tags` | string |  | An array of string separated by a comma (,) to tag the message with. Stats are accumulated using tags, though we only store the first 100 we see, so this should not be unique or change frequently. Tags should be 50 characters or less. Any tags starting with an underscore are reserved for internal use and will cause errors. |
| Text | `text` | string |  | Example text content |
| Track Clicks | `trackClicks` | boolean | False | Whether or not to turn on click tracking for the message |
| Track Opens | `trackOpens` | boolean | False | Whether or not to turn on open tracking for the message |
| Tracking Domain | `trackingDomain` | string |  | A custom domain to use for tracking opens and clicks instead of mandrillapp.com |
| Url Strip Qs | `urlStripQs` | boolean | False | Whether or not to strip the query string from URLs when aggregating tracked URL data |
| View Content Link | `viewContentLink` | boolean | False | Whether to remove content logging for sensitive emails |

</details>


### Send HTML parameters (`sendHtml`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From Email | `fromEmail` | string |  | ✓ | Email address of the sender optional with name | e.g. Admin <example@yourdomain.com> | email |
| To Email | `toEmail` | string |  | ✓ | Email address of the recipient. Multiple ones can be separated by comma. | e.g. info@example.com | email |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | Whether to enable a background sending mode that is optimized for bulk sending. In async mode, messages/send will immediately return a status of "queued" for every recipient. To handle rejections when sending in async mode, set up a webhook for the 'reject' event. Defaults to false for messages with no more than 10 recipients; messages with more than 10 recipients are always sent asynchronously, regardless of the value of async. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Async | `async` | boolean | False | Whether to enable a background sending mode that is optimized for bulk sending. In async mode, messages/send will immediately return a status of "queued" for every recipient. To handle rejections when sending in async mode, set up a webhook for the 'reject' event. Defaults to false for messages with no more than 10 recipients; messages with more than 10 recipients are always sent asynchronously, regardless of the value of async. |
| Auto Text | `autoText` | boolean | False | Whether or not to automatically generate a text part for messages that are not given text |
| Auto HTML | `autoHtml` | boolean | False | Whether or not to automatically generate an HTML part for messages that are not given HTML |
| BCC Address | `bccAddress` | string |  | An optional address to receive an exact copy of each recipient's email |
| From Name | `fromName` | string |  | Optional from name to be used |
| Google Analytics Campaign | `googleAnalyticsCampaign` | string |  | Optional string indicating the value to set for the utm_campaign tracking parameter. If this isn't provided the email's from address will be used instead. |
| Google Analytics Domains | `googleAnalyticsDomains` | string |  | An array of strings separated by a comma (,) indicating for which any matching URLs will automatically have Google Analytics parameters appended to their query string automatically |
| HTML | `html` | string |  | The html you want to send |
| Important | `important` | boolean | False | Whether or not this message is important, and should be delivered ahead of non-important messages |
| Inline CSS | `inlineCss` | boolean | False | Whether or not to automatically inline all CSS styles provided in the message HTML - only for HTML documents less than 256KB in size |
| Ip Pool | `ipPool` | string |  | The name of the dedicated ip pool that should be used to send the message. If you do not have any dedicated IPs, this parameter has no effect. If you specify a pool that does not exist, your default pool will be used instead. |
| Preserve Recipients | `preserveRecipients` | boolean | False | Whether or not to expose all recipients in to "To" header for each email |
| Return Path Domain | `returnPathDomain` | string |  | A custom domain to use for the messages's return-path |
| Sent At | `sendAt` | dateTime |  | When this message should be sent as a UTC timestamp in YYYY-MM-DD HH:MM:SS format. If you specify a time in the past, the message will be sent immediately. An additional fee applies for scheduled email, and this feature is only available to accounts with a positive balance. |
| Signing Domain | `signingDomain` | string |  | A custom domain to use for SPF/DKIM signing instead of mandrill(for "via" or "on behalf of" in email clients) |
| Subaccount | `subAccount` | string |  | The unique ID of a subaccount for this message - must already exist or will fail with an error |
| Subject | `subject` | string |  | Subject line of the email |
| Tags | `tags` | string |  | An array of string separated by a comma (,) to tag the message with. Stats are accumulated using tags, though we only store the first 100 we see, so this should not be unique or change frequently. Tags should be 50 characters or less. Any tags starting with an underscore are reserved for internal use and will cause errors. |
| Text | `text` | string |  | Example text content |
| Track Clicks | `trackClicks` | boolean | False | Whether or not to turn on click tracking for the message |
| Track Opens | `trackOpens` | boolean | False | Whether or not to turn on open tracking for the message |
| Tracking Domain | `trackingDomain` | string |  | A custom domain to use for tracking opens and clicks instead of mandrillapp.com |
| Url Strip Qs | `urlStripQs` | boolean | False | Whether or not to strip the query string from URLs when aggregating tracked URL data |
| View Content Link | `viewContentLink` | boolean | False | Whether to remove content logging for sensitive emails |

</details>


---

## Load Options Methods

- `getTemplates`

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Mandrill

**From workflow:** sendTemplateWithSubaccount

**Parameters:**
```json
{
  "resource": "message",
  "operation": "sendTemplate",
  "template": "test-template-subaccount",
  "fromEmail": "sender@example.com",
  "toEmail": "recipient@example.com",
  "options": {
    "subAccount": "regression-test-subaccount",
    "subject": "Testing subaccount functionality"
  }
}
```

**Credentials:**
- mandrillApi: `Test Mandrill API`

### Example 2: Mandrill

**From workflow:** sendTemplate

**Parameters:**
```json
{
  "resource": "message",
  "operation": "sendTemplate",
  "template": "test-template",
  "fromEmail": "sender@example.com",
  "toEmail": "recipient@example.com",
  "options": {
    "subAccount": "test-subaccount"
  }
}
```

**Credentials:**
- mandrillApi: `Test Mandrill API`

### Example 3: Mandrill

**From workflow:** sendHtml

**Parameters:**
```json
{
  "operation": "sendHtml",
  "fromEmail": "sender@example.com",
  "toEmail": "recipient@example.com",
  "options": {
    "html": "<h1>Test HTML Content</h1>",
    "subject": "Test HTML Subject"
  }
}
```

**Credentials:**
- mandrillApi: `Test Mandrill API`


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
node: mandrill
displayName: Mandrill
description: Consume Mandrill API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: mandrillApi
  required: true
operations:
- id: sendTemplate
  name: Send Template
  description: Send message based on template
  params:
  - id: template
    name: Template Name or ID
    type: options
    default: ''
    required: true
    description: The template you want to send. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - sendTemplate
    typeInfo:
      type: options
      displayName: Template Name or ID
      name: template
      typeOptions:
        loadOptionsMethod: getTemplates
      possibleValues: []
  - id: fromEmail
    name: From Email
    type: string
    default: ''
    required: true
    description: Email address of the sender optional with name
    placeholder: Admin <example@yourdomain.com>
    validation: &id001
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - sendHtml
          - sendTemplate
    typeInfo: &id002
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
    validation: &id003
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - sendHtml
          - sendTemplate
    typeInfo: &id004
      type: string
      displayName: To Email
      name: toEmail
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id005
      displayOptions:
        show:
          operation:
          - sendHtml
          - sendTemplate
    typeInfo: &id006
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
- id: sendHtml
  name: Send HTML
  description: Send message based on HTML
  params:
  - id: fromEmail
    name: From Email
    type: string
    default: ''
    required: true
    description: Email address of the sender optional with name
    placeholder: Admin <example@yourdomain.com>
    validation: *id001
    typeInfo: *id002
  - id: toEmail
    name: To Email
    type: string
    default: ''
    required: true
    description: Email address of the recipient. Multiple ones can be separated by
      comma.
    placeholder: info@example.com
    validation: *id003
    typeInfo: *id004
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id005
    typeInfo: *id006
examples:
- name: Mandrill
  parameters:
    resource: message
    operation: sendTemplate
    template: test-template-subaccount
    fromEmail: sender@example.com
    toEmail: recipient@example.com
    options:
      subAccount: regression-test-subaccount
      subject: Testing subaccount functionality
  workflow: sendTemplateWithSubaccount
- name: Mandrill
  parameters:
    resource: message
    operation: sendTemplate
    template: test-template
    fromEmail: sender@example.com
    toEmail: recipient@example.com
    options:
      subAccount: test-subaccount
  workflow: sendTemplate
- name: Mandrill
  parameters:
    operation: sendHtml
    fromEmail: sender@example.com
    toEmail: recipient@example.com
    options:
      html: <h1>Test HTML Content</h1>
      subject: Test HTML Subject
  workflow: sendHtml
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: fromEmail
    text: Admin <example@yourdomain.com>
  - field: toEmail
    text: info@example.com
  - field: options
    text: Add option
  - field: mergeVarsJson
    text: "[\n\t{\n\t\t{ \"name\": \"name\", \"content\": \"content\" }\n\t}\n]"
  - field: mergeVarsUi
    text: Add Merge Vars
  - field: metadataUi
    text: Add Metadata
  - field: metadataJson
    text: "{\n\t\"website\": \"www.example.com\"\n}"
  - field: attachmentsJson
    text: "[\n\t{\n\t\t\"type\": \"text/plain\" (the MIME type of the attachment),\n\
      \t\t\"name\": \"myfile.txt\" (the file name of the attachment),\n\t\t\"content\"\
      : \"ZXhhbXBsZSBmaWxl\" (the content of the attachment as a base64-encoded string)\n\
      \t}\n]"
  - field: attachmentsUi
    text: Add Attachments
  - field: headersJson
    text: "{\n\t\"Reply-To\": \"replies@example.com\"\n}"
  - field: headersUi
    text: Add Headers
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
  "$id": "https://n8n.io/schemas/nodes/mandrill.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Mandrill Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "sendTemplate",
        "sendHtml"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Send a message",
          "type": "string",
          "enum": [
            "message"
          ],
          "default": "message"
        },
        "operation": {
          "description": "Send message based on template",
          "type": "string",
          "enum": [
            "sendTemplate",
            "sendHtml"
          ],
          "default": "sendTemplate"
        },
        "template": {
          "description": "The template you want to send. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "fromEmail": {
          "description": "Email address of the sender optional with name",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "Admin <example@yourdomain.com>"
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
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "options": {
          "description": "Whether to enable a background sending mode that is optimized for bulk sending. In async mode, messages/send will immediately return a status of \"queued\" for every recipient. To handle rejections when sending in async mode, set up a webhook for the 'reject' event. Defaults to false for messages with no more than 10 recipients; messages with more than 10 recipients are always sent asynchronously, regardless of the value of async.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "mergeVarsJson": {
          "description": "Global merge variables",
          "type": "string",
          "default": "",
          "examples": [
            "[\n\t{\n\t\t{ \"name\": \"name\", \"content\": \"content\" }\n\t}\n]"
          ]
        },
        "mergeVarsUi": {
          "description": "Per-recipient merge variables",
          "type": "string",
          "default": {},
          "examples": [
            "Add Merge Vars"
          ]
        },
        "metadataUi": {
          "description": "Metadata an associative array of user metadata. Mandrill will store this metadata and make it available for retrieval. In addition, you can select up to 10 metadata fields to index and make searchable using the Mandrill search api.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Metadata"
          ]
        },
        "metadataJson": {
          "description": "Metadata an associative array of user metadata. Mandrill will store this metadata and make it available for retrieval. In addition, you can select up to 10 metadata fields to index and make searchable using the Mandrill search api.",
          "type": "string",
          "default": "",
          "examples": [
            "{\n\t\"website\": \"www.example.com\"\n}"
          ]
        },
        "attachmentsJson": {
          "description": "An array of supported attachments to add to the message",
          "type": "string",
          "default": "",
          "examples": [
            "[\n\t{\n\t\t\"type\": \"text/plain\" (the MIME type of the attachment),\n\t\t\"name\": \"myfile.txt\" (the file name of the attachment),\n\t\t\"content\": \"ZXhhbXBsZSBmaWxl\" (the content of the attachment as a base64-encoded string)\n\t}\n]"
          ]
        },
        "attachmentsUi": {
          "description": "The MIME type of the attachment",
          "type": "string",
          "default": "",
          "examples": [
            "Add Attachments"
          ]
        },
        "headersJson": {
          "description": "Optional extra headers to add to the message (most headers are allowed)",
          "type": "string",
          "default": "",
          "examples": [
            "{\n\t\"Reply-To\": \"replies@example.com\"\n}"
          ]
        },
        "headersUi": {
          "description": "Optional extra headers to add to the message (most headers are allowed)",
          "type": "string",
          "default": {},
          "examples": [
            "Add Headers"
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
      "name": "mandrillApi",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Mandrill",
      "value": {
        "resource": "message",
        "operation": "sendTemplate",
        "template": "test-template-subaccount",
        "fromEmail": "sender@example.com",
        "toEmail": "recipient@example.com",
        "options": {
          "subAccount": "regression-test-subaccount",
          "subject": "Testing subaccount functionality"
        }
      }
    },
    {
      "description": "Mandrill",
      "value": {
        "resource": "message",
        "operation": "sendTemplate",
        "template": "test-template",
        "fromEmail": "sender@example.com",
        "toEmail": "recipient@example.com",
        "options": {
          "subAccount": "test-subaccount"
        }
      }
    },
    {
      "description": "Mandrill",
      "value": {
        "operation": "sendHtml",
        "fromEmail": "sender@example.com",
        "toEmail": "recipient@example.com",
        "options": {
          "html": "<h1>Test HTML Content</h1>",
          "subject": "Test HTML Subject"
        }
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
