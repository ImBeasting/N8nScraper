---
title: "Node: RabbitMQ"
slug: "node-rabbitmq"
version: "['1', '1.1']"
updated: "2025-11-13"
summary: "Sends messages to a RabbitMQ topic"
node_type: "regular"
group: "['transform']"
---

# Node: RabbitMQ

**Purpose.** Sends messages to a RabbitMQ topic


---

## Node Details

- **Icon:** `file:rabbitmq.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **rabbitmq**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **deleteMessage** when operation=['deleteMessage']: Will delete an item from the queue triggered earlier in the workflow by a RabbitMQ Trigger node

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `rabbitmq` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | hidden | sendMessage | ✗ |  |  |
| Mode | `mode` | options | queue | ✗ | Publish data to queue |  |

**Mode options:**

* **Queue** (`queue`) - Publish data to queue
* **Exchange** (`exchange`) - Publish data to exchange

| Queue / Topic | `queue` | string |  | ✗ | Name of the queue to publish to | e.g. queue-name |  |
| Exchange | `exchange` | string |  | ✗ | Name of the exchange to publish to | e.g. exchange-name |  |
| Type | `exchangeType` | options | fanout | ✗ | Direct exchange type |  |

**Type options:**

* **Direct** (`direct`) - Direct exchange type
* **Topic** (`topic`) - Topic exchange type
* **Headers** (`headers`) - Headers exchange type
* **Fanout** (`fanout`) - Fanout exchange type

| Routing Key | `routingKey` | string |  | ✗ | The routing key for the message | e.g. routing-key |  |
| Send Input Data | `sendInputData` | boolean | True | ✗ | Whether to send the data the node receives as JSON |  |
| Message | `message` | string |  | ✗ | The message to be sent |  |
| Options | `options` | collection | {} | ✗ | An exchange to send messages to if this exchange can’t route them to any queues | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Alternate Exchange | `alternateExchange` | string |  | An exchange to send messages to if this exchange can’t route them to any queues |
| Arguments | `arguments` | fixedCollection | {} | Arguments to add, See <a href="https://amqp-node.github.io/amqplib/channel_api.html#channel_publish" target="_blank">here</a> for valid options |
| Auto Delete Queue | `autoDelete` | boolean | False | Whether the queue will be deleted when the number of consumers drops to zero |
| Durable | `durable` | boolean | True | Whether the queue will survive broker restarts |
| Exclusive | `exclusive` | boolean | False | Whether to scope the queue to the connection |
| Headers | `headers` | fixedCollection | {} | Headers to add |

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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: rabbitmq
displayName: RabbitMQ
description: Sends messages to a RabbitMQ topic
version:
- '1'
- '1.1'
nodeType: regular
group:
- transform
credentials:
- name: rabbitmq
  required: true
params:
- id: operation
  name: Operation
  type: hidden
  default: sendMessage
  required: false
  description: ''
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: hidden
    displayName: Operation
    name: operation
- id: mode
  name: Mode
  type: options
  default: queue
  required: false
  description: Publish data to queue
  validation:
    displayOptions:
      hide:
        operation:
        - deleteMessage
  typeInfo:
    type: options
    displayName: Mode
    name: mode
    possibleValues:
    - value: queue
      name: Queue
      description: Publish data to queue
    - value: exchange
      name: Exchange
      description: Publish data to exchange
- id: queue
  name: Queue / Topic
  type: string
  default: ''
  required: false
  description: Name of the queue to publish to
  placeholder: queue-name
  validation:
    displayOptions:
      show:
        mode:
        - queue
      hide:
        operation:
        - deleteMessage
  typeInfo:
    type: string
    displayName: Queue / Topic
    name: queue
- id: exchange
  name: Exchange
  type: string
  default: ''
  required: false
  description: Name of the exchange to publish to
  placeholder: exchange-name
  validation:
    displayOptions:
      show:
        mode:
        - exchange
  typeInfo:
    type: string
    displayName: Exchange
    name: exchange
- id: exchangeType
  name: Type
  type: options
  default: fanout
  required: false
  description: Direct exchange type
  validation:
    displayOptions:
      show:
        mode:
        - exchange
  typeInfo:
    type: options
    displayName: Type
    name: exchangeType
    possibleValues:
    - value: direct
      name: Direct
      description: Direct exchange type
    - value: topic
      name: Topic
      description: Topic exchange type
    - value: headers
      name: Headers
      description: Headers exchange type
    - value: fanout
      name: Fanout
      description: Fanout exchange type
- id: routingKey
  name: Routing Key
  type: string
  default: ''
  required: false
  description: The routing key for the message
  placeholder: routing-key
  validation:
    displayOptions:
      show:
        mode:
        - exchange
  typeInfo:
    type: string
    displayName: Routing Key
    name: routingKey
- id: sendInputData
  name: Send Input Data
  type: boolean
  default: true
  required: false
  description: Whether to send the data the node receives as JSON
  validation:
    displayOptions:
      show:
        operation:
        - sendMessage
  typeInfo:
    type: boolean
    displayName: Send Input Data
    name: sendInputData
- id: message
  name: Message
  type: string
  default: ''
  required: false
  description: The message to be sent
  validation:
    displayOptions:
      show:
        sendInputData:
        - false
  typeInfo:
    type: string
    displayName: Message
    name: message
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: An exchange to send messages to if this exchange can’t route them to
    any queues
  placeholder: Add option
  validation:
    displayOptions:
      show:
        operation:
        - sendMessage
  typeInfo:
    type: collection
    displayName: Options
    name: options
    typeOptions:
      multipleValues: true
    subProperties:
    - displayName: Alternate Exchange
      name: alternateExchange
      type: string
      description: An exchange to send messages to if this exchange can’t route them
        to any queues
      default: ''
      displayOptions:
        show: {}
    - displayName: Arguments
      name: arguments
      type: fixedCollection
      description: Arguments to add, See <a href="https://amqp-node.github.io/amqplib/channel_api.html#channel_publish"
        target="_blank">here</a> for valid options
      placeholder: Add Argument
      default: {}
      options:
      - name: argument
        displayName: Argument
        values:
        - displayName: Key
          name: key
          type: string
          default: ''
        - displayName: Value
          name: value
          type: string
          default: ''
      typeOptions:
        multipleValues: true
    - displayName: Auto Delete Queue
      name: autoDelete
      type: boolean
      description: Whether the queue will be deleted when the number of consumers
        drops to zero
      default: false
    - displayName: Durable
      name: durable
      type: boolean
      description: Whether the queue will survive broker restarts
      default: true
    - displayName: Exclusive
      name: exclusive
      type: boolean
      description: Whether to scope the queue to the connection
      default: false
      displayOptions:
        show: {}
    - displayName: Headers
      name: headers
      type: fixedCollection
      description: Headers to add
      placeholder: Add Header
      default: {}
      options:
      - name: header
        displayName: Header
        values:
        - displayName: Key
          name: key
          type: string
          default: ''
        - displayName: Value
          name: value
          type: string
          default: ''
      typeOptions:
        multipleValues: true
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: deleteMessage
    text: Will delete an item from the queue triggered earlier in the workflow by
      a RabbitMQ Trigger node
    conditions:
      show:
        operation:
        - deleteMessage
  tooltips: []
  placeholders:
  - field: queue
    text: queue-name
  - field: exchange
    text: exchange-name
  - field: routingKey
    text: routing-key
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
  "$id": "https://n8n.io/schemas/nodes/rabbitmq.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "RabbitMQ Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "",
          "type": "string",
          "default": "sendMessage"
        },
        "mode": {
          "description": "Publish data to queue",
          "type": "string",
          "enum": [
            "queue",
            "exchange"
          ],
          "default": "queue"
        },
        "queue": {
          "description": "Name of the queue to publish to",
          "type": "string",
          "default": "",
          "examples": [
            "queue-name"
          ]
        },
        "exchange": {
          "description": "Name of the exchange to publish to",
          "type": "string",
          "default": "",
          "examples": [
            "exchange-name"
          ]
        },
        "exchangeType": {
          "description": "Direct exchange type",
          "type": "string",
          "enum": [
            "direct",
            "topic",
            "headers",
            "fanout"
          ],
          "default": "fanout"
        },
        "routingKey": {
          "description": "The routing key for the message",
          "type": "string",
          "default": "",
          "examples": [
            "routing-key"
          ]
        },
        "sendInputData": {
          "description": "Whether to send the data the node receives as JSON",
          "type": "boolean",
          "default": true
        },
        "message": {
          "description": "The message to be sent",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "An exchange to send messages to if this exchange can\u2019t route them to any queues",
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
    "version": [
      "1",
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "rabbitmq",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
