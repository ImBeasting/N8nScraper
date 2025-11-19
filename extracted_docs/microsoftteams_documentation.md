---
title: "Node: Microsoft Teams"
slug: "node-microsoftteams"
version: "['1', '1.1']"
updated: "2025-11-13"
summary: "Consume Microsoft Teams API"
node_type: "regular"
group: "['input']"
---

# Node: Microsoft Teams

**Purpose.** Consume Microsoft Teams API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:teams.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftTeamsOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **oldVersionNotice**: <strong>New node version available:</strong> get the latest version with added features from the nodes panel.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `microsoftTeamsOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Channel Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a channel |
| Delete | `delete` | Delete a channel |
| Get | `get` | Get a channel |
| Get Many | `getAll` | Get many channels |
| Update | `update` | Update a channel |

### Channelmessage Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a message |
| Get Many | `getAll` | Get many messages |

### Chatmessage Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a message |
| Get | `get` | Get a message |
| Get Many | `getAll` | Get many messages |

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
| Resource | `resource` | options | channel | ✗ | Resource to operate on |  |

**Resource options:**

* **Channel** (`channel`)
* **Channel Message (Beta)** (`channelMessage`)
* **Chat Message** (`chatMessage`)
* **Task** (`task`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a channel |  |

**Operation options:**

* **Create** (`create`) - Create a channel
* **Delete** (`delete`) - Delete a channel
* **Get** (`get`) - Get a channel
* **Get Many** (`getAll`) - Get many channels
* **Update** (`update`) - Update a channel

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team Name or ID | `teamId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Name | `name` | string |  | ✓ | Channel name as it will appear to the user in Microsoft Teams |  |
| Options | `options` | collection | {} | ✗ | Channel's description | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Channel's description |
| Type | `type` | options | standard | The type of the channel |

</details>

| Team Name or ID | `teamId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Channel Name or ID | `channelId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Message Type | `messageType` | options | text | ✓ | The type of the content |  |

**Message Type options:**

* **Text** (`text`)
* **HTML** (`html`)

| Message | `message` | string |  | ✓ | The content of the item |  |
| Options | `options` | collection | {} | ✗ | Whether to append a link to this workflow at the end of the message. This is helpful if you have many workflows sending messages. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Link to Workflow | `includeLinkToWorkflow` | boolean | True | Whether to append a link to this workflow at the end of the message. This is helpful if you have many workflows sending messages. |
| Make Reply | `makeReply` | string |  | An optional ID of the message you want to reply to |

</details>

| Chat Name or ID | `chatId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Message Type | `messageType` | options | text | ✓ | The type of the content |  |

**Message Type options:**

* **Text** (`text`)
* **HTML** (`html`)

| Message | `message` | string |  | ✓ | The content of the item |  |
| Options | `options` | collection | {} | ✗ | Other options to set | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Link to Workflow | `includeLinkToWorkflow` | boolean | True | Whether to append a link to this workflow at the end of the message. This is helpful if you have many workflows sending messages. |

</details>

| Group Source | `groupSource` | options | all | ✓ | From all groups |  |

**Group Source options:**

* **All Groups** (`all`) - From all groups
* **My Groups** (`mine`) - Only load groups that account is member of

| Group Name or ID | `groupId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Plan Name or ID | `planId` | options |  | ✓ | The plan for the task to belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Bucket Name or ID | `bucketId` | options |  | ✓ | The bucket for the task to belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Title | `title` | string |  | ✓ | Title of the task |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Who the task should be assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assigned To Name or ID | `assignedTo` | options |  | Who the task should be assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Due Date Time | `dueDateTime` | dateTime |  | Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. |
| Label Names or IDs | `labels` | multiOptions | [] | Labels to assign to the task. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Percent Complete | `percentComplete` | number | 0 | Percentage of task completion. When set to 100, the task is considered completed. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team Name or ID | `teamId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Channel Name or ID | `channelId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Task ID | `taskId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team Name or ID | `teamId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Channel Name or ID | `channelId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Chat Name or ID | `chatId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Task ID | `taskId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team Name or ID | `teamId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Team Name or ID | `teamId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Channel Name or ID | `channelId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Chat Name or ID | `chatId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Group Source | `groupSource` | options | all | ✓ | From all groups |  |

**Group Source options:**

* **All Groups** (`all`) - From all groups
* **My Groups** (`mine`) - Only load groups that account is member of

| Tasks For | `tasksFor` | options | member | ✓ | Tasks assigned to group member |  |

**Tasks For options:**

* **Group Member** (`member`) - Tasks assigned to group member
* **Plan** (`plan`) - Tasks in group plan

| Group Name or ID | `groupId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Member Name or ID | `memberId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Plan Name or ID | `planId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team Name or ID | `teamId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Channel Name or ID | `channelId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Channel name as it will appear to the user in Microsoft Teams | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | Channel name as it will appear to the user in Microsoft Teams |
| Description | `description` | string |  | Channel's description |

