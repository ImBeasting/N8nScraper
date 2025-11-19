---
title: "Node: Twilio"
slug: "node-twilio"
version: "1"
updated: "2025-11-13"
summary: "Send SMS and WhatsApp messages or make phone calls"
node_type: "regular"
group: "['transform']"
---

# Node: Twilio

**Purpose.** Send SMS and WhatsApp messages or make phone calls
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:twilio.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **twilioApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `twilioApi` | ✓ | - |

---

## API Patterns

**Common Endpoints:**
- `https://events.twilio.com/v1/{endpoint}`

**Headers Used:** Content-Type

---

## Operations

### Sms Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send SMS/MMS/WhatsApp message |

### Call Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Make | `make` | Make a call |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | sms | ✗ | Resource to operate on |  |

**Resource options:**

* **Call** (`call`)
* **SMS** (`sms`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | send | ✗ | Send SMS/MMS/WhatsApp message |  |

**Operation options:**

* **Send** (`send`) - Send SMS/MMS/WhatsApp message

---

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From | `from` | string |  | ✓ | The number from which to send the message | e.g. +14155238886 |  |
| To | `to` | string |  | ✓ | The number to which to send the message | e.g. +14155238886 |  |
| To Whatsapp | `toWhatsapp` | boolean | False | ✗ | Whether the message should be sent to WhatsApp |  |
| Message | `message` | string |  | ✓ | The message to send |  |

### Make parameters (`make`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From | `from` | string |  | ✓ | The number from which to send the message | e.g. +14155238886 |  |
| To | `to` | string |  | ✓ | The number to which to send the message | e.g. +14155238886 |  |
| Use TwiML | `twiml` | boolean | False | ✗ | Whether to use the <a href="https://www.twilio.com/docs/voice/twiml">Twilio Markup Language</a> in the message |  |
| Message | `message` | string |  | ✓ |  |  |

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
* Aliases: SMS, Phone, Voice

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: twilio
displayName: Twilio
description: Send SMS and WhatsApp messages or make phone calls
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: twilioApi
  required: true
operations:
- id: send
  name: Send
  description: Send SMS/MMS/WhatsApp message
  params:
  - id: from
    name: From
    type: string
    default: ''
    required: true
    description: The number from which to send the message
    placeholder: '+14155238886'
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - send
          - make
          resource:
          - sms
          - call
    typeInfo: &id002
      type: string
      displayName: From
      name: from
  - id: to
    name: To
    type: string
    default: ''
    required: true
    description: The number to which to send the message
    placeholder: '+14155238886'
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - send
          - make
          resource:
          - sms
          - call
    typeInfo: &id004
      type: string
      displayName: To
      name: to
  - id: toWhatsapp
    name: To Whatsapp
    type: boolean
    default: false
    required: false
    description: Whether the message should be sent to WhatsApp
    validation:
      displayOptions:
        show:
          operation:
          - send
          resource:
          - sms
    typeInfo:
      type: boolean
      displayName: To Whatsapp
      name: toWhatsapp
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: The message to send
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - make
          resource:
          - call
    typeInfo: &id006
      type: string
      displayName: Message
      name: message
- id: make
  name: Make
  description: ''
  params:
  - id: from
    name: From
    type: string
    default: ''
    required: true
    description: The number from which to send the message
    placeholder: '+14155238886'
    validation: *id001
    typeInfo: *id002
  - id: to
    name: To
    type: string
    default: ''
    required: true
    description: The number to which to send the message
    placeholder: '+14155238886'
    validation: *id003
    typeInfo: *id004
  - id: twiml
    name: Use TwiML
    type: boolean
    default: false
    required: false
    description: Whether to use the <a href="https://www.twilio.com/docs/voice/twiml">Twilio
      Markup Language</a> in the message
    validation:
      displayOptions:
        show:
          operation:
          - make
          resource:
          - call
    typeInfo:
      type: boolean
      displayName: Use TwiML
      name: twiml
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints:
  - https://events.twilio.com/v1/{endpoint}
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: from
    text: '+14155238886'
  - field: to
    text: '+14155238886'
  - field: options
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
  "$id": "https://n8n.io/schemas/nodes/twilio.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Twilio Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "send",
        "make"
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
            "call",
            "sms"
          ],
          "default": "sms"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "make"
          ],
          "default": "make"
        },
        "from": {
          "description": "The number from which to send the message",
          "type": "string",
          "default": "",
          "examples": [
            "+14155238886"
          ]
        },
        "to": {
          "description": "The number to which to send the message",
          "type": "string",
          "default": "",
          "examples": [
            "+14155238886"
          ]
        },
        "toWhatsapp": {
          "description": "Whether the message should be sent to WhatsApp",
          "type": "boolean",
          "default": false
        },
        "message": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "twiml": {
          "description": "Whether to use the <a href=\"https://www.twilio.com/docs/voice/twiml\">Twilio Markup Language</a> in the message",
          "type": "boolean",
          "default": false
        },
        "options": {
          "description": "Status Callbacks allow you to receive events related to the REST resources managed by Twilio: Rooms, Recordings and Compositions",
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
      "name": "twilioApi",
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
