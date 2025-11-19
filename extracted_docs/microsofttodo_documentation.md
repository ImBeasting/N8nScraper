---
title: "Node: Microsoft To Do"
slug: "node-microsofttodo"
version: "1"
updated: "2025-11-13"
summary: "Consume Microsoft To Do API."
node_type: "regular"
group: "['input']"
---

# Node: Microsoft To Do

**Purpose.** Consume Microsoft To Do API.
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:todo.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftToDoOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `microsoftToDoOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Linkedresource Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a linked resource |
| Delete | `delete` | Delete a linked resource |
| Get | `get` | Get a linked resource |
| Get Many | `getAll` | Get many linked resources |
| Update | `update` | Update a linked resource |

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a task |
| Delete | `delete` | Delete a task |
| Get | `get` | Get a task |
| Get Many | `getAll` | Get many tasks |
| Update | `update` | Update a task |

### List Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a list |
| Delete | `delete` | Delete a list |
| Get | `get` | Get a list |
| Get Many | `getAll` | Get many lists |
| Update | `update` | Update a list |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | task | ✗ | Resource to operate on |  |

**Resource options:**

* **Linked Resource** (`linkedResource`)
* **List** (`list`)
* **Task** (`task`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create a linked resource
* **Delete** (`delete`) - Delete a linked resource
* **Get** (`get`) - Get a linked resource
* **Get Many** (`getAll`) - Get many linked resources
* **Update** (`update`) - Update a linked resource

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task List Name or ID | `taskListId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Name | `displayName` | string |  | ✗ | Field indicating title of the linked entity |  |
| Application Name | `applicationName` | string |  | ✓ | App name of the source that is sending the linked entity |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the object that is associated with this task on the third-party/partner system | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| External ID | `externalId` | string |  | ID of the object that is associated with this task on the third-party/partner system |
| Web URL | `webUrl` | string |  | Deeplink to the linked entity |

</details>

| List Name or ID | `taskListId` | options |  | ✓ | The identifier of the list, unique in the user's mailbox. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Subject | `title` | string |  | ✓ | A brief description of the task |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The content of the task | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content | `content` | string |  | The content of the task |
| Due | `dueDateTime` | dateTime |  | The date in the specified time zone that the task is to be finished |
| Reminder | `reminderDateTime` | dateTime |  | The date in the specified time zone that the task is to be reminded |
| Importance | `importance` | options | normal | The importance of the task |
| Status | `status` | options | notStarted | Indicates the state or progress of the task |

</details>

| List Name | `displayName` | string |  | ✓ | List display name |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task List Name or ID | `taskListId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Linked Resource ID | `linkedResourceId` | string |  | ✓ |  |  |
| List Name or ID | `taskListId` | options |  | ✓ | The identifier of the list, unique in the user's mailbox. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Task ID | `taskId` | string |  | ✓ |  |  |
| List ID | `listId` | string |  | ✓ | The identifier of the list, unique in the user's mailbox |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task List Name or ID | `taskListId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Linked Resource ID | `linkedResourceId` | string |  | ✓ |  |  |
| List Name or ID | `taskListId` | options |  | ✓ | The identifier of the list, unique in the user's mailbox. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Task ID | `taskId` | string |  | ✓ |  |  |
| List ID | `listId` | string |  | ✓ | The identifier of the list, unique in the user's mailbox |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task List Name or ID | `taskListId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| List Name or ID | `taskListId` | options |  | ✓ | The identifier of the list, unique in the user's mailbox. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task List Name or ID | `taskListId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Linked Resource ID | `linkedResourceId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | App name of the source that is sending the linked entity | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Application Name | `applicationName` | string |  | App name of the source that is sending the linked entity |
| Name | `displayName` | string |  | Field indicating title of the linked entity |
| External ID | `externalId` | string |  | ID of the object that is associated with this task on the third-party/partner system |
| Web URL | `webUrl` | string |  | Deeplink to the linked entity |

</details>

| List Name or ID | `taskListId` | options |  | ✓ | The identifier of the list, unique in the user's mailbox. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The content of the task | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content | `content` | string |  | The content of the task |
| Due Date Time | `dueDateTime` | dateTime |  | The date in the specified time zone that the task is to be finished |
| Reminder | `reminderDateTime` | dateTime |  | The date in the specified time zone that the task is to be reminded |
| Importance | `importance` | options | normal | The importance of the task |
| Status | `status` | options | notStarted | Indicates the state or progress of the task |
| Subject | `title` | string |  | A brief description of the task |

