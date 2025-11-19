---
title: "Node: Microsoft Outlook"
slug: "node-microsoftoutlook"
version: "1"
updated: "2025-11-13"
summary: "Consume Microsoft Outlook API"
node_type: "regular"
group: "['transform']"
---

# Node: Microsoft Outlook

**Purpose.** Consume Microsoft Outlook API
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:outlook.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftOutlookOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `microsoftOutlookOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Draft Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new email draft |
| Delete | `delete` | Delete a draft |
| Get | `get` | Get a single draft |
| Send | `send` | Send an existing draft message |
| Update | `update` | Update a draft |

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a message |
| Get | `get` | Get a single message |
| Get Many | `getAll` | Get many messages in the signed-in user's mailbox |
| Get MIME Content | `getMime` | Get MIME content of a message |
| Move | `move` | Move a message |
| Reply | `reply` | Create reply to a message |
| Send | `send` | Send a message |
| Update | `update` | Update a message |

### Messageattachment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add an attachment to a message |
| Download | `download` | Download attachment content |
| Get | `get` | Get an attachment from a message |
| Get Many | `getAll` | Get many message's attachments |

### Folder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new mail folder in the root folder of the user's mailbox |
| Delete | `delete` | Delete a folder |
| Get | `get` | Get a single folder details |
| Get Children | `getChildren` | Lists all child folders under the folder |
| Get Many | `getAll` | Get many folders under the root folder of the signed-in user |

### Foldermessage Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many messages in a folder |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✗ | Resource to operate on |  |

**Resource options:**

* **Draft** (`draft`)
* **Folder** (`folder`)
* **Folder Message** (`folderMessage`)
* **Message** (`message`)
* **Message Attachment** (`messageAttachment`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a new email draft |  |

**Operation options:**

* **Create** (`create`) - Create a new email draft
* **Delete** (`delete`) - Delete a draft
* **Get** (`get`) - Get a single draft
* **Send** (`send`) - Send an existing draft message
* **Update** (`update`) - Update a draft

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Subject | `subject` | string |  | ✗ | The subject of the message |  |
| Body Content | `bodyContent` | string |  | ✗ | Message body content |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the binary property containing the data to be added to the email as an attachment | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `attachments` | fixedCollection | {} | Name of the binary property containing the data to be added to the email as an attachment |
| BCC Recipients | `bccRecipients` | string |  | Email addresses of BCC recipients |
| Body Content Type | `bodyContentType` | options | html | Message body content type |
| Category Names or IDs | `categories` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| CC Recipients | `ccRecipients` | string |  | Email addresses of CC recipients |
| Custom Headers | `internetMessageHeaders` | fixedCollection | {} | Name of the header |
| From | `from` | string |  | The owner of the mailbox which the message is sent. Must correspond to the actual mailbox used. |
| Importance | `importance` | options | Low | The importance of the message |
| Read Receipt Requested | `isReadReceiptRequested` | boolean | False | Whether a read receipt is requested for the message |
| Recipients | `toRecipients` | string |  | Email addresses of recipients. Multiple can be added separated by comma. |
| Reply To | `replyTo` | string |  | Email addresses to use when replying |

</details>

| Subject | `subject` | string |  | ✗ | The subject of the message |  |
| Body Content | `bodyContent` | string |  | ✗ | Message body content |  |
| Type | `folderType` | options | folder | ✗ | Folder Type |  |

**Type options:**

* **Folder** (`folder`)
* **Search Folder** (`searchFolder`)

| Display Name | `displayName` | string |  | ✓ | Name of the folder |  |
| Include Nested Folders | `includeNestedFolders` | boolean | False | ✗ | Whether to include child folders in the search |  |
| Source Folder IDs | `sourceFolderIds` | string | [] | ✗ | The mailbox folders that should be mined |  |
| Filter Query | `filterQuery` | string |  | ✓ | The OData query to filter the messages |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Folder ID | `folderId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Attachment ID | `attachmentId` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields the response will contain. Multiple can be added separated by ,. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Fields the response will contain. Multiple can be added separated by ,. |
| Filter | `filter` | string |  | Microsoft Graph API OData $filter query |

</details>

| Folder ID | `folderId` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields the response will contain. Multiple can be added separated by ,. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Fields the response will contain. Multiple can be added separated by ,. |
| Filter | `filter` | string |  | Microsoft Graph API OData $filter query. Information about the syntax can be found <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">here</a>. |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" |
| Fields | `fields` | string |  | Fields the response will contain. Multiple can be added separated by comma. |
| Filter | `filter` | string |  | Microsoft Graph API OData $filter query. Information about the syntax can be found <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">here</a>. |

</details>


### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Email addresses of recipients. Mutiple can be set separated by comma. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Recipients | `recipients` | string |  | Email addresses of recipients. Mutiple can be set separated by comma. |

