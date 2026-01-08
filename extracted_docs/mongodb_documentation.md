---
title: "Node: MongoDB"
slug: "node-mongodb"
version: "['1', '1.1', '1.2']"
updated: "2026-01-08"
summary: "Find, insert and update documents in MongoDB"
node_type: "regular"
group: "['input']"
---

# Node: MongoDB

**Purpose.** Find, insert and update documents in MongoDB


---

## Node Details

- **Icon:** `file:mongodb.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **mongoDb**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `mongoDb` | ✓ | - |

---

## Operations

### Document Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Aggregate | `aggregate` | Aggregate documents |
| Delete | `delete` | Delete documents |
| Find | `find` | Find documents |
| Find And Replace | `findOneAndReplace` | Find and replace documents |
| Find And Update | `findOneAndUpdate` | Find and update documents |
| Insert | `insert` | Insert documents |
| Update | `update` | Update documents |

### Searchindexes Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `createSearchIndex` | Create Search Index |
| Drop | `dropSearchIndex` | Drop Search Index |
| List | `listSearchIndexes` | List Search Indexes |
| Update | `updateSearchIndex` | Update Search Index |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | document | ✗ | Resource to operate on |  |

**Resource options:**

* **Search Index** (`searchIndexes`)
* **Document** (`document`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | find | ✗ | Aggregate documents |  |

**Operation options:**

* **Aggregate** (`aggregate`) - Aggregate documents
* **Delete** (`delete`) - Delete documents
* **Find** (`find`) - Find documents
* **Find And Replace** (`findOneAndReplace`) - Find and replace documents
* **Find And Update** (`findOneAndUpdate`) - Find and update documents
* **Insert** (`insert`) - Insert documents
* **Update** (`update`) - Update documents

---

### Aggregate parameters (`aggregate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Query | `query` | json |  | ✓ | MongoDB aggregation pipeline query in JSON format | e.g. [{ "$match": { "$gt": "1950-01-01" }, ... }] |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Delete Query (JSON Format) | `query` | json | {} | ✓ | MongoDB Delete query | e.g. { "birth": { "$gt": "1950-01-01" } } |  |

### Find parameters (`find`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Options | `options` | collection | {} | ✗ | Add query options | e.g. Add option | min:1, max:∞ |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Limit | `limit` | number | 0 | Use limit to specify the maximum number of documents or 0 for unlimited documents |
| Skip | `skip` | number | 0 | The number of documents to skip in the results set |
| Sort (JSON Format) | `sort` | json | {} | A JSON that defines the sort order of the result set |
| Projection (JSON Format) | `projection` | json | {} | A JSON that defines a selection of fields to retrieve or exclude from the result set |

</details>

| Query (JSON Format) | `query` | json | {} | ✓ | MongoDB Find query | e.g. { "birth": { "$gt": "1950-01-01" } } |  |

### Find And Replace parameters (`findOneAndReplace`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Update Key | `updateKey` | string | id | ✓ | Name of the property which decides which rows in the database should be updated. Normally that would be "id". |  |
| Fields | `fields` | string |  | ✗ | Comma-separated list of the fields to be included into the new document | e.g. name,description |  |
| Upsert | `upsert` | boolean | False | ✗ | Whether to perform an insert if no documents match the update key |  |
| Options | `options` | collection | {} | ✗ | Comma-separated list of fields that will be parsed as Mongo Date type | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date Fields | `dateFields` | string |  | Comma-separated list of fields that will be parsed as Mongo Date type |
| Use Dot Notation | `useDotNotation` | boolean | False | Whether to use dot notation to access date fields |

</details>


### Find And Update parameters (`findOneAndUpdate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Update Key | `updateKey` | string | id | ✓ | Name of the property which decides which rows in the database should be updated. Normally that would be "id". |  |
| Fields | `fields` | string |  | ✗ | Comma-separated list of the fields to be included into the new document | e.g. name,description |  |
| Upsert | `upsert` | boolean | False | ✗ | Whether to perform an insert if no documents match the update key |  |
| Options | `options` | collection | {} | ✗ | Comma-separated list of fields that will be parsed as Mongo Date type | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date Fields | `dateFields` | string |  | Comma-separated list of fields that will be parsed as Mongo Date type |
| Use Dot Notation | `useDotNotation` | boolean | False | Whether to use dot notation to access date fields |

