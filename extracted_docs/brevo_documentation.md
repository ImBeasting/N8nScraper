---
title: "Node: Brevo"
slug: "node-brevo"
version: "1"
updated: "2025-11-13"
summary: "Consume Brevo API"
node_type: "regular"
group: "['transform']"
---

# Node: Brevo

**Purpose.** Consume Brevo API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:brevo.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **sendInBlueApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `sendInBlueApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** GET, POST, DELETE

---

## Operations

### Attribute Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Sender Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a sender |

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a contact |
| Create or Update | `upsert` | Upsert a contact |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact |

### Email Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send a transactional email |
| Send Template | `sendTemplate` | Send an email with an existing Template |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | email | ✗ | Resource to operate on |  |

**Resource options:**

* **Contact** (`contact`)
* **Contact Attribute** (`attribute`)
* **Email** (`email`)
* **Sender** (`sender`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Operation to perform |  |
---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Category | `attributeCategory` | options | normal | ✓ | Category of the attribute |  |

**Category options:**

* **Calculated** (`calculated`)
* **Category** (`category`)
* **Global** (`global`)
* **Normal** (`normal`)
* **Transactional** (`transactional`)

| Name | `attributeName` | string |  | ✓ | Name of the attribute |  |
| Type | `attributeType` | options |  | ✓ | Attribute Type |  |

**Type options:**

* **Boolean** (`boolean`)
* **Date** (`date`)
* **Float** (`float`)
* **Text** (`text`)

| Value | `attributeValue` | string |  | ✓ | Value of the attribute |  |
| Contact Attribute List | `attributeCategoryList` | collection | {} | ✗ | ID of the value, must be numeric | e.g. Add Attributes |  |

<details>
<summary><strong>Contact Attribute List sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Contact Attributes | `categoryEnumeration` | fixedCollection | 1 | ID of the value, must be numeric |

</details>

| Name | `name` | string |  | ✓ | Name of the sender |  |
| Email | `email` | string |  | ✓ | Email of the sender | e.g. name@email.com | email |
| Email | `email` | string |  | ✗ | e.g. name@email.com | email |
| Contact Attributes | `createContactAttributes` | options | {} | ✗ | Array of attributes to be added | e.g. Add Attribute |  |

### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | Email of the contact | e.g. name@email.com | email |
| Contact Attributes | `upsertAttributes` | options | {} | ✗ | Array of attributes to be updated | e.g. Add Attribute |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Category | `deleteAttributeCategory` | options | normal | ✗ | Category of the attribute |  |

**Category options:**

* **Calculated** (`calculated`)
* **Category** (`category`)
* **Global** (`global`)
* **Normal** (`normal`)
* **Transactional** (`transactional`)

| Name | `deleteAttributeName` | string |  | ✗ | Name of the attribute |  |
| Sender ID | `id` | string |  | ✗ | ID of the sender to delete |  |
| Contact Identifier | `identifier` | string |  | ✗ | Email (urlencoded) OR ID of the contact OR its SMS attribute value |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact Identifier | `identifier` | string |  | ✓ | Email (urlencoded) OR ID of the contact OR its SMS attribute value |  |

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Send HTML | `sendHTML` | boolean | False | ✗ |  |  |
| Subject | `subject` | string |  | ✗ | Subject of the email |  |
| Text Content | `textContent` | string |  | ✗ | Text content of the message |  |
| HTML Content | `htmlContent` | string |  | ✗ | HTML content of the message |  |
| Sender | `sender` | string |  | ✓ |  | validated |
| Receipients | `receipients` | string |  | ✓ |  | validated |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Additional fields to add | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `emailAttachments` | fixedCollection | {} | The name of the incoming field containing the binary file data to be processed |
| Receipients BCC | `receipientsBCC` | fixedCollection | {} |  |
| Receipients CC | `receipientsCC` | fixedCollection | {} |  |
| Email Tags | `emailTags` | fixedCollection | {} | Add tags to your emails to find them more easily |

</details>


### Send Template parameters (`sendTemplate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Template ID | `templateId` | options |  | ✗ |  |  |
| Receipients | `receipients` | string |  | ✓ |  | validated |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Additional fields to add | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `emailAttachments` | fixedCollection | {} | The name of the incoming field containing the binary file data to be processed |
| Email Tags | `emailTags` | fixedCollection | {} | Add tags to your emails to find them more easily |
| Template Parameters | `templateParameters` | fixedCollection | {} | Pass a set of attributes to customize the template |

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
* Categories: Marketing, Communication
* Aliases: sendinblue

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: brevo
displayName: Brevo
description: Consume Brevo API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: sendInBlueApi
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: attributeCategory
    name: Category
    type: options
    default: normal
    required: true
    description: Category of the attribute
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - attribute
          operation:
          - create
    typeInfo:
      type: options
      displayName: Category
      name: attributeCategory
      possibleValues:
      - value: calculated
        name: Calculated
        description: ''
      - value: category
        name: Category
        description: ''
      - value: global
        name: Global
        description: ''
      - value: normal
        name: Normal
        description: ''
      - value: transactional
        name: Transactional
        description: ''
  - id: attributeName
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the attribute
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - attribute
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: attributeName
  - id: attributeType
    name: Type
    type: options
    default: ''
    required: true
    description: Attribute Type
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - attribute
          operation:
          - create
          attributeCategory:
          - normal
    typeInfo:
      type: options
      displayName: Type
      name: attributeType
      possibleValues:
      - value: boolean
        name: Boolean
        description: ''
      - value: date
        name: Date
        description: ''
      - value: float
        name: Float
        description: ''
      - value: text
        name: Text
        description: ''
  - id: attributeValue
    name: Value
    type: string
    default: ''
    required: true
    description: Value of the attribute
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - attribute
          operation:
          - create
          attributeCategory:
          - global
          - calculated
    typeInfo:
      type: string
      displayName: Value
      name: attributeValue
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the sender
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - sender
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email of the sender
    placeholder: name@email.com
    validation: &id001
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - upsert
    typeInfo: &id002
      type: string
      displayName: Email
      name: email
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: ''
    placeholder: name@email.com
    validation: *id001
    typeInfo: *id002
  - id: createContactAttributes
    name: Contact Attributes
    type: options
    default: {}
    required: false
    description: Array of attributes to be added
    placeholder: Add Attribute
    validation:
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
    typeInfo:
      type: options
      displayName: Contact Attributes
      name: createContactAttributes
      possibleValues: []