</details>

| Subject | `subject` | string |  | ✗ | The subject of the message |  |
| Body Content | `bodyContent` | string |  | ✗ | Message body content |  |
| Recipients | `toRecipients` | string |  | ✓ | Email addresses of recipients. Multiple can be added separated by comma. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the binary property containing the data to be added to the email as an attachment | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `attachments` | fixedCollection | {} | Name of the binary property containing the data to be added to the email as an attachment |
| BCC Recipients | `bccRecipients` | string |  | Email addresses of BCC recipients |
| Body Content Type | `bodyContentType` | options | html | Message body content type |
| Category Names or IDs | `categories` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| CC Recipients | `ccRecipients` | string |  | Email addresses of CC recipients |
| Custom Headers | `internetMessageHeaders` | fixedCollection | {} | Name of the header |
| From | `from` | string |  | The owner of the mailbox which the message is sent. Must correspond to the actual mailbox used. |
| Importance | `importance` | options | Low | The importance of the message |
| Read Receipt Requested | `isReadReceiptRequested` | boolean | False | Whether a read receipt is requested for the message |
| Recipients | `toRecipients` | string |  | Email addresses of recipients. Multiple can be added separated by comma. |
| Reply To | `replyTo` | string |  | Email addresses to use when replying |
| Save To Sent Items | `saveToSentItems` | boolean | True | Whether to save the message in Sent Items |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Folder ID | `folderId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Fields to update |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Display Name | `displayName` | string |  | Name of the folder |
| Filter Query | `filterQuery` | string |  | The OData query to filter the messages. Only for search folders. |
| Include Nested Folders | `includeNestedFolders` | boolean | False | Whether to include child folders in the search. Only for search folders. |
| Source Folder IDs | `sourceFolderIds` | string | [] | The mailbox folders that should be mined. Only for search folders. |

</details>

| Update Fields | `updateFields` | collection | {} | ✗ | Email addresses of BCC recipients | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| BCC Recipients | `bccRecipients` | string |  | Email addresses of BCC recipients |
| Body Content | `bodyContent` | string |  | Message body content |
| Body Content Type | `bodyContentType` | options | html | Message body content type |
| Category Names or IDs | `categories` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| CC Recipients | `ccRecipients` | string |  | Email addresses of CC recipients |
| Custom Headers | `internetMessageHeaders` | fixedCollection | {} | Name of the header |
| From | `from` | string |  | The owner of the mailbox which the message is sent. Must correspond to the actual mailbox used. |
| Importance | `importance` | options | Low | The importance of the message |
| Is Read | `isRead` | boolean | False | Whether the message has been read |
| Read Receipt Requested | `isReadReceiptRequested` | boolean | False | Whether a read receipt is requested for the message |
| Recipients | `toRecipients` | string |  | Email addresses of recipients. Multiple can be added separated by comma. |
| Reply To | `replyTo` | string |  | Email addresses to use when replying |
| Subject | `subject` | string |  | The subject of the message |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields the response will contain. Multiple can be added separated by ,. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Fields the response will contain. Multiple can be added separated by ,. |
| Filter | `filter` | string |  | Microsoft Graph API OData $filter query |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields the response will contain. Multiple can be added separated by ,. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Fields the response will contain. Multiple can be added separated by ,. |
| Filter | `filter` | string |  | Microsoft Graph API OData $filter query. Information about the syntax can be found <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">here</a>. |

</details>

| Folder ID | `folderId` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields the response will contain. Multiple can be added separated by ,. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Fields the response will contain. Multiple can be added separated by ,. |
| Filter | `filter` | string |  | Microsoft Graph API OData $filter query. Information about the syntax can be found <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">here</a>. |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" |
| Fields | `fields` | string |  | Fields the response will contain. Multiple can be added separated by comma. |
| Filter | `filter` | string |  | Microsoft Graph API OData $filter query. Information about the syntax can be found <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">here</a>. |

</details>


### Get MIME Content parameters (`getMime`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |

### Move parameters (`move`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Folder ID | `folderId` | string |  | ✓ | Target Folder ID |  |

### Reply parameters (`reply`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Reply Type | `replyType` | options | reply | ✓ |  |  |

**Reply Type options:**

* **Reply** (`reply`)
* **Reply All** (`replyAll`)

| Comment | `comment` | string |  | ✗ | A comment to include. Can be an empty string. |  |
| Send | `send` | boolean | True | ✗ | Whether to send the reply message directly. If not set, it will be saved as draft. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the binary property containing the data to be added to the email as an attachment | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `attachments` | fixedCollection | {} | Name of the binary property containing the data to be added to the email as an attachment |
| BCC Recipients | `bccRecipients` | string |  | Email addresses of BCC recipients |
| Body Content | `bodyContent` | string |  | Message body content |
| Body Content Type | `bodyContentType` | options | html | Message body content type |
| CC Recipients | `ccRecipients` | string |  | Email addresses of CC recipients |
| Custom Headers | `internetMessageHeaders` | fixedCollection | {} | Name of the header |
| From | `from` | string |  | The owner of the mailbox which the message is sent. Must correspond to the actual mailbox used. |
| Importance | `importance` | options | Low | The importance of the message |
| Read Receipt Requested | `isReadReceiptRequested` | boolean | False | Whether a read receipt is requested for the message |
| Recipients | `toRecipients` | string |  | Email addresses of recipients. Multiple can be added separated by comma. |
| Reply To | `replyTo` | string |  | Email addresses to use when replying |
| Subject | `subject` | string |  | The subject of the message |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Filename of the attachment. If not set will the file-name of the binary property be used, if it exists. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Name | `fileName` | string |  | Filename of the attachment. If not set will the file-name of the binary property be used, if it exists. |

</details>


### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ |  |  |
| Attachment ID | `attachmentId` | string |  | ✓ |  |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |

### Get Children parameters (`getChildren`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Folder ID | `folderId` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields the response will contain. Multiple can be added separated by ,. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Fields the response will contain. Multiple can be added separated by ,. |
| Filter | `filter` | string |  | Microsoft Graph API OData $filter query. Information about the syntax can be found <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">here</a>. |

</details>


---

## Load Options Methods

- `getCategories`
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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: microsoftOutlook
displayName: Microsoft Outlook
description: Consume Microsoft Outlook API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: microsoftOutlookOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a new email draft
  params:
  - id: subject
    name: Subject
    type: string
    default: ''
    required: false
    description: The subject of the message
    validation: &id001
      displayOptions:
        show:
          resource:
          - message
          operation:
          - create
          - send
    typeInfo: &id002
      type: string
      displayName: Subject
      name: subject
  - id: bodyContent
    name: Body Content
    type: string
    default: ''
    required: false
    description: Message body content
    validation: &id003
      displayOptions:
        show:
          resource:
          - message
          operation:
          - create
          - send
    typeInfo: &id004
      type: string
      displayName: Body Content
      name: bodyContent
  - id: subject
    name: Subject
    type: string
    default: ''
    required: false
    description: The subject of the message
    validation: *id001
    typeInfo: *id002
  - id: bodyContent
    name: Body Content
    type: string
    default: ''
    required: false
    description: Message body content
    validation: *id003
    typeInfo: *id004
  - id: folderType
    name: Type
    type: options
    default: folder
    required: false
    description: Folder Type
    validation:
      displayOptions:
        show:
          resource:
          - folder
          operation:
          - create
    typeInfo:
      type: options
      displayName: Type
      name: folderType
      possibleValues:
      - value: folder
        name: Folder
        description: ''
      - value: searchFolder
        name: Search Folder
        description: ''
  - id: displayName
    name: Display Name
    type: string
    default: ''
    required: true
    description: Name of the folder
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - folder
          operation:
          - create
    typeInfo:
      type: string
      displayName: Display Name
      name: displayName
  - id: includeNestedFolders
    name: Include Nested Folders
    type: boolean
    default: false
    required: false
    description: Whether to include child folders in the search
    validation:
      displayOptions:
        show:
          resource:
          - folder
          operation:
          - create
          folderType:
          - searchFolder
    typeInfo:
      type: boolean
      displayName: Include Nested Folders
      name: includeNestedFolders
  - id: sourceFolderIds
    name: Source Folder IDs
    type: string
    default: []
    required: false
    description: The mailbox folders that should be mined
    validation:
      displayOptions:
        show:
          resource:
          - folder
          operation:
          - create
          folderType:
          - searchFolder
    typeInfo:
      type: string
      displayName: Source Folder IDs
      name: sourceFolderIds
      typeOptions:
        multipleValues: true
  - id: filterQuery
    name: Filter Query
    type: string
    default: ''
    required: true
    description: The OData query to filter the messages
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - folder
          operation:
          - create
          folderType:
          - searchFolder
    typeInfo:
      type: string
      displayName: Filter Query
      name: filterQuery
- id: delete
  name: Delete
  description: Delete a draft
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - messageAttachment
          operation:
          - add
          - download
          - get
          - getAll
    typeInfo: &id006
      type: string
      displayName: Message ID
      name: messageId
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - folderMessage
          operation:
          - getAll
    typeInfo: &id008
      type: string
      displayName: Folder ID
      name: folderId
- id: get
  name: Get
  description: Get a single draft
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: attachmentId
    name: Attachment ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - messageAttachment
          operation:
          - download
          - get
    typeInfo: &id016
      type: string
      displayName: Attachment ID
      name: attachmentId
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
- id: send
  name: Send
  description: Send an existing draft message
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: subject
    name: Subject
    type: string
    default: ''
    required: false
    description: The subject of the message
    validation: *id001
    typeInfo: *id002
  - id: bodyContent
    name: Body Content
    type: string
    default: ''
    required: false
    description: Message body content
    validation: *id003
    typeInfo: *id004
  - id: toRecipients
    name: Recipients
    type: string
    default: ''
    required: true
    description: Email addresses of recipients. Multiple can be added separated by
      comma.
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
      displayName: Recipients
      name: toRecipients
- id: update
  name: Update
  description: Update a draft
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
- id: getAll
  name: Get Many
  description: Get many messages in the signed-in user's mailbox
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
          resource:
          - folderMessage
          operation:
          - getAll
    typeInfo: &id010
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id011
      displayOptions:
        show:
          resource:
          - folderMessage
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id012
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
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
    default: 100
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: true
    description: ''
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
- id: getMime
  name: Get MIME Content
  description: Get MIME content of a message
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - messageAttachment
          operation:
          - add
          - download
    typeInfo: &id014
      type: string
      displayName: Put Output File in Field
      name: binaryPropertyName
- id: move
  name: Move
  description: Move a message
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: true
    description: Target Folder ID
    validation: *id007
    typeInfo: *id008
- id: reply
  name: Reply
  description: Create reply to a message
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: replyType
    name: Reply Type
    type: options
    default: reply
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - reply
    typeInfo:
      type: options
      displayName: Reply Type
      name: replyType
      possibleValues:
      - value: reply
        name: Reply
        description: ''
      - value: replyAll
        name: Reply All
        description: ''
  - id: comment
    name: Comment
    type: string
    default: ''
    required: false
    description: A comment to include. Can be an empty string.
    validation:
      displayOptions:
        show:
          resource:
          - message
          operation:
          - reply
    typeInfo:
      type: string
      displayName: Comment
      name: comment
  - id: send
    name: Send
    type: boolean
    default: true
    required: false
    description: Whether to send the reply message directly. If not set, it will be
      saved as draft.
    validation:
      displayOptions:
        show:
          resource:
          - message
          operation:
          - reply
    typeInfo:
      type: boolean
      displayName: Send
      name: send
- id: add
  name: Add
  description: Add an attachment to a message
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: *id013
    typeInfo: *id014
- id: download
  name: Download
  description: Download attachment content
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: attachmentId
    name: Attachment ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: *id013
    typeInfo: *id014
- id: getChildren
  name: Get Children
  description: Lists all child folders under the folder
  params:
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: true
    description: ''
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
    default: 100
    required: false
    description: Max number of results to return
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
  notices: []
  tooltips: []
  placeholders:
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
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  hints:
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/microsoftOutlook.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft Outlook Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "get",
        "send",
        "update",
        "getAll",
        "getMime",
        "move",
        "reply",
        "add",
        "download",
        "getChildren"
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
            "draft",
            "folder",
            "folderMessage",
            "message",
            "messageAttachment"
          ],
          "default": "message"
        },
        "operation": {
          "description": "Get many messages in a folder",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "create"
        },
        "messageId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "subject": {
          "description": "The subject of the message",
          "type": "string",
          "default": ""
        },
        "bodyContent": {
          "description": "Message body content",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is \"attachment_\" the first attachment is saved to \"attachment_0\"",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "replyType": {
          "description": "",
          "type": "string",
          "enum": [
            "reply",
            "replyAll"
          ],
          "default": "reply"
        },
        "comment": {
          "description": "A comment to include. Can be an empty string.",
          "type": "string",
          "default": ""
        },
        "send": {
          "description": "Whether to send the reply message directly. If not set, it will be saved as draft.",
          "type": "boolean",
          "default": true
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
        "toRecipients": {
          "description": "Email addresses of recipients. Multiple can be added separated by comma.",
          "type": "string",
          "default": ""
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "folderId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "attachmentId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "folderType": {
          "description": "Folder Type",
          "type": "string",
          "enum": [
            "folder",
            "searchFolder"
          ],
          "default": "folder"
        },
        "displayName": {
          "description": "Name of the folder",
          "type": "string",
          "default": ""
        },
        "includeNestedFolders": {
          "description": "Whether to include child folders in the search",
          "type": "boolean",
          "default": false
        },
        "sourceFolderIds": {
          "description": "The mailbox folders that should be mined",
          "type": "string",
          "default": []
        },
        "filterQuery": {
          "description": "The OData query to filter the messages",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Email addresses of BCC recipients",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
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
      "name": "microsoftOutlookOAuth2Api",
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
