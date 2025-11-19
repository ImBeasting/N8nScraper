---
title: "Node: E-goi"
slug: "node-egoi"
version: "1"
updated: "2025-11-13"
summary: "Consume E-goi API"
node_type: "regular"
group: "['output']"
---

# Node: E-goi

**Purpose.** Consume E-goi API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:egoi.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **egoiApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `egoiApi` | ✓ | - |

---

## API Patterns

**Common Endpoints:**
- `https://api.egoiapp.com{endpoint}`

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a member |
| Get | `get` | Get a member |
| Get Many | `getAll` | Get many members |
| Update | `update` | Update a member |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✓ | Resource to operate on |  |

**Resource options:**

* **Contact** (`contact`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✓ | Create a member |  |

**Operation options:**

* **Create** (`create`) - Create a member
* **Get** (`get`) - Get a member
* **Get Many** (`getAll`) - Get many members
* **Update** (`update`) - Update a member

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `list` | options |  | ✗ | ID of list to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Email | `email` | string |  | ✗ | Email address for a subscriber | e.g. name@email.com | email |
| Resolve Data | `resolveData` | boolean | True | ✗ | By default the response just includes the contact ID. If this option gets activated, it will resolve the data automatically. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Birth date of a subscriber | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Birth Date | `birth_date` | dateTime |  | Birth date of a subscriber |
| Cellphone | `cellphone` | string |  | Cellphone of a subscriber |
| Extra Fields | `extraFieldsUi` | fixedCollection | {} | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| First Name | `first_name` | string |  | Name of a subscriber |
| Last Name | `last_name` | string |  | Name of a subscriber |
| Status | `status` | options | active | Subscriber's current status |
| Tag Names or IDs | `tagIds` | multiOptions | [] | List of tag IDs to be added. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `list` | options |  | ✗ | ID of list to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| By | `by` | options | id | ✗ | Search by |  |

**By options:**

* **Contact ID** (`id`)
* **Email** (`email`)

| Contact ID | `contactId` | string |  | ✗ | Contact ID of the subscriber |  |
| Email | `email` | string |  | ✗ | Email address for subscriber | e.g. name@email.com | email |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `list` | options |  | ✗ | ID of list to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `list` | options |  | ✗ | ID of list to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Contact ID | `contactId` | string |  | ✗ | Contact ID of the subscriber |  |
| Resolve Data | `resolveData` | boolean | True | ✗ | By default the response just includes the contact ID. If this option gets activated, it will resolve the data automatically. |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Birth date of subscriber | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Birth Date | `birth_date` | dateTime |  | Birth date of subscriber |
| Cellphone | `cellphone` | string |  | Cellphone of subscriber |
| Email | `email` | string |  | Email address for subscriber |
| Extra Fields | `extraFieldsUi` | fixedCollection | {} | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| First Name | `first_name` | string |  | Name of subscriber |
| Last Name | `last_name` | string |  | Name of subscriber |
| Status | `status` | options | active | Subscriber's current status |
| Tag Names or IDs | `tagIds` | multiOptions | [] | List of tag IDs to be added. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


---

## Load Options Methods

- `getLists`
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
* Categories: Communication, Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: egoi
displayName: E-goi
description: Consume E-goi API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: egoiApi
  required: true
operations:
- id: create
  name: Create
  description: Create a member
  params:
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: false
    description: ID of list to operate on. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      displayOptions:
        show:
          operation:
          - getAll
          - create
          - update
          - get
    typeInfo: &id002
      type: options
      displayName: List Name or ID
      name: list
      typeOptions:
        loadOptionsMethod: getLists
      possibleValues: []
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email address for a subscriber
    placeholder: name@email.com
    validation: &id003
      format: email
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - get
          by:
          - email
    typeInfo: &id004
      type: string
      displayName: Email
      name: email
  - id: resolveData
    name: Resolve Data
    type: boolean
    default: true
    required: false
    description: By default the response just includes the contact ID. If this option
      gets activated, it will resolve the data automatically.
    validation: &id009
      displayOptions:
        show:
          operation:
          - create
          - update
    typeInfo: &id010
      type: boolean
      displayName: Resolve Data
      name: resolveData
- id: get
  name: Get
  description: Get a member
  params:
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: false
    description: ID of list to operate on. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: by
    name: By
    type: options
    default: id
    required: false
    description: Search by
    validation:
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
        name: Contact ID
        description: ''
      - value: email
        name: Email
        description: ''
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: false
    description: Contact ID of the subscriber
    validation: &id007
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - get
          by:
          - id
    typeInfo: &id008
      type: string
      displayName: Contact ID
      name: contactId
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email address for subscriber
    placeholder: name@email.com
    validation: *id003
    typeInfo: *id004
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id005
      displayOptions:
        show:
          operation:
          - get
          - getAll
          resource:
          - contact
    typeInfo: &id006
      type: boolean
      displayName: Simplify
      name: simple
- id: getAll
  name: Get Many
  description: Get many members
  params:
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: false
    description: ID of list to operate on. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - contact
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - contact
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id005
    typeInfo: *id006
- id: update
  name: Update
  description: Update a member
  params:
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: false
    description: ID of list to operate on. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: false
    description: Contact ID of the subscriber
    validation: *id007
    typeInfo: *id008
  - id: resolveData
    name: Resolve Data
    type: boolean
    default: true
    required: false
    description: By default the response just includes the contact ID. If this option
      gets activated, it will resolve the data automatically.
    validation: *id009
    typeInfo: *id010
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints:
  - https://api.egoiapp.com{endpoint}
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: email
    text: name@email.com
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
  "$id": "https://n8n.io/schemas/nodes/egoi.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "E-goi Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "get",
        "getAll",
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
            "contact"
          ],
          "default": "contact"
        },
        "operation": {
          "description": "Create a member",
          "type": "string",
          "enum": [
            "create",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "list": {
          "description": "ID of list to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "Email address for subscriber",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "contactId": {
          "description": "Contact ID of the subscriber",
          "type": "string",
          "default": ""
        },
        "resolveData": {
          "description": "By default the response just includes the contact ID. If this option gets activated, it will resolve the data automatically.",
          "type": "boolean",
          "default": true
        },
        "additionalFields": {
          "description": "Birth date of a subscriber",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "Birth date of subscriber",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "by": {
          "description": "Search by",
          "type": "string",
          "enum": [
            "id",
            "email"
          ],
          "default": "id"
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
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
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
      "name": "egoiApi",
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
