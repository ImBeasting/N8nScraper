---
title: "Node: Agile CRM"
slug: "node-agilecrm"
version: "1"
updated: "2025-11-13"
summary: "Consume Agile CRM API"
node_type: "regular"
group: "['transform']"
---

# Node: Agile CRM

**Purpose.** Consume Agile CRM API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:agilecrm.png`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **agileCrmApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **jsonNotice** when resource=['contact'], operation=['getAll'], filterType=['json']: See <a href="https://github.com/agilecrm/rest-api#121-get-contacts-by-dynamic-filter" target="_blank">Agile CRM guide</a> to creating filters
- **jsonNotice** when resource=['company'], operation=['getAll'], filterType=['json']: See <a href="https://github.com/agilecrm/rest-api#121-get-contacts-by-dynamic-filter" target="_blank">Agile CRM guide</a> to creating filters

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `agileCrmApi` | ✓ | - |

---

## Operations

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new contact |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact |
| Get Many | `getAll` | Get many contacts |
| Update | `update` | Update contact properties |

### Company Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new company |
| Delete | `delete` | Delete a company |
| Get | `get` | Get a company |
| Get Many | `getAll` | Get many companies |
| Update | `update` | Update company properties |

### Deal Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new deal |
| Delete | `delete` | Delete a deal |
| Get | `get` | Get a deal |
| Get Many | `getAll` | Get many deals |
| Update | `update` | Update deal properties |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✗ | Resource to operate on |  |

**Resource options:**

* **Company** (`company`)
* **Contact** (`contact`)
* **Deal** (`deal`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Create a new contact |  |

**Operation options:**

* **Create** (`create`) - Create a new contact
* **Delete** (`delete`) - Delete a contact
* **Get** (`get`) - Get a contact
* **Get Many** (`getAll`) - Get many contacts
* **Update** (`update`) - Update contact properties

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-contacts---companies-api">here</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Contacts address | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressOptions` | fixedCollection | {} | Contacts address |
| Company | `company` | string |  | Company Name |
| Email | `emailOptions` | fixedCollection | {} | Contact email |
| First Name | `firstName` | string |  | Contact first name |
| Last Name | `lastName` | string |  | Contact last name |
| Lead Score | `leadScore` | number |  | Lead score of contact |
| Star Value | `starValue` | options |  | Rating of contact (Max value 5). This is not applicable for companies. |
| Phone | `phoneOptions` | fixedCollection | {} | Contacts phone |
| Tags | `tags` | string | [] | Unique identifiers added to contact, for easy management of contacts. This is not applicable for companies. |
| Title | `title` | string |  | Professional title |
| Website | `websiteOptions` | fixedCollection | {} | Contacts websites |
| Custom Properties | `customProperties` | fixedCollection | {} | Property name |

</details>

| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-companys---companies-api">here</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Company address | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressOptions` | fixedCollection | {} | Company address |
| Email | `email` | string |  | Company email |
| Name | `name` | string |  | Company name |
| Phone | `phone` | string |  | Company phone |
| Star Value | `starValue` | options |  | Rating of company (Max value 5). This is not applicable for companies. |
| Tags | `tags` | string | [] | Unique identifiers added to company, for easy management of companys. This is not applicable for companies. |
| Website | `websiteOptions` | fixedCollection | {} | Companies websites |
| Custom Properties | `customProperties` | fixedCollection | {} | Property name |

</details>

| Close Date | `closeDate` | dateTime |  | ✓ | Closing date of deal |  |
| Expected Value | `expectedValue` | number | 1 | ✓ | Expected Value of deal | min:0, max:1000000000000 |
| Milestone | `milestone` | string |  | ✓ | Milestone of deal |  |
| Name | `name` | string |  | ✓ | Name of deal |  |
| Probability | `probability` | number | 50 | ✓ | Expected probability | min:0, max:100 |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-deals---companies-api">here</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Unique contact identifiers | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Contact IDs | `contactIds` | string | [] | Unique contact identifiers |
| Custom Data | `customData` | fixedCollection | {} | Property name |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | ID of contact to delete |  |
| Company ID | `companyId` | string |  | ✓ | ID of company to delete |  |
| Deal ID | `dealId` | string |  | ✓ | ID of deal to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | Unique identifier for a particular contact |  |
| Company ID | `companyId` | string |  | ✓ | Unique identifier for a particular company |  |
| Deal ID | `dealId` | string |  | ✓ | Unique identifier for a particular deal |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:∞ |
| Filter | `filterType` | options | none | ✗ |  |  |

