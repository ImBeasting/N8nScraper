---
title: "Node: DebugHelper"
slug: "node-debughelper"
version: "1"
updated: "2026-01-08"
summary: "Causes problems intentionally and generates useful data for debugging"
node_type: "regular"
group: "['output']"
---

# Node: DebugHelper

**Purpose.** Causes problems intentionally and generates useful data for debugging
**Subtitle.** ={{$parameter["category"]}}


---

## Node Details

- **Icon:** `{'light': 'file:DebugHelper.svg', 'dark': 'file:DebugHelper.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Category | `category` | options | throwError | ✗ | Does nothing |  |

**Category options:**

* **Do Nothing** (`doNothing`) - Does nothing
* **Throw Error** (`throwError`) - Throws an error with the specified type and message
* **Out Of Memory** (`oom`) - Generates a large amount of memory to cause an out of memory error
* **Generate Random Data** (`randomData`) - Generates random data sets

| Error Type | `throwErrorType` | options | NodeApiError | ✗ |  |  |

**Error Type options:**

* **NodeApiError** (`NodeApiError`)
* **NodeOperationError** (`NodeOperationError`)
* **Error** (`Error`)

| Error Message | `throwErrorMessage` | string | Node has thrown an error | ✗ | The message to send as part of the error |  |
| Memory Size to Generate | `memorySizeValue` | number | 10 | ✗ | The approximate amount of memory to generate. Be generous... |  |
| Data Type | `randomDataType` | options | user | ✗ |  |  |

**Data Type options:**

* **Address** (`address`)
* **Coordinates** (`latLong`)
* **Credit Card** (`creditCard`)
* **Email** (`email`)
* **IPv4** (`ipv4`)
* **IPv6** (`ipv6`)
* **MAC** (`macAddress`)
* **NanoIds** (`nanoid`)
* **URL** (`url`)
* **User Data** (`user`)
* **UUID** (`uuid`)
* **Version** (`semver`)

| NanoId Alphabet | `nanoidAlphabet` | string | 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ | ✗ | The alphabet to use for generating the nanoIds |  |
| NanoId Length | `nanoidLength` | string | 16 | ✗ | The length of each nanoIds |  |
| Seed | `randomDataSeed` | string |  | ✗ | If set, seed to use for generating the data (same seed will generate the same data) | e.g. Leave empty for random seed |  |
| Number of Items to Generate | `randomDataCount` | number | 10 | ✗ | The number of random data items to generate into an array |  |
| Output as Single Array | `randomDataSingleArray` | boolean | False | ✗ | Whether to output a single array instead of multiple items |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["category"]}}`

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
* Aliases: Mock, Sample, Demo, Test, Throw error, OOM, Out of Memory, placeholder

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: debughelper
displayName: DebugHelper
description: Causes problems intentionally and generates useful data for debugging
version: '1'
nodeType: regular
group:
- output
params:
- id: category
  name: Category
  type: options
  default: throwError
  required: false
  description: Does nothing
  typeInfo:
    type: options
    displayName: Category
    name: category
    possibleValues:
    - value: doNothing
      name: Do Nothing
      description: Does nothing
    - value: throwError
      name: Throw Error
      description: Throws an error with the specified type and message
    - value: oom
      name: Out Of Memory
      description: Generates a large amount of memory to cause an out of memory error
    - value: randomData
      name: Generate Random Data
      description: Generates random data sets
- id: throwErrorType
  name: Error Type
  type: options
  default: NodeApiError
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        category:
        - throwError
  typeInfo:
    type: options
    displayName: Error Type
    name: throwErrorType
    possibleValues:
    - value: NodeApiError
      name: NodeApiError
      description: ''
    - value: NodeOperationError
      name: NodeOperationError
      description: ''
    - value: Error
      name: Error
      description: ''
- id: throwErrorMessage
  name: Error Message
  type: string
  default: Node has thrown an error
  required: false
  description: The message to send as part of the error
  validation:
    displayOptions:
      show:
        category:
        - throwError
  typeInfo:
    type: string
    displayName: Error Message
    name: throwErrorMessage
- id: memorySizeValue
  name: Memory Size to Generate
  type: number
  default: 10
  required: false
  description: The approximate amount of memory to generate. Be generous...
  validation:
    displayOptions:
      show:
        category:
        - oom
  typeInfo:
    type: number
    displayName: Memory Size to Generate
    name: memorySizeValue
