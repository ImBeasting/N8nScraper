---
title: "Node: Monica CRM"
slug: "node-monicacrm"
version: "1"
updated: "2025-11-13"
summary: "Consume the Monica CRM API"
node_type: "regular"
group: "['transform']"
---

# Node: Monica CRM

**Purpose.** Consume the Monica CRM API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:monicaCrm.png`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **monicaCrmApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `monicaCrmApi` | ✓ | - |

---

## Operations

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a task |
| Delete | `delete` | Delete a task |
| Get | `get` | Retrieve a task |
| Get Many | `getAll` | Retrieve many tasks |
| Update | `update` | Update a task |

### Activity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an activity |
| Delete | `delete` | Delete an activity |
| Get | `get` | Retrieve an activity |
| Get Many | `getAll` | Retrieve many activities |
| Update | `update` | Update an activity |

### Call Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a call |
| Delete | `delete` | Delete a call |
| Get | `get` | Retrieve a call |
| Get Many | `getAll` | Retrieve many calls |
| Update | `update` | Update a call |

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a contact |
| Delete | `delete` | Delete a contact |
| Get | `get` | Retrieve a contact |
| Get Many | `getAll` | Retrieve many contacts |
| Update | `update` | Update a contact |

### Contactfield Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a contact field |
| Delete | `delete` | Delete a contact field |
| Get | `get` | Retrieve a contact field |
| Get All | `getAll` | Retrieve all contact fields |
| Update | `update` | Update a contact field |

### Contacttag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a tag to a contact |
| Remove | `remove` | Remove a tag from a contact |

### Conversation Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a conversation |
| Delete | `delete` | Delete a conversation |
| Get | `get` | Retrieve a conversation |
| Update | `update` | Update a conversation |

### Conversationmessage Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a message to a conversation |
| Update | `update` | Update a message in a conversation |

### Journalentry Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a journal entry |
| Delete | `delete` | Delete a journal entry |
| Get | `get` | Retrieve a journal entry |
| Get Many | `getAll` | Retrieve many journal entries |
| Update | `update` | Update a journal entry |

### Note Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a note |
| Delete | `delete` | Delete a note |
| Get | `get` | Retrieve a note |
| Get Many | `getAll` | Retrieve many notes |
| Update | `update` | Update a note |

### Reminder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a reminder |
| Delete | `delete` | Delete a reminder |
| Get | `get` | Retrieve a reminder |
| Get Many | `getAll` | Retrieve many reminders |
| Update | `update` | Update a reminder |

### Tag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a tag |
| Delete | `delete` | Delete a tag |
| Get | `get` | Retrieve a tag |
| Get Many | `getAll` | Retrieve many tags |
| Update | `update` | Update a tag |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✗ | Resource to operate on |  |

**Resource options:**

* **Activity** (`activity`)
* **Call** (`call`)
* **Contact** (`contact`)
* **Contact Field** (`contactField`)
* **Contact Tag** (`contactTag`)
* **Conversation** (`conversation`)
* **Conversation Message** (`conversationMessage`)
* **Journal Entry** (`journalEntry`)
* **Note** (`note`)
* **Reminder** (`reminder`)
* **Tag** (`tag`)
* **Task** (`task`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a task |  |

**Operation options:**

* **Create** (`create`) - Create a task
* **Delete** (`delete`) - Delete a task
* **Get** (`get`) - Retrieve a task
* **Get Many** (`getAll`) - Retrieve many tasks
* **Update** (`update`) - Update a task

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | ID of the contact to associate the task with |  |
| Title | `title` | string |  | ✓ | Title of the task entry - max 250 characters |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Description of the task - max 100,000 characters | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Description of the task - max 100,000 characters |

</details>

| Activity Type Name or ID | `activityTypeId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Contacts | `contacts` | string |  | ✓ | Comma-separated list of IDs of the contacts to associate the activity with |  |
| Happened At | `happenedAt` | dateTime |  | ✓ | Date when the activity happened |  |
| Summary | `summary` | string |  | ✓ | Brief description of the activity - max 255 characters |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Description of the activity - max 100,000 characters | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Description of the activity - max 100,000 characters |

