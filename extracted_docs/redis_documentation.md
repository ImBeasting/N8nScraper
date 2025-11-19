---
title: "Node: Redis"
slug: "node-redis"
version: "1"
updated: "2025-11-13"
summary: "Get, send and update data in Redis"
node_type: "regular"
group: "['input']"
---

# Node: Redis

**Purpose.** Get, send and update data in Redis


---

## Node Details

- **Icon:** `file:redis.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **redis**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `redis` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a key from Redis |
| Get | `get` | Get the value of a key from Redis |
| Increment | `incr` | Atomically increments a key by 1. Creates the key if it does not exist. |
| Info | `info` | Returns generic information about the Redis instance |
| Keys | `keys` | Returns all the keys matching a pattern |
| Pop | `pop` | Pop data from a redis list |
| Publish | `publish` | Publish message to redis channel |
| Push | `push` | Push data to a redis list |
| Set | `set` | Set the value of a key in redis |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | info | ✗ | Delete a key from Redis |  |

**Operation options:**

* **Delete** (`delete`) - Delete a key from Redis
* **Get** (`get`) - Get the value of a key from Redis
* **Increment** (`incr`) - Atomically increments a key by 1. Creates the key if it does not exist.
* **Info** (`info`) - Returns generic information about the Redis instance
* **Keys** (`keys`) - Returns all the keys matching a pattern
* **Pop** (`pop`) - Pop data from a redis list
* **Publish** (`publish`) - Publish message to redis channel
* **Push** (`push`) - Push data to a redis list
* **Set** (`set`) - Set the value of a key in redis

---

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Key | `key` | string |  | ✓ | Name of the key to delete from Redis |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `propertyName` | string | propertyName | ✓ | Name of the property to write received data to. Supports dot-notation. Example: "data.person[0].name". |  |
| Key | `key` | string |  | ✓ | Name of the key to get from Redis |  |
| Key Type | `keyType` | options | automatic | ✗ | Requests the type before requesting the data (slower) |  |

**Key Type options:**

* **Automatic** (`automatic`) - Requests the type before requesting the data (slower)
* **Hash** (`hash`) - Data in key is of type 'hash'
* **List** (`list`) - Data in key is of type 'lists'
* **Sets** (`sets`) - Data in key is of type 'sets'
* **String** (`string`) - Data in key is of type 'string'

| Options | `options` | collection | {} | ✗ | <p>By default, dot-notation is used in property names. This means that "a.b" will set the property "b" underneath "a" so { "a": { "b": value} }.<p></p>If that is not intended this can be deactivated, it will then set { "a.b": value } instead.</p>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Dot Notation | `dotNotation` | boolean | True | <p>By default, dot-notation is used in property names. This means that "a.b" will set the property "b" underneath "a" so { "a": { "b": value} }.<p></p>If that is not intended this can be deactivated, it will then set { "a.b": value } instead.</p>. |

</details>


### Increment parameters (`incr`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Key | `key` | string |  | ✓ | Name of the key to increment |  |
| Expire | `expire` | boolean | False | ✗ | Whether to set a timeout on key |  |
| TTL | `ttl` | number | 60 | ✗ | Number of seconds before key expiration | min:1, max:∞ |

### Keys parameters (`keys`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Key Pattern | `keyPattern` | string |  | ✓ | The key pattern for the keys to return |  |
| Get Values | `getValues` | boolean | True | ✗ | Whether to get the value of matching keys |  |

### Pop parameters (`pop`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List | `list` | string |  | ✓ | Name of the list in Redis |  |
| Tail | `tail` | boolean | False | ✗ | Whether to push or pop data from the end of the list |  |
| Name | `propertyName` | string | propertyName | ✗ | Optional name of the property to write received data to. Supports dot-notation. Example: "data.person[0].name". |  |
| Options | `options` | collection | {} | ✗ | <p>By default, dot-notation is used in property names. This means that "a.b" will set the property "b" underneath "a" so { "a": { "b": value} }.<p></p>If that is not intended this can be deactivated, it will then set { "a.b": value } instead.</p>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Dot Notation | `dotNotation` | boolean | True | <p>By default, dot-notation is used in property names. This means that "a.b" will set the property "b" underneath "a" so { "a": { "b": value} }.<p></p>If that is not intended this can be deactivated, it will then set { "a.b": value } instead.</p>. |

</details>


### Publish parameters (`publish`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channel` | string |  | ✓ | Channel name |  |
| Data | `messageData` | string |  | ✓ | Data to publish |  |

