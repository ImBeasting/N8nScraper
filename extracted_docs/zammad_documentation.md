---
title: "Node: Zammad"
slug: "node-zammad"
version: "1"
updated: "2025-11-13"
summary: "Consume the Zammad API"
node_type: "regular"
group: "['input']"
---

# Node: Zammad

**Purpose.** Consume the Zammad API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:zammad.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **zammadBasicAuthApi**: N/A
- **zammadTokenAuthApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `zammadBasicAuthApi` | ✓ | {'show': {'authentication': ['basicAuth']}} |
| `zammadTokenAuthApi` | ✓ | {'show': {'authentication': ['tokenAuth']}} |

---

## Operations

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a user |
| Delete | `delete` | Delete a user |
| Get | `get` | Retrieve a user |
| Get Many | `getAll` | Retrieve many users |
| Get Self | `getSelf` | Retrieve currently logged-in user |
| Update | `update` | Update a user |

### Group Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a group |
| Delete | `delete` | Delete a group |
| Get | `get` | Retrieve a group |
| Get Many | `getAll` | Get many groups |
| Update | `update` | Update a group |

### Organization Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an organization |
| Delete | `delete` | Delete an organization |
| Get | `get` | Retrieve an organization |
| Get Many | `getAll` | Retrieve many organizations |
| Update | `update` | Update an organization |

### Ticket Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a ticket |
| Delete | `delete` | Delete a ticket |
| Get | `get` | Retrieve a ticket |
| Get Many | `getAll` | Retrieve many tickets |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | user | ✗ | Resource to operate on |  |

**Resource options:**

