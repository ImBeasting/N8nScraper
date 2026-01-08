---
title: "Node: Intercom"
slug: "node-intercom"
version: "1"
updated: "2026-01-08"
summary: "Consume Intercom API"
node_type: "regular"
group: "['output']"
---

# Node: Intercom

**Purpose.** Consume Intercom API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:intercom.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **intercomApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `intercomApi` | ✓ | - |

---

## Operations

### Lead Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new lead |
| Delete | `delete` | Delete a lead |
| Get | `get` | Get data of a lead |
| Get Many | `getAll` | Get data of many leads |
| Update | `update` | Update new lead |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new user |
| Delete | `delete` | Delete a user |
| Get | `get` | Get data of a user |
| Get Many | `getAll` | Get data of many users |
| Update | `update` | Update a user |

### Company Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new company |
| Get | `get` | Get data of a company |
| Get Many | `getAll` | Get data of many companies |
| Update | `update` | Update a company |
| Users | `users` | List company's users |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | user | ✗ | Companies allow you to represent commercial organizations using your product |  |

**Resource options:**

* **Company** (`company`) - Companies allow you to represent commercial organizations using your product
* **Lead** (`lead`) - Leads are useful for representing logged-out users of your application
* **User** (`user`) - The Users resource is the primary way of interacting with Intercom

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a new lead |  |

**Operation options:**

* **Create** (`create`) - Create a new lead
* **Delete** (`delete`) - Delete a lead
* **Get** (`get`) - Get data of a lead
* **Get Many** (`getAll`) - Get data of many leads
* **Update** (`update`) - Update new lead

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Identifier Type | `identifierType` | options |  | ✗ | A unique string identifier for the user. It is required on creation if an email is not supplied. |  |

**Identifier Type options:**

* **User ID** (`userId`) - A unique string identifier for the user. It is required on creation if an email is not supplied.
* **Email** (`email`) - The user's email address. It is required on creation if a user_id is not supplied.

| Value | `idValue` | string |  | ✓ | Unique string identifier value |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | An avatar image URL. note: the image URL needs to be https. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Avatar | `avatar` | string |  | An avatar image URL. note: the image URL needs to be https. |
| Company Names or IDs | `companies` | multiOptions | [] | Identifies the companies this user belongs to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Email | `email` | string |  | Email of the user |
| Name | `name` | string |  | Name of the user |
| Phone | `phone` | string |  | The phone number of the user |
| Session Count | `sessionCount` | number | False | How many sessions the user has recorded |
| User ID | `userId` | string |  | Email of the user |
| Unsubscribed From Emails | `unsubscribedFromEmails` | boolean | False | Whether the user is unsubscribed from emails |
| Update Last Request At | `updateLastRequestAt` | boolean | False | Whether to instruct Intercom to update the users last_request_at value to the current API service time in UTC |
| UTM Campaign | `utmCampaign` | string |  | Identifies a specific product promotion or strategic campaign |
| UTM Content | `utmContent` | string |  | Identifies what specifically was clicked to bring the user to the site |
| UTM Medium | `utmMedium` | string |  | Identifies what type of link was used |
| UTM Source | `utmSource` | string |  | An avatar image URL. note: the image URL needs to be https. |
| UTM Term | `utmTerm` | string |  | Identifies search terms |

</details>

| Custom Attributes | `customAttributesJson` | json |  | ✗ | A hash of key/value pairs to represent custom data you want to attribute to a user |  |
| Custom Attributes | `customAttributesUi` | fixedCollection | {} | ✗ | A hash of key/value pairs to represent custom data you want to attribute to a user | e.g. Add Attribute |  |

<details>
<summary><strong>Custom Attributes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attributes | `customAttributesValues` |  |  |  |

</details>

