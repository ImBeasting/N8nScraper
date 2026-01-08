---
title: "Node: Venafi TLS Protect Datacenter"
slug: "node-venafitlsprotectdatacenter"
version: "1"
updated: "2026-01-08"
summary: "Consume Venafi TLS Protect Datacenter"
node_type: "regular"
group: "['input']"
---

# Node: Venafi TLS Protect Datacenter

**Purpose.** Consume Venafi TLS Protect Datacenter
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:../venafi.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **venafiTlsProtectDatacenterApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `venafiTlsProtectDatacenterApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Certificate Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Provision a new certificate |
| Delete | `delete` | Delete a certificate |
| Download | `download` | Download a certificate |
| Get | `get` | Retrieve a certificate |
| Get Many | `getMany` | Retrieve many certificates |
| Renew | `renew` | Renew a certificate |

### Policy Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a policy |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | certificate | ✗ | Resource to operate on |  |

**Resource options:**

* **Certificate** (`certificate`)
* **Policy** (`policy`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Provision a new certificate |  |

**Operation options:**

* **Create** (`create`) - Provision a new certificate
* **Delete** (`delete`) - Delete a certificate
* **Download** (`download`) - Download a certificate
* **Get** (`get`) - Retrieve a certificate
* **Get Many** (`getMany`) - Retrieve many certificates
* **Renew** (`renew`) - Renew a certificate

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Policy DN | `PolicyDN` | string |  | ✗ | The folder DN for the new certificate. If the value is missing, the folder name is the system default. If no system default is configured |  |
| Subject | `Subject` | string |  | ✗ | The Common Name field for the certificate Subject (DN) |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | An array of one or more identities for certificate workflow approvers | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Approvers | `Approvers` | string |  | An array of one or more identities for certificate workflow approvers |
| CADN | `CADN` | string |  | Only required when no policy sets a CA template. The Distinguished Name (DN) of the Trust Protection Platform Certificate Authority Template object for enrolling the certificate. |
| Certificate Type | `CertificateType` | options |  | X.509 Code Signing Certificate |
| City | `City` | string |  | The City field for the certificate Subject DN. Specify a value when requesting a centrally generated CSR. |
| Contacts | `Contacts` | string | [] | An array of one or more identities for users or groups who receive notifications about events pertaining to the object |
| Country | `Country` | string |  | The Country field for the certificate Subject DN. Specify a value when requesting a centrally generated CSR. |
| Custom Fields | `customFieldsUi` | fixedCollection | {} |  |
| Created By | `CreatedBy` | string | Web SDK | The person, entity, or caller of this request. The default is Web SDK. Avoid overriding the default unless the caller is a significant enterprise application that is tightly integrated with Trust Protection Platform, such as a custom web portal. To add details, use Origin instead. If you want both attributes to have the same value, set only CreatedBy. |
| Devices | `Devices` | collection | {} | An array of one or more Application objects to allow software, which runs on ObjectName, to use the same certificate |
| Disable Automatic Renewal | `DisableAutomaticRenewal` | boolean | False | The setting to control whether manual intervention is required for certificate renewal |
| Elliptic Curve | `EllipticCurve` | options |  | Use Elliptic Prime Curve 256 bit encryption |
| Key Algorithm | `KeyAlgorithm` | options |  | Rivest, Shamir, Adleman key (RSA) |
| Key Bit Size | `KeyBitSize` | number | 2048 | Use this parameter when KeyAlgorithm is RSA. The number of bits to allow for key generation. |
| Management Type | `ManagementType` | options |  | Issue a new certificate, renewcertificate, or key generation request to a CA for enrollment |
| Origin | `origin` | string | Web SDK | Additional information, such as the name and version of the calling application, that describes the source of this enrollment, renewal, or provisioning request. The default is Web SDK. |
| Organization | `Organization` | string |  | The Organization field for the certificate Subject DN. Specify a value when the CSR centrally generates. |
| Organizational Unit | `OrganizationalUnit` | string |  | The department or division within the organization that is responsible for maintaining the certificate |
| PKCS10 | `PKCS10` | string |  | The PKCS#10 Certificate Signing Request (CSR). Omit escape characters such as or . If this value is provided, any Subject DN fields and the KeyBitSize in the request are ignored. |
| Reenable | `Reenable` | boolean | False | The action to control a previously disabled certificate |
| Set Work To Do | `SetWorkToDo` | boolean | False | The setting to control certificate processing |
| State | `State` | string |  | The State field for the certificate Subject DN. Specify a value when requesting a centrally generated CSR. |
| Subject Alt Names | `SubjectAltNamesUi` | fixedCollection | {} | Specify a Uniform Resource Name (URN) or username |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate GUID | `certificateId` | string |  | ✓ | A GUID that uniquely identifies the certificate |  |

### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate DN | `certificateDn` | string |  | ✓ |  |  |
| Include Private Key | `includePrivateKey` | boolean | False | ✗ |  |  |
| Password | `password` | string |  | ✓ |  |  |
| Input Data Field Name | `binaryProperty` | string | data | ✓ | The name of the input field containing the binary file data to be uploaded |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Chain | `IncludeChain` | boolean | True |  |
| Root First Order | `RootFirstOrder` | string |  |  |
| Keystore Password | `KeystorePassword` | string |  |  |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate GUID | `certificateId` | string |  | ✓ | A GUID that uniquely identifies the certificate |  |
| Policy DN | `policyDn` | string |  | ✓ | The Distinguished Name (DN) of the policy folder |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The PKCS#10 policy Signing Request (CSR). Omit escape characters such as or . If this value is provided, any Subject DN fields and the KeyBitSize in the request are ignored. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| PKCS10 | `PKCS10` | string |  | The PKCS#10 policy Signing Request (CSR). Omit escape characters such as or . If this value is provided, any Subject DN fields and the KeyBitSize in the request are ignored. |

</details>


### Get Many parameters (`getMany`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Include one or more of the following certificate attributes in the return value | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | multiOptions | [] | Include one or more of the following certificate attributes in the return value |

</details>


### Renew parameters (`renew`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate DN | `certificateDN` | string |  | ✓ | The Distinguished Name (DN) of the certificate to renew |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The PKCS#10 Certificate Signing Request (CSR). Omit escape characters such as or . If this value is provided, any Subject DN fields and the KeyBitSize in the request are ignored. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| PKCS10 | `PKCS10` | string |  | The PKCS#10 Certificate Signing Request (CSR). Omit escape characters such as or . If this value is provided, any Subject DN fields and the KeyBitSize in the request are ignored. |
| Reenable | `Reenable` | boolean | False | The action to control a previously disabled certificate |

</details>


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
node: venafiTlsProtectDatacenter
displayName: Venafi TLS Protect Datacenter
description: Consume Venafi TLS Protect Datacenter
version: '1'
nodeType: regular
group:
- input
credentials:
- name: venafiTlsProtectDatacenterApi
  required: true
operations:
- id: create
  name: Create
  description: Provision a new certificate
  params:
  - id: PolicyDN
    name: Policy DN
    type: string
    default: ''
    required: false
    description: The folder DN for the new certificate. If the value is missing, the
      folder name is the system default. If no system default is configured
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - certificate
    typeInfo:
      type: string
      displayName: Policy DN
      name: PolicyDN
  - id: Subject
    name: Subject
    type: string
    default: ''
    required: false
    description: The Common Name field for the certificate Subject (DN)
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - certificate
    typeInfo:
      type: string
      displayName: Subject
      name: Subject
- id: delete
  name: Delete
  description: Delete a certificate
  params:
  - id: certificateId
    name: Certificate GUID
    type: string
    default: ''
    required: true
    description: A GUID that uniquely identifies the certificate
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
      displayName: Certificate GUID
      name: certificateId
- id: download
  name: Download
  description: Download a certificate
  params:
  - id: certificateDn
    name: Certificate DN
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
    typeInfo:
      type: string
      displayName: Certificate DN
      name: certificateDn
  - id: includePrivateKey
    name: Include Private Key
    type: boolean
    default: false
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - download
    typeInfo:
      type: boolean
      displayName: Include Private Key
      name: includePrivateKey
  - id: password
    name: Password
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
          - download
          includePrivateKey:
          - true
    typeInfo:
      type: string
      displayName: Password
      name: password
      typeOptions:
        password: true
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
    name: Certificate GUID
    type: string
    default: ''
    required: true
    description: A GUID that uniquely identifies the certificate
    validation: *id001
    typeInfo: *id002
  - id: policyDn
    name: Policy DN
    type: string
    default: ''
    required: true
    description: The Distinguished Name (DN) of the policy folder
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - policy
    typeInfo:
      type: string
      displayName: Policy DN
      name: policyDn
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
- id: renew
  name: Renew
  description: Renew a certificate
  params:
  - id: certificateDN
    name: Certificate DN
    type: string
    default: ''
    required: true
    description: The Distinguished Name (DN) of the certificate to renew
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - renew
          resource:
          - certificate
    typeInfo:
      type: string
      displayName: Certificate DN
      name: certificateDN
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: additionalFields
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
  "$id": "https://n8n.io/schemas/nodes/venafiTlsProtectDatacenter.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Venafi TLS Protect Datacenter Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "download",
        "get",
        "getMany",
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
            "certificate",
            "policy"
          ],
          "default": "certificate"
        },
        "operation": {
          "description": "Get a policy",
          "type": "string",
          "enum": [
            "get"
          ],
          "default": "get"
        },
        "PolicyDN": {
          "description": "The folder DN for the new certificate. If the value is missing, the folder name is the system default. If no system default is configured",
          "type": "string",
          "default": ""
        },
        "Subject": {
          "description": "The Common Name field for the certificate Subject (DN)",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The PKCS#10 policy Signing Request (CSR). Omit escape characters such as or . If this value is provided, any Subject DN fields and the KeyBitSize in the request are ignored.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "certificateDn": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "includePrivateKey": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "password": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "binaryProperty": {
          "description": "The name of the input field containing the binary file data to be uploaded",
          "type": "string",
          "default": "data"
        },
        "certificateId": {
          "description": "A GUID that uniquely identifies the certificate",
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
          "description": "Include one or more of the following certificate attributes in the return value",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "certificateDN": {
          "description": "The Distinguished Name (DN) of the certificate to renew",
          "type": "string",
          "default": ""
        },
        "policyDn": {
          "description": "The Distinguished Name (DN) of the policy folder",
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
      "name": "venafiTlsProtectDatacenterApi",
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
