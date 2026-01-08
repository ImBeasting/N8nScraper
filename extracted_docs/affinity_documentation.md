---
title: "Node: Affinity"
slug: "node-affinity"
version: "1"
updated: "2026-01-08"
summary: "Consume Affinity API"
node_type: "regular"
group: "['output']"
---

# Node: Affinity

**Purpose.** Consume Affinity API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:affinity.svg', 'dark': 'file:affinity.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **affinityApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `affinityApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### List Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a list |
| Get Many | `getAll` | Get many lists |

### Listentry Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a list entry |
| Delete | `delete` | Delete a list entry |
| Get | `get` | Get a list entry |
| Get Many | `getAll` | Get many list entries |

### Organization Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an organization |
| Delete | `delete` | Delete an organization |
| Get | `get` | Get an organization |
| Get Many | `getAll` | Get many organizations |
| Update | `update` | Update an organization |

### Person Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a person |
| Delete | `delete` | Delete a person |
| Get | `get` | Get a person |
| Get Many | `getAll` | Get many persons |
| Update | `update` | Update a person |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | organization | ✗ | Resource to operate on |  |

**Resource options:**

* **List** (`list`)
* **List Entry** (`listEntry`)
* **Organization** (`organization`)
* **Person** (`person`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Get a list |  |

**Operation options:**

* **Get** (`get`) - Get a list
* **Get Many** (`getAll`) - Get many lists

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List ID | `listId` | string |  | ✓ | The unique ID of the list object to be retrieved |  |
| List Name or ID | `listId` | options |  | ✓ | The unique ID of the list that contains the specified list_entry_id. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Entry ID | `listEntryId` | string |  | ✓ | The unique ID of the list entry object to be retrieved |  |
| Organization ID | `organizationId` | string |  | ✓ | Unique identifier for the organization |  |
| Options | `options` | collection | {} | ✗ | Whether interaction dates will be present on the returned resources | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| With Interaction Dates | `withInteractionDates` | boolean | False | Whether interaction dates will be present on the returned resources |

</details>

| Person ID | `personId` | string |  | ✓ | Unique identifier for the person |  |
| Options | `options` | collection | {} | ✗ | Whether interaction dates will be present on the returned resources | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| With Interaction Dates | `withInteractionDates` | boolean | False | Whether interaction dates will be present on the returned resources |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| List Name or ID | `listId` | options |  | ✗ | The unique ID of the list whose list entries are to be retrieved. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Options | `options` | collection | {} | ✗ | A string used to search all the organizations in your team’s address book. This could be an email address, a first name or a last name. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Term | `term` | string |  | A string used to search all the organizations in your team’s address book. This could be an email address, a first name or a last name. |
| With Interaction Dates | `withInteractionDates` | boolean | False | Whether interaction dates will be present on the returned resources |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Options | `options` | collection | {} | ✗ | A string used to search all the persons in your team’s address book. This could be an email address, a first name or a last name. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Term | `term` | string |  | A string used to search all the persons in your team’s address book. This could be an email address, a first name or a last name. |
| With Interaction Dates | `withInteractionDates` | boolean | False | Whether interaction dates will be present on the returned resources |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `listId` | options |  | ✓ | The unique ID of the list whose list entries are to be retrieved. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Entity ID | `entityId` | string |  | ✓ | The unique ID of the entity (person, organization, or opportunity) to add to this list |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The ID of a Person resource who should be recorded as adding the entry to the list. Must be a person who can access Affinity. If not provided the creator defaults to the owner of the API key. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Creator ID | `creator_id` | string |  | The ID of a Person resource who should be recorded as adding the entry to the list. Must be a person who can access Affinity. If not provided the creator defaults to the owner of the API key. |

</details>

| Name | `name` | string |  | ✓ | The name of the organization |  |
| Domain | `domain` | string |  | ✓ | The domain name of the organization |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Persons that the new organization will be associated with. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Person Names or IDs | `persons` | multiOptions | [] | Persons that the new organization will be associated with. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| First Name | `firstName` | string |  | ✓ | The first name of the person |  |
| Last Name | `lastName` | string |  | ✓ | The last name of the person |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Organizations that the person is associated with. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Organization Names or IDs | `organizations` | multiOptions | [] | Organizations that the person is associated with. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Emails | `emails` | string | [] | ✗ | The email addresses of the person | e.g. info@example.com | email |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `listId` | options |  | ✓ | The unique ID of the list that contains the specified list_entry_id. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| List Entry ID | `listEntryId` | string |  | ✓ | The unique ID of the list entry object to be deleted |  |
| Organization ID | `organizationId` | string |  | ✓ | Unique identifier for the organization |  |
| Person ID | `personId` | string |  | ✓ | Unique identifier for the person |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Organization ID | `organizationId` | string |  | ✓ | Unique identifier for the organization |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The domain name of the organization | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Domain | `domain` | string |  | The domain name of the organization |
| Name | `name` | string |  | The name of the organization |
| Person Names or IDs | `persons` | multiOptions | [] | Persons that the new organization will be associated with. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Person ID | `personId` | string |  | ✓ | Unique identifier for the person |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The first name of the person | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| First Name | `firstName` | string |  | The first name of the person |
| Last Name | `lastName` | string |  | The last name of the person |
| Organization Names or IDs | `organizations` | multiOptions | [] | Organizations that the person is associated with. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Emails | `emails` | string | [] | ✗ | The email addresses of the person | e.g. info@example.com | email |

---

## Load Options Methods

- `getOrganizations`

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
* Categories: Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: affinity
displayName: Affinity
description: Consume Affinity API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: affinityApi
  required: true
operations:
- id: get
  name: Get
  description: Get a list
  params:
  - id: listId
    name: List ID
    type: string
    default: ''
    required: true
    description: The unique ID of the list object to be retrieved
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - listEntry
          operation:
          - delete
    typeInfo: &id002
      type: options
      displayName: List Name or ID
      name: listId
      typeOptions:
        loadOptionsMethod: getLists
      possibleValues: []
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The unique ID of the list that contains the specified list_entry_id.
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: listEntryId
    name: List Entry ID
    type: string
    default: ''
    required: true
    description: The unique ID of the list entry object to be retrieved
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - listEntry
          operation:
          - delete
    typeInfo: &id008
      type: string
      displayName: List Entry ID
      name: listEntryId
  - id: organizationId
    name: Organization ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the organization
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - organization
          operation:
          - delete
    typeInfo: &id010
      type: string
      displayName: Organization ID
      name: organizationId
  - id: personId
    name: Person ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the person
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - person
          operation:
          - delete
    typeInfo: &id012
      type: string
      displayName: Person ID
      name: personId
- id: getAll
  name: Get Many
  description: Get many lists
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
          - person
          operation:
          - getAll
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          resource:
          - person
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
        maxValue: 10
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: false
    description: The unique ID of the list whose list entries are to be retrieved.
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
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
    default: 5
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
    default: 5
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
    default: 5
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: create
  name: Create
  description: Create a list entry
  params:
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The unique ID of the list whose list entries are to be retrieved.
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: entityId
    name: Entity ID
    type: string
    default: ''
    required: true
    description: The unique ID of the entity (person, organization, or opportunity)
      to add to this list
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - listEntry
          operation:
          - create
    typeInfo:
      type: string
      displayName: Entity ID
      name: entityId
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the organization
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - organization
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: domain
    name: Domain
    type: string
    default: ''
    required: true
    description: The domain name of the organization
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - organization
          operation:
          - create
    typeInfo:
      type: string
      displayName: Domain
      name: domain
  - id: firstName
    name: First Name
    type: string
    default: ''
    required: true
    description: The first name of the person
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - person
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
    description: The last name of the person
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - person
          operation:
          - create
    typeInfo:
      type: string
      displayName: Last Name
      name: lastName
  - id: emails
    name: Emails
    type: string
    default: []
    required: false
    description: The email addresses of the person
    placeholder: info@example.com
    validation: &id013
      format: email
      displayOptions:
        show:
          resource:
          - person
          operation:
          - update
    typeInfo: &id014
      type: string
      displayName: Emails
      name: emails
      typeOptions:
        multipleValues: true
- id: delete
  name: Delete
  description: Delete a list entry
  params:
  - id: listId
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: The unique ID of the list that contains the specified list_entry_id.
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: listEntryId
    name: List Entry ID
    type: string
    default: ''
    required: true
    description: The unique ID of the list entry object to be deleted
    validation: *id007
    typeInfo: *id008
  - id: organizationId
    name: Organization ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the organization
    validation: *id009
    typeInfo: *id010
  - id: personId
    name: Person ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the person
    validation: *id011
    typeInfo: *id012
- id: update
  name: Update
  description: Update an organization
  params:
  - id: organizationId
    name: Organization ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the organization
    validation: *id009
    typeInfo: *id010
  - id: personId
    name: Person ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the person
    validation: *id011
    typeInfo: *id012
  - id: emails
    name: Emails
    type: string
    default: []
    required: false
    description: The email addresses of the person
    placeholder: info@example.com
    validation: *id013
    typeInfo: *id014
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
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: emails
    text: info@example.com
  - field: updateFields
    text: Add Field
  - field: emails
    text: info@example.com
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/affinity.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Affinity Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll",
        "create",
        "delete",
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
            "list",
            "listEntry",
            "organization",
            "person"
          ],
          "default": "organization"
        },
        "operation": {
          "description": "Create a person",
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
        "listId": {
          "description": "The unique ID of the list that contains the specified list_entry_id. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
          "default": 5
        },
        "entityId": {
          "description": "The unique ID of the entity (person, organization, or opportunity) to add to this list",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Organizations that the person is associated with. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "listEntryId": {
          "description": "The unique ID of the list entry object to be deleted",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "The name of the organization",
          "type": "string",
          "default": ""
        },
        "domain": {
          "description": "The domain name of the organization",
          "type": "string",
          "default": ""
        },
        "organizationId": {
          "description": "Unique identifier for the organization",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "The first name of the person",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "options": {
          "description": "A string used to search all the persons in your team\u2019s address book. This could be an email address, a first name or a last name.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "firstName": {
          "description": "The first name of the person",
          "type": "string",
          "default": ""
        },
        "lastName": {
          "description": "The last name of the person",
          "type": "string",
          "default": ""
        },
        "emails": {
          "description": "The email addresses of the person",
          "type": "string",
          "default": [],
          "format": "email",
          "examples": [
            "info@example.com"
          ]
        },
        "personId": {
          "description": "Unique identifier for the person",
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
      "name": "affinityApi",
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
