---
title: "Node: SendGrid"
slug: "node-sendgrid"
version: "1"
updated: "2026-01-08"
summary: "Consume SendGrid API"
node_type: "regular"
group: "['transform']"
---

# Node: SendGrid

**Purpose.** Consume SendGrid API
**Subtitle.** ={{$parameter["operation"] + ":" + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:sendGrid.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **sendGridApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `sendGridApi` | ✓ | - |

---

## Operations

### List Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a list |
| Delete | `delete` | Delete a list |
| Get | `get` | Get a list |
| Get Many | `getAll` | Get many lists |
| Update | `update` | Update a list |

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create or Update | `upsert` | Create a new contact, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact by ID |
| Get Many | `getAll` | Get many contacts |

### Mail Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send an email |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | list | ✓ | Resource to operate on |  |

**Resource options:**

* **Contact** (`contact`)
* **List** (`list`)
* **Mail** (`mail`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a list |  |

**Operation options:**

* **Create** (`create`) - Create a list
* **Delete** (`delete`) - Delete a list
* **Get** (`get`) - Get a list
* **Get Many** (`getAll`) - Get many lists
* **Update** (`update`) - Update a list

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Name of the list |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List ID | `listId` | string |  | ✓ | ID of the list |  |
| Delete Contacts | `deleteContacts` | boolean | False | ✗ | Whether to delete all contacts on the list |  |
| Contact IDs | `ids` | string |  | ✗ | ID of the contact. Multiple can be added separated by comma. |  |
| Delete All | `deleteAll` | boolean | False | ✗ | Whether all contacts will be deleted |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List ID | `listId` | string |  | ✓ | ID of the list |  |
| Contact Sample | `contactSample` | boolean | False | ✗ | Whether to return the contact sample |  |
| By | `by` | options | id | ✓ | Search the user by ID or email |  |

**By options:**

* **ID** (`id`)
* **Email** (`email`)

| Contact ID | `contactId` | string |  | ✓ | ID of the contact |  |
| Email | `email` | string |  | ✓ | Email of the contact | e.g. name@email.com | email |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:1000 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | The query field accepts valid <a href="https://sendgrid.com/docs/for-developers/sending-email/segmentation-query-language/">SGQL</a> for searching for a contact | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | The query field accepts valid <a href="https://sendgrid.com/docs/for-developers/sending-email/segmentation-query-language/">SGQL</a> for searching for a contact |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List ID | `listId` | string |  | ✓ | ID of the list |  |
| Name | `name` | string |  | ✓ | Name of the list |  |

### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | Primary email for the contact | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Adds a custom field to set also values which have not been predefined | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressUi` | fixedCollection | {} |  |
| Alternate Emails | `alternateEmails` | string |  |  |
| City | `city` | string |  |  |
| Country | `country` | string |  |  |
| First Name | `firstName` | string |  |  |
| Last Name | `lastName` | string |  |  |
| Postal Code | `postalCode` | string |  |  |
| State/Province/Region | `stateProvinceRegion` | string |  |  |
| List IDs | `listIdsUi` | fixedCollection | {} | Adds a custom field to set also values which have not been predefined |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Adds custom fields |

</details>


### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Sender Email | `fromEmail` | string |  | ✗ | Email address of the sender of the email | e.g. sender@domain.com | email |
| Sender Name | `fromName` | string |  | ✗ | Name of the sender of the email | e.g. John Smith |  |
| Recipient Email | `toEmail` | string |  | ✗ | Comma-separated list of recipient email addresses | e.g. recipient@domain.com | email |
| Subject | `subject` | string |  | ✗ | Subject of the email to send |  |
| Dynamic Template | `dynamicTemplate` | boolean | False | ✓ | Whether this email will contain a dynamic template |  |
| MIME Type | `contentType` | options | text/plain | ✗ | MIME type of the email to send |  |

**MIME Type options:**

* **Plain Text** (`text/plain`)
* **HTML** (`text/html`)

| Message Body | `contentValue` | string |  | ✓ | Message body of the email to send |  |
| Template Name or ID | `templateId` | options | [] | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Dynamic Template Fields | `dynamicTemplateFields` | fixedCollection | {} | ✗ | Key of the dynamic template field | e.g. Add Dynamic Template Fields |  |

<details>
<summary><strong>Dynamic Template Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Comma-separated list of binary properties | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `attachments` | string |  | Comma-separated list of binary properties |
| BCC Email | `bccEmail` | string |  | Comma-separated list of emails of the recipients of a blind carbon copy of the email |
| Categories | `categories` | string |  | Comma-separated list of categories. Each category name may not exceed 255 characters. |
| CC Email | `ccEmail` | string |  | Comma-separated list of emails of the recipients of a carbon copy of the email |
| Enable Sandbox | `enableSandbox` | boolean | False | Whether to use to the sandbox for testing out email-sending functionality |
| IP Pool Name | `ipPoolName` | string |  | The IP Pool that you would like to send this email from |
| Reply-To Email | `replyToEmail` | string |  | Comma-separated list of email addresses that will appear in the reply-to field of the email |
| Headers | `headers` | fixedCollection | {} | Key to set in the header object |
| Send At | `sendAt` | dateTime |  | When to deliver the email. Scheduling more than 72 hours in advance is forbidden. |

</details>


---

## Load Options Methods

- `getCustomFields`

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: SendGrid

**From workflow:** mail

**Parameters:**
```json
{
  "resource": "mail",
  "fromEmail": "test@n8n.io",
  "fromName": "Test Sender",
  "toEmail": "test@n8n.io",
  "subject": "Test Subject",
  "contentValue": "Test Message",
  "additionalFields": {
    "replyToEmail": "test-reply-to@n8n.io"
  }
}
```

**Credentials:**
- sendGridApi: `SendGrid account`


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
* Categories: Marketing, Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: sendGrid
displayName: SendGrid
description: Consume SendGrid API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: sendGridApi
  required: true
operations:
- id: create
  name: Create
  description: Create a list
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the list
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
      displayName: Name
      name: name
- id: delete
  name: Delete
  description: Delete a list
  params:
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: ID of the list
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - list
    typeInfo: &id002
      type: string
      displayName: List ID
      name: listId
  - id: deleteContacts
    name: Delete Contacts
    type: boolean
    default: false
    required: false
    description: Whether to delete all contacts on the list
    validation:
      displayOptions:
        show:
          operation:
          - delete
          resource:
          - list
    typeInfo:
      type: boolean
      displayName: Delete Contacts
      name: deleteContacts
  - id: ids
    name: Contact IDs
    type: string
    default: ''
    required: false
    description: ID of the contact. Multiple can be added separated by comma.
    validation:
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - delete
          deleteAll:
          - false
    typeInfo:
      type: string
      displayName: Contact IDs
      name: ids
  - id: deleteAll
    name: Delete All
    type: boolean
    default: false
    required: false
    description: Whether all contacts will be deleted
    validation:
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - delete
    typeInfo:
      type: boolean
      displayName: Delete All
      name: deleteAll
- id: get
  name: Get
  description: Get a list
  params:
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: ID of the list
    validation: *id001
    typeInfo: *id002
  - id: contactSample
    name: Contact Sample
    type: boolean
    default: false
    required: false
    description: Whether to return the contact sample
    validation:
      displayOptions:
        show:
          operation:
          - get
          resource:
          - list
    typeInfo:
      type: boolean
      displayName: Contact Sample
      name: contactSample
  - id: by
    name: By
    type: options
    default: id
    required: true
    description: Search the user by ID or email
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - contact
    typeInfo:
      type: options
      displayName: By
      name: by
      possibleValues:
      - value: id
        name: ID
        description: ''
      - value: email
        name: Email
        description: ''
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - contact
          by:
          - id
    typeInfo:
      type: string
      displayName: Contact ID
      name: contactId
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email of the contact
    placeholder: name@email.com
    validation: &id009
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - get
          resource:
          - contact
          by:
          - email
    typeInfo: &id010
      type: string
      displayName: Email
      name: email
- id: getAll
  name: Get Many
  description: Get many lists
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id003
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - getAll
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 1000
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: update
  name: Update
  description: Update a list
  params:
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: ID of the list
    validation: *id001
    typeInfo: *id002
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the list
    validation: *id007
    typeInfo: *id008
- id: upsert
  name: Create or Update
  description: Create a new contact, or update the current one if it already exists
    (upsert)
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Primary email for the contact
    placeholder: name@email.com
    validation: *id009
    typeInfo: *id010
- id: send
  name: Send
  description: Send an email
  params:
  - id: fromEmail
    name: Sender Email
    type: string
    default: ''
    required: false
    description: Email address of the sender of the email
    placeholder: sender@domain.com
    validation:
      format: email
      displayOptions:
        show:
          resource:
          - mail
          operation:
          - send
    typeInfo:
      type: string
      displayName: Sender Email
      name: fromEmail
  - id: fromName
    name: Sender Name
    type: string
    default: ''
    required: false
    description: Name of the sender of the email
    placeholder: John Smith
    validation:
      displayOptions:
        show:
          resource:
          - mail
          operation:
          - send
    typeInfo:
      type: string
      displayName: Sender Name
      name: fromName
  - id: toEmail
    name: Recipient Email
    type: string
    default: ''
    required: false
    description: Comma-separated list of recipient email addresses
    placeholder: recipient@domain.com
    validation:
      format: email
      displayOptions:
        show:
          resource:
          - mail
          operation:
          - send
    typeInfo:
      type: string
      displayName: Recipient Email
      name: toEmail
  - id: subject
    name: Subject
    type: string
    default: ''
    required: false
    description: Subject of the email to send
    validation:
      displayOptions:
        show:
          resource:
          - mail
          operation:
          - send
          dynamicTemplate:
          - false
    typeInfo:
      type: string
      displayName: Subject
      name: subject
  - id: dynamicTemplate
    name: Dynamic Template
    type: boolean
    default: false
    required: true
    description: Whether this email will contain a dynamic template
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - mail
          operation:
          - send
    typeInfo:
      type: boolean
      displayName: Dynamic Template
      name: dynamicTemplate
  - id: contentType
    name: MIME Type
    type: options
    default: text/plain
    required: false
    description: MIME type of the email to send
    validation:
      displayOptions:
        show:
          resource:
          - mail
          operation:
          - send
          dynamicTemplate:
          - false
    typeInfo:
      type: options
      displayName: MIME Type
      name: contentType
      possibleValues:
      - value: text/plain
        name: Plain Text
        description: ''
      - value: text/html
        name: HTML
        description: ''
  - id: contentValue
    name: Message Body
    type: string
    default: ''
    required: true
    description: Message body of the email to send
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - mail
          operation:
          - send
          dynamicTemplate:
          - false
    typeInfo:
      type: string
      displayName: Message Body
      name: contentValue
  - id: templateId
    name: Template Name or ID
    type: options
    default: []
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      displayOptions:
        show:
          resource:
          - mail
          operation:
          - send
          dynamicTemplate:
          - true
    typeInfo:
      type: options
      displayName: Template Name or ID
      name: templateId
      typeOptions:
        loadOptionsMethod: getTemplateIds
      possibleValues: []
  - id: dynamicTemplateFields
    name: Dynamic Template Fields
    type: fixedCollection
    default: {}
    required: false
    description: Key of the dynamic template field
    placeholder: Add Dynamic Template Fields
    validation:
      displayOptions:
        show:
          resource:
          - mail
          operation:
          - send
          dynamicTemplate:
          - true
    typeInfo:
      type: fixedCollection
      displayName: Dynamic Template Fields
      name: dynamicTemplateFields
      typeOptions:
        multipleValues: true
      subProperties:
      - name: fields
        displayName: Fields
        values:
        - displayName: Key
          name: key
          type: string
          description: Key of the dynamic template field
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value for the field
          default: ''
examples:
- name: SendGrid
  parameters:
    resource: mail
    fromEmail: test@n8n.io
    fromName: Test Sender
    toEmail: test@n8n.io
    subject: Test Subject
    contentValue: Test Message
    additionalFields:
      replyToEmail: test-reply-to@n8n.io
  workflow: mail
common_expressions:
- ={{$parameter["operation"] + ":" + $parameter["resource"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: filters
    text: Add Field
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: fromEmail
    text: sender@domain.com
  - field: fromName
    text: John Smith
  - field: toEmail
    text: recipient@domain.com
  - field: dynamicTemplateFields
    text: Add Dynamic Template Fields
  - field: additionalFields
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
  "$id": "https://n8n.io/schemas/nodes/sendGrid.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SendGrid Node",
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
        "upsert",
        "send"
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
            "contact",
            "list",
            "mail"
          ],
          "default": "list"
        },
        "operation": {
          "description": "Send an email",
          "type": "string",
          "enum": [
            "send"
          ],
          "default": "send"
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
        "name": {
          "description": "Name of the list",
          "type": "string",
          "default": ""
        },
        "listId": {
          "description": "ID of the list",
          "type": "string",
          "default": ""
        },
        "deleteContacts": {
          "description": "Whether to delete all contacts on the list",
          "type": "boolean",
          "default": false
        },
        "contactSample": {
          "description": "Whether to return the contact sample",
          "type": "boolean",
          "default": false
        },
        "filters": {
          "description": "The query field accepts valid <a href=\"https://sendgrid.com/docs/for-developers/sending-email/segmentation-query-language/\">SGQL</a> for searching for a contact",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "email": {
          "description": "Email of the contact",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "additionalFields": {
          "description": "Comma-separated list of binary properties",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "ids": {
          "description": "ID of the contact. Multiple can be added separated by comma.",
          "type": "string",
          "default": ""
        },
        "deleteAll": {
          "description": "Whether all contacts will be deleted",
          "type": "boolean",
          "default": false
        },
        "by": {
          "description": "Search the user by ID or email",
          "type": "string",
          "enum": [
            "id",
            "email"
          ],
          "default": "id"
        },
        "contactId": {
          "description": "ID of the contact",
          "type": "string",
          "default": ""
        },
        "fromEmail": {
          "description": "Email address of the sender of the email",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "sender@domain.com"
          ]
        },
        "fromName": {
          "description": "Name of the sender of the email",
          "type": "string",
          "default": "",
          "examples": [
            "John Smith"
          ]
        },
        "toEmail": {
          "description": "Comma-separated list of recipient email addresses",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "recipient@domain.com"
          ]
        },
        "subject": {
          "description": "Subject of the email to send",
          "type": "string",
          "default": ""
        },
        "dynamicTemplate": {
          "description": "Whether this email will contain a dynamic template",
          "type": "boolean",
          "default": false
        },
        "contentType": {
          "description": "MIME type of the email to send",
          "type": "string",
          "enum": [
            "text/plain",
            "text/html"
          ],
          "default": "text/plain"
        },
        "contentValue": {
          "description": "Message body of the email to send",
          "type": "string",
          "default": ""
        },
        "templateId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "dynamicTemplateFields": {
          "description": "Key of the dynamic template field",
          "type": "string",
          "default": {},
          "examples": [
            "Add Dynamic Template Fields"
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
      "name": "sendGridApi",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "SendGrid",
      "value": {
        "resource": "mail",
        "fromEmail": "test@n8n.io",
        "fromName": "Test Sender",
        "toEmail": "test@n8n.io",
        "subject": "Test Subject",
        "contentValue": "Test Message",
        "additionalFields": {
          "replyToEmail": "test-reply-to@n8n.io"
        }
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
