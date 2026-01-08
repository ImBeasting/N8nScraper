---
title: "Node: RocketChat"
slug: "node-rocketchat"
version: "1"
updated: "2026-01-08"
summary: "Consume RocketChat API"
node_type: "regular"
group: "['output']"
---

# Node: RocketChat

**Purpose.** Consume RocketChat API
**Subtitle.** ={{$parameter["resource"] + ": " + $parameter["operation"]}}


---

## Node Details

- **Icon:** `file:rocketchat.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **rocketchatApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `rocketchatApi` | ✓ | - |

---

## Operations

### Chat Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Post Message | `postMessage` | Post a message to a channel or a direct message |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | chat | ✗ | Resource to operate on |  |

**Resource options:**

* **Chat** (`chat`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | postMessage | ✗ | Post a message to a channel or a direct message |  |

**Operation options:**

* **Post Message** (`postMessage`) - Post a message to a channel or a direct message

---

### Post Message parameters (`postMessage`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channel` | string |  | ✓ | The channel name with the prefix in front of it |  |
| Text | `text` | string |  | ✗ | The text of the message to send, is optional because of attachments |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | This will cause the message’s name to appear as the given alias, but your username will still display | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Alias | `alias` | string |  | This will cause the message’s name to appear as the given alias, but your username will still display |
| Avatar | `avatar` | string |  | If provided, this will make the avatar use the provided image URL |
| Emoji | `emoji` | string |  | This will cause the message’s name to appear as the given alias, but your username will still display |

</details>

| Attachments | `attachments` | collection | {} | ✗ | The color you want the order on the left side to be, any value background-css supports | e.g. Add Attachment Item |  |

<details>
<summary><strong>Attachments sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Color | `color` | color | #ff0000 | The color you want the order on the left side to be, any value background-css supports |
| Text | `text` | string |  | The text to display for this attachment, it is different than the message’s text |
| Timestamp | `ts` | dateTime |  | Displays the time next to the text portion |
| Thumb URL | `thumbUrl` | string |  | An image that displays to the left of the text, looks better when this is relatively small |
| Message Link | `messageLink` | string |  | Only applicable if the timestamp is provided, as it makes the time clickable to this link |
| Collapsed | `collapsed` | boolean | False | Causes the image, audio, and video sections to be hiding when collapsed is true |
| Author Name | `authorName` | string |  | Name of the author |
| Author Link | `authorLink` | string |  | Providing this makes the author name clickable and points to this link |
| Author Icon | `authorIcon` | string |  | Displays a tiny icon to the left of the Author’s name |
| Title | `title` | string |  | Title to display for this attachment, displays under the author |
| Title Link | `titleLink` | string |  | Providing this makes the title clickable, pointing to this link |
| Title Link Download | `titleLinkDownload` | boolean | False | When this is true, a download icon appears and clicking this saves the link to file |
| Image URL | `imageUrl` | string |  | The image to display, will be “big” and easy to see |
| Audio URL | `audioUrl` | string |  | Audio file to play, only supports what html audio does |
| Video URL | `videoUrl` | string |  | Video file to play, only supports what html video does |
| Fields | `fields` | fixedCollection | {} | Whether this field should be a short field |

</details>

| Attachments | `attachmentsJson` | json |  | ✗ |  |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["resource"] + ": " + $parameter["operation"]}}`

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
node: rocketchat
displayName: RocketChat
description: Consume RocketChat API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: rocketchatApi
  required: true
operations:
- id: postMessage
  name: Post Message
  description: Post a message to a channel or a direct message
  params:
  - id: channel
    name: Channel
    type: string
    default: ''
    required: true
    description: The channel name with the prefix in front of it
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - chat
          operation:
          - postMessage
    typeInfo:
      type: string
      displayName: Channel
      name: channel
  - id: text
    name: Text
    type: string
    default: ''
    required: false
    description: The text of the message to send, is optional because of attachments
    validation:
      displayOptions:
        show:
          resource:
          - chat
          operation:
          - postMessage
    typeInfo:
      type: string
      displayName: Text
      name: text
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - chat
          operation:
          - postMessage
    typeInfo:
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: attachmentsJson
    name: Attachments
    type: json
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - chat
          operation:
          - postMessage
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Attachments
      name: attachmentsJson
      typeOptions:
        alwaysOpenEditWindow: true
common_expressions:
- '={{$parameter["resource"] + ": " + $parameter["operation"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  - field: attachments
    text: Add Attachment Item
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
  "$id": "https://n8n.io/schemas/nodes/rocketchat.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "RocketChat Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "postMessage"
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
            "chat"
          ],
          "default": "chat"
        },
        "operation": {
          "description": "Post a message to a channel or a direct message",
          "type": "string",
          "enum": [
            "postMessage"
          ],
          "default": "postMessage"
        },
        "channel": {
          "description": "The channel name with the prefix in front of it",
          "type": "string",
          "default": ""
        },
        "text": {
          "description": "The text of the message to send, is optional because of attachments",
          "type": "string",
          "default": ""
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "options": {
          "description": "This will cause the message\u2019s name to appear as the given alias, but your username will still display",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "attachments": {
          "description": "The color you want the order on the left side to be, any value background-css supports",
          "type": "string",
          "default": {},
          "examples": [
            "Add Attachment Item"
          ]
        },
        "attachmentsJson": {
          "description": "",
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
      "name": "rocketchatApi",
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
