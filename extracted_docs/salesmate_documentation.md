---
title: "Node: Salesmate"
slug: "node-salesmate"
version: "1"
updated: "2025-11-13"
summary: "Consume Salesmate API"
node_type: "regular"
group: "['output']"
---

# Node: Salesmate

**Purpose.** Consume Salesmate API
**Subtitle.** ={{$parameter["operation"] + ":" + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:salesmate.png`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **salesmateApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `salesmateApi` | ✓ | - |

---

## API Patterns

**Headers Used:** x-linkname, Content-Type

---

## Operations

### Company Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a company |
| Delete | `delete` | Delete a company |
| Get | `get` | Get a company |
| Get Many | `getAll` | Get many companies |
| Update | `update` | Update a company |

### Activity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an activity |
| Delete | `delete` | Delete an activity |
| Get | `get` | Get an activity |
| Get Many | `getAll` | Get many companies |
| Update | `update` | Update an activity |

### Deal Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a deal |
| Delete | `delete` | Delete a deal |
| Get | `get` | Get a deal |
| Get Many | `getAll` | Get many deals |
| Update | `update` | Update a deal |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | activity | ✗ | Resource to operate on |  |

**Resource options:**

* **Activity** (`activity`)
* **Company** (`company`)
* **Deal** (`deal`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a company |  |

**Operation options:**

* **Create** (`create`) - Create a company
* **Delete** (`delete`) - Delete a company
* **Get** (`get`) - Get a company
* **Get Many** (`getAll`) - Get many companies
* **Update** (`update`) - Update a company

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ |  |  |
| Owner Name or ID | `owner` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| RAW Data | `rawData` | boolean | False | ✗ | Whether the data should include the fields details |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Website | `website` | string |  |  |
| Phone | `phone` | string |  |  |
| Other Phone | `otherPhone` | string |  |  |
| Facebook Handle | `facebookHandle` | string |  |  |
| Google Plus Handle | `googlePlusHandle` | string |  |  |
| LinkedIn Handle | `linkedInHandle` | string |  |  |
| Skype ID | `skypeId` | string |  |  |
| Twitter Handle | `twitterHandle` | string |  |  |
| Currency | `currency` | string |  |  |
| Billing Address Line 1 | `billingAddressLine1` | string |  |  |
| Billing Address Line 2 | `billingAddressLine2` | string |  |  |
| Billing City | `billingCity` | string |  |  |
| Billing Zip Code | `billingZipCode` | string |  |  |
| Billing State | `billingState` | string |  |  |
| Billing Country | `billingState` | string |  |  |
| Description | `description` | string |  |  |
| Tags | `tags` | string |  |  |

</details>

| Title | `title` | string |  | ✓ |  |  |
| Owner Name or ID | `owner` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Type | `type` | string |  | ✓ | This field displays activity type such as call, meeting etc |  |
| RAW Data | `rawData` | boolean | False | ✗ | Whether the data should include the fields details |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | This field contains details related to the activity | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | This field contains details related to the activity |
| Tags | `tags` | string |  | This field contains tags associated with an activity |
| Due Date | `dueDate` | dateTime |  | Expiry date of an activity |
| Duration | `duration` | number |  | Time duration of an activity |
| Is Calendar Invite | `isCalendarInvite` | boolean | False | Whether to send calendar invite |
| Is Completed | `isCompleted` | boolean | False | Whether the activity is completed or not |

</details>

| Title | `title` | string |  | ✓ |  |  |
| Owner Name or ID | `owner` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Primary Contact Name or ID | `primaryContact` | options |  | ✓ | Primary contact for the deal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Pipeline | `pipeline` | options |  | ✓ |  |  |

**Pipeline options:**

* **Sales** (`Sales`)

| Status | `status` | options | Open | ✓ |  |  |

**Status options:**

* **Open** (`Open`)
* **Close** (`Close`)
* **Lost** (`Lost`)

| Stage | `stage` | options |  | ✓ |  |  |

**Stage options:**

* **New (Untouched)** (`New (Untouched)`)
* **Contacted** (`Contacted`)
* **Qualified** (`Qualified`)
* **In Negotiation** (`In Negotiation`)
* **Proposal Presented** (`Proposal Presented`)

| Currency | `currency` | string |  | ✓ |  |  |
| RAW Data | `rawData` | boolean | False | ✗ | Whether the data should include the fields details |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | This field contains details related to the deal | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | This field contains details related to the deal |
| Tags | `tags` | string |  | This field contains tags associated with an deal |
| Primary Company Name or ID | `primaryCompany` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Source | `source` | options | Ads |  |
| Estimated Close Date | `estimatedCloseDate` | dateTime |  |  |
| Deal Value | `dealValue` | number | 0 |  |
| Priority | `priority` | options | Medium |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company ID | `id` | string |  | ✓ | If more than one company add them separated by , |  |
| Activity ID | `id` | string |  | ✓ | If more than one activity add them separated by , |  |
| Deal ID | `id` | string |  | ✓ | If more than one deal add them separated by , |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company ID | `id` | string |  | ✓ |  |  |
| RAW Data | `rawData` | boolean | False | ✗ | Whether the data should include the fields details |  |
| Activity ID | `id` | string |  | ✓ |  |  |
| RAW Data | `rawData` | boolean | False | ✗ | Whether the data should include the fields details |  |
| Deal ID | `id` | string |  | ✓ |  |  |
| RAW Data | `rawData` | boolean | False | ✗ | Whether the data should include the fields details |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:25 |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | Comma-separated list of fields to return | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Comma-separated list of fields to return |
| Sort By | `sortBy` | string |  | The field to sort by |
| Sort Order | `sortOrder` | options | desc |  |

</details>

| Filters | `filtersJson` | json |  | ✗ |  |  |
| Filters | `filters` | fixedCollection | {} | ✗ | Value of the property to set | e.g. Add filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filters | `filtersUi` |  |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:25 |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | Comma-separated list of fields to return | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Comma-separated list of fields to return |
| Sort By | `sortBy` | string |  | The field to sort by |
| Sort Order | `sortOrder` | options | desc |  |

</details>

| Filters | `filtersJson` | json |  | ✗ |  |  |
| Filters | `filters` | fixedCollection | {} | ✗ | Value of the property to set | e.g. Add filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filters | `filtersUi` |  |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:25 |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | Comma-separated list of fields to return | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Comma-separated list of fields to return |
| Sort By | `sortBy` | string |  | The field to sort by |
| Sort Order | `sortOrder` | options | desc |  |

</details>

| Filters | `filtersJson` | json |  | ✗ |  |  |
| Filters | `filters` | fixedCollection | {} | ✗ | Value of the property to set | e.g. Add filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filters | `filtersUi` |  |  |  |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company ID | `id` | string |  | ✓ |  |  |
| RAW Data | `rawData` | boolean | False | ✗ | Whether the data should include the fields details |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  |  |
| Owner Name or ID | `owner` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Website | `website` | string |  |  |
| Phone | `phone` | string |  |  |
| Other Phone | `otherPhone` | string |  |  |
| Facebook Handle | `facebookHandle` | string |  |  |
| Google Plus Handle | `googlePlusHandle` | string |  |  |
| LinkedIn Handle | `linkedInHandle` | string |  |  |
| Skype ID | `skypeId` | string |  |  |
| Twitter Handle | `twitterHandle` | string |  |  |
| Currency | `currency` | string |  |  |
| Billing Address Line 1 | `billingAddressLine1` | string |  |  |
| Billing Address Line 2 | `billingAddressLine2` | string |  |  |
| Billing City | `billingCity` | string |  |  |
| Billing Zip Code | `billingZipCode` | string |  |  |
| Billing State | `billingState` | string |  |  |
| Billing Country | `billingState` | string |  |  |
| Description | `description` | string |  |  |
| Tags | `tags` | string |  |  |

</details>

| Activity ID | `id` | string |  | ✓ |  |  |
| RAW Data | `rawData` | boolean | False | ✗ | Whether the data should include the fields details |  |
| Update Fields | `updateFields` | collection | {} | ✗ | This field contains details related to the activity | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Title | `title` | string |  |  |
| Type | `type` | string |  |  |
| Owner | `owner` | string |  |  |
| Description | `description` | string |  | This field contains details related to the activity |
| Tags | `tags` | string |  | This field contains tags associated with an activity |
| Due Date | `dueDate` | dateTime |  | Expiry date of an activity |
| Duration | `duration` | number |  | Time duration of an activity |
| Is Calendar Invite | `isCalendarInvite` | boolean | False | Whether to send calendar invite |
| Is Completed | `isCompleted` | boolean | False | Whether the activity is completed or not |

</details>

| Deal ID | `id` | string |  | ✓ |  |  |
| RAW Data | `rawData` | boolean | False | ✗ | Whether the data should include the fields details |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Title | `title` | string |  |  |
| Owner Name or ID | `owner` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Primary Contact Name or ID | `primaryContact` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Pipeline | `pipeline` | options |  |  |
| Status | `status` | options | Open |  |
| Stage | `stage` | options |  |  |
| Currency | `currency` | string |  |  |
| Description | `description` | string |  | This field contains details related to the deal |
| Tags | `tags` | string |  | This field contains tags associated with an deal |
| Primary Company Name or ID | `primaryCompany` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Source | `source` | options | Ads |  |
| Estimated Close Date | `estimatedCloseDate` | dateTime |  |  |
| Deal Value | `dealValue` | number | 0 |  |
| Priority | `priority` | options | Medium |  |

</details>


---

## Load Options Methods

- `getUsers`
- `for`
- `name`
- `value`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ":" + $parameter["resource"]}}`

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
node: salesmate
displayName: Salesmate
description: Consume Salesmate API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: salesmateApi
  required: true
operations:
- id: create
  name: Create
  description: Create a company
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - company
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: owner
    name: Owner Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
    typeInfo: &id002
      type: options
      displayName: Owner Name or ID
      name: owner
      typeOptions:
        loadOptionsMethod: getUsers
      possibleValues: []
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether the data should include the fields details
    validation: &id003
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - get
    typeInfo: &id004
      type: boolean
      displayName: RAW Data
      name: rawData
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: ''
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
    typeInfo: &id006
      type: string
      displayName: Title
      name: title
  - id: owner
    name: Owner Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: type
    name: Type
    type: string
    default: ''
    required: true
    description: This field displays activity type such as call, meeting etc
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - activity
          operation:
          - create
    typeInfo:
      type: string
      displayName: Type
      name: type
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether the data should include the fields details
    validation: *id003
    typeInfo: *id004
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: owner
    name: Owner Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: primaryContact
    name: Primary Contact Name or ID
    type: options
    default: ''
    required: true
    description: Primary contact for the deal. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
    typeInfo:
      type: options
      displayName: Primary Contact Name or ID
      name: primaryContact
      typeOptions:
        loadOptionsMethod: getContacts
      possibleValues: []
  - id: pipeline
    name: Pipeline
    type: options
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
    typeInfo:
      type: options
      displayName: Pipeline
      name: pipeline
      possibleValues:
      - value: Sales
        name: Sales
        description: ''
  - id: status
    name: Status
    type: options
    default: Open
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
    typeInfo:
      type: options
      displayName: Status
      name: status
      possibleValues:
      - value: Open
        name: Open
        description: ''
      - value: Close
        name: Close
        description: ''
      - value: Lost
        name: Lost
        description: ''
  - id: stage
    name: Stage
    type: options
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
    typeInfo:
      type: options
      displayName: Stage
      name: stage
      possibleValues:
      - value: New (Untouched)
        name: New (Untouched)
        description: ''
      - value: Contacted
        name: Contacted
        description: ''
      - value: Qualified
        name: Qualified
        description: ''
      - value: In Negotiation
        name: In Negotiation
        description: ''
      - value: Proposal Presented
        name: Proposal Presented
        description: ''
  - id: currency
    name: Currency
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
    typeInfo:
      type: string
      displayName: Currency
      name: currency
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether the data should include the fields details
    validation: *id003
    typeInfo: *id004
- id: delete
  name: Delete
  description: Delete a company
  params:
  - id: id
    name: Company ID
    type: string
    default: ''
    required: true
    description: If more than one company add them separated by ,
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - delete
    typeInfo: &id008
      type: string
      displayName: Deal ID
      name: id
  - id: id
    name: Activity ID
    type: string
    default: ''
    required: true
    description: If more than one activity add them separated by ,
    validation: *id007
    typeInfo: *id008
  - id: id
    name: Deal ID
    type: string
    default: ''
    required: true
    description: If more than one deal add them separated by ,
    validation: *id007
    typeInfo: *id008
- id: get
  name: Get
  description: Get a company
  params:
  - id: id
    name: Company ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether the data should include the fields details
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Activity ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether the data should include the fields details
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Deal ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether the data should include the fields details
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: Get many companies
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id009
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - getAll
    typeInfo: &id010
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: &id011
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id012
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 25
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id013
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - deal
    typeInfo: &id014
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: filtersJson
    name: Filters
    type: json
    default: ''
    required: false
    description: ''
    validation: &id015
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - deal
          jsonParameters:
          - true
    typeInfo: &id016
      type: json
      displayName: Filters
      name: filtersJson
      typeOptions:
        alwaysOpenEditWindow: true
  - id: filters
    name: Filters
    type: fixedCollection
    default: {}
    required: false
    description: Value of the property to set
    placeholder: Add filter
    validation: &id017
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - getAll
          jsonParameters:
          - false
    typeInfo: &id018
      type: fixedCollection
      displayName: Filters
      name: filters
      typeOptions:
        multipleValues: false
      subProperties:
      - name: filtersUi
        displayName: Filters
        values:
        - displayName: Operator
          name: operator
          type: options
          value: AND
          default: AND
          options:
          - name: AND
            value: AND
            displayName: And
          - name: OR
            value: OR
            displayName: Or
        - displayName: Conditions
          name: conditions
          type: fixedCollection
          description: Value of the property to set
          placeholder: Add Condition
          value: title
          default: {}
          options:
          - name: conditionsUi
            displayName: Conditions
            values:
            - displayName: Field
              name: field
              type: options
              value: title
              default: title
              options:
              - name: Title
                value: title
                displayName: Title
              - name: Tags
                value: tags
                displayName: Tags
              - name: Last Communication Mode
                value: lastCommunicationMode
                displayName: Last Communication Mode
            - displayName: Condition
              name: condition
              type: options
              description: Value of the property to set
              value: EQUALS
              default: EQUALS
              options:
              - name: Equals
                value: EQUALS
                displayName: Equals
              - name: Not Equals
                value: NOT_EQUALS
                displayName: Not Equals
              - name: CONTAINS
                value: Contains
                displayName: Contains
              - name: Does Not Contains
                value: DOES_NOT_CONTAINS
                displayName: Does Not Contains
              - name: Empty
                value: EMPTY
                displayName: Empty
              - name: Not Empty
                value: NOT_EMPTY
                displayName: Not Empty
              - name: Starts With
                value: STARTS_WITH
                displayName: Starts With
              - name: Ends With
                value: ENDS_WITH
                displayName: Ends With
            - displayName: Value
              name: value
              type: string
              default: ''
          typeOptions:
            multipleValues: true
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id009
    typeInfo: *id010
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id013
    typeInfo: *id014
  - id: filtersJson
    name: Filters
    type: json
    default: ''
    required: false
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: filters
    name: Filters
    type: fixedCollection
    default: {}
    required: false
    description: Value of the property to set
    placeholder: Add filter
    validation: *id017
    typeInfo: *id018
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id009
    typeInfo: *id010
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id013
    typeInfo: *id014
  - id: filtersJson
    name: Filters
    type: json
    default: ''
    required: false
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: filters
    name: Filters
    type: fixedCollection
    default: {}
    required: false
    description: Value of the property to set
    placeholder: Add filter
    validation: *id017
    typeInfo: *id018
- id: update
  name: Update
  description: Update a company
  params:
  - id: id
    name: Company ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether the data should include the fields details
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Activity ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether the data should include the fields details
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Deal ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether the data should include the fields details
    validation: *id003
    typeInfo: *id004
common_expressions:
- ={{$parameter["operation"] + ":" + $parameter["resource"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - x-linkname
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: filters
    text: Add filter
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: filters
    text: Add filter
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: filters
    text: Add filter
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
  "$id": "https://n8n.io/schemas/nodes/salesmate.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Salesmate Node",
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
            "activity",
            "company",
            "deal"
          ],
          "default": "activity"
        },
        "operation": {
          "description": "Create a deal",
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
        "name": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "owner": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "rawData": {
          "description": "Whether the data should include the fields details",
          "type": "boolean",
          "default": false
        },
        "additionalFields": {
          "description": "This field contains details related to the deal",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "id": {
          "description": "If more than one deal add them separated by ,",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
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
          "default": 10
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "options": {
          "description": "Comma-separated list of fields to return",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "filtersJson": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "filters": {
          "description": "Value of the property to set",
          "type": "string",
          "default": {},
          "examples": [
            "Add filter"
          ]
        },
        "title": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "type": {
          "description": "This field displays activity type such as call, meeting etc",
          "type": "string",
          "default": ""
        },
        "primaryContact": {
          "description": "Primary contact for the deal. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "pipeline": {
          "description": "",
          "type": "string",
          "enum": [
            "Sales"
          ],
          "default": ""
        },
        "status": {
          "description": "",
          "type": "string",
          "enum": [
            "Open",
            "Close",
            "Lost"
          ],
          "default": "Open"
        },
        "stage": {
          "description": "",
          "type": "string",
          "enum": [
            "New (Untouched)",
            "Contacted",
            "Qualified",
            "In Negotiation",
            "Proposal Presented"
          ],
          "default": ""
        },
        "currency": {
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
      "name": "salesmateApi",
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
