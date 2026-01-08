---
title: "Node: Crypto"
slug: "node-crypto"
version: "1"
updated: "2026-01-08"
summary: "Provide cryptographic utilities"
node_type: "regular"
group: "['transform']"
---

# Node: Crypto

**Purpose.** Provide cryptographic utilities
**Subtitle.** ={{$parameter["action"]}}


---

## Node Details

- **Icon:** `fa:key`
- **Group:** `['transform']`
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
| Action | `action` | options | hash | ✗ | Generate random string |  |

**Action options:**

* **Generate** (`generate`) - Generate random string
* **Hash** (`hash`) - Hash a text or file in a specified format
* **Hmac** (`hmac`) - Hmac a text or file in a specified format
* **Sign** (`sign`) - Sign a string using a private key

| Type | `type` | options | MD5 | ✓ | The hash type to use |  |

**Type options:**

* **MD5** (`MD5`)
* **SHA256** (`SHA256`)
* **SHA3-256** (`SHA3-256`)
* **SHA3-384** (`SHA3-384`)
* **SHA3-512** (`SHA3-512`)
* **SHA384** (`SHA384`)
* **SHA512** (`SHA512`)

| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to hashed should be taken from binary field |  |
| Binary Property Name | `binaryPropertyName` | string | data | ✓ | Name of the binary property which contains the input data |  |
| Value | `value` | string |  | ✓ | The value that should be hashed |  |
| Property Name | `dataPropertyName` | string | data | ✓ | Name of the property to which to write the hash |  |
| Encoding | `encoding` | options | hex | ✓ |  |  |

**Encoding options:**

* **BASE64** (`base64`)
* **HEX** (`hex`)

| Type | `type` | options | MD5 | ✓ | The hash type to use |  |

**Type options:**

* **MD5** (`MD5`)
* **SHA256** (`SHA256`)
* **SHA3-256** (`SHA3-256`)
* **SHA3-384** (`SHA3-384`)
* **SHA3-512** (`SHA3-512`)
* **SHA384** (`SHA384`)
* **SHA512** (`SHA512`)

| Value | `value` | string |  | ✓ | The value of which the hmac should be created |  |
| Property Name | `dataPropertyName` | string | data | ✓ | Name of the property to which to write the hmac |  |
| Secret | `secret` | string |  | ✓ |  |  |
| Encoding | `encoding` | options | hex | ✓ |  |  |

**Encoding options:**

* **BASE64** (`base64`)
* **HEX** (`hex`)

| Value | `value` | string |  | ✓ | The value that should be signed |  |
| Property Name | `dataPropertyName` | string | data | ✓ | Name of the property to which to write the signed value |  |
| Algorithm Name or ID | `algorithm` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Encoding | `encoding` | options | hex | ✓ |  |  |

**Encoding options:**

* **BASE64** (`base64`)
* **HEX** (`hex`)

| Private Key | `privateKey` | string |  | ✓ | Private key to use when signing the string |  |
| Property Name | `dataPropertyName` | string | data | ✓ | Name of the property to which to write the random string |  |
| Type | `encodingType` | options | uuid | ✓ | Encoding that will be used to generate string |  |

**Type options:**

* **ASCII** (`ascii`)
* **BASE64** (`base64`)
* **HEX** (`hex`)
* **UUID** (`uuid`)

| Length | `stringLength` | number | 32 | ✗ | Length of the generated string |  |

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Crypto Hash into Hex

**From workflow:** Crypto Test

**Parameters:**
```json
{
  "value": "test"
}
```

### Example 2: Crypto Hash into MD5

**From workflow:** Crypto Test

**Parameters:**
```json
{
  "value": "test"
}
```

### Example 3: Crypto Sign data with RSA-MD5

**From workflow:** Crypto Test

