---
title: "Node: Taiga"
slug: "node-taiga"
version: "1"
updated: "2025-11-13"
summary: "Consume Taiga API"
node_type: "regular"
group: "['transform']"
---

# Node: Taiga

**Purpose.** Consume Taiga API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:taiga.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **taigaApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `taigaApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

**Headers Used:** Content-Type

---

## Operations

### Userstory Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a user story |
| Delete | `delete` | Delete a user story |
| Get | `get` | Get a user story |
| Get Many | `getAll` | Get many user stories |
| Update | `update` | Update a user story |

### Epic Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an epic |
| Delete | `delete` | Delete an epic |
| Get | `get` | Get an epic |
| Get Many | `getAll` | Get many epics |
| Update | `update` | Update an epic |

### Issue Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an issue |
| Delete | `delete` | Delete an issue |
| Get | `get` | Get an issue |
| Get Many | `getAll` | Get many issues |
| Update | `update` | Update an issue |

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a task |
| Delete | `delete` | Delete a task |
| Get | `get` | Get a task |
| Get Many | `getAll` | Get many tasks |
| Update | `update` | Update a task |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | issue | ✗ | Resource to operate on |  |

**Resource options:**

* **Epic** (`epic`)
* **Issue** (`issue`)
* **Task** (`task`)
* **User Story** (`userStory`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a user story |  |

**Operation options:**

* **Create** (`create`) - Create a user story
* **Delete** (`delete`) - Delete a user story
* **Get** (`get`) - Get a user story
* **Get Many** (`getAll`) - Get many user stories
* **Update** (`update`) - Update a user story

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `projectId` | options |  | ✓ | ID of the project to which the user story belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Subject | `subject` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the user to whom the user story is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigned_to` | options |  | ID of the user to whom the user story is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Backlog Order | `backlog_order` | number | 1 | Order of the user story in the backlog |
| Blocked Note | `blocked_note` | string |  | Reason why the user story is blocked. Requires "Is Blocked" toggle to be enabled. |
| Description | `description` | string |  |  |
| Is Blocked | `is_blocked` | boolean | False | Whether the user story is blocked |
| Kanban Order | `kanban_order` | number | 1 | Order of the user story in the kanban |
| Milestone (Sprint) Name or ID | `milestone` | options |  | ID of the milestone of the user story. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sprint Order | `sprint_order` | number | 1 | Order of the user story in the milestone |
| Status Name or ID | `status` | options |  | ID of the status of the user story. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Type Name or ID | `type` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Project Name or ID | `projectId` | options |  | ✓ | ID of the project to which the epic belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Subject | `subject` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the user to assign the epic to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assigned To Name or ID | `assigned_to` | options |  | ID of the user to assign the epic to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Blocked Note | `blocked_note` | string |  | Reason why the epic is blocked. Requires "Is Blocked" toggle to be enabled. |
| Color | `color` | color | 0000FF | Color code in hexadecimal notation |
| Description | `description` | string |  |  |
| Is Blocked | `is_blocked` | boolean | False | Whether the issue is blocked |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Project Name or ID | `projectId` | options |  | ✓ | ID of the project to which the issue belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Subject | `subject` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the user to whom the issue is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigned_to` | options |  | ID of the user to whom the issue is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Blocked Note | `blocked_note` | string |  | Reason why the issue is blocked. Requires "Is Blocked" toggle to be enabled. |
| Description | `description` | string |  |  |
| Is Blocked | `is_blocked` | boolean | False | Whether the issue is blocked |
| Milestone (Sprint) Name or ID | `milestone` | options |  | ID of the milestone of the issue. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Priority Name or ID | `priority` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Severity Name or ID | `severity` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Status Name or ID | `status` | options |  | ID of the status of the issue. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Type Name or ID | `type` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Project Name or ID | `projectId` | options |  | ✓ | ID of the project to which the task belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Subject | `subject` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the user to whom the task is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigned_to` | options |  | ID of the user to whom the task is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Blocked Note | `blocked_note` | string |  | Reason why the task is blocked. Requires "Is Blocked" toggle to be enabled. |
| Description | `description` | string |  |  |
| Is Blocked | `is_blocked` | boolean | False | Whether the task is blocked |
| Milestone (Sprint) Name or ID | `milestone` | options |  | ID of the milestone of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Status Name or ID | `status` | options |  | ID of the status of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Taskboard Order | `taskboard_order` | number | 1 | Order of the task in the taskboard |
| User Story Name or ID | `user_story` | options |  | ID of the user story of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| User Story Order | `us_order` | number | 1 | Order of the task in the user story |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User Story ID | `userStoryId` | string |  | ✓ | ID of the user story to delete |  |
| Epic ID | `epicId` | string |  | ✓ | ID of the epic to delete |  |
| Issue ID | `issueId` | string |  | ✓ | ID of the issue to delete |  |
| Task ID | `taskId` | string |  | ✓ | ID of the task to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User Story ID | `userStoryId` | string |  | ✓ | ID of the user story to retrieve |  |
| Epic ID | `epicId` | string |  | ✓ | ID of the epic to retrieve |  |
| Issue ID | `issueId` | string |  | ✓ | ID of the issue to retrieve |  |
| Task ID | `taskId` | string |  | ✓ | ID of the task to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `projectId` | options |  | ✓ | ID of the project to which the user story belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | ID of the user whom the user story is assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigned_to` | options |  | ID of the user whom the user story is assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Epic Name or ID | `epic` | options |  | ID of the epic to which the user story belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Is Closed | `statusIsClosed` | boolean | False | Whether the user story is closed |
| Is Archived | `statusIsArchived` | boolean | False | Whether the user story has been archived |
| Milestone (Sprint) Name or ID | `milestone` | options |  | ID of the milestone of the user story. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Role Name or ID | `role` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Status Name or ID | `status` | options |  | ID of the status of the user story. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Project Name or ID | `projectId` | options |  | ✓ | ID of the project to which the epic belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | ID of the user whom the epic is assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigned_to` | options |  | ID of the user whom the epic is assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Is Closed | `statusIsClosed` | boolean | False | Whether the epic is closed |

