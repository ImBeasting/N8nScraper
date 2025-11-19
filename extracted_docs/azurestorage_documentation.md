---
title: "Node: Azure Storage"
slug: "node-azurestorage"
version: "1"
updated: "2025-11-13"
summary: "Interact with Azure Storage API"
node_type: "regular"
group: "['transform']"
---

# Node: Azure Storage

**Purpose.** Interact with Azure Storage API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:azureStorage.svg', 'dark': 'file:azureStorage.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **azureStorageOAuth2Api**: N/A
- **azureStorageSharedKeyApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `azureStorageOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |
| `azureStorageSharedKeyApi` | ✓ | {'show': {'authentication': ['sharedKey']}} |

---

## Operations

### Container Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Blob Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | container | ✗ | Resource to operate on |  |

**Resource options:**

* **Blob** (`blob`)
* **Container** (`container`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | sharedKey | ✗ |  |  |

**Authentication options:**

* **OAuth2** (`oAuth2`)
* **Shared Key** (`sharedKey`)

| Resource | `resource` | options | container | ✗ |  |  |

**Resource options:**

* **Blob** (`blob`)
* **Container** (`container`)

| Operation | `operation` | options | getAll | ✗ | Create a container |  |
| Container Name | `containerCreate` | string |  | ✓ | The name of the new container | e.g. e.g. mycontainer | validated |
| Options | `options` | options | {} | ✗ | Specifies public read access for blobs. Blob data within this container can be read via anonymous request, but container data isn't available. Clients can't enumerate blobs within the container via anonymous request. | e.g. Add metadata |  |
| Container | `container` | list |  | ✓ | Select the container to delete | e.g. e.g. mycontainer |  |
| Container | `container` | list |  | ✓ | Select the container to get | e.g. e.g. mycontainer |  |
| Options | `options` | boolean | {} | ✗ | Whether to return a simplified version of the response instead of the raw data | e.g. Add option |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | query | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Options | `options` | query | {} | ✗ | The fields to add to the output | e.g. e.g. mycontainer |  |
| Container | `container` | list |  | ✓ | Container to create or replace a blob in | e.g. e.g. mycontainer |  |
| Blob Name | `blobCreate` | string |  | ✓ | The name of the new or existing blob | e.g. e.g. myblob | validated |
| From | `from` | options | binary | ✓ |  |  |

**From options:**

* **Binary** (`binary`)
* **URL** (`url`)

| Binary Contents | `binaryPropertyName` | string | data | ✓ | The name of the input binary field containing the file to be written |  |
| URL | `url` | string |  | ✓ | URL where to read of the blob contents from | e.g. e.g. https://example.com/image.jpg | url |
| Options | `options` | options | {} | ✗ | The tier to be set on the blob. For detailed information about block blob tiering, see <a href="https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview">Hot, cool, and archive storage tiers</a>. | e.g. Add metadata |  |
| Container | `container` | list |  | ✓ | Container to delete a blob from | e.g. e.g. mycontainer |  |
| Blob | `blob` | list |  | ✓ | Blob to be deleted | e.g. e.g. myblob |  |
| Options | `options` | string | {} | ✗ | Required if the blob has an active lease | e.g. Add option |  |
| Container | `container` | list |  | ✓ | Container to get a blob from | e.g. e.g. mycontainer |  |
| Blob | `blob` | list |  | ✓ | Blob to get | e.g. e.g. myblob |  |
| Options | `options` | string | {} | ✗ | If this header is specified, the operation is performed only if both of the following conditions are met: <ul><li>The blob's lease is currently active.</li><li>The lease ID that's specified in the request matches the lease ID of the blob.</li></ul> | e.g. Add option |  |
| Container | `container` | list |  | ✓ | Container to get blobs from | e.g. e.g. mycontainer |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | query | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Options | `options` | query | {} | ✗ | The fields to add to the output | e.g. Add option |  |
| Operation | `operation` | options | getAll | ✗ | Create a new blob or replace an existing one |  |

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Azure Storage

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "operation": "delete",
  "container": {
    "__rl": true,
    "mode": "list",
    "value": "mycontainer"
  },
  "requestOptions": {}
}
```