| Email | `email` | string |  | ✓ | The email of the user | e.g. name@email.com | email |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | An avatar image URL. note: the image URL needs to be https. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Avatar | `avatar` | string |  | An avatar image URL. note: the image URL needs to be https. |
| Company Names or IDs | `companies` | multiOptions | [] | Identifies the companies this user belongs to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Email | `email` | string |  | The email of the user |
| Name | `name` | string |  | Name of the user |
| Phone | `phone` | string |  | The phone number of the user |
| Unsubscribed From Emails | `unsubscribedFromEmails` | boolean | False | Whether the Lead is unsubscribed from emails |
| Update Last Request At | `updateLastRequestAt` | boolean | False | Whether to instruct Intercom to update the users last_request_at value to the current API service time in UTC. default value if not sent is false. |
| UTM Campaign | `utmCampaign` | string |  | Identifies a specific product promotion or strategic campaign |
| UTM Content | `utmContent` | string |  | Identifies what specifically was clicked to bring the user to the site |
| UTM Medium | `utmMedium` | string |  | Identifies what type of link was used |
| UTM Source | `utmSource` | string |  | An avatar image URL. note: the image URL needs to be https. |
| UTM Term | `utmTerm` | string |  | Identifies search terms |

</details>

| Custom Attributes | `customAttributesJson` | json |  | ✗ | A hash of key/value pairs to represent custom data you want to attribute to a user |  |
| Custom Attributes | `customAttributesUi` | fixedCollection | {} | ✗ | A hash of key/value pairs to represent custom data you want to attribute to a user | e.g. Add Attribute |  |

<details>
<summary><strong>Custom Attributes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attributes | `customAttributesValues` |  |  |  |

</details>

| Company ID | `companyId` | string |  | ✗ | The company ID you have defined for the company |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The industry that this company operates in | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Industry | `industry` | string |  | The industry that this company operates in |
| Monthly Spend | `monthlySpend` | string |  | The phone number of the user |
| Name | `name` | string |  | Name of the user |
| Plan | `plan` | string |  | The name of the plan you have associated with the company |
| Size | `size` | number |  | The number of employees in this company |
| Website | `website` | string |  | The URL for this company's website. Please note that the value specified here is not validated. Accepts any string. |

</details>

| Custom Attributes | `customAttributesJson` | json |  | ✗ | A hash of key/value pairs to represent custom data you want to attribute to a user |  |
| Custom Attributes | `customAttributesUi` | fixedCollection | {} | ✗ | A hash of key/value pairs to represent custom data you want to attribute to a user | e.g. Add Attribute |  |

<details>
<summary><strong>Custom Attributes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attributes | `customAttributesValues` |  |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The Intercom defined ID representing the Lead |  |
| Delete By | `deleteBy` | options |  | ✗ | The Intercom defined ID representing the Lead |  |

**Delete By options:**

* **ID** (`id`) - The Intercom defined ID representing the Lead
* **User ID** (`userId`) - Automatically generated identifier for the Lead

| Value | `value` | string |  | ✓ | Delete by value |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Select By | `selectBy` | options |  | ✗ | The Intercom defined ID representing the Lead |  |

**Select By options:**

* **ID** (`id`) - The Intercom defined ID representing the Lead
* **User ID** (`userId`) - Automatically generated identifier for the Lead

| Value | `value` | string |  | ✓ | View by value |  |
| Select By | `selectBy` | options |  | ✗ | Email representing the Lead |  |

**Select By options:**

* **Email** (`email`) - Email representing the Lead
* **ID** (`id`) - The Intercom defined ID representing the Lead
* **User ID** (`userId`) - Automatically generated identifier for the Lead
* **Phone** (`phone`) - Phone representing the Lead

| Value | `value` | string |  | ✓ | View by value |  |
| Select By | `selectBy` | options |  | ✗ | The company_id you have given to the company |  |

**Select By options:**

* **Company ID** (`companyId`) - The company_id you have given to the company
* **ID** (`id`) - The Intercom defined ID representing the company
* **Name** (`name`) - The name of the company

| Value | `value` | string |  | ✓ | View by value |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:60 |
| Filters | `filters` | collection | {} | ✗ | Company ID representing the user | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company ID | `company_id` | string |  | Company ID representing the user |
| Email | `email` | string |  | The email address of the user |
| Segment ID | `segment_id` | string |  | Segment representing the user |
| Tag ID | `tag_id` | string |  | Tag representing the user |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:60 |
| Filters | `filters` | collection | {} | ✗ | The email address of the lead | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  | The email address of the lead |
| Phone | `phone` | string |  | The phone number of the lead |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:60 |
| Filters | `filters` | collection | {} | ✗ | Segment representing the Lead | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Segment ID | `segment_id` | string |  | Segment representing the Lead |
| Tag ID | `tag_id` | string |  | Tag representing the Lead |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Update By | `updateBy` | options | id | ✗ | The Intercom defined ID representing the user |  |