</details>

| Project Name or ID | `projectId` | options |  | ✓ | ID of the project to which the issue belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | ID of the user to assign the issue to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigned_to` | options |  | ID of the user to assign the issue to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Order By | `orderBy` | options | assigned_to | Field to order the issues by |
| Owner Name or ID | `owner` | options |  | ID of the owner of the issue. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Priority Name or ID | `priority` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Role Name or ID | `role` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Severity Name or ID | `severity` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Status Name or ID | `status` | options |  | ID of the status of the issue. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Type Name or ID | `type` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Project Name or ID | `projectId` | options |  | ✓ | ID of the project to which the task belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | ID of the user whom the task is assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigned_to` | options |  | ID of the user whom the task is assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Is Closed | `statusIsClosed` | boolean | False | Whether the task is closed |
| Milestone (Sprint) Name or ID | `milestone` | options |  | ID of the milestone of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Owner Name or ID | `owner` | options |  | ID of the owner of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Role Name or ID | `role` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Status Name or ID | `status` | options |  | ID of the status of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| User Story Name or ID | `userStory` | options |  | ID of the user story to which the task belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project Name or ID | `projectId` | options |  | ✗ | ID of the project to set the user story to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| User Story ID | `userStoryId` | string |  | ✓ | ID of the user story to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the user to assign the the user story to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigned_to` | options |  | ID of the user to assign the the user story to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Backlog Order | `backlog_order` | number | 1 | Order of the user story in the backlog |
| Blocked Note | `blocked_note` | string |  | Reason why the user story is blocked. Requires "Is Blocked" toggle to be enabled. |
| Description | `description` | string |  |  |
| Is Blocked | `is_blocked` | boolean | False | Whether the user story is blocked |
| Kanban Order | `kanban_order` | number | 1 | Order of the user story in the kanban |
| Milestone (Sprint) Name or ID | `milestone` | options |  | ID of the milestone of the user story. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Subject | `subject` | string |  |  |
| Sprint Order | `sprint_order` | number | 1 | Order of the user story in the milestone |
| Status Name or ID | `status` | options |  | ID of the status of the user story. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Type Name or ID | `type` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Project Name or ID | `projectId` | options |  | ✗ | ID of the project to set the epic to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Epic ID | `epicId` | string |  | ✓ | ID of the epic to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the user to whom the epic is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assigned To Name or ID | `assigned_to` | options |  | ID of the user to whom the epic is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Blocked Note | `blocked_note` | string |  | Reason why the epic is blocked. Requires "Is Blocked" toggle to be enabled. |
| Color | `color` | color | 0000FF | Color code in hexadecimal notation |
| Description | `description` | string |  |  |
| Is Blocked | `is_blocked` | boolean | False | Whether the epic is blocked |
| Subject | `subject` | string |  |  |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Project Name or ID | `projectId` | options |  | ✗ | ID of the project to set the issue to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Issue ID | `issueId` | string |  | ✓ | ID of the issue to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the user whom the issue is assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigned_to` | options |  | ID of the user whom the issue is assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Blocked Note | `blocked_note` | string |  | Reason why the issue is blocked. Requires "Is Blocked" toggle to be enabled. |
| Description | `description` | string |  |  |
| Is Blocked | `is_blocked` | boolean | False | Whether the issue is blocked |
| Milestone (Sprint) Name or ID | `milestone` | options |  | ID of the milestone of the issue. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Priority Name or ID | `priority` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Severity Name or ID | `severity` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Status Name or ID | `status` | options |  | ID of the status of the issue. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Subject | `subject` | string |  |  |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Type Name or ID | `type` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Project Name or ID | `projectId` | options |  | ✗ | ID of the project to set the task to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Task ID | `taskId` | string |  | ✓ | ID of the task to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the user to assign the task to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigned_to` | options |  | ID of the user to assign the task to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Blocked Note | `blocked_note` | string |  | Reason why the task is blocked. Requires "Is Blocked" toggle to be enabled. |
| Description | `description` | string |  |  |
| Is Blocked | `is_blocked` | boolean | False | Whether the task is blocked |
| Milestone (Sprint) Name or ID | `milestone` | options |  | ID of the milestone of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Status Name or ID | `status` | options |  | ID of the status of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Subject | `subject` | string |  |  |
| User Story Name or ID | `user_story` | options |  | ID of the user story of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| User Story Order | `us_order` | number | 1 | Order of the task in the user story |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Taskboard Order | `taskboard_order` | number | 1 | Order of the task in the taskboard |

</details>


---

## Load Options Methods

- `getEpics`

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
* Categories: Development, Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: taiga
displayName: Taiga
description: Consume Taiga API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: taigaApi
  required: true
operations:
- id: create
  name: Create
  description: Create a user story
  params:
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: ID of the project to which the user story belongs. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      displayOptions:
        show:
          resource:
          - task
          operation:
          - update
    typeInfo: &id002
      type: options
      displayName: Project Name or ID
      name: projectId
      typeOptions:
        loadOptionsMethod: getProjects
      possibleValues: []
  - id: subject
    name: Subject
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
          - create
    typeInfo: &id004
      type: string
      displayName: Subject
      name: subject
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: ID of the project to which the epic belongs. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: ID of the project to which the issue belongs. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: ID of the project to which the task belongs. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
- id: delete
  name: Delete
  description: Delete a user story
  params:
  - id: userStoryId
    name: User Story ID
    type: string
    default: ''
    required: true
    description: ID of the user story to delete
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - userStory
          operation:
          - update
    typeInfo: &id006
      type: string
      displayName: User Story ID
      name: userStoryId
  - id: epicId
    name: Epic ID
    type: string
    default: ''
    required: true
    description: ID of the epic to delete
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - epic
          operation:
          - update
    typeInfo: &id008
      type: string
      displayName: Epic ID
      name: epicId
  - id: issueId
    name: Issue ID
    type: string
    default: ''
    required: true
    description: ID of the issue to delete
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Issue ID
      name: issueId
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task to delete
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - update
    typeInfo: &id012
      type: string
      displayName: Task ID
      name: taskId
- id: get
  name: Get
  description: Get a user story
  params:
  - id: userStoryId
    name: User Story ID
    type: string
    default: ''
    required: true
    description: ID of the user story to retrieve
    validation: *id005
    typeInfo: *id006
  - id: epicId
    name: Epic ID
    type: string
    default: ''
    required: true
    description: ID of the epic to retrieve
    validation: *id007
    typeInfo: *id008
  - id: issueId
    name: Issue ID
    type: string
    default: ''
    required: true
    description: ID of the issue to retrieve
    validation: *id009
    typeInfo: *id010
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task to retrieve
    validation: *id011
    typeInfo: *id012
- id: getAll
  name: Get Many
  description: Get many user stories
  params:
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: ID of the project to which the user story belongs. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id013
      displayOptions:
        show:
          resource:
          - task
          operation:
          - getAll
    typeInfo: &id014
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id015
      displayOptions:
        show:
          resource:
          - task
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id016
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: ID of the project to which the epic belongs. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id013
    typeInfo: *id014
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id015
    typeInfo: *id016
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: ID of the project to which the issue belongs. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id013
    typeInfo: *id014
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id015
    typeInfo: *id016
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: true
    description: ID of the project to which the task belongs. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id013
    typeInfo: *id014
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id015
    typeInfo: *id016
- id: update
  name: Update
  description: Update a user story
  params:
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: false
    description: ID of the project to set the user story to. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: userStoryId
    name: User Story ID
    type: string
    default: ''
    required: true
    description: ID of the user story to update
    validation: *id005
    typeInfo: *id006
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: false
    description: ID of the project to set the epic to. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: epicId
    name: Epic ID
    type: string
    default: ''
    required: true
    description: ID of the epic to update
    validation: *id007
    typeInfo: *id008
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: false
    description: ID of the project to set the issue to. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: issueId
    name: Issue ID
    type: string
    default: ''
    required: true
    description: ID of the issue to update
    validation: *id009
    typeInfo: *id010
  - id: projectId
    name: Project Name or ID
    type: options
    default: ''
    required: false
    description: ID of the project to set the task to. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task to update
    validation: *id011
    typeInfo: *id012
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - POST
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
  - field: filters
    text: Add Filter
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
  - field: filters
    text: Add Filter
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/taiga.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Taiga Node",
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
            "epic",
            "issue",
            "task",
            "userStory"
          ],
          "default": "issue"
        },
        "operation": {
          "description": "Create a task",
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
        "projectId": {
          "description": "ID of the project to set the task to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "subject": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "ID of the user to whom the task is assigned. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "userStoryId": {
          "description": "ID of the user story to update",
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
          "description": "ID of the user whom the task is assigned to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "updateFields": {
          "description": "ID of the user to assign the task to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "epicId": {
          "description": "ID of the epic to update",
          "type": "string",
          "default": ""
        },
        "issueId": {
          "description": "ID of the issue to update",
          "type": "string",
          "default": ""
        },
        "taskId": {
          "description": "ID of the task to update",
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
      "name": "taigaApi",
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
