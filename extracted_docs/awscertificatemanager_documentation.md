---
title: "Node: AWS Certificate Manager"
slug: "node-awscertificatemanager"
version: "1"
updated: "2026-01-08"
summary: "Sends data to AWS Certificate Manager"
node_type: "regular"
group: "['output']"
---

# Node: AWS Certificate Manager

**Purpose.** Sends data to AWS Certificate Manager
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:acm.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Operations

### Certificate Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a certificate |
| Get | `get` | Get a certificate |
| Get Many | `getMany` | Get many certificates |
| Get Metadata | `getMetadata` | Get certificate metadata |
| Renew | `renew` | Renew a certificate |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | certificate | ✗ | Resource to operate on |  |

**Resource options:**

* **Certificate** (`certificate`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | renew | ✗ | Delete a certificate |  |

**Operation options:**

* **Delete** (`delete`) - Delete a certificate
* **Get** (`get`) - Get a certificate
* **Get Many** (`getMany`) - Get many certificates
* **Get Metadata** (`getMetadata`) - Get certificate metadata
* **Renew** (`renew`) - Renew a certificate

---

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate ARN | `certificateArn` | string |  | ✓ | String that contains the ARN of the ACM certificate to be renewed. This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012. |  |
| Bucket Name | `bucketName` | string |  | ✓ |  |  |
| Certificate Key | `certificateKey` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate ARN | `certificateArn` | string |  | ✓ | String that contains the ARN of the ACM certificate to be renewed. This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012. |  |

### Get Many parameters (`getMany`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Filter the certificate list by status value | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Certificate Statuses | `certificateStatuses` | multiOptions | [] | Filter the certificate list by status value |
| Extended Key Usage | `extendedKeyUsage` | multiOptions | [] | Specify one or more ExtendedKeyUsage extension values |
| Key Types | `keyTypes` | multiOptions |  | Specify one or more algorithms that can be used to generate key pairs |
| Key Usage | `keyUsage` | multiOptions | [] | Specify one or more KeyUsage extension values |

</details>


### Get Metadata parameters (`getMetadata`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate ARN | `certificateArn` | string |  | ✓ | String that contains the ARN of the ACM certificate to be renewed. This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012. |  |

### Renew parameters (`renew`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate ARN | `certificateArn` | string |  | ✓ | String that contains the ARN of the ACM certificate to be renewed. This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012. |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ": " + $parameter["resource"]}}`

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
node: awsCertificateManager
displayName: AWS Certificate Manager
description: Sends data to AWS Certificate Manager
version: '1'
nodeType: regular
group:
- output
operations:
- id: delete
  name: Delete
  description: Delete a certificate
  params:
  - id: certificateArn
    name: Certificate ARN
    type: string
    default: ''
    required: true
    description: 'String that contains the ARN of the ACM certificate to be renewed.
      This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012.'
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - renew
          - get
          - delete
          - getMetadata
    typeInfo: &id002
      type: string
      displayName: Certificate ARN
      name: certificateArn
  - id: bucketName
    name: Bucket Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - delete
    typeInfo:
      type: string
      displayName: Bucket Name
      name: bucketName
  - id: certificateKey
    name: Certificate Key
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - delete
    typeInfo:
      type: string
      displayName: Certificate Key
      name: certificateKey
- id: get
  name: Get
  description: Get a certificate
  params:
  - id: certificateArn
    name: Certificate ARN
    type: string
    default: ''
    required: true
    description: 'String that contains the ARN of the ACM certificate to be renewed.
      This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012.'
    validation: *id001
    typeInfo: *id002
- id: getMany
  name: Get Many
  description: Get many certificates
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          operation:
          - getMany
          resource:
          - certificate
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - getMany
          resource:
          - certificate
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
- id: getMetadata
  name: Get Metadata
  description: Get certificate metadata
  params:
  - id: certificateArn
    name: Certificate ARN
    type: string
    default: ''
    required: true
    description: 'String that contains the ARN of the ACM certificate to be renewed.
      This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012.'
    validation: *id001
    typeInfo: *id002
- id: renew
  name: Renew
  description: Renew a certificate
  params:
  - id: certificateArn
    name: Certificate ARN
    type: string
    default: ''
    required: true
    description: 'String that contains the ARN of the ACM certificate to be renewed.
      This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012.'
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
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
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/awsCertificateManager.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AWS Certificate Manager Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "delete",
        "get",
        "getMany",
        "getMetadata",
        "renew"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "certificate"
          ],
          "default": "certificate"
        },
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "iam",
            "assumeRole"
          ],
          "default": "iam"
        },
        "operation": {
          "description": "Delete a certificate",
          "type": "string",
          "enum": [
            "delete",
            "get",
            "getMany",
            "getMetadata",
            "renew"
          ],
          "default": "renew"
        },
        "certificateArn": {
          "description": "String that contains the ARN of the ACM certificate to be renewed. This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012.",
          "type": "string",
          "default": ""
        },
        "bucketName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "certificateKey": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
        },
        "options": {
          "description": "Filter the certificate list by status value",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "aws": {
          "description": "",
          "type": "string"
        },
        "awsAssumeRole": {
          "description": "",
          "type": "string"
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
