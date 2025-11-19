---
title: "Node: Help Scout"
slug: "node-helpscout"
version: "1"
updated: "2025-11-13"
summary: "Consume Help Scout API"
node_type: "regular"
group: "['input']"
---

# Node: Help Scout

**Purpose.** Consume Help Scout API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:helpScout.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **helpScoutOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `helpScoutOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Conversation Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new conversation |
| Delete | `delete` | Delete a conversation |
| Get | `get` | Get a conversation |
| Get Many | `getAll` | Get many conversations |

### Customer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new customer |
| Get | `get` | Get a customer |
| Get Many | `getAll` | Get many customers |
| Properties | `properties` | Get customer property definitions |
| Update | `update` | Update a customer |

### Mailbox Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get data of a mailbox |
| Get Many | `getAll` | Get many mailboxes |

### Thread Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new chat thread |
| Get Many | `getAll` | Get many chat threads |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | conversation | ✗ | Resource to operate on |  |

**Resource options:**

* **Conversation** (`conversation`)
* **Customer** (`customer`)
* **Mailbox** (`mailbox`)
* **Thread** (`thread`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a new conversation |  |

**Operation options:**

* **Create** (`create`) - Create a new conversation
* **Delete** (`delete`) - Delete a conversation
* **Get** (`get`) - Get a conversation
* **Get Many** (`getAll`) - Get many conversations

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Mailbox Name or ID | `mailboxId` | options |  | ✓ | ID of a mailbox where the conversation is being created. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Status | `status` | options |  | ✓ | Conversation status |  |

**Status options:**

* **Active** (`active`)
* **Closed** (`closed`)
* **Pending** (`pending`)

| Subject | `subject` | string |  | ✓ | Conversation’s subject |  |
| Type | `type` | options |  | ✓ | Conversation type |  |

**Type options:**

* **Chat** (`chat`)
* **Email** (`email`)
* **Phone** (`phone`)

| Resolve Data | `resolveData` | boolean | True | ✗ | By default the response only contain the ID to resource. If this option gets activated, it will resolve the data automatically. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The Help Scout user assigned to the conversation | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assign To | `assignTo` | number | 0 | The Help Scout user assigned to the conversation |
| Auto Reply | `autoReply` | boolean | False | Whether set to true, an auto reply will be sent as long as there is at least one customer thread in the conversation |
| Closed At | `closedAt` | dateTime |  | When the conversation was closed, only applicable for imported conversations |
| Created At | `createdAt` | dateTime |  | When this conversation was created - ISO 8601 date time |
| Customer Email | `customerEmail` | string |  |  |
| Customer ID | `customerId` | number | 0 |  |
| Imported | `imported` | boolean | False | Whether set to true, no outgoing emails or notifications will be generated |
| Tag Names or IDs | `tags` | multiOptions | [] | List of tags to be added to the conversation. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| User ID | `user` | number | 0 | ID of the user who is adding the conversation and threads |

</details>

| Threads | `threadsUi` | fixedCollection | {} | ✗ | The message text | e.g. Add Thread |  |

<details>
<summary><strong>Threads sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Thread | `threadsValues` |  |  |  |

</details>

| Resolve Data | `resolveData` | boolean | True | ✗ | By default the response only contain the ID to resource. If this option gets activated, it will resolve the data automatically. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Customer’s age | e.g. Add Field | min:1, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Age | `age` | number | 1 | Customer’s age |
| First Name | `firstName` | string |  | First name of the customer. When defined it must be between 1 and 40 characters. |
| Gender | `gender` | options |  | Gender of this customer |
| Job Title | `jobTitle` | string |  | Job title. Max length 60 characters. |
| Last Name | `lastName` | string |  | Last name of the customer |
| Location | `location` | string |  | Location of the customer |
| Notes | `background` | string |  |  |
| Organization | `organization` | string |  |  |
| Photo Url | `photoUrl` | string |  | URL of the customer’s photo |

</details>

| Address | `addressUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Address |  |

