---
title: "Node: Clockify"
slug: "node-clockify"
version: "1"
updated: "2026-01-08"
summary: "Consume Clockify REST API"
node_type: "regular"
group: "['transform']"
---

# Node: Clockify

**Purpose.** Consume Clockify REST API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:clockify.svg', 'dark': 'file:clockify.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **clockifyApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `clockifyApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Client Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a client |
| Delete | `delete` | Delete a client |
| Get | `get` | Get a client |
| Get Many | `getAll` | Get many clients |
| Update | `update` | Update a client |

### Project Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a project |
| Delete | `delete` | Delete a project |
| Get | `get` | Get a project |
| Get Many | `getAll` | Get many projects |
| Update | `update` | Update a project |

### Tag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a tag |
| Delete | `delete` | Delete a tag |
| Get Many | `getAll` | Get many tags |
| Update | `update` | Update a tag |

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a task |
| Delete | `delete` | Delete a task |
| Get | `get` | Get a task |
| Get Many | `getAll` | Get many tasks |
| Update | `update` | Update a task |

### Timeentry Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a time entry |
| Delete | `delete` | Delete a time entry |
| Get | `get` | Get time entrie |
| Update | `update` | Update a time entry |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many users |

### Workspace Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many workspaces |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | project | ✗ | Resource to operate on |  |

**Resource options:**

* **Client** (`client`)
* **Project** (`project`)
* **Tag** (`tag`)
* **Task** (`task`)
* **Time Entry** (`timeEntry`)
* **User** (`user`)
* **Workspace** (`workspace`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a client |  |

**Operation options:**

* **Create** (`create`) - Create a client
* **Delete** (`delete`) - Delete a client
* **Get** (`get`) - Get a client
* **Get Many** (`getAll`) - Get many clients
* **Update** (`update`) - Update a client

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Client Name | `name` | string |  | ✓ | Name of client being created |  |
| Project Name | `name` | string |  | ✓ | Name of project being created |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Billable | `billable` | boolean | True |  |
| Color | `color` | color | #0000FF |  |
| Client Name or ID | `clientId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Estimate | `estimateUi` | fixedCollection | {} |  |
| Is Public | `isPublic` | boolean | True |  |
| Note | `note` | string |  | Note about the project |

</details>

| Name | `name` | string |  | ✓ | Name of tag being created |  |
| Task Name | `name` | string |  | ✓ | Name of task to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Names or IDs | `assigneeIds` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Estimate | `estimate` | string |  | Estimate time the task will take, e.x: 2:30 (2 hours and 30 minutes) |

</details>

| Start | `start` | dateTime |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Filter by custom fields | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Billable | `billable` | boolean | False |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  |  |
| End | `end` | dateTime |  |  |
| Project Name or ID | `projectId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Tag Names or IDs | `tagIds` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Task ID | `taskId` | string |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Client ID | `clientId` | string |  | ✗ |  |  |
| Project ID | `projectId` | string |  | ✓ |  |  |
| Tag ID | `tagId` | string |  | ✓ |  |  |
| Task ID | `taskId` | string |  | ✓ | ID of task to delete |  |
| Time Entry ID | `timeEntryId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Client ID | `clientId` | string |  | ✗ |  |  |
| Project ID | `projectId` | string |  | ✓ |  |  |
| Task ID | `taskId` | string |  | ✓ | ID of task to get |  |
| Time Entry ID | `timeEntryId` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to return the time entry's duration rounded to minutes or seconds based on duration format (hh:mm or hh:mm:ss) from workspace settings | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Consider Duration Format | `consider-duration-format` | boolean | False | Whether to return the time entry's duration rounded to minutes or seconds based on duration format (hh:mm or hh:mm:ss) from workspace settings |
| Hydrated | `hydrated` | boolean | False | Whether to return the time entry's project, task and tags in full and not just their IDs |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | If provided, clients will be filtered by name | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Archived | `archived` | boolean | False |  |
| Name | `name` | string |  | If provided, clients will be filtered by name |
| Sort Order | `sort-order` | options |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Archived | `archived` | boolean | True |  |
| Billable | `billable` | boolean | True |  |
| Client Names or IDs | `clients` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Contains Client | `contains-client` | boolean | False | Whether to return only projects having a client |
| Client Status | `client-status` | options |  | If provided, projects will be filtered by whether they have a client |
| Contains User | `contains-user` | boolean | False | Whether to return only projects having users |
| Is Template | `is-template` | boolean | False | Whether to return only projects as templates |
| Name | `name` | string |  |  |
| Sort Column | `sort-column` | options |  |  |
| Sort Order | `sort-order` | options |  |  |
| User Name or ID | `users` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| User Status | `user-status` | options |  | If provided, projects will be filtered by whether they have a client |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Archived | `archived` | boolean | True |  |
| Name | `name` | string |  |  |
| Sort Column | `sort-column` | options |  |  |
| Sort Order | `sort-order` | options |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Filters | `filters` | collection | {} | ✗ | Text to match in the task name | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Is Active | `is-active` | boolean | False |  |
| Name | `name` | string |  | Text to match in the task name |
| Sort Column | `sort-column` | options | NAME |  |
| Sort Order | `sort-order` | options | ASCENDING |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | If provided, you'll get a filtered list of users that contain the provided string in their email address | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  | If provided, you'll get a filtered list of users that contain the provided string in their email address |
| Name | `name` | string |  | If provided, you'll get a filtered list of users that contain the provided string in their name |
| Status | `status` | options |  | If provided, you'll get a filtered list of users with the corresponding status |
| Sort Column | `sort-column` | options |  |  |
| Sort Order | `sort-order` | options |  |  |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Client ID | `clientId` | string |  | ✗ |  |  |
| Name | `name` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Address of client being created/updated | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  | Address of client being created/updated |
| Archived | `archived` | boolean | False |  |

