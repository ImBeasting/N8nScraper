---
title: "Node: Bubble"
slug: "node-bubble"
version: "1"
updated: "2025-11-13"
summary: "Consume the Bubble Data API"
node_type: "regular"
group: "['transform']"
---

# Node: Bubble

**Purpose.** Consume the Bubble Data API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:bubble.svg', 'dark': 'file:bubble.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **bubbleApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `bubbleApi` | ✓ | - |

---

## API Patterns

**Headers Used:** user-agent

---

## Operations

### Object Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an object |
| Delete | `delete` | Delete an object |
| Get | `get` | Get an object |
| Get Many | `getAll` | Get many objects |
| Update | `update` | Update an object |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | object | ✗ | Resource to operate on |  |

**Resource options:**

* **Object** (`object`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create an object
* **Delete** (`delete`) - Delete an object
* **Get** (`get`) - Get an object
* **Get Many** (`getAll`) - Get many objects
* **Update** (`update`) - Update an object

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Type Name | `typeName` | string |  | ✓ | Name of data type of the object to create |  |
| Properties | `properties` | fixedCollection | {} | ✗ | Field to set for the object to create | e.g. Add Property |  |

<details>
<summary><strong>Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Property | `property` |  |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Type Name | `typeName` | string |  | ✓ | Name of data type of the object to retrieve |  |
| Object ID | `objectId` | string |  | ✓ | ID of the object to retrieve |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Type Name | `typeName` | string |  | ✓ | Name of data type of the object to retrieve |  |
| Object ID | `objectId` | string |  | ✓ | ID of the object to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Type Name | `typeName` | string |  | ✓ | Name of data type of the object to create |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | Field to set for the object to create | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filters | `filters` | fixedCollection | {} | Field to set for the object to create |
| Filters (JSON) | `filtersJson` | json |  | Refine the list that is returned by the Data API with search constraints, exactly as you define a search in Bubble. See <a href="https://manual.bubble.io/core-resources/api/data-api#search-constraints">link</a>. |
| Sort | `sort` | fixedCollection | {} | Specify the field to use for sorting. Either use a fielddefined for the current typeor use <code>_random_sorting</code> to get the entries in a random order. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Type Name | `typeName` | string |  | ✓ | Name of data type of the object to update |  |
| Object ID | `objectId` | string |  | ✓ | ID of the object to update |  |
| Properties | `properties` | fixedCollection | {} | ✗ | Field to set for the object to create | e.g. Add Property |  |

<details>
<summary><strong>Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Property | `property` |  |  |  |

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
node: bubble
displayName: Bubble
description: Consume the Bubble Data API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: bubbleApi
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: typeName
    name: Type Name
    type: string
    default: ''
    required: true
    description: Name of data type of the object to create
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - object
          operation:
          - getAll
    typeInfo: &id002
      type: string
      displayName: Type Name
      name: typeName
  - id: properties
    name: Properties
    type: fixedCollection
    default: {}
    required: false
    description: Field to set for the object to create
    placeholder: Add Property
    validation: &id005
      displayOptions:
        show:
          resource:
          - object
          operation:
          - update
    typeInfo: &id006
      type: fixedCollection
      displayName: Properties
      name: properties
      typeOptions:
        multipleValues: true
      subProperties:
      - name: property
        displayName: Property
        values:
        - displayName: Key
          name: key
          type: string
          description: Field to set for the object to create
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value to set for the object to create
          default: ''
- id: delete
  name: Delete
  description: ''
  params:
  - id: typeName
    name: Type Name
    type: string
    default: ''
    required: true
    description: Name of data type of the object to retrieve
    validation: *id001
    typeInfo: *id002
  - id: objectId
    name: Object ID
    type: string
    default: ''
    required: true
    description: ID of the object to retrieve
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - object
          operation:
          - update
    typeInfo: &id004
      type: string
      displayName: Object ID
      name: objectId
- id: get
  name: Get
  description: ''
  params:
  - id: typeName
    name: Type Name
    type: string
    default: ''
    required: true
    description: Name of data type of the object to retrieve
    validation: *id001
    typeInfo: *id002
  - id: objectId
    name: Object ID
    type: string
    default: ''
    required: true
    description: ID of the object to retrieve
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: typeName
    name: Type Name
    type: string
    default: ''
    required: true
    description: Name of data type of the object to create
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
          - object
          operation:
          - getAll
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
          resource:
          - object
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
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - object
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
- id: update
  name: Update
  description: ''
  params:
  - id: typeName
    name: Type Name
    type: string
    default: ''
    required: true
    description: Name of data type of the object to update
    validation: *id001
    typeInfo: *id002
  - id: objectId
    name: Object ID
    type: string
    default: ''
    required: true
    description: ID of the object to update
    validation: *id003
    typeInfo: *id004
  - id: properties
    name: Properties
    type: fixedCollection
    default: {}
    required: false
    description: Field to set for the object to create
    placeholder: Add Property
    validation: *id005
    typeInfo: *id006
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - user-agent
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: properties
    text: Add Property
  - field: properties
    text: Add Property
  - field: options
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
  "$id": "https://n8n.io/schemas/nodes/bubble.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Bubble Node",
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
            "object"
          ],
          "default": "object"
        },
        "operation": {
          "description": "",
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
        "typeName": {
          "description": "Name of data type of the object to create",
          "type": "string",
          "default": ""
        },
        "properties": {
          "description": "Field to set for the object to create",
          "type": "string",
          "default": {},
          "examples": [
            "Add Property"
          ]
        },
        "objectId": {
          "description": "ID of the object to update",
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
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "options": {
          "description": "Field to set for the object to create",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
      "name": "bubbleApi",
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
