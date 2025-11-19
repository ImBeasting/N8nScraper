---
title: "Node: Iterable"
slug: "node-iterable"
version: "1"
updated: "2025-11-13"
summary: "Consume Iterable API"
node_type: "regular"
group: "['input']"
---

# Node: Iterable

**Purpose.** Consume Iterable API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:iterable.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **iterableApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `iterableApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Track | `track` | Record the actions a user perform |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create or Update | `upsert` | Create a new user, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a user |
| Get | `get` | Get a user |

### Userlist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add user to list |
| Remove | `remove` | Remove a user from a list |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | user | ✗ | Resource to operate on |  |

**Resource options:**

* **Event** (`event`)
* **User** (`user`)
* **User List** (`userList`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | track | ✗ | Record the actions a user perform |  |

**Operation options:**

* **Track** (`track`) - Record the actions a user perform

---

### Track parameters (`track`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | The name of the event to track |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Campaign tied to conversion | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Campaign ID | `campaignId` | string |  | Campaign tied to conversion |
| Created At | `createdAt` | dateTime |  | Time event happened |
| Data Fields | `dataFieldsUi` | fixedCollection | {} | The end event specified key of the event defined data |
| Email | `email` | string |  | Either email or userId must be passed in to identify the user. If both are passed in, email takes precedence. |
| ID | `id` | string |  | Optional event ID. If an event exists with that ID, the event will be updated. If none is specified, a new ID will automatically be generated and returned. |
| Template ID | `templateId` | string |  |  |
| User ID | `userId` | string |  | userId that was passed into the updateUser call |

</details>


### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Identifier | `identifier` | options |  | ✓ | Identifier to be used |  |

**Identifier options:**

* **Email** (`email`)
* **User ID** (`userId`)

| Value | `value` | string |  | ✓ |  |  |
| Create If Doesn't Exist | `preferUserId` | boolean | True | ✓ | Whether to create a new user if the idetifier does not exist |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The end user specified key of the user defined data | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Data Fields | `dataFieldsUi` | fixedCollection | {} | The end user specified key of the user defined data |
| Merge Nested Objects | `mergeNestedObjects` | boolean | False | Whether to merge top level objects instead of overwriting (default: false), e.g. if user profile has data: {mySettings:{mobile:true}} and change contact field has data: {mySettings:{email:true}}, the resulting profile: {mySettings:{mobile:true,email:true}} |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| By | `by` | options | email | ✓ | Identifier to be used |  |

**By options:**

* **Email** (`email`)
* **User ID** (`userId`)

| User ID | `userId` | string |  | ✓ | Unique identifier for a particular user |  |
| Email | `email` | string |  | ✓ | Email for a particular user | e.g. name@email.com | email |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| By | `by` | options | email | ✓ | Identifier to be used |  |

**By options:**

* **Email** (`email`)
* **User ID** (`userId`)

| User ID | `userId` | string |  | ✓ | Unique identifier for a particular user |  |
| Email | `email` | string |  | ✓ | Email for a particular user | e.g. name@email.com | email |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `listId` | options |  | ✓ | Identifier to be used. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Identifier | `identifier` | options |  | ✓ | Identifier to be used |  |

**Identifier options:**

* **Email** (`email`)
* **User ID** (`userId`)

| Value | `value` | string |  | ✓ |  |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `listId` | options |  | ✓ | Identifier to be used. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Identifier | `identifier` | options |  | ✓ | Identifier to be used |  |

**Identifier options:**

* **Email** (`email`)
* **User ID** (`userId`)

| Value | `value` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Attribute unsubscribe to a campaign | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Campaign ID | `campaignId` | number | 0 | Attribute unsubscribe to a campaign |
| Channel Unsubscribe | `channelUnsubscribe` | boolean | False | Whether to unsubscribe email from list's associated channel - essentially a global unsubscribe |

</details>


---

## Load Options Methods

- `getLists`

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
* Categories: Communication, Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: iterable
displayName: Iterable
description: Consume Iterable API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: iterableApi
  required: true
operations:
- id: track
  name: Track
  description: Record the actions a user perform
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the event to track
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - event
          operation:
          - track
    typeInfo:
      type: string
      displayName: Name
      name: name
- id: upsert
  name: Create or Update
  description: Create a new user, or update the current one if it already exists (upsert)
  params:
  - id: identifier
    name: Identifier
    type: options
    default: ''
    required: true
    description: Identifier to be used
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - userList
          operation:
          - remove
    typeInfo: &id008
      type: options
      displayName: Identifier
      name: identifier
      possibleValues:
      - value: email
        name: Email
        description: ''
      - value: userId
        name: User ID
        description: ''
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: ''
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - userList
          operation:
          - remove
    typeInfo: &id010
      type: string
      displayName: Value
      name: value
  - id: preferUserId
    name: Create If Doesn't Exist
    type: boolean
    default: true
    required: true
    description: Whether to create a new user if the idetifier does not exist
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - upsert
          identifier:
          - userId
    typeInfo:
      type: boolean
      displayName: Create If Doesn't Exist
      name: preferUserId
- id: delete
  name: Delete
  description: Delete a user
  params:
  - id: by
    name: By
    type: options
    default: email
    required: true
    description: Identifier to be used
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
    typeInfo: &id002
      type: options
      displayName: By
      name: by
      possibleValues:
      - value: email
        name: Email
        description: ''
      - value: userId
        name: User ID
        description: ''
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: Unique identifier for a particular user
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
          by:
          - userId
    typeInfo: &id004
      type: string
      displayName: User ID
      name: userId
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email for a particular user
    placeholder: name@email.com
    validation: &id005
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
          by:
          - email
    typeInfo: &id006
      type: string
      displayName: Email
      name: email
- id: get
  name: Get
  description: Get a user
  params:
  - id: by
    name: By
    type: options
    default: email
    required: true
    description: Identifier to be used
    validation: *id001
    typeInfo: *id002
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: Unique identifier for a particular user
    validation: *id003
    typeInfo: *id004
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email for a particular user
    placeholder: name@email.com
    validation: *id005
    typeInfo: *id006
- id: add
  name: Add
  description: Add user to list
  params:
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Identifier to be used. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - userList
          operation:
          - remove
    typeInfo: &id012
      type: options
      displayName: List Name or ID
      name: listId
      typeOptions:
        loadOptionsMethod: getLists
      possibleValues: []
  - id: identifier
    name: Identifier
    type: options
    default: ''
    required: true
    description: Identifier to be used
    validation: *id007
    typeInfo: *id008
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
- id: remove
  name: Remove
  description: Remove a user from a list
  params:
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Identifier to be used. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id011
    typeInfo: *id012
  - id: identifier
    name: Identifier
    type: options
    default: ''
    required: true
    description: Identifier to be used
    validation: *id007
    typeInfo: *id008
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
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
  - field: email
    text: name@email.com
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
  "$id": "https://n8n.io/schemas/nodes/iterable.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Iterable Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "track",
        "upsert",
        "delete",
        "get",
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
            "event",
            "user",
            "userList"
          ],
          "default": "user"
        },
        "operation": {
          "description": "Add user to list",
          "type": "string",
          "enum": [
            "add",
            "remove"
          ],
          "default": "add"
        },
        "name": {
          "description": "The name of the event to track",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Attribute unsubscribe to a campaign",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "identifier": {
          "description": "Identifier to be used",
          "type": "string",
          "enum": [
            "email",
            "userId"
          ],
          "default": ""
        },
        "value": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "preferUserId": {
          "description": "Whether to create a new user if the idetifier does not exist",
          "type": "boolean",
          "default": true
        },
        "by": {
          "description": "Identifier to be used",
          "type": "string",
          "enum": [
            "email",
            "userId"
          ],
          "default": "email"
        },
        "userId": {
          "description": "Unique identifier for a particular user",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "Email for a particular user",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "listId": {
          "description": "Identifier to be used. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
      "name": "iterableApi",
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
