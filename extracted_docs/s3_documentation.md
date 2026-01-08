---
title: "Node: S3"
slug: "node-s3"
version: "1"
updated: "2026-01-08"
summary: "Sends data to any S3-compatible service"
node_type: "regular"
group: "['output']"
---

# Node: S3

**Purpose.** Sends data to any S3-compatible service
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:s3.png`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **s3**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **s3StandardNotice**: This node is for services that use the S3 standard, e.g. Minio or Digital Ocean Spaces. For AWS S3 use the 'AWS S3' node.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `s3` | ✓ | - |

---

## Operations

### Bucket Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a bucket |
| Delete | `delete` | Delete a bucket |
| Get Many | `getAll` | Get many buckets |
| Search | `search` | Search within a bucket |

### Folder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a folder |
| Delete | `delete` | Delete a folder |
| Get Many | `getAll` | Get many folders |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Copy | `copy` | Copy a file |
| Delete | `delete` | Delete a file |
| Download | `download` | Download a file |
| Get Many | `getAll` | Get many files |
| Upload | `upload` | Upload a file |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | file | ✗ | Resource to operate on |  |

**Resource options:**

* **Bucket** (`bucket`)
* **File** (`file`)
* **Folder** (`folder`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a bucket |  |

**Operation options:**

* **Create** (`create`) - Create a bucket
* **Delete** (`delete`) - Delete a bucket
* **Get Many** (`getAll`) - Get many buckets
* **Search** (`search`) - Search within a bucket

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | A succinct description of the nature, symptoms, cause, or effect of the bucket |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The canned ACL to apply to the bucket | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| ACL | `acl` | options |  | The canned ACL to apply to the bucket |
| Bucket Object Lock Enabled | `bucketObjectLockEnabled` | boolean | False | Whether you want S3 Object Lock to be enabled for the new bucket |
| Grant Full Control | `grantFullControl` | boolean | False | Whether to allow grantee the read, write, read ACP, and write ACP permissions on the bucket |
| Grant Read | `grantRead` | boolean | False | Whether to allow grantee to list the objects in the bucket |
| Grant Read ACP | `grantReadAcp` | boolean | False | Whether to allow grantee to read the bucket ACL |
| Grant Write | `grantWrite` | boolean | False | Whether to allow grantee to create, overwrite, and delete any object in the bucket |
| Grant Write ACP | `grantWriteAcp` | boolean | False | Whether to allow grantee to write the ACL for the applicable bucket |
| Region | `region` | string |  | Region you want to create the bucket in, by default the buckets are created on the region defined on the credentials |

</details>

| Bucket Name | `bucketName` | string |  | ✓ |  |  |
| Folder Name | `folderName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Parent folder you want to create the folder in | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Parent Folder Key | `parentFolderKey` | string |  | Parent folder you want to create the folder in |
| Requester Pays | `requesterPays` | boolean | False | Whether the requester will pay for requests and data transfer. While Requester Pays is enabled, anonymous access to this bucket is disabled. |
| Storage Class | `storageClass` | options | standard | Amazon S3 storage classes |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Name of the AWS S3 bucket to delete |  |
| Bucket Name | `bucketName` | string |  | ✓ |  |  |
| Folder Key | `folderKey` | string |  | ✓ |  |  |
| Bucket Name | `bucketName` | string |  | ✓ |  |  |
| File Key | `fileKey` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Version ID | `versionId` | string |  |  |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Bucket Name | `bucketName` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fetch Owner | `fetchOwner` | boolean | False | The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true |
| Folder Key | `folderKey` | string |  |  |

</details>

| Bucket Name | `bucketName` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fetch Owner | `fetchOwner` | boolean | False | The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true |
| Folder Key | `folderKey` | string |  |  |

</details>


### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bucket Name | `bucketName` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | A delimiter is a character you use to group keys | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Delimiter | `delimiter` | string |  | A delimiter is a character you use to group keys |
| Encoding Type | `encodingType` | options |  | Encoding type used by Amazon S3 to encode object keys in the response |
| Fetch Owner | `fetchOwner` | boolean | False | The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true |
| Prefix | `prefix` | string |  | Limits the response to keys that begin with the specified prefix |
| Requester Pays | `requesterPays` | boolean | False | Whether the requester will pay for requests and data transfer. While Requester Pays is enabled, anonymous access to this bucket is disabled. |
| Start After | `startAfter` | string |  | StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. |

