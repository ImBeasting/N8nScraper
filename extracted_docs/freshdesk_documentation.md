---
title: "Node: Freshdesk"
slug: "node-freshdesk"
version: "1"
updated: "2026-01-08"
summary: "Consume Freshdesk API"
node_type: "regular"
group: "['output']"
---

# Node: Freshdesk

**Purpose.** Consume Freshdesk API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:freshdesk.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **freshdeskApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `freshdeskApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Ticket Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new ticket |
| Delete | `delete` | Delete a ticket |
| Get | `get` | Get a ticket |
| Get Many | `getAll` | Get many tickets |
| Update | `update` | Update a ticket |

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new contact |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact |
| Get Many | `getAll` | Get many contacts |
| Update | `update` | Update a contact |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | ticket | ✓ | Resource to operate on |  |

**Resource options:**

* **Contact** (`contact`)
* **Ticket** (`ticket`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✓ | Create a new ticket |  |

**Operation options:**

* **Create** (`create`) - Create a new ticket
* **Delete** (`delete`) - Delete a ticket
* **Get** (`get`) - Get a ticket
* **Get Many** (`getAll`) - Get many tickets
* **Update** (`update`) - Update a ticket

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Requester Identification | `requester` | options | requesterId | ✓ | Email address of the requester. If no contact exists with this email address in Freshdesk, it will be added as a new contact. |  |

**Requester Identification options:**

* **Email** (`email`) - Email address of the requester. If no contact exists with this email address in Freshdesk, it will be added as a new contact.
* **Facebook ID** (`facebookId`) - Facebook ID of the requester. If no contact exists with this facebook_id, then a new contact will be created.
* **Phone** (`phone`) - Phone number of the requester. If no contact exists with this phone number in Freshdesk, it will be added as a new contact. If the phone number is set and the email address is not, then the name attribute is mandatory.
* **Requester ID** (`requesterId`) - User ID of the requester. For existing contacts, the requester_id can be passed instead of the requester's email.
* **Twitter ID** (`twitterId`) - Twitter handle of the requester. If no contact exists with this handle in Freshdesk, it will be added as a new contact.
* **Unique External ID** (`uniqueExternalId`) - External ID of the requester. If no contact exists with this external ID in Freshdesk, they will be added as a new contact.

| Value | `requesterIdentificationValue` | string |  | ✓ | Value of the identification selected |  |
| Status | `status` | options | pending | ✓ |  |  |

**Status options:**

* **Closed** (`closed`)
* **Open** (`open`)
* **Pending** (`pending`)
* **Resolved** (`resolved`)

| Priority | `priority` | options | low | ✓ |  |  |

**Priority options:**

* **Low** (`low`)
* **Medium** (`medium`)
* **High** (`high`)
* **Urgent** (`urgent`)

| Source | `source` | options | portal | ✓ | The channel through which the ticket was created |  |

**Source options:**

* **Chat** (`chat`)
* **Email** (`email`)
* **Feedback Widget** (`feedbackWidget`)
* **Mobihelp** (`mobileHelp`)
* **Outbound Email** (`OutboundEmail`)
* **Phone** (`phone`)
* **Portal** (`portal`)

| Options | `options` | collection | {} | ✗ | ID of the agent to whom the ticket has been assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Agent Name or ID | `agent` | options |  | ID of the agent to whom the ticket has been assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| CC Emails | `ccEmails` | string |  | Separated by a comma (,) email addresses added in the 'cc' field of the incoming ticket email |
| Company Name or ID | `company` | options |  | Company ID of the requester. This attribute can only be set if the Multiple Companies feature is enabled (Estate plan and above). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | HTML content of the ticket |
| Due By | `dueBy` | dateTime |  | Timestamp that denotes when the ticket is due to be resolved |
| Email Config ID | `emailConfigId` | number |  | ID of email config which is used for this ticket. (i.e., support@yourcompany.com/sales@yourcompany.com) If product_id is given and email_config_id is not given, product's primary email_config_id will be set. |
| FR Due By | `frDueBy` | dateTime |  | Timestamp that denotes when the first response is due |
| Group Name or ID | `group` | options |  | ID of the group to which the ticket has been assigned. The default value is the ID of the group that is associated with the given email_config_id. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Name | `name` | string |  | Name of the requester |
| Product Name or ID | `product` | options |  | ID of the product to which the ticket is associated. It will be ignored if the email_config_id attribute is set in the request. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Subject | `subject` | string |  | Subject of the ticket |
| Tags | `tags` | string |  | Separated by a comma (,) tags that have been associated with the ticket |
| Type | `type` | options | Question | Helps categorize the ticket according to the different kinds of issues your support team deals with |

</details>

| Name | `name` | string |  | ✓ | Name of the contact |  |
| Email | `email` | string |  | ✗ | Primary email address of the contact. If you want to associate additional email(s) with this contact, use the other_emails attribute. | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Address of the contact | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  | Address of the contact |
| Avatar | `avatar` |  |  | Avatar image of the contact The maximum file size is 5MB
			// 	and the supported file types are .jpg, .jpeg, .jpe, and .png. |
| Company ID | `company_id` | number |  | ID of the primary company to which this contact belongs |
| Custom Fields | `customFields` | fixedCollection | [] | Key value pairs containing the name and value of the custom field. Only dates in the format YYYY-MM-DD are accepted as input for custom date fields. |
| Description | `description` | string |  | A small description of the contact |
| Email | `email` | string |  | Primary email address of the contact. If you want to associate additional email(s) with this contact, use the other_emails attribute. |
| Job Title | `job_title` | string |  | Job title of the contact |
| Language | `language` | string |  | Language of the contact. Default language is "en". This attribute can only be set if the Multiple Language feature is enabled (Garden plan and above). |
| Mobile | `mobile` | string |  | Mobile number of the contact |
| Name | `name` | string |  | Name of the contact |
| Other Companies | `other_companies` | string | [] | Additional companies associated with the contact. This attribute can only be set if the Multiple Companies feature is enabled (Estate plan and above). |
| Other Emails | `other_emails` | string | [] | Additional emails associated with the contact |
| Phone | `phone` | string |  | Telephone number of the contact |
| Tags | `tags` | string | [] | Tags associated with this contact |
| Time Zone | `time_zone` | string |  | Time zone of the contact. Default value is the time zone of the domain. This attribute can only be set if the Multiple Time Zone feature is enabled (Garden plan and above). |
| Twitter ID | `twitter_id` | string |  | Twitter handle of the contact |
| Unique External ID | `unique_external_id` | string |  | External ID of the contact |
| View All Tickets | `view_all_tickets` | boolean | False | Whether the contact can see all the tickets that are associated with the company to which they belong |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Ticket ID | `ticketId` | string |  | ✓ |  |  |
| Contact ID | `contactId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Ticket ID | `ticketId` | string |  | ✓ |  |  |
| Contact ID | `contactId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Options | `options` | collection | {} | ✗ | Order sort attribute ascending or descending | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company ID | `companyId` | string |  |  |
| Include | `include` | multiOptions | [] |  |
| Order | `order` | options | desc | Order sort attribute ascending or descending |
| Order By | `orderBy` | options |  | Sort collection by object attribute |
| Requester Email | `requesterEmail` | string |  |  |
| Requester ID | `requesterId` | string |  |  |
| Updated Since | `updatedSince` | dateTime |  |  |

</details>

| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company ID | `company_id` | number |  |  |
| Email | `email` | string |  |  |
| Mobile | `mobile` | string |  |  |
| Phone | `phone` | string |  |  |
| State | `state` | options |  |  |
| Updated Since | `updated_since` | dateTime |  |  |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Ticket ID | `ticketId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the agent to whom the ticket has been assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Agent Name or ID | `agent` | options |  | ID of the agent to whom the ticket has been assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| CC Emails | `ccEmails` | string |  | Separated by a comma (,) email addresses added in the 'cc' field of the incoming ticket email |
| Company Name or ID | `company` | options |  | Company ID of the requester. This attribute can only be set if the Multiple Companies feature is enabled (Estate plan and above). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Due By | `dueBy` | dateTime |  | Timestamp that denotes when the ticket is due to be resolved |
| Email Config ID | `emailConfigId` | number |  | ID of email config which is used for this ticket. (i.e., support@yourcompany.com/sales@yourcompany.com) If product_id is given and email_config_id is not given, product's primary email_config_id will be set. |
| FR Due By | `frDueBy` | dateTime |  | Timestamp that denotes when the first response is due |
| Group Name or ID | `group` | options |  | ID of the group to which the ticket has been assigned. The default value is the ID of the group that is associated with the given email_config_id. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Name | `name` | string |  | Name of the requester |
| Product Name or ID | `product` | options |  | ID of the product to which the ticket is associated. It will be ignored if the email_config_id attribute is set in the request. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Priority | `priority` | options | low |  |
| Requester Identification | `requester` | options | requesterId | Email address of the requester. If no contact exists with this email address in Freshdesk, it will be added as a new contact. |
| Requester Value | `requesterIdentificationValue` | string |  | Value of the identification selected |
| Status | `status` | options | pending |  |
| Source | `source` | options | portal | The channel through which the ticket was created |
| Tags | `tags` | string |  | Separated by a comma (,) tags that have been associated with the ticket |
| Type | `type` | options | Question | Helps categorize the ticket according to the different kinds of issues your support team deals with |