</details>

| Project ID | `projectId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Billable | `billable` | boolean | True |  |
| Color | `color` | color | #0000FF |  |
| Client Name or ID | `clientId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Estimate | `estimateUi` | fixedCollection | {} |  |
| Is Public | `isPublic` | boolean | False |  |
| Name | `name` | string |  |  |
| Note | `note` | string |  | Note about the project |

</details>

| Tag ID | `tagId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Archived | `archived` | boolean | False |  |
| Name | `name` | string |  |  |

</details>

| Task ID | `taskId` | string |  | ✓ | ID of task to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Names or IDs | `assigneeIds` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Estimate | `estimate` | string |  | Estimate time the task will take, e.x: 2:30 (2 hours and 30 minutes) |
| Name | `name` | string |  |  |
| Status | `status` | options | ACTIVE |  |

</details>

| Time Entry ID | `timeEntryId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Filter by custom fields | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Billable | `billable` | boolean | False |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  |  |
| End | `end` | dateTime |  |  |
| Project Name or ID | `projectId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Start | `start` | dateTime |  |  |
| Tag Names or IDs | `tagIds` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Task ID | `taskId` | string |  |  |

</details>


---

## Load Options Methods

- `listWorkspaces`
- `if`
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
node: clockify
displayName: Clockify
description: Consume Clockify REST API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: clockifyApi
  required: true
operations:
- id: create
  name: Create
  description: Create a client
  params:
  - id: name
    name: Client Name
    type: string
    default: ''
    required: true
    description: Name of client being created
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - create
    typeInfo: &id002
      type: string
      displayName: Task Name
      name: name
  - id: name
    name: Project Name
    type: string
    default: ''
    required: true
    description: Name of project being created
    validation: *id001
    typeInfo: *id002
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of tag being created
    validation: *id001
    typeInfo: *id002
  - id: name
    name: Task Name
    type: string
    default: ''
    required: true
    description: Name of task to create
    validation: *id001
    typeInfo: *id002
  - id: start
    name: Start
    type: dateTime
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - timeEntry
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: Start
      name: start
- id: delete
  name: Delete
  description: Delete a client
  params:
  - id: clientId
    name: Client ID
    type: string
    default: ''
    required: false
    description: ''
    validation: &id003
      displayOptions:
        show:
          resource:
          - client
          operation:
          - update
    typeInfo: &id004
      type: string
      displayName: Client ID
      name: clientId
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - task
    typeInfo: &id006
      type: options
      displayName: Project Name or ID
      name: projectId
      typeOptions:
        loadOptionsMethod: loadProjectsForWorkspace
      possibleValues: []
  - id: tagId
    name: Tag ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - tag
          operation:
          - update
    typeInfo: &id016
      type: string
      displayName: Tag ID
      name: tagId
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of task to delete
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - update
    typeInfo: &id008
      type: string
      displayName: Task ID
      name: taskId
  - id: timeEntryId
    name: Time Entry ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - timeEntry
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Time Entry ID
      name: timeEntryId
- id: get
  name: Get
  description: Get a client
  params:
  - id: clientId
    name: Client ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of task to get
    validation: *id007
    typeInfo: *id008
  - id: timeEntryId
    name: Time Entry ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
- id: getAll
  name: Get Many
  description: Get many clients
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id011
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - user
    typeInfo: &id012
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id013
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - user
          returnAll:
          - false
    typeInfo: &id014
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
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 100
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
    default: 100
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
    default: 100
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
    default: 100
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
- id: update
  name: Update
  description: Update a client
  params:
  - id: clientId
    name: Client ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: tagId
    name: Tag ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of task to update
    validation: *id007
    typeInfo: *id008
  - id: timeEntryId
    name: Time Entry ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
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
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
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
  "$id": "https://n8n.io/schemas/nodes/clockify.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Clockify Node",
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
            "client",
            "project",
            "tag",
            "task",
            "timeEntry",
            "user",
            "workspace"
          ],
          "default": "project"
        },
        "workspaceId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "operation": {
          "description": "Get many workspaces",
          "type": "string",
          "enum": [
            "getAll"
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
        "name": {
          "description": "Name of task to create",
          "type": "string",
          "default": ""
        },
        "clientId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Whether to return the time entry's duration rounded to minutes or seconds based on duration format (hh:mm or hh:mm:ss) from workspace settings",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "Filter by custom fields",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "projectId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "tagId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "taskId": {
          "description": "ID of task to update",
          "type": "string",
          "default": ""
        },
        "filters": {
          "description": "Text to match in the task name",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "start": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "timeEntryId": {
          "description": "",
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
      "name": "clockifyApi",
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
