---
title: "Node: Venafi TLS Protect Cloud"
slug: "node-venafitlsprotectcloud"
version: "1"
updated: "2026-01-08"
summary: "Consume Venafi TLS Protect Cloud API"
node_type: "regular"
group: "['input']"
---

# Node: Venafi TLS Protect Cloud

**Purpose.** Consume Venafi TLS Protect Cloud API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:../venafi.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **venafiTlsProtectCloudApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `venafiTlsProtectCloudApi` | ✓ | - |

---

## API Patterns

**Headers Used:** content-type

---

## Operations

### Certificate Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a certificate |
| Download | `download` | Download a certificate |
| Get | `get` | Retrieve a certificate |
| Get Many | `getMany` | Retrieve many certificates |
| Renew | `renew` | Renew a certificate |

### Certificaterequest Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new certificate request |
| Get | `get` | Retrieve a certificate request |
| Get Many | `getMany` | Retrieve many certificate requests |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | certificateRequest | ✗ | Resource to operate on |  |

**Resource options:**

* **Certificate** (`certificate`)
* **Certificate Request** (`certificateRequest`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | delete | ✗ | Delete a certificate |  |

**Operation options:**

* **Delete** (`delete`) - Delete a certificate
* **Download** (`download`) - Download a certificate
* **Get** (`get`) - Retrieve a certificate
* **Get Many** (`getMany`) - Retrieve many certificates
* **Renew** (`renew`) - Renew a certificate

---

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate ID | `certificateId` | string |  | ✓ |  |  |

### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate ID | `certificateId` | string |  | ✓ |  |  |
| Download Item | `downloadItem` | options | certificate | ✗ |  |  |

**Download Item options:**

* **Certificate** (`certificate`)
* **Keystore** (`keystore`)

| Keystore Type | `keystoreType` | options | PEM | ✗ |  |  |

**Keystore Type options:**

* **JKS** (`JKS`)
* **PKCS12** (`PKCS12`)
* **PEM** (`PEM`)

| Certificate Label | `certificateLabel` | string |  | ✓ |  |  |
| Private Key Passphrase | `privateKeyPassphrase` | string |  | ✓ |  |  |
| Keystore Passphrase | `keystorePassphrase` | string |  | ✓ |  |  |
| Input Data Field Name | `binaryProperty` | string | data | ✓ | The name of the input field containing the binary file data to be uploaded |  |
| Options | `options` | collection | {} | ✗ | Download the certificate with the end-entity portion of the chain first | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Chain Order | `chainOrder` | options | ROOT_FIRST | Download the certificate with the end-entity portion of the chain first |
| Format | `format` | options | PEM |  |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate ID | `certificateId` | string |  | ✓ |  |  |
| Certificate Request ID | `certificateRequestId` | string |  | ✓ |  |  |

### Get Many parameters (`getMany`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Subject | `subject` | string |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |

### Renew parameters (`renew`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Application Name or ID | `applicationId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Existing Certificate ID | `existingCertificateId` | string |  | ✗ |  |  |
| Certificate Issuing Template Name or ID | `certificateIssuingTemplateId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Certificate Signing Request | `certificateSigningRequest` | string |  | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Validity Period | `validityPeriod` | options | P1Y |  |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Application Name or ID | `applicationId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Certificate Issuing Template Name or ID | `certificateIssuingTemplateId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Generate CSR | `generateCsr` | boolean | False | ✗ |  |  |
| Common Name | `commonName` | string | n8n.io | ✓ | The Common Name field for the certificate Subject (CN) |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Elliptic Curve (EC) | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Key Type | `keyType` | options | RSA | Elliptic Curve (EC) |
| Key Curve | `keyCurve` | options | ED25519 | Use Edwards-curve Digital Signature Algorithm (EdDSA) |
| Key Length | `keyLength` | number | 2048 | The number of bits to allow for key generation |
| (O) Organization | `organization` | string |  | The name of a company or organization |
| (OU) Organizational Unit(s) | `organizationalUnits` | string |  | The name of a department or section |
| (L) City/Locality | `locality` | string |  | The name of a city or town |
| (ST) State | `state` | string |  | The name of a state or province |
| (C) Country | `country` | string |  | A 2 letter country code |
| Subject Alt Names | `SubjectAltNamesUi` | fixedCollection | {} | What type of SAN is being used |

</details>

| Certificate Signing Request | `certificateSigningRequest` | string |  | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | Specify how long the issued certificate should be valid for. Use ISO8601 format. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Validity Period | `validityPeriod` | string | P1Y | Specify how long the issued certificate should be valid for. Use ISO8601 format. |

</details>


---

## Load Options Methods

- `getApplications`

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
node: venafiTlsProtectCloud
displayName: Venafi TLS Protect Cloud
description: Consume Venafi TLS Protect Cloud API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: venafiTlsProtectCloudApi
  required: true
operations:
- id: delete
  name: Delete
  description: Delete a certificate
  params:
  - id: certificateId
    name: Certificate ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - get
          - delete
          resource:
          - certificate
    typeInfo: &id002
      type: string
      displayName: Certificate ID
      name: certificateId
- id: download
  name: Download
  description: Download a certificate
  params:
  - id: certificateId
    name: Certificate ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: downloadItem
    name: Download Item
    type: options
    default: certificate
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - download
          resource:
          - certificate
    typeInfo:
      type: options
      displayName: Download Item
      name: downloadItem
      possibleValues:
      - value: certificate
        name: Certificate
        description: ''
      - value: keystore
        name: Keystore
        description: ''
  - id: keystoreType
    name: Keystore Type
    type: options
    default: PEM
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - download
          resource:
          - certificate
          downloadItem:
          - keystore
    typeInfo:
      type: options
      displayName: Keystore Type
      name: keystoreType
      possibleValues:
      - value: JKS
        name: JKS
        description: ''
      - value: PKCS12
        name: PKCS12
        description: ''
      - value: PEM
        name: PEM
        description: ''
  - id: certificateLabel
    name: Certificate Label
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - download
          resource:
          - certificate
          downloadItem:
          - keystore
    typeInfo:
      type: string
      displayName: Certificate Label
      name: certificateLabel
  - id: privateKeyPassphrase
    name: Private Key Passphrase
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - download
          resource:
          - certificate
          downloadItem:
          - keystore
    typeInfo:
      type: string
      displayName: Private Key Passphrase
      name: privateKeyPassphrase
  - id: keystorePassphrase
    name: Keystore Passphrase
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - download
          resource:
          - certificate
          downloadItem:
          - keystore
          keystoreType:
          - JKS
    typeInfo:
      type: string
      displayName: Keystore Passphrase
      name: keystorePassphrase
  - id: binaryProperty
    name: Input Data Field Name
    type: string
    default: data
    required: true
    description: The name of the input field containing the binary file data to be
      uploaded
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - download
          resource:
          - certificate
    typeInfo:
      type: string
      displayName: Input Data Field Name
      name: binaryProperty
- id: get
  name: Get
  description: Retrieve a certificate
  params:
  - id: certificateId
    name: Certificate ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: certificateRequestId
    name: Certificate Request ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - certificateRequest
    typeInfo:
      type: string
      displayName: Certificate Request ID
      name: certificateRequestId
- id: getMany
  name: Get Many
  description: Retrieve many certificates
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id003
      displayOptions:
        show:
          operation:
          - getMany
          resource:
          - certificateRequest
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          operation:
          - getMany
          resource:
          - certificateRequest
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: renew
  name: Renew
  description: Renew a certificate
  params:
  - id: applicationId
    name: Application Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id007
      displayOptions:
        show:
          operation:
          - create
          resource:
          - certificateRequest
    typeInfo: &id008
      type: options
      displayName: Application Name or ID
      name: applicationId
      typeOptions:
        loadOptionsMethod: getApplications
      possibleValues: []
  - id: existingCertificateId
    name: Existing Certificate ID
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - renew
          resource:
          - certificate
    typeInfo:
      type: string
      displayName: Existing Certificate ID
      name: existingCertificateId
  - id: certificateIssuingTemplateId
    name: Certificate Issuing Template Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id009
      displayOptions:
        show:
          operation:
          - create
          resource:
          - certificateRequest
    typeInfo: &id010
      type: options
      displayName: Certificate Issuing Template Name or ID
      name: certificateIssuingTemplateId
      typeOptions:
        loadOptionsMethod: getCertificateIssuingTemplates
      possibleValues: []
  - id: certificateSigningRequest
    name: Certificate Signing Request
    type: string
    default: ''
    required: false
    description: ''
    validation: &id011
      displayOptions:
        show:
          operation:
          - create
          resource:
          - certificateRequest
          generateCsr:
          - false
    typeInfo: &id012
      type: string
      displayName: Certificate Signing Request
      name: certificateSigningRequest
- id: create
  name: Create
  description: Create a new certificate request
  params:
  - id: applicationId
    name: Application Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: certificateIssuingTemplateId
    name: Certificate Issuing Template Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id009
    typeInfo: *id010
  - id: generateCsr
    name: Generate CSR
    type: boolean
    default: false
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - certificateRequest
    typeInfo:
      type: boolean
      displayName: Generate CSR
      name: generateCsr
  - id: commonName
    name: Common Name
    type: string
    default: n8n.io
    required: true
    description: The Common Name field for the certificate Subject (CN)
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - certificateRequest
          generateCsr:
          - true
    typeInfo:
      type: string
      displayName: Common Name
      name: commonName
  - id: certificateSigningRequest
    name: Certificate Signing Request
    type: string
    default: ''
    required: false
    description: ''
    validation: *id011
    typeInfo: *id012
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - content-type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: options
    text: Add Field
  - field: filters
    text: Add Field
  - field: options
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add Field
  hints:
  - field: options
    text: e.g. 1 year -> P1Y
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
  "$id": "https://n8n.io/schemas/nodes/venafiTlsProtectCloud.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Venafi TLS Protect Cloud Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "delete",
        "download",
        "get",
        "getMany",
        "renew",
        "create"
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
            "certificate",
            "certificateRequest"
          ],
          "default": "certificateRequest"
        },
        "operation": {
          "description": "Create a new certificate request",
          "type": "string",
          "enum": [
            "create",
            "get",
            "getMany"
          ],
          "default": "create"
        },
        "certificateId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "downloadItem": {
          "description": "",
          "type": "string",
          "enum": [
            "certificate",
            "keystore"
          ],
          "default": "certificate"
        },
        "keystoreType": {
          "description": "",
          "type": "string",
          "enum": [
            "JKS",
            "PKCS12",
            "PEM"
          ],
          "default": "PEM"
        },
        "certificateLabel": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "privateKeyPassphrase": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "keystorePassphrase": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "binaryProperty": {
          "description": "The name of the input field containing the binary file data to be uploaded",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "Specify how long the issued certificate should be valid for. Use ISO8601 format.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 50
        },
        "filters": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "applicationId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "existingCertificateId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "certificateIssuingTemplateId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "certificateSigningRequest": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "generateCsr": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "commonName": {
          "description": "The Common Name field for the certificate Subject (CN)",
          "type": "string",
          "default": "n8n.io"
        },
        "additionalFields": {
          "description": "Elliptic Curve (EC)",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "certificateRequestId": {
          "description": "",
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
      "name": "venafiTlsProtectCloudApi",
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