</details>

| Contact ID | `contactId` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Address of the contact | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  | Address of the contact |
| Avatar | `avatar` |  |  | Avatar image of the contact The maximum file size is 5MB
			// 	and the supported file types are .jpg, .jpeg, .jpe, and .png. |
| Company ID | `company_id` | number |  | ID of the primary company to which this contact belongs |
| Custom Fields | `customFields` | fixedCollection | [] | Key value pairs containing the name and value of the custom field. Only dates in the format YYYY-MM-DD are accepted as input for custom date fields. |
| Description | `description` | string |  | A small description of the contact |
| Email | `email` | string |  | Primary email address of the contact. If you want to associate additional email(s) with this contact, use the other_emails attribute. |
| Job Title | `job_title` | string |  | Job title of the contact |
| Language | `language` | string |  | Language of the contact. Default language is "en". This attribute can only be set if the Multiple Language feature is enabled (Garden plan and above). |
| Mobile | `mobile` | string |  | Mobile number of the contact |
| Name | `name` | string |  | Name of the contact |
| Other Companies | `other_companies` | string | [] | Additional companies associated with the contact. This attribute can only be set if the Multiple Companies feature is enabled (Estate plan and above). |
| Other Emails | `other_emails` | string | [] | Additional emails associated with the contact |
| Phone | `phone` | string |  | Telephone number of the contact |
| Tags | `tags` | string | [] | Tags associated with this contact |
| Time Zone | `time_zone` | string |  | Time zone of the contact. Default value is the time zone of the domain. This attribute can only be set if the Multiple Time Zone feature is enabled (Garden plan and above). |
| Twitter ID | `twitter_id` | string |  | Twitter handle of the contact |
| Unique External ID | `unique_external_id` | string |  | External ID of the contact |
| View All Tickets | `view_all_tickets` | boolean | False | Whether the contact can see all the tickets that are associated with the company to which they belong |

