---
title: "Node: ConvertKit"
slug: "node-convertkit"
version: "1"
updated: "2025-11-13"
summary: "Consume ConvertKit API"
node_type: "regular"
group: "['input']"
---

# Node: ConvertKit

**Purpose.** Consume ConvertKit API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:convertKit.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **convertKitApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `convertKitApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Customfield Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a field |
| Delete | `delete` | Delete a field |
| Get Many | `getAll` | Get many fields |
| Update | `update` | Update a field |

### Form Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Subscriber | `addSubscriber` | Add a subscriber |
| Get Many | `getAll` | Get many forms |
| Get Subscriptions | `getSubscriptions` | List subscriptions to a form including subscriber data |

### Sequence Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Subscriber | `addSubscriber` | Add a subscriber |
| Get Many | `getAll` | Get many sequences |
| Get Subscriptions | `getSubscriptions` | Get all subscriptions to a sequence including subscriber data |

### Tag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a tag |
| Get Many | `getAll` | Get many tags |

### Tagsubscriber Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a tag to a subscriber |
| Get Many | `getAll` | List subscriptions to a tag including subscriber data |
| Delete | `delete` | Delete a tag from a subscriber |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | form | ✗ | Resource to operate on |  |

**Resource options:**

* **Custom Field** (`customField`)
* **Form** (`form`)
* **Sequence** (`sequence`)
* **Tag** (`tag`)
* **Tag Subscriber** (`tagSubscriber`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | update | ✗ | Create a field |  |

**Operation options:**

* **Create** (`create`) - Create a field
* **Delete** (`delete`) - Delete a field
* **Get Many** (`getAll`) - Get many fields
* **Update** (`update`) - Update a field

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Label | `label` | string |  | ✓ | The label of the custom field |  |
| Name | `name` | string |  | ✓ | Tag name, multiple can be added separated by comma |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Field ID | `id` | string |  | ✓ | The ID of your custom field |  |
| Tag Name or ID | `tagId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Email | `email` | string |  | ✓ | Subscriber email address | e.g. name@email.com | email |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Tag Name or ID | `tagId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Receive only active subscribers or cancelled subscribers | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Subscriber State | `subscriberState` | options | active |  |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Field ID | `id` | string |  | ✓ | The ID of your custom field |  |
| Label | `label` | string |  | ✓ | The label of the custom field |  |

### Add Subscriber parameters (`addSubscriber`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Name or ID | `id` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Email | `email` | string |  | ✓ | The subscriber's email address | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Object of key/value pairs for custom fields (the custom field must exist before you can use it here) | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `fieldsUi` | fixedCollection | {} | Object of key/value pairs for custom fields (the custom field must exist before you can use it here) |
| First Name | `firstName` | string |  | The subscriber's first name |

</details>

| Sequence Name or ID | `id` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Email | `email` | string |  | ✓ | The subscriber's email address | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Object of key/value pairs for custom fields (the custom field must exist before you can use it here) | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `fieldsUi` | fixedCollection | {} | Object of key/value pairs for custom fields (the custom field must exist before you can use it here) |
| First Name | `firstName` | string |  | The subscriber's first name |
| Tag Names or IDs | `tags` | multiOptions | [] | Tags. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Get Subscriptions parameters (`getSubscriptions`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Name or ID | `id` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Receive only active subscribers or cancelled subscribers | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Subscriber State | `subscriberState` | options | active |  |

</details>

| Sequence Name or ID | `id` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Receive only active subscribers or cancelled subscribers | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Subscriber State | `subscriberState` | options | active |  |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tag Name or ID | `tagId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Email | `email` | string |  | ✓ | Subscriber email address | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Object of key/value pairs for custom fields (the custom field must exist before you can use it here) | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `fields` | fixedCollection | {} | Object of key/value pairs for custom fields (the custom field must exist before you can use it here) |
| First Name | `firstName` | string |  | Subscriber first name |

</details>


---

## Load Options Methods

- `getTags`

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
* Categories: Marketing, Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: convertKit
displayName: ConvertKit
description: Consume ConvertKit API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: convertKitApi
  required: true
operations:
- id: create
  name: Create
  description: Create a field
  params:
  - id: label
    name: Label
    type: string
    default: ''
    required: true
    description: The label of the custom field
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - customField
          operation:
          - update
          - create
    typeInfo: &id010
      type: string
      displayName: Label
      name: label
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Tag name, multiple can be added separated by comma
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - tag
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
- id: delete
  name: Delete
  description: Delete a field
  params:
  - id: id
    name: Field ID
    type: string
    default: ''
    required: true
    description: The ID of your custom field
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - sequence
          operation:
          - addSubscriber
          - getSubscriptions
    typeInfo: &id008
      type: options
      displayName: Sequence Name or ID
      name: id
      typeOptions:
        loadOptionsMethod: getSequences
      possibleValues: []
  - id: tagId
    name: Tag Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - tagSubscriber
          operation:
          - add
          - getAll
          - delete
    typeInfo: &id006
      type: options
      displayName: Tag Name or ID
      name: tagId
      typeOptions:
        loadOptionsMethod: getTags
      possibleValues: []
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Subscriber email address
    placeholder: name@email.com
    validation: &id011
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - tagSubscriber
          operation:
          - add
          - delete
    typeInfo: &id012
      type: string
      displayName: Email
      name: email
- id: getAll
  name: Get Many
  description: Get many fields
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id001
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - tagSubscriber
    typeInfo: &id002
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id003
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - tagSubscriber
          returnAll:
          - false
    typeInfo: &id004
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
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: tagId
    name: Tag Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
- id: update
  name: Update
  description: Update a field
  params:
  - id: id
    name: Field ID
    type: string
    default: ''
    required: true
    description: The ID of your custom field
    validation: *id007
    typeInfo: *id008
  - id: label
    name: Label
    type: string
    default: ''
    required: true
    description: The label of the custom field
    validation: *id009
    typeInfo: *id010
- id: addSubscriber
  name: Add Subscriber
  description: Add a subscriber
  params:
  - id: id
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The subscriber's email address
    placeholder: name@email.com
    validation: *id011
    typeInfo: *id012
  - id: id
    name: Sequence Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The subscriber's email address
    placeholder: name@email.com
    validation: *id011
    typeInfo: *id012
- id: getSubscriptions
  name: Get Subscriptions
  description: List subscriptions to a form including subscriber data
  params:
  - id: id
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Sequence Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
- id: add
  name: Add
  description: Add a tag to a subscriber
  params:
  - id: tagId
    name: Tag Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Subscriber email address
    placeholder: name@email.com
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
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
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
  "$id": "https://n8n.io/schemas/nodes/convertKit.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ConvertKit Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "getAll",
        "update",
        "addSubscriber",
        "getSubscriptions",
        "add"
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
            "customField",
            "form",
            "sequence",
            "tag",
            "tagSubscriber"
          ],
          "default": "form"
        },
        "operation": {
          "description": "Add a tag to a subscriber",
          "type": "string",
          "enum": [
            "add",
            "getAll",
            "delete"
          ],
          "default": "create"
        },
        "id": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "label": {
          "description": "The label of the custom field",
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
        "email": {
          "description": "Subscriber email address",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "additionalFields": {
          "description": "Receive only active subscribers or cancelled subscribers",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "name": {
          "description": "Tag name, multiple can be added separated by comma",
          "type": "string",
          "default": ""
        },
        "tagId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
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
      "name": "convertKitApi",
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
