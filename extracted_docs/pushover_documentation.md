---
title: "Node: Pushover"
slug: "node-pushover"
version: "1"
updated: "2026-01-08"
summary: "Consume Pushover API"
node_type: "regular"
group: "['input']"
---

# Node: Pushover

**Purpose.** Consume Pushover API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:pushover.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **pushoverApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `pushoverApi` | ✓ | - |

---

## API Patterns

**Common Endpoints:**
- `https://api.pushover.net/1{path}`

**Headers Used:** Content-Type

---

## Operations

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Push | `push` | Push a message |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✗ | Resource to operate on |  |

**Resource options:**

* **Message** (`message`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | push | ✗ | Operation to perform |  |

**Operation options:**

* **Push** (`push`) - Push a message

---

### Push parameters (`push`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User Key | `userKey` | string |  | ✓ | The user/group key (not e-mail address) of your user (or you), viewable when logged into the <a href="https://pushover.net/">dashboard</a> (often referred to as <code>USER_KEY</code> in the <a href="https://support.pushover.net/i44-example-code-and-pushover-libraries">libraries</a> and code examples) |  |
| Message | `message` | string |  | ✓ | Your message |  |
| Priority | `priority` | options |  | ✗ | Send as -2 to generate no notification/alert, -1 to always send as a quiet notification, 1 to display as high-priority and bypass the user's quiet hours, or 2 to also require confirmation from the user |  |

**Priority options:**

* **Lowest Priority** (``)
* **Low Priority** (``)
* **Normal Priority** (``)
* **High Priority** (``)
* **Emergency Priority** (``)

| Retry (Seconds) | `retry` | number | 30 | ✓ | Specifies how often (in seconds) the Pushover servers will send the same notification to the user. This parameter must have a value of at least 30 seconds between retries. | min:0, max:∞ |
| Expire (Seconds) | `expire` | number | 30 | ✓ | Specifies how many seconds your notification will continue to be retried for (every retry seconds) | min:0, max:10800 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Your user's device name to send the message directly to that device, rather than all of the user's devices (multiple devices may be separated by a comma) | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment | `attachmentsUi` | fixedCollection |  |  |
| Device | `device` | string |  | Your user's device name to send the message directly to that device, rather than all of the user's devices (multiple devices may be separated by a comma) |
| HTML Formatting | `html` | boolean | False | Whether to enable messages formatting with HTML tags |
| Sound Name or ID | `sound` | options |  | The name of one of the sounds supported by device clients to override the user's default sound choice. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Timestamp | `timestamp` | dateTime |  | A Unix timestamp of your message's date and time to display to the user, rather than the time your message is received by our API |
| Title | `title` | string |  | Your message's title, otherwise your app's name is used |
| Timestamp | `timestamp` | dateTime |  | A Unix timestamp of your message's date and time to display to the user, rather than the time your message is received by our API |
| URL | `url` | string |  | A supplementary URL to show with your message |
| URL Title | `url_title` | string |  | A title for your supplementary URL, otherwise just the URL is shown |

</details>


---

## Load Options Methods

- `getSounds`

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
node: pushover
displayName: Pushover
description: Consume Pushover API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: pushoverApi
  required: true
operations:
- id: push
  name: Push
  description: ''
  params:
  - id: userKey
    name: User Key
    type: string
    default: ''
    required: true
    description: The user/group key (not e-mail address) of your user (or you), viewable
      when logged into the <a href="https://pushover.net/">dashboard</a> (often referred
      to as <code>USER_KEY</code> in the <a href="https://support.pushover.net/i44-example-code-and-pushover-libraries">libraries</a>
      and code examples)
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - push
    typeInfo:
      type: string
      displayName: User Key
      name: userKey
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: Your message
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - push
    typeInfo:
      type: string
      displayName: Message
      name: message
  - id: priority
    name: Priority
    type: options
    default: ''
    required: false
    description: Send as -2 to generate no notification/alert, -1 to always send as
      a quiet notification, 1 to display as high-priority and bypass the user's quiet
      hours, or 2 to also require confirmation from the user
    validation:
      displayOptions:
        show:
          resource:
          - message
          operation:
          - push
    typeInfo:
      type: options
      displayName: Priority
      name: priority
      possibleValues:
      - value: Lowest Priority
        name: Lowest Priority
        description: ''
      - value: Low Priority
        name: Low Priority
        description: ''
      - value: Normal Priority
        name: Normal Priority
        description: ''
      - value: High Priority
        name: High Priority
        description: ''
      - value: Emergency Priority
        name: Emergency Priority
        description: ''
  - id: retry
    name: Retry (Seconds)
    type: number
    default: 30
    required: true
    description: Specifies how often (in seconds) the Pushover servers will send the
      same notification to the user. This parameter must have a value of at least
      30 seconds between retries.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - push
          priority:
          - 2
    typeInfo:
      type: number
      displayName: Retry (Seconds)
      name: retry
      typeOptions:
        minValue: 0
  - id: expire
    name: Expire (Seconds)
    type: number
    default: 30
    required: true
    description: Specifies how many seconds your notification will continue to be
      retried for (every retry seconds)
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - push
          priority:
          - 2
    typeInfo:
      type: number
      displayName: Expire (Seconds)
      name: expire
      typeOptions:
        minValue: 0
        maxValue: 10800
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints:
  - https://api.pushover.net/1{path}
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  hints:
  - field: additionalFields
    text: The name of the input binary field containing the file which should be added
      to email as attachment
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
  "$id": "https://n8n.io/schemas/nodes/pushover.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Pushover Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "push"
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
            "message"
          ],
          "default": "message"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "push"
          ],
          "default": "push"
        },
        "userKey": {
          "description": "The user/group key (not e-mail address) of your user (or you), viewable when logged into the <a href=\"https://pushover.net/\">dashboard</a> (often referred to as <code>USER_KEY</code> in the <a href=\"https://support.pushover.net/i44-example-code-and-pushover-libraries\">libraries</a> and code examples)",
          "type": "string",
          "default": ""
        },
        "message": {
          "description": "Your message",
          "type": "string",
          "default": ""
        },
        "priority": {
          "description": "Send as -2 to generate no notification/alert, -1 to always send as a quiet notification, 1 to display as high-priority and bypass the user's quiet hours, or 2 to also require confirmation from the user",
          "type": "string",
          "enum": [
            "Lowest Priority",
            "Low Priority",
            "Normal Priority",
            "High Priority",
            "Emergency Priority"
          ]
        },
        "retry": {
          "description": "Specifies how often (in seconds) the Pushover servers will send the same notification to the user. This parameter must have a value of at least 30 seconds between retries.",
          "type": "number",
          "default": 30
        },
        "expire": {
          "description": "Specifies how many seconds your notification will continue to be retried for (every retry seconds)",
          "type": "number",
          "default": 30
        },
        "additionalFields": {
          "description": "Your user's device name to send the message directly to that device, rather than all of the user's devices (multiple devices may be separated by a comma)",
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
      "name": "pushoverApi",
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
