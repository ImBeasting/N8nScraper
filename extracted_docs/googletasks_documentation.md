---
title: "Node: Google Tasks"
slug: "node-googletasks"
version: "1"
updated: "2026-01-08"
summary: "Consume Google Tasks API"
node_type: "regular"
group: "['input']"
---

# Node: Google Tasks

**Purpose.** Consume Google Tasks API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:googleTasks.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleTasksOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleTasksOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Add a task to tasklist |
| Delete | `delete` | Delete a task |
| Get | `get` | Retrieve a task |
| Get Many | `getAll` | Retrieve many tasks from a tasklist |
| Update | `update` | Update a task |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | task | ✗ | Resource to operate on |  |

**Resource options:**

* **Task** (`task`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Add a task to tasklist |  |

**Operation options:**

* **Create** (`create`) - Add a task to tasklist
* **Delete** (`delete`) - Delete a task
* **Get** (`get`) - Retrieve a task
* **Get Many** (`getAll`) - Retrieve many tasks from a tasklist
* **Update** (`update`) - Update a task

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| TaskList Name or ID | `task` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Title | `title` | string |  | ✗ | Title of the task |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Completion date of the task (as a RFC 3339 timestamp). This field is omitted if the task has not been completed. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Completion Date | `completed` | dateTime |  | Completion date of the task (as a RFC 3339 timestamp). This field is omitted if the task has not been completed. |
| Deleted | `deleted` | boolean | False | Whether the task has been deleted |
| Due Date | `dueDate` | dateTime |  | Due date of the task |
| Notes | `notes` | string |  | Additional Notes |
| Parent | `parent` | string |  | Parent task identifier. If the task is created at the top level, this parameter is omitted. |
| Previous | `previous` | string |  | Previous sibling task identifier. If the task is created at the first position among its siblings, this parameter is omitted. |
| Status | `status` | options |  | Current status of the task |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| TaskList Name or ID | `task` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Task ID | `taskId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| TaskList Name or ID | `task` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Task ID | `taskId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| TaskList Name or ID | `task` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:100 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Upper bound for a task completion date (as a RFC 3339 timestamp) to filter by | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Completed Max | `completedMax` | dateTime |  | Upper bound for a task completion date (as a RFC 3339 timestamp) to filter by |
| Completed Min | `completedMin` | dateTime |  | Lower bound for a task completion date (as a RFC 3339 timestamp) to filter by |
| Due Min | `dueMin` | dateTime |  | Lower bound for a task due date (as a RFC 3339 timestamp) to filter by |
| Due Max | `dueMax` | dateTime |  | Upper bound for a task due date (as a RFC 3339 timestamp) to filter by |
| Show Completed | `showCompleted` | boolean | True | Whether completed tasks are returned in the result. <strong>Show Hidden</strong> must also be True to show tasks completed in first party clients such as the web UI or Google's mobile apps. |
| Show Deleted | `showDeleted` | boolean | False | Whether deleted tasks are returned in the result |
| Show Hidden | `showHidden` | boolean | False | Whether hidden tasks are returned in the result |
| Updated Min | `updatedMin` | dateTime |  | Lower bound for a task last modification time (as a RFC 3339 timestamp) to filter by |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| TaskList Name or ID | `task` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Completion date of the task (as a RFC 3339 timestamp). This field is omitted if the task has not been completed. | e.g. Update Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Completion Date | `completed` | dateTime |  | Completion date of the task (as a RFC 3339 timestamp). This field is omitted if the task has not been completed. |
| Deleted | `deleted` | boolean | False | Whether the task has been deleted |
| Due Date | `dueDate` | dateTime |  | Due date of the task |
| Notes | `notes` | string |  | Additional Notes |
| Previous | `previous` | string |  | Previous sibling task identifier. If the task is created at the first position among its siblings, this parameter is omitted. |
| Status | `status` | options |  | Current status of the task |
| Title | `title` | string |  | Title of the task |

</details>


---

## Load Options Methods

- `getTasks`
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
node: googleTasks
displayName: Google Tasks
description: Consume Google Tasks API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: googleTasksOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Add a task to tasklist
  params:
  - id: task
    name: TaskList Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - task
    typeInfo: &id002
      type: options
      displayName: TaskList Name or ID
      name: task
      typeOptions:
        loadOptionsMethod: getTasks
      possibleValues: []
  - id: title
    name: Title
    type: string
    default: ''
    required: false
    description: Title of the task
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - task
    typeInfo:
      type: string
      displayName: Title
      name: title
- id: delete
  name: Delete
  description: Delete a task
  params:
  - id: task
    name: TaskList Name or ID
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
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - task
    typeInfo: &id004
      type: string
      displayName: Task ID
      name: taskId
- id: get
  name: Get
  description: Retrieve a task
  params:
  - id: task
    name: TaskList Name or ID
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
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: Retrieve many tasks from a tasklist
  params:
  - id: task
    name: TaskList Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
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
          operation:
          - getAll
          resource:
          - task
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 20
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - task
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
  description: Update a task
  params:
  - id: task
    name: TaskList Name or ID
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
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Update Field
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
  "$id": "https://n8n.io/schemas/nodes/googleTasks.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Tasks Node",
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
            "task"
          ],
          "default": "task"
        },
        "operation": {
          "description": "Add a task to tasklist",
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
        "task": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "Title of the task",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Upper bound for a task completion date (as a RFC 3339 timestamp) to filter by",
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
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 20
        },
        "updateFields": {
          "description": "Completion date of the task (as a RFC 3339 timestamp). This field is omitted if the task has not been completed.",
          "type": "string",
          "default": {},
          "examples": [
            "Update Field"
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
      "name": "googleTasksOAuth2Api",
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
