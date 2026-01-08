---
title: "Node: Copper"
slug: "node-copper"
version: "1"
updated: "2026-01-08"
summary: "Consume the Copper API"
node_type: "regular"
group: "['transform']"
---

# Node: Copper

**Purpose.** Consume the Copper API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:copper.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **copperApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `copperApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many users |

### Company Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a company |
| Delete | `delete` | Delete a company |
| Get | `get` | Get a company |
| Get Many | `getAll` | Get many companies |
| Update | `update` | Update a company |

### Customersource Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many customer sources |

### Lead Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a lead |
| Delete | `delete` | Delete a lead |
| Get | `get` | Get a lead |
| Get Many | `getAll` | Get many leads |
| Update | `update` | Update a lead |

### Opportunity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an opportunity |
| Delete | `delete` | Delete an opportunity |
| Get | `get` | Get an opportunity |
| Get Many | `getAll` | Get many opportunities |
| Update | `update` | Update an opportunity |

### Person Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a person |
| Delete | `delete` | Delete a person |
| Get | `get` | Get a person |
| Get Many | `getAll` | Get many people |
| Update | `update` | Update a person |

### Project Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a project |
| Delete | `delete` | Delete a project |
| Get | `get` | Get a project |
| Get Many | `getAll` | Get many projects |
| Update | `update` | Update a project |

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a task |
| Delete | `delete` | Delete a task |
| Get | `get` | Get a task |
| Get Many | `getAll` | Get many tasks |
| Update | `update` | Update a task |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | company | ✗ | Resource to operate on |  |

**Resource options:**

* **Company** (`company`)
* **Customer Source** (`customerSource`)
* **Lead** (`lead`)
* **Opportunity** (`opportunity`)
* **Person** (`person`)
* **Project** (`project`)
* **Task** (`task`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Operation to perform |  |

**Operation options:**

* **Get Many** (`getAll`) - Get many users

---

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filterFields` | collection | {} | ✗ | Country of the company to filter by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Country | `country` | options |  | Country of the company to filter by |
| Name | `name` | string |  | Name of the company to filter by |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filterFields` | collection | {} | ✗ | Name of the country to filter by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Country | `country` | string |  | Name of the country to filter by |
| Name | `name` | string |  | Name of the lead to filter by |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filterFields` | collection | {} | ✗ | Comma-separated IDs of the primary companies to filter by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company IDs | `company_ids` | string |  | Comma-separated IDs of the primary companies to filter by |
| Customer Source IDs | `customer_source_ids` | string |  | Comma-separated IDs of the customer sources to filter by |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filterFields` | collection | {} | ✗ | Name of the person to filter by | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | Name of the person to filter by |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filterFields` | collection | {} | ✗ | Name of the project to filter by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | Name of the project to filter by |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filterFields` | collection | {} | ✗ | Comma-separated IDs of assignee IDs to filter by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee IDs | `assignee_ids` | string |  | Comma-separated IDs of assignee IDs to filter by |
| Project IDs | `project_ids` | string |  | Comma-separated IDs of project IDs to filter by |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Name of the company to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Description of the company to create | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Details | `details` | string |  | Description of the company to create |
| Email Domain | `email_domain` | string |  |  |

</details>

| Name | `name` | string |  | ✓ | Name of the lead to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Name | `name` | string |  | ✓ | Name of the opportunity to create |  |
| Customer Source ID | `customerSourceId` | string |  | ✗ | ID of the customer source that generated this opportunity |  |
| Primary Contact ID | `primaryContactId` | string |  | ✗ | ID of the primary company associated with this opportunity |  |
| Name | `name` | string |  | ✓ | Name of the person to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Description to set for the person | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Details | `details` | string |  | Description to set for the person |
| Email Domain | `email_domain` | string |  |  |

</details>

| Name | `name` | string |  | ✓ | Name of the project to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the user who will own the project to create | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee ID | `assignee_id` | string |  | ID of the user who will own the project to create |
| Details | `details` | string |  | Description of the project to create |
| Status | `status` | options | Open |  |

</details>

| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the user who will own the task to create | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee ID | `assignee_id` | string |  | ID of the user who will own the task to create |
| Details | `details` | string |  | Description of the task to create |
| Priority | `priority` | options | High |  |
| Status | `status` | options | Open |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company ID | `companyId` | string |  | ✓ | ID of the company to delete |  |
| Lead ID | `leadId` | string |  | ✓ | ID of the lead to delete |  |
| Opportunity ID | `opportunityId` | string |  | ✓ | ID of the opportunity to delete |  |
| Person ID | `personId` | string |  | ✓ | ID of the person to delete |  |
| Project ID | `projectId` | string |  | ✓ | ID of the project to delete |  |
| Task ID | `taskId` | string |  | ✓ | ID of the task to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company ID | `companyId` | string |  | ✓ | ID of the company to retrieve |  |
| Lead ID | `leadId` | string |  | ✓ | ID of the lead to retrieve |  |
| Opportunity ID | `opportunityId` | string |  | ✓ | ID of the opportunity to retrieve |  |
| Person ID | `personId` | string |  | ✓ | ID of the person to retrieve |  |
| Project ID | `projectId` | string |  | ✓ | ID of the project to retrieve |  |
| Task ID | `taskId` | string |  | ✓ | ID of the task to retrieve |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company ID | `companyId` | string |  | ✓ | ID of the company to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Description to set for the company | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Details | `details` | string |  | Description to set for the company |
| Name | `name` | string |  | Name to set for the company |

</details>

| Lead ID | `leadId` | string |  | ✓ | ID of the lead to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Description to set for the lead | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Details | `details` | string |  | Description to set for the lead |
| Name | `name` | string |  | Name to set for the lead |

</details>

| Opportunity ID | `opportunityId` | string |  | ✓ | ID of the opportunity to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the primary company associated with this opportunity | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Customer Source ID | `customer_source_id` | string |  | ID of the primary company associated with this opportunity |
| Name | `name` | string |  | Name to set for the opportunity |
| Primary Contact ID | `primary_contact_id` | string |  | ID of the customer source that generated this opportunity |

</details>

| Person ID | `personId` | string |  | ✓ | ID of the person to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Description to set for the person | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Details | `details` | string |  | Description to set for the person |
| Email Domain | `email_domain` | string |  |  |
| Name | `name` | string |  | Name to set for the person |

</details>

| Project ID | `projectId` | string |  | ✓ | ID of the project to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the user who will own the project | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee ID | `assignee_id` | string |  | ID of the user who will own the project |
| Details | `details` | string |  | Description to set for the project |
| Name | `name` | string |  | Name to set for the project |
| Status | `status` | options | Open |  |

</details>

| Task ID | `taskId` | string |  | ✓ | ID of the task to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the user who will own the task | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee ID | `assignee_id` | string |  | ID of the user who will own the task |
| Details | `details` | string |  | Description to set for the task |
| Name | `name` | string |  | Name to set for the task |
| Priority | `priority` | options | High |  |
| Status | `status` | options | Open |  |

</details>


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
node: copper
displayName: Copper
description: Consume the Copper API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: copperApi
  required: true
operations:
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
    validation: &id001
      displayOptions:
        show:
          resource:
          - task
          operation:
          - getAll
    typeInfo: &id002
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation: &id003
      displayOptions:
        show:
          resource:
          - task
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
        maxValue: 1000
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
    default: 5
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
    default: 5
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
    default: 5
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
    default: 5
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
    default: 5
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
    default: 5
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
    default: 5
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
- id: create
  name: Create
  description: ''
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the company to create
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - create
    typeInfo: &id006
      type: string
      displayName: Name
      name: name
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the lead to create
    validation: *id005
    typeInfo: *id006
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the opportunity to create
    validation: *id005
    typeInfo: *id006
  - id: customerSourceId
    name: Customer Source ID
    type: string
    default: ''
    required: false
    description: ID of the customer source that generated this opportunity
    validation:
      displayOptions:
        show:
          resource:
          - opportunity
          operation:
          - create
    typeInfo:
      type: string
      displayName: Customer Source ID
      name: customerSourceId
  - id: primaryContactId
    name: Primary Contact ID
    type: string
    default: ''
    required: false
    description: ID of the primary company associated with this opportunity
    validation:
      displayOptions:
        show:
          resource:
          - opportunity
          operation:
          - create
    typeInfo:
      type: string
      displayName: Primary Contact ID
      name: primaryContactId
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the person to create
    validation: *id005
    typeInfo: *id006
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the project to create
    validation: *id005
    typeInfo: *id006
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
- id: delete
  name: Delete
  description: ''
  params:
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: true
    description: ID of the company to delete
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - company
          operation:
          - update
    typeInfo: &id008
      type: string
      displayName: Company ID
      name: companyId
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of the lead to delete
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Lead ID
      name: leadId
  - id: opportunityId
    name: Opportunity ID
    type: string
    default: ''
    required: true
    description: ID of the opportunity to delete
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - opportunity
          operation:
          - update
    typeInfo: &id012
      type: string
      displayName: Opportunity ID
      name: opportunityId
  - id: personId
    name: Person ID
    type: string
    default: ''
    required: true
    description: ID of the person to delete
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - person
          operation:
          - update
    typeInfo: &id014
      type: string
      displayName: Person ID
      name: personId
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: ID of the project to delete
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - project
          operation:
          - update
    typeInfo: &id016
      type: string
      displayName: Project ID
      name: projectId
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task to delete
    validation: &id017
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - update
    typeInfo: &id018
      type: string
      displayName: Task ID
      name: taskId
- id: get
  name: Get
  description: ''
  params:
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: true
    description: ID of the company to retrieve
    validation: *id007
    typeInfo: *id008
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of the lead to retrieve
    validation: *id009
    typeInfo: *id010
  - id: opportunityId
    name: Opportunity ID
    type: string
    default: ''
    required: true
    description: ID of the opportunity to retrieve
    validation: *id011
    typeInfo: *id012
  - id: personId
    name: Person ID
    type: string
    default: ''
    required: true
    description: ID of the person to retrieve
    validation: *id013
    typeInfo: *id014
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: ID of the project to retrieve
    validation: *id015
    typeInfo: *id016
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task to retrieve
    validation: *id017
    typeInfo: *id018
- id: update
  name: Update
  description: ''
  params:
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: true
    description: ID of the company to update
    validation: *id007
    typeInfo: *id008
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of the lead to update
    validation: *id009
    typeInfo: *id010
  - id: opportunityId
    name: Opportunity ID
    type: string
    default: ''
    required: true
    description: ID of the opportunity to update
    validation: *id011
    typeInfo: *id012
  - id: personId
    name: Person ID
    type: string
    default: ''
    required: true
    description: ID of the person to update
    validation: *id013
    typeInfo: *id014
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: ID of the project to update
    validation: *id015
    typeInfo: *id016
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task to update
    validation: *id017
    typeInfo: *id018
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
  - field: filterFields
    text: Add Filter
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filterFields
    text: Add Filter
  - field: updateFields
    text: Add Field
  - field: filterFields
    text: Add Filter
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filterFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filterFields
    text: Add Filter
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filterFields
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
  "$id": "https://n8n.io/schemas/nodes/copper.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Copper Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "getAll",
        "create",
        "delete",
        "get",
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
            "company",
            "customerSource",
            "lead",
            "opportunity",
            "person",
            "project",
            "task",
            "user"
          ],
          "default": "company"
        },
        "operation": {
          "description": "",
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
        "name": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "ID of the user who will own the task to create",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "companyId": {
          "description": "ID of the company to update",
          "type": "string",
          "default": ""
        },
        "filterFields": {
          "description": "Comma-separated IDs of assignee IDs to filter by",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "updateFields": {
          "description": "ID of the user who will own the task",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "leadId": {
          "description": "ID of the lead to update",
          "type": "string",
          "default": ""
        },
        "customerSourceId": {
          "description": "ID of the customer source that generated this opportunity",
          "type": "string",
          "default": ""
        },
        "primaryContactId": {
          "description": "ID of the primary company associated with this opportunity",
          "type": "string",
          "default": ""
        },
        "opportunityId": {
          "description": "ID of the opportunity to update",
          "type": "string",
          "default": ""
        },
        "personId": {
          "description": "ID of the person to update",
          "type": "string",
          "default": ""
        },
        "projectId": {
          "description": "ID of the project to update",
          "type": "string",
          "default": ""
        },
        "taskId": {
          "description": "ID of the task to update",
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
      "name": "copperApi",
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