- id: upsert
  name: Create or Update
  description: ''
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email of the contact
    placeholder: name@email.com
    validation: *id001
    typeInfo: *id002
  - id: upsertAttributes
    name: Contact Attributes
    type: options
    default: {}
    required: false
    description: Array of attributes to be updated
    placeholder: Add Attribute
    validation:
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - upsert
    typeInfo:
      type: options
      displayName: Contact Attributes
      name: upsertAttributes
      possibleValues: []
- id: delete
  name: Delete
  description: ''
  params:
  - id: deleteAttributeCategory
    name: Category
    type: options
    default: normal
    required: false
    description: Category of the attribute
    validation:
      displayOptions:
        show:
          resource:
          - attribute
          operation:
          - delete
    typeInfo:
      type: options
      displayName: Category
      name: deleteAttributeCategory
      possibleValues:
      - value: calculated
        name: Calculated
        description: ''
      - value: category
        name: Category
        description: ''
      - value: global
        name: Global
        description: ''
      - value: normal
        name: Normal
        description: ''
      - value: transactional
        name: Transactional
        description: ''
  - id: deleteAttributeName
    name: Name
    type: string
    default: ''
    required: false
    description: Name of the attribute
    validation:
      displayOptions:
        show:
          resource:
          - attribute
          operation:
          - delete
    typeInfo:
      type: string
      displayName: Name
      name: deleteAttributeName
  - id: id
    name: Sender ID
    type: string
    default: ''
    required: false
    description: ID of the sender to delete
    validation:
      displayOptions:
        show:
          resource:
          - sender
          operation:
          - delete
    typeInfo:
      type: string
      displayName: Sender ID
      name: id
  - id: identifier
    name: Contact Identifier
    type: string
    default: ''
    required: false
    description: Email (urlencoded) OR ID of the contact OR its SMS attribute value
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - update
    typeInfo: &id004
      type: string
      displayName: Contact Identifier
      name: identifier
- id: get
  name: Get
  description: ''
  params:
  - id: identifier
    name: Contact Identifier
    type: string
    default: ''
    required: true
    description: Email (urlencoded) OR ID of the contact OR its SMS attribute value
    validation: *id003
    typeInfo: *id004
- id: send
  name: Send
  description: ''
  params:
  - id: sendHTML
    name: Send HTML
    type: boolean
    default: false
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - email
          operation:
          - send
    typeInfo:
      type: boolean
      displayName: Send HTML
      name: sendHTML
  - id: subject
    name: Subject
    type: string
    default: ''
    required: false
    description: Subject of the email
    validation:
      displayOptions:
        show:
          resource:
          - email
          operation:
          - send
    typeInfo:
      type: string
      displayName: Subject
      name: subject
  - id: textContent
    name: Text Content
    type: string
    default: ''
    required: false
    description: Text content of the message
    validation:
      displayOptions:
        show:
          resource:
          - email
          operation:
          - send
          sendHTML:
          - false
    typeInfo:
      type: string
      displayName: Text Content
      name: textContent
  - id: htmlContent
    name: HTML Content
    type: string
    default: ''
    required: false
    description: HTML content of the message
    validation:
      displayOptions:
        show:
          resource:
          - email
          operation:
          - send
          sendHTML:
          - true
    typeInfo:
      type: string
      displayName: HTML Content
      name: htmlContent
  - id: sender
    name: Sender
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      format: validated
      displayOptions:
        show:
          resource:
          - email
          operation:
          - send
    typeInfo:
      type: string
      displayName: Sender
      name: sender
  - id: receipients
    name: Receipients
    type: string
    default: ''
    required: true
    description: ''
    validation: &id005
      required: true
      format: validated
      displayOptions:
        show:
          resource:
          - email
          operation:
          - sendTemplate
    typeInfo: &id006
      type: string
      displayName: Receipients
      name: receipients