**Parameters:**
```json
{
  "action": "sign",
  "value": "test",
  "algorithm": "RSA-MD5",
  "encoding": "base64",
  "privateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIBOgIBAAJBAKj34GkxFhD90vcNLYLInFEX6Ppy1tPf9Cnzj4p4WGeKLs1Pt8Qu\nKUpRKfFLfRYC9AIKjbJTWit+CqvjWYzvQwECAwEAAQJAIJLixBy2qpFoS4DSmoEm\no3qGy0t6z09AIJtH+5OeRV1be+N4cDYJKffGzDa88vQENZiRm0GRq6a+HPGQMd2k\nTQIhAKMSvzIBnni7ot/OSie2TmJLY4SwTQAevXysE2RbFDYdAiEBCUEaRQnMnbp7\n9mxDXDf6AU0cN/RPBjb9qSHDcWZHGzUCIG2Es59z8ugGrDY+pxLQnwfotadxd+Uy\nv/Ow5T0q5gIJAiEAyS4RaI9YG8EWx/2w0T67ZUVAw8eOMB6BIUg0Xcu+3okCIBOs\n/5OiPgoTdSy7bcF9IGpSE8ZgGKzgYQVZeN97YE00\n-----END RSA PRIVATE KEY-----"
}
```

### Example 4: Crypto Hmac data with MD5

**From workflow:** Crypto Test

**Parameters:**
```json
{
  "action": "hmac",
  "value": "test",
  "secret": "-----BEGIN RSA PRIVATE KEY-----|MIIBOgIBAAJBAKj34GkxFhD90vcNLYLInFEX6Ppy1tPf9Cnzj4p4WGeKLs1Pt8QuKUpRKfFLfRYC9AIKjbJTWit+CqvjWYzvQwECAwEAAQJAIJLixBy2qpFoS4DSmoEmo3qGy0t6z09AIJtH+5OeRV1be+N4cDYJKffGzDa88vQENZiRm0GRq6a+HPGQMd2kTQIhAKMSvzIBnni7ot/OSie2TmJLY4SwTQAevXysE2RbFDYdAiEBCUEaRQnMnbp79mxDXDf6AU0cN/RPBjb9qSHDcWZHGzUCIG2Es59z8ugGrDY+pxLQnwfotadxd+Uyv/Ow5T0q5gIJAiEAyS4RaI9YG8EWx/2w0T67ZUVAw8eOMB6BIUg0Xcu+3okCIBOs/5OiPgoTdSy7bcF9IGpSE8ZgGKzgYQVZeN97YE00-----END RSA PRIVATE KEY-----",
  "encoding": "base64"
}
```

### Example 5: Crypto Generate UUID

**From workflow:** Crypto Test

