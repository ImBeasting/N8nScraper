---
title: "Node: Vonage"
slug: "node-vonage"
version: "1"
updated: "2025-11-13"
summary: "Consume Vonage API"
node_type: "regular"
group: "['input']"
---

# Node: Vonage

**Purpose.** Consume Vonage API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:vonage.svg', 'dark': 'file:vonage.dark.svg'}`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **vonageApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `vonageApi` | ✓ | - |

---

## Operations

### Sms Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send an SMS |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | sms | ✗ | Resource to operate on |  |

**Resource options:**

* **SMS** (`sms`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | send | ✗ | Operation to perform |  |

**Operation options:**

* **Send** (`send`) - Send an SMS

---

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From | `from` | string |  | ✗ | The name or number the message should be sent from |  |
| To | `to` | string |  | ✗ | The number that the message should be sent to. Numbers are specified in E.164 format. |  |
| Message | `message` | string |  | ✗ | The body of the message being sent |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | An optional string used to identify separate accounts using the SMS endpoint for billing purposes. To use this feature, please email support@nexmo.com. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Ref | `account-ref` | string |  | An optional string used to identify separate accounts using the SMS endpoint for billing purposes. To use this feature, please email support@nexmo.com. |
| Callback | `callback` | string |  | The webhook endpoint the delivery receipt for this sms is sent to. This parameter overrides the webhook endpoint you set in Dashboard. |
| Client Ref | `client-ref` | string |  | You can optionally include your own reference of up to 40 characters |
| Message Class | `message-class` | options |  | The Data Coding Scheme value of the message |
| Protocol ID | `protocol-id` | string |  | The value of the protocol identifier to use. Ensure that the value is aligned with udh. |
| Status Report Req | `status-report-req` | boolean | False | Whether to receive a Delivery Receipt |
| TTL (in Minutes) | `ttl` | number | 4320 | By default Nexmo attempt delivery for 72 hours |

</details>


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
* Categories: Communication
* Aliases: SMS

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: vonage
displayName: Vonage
description: Consume Vonage API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: vonageApi
  required: true
operations:
- id: send
  name: Send
  description: ''
  params:
  - id: from
    name: From
    type: string
    default: ''
    required: false
    description: The name or number the message should be sent from
    validation:
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
    required: false
    description: The number that the message should be sent to. Numbers are specified
      in E.164 format.
    validation:
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
  - id: message
    name: Message
    type: string
    default: ''
    required: false
    description: The body of the message being sent
    validation:
      displayOptions:
        show:
          resource:
          - sms
          operation:
          - send
          type:
          - "// \t'text"
          - "// \t'unicode"
          - //
    typeInfo:
      type: string
      displayName: Message
      name: message
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
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/vonage.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Vonage Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "send"
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
            "sms"
          ],
          "default": "sms"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "send"
          ],
          "default": "send"
        },
        "from": {
          "description": "The name or number the message should be sent from",
          "type": "string",
          "default": ""
        },
        "to": {
          "description": "The number that the message should be sent to. Numbers are specified in E.164 format.",
          "type": "string",
          "default": ""
        },
        "type": {
          "description": "The format of the message body",
          "type": "string",
          "enum": [
            "binary",
            "text",
            "wappush",
            "unicode",
            "vcal",
            "vcard"
          ],
          "default": "text"
        },
        "binaryPropertyName": {
          "description": "Object property name which holds binary data.",
          "type": "string",
          "default": "data"
        },
        "body": {
          "description": "Hex encoded binary data",
          "type": "string",
          "default": ""
        },
        "udh": {
          "description": "Your custom Hex encoded User Data Header",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "The title for a wappush SMS",
          "type": "string",
          "default": ""
        },
        "url": {
          "description": "The URL of your website",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "validity": {
          "description": "The availability for an SMS in minutes",
          "type": "number",
          "default": 0
        },
        "message": {
          "description": "The body of the message being sent",
          "type": "string",
          "default": ""
        },
        "vcard": {
          "description": "A business card in vCard format",
          "type": "string",
          "default": ""
        },
        "vcal": {
          "description": "A calendar event in vCal format",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "An optional string used to identify separate accounts using the SMS endpoint for billing purposes. To use this feature, please email support@nexmo.com.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
      "name": "vonageApi",
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