### Push parameters (`push`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List | `list` | string |  | ✓ | Name of the list in Redis |  |
| Data | `messageData` | string |  | ✓ | Data to push |  |
| Tail | `tail` | boolean | False | ✗ | Whether to push or pop data from the end of the list |  |

### Set parameters (`set`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Key | `key` | string |  | ✓ | Name of the key to set in Redis |  |
| Value | `value` | string |  | ✗ | The value to write in Redis |  |
| Key Type | `keyType` | options | automatic | ✗ | Tries to figure out the type automatically depending on the data |  |

**Key Type options:**

* **Automatic** (`automatic`) - Tries to figure out the type automatically depending on the data
* **Hash** (`hash`) - Data in key is of type 'hash'
* **List** (`list`) - Data in key is of type 'lists'
* **Sets** (`sets`) - Data in key is of type 'sets'
* **String** (`string`) - Data in key is of type 'string'

| Expire | `expire` | boolean | False | ✗ | Whether to set a timeout on key |  |
| TTL | `ttl` | number | 60 | ✗ | Number of seconds before key expiration | min:1, max:∞ |

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
* Categories: Development, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: redis
displayName: Redis
description: Get, send and update data in Redis
version: '1'
nodeType: regular
group:
- input
credentials:
- name: redis
  required: true
operations:
- id: delete
  name: Delete
  description: Delete a key from Redis
  params:
  - id: key
    name: Key
    type: string
    default: ''
    required: true
    description: Name of the key to delete from Redis
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - set
    typeInfo: &id002
      type: string
      displayName: Key
      name: key
- id: get
  name: Get
  description: Get the value of a key from Redis
  params:
  - id: propertyName
    name: Name
    type: string
    default: propertyName
    required: true
    description: 'Name of the property to write received data to. Supports dot-notation.
      Example: "data.person[0].name".'
    validation: &id003
      displayOptions:
        show:
          operation:
          - pop
    typeInfo: &id004
      type: string
      displayName: Name
      name: propertyName
  - id: key
    name: Key
    type: string
    default: ''
    required: true
    description: Name of the key to get from Redis
    validation: *id001
    typeInfo: *id002
  - id: keyType
    name: Key Type
    type: options
    default: automatic
    required: false
    description: Requests the type before requesting the data (slower)
    validation: &id011
      displayOptions:
        show:
          operation:
          - set
    typeInfo: &id012
      type: options
      displayName: Key Type
      name: keyType
      possibleValues:
      - value: automatic
        name: Automatic
        description: Tries to figure out the type automatically depending on the data
      - value: hash
        name: Hash
        description: Data in key is of type 'hash'
      - value: list
        name: List
        description: Data in key is of type 'lists'
      - value: sets
        name: Sets
        description: Data in key is of type 'sets'
      - value: string
        name: String
        description: Data in key is of type 'string'
- id: incr
  name: Increment
  description: Atomically increments a key by 1. Creates the key if it does not exist.
  params:
  - id: key
    name: Key
    type: string
    default: ''
    required: true
    description: Name of the key to increment
    validation: *id001
    typeInfo: *id002
  - id: expire
    name: Expire
    type: boolean
    default: false
    required: false
    description: Whether to set a timeout on key
    validation: &id013
      displayOptions:
        show:
          operation:
          - set
    typeInfo: &id014
      type: boolean
      displayName: Expire
      name: expire
  - id: ttl
    name: TTL
    type: number
    default: 60
    required: false
    description: Number of seconds before key expiration
    validation: &id015
      displayOptions:
        show:
          operation:
          - set
          expire:
          - true
    typeInfo: &id016
      type: number
      displayName: TTL
      name: ttl
      typeOptions:
        minValue: 1
- id: info
  name: Info
  description: Returns generic information about the Redis instance
- id: keys
  name: Keys
  description: Returns all the keys matching a pattern
  params:
  - id: keyPattern
    name: Key Pattern
    type: string
    default: ''
    required: true
    description: The key pattern for the keys to return
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - keys
    typeInfo:
      type: string
      displayName: Key Pattern
      name: keyPattern
  - id: getValues
    name: Get Values
    type: boolean
    default: true
    required: false
    description: Whether to get the value of matching keys
    validation:
      displayOptions:
        show:
          operation:
          - keys
    typeInfo:
      type: boolean
      displayName: Get Values
      name: getValues
- id: pop
  name: Pop
  description: Pop data from a redis list
  params:
  - id: list
    name: List
    type: string
    default: ''
    required: true
    description: Name of the list in Redis
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - push
          - pop
    typeInfo: &id006
      type: string
      displayName: List
      name: list
  - id: tail
    name: Tail
    type: boolean
    default: false
    required: false
    description: Whether to push or pop data from the end of the list
    validation: &id009
      displayOptions:
        show:
          operation:
          - push
          - pop
    typeInfo: &id010
      type: boolean
      displayName: Tail
      name: tail
  - id: propertyName
    name: Name
    type: string
    default: propertyName
    required: false
    description: 'Optional name of the property to write received data to. Supports
      dot-notation. Example: "data.person[0].name".'
    validation: *id003
    typeInfo: *id004
