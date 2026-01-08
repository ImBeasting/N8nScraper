---
title: "Node: seven"
slug: "node-sms77"
version: "1"
updated: "2026-01-08"
summary: "Send SMS and make text-to-speech calls"
node_type: "regular"
group: "['transform']"
---

# Node: seven

**Purpose.** Send SMS and make text-to-speech calls
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:seven.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **sms77Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `sms77Api` | ✓ | - |

---

## Operations

### Sms Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send SMS |

### Voice Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Converts text to voice and calls a given number |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | sms | ✗ | Resource to operate on |  |

**Resource options:**

* **SMS** (`sms`)
* **Voice Call** (`voice`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | send | ✗ | Send SMS |  |

**Operation options:**

* **Send** (`send`) - Send SMS

---

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From | `from` | string |  | ✗ | The caller ID displayed in the receivers display. Max 16 numeric or 11 alphanumeric characters. | e.g. +4901234567890 |  |
| To | `to` | string |  | ✓ | The number of your recipient(s) separated by comma. Can be regular numbers or contact/groups from seven. | e.g. +49876543210, MyGroup |  |
| Message | `message` | string |  | ✓ | The message to send. Max. 1520 characters |  |
| Options | `options` | collection | {} | ✗ | Pick a date for time delayed dispatch | e.g. Add Option | min:1, max:∞ |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Delay | `delay` | dateTime |  | Pick a date for time delayed dispatch |
| Foreign ID | `foreign_id` | string |  | Custom foreign ID returned in DLR callbacks |
| Flash | `flash` | boolean | False | Send as flash message being displayed directly the receiver's display |
| Label | `label` | string |  | Custom label used to group analytics |
| Performance Tracking | `performance_tracking` | boolean | False | Whether to enable performance tracking for URLs found in the message text |
| TTL | `ttl` | number | 2880 | Custom time to live specifying the validity period of a message in minutes |

</details>

| Options | `options` | collection | {} | ✗ | The caller ID. Please use only verified sender IDs, one of your virtual inbound numbers or one of our shared virtual numbers. | e.g. Add Option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| From | `from` | string |  | The caller ID. Please use only verified sender IDs, one of your virtual inbound numbers or one of our shared virtual numbers. |

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
* Aliases: SMS, Sms77

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: sms77
displayName: seven
description: Send SMS and make text-to-speech calls
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: sms77Api
  required: true
operations:
- id: send
  name: Send
  description: Send SMS
  params:
  - id: from
    name: From
    type: string
    default: ''
    required: false
    description: The caller ID displayed in the receivers display. Max 16 numeric
      or 11 alphanumeric characters.
    placeholder: '+4901234567890'
    validation:
      displayOptions:
        show:
          operation:
          - send
          resource:
          - sms
    typeInfo:
      type: string
      displayName: From
      name: from
  - id: to
    name: To
    type: string
    default: ''
    required: true
    description: The number of your recipient(s) separated by comma. Can be regular
      numbers or contact/groups from seven.
    placeholder: +49876543210, MyGroup
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - send
          resource:
          - sms
          - voice
    typeInfo:
      type: string
      displayName: To
      name: to
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: The message to send. Max. 1520 characters
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - send
          resource:
          - sms
          - voice
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
  - field: from
    text: '+4901234567890'
  - field: to
    text: +49876543210, MyGroup
  - field: options
    text: Add Option
  - field: options
    text: Add Option
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
  "$id": "https://n8n.io/schemas/nodes/sms77.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "seven Node",
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
            "sms",
            "voice"
          ],
          "default": "sms"
        },
        "operation": {
          "description": "Converts text to voice and calls a given number",
          "type": "string",
          "enum": [
            "send"
          ],
          "default": "send"
        },
        "from": {
          "description": "The caller ID displayed in the receivers display. Max 16 numeric or 11 alphanumeric characters.",
          "type": "string",
          "default": "",
          "examples": [
            "+4901234567890"
          ]
        },
        "to": {
          "description": "The number of your recipient(s) separated by comma. Can be regular numbers or contact/groups from seven.",
          "type": "string",
          "default": "",
          "examples": [
            "+49876543210, MyGroup"
          ]
        },
        "message": {
          "description": "The message to send. Max. 1520 characters",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "The caller ID. Please use only verified sender IDs, one of your virtual inbound numbers or one of our shared virtual numbers.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Option"
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
      "name": "sms77Api",
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
