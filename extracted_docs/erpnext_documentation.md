---
title: "Node: ERPNext"
slug: "node-erpnext"
version: "1"
updated: "2026-01-08"
summary: "Consume ERPNext API"
node_type: "regular"
group: "['output']"
---

# Node: ERPNext

**Purpose.** Consume ERPNext API
**Subtitle.** ={{$parameter["resource"] + ": " + $parameter["operation"]}}


---

## Node Details

- **Icon:** `file:erpnext.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **erpNextApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `erpNextApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Document Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a document |
| Delete | `delete` | Delete a document |
| Get | `get` | Retrieve a document |
| Get Many | `getAll` | Retrieve many documents |
| Update | `update` | Update a document |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | document | ✗ | Resource to operate on |  |

**Resource options:**

* **Document** (`document`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a document |  |

**Operation options:**

* **Create** (`create`) - Create a document
* **Delete** (`delete`) - Delete a document
* **Get** (`get`) - Retrieve a document
* **Get Many** (`getAll`) - Retrieve many documents
* **Update** (`update`) - Update a document

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| DocType Name or ID | `docType` | options |  | ✓ | DocType you would like to create. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Customer |  |
| Properties | `properties` | fixedCollection | {} | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Property |  |

<details>
<summary><strong>Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Property | `customProperty` |  |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| DocType Name or ID | `docType` | options |  | ✓ | The type of document you would like to delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Document Name | `documentName` | string |  | ✓ | The name (ID) of document you would like to get |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| DocType Name or ID | `docType` | options |  | ✓ | The type of document you would like to get. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Document Name | `documentName` | string |  | ✓ | The name (ID) of document you would like to get |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| DocType Name or ID | `docType` | options |  | ✗ | DocType whose documents to retrieve. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Customer |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:∞ |
| Options | `options` | collection | {} | ✗ | Comma-separated list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field Names or IDs | `fields` | multiOptions | [] | Comma-separated list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Filters | `filters` | fixedCollection | {} | Custom Properties |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| DocType Name or ID | `docType` | options |  | ✓ | The type of document you would like to update. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Document Name | `documentName` | string |  | ✓ | The name (ID) of document you would like to get |  |
| Properties | `properties` | fixedCollection | {} | ✗ | Properties of request body | e.g. Add Property |  |

<details>
<summary><strong>Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Property | `customProperty` |  |  |  |

</details>


---

## Load Options Methods

- `getDocTypes`

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
* Categories: Finance & Accounting, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: erpNext
displayName: ERPNext
description: Consume ERPNext API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: erpNextApi
  required: true
operations:
- id: create
  name: Create
  description: Create a document
  params:
  - id: docType
    name: DocType Name or ID
    type: options
    default: ''
    required: true
    description: DocType you would like to create. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    placeholder: Customer
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - document
          operation:
          - update
    typeInfo: &id002
      type: options
      displayName: DocType Name or ID
      name: docType
      typeOptions:
        loadOptionsMethod: getDocTypes
      possibleValues: []
  - id: properties
    name: Properties
    type: fixedCollection
    default: {}
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Property
    validation: &id005
      displayOptions:
        show:
          resource:
          - document
          operation:
          - update
    typeInfo: &id006
      type: fixedCollection
      displayName: Properties
      name: properties
      typeOptions:
        multipleValues: true
      subProperties:
      - name: customProperty
        displayName: Property
        values:
        - displayName: Field Name or ID
          name: field
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getDocFields
        - displayName: Value
          name: value
          type: string
          default: ''
- id: delete
  name: Delete
  description: Delete a document
  params:
  - id: docType
    name: DocType Name or ID
    type: options
    default: ''
    required: true
    description: The type of document you would like to delete. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: documentName
    name: Document Name
    type: string
    default: ''
    required: true
    description: The name (ID) of document you would like to get
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - document
          operation:
          - update
    typeInfo: &id004
      type: string
      displayName: Document Name
      name: documentName
- id: get
  name: Get
  description: Retrieve a document
  params:
  - id: docType
    name: DocType Name or ID
    type: options
    default: ''
    required: true
    description: The type of document you would like to get. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: documentName
    name: Document Name
    type: string
    default: ''
    required: true
    description: The name (ID) of document you would like to get
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: Retrieve many documents
  params:
  - id: docType
    name: DocType Name or ID
    type: options
    default: ''
    required: false
    description: DocType whose documents to retrieve. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    placeholder: Customer
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
          - document
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          resource:
          - document
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
- id: update
  name: Update
  description: Update a document
  params:
  - id: docType
    name: DocType Name or ID
    type: options
    default: ''
    required: true
    description: The type of document you would like to update. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: documentName
    name: Document Name
    type: string
    default: ''
    required: true
    description: The name (ID) of document you would like to get
    validation: *id003
    typeInfo: *id004
  - id: properties
    name: Properties
    type: fixedCollection
    default: {}
    required: false
    description: Properties of request body
    placeholder: Add Property
    validation: *id005
    typeInfo: *id006
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
  - field: docType
    text: Customer
  - field: options
    text: Add Field
  - field: docType
    text: Customer
  - field: properties
    text: Add Property
  - field: properties
    text: Add Property
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
  "$id": "https://n8n.io/schemas/nodes/erpNext.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ERPNext Node",
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
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "document"
          ],
          "default": "document"
        },
        "operation": {
          "description": "Create a document",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "docType": {
          "description": "The type of document you would like to update. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
          "default": 10
        },
        "options": {
          "description": "Comma-separated list of fields to return. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "properties": {
          "description": "Properties of request body",
          "type": "string",
          "default": {},
          "examples": [
            "Add Property"
          ]
        },
        "documentName": {
          "description": "The name (ID) of document you would like to get",
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
      "name": "erpNextApi",
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
