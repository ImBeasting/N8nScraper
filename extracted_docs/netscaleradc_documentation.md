---
title: "Node: Netscaler ADC"
slug: "node-netscaleradc"
version: "1"
updated: "2025-11-13"
summary: "Consume Netscaler ADC API"
node_type: "regular"
group: "['output']"
---

# Node: Netscaler ADC

**Purpose.** Consume Netscaler ADC API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:netscaler.svg', 'dark': 'file:netscaler.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **citrixAdcApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `citrixAdcApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Certificate Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a certificate |
| Install | `install` | Install a certificate |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a file |
| Download | `download` | Download a file |
| Upload | `upload` | Upload a file |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | file | ✗ | Resource to operate on |  |

**Resource options:**

* **Certificate** (`certificate`)
* **File** (`file`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create a certificate
* **Install** (`install`) - Install a certificate

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate File Name | `certificateFileName` | string |  | ✓ | Name for and, optionally, path to the generated certificate file. /nsconfig/ssl/ is the default path. |  |
| Certificate Format | `certificateFormat` | options | PEM | ✓ | Format in which the certificate is stored on the appliance |  |

**Certificate Format options:**

* **PEM** (`PEM`)
* **DER** (`DER`)

| Certificate Type | `certificateType` | options | ROOT_CERT | ✓ | You must specify the key file name. The generated Root-CA certificate can be used for signing end-user client or server certificates or to create Intermediate-CA certificates. |  |

**Certificate Type options:**

* **Root-CA** (`ROOT_CERT`) - You must specify the key file name. The generated Root-CA certificate can be used for signing end-user client or server certificates or to create Intermediate-CA certificates.
* **Intermediate-CA** (`INTM_CERT`) - Intermediate-CA certificate
* **Server** (`SRVR_CERT`) - SSL server certificate used on SSL servers for end-to-end encryption
* **Client** (`CLNT_CERT`) - End-user client certificate used for client authentication

| Certificate Request File Name | `certificateRequestFileName` | string |  | ✓ | Name for and, optionally, path to the certificate-signing request (CSR). /nsconfig/ssl/ is the default path. |  |
| CA Certificate File Name | `caCertificateFileName` | string |  | ✓ | Name of the CA certificate file that issues and signs the Intermediate-CA certificate or the end-user client and server certificates |  |
| CA Certificate File Format | `caCertificateFileFormat` | options | PEM | ✓ | Format of the CA certificate |  |

**CA Certificate File Format options:**

* **PEM** (`PEM`)
* **DER** (`DER`)

| CA Private Key File Name | `caPrivateKeyFileName` | string |  | ✓ | Private key, associated with the CA certificate that is used to sign the Intermediate-CA certificate or the end-user client and server certificate. If the CA key file is password protected, the user is prompted to enter the pass phrase that was used to encrypt the key. |  |
| CA Private Key File Format | `caPrivateKeyFileFormat` | options | PEM | ✓ | Format of the CA certificate |  |

**CA Private Key File Format options:**

* **PEM** (`PEM`)
* **DER** (`DER`)

| Private Key File Name | `privateKeyFileName` | string |  | ✓ | Name for and, optionally, path to the private key. You can either use an existing RSA or DSA key that you own or create a new private key on the Netscaler ADC. This file is required only when creating a self-signed Root-CA certificate. The key file is stored in the /nsconfig/ssl directory by default. |  |
| CA Serial File Number | `caSerialFileNumber` | string |  | ✓ | Serial number file maintained for the CA certificate. This file contains the serial number of the next certificate to be issued or signed by the CA. |  |
| Private Key Format | `privateKeyFormat` | options | PEM | ✓ | Format in which the key is stored on the appliance |  |

**Private Key Format options:**

* **PEM** (`PEM`)
* **DER** (`DER`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Name for and, optionally, path to the private key. You can either use an existing RSA or DSA key that you own or create a new private key on the Netscaler ADC. This file is required only when creating a self-signed Root-CA certificate. The key file is stored in the /nsconfig/ssl directory by default. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| PEM Passphrase (For Encrypted Key) | `pempassphrase` | string |  | Name for and, optionally, path to the private key. You can either use an existing RSA or DSA key that you own or create a new private key on the Netscaler ADC. This file is required only when creating a self-signed Root-CA certificate. The key file is stored in the /nsconfig/ssl directory by default. |
| PEM Passphrase (For Encrypted CA Key) | `pempassphrase` | string |  | Name for and, optionally, path to the private key. You can either use an existing RSA or DSA key that you own or create a new private key on the Netscaler ADC. This file is required only when creating a self-signed Root-CA certificate. The key file is stored in the /nsconfig/ssl directory by default. |
| Subject Alternative Name | `subjectaltname` | string |  | Subject Alternative Name (SAN) is an extension to X.509 that allows various values to be associated with a security certificate using a subjectAltName field |
| Validity Period (Number of Days) | `days` | string |  | Number of days for which the certificate will be valid, beginning with the time and day (system time) of creation |

</details>


### Install parameters (`install`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Certificate-Key Pair Name | `certificateKeyPairName` | string |  | ✓ | Name for the certificate and private-key pair |  |
| Certificate File Name | `certificateFileName` | string |  | ✓ | Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key pair. /nsconfig/ssl/ is the default path. |  |
| Private Key File Name | `privateKeyFileName` | string |  | ✓ | Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key pair. /nsconfig/ssl/ is the default path. |  |
| Certificate Format | `certificateFormat` | options | PEM | ✓ | Input format of the certificate and the private-key files. The three formats supported by the appliance are: PEM - Privacy Enhanced Mail DER - Distinguished Encoding Rule PFX - Personal Information Exchange. |  |

**Certificate Format options:**

* **PEM** (`PEM`)
* **DER** (`DER`)

| Password | `password` | string |  | ✓ | Input format of the certificate and the private-key files. The three formats supported by the appliance are: PEM - Privacy Enhanced Mail DER - Distinguished Encoding Rule PFX - Personal Information Exchange. |  |
| Notify When Expires | `notifyExpiration` | boolean | False | ✓ | Whether to alert when the certificate is about to expire |  |
| Notification Period (Days) | `notificationPeriod` | number | 10 | ✓ | Time, in number of days, before certificate expiration, at which to generate an alert that the certificate is about to expire | min:10, max:100 |
| Certificate Bundle | `certificateBundle` | boolean | False | ✗ | Whether to parse the certificate chain as a single file after linking the server certificate to its issuer's certificate within the file |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Location | `fileLocation` | string | /nsconfig/ssl/ | ✓ |  |  |
| File Name | `fileName` | string |  | ✓ | Name of the file. It should not include filepath. |  |

### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Location | `fileLocation` | string | /nsconfig/ssl/ | ✓ |  |  |
| File Name | `fileName` | string |  | ✓ | Name of the file. It should not include filepath. |  |
| Put Output in Field | `binaryProperty` | string | data | ✓ | The name of the output field to put the binary file data in |  |

### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Location | `fileLocation` | string | /nsconfig/ssl/ | ✓ |  |  |
| Input Data Field Name | `binaryProperty` | string | data | ✓ | The name of the incoming field containing the binary file data to be processed |  |
| Options | `options` | collection | {} | ✗ | Name of the file. It should not include filepath. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Name | `fileName` | string |  | Name of the file. It should not include filepath. |

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
* Aliases: Citrix

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: netscalerAdc
displayName: Netscaler ADC
description: Consume Netscaler ADC API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: citrixAdcApi
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: certificateFileName
    name: Certificate File Name
    type: string
    default: ''
    required: true
    description: Name for and, optionally, path to the generated certificate file.
      /nsconfig/ssl/ is the default path.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - install
    typeInfo: &id002
      type: string
      displayName: Certificate File Name
      name: certificateFileName
  - id: certificateFormat
    name: Certificate Format
    type: options
    default: PEM
    required: true
    description: Format in which the certificate is stored on the appliance
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - install
    typeInfo: &id006
      type: options
      displayName: Certificate Format
      name: certificateFormat
      possibleValues:
      - value: PEM
        name: PEM
        description: ''
      - value: DER
        name: DER
        description: ''
  - id: certificateType
    name: Certificate Type
    type: options
    default: ROOT_CERT
    required: true
    description: You must specify the key file name. The generated Root-CA certificate
      can be used for signing end-user client or server certificates or to create
      Intermediate-CA certificates.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - create
    typeInfo:
      type: options
      displayName: Certificate Type
      name: certificateType
      possibleValues:
      - value: ROOT_CERT
        name: Root-CA
        description: You must specify the key file name. The generated Root-CA certificate
          can be used for signing end-user client or server certificates or to create
          Intermediate-CA certificates.
      - value: INTM_CERT
        name: Intermediate-CA
        description: Intermediate-CA certificate
      - value: SRVR_CERT
        name: Server
        description: SSL server certificate used on SSL servers for end-to-end encryption
      - value: CLNT_CERT
        name: Client
        description: End-user client certificate used for client authentication
  - id: certificateRequestFileName
    name: Certificate Request File Name
    type: string
    default: ''
    required: true
    description: Name for and, optionally, path to the certificate-signing request
      (CSR). /nsconfig/ssl/ is the default path.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - certificate
    typeInfo:
      type: string
      displayName: Certificate Request File Name
      name: certificateRequestFileName
  - id: caCertificateFileName
    name: CA Certificate File Name
    type: string
    default: ''
    required: true
    description: Name of the CA certificate file that issues and signs the Intermediate-CA
      certificate or the end-user client and server certificates
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - create
          certificateType:
          - INTM_CERT
          - SRVR_CERT
          - CLNT_CERT
    typeInfo:
      type: string
      displayName: CA Certificate File Name
      name: caCertificateFileName
  - id: caCertificateFileFormat
    name: CA Certificate File Format
    type: options
    default: PEM
    required: true
    description: Format of the CA certificate
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - create
          certificateType:
          - INTM_CERT
          - SRVR_CERT
          - CLNT_CERT
    typeInfo:
      type: options
      displayName: CA Certificate File Format
      name: caCertificateFileFormat
      possibleValues:
      - value: PEM
        name: PEM
        description: ''
      - value: DER
        name: DER
        description: ''
  - id: caPrivateKeyFileName
    name: CA Private Key File Name
    type: string
    default: ''
    required: true
    description: Private key, associated with the CA certificate that is used to sign
      the Intermediate-CA certificate or the end-user client and server certificate.
      If the CA key file is password protected, the user is prompted to enter the
      pass phrase that was used to encrypt the key.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - create
          certificateType:
          - INTM_CERT
          - SRVR_CERT
          - CLNT_CERT
    typeInfo:
      type: string
      displayName: CA Private Key File Name
      name: caPrivateKeyFileName
  - id: caPrivateKeyFileFormat
    name: CA Private Key File Format
    type: options
    default: PEM
    required: true
    description: Format of the CA certificate
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - create
          certificateType:
          - INTM_CERT
          - SRVR_CERT
          - CLNT_CERT
    typeInfo:
      type: options
      displayName: CA Private Key File Format
      name: caPrivateKeyFileFormat
      possibleValues:
      - value: PEM
        name: PEM
        description: ''
      - value: DER
        name: DER
        description: ''
  - id: privateKeyFileName
    name: Private Key File Name
    type: string
    default: ''
    required: true
    description: Name for and, optionally, path to the private key. You can either
      use an existing RSA or DSA key that you own or create a new private key on the
      Netscaler ADC. This file is required only when creating a self-signed Root-CA
      certificate. The key file is stored in the /nsconfig/ssl directory by default.
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - install
    typeInfo: &id004
      type: string
      displayName: Private Key File Name
      name: privateKeyFileName
  - id: caSerialFileNumber
    name: CA Serial File Number
    type: string
    default: ''
    required: true
    description: Serial number file maintained for the CA certificate. This file contains
      the serial number of the next certificate to be issued or signed by the CA.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - create
          certificateType:
          - INTM_CERT
          - SRVR_CERT
          - CLNT_CERT
    typeInfo:
      type: string
      displayName: CA Serial File Number
      name: caSerialFileNumber
  - id: privateKeyFormat
    name: Private Key Format
    type: options
    default: PEM
    required: true
    description: Format in which the key is stored on the appliance
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - create
          certificateType:
          - ROOT_CERT
    typeInfo:
      type: options
      displayName: Private Key Format
      name: privateKeyFormat
      possibleValues:
      - value: PEM
        name: PEM
        description: ''
      - value: DER
        name: DER
        description: ''
- id: install
  name: Install
  description: ''
  params:
  - id: certificateKeyPairName
    name: Certificate-Key Pair Name
    type: string
    default: ''
    required: true
    description: Name for the certificate and private-key pair
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - install
    typeInfo:
      type: string
      displayName: Certificate-Key Pair Name
      name: certificateKeyPairName
  - id: certificateFileName
    name: Certificate File Name
    type: string
    default: ''
    required: true
    description: Name of and, optionally, path to the X509 certificate file that is
      used to form the certificate-key pair. /nsconfig/ssl/ is the default path.
    validation: *id001
    typeInfo: *id002
  - id: privateKeyFileName
    name: Private Key File Name
    type: string
    default: ''
    required: true
    description: Name of and, optionally, path to the X509 certificate file that is
      used to form the certificate-key pair. /nsconfig/ssl/ is the default path.
    validation: *id003
    typeInfo: *id004
  - id: certificateFormat
    name: Certificate Format
    type: options
    default: PEM
    required: true
    description: 'Input format of the certificate and the private-key files. The three
      formats supported by the appliance are: PEM - Privacy Enhanced Mail DER - Distinguished
      Encoding Rule PFX - Personal Information Exchange.'
    validation: *id005
    typeInfo: *id006
  - id: password
    name: Password
    type: string
    default: ''
    required: true
    description: 'Input format of the certificate and the private-key files. The three
      formats supported by the appliance are: PEM - Privacy Enhanced Mail DER - Distinguished
      Encoding Rule PFX - Personal Information Exchange.'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - install
          certificateFormat:
          - PEM
    typeInfo:
      type: string
      displayName: Password
      name: password
      typeOptions:
        password: true
  - id: notifyExpiration
    name: Notify When Expires
    type: boolean
    default: false
    required: true
    description: Whether to alert when the certificate is about to expire
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - install
    typeInfo:
      type: boolean
      displayName: Notify When Expires
      name: notifyExpiration
  - id: notificationPeriod
    name: Notification Period (Days)
    type: number
    default: 10
    required: true
    description: Time, in number of days, before certificate expiration, at which
      to generate an alert that the certificate is about to expire
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - install
          notifyExpiration:
          - true
    typeInfo:
      type: number
      displayName: Notification Period (Days)
      name: notificationPeriod
      typeOptions:
        minValue: 10
        maxValue: 100
  - id: certificateBundle
    name: Certificate Bundle
    type: boolean
    default: false
    required: false
    description: Whether to parse the certificate chain as a single file after linking
      the server certificate to its issuer's certificate within the file
    validation:
      displayOptions:
        show:
          resource:
          - certificate
          operation:
          - install
          certificateFormat:
          - PEM
    typeInfo:
      type: boolean
      displayName: Certificate Bundle
      name: certificateBundle
- id: delete
  name: Delete
  description: ''
  params:
  - id: fileLocation
    name: File Location
    type: string
    default: /nsconfig/ssl/
    required: true
    description: ''
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - delete
          - download
          resource:
          - file
    typeInfo: &id008
      type: string
      displayName: File Location
      name: fileLocation
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: true
    description: Name of the file. It should not include filepath.
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - delete
          - download
          resource:
          - file
    typeInfo: &id010
      type: string
      displayName: File Name
      name: fileName
- id: download
  name: Download
  description: ''
  params:
  - id: fileLocation
    name: File Location
    type: string
    default: /nsconfig/ssl/
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: true
    description: Name of the file. It should not include filepath.
    validation: *id009
    typeInfo: *id010
  - id: binaryProperty
    name: Put Output in Field
    type: string
    default: data
    required: true
    description: The name of the output field to put the binary file data in
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - download
          resource:
          - file
    typeInfo: &id012
      type: string
      displayName: Put Output in Field
      name: binaryProperty
- id: upload
  name: Upload
  description: ''
  params:
  - id: fileLocation
    name: File Location
    type: string
    default: /nsconfig/ssl/
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: binaryProperty
    name: Input Data Field Name
    type: string
    default: data
    required: true
    description: The name of the incoming field containing the binary file data to
      be processed
    validation: *id011
    typeInfo: *id012
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
  "$id": "https://n8n.io/schemas/nodes/netscalerAdc.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Netscaler ADC Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "install",
        "delete",
        "download",
        "upload"
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
            "file"
          ],
          "default": "file"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "delete",
            "download",
            "upload"
          ],
          "default": "upload"
        },
        "certificateFileName": {
          "description": "Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key pair. /nsconfig/ssl/ is the default path.",
          "type": "string",
          "default": ""
        },
        "certificateFormat": {
          "description": "Input format of the certificate and the private-key files. The three formats supported by the appliance are: PEM - Privacy Enhanced Mail DER - Distinguished Encoding Rule PFX - Personal Information Exchange.",
          "type": "string",
          "enum": [
            "PEM",
            "DER"
          ],
          "default": "PEM"
        },
        "certificateType": {
          "description": "You must specify the key file name. The generated Root-CA certificate can be used for signing end-user client or server certificates or to create Intermediate-CA certificates.",
          "type": "string",
          "enum": [
            "ROOT_CERT",
            "INTM_CERT",
            "SRVR_CERT",
            "CLNT_CERT"
          ],
          "default": "ROOT_CERT"
        },
        "certificateRequestFileName": {
          "description": "Name for and, optionally, path to the certificate-signing request (CSR). /nsconfig/ssl/ is the default path.",
          "type": "string",
          "default": ""
        },
        "caCertificateFileName": {
          "description": "Name of the CA certificate file that issues and signs the Intermediate-CA certificate or the end-user client and server certificates",
          "type": "string",
          "default": ""
        },
        "caCertificateFileFormat": {
          "description": "Format of the CA certificate",
          "type": "string",
          "enum": [
            "PEM",
            "DER"
          ],
          "default": "PEM"
        },
        "caPrivateKeyFileName": {
          "description": "Private key, associated with the CA certificate that is used to sign the Intermediate-CA certificate or the end-user client and server certificate. If the CA key file is password protected, the user is prompted to enter the pass phrase that was used to encrypt the key.",
          "type": "string",
          "default": ""
        },
        "caPrivateKeyFileFormat": {
          "description": "Format of the CA certificate",
          "type": "string",
          "enum": [
            "PEM",
            "DER"
          ],
          "default": "PEM"
        },
        "privateKeyFileName": {
          "description": "Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key pair. /nsconfig/ssl/ is the default path.",
          "type": "string",
          "default": ""
        },
        "caSerialFileNumber": {
          "description": "Serial number file maintained for the CA certificate. This file contains the serial number of the next certificate to be issued or signed by the CA.",
          "type": "string",
          "default": ""
        },
        "privateKeyFormat": {
          "description": "Format in which the key is stored on the appliance",
          "type": "string",
          "enum": [
            "PEM",
            "DER"
          ],
          "default": "PEM"
        },
        "additionalFields": {
          "description": "Name for and, optionally, path to the private key. You can either use an existing RSA or DSA key that you own or create a new private key on the Netscaler ADC. This file is required only when creating a self-signed Root-CA certificate. The key file is stored in the /nsconfig/ssl directory by default.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "certificateKeyPairName": {
          "description": "Name for the certificate and private-key pair",
          "type": "string",
          "default": ""
        },
        "password": {
          "description": "Input format of the certificate and the private-key files. The three formats supported by the appliance are: PEM - Privacy Enhanced Mail DER - Distinguished Encoding Rule PFX - Personal Information Exchange.",
          "type": "string",
          "default": ""
        },
        "notifyExpiration": {
          "description": "Whether to alert when the certificate is about to expire",
          "type": "boolean",
          "default": false
        },
        "notificationPeriod": {
          "description": "Time, in number of days, before certificate expiration, at which to generate an alert that the certificate is about to expire",
          "type": "number",
          "default": 10
        },
        "certificateBundle": {
          "description": "Whether to parse the certificate chain as a single file after linking the server certificate to its issuer's certificate within the file",
          "type": "boolean",
          "default": false
        },
        "fileLocation": {
          "description": "",
          "type": "string",
          "default": "/nsconfig/ssl/"
        },
        "binaryProperty": {
          "description": "The name of the output field to put the binary file data in",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "Name of the file. It should not include filepath.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "fileName": {
          "description": "Name of the file. It should not include filepath.",
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
      "name": "citrixAdcApi",
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
