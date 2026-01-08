---
title: "Node: Gmail"
slug: "node-gmail"
version: "1"
updated: "2026-01-08"
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
| Get | `get` | Get a label |
| Get Many | `getAll` | Get many labels |

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a message |
| Get | `get` | Get a message |
| Get Many | `getAll` | Get many messages |
| Reply | `reply` | Reply to a message |
| Send | `send` | Send a message |

### Messagelabel Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a label to a message |
| Remove | `remove` | Remove a label from a message |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | draft | ✗ | Resource to operate on |  |

**Resource options:**

* **Draft** (`draft`)
* **Label** (`label`)
* **Message** (`message`)
* **Message Label** (`messageLabel`)

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
| HTML | `includeHtml` | boolean | False | ✗ | Whether the message should also be included as HTML |  |
| HTML Message | `htmlMessage` | string |  | ✓ | The HTML message body |  |
| Message | `message` | string |  | ✓ | The message body. If HTML formatted, then you have to add and activate the option "HTML content" in the "Additional Options" section. | e.g. Hello World! |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The email addresses of the recipients | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| To Email | `toList` | string | [] | The email addresses of the recipients |
| CC Email | `ccList` | string | [] | The email addresses of the copy recipients |
| BCC Email | `bccList` | string | [] | The email addresses of the blind copy recipients |
| Attachment | `attachmentsUi` | fixedCollection |  | Name of the binary property containing the data to be added to the email as an attachment. Multiple properties can be set separated by comma. |

</details>

| Name | `name` | string |  | ✓ | Label Name | e.g. invoices |  |
| Label List Visibility | `labelListVisibility` | options | labelShow | ✓ | The visibility of the label in the label list in the Gmail web interface |  |

**Label List Visibility options:**

* **Hide** (`labelHide`)
* **Show** (`labelShow`)
* **Show If Unread** (`labelShowIfUnread`)

| Message List Visibility | `messageListVisibility` | options | show | ✓ | The visibility of messages with this label in the message list in the Gmail web interface |  |

**Message List Visibility options:**

* **Hide** (`hide`)
* **Show** (`show`)


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Draft ID | `messageId` | string |  | ✓ | e.g. r-3254521568507167962 |  |
| Label ID | `labelId` | string |  | ✓ | The ID of the label |  |
| Message ID | `messageId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Draft ID | `messageId` | string |  | ✓ | e.g. r-3254521568507167962 |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" |
| Format | `format` | options | resolved | Returns the full email message data with body content parsed in the payload field |

</details>

| Label ID | `labelId` | string |  | ✓ | The ID of the label |  |
| Message ID | `messageId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Returns the full email message data with body content parsed in the payload field | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Format | `format` | options | resolved | Returns the full email message data with body content parsed in the payload field |
| Attachment Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" |
| Format | `format` | options | resolved | Returns the full email message data with body content parsed in the payload field |
| Include Spam and Trash | `includeSpamTrash` | boolean | False | Whether to include messages from SPAM and TRASH in the results |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0". | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0". |
| Format | `format` | options | resolved | Returns the full email message data with body content parsed in the payload field |
| Include Spam and Trash | `includeSpamTrash` | boolean | False | Whether to include messages from SPAM and TRASH in the results |
| Label Names or IDs | `labelIds` | multiOptions | [] | Only return messages with labels that match all of the specified label IDs. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Query | `q` | string |  | Only return messages matching the specified query. Supports the same query format as the Gmail search box. For example, "from:someuser@example.com rfc822msgid:&lt;somemsgid@example.com&gt; is:unread". Parameter cannot be used when accessing the api using the gmail.metadata scope. |

</details>


### Reply parameters (`reply`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Thread ID | `threadId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |
| Message ID | `messageId` | string |  | ✓ | e.g. CAHNQoFsC6JMMbOBJgtjsqN0eEc+gDg2a=SQj-tWUebQeHMDgqQ@mail.gmail.com |  |
| Subject | `subject` | string |  | ✓ | e.g. Hello World! |  |
| HTML | `includeHtml` | boolean | False | ✗ | Whether the message should also be included as HTML |  |
| HTML Message | `htmlMessage` | string |  | ✓ | The HTML message body |  |
| Message | `message` | string |  | ✓ | Plain text message body |  |
| To Email | `toList` | string | [] | ✓ | The email addresses of the recipients | e.g. info@example.com |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Add the field name from the input node. Multiple properties can be set separated by comma. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment | `attachmentsUi` | fixedCollection |  | Add the field name from the input node. Multiple properties can be set separated by comma. |
| BCC Email | `bccList` | string | [] | The email addresses of the blind copy recipients |
| CC Email | `ccList` | string | [] | The email addresses of the copy recipients |
| Override Sender Name | `senderName` | string |  | The name displayed in your contacts inboxes. It has to be in the format: "Display-Name &#60;name@gmail.com&#62;". The email address has to match the email address of the logged in user for the API. |

