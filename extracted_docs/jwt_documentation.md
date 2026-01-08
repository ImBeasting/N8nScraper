---
title: "Node: JWT"
slug: "node-jwt"
version: "1"
updated: "2026-01-08"
summary: "JWT"
node_type: "regular"
group: "['transform']"
---

# Node: JWT

**Purpose.** JWT
**Subtitle.** ={{((template: prettifyOperation))($parameter.operation)}}


---

## Node Details

- **Icon:** `file:jwt.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **jwtAuth**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `jwtAuth` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Decode | `decode` |  |
| Sign | `sign` |  |
| Verify | `verify` |  |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | sign | ✗ | Operation to perform |  |

**Operation options:**

* **Decode** (`decode`) - Decode a JWT
* **Sign** (`sign`) - Sign a JWT
* **Verify** (`verify`) - Verify a JWT

---

### Decode parameters (`decode`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Token | `token` | string |  | ✓ | The token to verify or decode | validated |

### Sign parameters (`sign`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Use JSON to Build Payload | `useJson` | boolean | False | ✗ | Whether to use JSON to build the claims |  |
| Payload Claims | `claims` | collection | {} | ✗ | Identifies the recipients that the JWT is intended for | e.g. Add Claim | min:0, max:∞ |

<details>
<summary><strong>Payload Claims sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Audience | `audience` | string |  | Identifies the recipients that the JWT is intended for |
| Expires In | `expiresIn` | number | 3600 | The lifetime of the token in seconds |
| Issuer | `issuer` | string |  | Identifies the principal that issued the JWT |
| JWT ID | `jwtid` | string |  | Unique identifier for the JWT |
| Not Before | `notBefore` | number | 0 | The time before which the JWT must not be accepted for processing |
| Subject | `subject` | string |  | Identifies the principal that is the subject of the JWT |

</details>

| Payload Claims (JSON) | `claimsJson` | json | {\n   | ✗ | Claims to add to the token in JSON format |  |

### Verify parameters (`verify`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Token | `token` | string |  | ✓ | The token to verify or decode | validated |

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Sign with claims

**From workflow:** JWT Test Workflow

**Parameters:**
```json
{
  "claims": {
    "audience": "test",
    "issuer": "test",
    "jwtid": "123",
    "subject": "test"
  },
  "options": {}
}
```

**Credentials:**
- jwtAuth: `JWT Auth account`

### Example 2: Sign with JSON Payload

**From workflow:** JWT Test Workflow

**Parameters:**
```json
{
  "useJson": true,
  "options": {}
}
```

**Credentials:**
- jwtAuth: `JWT Auth account`

### Example 3: Verify1

**From workflow:** JWT Test Workflow

**Parameters:**
```json
{
  "operation": "verify",
  "token": "={{ $json.token }}",
  "options": {
    "complete": true,
    "ignoreExpiration": true,
    "ignoreNotBefore": true
  }
}
```

**Credentials:**
- jwtAuth: `JWT Auth account`

### Example 4: Decode2

**From workflow:** JWT Test Workflow

**Parameters:**
```json
{
  "operation": "decode",
  "token": "={{ $json.token }}",
  "options": {}
}
```

**Credentials:**
- jwtAuth: `JWT Auth account`

### Example 5: Decode1

**From workflow:** JWT Test Workflow

**Parameters:**
```json
{
  "operation": "decode",
  "token": "={{ $json.token }}",
  "options": {}
}
```

**Credentials:**
- jwtAuth: `JWT Auth account`


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
* Aliases: Token, Key, JSON, Payload, Sign, Verify, Decode

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: jwt
displayName: JWT
description: JWT
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: jwtAuth
  required: true
operations:
- id: decode
  name: Decode
  description: ''
  params:
  - id: token
    name: Token
    type: string
    default: ''
    required: true
    description: The token to verify or decode
    validation: &id001
      required: true
      format: validated
      displayOptions:
        show:
          operation:
          - verify
          - decode
    typeInfo: &id002
      type: string
      displayName: Token
      name: token
      typeOptions:
        password: true
- id: sign
  name: Sign
  description: ''
  params:
  - id: useJson
    name: Use JSON to Build Payload
    type: boolean
    default: false
    required: false
    description: Whether to use JSON to build the claims
    validation:
      displayOptions:
        show:
          operation:
          - sign
    typeInfo:
      type: boolean
      displayName: Use JSON to Build Payload
      name: useJson
  - id: claimsJson
    name: Payload Claims (JSON)
    type: json
    default: '{\n  '
    required: false
    description: Claims to add to the token in JSON format
    validation:
      displayOptions:
        show:
          operation:
          - sign
          useJson:
          - true
    typeInfo:
      type: json
      displayName: Payload Claims (JSON)
      name: claimsJson
      typeOptions:
        rows: 5
- id: verify
  name: Verify
  description: ''
  params:
  - id: token
    name: Token
    type: string
    default: ''
    required: true
    description: The token to verify or decode
    validation: *id001
    typeInfo: *id002
examples:
- name: Sign with claims
  parameters:
    claims:
      audience: test
      issuer: test
      jwtid: '123'
      subject: test
    options: {}
  workflow: JWT Test Workflow
- name: Sign with JSON Payload
  parameters:
    useJson: true
    options: {}
  workflow: JWT Test Workflow
- name: Verify1
  parameters:
    operation: verify
    token: ={{ $json.token }}
    options:
      complete: true
      ignoreExpiration: true
      ignoreNotBefore: true
  workflow: JWT Test Workflow
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: claims
    text: Add Claim
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
  "$id": "https://n8n.io/schemas/nodes/jwt.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "JWT Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "decode",
        "sign",
        "verify"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "decode",
            "sign",
            "verify"
          ],
          "default": "sign"
        },
        "useJson": {
          "description": "Whether to use JSON to build the claims",
          "type": "boolean",
          "default": false
        },
        "claims": {
          "description": "Identifies the recipients that the JWT is intended for",
          "type": "string",
          "default": {},
          "examples": [
            "Add Claim"
          ]
        },
        "claimsJson": {
          "description": "Claims to add to the token in JSON format",
          "type": "string",
          "default": "{\\n  "
        },
        "token": {
          "description": "The token to verify or decode",
          "type": "string",
          "default": "",
          "format": "validated"
        },
        "options": {
          "description": "Whether to return the complete decoded token with information about the header and signature or just the payload",
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
      "name": "jwtAuth",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Sign with claims",
      "value": {
        "claims": {
          "audience": "test",
          "issuer": "test",
          "jwtid": "123",
          "subject": "test"
        },
        "options": {}
      }
    },
    {
      "description": "Sign with JSON Payload",
      "value": {
        "useJson": true,
        "options": {}
      }
    },
    {
      "description": "Verify1",
      "value": {
        "operation": "verify",
        "token": "={{ $json.token }}",
        "options": {
          "complete": true,
          "ignoreExpiration": true,
          "ignoreNotBefore": true
        }
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
