---
title: "Node: AMQP Sender"
slug: "node-amqp"
version: "1"
updated: "2025-11-13"
summary: "Sends a raw-message via AMQP 1.0, executed once per item"
node_type: "regular"
group: "['transform']"
---

# Node: AMQP Sender

**Purpose.** Sends a raw-message via AMQP 1.0, executed once per item


---

## Node Details

- **Icon:** `file:amqp.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **amqp**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `amqp` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Queue / Topic | `sink` | string |  | ✗ | Name of the queue of topic to publish to | e.g. e.g. topic://sourcename.something |  |
| Headers | `headerParametersJson` | json |  | ✗ | Header parameters as JSON (flat object). Sent as application_properties in amqp-message meta info. |  |
| Options | `options` | collection | {} | ✗ | Will be used to pass to the RHEA Backend as container_id | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Container ID | `containerId` | string |  | Will be used to pass to the RHEA Backend as container_id |
| Data as Object | `dataAsObject` | boolean | False | Whether to send the data as an object |
| Reconnect | `reconnect` | boolean | True | Whether to automatically reconnect if disconnected |
| Reconnect Limit | `reconnectLimit` | number | 50 | Maximum number of reconnect attempts |
| Send Property | `sendOnlyProperty` | string |  | The only property to send. If empty the whole item will be sent. |

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
* Categories: Development, Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: amqp
displayName: AMQP Sender
description: Sends a raw-message via AMQP 1.0, executed once per item
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: amqp
  required: true
params:
- id: sink
  name: Queue / Topic
  type: string
  default: ''
  required: false
  description: Name of the queue of topic to publish to
  placeholder: e.g. topic://sourcename.something
  typeInfo:
    type: string
    displayName: Queue / Topic
    name: sink
- id: headerParametersJson
  name: Headers
  type: json
  default: ''
  required: false
  description: Header parameters as JSON (flat object). Sent as application_properties
    in amqp-message meta info.
  typeInfo:
    type: json
    displayName: Headers
    name: headerParametersJson
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Will be used to pass to the RHEA Backend as container_id
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Container ID
      name: containerId
      type: string
      description: Will be used to pass to the RHEA Backend as container_id
      default: ''
    - displayName: Data as Object
      name: dataAsObject
      type: boolean
      description: Whether to send the data as an object
      default: false
    - displayName: Reconnect
      name: reconnect
      type: boolean
      description: Whether to automatically reconnect if disconnected
      default: true
    - displayName: Reconnect Limit
      name: reconnectLimit
      type: number
      description: Maximum number of reconnect attempts
      default: 50
    - displayName: Send Property
      name: sendOnlyProperty
      type: string
      description: The only property to send. If empty the whole item will be sent.
      default: ''
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: sink
    text: e.g. topic://sourcename.something
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
  "$id": "https://n8n.io/schemas/nodes/amqp.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AMQP Sender Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "sink": {
          "description": "Name of the queue of topic to publish to",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. topic://sourcename.something"
          ]
        },
        "headerParametersJson": {
          "description": "Header parameters as JSON (flat object). Sent as application_properties in amqp-message meta info.",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Will be used to pass to the RHEA Backend as container_id",
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
  },
  "credentials": [
    {
      "name": "amqp",
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