**Filter options:**

* **None** (`none`)
* **Build Manually** (`manual`)
* **JSON** (`json`)

| Must Match | `matchType` | options | anyFilter | ✗ |  |  |

**Must Match options:**

* **Any Filter** (`anyFilter`)
* **All Filters** (`allFilters`)

| Simplify | `simple` | boolean | False | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Filters | `filters` | fixedCollection | {} | ✗ | Any searchable field | e.g. Add Condition |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conditions | `conditions` |  |  |  |

</details>

| Filters (JSON) | `filterJson` | string |  | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | The sorting direction | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort | `sort` | fixedCollection | [] | The sorting direction |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:∞ |
| Filter | `filterType` | options | none | ✗ |  |  |

**Filter options:**

* **None** (`none`)
* **Build Manually** (`manual`)
* **JSON** (`json`)

| Must Match | `matchType` | options | anyFilter | ✗ |  |  |

**Must Match options:**

* **Any Filter** (`anyFilter`)
* **All Filters** (`allFilters`)

| Simplify | `simple` | boolean | False | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Filters | `filters` | fixedCollection | {} | ✗ | Any searchable field | e.g. Add Condition |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conditions | `conditions` |  |  |  |

</details>

| Filters (JSON) | `filterJson` | string |  | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | The sorting direction | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort | `sort` | fixedCollection | [] | The sorting direction |

</details>

| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | Unique identifier for a particular contact |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-contacts---companies-api">here</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Contacts address | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressOptions` | fixedCollection | {} | Contacts address |
| Company | `company` | string |  | Company Name |
| Email | `emailOptions` | fixedCollection | {} | Contact email |
| First Name | `firstName` | string |  | Contact first name |
| Last Name | `lastName` | string |  | Contact last name |
| Lead Score | `leadScore` | number |  | Lead score of contact |
| Star Value | `starValue` | options |  | Rating of contact (Max value 5). This is not applicable for companies. |
| Phone | `phoneOptions` | fixedCollection | {} | Contacts phone |
| Tags | `tags` | string | [] | Unique identifiers added to contact, for easy management of contacts. This is not applicable for companies. |
| Title | `title` | string |  | Professional title |
| Website | `websiteOptions` | fixedCollection | {} | Contacts websites |
| Custom Properties | `customProperties` | fixedCollection | {} | Property name |

</details>

| Company ID | `companyId` | string |  | ✓ | Unique identifier for a particular company |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-companys---companies-api">here</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Company address | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressOptions` | fixedCollection | {} | Company address |
| Email | `email` | string |  | Company email |
| Star Value | `starValue` | options |  | Rating of company (Max value 5). This is not applicable for companies. |
| Tags | `tags` | string | [] | Unique identifiers added to company, for easy management of companys. This is not applicable for companies. |
| Name | `name` | string |  | Company name |
| Phone | `phone` | string |  | Company phone |
| Website | `websiteOptions` | fixedCollection | {} | Companys websites |
| Custom Properties | `customProperties` | fixedCollection | {} | Property name |

</details>

| Deal ID | `dealId` | string |  | ✓ | ID of deal to update |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-deals---companies-api">here</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Expected Value of deal | e.g. Add Field | min:0, max:10000 |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Expected Value | `expectedValue` | number |  | Expected Value of deal |
| Name | `name` | string |  | Name of deal |
| Probability | `probability` | number | 50 | Expected Value of deal |
| Contact IDs | `contactIds` | string | [] | Unique contact identifiers |
| Custom Data | `customData` | fixedCollection | {} | Property name |

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
node: agileCrm
displayName: Agile CRM
description: Consume Agile CRM API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: agileCrmApi
  required: true
