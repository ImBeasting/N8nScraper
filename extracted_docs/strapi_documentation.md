---
title: "Node: Strapi"
slug: "node-strapi"
version: "1"
updated: "2025-11-13"
summary: "Consume Strapi API"
node_type: "regular"
group: "['input']"
---

# Node: Strapi

**Purpose.** Consume Strapi API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:strapi.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **strapiApi**: N/A
- **strapiTokenApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `strapiApi` | ✓ | {'show': {'authentication': ['password']}} |
| `strapiTokenApi` | ✓ | {'show': {'authentication': ['token']}} |

---

## API Patterns

**HTTP Methods:** POST

**Headers Used:** content-type

---

## Operations

### Entry Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an entry |
| Delete | `delete` | Delete an entry |
| Get | `get` | Get an entry |
| Get Many | `getAll` | Get many entries |
| Update | `update` | Update an entry |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | entry | ✗ | Resource to operate on |  |

**Resource options:**

* **Entry** (`entry`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Create an entry |  |

**Operation options:**

* **Create** (`create`) - Create an entry
* **Delete** (`delete`) - Delete an entry
* **Get** (`get`) - Get an entry
* **Get Many** (`getAll`) - Get many entries
* **Update** (`update`) - Update an entry

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Content Type | `contentType` | string |  | ✓ | Name of the content type |  |
| Columns | `columns` | string |  | ✗ | Comma-separated list of the properties which should used as columns for the new rows | e.g. id,name,description |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Content Type | `contentType` | string |  | ✓ | Name of the content type |  |
| Entry ID | `entryId` | string |  | ✓ | The ID of the entry to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Content Type | `contentType` | string |  | ✓ | Name of the content type |  |
| Entry ID | `entryId` | string |  | ✓ | The ID of the entry to get |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Content Type | `contentType` | string |  | ✓ | Name of the content type |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Only select entries matching the publication state provided | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Publication State | `publicationState` | options |  | Only select entries matching the publication state provided |
| Sort Fields | `sort` | string |  | Name of the fields to sort the data by. By default will be sorted ascendingly. To modify that behavior, you have to add the sort direction after the name of sort field preceded by a colon. For example: <code>name:asc</code>. |
| Where (JSON) | `where` | string |  | JSON query to filter the data. <a href="https://strapi.io/documentation/developer-docs/latest/developer-resources/content-api/content-api.html#filters">More info</a>. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Content Type | `contentType` | string |  | ✓ | Name of the content type |  |
| Update Key | `updateKey` | string | id | ✓ | Name of the property which decides which rows in the database should be updated. Normally that would be "id". |  |
| Columns | `columns` | string |  | ✗ | Comma-separated list of the properties which should used as columns for the new rows | e.g. id,name,description |  |

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
* Categories: Data & Storage, Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: strapi
displayName: Strapi
description: Consume Strapi API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: strapiApi
  required: true
- name: strapiTokenApi
  required: true
operations:
- id: create
  name: Create
  description: Create an entry
  params:
  - id: contentType
    name: Content Type
    type: string
    default: ''
    required: true
    description: Name of the content type
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - entry
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: Content Type
      name: contentType
  - id: columns
    name: Columns
    type: string
    default: ''
    required: false
    description: Comma-separated list of the properties which should used as columns
      for the new rows
    placeholder: id,name,description
    validation: &id005
      displayOptions:
        show:
          resource:
          - entry
          operation:
          - update
    typeInfo: &id006
      type: string
      displayName: Columns
      name: columns
- id: delete
  name: Delete
  description: Delete an entry
  params:
  - id: contentType
    name: Content Type
    type: string
    default: ''
    required: true
    description: Name of the content type
    validation: *id001
    typeInfo: *id002
  - id: entryId
    name: Entry ID
    type: string
    default: ''
    required: true
    description: The ID of the entry to delete
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - entry
          operation:
          - get
    typeInfo: &id004
      type: string
      displayName: Entry ID
      name: entryId
- id: get
  name: Get
  description: Get an entry
  params:
  - id: contentType
    name: Content Type
    type: string
    default: ''
    required: true
    description: Name of the content type
    validation: *id001
    typeInfo: *id002
  - id: entryId
    name: Entry ID
    type: string
    default: ''
    required: true
    description: The ID of the entry to get
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: Get many entries
  params:
  - id: contentType
    name: Content Type
    type: string
    default: ''
    required: true
    description: Name of the content type
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          resource:
          - entry
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          resource:
          - entry
          operation:
          - getAll
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
- id: update
  name: Update
  description: Update an entry
  params:
  - id: contentType
    name: Content Type
    type: string
    default: ''
    required: true
    description: Name of the content type
    validation: *id001
    typeInfo: *id002
  - id: updateKey
    name: Update Key
    type: string
    default: id
    required: true
    description: Name of the property which decides which rows in the database should
      be updated. Normally that would be "id".
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - entry
          operation:
          - update
    typeInfo:
      type: string
      displayName: Update Key
      name: updateKey
  - id: columns
    name: Columns
    type: string
    default: ''
    required: false
    description: Comma-separated list of the properties which should used as columns
      for the new rows
    placeholder: id,name,description
    validation: *id005
    typeInfo: *id006
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - POST
  endpoints: []
  headers:
  - content-type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: columns
    text: id,name,description
  - field: options
    text: Add Field
  - field: columns
    text: id,name,description
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
  "$id": "https://n8n.io/schemas/nodes/strapi.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Strapi Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "get",
        "getAll",
        "update"
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
            "password",
            "token"
          ],
          "default": "password"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "entry"
          ],
          "default": "entry"
        },
        "operation": {
          "description": "Create an entry",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "get"
        },
        "contentType": {
          "description": "Name of the content type",
          "type": "string",
          "default": ""
        },
        "columns": {
          "description": "Comma-separated list of the properties which should used as columns for the new rows",
          "type": "string",
          "default": "",
          "examples": [
            "id,name,description"
          ]
        },
        "entryId": {
          "description": "The ID of the entry to get",
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
          "default": 50
        },
        "options": {
          "description": "Only select entries matching the publication state provided",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateKey": {
          "description": "Name of the property which decides which rows in the database should be updated. Normally that would be \"id\".",
          "type": "string",
          "default": "id"
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
      "name": "strapiApi",
      "required": true
    },
    {
      "name": "strapiTokenApi",
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
