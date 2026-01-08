---
title: "Node: Bitwarden"
slug: "node-bitwarden"
version: "1"
updated: "2026-01-08"
summary: "Consume the Bitwarden API"
node_type: "regular"
group: "['transform']"
---

# Node: Bitwarden

**Purpose.** Consume the Bitwarden API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:bitwarden.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **bitwardenApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `bitwardenApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

**Headers Used:** user-agent, Content-Type

---

## Operations

### Collection Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a collection |
| Get | `get` | Get a collection |
| Get Many | `getAll` | Get many collections |
| Update | `update` | Update a collection |

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many events |

### Group Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a group |
| Delete | `delete` | Delete a group |
| Get | `get` | Get a group |
| Get Many | `getAll` | Get many groups |
| Get Members | `getMembers` | Get group members |
| Update | `update` | Update a group |
| Update Members | `updateMembers` | Update group members |

### Member Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a member |
| Delete | `delete` | Delete a member |
| Get | `get` | Get a member |
| Get Groups | `getGroups` | Get groups for a member |
| Get Many | `getAll` | Get many members |
| Update | `update` | Update a member |
| Update Groups | `updateGroups` | Update groups for a member |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | collection | ✗ | Resource to operate on |  |

**Resource options:**

* **Collection** (`collection`)
* **Event** (`event`)
* **Group** (`group`)
* **Member** (`member`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Delete** (`delete`) - Delete a collection
* **Get** (`get`) - Get a collection
* **Get Many** (`getAll`) - Get many collections
* **Update** (`update`) - Update a collection

---

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Collection ID | `collectionId` | string |  | ✓ | The identifier of the collection | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |
| Group ID | `groupId` | string |  | ✓ | The identifier of the group | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |
| Member ID | `memberId` | string |  | ✓ | The identifier of the member | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Collection ID | `collectionId` | string |  | ✓ | The identifier of the collection | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |
| Group ID | `groupId` | string |  | ✓ | The identifier of the group | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |
| Member ID | `memberId` | string |  | ✓ | The identifier of the member | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | The unique identifier of the acting user | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Acting User ID | `actingUserId` | string |  | The unique identifier of the acting user |
| End Date | `end` | dateTime |  | The end date for the search |
| Item ID | `itemID` | string |  | The unique identifier of the item that the event describes |
| Start Date | `start` | dateTime |  | The start date for the search |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:∞ |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Collection ID | `collectionId` | string |  | ✓ | The identifier of the collection | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |
| Update Fields | `updateFields` | collection | {} | ✓ | The group to assign this collection to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Group Names or IDs | `groups` | multiOptions | [] | The group to assign this collection to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| External ID | `externalId` | string |  | The external identifier to set to this collection |

</details>

| Group ID | `groupId` | string |  | ✓ | The identifier of the group | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Whether to allow this group to access all collections within the organization, instead of only its associated collections. If set to true, this option overrides any collection assignments. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Access All | `accessAll` | boolean | False | Whether to allow this group to access all collections within the organization, instead of only its associated collections. If set to true, this option overrides any collection assignments. |
| Collection Names or IDs | `collections` | multiOptions | [] | The collections to assign to this group. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| External ID | `externalId` | string |  | The external identifier to set to this group |
| Name | `name` | string |  | The name of the group to update |

</details>

| Member ID | `memberId` | string |  | ✓ | The identifier of the member | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The collections to assign to this member. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Type | `type` | options | {} |  |
| Collection Names or IDs | `collections` | multiOptions | [] | The collections to assign to this member. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| External ID | `externalId` | string |  | The external identifier to set to this member |
| Access All | `accessAll` | boolean | False |  |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | The name of the group to create |  |
| Access All | `accessAll` | boolean | False | ✗ | Whether to allow this group to access all collections within the organization, instead of only its associated collections. If set to true, this option overrides any collection assignments. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The collections to assign to this group. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Collection Names or IDs | `collections` | multiOptions | [] | The collections to assign to this group. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| External ID | `externalId` | string |  | The external identifier to set to this group |

</details>

| Type | `type` | options | 2 | ✓ |  |  |

**Type options:**

* **Owner** (``)
* **Admin** (``)
* **User** (``)
* **Manager** (``)

| Email | `email` | string |  | ✗ | The email of the member to update | e.g. name@email.com | email |
| Access All | `accessAll` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The collections to assign to this member. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Collection Names or IDs | `collections` | multiOptions | [] | The collections to assign to this member. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| External ID | `externalId` | string |  | The external identifier to set to this member |

</details>


### Get Members parameters (`getMembers`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Group ID | `groupId` | string |  | ✓ | The identifier of the group | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |

### Update Members parameters (`updateMembers`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Group ID | `groupId` | string |  | ✓ | The identifier of the group | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |
| Member IDs | `memberIds` | string |  | ✗ | Comma-separated list of IDs of members to set in a group |  |

### Get Groups parameters (`getGroups`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Member ID | `memberId` | string |  | ✓ | The identifier of the member | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |

### Update Groups parameters (`updateGroups`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Member ID | `memberId` | string |  | ✓ | The identifier of the member | e.g. 5e59c8c7-e05a-4d17-8e85-acc301343926 |  |
| Group IDs | `groupIds` | string |  | ✗ | Comma-separated list of IDs of groups to set for a member |  |

---

## Load Options Methods

- `getGroups`

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
* Categories: Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: bitwarden
displayName: Bitwarden
description: Consume the Bitwarden API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: bitwardenApi
  required: true
operations:
- id: delete
  name: Delete
  description: ''
  params:
  - id: collectionId
    name: Collection ID
    type: string
    default: ''
    required: true
    description: The identifier of the collection
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - collection
          operation:
          - delete
          - get
          - update
    typeInfo: &id002
      type: string
      displayName: Collection ID
      name: collectionId
  - id: groupId
    name: Group ID
    type: string
    default: ''
    required: true
    description: The identifier of the group
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - group
          operation:
          - delete
          - get
          - getMembers
          - update
          - updateMembers
    typeInfo: &id004
      type: string
      displayName: Group ID
      name: groupId
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: The identifier of the member
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - delete
          - get
          - getGroups
          - update
          - updateGroups
    typeInfo: &id006
      type: string
      displayName: Member ID
      name: memberId
- id: get
  name: Get
  description: ''
  params:
  - id: collectionId
    name: Collection ID
    type: string
    default: ''
    required: true
    description: The identifier of the collection
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: *id001
    typeInfo: *id002
  - id: groupId
    name: Group ID
    type: string
    default: ''
    required: true
    description: The identifier of the group
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: *id003
    typeInfo: *id004
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: The identifier of the member
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: *id005
    typeInfo: *id006
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id007
      displayOptions:
        show:
          resource:
          - member
          operation:
          - getAll
    typeInfo: &id008
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: &id009
      displayOptions:
        show:
          resource:
          - member
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id010
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
    validation: *id007
    typeInfo: *id008
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id007
    typeInfo: *id008
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id007
    typeInfo: *id008
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
- id: update
  name: Update
  description: ''
  params:
  - id: collectionId
    name: Collection ID
    type: string
    default: ''
    required: true
    description: The identifier of the collection
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: *id001
    typeInfo: *id002
  - id: groupId
    name: Group ID
    type: string
    default: ''
    required: true
    description: The identifier of the group
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: *id003
    typeInfo: *id004
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: The identifier of the member
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: *id005
    typeInfo: *id006
- id: create
  name: Create
  description: ''
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the group to create
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - group
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: accessAll
    name: Access All
    type: boolean
    default: false
    required: false
    description: Whether to allow this group to access all collections within the
      organization, instead of only its associated collections. If set to true, this
      option overrides any collection assignments.
    validation: &id011
      displayOptions:
        show:
          resource:
          - member
          operation:
          - create
    typeInfo: &id012
      type: boolean
      displayName: Access All
      name: accessAll
  - id: type
    name: Type
    type: options
    default: 2
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - create
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: Owner
        name: Owner
        description: ''
      - value: Admin
        name: Admin
        description: ''
      - value: User
        name: User
        description: ''
      - value: Manager
        name: Manager
        description: ''
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: The email of the member to update
    placeholder: name@email.com
    validation:
      format: email
      displayOptions:
        show:
          resource:
          - member
          operation:
          - create
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: accessAll
    name: Access All
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id011
    typeInfo: *id012
- id: getMembers
  name: Get Members
  description: ''
  params:
  - id: groupId
    name: Group ID
    type: string
    default: ''
    required: true
    description: The identifier of the group
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: *id003
    typeInfo: *id004
- id: updateMembers
  name: Update Members
  description: ''
  params:
  - id: groupId
    name: Group ID
    type: string
    default: ''
    required: true
    description: The identifier of the group
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: *id003
    typeInfo: *id004
  - id: memberIds
    name: Member IDs
    type: string
    default: ''
    required: false
    description: Comma-separated list of IDs of members to set in a group
    validation:
      displayOptions:
        show:
          resource:
          - group
          operation:
          - updateMembers
    typeInfo:
      type: string
      displayName: Member IDs
      name: memberIds
- id: getGroups
  name: Get Groups
  description: ''
  params:
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: The identifier of the member
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: *id005
    typeInfo: *id006
- id: updateGroups
  name: Update Groups
  description: ''
  params:
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: The identifier of the member
    placeholder: 5e59c8c7-e05a-4d17-8e85-acc301343926
    validation: *id005
    typeInfo: *id006
  - id: groupIds
    name: Group IDs
    type: string
    default: ''
    required: false
    description: Comma-separated list of IDs of groups to set for a member
    validation:
      displayOptions:
        show:
          resource:
          - member
          operation:
          - updateGroups
    typeInfo:
      type: string
      displayName: Group IDs
      name: groupIds
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - POST
  endpoints: []
  headers:
  - user-agent
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: collectionId
    text: 5e59c8c7-e05a-4d17-8e85-acc301343926
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: groupId
    text: 5e59c8c7-e05a-4d17-8e85-acc301343926
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: memberId
    text: 5e59c8c7-e05a-4d17-8e85-acc301343926
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/bitwarden.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Bitwarden Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "delete",
        "get",
        "getAll",
        "update",
        "create",
        "getMembers",
        "updateMembers",
        "getGroups",
        "updateGroups"
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
            "collection",
            "event",
            "group",
            "member"
          ],
          "default": "collection"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getGroups",
            "getAll",
            "update",
            "updateGroups"
          ],
          "default": "get"
        },
        "collectionId": {
          "description": "The identifier of the collection",
          "type": "string",
          "default": "",
          "examples": [
            "5e59c8c7-e05a-4d17-8e85-acc301343926"
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
          "default": 10
        },
        "updateFields": {
          "description": "The collections to assign to this member. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "filters": {
          "description": "The unique identifier of the acting user",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "groupId": {
          "description": "The identifier of the group",
          "type": "string",
          "default": "",
          "examples": [
            "5e59c8c7-e05a-4d17-8e85-acc301343926"
          ]
        },
        "name": {
          "description": "The name of the group to create",
          "type": "string",
          "default": ""
        },
        "accessAll": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "additionalFields": {
          "description": "The collections to assign to this member. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "memberIds": {
          "description": "Comma-separated list of IDs of members to set in a group",
          "type": "string",
          "default": ""
        },
        "memberId": {
          "description": "The identifier of the member",
          "type": "string",
          "default": "",
          "examples": [
            "5e59c8c7-e05a-4d17-8e85-acc301343926"
          ]
        },
        "type": {
          "description": "",
          "type": "string",
          "enum": [
            "Owner",
            "Admin",
            "User",
            "Manager"
          ],
          "default": 2
        },
        "email": {
          "description": "The email of the member to update",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "groupIds": {
          "description": "Comma-separated list of IDs of groups to set for a member",
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
      "name": "bitwardenApi",
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