**Update By options:**

* **ID** (`id`) - The Intercom defined ID representing the user
* **Email** (`email`) - The email address of user
* **User ID** (`userId`) - Automatically generated identifier for the user

| Value | `value` | string |  | ✓ | Value of the property to identify the user to update |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | An avatar image URL. note: the image URL needs to be https. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Avatar | `avatar` | string |  | An avatar image URL. note: the image URL needs to be https. |
| Company Names or IDs | `companies` | multiOptions | [] | Identifies the companies this user belongs to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Email | `email` | string |  | Email of the user |
| Name | `name` | string |  | Name of the user |
| Phone | `phone` | string |  | The phone number of the user |
| Session Count | `sessionCount` | number | False | How many sessions the user has recorded |
| User ID | `userId` | string |  | Email of the user |
| Unsubscribed From Emails | `unsubscribedFromEmails` | boolean | False | Whether the user is unsubscribed from emails |
| Update Last Request At | `updateLastRequestAt` | boolean | False | Whether to instruct Intercom to update the users last_request_at value to the current API service time in UTC |
| UTM Campaign | `utmCampaign` | string |  | Identifies a specific product promotion or strategic campaign |
| UTM Content | `utmContent` | string |  | Identifies what specifically was clicked to bring the user to the site |
| UTM Medium | `utmMedium` | string |  | Identifies what type of link was used |
| UTM Source | `utmSource` | string |  | An avatar image URL. note: the image URL needs to be https. |
| UTM Term | `utmTerm` | string |  | Identifies search terms |

</details>

| Custom Attributes | `customAttributesJson` | json |  | ✗ | A hash of key/value pairs to represent custom data you want to attribute to a user |  |
| Custom Attributes | `customAttributesUi` | fixedCollection | {} | ✗ | A hash of key/value pairs to represent custom data you want to attribute to a user | e.g. Add Attribute |  |

<details>
<summary><strong>Custom Attributes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attributes | `customAttributesValues` |  |  |  |

</details>

| Update By | `updateBy` | options | id | ✗ | Automatically generated identifier for the Lead |  |

**Update By options:**

* **User ID** (`userId`) - Automatically generated identifier for the Lead
* **ID** (`id`) - The Intercom defined ID representing the Lead

| Value | `value` | string |  | ✓ | Value of the property to identify the lead to update |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | An avatar image URL. note: the image URL needs to be https. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Avatar | `avatar` | string |  | An avatar image URL. note: the image URL needs to be https. |
| Company Names or IDs | `companies` | multiOptions | [] | Identifies the companies this user belongs to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Email | `email` | string |  | The email of the user |
| Name | `name` | string |  | Name of the user |
| Phone | `phone` | string |  | The phone number of the user |
| Unsubscribed From Emails | `unsubscribedFromEmails` | boolean | False | Whether the Lead is unsubscribed from emails |
| Update Last Request At | `updateLastRequestAt` | boolean | False | Whether to instruct Intercom to update the users last_request_at value to the current API service time in UTC. default value if not sent is false. |
| UTM Campaign | `utmCampaign` | string |  | Identifies a specific product promotion or strategic campaign |
| UTM Content | `utmContent` | string |  | Identifies what specifically was clicked to bring the user to the site |
| UTM Medium | `utmMedium` | string |  | Identifies what type of link was used |
| UTM Source | `utmSource` | string |  | An avatar image URL. note: the image URL needs to be https. |
| UTM Term | `utmTerm` | string |  | Identifies search terms |

</details>

| Custom Attributes | `customAttributesJson` | json |  | ✗ | A hash of key/value pairs to represent custom data you want to attribute to a user |  |
| Custom Attributes | `customAttributesUi` | fixedCollection | {} | ✗ | A hash of key/value pairs to represent custom data you want to attribute to a user | e.g. Add Attribute |  |

