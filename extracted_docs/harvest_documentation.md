---
title: "Node: Harvest"
slug: "node-harvest"
version: "1"
updated: "2026-01-08"
summary: "Access data on Harvest"
node_type: "regular"
group: "['input']"
---

# Node: Harvest

**Purpose.** Access data on Harvest
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:harvest.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **harvestApi**: N/A
- **harvestOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `harvestApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `harvestOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** accountId, Harvest-Account-Id

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a client |
| Delete | `delete` | Delete a client |
| Get | `get` | Get data of a client |
| Get Many | `getAll` | Get data of many clients |
| Update | `update` | Update a client |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | task | ✗ | Resource to operate on |  |

**Resource options:**

* **Client** (`client`)
* **Company** (`company`)
* **Contact** (`contact`)
* **Estimate** (`estimate`)
* **Expense** (`expense`)
* **Invoice** (`invoice`)
* **Project** (`project`)
* **Task** (`task`)
* **Time Entry** (`timeEntry`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Create a client |  |

**Operation options:**

* **Create** (`create`) - Create a client
* **Delete** (`delete`) - Delete a client
* **Get** (`get`) - Get data of a client
* **Get Many** (`getAll`) - Get data of many clients
* **Update** (`update`) - Update a client

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | The name of the client |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | A textual representation of the client’s physical address. May include new line characters. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  | A textual representation of the client’s physical address. May include new line characters. |
| Currency | `currency` | string |  | The currency used by the estimate. If not provided, the client’s currency will be used. See a list of supported currencies |
| Is Active | `is_active` | string |  | Whether the client is active, or archived. Defaults to true. |

</details>

| First Name | `firstName` | string |  | ✓ | The first name of the contact |  |
| Client ID | `clientId` | string |  | ✓ | The ID of the client associated with this contact |  |
| Project ID | `projectId` | string |  | ✓ | The ID of the project associated with this expense |  |
| Expense Category ID | `expenseCategoryId` | string |  | ✓ | The ID of the expense category this expense is being tracked against |  |
| Spent Date | `spentDate` | dateTime |  | ✓ | Date the expense occurred |  |
| Is Billable | `isBillable` | boolean | True | ✓ | Whether the project is billable or not |  |
| Bill By | `billBy` | options | none | ✓ | The method by which the project is invoiced |  |

**Bill By options:**

* **None** (`none`)
* **People** (`People`)
* **Project** (`Project`)
* **Tasks** (`Tasks`)

| Budget By | `budgetBy` | string | none | ✓ | The email of the user or "none" |  |
| Last Name | `lastName` | string |  | ✓ | The last name of the user |  |
| Email | `email` | string |  | ✓ | The email of the user | e.g. name@email.com | email |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Client ID | `id` | string |  | ✓ | The ID of the client you want to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Client ID | `id` | string |  | ✓ | The ID of the client you are retrieving |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Whether to only return active clients and false to return inactive clients | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Is Active | `is_active` | boolean | True | Whether to only return active clients and false to return inactive clients |
| Updated Since | `updated_since` | dateTime |  | Only return clients that have been updated since the given date and time |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Client ID | `id` | string |  | ✓ | The ID of the client want to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | A textual representation of the client’s physical address. May include new line characters. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  | A textual representation of the client’s physical address. May include new line characters. |
| Currency | `currency` | string |  | The currency used by the estimate. If not provided, the client’s currency will be used. See a list of supported currencies |
| Is Active | `is_active` | boolean | True | Whether the client is active, or archived. Defaults to true. |
| Name | `name` | string |  | Whether the client is active, or archived. Defaults to true. |

</details>


---

## Load Options Methods

- `getAccounts`

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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: harvest
displayName: Harvest
description: Access data on Harvest
version: '1'
nodeType: regular
group:
- input
credentials:
- name: harvestApi
  required: true
- name: harvestOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a client
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the client
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: firstName
    name: First Name
    type: string
    default: ''
    required: true
    description: The first name of the contact
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
    typeInfo:
      type: string
      displayName: First Name
      name: firstName
  - id: clientId
    name: Client ID
    type: string
    default: ''
    required: true
    description: The ID of the client associated with this contact
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
    typeInfo:
      type: string
      displayName: Client ID
      name: clientId
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: The ID of the project associated with this expense
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - createByStartEnd
    typeInfo:
      type: string
      displayName: Project ID
      name: projectId
  - id: expenseCategoryId
    name: Expense Category ID
    type: string
    default: ''
    required: true
    description: The ID of the expense category this expense is being tracked against
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
    typeInfo:
      type: string
      displayName: Expense Category ID
      name: expenseCategoryId
  - id: spentDate
    name: Spent Date
    type: dateTime
    default: ''
    required: true
    description: Date the expense occurred
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - createByStartEnd
    typeInfo:
      type: dateTime
      displayName: Spent Date
      name: spentDate
  - id: isBillable
    name: Is Billable
    type: boolean
    default: true
    required: true
    description: Whether the project is billable or not
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
    typeInfo:
      type: boolean
      displayName: Is Billable
      name: isBillable
  - id: billBy
    name: Bill By
    type: options
    default: none
    required: true
    description: The method by which the project is invoiced
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
    typeInfo:
      type: options
      displayName: Bill By
      name: billBy
      possibleValues:
      - value: none
        name: None
        description: ''
      - value: People
        name: People
        description: ''
      - value: Project
        name: Project
        description: ''
      - value: Tasks
        name: Tasks
        description: ''
  - id: budgetBy
    name: Budget By
    type: string
    default: none
    required: true
    description: The email of the user or "none"
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
    typeInfo:
      type: string
      displayName: Budget By
      name: budgetBy
  - id: lastName
    name: Last Name
    type: string
    default: ''
    required: true
    description: The last name of the user
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
    typeInfo:
      type: string
      displayName: Last Name
      name: lastName
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email of the user
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - create
    typeInfo:
      type: string
      displayName: Email
      name: email
- id: delete
  name: Delete
  description: Delete a client
  params:
  - id: id
    name: Client ID
    type: string
    default: ''
    required: true
    description: The ID of the client you want to delete
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - restartTime
    typeInfo: &id002
      type: string
      displayName: Time Entry ID
      name: id
- id: get
  name: Get
  description: Get data of a client
  params:
  - id: id
    name: Client ID
    type: string
    default: ''
    required: true
    description: The ID of the client you are retrieving
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get data of many clients
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
  description: Update a client
  params:
  - id: id
    name: Client ID
    type: string
    default: ''
    required: true
    description: The ID of the client want to update
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - accountId
  - Harvest-Account-Id
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: filters
    text: Add Filter
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
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
  "$id": "https://n8n.io/schemas/nodes/harvest.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Harvest Node",
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
            "accessToken",
            "oAuth2"
          ],
          "default": "accessToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "client",
            "company",
            "contact",
            "estimate",
            "expense",
            "invoice",
            "project",
            "task",
            "timeEntry",
            "user"
          ],
          "default": "task"
        },
        "accountId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "operation": {
          "description": "Create a client",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "getAll"
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
        "filters": {
          "description": "Whether to only return active clients and false to return inactive clients",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "id": {
          "description": "Restart a stopped time entry. Restarting a time entry is only possible if it isn\u2019t currently running.",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "The name of the client",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The time the entry ended",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "A textual representation of the client\u2019s physical address. May include new line characters.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "firstName": {
          "description": "The first name of the contact",
          "type": "string",
          "default": ""
        },
        "clientId": {
          "description": "The ID of the client associated with this contact",
          "type": "string",
          "default": ""
        },
        "projectId": {
          "description": "The ID of the project to associate with the time entry",
          "type": "string",
          "default": ""
        },
        "expenseCategoryId": {
          "description": "The ID of the expense category this expense is being tracked against",
          "type": "string",
          "default": ""
        },
        "spentDate": {
          "description": "The ISO 8601 formatted date the time entry was spent",
          "type": "string",
          "default": ""
        },
        "isBillable": {
          "description": "Whether the project is billable or not",
          "type": "boolean",
          "default": true
        },
        "billBy": {
          "description": "The method by which the project is invoiced",
          "type": "string",
          "enum": [
            "none",
            "People",
            "Project",
            "Tasks"
          ],
          "default": "none"
        },
        "budgetBy": {
          "description": "The email of the user or \"none\"",
          "type": "string",
          "default": "none"
        },
        "taskId": {
          "description": "The ID of the task to associate with the time entry",
          "type": "string",
          "default": ""
        },
        "lastName": {
          "description": "The last name of the user",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "The email of the user",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
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
      "name": "harvestApi",
      "required": true
    },
    {
      "name": "harvestOAuth2Api",
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
