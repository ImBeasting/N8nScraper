---
title: "Node: Google Cloud Firestore"
slug: "node-googlefirebasecloudfirestore"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Interact with Google Firebase - Cloud Firestore API"
node_type: "regular"
group: "['input']"
---

# Node: Google Cloud Firestore

**Purpose.** Interact with Google Firebase - Cloud Firestore API
**Subtitle.** ={{$parameter["resource"] + ": " + $parameter["operation"]}}


---

## Node Details

- **Icon:** `file:googleFirebaseCloudFirestore.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleFirebaseCloudFirestoreOAuth2Api**: N/A
- **googleApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleFirebaseCloudFirestoreOAuth2Api` | ✓ | {'show': {'authentication': ['googleFirebaseCloudFirestoreOAuth2Api']}} |
| `googleApi` | ✓ | {'show': {'authentication': ['serviceAccount']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Document Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a document |
| Create or Update | `upsert` | Create a new document, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a document |
| Get | `get` | Get a document |
| Get Many | `getAll` | Get many documents from a collection |
| Update | `update` | Update a document |
| Query | `query` | Runs a query against your documents |

### Collection Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many root collections |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | document | ✗ | Resource to operate on |  |

**Resource options:**

* **Document** (`document`)
* **Collection** (`collection`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Create a document |  |

**Operation options:**

* **Create** (`create`) - Create a document
* **Create or Update** (`upsert`) - Create a new document, or update the current one if it already exists (upsert)
* **Delete** (`delete`) - Delete a document
* **Get** (`get`) - Get a document
* **Get Many** (`getAll`) - Get many documents from a collection
* **Update** (`update`) - Update a document
* **Query** (`query`) - Runs a query against your documents

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `projectId` | options |  | ✓ | As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Database | `database` | string | (default) | ✓ | Usually the provided default value will work |  |
| Collection | `collection` | string |  | ✓ | Collection name |  |
| Document ID | `documentId` | string |  | ✗ |  |  |
| Columns / Attributes | `columns` | string |  | ✓ | List of attributes to save | e.g. productId, modelName, description |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `projectId` | options |  | ✓ | As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Database | `database` | string | (default) | ✓ | Usually the provided default value will work |  |
| Collection | `collection` | string |  | ✓ | Collection name |  |
| Update Key | `updateKey` | string |  | ✓ | Name of the field in an input item that contains the document ID | e.g. documentId |  |
| Columns /Attributes | `columns` | string |  | ✓ | Columns to insert | e.g. age, city, location |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `projectId` | options |  | ✓ | As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Database | `database` | string | (default) | ✓ | Usually the provided default value will work |  |
| Collection | `collection` | string |  | ✓ | Collection name |  |
| Document ID | `documentId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `projectId` | options |  | ✓ | As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Database | `database` | string | (default) | ✓ | Usually the provided default value will work |  |
| Collection | `collection` | string |  | ✓ | Collection name |  |
| Document ID | `documentId` | string |  | ✓ |  |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `projectId` | options |  | ✓ | As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Database | `database` | string | (default) | ✓ | Usually the provided default value will work |  |
| Collection | `collection` | string |  | ✓ | Collection name |  |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Project Name or ID | `projectId` | options |  | ✓ | As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Database | `database` | string | (default) | ✓ | Usually the provided default value will work |  |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |

### Query parameters (`query`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `projectId` | options |  | ✓ | As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Database | `database` | string | (default) | ✓ | Usually the provided default value will work |  |
| Query JSON | `query` | string |  | ✓ | JSON query to execute | e.g. {"structuredQuery": {"where": {"fieldFilter": {"field": {"fieldPath": "age"},"op": "EQUAL", "value": {"integerValue": 28}}}, "from": [{"collectionId": "users-collection"}]}} |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

---

## Load Options Methods

- `getProjects`

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Get Document

**From workflow:** CloudFirestore Document Get Test

**Parameters:**
```json
{
  "authentication": "googleFirebaseCloudFirestoreOAuth2Api",
  "resource": "document",
  "operation": "get",
  "projectId": "test-project",
  "database": "(default)",
  "collection": "users",
  "documentId": "test-doc-id"
}
```

**Credentials:**
- googleFirebaseCloudFirestoreOAuth2Api: `CloudFirestore OAuth2`

### Example 2: Query Documents

**From workflow:** CloudFirestore Document Query Test

**Parameters:**
```json
{
  "authentication": "googleFirebaseCloudFirestoreOAuth2Api",
  "resource": "document",
  "operation": "query",
  "projectId": "test-project",
  "database": "(default)",
  "query": "{\"structuredQuery\": {\"where\": {\"fieldFilter\": {\"field\": {\"fieldPath\": \"active\"}, \"op\": \"EQUAL\", \"value\": {\"booleanValue\": true}}}, \"from\": [{\"collectionId\": \"users\"}]}}"
}
```

**Credentials:**
- googleFirebaseCloudFirestoreOAuth2Api: `CloudFirestore OAuth2`

### Example 3: Delete Document

**From workflow:** CloudFirestore Document Delete Test

**Parameters:**
```json
{
  "authentication": "googleFirebaseCloudFirestoreOAuth2Api",
  "resource": "document",
  "operation": "delete",
  "projectId": "test-project",
  "database": "(default)",
  "collection": "users",
  "documentId": "test-doc-id"
}
```

**Credentials:**
- googleFirebaseCloudFirestoreOAuth2Api: `CloudFirestore OAuth2`

### Example 4: Get All Documents

**From workflow:** CloudFirestore Collection Get All Test

**Parameters:**
```json
{
  "authentication": "googleFirebaseCloudFirestoreOAuth2Api",
  "resource": "document",
  "operation": "getAll",
  "projectId": "test-project",
  "database": "(default)",
  "collection": "users"
}
```

**Credentials:**
- googleFirebaseCloudFirestoreOAuth2Api: `CloudFirestore OAuth2`

### Example 5: Update Document

**From workflow:** CloudFirestore Document Update Test

**Parameters:**
```json
{
  "authentication": "googleFirebaseCloudFirestoreOAuth2Api",
  "resource": "document",
  "operation": "upsert",
  "projectId": "test-project",
  "database": "(default)",
  "collection": "users",
  "updateKey": "documentId",
  "columns": "name,email,age,active"
}
```

**Credentials:**
- googleFirebaseCloudFirestoreOAuth2Api: `CloudFirestore OAuth2`


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["resource"] + ": " + $parameter["operation"]}}`

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
node: googleFirebaseCloudFirestore
displayName: Google Cloud Firestore
description: Interact with Google Firebase - Cloud Firestore API
version:
- '1'
- '1.1'
nodeType: regular
group:
- input
credentials:
- name: googleFirebaseCloudFirestoreOAuth2Api
  required: true
- name: googleApi
  required: true
operations:
- id: create
  name: Create
  description: Create a document
  params:
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: As displayed in firebase console URL. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - collection
          operation:
          - getAll
    typeInfo: &id002
      type: options
      displayName: Project Name or ID
      name: projectId
      typeOptions:
        loadOptionsMethod: getProjects
      possibleValues: []
  - id: database
    name: Database
    type: string
    default: (default)
    required: true
    description: Usually the provided default value will work
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - collection
          operation:
          - getAll
    typeInfo: &id004
      type: string
      displayName: Database
      name: database
  - id: collection
    name: Collection
    type: string
    default: ''
    required: true
    description: Collection name
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - document
          operation:
          - upsert
    typeInfo: &id006
      type: string
      displayName: Collection
      name: collection
  - id: documentId
    name: Document ID
    type: string
    default: ''
    required: false
    description: ''
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - delete
          resource:
          - document
    typeInfo: &id010
      type: string
      displayName: Document ID
      name: documentId
  - id: columns
    name: Columns / Attributes
    type: string
    default: ''
    required: true
    description: List of attributes to save
    placeholder: productId, modelName, description
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - document
          operation:
          - upsert
    typeInfo: &id008
      type: string
      displayName: Columns /Attributes
      name: columns
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id011
      displayOptions:
        show:
          operation:
          - query
          resource:
          - document
    typeInfo: &id012
      type: boolean
      displayName: Simplify
      name: simple
- id: upsert
  name: Create or Update
  description: Create a new document, or update the current one if it already exists
    (upsert)
  params:
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: As displayed in firebase console URL. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: database
    name: Database
    type: string
    default: (default)
    required: true
    description: Usually the provided default value will work
    validation: *id003
    typeInfo: *id004
  - id: collection
    name: Collection
    type: string
    default: ''
    required: true
    description: Collection name
    validation: *id005
    typeInfo: *id006
  - id: updateKey
    name: Update Key
    type: string
    default: ''
    required: true
    description: Name of the field in an input item that contains the document ID
    placeholder: documentId
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - document
          operation:
          - upsert
    typeInfo:
      type: string
      displayName: Update Key
      name: updateKey
  - id: columns
    name: Columns /Attributes
    type: string
    default: ''
    required: true
    description: Columns to insert
    placeholder: age, city, location
    validation: *id007
    typeInfo: *id008
- id: delete
  name: Delete
  description: Delete a document
  params:
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: As displayed in firebase console URL. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: database
    name: Database
    type: string
    default: (default)
    required: true
    description: Usually the provided default value will work
    validation: *id003
    typeInfo: *id004
  - id: collection
    name: Collection
    type: string
    default: ''
    required: true
    description: Collection name
    validation: *id005
    typeInfo: *id006
  - id: documentId
    name: Document ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
- id: get
  name: Get
  description: Get a document
  params:
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: As displayed in firebase console URL. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: database
    name: Database
    type: string
    default: (default)
    required: true
    description: Usually the provided default value will work
    validation: *id003
    typeInfo: *id004
  - id: collection
    name: Collection
    type: string
    default: ''
    required: true
    description: Collection name
    validation: *id005
    typeInfo: *id006
  - id: documentId
    name: Document ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id011
    typeInfo: *id012
- id: getAll
  name: Get Many
  description: Get many documents from a collection
  params:
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: As displayed in firebase console URL. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: database
    name: Database
    type: string
    default: (default)
    required: true
    description: Usually the provided default value will work
    validation: *id003
    typeInfo: *id004
  - id: collection
    name: Collection
    type: string
    default: ''
    required: true
    description: Collection name
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - collection
          operation:
          - getAll
    typeInfo: &id014
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id015
      displayOptions:
        show:
          resource:
          - collection
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id016
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id011
    typeInfo: *id012
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: As displayed in firebase console URL. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: database
    name: Database
    type: string
    default: (default)
    required: true
    description: Usually the provided default value will work
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: *id013
    typeInfo: *id014
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id015
    typeInfo: *id016
- id: update
  name: Update
  description: Update a document
- id: query
  name: Query
  description: Runs a query against your documents
  params:
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: As displayed in firebase console URL. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: database
    name: Database
    type: string
    default: (default)
    required: true
    description: Usually the provided default value will work
    validation: *id003
    typeInfo: *id004
  - id: query
    name: Query JSON
    type: string
    default: ''
    required: true
    description: JSON query to execute
    placeholder: '{"structuredQuery": {"where": {"fieldFilter": {"field": {"fieldPath":
      "age"},"op": "EQUAL", "value": {"integerValue": 28}}}, "from": [{"collectionId":
      "users-collection"}]}}'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - document
          operation:
          - query
    typeInfo:
      type: string
      displayName: Query JSON
      name: query
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id011
    typeInfo: *id012