</details>


---

## Load Options Methods

- `getAgents`
- `for`
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
node: freshdesk
displayName: Freshdesk
description: Consume Freshdesk API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: freshdeskApi
  required: true
operations:
- id: create
  name: Create
  description: Create a new ticket
  params:
  - id: requester
    name: Requester Identification
    type: options
    default: requesterId
    required: true
    description: Email address of the requester. If no contact exists with this email
      address in Freshdesk, it will be added as a new contact.
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
      displayName: Requester Identification
      name: requester
      possibleValues:
      - value: email
        name: Email
        description: Email address of the requester. If no contact exists with this
          email address in Freshdesk, it will be added as a new contact.
      - value: facebookId
        name: Facebook ID
        description: Facebook ID of the requester. If no contact exists with this
          facebook_id, then a new contact will be created.
      - value: phone
        name: Phone
        description: Phone number of the requester. If no contact exists with this
          phone number in Freshdesk, it will be added as a new contact. If the phone
          number is set and the email address is not, then the name attribute is mandatory.
      - value: requesterId
        name: Requester ID
        description: User ID of the requester. For existing contacts, the requester_id
          can be passed instead of the requester's email.
      - value: twitterId
        name: Twitter ID
        description: Twitter handle of the requester. If no contact exists with this
          handle in Freshdesk, it will be added as a new contact.
      - value: uniqueExternalId
        name: Unique External ID
        description: External ID of the requester. If no contact exists with this
          external ID in Freshdesk, they will be added as a new contact.
  - id: requesterIdentificationValue
    name: Value
    type: string
    default: ''
    required: true
    description: Value of the identification selected
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
      displayName: Value
      name: requesterIdentificationValue
  - id: status
    name: Status
    type: options
    default: pending
    required: true
    description: ''
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
      displayName: Status
      name: status
      possibleValues:
      - value: closed
        name: Closed
        description: ''
      - value: open
        name: Open
        description: ''
      - value: pending
        name: Pending
        description: ''
      - value: resolved
        name: Resolved
        description: ''
  - id: priority
    name: Priority
    type: options
    default: low
    required: true
    description: ''
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
      displayName: Priority
      name: priority
      possibleValues:
      - value: low
        name: Low
        description: ''
      - value: medium
        name: Medium
        description: ''
      - value: high
        name: High
        description: ''
      - value: urgent
        name: Urgent
        description: ''
  - id: source
    name: Source
    type: options
    default: portal
    required: true
    description: The channel through which the ticket was created
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
      displayName: Source
      name: source
      possibleValues:
      - value: chat
        name: Chat
        description: ''
      - value: email
        name: Email
        description: ''
      - value: feedbackWidget
        name: Feedback Widget
        description: ''
      - value: mobileHelp
        name: Mobihelp
        description: ''
      - value: OutboundEmail
        name: Outbound Email
        description: ''
      - value: phone
        name: Phone
        description: ''
      - value: portal
        name: Portal
        description: ''
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the contact
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - contact
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Primary email address of the contact. If you want to associate additional
      email(s) with this contact, use the other_emails attribute.
    placeholder: name@email.com
    validation:
      format: email
      displayOptions:
        show:
          operation:
          - create
          resource:
          - contact
    typeInfo:
      type: string
      displayName: Email
      name: email