</details>

| Contact ID | `contactId` | string |  | ✓ | ID of the contact to associate the call with |  |
| Called At | `calledAt` | dateTime |  | ✓ | Date when the call happened |  |
| Description | `content` | string |  | ✓ | Description of the call - max 100,000 characters |  |
| First Name | `firstName` | string |  | ✓ |  |  |
| Gender Name or ID | `genderId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether the contact has passed away | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Birthdate | `birthdate` | dateTime |  |  |
| Deceased Date | `deceasedDate` | dateTime |  |  |
| Is Deceased | `isDeceased` | boolean | False | Whether the contact has passed away |
| Last Name | `last_name` | string |  |  |
| Nickname | `nickname` | string |  |  |
| Type | `is_partial` | options | False | Contact with their own contact sheet |

</details>

| Contact ID | `contactId` | string |  | ✓ | ID of the contact to associate the contact field with |  |
| Contact Field Type Name or ID | `contactFieldTypeId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Content | `data` | string |  | ✓ | Content of the contact field - max 255 characters |  |
| Contact ID | `contactId` | string |  | ✓ | ID of the contact to associate the conversation with |  |
| Contact Field Type Name or ID | `contactFieldTypeId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Happened At | `happenedAt` | dateTime |  | ✓ | Date when the conversation happened |  |
| Title | `title` | string |  | ✓ | Title of the journal entry - max 250 characters |  |
| Content | `post` | string |  | ✓ | Content of the journal entry - max 100,000 characters |  |
| Contact ID | `contactId` | string |  | ✓ | ID of the contact to associate the note with |  |
| Body | `body` | string |  | ✓ | Body of the note - max 100,000 characters |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether the note has been favorited | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Is Favorited | `isFavorited` | boolean | False | Whether the note has been favorited |

</details>

| Contact ID | `contactId` | string |  | ✗ | ID of the contact to associate the reminder with |  |
| Frequency Type | `frequencyType` | options | one_time | ✓ | Type of frequency of the reminder |  |

**Frequency Type options:**

* **Once** (`one_time`)
* **Weekly** (`week`)
* **Monthly** (`month`)
* **Yearly** (`year`)

| Recurring Interval | `frequencyNumber` | number | 0 | ✗ | Interval for the reminder |  |
| Initial Date | `initialDate` | dateTime |  | ✓ | Date of the reminder |  |
| Title | `title` | string |  | ✓ | Title of the reminder - max 100,000 characters |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Description about the reminder - Max 100,000 characters | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Description about the reminder - Max 100,000 characters |

</details>

| Name | `name` | string |  | ✓ | Name of the tag - max 250 characters |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ | ID of the task to delete |  |
| Activity ID | `activityId` | string |  | ✓ | ID of the activity to delete |  |
| Call ID | `callId` | string |  | ✓ | ID of the call to delete |  |
| Contact ID | `contactId` | string |  | ✓ | ID of the contact to delete |  |
| Contact Field ID | `contactFieldId` | string |  | ✓ | ID of the contactField to delete |  |
| Conversation ID | `conversationId` | string |  | ✓ | ID of the conversation to delete |  |
| Journal Entry ID | `journalId` | string |  | ✓ | ID of the journal entry to delete |  |
| Note ID | `noteId` | string |  | ✓ | ID of the note to delete |  |
| Reminder ID | `reminderId` | string |  | ✓ | ID of the reminder to delete |  |
| Tag ID | `tagId` | string |  | ✓ | ID of the tag to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ | ID of the task to retrieve |  |
| Activity ID | `activityId` | string |  | ✓ | ID of the activity to retrieve |  |
| Call ID | `callId` | string |  | ✓ | ID of the call to retrieve |  |
| Contact ID | `contactId` | string |  | ✓ | ID of the contact to retrieve |  |
| Contact Field ID | `contactFieldId` | string |  | ✓ | ID of the contact field to retrieve |  |
| Conversation ID | `conversationId` | string |  | ✓ | ID of the conversation to retrieve |  |
| Journal Entry ID | `journalId` | string |  | ✓ | ID of the journal entry to retrieve |  |
| Note ID | `noteId` | string |  | ✓ | ID of the note to retrieve |  |
| Reminder ID | `reminderId` | string |  | ✓ | ID of the reminder to retrieve |  |
| Tag ID | `tagId` | string |  | ✓ | ID of the tag to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Search term to filter results by | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Search Term | `query` | string |  | Search term to filter results by |
| Sort | `sort` | options |  |  |

</details>

| Contact ID | `contactId` | string |  | ✓ | ID of the contact whose fields to retrieve |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ | ID of the task to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the contact to associate the task with | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Contact ID | `contactId` | string |  | ID of the contact to associate the task with |
| Completed | `completed` | boolean | False | Whether the task has been completed |
| Description | `description` | string |  | Description of the task - max 100,000 characters |
| Title | `title` | string |  | Title of the task entry - max 250 characters |

</details>

| Activity ID | `activityId` | string |  | ✓ | ID of the activity to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Activity Type Name or ID | `activity_type_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Contacts | `contacts` | string |  | IDs of the contacts to associate the activity with |
| Description | `description` | string |  | Description to add more details on the activity - max 100,000 characters |
| Happened At | `happened_at` | dateTime |  | Date when the activity happened |
| Summary | `summary` | string |  | Brief description of the activity - max 255 characters |