<details>
<summary><strong>Custom Attributes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attributes | `customAttributesValues` |  |  |  |

</details>

| Company ID | `companyId` | string |  | ✗ | The company ID you have defined for the company |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The industry that this company operates in | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Industry | `industry` | string |  | The industry that this company operates in |
| Monthly Spend | `monthlySpend` | string |  | The phone number of the user |
| Name | `name` | string |  | Name of the user |
| Plan | `plan` | string |  | The name of the plan you have associated with the company |
| Size | `size` | number |  | The number of employees in this company |
| Website | `website` | string |  | The URL for this company's website. Please note that the value specified here is not validated. Accepts any string. |

</details>

| Custom Attributes | `customAttributesJson` | json |  | ✗ | A hash of key/value pairs to represent custom data you want to attribute to a user |  |
| Custom Attributes | `customAttributesUi` | fixedCollection | {} | ✗ | A hash of key/value pairs to represent custom data you want to attribute to a user | e.g. Add Attribute |  |

<details>
<summary><strong>Custom Attributes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attributes | `customAttributesValues` |  |  |  |

</details>


### Users parameters (`users`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List By | `listBy` | options |  | ✗ | The Intercom defined ID representing the company |  |

**List By options:**

* **ID** (`id`) - The Intercom defined ID representing the company
* **Company ID** (`companyId`) - The company_id you have given to the company

| Value | `value` | string |  | ✓ | View by value |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:60 |

---

## Load Options Methods

- `getCompanies`

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
* Categories: Communication, Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: intercom
displayName: Intercom
description: Consume Intercom API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: intercomApi
  required: true
operations:
- id: create
  name: Create
  description: Create a new lead
  params:
  - id: identifierType
    name: Identifier Type
    type: options
    default: ''
    required: false
    description: A unique string identifier for the user. It is required on creation
      if an email is not supplied.
    validation:
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: options
      displayName: Identifier Type
      name: identifierType
      possibleValues:
      - value: userId
        name: User ID
        description: A unique string identifier for the user. It is required on creation
          if an email is not supplied.
      - value: email
        name: Email
        description: The user's email address. It is required on creation if a user_id
          is not supplied.
  - id: idValue
    name: Value
    type: string
    default: ''
    required: true
    description: Unique string identifier value
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
      displayName: Value
      name: idValue
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id001
      displayOptions:
        show:
          operation:
          - create
          - update
          resource:
          - company
    typeInfo: &id002
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: customAttributesJson
    name: Custom Attributes
    type: json
    default: ''
    required: false
    description: A hash of key/value pairs to represent custom data you want to attribute
      to a user
    validation: &id003
      displayOptions:
        show:
          resource:
          - company
          operation:
          - create
          - update
          jsonParameters:
          - true
    typeInfo: &id004
      type: json
      displayName: Custom Attributes
      name: customAttributesJson
      typeOptions:
        alwaysOpenEditWindow: true
  - id: customAttributesUi
    name: Custom Attributes
    type: fixedCollection
    default: &id015 {}
    required: false
    description: A hash of key/value pairs to represent custom data you want to attribute
      to a user
    placeholder: Add Attribute
    validation: &id005
      displayOptions:
        show:
          resource:
          - company
          operation:
          - create
          - update
          jsonParameters:
          - false
    typeInfo: &id006
      type: fixedCollection
      displayName: Custom Attributes
      name: customAttributesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: customAttributesValues
        displayName: Attributes
        values:
        - displayName: Name
          name: name
          type: string
          default: ''
        - displayName: Value
          name: value
          type: string
          default: ''
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email of the user
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - create
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: customAttributesJson
    name: Custom Attributes
    type: json
    default: ''
    required: false
    description: A hash of key/value pairs to represent custom data you want to attribute
      to a user
    validation: *id003
    typeInfo: *id004
  - id: customAttributesUi
    name: Custom Attributes
    type: fixedCollection
    default: &id018 {}
    required: false
    description: A hash of key/value pairs to represent custom data you want to attribute
      to a user
    placeholder: Add Attribute
    validation: *id005
    typeInfo: *id006
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: false
    description: The company ID you have defined for the company
    validation: &id019
      displayOptions:
        show:
          resource:
          - company
          operation:
          - create
          - update
    typeInfo: &id020
      type: string
      displayName: Company ID
      name: companyId
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: customAttributesJson
    name: Custom Attributes
    type: json
    default: ''
    required: false
    description: A hash of key/value pairs to represent custom data you want to attribute
      to a user
    validation: *id003
    typeInfo: *id004
  - id: customAttributesUi
    name: Custom Attributes
    type: fixedCollection
    default: &id021 {}
    required: false
    description: A hash of key/value pairs to represent custom data you want to attribute
      to a user
    placeholder: Add Attribute
    validation: *id005
    typeInfo: *id006