</details>


### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Subject | `subject` | string |  | ✓ | e.g. Hello World! |  |
| HTML | `includeHtml` | boolean | False | ✗ | Whether the message should also be included as HTML |  |
| HTML Message | `htmlMessage` | string |  | ✓ | The HTML message body |  |
| Message | `message` | string |  | ✓ | Plain text message body |  |
| To Email | `toList` | string | [] | ✓ | The email addresses of the recipients | e.g. info@example.com |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Add the field name from the input node. Multiple properties can be set separated by comma. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment | `attachmentsUi` | fixedCollection |  | Add the field name from the input node. Multiple properties can be set separated by comma. |
| BCC Email | `bccList` | string | [] | The email addresses of the blind copy recipients |
| CC Email | `ccList` | string | [] | The email addresses of the copy recipients |
| Override Sender Name | `senderName` | string |  | The name displayed in your contacts inboxes. It has to be in the format: "Display-Name &#60;name@gmail.com&#62;". The email address has to match the email address of the logged in user for the API. |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |
| Label Names or IDs | `labelIds` | multiOptions | [] | ✓ | The ID of the label. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | e.g. 172ce2c4a72cc243 |  |
| Label Names or IDs | `labelIds` | multiOptions | [] | ✓ | The ID of the label. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

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
node: gmail
displayName: Gmail
description: Consume the Gmail API
version: '1'
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
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - reply
          - send
    typeInfo: &id010
      type: string
      displayName: Subject
      name: subject
  - id: includeHtml
    name: HTML
    type: boolean
    default: false
    required: false
    description: Whether the message should also be included as HTML
    validation: &id011
      displayOptions:
        show:
          resource:
          - message
          operation:
          - send
          - reply
    typeInfo: &id012
      type: boolean
      displayName: HTML
      name: includeHtml
  - id: htmlMessage
    name: HTML Message
    type: string
    default: ''
    required: true
    description: The HTML message body
    validation: &id013
      required: true
      displayOptions:
        show:
          includeHtml:
          - true
          resource:
          - message
          operation:
          - reply
          - send
    typeInfo: &id014
      type: string
      displayName: HTML Message
      name: htmlMessage
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: The message body. If HTML formatted, then you have to add and activate
      the option "HTML content" in the "Additional Options" section.
    placeholder: Hello World!
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - reply
          - send
    typeInfo: &id016
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
  - id: labelListVisibility
    name: Label List Visibility
    type: options
    default: labelShow
    required: true
    description: The visibility of the label in the label list in the Gmail web interface
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - label
          operation:
          - create
    typeInfo:
      type: options
      displayName: Label List Visibility
      name: labelListVisibility
      possibleValues:
      - value: labelHide
        name: Hide
        description: ''
      - value: labelShow
        name: Show
        description: ''
      - value: labelShowIfUnread
        name: Show If Unread
        description: ''
  - id: messageListVisibility
    name: Message List Visibility
    type: options
    default: show
    required: true
    description: The visibility of messages with this label in the message list in
      the Gmail web interface
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - label
          operation:
          - create
    typeInfo:
      type: options
      displayName: Message List Visibility
      name: messageListVisibility
      possibleValues:
      - value: hide
        name: Hide
        description: ''
      - value: show
        name: Show
        description: ''
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
      required: true
      displayOptions:
        show:
          resource:
          - messageLabel
          operation:
          - add
          - remove
    typeInfo: &id002
      type: string
      displayName: Message ID
      name: messageId
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
    validation: &id005
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - message
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - message
          returnAll:
          - false
    typeInfo: &id008
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
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: reply
  name: Reply
  description: ''
  params:
  - id: threadId
    name: Thread ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: 172ce2c4a72cc243
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - reply
    typeInfo:
      type: string
      displayName: Thread ID
      name: threadId
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: CAHNQoFsC6JMMbOBJgtjsqN0eEc+gDg2a=SQj-tWUebQeHMDgqQ@mail.gmail.com
    validation: *id001
    typeInfo: *id002
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: ''
    placeholder: Hello World!
    validation: *id009
    typeInfo: *id010
  - id: includeHtml
    name: HTML
    type: boolean
    default: false
    required: false
    description: Whether the message should also be included as HTML
    validation: *id011
    typeInfo: *id012
  - id: htmlMessage
    name: HTML Message
    type: string
    default: ''
    required: true
    description: The HTML message body
    validation: *id013
    typeInfo: *id014
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: Plain text message body
    validation: *id015
    typeInfo: *id016
  - id: toList
    name: To Email
    type: string
    default: &id017 []
    required: true
    description: The email addresses of the recipients
    placeholder: info@example.com
    validation: &id018
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - reply
          - send
    typeInfo: &id019
      type: string
      displayName: To Email
      name: toList
      typeOptions:
        multipleValues: true
