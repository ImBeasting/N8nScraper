---
title: "Node: Wekan"
slug: "node-wekan"
version: "1"
updated: "2025-11-13"
summary: "Consume Wekan API"
node_type: "regular"
group: "['transform']"
---

# Node: Wekan

**Purpose.** Consume Wekan API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:wekan.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **wekanApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `wekanApi` | ✓ | - |

---

## Operations

### Board Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new board |
| Delete | `delete` | Delete a board |
| Get | `get` | Get the data of a board |
| Get Many | `getAll` | Get many user boards |

### Card Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new card |
| Delete | `delete` | Delete a card |
| Get | `get` | Get a card |
| Get Many | `getAll` | Get many cards |
| Update | `update` | Update a card |

### Cardcomment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a comment on a card |
| Delete | `delete` | Delete a comment from a card |
| Get | `get` | Get a card comment |
| Get Many | `getAll` | Get many card comments |

### Checklist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new checklist |
| Delete | `delete` | Delete a checklist |
| Get | `get` | Get the data of a checklist |
| Get Many | `getAll` | Returns many checklists for the card |

### Checklistitem Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a checklist item |
| Get | `get` | Get a checklist item |
| Update | `update` | Update a checklist item |

### List Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new list |
| Delete | `delete` | Delete a list |
| Get | `get` | Get the data of a list |
| Get Many | `getAll` | Get many board lists |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | card | ✗ | Resource to operate on |  |

**Resource options:**