</details>


### Copy parameters (`copy`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Source Path | `sourcePath` | string |  | ✓ | The name of the source bucket should start with (/) and key name of the source object, separated by a slash (/) | e.g. /bucket/my-image.jpg |  |
| Destination Path | `destinationPath` | string |  | ✓ | The name of the destination bucket and key name of the destination object, separated by a slash (/) | e.g. /bucket/my-second-image.jpg |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The canned ACL to apply to the object | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| ACL | `acl` | options | private | The canned ACL to apply to the object |
| Grant Full Control | `grantFullControl` | boolean | False | Whether to give the grantee READ, READ_ACP, and WRITE_ACP permissions on the object |
| Grant Read | `grantRead` | boolean | False | Whether to allow grantee to read the object data and its metadata |
| Grant Read ACP | `grantReadAcp` | boolean | False | Whether to allow grantee to read the object ACL |
| Grant Write ACP | `grantWriteAcp` | boolean | False | Whether to allow grantee to write the ACL for the applicable object |
| Lock Legal Hold | `lockLegalHold` | boolean | False | Whether a legal hold will be applied to this object |
| Lock Mode | `lockMode` | options |  | The Object Lock mode that you want to apply to this object |
| Lock Retain Until Date | `lockRetainUntilDate` | dateTime |  | The date and time when you want this object's Object Lock to expire |
| Metadata Directive | `metadataDirective` | options |  | Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request |
| Requester Pays | `requesterPays` | boolean | False | Whether the requester will pay for requests and data transfer. While Requester Pays is enabled, anonymous access to this bucket is disabled. |
| Server Side Encryption | `serverSideEncryption` | options |  | The server-side encryption algorithm used when storing this object in Amazon S3 |
| Server Side Encryption Context | `serverSideEncryptionContext` | string |  | Specifies the AWS KMS Encryption Context to use for object encryption |
| Server Side Encryption AWS KMS Key ID | `encryptionAwsKmsKeyId` | string |  | If x-amz-server-side-encryption is present and has the value of aws:kms |
| Server Side Encryption Customer Algorithm | `serversideEncryptionCustomerAlgorithm` | string |  | Specifies the algorithm to use to when encrypting the object (for example, AES256) |
| Server Side Encryption Customer Key | `serversideEncryptionCustomerKey` | string |  | Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data |
| Server Side Encryption Customer Key MD5 | `serversideEncryptionCustomerKeyMD5` | string |  | Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321 |
| Storage Class | `storageClass` | options | standard | Amazon S3 storage classes |
| Tagging Directive | `taggingDirective` | options |  | Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request |

</details>


### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bucket Name | `bucketName` | string |  | ✓ |  |  |
| File Key | `fileKey` | string |  | ✓ |  |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |

### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bucket Name | `bucketName` | string |  | ✓ |  |  |
| File Name | `fileName` | string |  | ✓ | e.g. hello.txt |  |
| File Name | `fileName` | string |  | ✗ | If not set the binary data filename will be used |  |
| Binary File | `binaryData` | boolean | True | ✗ | Whether the data to upload should be taken from binary field |  |
| File Content | `fileContent` | string |  | ✗ | The text content of the file to upload |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The canned ACL to apply to the object | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| ACL | `acl` | options | private | The canned ACL to apply to the object |
| Grant Full Control | `grantFullControl` | boolean | False | Whether to give the grantee READ, READ_ACP, and WRITE_ACP permissions on the object |
| Grant Read | `grantRead` | boolean | False | Whether to allow grantee to read the object data and its metadata |
| Grant Read ACP | `grantReadAcp` | boolean | False | Whether to allow grantee to read the object ACL |
| Grant Write ACP | `grantWriteAcp` | boolean | False | Whether to allow grantee to write the ACL for the applicable object |
| Lock Legal Hold | `lockLegalHold` | boolean | False | Whether a legal hold will be applied to this object |
| Lock Mode | `lockMode` | options |  | The Object Lock mode that you want to apply to this object |
| Lock Retain Until Date | `lockRetainUntilDate` | dateTime |  | The date and time when you want this object's Object Lock to expire |
| Parent Folder Key | `parentFolderKey` | string |  | Parent folder you want to create the file in |
| Requester Pays | `requesterPays` | boolean | False | Whether the requester will pay for requests and data transfer. While Requester Pays is enabled, anonymous access to this bucket is disabled. |
| Server Side Encryption | `serverSideEncryption` | options |  | The server-side encryption algorithm used when storing this object in Amazon S3 |
| Server Side Encryption Context | `serverSideEncryptionContext` | string |  | Specifies the AWS KMS Encryption Context to use for object encryption |
| Server Side Encryption AWS KMS Key ID | `encryptionAwsKmsKeyId` | string |  | If x-amz-server-side-encryption is present and has the value of aws:kms |
| Server Side Encryption Customer Algorithm | `serversideEncryptionCustomerAlgorithm` | string |  | Specifies the algorithm to use to when encrypting the object (for example, AES256) |
| Server Side Encryption Customer Key | `serversideEncryptionCustomerKey` | string |  | Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data |
| Server Side Encryption Customer Key MD5 | `serversideEncryptionCustomerKeyMD5` | string |  | Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321 |
| Storage Class | `storageClass` | options | standard | Amazon S3 storage classes |

</details>

| Tags | `tagsUi` | fixedCollection | {} | ✗ | Optional extra headers to add to the message (most headers are allowed) | e.g. Add Tag |  |

<details>
<summary><strong>Tags sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Tag | `tagsValues` |  |  |  |

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
* Categories: Development, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: s3
displayName: S3
description: Sends data to any S3-compatible service
version: '1'
nodeType: regular
group:
- output
credentials:
- name: s3
  required: true
operations:
- id: create
  name: Create
  description: Create a bucket
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: A succinct description of the nature, symptoms, cause, or effect
      of the bucket
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - bucket
          operation:
          - delete
    typeInfo: &id002
      type: string
      displayName: Name
      name: name
  - id: bucketName
    name: Bucket Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - getAll
    typeInfo: &id004
      type: string
      displayName: Bucket Name
      name: bucketName
  - id: folderName
    name: Folder Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - folder
          operation:
          - create
    typeInfo:
      type: string
      displayName: Folder Name
      name: folderName
- id: delete
  name: Delete
  description: Delete a bucket
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the AWS S3 bucket to delete
    validation: *id001
    typeInfo: *id002
  - id: bucketName
    name: Bucket Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: folderKey
    name: Folder Key
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - folder
          operation:
          - delete
    typeInfo:
      type: string
      displayName: Folder Key
      name: folderKey
  - id: bucketName
    name: Bucket Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: fileKey
    name: File Key
    type: string
    default: ''
    required: true
    description: ''
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - delete
    typeInfo: &id010
      type: string
      displayName: File Key
      name: fileKey
- id: getAll
  name: Get Many
  description: Get many buckets
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id005
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - file
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - file
          returnAll:
          - false
    typeInfo: &id008
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: bucketName
    name: Bucket Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
  - id: bucketName
    name: Bucket Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: search
  name: Search
  description: Search within a bucket
  params:
  - id: bucketName
    name: Bucket Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: copy
  name: Copy
  description: Copy a file
  params:
  - id: sourcePath
    name: Source Path
    type: string
    default: ''
    required: true
    description: The name of the source bucket should start with (/) and key name
      of the source object, separated by a slash (/)
    placeholder: /bucket/my-image.jpg
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - copy
    typeInfo:
      type: string
      displayName: Source Path
      name: sourcePath
  - id: destinationPath
    name: Destination Path
    type: string
    default: ''
    required: true
    description: The name of the destination bucket and key name of the destination
      object, separated by a slash (/)
    placeholder: /bucket/my-second-image.jpg
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - copy
    typeInfo:
      type: string
      displayName: Destination Path
      name: destinationPath
