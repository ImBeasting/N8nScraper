---
title: "Node: Autopilot"
slug: "node-autopilot"
version: "1"
updated: "2026-01-08"
summary: "Consume Autopilot API"
node_type: "regular"
group: "['input']"
---

# Node: Autopilot

**Purpose.** Consume Autopilot API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:autopilot.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **autopilotApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `autopilotApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create or Update | `upsert` | Create a new contact, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact |
| Get Many | `getAll` | Get many contacts |

### Contactjourney Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add contact to list |

### Contactlist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add contact to list |
| Exist | `exist` | Check if contact is on list |
| Get Many | `getAll` | Get many contacts from a list |
| Remove | `remove` | Remove a contact from a list |

### List Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a list |
| Get Many | `getAll` | Get many lists |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✗ | Resource to operate on |  |

**Resource options:**

* **Contact** (`contact`)
* **Contact Journey** (`contactJourney`)
* **Contact List** (`contactList`)
* **List** (`list`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | upsert | ✗ | Create a new contact, or update the current one if it already exists (upsert) |  |

**Operation options:**

* **Create or Update** (`upsert`) - Create a new contact, or update the current one if it already exists (upsert)
* **Delete** (`delete`) - Delete a contact
* **Get** (`get`) - Get a contact
* **Get Many** (`getAll`) - Get many contacts

---

### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | Email address of the contact | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | User-specified key of user-defined data. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company | `Company` | string |  |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | User-specified key of user-defined data. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Fax | `Fax` | string |  |  |
| First Name | `FirstName` | string |  |  |
| Industry | `Industry` | string |  |  |
| Last Name | `LastName` | string |  |  |
| Lead Source | `LeadSource` | string |  |  |
| LinkedIn URL | `LinkedIn` | string |  |  |
| List Name or ID | `autopilotList` | options |  | List to which this contact will be added on creation. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Mailing Country | `MailingCountry` | string |  |  |
| Mailing Postal Code | `MailingPostalCode` | string |  |  |
| Mailing State | `MailingState` | string |  |  |
| Mailing Street | `MailingStreet` | string |  |  |
| Mailing City | `MailingCity` | string |  |  |
| Mobile Phone | `MobilePhone` | string |  |  |
| New Email | `newEmail` | string |  | If provided, will change the email address of the contact identified by the Email field |
| Notify | `notify` | boolean | True | By default Autopilot notifies registered REST hook endpoints for contact_added/contact_updated events when a new contact is added or an existing contact is updated via API. Disable to skip notifications. |
| Number of Employees | `NumberOfEmployees` | number | 0 |  |
| Owner Name | `owner_name` | string |  |  |
| Phone | `Phone` | string |  |  |
| Salutation | `Salutation` | string |  |  |
| Session ID | `autopilotSessionId` | string |  | Used to associate a contact with a session |
| Status | `Status` | string |  |  |
| Title | `Title` | string |  |  |
| Subscribe | `unsubscribed` | boolean | False | Whether to subscribe or un-subscribe a contact |
| Website URL | `Website` | string |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | Can be ID or email |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | Can be ID or email |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| List Name or ID | `listId` | options |  | ✓ | ID of the list to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger Name or ID | `triggerId` | options |  | ✓ | List ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Contact ID | `contactId` | string |  | ✓ | Can be ID or email |  |
| List Name or ID | `listId` | options |  | ✓ | ID of the list to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Contact ID | `contactId` | string |  | ✓ | Can be ID or email |  |

### Exist parameters (`exist`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `listId` | options |  | ✓ | ID of the list to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Contact ID | `contactId` | string |  | ✓ | Can be ID or email |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `listId` | options |  | ✓ | ID of the list to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Contact ID | `contactId` | string |  | ✓ | Can be ID or email |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Name of the list to create |  |

---

## Load Options Methods

- `getCustomFields`
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
* Categories: Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: autopilot
displayName: Autopilot
description: Consume Autopilot API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: autopilotApi
  required: true
operations:
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
    description: Email address of the contact
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - upsert
          resource:
          - contact
    typeInfo:
      type: string
      displayName: Email
      name: email
- id: delete
  name: Delete
  description: Delete a contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Can be ID or email
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - add
          - remove
          - exist
          resource:
          - contactList
    typeInfo: &id002
      type: string
      displayName: Contact ID
      name: contactId
- id: get
  name: Get
  description: Get a contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Can be ID or email
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many contacts
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
          operation:
          - getAll
          resource:
          - list
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
          operation:
          - getAll
          resource:
          - list
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: ID of the list to operate on. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - add
          - remove
          - exist
          - getAll
          resource:
          - contactList
    typeInfo: &id008
      type: options
      displayName: List Name or ID
      name: listId
      typeOptions:
        loadOptionsMethod: getLists
      possibleValues: []
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
- id: add
  name: Add
  description: Add contact to list
  params:
  - id: triggerId
    name: Trigger Name or ID
    type: options
    default: ''
    required: true
    description: List ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - add
          resource:
          - contactJourney
    typeInfo:
      type: options
      displayName: Trigger Name or ID
      name: triggerId
      typeOptions:
        loadOptionsMethod: getTriggers
      possibleValues: []
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Can be ID or email
    validation: *id001
    typeInfo: *id002
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: ID of the list to operate on. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Can be ID or email
    validation: *id001
    typeInfo: *id002
- id: exist
  name: Exist
  description: Check if contact is on list
  params:
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: ID of the list to operate on. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Can be ID or email
    validation: *id001
    typeInfo: *id002
- id: remove
  name: Remove
  description: Remove a contact from a list
  params:
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: ID of the list to operate on. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Can be ID or email
    validation: *id001
    typeInfo: *id002
- id: create
  name: Create
  description: Create a list
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the list to create
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
      displayName: Name
      name: name
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
  - field: email
    text: name@email.com
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
  "$id": "https://n8n.io/schemas/nodes/autopilot.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Autopilot Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "upsert",
        "delete",
        "get",
        "getAll",
        "add",
        "exist",
        "remove",
        "create"
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
            "contactJourney",
            "contactList",
            "list"
          ],
          "default": "contact"
        },
        "operation": {
          "description": "Create a list",
          "type": "string",
          "enum": [
            "create",
            "getAll"
          ],
          "default": "create"
        },
        "email": {
          "description": "Email address of the contact",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "additionalFields": {
          "description": "User-specified key of user-defined data. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "contactId": {
          "description": "Can be ID or email",
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
          "default": 100
        },
        "triggerId": {
          "description": "List ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "listId": {
          "description": "ID of the list to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "Name of the list to create",
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
      "name": "autopilotApi",
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
