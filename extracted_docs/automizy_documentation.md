---
title: "Node: Automizy"
slug: "node-automizy"
version: "1"
updated: "2025-11-19"
summary: "Consume Automizy API"
node_type: "regular"
group: "['input']"
---

# Node: Automizy

**Purpose.** Consume Automizy API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:automizy.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **automizyApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **deprecated**: This service may no longer exist and will be removed from n8n in a future release.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `automizyApi` | ✓ | - |

---

## Operations

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a contact |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact |
| Get Many | `getAll` | Get many contacts |
| Update | `update` | Update a contact |

### List Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a list |
| Delete | `delete` | Delete a list |
| Get | `get` | Get a list |
| Get Many | `getAll` | Get many lists |
| Update | `update` | Update a list |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✗ | Resource to operate on |  |

**Resource options:**

* **Contact** (`contact`)
* **List** (`list`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a contact |  |

**Operation options:**

* **Create** (`create`) - Create a contact
* **Delete** (`delete`) - Delete a contact
* **Get** (`get`) - Get a contact
* **Get Many** (`getAll`) - Get many contacts
* **Update** (`update`) - Update a contact

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | The email address of the contact | e.g. name@email.com | email |
| List Name or ID | `listId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The end user specified key of the user defined data. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | The end user specified key of the user defined data. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Status | `status` | options |  | The status of the contact. You can only send email to contacts with ACTIVE status. |
| Tag Names or IDs | `tags` | multiOptions | [] | The tags you want to set to the contact. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Name | `name` | string |  | ✓ |  |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | Can be ID or email |  |
| List ID | `listId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | Can be ID or email |  |
| List ID | `listId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `listId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Defines the direction in which search results are ordered. Default value is DESC. Note: It has to be using with the Sort By parameter | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Direction | `direction` | options | desc | Defines the direction in which search results are ordered. Default value is DESC. Note: It has to be using with the Sort By parameter |
| Fields | `fields` | string |  | A comma-separated list of attributes to include in the response |
| Sort By | `sortBy` | string | Defines the field in which search results are sort by. Note: It has to be using with the Direcction parameter |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Defines the direction in which search results are ordered. Default value is DESC. Note: It has to be using with the Sort By parameter | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Direction | `direction` | options | desc | Defines the direction in which search results are ordered. Default value is DESC. Note: It has to be using with the Sort By parameter |
| Fields | `fields` | string |  | A comma-separated list of attributes to include in the response |
| Sort By | `sortBy` | string | Defines the field in which search results are sort by. Note: It has to be using with the Direcction parameter |  |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | e.g. name@email.com | email |
| Update Fields | `updateFields` | collection | {} | ✗ | The tags you want to add to the contact. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Add Tag Names or IDs | `addTags` | multiOptions | [] | The tags you want to add to the contact. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | The end user specified key of the user defined data. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Remove Tags | `removeTags` | multiOptions | [] | The tags you want to add to the contact. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Status | `status` | options |  | The status of the contact. You can only send email to contacts with ACTIVE status. |
| Tag Names or IDs | `tags` | multiOptions | [] | The tags you want to set to the contact. Will replace all existing ones. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| List ID | `listId` | string |  | ✓ |  |  |
| Name | `name` | string |  | ✓ |  |  |

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
node: automizy
displayName: Automizy
description: Consume Automizy API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: automizyApi
  required: true
operations:
- id: create
  name: Create
  description: Create a contact
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email address of the contact
    placeholder: name@email.com
    validation: &id009
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - update
          resource:
          - contact
    typeInfo: &id010
      type: string
      displayName: Email
      name: email
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
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
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - list
    typeInfo: &id012
      type: string
      displayName: Name
      name: name
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
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - contact
    typeInfo: &id004
      type: string
      displayName: Contact ID
      name: contactId
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
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
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many contacts
  params:
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
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
          - list
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - list
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: update
  name: Update
  description: Update a contact
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: ''
    placeholder: name@email.com
    validation: *id009
    typeInfo: *id010
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: deprecated
    text: This service may no longer exist and will be removed from n8n in a future
      release.
    conditions: null
  tooltips: []
  placeholders:
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: updateFields
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
  "$id": "https://n8n.io/schemas/nodes/automizy.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Automizy Node",
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
            "contact",
            "list"
          ],
          "default": "contact"
        },
        "operation": {
          "description": "Create a list",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "email": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "listId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Defines the direction in which search results are ordered. Default value is DESC. Note: It has to be using with the Sort By parameter",
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
        "updateFields": {
          "description": "The tags you want to add to the contact. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "name": {
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
      "name": "automizyApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-19 | Ultimate extraction with maximum detail for AI training |
