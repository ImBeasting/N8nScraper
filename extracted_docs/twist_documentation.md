---
title: "Node: Twist"
slug: "node-twist"
version: "1"
updated: "2026-01-08"
summary: "Consume Twist API"
node_type: "regular"
group: "['input']"
---

# Node: Twist

**Purpose.** Consume Twist API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:twist.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **twistOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `twistOAuth2Api` | ✓ | - |

---

## Operations

### Channel Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Archive | `archive` | Archive a channel |
| Create | `create` | Initiates a public or private channel-based conversation |
| Delete | `delete` | Delete a channel |
| Get | `get` | Get information about a channel |
| Get Many | `getAll` | Get many channels |
| Unarchive | `unarchive` | Unarchive a channel |
| Update | `update` | Update a channel |

### Comment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new comment to a thread |
| Delete | `delete` | Delete a comment |
| Get | `get` | Get information about a comment |
| Get Many | `getAll` | Get many comments |
| Update | `update` | Update a comment |

### Messageconversation Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a message in a conversation |
| Delete | `delete` | Delete a message in a conversation |
| Get | `get` | Get a message in a conversation |
| Get Many | `getAll` | Get many messages in a conversation |
| Update | `update` | Update a message in a conversation |

### Thread Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new thread in a channel |
| Delete | `delete` | Delete a thread |
| Get | `get` | Get information about a thread |
| Get Many | `getAll` | Get many threads |
| Update | `update` | Update a thread |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | messageConversation | ✗ | Resource to operate on |  |

**Resource options:**