* **Board** (`board`)
* **Card** (`card`)
* **Card Comment** (`cardComment`)
* **Checklist** (`checklist`)
* **Checklist Item** (`checklistItem`)
* **List** (`list`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a new board |  |

**Operation options:**

* **Create** (`create`) - Create a new board
* **Delete** (`delete`) - Delete a board
* **Get** (`get`) - Get the data of a board
* **Get Many** (`getAll`) - Get many user boards

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ | The title of the board | e.g. My board |  |
| Owner Name or ID | `owner` | options |  | ✓ | The user ID in Wekan. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to set the board active | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Active | `isActive` | boolean | False | Whether to set the board active |
| Admin | `isAdmin` | boolean | False | Whether to set the owner an admin of the board |
| Color | `color` | options |  | The color of the board |
| Comment Only | `isCommentOnly` | boolean | False | Whether to enable comments |
| No Comments | `isNoComments` | boolean | False | Whether to disable comments |
| Permission | `permission` | options | private | Set the board permission |
| Worker | `isWorker` | boolean | False | Whether to only move cards, assign himself to card and comment |

</details>

| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that list belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list to create card in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Title | `title` | string |  | ✓ | The title of the card | e.g. My card |  |
| Swimlane Name or ID | `swimlaneId` | options |  | ✓ | The swimlane ID of the new card. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Author Name or ID | `authorId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The new list of assignee IDs attached to the card. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Names or IDs | `assignees` | multiOptions | [] | The new list of assignee IDs attached to the card. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | The new description of the card |
| Member Names or IDs | `members` | multiOptions | [] | The new list of member IDs attached to the card. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Author Name or ID | `authorId` | options |  | ✓ | The user who posted the comment. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Comment | `comment` | string |  | ✓ | The comment text |  |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board where the card is in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card to add checklist to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Title | `title` | string |  | ✓ | The title of the checklist to add |  |
| Items | `items` | string | [] | ✗ | Items to be added to the checklist |  |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board the list should be created in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Title | `title` | string |  | ✓ | The title of the list | e.g. My list |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board ID | `boardId` | string |  | ✓ | The ID of the board to delete |  |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that list belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card to delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Comment Name or ID | `commentId` | options |  | ✓ | The ID of the comment to delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card that checklist belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Checklist Name or ID | `checklistId` | options |  | ✓ | The ID of the checklist to delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card that checklistItem belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Checklist Name or ID | `checklistId` | options |  | ✓ | The ID of the checklistItem that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Checklist Item Name or ID | `checklistItemId` | options |  | ✓ | The ID of the checklistItem item to get. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that list belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list to delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board ID | `boardId` | string |  | ✓ | The ID of the board to get |  |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that list belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card ID | `cardId` | string |  | ✓ | The ID of the card to get |  |
| Board ID | `boardId` | string |  | ✓ | The ID of the board that card belongs to |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Comment ID | `commentId` | string |  | ✓ | The ID of the comment to get |  |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card that checklist belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Checklist Name or ID | `checklistId` | options |  | ✓ | The ID of the checklist to get. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card that checklistItem belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Checklist ID | `checklistId` | string |  | ✓ | The ID of the checklistItem that card belongs to |  |
| Checklist Item Name or ID | `checklistItemId` | options |  | ✓ | The ID of the checklistItem item to get. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that list belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List ID | `listId` | string |  | ✓ | The ID of the list to get |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User Name or ID | `IdUser` | options |  | ✓ | The ID of the user that boards are attached. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that list belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| From Object | `fromObject` | options |  | ✓ |  |  |

**From Object options:**

* **List** (`list`)
* **Swimlane** (`swimlane`)

| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Swimlane Name or ID | `swimlaneId` | options |  | ✗ | The ID of the swimlane that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that list belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card to get checklists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Board Name or ID | `boardId` | options |  | ✓ | ID of the board where the lists are in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that list belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card to update. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Update the owner of the card. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Author Name or ID | `authorId` | options |  | Update the owner of the card. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Assignee Names or IDs | `assignees` | multiOptions | [] | The new list of assignee IDs attached to the card. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Color | `color` | options |  | The new color of the card |
| Description | `description` | string |  | The new description of the card |
| Due At | `dueAt` | dateTime |  | The new due at field of the card |
| End At | `endAt` | dateTime |  | The new end at field of the card |
| Label IDs | `labelIds` | string |  | The label IDs attached to the card |
| List Name or ID | `listId` | options |  | The new list ID of the card (move operation). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Member Names or IDs | `members` | multiOptions | [] | The new list of member IDs attached to the card. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Over Time | `isOverTime` | boolean | False | The new over time field of the card |
| Parent Name or ID | `parentId` | options |  | The parent of the card. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Received At | `receivedAt` | dateTime |  | The new received at field of the card |
| Sort | `sort` | number | 0 | The internally used sort value of a card |
| Spent Time | `spentTime` | number |  | The new spent time field of the card |
| Start At | `startAt` | dateTime |  | The new start at field of the card |
| Swimlane Name or ID | `swimlaneId` | options |  | The new swimlane ID of the card. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Title | `title` | string |  | The new title of the card |

</details>

| Board Name or ID | `boardId` | options |  | ✓ | The ID of the board that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Name or ID | `listId` | options |  | ✓ | The ID of the list that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Card Name or ID | `cardId` | options |  | ✓ | The ID of the card that checklistItem belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| CheckList Name or ID | `checklistId` | options |  | ✓ | The ID of the checklistItem that card belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Checklist Item Name or ID | `checklistItemId` | options |  | ✓ | The ID of the checklistItem item to update. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The new title for the checklistItem item | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Title | `title` | string |  | The new title for the checklistItem item |
| Finished | `isFinished` | boolean | False | Whether the item is checked |

</details>


---

## Load Options Methods

- `getUsers`

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
node: wekan
displayName: Wekan
description: Consume Wekan API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: wekanApi
  required: true
operations:
- id: create
  name: Create
  description: Create a new board
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The title of the board
    placeholder: My board
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - list
    typeInfo: &id002
      type: string
      displayName: Title
      name: title
  - id: owner
    name: Owner Name or ID
    type: options
    default: ''
    required: true
    description: The user ID in Wekan. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - board
    typeInfo:
      type: options
      displayName: Owner Name or ID
      name: owner
      typeOptions:
        loadOptionsMethod: getUsers
      possibleValues: []
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that list belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - list
    typeInfo: &id004
      type: options
      displayName: Board Name or ID
      name: boardId
      typeOptions:
        loadOptionsMethod: getBoards
      possibleValues: []
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list to create card in. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - list
    typeInfo: &id006
      type: string
      displayName: List ID
      name: listId
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The title of the card
    placeholder: My card
    validation: *id001
    typeInfo: *id002
  - id: swimlaneId
    name: Swimlane Name or ID
    type: options
    default: ''
    required: true
    description: The swimlane ID of the new card. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id017
      displayOptions:
        show:
          fromObject:
          - swimlane
          operation:
          - getAll
          resource:
          - card
    typeInfo: &id018
      type: options
      displayName: Swimlane Name or ID
      name: swimlaneId
      typeOptions:
        loadOptionsMethod: getSwimlanes
      possibleValues: []
  - id: authorId
    name: Author Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - cardComment
    typeInfo: &id008
      type: options
      displayName: Author Name or ID
      name: authorId
      typeOptions:
        loadOptionsMethod: getUsers
      possibleValues: []
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - checklistItem
    typeInfo: &id010
      type: options
      displayName: Card Name or ID
      name: cardId
      typeOptions:
        loadOptionsMethod: getCards
      possibleValues: []
  - id: authorId
    name: Author Name or ID
    type: options
    default: ''
    required: true
    description: The user who posted the comment. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
  - id: comment
    name: Comment
    type: string
    default: ''
    required: true
    description: The comment text
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - cardComment
    typeInfo:
      type: string
      displayName: Comment
      name: comment
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board where the card is in. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card to add checklist to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The title of the checklist to add
    validation: *id001
    typeInfo: *id002
  - id: items
    name: Items
    type: string
    default: []
    required: false
    description: Items to be added to the checklist
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - checklist
    typeInfo:
      type: string
      displayName: Items
      name: items
      typeOptions:
        multipleValues: true
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board the list should be created in. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The title of the list
    placeholder: My list
    validation: *id001
    typeInfo: *id002
- id: delete
  name: Delete
  description: Delete a board
  params:
  - id: boardId
    name: Board ID
    type: string
    default: ''
    required: true
    description: The ID of the board to delete
    validation: *id003
    typeInfo: *id004
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that list belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card to delete. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: commentId
    name: Comment Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the comment to delete. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id013
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - cardComment
    typeInfo: &id014
      type: string
      displayName: Comment ID
      name: commentId
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card that checklist belongs to. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: checklistId
    name: Checklist Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the checklist to delete. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - checklistItem
    typeInfo: &id012
      type: options
      displayName: CheckList Name or ID
      name: checklistId
      typeOptions:
        loadOptionsMethod: getChecklists
      possibleValues: []
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card that checklistItem belongs to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: checklistId
    name: Checklist Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the checklistItem that card belongs to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id011
    typeInfo: *id012
  - id: checklistItemId
    name: Checklist Item Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the checklistItem item to get. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id015
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - checklistItem
    typeInfo: &id016
      type: options
      displayName: Checklist Item Name or ID
      name: checklistItemId
      typeOptions:
        loadOptionsMethod: getChecklistItems
      possibleValues: []
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that list belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list to delete. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
- id: get
  name: Get
  description: Get the data of a board
  params:
  - id: boardId
    name: Board ID
    type: string
    default: ''
    required: true
    description: The ID of the board to get
    validation: *id003
    typeInfo: *id004
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that list belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card ID
    type: string
    default: ''
    required: true
    description: The ID of the card to get
    validation: *id009
    typeInfo: *id010
  - id: boardId
    name: Board ID
    type: string
    default: ''
    required: true
    description: The ID of the board that card belongs to
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: The ID of the comment to get
    validation: *id013
    typeInfo: *id014
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card that checklist belongs to. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: checklistId
    name: Checklist Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the checklist to get. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id011
    typeInfo: *id012
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card that checklistItem belongs to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: checklistId
    name: Checklist ID
    type: string
    default: ''
    required: true
    description: The ID of the checklistItem that card belongs to
    validation: *id011
    typeInfo: *id012
  - id: checklistItemId
    name: Checklist Item Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the checklistItem item to get. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id015
    typeInfo: *id016
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that list belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: The ID of the list to get
    validation: *id005
    typeInfo: *id006
- id: getAll
  name: Get Many
  description: Get many user boards
  params:
  - id: IdUser
    name: User Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the user that boards are attached. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - board
    typeInfo:
      type: options
      displayName: User Name or ID
      name: IdUser
      typeOptions:
        loadOptionsMethod: getUsers
      possibleValues: []
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id019
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - list
    typeInfo: &id020
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id021
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - list
          returnAll:
          - false
    typeInfo: &id022
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 200
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that list belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: fromObject
    name: From Object
    type: options
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - card
    typeInfo:
      type: options
      displayName: From Object
      name: fromObject
      possibleValues:
      - value: list
        name: List
        description: ''
      - value: swimlane
        name: Swimlane
        description: ''
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: swimlaneId
    name: Swimlane Name or ID
    type: options
    default: ''
    required: false
    description: The ID of the swimlane that card belongs to. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id017
    typeInfo: *id018
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id021
    typeInfo: *id022
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id021
    typeInfo: *id022
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that list belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card to get checklists. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id021
    typeInfo: *id022
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: ID of the board where the lists are in. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id021
    typeInfo: *id022
- id: update
  name: Update
  description: Update a card
  params:
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that list belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card to update. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the board that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the list that card belongs to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the card that checklistItem belongs to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: checklistId
    name: CheckList Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the checklistItem that card belongs to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id011
    typeInfo: *id012
  - id: checklistItemId
    name: Checklist Item Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the checklistItem item to update. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id015
    typeInfo: *id016
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
  - field: title
    text: My board
  - field: additionalFields
    text: Add Field
  - field: title
    text: My card
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: title
    text: My list
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
  "$id": "https://n8n.io/schemas/nodes/wekan.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Wekan Node",
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
            "board",
            "card",
            "cardComment",
            "checklist",
            "checklistItem",
            "list"
          ],
          "default": "card"
        },
        "operation": {
          "description": "Create a new list",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll"
          ],
          "default": "create"
        },
        "title": {
          "description": "The title of the list",
          "type": "string",
          "default": "",
          "examples": [
            "My list"
          ]
        },
        "owner": {
          "description": "The user ID in Wekan. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The new list of assignee IDs attached to the card. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "boardId": {
          "description": "ID of the board where the lists are in. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "IdUser": {
          "description": "The ID of the user that boards are attached. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
          "default": 100
        },
        "listId": {
          "description": "The ID of the list to get",
          "type": "string",
          "default": ""
        },
        "swimlaneId": {
          "description": "The ID of the swimlane that card belongs to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "authorId": {
          "description": "The user who posted the comment. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "cardId": {
          "description": "The ID of the card that checklistItem belongs to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "fromObject": {
          "description": "",
          "type": "string",
          "enum": [
            "list",
            "swimlane"
          ],
          "default": ""
        },
        "updateFields": {
          "description": "The new title for the checklistItem item",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "comment": {
          "description": "The comment text",
          "type": "string",
          "default": ""
        },
        "commentId": {
          "description": "The ID of the comment to get",
          "type": "string",
          "default": ""
        },
        "items": {
          "description": "Items to be added to the checklist",
          "type": "string",
          "default": []
        },
        "checklistId": {
          "description": "The ID of the checklistItem that card belongs to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "checklistItemId": {
          "description": "The ID of the checklistItem item to update. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
      "name": "wekanApi",
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
