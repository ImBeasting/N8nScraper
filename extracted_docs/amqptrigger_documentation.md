---
title: "Node: AMQP Trigger"
slug: "node-amqptrigger"
version: "1"
updated: "2026-01-08"
summary: "Listens to AMQP 1.0 Messages"
node_type: "trigger"
group: "['trigger']"
---

# Node: AMQP Trigger

**Purpose.** Listens to AMQP 1.0 Messages


---

## Node Details

- **Icon:** `file:amqp.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **amqp**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

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
| Queue / Topic | `sink` | string |  | ✗ | Name of the queue of topic to listen to | e.g. topic://sourcename.something |  |
| Clientname | `clientname` | string |  | ✗ | Leave empty for non-durable topic subscriptions or queues | e.g. e.g. n8n |  |
| Subscription | `subscription` | string |  | ✗ | Leave empty for non-durable topic subscriptions or queues | e.g. e.g. order-worker |  |
| Options | `options` | collection | {} | ✗ | Will be used to pass to the RHEA Backend as container_id | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Container ID | `containerId` | string |  | Will be used to pass to the RHEA Backend as container_id |
| Convert Body To String | `jsonConvertByteArrayToString` | boolean | False | Whether to convert JSON Body content (["body"]["content"]) from Byte Array to string. Needed for Azure Service Bus. |
| JSON Parse Body | `jsonParseBody` | boolean | False | Whether to parse the body to an object |
| Messages per Cicle | `pullMessagesNumber` | number | 100 | Number of messages to pull from the bus for every cicle |
| Only Body | `onlyBody` | boolean | False | Whether to return only the body property |
| Parallel Processing | `parallelProcessing` | boolean | True | Whether to process messages in parallel |
| Reconnect | `reconnect` | boolean | True | Whether to automatically reconnect if disconnected |
| Reconnect Limit | `reconnectLimit` | number | 50 | Maximum number of reconnect attempts |
| Sleep Time | `sleepTime` | number | 10 | Milliseconds to sleep after every cicle |

</details>


---

## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |

---

## Notes & Caveats

* This node is part of n8n-nodes-base
* Categories: Development, Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: amqpTrigger
displayName: AMQP Trigger
description: Listens to AMQP 1.0 Messages
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: amqp
  required: true
params:
- id: sink
  name: Queue / Topic
  type: string
  default: ''
  required: false
  description: Name of the queue of topic to listen to
  placeholder: topic://sourcename.something
  typeInfo:
    type: string
    displayName: Queue / Topic
    name: sink
- id: clientname
  name: Clientname
  type: string
  default: ''
  required: false
  description: Leave empty for non-durable topic subscriptions or queues
  hint: for durable/persistent topic subscriptions
  placeholder: e.g. n8n
  typeInfo:
    type: string
    displayName: Clientname
    name: clientname
- id: subscription
  name: Subscription
  type: string
  default: ''
  required: false
  description: Leave empty for non-durable topic subscriptions or queues
  hint: for durable/persistent topic subscriptions
  placeholder: e.g. order-worker
  typeInfo:
    type: string
    displayName: Subscription
    name: subscription
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
    - displayName: Convert Body To String
      name: jsonConvertByteArrayToString
      type: boolean
      description: Whether to convert JSON Body content (["body"]["content"]) from
        Byte Array to string. Needed for Azure Service Bus.
      default: false
    - displayName: JSON Parse Body
      name: jsonParseBody
      type: boolean
      description: Whether to parse the body to an object
      default: false
    - displayName: Messages per Cicle
      name: pullMessagesNumber
      type: number
      description: Number of messages to pull from the bus for every cicle
      default: 100
    - displayName: Only Body
      name: onlyBody
      type: boolean
      description: Whether to return only the body property
      default: false
    - displayName: Parallel Processing
      name: parallelProcessing
      type: boolean
      description: Whether to process messages in parallel
      default: true
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
    - displayName: Sleep Time
      name: sleepTime
      type: number
      description: Milliseconds to sleep after every cicle
      default: 10
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: sink
    text: topic://sourcename.something
  - field: clientname
    text: e.g. n8n
  - field: subscription
    text: e.g. order-worker
  - field: options
    text: Add option
  hints:
  - field: clientname
    text: for durable/persistent topic subscriptions
  - field: subscription
    text: for durable/persistent topic subscriptions
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/amqpTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AMQP Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "sink": {
          "description": "Name of the queue of topic to listen to",
          "type": "string",
          "default": "",
          "examples": [
            "topic://sourcename.something"
          ]
        },
        "clientname": {
          "description": "Leave empty for non-durable topic subscriptions or queues",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. n8n"
          ]
        },
        "subscription": {
          "description": "Leave empty for non-durable topic subscriptions or queues",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. order-worker"
          ]
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
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
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
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