**Credentials:**
- azureStorageSharedKeyApi: `Azure Storage Shared Key account`

### Example 2: Azure Storage

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "operation": "getAll",
  "limit": 1,
  "options": {
    "fields": [
      "metadata",
      "deleted",
      "system"
    ],
    "filter": "mycontainer"
  },
  "requestOptions": {}
}
```

**Credentials:**
- azureStorageSharedKeyApi: `Azure Storage Shared Key account`

### Example 3: Azure Storage

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "operation": "create",
  "containerCreate": "mycontainer",
  "options": {
    "accessLevel": "blob",
    "metadata": {
      "metadataValues": [
        {
          "fieldName": "key1",
          "fieldValue": "value1"
        }
      ]
    }
  },
  "requestOptions": {}
}
```

**Credentials:**
- azureStorageSharedKeyApi: `Azure Storage Shared Key account`

### Example 4: Azure Storage

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "operation": "get",
  "container": {
    "__rl": true,
    "mode": "list",
    "value": "mycontainer"
  },
  "options": {
    "simplify": false
  },
  "requestOptions": {}
}
```

**Credentials:**
- azureStorageSharedKeyApi: `Azure Storage Shared Key account`

### Example 5: Azure Storage

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "operation": "getAll",
  "returnAll": true,
  "requestOptions": {}
}
```

