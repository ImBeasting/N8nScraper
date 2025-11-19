---
title: "Node: ClickUp"
slug: "node-clickup"
version: "1"
updated: "2025-11-13"
summary: "Consume ClickUp API (Beta)"
node_type: "regular"
group: "['output']"
---

# Node: ClickUp

**Purpose.** Consume ClickUp API (Beta)
**Subtitle.** ={{$parameter["operation"] + ":" + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:clickup.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **clickUpApi**: N/A
- **clickUpOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `clickUpApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `clickUpOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Checklist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a checklist |
| Delete | `delete` | Delete a checklist |
| Update | `update` | Update a checklist |

### Checklistitem Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a checklist item |
| Delete | `delete` | Delete a checklist item |
| Update | `update` | Update a checklist item |

### Comment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a comment |
| Delete | `delete` | Delete a comment |
| Get Many | `getAll` | Get many comments |
| Update | `update` | Update a comment |

### Folder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a folder |
| Delete | `delete` | Delete a folder |
| Get | `get` | Get a folder |
| Get Many | `getAll` | Get many folders |
| Update | `update` | Update a folder |

### Goal Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a goal |
| Delete | `delete` | Delete a goal |
| Get | `get` | Get a goal |
| Get Many | `getAll` | Get many goals |
| Update | `update` | Update a goal |

### Goalkeyresult Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a key result |
| Delete | `delete` | Delete a key result |
| Update | `update` | Update a key result |

### Tasktag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a tag to a task |
| Remove | `remove` | Remove a tag from a task |

### Tasklist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a task to a list |
| Remove | `remove` | Remove a task from a list |

### Spacetag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a space tag |
| Delete | `delete` | Delete a space tag |
| Get Many | `getAll` | Get many space tags |
| Update | `update` | Update a space tag |

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a task |
| Delete | `delete` | Delete a task |
| Get | `get` | Get a task |
| Get Many | `getAll` | Get many tasks |
| Member | `member` | Get task members |
| Set Custom Field | `setCustomField` | Set a custom field |
| Update | `update` | Update a task |

### Taskdependency Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a task dependency |
| Delete | `delete` | Delete a task dependency |

### Timeentry Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a time entry |
| Delete | `delete` | Delete a time entry |
| Get | `get` | Get a time entry |
| Get Many | `getAll` | Get many time entries |
| Start | `start` | Start a time entry |
| Stop | `stop` | Stop the current running timer |
| Update | `update` | Update a time Entry |

### Timeentrytag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add tag to time entry |
| Get Many | `getAll` | Get many time entry tags |
| Remove | `remove` | Remove tag from time entry |

### List Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a list |
| Custom Fields | `customFields` | Retrieve list's custom fields |
| Delete | `delete` | Delete a list |
| Get | `get` | Get a list |
| Get Many | `getAll` | Get many lists |
| Member | `member` | Get list members |
| Update | `update` | Update a list |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | task | ✗ | Resource to operate on |  |

**Resource options:**

* **Checklist** (`checklist`)
* **Checklist Item** (`checklistItem`)
* **Comment** (`comment`)
* **Folder** (`folder`)
* **Goal** (`goal`)
* **Goal Key Result** (`goalKeyResult`)
* **Guest** (`guest`)
* **List** (`list`)
* **Space Tag** (`spaceTag`)
* **Task** (`task`)
* **Task Dependency** (`taskDependency`)
* **Task List** (`taskList`)
* **Task Tag** (`taskTag`)
* **Time Entry** (`timeEntry`)
* **Time Entry Tag** (`timeEntryTag`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a checklist |  |

**Operation options:**

* **Create** (`create`) - Create a checklist
* **Delete** (`delete`) - Delete a checklist
* **Update** (`update`) - Update a checklist

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `task` | string |  | ✓ |  |  |
| Name | `name` | string |  | ✓ |  |  |
| Checklist ID | `checklist` | string |  | ✓ |  |  |
| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee ID | `assignee` | string |  |  |

</details>

| Comment On | `commentOn` | options |  | ✗ |  |  |

**Comment On options:**

* **List** (`list`)
* **Task** (`task`)
* **View** (`view`)

| ID | `id` | string |  | ✓ |  |  |
| Comment Text | `commentText` | string |  | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether creation notifications will be sent to everyone including the creator of the comment | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee ID | `assignee` | string |  |  |
| Notify All | `notifyAll` | boolean | False | Whether creation notifications will be sent to everyone including the creator of the comment |

</details>

| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Name | `name` | string |  | ✓ |  |  |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Color | `color` | color |  |  |
| Description | `description` | string |  |  |
| Due Date | `dueDate` | dateTime |  |  |
| Multiple Owners | `multipleOwners` | boolean | False |  |
| Owners | `owners` | string |  |  |

</details>

| Goal ID | `goal` | string |  | ✓ |  |  |
| Name | `name` | string |  | ✓ |  |  |
| Type | `type` | options |  | ✓ |  |  |

**Type options:**

* **Automatic** (`automatic`)
* **Boolean** (`boolean`)
* **Currency** (`currency`)
* **Number** (`number`)
* **Percentage** (`percentage`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Required for Percentage, Automatic, Number and Currency | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| List IDs | `listIds` | string |  |  |
| Owners | `owners` | string |  |  |
| Steps Start | `stepsStart` | number | 0 | Required for Percentage, Automatic, Number and Currency |
| Steps End | `stepsEnd` | number | 0 | Required for Percentage, Automatic, Number and Currency |
| Task IDs | `taskIds` | string |  |  |
| Unit | `unit` | string |  | Only matters for type Number and Currency. For Currency the unit must be a valid currency code. |

</details>

| Space ID | `space` | string |  | ✓ |  |  |
| Name | `name` | string |  | ✓ |  |  |
| Foreground Color | `foregroundColor` | color | #000000 | ✓ |  |  |
| Background Color | `backgroundColor` | color | #000000 | ✓ |  |  |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folderless List | `folderless` | boolean | False | ✓ |  |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List Name or ID | `list` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List Name or ID | `list` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Name | `name` | string |  | ✓ | The first name on the task |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Names or IDs | `assignees` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Custom Fields JSON | `customFieldsJson` | json |  | Custom fields to set as JSON in the format: <code>[ {"id": "", "value": ""} ]</code> |
| Content | `content` | string |  |  |
| Due Date | `dueDate` | dateTime |  |  |
| Due Date Time | `dueDateTime` | boolean | False |  |
| Is Markdown Content | `markdownContent` | boolean | False |  |
| Notify All | `notifyAll` | boolean | False |  |
| Parent ID | `parentId` | string |  |  |
| Priority | `priority` | number | 3 | Integer mapping as 1 : Urgent, 2 : High, 3 : Normal, 4 : Low |
| Start Date | `startDate` | dateTime |  |  |
| Start Date Time | `startDateTime` | boolean | False |  |
| Status Name or ID | `status` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Tag Names or IDs | `tags` | multiOptions | [] | The array of tags applied to this task. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Time Estimate | `timeEstimate` | number | 1 | Time estimate in minutes |

</details>

| Task ID | `task` | string |  | ✓ |  |  |
| Depends On Task ID | `dependsOnTask` | string |  | ✓ |  |  |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folderless List | `folderless` | boolean | False | ✓ |  |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List Name or ID | `list` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List Name or ID | `list` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Start | `start` | dateTime |  | ✓ |  |  |
| Duration (Minutes) | `duration` | number | 0 | ✓ | Duration in minutes |  |
| Task Name or ID | `task` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assignee` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Billable | `billable` | boolean | True |  |
| Description | `description` | string |  | Description of the time entry |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folderless List | `folderless` | boolean | False | ✓ |  |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Integer mapping as 1 : Urgent, 2 : High, 3 : Normal, 4 : Low | e.g. Add Field | min:1, max:4 |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee | `assignee` | string |  |  |
| Content | `content` | string |  |  |
| Due Date | `dueDate` | dateTime |  |  |
| Due Date Time | `dueDateTime` | boolean | False |  |
| Priority | `priority` | number | 3 | Integer mapping as 1 : Urgent, 2 : High, 3 : Normal, 4 : Low |
| Status Name or ID | `status` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Checklist ID | `checklist` | string |  | ✓ |  |  |
| Checklist ID | `checklist` | string |  | ✓ |  |  |
| Checklist Item ID | `checklistItem` | string |  | ✓ |  |  |
| Comment ID | `comment` | string |  | ✓ |  |  |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Goal ID | `goal` | string |  | ✓ |  |  |
| Key Result ID | `keyResult` | string |  | ✓ |  |  |
| Space ID | `space` | string |  | ✓ |  |  |
| Name or ID | `name` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Task ID | `id` | string |  | ✓ |  |  |
| Task ID | `task` | string |  | ✓ |  |  |
| Depends On Task ID | `dependsOnTask` | string |  | ✓ |  |  |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Time Entry ID | `timeEntry` | string |  | ✓ |  |  |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folderless List | `folderless` | boolean | False | ✓ |  |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List ID | `list` | string |  | ✓ |  |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Checklist ID | `checklist` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  |  |
| Position | `position` | number | 0 |  |

</details>

| Checklist ID | `checklist` | string |  | ✓ |  |  |
| Checklist Item ID | `checklistItem` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Checklist item that you want to nest the target checklist item underneath | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee ID | `assignee` | string |  |  |
| Name | `name` | string |  |  |
| Parent Checklist Item ID | `parent` | string |  | Checklist item that you want to nest the target checklist item underneath |
| Resolved | `resolved` | boolean | False |  |

</details>

| Comment ID | `comment` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee ID | `assignee` | string |  |  |
| Comment Text | `commentText` | string |  |  |
| Resolved | `resolved` | boolean | False |  |

</details>

| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  |  |

</details>

| Goal ID | `goal` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Add Owners | `addOwners` | string |  |  |
| Color | `color` | color |  |  |
| Description | `description` | string |  |  |
| Due Date | `dueDate` | dateTime |  |  |
| Name | `name` | string |  |  |
| Remove Owners | `removeOwners` | string |  |  |

</details>

| Key Result ID | `keyResult` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Only matters for type Number and Currency. For Currency the unit must be a valid currency code. | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  |  |
| Note | `note` | string |  |  |
| Steps Current | `stepsCurrent` | number | 1 |  |
| Steps End | `stepsEnd` | number | 0 |  |
| Steps Start | `stepsStart` | number | 0 |  |
| Unit | `unit` | string |  | Only matters for type Number and Currency. For Currency the unit must be a valid currency code. |

</details>

| Space ID | `space` | string |  | ✓ |  |  |
| Name or ID | `name` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| New Name | `newName` | string |  | ✓ | New name to set for the tag |  |
| Foreground Color | `foregroundColor` | color | #000000 | ✓ |  |  |
| Background Color | `backgroundColor` | color | #000000 | ✓ |  |  |
| Task ID | `id` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Assignees IDs. Multiple ca be added separated by comma. | e.g. Add Field | min:1, max:4 |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Add Assignees | `addAssignees` | string |  | Assignees IDs. Multiple ca be added separated by comma. |
| Content | `content` | string |  |  |
| Due Date | `dueDate` | dateTime |  |  |
| Due Date Time | `dueDateTime` | boolean | False |  |
| Is Markdown Content | `markdownContent` | boolean | False |  |
| Name | `name` | string |  |  |
| Notify All | `notifyAll` | boolean | False |  |
| Parent ID | `parentId` | string |  |  |
| Priority | `priority` | number | 3 | Integer mapping as 1 : Urgent, 2 : High, 3 : Normal, 4 : Low |
| Remove Assignees | `removeAssignees` | string |  | Assignees IDs. Multiple ca be added separated by comma. |
| Status | `status` | string |  |  |
| Start Date | `startDate` | dateTime |  |  |
| Start Date Time | `startDateTime` | boolean | False |  |
| Time Estimate | `timeEstimate` | number | 1 | Time estimate in minutes |

</details>

| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folderless List | `folderless` | boolean | False | ✓ |  |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List Name or ID | `list` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List Name or ID | `list` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Archived | `archived` | boolean | False | ✓ |  |  |
| Time Entry ID | `timeEntry` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assignee` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Billable | `billable` | boolean | True |  |
| Description | `description` | string |  | Description of the time entry |
| Duration (Minutes) | `duration` | number | 0 | Duration in minutes |
| Start | `start` | dateTime |  |  |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Task Name or ID | `task` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folderless List | `folderless` | boolean | False | ✓ |  |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List ID | `list` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assignee` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Content | `content` | string |  |  |
| Due Date | `dueDate` | dateTime |  |  |
| Due Date Time | `dueDateTime` | boolean | False |  |
| Name | `name` | string |  |  |
| Priority | `priority` | number | 3 | Integer mapping as 1 : Urgent, 2 : High, 3 : Normal, 4 : Low |
| Unset Status | `unsetStatus` | boolean | False |  |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Comments On | `commentsOn` | options |  | ✗ |  |  |

**Comments On options:**

* **List** (`list`)
* **Task** (`task`)
* **View** (`view`)

| ID | `id` | string |  | ✓ |  |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Archived | `archived` | boolean | False |  |

</details>

| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Space ID | `space` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | True | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folderless List | `folderless` | boolean | False | ✓ |  |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List Name or ID | `list` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List Name or ID | `list` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | True | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Archived | `archived` | boolean | False |  |
| Assignee Names or IDs | `assignees` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Date Created Greater Than | `dateCreatedGt` | dateTime |  | Filter date created greater |
| Date Created Less Than | `dateCreatedLt` | dateTime |  | Filter date created less than posix time |
| Date Updated Greater Than | `dateUpdatedGt` | dateTime |  | Filter date updated greater than |
| Date Update Less Than | `dateUpdatedLt` | dateTime |  | Filter date updated less than |
| Due Date Greater Than | `dueDateGt` | dateTime |  | Filter due date greater than |
| Due Date Less Than | `dueDateLt` | dateTime |  | Filter due date less than |
| Include Closed | `includeClosed` | boolean | False | The response does by default not include closed tasks. Set this to true and dont send a status filter to include closed tasks. |
| Order By | `orderBy` | options |  |  |
| Status Names or IDs | `statuses` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Subtasks | `subtasks` | boolean | False | Whether to include subtasks, default false |
| Tag Names or IDs | `tags` | multiOptions | [] | The array of tags applied to this task. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| End Date | `end_date` | dateTime |  |  |
| Start Date | `start_date` | dateTime |  |  |

</details>

| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folderless List | `folderless` | boolean | False | ✓ |  |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Archived | `archived` | boolean | False |  |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Goal ID | `goal` | string |  | ✓ |  |  |
| Task ID | `id` | string |  | ✓ |  |  |
| Include Subtasks | `includeSubtasks` | boolean | False | ✗ | Whether to also fetch and include subtasks for this task |  |
| Include Markdown Description | `includeMarkdownDescription` | boolean | False | ✗ | Whether to include the markdown_description field in the response. This is important for preserving links in the description. |  |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Running | `running` | boolean | False | ✗ | Whether to return just the current running time entry |  |
| Time Entry ID | `timeEntry` | string |  | ✓ |  |  |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folderless List | `folderless` | boolean | False | ✓ |  |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List ID | `list` | string |  | ✓ |  |  |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Tag Name | `tagName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to reference a task by it's custom task ID | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Task IDs | `custom_task_ids` | boolean | False | Whether to reference a task by it's custom task ID |
| Team Name or ID | `team_id` | options |  | Only used when the parameter is set to custom_task_ids=true. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Task ID | `taskId` | string |  | ✓ |  |  |
| List ID | `listId` | string |  | ✓ |  |  |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Time Entry IDs | `timeEntryIds` | string |  | ✓ |  |  |
| Tags | `tagsUi` | fixedCollection | {} | ✗ | e.g. Add Tag |  |

<details>
<summary><strong>Tags sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Tag | `tagsValues` |  |  |  |

</details>


### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Tag Name | `tagName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to reference a task by it's custom task ID | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Task IDs | `custom_task_ids` | boolean | False | Whether to reference a task by it's custom task ID |
| Team Name or ID | `team_id` | options |  | Only used when the parameter is set to custom_task_ids=true. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Task ID | `taskId` | string |  | ✓ |  |  |
| List ID | `listId` | string |  | ✓ |  |  |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Time Entry IDs | `timeEntryIds` | string |  | ✓ |  |  |
| Tag Names or IDs | `tagNames` | multiOptions | [] | ✓ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Member parameters (`member`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `id` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | True | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| List ID | `id` | string |  | ✓ | Task ID |  |
| Return All | `returnAll` | boolean | True | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Set Custom Field parameters (`setCustomField`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `task` | string |  | ✓ | The ID of the task to add custom field to |  |
| Field ID | `field` | string |  | ✓ | The ID of the field to add custom field to |  |
| Value Is JSON | `jsonParse` | boolean | False | ✗ | The value is JSON and will be parsed as such. Is needed if for example needed for labels which expects the value to be an array. |  |
| Value | `value` | string |  | ✓ | The value to set on custom field |  |

### Start parameters (`start`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Task ID | `task` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Description of the time entry | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Billable | `billable` | boolean | True |  |
| Description | `description` | string |  | Description of the time entry |

</details>


### Stop parameters (`stop`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Custom Fields parameters (`customFields`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Space Name or ID | `space` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folderless List | `folderless` | boolean | False | ✓ |  |  |
| Folder Name or ID | `folder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List Name or ID | `list` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| List Name or ID | `list` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

---

## Load Options Methods

- `getTeams`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ":" + $parameter["resource"]}}`

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
* Categories: Productivity, Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: clickUp
displayName: ClickUp
description: Consume ClickUp API (Beta)
version: '1'
nodeType: regular
group:
- output
credentials:
- name: clickUpApi
  required: true
- name: clickUpOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a checklist
  params:
  - id: task
    name: Task ID
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
          - start
    typeInfo: &id010
      type: string
      displayName: Task ID
      name: task
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - list
          operation:
          - create
    typeInfo: &id002
      type: string
      displayName: Name
      name: name
  - id: checklist
    name: Checklist ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - checklistItem
          operation:
          - update
    typeInfo: &id016
      type: string
      displayName: Checklist ID
      name: checklist
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: commentOn
    name: Comment On
    type: options
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - comment
          operation:
          - create
    typeInfo:
      type: options
      displayName: Comment On
      name: commentOn
      possibleValues:
      - value: list
        name: List
        description: ''
      - value: task
        name: Task
        description: ''
      - value: view
        name: View
        description: ''
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id019
      required: true
      displayOptions:
        show:
          resource:
          - list
          operation:
          - member
    typeInfo: &id020
      type: string
      displayName: List ID
      name: id
  - id: commentText
    name: Comment Text
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - comment
          operation:
          - create
    typeInfo:
      type: string
      displayName: Comment Text
      name: commentText
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - list
          operation:
          - update
    typeInfo: &id004
      type: options
      displayName: Team Name or ID
      name: team
      typeOptions:
        loadOptionsMethod: getTeams
      possibleValues: []
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - list
          operation:
          - update
    typeInfo: &id006
      type: options
      displayName: Space Name or ID
      name: space
      typeOptions:
        loadOptionsMethod: getSpaces
      possibleValues: []
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
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
  - id: goal
    name: Goal ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id017
      required: true
      displayOptions:
        show:
          resource:
          - goalKeyResult
          operation:
          - create
    typeInfo: &id018
      type: string
      displayName: Goal ID
      name: goal
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: type
    name: Type
    type: options
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - goalKeyResult
          operation:
          - create
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: automatic
        name: Automatic
        description: ''
      - value: boolean
        name: Boolean
        description: ''
      - value: currency
        name: Currency
        description: ''
      - value: number
        name: Number
        description: ''
      - value: percentage
        name: Percentage
        description: ''
  - id: space
    name: Space ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: foregroundColor
    name: Foreground Color
    type: color
    default: '#000000'
    required: true
    description: ''
    validation: &id029
      required: true
      displayOptions:
        show:
          resource:
          - spaceTag
          operation:
          - create
          - update
    typeInfo: &id030
      type: color
      displayName: Foreground Color
      name: foregroundColor
  - id: backgroundColor
    name: Background Color
    type: color
    default: '#000000'
    required: true
    description: ''
    validation: &id031
      required: true
      displayOptions:
        show:
          resource:
          - spaceTag
          operation:
          - create
          - update
    typeInfo: &id032
      type: color
      displayName: Background Color
      name: backgroundColor
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folderless
    name: Folderless List
    type: boolean
    default: false
    required: true
    description: ''
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - list
          operation:
          - update
    typeInfo: &id012
      type: boolean
      displayName: Folderless List
      name: folderless
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - list
          operation:
          - update
          folderless:
          - false
    typeInfo: &id014
      type: options
      displayName: Folder Name or ID
      name: folder
      typeOptions:
        loadOptionsMethod: getFolders
      possibleValues: []
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - list
          operation:
          - update
    typeInfo: &id008
      type: string
      displayName: List ID
      name: list
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The first name on the task
    validation: *id001
    typeInfo: *id002
  - id: task
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: dependsOnTask
    name: Depends On Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id021
      required: true
      displayOptions:
        show:
          resource:
          - taskDependency
          operation:
          - delete
    typeInfo: &id022
      type: string
      displayName: Depends On Task ID
      name: dependsOnTask
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folderless
    name: Folderless List
    type: boolean
    default: false
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
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
  - id: duration
    name: Duration (Minutes)
    type: number
    default: 0
    required: true
    description: Duration in minutes
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - timeEntry
          operation:
          - create
    typeInfo:
      type: number
      displayName: Duration (Minutes)
      name: duration
  - id: task
    name: Task Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id009
    typeInfo: *id010
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folderless
    name: Folderless List
    type: boolean
    default: false
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
- id: delete
  name: Delete
  description: Delete a checklist
  params:
  - id: checklist
    name: Checklist ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: checklist
    name: Checklist ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: checklistItem
    name: Checklist Item ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id023
      required: true
      displayOptions:
        show:
          resource:
          - checklistItem
          operation:
          - update
    typeInfo: &id024
      type: string
      displayName: Checklist Item ID
      name: checklistItem
  - id: comment
    name: Comment ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id025
      required: true
      displayOptions:
        show:
          resource:
          - comment
          operation:
          - update
    typeInfo: &id026
      type: string
      displayName: Comment ID
      name: comment
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: goal
    name: Goal ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: keyResult
    name: Key Result ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id027
      required: true
      displayOptions:
        show:
          resource:
          - goalKeyResult
          operation:
          - update
    typeInfo: &id028
      type: string
      displayName: Key Result ID
      name: keyResult
  - id: space
    name: Space ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: name
    name: Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id019
    typeInfo: *id020
  - id: task
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: dependsOnTask
    name: Depends On Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id021
    typeInfo: *id022
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: timeEntry
    name: Time Entry ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id033
      required: true
      displayOptions:
        show:
          resource:
          - timeEntry
          operation:
          - update
    typeInfo: &id034
      type: string
      displayName: Time Entry ID
      name: timeEntry
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folderless
    name: Folderless List
    type: boolean
    default: false
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: list
    name: List ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
- id: update
  name: Update
  description: Update a checklist
  params:
  - id: checklist
    name: Checklist ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: checklist
    name: Checklist ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: checklistItem
    name: Checklist Item ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id023
    typeInfo: *id024
  - id: comment
    name: Comment ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id025
    typeInfo: *id026
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: goal
    name: Goal ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: keyResult
    name: Key Result ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id027
    typeInfo: *id028
  - id: space
    name: Space ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: name
    name: Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: newName
    name: New Name
    type: string
    default: ''
    required: true
    description: New name to set for the tag
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - spaceTag
          operation:
          - update
    typeInfo:
      type: string
      displayName: New Name
      name: newName
  - id: foregroundColor
    name: Foreground Color
    type: color
    default: '#000000'
    required: true
    description: ''
    validation: *id029
    typeInfo: *id030
  - id: backgroundColor
    name: Background Color
    type: color
    default: '#000000'
    required: true
    description: ''
    validation: *id031
    typeInfo: *id032
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id019
    typeInfo: *id020
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folderless
    name: Folderless List
    type: boolean
    default: false
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: archived
    name: Archived
    type: boolean
    default: false
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - timeEntry
          operation:
          - update
    typeInfo:
      type: boolean
      displayName: Archived
      name: archived
  - id: timeEntry
    name: Time Entry ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id033
    typeInfo: *id034
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folderless
    name: Folderless List
    type: boolean
    default: false
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: list
    name: List ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
- id: getAll
  name: Get Many
  description: Get many comments
  params:
  - id: commentsOn
    name: Comments On
    type: options
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - comment
          operation:
          - getAll
    typeInfo:
      type: options
      displayName: Comments On
      name: commentsOn
      possibleValues:
      - value: list
        name: List
        description: ''
      - value: task
        name: Task
        description: ''
      - value: view
        name: View
        description: ''
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id035
      displayOptions:
        show:
          resource:
          - list
          operation:
          - getAll
    typeInfo: &id036
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id035
    typeInfo: *id036
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id035
    typeInfo: *id036
  - id: space
    name: Space ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: true
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id037
      displayOptions:
        show:
          resource:
          - list
          operation:
          - member
    typeInfo: &id038
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id035
    typeInfo: *id036
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folderless
    name: Folderless List
    type: boolean
    default: false
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: returnAll
    name: Return All
    type: boolean
    default: true
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id037
    typeInfo: *id038
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id035
    typeInfo: *id036
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id037
    typeInfo: *id038
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation: *id035
    typeInfo: *id036
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id037
    typeInfo: *id038
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation: *id035
    typeInfo: *id036
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folderless
    name: Folderless List
    type: boolean
    default: false
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id035
    typeInfo: *id036
- id: get
  name: Get
  description: Get a folder
  params:
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: goal
    name: Goal ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id019
    typeInfo: *id020
  - id: includeSubtasks
    name: Include Subtasks
    type: boolean
    default: false
    required: false
    description: Whether to also fetch and include subtasks for this task
    validation:
      displayOptions:
        show:
          resource:
          - task
          operation:
          - get
    typeInfo:
      type: boolean
      displayName: Include Subtasks
      name: includeSubtasks
  - id: includeMarkdownDescription
    name: Include Markdown Description
    type: boolean
    default: false
    required: false
    description: Whether to include the markdown_description field in the response.
      This is important for preserving links in the description.
    validation:
      displayOptions:
        show:
          resource:
          - task
          operation:
          - get
    typeInfo:
      type: boolean
      displayName: Include Markdown Description
      name: includeMarkdownDescription
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: running
    name: Running
    type: boolean
    default: false
    required: false
    description: Whether to return just the current running time entry
    validation:
      displayOptions:
        show:
          resource:
          - timeEntry
          operation:
          - get
    typeInfo:
      type: boolean
      displayName: Running
      name: running
  - id: timeEntry
    name: Time Entry ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id033
    typeInfo: *id034
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folderless
    name: Folderless List
    type: boolean
    default: false
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: list
    name: List ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
- id: add
  name: Add
  description: Add a tag to a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id039
      required: true
      displayOptions:
        show:
          resource:
          - taskList
          operation:
          - remove
          - add
    typeInfo: &id040
      type: string
      displayName: Task ID
      name: taskId
  - id: tagName
    name: Tag Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id041
      required: true
      displayOptions:
        show:
          resource:
          - taskTag
          operation:
          - remove
          - add
    typeInfo: &id042
      type: string
      displayName: Tag Name
      name: tagName
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id039
    typeInfo: *id040
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id043
      required: true
      displayOptions:
        show:
          resource:
          - taskList
          operation:
          - remove
          - add
    typeInfo: &id044
      type: string
      displayName: List ID
      name: listId
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: timeEntryIds
    name: Time Entry IDs
    type: string
    default: ''
    required: true
    description: ''
    validation: &id045
      required: true
      displayOptions:
        show:
          resource:
          - timeEntryTag
          operation:
          - remove
    typeInfo: &id046
      type: string
      displayName: Time Entry IDs
      name: timeEntryIds
  - id: tagsUi
    name: Tags
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Tag
    validation:
      displayOptions:
        show:
          resource:
          - timeEntryTag
          operation:
          - add
    typeInfo:
      type: fixedCollection
      displayName: Tags
      name: tagsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: tagsValues
        displayName: Tag
        values:
        - displayName: Name
          name: name
          type: string
          default: ''
        - displayName: Background Color
          name: tag_bg
          type: color
          default: '#ff0000'
        - displayName: Foreground Color
          name: tag_fg
          type: color
          default: '#ff0000'
- id: remove
  name: Remove
  description: Remove a tag from a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id039
    typeInfo: *id040
  - id: tagName
    name: Tag Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id041
    typeInfo: *id042
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id039
    typeInfo: *id040
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id043
    typeInfo: *id044
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: timeEntryIds
    name: Time Entry IDs
    type: string
    default: ''
    required: true
    description: ''
    validation: *id045
    typeInfo: *id046
  - id: tagNames
    name: Tag Names or IDs
    type: multiOptions
    default: []
    required: true
    description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - timeEntryTag
          operation:
          - remove
    typeInfo:
      type: multiOptions
      displayName: Tag Names or IDs
      name: tagNames
      typeOptions:
        loadOptionsMethod: getTimeEntryTags
      possibleValues: []
- id: member
  name: Member
  description: Get task members
  params:
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id019
    typeInfo: *id020
  - id: returnAll
    name: Return All
    type: boolean
    default: true
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id037
    typeInfo: *id038
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id035
    typeInfo: *id036
  - id: id
    name: List ID
    type: string
    default: ''
    required: true
    description: Task ID
    validation: *id019
    typeInfo: *id020
  - id: returnAll
    name: Return All
    type: boolean
    default: true
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id037
    typeInfo: *id038
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id035
    typeInfo: *id036
- id: setCustomField
  name: Set Custom Field
  description: Set a custom field
  params:
  - id: task
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the task to add custom field to
    validation: *id009
    typeInfo: *id010
  - id: field
    name: Field ID
    type: string
    default: ''
    required: true
    description: The ID of the field to add custom field to
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - setCustomField
    typeInfo:
      type: string
      displayName: Field ID
      name: field
  - id: jsonParse
    name: Value Is JSON
    type: boolean
    default: false
    required: false
    description: The value is JSON and will be parsed as such. Is needed if for example
      needed for labels which expects the value to be an array.
    validation:
      displayOptions:
        show:
          resource:
          - task
          operation:
          - setCustomField
    typeInfo:
      type: boolean
      displayName: Value Is JSON
      name: jsonParse
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: The value to set on custom field
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - setCustomField
    typeInfo:
      type: string
      displayName: Value
      name: value
- id: start
  name: Start
  description: Start a time entry
  params:
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: task
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
- id: stop
  name: Stop
  description: Stop the current running timer
  params:
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
- id: customFields
  name: Custom Fields
  description: Retrieve list's custom fields
  params:
  - id: team
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: folderless
    name: Folderless List
    type: boolean
    default: false
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: folder
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
common_expressions:
- ={{$parameter["operation"] + ":" + $parameter["resource"]}}
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
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: updateFields
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
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: filters
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: tagsUi
    text: Add Tag
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
  "$id": "https://n8n.io/schemas/nodes/clickUp.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ClickUp Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "update",
        "getAll",
        "get",
        "add",
        "remove",
        "member",
        "setCustomField",
        "start",
        "stop",
        "customFields"
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
            "checklist",
            "checklistItem",
            "comment",
            "folder",
            "goal",
            "goalKeyResult",
            "guest",
            "list",
            "spaceTag",
            "task",
            "taskDependency",
            "taskList",
            "taskTag",
            "timeEntry",
            "timeEntryTag"
          ],
          "default": "task"
        },
        "operation": {
          "description": "Create a list",
          "type": "string",
          "enum": [
            "create",
            "customFields",
            "delete",
            "get",
            "getAll",
            "member",
            "update"
          ],
          "default": "customFields"
        },
        "task": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "checklist": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "additionalFields": {
          "description": "Integer mapping as 1 : Urgent, 2 : High, 3 : Normal, 4 : Low",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "checklistItem": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "commentOn": {
          "description": "",
          "type": "string",
          "enum": [
            "list",
            "task",
            "view"
          ],
          "default": ""
        },
        "id": {
          "description": "Task ID",
          "type": "string",
          "default": ""
        },
        "commentText": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "comment": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "commentsOn": {
          "description": "",
          "type": "string",
          "enum": [
            "list",
            "task",
            "view"
          ],
          "default": ""
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 50
        },
        "team": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "space": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "folder": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "filters": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "goal": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "type": {
          "description": "",
          "type": "string",
          "enum": [
            "automatic",
            "boolean",
            "currency",
            "number",
            "percentage"
          ],
          "default": ""
        },
        "keyResult": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "taskId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "tagName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "listId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "newName": {
          "description": "New name to set for the tag",
          "type": "string",
          "default": ""
        },
        "foregroundColor": {
          "description": "",
          "type": "string",
          "default": "#000000"
        },
        "backgroundColor": {
          "description": "",
          "type": "string",
          "default": "#000000"
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": true
        },
        "folderless": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "list": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "includeSubtasks": {
          "description": "Whether to also fetch and include subtasks for this task",
          "type": "boolean",
          "default": false
        },
        "includeMarkdownDescription": {
          "description": "Whether to include the markdown_description field in the response. This is important for preserving links in the description.",
          "type": "boolean",
          "default": false
        },
        "field": {
          "description": "The ID of the field to add custom field to",
          "type": "string",
          "default": ""
        },
        "jsonParse": {
          "description": "The value is JSON and will be parsed as such. Is needed if for example needed for labels which expects the value to be an array.",
          "type": "boolean",
          "default": false
        },
        "value": {
          "description": "The value to set on custom field",
          "type": "string",
          "default": ""
        },
        "dependsOnTask": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "running": {
          "description": "Whether to return just the current running time entry",
          "type": "boolean",
          "default": false
        },
        "timeEntry": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "start": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "duration": {
          "description": "Duration in minutes",
          "type": "number",
          "default": 0
        },
        "archived": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "timeEntryIds": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "tagsUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Tag"
          ]
        },
        "tagNames": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
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
      "name": "clickUpApi",
      "required": true
    },
    {
      "name": "clickUpOAuth2Api",
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
