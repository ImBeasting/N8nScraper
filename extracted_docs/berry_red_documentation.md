---
title: "Node: Todoist"
slug: "node-berry-red"
version: "['2', '2.1']"
updated: "2026-01-08"
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
| Quick Add | `quickAdd` | Quick add a task using natural language |
| Reopen | `reopen` | Reopen a task |
| Update | `update` | Update a task |

### Project Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Archive | `archive` | Archive a project |
| Create | `create` | Create a new project |
| Delete | `delete` | Delete a project |
| Get | `get` | Get a project |
| Get Collaborators | `getCollaborators` | Get project collaborators |
| Get Many | `getAll` | Get many projects |
| Unarchive | `unarchive` | Unarchive a project |
| Update | `update` | Update a project |

### Section Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new section |
| Delete | `delete` | Delete a section |
| Get | `get` | Get a section |
| Get Many | `getAll` | Get many sections |
| Update | `update` | Update a section |

### Comment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new comment |
| Delete | `delete` | Delete a comment |
| Get | `get` | Get a comment |
| Get Many | `getAll` | Get many comments |
| Update | `update` | Update a comment |

### Label Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new label |
| Delete | `delete` | Delete a label |
| Get | `get` | Get a label |
| Get Many | `getAll` | Get many labels |
| Update | `update` | Update a label |

### Reminder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new reminder |
| Delete | `delete` | Delete a reminder |
| Get Many | `getAll` | Get many reminders |
| Update | `update` | Update a reminder |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | task | ✓ | Task resource |  |

**Resource options:**

* **Task** (`task`) - Task resource
* **Project** (`project`) - Project resource
* **Section** (`section`) - Section resource
* **Comment** (`comment`) - Comment resource
* **Label** (`label`) - Label resource
* **Reminder** (`reminder`) - Reminder resource

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
* **Quick Add** (`quickAdd`) - Quick add a task using natural language
* **Reopen** (`reopen`) - Reopen a task
* **Update** (`update`) - Update a task

---

### Close parameters (`close`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `project` | resourceLocator |  | ✓ | The destination project. Choose from the list, or specify an ID. | e.g. Select a project... |  |
| Label Names | `labels` | multiOptions | [] | ✗ | Optional labels that will be assigned to a created task. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
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
| Order | `order` | number | 0 | Non-zero integer used to sort tasks under the same parent |
| Due Date | `dueDate` | string |  | Specific date in YYYY-MM-DD format |
| Assignee ID | `assigneeId` | string |  | Responsible user ID (for shared tasks) |
| Duration | `duration` | number | 0 | Positive integer for task duration (must be used with Duration Unit) |
| Duration Unit | `durationUnit` | options | minute | Unit of time for duration (must be used with Duration) |
| Deadline Date | `deadlineDate` | string |  | Specific deadline date in YYYY-MM-DD format |

</details>

| Name | `name` | string |  | ✓ | Name of the project |  |
| Additional Fields | `projectOptions` | collection | {} | ✗ | The color of the project | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Color | `color` | options |  | The color of the project |
| Is Favorite | `is_favorite` | boolean | False | Whether the project is a favorite |
| Parent ID | `parent_id` | string |  | Parent project ID |
| View Style | `view_style` | options | list | The default view style of the project |

</details>

| Project Name or ID | `sectionProject` | resourceLocator |  | ✓ | The project to add the section to | e.g. Select a project... |  |
| Name | `sectionName` | string |  | ✓ | Name of the section |  |
| Additional Fields | `sectionOptions` | collection | {} | ✗ | The order of the section | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Order | `order` | number | 0 | The order of the section |

</details>

| Task ID | `commentTaskId` | string |  | ✓ | The ID of the task to comment on |  |
| Content | `commentContent` | string |  | ✓ | Comment content |  |
| Name | `labelName` | string |  | ✓ | Name of the label |  |
| Additional Fields | `labelOptions` | collection | {} | ✗ | The color of the label | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Color | `color` | options |  | The color of the label |
| Order | `order` | number | 0 | Label order |
| Is Favorite | `is_favorite` | boolean | False | Whether the label is a favorite |

</details>

| Task ID | `itemId` | string |  | ✓ | The ID of the task to attach reminder to |  |
| Due Date Type | `dueDateType` | options | natural_language | ✓ | Human-readable date and time (e.g., "tomorrow 2pm") |  |

**Due Date Type options:**