- id: send
  name: Send
  description: ''
  params:
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: ''
    placeholder: Hello World!
    validation: *id009
    typeInfo: *id010
  - id: includeHtml
    name: HTML
    type: boolean
    default: false
    required: false
    description: Whether the message should also be included as HTML
    validation: *id011
    typeInfo: *id012
  - id: htmlMessage
    name: HTML Message
    type: string
    default: ''
    required: true
    description: The HTML message body
    validation: *id013
    typeInfo: *id014
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: Plain text message body
    validation: *id015
    typeInfo: *id016
  - id: toList
    name: To Email
    type: string
    default: *id017
    required: true
    description: The email addresses of the recipients
    placeholder: info@example.com
    validation: *id018
    typeInfo: *id019
- id: add
  name: Add
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
    default: &id020 []
    required: true
    description: The ID of the label. Choose from the list, or specify IDs using an
      <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id021
      required: true
      displayOptions:
        show:
          resource:
          - messageLabel
          operation:
          - add
          - remove
    typeInfo: &id022
      type: multiOptions
      displayName: Label Names or IDs
      name: labelIds
      typeOptions:
        loadOptionsMethod: getLabels
      possibleValues: []
- id: remove
  name: Remove
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
    default: *id020
    required: true
    description: The ID of the label. Choose from the list, or specify IDs using an
      <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id021
    typeInfo: *id022
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: messageId
    text: r-3254521568507167962
  - field: subject
    text: Hello World!
  - field: message
    text: Hello World!
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: name
    text: invoices
  - field: messageId
    text: 172ce2c4a72cc243
  - field: threadId
    text: 172ce2c4a72cc243
  - field: messageId
    text: CAHNQoFsC6JMMbOBJgtjsqN0eEc+gDg2a=SQj-tWUebQeHMDgqQ@mail.gmail.com
  - field: subject
    text: Hello World!
  - field: toList
    text: info@example.com
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: messageId
    text: 172ce2c4a72cc243
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
  "$id": "https://n8n.io/schemas/nodes/gmail.json",
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
        "reply",
        "send",
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
            "oAuth2",
            "serviceAccount"
          ],
          "default": "oAuth2"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "draft",
            "label",
            "message",
            "messageLabel"
          ],
          "default": "draft"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "add",
            "remove"
          ],
          "default": "add"
        },
        "messageId": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "172ce2c4a72cc243"
          ]
        },
        "subject": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Hello World!"
          ]
        },
        "includeHtml": {
          "description": "Whether the message should also be included as HTML",
          "type": "boolean",
          "default": false
        },
        "htmlMessage": {
          "description": "The HTML message body",
          "type": "string",
          "default": ""
        },
        "message": {
          "description": "Plain text message body",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is \"attachment_\" the first attachment is saved to \"attachment_0\".",
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
          "default": 10
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
        "labelListVisibility": {
          "description": "The visibility of the label in the label list in the Gmail web interface",
          "type": "string",
          "enum": [
            "labelHide",
            "labelShow",
            "labelShowIfUnread"
          ],
          "default": "labelShow"
        },
        "messageListVisibility": {
          "description": "The visibility of messages with this label in the message list in the Gmail web interface",
          "type": "string",
          "enum": [
            "hide",
            "show"
          ],
          "default": "show"
        },
        "threadId": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "172ce2c4a72cc243"
          ]
        },
        "toList": {
          "description": "The email addresses of the recipients",
          "type": "string",
          "default": [],
          "examples": [
            "info@example.com"
          ]
        },
        "labelIds": {
          "description": "The ID of the label. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
