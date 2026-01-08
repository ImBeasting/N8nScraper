---
title: "Node: Plivo"
slug: "node-plivo"
version: "1"
updated: "2026-01-08"
summary: "Send SMS/MMS messages or make phone calls"
node_type: "regular"
group: "['transform']"
---

# Node: Plivo

**Purpose.** Send SMS/MMS messages or make phone calls
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:plivo.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **plivoApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `plivoApi` | ✓ | - |

---

## API Patterns

**Headers Used:** user-agent

---

## Operations

### Sms Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send an SMS message |

### Mms Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send an MMS message (US/Canada only) |

### Call Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Make | `make` | Make a voice call |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | sms | ✓ | Resource to operate on |  |

**Resource options:**

* **Call** (`call`)
* **MMS** (`mms`)
* **SMS** (`sms`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | send | ✗ | Send an SMS message |  |

**Operation options:**

* **Send** (`send`) - Send an SMS message

---

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From | `from` | string |  | ✓ | Plivo Number to send the SMS from | e.g. +14156667777 |  |
| To | `to` | string |  | ✓ | Phone number to send the message to | e.g. +14156667778 |  |
| Message | `message` | string |  | ✓ | Message to send |  |
| From | `from` | string |  | ✓ | Plivo Number to send the MMS from | e.g. +14156667777 |  |
| To | `to` | string |  | ✓ | Phone number to send the MMS to | e.g. +14156667778 |  |
| Message | `message` | string |  | ✗ | Message to send |  |
| Media URLs | `media_urls` | string |  | ✗ | Comma-separated list of media URLs of the files from your file server | url |

### Make parameters (`make`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From | `from` | string |  | ✓ | Caller ID for the call to make | e.g. +14156667777 |  |
| To | `to` | string |  | ✓ | Phone number to make the call to | e.g. +14156667778 |  |
| Answer Method | `answer_method` | options | POST | ✓ | HTTP verb to be used when invoking the Answer URL |  |

**Answer Method options:**

* **GET** (`GET`)
* **POST** (`POST`)

| Answer URL | `answer_url` | string |  | ✓ | URL to be invoked by Plivo once the call is answered. It should return the XML to handle the call once answered. | url |

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
node: plivo
displayName: Plivo
description: Send SMS/MMS messages or make phone calls
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: plivoApi
  required: true
operations:
- id: send
  name: Send
  description: Send an SMS message
  params:
  - id: from
    name: From
    type: string
    default: ''
    required: true
    description: Plivo Number to send the SMS from
    placeholder: '+14156667777'
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - call
          operation:
          - make
    typeInfo: &id002
      type: string
      displayName: From
      name: from
  - id: to
    name: To
    type: string
    default: ''
    required: true
    description: Phone number to send the message to
    placeholder: '+14156667778'
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - call
          operation:
          - make
    typeInfo: &id004
      type: string
      displayName: To
      name: to
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: Message to send
    validation: &id005
      displayOptions:
        show:
          resource:
          - mms
          operation:
          - send
    typeInfo: &id006
      type: string
      displayName: Message
      name: message
  - id: from
    name: From
    type: string
    default: ''
    required: true
    description: Plivo Number to send the MMS from
    placeholder: '+14156667777'
    validation: *id001
    typeInfo: *id002
  - id: to
    name: To
    type: string
    default: ''
    required: true
    description: Phone number to send the MMS to
    placeholder: '+14156667778'
    validation: *id003
    typeInfo: *id004
  - id: message
    name: Message
    type: string
    default: ''
    required: false
    description: Message to send
    validation: *id005
    typeInfo: *id006
  - id: media_urls
    name: Media URLs
    type: string
    default: ''
    required: false
    description: Comma-separated list of media URLs of the files from your file server
    validation:
      format: url
      displayOptions:
        show:
          resource:
          - mms
          operation:
          - send
    typeInfo:
      type: string
      displayName: Media URLs
      name: media_urls
- id: make
  name: Make
  description: Make a voice call
  params:
  - id: from
    name: From
    type: string
    default: ''
    required: true
    description: Caller ID for the call to make
    placeholder: '+14156667777'
    validation: *id001
    typeInfo: *id002
  - id: to
    name: To
    type: string
    default: ''
    required: true
    description: Phone number to make the call to
    placeholder: '+14156667778'
    validation: *id003
    typeInfo: *id004
  - id: answer_method
    name: Answer Method
    type: options
    default: POST
    required: true
    description: HTTP verb to be used when invoking the Answer URL
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - call
          operation:
          - make
    typeInfo:
      type: options
      displayName: Answer Method
      name: answer_method
      possibleValues:
      - value: GET
        name: GET
        description: ''
      - value: POST
        name: POST
        description: ''
  - id: answer_url
    name: Answer URL
    type: string
    default: ''
    required: true
    description: URL to be invoked by Plivo once the call is answered. It should return
      the XML to handle the call once answered.
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - call
          operation:
          - make
    typeInfo:
      type: string
      displayName: Answer URL
      name: answer_url
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - user-agent
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: from
    text: '+14156667777'
  - field: to
    text: '+14156667778'
  - field: from
    text: '+14156667777'
  - field: to
    text: '+14156667778'
  - field: from
    text: '+14156667777'
  - field: to
    text: '+14156667778'
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
  "$id": "https://n8n.io/schemas/nodes/plivo.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Plivo Node",
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
            "mms",
            "sms"
          ],
          "default": "sms"
        },
        "operation": {
          "description": "Make a voice call",
          "type": "string",
          "enum": [
            "make"
          ],
          "default": "make"
        },
        "from": {
          "description": "Caller ID for the call to make",
          "type": "string",
          "default": "",
          "examples": [
            "+14156667777"
          ]
        },
        "to": {
          "description": "Phone number to make the call to",
          "type": "string",
          "default": "",
          "examples": [
            "+14156667778"
          ]
        },
        "message": {
          "description": "Message to send",
          "type": "string",
          "default": ""
        },
        "media_urls": {
          "description": "Comma-separated list of media URLs of the files from your file server",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "answer_method": {
          "description": "HTTP verb to be used when invoking the Answer URL",
          "type": "string",
          "enum": [
            "GET",
            "POST"
          ],
          "default": "POST"
        },
        "answer_url": {
          "description": "URL to be invoked by Plivo once the call is answered. It should return the XML to handle the call once answered.",
          "type": "string",
          "default": "",
          "format": "url"
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
      "name": "plivoApi",
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