</details>


### Insert parameters (`insert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Fields | `fields` | string |  | ✗ | Comma-separated list of the fields to be included into the new document | e.g. name,description |  |
| Options | `options` | collection | {} | ✗ | Comma-separated list of fields that will be parsed as Mongo Date type | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date Fields | `dateFields` | string |  | Comma-separated list of fields that will be parsed as Mongo Date type |
| Use Dot Notation | `useDotNotation` | boolean | False | Whether to use dot notation to access date fields |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Update Key | `updateKey` | string | id | ✓ | Name of the property which decides which rows in the database should be updated. Normally that would be "id". |  |
| Fields | `fields` | string |  | ✗ | Comma-separated list of the fields to be included into the new document | e.g. name,description |  |
| Upsert | `upsert` | boolean | False | ✗ | Whether to perform an insert if no documents match the update key |  |
| Options | `options` | collection | {} | ✗ | Comma-separated list of fields that will be parsed as Mongo Date type | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date Fields | `dateFields` | string |  | Comma-separated list of fields that will be parsed as Mongo Date type |
| Use Dot Notation | `useDotNotation` | boolean | False | Whether to use dot notation to access date fields |

</details>


### Create parameters (`createSearchIndex`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Index Name | `indexNameRequired` | string |  | ✓ | The name of the search index |  |
| Index Definition | `indexDefinition` | json | {} | ✓ | The search index definition | e.g. { "type": "vectorSearch", "definition": {} } |  |
| Index Type | `indexType` | options | vectorSearch | ✓ | The search index index type |  |

**Index Type options:**

* **Vector Search** (`vectorSearch`)
* **Search** (`search`)


### Drop parameters (`dropSearchIndex`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Index Name | `indexNameRequired` | string |  | ✓ | The name of the search index |  |

### List parameters (`listSearchIndexes`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Index Name | `indexName` | string |  | ✗ | If provided, only lists indexes with the specified name |  |

### Update parameters (`updateSearchIndex`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Index Name | `indexNameRequired` | string |  | ✓ | The name of the search index |  |
| Index Definition | `indexDefinition` | json | {} | ✓ | The search index definition | e.g. { "type": "vectorSearch", "definition": {} } |  |

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
node: mongoDb
displayName: MongoDB
description: Find, insert and update documents in MongoDB
version:
- '1'
- '1.1'
- '1.2'
nodeType: regular
group:
- input
credentials:
- name: mongoDb
  required: true
operations:
- id: aggregate
  name: Aggregate
  description: Aggregate documents
  params:
  - id: query
    name: Query
    type: json
    default: ''
    required: true
    description: MongoDB aggregation pipeline query in JSON format
    hint: Learn more about aggregation pipeline <a href="https://docs.mongodb.com/manual/core/aggregation-pipeline/">here</a>
    placeholder: '[{ "$match": { "$gt": "1950-01-01" }, ... }]'
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - find
          resource:
          - document
    typeInfo: &id002
      type: json
      displayName: Query (JSON Format)
      name: query
      typeOptions:
        rows: 5
- id: delete
  name: Delete
  description: Delete documents
  params:
  - id: query
    name: Delete Query (JSON Format)
    type: json
    default: '{}'
    required: true
    description: MongoDB Delete query
    placeholder: '{ "birth": { "$gt": "1950-01-01" } }'
    validation: *id001
    typeInfo: *id002
- id: find
  name: Find
  description: Find documents
  params:
  - id: query
    name: Query (JSON Format)
    type: json
    default: '{}'
    required: true
    description: MongoDB Find query
    placeholder: '{ "birth": { "$gt": "1950-01-01" } }'
    validation: *id001
    typeInfo: *id002
