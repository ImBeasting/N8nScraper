---
title: "Node: Mautic"
slug: "node-mautic"
version: "1"
updated: "2026-01-08"
summary: "Consume Mautic API"
node_type: "regular"
group: "['output']"
---

# Node: Mautic

**Purpose.** Consume Mautic API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:mautic.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **mauticApi**: N/A
- **mauticOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `mauticApi` | ✓ | {'show': {'authentication': ['credentials']}} |
| `mauticOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Company Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new company |
| Delete | `delete` | Delete a company |
| Get | `get` | Get data of a company |
| Get Many | `getAll` | Get data of many companies |
| Update | `update` | Update a company |

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new contact |
| Delete | `delete` | Delete a contact |
| Edit Contact Points | `editContactPoint` | Edit contact's points |
| Edit Do Not Contact List | `editDoNotContactList` | Add/remove contacts from/to the do not contact list |
| Get | `get` | Get data of a contact |
| Get Many | `getAll` | Get data of many contacts |
| Send Email | `sendEmail` | Send email to contact |
| Update | `update` | Update a contact |

### Contactsegment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add contact to a segment |
| Remove | `remove` | Remove contact from a segment |

### Campaigncontact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add contact to a campaign |
| Remove | `remove` | Remove contact from a campaign |

### Companycontact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add contact to a company |
| Remove | `remove` | Remove a contact from a company |

### Segmentemail Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send an email to a segment |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✗ | Add/remove contacts to/from a campaign |  |

**Resource options:**

* **Campaign Contact** (`campaignContact`) - Add/remove contacts to/from a campaign
* **Company** (`company`) - Create or modify a company
* **Company Contact** (`companyContact`) - Add/remove contacts to/from a company
* **Contact** (`contact`) - Create & modify contacts
* **Contact Segment** (`contactSegment`) - Add/remove contacts to/from a segment
* **Segment Email** (`segmentEmail`) - Send an email

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a new company |  |

**Operation options:**

* **Create** (`create`) - Create a new company
* **Delete** (`delete`) - Delete a company
* **Get** (`get`) - Get data of a company
* **Get Many** (`getAll`) - Get data of many companies
* **Update** (`update`) - Update a company

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company Name | `name` | string |  | ✗ | The name of the company to create |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Adds a custom fields to set also values which have not been predefined | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressUi` | fixedCollection | {} |  |
| Annual Revenue | `annualRevenue` | number | 0 |  |
| Company Email | `companyEmail` | string |  |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Adds a custom fields to set also values which have not been predefined |
| Description | `description` | string |  |  |
| Fax | `fax` | string |  |  |
| Industry Name or ID | `industry` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Is Published | `isPublished` | boolean | False |  |
| Number of Employees | `numberOfEmpoyees` | number | 0 |  |
| Overwrite With Blank | `overwriteWithBlank` | boolean | False | Whether empty values are set to fields. Otherwise empty values are skipped. |
| Phone | `phone` | string |  |  |
| Website | `website` | string |  |  |

</details>

| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Email | `email` | string |  | ✗ | Email address of the contact | e.g. name@email.com | email |
| First Name | `firstName` | string |  | ✗ |  |  |
| Last Name | `lastName` | string |  | ✗ |  |  |
| Primary Company Name or ID | `company` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Position | `position` | string |  | ✗ |  |  |
| Title | `title` | string |  | ✗ |  |  |
| Body | `bodyJson` | json |  | ✗ | Contact parameters |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Adds a custom fields to set also values which have not been predefined | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressUi` | fixedCollection | {} |  |
| B2B or B2C | `b2bOrb2c` | options |  |  |
| CRM ID | `crmId` | string |  |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Adds a custom fields to set also values which have not been predefined |
| Fax | `fax` | string |  |  |
| Has Purchased | `hasPurchased` | boolean | False |  |
| IP Address | `ipAddress` | string |  | IP address to associate with the contact |
| Last Active | `lastActive` | dateTime |  | Date/time in UTC; |
| Mobile | `mobile` | string |  |  |
| Owner ID | `ownerId` | string |  | ID of a Mautic user to assign this contact to |
| Phone | `phone` | string |  |  |
| Prospect or Customer | `prospectOrCustomer` | options |  |  |
| Sandbox | `sandbox` | boolean | False |  |
| Stage Name or ID | `stage` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Social Media | `socialMediaUi` | fixedCollection | {} |  |
| Website | `website` | string |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company ID | `companyId` | string |  | ✗ | The ID of the company to delete |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Contact ID | `contactId` | string |  | ✗ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company ID | `companyId` | string |  | ✗ | The ID of the company to return |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Contact ID | `contactId` | string |  | ✗ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 30 | ✗ | Max number of results to return | min:1, max:30 |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Sort direction: asc or desc | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Order Direction | `orderByDir` | options |  | Sort direction: asc or desc |
| Order By Name or ID | `orderBy` | options |  | Column to sort by. Can use any column listed in the response. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Search | `search` | string |  | String or search command to filter entities by |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 30 | ✗ | Max number of results to return | min:1, max:30 |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company ID | `companyId` | string |  | ✗ | The ID of the company to update |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Adds a custom fields to set also values which have not been predefined | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressUi` | fixedCollection | {} |  |
| Annual Revenue | `annualRevenue` | number | 0 |  |
| Company Email | `companyEmail` | string |  |  |
| Company Name | `name` | string |  |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Adds a custom fields to set also values which have not been predefined |
| Description | `description` | string |  |  |
| Fax | `fax` | string |  |  |
| Industry Name or ID | `industry` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Is Published | `isPublished` | boolean | False |  |
| Number of Employees | `numberOfEmpoyees` | number | 0 |  |
| Overwrite With Blank | `overwriteWithBlank` | boolean | False | Whether empty values are set to fields. Otherwise, empty values are skipped. |
| Phone | `phone` | string |  |  |
| Website | `website` | string |  |  |

</details>

| Contact ID | `contactId` | string |  | ✗ |  |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Contact parameters | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body | `bodyJson` | json |  | Contact parameters |
| Address | `addressUi` | fixedCollection | {} |  |
| B2B or B2C | `b2bOrb2c` | options |  |  |
| CRM ID | `crmId` | string |  |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Adds a custom fields to set also values which have not been predefined |
| Email | `email` | string |  | Email address of the contact |
| Fax | `fax` | string |  |  |
| First Name | `firstName` | string |  |  |
| Has Purchased | `hasPurchased` | boolean | False |  |
| IP Address | `ipAddress` | string |  | IP address to associate with the contact |
| Last Active | `lastActive` | dateTime |  | Date/time in UTC; |
| Last Name | `lastName` | string |  | LastName |
| Mobile | `mobile` | string |  |  |
| Owner ID | `ownerId` | string |  | ID of a Mautic user to assign this contact to |
| Phone | `phone` | string |  |  |
| Position | `position` | string |  |  |
| Primary Company Name or ID | `company` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Prospect or Customer | `prospectOrCustomer` | options |  |  |
| Sandbox | `sandbox` | boolean | False |  |
| Stage Name or ID | `stage` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Title | `title` | string |  |  |
| Social Media | `socialMediaUi` | fixedCollection | {} |  |
| Website | `website` | string |  |  |
| IP Address | `ipAddress` | string |  | IP address to associate with the contact |

</details>


### Edit Contact Points parameters (`editContactPoint`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✗ |  |  |
| Action | `action` | options | add | ✗ |  |  |

**Action options:**

* **Add** (`add`) - Add a contact
* **Remove** (`remove`) - Remove a contact

| Points | `points` | number | 0 | ✗ |  |  |

### Edit Do Not Contact List parameters (`editDoNotContactList`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✗ |  |  |
| Action | `action` | options | add | ✗ |  |  |

**Action options:**

* **Add** (`add`) - Add a contact
* **Remove** (`remove`) - Remove a contact

| Channel | `channel` | options | email | ✓ |  |  |

**Channel options:**

