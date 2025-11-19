---
title: "Node: AWS SNS"
slug: "node-awssns"
version: "1"
updated: "2025-11-13"
summary: "Sends data to AWS SNS"
node_type: "regular"
group: "['output']"
---

# Node: AWS SNS

**Purpose.** Sends data to AWS SNS
**Subtitle.** ={{$parameter["topic"]}}


---

## Node Details

- **Icon:** `file:sns.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **aws**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `aws` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a topic |
| Delete | `delete` | Delete a topic |
| Publish | `publish` | Publish a message to a topic |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | publish | ✗ | Create a topic |  |

**Operation options:**

* **Create** (`create`) - Create a topic
* **Delete** (`delete`) - Delete a topic
* **Publish** (`publish`) - Publish a message to a topic

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | The display name to use for a topic with SMS subscriptions | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Display Name | `displayName` | string |  | The display name to use for a topic with SMS subscriptions |
| Fifo Topic | `fifoTopic` | boolean | False | Whether the topic you want to create is a FIFO (first-in-first-out) topic |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Topic | `topic` | resourceLocator |  | ✓ | e.g. Select a topic... |  |

### Publish parameters (`publish`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Topic | `topic` | resourceLocator |  | ✓ | e.g. Select a topic... |  |
| Subject | `subject` | string |  | ✓ | Subject when the message is delivered to email endpoints |  |
| Message | `message` | string |  | ✓ | The message you want to send |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["topic"]}}`

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
node: awsSns
displayName: AWS SNS
description: Sends data to AWS SNS
version: '1'
nodeType: regular
group:
- output
credentials:
- name: aws
  required: true
operations:
- id: create
  name: Create
  description: Create a topic
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
- id: delete
  name: Delete
  description: Delete a topic
  params:
  - id: topic
    name: Topic
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select a topic...
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - publish
          - delete
    typeInfo: &id002
      type: resourceLocator
      displayName: Topic
      name: topic
- id: publish
  name: Publish
  description: Publish a message to a topic
  params:
  - id: topic
    name: Topic
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select a topic...
    validation: *id001
    typeInfo: *id002
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: Subject when the message is delivered to email endpoints
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - publish
    typeInfo:
      type: string
      displayName: Subject
      name: subject
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: The message you want to send
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - publish
    typeInfo:
      type: string
      displayName: Message
      name: message
common_expressions:
- ={{$parameter["topic"]}}
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
  - field: topic
    text: Select a topic...
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
  "$id": "https://n8n.io/schemas/nodes/awsSns.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AWS SNS Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "publish"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Create a topic",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "publish"
          ],
          "default": "publish"
        },
        "name": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "The display name to use for a topic with SMS subscriptions",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "topic": {
          "description": "",
          "type": "string",
          "examples": [
            "Select a topic..."
          ]
        },
        "subject": {
          "description": "Subject when the message is delivered to email endpoints",
          "type": "string",
          "default": ""
        },
        "message": {
          "description": "The message you want to send",
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
      "name": "aws",
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
