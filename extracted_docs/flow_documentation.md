---
title: "Node: Flow"
slug: "node-flow"
version: "1"
updated: "2026-01-08"
summary: "Consume Flow API"
node_type: "regular"
group: "['output']"
---

# Node: Flow

**Purpose.** Consume Flow API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:flow.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **flowApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `flowApi` | ✓ | - |

---

## Operations

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new task |
| Update | `update` | Update a task |
| Get | `get` | Get a task |
| Get Many | `getAll` | Get many tasks |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | task | ✗ | Tasks are units of work that can be private or assigned to a list. Through this endpoint, you can manipulate your tasks in Flow, including creating new ones. |  |

**Resource options:**

* **Task** (`task`) - Tasks are units of work that can be private or assigned to a list. Through this endpoint, you can manipulate your tasks in Flow, including creating new ones.

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a new task |  |

**Operation options:**

* **Create** (`create`) - Create a new task
* **Update** (`update`) - Update a task
* **Get** (`get`) - Get a task
* **Get Many** (`getAll`) - Get many tasks

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workspace ID | `workspaceId` | string |  | ✓ | Create resources under the given workspace |  |
| Name | `name` | string |  | ✓ | The title of the task |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The ID of the account to whom this task will be assigned | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Owner ID | `ownerid` | string |  | The ID of the account to whom this task will be assigned |
| List ID | `listID` | string |  | Put the new task in a list ("project"). Omit this param to have the task be private. |
| Starts On | `startsOn` | dateTime |  | The date on which the task should start |
| Due On | `dueOn` | dateTime |  | The date on which the task should be due |
| Mirror Parent Subscribers | `mirrorParentSubscribers` | boolean | False | Whether this task will be a subtask, and this is true, the parent tasks's subscribers will be mirrored to this one |
| Mirror Parent Tags | `mirrorParentTags` | boolean | False | Whether this task will be a subtask, and this is true, the parent tasks's tags will be mirrored to this one |
| Note Content | `noteContent` | string |  | Provide the content for the task's note |
| Note Mime Type | `noteMimeType` | options | text/plain | Identify which markup language is used to format the given note |
| Parent ID | `parentId` | string |  | If provided, this task will become a subtask of the given task |
| Position List | `positionList` | number | 0 | Determines the sort order when showing tasks in, or grouped by, a list |
| Position Upcoming | `positionUpcoming` | number | 0 | Determines the sort order when showing tasks grouped by their due_date |
| Position | `position` | number | 0 | Determines the sort order of tasks |
| Section ID | `sectionId` | string |  | Specify which section under which to create this task |
| Tags | `tags` | string |  | A list of tag names to apply to the new task separated by a comma (,) |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workspace ID | `workspaceId` | string |  | ✓ | Create resources under the given workspace |  |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The title of the task | e.g. Add Update Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | The title of the task |
| Completed | `completed` | boolean | False | Whether to complete the task |
| Owner ID | `ownerid` | string |  | The ID of the account to whom this task will be assigned |
| List ID | `listID` | string |  | Put the new task in a list ("project"). Omit this param to have the task be private. |
| Starts On | `startsOn` | dateTime |  | The date on which the task should start |
| Due On | `dueOn` | dateTime |  | The date on which the task should be due |
| Mirror Parent Subscribers | `mirrorParentSubscribers` | boolean | False | Whether this task will be a subtask, and this is true, the parent tasks's subscribers will be mirrored to this one |
| Mirror Parent Tags | `mirrorParentTags` | boolean | False | Whether this task will be a subtask, and this is true, the parent tasks's tags will be mirrored to this one |
| Note Content | `noteContent` | string |  | Provide the content for the task's note |
| Note Mime Type | `noteMimeType` | options | text/plain | Identify which markup language is used to format the given note |
| Parent ID | `parentId` | string |  | If provided, this task will become a subtask of the given task |
| Position List | `positionList` | number | 0 | Determines the sort order when showing tasks in, or grouped by, a list |
| Position Upcoming | `positionUpcoming` | number | 0 | Determines the sort order when showing tasks grouped by their due_date |
| Position | `position` | number | 0 | Determines the sort order of tasks |
| Section ID | `sectionId` | string |  | Specify which section under which to create this task |
| Tags | `tags` | string |  | A list of tag names to apply to the new task separated by a comma (,) |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | multiOptions | [] |  |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Create resources under the given workspace | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | multiOptions | [] |  |
| Order | `order` | options | created_at |  |
| Workspace ID | `workspaceId` | string |  | Create resources under the given workspace |
| Created Before | `createdBefore` | dateTime |  | Select resources created before a certain time |
| Created After | `createdAfter` | dateTime |  | Select resources created after a certain time |
| Update Before | `updateBefore` | dateTime |  | Select resources updated before a certain time |
| Update After | `updateAfter` | dateTime |  | Select resources updated after a certain time |
| Deleted | `deleted` | boolean | False | Whether to select deleted resources |
| Cleared | `cleared` | boolean | False | Whether to select cleared resources |

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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: flow
displayName: Flow
description: Consume Flow API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: flowApi
  required: true
operations:
- id: create
  name: Create
  description: Create a new task
  params:
  - id: workspaceId
    name: Workspace ID
    type: string
    default: ''
    required: true
    description: Create resources under the given workspace
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: Workspace ID
      name: workspaceId
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The title of the task
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
- id: update
  name: Update
  description: Update a task
  params:
  - id: workspaceId
    name: Workspace ID
    type: string
    default: ''
    required: true
    description: Create resources under the given workspace
    validation: *id001
    typeInfo: *id002
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - get
    typeInfo: &id004
      type: string
      displayName: Task ID
      name: taskId
- id: get
  name: Get
  description: Get a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: Get many tasks
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
          resource:
          - task
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
          - task
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
common_expressions:
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
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Update Field
  - field: filters
    text: Add Filter
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/flow.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Flow Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "update",
        "get",
        "getAll"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Tasks are units of work that can be private or assigned to a list. Through this endpoint, you can manipulate your tasks in Flow, including creating new ones.",
          "type": "string",
          "enum": [
            "task"
          ],
          "default": "task"
        },
        "operation": {
          "description": "Create a new task",
          "type": "string",
          "enum": [
            "create",
            "update",
            "get",
            "getAll"
          ],
          "default": "create"
        },
        "workspaceId": {
          "description": "Create resources under the given workspace",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "The title of the task",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The ID of the account to whom this task will be assigned",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "taskId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "The title of the task",
          "type": "string",
          "default": {},
          "examples": [
            "Add Update Field"
          ]
        },
        "filters": {
          "description": "Create resources under the given workspace",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
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
      "name": "flowApi",
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