* **Email** (`email`)
* **SMS** (`sms`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | A text describing details of Do Not Contact entry | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Reason To Do Not Contact | `reason` | options | 3 |  |
| Comments | `comments` | string |  | A text describing details of Do Not Contact entry |

</details>


### Send Email parameters (`sendEmail`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign Email Name or ID | `campaignEmailId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | email |
| Contact ID | `contactId` | string |  | ✓ |  |  |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Segment Name or ID | `segmentId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Campaign Name or ID | `campaignId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Contact ID | `contactId` | string |  | ✗ | The ID of the contact |  |
| Company ID | `companyId` | string |  | ✗ | The ID of the company |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Segment Name or ID | `segmentId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Campaign Name or ID | `campaignId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Contact ID | `contactId` | string |  | ✗ | The ID of the contact |  |
| Company ID | `companyId` | string |  | ✗ | The ID of the company |  |

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Segment Email Name or ID | `segmentEmailId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | email |

---

## Load Options Methods

- `getCompanies`
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
* Categories: Marketing, Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: mautic
displayName: Mautic
description: Consume Mautic API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: mauticApi
  required: true
- name: mauticOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a new company
  params:
  - id: name
    name: Company Name
    type: string
    default: ''
    required: false
    description: The name of the company to create
    validation:
      displayOptions:
        show:
          resource:
          - company
          operation:
          - create
    typeInfo:
      type: string
      displayName: Company Name
      name: name
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id001
      displayOptions:
        show:
          resource:
          - company
          operation:
          - delete
    typeInfo: &id002
      type: boolean
      displayName: Simplify
      name: simple
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id011
      displayOptions:
        show:
          operation:
          - update
          resource:
          - contact
    typeInfo: &id012
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email address of the contact
    placeholder: name@email.com
    validation:
      format: email
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: firstName
    name: First Name
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: string
      displayName: First Name
      name: firstName
  - id: lastName
    name: Last Name
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: string
      displayName: Last Name
      name: lastName
  - id: company
    name: Primary Company Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: options
      displayName: Primary Company Name or ID
      name: company
      typeOptions:
        loadOptionsMethod: getCompanies
      possibleValues: []
  - id: position
    name: Position
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: string
      displayName: Position
      name: position
  - id: title
    name: Title
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: bodyJson
    name: Body
    type: json
    default: ''
    required: false
    description: Contact parameters
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - contact
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Body
      name: bodyJson
- id: delete
  name: Delete
  description: Delete a company
  params:
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: false
    description: The ID of the company to delete
    validation: &id003
      displayOptions:
        show:
          resource:
          - companyContact
          operation:
          - add
          - remove
    typeInfo: &id004
      type: string
      displayName: Company ID
      name: companyId
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id001
    typeInfo: *id002
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: false
    description: ''
    validation: &id005
      displayOptions:
        show:
          resource:
          - companyContact
          operation:
          - add
          - remove
    typeInfo: &id006
      type: string
      displayName: Contact ID
      name: contactId
- id: get
  name: Get
  description: Get data of a company
  params:
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: false
    description: The ID of the company to return
    validation: *id003
    typeInfo: *id004
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id001
    typeInfo: *id002
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id005
    typeInfo: *id006
- id: getAll
  name: Get Many
  description: Get data of many companies
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
          - contact
          operation:
          - getAll
    typeInfo: &id008
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 30
    required: false
    description: Max number of results to return
    validation: &id009
      displayOptions:
        show:
          resource:
          - contact
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
        maxValue: 30
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id001
    typeInfo: *id002
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
    default: 30
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
- id: update
  name: Update
  description: Update a company
  params:
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: false
    description: The ID of the company to update
    validation: *id003
    typeInfo: *id004
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id001
    typeInfo: *id002
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id011
    typeInfo: *id012
- id: editContactPoint
  name: Edit Contact Points
  description: Edit contact's points
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: action
    name: Action
    type: options
    default: add
    required: false
    description: ''
    validation: &id013
      displayOptions:
        show:
          operation:
          - editContactPoint
          resource:
          - contact
    typeInfo: &id014
      type: options
      displayName: Action
      name: action
      possibleValues:
      - value: add
        name: Add
        description: ''
      - value: remove
        name: Remove
        description: ''
  - id: points
    name: Points
    type: number
    default: 0
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - editContactPoint
          resource:
          - contact
    typeInfo:
      type: number
      displayName: Points
      name: points
- id: editDoNotContactList
  name: Edit Do Not Contact List
  description: Add/remove contacts from/to the do not contact list
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: action
    name: Action
    type: options
    default: add
    required: false
    description: ''
    validation: *id013
    typeInfo: *id014
  - id: channel
    name: Channel
    type: options
    default: email
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - editDoNotContactList
    typeInfo:
      type: options
      displayName: Channel
      name: channel
      possibleValues:
      - value: email
        name: Email
        description: ''
      - value: sms
        name: SMS
        description: ''
- id: sendEmail
  name: Send Email
  description: Send email to contact
  params:
  - id: campaignEmailId
    name: Campaign Email Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - sendEmail
    typeInfo:
      type: options
      displayName: Campaign Email Name or ID
      name: campaignEmailId
      typeOptions:
        loadOptionsMethod: getCampaignEmails
      possibleValues: []
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
- id: add
  name: Add
  description: Add contact to a segment
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: segmentId
    name: Segment Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - contactSegment
          operation:
          - add
          - remove
    typeInfo: &id016
      type: options
      displayName: Segment Name or ID
      name: segmentId
      typeOptions:
        loadOptionsMethod: getSegments
      possibleValues: []
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: campaignId
    name: Campaign Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id017
      required: true
      displayOptions:
        show:
          resource:
          - campaignContact
          operation:
          - add
          - remove
    typeInfo: &id018
      type: options
      displayName: Campaign Name or ID
      name: campaignId
      typeOptions:
        loadOptionsMethod: getCampaigns
      possibleValues: []
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: false
    description: The ID of the contact
    validation: *id005
    typeInfo: *id006
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: false
    description: The ID of the company
    validation: *id003
    typeInfo: *id004
- id: remove
  name: Remove
  description: Remove contact from a segment
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: segmentId
    name: Segment Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id015
    typeInfo: *id016
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: campaignId
    name: Campaign Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id017
    typeInfo: *id018
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: false
    description: The ID of the contact
    validation: *id005
    typeInfo: *id006
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: false
    description: The ID of the company
    validation: *id003
    typeInfo: *id004
- id: send
  name: Send
  description: ''
  params:
  - id: segmentEmailId
    name: Segment Email Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - segmentEmail
          operation:
          - send
    typeInfo:
      type: options
      displayName: Segment Email Name or ID
      name: segmentEmailId
      typeOptions:
        loadOptionsMethod: getSegmentEmails
      possibleValues: []
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
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/mautic.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Mautic Node",
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
        "update",
        "editContactPoint",
        "editDoNotContactList",
        "sendEmail",
        "add",
        "remove",
        "send"
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
            "credentials",
            "oAuth2"
          ],
          "default": "credentials"
        },
        "resource": {
          "description": "Add/remove contacts to/from a campaign",
          "type": "string",
          "enum": [
            "campaignContact",
            "company",
            "companyContact",
            "contact",
            "contactSegment",
            "segmentEmail"
          ],
          "default": "contact"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "send"
          ],
          "default": "send"
        },
        "name": {
          "description": "The name of the company to create",
          "type": "string",
          "default": ""
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "additionalFields": {
          "description": "A text describing details of Do Not Contact entry",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "companyId": {
          "description": "The ID of the company",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Contact parameters",
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
          "default": 30
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "email": {
          "description": "Email address of the contact",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "firstName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "lastName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "company": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "position": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "bodyJson": {
          "description": "Contact parameters",
          "type": "string",
          "default": ""
        },
        "contactId": {
          "description": "The ID of the contact",
          "type": "string",
          "default": ""
        },
        "action": {
          "description": "",
          "type": "string",
          "enum": [
            "add",
            "remove"
          ],
          "default": "add"
        },
        "channel": {
          "description": "",
          "type": "string",
          "enum": [
            "email",
            "sms"
          ],
          "default": "email"
        },
        "points": {
          "description": "",
          "type": "number",
          "default": 0
        },
        "options": {
          "description": "String or search command to filter entities by",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "campaignEmailId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": "",
          "format": "email"
        },
        "segmentId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "campaignId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "segmentEmailId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": "",
          "format": "email"
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
      "name": "mauticApi",
      "required": true
    },
    {
      "name": "mauticOAuth2Api",
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