* **Channel** (`channel`)
* **Comment** (`comment`)
* **Message Conversation** (`messageConversation`)
* **Thread** (`thread`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Archive a channel |  |

**Operation options:**

* **Archive** (`archive`) - Archive a channel
* **Create** (`create`) - Initiates a public or private channel-based conversation
* **Delete** (`delete`) - Delete a channel
* **Get** (`get`) - Get information about a channel
* **Get Many** (`getAll`) - Get many channels
* **Unarchive** (`unarchive`) - Unarchive a channel
* **Update** (`update`) - Update a channel

---

### Archive parameters (`archive`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel ID | `channelId` | string |  | ✓ | The ID of the channel |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workspace Name or ID | `workspaceId` | options |  | ✓ | The ID of the workspace. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Name | `name` | string |  | ✓ | The name of the channel |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The color of the channel | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Color | `color` | options | 0 | The color of the channel |
| Description | `description` | string |  | The description of the channel |
| Public | `public` | boolean | False | Whether the channel will be marked as public |
| Temp ID | `temp_id` | number |  | The temporary ID of the channel. It needs to be a negative number. |
| User Names or IDs | `user_ids` | multiOptions | [] | The users that will participate in the channel. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Thread ID | `threadId` | string |  | ✓ | The ID of the thread |  |
| Content | `content` | string |  | ✓ | The content of the comment |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The action of the button | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Actions | `actionsUi` | fixedCollection | {} | The action of the button |
| Attachments | `binaryProperties` | string | data | Name of the property that holds the binary data. Multiple can be defined separated by comma. |
| Direct Mention Names or IDs | `direct_mentions` | multiOptions | [] | The users that are directly mentioned. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Mark Thread Position | `mark_thread_position` | boolean | True | Whether the position of the thread is marked |
| Recipient Names or IDs | `recipients` | multiOptions | [] | The users that will attached to the comment. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Temporary ID | `temp_id` | number | 0 | The temporary ID of the comment |
| Send as Integration | `send_as_integration` | boolean | False | Whether to display the integration as the comment creator |

</details>

| Workspace Name or ID | `workspaceId` | options |  | ✓ | The ID of the workspace. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Conversation Name or ID | `conversationId` | options |  | ✓ | The ID of the conversation. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Content | `content` | string |  | ✗ | The content of the new message. Mentions can be used as <code>[Name](twist-mention://user_id)</code> for users or <code>[Group name](twist-group-mention://group_id)</code> for groups. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Other options to set | e.g. Add option |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Actions | `actionsUi` | fixedCollection | {} | The action of the button |
| Attachments | `binaryProperties` | string | data | Name of the property that holds the binary data. Multiple can be defined separated by comma. |
| Direct Mention Names or IDs | `direct_mentions` | multiOptions | [] | The users that are directly mentioned. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Direct Group Mentions | `direct_group_mentions` | multiOptions | [] | The groups that are directly mentioned. |

</details>

| Channel ID | `channelId` | string |  | ✓ | The ID of the channel |  |
| Title | `title` | string |  | ✓ | The title of the new thread (1 < length < 300) |  |
| Content | `content` | string |  | ✓ | The content of the thread |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The action of the button | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Actions | `actionsUi` | fixedCollection | {} | The action of the button |
| Attachments | `binaryProperties` | string | data | Name of the property that holds the binary data. Multiple can be defined separated by comma. |
| Direct Mention Names or IDs | `direct_mentions` | multiOptions | [] | The users that are directly mentioned. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Recipient Names or IDs | `recipients` | multiOptions | [] | The users that will attached to the thread. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Send as Integration | `send_as_integration` | boolean | False | Whether to display the integration as the thread creator |
| Temporary ID | `temp_id` | number | 0 | The temporary ID of the thread |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel ID | `channelId` | string |  | ✓ | The ID of the channel |  |
| Comment ID | `commentId` | string |  | ✓ | The ID of the comment |  |
| Message ID | `id` | string |  | ✓ | The ID of the conversation message |  |
| Thread ID | `threadId` | string |  | ✓ | The ID of the thread |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel ID | `channelId` | string |  | ✓ | The ID of the channel |  |
| Comment ID | `commentId` | string |  | ✓ | The ID of the comment |  |
| Message ID | `id` | string |  | ✓ | The ID of the conversation message |  |
| Thread ID | `threadId` | string |  | ✓ | The ID of the thread |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workspace Name or ID | `workspaceId` | options |  | ✓ | The ID of the workspace. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Whether only archived conversations are returned | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Archived | `archived` | boolean | False | Whether only archived conversations are returned |

</details>

| Thread ID | `threadId` | string |  | ✓ | The ID of the channel |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Whether only the IDs of the comments are returned | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| As IDs | `as_ids` | boolean | False | Whether only the IDs of the comments are returned |
| Ending Object Index | `to_obj_index` | number | 50 | Limit comments ending at the specified object index |
| Newer Than | `newer_than_ts` | dateTime |  | Limits comments to those newer when the specified Unix time |
| Older Than | `older_than_ts` | dateTime |  | Limits comments to those older than the specified Unix time |
| Order By | `order_by` | options | ASC | The order of the comments returned - one of DESC or ASC |
| Starting Object Index | `from_obj_index` | number | 0 | Limit comments starting at the specified object index |

</details>

| Workspace Name or ID | `workspaceId` | options |  | ✓ | The ID of the workspace. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Conversation Name or ID | `conversationId` | options |  | ✓ | The ID of the conversation. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Other options to set | min:1, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Ending Object Index | `to_obj_index` | number | 50 | Limit messages ending at the specified object index |
| Limit | `limit` | number | 50 | Max number of results to return |
| Order By | `order_by` | options | ASC | The order of the conversations returned - one of DESC or ASC |
| Starting Object Index | `from_obj_index` | number | 0 | Limit messages starting at the specified object index |

</details>

| Channel ID | `channelId` | string |  | ✓ | The ID of the channel |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Whether only the IDs of the threads are returned | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| As IDs | `as_ids` | boolean | False | Whether only the IDs of the threads are returned |
| Filter By | `filter_by` | options |  | A filter can be one of <code>attached_to_me</code>, <code>everyone</code> and <code>is_starred</code> |
| Newer Than | `newer_than_ts` | dateTime |  | Limits threads to those newer when the specified Unix time |
| Older Than | `older_than_ts` | dateTime |  | Limits threads to those older than the specified Unix time |

</details>


### Unarchive parameters (`unarchive`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel ID | `channelId` | string |  | ✓ | The ID of the channel |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel ID | `channelId` | string |  | ✓ | The ID of the channel |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The color of the channel | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Color | `color` | options | 0 | The color of the channel |
| Description | `description` | string |  | The description of the channel |
| Name | `name` | string |  | The name of the channel |
| Public | `public` | boolean | False | Whether the channel will be marked as public |

</details>

| Comment ID | `commentId` | string |  | ✓ | The ID of the comment |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The action of the button | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Actions | `actionsUi` | fixedCollection | {} | The action of the button |
| Attachments | `binaryProperties` | string | data | Name of the property that holds the binary data. Multiple can be defined separated by comma. |
| Content | `content` | string |  | The content of the comment |
| Direct Mention Names or IDs | `direct_mentions` | multiOptions | [] | The users that are directly mentioned. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Conversation Message ID | `id` | string |  | ✓ | The ID of the conversation message |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Other options to set | e.g. Add Action |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Actions | `actionsUi` | fixedCollection | {} | The action of the button |
| Attachments | `binaryProperties` | string | data | Name of the property that holds the binary data. Multiple can be defined separated by comma. |
| Content | `content` | string |  | The content of the new message. Mentions can be used as <code>[Name](twist-mention://user_id)</code> for users or <code>[Group name](twist-group-mention://group_id)</code> for groups. |
| Direct Mention Names or IDs | `direct_mentions` | multiOptions | [] | The users that are directly mentioned. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Thread ID | `threadId` | string |  | ✓ | The ID of the thread |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The action of the button | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Actions | `actionsUi` | fixedCollection | {} | The action of the button |
| Attachments | `binaryProperties` | string | data | Name of the property that holds the binary data. Multiple can be defined separated by comma. |
| Content | `content` | string |  | The content of the thread |
| Direct Mention Names or IDs | `direct_mentions` | multiOptions | [] | The users that are directly mentioned. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Title | `title` | string |  | The title of the thread (1 < length < 300) |

</details>


---

## Load Options Methods

- `getWorkspaces`
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
* Categories: Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: twist
displayName: Twist
description: Consume Twist API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: twistOAuth2Api
  required: true
operations:
- id: archive
  name: Archive
  description: Archive a channel
  params:
  - id: channelId
    name: Channel ID
    type: string
    default: ''
    required: true
    description: The ID of the channel
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - thread
    typeInfo: &id006
      type: string
      displayName: Channel ID
      name: channelId
- id: create
  name: Create
  description: Initiates a public or private channel-based conversation
  params:
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the workspace. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - messageConversation
    typeInfo: &id002
      type: options
      displayName: Workspace Name or ID
      name: workspaceId
      typeOptions:
        loadOptionsMethod: getWorkspaces
      possibleValues: []
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the channel
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - channel
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: The ID of the thread
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - thread
    typeInfo: &id008
      type: string
      displayName: Thread ID
      name: threadId
  - id: content
    name: Content
    type: string
    default: ''
    required: true
    description: The content of the comment
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - thread
    typeInfo: &id004
      type: string
      displayName: Content
      name: content
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the workspace. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: conversationId
    name: Conversation Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the conversation. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id017
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - messageConversation
    typeInfo: &id018
      type: options
      displayName: Conversation Name or ID
      name: conversationId
      typeOptions:
        loadOptionsMethod: getConversations
      possibleValues: []
  - id: content
    name: Content
    type: string
    default: ''
    required: false
    description: The content of the new message. Mentions can be used as <code>[Name](twist-mention://user_id)</code>
      for users or <code>[Group name](twist-group-mention://group_id)</code> for groups.
    validation: *id003
    typeInfo: *id004
  - id: channelId
    name: Channel ID
    type: string
    default: ''
    required: true
    description: The ID of the channel
    validation: *id005
    typeInfo: *id006
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The title of the new thread (1 < length < 300)
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - thread
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: content
    name: Content
    type: string
    default: ''
    required: true
    description: The content of the thread
    validation: *id003
    typeInfo: *id004
- id: delete
  name: Delete
  description: Delete a channel
  params:
  - id: channelId
    name: Channel ID
    type: string
    default: ''
    required: true
    description: The ID of the channel
    validation: *id005
    typeInfo: *id006
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: The ID of the comment
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - comment
    typeInfo: &id010
      type: string
      displayName: Comment ID
      name: commentId
  - id: id
    name: Message ID
    type: string
    default: ''
    required: true
    description: The ID of the conversation message
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - messageConversation
    typeInfo: &id012
      type: string
      displayName: Conversation Message ID
      name: id
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: The ID of the thread
    validation: *id007
    typeInfo: *id008
- id: get
  name: Get
  description: Get information about a channel
  params:
  - id: channelId
    name: Channel ID
    type: string
    default: ''
    required: true
    description: The ID of the channel
    validation: *id005
    typeInfo: *id006
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: The ID of the comment
    validation: *id009
    typeInfo: *id010
  - id: id
    name: Message ID
    type: string
    default: ''
    required: true
    description: The ID of the conversation message
    validation: *id011
    typeInfo: *id012
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: The ID of the thread
    validation: *id007
    typeInfo: *id008
- id: getAll
  name: Get Many
  description: Get many channels
  params:
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the workspace. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
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
          - thread
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
          - thread
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
        maxValue: 100
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: The ID of the channel
    validation: *id007
    typeInfo: *id008
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
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the workspace. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: conversationId
    name: Conversation Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the conversation. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id017
    typeInfo: *id018
  - id: channelId
    name: Channel ID
    type: string
    default: ''
    required: true
    description: The ID of the channel
    validation: *id005
    typeInfo: *id006
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
- id: unarchive
  name: Unarchive
  description: Unarchive a channel
  params:
  - id: channelId
    name: Channel ID
    type: string
    default: ''
    required: true
    description: The ID of the channel
    validation: *id005
    typeInfo: *id006
- id: update
  name: Update
  description: Update a channel
  params:
  - id: channelId
    name: Channel ID
    type: string
    default: ''
    required: true
    description: The ID of the channel
    validation: *id005
    typeInfo: *id006
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: The ID of the comment
    validation: *id009
    typeInfo: *id010
  - id: id
    name: Conversation Message ID
    type: string
    default: ''
    required: true
    description: The ID of the conversation message
    validation: *id011
    typeInfo: *id012
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: The ID of the thread
    validation: *id007
    typeInfo: *id008
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
  - field: filters
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add option
  - field: updateFields
    text: Add Action
  - field: additionalFields
    text: Add Field
  - field: filters
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
  "$id": "https://n8n.io/schemas/nodes/twist.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Twist Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "archive",
        "create",
        "delete",
        "get",
        "getAll",
        "unarchive",
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
            "channel",
            "comment",
            "messageConversation",
            "thread"
          ],
          "default": "messageConversation"
        },
        "operation": {
          "description": "Create a new thread in a channel",
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
        "workspaceId": {
          "description": "The ID of the workspace. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "The name of the channel",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The action of the button",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "channelId": {
          "description": "The ID of the channel",
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
          "description": "Whether only the IDs of the threads are returned",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "The action of the button",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "threadId": {
          "description": "The ID of the thread",
          "type": "string",
          "default": ""
        },
        "content": {
          "description": "The content of the thread",
          "type": "string",
          "default": ""
        },
        "commentId": {
          "description": "The ID of the comment",
          "type": "string",
          "default": ""
        },
        "conversationId": {
          "description": "The ID of the conversation. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "id": {
          "description": "The ID of the conversation message",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "The title of the new thread (1 < length < 300)",
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
      "name": "twistOAuth2Api",
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