- id: delete
  name: Delete
  description: Delete a lead
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The Intercom defined ID representing the Lead
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - delete
    typeInfo:
      type: string
      displayName: ID
      name: id
  - id: deleteBy
    name: Delete By
    type: options
    default: ''
    required: false
    description: The Intercom defined ID representing the Lead
    validation:
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - delete
    typeInfo:
      type: options
      displayName: Delete By
      name: deleteBy
      possibleValues:
      - value: id
        name: ID
        description: The Intercom defined ID representing the Lead
      - value: userId
        name: User ID
        description: Automatically generated identifier for the Lead
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: Delete by value
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - company
          operation:
          - get
    typeInfo: &id008
      type: string
      displayName: Value
      name: value
- id: get
  name: Get
  description: Get data of a lead
  params:
  - id: selectBy
    name: Select By
    type: options
    default: ''
    required: false
    description: The Intercom defined ID representing the Lead
    validation: &id009
      displayOptions:
        show:
          resource:
          - company
          operation:
          - get
    typeInfo: &id010
      type: options
      displayName: Select By
      name: selectBy
      possibleValues:
      - value: companyId
        name: Company ID
        description: The company_id you have given to the company
      - value: id
        name: ID
        description: The Intercom defined ID representing the company
      - value: name
        name: Name
        description: The name of the company
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: View by value
    validation: *id007
    typeInfo: *id008
  - id: selectBy
    name: Select By
    type: options
    default: ''
    required: false
    description: Email representing the Lead
    validation: *id009
    typeInfo: *id010
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: View by value
    validation: *id007
    typeInfo: *id008
  - id: selectBy
    name: Select By
    type: options
    default: ''
    required: false
    description: The company_id you have given to the company
    validation: *id009
    typeInfo: *id010
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: View by value
    validation: *id007
    typeInfo: *id008
- id: getAll
  name: Get Many
  description: Get data of many leads
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id011
      displayOptions:
        show:
          resource:
          - company
          operation:
          - getAll
    typeInfo: &id012
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id013
      displayOptions:
        show:
          resource:
          - company
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id014
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 60
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
- id: update
  name: Update
  description: Update new lead
  params:
  - id: updateBy
    name: Update By
    type: options
    default: id
    required: false
    description: The Intercom defined ID representing the user
    validation: &id016
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - update
    typeInfo: &id017
      type: options
      displayName: Update By
      name: updateBy
      possibleValues:
      - value: userId
        name: User ID
        description: Automatically generated identifier for the Lead
      - value: id
        name: ID
        description: The Intercom defined ID representing the Lead
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: Value of the property to identify the user to update
    validation: *id007
    typeInfo: *id008
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: customAttributesJson
    name: Custom Attributes
    type: json
    default: ''
    required: false
    description: A hash of key/value pairs to represent custom data you want to attribute
      to a user
    validation: *id003
    typeInfo: *id004
  - id: customAttributesUi
    name: Custom Attributes
    type: fixedCollection
    default: *id015
    required: false
    description: A hash of key/value pairs to represent custom data you want to attribute
      to a user
    placeholder: Add Attribute
    validation: *id005
    typeInfo: *id006
  - id: updateBy
    name: Update By
    type: options
    default: id
    required: false
    description: Automatically generated identifier for the Lead
    validation: *id016
    typeInfo: *id017
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: Value of the property to identify the lead to update
    validation: *id007
    typeInfo: *id008
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: customAttributesJson
    name: Custom Attributes
    type: json
    default: ''
    required: false
    description: A hash of key/value pairs to represent custom data you want to attribute
      to a user
    validation: *id003
    typeInfo: *id004
  - id: customAttributesUi
    name: Custom Attributes
    type: fixedCollection
    default: *id018
    required: false
    description: A hash of key/value pairs to represent custom data you want to attribute
      to a user
    placeholder: Add Attribute
    validation: *id005
    typeInfo: *id006
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: false
    description: The company ID you have defined for the company
    validation: *id019
    typeInfo: *id020
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: customAttributesJson
    name: Custom Attributes
    type: json
    default: ''
    required: false
    description: A hash of key/value pairs to represent custom data you want to attribute
      to a user
    validation: *id003
    typeInfo: *id004
  - id: customAttributesUi
    name: Custom Attributes
    type: fixedCollection
    default: *id021
    required: false
    description: A hash of key/value pairs to represent custom data you want to attribute
      to a user
    placeholder: Add Attribute
    validation: *id005
    typeInfo: *id006
