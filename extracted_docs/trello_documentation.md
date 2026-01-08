---
title: "Node: Trello"
slug: "node-trello"
version: "1"
updated: "2026-01-08"
summary: "Create, change and delete boards and cards"
node_type: "regular"
group: "['transform']"
---

# Node: Trello

**Purpose.** Create, change and delete boards and cards
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:trello.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **trelloApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `trelloApi` | ✓ | - |

---

## Operations

### Attachment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new attachment for a card |
| Delete | `delete` | Delete an attachment |
| Get | `get` | Get the data of an attachment |
| Get Many | `getAll` | Returns many attachments for the card |

### Board Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new board |
| Delete | `delete` | Delete a board |
| Get | `get` | Get the data of a board |
| Update | `update` | Update a board |

### Boardmember Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add member to board using member ID |
| Get Many | `getAll` | Get many members of a board |
| Invite | `invite` | Invite a new member to a board via email |
| Remove | `remove` | Remove member from board using member ID |

### Card Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new card |
| Delete | `delete` | Delete a card |
| Get | `get` | Get the data of a card |
| Update | `update` | Update a card |

### Cardcomment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a comment on a card |
| Delete | `delete` | Delete a comment from a card |
| Update | `update` | Update a comment on a card |

### Checklist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new checklist |
| Create Checklist Item | `createCheckItem` | Create a checklist item |
| Delete | `delete` | Delete a checklist |
| Delete Checklist Item | `deleteCheckItem` | Delete a checklist item |
| Get | `get` | Get the data of a checklist |
| Get Checklist Items | `getCheckItem` | Get a specific checklist on a card |
| Get Completed Checklist Items | `completedCheckItems` | Get the completed checklist items on a card |
| Get Many | `getAll` | Returns many checklists for the card |
| Update Checklist Item | `updateCheckItem` | Update an item in a checklist on a card |

### Label Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add to Card | `addLabel` | Add a label to a card |
| Create | `create` | Create a new label |
| Delete | `delete` | Delete a label |
| Get | `get` | Get the data of a label |
| Get Many | `getAll` | Returns many labels for the board |
| Remove From Card | `removeLabel` | Remove a label from a card |
| Update | `update` | Update a label |

### List Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Archive | `archive` | Archive/Unarchive a list |
| Create | `create` | Create a new list |
| Get | `get` | Get the data of a list |
| Get Cards | `getCards` | Get all the cards in a list |
| Get Many | `getAll` | Get many lists |
| Update | `update` | Update a list |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | card | ✗ | Resource to operate on |  |

**Resource options:**