**Credentials:**
- azureStorageSharedKeyApi: `Azure Storage Shared Key account`


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $credentials.baseUrl }}`
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
* Categories: Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: azureStorage
displayName: Azure Storage
description: Interact with Azure Storage API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: azureStorageOAuth2Api
  required: true
- name: azureStorageSharedKeyApi
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: sharedKey
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: oAuth2
      name: OAuth2
      description: ''
    - value: sharedKey
      name: Shared Key
      description: ''
- id: resource
  name: Resource
  type: options
  default: container
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: blob
      name: Blob
      description: ''
    - value: container
      name: Container
      description: ''
- id: operation
  name: Operation
  type: options
  default: getAll
  required: false
  description: Create a container
  validation: &id011
    displayOptions:
      show:
        resource:
        - blob
  typeInfo: &id012
    type: options
    displayName: Operation
    name: operation
    possibleValues: []
- id: containerCreate
  name: Container Name
  type: string
  default: ''
  required: true
  description: The name of the new container
  placeholder: e.g. mycontainer
  validation:
    required: true
    format: validated
    displayOptions:
      show:
        resource:
        - container
        operation:
        - create
  typeInfo:
    type: string
    displayName: Container Name
    name: containerCreate
- id: options
  name: Options
  type: options
  default: {}
  required: false
  description: Specifies public read access for blobs. Blob data within this container
    can be read via anonymous request, but container data isn't available. Clients
    can't enumerate blobs within the container via anonymous request.
  placeholder: Add metadata
  validation: &id003
    displayOptions:
      show:
        resource:
        - blob
        operation:
        - getAll
  typeInfo: &id004
    type: query
    displayName: Options
    name: options
- id: container
  name: Container
  type: list
  default: ''
  required: true
  description: Select the container to delete
  placeholder: e.g. mycontainer
  validation: &id001
    required: true
    displayOptions:
      show:
        resource:
        - blob
        operation:
        - getAll
  typeInfo: &id002
    type: list
    displayName: Container
    name: container
- id: container
  name: Container
  type: list
  default: ''
  required: true
  description: Select the container to get
  placeholder: e.g. mycontainer
  validation: *id001
  typeInfo: *id002
- id: options
  name: Options
  type: boolean
  default: {}
  required: false
  description: Whether to return a simplified version of the response instead of the
    raw data
  placeholder: Add option
  validation: *id003
  typeInfo: *id004
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
        - blob
        operation:
        - getAll
  typeInfo: &id008
    type: boolean
    displayName: Return All
    name: returnAll
- id: limit
  name: Limit
  type: query
  default: 50
  required: false
  description: Max number of results to return
  validation: &id009
    displayOptions:
      show:
        resource:
        - blob
        operation:
        - getAll
        returnAll:
        - false
  typeInfo: &id010
    type: query
    displayName: Limit
    name: limit
    typeOptions:
      minValue: 1
- id: options
  name: Options
  type: query
  default: {}
  required: false
  description: The fields to add to the output
  placeholder: e.g. mycontainer
  validation: *id003
  typeInfo: *id004
- id: container
  name: Container
  type: list
  default: ''
  required: true
  description: Container to create or replace a blob in
  placeholder: e.g. mycontainer
  validation: *id001
  typeInfo: *id002
- id: blobCreate
  name: Blob Name
  type: string
  default: ''
  required: true
  description: The name of the new or existing blob
  placeholder: e.g. myblob
  validation:
    required: true
    format: validated
    displayOptions:
      show:
        resource:
        - blob
        operation:
        - create
  typeInfo:
    type: string
    displayName: Blob Name
    name: blobCreate
- id: from
  name: From
  type: options
  default: binary
  required: true
  description: ''
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - blob
        operation:
        - create
  typeInfo:
    type: options
    displayName: From
    name: from
    possibleValues:
    - value: binary
      name: Binary
      description: ''
    - value: url
      name: URL
      description: ''
- id: binaryPropertyName
  name: Binary Contents
  type: string
  default: data
  required: true
  description: The name of the input binary field containing the file to be written
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - blob
        operation:
        - create
        from:
        - binary
  typeInfo:
    type: string
    displayName: Binary Contents
    name: binaryPropertyName
- id: url
  name: URL
  type: string
  default: ''
  required: true
  description: URL where to read of the blob contents from
  placeholder: e.g. https://example.com/image.jpg
  validation:
    required: true
    format: url
    displayOptions:
      show:
        resource:
        - blob
        operation:
        - create
        from:
        - url
  typeInfo:
    type: string
    displayName: URL
    name: url
- id: options
  name: Options
  type: options
  default: {}
  required: false
  description: The tier to be set on the blob. For detailed information about block
    blob tiering, see <a href="https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview">Hot,
    cool, and archive storage tiers</a>.
  placeholder: Add metadata
  validation: *id003
  typeInfo: *id004
- id: container
  name: Container
  type: list
  default: ''
  required: true
  description: Container to delete a blob from
  placeholder: e.g. mycontainer
  validation: *id001
  typeInfo: *id002
- id: blob
  name: Blob
  type: list
  default: ''
  required: true
  description: Blob to be deleted
  placeholder: e.g. myblob
  validation: &id005
    required: true
    displayOptions:
      show:
        resource:
        - blob
        operation:
        - get
  typeInfo: &id006
    type: list
    displayName: Blob
    name: blob
- id: options
  name: Options
  type: string
  default: {}
  required: false
  description: Required if the blob has an active lease
  placeholder: Add option
  validation: *id003
  typeInfo: *id004
- id: container
  name: Container
  type: list
  default: ''
  required: true
  description: Container to get a blob from
  placeholder: e.g. mycontainer
  validation: *id001
  typeInfo: *id002
- id: blob
  name: Blob
  type: list
  default: ''
  required: true
  description: Blob to get
  placeholder: e.g. myblob
  validation: *id005
  typeInfo: *id006
- id: options
  name: Options
  type: string
  default: {}
  required: false
  description: 'If this header is specified, the operation is performed only if both
    of the following conditions are met: <ul><li>The blob''s lease is currently active.</li><li>The
    lease ID that''s specified in the request matches the lease ID of the blob.</li></ul>'
  placeholder: Add option
  validation: *id003
  typeInfo: *id004
- id: container
  name: Container
  type: list
  default: ''
  required: true
  description: Container to get blobs from
  placeholder: e.g. mycontainer
  validation: *id001
  typeInfo: *id002
- id: returnAll
  name: Return All
  type: boolean
  default: false
  required: false
  description: Whether to return all results or only up to a given limit
  validation: *id007
  typeInfo: *id008
- id: limit
  name: Limit
  type: query
  default: 50
  required: false
  description: Max number of results to return
  validation: *id009
  typeInfo: *id010
- id: options
  name: Options
  type: query
  default: {}
  required: false
  description: The fields to add to the output
  placeholder: Add option
  validation: *id003
  typeInfo: *id004
- id: operation
  name: Operation
  type: options
  default: getAll
  required: false
  description: Create a new blob or replace an existing one
  validation: *id011
  typeInfo: *id012
examples:
- name: Azure Storage
  parameters:
    operation: delete
    container:
      __rl: true
      mode: list
      value: mycontainer
    requestOptions: {}
  workflow: Unnamed workflow
- name: Azure Storage
  parameters:
    operation: getAll
    limit: 1
    options:
      fields:
      - metadata
      - deleted
      - system
      filter: mycontainer
    requestOptions: {}
  workflow: Unnamed workflow
- name: Azure Storage
  parameters:
    operation: create
    containerCreate: mycontainer
    options:
      accessLevel: blob
      metadata:
        metadataValues:
        - fieldName: key1
          fieldValue: value1
    requestOptions: {}
  workflow: Unnamed workflow
common_expressions:
- ={{ $credentials.baseUrl }}
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
  - field: containerCreate
    text: e.g. mycontainer
  - field: options
    text: Add metadata
  - field: container
    text: e.g. mycontainer
  - field: container
    text: e.g. mycontainer
  - field: options
    text: Add option
  - field: options
    text: e.g. mycontainer
  - field: container
    text: e.g. mycontainer
  - field: blobCreate
    text: e.g. myblob
  - field: url
    text: e.g. https://example.com/image.jpg
  - field: options
    text: Add metadata
  - field: container
    text: e.g. mycontainer
  - field: blob
    text: e.g. myblob
  - field: options
    text: Add option
  - field: container
    text: e.g. mycontainer
  - field: blob
    text: e.g. myblob
  - field: options
    text: Add option
  - field: container
    text: e.g. mycontainer
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
  "$id": "https://n8n.io/schemas/nodes/azureStorage.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Azure Storage Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "oAuth2",
            "sharedKey"
          ],
          "default": "sharedKey"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "blob",
            "container"
          ],
          "default": "container"
        },
        "operation": {
          "description": "Create a new blob or replace an existing one",
          "type": "string",
          "default": "getAll"
        },
        "containerCreate": {
          "description": "The name of the new container",
          "type": "string",
          "default": "",
          "format": "validated",
          "examples": [
            "e.g. mycontainer"
          ]
        },
        "options": {
          "description": "The fields to add to the output",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "container": {
          "description": "Container to get blobs from",
          "type": "string",
          "examples": [
            "e.g. mycontainer"
          ]
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "string",
          "default": 50
        },
        "blobCreate": {
          "description": "The name of the new or existing blob",
          "type": "string",
          "default": "",
          "format": "validated",
          "examples": [
            "e.g. myblob"
          ]
        },
        "from": {
          "description": "",
          "type": "string",
          "enum": [
            "binary",
            "url"
          ],
          "default": "binary"
        },
        "binaryPropertyName": {
          "description": "The name of the input binary field containing the file to be written",
          "type": "string",
          "default": "data"
        },
        "url": {
          "description": "URL where to read of the blob contents from",
          "type": "string",
          "default": "",
          "format": "url",
          "examples": [
            "e.g. https://example.com/image.jpg"
          ]
        },
        "blob": {
          "description": "Blob to get",
          "type": "string",
          "examples": [
            "e.g. myblob"
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
      "name": "azureStorageOAuth2Api",
      "required": true
    },
    {
      "name": "azureStorageSharedKeyApi",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Azure Storage",
      "value": {
        "operation": "delete",
        "container": {
          "__rl": true,
          "mode": "list",
          "value": "mycontainer"
        },
        "requestOptions": {}
      }
    },
    {
      "description": "Azure Storage",
      "value": {
        "operation": "getAll",
        "limit": 1,
        "options": {
          "fields": [
            "metadata",
            "deleted",
            "system"
          ],
          "filter": "mycontainer"
        },
        "requestOptions": {}
      }
    },
    {
      "description": "Azure Storage",
      "value": {
        "operation": "create",
        "containerCreate": "mycontainer",
        "options": {
          "accessLevel": "blob",
          "metadata": {
            "metadataValues": [
              {
                "fieldName": "key1",
                "fieldValue": "value1"
              }
            ]
          }
        },
        "requestOptions": {}
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