- id: users
  name: Users
  description: List company's users
  params:
  - id: listBy
    name: List By
    type: options
    default: ''
    required: false
    description: The Intercom defined ID representing the company
    validation:
      displayOptions:
        show:
          resource:
          - company
          operation:
          - users
    typeInfo:
      type: options
      displayName: List By
      name: listBy
      possibleValues:
      - value: id
        name: ID
        description: The Intercom defined ID representing the company
      - value: companyId
        name: Company ID
        description: The company_id you have given to the company
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: View by value
    validation: *id007
    typeInfo: *id008
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
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
  - field: filters
    text: Add Filter
  - field: additionalFields
    text: Add Field
  - field: customAttributesUi
    text: Add Attribute
  - field: filters
    text: Add Filter
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: customAttributesUi
    text: Add Attribute
  - field: filters
    text: Add Filter
  - field: additionalFields
    text: Add Field
  - field: customAttributesUi
    text: Add Attribute
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
  "$id": "https://n8n.io/schemas/nodes/intercom.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Intercom Node",
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
        "users"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Companies allow you to represent commercial organizations using your product",
          "type": "string",
          "enum": [
            "company",
            "lead",
            "user"
          ],
          "default": "user"
        },
        "operation": {
          "description": "Create a new company",
          "type": "string",
          "enum": [
            "create",
            "get",
            "getAll",
            "update",
            "users"
          ],
          "default": "create"
        },
        "id": {
          "description": "The Intercom defined ID representing the Lead",
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
          "default": 50
        },
        "filters": {
          "description": "Segment representing the Lead",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "selectBy": {
          "description": "The company_id you have given to the company",
          "type": "string",
          "enum": [
            "companyId",
            "id",
            "name"
          ],
          "default": ""
        },
        "value": {
          "description": "View by value",
          "type": "string",
          "default": ""
        },
        "updateBy": {
          "description": "Automatically generated identifier for the Lead",
          "type": "string",
          "enum": [
            "userId",
            "id"
          ],
          "default": "id"
        },
        "identifierType": {
          "description": "A unique string identifier for the user. It is required on creation if an email is not supplied.",
          "type": "string",
          "enum": [
            "userId",
            "email"
          ],
          "default": ""
        },
        "idValue": {
          "description": "Unique string identifier value",
          "type": "string",
          "default": ""
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "additionalFields": {
          "description": "The industry that this company operates in",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "customAttributesJson": {
          "description": "A hash of key/value pairs to represent custom data you want to attribute to a user",
          "type": "string",
          "default": ""
        },
        "customAttributesUi": {
          "description": "A hash of key/value pairs to represent custom data you want to attribute to a user",
          "type": "string",
          "default": {},
          "examples": [
            "Add Attribute"
          ]
        },
        "deleteBy": {
          "description": "The Intercom defined ID representing the Lead",
          "type": "string",
          "enum": [
            "id",
            "userId"
          ],
          "default": ""
        },
        "email": {
          "description": "The email of the user",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "listBy": {
          "description": "The Intercom defined ID representing the company",
          "type": "string",
          "enum": [
            "id",
            "companyId"
          ],
          "default": ""
        },
        "companyId": {
          "description": "The company ID you have defined for the company",
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
      "name": "intercomApi",
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