* **Group** (`group`)
* **Organization** (`organization`)
* **Ticket** (`ticket`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a user |  |

**Operation options:**

* **Create** (`create`) - Create a user
* **Delete** (`delete`) - Delete a user
* **Get** (`get`) - Retrieve a user
* **Get Many** (`getAll`) - Retrieve many users
* **Get Self** (`getSelf`) - Retrieve currently logged-in user
* **Update** (`update`) - Update a user

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| First Name | `firstname` | string |  | ✓ | e.g. John |  |
| Last Name | `lastname` | string |  | ✓ | e.g. Smith |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the custom field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Active | `active` | boolean | True |  |
| Address | `addressUi` | fixedCollection | {} |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Name of the custom field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Department | `department` | string |  |  |
| Email Address | `email` | string |  |  |
| Fax | `fax` | string |  |  |
| Notes | `note` | string |  |  |
| Organization Name or ID | `organization` | options |  | Name of the organization to assign to the user. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone (Landline) | `phone` | string |  |  |
| Phone (Mobile) | `mobile` | string |  |  |
| Verified | `verified` | boolean | False | Whether the user has been verified |
| VIP | `vip` | boolean | False | Whether the user is a Very Important Person |
| Website | `web` | string |  |  |

</details>

| Group Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the custom field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Active | `active` | boolean | True |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Name of the custom field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Notes | `note` | string |  |  |

</details>

| Organization Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether the organization is shared with other instances | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Shared | `shared` | boolean | False | Whether the organization is shared with other instances |
| Domain | `domain` | string |  | The domain associated with the organization |
| Domain Assignment | `domain_assignment` | boolean | True | Whether to assign users based on their email domain |
| Active | `active` | boolean | True | Whether the organization is active |
| VIP | `vip` | boolean | False | Whether the organization is marked as VIP |
| Notes | `note` | string |  | A note about the organization |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Name of the custom field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Title | `title` | string |  | ✓ | Title of the ticket to create |  |
| Group Name or ID | `group` | options |  | ✓ | Group that will own the ticket to create. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. First-Level Helpdesk |  |
| Customer Email Name or ID | `customer` | options |  | ✓ | Email address of the customer concerned in the ticket to create. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. hello@n8n.io |  |
| Article | `article` | fixedCollection | {} | ✓ | Visible to customers | e.g. Add Article |  |

<details>
<summary><strong>Article sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Article Details | `articleDetails` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the custom field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Name of the custom field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `id` | string |  | ✓ | User to delete. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Group ID | `id` | string |  | ✓ | Group to delete. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Organization ID | `id` | string |  | ✓ | Organization to delete. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Ticket ID | `id` | string |  | ✓ | Ticket to delete. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `id` | string |  | ✓ | User to retrieve. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Group ID | `id` | string |  | ✓ | Group to retrieve. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Organization ID | `id` | string |  | ✓ | Organization to retrieve. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Ticket ID | `id` | string |  | ✓ | Ticket to retrieve. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Query to filter results by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | Query to filter results by |
| Sort | `sortUi` | fixedCollection | {} | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `id` | string |  | ✓ | User to update. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Name of the custom field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Active | `active` | boolean | True |  |
| Address | `addressUi` | fixedCollection | {} |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Name of the custom field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Department | `department` | string |  |  |
| Email Address | `email` | string |  |  |
| Fax | `fax` | string |  |  |
| First Name | `firstname` | string |  |  |
| Last Name | `lastname` | string |  |  |
| Notes | `note` | string |  |  |
| Organization Name or ID | `organization` | options |  | Name of the organization to assign to the user. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone (Landline) | `phone` | string |  |  |
| Phone (Mobile) | `mobile` | string |  |  |
| Verified | `verified` | boolean | False | Whether the user has been verified |
| VIP | `vip` | boolean | False | Whether the user is a Very Important Person |
| Website | `web` | string |  |  |

</details>

| Group ID | `id` | string |  | ✓ | Group to update. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Name of the custom field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Active | `active` | boolean | True |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Name of the custom field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Group Name | `name` | string |  |  |
| Notes | `note` | string |  |  |

</details>

| Organization ID | `id` | string |  | ✓ | Organization to update. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Whether the organization is shared with other instances | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Shared | `shared` | boolean | False | Whether the organization is shared with other instances |
| Domain | `domain` | string |  | The domain associated with the organization |
| Domain Assignment | `domain_assignment` | boolean | True | Whether to assign users based on their email domain |
| Active | `active` | boolean | True | Whether the organization is active |
| VIP | `vip` | boolean | False | Whether the organization is marked as VIP |
| Notes | `note` | string |  | A note about the organization |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Name of the custom field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


---

## Load Options Methods

- `loadGroupCustomFields`

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
node: zammad
displayName: Zammad
description: Consume the Zammad API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: zammadBasicAuthApi
  required: true
- name: zammadTokenAuthApi
  required: true
operations:
- id: create
  name: Create
  description: Create a user
  params:
  - id: firstname
    name: First Name
    type: string
    default: ''
    required: true
    description: ''
    placeholder: John
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
      displayName: First Name
      name: firstname
  - id: lastname
    name: Last Name
    type: string
    default: ''
    required: true
    description: ''
    placeholder: Smith
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
      displayName: Last Name
      name: lastname
  - id: name
    name: Group Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - organization
    typeInfo: &id002
      type: string
      displayName: Organization Name
      name: name
  - id: name
    name: Organization Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the ticket to create
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
      displayName: Title
      name: title
  - id: group
    name: Group Name or ID
    type: options
    default: ''
    required: true
    description: Group that will own the ticket to create. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    placeholder: First-Level Helpdesk
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - create
    typeInfo:
      type: options
      displayName: Group Name or ID
      name: group
      typeOptions:
        loadOptionsMethod: loadGroupNames
      possibleValues: []
  - id: customer
    name: Customer Email Name or ID
    type: options
    default: ''
    required: true
    description: Email address of the customer concerned in the ticket to create.
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    placeholder: hello@n8n.io
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - create
    typeInfo:
      type: options
      displayName: Customer Email Name or ID
      name: customer
      typeOptions:
        loadOptionsMethod: loadCustomerEmails
      possibleValues: []
  - id: article
    name: Article
    type: fixedCollection
    default: {}
    required: true
    description: Visible to customers
    placeholder: Add Article
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Article
      name: article
      subProperties:
      - name: articleDetails
        displayName: Article Details
        values:
        - displayName: Subject
          name: subject
          type: string
          default: ''
        - displayName: Body
          name: body
          type: string
          default: ''
        - displayName: Visibility
          name: visibility
          type: options
          description: Visible to customers
          value: external
          default: internal
          options:
          - name: External
            description: Visible to customers
            value: external
            displayName: External
          - name: Internal
            description: Visible to help desk
            value: internal
            displayName: Internal
        - displayName: Sender
          name: sender
          type: options
          description: Only subject will be displayed in Zammad
          value: Agent
          default: Agent
          options:
          - name: Agent
            value: Agent
            displayName: Agent
          - name: Customer
            value: Customer
            displayName: Customer
          - name: System
            description: Only subject will be displayed in Zammad
            value: System
            displayName: System
        - displayName: Article Type
          name: type
          type: options
          value: chat
          default: note
          options:
          - name: Chat
            value: chat
            displayName: Chat
          - name: Email
            value: email
            displayName: Email
          - name: Fax
            value: fax
            displayName: Fax
          - name: Note
            value: note
            displayName: Note
          - name: Phone
            value: phone
            displayName: Phone
          - name: SMS
            value: sms
            displayName: Sms
        - displayName: Reply To
          name: reply_to
          type: string
          default: ''
- id: delete
  name: Delete
  description: Delete a user
  params:
  - id: id
    name: User ID
    type: string
    default: ''
    required: true
    description: User to delete. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - delete
    typeInfo: &id004
      type: string
      displayName: Ticket ID
      name: id
  - id: id
    name: Group ID
    type: string
    default: ''
    required: true
    description: Group to delete. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Organization ID
    type: string
    default: ''
    required: true
    description: Organization to delete. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Ticket ID
    type: string
    default: ''
    required: true
    description: Ticket to delete. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
- id: get
  name: Get
  description: Retrieve a user
  params:
  - id: id
    name: User ID
    type: string
    default: ''
    required: true
    description: User to retrieve. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Group ID
    type: string
    default: ''
    required: true
    description: Group to retrieve. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Organization ID
    type: string
    default: ''
    required: true
    description: Organization to retrieve. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Ticket ID
    type: string
    default: ''
    required: true
    description: Ticket to retrieve. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: Retrieve many users
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id005
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - getAll
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id008
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
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: getSelf
  name: Get Self
  description: Retrieve currently logged-in user
- id: update
  name: Update
  description: Update a user
  params:
  - id: id
    name: User ID
    type: string
    default: ''
    required: true
    description: User to update. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Group ID
    type: string
    default: ''
    required: true
    description: Group to update. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Organization ID
    type: string
    default: ''
    required: true
    description: Organization to update. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
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
  - field: firstname
    text: John
  - field: lastname
    text: Smith
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: group
    text: First-Level Helpdesk
  - field: customer
    text: hello@n8n.io
  - field: article
    text: Add Article
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
  "$id": "https://n8n.io/schemas/nodes/zammad.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Zammad Node",
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
        "getSelf",
        "update"
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
            "basicAuth",
            "tokenAuth"
          ],
          "default": "tokenAuth"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "group",
            "organization",
            "ticket",
            "user"
          ],
          "default": "user"
        },
        "operation": {
          "description": "Create a ticket",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll"
          ],
          "default": "create"
        },
        "firstname": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "John"
          ]
        },
        "lastname": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Smith"
          ]
        },
        "id": {
          "description": "Ticket to delete. Specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Name of the custom field to set. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "Whether the organization is shared with other instances",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "query": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 50
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "filters": {
          "description": "Query to filter results by",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "name": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "Title of the ticket to create",
          "type": "string",
          "default": ""
        },
        "group": {
          "description": "Group that will own the ticket to create. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "First-Level Helpdesk"
          ]
        },
        "customer": {
          "description": "Email address of the customer concerned in the ticket to create. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "hello@n8n.io"
          ]
        },
        "article": {
          "description": "Visible to customers",
          "type": "string",
          "default": {},
          "examples": [
            "Add Article"
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
      "name": "zammadBasicAuthApi",
      "required": true
    },
    {
      "name": "zammadTokenAuthApi",
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
