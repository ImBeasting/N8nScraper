---
title: "Node: Discord"
slug: "node-discord"
version: "1"
updated: "2026-01-08"
summary: "Sends data to Discord"
node_type: "regular"
group: "['output']"
---

# Node: Discord

**Purpose.** Sends data to Discord


---

## Node Details

- **Icon:** `file:discord.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **oldVersionNotice**: <strong>New node version available:</strong> get the latest version with added features from the nodes panel.

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Webhook URL | `webhookUri` | string |  | ✓ | e.g. https://discord.com/api/webhooks/ID/TOKEN |  |
| Content | `text` | string |  | ✗ | e.g. Hello World! | min:∞, max:2000 |
| Additional Fields | `options` | collection | {} | ✗ | Whether this message be sent as a Text To Speech message | e.g. Add option |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Allowed Mentions | `allowedMentions` | json |  |  |
| Attachments | `attachments` | json |  |  |
| Avatar URL | `avatarUrl` | string |  |  |
| Components | `components` | json |  |  |
| Embeds | `embeds` | json |  |  |
| Flags | `flags` | number |  |  |
| JSON Payload | `payloadJson` | json |  |  |
| Username | `username` | string |  |  |
| TTS | `tts` | boolean | False | Whether this message be sent as a Text To Speech message |

</details>


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
node: discord
displayName: Discord
description: Sends data to Discord
version: '1'
nodeType: regular
group:
- output
params:
- id: webhookUri
  name: Webhook URL
  type: string
  default: ''
  required: true
  description: ''
  placeholder: https://discord.com/api/webhooks/ID/TOKEN
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Webhook URL
    name: webhookUri
- id: text
  name: Content
  type: string
  default: ''
  required: false
  description: ''
  placeholder: Hello World!
  typeInfo:
    type: string
    displayName: Content
    name: text
    typeOptions:
      maxValue: 2000
- id: options
  name: Additional Fields
  type: collection
  default: {}
  required: false
  description: Whether this message be sent as a Text To Speech message
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Additional Fields
    name: options
    typeOptions:
      alwaysOpenEditWindow: true
    subProperties:
    - displayName: Allowed Mentions
      name: allowedMentions
      type: json
      default: ''
      typeOptions:
        alwaysOpenEditWindow: true
    - displayName: Attachments
      name: attachments
      type: json
      default: ''
      typeOptions:
        alwaysOpenEditWindow: true
    - displayName: Avatar URL
      name: avatarUrl
      type: string
      default: ''
    - displayName: Components
      name: components
      type: json
      default: ''
      typeOptions:
        alwaysOpenEditWindow: true
    - displayName: Embeds
      name: embeds
      type: json
      default: ''
      typeOptions:
        alwaysOpenEditWindow: true
    - displayName: Flags
      name: flags
      type: number
      default: ''
    - displayName: JSON Payload
      name: payloadJson
      type: json
      default: ''
      typeOptions:
        alwaysOpenEditWindow: true
    - displayName: Username
      name: username
      type: string
      placeholder: User
      default: ''
    - displayName: TTS
      name: tts
      type: boolean
      description: Whether this message be sent as a Text To Speech message
      default: false
ui_elements:
  notices:
  - name: oldVersionNotice
    text: <strong>New node version available:</strong> get the latest version with
      added features from the nodes panel.
    conditions: null
  tooltips: []
  placeholders:
  - field: webhookUri
    text: https://discord.com/api/webhooks/ID/TOKEN
  - field: text
    text: Hello World!
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/discord.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Discord Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "webhookUri": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "https://discord.com/api/webhooks/ID/TOKEN"
          ]
        },
        "text": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Hello World!"
          ]
        },
        "options": {
          "description": "Whether this message be sent as a Text To Speech message",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