</details>

| List ID | `listId` | string |  | ✓ | The identifier of the list, unique in the user's mailbox |  |
| New List Name | `displayName` | string |  | ✓ | List display name |  |

---

## Load Options Methods

- `getTaskLists`
- `for`
- `name`
- `value`

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
node: microsoftToDo
displayName: Microsoft To Do
description: Consume Microsoft To Do API.
version: '1'
nodeType: regular
group:
- input
credentials:
- name: microsoftToDoOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: taskListId
    name: Task List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - delete
          - get
          - getAll
          - update
          resource:
          - task
    typeInfo: &id002
      type: options
      displayName: List Name or ID
      name: taskListId
      typeOptions:
        loadOptionsMethod: getTaskLists
      possibleValues: []
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - delete
          - get
          - update
          resource:
          - task
    typeInfo: &id006
      type: string
      displayName: Task ID
      name: taskId
  - id: displayName
    name: Name
    type: string
    default: ''
    required: false
    description: Field indicating title of the linked entity
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - list
    typeInfo: &id004
      type: string
      displayName: New List Name
      name: displayName
  - id: applicationName
    name: Application Name
    type: string
    default: ''
    required: true
    description: App name of the source that is sending the linked entity
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - linkedResource
    typeInfo:
      type: string
      displayName: Application Name
      name: applicationName
  - id: taskListId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The identifier of the list, unique in the user's mailbox. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: title
    name: Subject
    type: string
    default: ''
    required: true
    description: A brief description of the task
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - task
    typeInfo:
      type: string
      displayName: Subject
      name: title
  - id: displayName
    name: List Name
    type: string
    default: ''
    required: true
    description: List display name
    validation: *id003
    typeInfo: *id004
- id: delete
  name: Delete
  description: ''
  params:
  - id: taskListId
    name: Task List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: linkedResourceId
    name: Linked Resource ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - linkedResource
          operation:
          - delete
          - get
          - update
    typeInfo: &id008
      type: string
      displayName: Linked Resource ID
      name: linkedResourceId
  - id: taskListId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The identifier of the list, unique in the user's mailbox. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: The identifier of the list, unique in the user's mailbox
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - delete
          - get
          - update
          resource:
          - list
    typeInfo: &id010
      type: string
      displayName: List ID
      name: listId
- id: get
  name: Get
  description: ''
  params:
  - id: taskListId
    name: Task List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: linkedResourceId
    name: Linked Resource ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: taskListId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The identifier of the list, unique in the user's mailbox. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: The identifier of the list, unique in the user's mailbox
    validation: *id009
    typeInfo: *id010
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: taskListId
    name: Task List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id011
      displayOptions:
        show:
          resource:
          - list
          operation:
          - getAll
    typeInfo: &id012
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id013
      displayOptions:
        show:
          resource:
          - list
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id014
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: taskListId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The identifier of the list, unique in the user's mailbox. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
- id: update
  name: Update
  description: ''
  params:
  - id: taskListId
    name: Task List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: linkedResourceId
    name: Linked Resource ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: taskListId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The identifier of the list, unique in the user's mailbox. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: The identifier of the list, unique in the user's mailbox
    validation: *id009
    typeInfo: *id010
  - id: displayName
    name: New List Name
    type: string
    default: ''
    required: true
    description: List display name
    validation: *id003
    typeInfo: *id004
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
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
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/microsoftToDo.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft To Do Node",
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
            "linkedResource",
            "list",
            "task"
          ],
          "default": "task"
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
        "taskListId": {
          "description": "The identifier of the list, unique in the user's mailbox. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "taskId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "displayName": {
          "description": "List display name",
          "type": "string",
          "default": ""
        },
        "applicationName": {
          "description": "App name of the source that is sending the linked entity",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The content of the task",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "linkedResourceId": {
          "description": "",
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
        "updateFields": {
          "description": "The content of the task",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "title": {
          "description": "A brief description of the task",
          "type": "string",
          "default": ""
        },
        "listId": {
          "description": "The identifier of the list, unique in the user's mailbox",
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
      "name": "microsoftToDoOAuth2Api",
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