- id: publish
  name: Publish
  description: Publish message to redis channel
  params:
  - id: channel
    name: Channel
    type: string
    default: ''
    required: true
    description: Channel name
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - publish
    typeInfo:
      type: string
      displayName: Channel
      name: channel
  - id: messageData
    name: Data
    type: string
    default: ''
    required: true
    description: Data to publish
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - push
    typeInfo: &id008
      type: string
      displayName: Data
      name: messageData
- id: push
  name: Push
  description: Push data to a redis list
  params:
  - id: list
    name: List
    type: string
    default: ''
    required: true
    description: Name of the list in Redis
    validation: *id005
    typeInfo: *id006
  - id: messageData
    name: Data
    type: string
    default: ''
    required: true
    description: Data to push
    validation: *id007
    typeInfo: *id008
  - id: tail
    name: Tail
    type: boolean
    default: false
    required: false
    description: Whether to push or pop data from the end of the list
    validation: *id009
    typeInfo: *id010
- id: set
  name: Set
  description: Set the value of a key in redis
  params:
  - id: key
    name: Key
    type: string
    default: ''
    required: true
    description: Name of the key to set in Redis
    validation: *id001
    typeInfo: *id002
  - id: value
    name: Value
    type: string
    default: ''
    required: false
    description: The value to write in Redis
    validation:
      displayOptions:
        show:
          operation:
          - set
    typeInfo:
      type: string
      displayName: Value
      name: value
  - id: keyType
    name: Key Type
    type: options
    default: automatic
    required: false
    description: Tries to figure out the type automatically depending on the data
    validation: *id011
    typeInfo: *id012
  - id: expire
    name: Expire
    type: boolean
    default: false
    required: false
    description: Whether to set a timeout on key
    validation: *id013
    typeInfo: *id014
  - id: ttl
    name: TTL
    type: number
    default: 60
    required: false
    description: Number of seconds before key expiration
    validation: *id015
    typeInfo: *id016
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/redis.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Redis Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "delete",
        "get",
        "incr",
        "info",
        "keys",
        "pop",
        "publish",
        "push",
        "set"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Delete a key from Redis",
          "type": "string",
          "enum": [
            "delete",
            "get",
            "incr",
            "info",
            "keys",
            "pop",
            "publish",
            "push",
            "set"
          ],
          "default": "info"
        },
        "key": {
          "description": "Name of the key to set in Redis",
          "type": "string",
          "default": ""
        },
        "propertyName": {
          "description": "Optional name of the property to write received data to. Supports dot-notation. Example: \"data.person[0].name\".",
          "type": "string",
          "default": "propertyName"
        },
        "keyType": {
          "description": "Tries to figure out the type automatically depending on the data",
          "type": "string",
          "enum": [
            "automatic",
            "hash",
            "list",
            "sets",
            "string"
          ],
          "default": "automatic"
        },
        "options": {
          "description": "<p>By default, dot-notation is used in property names. This means that \"a.b\" will set the property \"b\" underneath \"a\" so { \"a\": { \"b\": value} }.<p></p>If that is not intended this can be deactivated, it will then set { \"a.b\": value } instead.</p>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "expire": {
          "description": "Whether to set a timeout on key",
          "type": "boolean",
          "default": false
        },
        "ttl": {
          "description": "Number of seconds before key expiration",
          "type": "number",
          "default": 60
        },
        "keyPattern": {
          "description": "The key pattern for the keys to return",
          "type": "string",
          "default": ""
        },
        "getValues": {
          "description": "Whether to get the value of matching keys",
          "type": "boolean",
          "default": true
        },
        "value": {
          "description": "The value to write in Redis",
          "type": "string",
          "default": ""
        },
        "valueIsJSON": {
          "description": "Whether the value is JSON or key value pairs",
          "type": "boolean",
          "default": true
        },
        "channel": {
          "description": "Channel name",
          "type": "string",
          "default": ""
        },
        "messageData": {
          "description": "Data to push",
          "type": "string",
          "default": ""
        },
        "list": {
          "description": "Name of the list in Redis",
          "type": "string",
          "default": ""
        },
        "tail": {
          "description": "Whether to push or pop data from the end of the list",
          "type": "boolean",
          "default": false
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
      "name": "redis",
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