<details>
<summary><strong>Address sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressValue` |  |  |  |

</details>

| Chat Handles | `chatsUi` | fixedCollection | {} | ✗ | Chat type | e.g. Add Chat Handle |  |

<details>
<summary><strong>Chat Handles sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Chat Handle | `chatsValues` |  |  |  |

</details>

| Emails | `emailsUi` | fixedCollection | {} | ✗ | Location for this email address | e.g. Add Email | email |

<details>
<summary><strong>Emails sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `emailsValues` |  |  |  |

</details>

| Phones | `phonesUi` | fixedCollection | {} | ✗ | Location for this phone | e.g. Add Phone |  |

<details>
<summary><strong>Phones sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `phonesValues` |  |  |  |

</details>

| Social Profiles | `socialProfilesUi` | fixedCollection | {} | ✗ | Type of social profile | e.g. Add Social Profile |  |

<details>
<summary><strong>Social Profiles sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Social Profile | `socialProfilesValues` |  |  |  |

</details>

| Websites | `websitesUi` | fixedCollection | {} | ✗ | Website URL | e.g. Add Website |  |

<details>
<summary><strong>Websites sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Website | `websitesValues` |  |  |  |

</details>

| Conversation ID | `conversationId` | string |  | ✓ |  |  |
| Type | `type` | options |  | ✓ |  |  |

**Type options:**

* **Chat** (`chat`)
* **Customer** (`customer`)
* **Note** (`note`)
* **Phone** (`phone`)
* **Reply** (`reply`)

| Text | `text` | string |  | ✓ | The chat text |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether a draft reply is created | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Created At | `createdAt` | dateTime |  |  |
| Customer Email | `customerEmail` | string |  |  |
| Customer ID | `customerId` | number | 0 |  |
| Draft | `draft` | boolean | False | Whether a draft reply is created |
| Imported | `imported` | boolean | False | Whether no outgoing emails or notifications will be generated |

</details>

| Attachments | `attachmentsUi` | fixedCollection |  | ✗ | Attachment’s file name | e.g. Add Attachments |  |

<details>
<summary><strong>Attachments sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments Values | `attachmentsValues` |  |  |  |
| Attachments Binary | `attachmentsBinary` |  |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Conversation ID | `conversationId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Conversation ID | `conversationId` | string |  | ✓ |  |  |
| Customer ID | `customerId` | string |  | ✓ |  |  |
| Mailbox ID | `mailboxId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Options | `options` | collection | {} | ✗ | Filters conversations by assignee ID | e.g. Add option | min:0, max:∞ |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assign To | `assignTo` | number | 0 | Filters conversations by assignee ID |
| Embed | `embed` | options |  | Allows embedding/loading of sub-entities |
| Folder ID | `folder` | string |  | Filters conversations from a specific folder ID |
| Mailbox ID | `mailbox` | string |  | Filters conversations from a specific mailbox |
| Modified Since | `modifiedSince` | dateTime |  | Returns only conversations that were modified after this date |
| Number | `number` | number | 0 | Looks up conversation by conversation number |
| Query | `query` | string |  | Advanced search <a href="https://developer.helpscout.com/mailbox-api/endpoints/conversations/list/#query">Examples</a> |
| Sort Field | `sortField` | options |  | Sorts the result by specified field |
| Sort Order | `sortOrder` | options | desc |  |
| Status | `status` | options | active | Filter conversation by status |
| Tag Names or IDs | `tags` | multiOptions | [] | Filter conversation by tags. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Options | `options` | collection | {} | ✗ | Filters customers by first name | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| First Name | `firstName` | string |  | Filters customers by first name |
| Last Name | `lastName` | string |  | Filters customers by last name |
| Mailbox ID | `mailbox` | string |  | Filters customers from a specific mailbox |
| Modified Since | `modifiedSince` | dateTime |  | Returns only customers that were modified after this date |
| Sort Field | `sortField` | options | score | Sorts the result by specified field |
| Sort Order | `sortOrder` | options | desc |  |
| Query | `query` | string |  | Advanced search <a href="https://developer.helpscout.com/mailbox-api/endpoints/customers/list/#query">Examples</a> |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Conversation ID | `conversationId` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Customer ID | `customerId` | string |  | ✗ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Customer’s age | e.g. Add Field | min:1, max:∞ |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Age | `age` | number | 1 | Customer’s age |
| First Name | `firstName` | string |  | First name of the customer. When defined it must be between 1 and 40 characters. |
| Gender | `gender` | options |  | Gender of this customer |
| Job Title | `jobTitle` | string |  | Job title. Max length 60 characters. |
| Last Name | `lastName` | string |  | Last name of the customer |
| Location | `location` | string |  | Location of the customer |
| Notes | `background` | string |  |  |
| Organization | `organization` | string |  |  |
| Photo Url | `photoUrl` | string |  | URL of the customer’s photo |

</details>


---

## Load Options Methods

- `getCountriesCodes`
- `for`

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
node: helpScout
displayName: Help Scout
description: Consume Help Scout API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: helpScoutOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a new conversation
  params:
  - id: mailboxId
    name: Mailbox Name or ID
    type: options
    default: ''
    required: true
    description: ID of a mailbox where the conversation is being created. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - mailbox
          operation:
          - get
    typeInfo: &id008
      type: string
      displayName: Mailbox ID
      name: mailboxId
  - id: status
    name: Status
    type: options
    default: ''
    required: true
    description: Conversation status
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - conversation
    typeInfo:
      type: options
      displayName: Status
      name: status
      possibleValues:
      - value: active
        name: Active
        description: ''
      - value: closed
        name: Closed
        description: ''
      - value: pending
        name: Pending
        description: ''
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: Conversation’s subject
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - conversation
    typeInfo:
      type: string
      displayName: Subject
      name: subject
  - id: type
    name: Type
    type: options
    default: ''
    required: true
    description: Conversation type
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - thread
          operation:
          - create
    typeInfo: &id004
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: chat
        name: Chat
        description: ''
      - value: customer
        name: Customer
        description: ''
      - value: note
        name: Note
        description: ''
      - value: phone
        name: Phone
        description: ''
      - value: reply
        name: Reply
        description: ''
  - id: resolveData
    name: Resolve Data
    type: boolean
    default: true
    required: false
    description: By default the response only contain the ID to resource. If this
      option gets activated, it will resolve the data automatically.
    validation: &id001
      displayOptions:
        show:
          operation:
          - create
          resource:
          - customer
    typeInfo: &id002
      type: boolean
      displayName: Resolve Data
      name: resolveData
  - id: threadsUi
    name: Threads
    type: fixedCollection
    default: {}
    required: false
    description: The message text
    placeholder: Add Thread
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - conversation
    typeInfo:
      type: fixedCollection
      displayName: Threads
      name: threadsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: threadsValues
        displayName: Thread
        values:
        - displayName: Type
          name: type
          type: options
          value: chat
          default: ''
          options:
          - name: Chat
            value: chat
            displayName: Chat
          - name: Customer
            value: customer
            displayName: Customer
          - name: Note
            value: note
            displayName: Note
          - name: Phone
            value: phone
            displayName: Phone
          - name: Reply
            value: reply
            displayName: Reply
        - displayName: Text
          name: text
          type: string
          description: The message text
          default: ''
        - displayName: Bcc
          name: bcc
          type: string
          description: Email addresses
          default: []
          typeOptions:
            multipleValues: true
          displayOptions:
            show:
              type:
              - customer
        - displayName: Cc
          name: cc
          type: string
          description: Email addresses
          default: []
          typeOptions:
            multipleValues: true
          displayOptions:
            show:
              type:
              - customer
        - displayName: Draft
          name: draft
          type: boolean
          description: Whether true, a draft reply is created
          default: false
          displayOptions:
            show:
              type:
              - reply
  - id: resolveData
    name: Resolve Data
    type: boolean
    default: true
    required: false
    description: By default the response only contain the ID to resource. If this
      option gets activated, it will resolve the data automatically.
    validation: *id001
    typeInfo: *id002
  - id: addressUi
    name: Address
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Address
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - customer
    typeInfo:
      type: fixedCollection
      displayName: Address
      name: addressUi
      typeOptions:
        loadOptionsMethod: getCountriesCodes
      subProperties:
      - name: addressValue
        displayName: Address
        values:
        - displayName: Line 1
          name: line1
          type: string
          default: ''
        - displayName: Line 2
          name: line2
          type: string
          default: ''
        - displayName: City
          name: city
          type: string
          default: ''
        - displayName: State
          name: state
          type: string
          default: ''
        - displayName: Country Name or ID
          name: country
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getCountriesCodes
        - displayName: Postal Code
          name: postalCode
          type: string
          default: ''
  - id: chatsUi
    name: Chat Handles
    type: fixedCollection
    default: {}
    required: false
    description: Chat type
    placeholder: Add Chat Handle
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - customer
    typeInfo:
      type: fixedCollection
      displayName: Chat Handles
      name: chatsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: chatsValues
        displayName: Chat Handle
        values:
        - displayName: Type
          name: type
          type: options
          description: Chat type
          value: aim
          default: ''
          options:
          - name: AIM
            value: aim
            displayName: Aim
          - name: Google Talk
            value: gtalk
            displayName: Google Talk
          - name: ICQ
            value: icq
            displayName: Icq
          - name: MSN
            value: msn
            displayName: Msn
          - name: Other
            value: other
            displayName: Other
          - name: QQ
            value: qq
            displayName: Qq
          - name: Skype
            value: skype
            displayName: Skype
          - name: XMPP
            value: xmpp
            displayName: Xmpp
          - name: Yahoo
            value: yahoo
            displayName: Yahoo
        - displayName: Value
          name: value
          type: string
          description: Chat handle
          default: ''
  - id: emailsUi
    name: Emails
    type: fixedCollection
    default: {}
    required: false
    description: Location for this email address
    placeholder: Add Email
    validation:
      format: email
      displayOptions:
        show:
          operation:
          - create
          resource:
          - customer
    typeInfo:
      type: fixedCollection
      displayName: Emails
      name: emailsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: emailsValues
        displayName: Email
        values:
        - displayName: Type
          name: type
          type: options
          description: Location for this email address
          value: home
          default: ''
          options:
          - name: Home
            value: home
            displayName: Home
          - name: Other
            value: other
            displayName: Other
          - name: Work
            value: work
            displayName: Work
        - displayName: Value
          name: value
          type: string
          description: Email
          default: ''
  - id: phonesUi
    name: Phones
    type: fixedCollection
    default: {}
    required: false
    description: Location for this phone
    placeholder: Add Phone
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - customer
    typeInfo:
      type: fixedCollection
      displayName: Phones
      name: phonesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: phonesValues
        displayName: Email
        values:
        - displayName: Type
          name: type
          type: options
          description: Location for this phone
          value: fax
          default: ''
          options:
          - name: Fax
            value: fax
            displayName: Fax
          - name: Home
            value: home
            displayName: Home
          - name: Other
            value: other
            displayName: Other
          - name: Pager
            value: pager
            displayName: Pager
          - name: Work
            value: work
            displayName: Work
        - displayName: Value
          name: value
          type: string
          description: Phone
          default: ''
  - id: socialProfilesUi
    name: Social Profiles
    type: fixedCollection
    default: {}
    required: false
    description: Type of social profile
    placeholder: Add Social Profile
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - customer
    typeInfo:
      type: fixedCollection
      displayName: Social Profiles
      name: socialProfilesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: socialProfilesValues
        displayName: Social Profile
        values:
        - displayName: Type
          name: type
          type: options
          description: Type of social profile
          value: aboutMe
          default: ''
          options:
          - name: About Me
            value: aboutMe
            displayName: About Me
          - name: Facebook
            value: facebook
            displayName: Facebook
          - name: Flickr
            value: flickr
            displayName: Flickr
          - name: Forsquare
            value: forsquare
            displayName: Forsquare
          - name: Google
            value: google
            displayName: Google
          - name: Google Plus
            value: googleplus
            displayName: Google Plus
          - name: Linkedin
            value: linkedin
            displayName: Linkedin
          - name: Other
            value: other
            displayName: Other
          - name: Quora
            value: quora
            displayName: Quora
          - name: Tungleme
            value: tungleme
            displayName: Tungleme
          - name: Twitter
            value: twitter
            displayName: Twitter
          - name: Youtube
            value: youtube
            displayName: Youtube
        - displayName: Value
          name: value
          type: string
          description: Social Profile handle (URL for example)
          default: ''
  - id: websitesUi
    name: Websites
    type: fixedCollection
    default: {}
    required: false
    description: Website URL
    placeholder: Add Website
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - customer
    typeInfo:
      type: fixedCollection
      displayName: Websites
      name: websitesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: websitesValues
        displayName: Website
        values:
        - displayName: Value
          name: value
          type: string
          description: Website URL
          default: ''
  - id: conversationId
    name: Conversation ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - thread
          operation:
          - getAll
    typeInfo: &id006
      type: string
      displayName: Conversation ID
      name: conversationId
  - id: type
    name: Type
    type: options
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: The chat text
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - thread
          operation:
          - create
    typeInfo:
      type: string
      displayName: Text
      name: text
  - id: attachmentsUi
    name: Attachments
    type: fixedCollection
    default: ''
    required: false
    description: Attachment’s file name
    placeholder: Add Attachments
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - thread
    typeInfo:
      type: fixedCollection
      displayName: Attachments
      name: attachmentsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: attachmentsValues
        displayName: Attachments Values
        values:
        - displayName: FileName
          name: fileName
          type: string
          description: Attachment’s file name
          default: ''
        - displayName: Mime Type
          name: mimeType
          type: string
          description: Attachment’s mime type
          default: ''
        - displayName: Data
          name: data
          type: string
          description: Base64-encoded stream of data
          placeholder: ZXhhbXBsZSBmaWxl
          default: ''
      - name: attachmentsBinary
        displayName: Attachments Binary
        values:
        - displayName: Property
          name: property
          type: string
          description: Name of the binary properties which contain data which should
            be added to email as attachment
          default: data
- id: delete
  name: Delete
  description: Delete a conversation
  params:
  - id: conversationId
    name: Conversation ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
- id: get
  name: Get
  description: Get a conversation
  params:
  - id: conversationId
    name: Conversation ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id013
      displayOptions:
        show:
          operation:
          - update
          resource:
          - customer
    typeInfo: &id014
      type: string
      displayName: Customer ID
      name: customerId
  - id: mailboxId
    name: Mailbox ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
- id: getAll
  name: Get Many
  description: Get many conversations
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
  - id: conversationId
    name: Conversation ID
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
- id: properties
  name: Properties
  description: Get customer property definitions
- id: update
  name: Update
  description: Update a customer
  params:
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id013
    typeInfo: *id014
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
  - field: threadsUi
    text: Add Thread
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: addressUi
    text: Add Address
  - field: chatsUi
    text: Add Chat Handle
  - field: emailsUi
    text: Add Email
  - field: phonesUi
    text: Add Phone
  - field: socialProfilesUi
    text: Add Social Profile
  - field: websitesUi
    text: Add Website
  - field: options
    text: Add option
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: attachmentsUi
    text: Add Attachments
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
  "$id": "https://n8n.io/schemas/nodes/helpScout.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Help Scout Node",
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
        "properties",
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
            "conversation",
            "customer",
            "mailbox",
            "thread"
          ],
          "default": "conversation"
        },
        "operation": {
          "description": "Create a new chat thread",
          "type": "string",
          "enum": [
            "create",
            "getAll"
          ],
          "default": "create"
        },
        "mailboxId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "status": {
          "description": "Conversation status",
          "type": "string",
          "enum": [
            "active",
            "closed",
            "pending"
          ],
          "default": ""
        },
        "subject": {
          "description": "Conversation\u2019s subject",
          "type": "string",
          "default": ""
        },
        "type": {
          "description": "",
          "type": "string",
          "enum": [
            "chat",
            "customer",
            "note",
            "phone",
            "reply"
          ],
          "default": ""
        },
        "resolveData": {
          "description": "By default the response only contain the ID to resource. If this option gets activated, it will resolve the data automatically.",
          "type": "boolean",
          "default": true
        },
        "additionalFields": {
          "description": "Whether a draft reply is created",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "threadsUi": {
          "description": "The message text",
          "type": "string",
          "default": {},
          "examples": [
            "Add Thread"
          ]
        },
        "conversationId": {
          "description": "",
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
        "options": {
          "description": "Filters customers by first name",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "addressUi": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Address"
          ]
        },
        "chatsUi": {
          "description": "Chat type",
          "type": "string",
          "default": {},
          "examples": [
            "Add Chat Handle"
          ]
        },
        "emailsUi": {
          "description": "Location for this email address",
          "type": "string",
          "default": {},
          "format": "email",
          "examples": [
            "Add Email"
          ]
        },
        "phonesUi": {
          "description": "Location for this phone",
          "type": "string",
          "default": {},
          "examples": [
            "Add Phone"
          ]
        },
        "socialProfilesUi": {
          "description": "Type of social profile",
          "type": "string",
          "default": {},
          "examples": [
            "Add Social Profile"
          ]
        },
        "websitesUi": {
          "description": "Website URL",
          "type": "string",
          "default": {},
          "examples": [
            "Add Website"
          ]
        },
        "customerId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Customer\u2019s age",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "text": {
          "description": "The chat text",
          "type": "string",
          "default": ""
        },
        "attachmentsUi": {
          "description": "Attachment\u2019s file name",
          "type": "string",
          "default": "",
          "examples": [
            "Add Attachments"
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
      "name": "helpScoutOAuth2Api",
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