- id: sendTemplate
  name: Send Template
  description: ''
  params:
  - id: templateId
    name: Template ID
    type: options
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - email
          operation:
          - sendTemplate
    typeInfo:
      type: options
      displayName: Template ID
      name: templateId
      possibleValues: []
  - id: receipients
    name: Receipients
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - GET
  - POST
  - DELETE
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: attributeCategoryList
    text: Add Attributes
  - field: updateAttributeCategoryList
    text: Add Field
  - field: email
    text: name@email.com
  - field: email
    text: name@email.com
  - field: createContactAttributes
    text: Add Attribute
  - field: options
    text: Add option
  - field: filters
    text: Add Filter
  - field: updateAttributes
    text: Add Attribute
  - field: email
    text: name@email.com
  - field: upsertAttributes
    text: Add Attribute
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/brevo.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Brevo Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "upsert",
        "delete",
        "get",
        "send",
        "sendTemplate"
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
            "attribute",
            "email",
            "sender"
          ],
          "default": "email"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "send",
            "sendTemplate"
          ],
          "default": "send"
        },
        "attributeCategory": {
          "description": "Category of the attribute",
          "type": "string",
          "enum": [
            "calculated",
            "category",
            "global",
            "normal",
            "transactional"
          ],
          "default": "normal"
        },
        "attributeName": {
          "description": "Name of the attribute",
          "type": "string",
          "default": ""
        },
        "attributeType": {
          "description": "Attribute Type",
          "type": "string",
          "enum": [
            "boolean",
            "date",
            "float",
            "text"
          ],
          "default": ""
        },
        "attributeValue": {
          "description": "Value of the attribute",
          "type": "string",
          "default": ""
        },
        "attributeCategoryList": {
          "description": "ID of the value, must be numeric",
          "type": "string",
          "default": {},
          "examples": [
            "Add Attributes"
          ]
        },
        "updateAttributeCategory": {
          "description": "Category of the attribute",
          "type": "string",
          "enum": [
            "calculated",
            "category",
            "global"
          ],
          "default": "calculated"
        },
        "updateAttributeName": {
          "description": "Name of the existing attribute",
          "type": "string",
          "default": ""
        },
        "updateAttributeValue": {
          "description": "Value of the attribute to update",
          "type": "string",
          "default": ""
        },
        "updateAttributeCategoryList": {
          "description": "List of the values and labels that the attribute can take",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "deleteAttributeCategory": {
          "description": "Category of the attribute",
          "type": "string",
          "enum": [
            "calculated",
            "category",
            "global",
            "normal",
            "transactional"
          ],
          "default": "normal"
        },
        "deleteAttributeName": {
          "description": "Name of the attribute",
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
        "name": {
          "description": "Name of the sender",
          "type": "string",
          "default": ""
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
        "id": {
          "description": "ID of the sender to delete",
          "type": "string",
          "default": ""
        },
        "createContactAttributes": {
          "description": "Array of attributes to be added",
          "type": "string",
          "default": {},
          "examples": [
            "Add Attribute"
          ]
        },
        "options": {
          "description": "Sort the results in the ascending/descending order of record creation",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "filters": {
          "description": "Filter (urlencoded) the contacts modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ)",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "identifier": {
          "description": "Email (urlencoded) OR ID of the contact OR its SMS attribute value",
          "type": "string",
          "default": ""
        },
        "updateAttributes": {
          "description": "Array of attributes to be updated",
          "type": "string",
          "default": {},
          "examples": [
            "Add Attribute"
          ]
        },
        "upsertAttributes": {
          "description": "Array of attributes to be updated",
          "type": "string",
          "default": {},
          "examples": [
            "Add Attribute"
          ]
        },
        "sendHTML": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "subject": {
          "description": "Subject of the email",
          "type": "string",
          "default": ""
        },
        "textContent": {
          "description": "Text content of the message",
          "type": "string",
          "default": ""
        },
        "htmlContent": {
          "description": "HTML content of the message",
          "type": "string",
          "default": ""
        },
        "sender": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "validated"
        },
        "receipients": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "validated"
        },
        "additionalFields": {
          "description": "Additional fields to add",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "templateId": {
          "description": "",
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
      "name": "sendInBlueApi",
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
