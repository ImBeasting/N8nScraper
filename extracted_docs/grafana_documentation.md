---
title: "Node: Grafana"
slug: "node-grafana"
version: "1"
updated: "2025-11-13"
summary: "Consume the Grafana API"
node_type: "regular"
group: "['transform']"
---

# Node: Grafana

**Purpose.** Consume the Grafana API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:grafana.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **grafanaApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `grafanaApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a user from the current organization |
| Get Many | `getAll` | Retrieve many users in the current organization |
| Update | `update` | Update a user in the current organization |

### Dashboard Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a dashboard |
| Delete | `delete` | Delete a dashboard |
| Get | `get` | Get a dashboard |
| Get Many | `getAll` | Get many dashboards |
| Update | `update` | Update a dashboard |

### Team Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a team |
| Delete | `delete` | Delete a team |
| Get | `get` | Get a team |
| Get Many | `getAll` | Retrieve many teams |
| Update | `update` | Update a team |

### Teammember Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a member to a team |
| Get Many | `getAll` | Retrieve many team members |
| Remove | `remove` | Remove a member from a team |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | dashboard | ✗ | Resource to operate on |  |

**Resource options:**

* **Dashboard** (`dashboard`)
* **Team** (`team`)
* **Team Member** (`teamMember`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Delete a user from the current organization |  |

**Operation options:**

* **Delete** (`delete`) - Delete a user from the current organization
* **Get Many** (`getAll`) - Retrieve many users in the current organization
* **Update** (`update`) - Update a user in the current organization

---

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✓ | ID of the user to delete |  |
| Dashboard UID or URL | `dashboardUidOrUrl` | string |  | ✓ | Unique alphabetic identifier or URL of the dashboard to delete | e.g. cIBgcSjkk | url |
| Team ID | `teamId` | string |  | ✓ | ID of the team to delete |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Search Query | `query` | string |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Name of the team to filter by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | Name of the team to filter by |

</details>

| Team Name or ID | `teamId` | options |  | ✓ | Team to retrieve all members from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✓ | ID of the user to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | New role for the user | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Role | `role` | options | Admin | New role for the user |

</details>

| Dashboard UID or URL | `dashboardUidOrUrl` | string |  | ✓ | Unique alphabetic identifier or URL of the dashboard to update | e.g. cIBgcSjkk | url |
| Update Fields | `updateFields` | collection | {} | ✗ | Folder to move the dashboard into - if the folder is unspecified, the dashboard will be saved to the General folder. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Folder Name or ID | `folderId` | options |  | Folder to move the dashboard into - if the folder is unspecified, the dashboard will be saved to the General folder. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Title | `title` | string |  | New title of the dashboard |

</details>

| Team ID | `teamId` | string |  | ✓ | ID of the team to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Email of the team to update | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  | Email of the team to update |
| Name | `name` | string |  | Name of the team to update |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ | Title of the dashboard to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Folder to create the dashboard in - if the folder is unspecified, the dashboard will be saved to the General folder. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Folder Name or ID | `folderId` | options |  | Folder to create the dashboard in - if the folder is unspecified, the dashboard will be saved to the General folder. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Name | `name` | string |  | ✓ | Name of the team to create | e.g. Engineering |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Email of the team to create | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  | Email of the team to create |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Dashboard UID or URL | `dashboardUidOrUrl` | string |  | ✓ | Unique alphabetic identifier or URL of the dashboard to retrieve | e.g. cIBgcSjkk | url |
| Team ID | `teamId` | string |  | ✓ | ID of the team to retrieve |  |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User Name or ID | `userId` | options |  | ✓ | User to add to a team. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Team Name or ID | `teamId` | options |  | ✓ | Team to add the user to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User Name or ID | `memberId` | options |  | ✓ | User to remove from the team. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Team Name or ID | `teamId` | options |  | ✓ | Team to remove the user from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

---

## Load Options Methods

- `getDashboards`

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
* Categories: Development, Analytics
* Aliases: Prometheus

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: grafana
displayName: Grafana
description: Consume the Grafana API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: grafanaApi
  required: true
operations:
- id: delete
  name: Delete
  description: Delete a user from the current organization
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: ID of the user to delete
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - teamMember
          operation:
          - add
    typeInfo: &id008
      type: options
      displayName: User Name or ID
      name: userId
      typeOptions:
        loadOptionsMethod: getUsers
      possibleValues: []
  - id: dashboardUidOrUrl
    name: Dashboard UID or URL
    type: string
    default: ''
    required: true
    description: Unique alphabetic identifier or URL of the dashboard to delete
    placeholder: cIBgcSjkk
    validation: &id009
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - dashboard
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Dashboard UID or URL
      name: dashboardUidOrUrl
  - id: teamId
    name: Team ID
    type: string
    default: ''
    required: true
    description: ID of the team to delete
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - teamMember
          operation:
          - getAll
    typeInfo: &id006
      type: options
      displayName: Team Name or ID
      name: teamId
      typeOptions:
        loadOptionsMethod: getTeams
      possibleValues: []
- id: getAll
  name: Get Many
  description: Retrieve many users in the current organization
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
          resource:
          - teamMember
          operation:
          - getAll
    typeInfo: &id002
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id003
      displayOptions:
        show:
          resource:
          - teamMember
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id004
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
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 50
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: teamId
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Team to retrieve all members from. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
- id: update
  name: Update
  description: Update a user in the current organization
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: ID of the user to update
    validation: *id007
    typeInfo: *id008
  - id: dashboardUidOrUrl
    name: Dashboard UID or URL
    type: string
    default: ''
    required: true
    description: Unique alphabetic identifier or URL of the dashboard to update
    placeholder: cIBgcSjkk
    validation: *id009
    typeInfo: *id010
  - id: teamId
    name: Team ID
    type: string
    default: ''
    required: true
    description: ID of the team to update
    validation: *id005
    typeInfo: *id006
- id: create
  name: Create
  description: Create a dashboard
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the dashboard to create
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - dashboard
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the team to create
    placeholder: Engineering
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - team
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
- id: get
  name: Get
  description: Get a dashboard
  params:
  - id: dashboardUidOrUrl
    name: Dashboard UID or URL
    type: string
    default: ''
    required: true
    description: Unique alphabetic identifier or URL of the dashboard to retrieve
    placeholder: cIBgcSjkk
    validation: *id009
    typeInfo: *id010
  - id: teamId
    name: Team ID
    type: string
    default: ''
    required: true
    description: ID of the team to retrieve
    validation: *id005
    typeInfo: *id006
- id: add
  name: Add
  description: Add a member to a team
  params:
  - id: userId
    name: User Name or ID
    type: options
    default: ''
    required: true
    description: User to add to a team. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
  - id: teamId
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Team to add the user to. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
- id: remove
  name: Remove
  description: Remove a member from a team
  params:
  - id: memberId
    name: User Name or ID
    type: options
    default: ''
    required: true
    description: User to remove from the team. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - teamMember
          operation:
          - remove
    typeInfo:
      type: options
      displayName: User Name or ID
      name: memberId
      typeOptions:
        loadOptionsMethod: getUsers
      possibleValues: []
  - id: teamId
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Team to remove the user from. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
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
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: dashboardUidOrUrl
    text: cIBgcSjkk
  - field: dashboardUidOrUrl
    text: cIBgcSjkk
  - field: filters
    text: Add Filter
  - field: dashboardUidOrUrl
    text: cIBgcSjkk
  - field: updateFields
    text: Add Field
  - field: name
    text: Engineering
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: updateFields
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
  "$id": "https://n8n.io/schemas/nodes/grafana.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Grafana Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "delete",
        "getAll",
        "update",
        "create",
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
            "dashboard",
            "team",
            "teamMember",
            "user"
          ],
          "default": "dashboard"
        },
        "operation": {
          "description": "Add a member to a team",
          "type": "string",
          "enum": [
            "add",
            "getAll",
            "remove"
          ],
          "default": "add"
        },
        "userId": {
          "description": "User to add to a team. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Email of the team to update",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
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
        "title": {
          "description": "Title of the dashboard to create",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Email of the team to create",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "dashboardUidOrUrl": {
          "description": "Unique alphabetic identifier or URL of the dashboard to update",
          "type": "string",
          "default": "",
          "format": "url",
          "examples": [
            "cIBgcSjkk"
          ]
        },
        "filters": {
          "description": "Name of the team to filter by",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "name": {
          "description": "Name of the team to create",
          "type": "string",
          "default": "",
          "examples": [
            "Engineering"
          ]
        },
        "teamId": {
          "description": "Team to retrieve all members from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "memberId": {
          "description": "User to remove from the team. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
      "name": "grafanaApi",
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
