---
title: "Node: Asana"
slug: "node-asana"
version: "1"
updated: "2025-11-13"
summary: "Consume Asana REST API"
node_type: "regular"
group: "['input']"
---

# Node: Asana

**Purpose.** Consume Asana REST API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:asana.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **asanaApi**: N/A
- **asanaOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `asanaApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `asanaOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Subtask Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a subtask |
| Get Many | `getAll` | Get many subtasks |

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a task |
| Delete | `delete` | Delete a task |
| Get | `get` | Get a task |
| Get Many | `getAll` | Get many tasks |
| Move | `move` | Move a task |
| Search | `search` | Search for tasks |
| Update | `update` | Update a task |

### Taskcomment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a comment to a task |
| Remove | `remove` | Remove a comment from a task |

### Taskproject Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a task to a project |
| Remove | `remove` | Remove a task from a project |

### Tasktag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a tag to a task |
| Remove | `remove` | Remove a tag from a task |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a user |
| Get Many | `getAll` | Get many users |

### Project Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new project |
| Delete | `delete` | Delete a project |
| Get | `get` | Get a project |
| Get Many | `getAll` | Get many projects |
| Update | `update` | Update a project |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | task | ✗ | Resource to operate on |  |

**Resource options:**

* **Project** (`project`)
* **Subtask** (`subtask`)
* **Task** (`task`)
* **Task Comment** (`taskComment`)
* **Task Project** (`taskProject`)
* **Task Tag** (`taskTag`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a subtask |  |

**Operation options:**

* **Create** (`create`) - Create a subtask
* **Get Many** (`getAll`) - Get many subtasks

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Parent Task ID | `taskId` | string |  | ✓ | The task to operate on |  |
| Name | `name` | string |  | ✓ | The name of the subtask to create |  |
| Additional Fields | `otherProperties` | collection | {} | ✗ | Set Assignee on the subtask. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assignee` | options |  | Set Assignee on the subtask. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Assignee Status | `assignee_status` | options | inbox | Set Assignee status on the subtask (requires Assignee) |
| Completed | `completed` | boolean | False | Whether the subtask should be marked completed |
| Due On | `due_on` | dateTime |  | Date on which the time is due |
| Liked | `liked` | boolean | False | Whether the task is liked by the authorized user |
| Notes | `notes` | string |  | The task notes |
| Workspace Name or ID | `workspace` | options |  | The workspace to create the subtask in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Workspace Name or ID | `workspace` | options |  | ✓ | The workspace to create the task in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Name | `name` | string |  | ✓ | The name of the task to create |  |
| Additional Fields | `otherProperties` | collection | {} | ✗ | Set Assignee on the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assignee` | options |  | Set Assignee on the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Assignee Status | `assignee_status` | options | inbox | Set Assignee status on the task (requires Assignee) |
| Completed | `completed` | boolean | False | Whether the task should be marked completed |
| Due On | `due_on` | dateTime |  | Date on which the time is due |
| Name | `name` | string |  | The new name of the task |
| Liked | `liked` | boolean | False | Whether the task is liked by the authorized user |
| Notes | `notes` | string |  | The task notes |
| Project Names or IDs | `projects` | multiOptions | [] | The project to filter tasks on. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Name | `name` | string |  | ✓ | The name of the project to create |  |
| Workspace Name or ID | `workspace` | options |  | ✓ | The workspace to create the project in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Team Name or ID | `team` | options |  | ✗ | The team this project will be assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Other properties to set | e.g. Add Property |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Color | `color` | options | none | Color of the project |
| Due On | `due_on` | dateTime |  | The day on which this project is due. This takes a date with format YYYY-MM-DD. |
| Notes | `notes` | string |  | Basic description or notes for the project |
| Privacy Setting | `privacy_setting` | options | private | The privacy setting of the project |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Parent Task ID | `taskId` | string |  | ✓ | The task to operate on |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Defines fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field Names or IDs | `opt_fields` | multiOptions |  | Defines fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Pretty | `opt_pretty` | boolean | False | Whether to provide “pretty” output |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Filters | `filters` | collection | {} | ✗ | Properties to search for | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assignee` | options |  | The assignee to filter tasks on. Note: If you specify assignee, you must also specify the workspace to filter on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Field Names or IDs | `opt_fields` | multiOptions |  | Defines fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Pretty | `opt_pretty` | boolean | False | Whether to provide “pretty” output |
| Project Name or ID | `project` | options |  | The project to filter tasks on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Section Name or ID | `section` | options |  | The section to filter tasks on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Workspace Name or ID | `workspace` | options |  | The workspace to filter tasks on. Note: If you specify workspace, you must also specify the assignee to filter on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Completed Since | `completed_since` | dateTime |  | Only return tasks that are either incomplete or that have been completed since this time |
| Modified Since | `modified_since` | dateTime |  | Only return tasks that have been modified since the given time |

</details>

| Workspace Name or ID | `workspace` | options |  | ✓ | The workspace in which to get users. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Workspace Name or ID | `workspace` | options |  | ✓ | The workspace in which to get users. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Other properties to set | e.g. Add Property |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Archived | `archived` | boolean | False | Whether to only return projects whose archived field takes on the value of this parameter |
| Teams Name or ID | `team` | options |  | The new name of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `id` | string |  | ✓ | The ID of the task to delete |  |
| Project ID | `id` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `id` | string |  | ✓ | The ID of the task to get the data of |  |
| User ID | `userId` | string |  | ✓ | An identifier for the user to get data of. Can be one of an email address,the globally unique identifier for the user, or the keyword me to indicate the current user making the request. |  |
| Project ID | `id` | string |  | ✓ |  |  |

### Move parameters (`move`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `id` | string |  | ✓ | The ID of the task to be moved |  |
| Project Name or ID | `projectId` | options |  | ✓ | Project to show the sections of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Section Name or ID | `section` | options |  | ✓ | The Section to move the task to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workspace Name or ID | `workspace` | options |  | ✓ | The workspace in which the task is searched. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Filters | `searchTaskProperties` | collection | {} | ✗ | Properties to search for | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Completed | `completed` | boolean | False | Whether the task is marked completed |
| Text | `text` | string |  | Text to search for in name or notes |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `id` | string |  | ✓ | The ID of the task to update the data of |  |
| Additional Fields | `otherProperties` | collection | {} | ✗ | Set Assignee on the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assignee` | options |  | Set Assignee on the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Assignee Status | `assignee_status` | options | inbox | Set Assignee status on the task (requires Assignee) |
| Completed | `completed` | boolean | False | Whether the task should be marked completed |
| Due On | `due_on` | dateTime |  | Date on which the time is due |
| Name | `name` | string |  | The new name of the task |
| Liked | `liked` | boolean | False | Whether the task is liked by the authorized user |
| Notes | `notes` | string |  | The task notes |
| Project Names or IDs | `projects` | multiOptions | [] | The project to filter tasks on. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Workspace Name or ID | `workspace` | options |  | ✓ | The workspace in which to get users. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Project ID | `id` | string |  | ✓ | The ID of the project to update the data of |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Other properties to set | e.g. Add Property |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Color | `color` | options | none | Color of the project |
| Due On | `due_on` | dateTime |  | The day on which this project is due. This takes a date with format YYYY-MM-DD. |
| Name | `name` | string |  | The name of the project |
| Notes | `notes` | string |  | Basic description or notes for the project |
| Owner | `owner` | string |  | The new assignee/cardinal for this project |
| Privacy Setting | `privacy_setting` | options | private | The privacy setting of the project |
| Team Name or ID | `team` | options |  | The team this project will be assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `id` | string |  | ✓ | The ID of the task to add the comment to |  |
| Is Text HTML | `isTextHtml` | boolean | False | ✗ | Whether body is HTML or simple text |  |
| Text | `text` | string |  | ✓ | The plain text of the comment to add |  |
| HTML Text | `text` | string |  | ✓ | Comment as HTML string. Do not use together with plain text. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Properties of the task comment | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Pinned | `is_pinned` | boolean | False | Whether to pin the comment |

</details>

| Task ID | `id` | string |  | ✓ | The ID of the task to add the project to |  |
| Project Name or ID | `project` | options |  | ✓ | The project where the task will be added. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Other properties to set | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Insert After | `insert_after` | string |  | A task in the project to insert the task after, or null to insert at the beginning of the list |
| Insert Before | `insert_before` | string |  | A task in the project to insert the task before, or null to insert at the end of the list |
| Section | `section` | string |  | A section in the project to insert the task into. The task will be inserted at the bottom of the section. |

</details>

| Task ID | `id` | string |  | ✓ | The ID of the task to add the tag to |  |
| Tags Name or ID | `tag` | options |  | ✓ | The tag that should be added. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Comment ID | `id` | string |  | ✓ | The ID of the comment to be removed |  |
| Task ID | `id` | string |  | ✓ | The ID of the task to add the project to |  |
| Project Name or ID | `project` | options |  | ✓ | The project where the task will be removed from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Task ID | `id` | string |  | ✓ | The ID of the task to add the tag to |  |
| Tags Name or ID | `tag` | options |  | ✓ | The tag that should be added. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

---

## Load Options Methods

- `getProjects`

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
node: asana
displayName: Asana
description: Consume Asana REST API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: asanaApi
  required: true
- name: asanaOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a subtask
  params:
  - id: taskId
    name: Parent Task ID
    type: string
    default: ''
    required: true
    description: The task to operate on
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - subtask
    typeInfo: &id006
      type: string
      displayName: Parent Task ID
      name: taskId
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the subtask to create
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - project
    typeInfo: &id002
      type: string
      displayName: Name
      name: name
  - id: workspace
    name: Workspace Name or ID
    type: options
    default: ''
    required: true
    description: The workspace to create the task in. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - project
    typeInfo: &id004
      type: options
      displayName: Workspace Name or ID
      name: workspace
      typeOptions:
        loadOptionsMethod: getWorkspaces
      possibleValues: []
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the task to create
    validation: *id001
    typeInfo: *id002
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the project to create
    validation: *id001
    typeInfo: *id002
  - id: workspace
    name: Workspace Name or ID
    type: options
    default: ''
    required: true
    description: The workspace to create the project in. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: false
    description: The team this project will be assigned to. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - project
    typeInfo:
      type: options
      displayName: Team Name or ID
      name: team
      typeOptions:
        loadOptionsMethod: getTeams
      possibleValues: []
- id: getAll
  name: Get Many
  description: Get many subtasks
  params:
  - id: taskId
    name: Parent Task ID
    type: string
    default: ''
    required: true
    description: The task to operate on
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id007
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - project
    typeInfo: &id008
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id009
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - project
          returnAll:
          - false
    typeInfo: &id010
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id007
    typeInfo: *id008
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
  - id: workspace
    name: Workspace Name or ID
    type: options
    default: ''
    required: true
    description: The workspace in which to get users. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: workspace
    name: Workspace Name or ID
    type: options
    default: ''
    required: true
    description: The workspace in which to get users. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id007
    typeInfo: *id008
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
- id: delete
  name: Delete
  description: Delete a task
  params:
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the task to delete
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - project
    typeInfo: &id012
      type: string
      displayName: Project ID
      name: id
  - id: id
    name: Project ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
- id: get
  name: Get
  description: Get a task
  params:
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the task to get the data of
    validation: *id011
    typeInfo: *id012
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: An identifier for the user to get data of. Can be one of an email
      address,the globally unique identifier for the user, or the keyword me to indicate
      the current user making the request.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - user
    typeInfo:
      type: string
      displayName: User ID
      name: userId
  - id: id
    name: Project ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
- id: move
  name: Move
  description: Move a task
  params:
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the task to be moved
    validation: *id011
    typeInfo: *id012
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: Project to show the sections of. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - move
          resource:
          - task
    typeInfo:
      type: options
      displayName: Project Name or ID
      name: projectId
      typeOptions:
        loadOptionsMethod: getProjects
      possibleValues: []
  - id: section
    name: Section Name or ID
    type: options
    default: ''
    required: true
    description: The Section to move the task to. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - move
          resource:
          - task
    typeInfo:
      type: options
      displayName: Section Name or ID
      name: section
      typeOptions:
        loadOptionsMethod: getSections
      possibleValues: []
- id: search
  name: Search
  description: Search for tasks
  params:
  - id: workspace
    name: Workspace Name or ID
    type: options
    default: ''
    required: true
    description: The workspace in which the task is searched. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
- id: update
  name: Update
  description: Update a task
  params:
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the task to update the data of
    validation: *id011
    typeInfo: *id012
  - id: workspace
    name: Workspace Name or ID
    type: options
    default: ''
    required: true
    description: The workspace in which to get users. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Project ID
    type: string
    default: ''
    required: true
    description: The ID of the project to update the data of
    validation: *id011
    typeInfo: *id012
- id: add
  name: Add
  description: Add a comment to a task
  params:
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the task to add the comment to
    validation: *id011
    typeInfo: *id012
  - id: isTextHtml
    name: Is Text HTML
    type: boolean
    default: false
    required: false
    description: Whether body is HTML or simple text
    validation:
      displayOptions:
        show:
          operation:
          - add
          resource:
          - taskComment
    typeInfo:
      type: boolean
      displayName: Is Text HTML
      name: isTextHtml
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: The plain text of the comment to add
    validation: &id013
      required: true
      displayOptions:
        show:
          operation:
          - add
          resource:
          - taskComment
          isTextHtml:
          - true
    typeInfo: &id014
      type: string
      displayName: HTML Text
      name: text
  - id: text
    name: HTML Text
    type: string
    default: ''
    required: true
    description: Comment as HTML string. Do not use together with plain text.
    validation: *id013
    typeInfo: *id014
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the task to add the project to
    validation: *id011
    typeInfo: *id012
  - id: project
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: The project where the task will be added. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id015
      required: true
      displayOptions:
        show:
          operation:
          - remove
          resource:
          - taskProject
    typeInfo: &id016
      type: options
      displayName: Project Name or ID
      name: project
      typeOptions:
        loadOptionsMethod: getProjects
      possibleValues: []
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the task to add the tag to
    validation: *id011
    typeInfo: *id012
  - id: tag
    name: Tags Name or ID
    type: options
    default: ''
    required: true
    description: The tag that should be added. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id017
      required: true
      displayOptions:
        show:
          operation:
          - remove
          resource:
          - taskTag
    typeInfo: &id018
      type: options
      displayName: Tags Name or ID
      name: tag
      typeOptions:
        loadOptionsMethod: getTags
      possibleValues: []
- id: remove
  name: Remove
  description: Remove a comment from a task
  params:
  - id: id
    name: Comment ID
    type: string
    default: ''
    required: true
    description: The ID of the comment to be removed
    validation: *id011
    typeInfo: *id012
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the task to add the project to
    validation: *id011
    typeInfo: *id012
  - id: project
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: The project where the task will be removed from. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id015
    typeInfo: *id016
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the task to add the tag to
    validation: *id011
    typeInfo: *id012
  - id: tag
    name: Tags Name or ID
    type: options
    default: ''
    required: true
    description: The tag that should be added. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id017
    typeInfo: *id018
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
  - field: otherProperties
    text: Add Field
  - field: options
    text: Add Field
  - field: filters
    text: Add Filter
  - field: searchTaskProperties
    text: Add Filter
  - field: otherProperties
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Property
  - field: additionalFields
    text: Add Property
  - field: updateFields
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
  "$id": "https://n8n.io/schemas/nodes/asana.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Asana Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "getAll",
        "delete",
        "get",
        "move",
        "search",
        "update",
        "add",
        "remove"
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
            "project",
            "subtask",
            "task",
            "taskComment",
            "taskProject",
            "taskTag",
            "user"
          ],
          "default": "task"
        },
        "operation": {
          "description": "Create a new project",
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
        "taskId": {
          "description": "The task to operate on",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "The name of the project to create",
          "type": "string",
          "default": ""
        },
        "otherProperties": {
          "description": "Set Assignee on the task. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
          "default": 100
        },
        "options": {
          "description": "Defines fields to return. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "workspace": {
          "description": "The workspace in which to get users. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "id": {
          "description": "The ID of the project to update the data of",
          "type": "string",
          "default": ""
        },
        "filters": {
          "description": "Properties to search for",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "projectId": {
          "description": "Project to show the sections of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "section": {
          "description": "The Section to move the task to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "searchTaskProperties": {
          "description": "Properties to search for",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "isTextHtml": {
          "description": "Whether body is HTML or simple text",
          "type": "boolean",
          "default": false
        },
        "text": {
          "description": "Comment as HTML string. Do not use together with plain text.",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Other properties to set",
          "type": "string",
          "default": {},
          "examples": [
            "Add Property"
          ]
        },
        "project": {
          "description": "The project where the task will be removed from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "tag": {
          "description": "The tag that should be added. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "userId": {
          "description": "An identifier for the user to get data of. Can be one of an email address,the globally unique identifier for the user, or the keyword me to indicate the current user making the request.",
          "type": "string",
          "default": ""
        },
        "team": {
          "description": "The team this project will be assigned to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Other properties to set",
          "type": "string",
          "default": {},
          "examples": [
            "Add Property"
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
      "name": "asanaApi",
      "required": true
    },
    {
      "name": "asanaOAuth2Api",
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