- id: delete
  name: Delete
  description: Delete a ticket
  params:
  - id: ticketId
    name: Ticket ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - delete
    typeInfo: &id002
      type: string
      displayName: Ticket ID
      name: ticketId
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - get
    typeInfo: &id004
      type: string
      displayName: Contact ID
      name: contactId
- id: get
  name: Get
  description: Get a ticket
  params:
  - id: ticketId
    name: Ticket ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: contactId
    name: Contact ID
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
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - getAll
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 10
- id: update
  name: Update
  description: Update a ticket
  params:
  - id: ticketId
    name: Ticket ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
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
  - field: options
    text: Add option
  - field: customFieldsUi
    text: Add Custom fields
  - field: customFieldsJson
    text: "{\n\t\t\t// \t\t'gadget': 'Cold Welder',\n\t\t\t// \t}"
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/freshdesk.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Freshdesk Node",
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
            "contact",
            "ticket"
          ],
          "default": "ticket"
        },
        "operation": {
          "description": "Create a new contact",
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
        "requester": {
          "description": "Email address of the requester. If no contact exists with this email address in Freshdesk, it will be added as a new contact.",
          "type": "string",
          "enum": [
            "email",
            "facebookId",
            "phone",
            "requesterId",
            "twitterId",
            "uniqueExternalId"
          ],
          "default": "requesterId"
        },
        "requesterIdentificationValue": {
          "description": "Value of the identification selected",
          "type": "string",
          "default": ""
        },
        "status": {
          "description": "",
          "type": "string",
          "enum": [
            "closed",
            "open",
            "pending",
            "resolved"
          ],
          "default": "pending"
        },
        "priority": {
          "description": "",
          "type": "string",
          "enum": [
            "low",
            "medium",
            "high",
            "urgent"
          ],
          "default": "low"
        },
        "source": {
          "description": "The channel through which the ticket was created",
          "type": "string",
          "enum": [
            "chat",
            "email",
            "feedbackWidget",
            "mobileHelp",
            "OutboundEmail",
            "phone",
            "portal"
          ],
          "default": "portal"
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "options": {
          "description": "Order sort attribute ascending or descending",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "customFieldsUi": {
          "description": "Key value pairs containing the names and values of custom fields.",
          "type": "string",
          "default": "",
          "examples": [
            "Add Custom fields"
          ]
        },
        "customFieldsJson": {
          "description": "Key value pairs containing the names and values of custom fields.",
          "type": "string",
          "default": "",
          "examples": [
            "{\n\t\t\t// \t\t'gadget': 'Cold Welder',\n\t\t\t// \t}"
          ]
        },
        "ticketId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "ID of the agent to whom the ticket has been assigned. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
          "default": 5
        },
        "name": {
          "description": "Name of the contact",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "Primary email address of the contact. If you want to associate additional email(s) with this contact, use the other_emails attribute.",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "contactId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Address of the contact",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
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
      "name": "freshdeskApi",
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