- id: findOneAndReplace
  name: Find And Replace
  description: Find and replace documents
  params:
  - id: updateKey
    name: Update Key
    type: string
    default: id
    required: true
    description: Name of the property which decides which rows in the database should
      be updated. Normally that would be "id".
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - update
          - findOneAndReplace
          - findOneAndUpdate
          resource:
          - document
    typeInfo: &id004
      type: string
      displayName: Update Key
      name: updateKey
  - id: fields
    name: Fields
    type: string
    default: ''
    required: false
    description: Comma-separated list of the fields to be included into the new document
    placeholder: name,description
    validation: &id005
      displayOptions:
        show:
          operation:
          - update
          - findOneAndReplace
          - findOneAndUpdate
          resource:
          - document
    typeInfo: &id006
      type: string
      displayName: Fields
      name: fields
  - id: upsert
    name: Upsert
    type: boolean
    default: false
    required: false
    description: Whether to perform an insert if no documents match the update key
    validation: &id007
      displayOptions:
        show:
          operation:
          - update
          - findOneAndReplace
          - findOneAndUpdate
          resource:
          - document
    typeInfo: &id008
      type: boolean
      displayName: Upsert
      name: upsert
- id: findOneAndUpdate
  name: Find And Update
  description: Find and update documents
  params:
  - id: updateKey
    name: Update Key
    type: string
    default: id
    required: true
    description: Name of the property which decides which rows in the database should
      be updated. Normally that would be "id".
    validation: *id003
    typeInfo: *id004
  - id: fields
    name: Fields
    type: string
    default: ''
    required: false
    description: Comma-separated list of the fields to be included into the new document
    placeholder: name,description
    validation: *id005
    typeInfo: *id006
  - id: upsert
    name: Upsert
    type: boolean
    default: false
    required: false
    description: Whether to perform an insert if no documents match the update key
    validation: *id007
    typeInfo: *id008
- id: insert
  name: Insert
  description: Insert documents
  params:
  - id: fields
    name: Fields
    type: string
    default: ''
    required: false
    description: Comma-separated list of the fields to be included into the new document
    placeholder: name,description
    validation: *id005
    typeInfo: *id006
- id: update
  name: Update
  description: Update documents
  params:
  - id: updateKey
    name: Update Key
    type: string
    default: id
    required: true
    description: Name of the property which decides which rows in the database should
      be updated. Normally that would be "id".
    validation: *id003
    typeInfo: *id004
  - id: fields
    name: Fields
    type: string
    default: ''
    required: false
    description: Comma-separated list of the fields to be included into the new document
    placeholder: name,description
    validation: *id005
    typeInfo: *id006
  - id: upsert
    name: Upsert
    type: boolean
    default: false
    required: false
    description: Whether to perform an insert if no documents match the update key
    validation: *id007
    typeInfo: *id008
- id: createSearchIndex
  name: Create
  description: ''
  params:
  - id: indexNameRequired
    name: Index Name
    type: string
    default: ''
    required: true
    description: The name of the search index
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - createSearchIndex
          - dropSearchIndex
          - updateSearchIndex
          resource:
          - searchIndexes
    typeInfo: &id010
      type: string
      displayName: Index Name
      name: indexNameRequired
  - id: indexDefinition
    name: Index Definition
    type: json
    default: '{}'
    required: true
    description: The search index definition
    hint: Learn more about search index definitions <a href="https://www.mongodb.com/docs/atlas/atlas-search/index-definitions/">here</a>
    placeholder: '{ "type": "vectorSearch", "definition": {} }'
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - createSearchIndex
          - updateSearchIndex
          resource:
          - searchIndexes
    typeInfo: &id012
      type: json
      displayName: Index Definition
      name: indexDefinition
      typeOptions:
        alwaysOpenEditWindow: true
  - id: indexType
    name: Index Type
    type: options
    default: vectorSearch
    required: true
    description: The search index index type
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - createSearchIndex
          resource:
          - searchIndexes
    typeInfo:
      type: options
      displayName: Index Type
      name: indexType
      possibleValues:
      - value: vectorSearch
        name: Vector Search
        description: ''
      - value: search
        name: Search
        description: ''
- id: dropSearchIndex
  name: Drop
  description: ''
  params:
  - id: indexNameRequired
    name: Index Name
    type: string
    default: ''
    required: true
    description: The name of the search index
    validation: *id009
    typeInfo: *id010