* **Natural Language** (`natural_language`) - Human-readable date and time (e.g., "tomorrow 2pm")
* **Full-Day Date** (`full_day`) - Date without specific time (floating)
* **Floating Date with Time** (`floating_time`) - Date and time without timezone
* **Fixed Timezone Date with Time** (`fixed_timezone`) - Date and time with specific timezone

| Natural Language Representation | `natural_language_representation` | string |  | ✓ | Human-readable date and time | e.g. e.g., "tomorrow 2pm", "monday 10:45am" |  |
| Date | `date` | string |  | ✓ | Full-day date in YYYY-MM-DD format | e.g. YYYY-MM-DD |  |
| Date Time | `datetime` | dateTime |  | ✓ | Floating date and time (no timezone) |  |
| Date Time | `datetime` | dateTime |  | ✓ | Date and time with timezone |  |
| Timezone | `timezone` | string |  | ✓ | Timezone for the fixed timezone date | e.g. e.g., "America/New_York" |  |
| Additional Fields | `reminderOptions` | collection | {} | ✗ | The reminder type | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Type | `type` | options | absolute | The reminder type |
| Minute Offset | `minute_offset` | number | 0 | Minutes before the task due date |
| Notify User ID | `notify_uid` | string |  | User ID to notify (for shared tasks) |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Project ID | `projectId` | string |  | ✓ | The project ID - can be either a string or number |  |
| Section ID | `sectionId` | string |  | ✓ |  |  |
| Comment ID | `commentId` | string |  | ✓ |  |  |
| Label ID | `labelId` | string |  | ✓ |  |  |
| Reminder ID | `reminderId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Project ID | `projectId` | string |  | ✓ | The project ID - can be either a string or number |  |
| Section ID | `sectionId` | string |  | ✓ |  |  |
| Comment ID | `commentId` | string |  | ✓ |  |  |
| Label ID | `labelId` | string |  | ✓ |  |  |

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

| Filters | `sectionFilters` | collection | {} | ✗ | Filter sections by project. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Project Name or ID | `project_id` | options |  | Filter sections by project. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Filters | `commentFilters` | collection | {} | ✗ | Filter comments by task ID | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Task ID | `task_id` | string |  | Filter comments by task ID |
| Project ID | `project_id` | string |  | Filter comments by project ID |

</details>


### Move parameters (`move`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Project Name or ID | `project` | resourceLocator |  | ✓ | The destination project. Choose from the list, or specify an ID. | e.g. Select a project... |  |
| Section Name or ID | `section` | options |  | ✗ | Section to which you want move the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `options` | collection | {} | ✗ | The destination section. The task becomes the last root task of the section. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Section Name or ID | `section` | options |  | The destination section. The task becomes the last root task of the section. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Parent Name or ID | `parent` | options |  | The destination parent task. The task becomes the last child task of the parent task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Quick Add parameters (`quickAdd`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Text | `text` | string |  | ✓ | Natural language text for quick adding task (e.g., "Buy milk @Grocery #shopping tomorrow"). It can include a due date in free form text, a project name starting with the "#" character (without spaces), a label starting with the "@" character, an assignee starting with the "+" character, a priority (e.g., p1), a deadline between "{}" (e.g. {in 3 days}), or a description starting from "//" until the end of the text. |  |
| Additional Fields | `options` | collection | {} | ✗ | The content of the note | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Note | `note` | string |  | The content of the note |
| Reminder | `reminder` | string |  | The date of the reminder, added in free form text |
| Auto Reminder | `auto_reminder` | boolean | False | When this option is enabled, the default reminder will be added to the new item if it has a due date with time set |

</details>


### Reopen parameters (`reopen`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |

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
| Label Names | `labels` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Priority | `priority` | number | 1 | Task priority from 1 (normal) to 4 (urgent) |
| Order | `order` | number | 0 | Non-zero integer used to sort tasks under the same parent |
| Due Date | `dueDate` | string |  | Specific date in YYYY-MM-DD format |
| Assignee ID | `assigneeId` | string |  | Responsible user ID (for shared tasks) |
| Duration | `duration` | number | 0 | Positive integer for task duration (must be used with Duration Unit) |
| Duration Unit | `durationUnit` | options | minute | Unit of time for duration (must be used with Duration) |
| Deadline Date | `deadlineDate` | string |  | Specific deadline date in YYYY-MM-DD format |

</details>

| Project ID | `projectId` | string |  | ✓ | The project ID - can be either a string or number |  |
| Update Fields | `projectUpdateFields` | collection | {} | ✗ | Name of the project | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | Name of the project |
| Color | `color` | options |  | The color of the project |
| Is Favorite | `is_favorite` | boolean | False | Whether the project is a favorite |
| View Style | `view_style` | options | list | The default view style of the project |

</details>

| Section ID | `sectionId` | string |  | ✓ |  |  |
| Update Fields | `sectionUpdateFields` | collection | {} | ✗ | Name of the section | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | Name of the section |

</details>

| Comment ID | `commentId` | string |  | ✓ |  |  |
| Update Fields | `commentUpdateFields` | collection | {} | ✗ | Comment content | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content | `content` | string |  | Comment content |

</details>

| Label ID | `labelId` | string |  | ✓ |  |  |
| Update Fields | `labelUpdateFields` | collection | {} | ✗ | Name of the label | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | Name of the label |
| Color | `color` | options |  | The color of the label |
| Order | `order` | number | 0 | Label order |
| Is Favorite | `is_favorite` | boolean | False | Whether the label is a favorite |

</details>

| Reminder ID | `reminderId` | string |  | ✓ |  |  |
| Update Fields | `reminderUpdateFields` | collection | {} | ✗ | Human-readable date and time | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Due | `due` | collection | {} | Human-readable date and time |
| Type | `type` | options | absolute | The reminder type |
| Minute Offset | `minute_offset` | number | 0 | Minutes before the task due date |
| Notify User ID | `notify_uid` | string |  | User ID to notify (for shared tasks) |

</details>


### Archive parameters (`archive`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project ID | `projectId` | string |  | ✓ | The project ID - can be either a string or number |  |

### Get Collaborators parameters (`getCollaborators`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project ID | `projectId` | string |  | ✓ | The project ID - can be either a string or number |  |

### Unarchive parameters (`unarchive`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project ID | `projectId` | string |  | ✓ | The project ID - can be either a string or number |  |

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
node: Berry Red
displayName: Todoist
description: Consume Todoist API
version:
- '2'
- '2.1'
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
    validation: &id003
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
    typeInfo: &id004
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
    description: The destination project. Choose from the list, or specify an ID.
    placeholder: Select a project...
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - create
          - move
    typeInfo: &id014
      type: resourceLocator
      displayName: Project Name or ID
      name: project
  - id: labels
    name: Label Names
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
      displayName: Label Names
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
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the project
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - project
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: sectionProject
    name: Project Name or ID
    type: resourceLocator
    default: ''
    required: true
    description: The project to add the section to
    placeholder: Select a project...
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - section
          operation:
          - create
    typeInfo:
      type: resourceLocator
      displayName: Project Name or ID
      name: sectionProject
  - id: sectionName
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the section
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - section
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: sectionName
  - id: commentTaskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the task to comment on
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - comment
          operation:
          - create
    typeInfo:
      type: string
      displayName: Task ID
      name: commentTaskId
  - id: commentContent
    name: Content
    type: string
    default: ''
    required: true
    description: Comment content
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - comment
          operation:
          - create
    typeInfo:
      type: string
      displayName: Content
      name: commentContent
      typeOptions:
        rows: 3
  - id: labelName
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the label
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - label
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: labelName
  - id: itemId
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the task to attach reminder to
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - reminder
          operation:
          - create
    typeInfo:
      type: string
      displayName: Task ID
      name: itemId
  - id: dueDateType
    name: Due Date Type
    type: options
    default: natural_language
    required: true
    description: Human-readable date and time (e.g., "tomorrow 2pm")
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - reminder
          operation:
          - create
    typeInfo:
      type: options
      displayName: Due Date Type
      name: dueDateType
      possibleValues:
      - value: natural_language
        name: Natural Language
        description: Human-readable date and time (e.g., "tomorrow 2pm")
      - value: full_day
        name: Full-Day Date
        description: Date without specific time (floating)
      - value: floating_time
        name: Floating Date with Time
        description: Date and time without timezone
      - value: fixed_timezone
        name: Fixed Timezone Date with Time
        description: Date and time with specific timezone
  - id: natural_language_representation
    name: Natural Language Representation
    type: string
    default: ''
    required: true
    description: Human-readable date and time
    placeholder: e.g., "tomorrow 2pm", "monday 10:45am"
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - reminder
          operation:
          - create
          dueDateType:
          - natural_language
    typeInfo:
      type: string
      displayName: Natural Language Representation
      name: natural_language_representation
  - id: date
    name: Date
    type: string
    default: ''
    required: true
    description: Full-day date in YYYY-MM-DD format
    placeholder: YYYY-MM-DD
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - reminder
          operation:
          - create
          dueDateType:
          - full_day
    typeInfo:
      type: string
      displayName: Date
      name: date
  - id: datetime
    name: Date Time
    type: dateTime
    default: ''
    required: true
    description: Floating date and time (no timezone)
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - reminder
          operation:
          - create
          dueDateType:
          - fixed_timezone
    typeInfo: &id002
      type: dateTime
      displayName: Date Time
      name: datetime
  - id: datetime
    name: Date Time
    type: dateTime
    default: ''
    required: true
    description: Date and time with timezone
    validation: *id001
    typeInfo: *id002
  - id: timezone
    name: Timezone
    type: string
    default: ''
    required: true
    description: Timezone for the fixed timezone date
    placeholder: e.g., "America/New_York"
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - reminder
          operation:
          - create
          dueDateType:
          - fixed_timezone
    typeInfo:
      type: string
      displayName: Timezone
      name: timezone
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
    validation: *id003
    typeInfo: *id004
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: The project ID - can be either a string or number
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - project
          operation:
          - archive
          - delete
          - get
          - getCollaborators
          - unarchive
          - update
    typeInfo: &id006
      type: string
      displayName: Project ID
      name: projectId
  - id: sectionId
    name: Section ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - section
          operation:
          - delete
          - get
          - update
    typeInfo: &id008
      type: string
      displayName: Section ID
      name: sectionId
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - comment
          operation:
          - delete
          - get
          - update
    typeInfo: &id010
      type: string
      displayName: Comment ID
      name: commentId
  - id: labelId
    name: Label ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - label
          operation:
          - delete
          - get
          - update
    typeInfo: &id012
      type: string
      displayName: Label ID
      name: labelId
  - id: reminderId
    name: Reminder ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - reminder
          operation:
          - delete
          - update
    typeInfo: &id016
      type: string
      displayName: Reminder ID
      name: reminderId
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
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: The project ID - can be either a string or number
    validation: *id005
    typeInfo: *id006
  - id: sectionId
    name: Section ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: labelId
    name: Label ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
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
    validation: *id003
    typeInfo: *id004
  - id: project
    name: Project Name or ID
    type: resourceLocator
    default: ''
    required: true
    description: The destination project. Choose from the list, or specify an ID.
    placeholder: Select a project...
    validation: *id013
    typeInfo: *id014
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
        hide: {}
    typeInfo:
      type: options
      displayName: Section Name or ID
      name: section
      typeOptions:
        loadOptionsMethod: getSections
      possibleValues: []
- id: quickAdd
  name: Quick Add
  description: Quick add a task using natural language
  params:
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: 'Natural language text for quick adding task (e.g., "Buy milk @Grocery
      #shopping tomorrow"). It can include a due date in free form text, a project
      name starting with the "#" character (without spaces), a label starting with
      the "@" character, an assignee starting with the "+" character, a priority (e.g.,
      p1), a deadline between "{}" (e.g. {in 3 days}), or a description starting from
      "//" until the end of the text.'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - quickAdd
    typeInfo:
      type: string
      displayName: Text
      name: text
      typeOptions:
        rows: 3
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
    validation: *id003
    typeInfo: *id004
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
    validation: *id003
    typeInfo: *id004
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: The project ID - can be either a string or number
    validation: *id005
    typeInfo: *id006
  - id: sectionId
    name: Section ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: labelId
    name: Label ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: reminderId
    name: Reminder ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id015
    typeInfo: *id016
- id: archive
  name: Archive
  description: Archive a project
  params:
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: The project ID - can be either a string or number
    validation: *id005
    typeInfo: *id006
- id: getCollaborators
  name: Get Collaborators
  description: Get project collaborators
  params:
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: The project ID - can be either a string or number
    validation: *id005
    typeInfo: *id006
- id: unarchive
  name: Unarchive
  description: Unarchive a project
  params:
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: The project ID - can be either a string or number
    validation: *id005
    typeInfo: *id006
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
  - field: options
    text: Add Field
  - field: options
    text: Add option
  - field: filters
    text: Add option
  - field: updateFields
    text: Add Field
  - field: projectOptions
    text: Add Field
  - field: projectUpdateFields
    text: Add Field
  - field: sectionProject
    text: Select a project...
  - field: sectionOptions
    text: Add Field
  - field: sectionUpdateFields
    text: Add Field
  - field: sectionFilters
    text: Add Filter
  - field: commentUpdateFields
    text: Add Field
  - field: commentFilters
    text: Add Filter
  - field: labelOptions
    text: Add Field
  - field: labelUpdateFields
    text: Add Field
  - field: natural_language_representation
    text: e.g., "tomorrow 2pm", "monday 10:45am"
  - field: date
    text: YYYY-MM-DD
  - field: timezone
    text: e.g., "America/New_York"
  - field: reminderOptions
    text: Add Field
  - field: reminderUpdateFields
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
  "$id": "https://n8n.io/schemas/nodes/Berry Red.json",
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
        "quickAdd",
        "reopen",
        "update",
        "archive",
        "getCollaborators",
        "unarchive"
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
            "task",
            "project",
            "section",
            "comment",
            "label",
            "reminder"
          ],
          "default": "task"
        },
        "operation": {
          "description": "Create a new reminder",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "getAll",
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
          "description": "The destination project. Choose from the list, or specify an ID.",
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
        "options": {
          "description": "A description for the task",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
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
        "text": {
          "description": "Natural language text for quick adding task (e.g., \"Buy milk @Grocery #shopping tomorrow\"). It can include a due date in free form text, a project name starting with the \"#\" character (without spaces), a label starting with the \"@\" character, an assignee starting with the \"+\" character, a priority (e.g., p1), a deadline between \"{}\" (e.g. {in 3 days}), or a description starting from \"//\" until the end of the text.",
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
        },
        "projectId": {
          "description": "The project ID - can be either a string or number",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "Name of the project",
          "type": "string",
          "default": ""
        },
        "projectOptions": {
          "description": "The color of the project",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "projectUpdateFields": {
          "description": "Name of the project",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "sectionId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "sectionProject": {
          "description": "The project to add the section to",
          "type": "string",
          "examples": [
            "Select a project..."
          ]
        },
        "sectionName": {
          "description": "Name of the section",
          "type": "string",
          "default": ""
        },
        "sectionOptions": {
          "description": "The order of the section",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "sectionUpdateFields": {
          "description": "Name of the section",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "sectionFilters": {
          "description": "Filter sections by project. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "commentId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "commentTaskId": {
          "description": "The ID of the task to comment on",
          "type": "string",
          "default": ""
        },
        "commentContent": {
          "description": "Comment content",
          "type": "string",
          "default": ""
        },
        "commentUpdateFields": {
          "description": "Comment content",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "commentFilters": {
          "description": "Filter comments by task ID",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "labelId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "labelName": {
          "description": "Name of the label",
          "type": "string",
          "default": ""
        },
        "labelOptions": {
          "description": "The color of the label",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "labelUpdateFields": {
          "description": "Name of the label",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "reminderId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "itemId": {
          "description": "The ID of the task to attach reminder to",
          "type": "string",
          "default": ""
        },
        "dueDateType": {
          "description": "Human-readable date and time (e.g., \"tomorrow 2pm\")",
          "type": "string",
          "enum": [
            "natural_language",
            "full_day",
            "floating_time",
            "fixed_timezone"
          ],
          "default": "natural_language"
        },
        "natural_language_representation": {
          "description": "Human-readable date and time",
          "type": "string",
          "default": "",
          "examples": [
            "e.g., \"tomorrow 2pm\", \"monday 10:45am\""
          ]
        },
        "date": {
          "description": "Full-day date in YYYY-MM-DD format",
          "type": "string",
          "default": "",
          "examples": [
            "YYYY-MM-DD"
          ]
        },
        "datetime": {
          "description": "Date and time with timezone",
          "type": "string",
          "default": ""
        },
        "timezone": {
          "description": "Timezone for the fixed timezone date",
          "type": "string",
          "default": "",
          "examples": [
            "e.g., \"America/New_York\""
          ]
        },
        "reminderOptions": {
          "description": "The reminder type",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "reminderUpdateFields": {
          "description": "Human-readable date and time",
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
    "version": [
      "2",
      "2.1"
    ]
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
| ['2', '2.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
