---
title: "Node: Microsoft Entra ID"
slug: "node-microsoftentra"
version: "1"
updated: "2026-01-08"
summary: "Interact with Microsoft Entra ID API"
node_type: "regular"
group: "['transform']"
---

# Node: Microsoft Entra ID

**Purpose.** Interact with Microsoft Entra ID API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:microsoftEntra.svg', 'dark': 'file:microsoftEntra.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftEntraOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `microsoftEntraOAuth2Api` | ✓ | - |

---

## API Patterns

**Common Endpoints:**
- `={{ $response.body?.[`

---

## Operations

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Group Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | user | ✗ | Resource to operate on |  |

**Resource options:**

* **Group** (`group`)
* **User** (`user`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | user | ✗ |  |  |

**Resource options:**

* **Group** (`group`)
* **User** (`user`)

| Operation | `operation` | options | getAll | ✗ | Add user to group |  |
| Group | `group` | list |  | ✓ | e.g. e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315 |  |
| User to Add | `user` | list |  | ✓ | e.g. e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315 |  |
| Account Enabled | `accountEnabled` | body | True | ✓ | Whether the account is enabled |  |
| Display Name | `displayName` | body |  | ✓ | The name to display in the address book for the user | e.g. e.g. Nathan Smith |  |
| User Principal Name | `userPrincipalName` | body |  | ✓ | The user principal name (UPN) | e.g. e.g. NathanSmith@contoso.com |  |
| Mail Nickname | `mailNickname` | body |  | ✓ | The mail alias for the user | e.g. e.g. NathanSmith |  |
| Password | `password` | body |  | ✓ | The password for the user |  |
| Additional Fields | `additionalFields` | string | {} | ✗ | A freeform text entry field for the user to describe themselves | e.g. e.g. US |  |
| User to Delete | `user` | list |  | ✓ | e.g. e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315 |  |
| User to Get | `user` | list |  | ✓ | e.g. e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315 |  |
| Output | `output` | query | simple | ✗ |  |  |
| Fields | `fields` | query | [] | ✗ | The fields to add to the output |  |
| Return All | `returnAll` | generic | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | query | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filter | `filter` | query |  | ✗ | <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">Query parameter</a> to filter results by | e.g. e.g. startswith(displayName, 'a') |  |
| Output | `output` | query | simple | ✗ |  |  |
| Fields | `fields` | query | [] | ✗ | The fields to add to the output |  |
| Group | `group` | list |  | ✓ | e.g. e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315 |  |
| User to Remove | `user` | list |  | ✓ | e.g. e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315 |  |
| User to Update | `user` | list |  | ✓ | e.g. e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315 |  |
| Update Fields | `updateFields` | string | {} | ✗ | A freeform text entry field for the user to describe themselves | e.g. e.g. US |  |
| Group Type | `groupType` | options |  | ✗ |  |  |

**Group Type options:**

* **Microsoft 365** (`Unified`)
* **Security** (``)

| Group Name | `displayName` | body |  | ✓ | The name to display in the address book for the group |  |
| Group Email Address | `mailNickname` | body |  | ✓ | The mail alias for the group. Only enter the local-part without the domain. | e.g. e.g. alias |  |
| Mail Enabled | `mailEnabled` | body | False | ✓ | Whether the group is mail-enabled |  |
| Membership Type | `membershipType` | options |  | ✗ | Lets you add specific users as members of a group and have unique permissions |  |

**Membership Type options:**

* **Assigned** (``) - Lets you add specific users as members of a group and have unique permissions
* **Dynamic** (`DynamicMembership`) - Lets you use rules to automatically add and remove users as members

| Security Enabled | `securityEnabled` | body | True | ✗ | Whether the group is a security group |  |
| Additional Fields | `additionalFields` | body | {} | ✗ | Whether Microsoft Entra roles can be assigned to the group | e.g. e.g. user.department -eq "Marketing" |  |
| Group to Delete | `group` | list |  | ✓ | e.g. e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315 |  |
| Group to Get | `group` | list |  | ✓ | e.g. e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315 |  |
| Output | `output` | query | simple | ✗ |  |  |
| Fields | `fields` | query | [] | ✗ | The fields to add to the output |  |
| Options | `options` | query | {} | ✗ | e.g. Add Option |  |
| Return All | `returnAll` | generic | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | query | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filter | `filter` | query |  | ✗ | <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">Query parameter</a> to filter results by | e.g. e.g. startswith(displayName, 'a') |  |
| Output | `output` | query | simple | ✗ |  |  |
| Fields | `fields` | query | [] | ✗ | The fields to add to the output |  |
| Group to Update | `group` | list |  | ✓ | e.g. e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315 |  |
| Update Fields | `updateFields` | boolean | {} | ✗ | Whether people external to the organization can send messages to the group. Wait a few seconds before editing this field in a newly created group. | e.g. e.g. alias |  |
| Operation | `operation` | options | getAll | ✗ | Create a group |  |

---

## Load Options Methods

- `getGroupPropertiesGetAll`
- `return`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ !!$response.body?.["@odata.nextLink"] }}`
- `={{ $response.body?.["@odata.nextLink"] ?? $request.url }}`
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
* Categories: Development, Developer Tools

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: microsoftEntra
displayName: Microsoft Entra ID
description: Interact with Microsoft Entra ID API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: microsoftEntraOAuth2Api
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
    - value: group
      name: Group
      description: ''
    - value: user
      name: User
      description: ''
- id: operation
  name: Operation
  type: options
  default: getAll
  required: false
  description: Add user to group
  validation: &id023
    displayOptions:
      show:
        resource:
        - group
  typeInfo: &id024
    type: options
    displayName: Operation
    name: operation
    possibleValues: []
- id: group
  name: Group
  type: list
  default: ''
  required: true
  description: ''
  placeholder: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  validation: &id007
    required: true
    displayOptions:
      show:
        resource:
        - group
        operation:
        - update
  typeInfo: &id008
    type: list
    displayName: Group to Update
    name: group
- id: user
  name: User to Add
  type: list
  default: ''
  required: true
  description: ''
  placeholder: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  validation: &id001
    required: true
    displayOptions:
      show:
        resource:
        - user
        operation:
        - update
  typeInfo: &id002
    type: list
    displayName: User to Update
    name: user
- id: accountEnabled
  name: Account Enabled
  type: body
  default: true
  required: true
  description: Whether the account is enabled
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - user
        operation:
        - create
  typeInfo:
    type: body
    displayName: Account Enabled
    name: accountEnabled
- id: displayName
  name: Display Name
  type: body
  default: ''
  required: true
  description: The name to display in the address book for the user
  placeholder: e.g. Nathan Smith
  validation: &id009
    required: true
    displayOptions:
      show:
        resource:
        - group
        operation:
        - create
  typeInfo: &id010
    type: body
    displayName: Group Name
    name: displayName
- id: userPrincipalName
  name: User Principal Name
  type: body
  default: ''
  required: true
  description: The user principal name (UPN)
  placeholder: e.g. NathanSmith@contoso.com
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - user
        operation:
        - create
  typeInfo:
    type: body
    displayName: User Principal Name
    name: userPrincipalName
- id: mailNickname
  name: Mail Nickname
  type: body
  default: ''
  required: true
  description: The mail alias for the user
  placeholder: e.g. NathanSmith
  validation: &id011
    required: true
    displayOptions:
      show:
        resource:
        - group
        operation:
        - create
  typeInfo: &id012
    type: body
    displayName: Group Email Address
    name: mailNickname
- id: password
  name: Password
  type: body
  default: ''
  required: true
  description: The password for the user
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - user
        operation:
        - create
  typeInfo:
    type: body
    displayName: Password
    name: password
    typeOptions:
      password: true
- id: additionalFields
  name: Additional Fields
  type: string
  default: {}
  required: false
  description: A freeform text entry field for the user to describe themselves
  placeholder: e.g. US
  validation: &id013
    displayOptions:
      show:
        resource:
        - group
        operation:
        - create
  typeInfo: &id014
    type: body
    displayName: Additional Fields
    name: additionalFields
- id: user
  name: User to Delete
  type: list
  default: ''
  required: true
  description: ''
  placeholder: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  validation: *id001
  typeInfo: *id002
- id: user
  name: User to Get
  type: list
  default: ''
  required: true
  description: ''
  placeholder: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  validation: *id001
  typeInfo: *id002
- id: output
  name: Output
  type: query
  default: simple
  required: false
  description: ''
  validation: &id003
    displayOptions:
      show:
        resource:
        - group
        operation:
        - getAll
  typeInfo: &id004
    type: query
    displayName: Output
    name: output
- id: fields
  name: Fields
  type: query
  default: []
  required: false
  description: The fields to add to the output
  validation: &id005
    displayOptions:
      show:
        resource:
        - group
        operation:
        - getAll
        output:
        - fields
  typeInfo: &id006
    type: query
    displayName: Fields
    name: fields
    typeOptions:
      loadOptionsMethod: getGroupPropertiesGetAll
- id: returnAll
  name: Return All
  type: generic
  default: false
  required: false
  description: Whether to return all results or only up to a given limit
  validation: &id015
    displayOptions:
      show:
        resource:
        - group
        operation:
        - getAll
  typeInfo: &id016
    type: generic
    displayName: Return All
    name: returnAll
- id: limit
  name: Limit
  type: query
  default: 50
  required: false
  description: Max number of results to return
  validation: &id017
    displayOptions:
      show:
        resource:
        - group
        operation:
        - getAll
        returnAll:
        - false
  typeInfo: &id018
    type: query
    displayName: Limit
    name: limit
    typeOptions:
      minValue: 1
- id: filter
  name: Filter
  type: query
  default: ''
  required: false
  description: <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">Query
    parameter</a> to filter results by
  placeholder: e.g. startswith(displayName, 'a')
  validation: &id019
    displayOptions:
      show:
        resource:
        - group
        operation:
        - getAll
  typeInfo: &id020
    type: query
    displayName: Filter
    name: filter
- id: output
  name: Output
  type: query
  default: simple
  required: false
  description: ''
  validation: *id003
  typeInfo: *id004
- id: fields
  name: Fields
  type: query
  default: []
  required: false
  description: The fields to add to the output
  validation: *id005
  typeInfo: *id006
- id: group
  name: Group
  type: list
  default: ''
  required: true
  description: ''
  placeholder: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  validation: *id007
  typeInfo: *id008
- id: user
  name: User to Remove
  type: list
  default: ''
  required: true
  description: ''
  placeholder: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  validation: *id001
  typeInfo: *id002
- id: user
  name: User to Update
  type: list
  default: ''
  required: true
  description: ''
  placeholder: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  validation: *id001
  typeInfo: *id002
- id: updateFields
  name: Update Fields
  type: string
  default: {}
  required: false
  description: A freeform text entry field for the user to describe themselves
  placeholder: e.g. US
  validation: &id021
    displayOptions:
      show:
        resource:
        - group
        operation:
        - update
  typeInfo: &id022
    type: boolean
    displayName: Update Fields
    name: updateFields
- id: groupType
  name: Group Type
  type: options
  default: ''
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        resource:
        - group
        operation:
        - create
  typeInfo:
    type: options
    displayName: Group Type
    name: groupType
    possibleValues:
    - value: Unified
      name: Microsoft 365
      description: ''
    - value: Security
      name: Security
      description: ''
- id: displayName
  name: Group Name
  type: body
  default: ''
  required: true
  description: The name to display in the address book for the group
  validation: *id009
  typeInfo: *id010
- id: mailNickname
  name: Group Email Address
  type: body
  default: ''
  required: true
  description: The mail alias for the group. Only enter the local-part without the
    domain.
  placeholder: e.g. alias
  validation: *id011
  typeInfo: *id012
- id: mailEnabled
  name: Mail Enabled
  type: body
  default: false
  required: true
  description: Whether the group is mail-enabled
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - group
        operation:
        - create
        groupType:
        - Unified
  typeInfo:
    type: body
    displayName: Mail Enabled
    name: mailEnabled
- id: membershipType
  name: Membership Type
  type: options
  default: ''
  required: false
  description: Lets you add specific users as members of a group and have unique permissions
  validation:
    displayOptions:
      show:
        resource:
        - group
        operation:
        - create
  typeInfo:
    type: options
    displayName: Membership Type
    name: membershipType
    possibleValues:
    - value: Assigned
      name: Assigned
      description: Lets you add specific users as members of a group and have unique
        permissions
    - value: DynamicMembership
      name: Dynamic
      description: Lets you use rules to automatically add and remove users as members
- id: securityEnabled
  name: Security Enabled
  type: body
  default: true
  required: false
  description: Whether the group is a security group
  validation:
    displayOptions:
      show:
        resource:
        - group
        operation:
        - create
        groupType:
        - Unified
  typeInfo:
    type: body
    displayName: Security Enabled
    name: securityEnabled
- id: additionalFields
  name: Additional Fields
  type: body
  default: {}
  required: false
  description: Whether Microsoft Entra roles can be assigned to the group
  placeholder: e.g. user.department -eq "Marketing"
  validation: *id013
  typeInfo: *id014
- id: group
  name: Group to Delete
  type: list
  default: ''
  required: true
  description: ''
  placeholder: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  validation: *id007
  typeInfo: *id008
- id: group
  name: Group to Get
  type: list
  default: ''
  required: true
  description: ''
  placeholder: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  validation: *id007
  typeInfo: *id008
- id: output
  name: Output
  type: query
  default: simple
  required: false
  description: ''
  validation: *id003
  typeInfo: *id004
- id: fields
  name: Fields
  type: query
  default: []
  required: false
  description: The fields to add to the output
  validation: *id005
  typeInfo: *id006
- id: options
  name: Options
  type: query
  default: {}
  required: false
  description: ''
  placeholder: Add Option
  validation:
    displayOptions:
      show:
        resource:
        - group
        operation:
        - get
  typeInfo:
    type: query
    displayName: Options
    name: options
- id: returnAll
  name: Return All
  type: generic
  default: false
  required: false
  description: Whether to return all results or only up to a given limit
  validation: *id015
  typeInfo: *id016
- id: limit
  name: Limit
  type: query
  default: 50
  required: false
  description: Max number of results to return
  validation: *id017
  typeInfo: *id018
- id: filter
  name: Filter
  type: query
  default: ''
  required: false
  description: <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">Query
    parameter</a> to filter results by
  hint: If empty, all the groups will be returned
  placeholder: e.g. startswith(displayName, 'a')
  validation: *id019
  typeInfo: *id020
- id: output
  name: Output
  type: query
  default: simple
  required: false
  description: ''
  validation: *id003
  typeInfo: *id004
- id: fields
  name: Fields
  type: query
  default: []
  required: false
  description: The fields to add to the output
  validation: *id005
  typeInfo: *id006
- id: group
  name: Group to Update
  type: list
  default: ''
  required: true
  description: ''
  placeholder: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  validation: *id007
  typeInfo: *id008
- id: updateFields
  name: Update Fields
  type: boolean
  default: {}
  required: false
  description: Whether people external to the organization can send messages to the
    group. Wait a few seconds before editing this field in a newly created group.
  placeholder: e.g. alias
  validation: *id021
  typeInfo: *id022
- id: operation
  name: Operation
  type: options
  default: getAll
  required: false
  description: Create a group
  validation: *id023
  typeInfo: *id024
common_expressions:
- ={{ !!$response.body?.["@odata.nextLink"] }}
- ={{ $response.body?.["@odata.nextLink"] ?? $request.url }}
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints:
  - ={{ $response.body?.[
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: group
    text: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  - field: user
    text: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  - field: displayName
    text: e.g. Nathan Smith
  - field: userPrincipalName
    text: e.g. NathanSmith@contoso.com
  - field: mailNickname
    text: e.g. NathanSmith
  - field: additionalFields
    text: e.g. US
  - field: user
    text: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  - field: user
    text: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  - field: filter
    text: e.g. startswith(displayName, 'a')
  - field: group
    text: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  - field: user
    text: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  - field: user
    text: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  - field: updateFields
    text: e.g. US
  - field: mailNickname
    text: e.g. alias
  - field: additionalFields
    text: e.g. user.department -eq "Marketing"
  - field: group
    text: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  - field: group
    text: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  - field: options
    text: Add Option
  - field: filter
    text: e.g. startswith(displayName, 'a')
  - field: group
    text: e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315
  - field: updateFields
    text: e.g. alias
  hints:
  - field: filter
    text: If empty, all the groups will be returned
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
  "$id": "https://n8n.io/schemas/nodes/microsoftEntra.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft Entra ID Node",
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
            "group",
            "user"
          ],
          "default": "user"
        },
        "operation": {
          "description": "Create a group",
          "type": "string",
          "default": "getAll"
        },
        "group": {
          "description": "",
          "type": "string",
          "examples": [
            "e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315"
          ]
        },
        "user": {
          "description": "",
          "type": "string",
          "examples": [
            "e.g. 02bd9fd6-8f93-4758-87c3-1fb73740a315"
          ]
        },
        "accountEnabled": {
          "description": "Whether the account is enabled",
          "type": "string",
          "default": true
        },
        "displayName": {
          "description": "The name to display in the address book for the group",
          "type": "string",
          "default": ""
        },
        "userPrincipalName": {
          "description": "The user principal name (UPN)",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. NathanSmith@contoso.com"
          ]
        },
        "mailNickname": {
          "description": "The mail alias for the group. Only enter the local-part without the domain.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. alias"
          ]
        },
        "password": {
          "description": "The password for the user",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Whether Microsoft Entra roles can be assigned to the group",
          "type": "string",
          "default": {},
          "examples": [
            "e.g. user.department -eq \"Marketing\""
          ]
        },
        "output": {
          "description": "",
          "type": "string",
          "default": "simple"
        },
        "fields": {
          "description": "The fields to add to the output",
          "type": "string",
          "default": []
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "string",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "string",
          "default": 50
        },
        "filter": {
          "description": "<a href=\"https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter\">Query parameter</a> to filter results by",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. startswith(displayName, 'a')"
          ]
        },
        "updateFields": {
          "description": "Whether people external to the organization can send messages to the group. Wait a few seconds before editing this field in a newly created group.",
          "type": "boolean",
          "default": {},
          "examples": [
            "e.g. alias"
          ]
        },
        "groupType": {
          "description": "",
          "type": "string",
          "enum": [
            "Unified",
            "Security"
          ],
          "default": ""
        },
        "mailEnabled": {
          "description": "Whether the group is mail-enabled",
          "type": "string",
          "default": false
        },
        "membershipType": {
          "description": "Lets you add specific users as members of a group and have unique permissions",
          "type": "string",
          "enum": [
            "Assigned",
            "DynamicMembership"
          ],
          "default": ""
        },
        "securityEnabled": {
          "description": "Whether the group is a security group",
          "type": "string",
          "default": true
        },
        "options": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Option"
          ]
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
      "name": "microsoftEntraOAuth2Api",
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