operations:
- id: create
  name: Create
  description: Create a new contact
  params:
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id001
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - update
    typeInfo: &id002
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-contacts---companies-api">here</a>
    validation: &id003
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - update
          jsonParameters:
          - true
    typeInfo: &id004
      type: json
      displayName: Additional Fields
      name: additionalFieldsJson
      typeOptions:
        alwaysOpenEditWindow: true
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-companys---companies-api">here</a>
    validation: *id003
    typeInfo: *id004
  - id: closeDate
    name: Close Date
    type: dateTime
    default: ''
    required: true
    description: Closing date of deal
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: dateTime
      displayName: Close Date
      name: closeDate
  - id: expectedValue
    name: Expected Value
    type: number
    default: 1
    required: true
    description: Expected Value of deal
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: number
      displayName: Expected Value
      name: expectedValue
      typeOptions:
        minValue: 0
        maxValue: 1000000000000
  - id: milestone
    name: Milestone
    type: string
    default: ''
    required: true
    description: Milestone of deal
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: string
      displayName: Milestone
      name: milestone
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of deal
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: probability
    name: Probability
    type: number
    default: 50
    required: true
    description: Expected probability
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: number
      displayName: Probability
      name: probability
      typeOptions:
        minValue: 0
        maxValue: 100
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-deals---companies-api">here</a>
    validation: *id003
    typeInfo: *id004
- id: delete
  name: Delete
  description: Delete a contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of contact to delete
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - update
    typeInfo: &id006
      type: string
      displayName: Contact ID
      name: contactId
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: true
    description: ID of company to delete
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
  - id: dealId
    name: Deal ID
    type: string
    default: ''
    required: true
    description: ID of deal to delete
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Deal ID
      name: dealId
- id: get
  name: Get
  description: Get a contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Unique identifier for a particular contact
    validation: *id005
    typeInfo: *id006
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: true
    description: Unique identifier for a particular company
    validation: *id007
    typeInfo: *id008
  - id: dealId
    name: Deal ID
    type: string
    default: ''
    required: true
    description: Unique identifier for a particular deal
    validation: *id009
    typeInfo: *id010