**Parameters:**
```json
{
  "action": "generate"
}
```


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["action"]}}`

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
* Categories: Development, Core Nodes
* Aliases: Encrypt, SHA, Hash

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: crypto
displayName: Crypto
description: Provide cryptographic utilities
version: '1'
nodeType: regular
group:
- transform
params:
- id: action
  name: Action
  type: options
  default: hash
  required: false
  description: Generate random string
  typeInfo:
    type: options
    displayName: Action
    name: action
    possibleValues:
    - value: generate
      name: Generate
      description: Generate random string
    - value: hash
      name: Hash
      description: Hash a text or file in a specified format
    - value: hmac
      name: Hmac
      description: Hmac a text or file in a specified format
    - value: sign
      name: Sign
      description: Sign a string using a private key
- id: type
  name: Type
  type: options
  default: MD5
  required: true
  description: The hash type to use
  validation: &id001
    required: true
    displayOptions:
      show:
        action:
        - hmac
  typeInfo: &id002
    type: options
    displayName: Type
    name: type
    possibleValues:
    - value: MD5
      name: MD5
      description: ''
    - value: SHA256
      name: SHA256
      description: ''
    - value: SHA3-256
      name: SHA3-256
      description: ''
    - value: SHA3-384
      name: SHA3-384
      description: ''
    - value: SHA3-512
      name: SHA3-512
      description: ''
    - value: SHA384
      name: SHA384
      description: ''
    - value: SHA512
      name: SHA512
      description: ''
- id: binaryData
  name: Binary File
  type: boolean
  default: false
  required: true
  description: Whether the data to hashed should be taken from binary field
  validation:
    required: true
    displayOptions:
      show:
        action:
        - hash
        - hmac
  typeInfo:
    type: boolean
    displayName: Binary File
    name: binaryData
- id: binaryPropertyName
  name: Binary Property Name
  type: string
  default: data
  required: true
  description: Name of the binary property which contains the input data
  validation:
    required: true
    displayOptions:
      show:
        action:
        - hash
        - hmac
        binaryData:
        - true
  typeInfo:
    type: string
    displayName: Binary Property Name
    name: binaryPropertyName
- id: value
  name: Value
  type: string
  default: ''
  required: true
  description: The value that should be hashed
  validation: &id003
    required: true
    displayOptions:
      show:
        action:
        - sign
  typeInfo: &id004
    type: string
    displayName: Value
    name: value
- id: dataPropertyName
  name: Property Name
  type: string
  default: data
  required: true
  description: Name of the property to which to write the hash
  validation: &id005
    required: true
    displayOptions:
      show:
        action:
        - generate
  typeInfo: &id006
    type: string
    displayName: Property Name
    name: dataPropertyName
- id: encoding
  name: Encoding
  type: options
  default: hex
  required: true
  description: ''
  validation: &id007
    required: true
    displayOptions:
      show:
        action:
        - sign
  typeInfo: &id008
    type: options
    displayName: Encoding
    name: encoding
    possibleValues:
    - value: base64
      name: BASE64
      description: ''
    - value: hex
      name: HEX
      description: ''
- id: type
  name: Type
  type: options
  default: MD5
  required: true
  description: The hash type to use
  validation: *id001
  typeInfo: *id002
- id: value
  name: Value
  type: string
  default: ''
  required: true
  description: The value of which the hmac should be created
  validation: *id003
  typeInfo: *id004
- id: dataPropertyName
  name: Property Name
  type: string
  default: data
  required: true
  description: Name of the property to which to write the hmac
  validation: *id005
  typeInfo: *id006
- id: secret
  name: Secret
  type: string
  default: ''
  required: true
  description: ''
  validation:
    required: true
    displayOptions:
      show:
        action:
        - hmac
  typeInfo:
    type: string
    displayName: Secret
    name: secret
    typeOptions:
      password: true
- id: encoding
  name: Encoding
  type: options
  default: hex
  required: true
  description: ''
  validation: *id007
  typeInfo: *id008
- id: value
  name: Value
  type: string
  default: ''
  required: true
  description: The value that should be signed
  validation: *id003
  typeInfo: *id004
- id: dataPropertyName
  name: Property Name
  type: string
  default: data
  required: true
  description: Name of the property to which to write the signed value
  validation: *id005
  typeInfo: *id006
- id: algorithm
  name: Algorithm Name or ID
  type: options
  default: ''
  required: true
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
    displayOptions:
      show:
        action:
        - sign
  typeInfo:
    type: options
    displayName: Algorithm Name or ID
    name: algorithm
    possibleValues: []
- id: encoding
  name: Encoding
  type: options
  default: hex
  required: true
  description: ''
  validation: *id007
  typeInfo: *id008
- id: privateKey
  name: Private Key
  type: string
  default: ''
  required: true
  description: Private key to use when signing the string
  validation:
    required: true
    displayOptions:
      show:
        action:
        - sign
  typeInfo:
    type: string
    displayName: Private Key
    name: privateKey
- id: dataPropertyName
  name: Property Name
  type: string
  default: data
  required: true
  description: Name of the property to which to write the random string
  validation: *id005
  typeInfo: *id006
- id: encodingType
  name: Type
  type: options
  default: uuid
  required: true
  description: Encoding that will be used to generate string
  validation:
    required: true
    displayOptions:
      show:
        action:
        - generate
  typeInfo:
    type: options
    displayName: Type
    name: encodingType
    possibleValues:
    - value: ascii
      name: ASCII
      description: ''
    - value: base64
      name: BASE64
      description: ''
    - value: hex
      name: HEX
      description: ''
    - value: uuid
      name: UUID
      description: ''
- id: stringLength
  name: Length
  type: number
  default: 32
  required: false
  description: Length of the generated string
  validation:
    displayOptions:
      show:
        action:
        - generate
        encodingType:
        - ascii
        - base64
        - hex
  typeInfo:
    type: number
    displayName: Length
    name: stringLength
examples:
- name: Crypto Hash into Hex
  parameters:
    value: test
  workflow: Crypto Test
- name: Crypto Hash into MD5
  parameters:
    value: test
  workflow: Crypto Test
- name: Crypto Sign data with RSA-MD5
  parameters:
    action: sign
    value: test
    algorithm: RSA-MD5
    encoding: base64
    privateKey: '-----BEGIN RSA PRIVATE KEY-----

      MIIBOgIBAAJBAKj34GkxFhD90vcNLYLInFEX6Ppy1tPf9Cnzj4p4WGeKLs1Pt8Qu

      KUpRKfFLfRYC9AIKjbJTWit+CqvjWYzvQwECAwEAAQJAIJLixBy2qpFoS4DSmoEm

      o3qGy0t6z09AIJtH+5OeRV1be+N4cDYJKffGzDa88vQENZiRm0GRq6a+HPGQMd2k

      TQIhAKMSvzIBnni7ot/OSie2TmJLY4SwTQAevXysE2RbFDYdAiEBCUEaRQnMnbp7

      9mxDXDf6AU0cN/RPBjb9qSHDcWZHGzUCIG2Es59z8ugGrDY+pxLQnwfotadxd+Uy

      v/Ow5T0q5gIJAiEAyS4RaI9YG8EWx/2w0T67ZUVAw8eOMB6BIUg0Xcu+3okCIBOs

      /5OiPgoTdSy7bcF9IGpSE8ZgGKzgYQVZeN97YE00

      -----END RSA PRIVATE KEY-----'
  workflow: Crypto Test
common_expressions:
- ={{$parameter["action"]}}
ui_elements:
  notices: []
  tooltips: []
  placeholders: []
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
  "$id": "https://n8n.io/schemas/nodes/crypto.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Crypto Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "action": {
          "description": "Generate random string",
          "type": "string",
          "enum": [
            "generate",
            "hash",
            "hmac",
            "sign"
          ],
          "default": "hash"
        },
        "type": {
          "description": "The hash type to use",
          "type": "string",
          "enum": [
            "MD5",
            "SHA256",
            "SHA3-256",
            "SHA3-384",
            "SHA3-512",
            "SHA384",
            "SHA512"
          ],
          "default": "MD5"
        },
        "binaryData": {
          "description": "Whether the data to hashed should be taken from binary field",
          "type": "boolean",
          "default": false
        },
        "binaryPropertyName": {
          "description": "Name of the binary property which contains the input data",
          "type": "string",
          "default": "data"
        },
        "value": {
          "description": "The value that should be signed",
          "type": "string",
          "default": ""
        },
        "dataPropertyName": {
          "description": "Name of the property to which to write the random string",
          "type": "string",
          "default": "data"
        },
        "encoding": {
          "description": "",
          "type": "string",
          "enum": [
            "base64",
            "hex"
          ],
          "default": "hex"
        },
        "secret": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "algorithm": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "privateKey": {
          "description": "Private key to use when signing the string",
          "type": "string",
          "default": ""
        },
        "encodingType": {
          "description": "Encoding that will be used to generate string",
          "type": "string",
          "enum": [
            "ascii",
            "base64",
            "hex",
            "uuid"
          ],
          "default": "uuid"
        },
        "stringLength": {
          "description": "Length of the generated string",
          "type": "number",
          "default": 32
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
  "examples": [
    {
      "description": "Crypto Hash into Hex",
      "value": {
        "value": "test"
      }
    },
    {
      "description": "Crypto Hash into MD5",
      "value": {
        "value": "test"
      }
    },
    {
      "description": "Crypto Sign data with RSA-MD5",
      "value": {
        "action": "sign",
        "value": "test",
        "algorithm": "RSA-MD5",
        "encoding": "base64",
        "privateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIBOgIBAAJBAKj34GkxFhD90vcNLYLInFEX6Ppy1tPf9Cnzj4p4WGeKLs1Pt8Qu\nKUpRKfFLfRYC9AIKjbJTWit+CqvjWYzvQwECAwEAAQJAIJLixBy2qpFoS4DSmoEm\no3qGy0t6z09AIJtH+5OeRV1be+N4cDYJKffGzDa88vQENZiRm0GRq6a+HPGQMd2k\nTQIhAKMSvzIBnni7ot/OSie2TmJLY4SwTQAevXysE2RbFDYdAiEBCUEaRQnMnbp7\n9mxDXDf6AU0cN/RPBjb9qSHDcWZHGzUCIG2Es59z8ugGrDY+pxLQnwfotadxd+Uy\nv/Ow5T0q5gIJAiEAyS4RaI9YG8EWx/2w0T67ZUVAw8eOMB6BIUg0Xcu+3okCIBOs\n/5OiPgoTdSy7bcF9IGpSE8ZgGKzgYQVZeN97YE00\n-----END RSA PRIVATE KEY-----"
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
