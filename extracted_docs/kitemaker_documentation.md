---
title: "Node: Kitemaker"
slug: "node-kitemaker"
version: "1"
updated: "2025-11-19"
summary: "Consume the Kitemaker GraphQL API"
node_type: "regular"
group: "['input']"
---

# Node: Kitemaker

**Purpose.** Consume the Kitemaker GraphQL API
**Subtitle.** ={{$parameter["resource"] + ": " + $parameter["operation"]}}


---

## Node Details

- **Icon:** `{'light': 'file:kitemaker.svg', 'dark': 'file:kitemaker.dark.svg'}`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **kitemakerApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `kitemakerApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

---

## Operations

### Workitem Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a work item |
| Get | `get` | Get a work item |
| Get Many | `getAll` | Get many work items |
| Update | `update` | Update a work item |

### Organization Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve data on the logged-in user's organization |

### Space Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Retrieve data on many spaces in the logged-in user's organization |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Retrieve data on many users in the logged-in user's organization |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | workItem | ✓ | Resource to operate on |  |

**Resource options:**

* **Organization** (`organization`)
* **Space** (`space`)
* **User** (`user`)
* **Work Item** (`workItem`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create a work item
* **Get** (`get`) - Get a work item
* **Get Many** (`getAll`) - Get many work items
* **Update** (`update`) - Update a work item

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ | Title of the work item to create |  |
| Space Name or ID | `spaceId` | options | [] | ✓ | ID of the space to retrieve the work items from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Status Name or ID | `statusId` | options | [] | ✓ | ID of the status to set on the item to create. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Description of the item to create. Markdown supported. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Description of the item to create. Markdown supported. |
| Effort | `effort` | options | SMALL | Effort to set for the item to create |
| Impact | `impact` | options | SMALL | Impact to set for the item to create |
| Label Names or IDs | `labelIds` | multiOptions | [] | ID of the label to set on the item to create. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Member Names or IDs | `memberIds` | multiOptions | [] | ID of the user to assign to the item to create. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Work Item ID | `workItemId` | string |  | ✓ | ID of the work item to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Space Name or ID | `spaceId` | options | [] | ✓ | ID of the space to retrieve the work items from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Work Item ID | `workItemId` | string |  | ✓ | ID of the work item to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Description of the item to update. Markdown supported. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Description of the item to update. Markdown supported. |
| Effort | `effort` | options | SMALL | Effort to set for the item to update |
| Impact | `impact` | options | SMALL | Impact to set for the item to update |
| Status Name or ID | `statusId` | options | [] | ID of the status to set on the item to update. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Title | `title` | string |  | Title to set for the work item to update |

</details>


---

## Load Options Methods

- `getLabels`

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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: kitemaker
displayName: Kitemaker
description: Consume the Kitemaker GraphQL API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: kitemakerApi
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the work item to create
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - workItem
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: spaceId
    name: Space Name or ID
    type: options
    default: []
    required: true
    description: ID of the space to retrieve the work items from. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - workItem
          operation:
          - getAll
    typeInfo: &id002
      type: options
      displayName: Space Name or ID
      name: spaceId
      typeOptions:
        loadOptionsMethod: getSpaces
      possibleValues: []
  - id: statusId
    name: Status Name or ID
    type: options
    default: []
    required: true
    description: ID of the status to set on the item to create. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - workItem
          operation:
          - create
    typeInfo:
      type: options
      displayName: Status Name or ID
      name: statusId
      typeOptions:
        loadOptionsMethod: getStatuses
      possibleValues: []
- id: get
  name: Get
  description: ''
  params:
  - id: workItemId
    name: Work Item ID
    type: string
    default: ''
    required: true
    description: ID of the work item to retrieve
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - workItem
          operation:
          - update
    typeInfo: &id008
      type: string
      displayName: Work Item ID
      name: workItemId
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: spaceId
    name: Space Name or ID
    type: options
    default: []
    required: true
    description: ID of the space to retrieve the work items from. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id003
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 1000
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: update
  name: Update
  description: ''
  params:
  - id: workItemId
    name: Work Item ID
    type: string
    default: ''
    required: true
    description: ID of the work item to update
    validation: *id007
    typeInfo: *id008
common_expressions:
- '={{$parameter["resource"] + ": " + $parameter["operation"]}}'
api_patterns:
  http_methods:
  - POST
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: updateFields
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
  "$id": "https://n8n.io/schemas/nodes/kitemaker.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Kitemaker Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
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
            "organization",
            "space",
            "user",
            "workItem"
          ],
          "default": "workItem"
        },
        "operation": {
          "description": "Retrieve data on many users in the logged-in user's organization",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "getAll"
        },
        "title": {
          "description": "Title of the work item to create",
          "type": "string",
          "default": ""
        },
        "spaceId": {
          "description": "ID of the space to retrieve the work items from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "statusId": {
          "description": "ID of the status to set on the item to create. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "additionalFields": {
          "description": "Description of the item to create. Markdown supported.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "workItemId": {
          "description": "ID of the work item to update",
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
          "default": 5
        },
        "updateFields": {
          "description": "Description of the item to update. Markdown supported.",
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
      "name": "kitemakerApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-19 | Ultimate extraction with maximum detail for AI training |