</details>

| Group Source | `groupSource` | options | all | ✓ | From all groups |  |

**Group Source options:**

* **All Groups** (`all`) - From all groups
* **My Groups** (`mine`) - Only load groups that account is member of

| Task ID | `taskId` | string |  | ✓ | The ID of the Task |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Who the task should be assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assigned To Name or ID | `assignedTo` | options |  | Who the task should be assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Bucket Name or ID | `bucketId` | options |  | The bucket for the task to belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Due Date Time | `dueDateTime` | dateTime |  | Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. |
| Group Name or ID | `groupId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Label Names or IDs | `labels` | multiOptions | [] | Labels to assign to the task. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Percent Complete | `percentComplete` | number | 0 | Percentage of task completion. When set to 100, the task is considered completed. |
| Plan Name or ID | `planId` | options |  | The plan for the task to belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Title | `title` | string |  | Title of the task |

</details>


---

## Load Options Methods

- `getChannels`

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
node: microsoftTeams
displayName: Microsoft Teams
description: Consume Microsoft Teams API
version:
- '1'
- '1.1'
nodeType: regular
group:
- input
credentials:
- name: microsoftTeamsOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a channel
  params:
  - id: teamId
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - channelMessage
    typeInfo: &id002
      type: options
      displayName: Team Name or ID
      name: teamId
      typeOptions:
        loadOptionsMethod: getTeams
      possibleValues: []
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Channel name as it will appear to the user in Microsoft Teams
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
  - id: teamId
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: channelId
    name: Channel Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id007
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - channelMessage
    typeInfo: &id008
      type: options
      displayName: Channel Name or ID
      name: channelId
      typeOptions:
        loadOptionsMethod: getChannels
      possibleValues: []
  - id: messageType
    name: Message Type
    type: options
    default: text
    required: true
    description: The type of the content
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - chatMessage
    typeInfo: &id004
      type: options
      displayName: Message Type
      name: messageType
      possibleValues:
      - value: text
        name: Text
        description: ''
      - value: html
        name: HTML
        description: ''
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: The content of the item
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - chatMessage
    typeInfo: &id006
      type: string
      displayName: Message
      name: message
  - id: chatId
    name: Chat Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - chatMessage
    typeInfo: &id010
      type: options
      displayName: Chat Name or ID
      name: chatId
      typeOptions:
        loadOptionsMethod: getChats
      possibleValues: []
  - id: messageType
    name: Message Type
    type: options
    default: text
    required: true
    description: The type of the content
    validation: *id003
    typeInfo: *id004
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: The content of the item
    validation: *id005
    typeInfo: *id006
  - id: groupSource
    name: Group Source
    type: options
    default: all
    required: true
    description: From all groups
    validation: &id017
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          - create
          - update
          resource:
          - task
    typeInfo: &id018
      type: options
      displayName: Group Source
      name: groupSource
      possibleValues:
      - value: all
        name: All Groups
        description: From all groups
      - value: mine
        name: My Groups
        description: Only load groups that account is member of
  - id: groupId
    name: Group Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id019
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - task
    typeInfo: &id020
      type: options
      displayName: Group Name or ID
      name: groupId
      typeOptions:
        loadOptionsMethod: getGroups
      possibleValues: []
  - id: planId
    name: Plan Name or ID
    type: options
    default: ''
    required: true
    description: The plan for the task to belong to. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id021
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - task
          tasksFor:
          - plan
    typeInfo: &id022
      type: options
      displayName: Plan Name or ID
      name: planId
      typeOptions:
        loadOptionsMethod: getPlans
      possibleValues: []
  - id: bucketId
    name: Bucket Name or ID
    type: options
    default: ''
    required: true
    description: The bucket for the task to belong to. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - task
    typeInfo:
      type: options
      displayName: Bucket Name or ID
      name: bucketId
      typeOptions:
        loadOptionsMethod: getBuckets
      possibleValues: []
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the task
    validation:
      required: true
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
  description: Delete a channel
  params:
  - id: teamId
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: channelId
    name: Channel Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - task
    typeInfo: &id012
      type: string
      displayName: Task ID
      name: taskId
- id: get
  name: Get
  description: Get a channel
  params:
  - id: teamId
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: channelId
    name: Channel Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: chatId
    name: Chat Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id009
    typeInfo: *id010
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - chatMessage
    typeInfo:
      type: string
      displayName: Message ID
      name: messageId
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
- id: getAll
  name: Get Many
  description: Get many channels
  params:
  - id: teamId
    name: Team Name or ID
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
    validation: &id013
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - task
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
          operation:
          - getAll
          resource:
          - task
          returnAll:
          - false
    typeInfo: &id016
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: teamId
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: channelId
    name: Channel Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
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
  - id: chatId
    name: Chat Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id009
    typeInfo: *id010
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
  - id: groupSource
    name: Group Source
    type: options
    default: all
    required: true
    description: From all groups
    validation: *id017
    typeInfo: *id018
  - id: tasksFor
    name: Tasks For
    type: options
    default: member
    required: true
    description: Tasks assigned to group member
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - task
    typeInfo:
      type: options
      displayName: Tasks For
      name: tasksFor
      possibleValues:
      - value: member
        name: Group Member
        description: Tasks assigned to group member
      - value: plan
        name: Plan
        description: Tasks in group plan
  - id: groupId
    name: Group Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id019
    typeInfo: *id020
  - id: memberId
    name: Member Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - task
          tasksFor:
          - member
    typeInfo:
      type: options
      displayName: Member Name or ID
      name: memberId
      typeOptions:
        loadOptionsMethod: getMembers
      possibleValues: []
  - id: planId
    name: Plan Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id021
    typeInfo: *id022
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
  description: Update a channel
  params:
  - id: teamId
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: channelId
    name: Channel Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: groupSource
    name: Group Source
    type: options
    default: all
    required: true
    description: From all groups
    validation: *id017
    typeInfo: *id018
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: The ID of the Task
    validation: *id011
    typeInfo: *id012
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices:
  - name: oldVersionNotice
    text: <strong>New node version available:</strong> get the latest version with
      added features from the nodes panel.
    conditions: null
  tooltips: []
  placeholders:
  - field: options
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/microsoftTeams.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft Teams Node",
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
            "channel",
            "channelMessage",
            "chatMessage",
            "task"
          ],
          "default": "channel"
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
        "teamId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "Channel name as it will appear to the user in Microsoft Teams",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Other options to set",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "channelId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
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
        "updateFields": {
          "description": "Who the task should be assigned to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "messageType": {
          "description": "The type of the content",
          "type": "string",
          "enum": [
            "text",
            "html"
          ],
          "default": "text"
        },
        "message": {
          "description": "The content of the item",
          "type": "string",
          "default": ""
        },
        "chatId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "messageId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "groupSource": {
          "description": "From all groups",
          "type": "string",
          "enum": [
            "all",
            "mine"
          ],
          "default": "all"
        },
        "groupId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "planId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "bucketId": {
          "description": "The bucket for the task to belong to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "Title of the task",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Who the task should be assigned to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "taskId": {
          "description": "The ID of the Task",
          "type": "string",
          "default": ""
        },
        "tasksFor": {
          "description": "Tasks assigned to group member",
          "type": "string",
          "enum": [
            "member",
            "plan"
          ],
          "default": "member"
        },
        "memberId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
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
    "version": [
      "1",
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "microsoftTeamsOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