- id: listSearchIndexes
  name: List
  description: ''
  params:
  - id: indexName
    name: Index Name
    type: string
    default: ''
    required: false
    description: If provided, only lists indexes with the specified name
    validation:
      displayOptions:
        show:
          operation:
          - listSearchIndexes
          resource:
          - searchIndexes
    typeInfo:
      type: string
      displayName: Index Name
      name: indexName
- id: updateSearchIndex
  name: Update
  description: ''
  params:
  - id: indexNameRequired
    name: Index Name
    type: string
    default: ''
    required: true
    description: The name of the search index
    validation: *id009
    typeInfo: *id010
  - id: indexDefinition
    name: Index Definition
    type: json
    default: '{}'
    required: true
    description: The search index definition
    hint: Learn more about search index definitions <a href="https://www.mongodb.com/docs/atlas/atlas-search/index-definitions/">here</a>
    placeholder: '{ "type": "vectorSearch", "definition": {} }'
    validation: *id011
    typeInfo: *id012
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: query
    text: '[{ "$match": { "$gt": "1950-01-01" }, ... }]'
  - field: query
    text: '{ "birth": { "$gt": "1950-01-01" } }'
  - field: options
    text: Add option
  - field: query
    text: '{ "birth": { "$gt": "1950-01-01" } }'
  - field: fields
    text: name,description
  - field: fields
    text: name,description
  - field: options
    text: Add option
  - field: indexDefinition
    text: '{ "type": "vectorSearch", "definition": {} }'
  hints:
  - field: query
    text: Learn more about aggregation pipeline <a href="https://docs.mongodb.com/manual/core/aggregation-pipeline/">here</a>
  - field: indexDefinition
    text: Learn more about search index definitions <a href="https://www.mongodb.com/docs/atlas/atlas-search/index-definitions/">here</a>
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
  "$id": "https://n8n.io/schemas/nodes/mongoDb.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MongoDB Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "aggregate",
        "delete",
        "find",
        "findOneAndReplace",
        "findOneAndUpdate",
        "insert",
        "update",
        "createSearchIndex",
        "dropSearchIndex",
        "listSearchIndexes",
        "updateSearchIndex"
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
            "searchIndexes",
            "document"
          ],
          "default": "document"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "createSearchIndex",
            "dropSearchIndex",
            "listSearchIndexes",
            "updateSearchIndex"
          ],
          "default": "createSearchIndex"
        },
        "collection": {
          "description": "MongoDB Collection",
          "type": "string",
          "default": ""
        },
        "query": {
          "description": "MongoDB Find query",
          "type": "string",
          "default": "{}",
          "examples": [
            "{ \"birth\": { \"$gt\": \"1950-01-01\" } }"
          ]
        },
        "options": {
          "description": "Comma-separated list of fields that will be parsed as Mongo Date type",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "fields": {
          "description": "Comma-separated list of the fields to be included into the new document",
          "type": "string",
          "default": "",
          "examples": [
            "name,description"
          ]
        },
        "updateKey": {
          "description": "Name of the property which decides which rows in the database should be updated. Normally that would be \"id\".",
          "type": "string",
          "default": "id"
        },
        "upsert": {
          "description": "Whether to perform an insert if no documents match the update key",
          "type": "boolean",
          "default": false
        },
        "indexName": {
          "description": "If provided, only lists indexes with the specified name",
          "type": "string",
          "default": ""
        },
        "indexNameRequired": {
          "description": "The name of the search index",
          "type": "string",
          "default": ""
        },
        "indexDefinition": {
          "description": "The search index definition",
          "type": "string",
          "default": "{}",
          "examples": [
            "{ \"type\": \"vectorSearch\", \"definition\": {} }"
          ]
        },
        "indexType": {
          "description": "The search index index type",
          "type": "string",
          "enum": [
            "vectorSearch",
            "search"
          ],
          "default": "vectorSearch"
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
      "1.1",
      "1.2"
    ]
  },
  "credentials": [
    {
      "name": "mongoDb",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1', '1.2'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
