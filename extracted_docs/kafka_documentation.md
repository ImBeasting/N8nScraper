---
title: "Node: Kafka"
slug: "node-kafka"
version: "1"
updated: "2026-01-08"
summary: "Sends messages to a Kafka topic"
node_type: "regular"
group: "['transform']"
---

# Node: Kafka

**Purpose.** Sends messages to a Kafka topic


---

## Node Details

- **Icon:** `{'light': 'file:kafka.svg', 'dark': 'file:kafka.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **kafka**: N/A


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
| Topic | `topic` | string |  | ✗ | Name of the queue of topic to publish to | e.g. topic-name |  |
| Send Input Data | `sendInputData` | boolean | True | ✗ | Whether to send the data the node receives as JSON to Kafka |  |
| Message | `message` | string |  | ✗ | The message to be sent |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Use Schema Registry | `useSchemaRegistry` | boolean | False | ✗ | Whether to use Confluent Schema Registry |  |
| Schema Registry URL | `schemaRegistryUrl` | string |  | ✓ | URL of the schema registry | e.g. https://schema-registry-domain:8081 | url |
| Use Key | `useKey` | boolean | False | ✗ | Whether to use a message key |  |
| Key | `key` | string |  | ✓ | The message key |  |
| Event Name | `eventName` | string |  | ✓ | Namespace and Name of Schema in Schema Registry (namespace.name) |  |
| Headers | `headersUi` | fixedCollection | {} | ✗ | e.g. Add Header |  |

<details>
<summary><strong>Headers sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Header | `headerValues` |  |  |  |

</details>

| Headers (JSON) | `headerParametersJson` | json |  | ✗ | Header parameters as JSON (flat object) |  |
| Options | `options` | collection | {} | ✗ | Whether or not producer must wait for acknowledgement from all replicas | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Acks | `acks` | boolean | False | Whether or not producer must wait for acknowledgement from all replicas |
| Compression | `compression` | boolean | False | Whether to send the data in a compressed format using the GZIP codec |
| Timeout | `timeout` | number | 30000 | The time to await a response in ms |

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
node: kafka
displayName: Kafka
description: Sends messages to a Kafka topic
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: kafka
  required: true
params:
- id: topic
  name: Topic
  type: string
  default: ''
  required: false
  description: Name of the queue of topic to publish to
  placeholder: topic-name
  typeInfo:
    type: string
    displayName: Topic
    name: topic
- id: sendInputData
  name: Send Input Data
  type: boolean
  default: true
  required: false
  description: Whether to send the data the node receives as JSON to Kafka
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
- id: jsonParameters
  name: JSON Parameters
  type: boolean
  default: false
  required: false
  description: ''
  typeInfo:
    type: boolean
    displayName: JSON Parameters
    name: jsonParameters
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
- id: useKey
  name: Use Key
  type: boolean
  default: false
  required: false
  description: Whether to use a message key
  typeInfo:
    type: boolean
    displayName: Use Key
    name: useKey
- id: key
  name: Key
  type: string
  default: ''
  required: true
  description: The message key
  validation:
    required: true
    displayOptions:
      show:
        useKey:
        - true
  typeInfo:
    type: string
    displayName: Key
    name: key
- id: eventName
  name: Event Name
  type: string
  default: ''
  required: true
  description: Namespace and Name of Schema in Schema Registry (namespace.name)
  validation:
    required: true
    displayOptions:
      show:
        useSchemaRegistry:
        - true
  typeInfo:
    type: string
    displayName: Event Name
    name: eventName
- id: headersUi
  name: Headers
  type: fixedCollection
  default: {}
  required: false
  description: ''
  placeholder: Add Header
  validation:
    displayOptions:
      show:
        jsonParameters:
        - false
  typeInfo:
    type: fixedCollection
    displayName: Headers
    name: headersUi
    typeOptions:
      multipleValues: true
    subProperties:
    - name: headerValues
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
- id: headerParametersJson
  name: Headers (JSON)
  type: json
  default: ''
  required: false
  description: Header parameters as JSON (flat object)
  validation:
    displayOptions:
      show:
        jsonParameters:
        - true
  typeInfo:
    type: json
    displayName: Headers (JSON)
    name: headerParametersJson
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether or not producer must wait for acknowledgement from all replicas
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Acks
      name: acks
      type: boolean
      description: Whether or not producer must wait for acknowledgement from all
        replicas
      default: false
    - displayName: Compression
      name: compression
      type: boolean
      description: Whether to send the data in a compressed format using the GZIP
        codec
      default: false
    - displayName: Timeout
      name: timeout
      type: number
      description: The time to await a response in ms
      default: 30000
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: topic
    text: topic-name
  - field: schemaRegistryUrl
    text: https://schema-registry-domain:8081
  - field: headersUi
    text: Add Header
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
  "$id": "https://n8n.io/schemas/nodes/kafka.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Kafka Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "topic": {
          "description": "Name of the queue of topic to publish to",
          "type": "string",
          "default": "",
          "examples": [
            "topic-name"
          ]
        },
        "sendInputData": {
          "description": "Whether to send the data the node receives as JSON to Kafka",
          "type": "boolean",
          "default": true
        },
        "message": {
          "description": "The message to be sent",
          "type": "string",
          "default": ""
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
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
        "useKey": {
          "description": "Whether to use a message key",
          "type": "boolean",
          "default": false
        },
        "key": {
          "description": "The message key",
          "type": "string",
          "default": ""
        },
        "eventName": {
          "description": "Namespace and Name of Schema in Schema Registry (namespace.name)",
          "type": "string",
          "default": ""
        },
        "headersUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Header"
          ]
        },
        "headerParametersJson": {
          "description": "Header parameters as JSON (flat object)",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Whether or not producer must wait for acknowledgement from all replicas",
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
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
