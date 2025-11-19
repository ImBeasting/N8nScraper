---
title: "Node: Google Cloud Storage"
slug: "node-googlecloudstorage"
version: "1"
updated: "2025-11-13"
summary: "Use the Google Cloud Storage API"
node_type: "regular"
group: "['transform']"
---

# Node: Google Cloud Storage

**Purpose.** Use the Google Cloud Storage API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:googleCloudStorage.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleCloudStorageOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleCloudStorageOAuth2Api` | ✓ | - |

---

## Operations

### Bucket Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Object Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | bucket | ✗ | Resource to operate on |  |

**Resource options:**

* **Bucket** (`bucket`)
* **Object** (`object`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | bucket | ✗ |  |  |

**Resource options:**

* **Bucket** (`bucket`)
* **Object** (`object`)

| Operation | `operation` | options | getAll | ✗ | Create a new Bucket |  |
| Project ID | `projectId` | string |  | ✓ | e.g. Project ID |  |
| Bucket Name | `bucketName` | string |  | ✓ | e.g. Bucket Name |  |
| Prefix | `prefix` | string |  | ✗ | e.g. Filter for Bucket Names |  |
| Projection | `projection` | options | noAcl | ✗ |  |  |

**Projection options:**

* **All Properties** (`full`)
* **No ACL** (`noAcl`)

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Filters | `getFilters` | collection | {} | ✗ | Only return data if the metageneration value of the Bucket matches the sent value | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Metageneration Match | `ifMetagenerationMatch` | number | 0 | Only return data if the metageneration value of the Bucket matches the sent value |
| Metageneration Exclude | `ifMetagenerationNotMatch` | number | 0 | Only return data if the metageneration value of the Bucket does not match the sent value |

</details>

| Predefined Access Control | `createAcl` | collection | {} | ✗ | e.g. Add Access Control Parameters |  |

<details>
<summary><strong>Predefined Access Control sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Predefined ACL | `predefinedAcl` | options | authenticatedRead |  |
| Predefined Default Object ACL | `predefinedDefaultObjectAcl` | options | authenticatedRead |  |

</details>

| Additional Parameters | `createBody` | collection | {} | ✗ | e.g. Add Metadata Parameter |  |

<details>
<summary><strong>Additional Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Access Control | `acl` | json | [] |  |
| Billing | `billing` | json | {} |  |
| CORS | `cors` | json | [] |  |
| Custom Placement Config | `customPlacementConfig` | json | {} |  |
| Data Locations | `dataLocations` | json | [] |  |
| Default Event Based Hold | `defaultEventBasedHold` | boolean | True |  |
| Default Object ACL | `defaultObjectAcl` | json | [] |  |
| Encryption | `encryption` | json | {} |  |
| IAM Configuration | `iamConfiguration` | json | {} |  |
| Labels | `labels` | json | {} |  |
| Lifecycle | `lifecycle` | json | {} |  |
| Location | `location` | string | US |  |
| Logging | `logging` | json | {} |  |
| Retention Policy | `retentionPolicy` | json | {} |  |
| Recovery Point Objective | `rpo` | string | DEFAULT |  |
| Storage Class | `storageClass` | string | STANDARD |  |
| Versioning | `versioning` | json | {} |  |
| Website | `website` | json | {} |  |

</details>

| Operation | `operation` | options | getAll | ✗ | Create an object |  |
| Bucket Name | `bucketName` | string |  | ✓ | e.g. Bucket Name |  |
| Object Name | `objectName` | string |  | ✓ | e.g. Object Name |  |
| Projection | `projection` | options | noAcl | ✗ |  |  |

**Projection options:**

* **All Properties** (`full`)
* **No ACL** (`noAcl`)

| Projection | `updateProjection` | options | full | ✗ |  |  |

**Projection options:**

* **All Properties** (`full`)
* **No ACL** (`noAcl`)

| Return Data | `alt` | options | json | ✗ | e.g. The type of data to return from the request |  |

**Return Data options:**

* **Metadata** (`json`)
* **Object Data** (`media`)

| Use Input Binary Field | `createFromBinary` | boolean | True | ✗ | Whether the data for creating a file should come from a binary field |  |
| Input Binary Field | `createBinaryPropertyName` | string | data | ✗ | e.g. The name of the input binary field containing the file to be written |  |
| File Content | `createContent` | string |  | ✗ | Content of the file to be uploaded |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✗ | e.g. The name of the output binary field to put the file in |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `maxResults` | number | 100 | ✗ | Max number of results to return | min:1, max:1000 |
| Create Fields | `createData` | collection | {} | ✗ | e.g. Add Create Body Field |  |

<details>
<summary><strong>Create Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Access Control List | `acl` | json | [] |  |
| Cache Control | `cacheControl` | string |  |  |
| Content Disposition | `contentDisposition` | string |  |  |
| Content Encoding | `contentEncoding` | string |  |  |
| Content Language | `contentLanguage` | string |  |  |
| Content Type | `contentType` | string |  |  |
| CRC32c Checksum | `crc32c` | string |  |  |
| Custom Time | `customTime` | string |  |  |
| Event Based Hold | `eventBasedHold` | boolean | False |  |
| MD5 Hash | `md5Hash` | string |  |  |
| Metadata | `metadata` | json | {} |  |
| Storage Class | `storageClass` | string |  |  |
| Temporary Hold | `temporaryHold` | boolean | False |  |

</details>

| Update Fields | `updateData` | collection | [] | ✗ | e.g. Add Update Body Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Access Control | `acl` | json | [] |  |
| Cache Control | `cacheControl` | string |  |  |
| Content Disposition | `contentDisposition` | string |  |  |
| Content Encoding | `contentEncoding` | string |  |  |
| Content Language | `contentLanguage` | string |  |  |
| Content Type | `contentType` | string |  |  |
| Custom Time | `customTime` | string |  |  |
| Event Based Hold | `eventBasedHold` | boolean | False |  |
| Metadata | `metadata` | json | {} |  |
| Temporary Hold | `temporaryHold` | boolean | False |  |

</details>

| Additional Parameters | `createQuery` | collection | {} | ✗ | e.g. Add Additional Parameters |  |

<details>
<summary><strong>Additional Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content Encoding | `contentEncoding` | string |  |  |
| KMS Key Name | `kmsKeyName` | string |  |  |

</details>

| Additional Parameters | `getParameters` | collection | {} | ✗ | e.g. Add Additional Parameters |  |
| Additional Parameters | `metagenAndAclQuery` | collection | {} | ✗ | e.g. Add Additional Parameters |  |
| Encryption Headers | `encryptionHeaders` | collection | {} | ✗ | e.g. Add Encryption Headers |  |

<details>
<summary><strong>Encryption Headers sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Encryption Algorithm | `X-Goog-Encryption-Algorithm` | options | AES256 |  |
| Encryption Key | `X-Goog-Encryption-Key` | string |  |  |
| Encryption Key Hash | `X-Goog-Encryption-Key-Sha256` | string |  |  |

</details>

| Additional Parameters | `listFilters` | collection | {} | ✗ | e.g. Add Additional Parameters |  |

<details>
<summary><strong>Additional Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Delimiter | `delimiter` | string | / |  |
| End Offset | `endOffset` | string |  |  |
| Include Trailing Delimiter | `includeTrailingDelimiter` | boolean | False |  |
| Prefix | `prefix` | string |  |  |
| Start Offset | `startOffset` | string |  |  |
| Versions | `versions` | boolean | False |  |

</details>

| Generation | `generation` | number |  | ✗ | e.g. Select a specific revision of the chosen object |  |
| Generation Match | `ifGenerationMatch` | number |  | ✗ | e.g. Make operation conditional of the object generation matching this value |  |
| Generation Exclude | `ifGenerationNotMatch` | number |  | ✗ | e.g. Make operation conditional of the object generation not matching this value |  |
| Metageneration Match | `ifMetagenerationMatch` | number |  | ✗ | e.g. Make operation conditional of the object's current metageneration matching this value |  |
| Metageneration Exclude | `ifMetagenerationNotMatch` | number |  | ✗ | e.g. Make operation conditional of the object's current metageneration not matching this value |  |

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
* Categories: Development, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleCloudStorage
displayName: Google Cloud Storage
description: Use the Google Cloud Storage API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: googleCloudStorageOAuth2Api
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: bucket
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: bucket
      name: Bucket
      description: ''
    - value: object
      name: Object
      description: ''
- id: operation
  name: Operation
  type: options
  default: getAll
  required: false
  description: Create a new Bucket
  validation: &id001
    displayOptions:
      show:
        resource:
        - object
  typeInfo: &id002
    type: options
    displayName: Operation
    name: operation
    possibleValues: []
- id: projectId
  name: Project ID
  type: string
  default: ''
  required: true
  description: ''
  placeholder: Project ID
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - bucket
        operation:
        - create
        - getAll
  typeInfo:
    type: string
    displayName: Project ID
    name: projectId
- id: bucketName
  name: Bucket Name
  type: string
  default: ''
  required: true
  description: ''
  placeholder: Bucket Name
  validation: &id003
    required: true
    displayOptions:
      show:
        resource:
        - object
  typeInfo: &id004
    type: string
    displayName: Bucket Name
    name: bucketName
- id: prefix
  name: Prefix
  type: string
  default: ''
  required: false
  description: ''
  placeholder: Filter for Bucket Names
  validation:
    displayOptions:
      show:
        resource:
        - bucket
        operation:
        - getAll
  typeInfo:
    type: string
    displayName: Prefix
    name: prefix
- id: projection
  name: Projection
  type: options
  default: noAcl
  required: false
  description: ''
  validation: &id005
    displayOptions:
      show:
        resource:
        - object
        operation:
        - get
        - getAll
  typeInfo: &id006
    type: options
    displayName: Projection
    name: projection
    possibleValues:
    - value: full
      name: All Properties
      description: ''
    - value: noAcl
      name: No ACL
      description: ''
- id: returnAll
  name: Return All
  type: boolean
  default: false
  required: false
  description: Whether to return all results or only up to a given limit
  validation: &id007
    displayOptions:
      show:
        resource:
        - object
        operation:
        - getAll
  typeInfo: &id008
    type: boolean
    displayName: Return All
    name: returnAll
- id: getFilters
  name: Filters
  type: collection
  default: {}
  required: false
  description: Only return data if the metageneration value of the Bucket matches
    the sent value
  placeholder: Add Filter
  validation:
    displayOptions:
      show:
        resource:
        - bucket
        operation:
        - delete
        - get
        - update
  typeInfo:
    type: collection
    displayName: Filters
    name: getFilters
    subProperties:
    - displayName: Metageneration Match
      name: ifMetagenerationMatch
      type: number
      description: Only return data if the metageneration value of the Bucket matches
        the sent value
      default: 0
      routing: "\n\t\t\t\t\trequest: {\n\t\t\t\t\t\tqs: {\n\t\t\t\t\t\t\tifMetagenerationMatch:\
        \ '={{$value"
    - displayName: Metageneration Exclude
      name: ifMetagenerationNotMatch
      type: number
      description: Only return data if the metageneration value of the Bucket does
        not match the sent value
      default: 0
      routing: "\n\t\t\t\t\trequest: {\n\t\t\t\t\t\tqs: {\n\t\t\t\t\t\t\tifMetagenerationNotMatch:\
        \ '={{$value"
- id: createAcl
  name: Predefined Access Control
  type: collection
  default: {}
  required: false
  description: ''
  placeholder: Add Access Control Parameters
  validation:
    displayOptions:
      show:
        resource:
        - bucket
        operation:
        - create
        - update
  typeInfo:
    type: collection
    displayName: Predefined Access Control
    name: createAcl
    subProperties:
    - displayName: Predefined ACL
      name: predefinedAcl
      type: options
      placeholder: Apply a predefined set of access controls to this bucket
      value: authenticatedRead
      default: authenticatedRead
      options:
      - name: Authenticated Read
        value: authenticatedRead
        displayName: Authenticated Read
      - name: Private
        value: private
        displayName: Private
      - name: Project Private
        value: projectPrivate
        displayName: Project Private
      - name: Public Read
        value: publicRead
        displayName: Public Read
      - name: Public Read/Write
        value: publicReadWrite
        displayName: Public Read/write
      routing: "\n\t\t\t\t\trequest: {\n\t\t\t\t\t\tqs: {\n\t\t\t\t\t\t\tpredefinedAcl:\
        \ '={{$value"
    - displayName: Predefined Default Object ACL
      name: predefinedDefaultObjectAcl
      type: options
      placeholder: Apply a predefined set of default object access controls to this
        bucket
      value: authenticatedRead
      default: authenticatedRead
      options:
      - name: Authenticated Read
        value: authenticatedRead
        displayName: Authenticated Read
      - name: Bucket Owner Full Control
        value: bucketOwnerFullControl
        displayName: Bucket Owner Full Control
      - name: Bucket Owner Read
        value: bucketOwnerRead
        displayName: Bucket Owner Read
      - name: Private
        value: private
        displayName: Private
      - name: Project Private
        value: projectPrivate
        displayName: Project Private
      - name: Public Read
        value: publicRead
        displayName: Public Read
      routing: "\n\t\t\t\t\trequest: {\n\t\t\t\t\t\tqs: {\n\t\t\t\t\t\t\tpredefinedObjectAcl:\
        \ '={{$value"
- id: createBody
  name: Additional Parameters
  type: collection
  default: {}
  required: false
  description: ''
  placeholder: Add Metadata Parameter
  validation:
    displayOptions:
      show:
        resource:
        - bucket
        operation:
        - create
        - update
  typeInfo:
    type: collection
    displayName: Additional Parameters
    name: createBody
    subProperties:
    - displayName: Access Control
      name: acl
      type: json
      placeholder: Access controls on the Bucket
      default: '[]'
    - displayName: Billing
      name: billing
      type: json
      placeholder: The bucket's billing configuration
      default: '{}'
    - displayName: CORS
      name: cors
      type: json
      placeholder: The bucket's Cross Origin Resource Sharing configuration
      default: '[]'
    - displayName: Custom Placement Config
      name: customPlacementConfig
      type: json
      placeholder: The configuration for the region(s) for the Bucket
      default: '{}'
    - displayName: Data Locations
      name: dataLocations
      type: json
      placeholder: The list of individual regions that comprise a dual-region Bucket
      default: '[]'
    - displayName: Default Event Based Hold
      name: defaultEventBasedHold
      type: boolean
      placeholder: Whether or not to automatically apply an event based hold to new
        objects
      default: true
    - displayName: Default Object ACL
      name: defaultObjectAcl
      type: json
      placeholder: Default Access Controls for new objects when no ACL is provided
      default: '[]'
    - displayName: Encryption
      name: encryption
      type: json
      placeholder: Encryption configuration for a bucket
      default: '{}'
    - displayName: IAM Configuration
      name: iamConfiguration
      type: json
      placeholder: The bucket's IAM configuration
      default: '{}'
    - displayName: Labels
      name: labels
      type: json
      placeholder: User provided bucket labels, in key/value pairs
      default: '{}'
    - displayName: Lifecycle
      name: lifecycle
      type: json
      placeholder: The bucket's lifecycle configuration
      default: '{}'
    - displayName: Location
      name: location
      type: string
      placeholder: The location of the bucket
      default: US
    - displayName: Logging
      name: logging
      type: json
      placeholder: The bucket's logging configuration
      default: '{}'
    - displayName: Retention Policy
      name: retentionPolicy
      type: json
      placeholder: The bucket's retention policy
      default: '{}'
    - displayName: Recovery Point Objective
      name: rpo
      type: string
      placeholder: The recovery point objective for the bucket
      default: DEFAULT
    - displayName: Storage Class
      name: storageClass
      type: string
      placeholder: The bucket's default storage class for objects that don't define
        one
      default: STANDARD
    - displayName: Versioning
      name: versioning
      type: json
      placeholder: The bucket's versioning configuration
      default: '{}'
    - displayName: Website
      name: website
      type: json
      placeholder: The bucket's website configuration for when it is used to host
        a website
      default: '{}'
- id: operation
  name: Operation
  type: options
  default: getAll
  required: false
  description: Create an object
  validation: *id001
  typeInfo: *id002
- id: bucketName
  name: Bucket Name
  type: string
  default: ''
  required: true
  description: ''
  placeholder: Bucket Name
  validation: *id003
  typeInfo: *id004
- id: objectName
  name: Object Name
  type: string
  default: ''
  required: true
  description: ''
  placeholder: Object Name
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - object
        operation:
        - create
        - delete
        - get
        - update
  typeInfo:
    type: string
    displayName: Object Name
    name: objectName
- id: projection
  name: Projection
  type: options
  default: noAcl
  required: false
  description: ''
  validation: *id005
  typeInfo: *id006
- id: updateProjection
  name: Projection
  type: options
  default: full
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - create
        - update
  typeInfo:
    type: options
    displayName: Projection
    name: updateProjection
    possibleValues:
    - value: full
      name: All Properties
      description: ''
    - value: noAcl
      name: No ACL
      description: ''
- id: alt
  name: Return Data
  type: options
  default: json
  required: false
  description: ''
  placeholder: The type of data to return from the request
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - get
  typeInfo:
    type: options
    displayName: Return Data
    name: alt
    possibleValues:
    - value: json
      name: Metadata
      description: ''
    - value: media
      name: Object Data
      description: ''
- id: createFromBinary
  name: Use Input Binary Field
  type: boolean
  default: true
  required: false
  description: Whether the data for creating a file should come from a binary field
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - create
  typeInfo:
    type: boolean
    displayName: Use Input Binary Field
    name: createFromBinary
- id: createBinaryPropertyName
  name: Input Binary Field
  type: string
  default: data
  required: false
  description: ''
  hint: The name of the input binary field containing the file to be written
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - create
        createFromBinary:
        - true
  typeInfo:
    type: string
    displayName: Input Binary Field
    name: createBinaryPropertyName
- id: createContent
  name: File Content
  type: string
  default: ''
  required: false
  description: Content of the file to be uploaded
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - create
        createFromBinary:
        - false
  typeInfo:
    type: string
    displayName: File Content
    name: createContent
- id: binaryPropertyName
  name: Put Output File in Field
  type: string
  default: data
  required: false
  description: ''
  hint: The name of the output binary field to put the file in
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - get
        alt:
        - media
  typeInfo:
    type: string
    displayName: Put Output File in Field
    name: binaryPropertyName
- id: returnAll
  name: Return All
  type: boolean
  default: false
  required: false
  description: Whether to return all results or only up to a given limit
  validation: *id007
  typeInfo: *id008
- id: maxResults
  name: Limit
  type: number
  default: 100
  required: false
  description: Max number of results to return
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - getAll
        returnAll:
        - false
  typeInfo:
    type: number
    displayName: Limit
    name: maxResults
    typeOptions:
      minValue: 1
      maxValue: 1000
- id: createData
  name: Create Fields
  type: collection
  default: {}
  required: false
  description: ''
  placeholder: Add Create Body Field
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - create
  typeInfo:
    type: collection
    displayName: Create Fields
    name: createData
    subProperties:
    - displayName: Access Control List
      name: acl
      type: json
      default: '[]'
    - displayName: Cache Control
      name: cacheControl
      type: string
      default: ''
    - displayName: Content Disposition
      name: contentDisposition
      type: string
      default: ''
    - displayName: Content Encoding
      name: contentEncoding
      type: string
      default: ''
    - displayName: Content Language
      name: contentLanguage
      type: string
      default: ''
    - displayName: Content Type
      name: contentType
      type: string
      default: ''
    - displayName: CRC32c Checksum
      name: crc32c
      type: string
      default: ''
    - displayName: Custom Time
      name: customTime
      type: string
      default: ''
    - displayName: Event Based Hold
      name: eventBasedHold
      type: boolean
      default: false
    - displayName: MD5 Hash
      name: md5Hash
      type: string
      default: ''
    - displayName: Metadata
      name: metadata
      type: json
      default: '{}'
    - displayName: Storage Class
      name: storageClass
      type: string
      default: ''
    - displayName: Temporary Hold
      name: temporaryHold
      type: boolean
      default: false
- id: updateData
  name: Update Fields
  type: collection
  default: '[]'
  required: false
  description: ''
  placeholder: Add Update Body Field
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - update
  typeInfo:
    type: collection
    displayName: Update Fields
    name: updateData
    subProperties:
    - displayName: Access Control
      name: acl
      type: json
      default: '[]'
    - displayName: Cache Control
      name: cacheControl
      type: string
      default: ''
    - displayName: Content Disposition
      name: contentDisposition
      type: string
      default: ''
    - displayName: Content Encoding
      name: contentEncoding
      type: string
      default: ''
    - displayName: Content Language
      name: contentLanguage
      type: string
      default: ''
    - displayName: Content Type
      name: contentType
      type: string
      default: ''
    - displayName: Custom Time
      name: customTime
      type: string
      default: ''
    - displayName: Event Based Hold
      name: eventBasedHold
      type: boolean
      default: false
    - displayName: Metadata
      name: metadata
      type: json
      default: '{}'
    - displayName: Temporary Hold
      name: temporaryHold
      type: boolean
      default: false
- id: createQuery
  name: Additional Parameters
  type: collection
  default: {}
  required: false
  description: ''
  placeholder: Add Additional Parameters
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - create
  typeInfo:
    type: collection
    displayName: Additional Parameters
    name: createQuery
    subProperties:
    - displayName: Content Encoding
      name: contentEncoding
      type: string
      default: ''
    - displayName: KMS Key Name
      name: kmsKeyName
      type: string
      default: ''
- id: getParameters
  name: Additional Parameters
  type: collection
  default: {}
  required: false
  description: ''
  placeholder: Add Additional Parameters
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - delete
        - get
  typeInfo:
    type: collection
    displayName: Additional Parameters
    name: getParameters
    subProperties: []
- id: metagenAndAclQuery
  name: Additional Parameters
  type: collection
  default: {}
  required: false
  description: ''
  placeholder: Add Additional Parameters
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - update
  typeInfo:
    type: collection
    displayName: Additional Parameters
    name: metagenAndAclQuery
    subProperties: []
- id: encryptionHeaders
  name: Encryption Headers
  type: collection
  default: {}
  required: false
  description: ''
  placeholder: Add Encryption Headers
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - create
        - get
        - update
  typeInfo:
    type: collection
    displayName: Encryption Headers
    name: encryptionHeaders
    subProperties:
    - displayName: Encryption Algorithm
      name: X-Goog-Encryption-Algorithm
      type: options
      placeholder: The encryption algorithm to use, which must be AES256. Use to supply
        your own key in the request
      value: AES256
      default: AES256
      options:
      - name: AES256
        value: AES256
        displayName: Aes256
    - displayName: Encryption Key
      name: X-Goog-Encryption-Key
      type: string
      placeholder: Base64 encoded string of your AES256 encryption key
      default: ''
    - displayName: Encryption Key Hash
      name: X-Goog-Encryption-Key-Sha256
      type: string
      placeholder: Base64 encoded string of the SHA256 hash of your encryption key
      default: ''
- id: listFilters
  name: Additional Parameters
  type: collection
  default: {}
  required: false
  description: ''
  placeholder: Add Additional Parameters
  validation:
    displayOptions:
      show:
        resource:
        - object
        operation:
        - getAll
  typeInfo:
    type: collection
    displayName: Additional Parameters
    name: listFilters
    subProperties:
    - displayName: Delimiter
      name: delimiter
      type: string
      placeholder: Returns results in directory-like mode, using this value as the
        delimiter
      default: /
    - displayName: End Offset
      name: endOffset
      type: string
      placeholder: Filter results to names lexicographically before this value
      default: ''
    - displayName: Include Trailing Delimiter
      name: includeTrailingDelimiter
      type: boolean
      placeholder: If true, objects will appear with exactly one instance of delimiter
        at the end of the name
      default: false
    - displayName: Prefix
      name: prefix
      type: string
      placeholder: Filter results to names that start with this value
      default: ''
    - displayName: Start Offset
      name: startOffset
      type: string
      placeholder: Filter results to names lexicographically equal or after this value
      default: ''
    - displayName: Versions
      name: versions
      type: boolean
      placeholder: If true, list all versions of objects as distinct entries
      default: false
- id: generation
  name: Generation
  type: number
  default: ''
  required: false
  description: ''
  placeholder: Select a specific revision of the chosen object
  typeInfo:
    type: number
    displayName: Generation
    name: generation
- id: ifGenerationMatch
  name: Generation Match
  type: number
  default: ''
  required: false
  description: ''
  placeholder: Make operation conditional of the object generation matching this value
  typeInfo:
    type: number
    displayName: Generation Match
    name: ifGenerationMatch
- id: ifGenerationNotMatch
  name: Generation Exclude
  type: number
  default: ''
  required: false
  description: ''
  placeholder: Make operation conditional of the object generation not matching this
    value
  typeInfo:
    type: number
    displayName: Generation Exclude
    name: ifGenerationNotMatch
- id: ifMetagenerationMatch
  name: Metageneration Match
  type: number
  default: ''
  required: false
  description: ''
  placeholder: Make operation conditional of the object's current metageneration matching
    this value
  typeInfo:
    type: number
    displayName: Metageneration Match
    name: ifMetagenerationMatch
- id: ifMetagenerationNotMatch
  name: Metageneration Exclude
  type: number
  default: ''
  required: false
  description: ''
  placeholder: Make operation conditional of the object's current metageneration not
    matching this value
  typeInfo:
    type: number
    displayName: Metageneration Exclude
    name: ifMetagenerationNotMatch
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: projectId
    text: Project ID
  - field: bucketName
    text: Bucket Name
  - field: prefix
    text: Filter for Bucket Names
  - field: getFilters
    text: Add Filter
  - field: createAcl
    text: Add Access Control Parameters
  - field: createBody
    text: Add Metadata Parameter
  - field: bucketName
    text: Bucket Name
  - field: objectName
    text: Object Name
  - field: alt
    text: The type of data to return from the request
  - field: createData
    text: Add Create Body Field
  - field: updateData
    text: Add Update Body Field
  - field: createQuery
    text: Add Additional Parameters
  - field: getParameters
    text: Add Additional Parameters
  - field: metagenAndAclQuery
    text: Add Additional Parameters
  - field: encryptionHeaders
    text: Add Encryption Headers
  - field: listFilters
    text: Add Additional Parameters
  - field: generation
    text: Select a specific revision of the chosen object
  - field: ifGenerationMatch
    text: Make operation conditional of the object generation matching this value
  - field: ifGenerationNotMatch
    text: Make operation conditional of the object generation not matching this value
  - field: ifMetagenerationMatch
    text: Make operation conditional of the object's current metageneration matching
      this value
  - field: ifMetagenerationNotMatch
    text: Make operation conditional of the object's current metageneration not matching
      this value
  hints:
  - field: createBinaryPropertyName
    text: The name of the input binary field containing the file to be written
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/googleCloudStorage.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Cloud Storage Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "bucket",
            "object"
          ],
          "default": "bucket"
        },
        "operation": {
          "description": "Create an object",
          "type": "string",
          "default": "getAll"
        },
        "projectId": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Project ID"
          ]
        },
        "bucketName": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Bucket Name"
          ]
        },
        "prefix": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Filter for Bucket Names"
          ]
        },
        "projection": {
          "description": "",
          "type": "string",
          "enum": [
            "full",
            "noAcl"
          ],
          "default": "noAcl"
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "getFilters": {
          "description": "Only return data if the metageneration value of the Bucket matches the sent value",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "createAcl": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Access Control Parameters"
          ]
        },
        "createBody": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Metadata Parameter"
          ]
        },
        "objectName": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Object Name"
          ]
        },
        "updateProjection": {
          "description": "",
          "type": "string",
          "enum": [
            "full",
            "noAcl"
          ],
          "default": "full"
        },
        "alt": {
          "description": "",
          "type": "string",
          "enum": [
            "json",
            "media"
          ],
          "default": "json",
          "examples": [
            "The type of data to return from the request"
          ]
        },
        "createFromBinary": {
          "description": "Whether the data for creating a file should come from a binary field",
          "type": "boolean",
          "default": true
        },
        "createBinaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "createContent": {
          "description": "Content of the file to be uploaded",
          "type": "string",
          "default": ""
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "maxResults": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
        },
        "createData": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Create Body Field"
          ]
        },
        "updateData": {
          "description": "",
          "type": "string",
          "default": "[]",
          "examples": [
            "Add Update Body Field"
          ]
        },
        "createQuery": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Additional Parameters"
          ]
        },
        "getParameters": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Additional Parameters"
          ]
        },
        "metagenAndAclQuery": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Additional Parameters"
          ]
        },
        "encryptionHeaders": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Encryption Headers"
          ]
        },
        "listFilters": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Additional Parameters"
          ]
        },
        "generation": {
          "description": "",
          "type": "number",
          "examples": [
            "Select a specific revision of the chosen object"
          ]
        },
        "ifGenerationMatch": {
          "description": "",
          "type": "number",
          "examples": [
            "Make operation conditional of the object generation matching this value"
          ]
        },
        "ifGenerationNotMatch": {
          "description": "",
          "type": "number",
          "examples": [
            "Make operation conditional of the object generation not matching this value"
          ]
        },
        "ifMetagenerationMatch": {
          "description": "",
          "type": "number",
          "examples": [
            "Make operation conditional of the object's current metageneration matching this value"
          ]
        },
        "ifMetagenerationNotMatch": {
          "description": "",
          "type": "number",
          "examples": [
            "Make operation conditional of the object's current metageneration not matching this value"
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
      "name": "googleCloudStorageOAuth2Api",
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
