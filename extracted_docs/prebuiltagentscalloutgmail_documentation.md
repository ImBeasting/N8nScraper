---
title: "Node: Gmail"
slug: "node-prebuiltagentscalloutgmail"
version: "['2', '2.1']"
updated: "2025-11-13"
summary: "Consume the Gmail API"
node_type: "regular"
group: "['transform']"
---

# Node: Gmail

**Purpose.** Consume the Gmail API
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:gmail.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleApi**: N/A
- **gmailOAuth2**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **threadNotice** when resource=['draft'], operation=['create']: To reply to an existing thread, specify the exact subject title of that thread.
- **filtersNotice** when operation=['getAll'], resource=['message'], returnAll=[True]: Fetching a lot of messages may take a long time. Consider using filters to speed things up
- **filtersNotice** when operation=['getAll'], resource=['thread'], returnAll=[True]: Fetching a lot of messages may take a long time. Consider using filters to speed things up

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleApi` | ✓ | {'show': {'authentication': ['serviceAccount']}} |
| `gmailOAuth2` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Draft Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a draft |
| Delete | `delete` | Delete a draft |
| Get | `get` | Get a draft |
| Get Many | `getAll` | Get many drafts |

### Label Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a label |
| Delete | `delete` | Delete a label |
| Get | `get` | Get a label info |
| Get Many | `getAll` | Get many labels |

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Label | `addLabels` | Add label to message |
| Delete | `delete` | Delete a message |
| Get | `get` | Get a message |
| Get Many | `getAll` | Get many messages |
| Mark as Read | `markAsRead` | Mark a message as read |
| Mark as Unread | `markAsUnread` | Mark a message as unread |
| Remove Label | `removeLabels` | Remove label from message |
| Reply | `reply` | Reply to a message |
| Send | `send` | Send a message |
| Send and Wait for Response | `` | Send message and wait for response |

### Thread Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Label | `addLabels` | Add label to thread |
| Delete | `delete` | Delete a thread |
| Get | `get` | Get a thread |
| Get Many | `getAll` | Get many threads |
| Remove Label | `removeLabels` | Remove label from thread |
| Reply | `reply` | Reply to a message |
| Trash | `trash` | Trash a thread |
| Untrash | `untrash` | Untrash a thread |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✗ | Resource to operate on |  |

**Resource options:**

* **Message** (`message`)
* **Label** (`label`)
* **Draft** (`draft`)
* **Thread** (`thread`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create a draft
* **Delete** (`delete`) - Delete a draft
* **Get** (`get`) - Get a draft
* **Get Many** (`getAll`) - Get many drafts

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Subject | `subject` | string |  | ✓ | e.g. Hello World! |  |
| Email Type | `emailType` | options | text | ✓ |  | email |

**Email Type options:**

* **HTML** (`html`)
* **Text** (`text`)

| Message | `message` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | Add the field name from the input node. Multiple properties can be set separated by comma. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `attachmentsUi` | fixedCollection |  | Add the field name from the input node. Multiple properties can be set separated by comma. |
| BCC | `bccList` | string |  | The email addresses of the blind copy recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com. |
| CC | `ccList` | string |  | The email addresses of the copy recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com. |
| From Alias Name or ID | `fromAlias` | options |  | Select the alias to send the email from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Send Replies To | `replyTo` | string |  | The email address that the reply message is sent to |
| Thread ID | `threadId` | string |  | The identifier of the thread to attach the draft |
| To Email | `sendTo` | string |  | The email addresses of the recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com. |

</details>

| Name | `name` | string |  | ✓ | Label Name | e.g. invoices |  |
| Options | `options` | collection | {} | ✗ | The visibility of the label in the label list in the Gmail web interface | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Label List Visibility | `labelListVisibility` | options | labelShow | The visibility of the label in the label list in the Gmail web interface |
| Message List Visibility | `messageListVisibility` | options | show | The visibility of messages with this label in the message list in the Gmail web interface |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Draft ID | `messageId` | string |  | ✓ | e.g. r-3254521568507167962 |  |
| Label ID | `labelId` | string |  | ✓ | The ID of the label |  |
| Message ID | `messageId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |
| Thread ID | `threadId` | string |  | ✓ | The ID of the thread you are operating on |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Draft ID | `messageId` | string |  | ✓ | e.g. r-3254521568507167962 |  |
| Options | `options` | collection | {} | ✗ | Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is 'attachment_' the first attachment is saved to 'attachment_0'. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is 'attachment_' the first attachment is saved to 'attachment_0'. |
| Download Attachments | `downloadAttachments` | boolean | False | Whether the draft's attachments will be downloaded |

