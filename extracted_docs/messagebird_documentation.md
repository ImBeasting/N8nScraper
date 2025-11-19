---
title: "Node: MessageBird"
slug: "node-messagebird"
version: "1"
updated: "2025-11-13"
summary: "Sends SMS via MessageBird"
node_type: "regular"
group: "['output']"
---

# Node: MessageBird

**Purpose.** Sends SMS via MessageBird
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:messagebird.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **messageBirdApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `messageBirdApi` | ✓ | - |

---

## Operations

### Sms Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send text messages (SMS) |

### Balance Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get the balance |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | sms | ✗ | Resource to operate on |  |

**Resource options:**

* **SMS** (`sms`)
* **Balance** (`balance`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | send | ✗ | Send text messages (SMS) |  |

**Operation options:**

* **Send** (`send`) - Send text messages (SMS)

---

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From | `originator` | string |  | ✓ | The number from which to send the message | e.g. 14155238886 |  |
| To | `recipients` | string |  | ✓ | All recipients separated by commas | e.g. 14155238886/+14155238886 |  |
| Message | `message` | string |  | ✓ | The message to be send |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The date and time of the creation of the message in RFC3339 format (Y-m-dTH:i:sP) | e.g. Add Fields | min:1, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Created Date-Time | `createdDatetime` | dateTime |  | The date and time of the creation of the message in RFC3339 format (Y-m-dTH:i:sP) |
| Datacoding | `datacoding` | options |  | Using unicode will limit the maximum number of characters to 70 instead of 160 |
| Gateway | `gateway` | number |  | The SMS route that is used to send the message |
| Group IDs | `groupIds` | string |  | Group IDs separated by commas, If provided recipients can be omitted |
| Message Type | `mclass` | options | 1 | Indicated the message type. 1 is a normal message, 0 is a flash message. |
| Reference | `reference` | string |  | A client reference |
| Report Url | `reportUrl` | string |  | The status report URL to be used on a per-message basis. Reference is required for a status report webhook to be sent. |
| Scheduled Date-Time | `scheduledDatetime` | dateTime |  | The scheduled date and time of the message in RFC3339 format (Y-m-dTH:i:sP) |
| Type | `type` | options |  | The type of message. Values can be: sms, binary, or flash. |
| Type Details | `typeDetails` | string |  | A hash with extra information. Is only used when a binary message is sent. |
| Validity | `validity` | number | 1 | The amount of seconds that the message is valid |

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: messageBird
displayName: MessageBird
description: Sends SMS via MessageBird
version: '1'
nodeType: regular
group:
- output
credentials:
- name: messageBirdApi
  required: true
operations:
- id: send
  name: Send
  description: Send text messages (SMS)
  params:
  - id: originator
    name: From
    type: string
    default: ''
    required: true
    description: The number from which to send the message
    placeholder: '14155238886'
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - send
          resource:
          - sms
    typeInfo:
      type: string
      displayName: From
      name: originator
  - id: recipients
    name: To
    type: string
    default: ''
    required: true
    description: All recipients separated by commas
    placeholder: 14155238886/+14155238886
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - send
          resource:
          - sms
    typeInfo:
      type: string
      displayName: To
      name: recipients
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: The message to be send
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - send
          resource:
          - sms
    typeInfo:
      type: string
      displayName: Message
      name: message
- id: get
  name: Get
  description: Get the balance
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
  - field: originator
    text: '14155238886'
  - field: recipients
    text: 14155238886/+14155238886
  - field: additionalFields
    text: Add Fields
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
  "$id": "https://n8n.io/schemas/nodes/messageBird.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MessageBird Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "send",
        "get"
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
            "sms",
            "balance"
          ],
          "default": "sms"
        },
        "operation": {
          "description": "Get the balance",
          "type": "string",
          "enum": [
            "get"
          ],
          "default": "get"
        },
        "originator": {
          "description": "The number from which to send the message",
          "type": "string",
          "default": "",
          "examples": [
            "14155238886"
          ]
        },
        "recipients": {
          "description": "All recipients separated by commas",
          "type": "string",
          "default": "",
          "examples": [
            "14155238886/+14155238886"
          ]
        },
        "message": {
          "description": "The message to be send",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The date and time of the creation of the message in RFC3339 format (Y-m-dTH:i:sP)",
          "type": "string",
          "default": {},
          "examples": [
            "Add Fields"
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
      "name": "messageBirdApi",
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
