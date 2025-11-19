---
title: "Node: Discourse"
slug: "node-discourse"
version: "1"
updated: "2025-11-13"
summary: "Consume Discourse API"
node_type: "regular"
group: "['input']"
---

# Node: Discourse

**Purpose.** Consume Discourse API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:discourse.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **discourseApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `discourseApi` | ✓ | - |

---

## Operations

### Category Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a category |
| Get Many | `getAll` | Get many categories |
| Update | `update` | Update a category |

### Group Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a group |
| Get | `get` | Get a group |
| Get Many | `getAll` | Get many groups |
| Update | `update` | Update a group |

### Post Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a post |
| Get | `get` | Get a post |
| Get Many | `getAll` | Get many posts |
| Update | `update` | Update a post |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a user |
| Get | `get` | Get a user |
| Get Many | `getAll` | Get many users |

### Usergroup Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Create a user to group |
| Remove | `remove` | Remove user from group |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | post | ✗ | Resource to operate on |  |

**Resource options:**

* **Category** (`category`)
* **Group** (`group`)
* **Post** (`post`)
* **Search** (`search`)
* **User** (`user`)
* **User Group** (`userGroup`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✓ | Choose an operation |  |

**Operation options:**

* **Create** (`create`) - Create a category
* **Get Many** (`getAll`) - Get many categories
* **Update** (`update`) - Update a category

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Name of the category |  |
| Color | `color` | color | 0000FF | ✓ | Color of the category |  |
| Text Color | `textColor` | color | 0000FF | ✓ | Text color of the category |  |
| Name | `name` | string |  | ✓ | Name of the group |  |
| Title | `title` | string |  | ✗ | Title of the post |  |
| Content | `content` | string |  | ✓ | Content of the post |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the category. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Category Name or ID | `category` | options |  | ID of the category. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Reply To Post Number | `reply_to_post_number` | string |  | The number of the post to reply to |
| Topic ID | `topic_id` | string |  | ID of the topic |

</details>

| Name | `name` | string |  | ✓ | Name of the user to create |  |
| Email | `email` | string |  | ✓ | Email of the user to create | e.g. name@email.com | email |
| Username | `username` | string |  | ✓ | The username of the user to create |  |
| Password | `password` | string |  | ✓ | The password of the user to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Active | `active` | boolean | False |  |
| Approved | `approved` | boolean | False |  |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Flag | `flag` | options |  | ✗ | User flags to search for |  |

**Flag options:**

* **Active** (`active`)
* **Blocked** (`blocked`)
* **New** (`new`)
* **Staff** (`staff`)
* **Suspect** (`suspect`)
* **Suspended** (`suspended`)

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Whether to sort ascending | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Ascending | `asc` | boolean | True | Whether to sort ascending |
| Order | `order` | options | created | What to order by |
| Show Emails | `showEmails` | boolean | False | Whether to include user email addresses |
| Stats | `stats` | boolean | False | Whether to return user stats |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Category ID | `categoryId` | string |  | ✓ | ID of the category |  |
| Name | `name` | string |  | ✓ | New name of the category |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Color of the category | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Color | `color` | color | 0000FF | Color of the category |
| Text Color | `textColor` | color | 0000FF | Text color of the category |

</details>

| Group ID | `groupId` | string |  | ✓ | ID of the group to update |  |
| Name | `name` | string |  | ✓ | New name of the group |  |
| Post ID | `postId` | string |  | ✓ | ID of the post |  |
| Content | `content` | string |  | ✓ | Content of the post. HTML is supported. |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Edit Reason | `edit_reason` | string |  |  |
| Cooked | `cooked` | boolean | False |  |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Name of the group |  |
| Post ID | `postId` | string |  | ✓ | ID of the post |  |
| By | `by` | options | username | ✓ | What to search by |  |

**By options:**

* **Username** (`username`)
* **SSO External ID** (`externalId`)

| Username | `username` | string |  | ✓ | The username of the user to return |  |
| SSO External ID | `externalId` | string |  | ✓ | Discourse SSO external ID |  |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Usernames | `usernames` | string |  | ✓ | Usernames to add to group. Multiples can be defined separated by comma. |  |
| Group ID | `groupId` | string |  | ✓ | ID of the group |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Usernames | `usernames` | string |  | ✓ | Usernames to remove from group. Multiples can be defined separated by comma. |  |
| Group ID | `groupId` | string |  | ✓ | ID of the group to remove |  |

---

## Load Options Methods

- `getCategories`

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
node: discourse
displayName: Discourse
description: Consume Discourse API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: discourseApi
  required: true
operations:
- id: create
  name: Create
  description: Create a category
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the category
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo: &id002
      type: string
      displayName: Name
      name: name
  - id: color
    name: Color
    type: color
    default: 0000FF
    required: true
    description: Color of the category
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - category
          operation:
          - create
    typeInfo:
      type: color
      displayName: Color
      name: color
  - id: textColor
    name: Text Color
    type: color
    default: 0000FF
    required: true
    description: Text color of the category
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - category
          operation:
          - create
    typeInfo:
      type: color
      displayName: Text Color
      name: textColor
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the group
    validation: *id001
    typeInfo: *id002
  - id: title
    name: Title
    type: string
    default: ''
    required: false
    description: Title of the post
    validation:
      displayOptions:
        show:
          resource:
          - post
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: content
    name: Content
    type: string
    default: ''
    required: true
    description: Content of the post
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - post
          operation:
          - update
    typeInfo: &id008
      type: string
      displayName: Content
      name: content
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the user to create
    validation: *id001
    typeInfo: *id002
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email of the user to create
    placeholder: name@email.com
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
  - id: username
    name: Username
    type: string
    default: ''
    required: true
    description: The username of the user to create
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
          by:
          - username
    typeInfo: &id012
      type: string
      displayName: Username
      name: username
  - id: password
    name: Password
    type: string
    default: ''
    required: true
    description: The password of the user to create
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
      displayName: Password
      name: password
      typeOptions:
        password: true
- id: getAll
  name: Get Many
  description: Get many categories
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
          - user
          operation:
          - getAll
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          resource:
          - user
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
        maxValue: 100
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
    default: 50
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: flag
    name: Flag
    type: options
    default: ''
    required: false
    description: User flags to search for
    validation:
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
    typeInfo:
      type: options
      displayName: Flag
      name: flag
      possibleValues:
      - value: active
        name: Active
        description: ''
      - value: blocked
        name: Blocked
        description: ''
      - value: new
        name: New
        description: ''
      - value: staff
        name: Staff
        description: ''
      - value: suspect
        name: Suspect
        description: ''
      - value: suspended
        name: Suspended
        description: ''
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: update
  name: Update
  description: Update a category
  params:
  - id: categoryId
    name: Category ID
    type: string
    default: ''
    required: true
    description: ID of the category
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - category
          operation:
          - update
    typeInfo:
      type: string
      displayName: Category ID
      name: categoryId
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: New name of the category
    validation: *id001
    typeInfo: *id002
  - id: groupId
    name: Group ID
    type: string
    default: ''
    required: true
    description: ID of the group to update
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - userGroup
          operation:
          - remove
    typeInfo: &id014
      type: string
      displayName: Group ID
      name: groupId
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: New name of the group
    validation: *id001
    typeInfo: *id002
  - id: postId
    name: Post ID
    type: string
    default: ''
    required: true
    description: ID of the post
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - post
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Post ID
      name: postId
  - id: content
    name: Content
    type: string
    default: ''
    required: true
    description: Content of the post. HTML is supported.
    validation: *id007
    typeInfo: *id008
- id: get
  name: Get
  description: Get a group
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the group
    validation: *id001
    typeInfo: *id002
  - id: postId
    name: Post ID
    type: string
    default: ''
    required: true
    description: ID of the post
    validation: *id009
    typeInfo: *id010
  - id: by
    name: By
    type: options
    default: username
    required: true
    description: What to search by
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
    typeInfo:
      type: options
      displayName: By
      name: by
      possibleValues:
      - value: username
        name: Username
        description: ''
      - value: externalId
        name: SSO External ID
        description: ''
  - id: username
    name: Username
    type: string
    default: ''
    required: true
    description: The username of the user to return
    validation: *id011
    typeInfo: *id012
  - id: externalId
    name: SSO External ID
    type: string
    default: ''
    required: true
    description: Discourse SSO external ID
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
          by:
          - externalId
    typeInfo:
      type: string
      displayName: SSO External ID
      name: externalId
- id: add
  name: Add
  description: Create a user to group
  params:
  - id: usernames
    name: Usernames
    type: string
    default: ''
    required: true
    description: Usernames to add to group. Multiples can be defined separated by
      comma.
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - userGroup
          operation:
          - remove
    typeInfo: &id016
      type: string
      displayName: Usernames
      name: usernames
  - id: groupId
    name: Group ID
    type: string
    default: ''
    required: true
    description: ID of the group
    validation: *id013
    typeInfo: *id014
- id: remove
  name: Remove
  description: Remove user from group
  params:
  - id: usernames
    name: Usernames
    type: string
    default: ''
    required: true
    description: Usernames to remove from group. Multiples can be defined separated
      by comma.
    validation: *id015
    typeInfo: *id016
  - id: groupId
    name: Group ID
    type: string
    default: ''
    required: true
    description: ID of the group to remove
    validation: *id013
    typeInfo: *id014
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/discourse.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Discourse Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "getAll",
        "update",
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
            "category",
            "group",
            "post",
            "search",
            "user",
            "userGroup"
          ],
          "default": "post"
        },
        "operation": {
          "description": "Choose an operation",
          "type": "string",
          "enum": [
            "add",
            "remove"
          ],
          "default": "add"
        },
        "name": {
          "description": "Name of the user to create",
          "type": "string",
          "default": ""
        },
        "color": {
          "description": "Color of the category",
          "type": "string",
          "default": "0000FF"
        },
        "textColor": {
          "description": "Text color of the category",
          "type": "string",
          "default": "0000FF"
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
        "categoryId": {
          "description": "ID of the category",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "groupId": {
          "description": "ID of the group to remove",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "Title of the post",
          "type": "string",
          "default": ""
        },
        "content": {
          "description": "Content of the post. HTML is supported.",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "postId": {
          "description": "ID of the post",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "Email of the user to create",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "username": {
          "description": "The username of the user to return",
          "type": "string",
          "default": ""
        },
        "password": {
          "description": "The password of the user to create",
          "type": "string",
          "default": ""
        },
        "by": {
          "description": "What to search by",
          "type": "string",
          "enum": [
            "username",
            "externalId"
          ],
          "default": "username"
        },
        "externalId": {
          "description": "Discourse SSO external ID",
          "type": "string",
          "default": ""
        },
        "flag": {
          "description": "User flags to search for",
          "type": "string",
          "enum": [
            "active",
            "blocked",
            "new",
            "staff",
            "suspect",
            "suspended"
          ],
          "default": ""
        },
        "options": {
          "description": "Whether to sort ascending",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "usernames": {
          "description": "Usernames to remove from group. Multiples can be defined separated by comma.",
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
      "name": "discourseApi",
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