examples:
- name: Get Document
  parameters:
    authentication: googleFirebaseCloudFirestoreOAuth2Api
    resource: document
    operation: get
    projectId: test-project
    database: (default)
    collection: users
    documentId: test-doc-id
  workflow: CloudFirestore Document Get Test
- name: Query Documents
  parameters:
    authentication: googleFirebaseCloudFirestoreOAuth2Api
    resource: document
    operation: query
    projectId: test-project
    database: (default)
    query: '{"structuredQuery": {"where": {"fieldFilter": {"field": {"fieldPath":
      "active"}, "op": "EQUAL", "value": {"booleanValue": true}}}, "from": [{"collectionId":
      "users"}]}}'
  workflow: CloudFirestore Document Query Test
- name: Delete Document
  parameters:
    authentication: googleFirebaseCloudFirestoreOAuth2Api
    resource: document
    operation: delete
    projectId: test-project
    database: (default)
    collection: users
    documentId: test-doc-id
  workflow: CloudFirestore Document Delete Test
common_expressions:
- '={{$parameter["resource"] + ": " + $parameter["operation"]}}'
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
  - field: columns
    text: productId, modelName, description
  - field: updateKey
    text: documentId
  - field: columns
    text: age, city, location
  - field: updateKey
    text: documentId
  - field: columns
    text: age, city, location
  - field: query
    text: '{"structuredQuery": {"where": {"fieldFilter": {"field": {"fieldPath": "age"},"op":
      "EQUAL", "value": {"integerValue": 28}}}, "from": [{"collectionId": "users-collection"}]}}'
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
  "$id": "https://n8n.io/schemas/nodes/googleFirebaseCloudFirestore.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Cloud Firestore Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "upsert",
        "delete",
        "get",
        "getAll",
        "update",
        "query"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "googleFirebaseCloudFirestoreOAuth2Api",
            "serviceAccount"
          ],
          "default": "googleFirebaseCloudFirestoreOAuth2Api"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "document",
            "collection"
          ],
          "default": "document"
        },
        "operation": {
          "description": "Get many root collections",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "getAll"
        },
        "projectId": {
          "description": "As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "database": {
          "description": "Usually the provided default value will work",
          "type": "string",
          "default": "(default)"
        },
        "collection": {
          "description": "Collection name",
          "type": "string",
          "default": ""
        },
        "documentId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "columns": {
          "description": "Columns to insert",
          "type": "string",
          "default": "",
          "examples": [
            "age, city, location"
          ]
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
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
        "updateKey": {
          "description": "Name of the field in an input item that contains the document ID",
          "type": "string",
          "default": "",
          "examples": [
            "documentId"
          ]
        },
        "query": {
          "description": "JSON query to execute",
          "type": "string",
          "default": "",
          "examples": [
            "{\"structuredQuery\": {\"where\": {\"fieldFilter\": {\"field\": {\"fieldPath\": \"age\"},\"op\": \"EQUAL\", \"value\": {\"integerValue\": 28}}}, \"from\": [{\"collectionId\": \"users-collection\"}]}}"
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
    "version": [
      "1",
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "googleFirebaseCloudFirestoreOAuth2Api",
      "required": true
    },
    {
      "name": "googleApi",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Get Document",
      "value": {
        "authentication": "googleFirebaseCloudFirestoreOAuth2Api",
        "resource": "document",
        "operation": "get",
        "projectId": "test-project",
        "database": "(default)",
        "collection": "users",
        "documentId": "test-doc-id"
      }
    },
    {
      "description": "Query Documents",
      "value": {
        "authentication": "googleFirebaseCloudFirestoreOAuth2Api",
        "resource": "document",
        "operation": "query",
        "projectId": "test-project",
        "database": "(default)",
        "query": "{\"structuredQuery\": {\"where\": {\"fieldFilter\": {\"field\": {\"fieldPath\": \"active\"}, \"op\": \"EQUAL\", \"value\": {\"booleanValue\": true}}}, \"from\": [{\"collectionId\": \"users\"}]}}"
      }
    },
    {
      "description": "Delete Document",
      "value": {
        "authentication": "googleFirebaseCloudFirestoreOAuth2Api",
        "resource": "document",
        "operation": "delete",
        "projectId": "test-project",
        "database": "(default)",
        "collection": "users",
        "documentId": "test-doc-id"
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
