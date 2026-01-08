---
title: "Node: Zendesk"
slug: "node-zendesk"
version: "1"
updated: "2026-01-08"
summary: "Consume Zendesk API"
node_type: "regular"
group: "['output']"
---

# Node: Zendesk

**Purpose.** Consume Zendesk API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:zendesk.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **zendeskApi**: N/A
- **zendeskOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `zendeskApi` | ✓ | {'show': {'authentication': ['apiToken']}} |
| `zendeskOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Ticket Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a ticket |
| Delete | `delete` | Delete a ticket |
| Get | `get` | Get a ticket |
| Get Many | `getAll` | Get many tickets |
| Recover | `recover` | Recover a suspended ticket |
| Update | `update` | Update a ticket |

### Ticketfield Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a ticket field |
| Get Many | `getAll` | Get many system and custom ticket fields |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a user |
| Delete | `delete` | Delete a user |
| Get | `get` | Get a user |
| Get Many | `getAll` | Get many users |
| Get Organizations | `getOrganizations` | Get a user's organizations |
| Get Related Data | `getRelatedData` | Get data related to the user |
| Search | `search` | Search users |
| Update | `update` | Update a user |

### Organization Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Count | `count` | Count organizations |
| Create | `create` | Create an organization |
| Delete | `delete` | Delete an organization |
| Get | `get` | Get an organization |
| Get Many | `getAll` | Get many organizations |
| Get Related Data | `getRelatedData` | Get data related to the organization |
| Update | `update` | Update a organization |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | ticket | ✗ | Tickets are the means through which your end users (customers) communicate with agents in Zendesk Support |  |

**Resource options:**

* **Ticket** (`ticket`) - Tickets are the means through which your end users (customers) communicate with agents in Zendesk Support
* **Ticket Field** (`ticketField`) - Manage system and custom ticket fields
* **User** (`user`) - Manage users
* **Organization** (`organization`) - Manage organizations

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a ticket |  |

**Operation options:**

* **Create** (`create`) - Create a ticket
* **Delete** (`delete`) - Delete a ticket
* **Get** (`get`) - Get a ticket
* **Get Many** (`getAll`) - Get many tickets
* **Recover** (`recover`) - Recover a suspended ticket
* **Update** (`update`) - Update a ticket

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Description | `description` | string |  | ✓ | The first comment on the ticket |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Custom field ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Custom field ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| External ID | `externalId` | string |  | An ID you can use to link Zendesk Support tickets to local records |
| Group Name or ID | `group` | options |  | The group this ticket is assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Recipient | `recipient` | string |  | The original recipient e-mail address of the ticket |
| Status | `status` | options |  | The state of the ticket |
| Subject | `subject` | string |  | The value of the subject field for this ticket |
| Tag Names or IDs | `tags` | multiOptions | [] | The array of tags applied to this ticket. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Type | `type` | options |  | The type of this ticket |

</details>

| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Object of values to set as described <a href="https://developer.zendesk.com/rest_api/docs/support/tickets">here</a> |  |
| Name | `name` | string |  | ✓ | The user's name |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | An alias displayed to end users | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Alias | `alias` | string |  | An alias displayed to end users |
| Custom Role ID | `custom_role_id` | number | 0 | A custom role if the user is an agent on the Enterprise plan |
| Details | `details` | string |  | Any details you want to store about the user, such as an address |
| Email | `email` | string |  | The user's primary email address |
| External ID | `external_id` | string |  | A unique identifier from another system |
| Locale | `locale` | options |  | The user's locale. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Moderator | `moderator` | boolean | False | Whether the user has forum moderation capabilities |
| Notes | `notes` | string |  | Any notes you want to store about the user |
| Only Private Comments | `only_private_comments` | boolean | False | Whether the user can only create private comments |
| Organization Name or ID | `organization_id` | options |  | The ID of the user's organization. If the user has more than one organization memberships, the ID of the user's default organization. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone | `phone` | string |  | The user's primary phone number |
| Report CSV | `report_csv` | boolean | False | Whether or not the user can access the CSV report on the Search tab of the Reporting page in the Support admin interface |
| Restricted Agent | `restricted_agent` | boolean | False | Whether the agent has any restrictions; false for admins and unrestricted agents, true for other agents |
| Role | `role` | options |  | The user's role |
| Signature | `signature` | string |  | The user's signature. Only agents and admins can have signatures. |
| Suspended | `suspended` | boolean | False | Whether the agent is suspended. Tickets from suspended users are also suspended, and these users cannot sign in to the end user portal. |
| Tag Names or IDs | `tags` | multiOptions | [] | The array of tags applied to this user. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Ticket Restriction | `ticket_restriction` | options |  | Specifies which tickets the user has access to |
| Timezone | `time_zone` | string |  | The user's time zone |
| User Fields | `userFieldsUi` | fixedCollection | {} | Values of custom fields in the user's profile |
| Verified | `verified` | boolean | False | Whether the user's primary identity is verified or not |

</details>

| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Details about the organization, such as the address | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Details | `details` | string |  | Details about the organization, such as the address |
| Domain Names | `domain_names` | string |  | Comma-separated domain names associated with this organization |
| Notes | `notes` | string |  |  |
| Organization Fields | `organizationFieldsUi` | fixedCollection | {} | Values of custom fields in the organization's profile |
| Tag Names or IDs | `tags` | multiOptions | [] | IDs of tags applied to this organization. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Ticket Type | `ticketType` | options | regular | ✓ |  |  |

**Ticket Type options:**

* **Regular** (`regular`)
* **Suspended** (`suspended`)

| Ticket ID | `id` | string |  | ✓ |  |  |
| Suspended Ticket ID | `id` | string |  | ✓ | Ticket ID |  |
| User ID | `id` | string |  | ✓ |  |  |
| Organization ID | `id` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Ticket Type | `ticketType` | options | regular | ✓ |  |  |

**Ticket Type options:**

* **Regular** (`regular`)
* **Suspended** (`suspended`)

| Ticket ID | `id` | string |  | ✓ |  |  |
| Suspended Ticket ID | `id` | string |  | ✓ | Ticket ID |  |
| Ticket Field ID | `ticketFieldId` | string |  | ✓ |  |  |
| User ID | `id` | string |  | ✓ |  |  |
| Organization ID | `id` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Ticket Type | `ticketType` | options | regular | ✓ |  |  |

**Ticket Type options:**

* **Regular** (`regular`)
* **Suspended** (`suspended`)

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | The group to search. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Group Name or ID | `group` | options |  | The group to search. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Query | `query` | string |  | <a href="https://developer.zendesk.com/api-reference/ticketing/ticket-management/search/#syntax-examples">Query syntax</a> to search tickets |
| Sort By | `sortBy` | options | updated_at | Defaults to sorting by relevance |
| Sort Order | `sortOrder` | options | asc |  |
| Status | `status` | options |  | The state of the ticket |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Roles | `role` | multiOptions | [] |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |

### Recover parameters (`recover`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Suspended Ticket ID | `id` | string |  | ✓ |  |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Ticket ID | `id` | string |  | ✓ |  |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The e-mail address of the assignee | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Email | `assigneeEmail` | string |  | The e-mail address of the assignee |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Custom field ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| External ID | `externalId` | string |  | An ID you can use to link Zendesk Support tickets to local records |
| Group Name or ID | `group` | options |  | The group this ticket is assigned to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Internal Note | `internalNote` | string |  | Internal Ticket Note (Accepts HTML) |
| Public Reply | `publicReply` | string |  | Public ticket reply |
| Recipient | `recipient` | string |  | The original recipient e-mail address of the ticket |
| Status | `status` | options |  | The state of the ticket |
| Subject | `subject` | string |  | The value of the subject field for this ticket |
| Tag Names or IDs | `tags` | multiOptions | [] | The array of tags applied to this ticket. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Type | `type` | options |  | The type of this ticket |

</details>

| Update Fields | `updateFieldsJson` | json |  | ✗ | Object of values to update as described <a href="https://developer.zendesk.com/rest_api/docs/support/tickets">here</a> |  |
| User ID | `id` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | An alias displayed to end users | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Alias | `alias` | string |  | An alias displayed to end users |
| Custom Role ID | `custom_role_id` | number | 0 | A custom role if the user is an agent on the Enterprise plan |
| Details | `details` | string |  | Any details you want to store about the user, such as an address |
| Email | `email` | string |  | The user's primary email address |
| External ID | `external_id` | string |  | A unique identifier from another system |
| Locale | `locale` | options |  | The user's locale. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Moderator | `moderator` | boolean | False | Whether the user has forum moderation capabilities |
| Name | `name` | string |  | The user's name |
| Notes | `notes` | string |  | Any notes you want to store about the user |
| Only Private Comments | `only_private_comments` | boolean | False | Whether the user can only create private comments |
| Organization Name or ID | `organization_id` | options |  | The ID of the user's organization. If the user has more than one organization memberships, the ID of the user's default organization. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone | `phone` | string |  | The user's primary phone number |
| Report CSV | `report_csv` | boolean | False | Whether or not the user can access the CSV report on the Search tab of the Reporting page in the Support admin interface |
| Restricted Agent | `restricted_agent` | boolean | False | Whether the agent has any restrictions; false for admins and unrestricted agents, true for other agents |
| Role | `role` | options |  | The user's role |
| Signature | `signature` | string |  | The user's signature. Only agents and admins can have signatures. |
| Suspended | `suspended` | boolean | False | Whether the agent is suspended. Tickets from suspended users are also suspended, and these users cannot sign in to the end user portal. |
| Tag Names or IDs | `tags` | multiOptions | [] | The array of tags applied to this user. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Ticket Restriction | `ticket_restriction` | options |  | Specifies which tickets the user has access to |
| Timezone | `time_zone` | string |  | The user's time zone |
| User Fields | `userFieldsUi` | fixedCollection | {} | Values of custom fields in the user's profile |
| Verified | `verified` | boolean | False | Whether the user's primary identity is verified or not |

</details>

| Organization ID | `id` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Details about the organization, such as the address | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Details | `details` | string |  | Details about the organization, such as the address |
| Domain Names | `domain_names` | string |  | Comma-separated domain names associated with this organization |
| Name | `name` | string |  |  |
| Notes | `notes` | string |  |  |
| Organization Fields | `organizationFieldsUi` | fixedCollection | {} | Values of custom fields in the organization's profile |
| Tag Names or IDs | `tags` | multiOptions | [] | IDs of tags applied to this organization. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Get Organizations parameters (`getOrganizations`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `id` | string |  | ✓ |  |  |

### Get Related Data parameters (`getRelatedData`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `id` | string |  | ✓ |  |  |
| Organization ID | `id` | string |  | ✓ |  |  |

### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  |  |
| External ID | `external_id` | string |  |  |

</details>


---

## Load Options Methods

- `getCustomFields`
- `for`
- `if`
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
* Categories: Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: zendesk
displayName: Zendesk
description: Consume Zendesk API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: zendeskApi
  required: true
- name: zendeskOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a ticket
  params:
  - id: description
    name: Description
    type: string
    default: ''
    required: true
    description: The first comment on the ticket
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - create
    typeInfo:
      type: string
      displayName: Description
      name: description
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id011
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - update
    typeInfo: &id012
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Object of values to set as described <a href="https://developer.zendesk.com/rest_api/docs/support/tickets">here</a>
    validation:
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - create
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Additional Fields
      name: additionalFieldsJson
      typeOptions:
        alwaysOpenEditWindow: true
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The user's name
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - organization
          operation:
          - create
    typeInfo: &id002
      type: string
      displayName: Name
      name: name
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
- id: delete
  name: Delete
  description: Delete a ticket
  params:
  - id: ticketType
    name: Ticket Type
    type: options
    default: regular
    required: true
    description: ''
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - get
          - delete
          - getAll
    typeInfo: &id006
      type: options
      displayName: Ticket Type
      name: ticketType
      possibleValues:
      - value: regular
        name: Regular
        description: ''
      - value: suspended
        name: Suspended
        description: ''
  - id: id
    name: Ticket ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - organization
          operation:
          - getRelatedData
    typeInfo: &id004
      type: string
      displayName: Organization ID
      name: id
  - id: id
    name: Suspended Ticket ID
    type: string
    default: ''
    required: true
    description: Ticket ID
    validation: *id003
    typeInfo: *id004
  - id: id
    name: User ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Organization ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
- id: get
  name: Get
  description: Get a ticket
  params:
  - id: ticketType
    name: Ticket Type
    type: options
    default: regular
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: id
    name: Ticket ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Suspended Ticket ID
    type: string
    default: ''
    required: true
    description: Ticket ID
    validation: *id003
    typeInfo: *id004
  - id: ticketFieldId
    name: Ticket Field ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - ticketField
          operation:
          - get
    typeInfo:
      type: string
      displayName: Ticket Field ID
      name: ticketFieldId
  - id: id
    name: User ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Organization ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: Get many tickets
  params:
  - id: ticketType
    name: Ticket Type
    type: options
    default: regular
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
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
          - organization
          operation:
          - getAll
    typeInfo: &id008
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id009
      displayOptions:
        show:
          resource:
          - organization
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
        maxValue: 100
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
    default: 100
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
    default: 100
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
- id: recover
  name: Recover
  description: Recover a suspended ticket
  params:
  - id: id
    name: Suspended Ticket ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
- id: update
  name: Update
  description: Update a ticket
  params:
  - id: id
    name: Ticket ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: updateFieldsJson
    name: Update Fields
    type: json
    default: ''
    required: false
    description: Object of values to update as described <a href="https://developer.zendesk.com/rest_api/docs/support/tickets">here</a>
    validation:
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - update
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Update Fields
      name: updateFieldsJson
      typeOptions:
        alwaysOpenEditWindow: true
  - id: id
    name: User ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Organization ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
- id: getOrganizations
  name: Get Organizations
  description: Get a user's organizations
  params:
  - id: id
    name: User ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
- id: getRelatedData
  name: Get Related Data
  description: Get data related to the user
  params:
  - id: id
    name: User ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Organization ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
- id: search
  name: Search
  description: Search users
  params:
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
- id: count
  name: Count
  description: Count organizations
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
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/zendesk.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Zendesk Node",
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
        "recover",
        "update",
        "getOrganizations",
        "getRelatedData",
        "search",
        "count"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "apiToken",
            "oAuth2"
          ],
          "default": "apiToken"
        },
        "resource": {
          "description": "Tickets are the means through which your end users (customers) communicate with agents in Zendesk Support",
          "type": "string",
          "enum": [
            "ticket",
            "ticketField",
            "user",
            "organization"
          ],
          "default": "ticket"
        },
        "operation": {
          "description": "Count organizations",
          "type": "string",
          "enum": [
            "count",
            "create",
            "delete",
            "get",
            "getAll",
            "getRelatedData",
            "update"
          ],
          "default": "create"
        },
        "description": {
          "description": "The first comment on the ticket",
          "type": "string",
          "default": ""
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "additionalFields": {
          "description": "Details about the organization, such as the address",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "additionalFieldsJson": {
          "description": "Object of values to set as described <a href=\"https://developer.zendesk.com/rest_api/docs/support/tickets\">here</a>",
          "type": "string",
          "default": ""
        },
        "id": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Details about the organization, such as the address",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFieldsJson": {
          "description": "Object of values to update as described <a href=\"https://developer.zendesk.com/rest_api/docs/support/tickets\">here</a>",
          "type": "string",
          "default": ""
        },
        "ticketType": {
          "description": "",
          "type": "string",
          "enum": [
            "regular",
            "suspended"
          ],
          "default": "regular"
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
        "options": {
          "description": "The group to search. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "ticketFieldId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "filters": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
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
      "name": "zendeskApi",
      "required": true
    },
    {
      "name": "zendeskOAuth2Api",
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
