---
title: "Node: Okta"
slug: "node-okta"
version: "1"
updated: "2026-01-08"
summary: "Use the Okta API"
node_type: "regular"
group: "['transform']"
---

# Node: Okta

**Purpose.** Use the Okta API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:Okta.svg', 'dark': 'file:Okta.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **oktaApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `oktaApi` | ✓ | - |

---

## Operations

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | user | ✗ | Resource to operate on |  |

**Resource options:**

* **User** (`user`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | user | ✗ |  |  |

**Resource options:**

* **User** (`user`)

| Operation | `operation` | options | getAll | ✗ | Create a new user |  |
| User | `userId` | resourceLocator |  | ✓ | The user you want to operate on. Choose from the list, or specify an ID. | e.g. Select a user... |  |
| First Name | `firstName` | string |  | ✓ | e.g. e.g. Nathan |  |
| Last Name | `lastName` | string |  | ✓ | e.g. e.g. Smith |  |
| Username | `login` | string |  | ✓ | e.g. e.g. nathan@example.com |  |
| Email | `email` | string |  | ✓ | e.g. e.g. nathan@example.com | email |
| Activate | `activate` | boolean | True | ✗ | Whether to activate the user and allow access to all assigned applications |  |
| Fields | `getCreateFields` | collection | {} | ✗ | e.g. Add field |  |
| Fields | `getUpdateFields` | collection | {} | ✗ | e.g. Add field |  |
| Search Query | `searchQuery` | string |  | ✗ | e.g. e.g. profile.lastName sw "Smi" |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:200 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Simplify | `simplify` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Send Email | `sendEmail` | boolean | False | ✗ | Whether to send a deactivation email to the administrator | email |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$credentials.url.replace(new RegExp("/$"), "")}}`
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
* Categories: Development
* Aliases: authentication, users, Security

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: okta
displayName: Okta
description: Use the Okta API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: oktaApi
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: user
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: user
      name: User
      description: ''
- id: operation
  name: Operation
  type: options
  default: getAll
  required: false
  description: Create a new user
  validation:
    displayOptions:
      show:
        resource:
        - user
  typeInfo:
    type: options
    displayName: Operation
    name: operation
    possibleValues: []
- id: userId
  name: User
  type: resourceLocator
  default: ''
  required: true
  description: The user you want to operate on. Choose from the list, or specify an
    ID.
  placeholder: Select a user...
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - user
        operation:
        - get
        - update
        - delete
  typeInfo:
    type: resourceLocator
    displayName: User
    name: userId
- id: firstName
  name: First Name
  type: string
  default: ''
  required: true
  description: ''
  placeholder: e.g. Nathan
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - user
        operation:
        - create
  typeInfo:
    type: string
    displayName: First Name
    name: firstName
- id: lastName
  name: Last Name
  type: string
  default: ''
  required: true
  description: ''
  placeholder: e.g. Smith
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - user
        operation:
        - create
  typeInfo:
    type: string
    displayName: Last Name
    name: lastName
- id: login
  name: Username
  type: string
  default: ''
  required: true
  description: ''
  hint: Unique identifier for the user, must be an email
  placeholder: e.g. nathan@example.com
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - user
        operation:
        - create
  typeInfo:
    type: string
    displayName: Username
    name: login
- id: email
  name: Email
  type: string
  default: ''
  required: true
  description: ''
  placeholder: e.g. nathan@example.com
  validation:
    required: true
    format: email
    displayOptions:
      show:
        resource:
        - user
        operation:
        - create
  typeInfo:
    type: string
    displayName: Email
    name: email
- id: activate
  name: Activate
  type: boolean
  default: true
  required: false
  description: Whether to activate the user and allow access to all assigned applications
  validation:
    displayOptions:
      show:
        resource:
        - user
        operation:
        - create
  typeInfo:
    type: boolean
    displayName: Activate
    name: activate
- id: getCreateFields
  name: Fields
  type: collection
  default: {}
  required: false
  description: ''
  placeholder: Add field
  validation:
    displayOptions:
      show:
        resource:
        - user
        operation:
        - create
  typeInfo:
    type: collection
    displayName: Fields
    name: getCreateFields
    subProperties: []
- id: getUpdateFields
  name: Fields
  type: collection
  default: {}
  required: false
  description: ''
  placeholder: Add field
  validation:
    displayOptions:
      show:
        resource:
        - user
        operation:
        - update
  typeInfo:
    type: collection
    displayName: Fields
    name: getUpdateFields
    subProperties: []
- id: searchQuery
  name: Search Query
  type: string
  default: ''
  required: false
  description: ''
  hint: Filter users by using the allowed syntax. <a href="https://developer.okta.com/docs/reference/core-okta-api/#filter"
    target="_blank">More info</a>.
  placeholder: e.g. profile.lastName sw "Smi"
  validation:
    displayOptions:
      show:
        resource:
        - user
        operation:
        - getAll
  typeInfo:
    type: string
    displayName: Search Query
    name: searchQuery
- id: limit
  name: Limit
  type: number
  default: 20
  required: false
  description: Max number of results to return
  validation:
    displayOptions:
      show:
        resource:
        - user
        operation:
        - getAll
        returnAll:
        - false
  typeInfo:
    type: number
    displayName: Limit
    name: limit
    typeOptions:
      minValue: 1
      maxValue: 200
- id: returnAll
  name: Return All
  type: boolean
  default: false
  required: false
  description: Whether to return all results or only up to a given limit
  validation:
    displayOptions:
      show:
        resource:
        - user
        operation:
        - getAll
  typeInfo:
    type: boolean
    displayName: Return All
    name: returnAll
- id: simplify
  name: Simplify
  type: boolean
  default: true
  required: false
  description: Whether to return a simplified version of the response instead of the
    raw data
  validation:
    displayOptions:
      show:
        resource:
        - user
        operation:
        - get
        - getAll
  typeInfo:
    type: boolean
    displayName: Simplify
    name: simplify
- id: sendEmail
  name: Send Email
  type: boolean
  default: false
  required: false
  description: Whether to send a deactivation email to the administrator
  validation:
    format: email
    displayOptions:
      show:
        resource:
        - user
        operation:
        - delete
  typeInfo:
    type: boolean
    displayName: Send Email
    name: sendEmail
common_expressions:
- ={{$credentials.url.replace(new RegExp("/$"), "")}}
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: userId
    text: Select a user...
  - field: firstName
    text: e.g. Nathan
  - field: lastName
    text: e.g. Smith
  - field: login
    text: e.g. nathan@example.com
  - field: email
    text: e.g. nathan@example.com
  - field: getCreateFields
    text: Add field
  - field: getUpdateFields
    text: Add field
  - field: searchQuery
    text: e.g. profile.lastName sw "Smi"
  hints:
  - field: login
    text: Unique identifier for the user, must be an email
  - field: searchQuery
    text: Filter users by using the allowed syntax. <a href="https://developer.okta.com/docs/reference/core-okta-api/#filter"
      target="_blank">More info</a>.
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
  "$id": "https://n8n.io/schemas/nodes/okta.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Okta Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "user"
          ],
          "default": "user"
        },
        "operation": {
          "description": "Create a new user",
          "type": "string",
          "default": "getAll"
        },
        "userId": {
          "description": "The user you want to operate on. Choose from the list, or specify an ID.",
          "type": "string",
          "examples": [
            "Select a user..."
          ]
        },
        "firstName": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Nathan"
          ]
        },
        "lastName": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Smith"
          ]
        },
        "login": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. nathan@example.com"
          ]
        },
        "email": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "e.g. nathan@example.com"
          ]
        },
        "activate": {
          "description": "Whether to activate the user and allow access to all assigned applications",
          "type": "boolean",
          "default": true
        },
        "getCreateFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add field"
          ]
        },
        "getUpdateFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add field"
          ]
        },
        "searchQuery": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. profile.lastName sw \"Smi\""
          ]
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 20
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "simplify": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "sendEmail": {
          "description": "Whether to send a deactivation email to the administrator",
          "type": "boolean",
          "default": false,
          "format": "email"
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
      "name": "oktaApi",
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