- id: getAll
  name: Get Many
  description: Get many contacts
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
          - deal
          operation:
          - getAll
    typeInfo: &id012
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 20
    required: false
    description: Max number of results to return
    validation: &id013
      displayOptions:
        show:
          resource:
          - deal
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
  - id: filterType
    name: Filter
    type: options
    default: none
    required: false
    description: ''
    validation: &id015
      displayOptions:
        show:
          resource:
          - company
          operation:
          - getAll
    typeInfo: &id016
      type: options
      displayName: Filter
      name: filterType
      possibleValues:
      - value: none
        name: None
        description: ''
      - value: manual
        name: Build Manually
        description: ''
      - value: json
        name: JSON
        description: ''
  - id: matchType
    name: Must Match
    type: options
    default: anyFilter
    required: false
    description: ''
    validation: &id017
      displayOptions:
        show:
          resource:
          - company
          operation:
          - getAll
          filterType:
          - manual
    typeInfo: &id018
      type: options
      displayName: Must Match
      name: matchType
      possibleValues:
      - value: anyFilter
        name: Any Filter
        description: ''
      - value: allFilters
        name: All Filters
        description: ''
  - id: simple
    name: Simplify
    type: boolean
    default: false
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id019
      displayOptions:
        show:
          resource:
          - company
          operation:
          - getAll
    typeInfo: &id020
      type: boolean
      displayName: Simplify
      name: simple
  - id: filters
    name: Filters
    type: fixedCollection
    default: {}
    required: false
    description: Any searchable field
    placeholder: Add Condition
    validation: &id021
      displayOptions:
        show:
          resource:
          - company
          operation:
          - getAll
          filterType:
          - manual
    typeInfo: &id022
      type: fixedCollection
      displayName: Filters
      name: filters
      typeOptions:
        multipleValues: true
      subProperties:
      - name: conditions
        displayName: Conditions
        values:
        - displayName: Field
          name: field
          type: string
          description: Any searchable field
          default: ''
        - displayName: Condition Type
          name: condition_type
          type: options
          value: AFTER
          default: EQUALS
          options:
          - name: After
            value: AFTER
            displayName: After
          - name: Before
            value: BEFORE
            displayName: Before
          - name: Between
            value: BETWEEN
            displayName: Between
          - name: Equals
            value: EQUALS
            displayName: Equals
          - name: Last
            value: LAST
            displayName: Last
          - name: Not Equal
            value: NOTEQUALS
            displayName: Not Equal
          - name: 'On'
            value: 'ON'
            displayName: 'On'
        - displayName: Value
          name: value
          type: string
          default: ''
        - displayName: Value 2
          name: value2
          type: string
          default: ''
          displayOptions:
            show:
              condition_type:
              - BETWEEN
  - id: filterJson
    name: Filters (JSON)
    type: string
    default: ''
    required: false
    description: ''
    validation: &id023
      displayOptions:
        show:
          resource:
          - company
          operation:
          - getAll
          filterType:
          - json
    typeInfo: &id024
      type: string
      displayName: Filters (JSON)
      name: filterJson
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
    default: 20
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: filterType
    name: Filter
    type: options
    default: none
    required: false
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: matchType
    name: Must Match
    type: options
    default: anyFilter
    required: false
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: simple
    name: Simplify
    type: boolean
    default: false
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id019
    typeInfo: *id020
  - id: filters
    name: Filters
    type: fixedCollection
    default: {}
    required: false
    description: Any searchable field
    placeholder: Add Condition
    validation: *id021
    typeInfo: *id022
  - id: filterJson
    name: Filters (JSON)
    type: string
    default: ''
    required: false
    description: ''
    validation: *id023
    typeInfo: *id024
  - id: limit
    name: Limit
    type: number
    default: 20
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
- id: update
  name: Update
  description: Update contact properties
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Unique identifier for a particular contact
    validation: *id005
    typeInfo: *id006
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-contacts---companies-api">here</a>
    validation: *id003
    typeInfo: *id004
  - id: companyId
    name: Company ID
    type: string
    default: ''
    required: true
    description: Unique identifier for a particular company
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
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-companys---companies-api">here</a>
    validation: *id003
    typeInfo: *id004
  - id: dealId
    name: Deal ID
    type: string
    default: ''
    required: true
    description: ID of deal to update
    validation: *id009
    typeInfo: *id010
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-deals---companies-api">here</a>
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
  notices:
  - name: jsonNotice
    text: See <a href="https://github.com/agilecrm/rest-api#121-get-contacts-by-dynamic-filter"
      target="_blank">Agile CRM guide</a> to creating filters
    conditions:
      show:
        resource:
        - contact
        operation:
        - getAll
        filterType:
        - json
  - name: jsonNotice
    text: See <a href="https://github.com/agilecrm/rest-api#121-get-contacts-by-dynamic-filter"
      target="_blank">Agile CRM guide</a> to creating filters
    conditions:
      show:
        resource:
        - company
        operation:
        - getAll
        filterType:
        - json
  tooltips: []
  placeholders:
  - field: filters
    text: Add Condition
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Condition
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/agileCrm.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Agile CRM Node",
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
            "company",
            "contact",
            "deal"
          ],
          "default": "contact"
        },
        "operation": {
          "description": "Create a new deal",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "get"
        },
        "contactId": {
          "description": "Unique identifier for a particular contact",
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
          "default": 20
        },
        "filterType": {
          "description": "",
          "type": "string",
          "enum": [
            "none",
            "manual",
            "json"
          ],
          "default": "none"
        },
        "matchType": {
          "description": "",
          "type": "string",
          "enum": [
            "anyFilter",
            "allFilters"
          ],
          "default": "anyFilter"
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": false
        },
        "filters": {
          "description": "Any searchable field",
          "type": "string",
          "default": {},
          "examples": [
            "Add Condition"
          ]
        },
        "filterJson": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "The sorting direction",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "additionalFieldsJson": {
          "description": "Object of values to set as described <a href=\"https://github.com/agilecrm/rest-api#1-deals---companies-api\">here</a>",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Expected Value of deal",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "companyId": {
          "description": "Unique identifier for a particular company",
          "type": "string",
          "default": ""
        },
        "dealId": {
          "description": "ID of deal to update",
          "type": "string",
          "default": ""
        },
        "closeDate": {
          "description": "Closing date of deal",
          "type": "string",
          "default": ""
        },
        "expectedValue": {
          "description": "Expected Value of deal",
          "type": "number",
          "default": 1
        },
        "milestone": {
          "description": "Milestone of deal",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "Name of deal",
          "type": "string",
          "default": ""
        },
        "probability": {
          "description": "Expected probability",
          "type": "number",
          "default": 50
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
      "name": "agileCrmApi",
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