- id: download
  name: Download
  description: Download a file
  params:
  - id: bucketName
    name: Bucket Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: fileKey
    name: File Key
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id013
      required: true
      displayOptions:
        show:
          operation:
          - download
          resource:
          - file
    typeInfo: &id014
      type: string
      displayName: Put Output File in Field
      name: binaryPropertyName
- id: upload
  name: Upload
  description: Upload a file
  params:
  - id: bucketName
    name: Bucket Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: true
    description: ''
    placeholder: hello.txt
    validation: &id011
      displayOptions:
        show:
          resource:
          - file
          operation:
          - upload
          binaryData:
          - true
    typeInfo: &id012
      type: string
      displayName: File Name
      name: fileName
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: false
    description: If not set the binary data filename will be used
    validation: *id011
    typeInfo: *id012
  - id: binaryData
    name: Binary File
    type: boolean
    default: true
    required: false
    description: Whether the data to upload should be taken from binary field
    validation:
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
    typeInfo:
      type: boolean
      displayName: Binary File
      name: binaryData
  - id: fileContent
    name: File Content
    type: string
    default: ''
    required: false
    description: The text content of the file to upload
    validation:
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
          binaryData:
          - false
    typeInfo:
      type: string
      displayName: File Content
      name: fileContent
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be uploaded
    validation: *id013
    typeInfo: *id014
  - id: tagsUi
    name: Tags
    type: fixedCollection
    default: {}
    required: false
    description: Optional extra headers to add to the message (most headers are allowed)
    placeholder: Add Tag
    validation:
      displayOptions:
        show:
          resource:
          - file
          operation:
          - upload
    typeInfo:
      type: fixedCollection
      displayName: Tags
      name: tagsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: tagsValues
        displayName: Tag
        values:
        - displayName: Key
          name: key
          type: string
          default: ''
        - displayName: Value
          name: value
          type: string
          default: ''
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: s3StandardNotice
    text: This node is for services that use the S3 standard, e.g. Minio or Digital
      Ocean Spaces. For AWS S3 use the 'AWS S3' node.
    conditions: null
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add Field
  - field: sourcePath
    text: /bucket/my-image.jpg
  - field: destinationPath
    text: /bucket/my-second-image.jpg
  - field: additionalFields
    text: Add Field
  - field: fileName
    text: hello.txt
  - field: additionalFields
    text: Add Field
  - field: tagsUi
    text: Add Tag
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be uploaded
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
  "$id": "https://n8n.io/schemas/nodes/s3.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "S3 Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "getAll",
        "search",
        "copy",
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
            "bucket",
            "file",
            "folder"
          ],
          "default": "file"
        },
        "operation": {
          "description": "Copy a file",
          "type": "string",
          "enum": [
            "copy",
            "delete",
            "download",
            "getAll",
            "upload"
          ],
          "default": "download"
        },
        "name": {
          "description": "Name of the AWS S3 bucket to delete",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The canned ACL to apply to the object",
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
          "default": 100
        },
        "bucketName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "folderName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "folderKey": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "sourcePath": {
          "description": "The name of the source bucket should start with (/) and key name of the source object, separated by a slash (/)",
          "type": "string",
          "default": "",
          "examples": [
            "/bucket/my-image.jpg"
          ]
        },
        "destinationPath": {
          "description": "The name of the destination bucket and key name of the destination object, separated by a slash (/)",
          "type": "string",
          "default": "",
          "examples": [
            "/bucket/my-second-image.jpg"
          ]
        },
        "fileName": {
          "description": "If not set the binary data filename will be used",
          "type": "string",
          "default": ""
        },
        "binaryData": {
          "description": "Whether the data to upload should be taken from binary field",
          "type": "boolean",
          "default": true
        },
        "fileContent": {
          "description": "The text content of the file to upload",
          "type": "string",
          "default": ""
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "tagsUi": {
          "description": "Optional extra headers to add to the message (most headers are allowed)",
          "type": "string",
          "default": {},
          "examples": [
            "Add Tag"
          ]
        },
        "fileKey": {
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
      "name": "s3",
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