</details>

| Label ID | `labelId` | string |  | ✓ | The ID of the label |  |
| Message ID | `messageId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is 'attachment_' the first attachment is saved to 'attachment_0'. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is 'attachment_' the first attachment is saved to 'attachment_0'. |
| Download Attachments | `downloadAttachments` | boolean | False | Whether the email's attachments will be downloaded and included in the output |

</details>

| Thread ID | `threadId` | string |  | ✓ | The ID of the thread you are operating on |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Whether to return only thread messages | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Return Only Messages | `returnOnlyMessages` | boolean | True | Whether to return only thread messages |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is 'attachment_' the first attachment is saved to 'attachment_0'. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is 'attachment_' the first attachment is saved to 'attachment_0'. |
| Download Attachments | `downloadAttachments` | boolean | False | Whether the draft's attachments will be downloaded |
| Include Spam and Trash | `includeSpamTrash` | boolean | False | Whether to include messages from SPAM and TRASH in the results |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Filters | `filters` | collection | {} | ✗ | Whether to include messages from SPAM and TRASH in the results | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Spam and Trash | `includeSpamTrash` | boolean | False | Whether to include messages from SPAM and TRASH in the results |
| Label Names or IDs | `labelIds` | multiOptions | [] | Only return messages with labels that match all of the specified label IDs. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Search | `q` | string |  | Only return messages matching the specified query |
| Read Status | `readStatus` | options | unread |  |
| Received After | `receivedAfter` | dateTime |  | Get all emails received after the specified date. In an expression you can set date using string in ISO format or a timestamp in miliseconds. |
| Received Before | `receivedBefore` | dateTime |  | Get all emails received before the specified date. In an expression you can set date using string in ISO format or a timestamp in miliseconds. |
| Sender | `sender` | string |  | Sender name or email to filter by |

</details>

| Options | `options` | collection | {} | ✗ | Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is 'attachment_' the first attachment is saved to 'attachment_0'. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is 'attachment_' the first attachment is saved to 'attachment_0'. |
| Download Attachments | `downloadAttachments` | boolean | False | Whether the email's attachments will be downloaded and included in the output |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Filters | `filters` | collection | {} | ✗ | Whether to include threads from SPAM and TRASH in the results | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Spam and Trash | `includeSpamTrash` | boolean | False | Whether to include threads from SPAM and TRASH in the results |
| Label ID Names or IDs | `labelIds` | multiOptions | [] | Only return threads with labels that match all of the specified label IDs. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Search | `q` | string |  | Only return messages matching the specified query |
| Read Status | `readStatus` | options | unread |  |
| Received After | `receivedAfter` | dateTime |  | Get all emails received after the specified date. In an expression you can set date using string in ISO format or a timestamp in miliseconds. |
| Received Before | `receivedBefore` | dateTime |  | Get all emails received before the specified date. In an expression you can set date using string in ISO format or a timestamp in miliseconds. |

</details>


### Add Label parameters (`addLabels`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |
| Label Names or IDs | `labelIds` | multiOptions | [] | ✓ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Thread ID | `threadId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |
| Label Names or IDs | `labelIds` | multiOptions | [] | ✓ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Mark as Read parameters (`markAsRead`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |

### Mark as Unread parameters (`markAsUnread`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |

### Remove Label parameters (`removeLabels`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |
| Label Names or IDs | `labelIds` | multiOptions | [] | ✓ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Thread ID | `threadId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |
| Label Names or IDs | `labelIds` | multiOptions | [] | ✓ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Reply parameters (`reply`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |
| Email Type | `emailType` | options | html | ✓ |  | email |

**Email Type options:**

* **Text** (`text`)
* **HTML** (`html`)

| Email Type | `emailType` | options | html | ✓ |  | email |

**Email Type options:**

* **Text** (`text`)
* **HTML** (`html`)

| Message | `message` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | Whether to include the phrase “This email was sent automatically with n8n” to the end of the email | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `attachmentsUi` | fixedCollection | data | Add the field name from the input node. Multiple properties can be set separated by comma. |
| BCC | `bccList` | string |  | The email addresses of the blind copy recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com. |
| CC | `ccList` | string |  | The email addresses of the copy recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com. |
| Sender Name | `senderName` | string |  | The name that will be shown in recipients' inboxes |
| Send Replies To | `replyTo` | string |  | The email address that the reply message is sent to |
| Reply to Sender Only | `replyToSenderOnly` | boolean | False | Whether to reply to the sender only or to the entire list of recipients |

</details>

| Thread ID | `threadId` | string |  | ✓ | The ID of the thread you are operating on |  |
| Message Snippet or ID | `messageId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Email Type | `emailType` | options | text | ✓ |  | email |

**Email Type options:**

* **Text** (`text`)
* **HTML** (`html`)

| Message | `message` | string |  | ✓ | e.g. Get better Text and Expressions writing experience by using the expression editor |  |
| Options | `options` | collection | {} | ✗ | Add the field name from the input node. Multiple properties can be set separated by comma. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `attachmentsUi` | fixedCollection |  | Add the field name from the input node. Multiple properties can be set separated by comma. |
| BCC | `bccList` | string |  | The email addresses of the blind copy recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com. |
| CC | `ccList` | string |  | The email addresses of the copy recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com. |
| Sender Name | `senderName` | string |  | The name displayed in your contacts inboxes |
| Reply to Sender Only | `replyToSenderOnly` | boolean | False | Whether to reply to the sender only or to the entire list of recipients |
| Reply to Recipients Only | `replyToRecipientsOnly` | boolean | False | Whether to exclude the sender from the reply |

</details>


### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| To | `sendTo` | string |  | ✓ | The email addresses of the recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com. | e.g. info@example.com |  |
| Subject | `subject` | string |  | ✓ | e.g. Hello World! |  |
| Email Type | `emailType` | options | html | ✓ |  | email |

**Email Type options:**

* **Text** (`text`)
* **HTML** (`html`)

| Email Type | `emailType` | options | html | ✓ |  | email |

**Email Type options:**

* **Text** (`text`)
* **HTML** (`html`)

| Message | `message` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | Whether to include the phrase “This email was sent automatically with n8n” to the end of the email | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `attachmentsUi` | fixedCollection | data | Add the field name from the input node. Multiple properties can be set separated by comma. |
| BCC | `bccList` | string |  | The email addresses of the blind copy recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com. |
| CC | `ccList` | string |  | The email addresses of the copy recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com. |
| Sender Name | `senderName` | string |  | The name that will be shown in recipients' inboxes |
| Send Replies To | `replyTo` | string |  | The email address that the reply message is sent to |
| Reply to Sender Only | `replyToSenderOnly` | boolean | False | Whether to reply to the sender only or to the entire list of recipients |

</details>


### Trash parameters (`trash`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Thread ID | `threadId` | string |  | ✓ | The ID of the thread you are operating on |  |

### Untrash parameters (`untrash`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Thread ID | `threadId` | string |  | ✓ | The ID of the thread you are operating on |  |

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
node: preBuiltAgentsCalloutGmail
displayName: Gmail
description: Consume the Gmail API
version:
- '2'
- '2.1'
nodeType: regular
group:
- transform
credentials:
- name: googleApi
  required: true
- name: gmailOAuth2
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: ''
    placeholder: Hello World!
    validation: &id021
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - send
    typeInfo: &id022
      type: string
      displayName: Subject
      name: subject
  - id: emailType
    name: Email Type
    type: options
    default: text
    required: true
    description: ''
    validation: &id017
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - thread
          operation:
          - reply
    typeInfo: &id018
      type: options
      displayName: Email Type
      name: emailType
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
    description: ''
    validation: &id019
      required: true
      displayOptions:
        show:
          resource:
          - thread
          operation:
          - reply
    typeInfo: &id020
      type: string
      displayName: Message
      name: message
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Label Name
    placeholder: invoices
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
      name: name
- id: delete
  name: Delete
  description: ''
  params:
  - id: messageId
    name: Draft ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: r-3254521568507167962
    validation: &id001
      displayOptions:
        show:
          resource:
          - thread
          operation:
          - reply
    typeInfo: &id002
      type: options
      displayName: Message Snippet or ID
      name: messageId
      typeOptions:
        loadOptionsMethod: getThreadMessages
      possibleValues: []
  - id: labelId
    name: Label ID
    type: string
    default: ''
    required: true
    description: The ID of the label
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - label
          operation:
          - get
          - delete
    typeInfo: &id004
      type: string
      displayName: Label ID
      name: labelId
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: 172ce2c4a72cc243
    validation: *id001
    typeInfo: *id002
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: The ID of the thread you are operating on
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - thread
          operation:
          - addLabels
          - removeLabels
    typeInfo: &id006
      type: string
      displayName: Thread ID
      name: threadId
- id: get
  name: Get
  description: ''
  params:
  - id: messageId
    name: Draft ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: r-3254521568507167962
    validation: *id001
    typeInfo: *id002
  - id: labelId
    name: Label ID
    type: string
    default: ''
    required: true
    description: The ID of the label
    validation: *id003
    typeInfo: *id004
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: 172ce2c4a72cc243
    validation: *id001
    typeInfo: *id002
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id007
      displayOptions:
        show:
          operation:
          - get
          resource:
          - thread
    typeInfo: &id008
      type: boolean
      displayName: Simplify
      name: simple
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: The ID of the thread you are operating on
    validation: *id005
    typeInfo: *id006
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id009
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - thread
    typeInfo: &id010
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id011
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - thread
          returnAll:
          - false
    typeInfo: &id012
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
    validation: *id009
    typeInfo: *id010
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id009
    typeInfo: *id010
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id009
    typeInfo: *id010
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
- id: addLabels
  name: Add Label
  description: ''
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: 172ce2c4a72cc243
    validation: *id001
    typeInfo: *id002
  - id: labelIds
    name: Label Names or IDs
    type: multiOptions
    default: &id015 []
    required: true
    description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - thread
          operation:
          - addLabels
          - removeLabels
    typeInfo: &id014
      type: multiOptions
      displayName: Label Names or IDs
      name: labelIds
      typeOptions:
        loadOptionsMethod: getLabels
      possibleValues: []
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: 172ce2c4a72cc243
    validation: *id005
    typeInfo: *id006
  - id: labelIds
    name: Label Names or IDs
    type: multiOptions
    default: &id016 []
    required: true
    description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
- id: markAsRead
  name: Mark as Read
  description: ''
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: 172ce2c4a72cc243
    validation: *id001
    typeInfo: *id002
- id: markAsUnread
  name: Mark as Unread
  description: ''
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: 172ce2c4a72cc243
    validation: *id001
    typeInfo: *id002
- id: removeLabels
  name: Remove Label
  description: ''
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: 172ce2c4a72cc243
    validation: *id001
    typeInfo: *id002
  - id: labelIds
    name: Label Names or IDs
    type: multiOptions
    default: *id015
    required: true
    description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: 172ce2c4a72cc243
    validation: *id005
    typeInfo: *id006
  - id: labelIds
    name: Label Names or IDs
    type: multiOptions
    default: *id016
    required: true
    description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
- id: reply
  name: Reply
  description: ''
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: 172ce2c4a72cc243
    validation: *id001
    typeInfo: *id002
  - id: emailType
    name: Email Type
    type: options
    default: html
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: emailType
    name: Email Type
    type: options
    default: html
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: ''
    validation: *id019
    typeInfo: *id020
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: The ID of the thread you are operating on
    validation: *id005
    typeInfo: *id006
  - id: messageId
    name: Message Snippet or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: emailType
    name: Email Type
    type: options
    default: text
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: ''
    hint: Get better Text and Expressions writing experience by using the expression
      editor
    validation: *id019
    typeInfo: *id020
- id: send
  name: Send
  description: ''
  params:
  - id: sendTo
    name: To
    type: string
    default: ''
    required: true
    description: The email addresses of the recipients. Multiple addresses can be
      separated by a comma. e.g. jay@getsby.com, jon@smith.com.
    placeholder: info@example.com
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - send
    typeInfo:
      type: string
      displayName: To
      name: sendTo
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: ''
    placeholder: Hello World!
    validation: *id021
    typeInfo: *id022
  - id: emailType
    name: Email Type
    type: options
    default: html
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: emailType
    name: Email Type
    type: options
    default: html
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: ''
    validation: *id019
    typeInfo: *id020
- id: ''
  name: Send and Wait for Response
  description: ''
- id: trash
  name: Trash
  description: ''
  params:
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: The ID of the thread you are operating on
    validation: *id005
    typeInfo: *id006
- id: untrash
  name: Untrash
  description: ''
  params:
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: The ID of the thread you are operating on
    validation: *id005
    typeInfo: *id006
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices:
  - name: threadNotice
    text: To reply to an existing thread, specify the exact subject title of that
      thread.
    conditions:
      show:
        resource:
        - draft
        operation:
        - create
  - name: filtersNotice
    text: Fetching a lot of messages may take a long time. Consider using filters
      to speed things up
    conditions:
      show:
        operation:
        - getAll
        resource:
        - message
        returnAll:
        - true
  - name: filtersNotice
    text: Fetching a lot of messages may take a long time. Consider using filters
      to speed things up
    conditions:
      show:
        operation:
        - getAll
        resource:
        - thread
        returnAll:
        - true
  tooltips: []
  placeholders:
  - field: sendTo
    text: e.g. info@example.com
  - field: messageId
    text: r-3254521568507167962
  - field: subject
    text: Hello World!
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: name
    text: invoices
  - field: options
    text: Add option
  - field: messageId
    text: 172ce2c4a72cc243
  - field: messageId
    text: 172ce2c4a72cc243
  - field: sendTo
    text: info@example.com
  - field: subject
    text: Hello World!
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: filters
    text: Add Filter
  - field: options
    text: Add option
  - field: messageId
    text: 172ce2c4a72cc243
  - field: options
    text: Add option
  - field: options
    text: Add Field
  - field: filters
    text: Add Filter
  - field: threadId
    text: 172ce2c4a72cc243
  hints:
  - field: options
    text: The name of the field with the attachment in the node input
  - field: filters
    text: Use the same format as in the Gmail search box. <a href="https://support.google.com/mail/answer/7190?hl=en">More
      info</a>.
  - field: message
    text: Get better Text and Expressions writing experience by using the expression
      editor
  - field: filters
    text: Use the same format as in the Gmail search box. <a href="https://support.google.com/mail/answer/7190?hl=en">More
      info</a>.
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
  "$id": "https://n8n.io/schemas/nodes/preBuiltAgentsCalloutGmail.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Gmail Node",
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
        "addLabels",
        "markAsRead",
        "markAsUnread",
        "removeLabels",
        "reply",
        "send",
        "",
        "trash",
        "untrash"
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
            "oAuth2",
            "serviceAccount"
          ],
          "default": "oAuth2"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "message",
            "label",
            "draft",
            "thread"
          ],
          "default": "message"
        },
        "sendTo": {
          "description": "The email addresses of the recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com.",
          "type": "string",
          "default": "",
          "examples": [
            "info@example.com"
          ]
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "addLabels",
            "delete",
            "get",
            "getAll",
            "removeLabels",
            "reply",
            "trash",
            "untrash"
          ],
          "default": "getAll"
        },
        "messageId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "subject": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Hello World!"
          ]
        },
        "emailType": {
          "description": "",
          "type": "string",
          "enum": [
            "text",
            "html"
          ],
          "default": "text",
          "format": "email"
        },
        "message": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Whether to return only thread messages",
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
          "default": 50
        },
        "name": {
          "description": "Label Name",
          "type": "string",
          "default": "",
          "examples": [
            "invoices"
          ]
        },
        "labelId": {
          "description": "The ID of the label",
          "type": "string",
          "default": ""
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "filters": {
          "description": "Whether to include threads from SPAM and TRASH in the results",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "labelIds": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "appendAttribution": {
          "description": "",
          "type": "boolean",
          "default": true
        },
        "threadId": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "172ce2c4a72cc243"
          ]
        },
        "default": {
          "description": "",
          "type": "string"
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
      "name": "googleApi",
      "required": true
    },
    {
      "name": "gmailOAuth2",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2', '2.1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