</details>

| Call ID | `callId` | string |  | ✓ | ID of the call to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Date when the call happened | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Called At | `calledAt` | dateTime |  | Date when the call happened |
| Contact ID | `contactId` | string |  | ID of the contact to associate the call with |
| Description | `content` | string |  | Description of the call - max 100,000 characters |

</details>

| Contact ID | `contactId` | string |  | ✓ | ID of the contact to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Birthdate | `birthdate` | dateTime |  |  |
| Deceased Date | `deceased_date` | dateTime |  |  |
| First Name | `first_name` | string |  |  |
| Gender Name or ID | `gender_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Is Deceased | `is_deceased` | boolean | False | Whether the contact has passed away |
| Last Name | `last_name` | string |  |  |
| Nickname | `nickname` | string |  |  |
| Type | `is_partial` | options | False | Contact with their own contact sheet |

</details>

| Contact ID | `contactId` | string |  | ✓ | ID of the contact to associate the contact field with |  |
| Contact Field ID | `contactFieldId` | string |  | ✓ | ID of the contact field to update |  |
| Contact Field Type Name or ID | `contactFieldTypeId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Content | `data` | string |  | ✓ | Content of the contact field - max 255 characters |  |
| Conversation ID | `conversationId` | string |  | ✓ | ID of the conversation to update |  |
| Contact Field Type Name or ID | `contactFieldTypeId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Happened At | `happenedAt` | dateTime |  | ✓ | Date when the conversation happened |  |
| Message ID | `messageId` | string |  | ✓ | ID of the message to update |  |
| Conversation ID | `conversationId` | string |  | ✓ | ID of the conversation whose message to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the contact to associate the conversationMessage with | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Contact ID | `contact_id` | string |  | ID of the contact to associate the conversationMessage with |
| Content | `content` | string |  | Content of the message |
| Written At | `written_at` | dateTime |  | Date when the message was written |
| Written By | `written_by_me` | options | True | Author of the message |

</details>

| Journal Entry ID | `journalId` | string |  | ✓ | ID of the journal entry to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Content of the journal entry - max 100,000 characters | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content | `post` | string |  | Content of the journal entry - max 100,000 characters |
| Title | `title` | string |  | Title of the journal entry - max 250 characters |

</details>

| Note ID | `noteId` | string |  | ✓ | ID of the note to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Body of the note - max 100,000 characters | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body | `body` | string |  | Body of the note - max 100,000 characters |
| Contact ID | `contact_id` | string |  | ID of the contact to associate the note with |
| Is Favorited | `is_favorited` | boolean | False | Whether the note has been favorited |

</details>

| Reminder ID | `reminderId` | string |  | ✓ | ID of the reminder to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the contact to associate the reminder with | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Contact ID | `contact_id` | string |  | ID of the contact to associate the reminder with |
| Description | `description` | string |  | Description about the reminder - Max 100,000 characters |
| Frequency Type | `frequency_type` | options | one_time | Frequency of the reminder |
| Initial Date | `initial_data` | dateTime |  | Date of the reminder |
| Recurring Interval | `frequency_number` | number | 0 | Interval for the reminder |
| Title | `title` | string |  | Title of the reminder - max 100,000 characters |

</details>

| Tag ID | `tagId` | string |  | ✓ | ID of the tag to update |  |
| Name | `name` | string |  | ✓ | Name of the tag - max 250 characters |  |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | ID of the contact to add a tag to |  |
| Tag Names or IDs | `tagsToAdd` | multiOptions | [] | ✓ | Tags to add to the contact. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Conversation ID | `conversationId` | string |  | ✓ | ID of the contact whose conversation |  |
| Content | `content` | string |  | ✓ | Content of the message |  |
| Written At | `writtenAt` | dateTime |  | ✓ | Date when the message was written |  |
| Written By | `writtenByMe` | options | True | ✓ | Author of the message |  |

**Written By options:**

* **User** (``)
* **Contact** (``)


### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | ID of the contact to remove the tag from |  |
| Tag Names or IDs | `tagsToRemove` | multiOptions | [] | ✓ | Tags to remove from the contact. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

---

## Load Options Methods

- `getActivityTypes`

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
node: monicaCrm
displayName: Monica CRM
description: Consume the Monica CRM API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: monicaCrmApi
  required: true
operations:
- id: create
  name: Create
  description: Create a task
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to associate the task with
    validation: &id001
      displayOptions:
        show:
          resource:
          - reminder
          operation:
          - create
    typeInfo: &id002
      type: string
      displayName: Contact ID
      name: contactId
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the task entry - max 250 characters
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - reminder
          operation:
          - create
    typeInfo: &id008
      type: string
      displayName: Title
      name: title
  - id: activityTypeId
    name: Activity Type Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - activity
          operation:
          - create
    typeInfo:
      type: options
      displayName: Activity Type Name or ID
      name: activityTypeId
      typeOptions:
        loadOptionsMethod: getActivityTypes
      possibleValues: []
  - id: contacts
    name: Contacts
    type: string
    default: ''
    required: true
    description: Comma-separated list of IDs of the contacts to associate the activity
      with
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - activity
          operation:
          - create
    typeInfo:
      type: string
      displayName: Contacts
      name: contacts
  - id: happenedAt
    name: Happened At
    type: dateTime
    default: ''
    required: true
    description: Date when the activity happened
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - conversation
          operation:
          - update
    typeInfo: &id006
      type: dateTime
      displayName: Happened At
      name: happenedAt
  - id: summary
    name: Summary
    type: string
    default: ''
    required: true
    description: Brief description of the activity - max 255 characters
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - activity
          operation:
          - create
    typeInfo:
      type: string
      displayName: Summary
      name: summary
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to associate the call with
    validation: *id001
    typeInfo: *id002
  - id: calledAt
    name: Called At
    type: dateTime
    default: ''
    required: true
    description: Date when the call happened
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - call
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: Called At
      name: calledAt
  - id: content
    name: Description
    type: string
    default: ''
    required: true
    description: Description of the call - max 100,000 characters
    validation: &id035
      required: true
      displayOptions:
        show:
          resource:
          - conversationMessage
          operation:
          - add
    typeInfo: &id036
      type: string
      displayName: Content
      name: content
  - id: firstName
    name: First Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
    typeInfo:
      type: string
      displayName: First Name
      name: firstName
  - id: genderId
    name: Gender Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
    typeInfo:
      type: options
      displayName: Gender Name or ID
      name: genderId
      typeOptions:
        loadOptionsMethod: getGenders
      possibleValues: []
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to associate the contact field with
    validation: *id001
    typeInfo: *id002
  - id: contactFieldTypeId
    name: Contact Field Type Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - conversation
          operation:
          - update
    typeInfo: &id004
      type: options
      displayName: Contact Field Type Name or ID
      name: contactFieldTypeId
      typeOptions:
        loadOptionsMethod: getContactFieldTypes
      possibleValues: []
  - id: data
    name: Content
    type: string
    default: ''
    required: true
    description: Content of the contact field - max 255 characters
    validation: &id031
      required: true
      displayOptions:
        show:
          resource:
          - contactField
          operation:
          - update
    typeInfo: &id032
      type: string
      displayName: Content
      name: data
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to associate the conversation with
    validation: *id001
    typeInfo: *id002
  - id: contactFieldTypeId
    name: Contact Field Type Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: happenedAt
    name: Happened At
    type: dateTime
    default: ''
    required: true
    description: Date when the conversation happened
    validation: *id005
    typeInfo: *id006
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the journal entry - max 250 characters
    validation: *id007
    typeInfo: *id008
  - id: post
    name: Content
    type: string
    default: ''
    required: true
    description: Content of the journal entry - max 100,000 characters
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - journalEntry
          operation:
          - create
    typeInfo:
      type: string
      displayName: Content
      name: post
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to associate the note with
    validation: *id001
    typeInfo: *id002
  - id: body
    name: Body
    type: string
    default: ''
    required: true
    description: Body of the note - max 100,000 characters
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - note
          operation:
          - create
    typeInfo:
      type: string
      displayName: Body
      name: body
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: false
    description: ID of the contact to associate the reminder with
    validation: *id001
    typeInfo: *id002
  - id: frequencyType
    name: Frequency Type
    type: options
    default: one_time
    required: true
    description: Type of frequency of the reminder
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
      displayName: Frequency Type
      name: frequencyType
      possibleValues:
      - value: one_time
        name: Once
        description: ''
      - value: week
        name: Weekly
        description: ''
      - value: month
        name: Monthly
        description: ''
      - value: year
        name: Yearly
        description: ''
  - id: frequencyNumber
    name: Recurring Interval
    type: number
    default: 0
    required: false
    description: Interval for the reminder
    validation:
      displayOptions:
        show:
          resource:
          - reminder
          operation:
          - create
          frequencyType:
          - week
          - month
          - year
    typeInfo:
      type: number
      displayName: Recurring Interval
      name: frequencyNumber
  - id: initialDate
    name: Initial Date
    type: dateTime
    default: ''
    required: true
    description: Date of the reminder
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - reminder
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: Initial Date
      name: initialDate
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the reminder - max 100,000 characters
    validation: *id007
    typeInfo: *id008
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the tag - max 250 characters
    validation: &id033
      required: true
      displayOptions:
        show:
          resource:
          - tag
          operation:
          - update
    typeInfo: &id034
      type: string
      displayName: Name
      name: name
- id: delete
  name: Delete
  description: Delete a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task to delete
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Task ID
      name: taskId
  - id: activityId
    name: Activity ID
    type: string
    default: ''
    required: true
    description: ID of the activity to delete
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - activity
          operation:
          - update
    typeInfo: &id012
      type: string
      displayName: Activity ID
      name: activityId
  - id: callId
    name: Call ID
    type: string
    default: ''
    required: true
    description: ID of the call to delete
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - call
          operation:
          - update
    typeInfo: &id014
      type: string
      displayName: Call ID
      name: callId
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to delete
    validation: *id001
    typeInfo: *id002
  - id: contactFieldId
    name: Contact Field ID
    type: string
    default: ''
    required: true
    description: ID of the contactField to delete
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - contactField
          operation:
          - update
    typeInfo: &id016
      type: string
      displayName: Contact Field ID
      name: contactFieldId
  - id: conversationId
    name: Conversation ID
    type: string
    default: ''
    required: true
    description: ID of the conversation to delete
    validation: &id017
      required: true
      displayOptions:
        show:
          resource:
          - conversationMessage
          operation:
          - update
    typeInfo: &id018
      type: string
      displayName: Conversation ID
      name: conversationId
  - id: journalId
    name: Journal Entry ID
    type: string
    default: ''
    required: true
    description: ID of the journal entry to delete
    validation: &id019
      required: true
      displayOptions:
        show:
          resource:
          - journalEntry
          operation:
          - update
    typeInfo: &id020
      type: string
      displayName: Journal Entry ID
      name: journalId
  - id: noteId
    name: Note ID
    type: string
    default: ''
    required: true
    description: ID of the note to delete
    validation: &id021
      required: true
      displayOptions:
        show:
          resource:
          - note
          operation:
          - update
    typeInfo: &id022
      type: string
      displayName: Note ID
      name: noteId
  - id: reminderId
    name: Reminder ID
    type: string
    default: ''
    required: true
    description: ID of the reminder to delete
    validation: &id023
      required: true
      displayOptions:
        show:
          resource:
          - reminder
          operation:
          - update
    typeInfo: &id024
      type: string
      displayName: Reminder ID
      name: reminderId
  - id: tagId
    name: Tag ID
    type: string
    default: ''
    required: true
    description: ID of the tag to delete
    validation: &id025
      required: true
      displayOptions:
        show:
          resource:
          - tag
          operation:
          - update
    typeInfo: &id026
      type: string
      displayName: Tag ID
      name: tagId
- id: get
  name: Get
  description: Retrieve a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task to retrieve
    validation: *id009
    typeInfo: *id010
  - id: activityId
    name: Activity ID
    type: string
    default: ''
    required: true
    description: ID of the activity to retrieve
    validation: *id011
    typeInfo: *id012
  - id: callId
    name: Call ID
    type: string
    default: ''
    required: true
    description: ID of the call to retrieve
    validation: *id013
    typeInfo: *id014
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to retrieve
    validation: *id001
    typeInfo: *id002
  - id: contactFieldId
    name: Contact Field ID
    type: string
    default: ''
    required: true
    description: ID of the contact field to retrieve
    validation: *id015
    typeInfo: *id016
  - id: conversationId
    name: Conversation ID
    type: string
    default: ''
    required: true
    description: ID of the conversation to retrieve
    validation: *id017
    typeInfo: *id018
  - id: journalId
    name: Journal Entry ID
    type: string
    default: ''
    required: true
    description: ID of the journal entry to retrieve
    validation: *id019
    typeInfo: *id020
  - id: noteId
    name: Note ID
    type: string
    default: ''
    required: true
    description: ID of the note to retrieve
    validation: *id021
    typeInfo: *id022
  - id: reminderId
    name: Reminder ID
    type: string
    default: ''
    required: true
    description: ID of the reminder to retrieve
    validation: *id023
    typeInfo: *id024
  - id: tagId
    name: Tag ID
    type: string
    default: ''
    required: true
    description: ID of the tag to retrieve
    validation: *id025
    typeInfo: *id026
- id: getAll
  name: Get Many
  description: Retrieve many tasks
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id027
      displayOptions:
        show:
          resource:
          - tag
          operation:
          - getAll
    typeInfo: &id028
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id029
      displayOptions:
        show:
          resource:
          - tag
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id030
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id027
    typeInfo: *id028
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id029
    typeInfo: *id030
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id027
    typeInfo: *id028
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id029
    typeInfo: *id030
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id027
    typeInfo: *id028
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id029
    typeInfo: *id030
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact whose fields to retrieve
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id027
    typeInfo: *id028
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id029
    typeInfo: *id030
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id027
    typeInfo: *id028
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id029
    typeInfo: *id030
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id027
    typeInfo: *id028
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id029
    typeInfo: *id030
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id027
    typeInfo: *id028
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id029
    typeInfo: *id030
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id027
    typeInfo: *id028
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id029
    typeInfo: *id030
- id: update
  name: Update
  description: Update a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task to update
    validation: *id009
    typeInfo: *id010
  - id: activityId
    name: Activity ID
    type: string
    default: ''
    required: true
    description: ID of the activity to update
    validation: *id011
    typeInfo: *id012
  - id: callId
    name: Call ID
    type: string
    default: ''
    required: true
    description: ID of the call to update
    validation: *id013
    typeInfo: *id014
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to update
    validation: *id001
    typeInfo: *id002
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to associate the contact field with
    validation: *id001
    typeInfo: *id002
  - id: contactFieldId
    name: Contact Field ID
    type: string
    default: ''
    required: true
    description: ID of the contact field to update
    validation: *id015
    typeInfo: *id016
  - id: contactFieldTypeId
    name: Contact Field Type Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: data
    name: Content
    type: string
    default: ''
    required: true
    description: Content of the contact field - max 255 characters
    validation: *id031
    typeInfo: *id032
  - id: conversationId
    name: Conversation ID
    type: string
    default: ''
    required: true
    description: ID of the conversation to update
    validation: *id017
    typeInfo: *id018
  - id: contactFieldTypeId
    name: Contact Field Type Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: happenedAt
    name: Happened At
    type: dateTime
    default: ''
    required: true
    description: Date when the conversation happened
    validation: *id005
    typeInfo: *id006
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ID of the message to update
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - conversationMessage
          operation:
          - update
    typeInfo:
      type: string
      displayName: Message ID
      name: messageId
  - id: conversationId
    name: Conversation ID
    type: string
    default: ''
    required: true
    description: ID of the conversation whose message to update
    validation: *id017
    typeInfo: *id018
  - id: journalId
    name: Journal Entry ID
    type: string
    default: ''
    required: true
    description: ID of the journal entry to update
    validation: *id019
    typeInfo: *id020
  - id: noteId
    name: Note ID
    type: string
    default: ''
    required: true
    description: ID of the note to update
    validation: *id021
    typeInfo: *id022
  - id: reminderId
    name: Reminder ID
    type: string
    default: ''
    required: true
    description: ID of the reminder to update
    validation: *id023
    typeInfo: *id024
  - id: tagId
    name: Tag ID
    type: string
    default: ''
    required: true
    description: ID of the tag to update
    validation: *id025
    typeInfo: *id026
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the tag - max 250 characters
    validation: *id033
    typeInfo: *id034
- id: add
  name: Add
  description: ''
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to add a tag to
    validation: *id001
    typeInfo: *id002
  - id: tagsToAdd
    name: Tag Names or IDs
    type: multiOptions
    default: []
    required: true
    description: Tags to add to the contact. Choose from the list, or specify IDs
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - contactTag
          operation:
          - add
    typeInfo:
      type: multiOptions
      displayName: Tag Names or IDs
      name: tagsToAdd
      typeOptions:
        loadOptionsMethod: getTagsToAdd
      possibleValues: []
  - id: conversationId
    name: Conversation ID
    type: string
    default: ''
    required: true
    description: ID of the contact whose conversation
    validation: *id017
    typeInfo: *id018
  - id: content
    name: Content
    type: string
    default: ''
    required: true
    description: Content of the message
    validation: *id035
    typeInfo: *id036
  - id: writtenAt
    name: Written At
    type: dateTime
    default: ''
    required: true
    description: Date when the message was written
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - conversationMessage
          operation:
          - add
    typeInfo:
      type: dateTime
      displayName: Written At
      name: writtenAt
  - id: writtenByMe
    name: Written By
    type: options
    default: true
    required: true
    description: Author of the message
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - conversationMessage
          operation:
          - add
    typeInfo:
      type: options
      displayName: Written By
      name: writtenByMe
      possibleValues:
      - value: User
        name: User
        description: ''
      - value: Contact
        name: Contact
        description: ''
- id: remove
  name: Remove
  description: ''
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to remove the tag from
    validation: *id001
    typeInfo: *id002
  - id: tagsToRemove
    name: Tag Names or IDs
    type: multiOptions
    default: []
    required: true
    description: Tags to remove from the contact. Choose from the list, or specify
      IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - contactTag
          operation:
          - remove
    typeInfo:
      type: multiOptions
      displayName: Tag Names or IDs
      name: tagsToRemove
      typeOptions:
        loadOptionsMethod: getTagsToRemove
      possibleValues: []
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
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: updateFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/monicaCrm.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Monica CRM Node",
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
        "remove"
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
            "activity",
            "call",
            "contact",
            "contactField",
            "contactTag",
            "conversation",
            "conversationMessage",
            "journalEntry",
            "note",
            "reminder",
            "tag",
            "task"
          ],
          "default": "contact"
        },
        "operation": {
          "description": "Create a tag",
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
        "contactId": {
          "description": "ID of the contact to associate the reminder with",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "Title of the reminder - max 100,000 characters",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Description about the reminder - Max 100,000 characters",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "taskId": {
          "description": "ID of the task to update",
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
          "description": "ID of the contact to associate the reminder with",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "activityTypeId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "contacts": {
          "description": "Comma-separated list of IDs of the contacts to associate the activity with",
          "type": "string",
          "default": ""
        },
        "happenedAt": {
          "description": "Date when the conversation happened",
          "type": "string",
          "default": ""
        },
        "summary": {
          "description": "Brief description of the activity - max 255 characters",
          "type": "string",
          "default": ""
        },
        "activityId": {
          "description": "ID of the activity to update",
          "type": "string",
          "default": ""
        },
        "calledAt": {
          "description": "Date when the call happened",
          "type": "string",
          "default": ""
        },
        "content": {
          "description": "Content of the message",
          "type": "string",
          "default": ""
        },
        "callId": {
          "description": "ID of the call to update",
          "type": "string",
          "default": ""
        },
        "firstName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "genderId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "filters": {
          "description": "Search term to filter results by",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "contactFieldTypeId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "data": {
          "description": "Content of the contact field - max 255 characters",
          "type": "string",
          "default": ""
        },
        "contactFieldId": {
          "description": "ID of the contact field to update",
          "type": "string",
          "default": ""
        },
        "tagsToAdd": {
          "description": "Tags to add to the contact. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "tagsToRemove": {
          "description": "Tags to remove from the contact. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "conversationId": {
          "description": "ID of the conversation whose message to update",
          "type": "string",
          "default": ""
        },
        "writtenAt": {
          "description": "Date when the message was written",
          "type": "string",
          "default": ""
        },
        "writtenByMe": {
          "description": "Author of the message",
          "type": "string",
          "enum": [
            "User",
            "Contact"
          ],
          "default": true
        },
        "messageId": {
          "description": "ID of the message to update",
          "type": "string",
          "default": ""
        },
        "post": {
          "description": "Content of the journal entry - max 100,000 characters",
          "type": "string",
          "default": ""
        },
        "journalId": {
          "description": "ID of the journal entry to update",
          "type": "string",
          "default": ""
        },
        "body": {
          "description": "Body of the note - max 100,000 characters",
          "type": "string",
          "default": ""
        },
        "noteId": {
          "description": "ID of the note to update",
          "type": "string",
          "default": ""
        },
        "frequencyType": {
          "description": "Type of frequency of the reminder",
          "type": "string",
          "enum": [
            "one_time",
            "week",
            "month",
            "year"
          ],
          "default": "one_time"
        },
        "frequencyNumber": {
          "description": "Interval for the reminder",
          "type": "number",
          "default": 0
        },
        "initialDate": {
          "description": "Date of the reminder",
          "type": "string",
          "default": ""
        },
        "reminderId": {
          "description": "ID of the reminder to update",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "Name of the tag - max 250 characters",
          "type": "string",
          "default": ""
        },
        "tagId": {
          "description": "ID of the tag to update",
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
      "name": "monicaCrmApi",
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
