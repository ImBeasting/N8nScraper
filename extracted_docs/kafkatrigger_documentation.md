---
title: "Node: Kafka Trigger"
slug: "node-kafkatrigger"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Consume messages from a Kafka topic"
node_type: "trigger"
group: "['trigger']"
---

# Node: Kafka Trigger

**Purpose.** Consume messages from a Kafka topic


---

## Node Details

- **Icon:** `{'light': 'file:kafka.svg', 'dark': 'file:kafka.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **kafka**: N/A


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
| `kafka` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Topic | `topic` | string |  | ✓ | Name of the queue of topic to consume from | e.g. topic-name |  |
| Group ID | `groupId` | string |  | ✓ | ID of the consumer group | e.g. n8n-kafka |  |
| Use Schema Registry | `useSchemaRegistry` | boolean | False | ✗ | Whether to use Confluent Schema Registry |  |
| Schema Registry URL | `schemaRegistryUrl` | string |  | ✓ | URL of the schema registry | e.g. https://schema-registry-domain:8081 | url |
| Options | `options` | collection | {} | ✗ | Whether to allow sending message to a previously non exisiting topic | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Allow Topic Creation | `allowAutoTopicCreation` | boolean | False | Whether to allow sending message to a previously non exisiting topic |
| Auto Commit Threshold | `autoCommitThreshold` | number | 0 | The consumer will commit offsets after resolving a given number of messages |
| Auto Commit Interval | `autoCommitInterval` | number | 0 | The consumer will commit offsets after a given period, for example, five seconds |
| Heartbeat Interval | `heartbeatInterval` | number | 3000 | Heartbeats are used to ensure that the consumer's session stays active |
| Max Number of Requests | `maxInFlightRequests` | number | 1 | The maximum number of unacknowledged requests the client will send on a single connection |
| Read Messages From Beginning | `fromBeginning` | boolean | True | Whether to read message from beginning |
| JSON Parse Message | `jsonParseMessage` | boolean | False | Whether to try to parse the message to an object |
| Parallel Processing | `parallelProcessing` | boolean | True | Whether to process messages in parallel or by keeping the message in order |
| Only Message | `onlyMessage` | boolean | False | Whether to return only the message property |
| Return Headers | `returnHeaders` | boolean | False | Whether to return the headers received from Kafka |
| Session Timeout | `sessionTimeout` | number | 30000 | The time to await a response in ms |

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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: kafkaTrigger
displayName: Kafka Trigger
description: Consume messages from a Kafka topic
version:
- '1'
- '1.1'
nodeType: trigger
group:
- trigger
credentials:
- name: kafka
  required: true
params:
- id: topic
  name: Topic
  type: string
  default: ''
  required: true
  description: Name of the queue of topic to consume from
  placeholder: topic-name
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Topic
    name: topic
- id: groupId
  name: Group ID
  type: string
  default: ''
  required: true
  description: ID of the consumer group
  placeholder: n8n-kafka
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Group ID
    name: groupId
- id: useSchemaRegistry
  name: Use Schema Registry
  type: boolean
  default: false
  required: false
  description: Whether to use Confluent Schema Registry
  typeInfo:
    type: boolean
    displayName: Use Schema Registry
    name: useSchemaRegistry
- id: schemaRegistryUrl
  name: Schema Registry URL
  type: string
  default: ''
  required: true
  description: URL of the schema registry
  placeholder: https://schema-registry-domain:8081
  validation:
    required: true
    format: url
    displayOptions:
      show:
        useSchemaRegistry:
        - true
  typeInfo:
    type: string
    displayName: Schema Registry URL
    name: schemaRegistryUrl
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to allow sending message to a previously non exisiting topic
  hint: Value in milliseconds
  placeholder: Add option
  validation:
    displayOptions:
      hide: {}
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Allow Topic Creation
      name: allowAutoTopicCreation
      type: boolean
      description: Whether to allow sending message to a previously non exisiting
        topic
      default: false
    - displayName: Auto Commit Threshold
      name: autoCommitThreshold
      type: number
      description: The consumer will commit offsets after resolving a given number
        of messages
      default: 0
    - displayName: Auto Commit Interval
      name: autoCommitInterval
      type: number
      description: The consumer will commit offsets after a given period, for example,
        five seconds
      hint: Value in milliseconds
      default: 0
    - displayName: Heartbeat Interval
      name: heartbeatInterval
      type: number
      description: Heartbeats are used to ensure that the consumer's session stays
        active
      hint: The value must be set lower than Session Timeout
      default: 3000
    - displayName: Max Number of Requests
      name: maxInFlightRequests
      type: number
      description: The maximum number of unacknowledged requests the client will send
        on a single connection
      default: 1
    - displayName: Read Messages From Beginning
      name: fromBeginning
      type: boolean
      description: Whether to read message from beginning
      default: true
    - displayName: JSON Parse Message
      name: jsonParseMessage
      type: boolean
      description: Whether to try to parse the message to an object
      default: false
    - displayName: Parallel Processing
      name: parallelProcessing
      type: boolean
      description: Whether to process messages in parallel or by keeping the message
        in order
      default: true
      displayOptions:
        hide: {}
    - displayName: Only Message
      name: onlyMessage
      type: boolean
      description: Whether to return only the message property
      default: false
      displayOptions:
        show:
          jsonParseMessage:
          - true
    - displayName: Return Headers
      name: returnHeaders
      type: boolean
      description: Whether to return the headers received from Kafka
      default: false
    - displayName: Session Timeout
      name: sessionTimeout
      type: number
      description: The time to await a response in ms
      hint: Value in milliseconds
      default: 30000
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: topic
    text: topic-name
  - field: groupId
    text: n8n-kafka
  - field: schemaRegistryUrl
    text: https://schema-registry-domain:8081
  - field: options
    text: Add option
  hints:
  - field: options
    text: Value in milliseconds
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
  "$id": "https://n8n.io/schemas/nodes/kafkaTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Kafka Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "topic": {
          "description": "Name of the queue of topic to consume from",
          "type": "string",
          "default": "",
          "examples": [
            "topic-name"
          ]
        },
        "groupId": {
          "description": "ID of the consumer group",
          "type": "string",
          "default": "",
          "examples": [
            "n8n-kafka"
          ]
        },
        "useSchemaRegistry": {
          "description": "Whether to use Confluent Schema Registry",
          "type": "boolean",
          "default": false
        },
        "schemaRegistryUrl": {
          "description": "URL of the schema registry",
          "type": "string",
          "default": "",
          "format": "url",
          "examples": [
            "https://schema-registry-domain:8081"
          ]
        },
        "options": {
          "description": "Whether to allow sending message to a previously non exisiting topic",
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
    "version": [
      "1",
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "kafka",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
