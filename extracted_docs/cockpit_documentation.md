---
title: "Node: Cockpit"
slug: "node-cockpit"
version: "1"
updated: "2026-01-08"
summary: "Consume Cockpit API"
node_type: "regular"
group: "['output']"
---

# Node: Cockpit

**Purpose.** Consume Cockpit API
**Subtitle.** ={{ $parameter["operation"] + ": " + $parameter["resource"] }}


---

## Node Details

- **Icon:** `{'light': 'file:cockpit.svg', 'dark': 'file:cockpit.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **cockpitApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `cockpitApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Collection Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create an Entry | `create` | Create a collection entry |
| Get Many Entries | `getAll` | Get many collection entries |
| Update an Entry | `update` | Update a collection entry |

### Form Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Submit a Form | `submit` | Store data from a form submission |

### Singleton Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a singleton |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | collection | ✗ | Resource to operate on |  |

**Resource options:**

* **Collection** (`collection`)
* **Form** (`form`)
* **Singleton** (`singleton`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Create a collection entry |  |

**Operation options:**

* **Create an Entry** (`create`) - Create a collection entry
* **Get Many Entries** (`getAll`) - Get many collection entries
* **Update an Entry** (`update`) - Update a collection entry

---

### Create an Entry parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| JSON Data Fields | `jsonDataFields` | boolean | False | ✗ | Whether new entry fields should be set via the value-key pair UI or JSON |  |
| Entry Data | `dataFieldsJson` | json |  | ✗ | Entry data to send as JSON |  |
| Entry Data | `dataFieldsUi` | fixedCollection | {} | ✗ | Name of the field |  |

<details>
<summary><strong>Entry Data sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `field` |  |  |  |

</details>


### Get Many Entries parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Comma-separated list of fields to get | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Comma-separated list of fields to get |
| Filter Query | `filter` | json |  | Filter query in <a href="https://jeroen.github.io/mongolite/query-data.html">Mongolite format</a> |
| Language | `language` | string |  | Return normalized language fields |
| Populate | `populate` | boolean | True | Whether to resolve linked collection items |
| RAW Data | `rawData` | boolean | False | Whether to return the data exactly in the way it got received from the API |
| Skip | `skip` | number |  | Skip number of entries |
| Sort Query | `sort` | json |  | Sort query in <a href="https://jeroen.github.io/mongolite/query-data.html">Mongolite format</a> |

</details>


### Update an Entry parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Entry ID | `id` | string |  | ✓ |  |  |
| JSON Data Fields | `jsonDataFields` | boolean | False | ✗ | Whether new entry fields should be set via the value-key pair UI or JSON |  |
| Entry Data | `dataFieldsJson` | json |  | ✗ | Entry data to send as JSON |  |
| Entry Data | `dataFieldsUi` | fixedCollection | {} | ✗ | Name of the field |  |

<details>
<summary><strong>Entry Data sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `field` |  |  |  |

</details>


### Submit a Form parameters (`submit`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| JSON Data Fields | `jsonDataFields` | boolean | False | ✗ | Whether form fields should be set via the value-key pair UI or JSON |  |
| Form Data | `dataFieldsJson` | json |  | ✗ | Form data to send as JSON |  |
| Form Data | `dataFieldsUi` | fixedCollection | {} | ✗ | Name of the field |  |

<details>
<summary><strong>Form Data sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `field` |  |  |  |

</details>


---

## Load Options Methods

- `getCollections`
- `name`
- `value`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter["operation"] + ": " + $parameter["resource"] }}`

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
* Categories: Marketing, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: cockpit
displayName: Cockpit
description: Consume Cockpit API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: cockpitApi
  required: true
operations:
- id: create
  name: Create an Entry
  description: Create a collection entry
  params:
  - id: jsonDataFields
    name: JSON Data Fields
    type: boolean
    default: false
    required: false
    description: Whether new entry fields should be set via the value-key pair UI
      or JSON
    validation: &id001
      displayOptions:
        show:
          resource:
          - form
          operation:
          - submit
    typeInfo: &id002
      type: boolean
      displayName: JSON Data Fields
      name: jsonDataFields
  - id: dataFieldsJson
    name: Entry Data
    type: json
    default: ''
    required: false
    description: Entry data to send as JSON
    validation: &id003
      displayOptions:
        show:
          jsonDataFields:
          - true
          resource:
          - form
          operation:
          - submit
    typeInfo: &id004
      type: json
      displayName: Form Data
      name: dataFieldsJson
      typeOptions:
        alwaysOpenEditWindow: true
  - id: dataFieldsUi
    name: Entry Data
    type: fixedCollection
    default: &id005 {}
    required: false
    description: Name of the field
    validation: &id006
      displayOptions:
        show:
          jsonDataFields:
          - false
          resource:
          - form
          operation:
          - submit
    typeInfo: &id007
      type: fixedCollection
      displayName: Form Data
      name: dataFieldsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: field
        displayName: Field
        values:
        - displayName: Name
          name: name
          type: string
          description: Name of the field
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value of the field
          default: ''
- id: getAll
  name: Get Many Entries
  description: Get many collection entries
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
          - getAll
          resource:
          - collection
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
          - getAll
          resource:
          - collection
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
- id: update
  name: Update an Entry
  description: Update a collection entry
  params:
  - id: id
    name: Entry ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - collection
          operation:
          - update
    typeInfo:
      type: string
      displayName: Entry ID
      name: id
  - id: jsonDataFields
    name: JSON Data Fields
    type: boolean
    default: false
    required: false
    description: Whether new entry fields should be set via the value-key pair UI
      or JSON
    validation: *id001
    typeInfo: *id002
  - id: dataFieldsJson
    name: Entry Data
    type: json
    default: ''
    required: false
    description: Entry data to send as JSON
    validation: *id003
    typeInfo: *id004
  - id: dataFieldsUi
    name: Entry Data
    type: fixedCollection
    default: *id005
    required: false
    description: Name of the field
    validation: *id006
    typeInfo: *id007
- id: submit
  name: Submit a Form
  description: Store data from a form submission
  params:
  - id: jsonDataFields
    name: JSON Data Fields
    type: boolean
    default: false
    required: false
    description: Whether form fields should be set via the value-key pair UI or JSON
    validation: *id001
    typeInfo: *id002
  - id: dataFieldsJson
    name: Form Data
    type: json
    default: ''
    required: false
    description: Form data to send as JSON
    validation: *id003
    typeInfo: *id004
  - id: dataFieldsUi
    name: Form Data
    type: fixedCollection
    default: {}
    required: false
    description: Name of the field
    validation: *id006
    typeInfo: *id007
- id: get
  name: Get
  description: Get a singleton
common_expressions:
- '={{ $parameter["operation"] + ": " + $parameter["resource"] }}'
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
  "$id": "https://n8n.io/schemas/nodes/cockpit.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Cockpit Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "getAll",
        "update",
        "submit",
        "get"
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
            "collection",
            "form",
            "singleton"
          ],
          "default": "collection"
        },
        "operation": {
          "description": "Get a singleton",
          "type": "string",
          "enum": [
            "get"
          ],
          "default": "get"
        },
        "collection": {
          "description": "Name of the collection to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
          "description": "Comma-separated list of fields to get",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "id": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "jsonDataFields": {
          "description": "Whether form fields should be set via the value-key pair UI or JSON",
          "type": "boolean",
          "default": false
        },
        "dataFieldsJson": {
          "description": "Form data to send as JSON",
          "type": "string",
          "default": ""
        },
        "dataFieldsUi": {
          "description": "Name of the field",
          "type": "string",
          "default": {}
        },
        "form": {
          "description": "Name of the form to operate on",
          "type": "string",
          "default": ""
        },
        "singleton": {
          "description": "Name of the singleton to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
      "name": "cockpitApi",
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