* **Attachment** (`attachment`)
* **Board** (`board`)
* **Board Member** (`boardMember`)
* **Card** (`card`)
* **Card Comment** (`cardComment`)
* **Checklist** (`checklist`)
* **Label** (`label`)
* **List** (`list`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Create a new attachment for a card |  |

**Operation options:**

* **Create** (`create`) - Create a new attachment for a card
* **Delete** (`delete`) - Delete an attachment
* **Get** (`get`) - Get the data of an attachment
* **Get Many** (`getAll`) - Returns many attachments for the card

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Card ID | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Source URL | `url` | string |  | ✓ | The URL of the attachment to add | url |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The MIME type of the attachment to add | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| MIME Type | `mimeType` | string |  | The MIME type of the attachment to add |
| Name | `name` | string |  | The name of the attachment to add |

</details>

| Name | `name` | string |  | ✓ | The name of the board | e.g. My board |  |
| Description | `description` | string |  | ✗ | The description of the board |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Determines the type of card aging that should take place on the board if card aging is enabled | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Aging | `prefs_cardAging` | options | regular | Determines the type of card aging that should take place on the board if card aging is enabled |
| Background | `prefs_background` | string | blue | The ID of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey |
| Comments | `prefs_comments` | options | members | Who can comment on cards on this board |
| Covers | `prefs_cardCovers` | boolean | True | Whether card covers are enabled |
| Invitations | `prefs_invitations` | options | members | Determines what types of members can invite users to join |
| Keep From Source | `keepFromSource` | string | none | To keep cards from the original board pass in the value cards |
| Labels | `defaultLabels` | boolean | True | Whether to use the default set of labels |
| Lists | `defaultLists` | boolean | True | Whether to add the default set of lists to a board(To Do, Doing, Done).It is ignored if idBoardSource is provided |
| Organization ID | `idOrganization` | string |  | The ID or name of the team the board should belong to |
| Permission Level | `prefs_permissionLevel` | options | private | The permissions level of the board |
| Power Ups | `powerUps` | options | all | The Power-Ups that should be enabled on the new board |
| Self Join | `prefs_selfJoin` | boolean | True | Whether users can join the boards themselves or whether they have to be invited |
| Source IDs | `idBoardSource` | string |  | The ID of a board to copy into the new board |
| Voting | `prefs_voting` | options | disabled | Who can vote on this board |

</details>

| List ID | `listId` | string |  | ✓ | The ID of the list to create card in |  |
| Name | `name` | string |  | ✓ | The name of the card | e.g. My card |  |
| Description | `description` | string |  | ✗ | The description of the card |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | A due date for the card | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Due Date | `due` | dateTime |  | A due date for the card |
| Due Complete | `dueComplete` | boolean | False | Whether the card is completed |
| Position | `pos` | string | bottom | The position of the new card. top, bottom, or a positive float. |
| Member IDs | `idMembers` | string |  | Comma-separated list of member IDs to add to the card |
| Label IDs | `idLabels` | string |  | Comma-separated list of label IDs to add to the card |
| URL Source | `urlSource` | string |  | A source URL to attach to card |
| Source ID | `idCardSource` | string |  | The ID of a card to copy into the new card |
| Keep From Source | `keepFromSource` | string | all | If using idCardSource you can specify which properties to copy over. all or comma-separated list of: attachments, checklists, comments, due, labels, members, stickers. |

</details>

| Card | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Text | `text` | string |  | ✓ | Text of the comment |  |
| Card | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Name | `name` | string |  | ✓ | The URL of the checklist to add |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The ID of a source checklist to copy into the new one | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| ID Of Checklist Source | `idChecklistSource` | string |  | The ID of a source checklist to copy into the new one |
| Position | `pos` | string |  | The position of the checklist on the card. One of: top, bottom, or a positive number. |

</details>

| Board | `boardId` | resourceLocator |  | ✓ | The ID of the board | e.g. Select a Board... |  |
| Name | `name` | string |  | ✓ | Name for the label |  |
| Color | `color` | options | null | ✓ | The color for the label |  |

**Color options:**

* **Black** (`black`)
* **Blue** (`blue`)
* **Green** (`green`)
* **Lime** (`lime`)
* **Null** (`null`)
* **Orange** (`orange`)
* **Pink** (`pink`)
* **Purple** (`purple`)
* **Red** (`red`)
* **Sky** (`sky`)
* **Yellow** (`yellow`)

| Board ID | `idBoard` | string |  | ✓ | The ID of the board the list should be created in |  |
| Name | `name` | string |  | ✓ | The name of the list | e.g. My list |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the list to copy into the new list | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| List Source | `idListSource` | string |  | ID of the list to copy into the new list |
| Position | `pos` | string | bottom | The position of the new list. top, bottom, or a positive float. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Card ID | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Attachment ID | `id` | string |  | ✓ | The ID of the attachment to delete |  |
| Board | `id` | resourceLocator |  | ✓ | The ID of the board | e.g. Select a Board... |  |
| Card | `id` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Card | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Comment ID | `commentId` | string |  | ✓ | The ID of the comment to delete |  |
| Card | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Checklist ID | `id` | string |  | ✓ | The ID of the checklist to delete |  |
| Label ID | `id` | string |  | ✓ | The ID of the label to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Card ID | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Attachment ID | `id` | string |  | ✓ | The ID of the attachment to get |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list of fields. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list of fields. |

</details>

| Board | `id` | resourceLocator |  | ✓ | The ID of the board | e.g. Select a Board... |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, URL. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, URL. |
| Plugin Data | `pluginData` | boolean | False | Whether to include pluginData on the card with the response |

</details>

| Card | `id` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl, url. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl, url. |
| Board | `board` | boolean | False | Whether to return the board object the card is on |
| Board Fields | `board_fields` | string | all | Fields to return. Either "all" or a comma-separated list: name, desc, descData, closed, idOrganization, pinned, url, prefs. |
| Custom Field Items | `customFieldItems` | boolean | False | Whether to include the customFieldItems |
| Members | `members` | boolean | False | Whether to return member objects for members on the card |
| Member Fields | `member_fields` | string | all | Fields to return. Either "all" or a comma-separated list: avatarHash, fullName, initials, username. |
| Plugin Data | `pluginData` | boolean | False | Whether to include pluginData on the card with the response |
| Stickers | `stickers` | boolean | False | Whether to include sticker models with the response |
| Sticker Fields | `sticker_fields` | string | all | Fields to return. Either "all" or a comma-separated list of sticker fields. |

</details>

| Checklist ID | `id` | string |  | ✓ | The ID of the checklist to get |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list of fields. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list of fields. |

</details>

| Label ID | `id` | string |  | ✓ | Get information about a label by ID |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list of fields. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list of fields. |

</details>

| List ID | `id` | string |  | ✓ | The ID of the list to get |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list of fields. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list of fields. |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Card ID | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list of fields. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list of fields. |

</details>

| Board ID | `id` | string |  | ✓ | The ID of the board to get members from |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:∞ |
| Card | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list of fields. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list of fields. |

</details>

| Board | `boardId` | resourceLocator |  | ✓ | The ID of the board | e.g. Select a Board... |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list of fields. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list of fields. |

</details>

| Board ID | `id` | string |  | ✓ | The ID of the board |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:∞ |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list of fields. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list of fields. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board | `id` | resourceLocator |  | ✓ | The ID of the board | e.g. Select a Board... |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Whether the board is closed | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Closed | `closed` | boolean | False | Whether the board is closed |
| Description | `desc` | string |  | New description of the board |
| Name | `name` | string |  | New name of the board |
| Organization ID | `idOrganization` | string |  | The ID of the team the board should be moved to |
| Subscribed | `subscribed` | boolean | False | Whether the acting user is subscribed to the board |

</details>

| Card | `id` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The ID of the image attachment the card should use as its cover, or null for none | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment Cover | `idAttachmentCover` | string |  | The ID of the image attachment the card should use as its cover, or null for none |
| Board ID | `idBoard` | string |  | The ID of the board the card should be on |
| Closed | `closed` | boolean | False | Whether the board is closed |
| Description | `desc` | string |  | New description of the board |
| Due Date | `due` | dateTime |  | A due date for the card |
| Due Complete | `dueComplete` | boolean | False | Whether the card is completed |
| Label IDs | `idLabels` | string |  | Comma-separated list of label IDs to set on card |
| List ID | `idList` | string |  | The ID of the list the card should be in |
| Member IDs | `idMembers` | string |  | Comma-separated list of member IDs to set on card |
| Name | `name` | string |  | New name of the board |
| Position | `pos` | string | bottom | The position of the card. top, bottom, or a positive float. |
| Subscribed | `subscribed` | boolean | False | Whether the acting user is subscribed to the board |

</details>

| Card | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| Comment ID | `commentId` | string |  | ✓ | The ID of the comment to delete |  |
| Text | `text` | string |  | ✓ | Text of the comment |  |
| Label ID | `id` | string |  | ✓ | The ID of the label to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Name of the label | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | Name of the label |
| Color | `color` | options | null | The color for the label |

</details>

| List ID | `id` | string |  | ✓ | The ID of the list to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of a board the list should be moved to | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Board ID | `idBoard` | string |  | ID of a board the list should be moved to |
| Closed | `closed` | boolean | False | Whether the list is closed |
| Name | `name` | string |  | New name of the list |
| Position | `pos` | string | bottom | The position of the list. top, bottom, or a positive float. |
| Subscribed | `subscribed` | boolean | False | Whether the acting user is subscribed to the list |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board ID | `id` | string |  | ✓ | The ID of the board to add member to |  |
| Member ID | `idMember` | string |  | ✓ | The ID of the member to add to the board |  |
| Type | `type` | options | normal | ✓ | Invite as normal member |  |

**Type options:**

* **Normal** (`normal`) - Invite as normal member
* **Admin** (`admin`) - Invite as admin
* **Observer** (`observer`) - Invite as observer (Trello premium feature)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to allow organization admins to add multi-board guests onto a board | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Allow Billable Guest | `allowBillableGuest` | boolean | False | Whether to allow organization admins to add multi-board guests onto a board |

</details>


### Invite parameters (`invite`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board ID | `id` | string |  | ✓ | The ID of the board to invite member to |  |
| Email | `email` | string |  | ✓ | The ID of the board to update | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Invite as normal member | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Type | `type` | options | normal | Invite as normal member |
| Full Name | `fullName` | string |  | The full name of the user to add as a member of the board. Must have a length of at least 1 and cannot begin nor end with a space. |

</details>


### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board ID | `id` | string |  | ✓ | The ID of the board to remove member from |  |
| Member ID | `idMember` | string |  | ✓ | The ID of the member to remove from the board |  |

### Create Checklist Item parameters (`createCheckItem`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Checklist ID | `checklistId` | string |  | ✓ | The ID of the checklist to update |  |
| Name | `name` | string |  | ✓ | The name of the new check item on the checklist |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether the check item is already checked when created | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Checked | `checked` | boolean | False | Whether the check item is already checked when created |
| Position | `pos` | string |  | The position of the checklist on the card. One of: top, bottom, or a positive number. |

</details>


### Delete Checklist Item parameters (`deleteCheckItem`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Card | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| CheckItem ID | `checkItemId` | string |  | ✓ | The ID of the checklist item to delete |  |

### Get Checklist Items parameters (`getCheckItem`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Card | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| CheckItem ID | `checkItemId` | string |  | ✓ | The ID of the checklist item to get |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list of fields. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list of fields. |

</details>


### Get Completed Checklist Items parameters (`completedCheckItems`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list of: "idCheckItem", "state". | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list of: "idCheckItem", "state". |

</details>


### Update Checklist Item parameters (`updateCheckItem`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Card | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Select a Card... |  |
| CheckItem ID | `checkItemId` | string |  | ✓ | The ID of the checklist item to update |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The new name for the checklist item | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | The new name for the checklist item |
| State | `state` | options | complete |  |
| Checklist ID | `checklistId` | string |  | The ID of the checklist this item is in |
| Position | `pos` | string |  | The position of the checklist on the card. One of: top, bottom, or a positive number. |

</details>


### Add to Card parameters (`addLabel`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Card ID | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Choose... |  |
| Label ID | `id` | string |  | ✓ | The ID of the label to add |  |

### Remove From Card parameters (`removeLabel`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Card ID | `cardId` | resourceLocator |  | ✓ | The ID of the card | e.g. Choose... |  |
| Label ID | `id` | string |  | ✓ | The ID of the label to remove |  |

### Archive parameters (`archive`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List ID | `id` | string |  | ✓ | The ID of the list to archive or unarchive |  |
| Archive | `archive` | boolean | False | ✗ | Whether the list should be archived or unarchived |  |

### Get Cards parameters (`getCards`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List ID | `id` | string |  | ✓ | The ID of the list to get cards |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:∞ |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to return. Either "all" or a comma-separated list of fields. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string | all | Fields to return. Either "all" or a comma-separated list of fields. |

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
node: trello
displayName: Trello
description: Create, change and delete boards and cards
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: trelloApi
  required: true
operations:
- id: create
  name: Create
  description: Create a new attachment for a card
  params:
  - id: cardId
    name: Card ID
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - addLabel
          - removeLabel
          resource:
          - label
    typeInfo: &id006
      type: resourceLocator
      displayName: Card ID
      name: cardId
  - id: url
    name: Source URL
    type: string
    default: ''
    required: true
    description: The URL of the attachment to add
    validation:
      required: true
      format: url
      displayOptions:
        show:
          operation:
          - create
          resource:
          - attachment
    typeInfo:
      type: string
      displayName: Source URL
      name: url
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the board
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
      displayName: Name
      name: name
  - id: description
    name: Description
    type: string
    default: ''
    required: false
    description: The description of the board
    validation: &id003
      displayOptions:
        show:
          operation:
          - create
          resource:
          - card
    typeInfo: &id004
      type: string
      displayName: Description
      name: description
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: The ID of the list to create card in
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - card
    typeInfo:
      type: string
      displayName: List ID
      name: listId
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the card
    placeholder: My card
    validation: *id001
    typeInfo: *id002
  - id: description
    name: Description
    type: string
    default: ''
    required: false
    description: The description of the card
    validation: *id003
    typeInfo: *id004
  - id: cardId
    name: Card
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id005
    typeInfo: *id006
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: Text of the comment
    validation: &id017
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - cardComment
    typeInfo: &id018
      type: string
      displayName: Text
      name: text
  - id: cardId
    name: Card
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id005
    typeInfo: *id006
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The URL of the checklist to add
    validation: *id001
    typeInfo: *id002
  - id: boardId
    name: Board
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the board
    placeholder: Select a Board...
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - create
          - getAll
          resource:
          - label
    typeInfo: &id010
      type: resourceLocator
      displayName: Board
      name: boardId
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name for the label
    validation: *id001
    typeInfo: *id002
  - id: color
    name: Color
    type: options
    default: 'null'
    required: true
    description: The color for the label
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - label
    typeInfo:
      type: options
      displayName: Color
      name: color
      possibleValues:
      - value: black
        name: Black
        description: ''
      - value: blue
        name: Blue
        description: ''
      - value: green
        name: Green
        description: ''
      - value: lime
        name: Lime
        description: ''
      - value: 'null'
        name: 'Null'
        description: ''
      - value: orange
        name: Orange
        description: ''
      - value: pink
        name: Pink
        description: ''
      - value: purple
        name: Purple
        description: ''
      - value: red
        name: Red
        description: ''
      - value: sky
        name: Sky
        description: ''
      - value: yellow
        name: Yellow
        description: ''
  - id: idBoard
    name: Board ID
    type: string
    default: ''
    required: true
    description: The ID of the board the list should be created in
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - list
    typeInfo:
      type: string
      displayName: Board ID
      name: idBoard
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the list
    placeholder: My list
    validation: *id001
    typeInfo: *id002
- id: delete
  name: Delete
  description: Delete an attachment
  params:
  - id: cardId
    name: Card ID
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id005
    typeInfo: *id006
  - id: id
    name: Attachment ID
    type: string
    default: ''
    required: true
    description: The ID of the attachment to delete
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - list
    typeInfo: &id008
      type: string
      displayName: List ID
      name: id
  - id: id
    name: Board
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the board
    placeholder: Select a Board...
    validation: *id007
    typeInfo: *id008
  - id: id
    name: Card
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id007
    typeInfo: *id008
  - id: cardId
    name: Card
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id005
    typeInfo: *id006
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: The ID of the comment to delete
    validation: &id015
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - cardComment
    typeInfo: &id016
      type: string
      displayName: Comment ID
      name: commentId
  - id: cardId
    name: Card
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id005
    typeInfo: *id006
  - id: id
    name: Checklist ID
    type: string
    default: ''
    required: true
    description: The ID of the checklist to delete
    validation: *id007
    typeInfo: *id008
  - id: id
    name: Label ID
    type: string
    default: ''
    required: true
    description: The ID of the label to delete
    validation: *id007
    typeInfo: *id008
- id: get
  name: Get
  description: Get the data of an attachment
  params:
  - id: cardId
    name: Card ID
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id005
    typeInfo: *id006
  - id: id
    name: Attachment ID
    type: string
    default: ''
    required: true
    description: The ID of the attachment to get
    validation: *id007
    typeInfo: *id008
  - id: id
    name: Board
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the board
    placeholder: Select a Board...
    validation: *id007
    typeInfo: *id008
  - id: id
    name: Card
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id007
    typeInfo: *id008
  - id: id
    name: Checklist ID
    type: string
    default: ''
    required: true
    description: The ID of the checklist to get
    validation: *id007
    typeInfo: *id008
  - id: id
    name: Label ID
    type: string
    default: ''
    required: true
    description: Get information about a label by ID
    validation: *id007
    typeInfo: *id008
  - id: id
    name: List ID
    type: string
    default: ''
    required: true
    description: The ID of the list to get
    validation: *id007
    typeInfo: *id008
- id: getAll
  name: Get Many
  description: Returns many attachments for the card
  params:
  - id: cardId
    name: Card ID
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id005
    typeInfo: *id006
  - id: id
    name: Board ID
    type: string
    default: ''
    required: true
    description: The ID of the board to get members from
    validation: *id007
    typeInfo: *id008
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
    default: 20
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
  - id: cardId
    name: Card
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id005
    typeInfo: *id006
  - id: boardId
    name: Board
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the board
    placeholder: Select a Board...
    validation: *id009
    typeInfo: *id010
  - id: id
    name: Board ID
    type: string
    default: ''
    required: true
    description: The ID of the board
    validation: *id007
    typeInfo: *id008
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
    default: 20
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
- id: update
  name: Update
  description: Update a board
  params:
  - id: id
    name: Board
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the board
    placeholder: Select a Board...
    validation: *id007
    typeInfo: *id008
  - id: id
    name: Card
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id007
    typeInfo: *id008
  - id: cardId
    name: Card
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id005
    typeInfo: *id006
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: The ID of the comment to delete
    validation: *id015
    typeInfo: *id016
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: Text of the comment
    validation: *id017
    typeInfo: *id018
  - id: id
    name: Label ID
    type: string
    default: ''
    required: true
    description: The ID of the label to update
    validation: *id007
    typeInfo: *id008
  - id: id
    name: List ID
    type: string
    default: ''
    required: true
    description: The ID of the list to update
    validation: *id007
    typeInfo: *id008
- id: add
  name: Add
  description: Add member to board using member ID
  params:
  - id: id
    name: Board ID
    type: string
    default: ''
    required: true
    description: The ID of the board to add member to
    validation: *id007
    typeInfo: *id008
  - id: idMember
    name: Member ID
    type: string
    default: ''
    required: true
    description: The ID of the member to add to the board
    validation: &id019
      required: true
      displayOptions:
        show:
          operation:
          - remove
          resource:
          - boardMember
    typeInfo: &id020
      type: string
      displayName: Member ID
      name: idMember
  - id: type
    name: Type
    type: options
    default: normal
    required: true
    description: Invite as normal member
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - add
          resource:
          - boardMember
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: normal
        name: Normal
        description: Invite as normal member
      - value: admin
        name: Admin
        description: Invite as admin
      - value: observer
        name: Observer
        description: Invite as observer (Trello premium feature)
- id: invite
  name: Invite
  description: Invite a new member to a board via email
  params:
  - id: id
    name: Board ID
    type: string
    default: ''
    required: true
    description: The ID of the board to invite member to
    validation: *id007
    typeInfo: *id008
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The ID of the board to update
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - invite
          resource:
          - boardMember
    typeInfo:
      type: string
      displayName: Email
      name: email
- id: remove
  name: Remove
  description: Remove member from board using member ID
  params:
  - id: id
    name: Board ID
    type: string
    default: ''
    required: true
    description: The ID of the board to remove member from
    validation: *id007
    typeInfo: *id008
  - id: idMember
    name: Member ID
    type: string
    default: ''
    required: true
    description: The ID of the member to remove from the board
    validation: *id019
    typeInfo: *id020
- id: createCheckItem
  name: Create Checklist Item
  description: Create a checklist item
  params:
  - id: checklistId
    name: Checklist ID
    type: string
    default: ''
    required: true
    description: The ID of the checklist to update
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - createCheckItem
          resource:
          - checklist
    typeInfo:
      type: string
      displayName: Checklist ID
      name: checklistId
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the new check item on the checklist
    validation: *id001
    typeInfo: *id002
- id: deleteCheckItem
  name: Delete Checklist Item
  description: Delete a checklist item
  params:
  - id: cardId
    name: Card
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id005
    typeInfo: *id006
  - id: checkItemId
    name: CheckItem ID
    type: string
    default: ''
    required: true
    description: The ID of the checklist item to delete
    validation: &id021
      required: true
      displayOptions:
        show:
          operation:
          - updateCheckItem
          resource:
          - checklist
    typeInfo: &id022
      type: string
      displayName: CheckItem ID
      name: checkItemId
- id: getCheckItem
  name: Get Checklist Items
  description: Get a specific checklist on a card
  params:
  - id: cardId
    name: Card
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id005
    typeInfo: *id006
  - id: checkItemId
    name: CheckItem ID
    type: string
    default: ''
    required: true
    description: The ID of the checklist item to get
    validation: *id021
    typeInfo: *id022
- id: completedCheckItems
  name: Get Completed Checklist Items
  description: Get the completed checklist items on a card
  params: []
- id: updateCheckItem
  name: Update Checklist Item
  description: Update an item in a checklist on a card
  params:
  - id: cardId
    name: Card
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Select a Card...
    validation: *id005
    typeInfo: *id006
  - id: checkItemId
    name: CheckItem ID
    type: string
    default: ''
    required: true
    description: The ID of the checklist item to update
    validation: *id021
    typeInfo: *id022
- id: addLabel
  name: Add to Card
  description: Add a label to a card
  params:
  - id: cardId
    name: Card ID
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Choose...
    validation: *id005
    typeInfo: *id006
  - id: id
    name: Label ID
    type: string
    default: ''
    required: true
    description: The ID of the label to add
    validation: *id007
    typeInfo: *id008
- id: removeLabel
  name: Remove From Card
  description: Remove a label from a card
  params:
  - id: cardId
    name: Card ID
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the card
    placeholder: Choose...
    validation: *id005
    typeInfo: *id006
  - id: id
    name: Label ID
    type: string
    default: ''
    required: true
    description: The ID of the label to remove
    validation: *id007
    typeInfo: *id008
- id: archive
  name: Archive
  description: Archive/Unarchive a list
  params:
  - id: id
    name: List ID
    type: string
    default: ''
    required: true
    description: The ID of the list to archive or unarchive
    validation: *id007
    typeInfo: *id008
  - id: archive
    name: Archive
    type: boolean
    default: false
    required: false
    description: Whether the list should be archived or unarchived
    validation:
      displayOptions:
        show:
          operation:
          - archive
          resource:
          - list
    typeInfo:
      type: boolean
      displayName: Archive
      name: archive
- id: getCards
  name: Get Cards
  description: Get all the cards in a list
  params:
  - id: id
    name: List ID
    type: string
    default: ''
    required: true
    description: The ID of the list to get cards
    validation: *id007
    typeInfo: *id008
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
    default: 20
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
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
  - field: cardId
    text: Select a Card...
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: name
    text: My board
  - field: additionalFields
    text: Add Field
  - field: id
    text: Select a Board...
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: name
    text: My card
  - field: additionalFields
    text: Add Field
  - field: id
    text: Select a Card...
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: cardId
    text: Select a Card...
  - field: cardId
    text: Select a Card...
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: boardId
    text: Select a Board...
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: cardId
    text: Choose...
  - field: updateFields
    text: Add Field
  - field: name
    text: My list
  - field: additionalFields
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
  "$id": "https://n8n.io/schemas/nodes/trello.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Trello Node",
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
        "update",
        "add",
        "invite",
        "remove",
        "createCheckItem",
        "deleteCheckItem",
        "getCheckItem",
        "completedCheckItems",
        "updateCheckItem",
        "addLabel",
        "removeLabel",
        "archive",
        "getCards"
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
            "attachment",
            "board",
            "boardMember",
            "card",
            "cardComment",
            "checklist",
            "label",
            "list"
          ],
          "default": "card"
        },
        "operation": {
          "description": "Archive/Unarchive a list",
          "type": "string",
          "enum": [
            "archive",
            "create",
            "get",
            "getCards",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "cardId": {
          "description": "The ID of the card",
          "type": "string",
          "examples": [
            "Choose..."
          ]
        },
        "url": {
          "description": "The URL of the attachment to add",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "additionalFields": {
          "description": "Fields to return. Either \"all\" or a comma-separated list of fields.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "id": {
          "description": "The ID of the list to update",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "The name of the list",
          "type": "string",
          "default": "",
          "examples": [
            "My list"
          ]
        },
        "description": {
          "description": "The description of the card",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "ID of a board the list should be moved to",
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
          "default": 20
        },
        "idMember": {
          "description": "The ID of the member to remove from the board",
          "type": "string",
          "default": ""
        },
        "type": {
          "description": "Invite as normal member",
          "type": "string",
          "enum": [
            "normal",
            "admin",
            "observer"
          ],
          "default": "normal"
        },
        "email": {
          "description": "The ID of the board to update",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "listId": {
          "description": "The ID of the list to create card in",
          "type": "string",
          "default": ""
        },
        "text": {
          "description": "Text of the comment",
          "type": "string",
          "default": ""
        },
        "commentId": {
          "description": "The ID of the comment to delete",
          "type": "string",
          "default": ""
        },
        "checklistId": {
          "description": "The ID of the checklist to update",
          "type": "string",
          "default": ""
        },
        "checkItemId": {
          "description": "The ID of the checklist item to update",
          "type": "string",
          "default": ""
        },
        "boardId": {
          "description": "The ID of the board",
          "type": "string",
          "examples": [
            "Select a Board..."
          ]
        },
        "color": {
          "description": "The color for the label",
          "type": "string",
          "enum": [
            "black",
            "blue",
            "green",
            "lime",
            "null",
            "orange",
            "pink",
            "purple",
            "red",
            "sky",
            "yellow"
          ],
          "default": "null"
        },
        "archive": {
          "description": "Whether the list should be archived or unarchived",
          "type": "boolean",
          "default": false
        },
        "idBoard": {
          "description": "The ID of the board the list should be created in",
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
      "name": "trelloApi",
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