- id: randomDataType
  name: Data Type
  type: options
  default: user
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        category:
        - randomData
  typeInfo:
    type: options
    displayName: Data Type
    name: randomDataType
    possibleValues:
    - value: address
      name: Address
      description: ''
    - value: latLong
      name: Coordinates
      description: ''
    - value: creditCard
      name: Credit Card
      description: ''
    - value: email
      name: Email
      description: ''
    - value: ipv4
      name: IPv4
      description: ''
    - value: ipv6
      name: IPv6
      description: ''
    - value: macAddress
      name: MAC
      description: ''
    - value: nanoid
      name: NanoIds
      description: ''
    - value: url
      name: URL
      description: ''
    - value: user
      name: User Data
      description: ''
    - value: uuid
      name: UUID
      description: ''
    - value: semver
      name: Version
      description: ''
- id: nanoidAlphabet
  name: NanoId Alphabet
  type: string
  default: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
  required: false
  description: The alphabet to use for generating the nanoIds
  validation:
    displayOptions:
      show:
        category:
        - randomData
        randomDataType:
        - nanoid
  typeInfo:
    type: string
    displayName: NanoId Alphabet
    name: nanoidAlphabet
- id: nanoidLength
  name: NanoId Length
  type: string
  default: '16'
  required: false
  description: The length of each nanoIds
  validation:
    displayOptions:
      show:
        category:
        - randomData
        randomDataType:
        - nanoid
  typeInfo:
    type: string
    displayName: NanoId Length
    name: nanoidLength
- id: randomDataSeed
  name: Seed
  type: string
  default: ''
  required: false
  description: If set, seed to use for generating the data (same seed will generate
    the same data)
  placeholder: Leave empty for random seed
  validation:
    displayOptions:
      show:
        category:
        - randomData
  typeInfo:
    type: string
    displayName: Seed
    name: randomDataSeed
- id: randomDataCount
  name: Number of Items to Generate
  type: number
  default: 10
  required: false
  description: The number of random data items to generate into an array
  validation:
    displayOptions:
      show:
        category:
        - randomData
  typeInfo:
    type: number
    displayName: Number of Items to Generate
    name: randomDataCount
- id: randomDataSingleArray
  name: Output as Single Array
  type: boolean
  default: false
  required: false
  description: Whether to output a single array instead of multiple items
  validation:
    displayOptions:
      show:
        category:
        - randomData
  typeInfo:
    type: boolean
    displayName: Output as Single Array
    name: randomDataSingleArray
common_expressions:
- ={{$parameter["category"]}}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: randomDataSeed
    text: Leave empty for random seed
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
  "$id": "https://n8n.io/schemas/nodes/debughelper.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "DebugHelper Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "category": {
          "description": "Does nothing",
          "type": "string",
          "enum": [
            "doNothing",
            "throwError",
            "oom",
            "randomData"
          ],
          "default": "throwError"
        },
        "throwErrorType": {
          "description": "",
          "type": "string",
          "enum": [
            "NodeApiError",
            "NodeOperationError",
            "Error"
          ],
          "default": "NodeApiError"
        },
        "throwErrorMessage": {
          "description": "The message to send as part of the error",
          "type": "string",
          "default": "Node has thrown an error"
        },
        "memorySizeValue": {
          "description": "The approximate amount of memory to generate. Be generous...",
          "type": "number",
          "default": 10
        },
        "randomDataType": {
          "description": "",
          "type": "string",
          "enum": [
            "address",
            "latLong",
            "creditCard",
            "email",
            "ipv4",
            "ipv6",
            "macAddress",
            "nanoid",
            "url",
            "user",
            "uuid",
            "semver"
          ],
          "default": "user"
        },
        "nanoidAlphabet": {
          "description": "The alphabet to use for generating the nanoIds",
          "type": "string",
          "default": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        },
        "nanoidLength": {
          "description": "The length of each nanoIds",
          "type": "string",
          "default": "16"
        },
        "randomDataSeed": {
          "description": "If set, seed to use for generating the data (same seed will generate the same data)",
          "type": "string",
          "default": "",
          "examples": [
            "Leave empty for random seed"
          ]
        },
        "randomDataCount": {
          "description": "The number of random data items to generate into an array",
          "type": "number",
          "default": 10
        },
        "randomDataSingleArray": {
          "description": "Whether to output a single array instead of multiple items",
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
