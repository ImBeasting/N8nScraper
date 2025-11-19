---
title: "Node: Todoist"
slug: "node-todoist"
version: "1"
updated: "2025-11-13"
summary: "Consume Todoist API"
node_type: "regular"
group: "['output']"
---

# Node: Todoist

**Purpose.** Consume Todoist API
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:todoist.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **todoistApi**: N/A
- **todoistOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `todoistApi` | ✓ | {'show': {'authentication': ['apiKey']}} |
| `todoistOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Close | `close` | Close a task |
| Create | `create` | Create a new task |
| Delete | `delete` | Delete a task |
| Get | `get` | Get a task |
| Get Many | `getAll` | Get many tasks |
| Move | `move` | Move a task |
| Reopen | `reopen` | Reopen a task |
| Sync | `sync` | Sync a project |
| Update | `update` | Update a task |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | task | ✓ | Task resource |  |

**Resource options:**

* **Task** (`task`) - Task resource

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✓ | Close a task |  |

**Operation options:**

* **Close** (`close`) - Close a task
* **Create** (`create`) - Create a new task
* **Delete** (`delete`) - Delete a task
* **Get** (`get`) - Get a task
* **Get Many** (`getAll`) - Get many tasks
* **Move** (`move`) - Move a task
* **Reopen** (`reopen`) - Reopen a task
* **Sync** (`sync`) - Sync a project
* **Update** (`update`) - Update a task

---

### Close parameters (`close`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `project` | resourceLocator |  | ✓ | The project you want to operate on. Choose from the list, or specify an ID. | e.g. Select a project... |  |
| Label Names or IDs | `labels` | multiOptions | [] | ✗ | Optional labels that will be assigned to a created task. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Content | `content` | string |  | ✓ | Task content |  |
| Additional Fields | `options` | collection | {} | ✗ | A description for the task | e.g. Add option |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | A description for the task |
| Due Date Time | `dueDateTime` | dateTime |  | Specific date and time in RFC3339 format in UTC |
| Due String Locale | `dueLang` | string |  | 2-letter code specifying language in case due_string is not written in English |
| Due String | `dueString` | string |  | Human defined task due date (ex.: “next Monday”, “Tomorrow”). Value is set using local (not UTC) time. |
| Parent Name or ID | `parentId` | options | {} | The parent task you want to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Priority | `priority` | number | 1 | Task priority from 1 (normal) to 4 (urgent) |
| Section Name or ID | `section` | options | {} | The section you want to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Filters | `filters` | collection | {} | ✗ | Filter by any <a href="https://get.todoist.help/hc/en-us/articles/205248842">supported filter.</a> | e.g. Add option |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filter | `filter` | string |  | Filter by any <a href="https://get.todoist.help/hc/en-us/articles/205248842">supported filter.</a> |
| IDs | `ids` | string |  | A list of the task IDs to retrieve, this should be a comma-separated list |
| Label Name or ID | `labelId` | options | {} | Filter tasks by label. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Lang | `lang` | string |  | IETF language tag defining what language filter is written in, if differs from default English |
| Parent Name or ID | `parentId` | options |  | Filter tasks by parent task ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Project Name or ID | `projectId` | options |  | Filter tasks by project ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Section Name or ID | `sectionId` | options |  | Filter tasks by section ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Move parameters (`move`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Project Name or ID | `project` | resourceLocator |  | ✓ | The project you want to operate on. Choose from the list, or specify an ID. | e.g. Select a project... |  |
| Section Name or ID | `section` | options |  | ✗ | Section to which you want move the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Reopen parameters (`reopen`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |

### Sync parameters (`sync`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `project` | resourceLocator |  | ✓ | The project you want to operate on. Choose from the list, or specify an ID. | e.g. Select a project... |  |
| Sync Commands | `commands` | string | [] | ✗ | Sync body | e.g. See docs for possible commands: https://developer.todoist.com/sync/v8/#sync |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Task content | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content | `content` | string |  | Task content |
| Description | `description` | string |  | A description for the task |
| Due Date Time | `dueDateTime` | dateTime |  | Specific date and time in RFC3339 format in UTC |
| Due String Locale | `dueLang` | string |  | 2-letter code specifying language in case due_string is not written in English |
| Due String | `dueString` | string |  | Human defined task due date (ex.: “next Monday”, “Tomorrow”). Value is set using local (not UTC) time. |
| Due String Locale | `dueLang` | string |  | 2-letter code specifying language in case due_string is not written in English |
| Label Names or IDs | `labels` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Priority | `priority` | number | 1 | Task priority from 1 (normal) to 4 (urgent) |

</details>


---

## Load Options Methods

- `getProjects`
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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: todoist
displayName: Todoist
description: Consume Todoist API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: todoistApi
  required: true
- name: todoistOAuth2Api
  required: true
operations:
- id: close
  name: Close
  description: Close a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - delete
          - close
          - get
          - reopen
          - update
          - move
    typeInfo: &id002
      type: string
      displayName: Task ID
      name: taskId
- id: create
  name: Create
  description: Create a new task
  params:
  - id: project
    name: Project Name or ID
    type: resourceLocator
    default: ''
    required: true
    description: The project you want to operate on. Choose from the list, or specify
      an ID.
    placeholder: Select a project...
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - create
          - move
          - sync
    typeInfo: &id004
      type: resourceLocator
      displayName: Project Name or ID
      name: project
  - id: labels
    name: Label Names or IDs
    type: multiOptions
    default: []
    required: false
    description: Optional labels that will be assigned to a created task. Choose from
      the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      displayOptions:
        show:
          resource:
          - task
          operation:
          - create
    typeInfo:
      type: multiOptions
      displayName: Label Names or IDs
      name: labels
      typeOptions:
        loadOptionsMethod: getLabels
      possibleValues: []
  - id: content
    name: Content
    type: string
    default: ''
    required: true
    description: Task content
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
      displayName: Content
      name: content
      typeOptions:
        rows: 5
- id: delete
  name: Delete
  description: Delete a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
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
    validation: *id001
    typeInfo: *id002
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
    default: 50
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
        maxValue: 500
- id: move
  name: Move
  description: Move a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: project
    name: Project Name or ID
    type: resourceLocator
    default: ''
    required: true
    description: The project you want to operate on. Choose from the list, or specify
      an ID.
    placeholder: Select a project...
    validation: *id003
    typeInfo: *id004
  - id: section
    name: Section Name or ID
    type: options
    default: ''
    required: false
    description: Section to which you want move the task. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      displayOptions:
        show:
          resource:
          - task
          operation:
          - move
    typeInfo:
      type: options
      displayName: Section Name or ID
      name: section
      typeOptions:
        loadOptionsMethod: getSections
      possibleValues: []
- id: reopen
  name: Reopen
  description: Reopen a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
- id: sync
  name: Sync
  description: Sync a project
  params:
  - id: project
    name: Project Name or ID
    type: resourceLocator
    default: ''
    required: true
    description: The project you want to operate on. Choose from the list, or specify
      an ID.
    placeholder: Select a project...
    validation: *id003
    typeInfo: *id004
  - id: commands
    name: Sync Commands
    type: string
    default: '[]'
    required: false
    description: Sync body
    hint: 'See docs for possible commands: https://developer.todoist.com/sync/v8/#sync'
    validation:
      displayOptions:
        show:
          resource:
          - task
          operation:
          - sync
    typeInfo:
      type: string
      displayName: Sync Commands
      name: commands
- id: update
  name: Update
  description: Update a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: project
    text: Select a project...
  - field: options
    text: Add option
  - field: filters
    text: Add option
  - field: updateFields
    text: Add Field
  hints:
  - field: commands
    text: 'See docs for possible commands: https://developer.todoist.com/sync/v8/#sync'
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
  "$id": "https://n8n.io/schemas/nodes/todoist.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Todoist Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "close",
        "create",
        "delete",
        "get",
        "getAll",
        "move",
        "reopen",
        "sync",
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
            "apiKey",
            "oAuth2"
          ],
          "default": "apiKey"
        },
        "resource": {
          "description": "Task resource",
          "type": "string",
          "enum": [
            "task"
          ],
          "default": "task"
        },
        "operation": {
          "description": "Close a task",
          "type": "string",
          "enum": [
            "close",
            "create",
            "delete",
            "get",
            "getAll",
            "move",
            "reopen",
            "sync",
            "update"
          ],
          "default": "create"
        },
        "taskId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "project": {
          "description": "The project you want to operate on. Choose from the list, or specify an ID.",
          "type": "string",
          "examples": [
            "Select a project..."
          ]
        },
        "section": {
          "description": "Section to which you want move the task. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "labels": {
          "description": "Optional labels that will be assigned to a created task. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "content": {
          "description": "Task content",
          "type": "string",
          "default": ""
        },
        "commands": {
          "description": "Sync body",
          "type": "string",
          "default": "[]"
        },
        "options": {
          "description": "A description for the task",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
        },
        "filters": {
          "description": "Filter by any <a href=\"https://get.todoist.help/hc/en-us/articles/205248842\">supported filter.</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "updateFields": {
          "description": "Task content",
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
      "name": "todoistApi",
      "required": true
    },
    {
      "name": "todoistOAuth2Api",
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
