---
title: "Node: Google Contacts"
slug: "node-googlecontacts"
version: "1"
updated: "2025-11-13"
summary: "Consume Google Contacts API"
node_type: "regular"
group: "['input']"
---

# Node: Google Contacts

**Purpose.** Consume Google Contacts API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:googleContacts.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleContactsOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleContactsOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a contact |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact |
| Get Many | `getAll` | Retrieve many contacts |
| Update | `update` | Update a contact |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✗ | Resource to operate on |  |

**Resource options:**

* **Contact** (`contact`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a contact |  |

**Operation options:**

* **Create** (`create`) - Create a contact
* **Delete** (`delete`) - Delete a contact
* **Get** (`get`) - Get a contact
* **Get Many** (`getAll`) - Retrieve many contacts
* **Update** (`update`) - Update a contact

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Family Name | `familyName` | string |  | ✗ |  |  |
| Given Name | `givenName` | string |  | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The end user specified key of the user defined data | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Addresses | `addressesUi` | fixedCollection | {} |  |
| Birthday | `birthday` | dateTime |  |  |
| Company | `companyUi` | fixedCollection | {} |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | The end user specified key of the user defined data |
| Emails | `emailsUi` | fixedCollection | {} | The type of the email address. The type can be custom or one of these predefined values. |
| Events | `eventsUi` | fixedCollection | {} | An event related to the person |
| File As | `fileAs` | string |  | The name that should be used to sort the person in a list |
| Group Names or IDs | `group` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Honorific Prefix | `honorificPrefix` | string |  |  |
| Honorific Suffix | `honorificSuffix` | string |  |  |
| Middle Name | `middleName` | string |  |  |
| Notes | `biographies` | string |  |  |
| Phone | `phoneUi` | fixedCollection | {} | The phone number |
| Relations | `relationsUi` | fixedCollection | {} | The name of the other person this relation refers to |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Fields | `fields` | multiOptions | [] | ✗ | A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. |  |

**Fields options:**

* ***** (`*`)
* **Addresses** (`addresses`)
* **Biographies** (`biographies`)
* **Birthdays** (`birthdays`)
* **Cover Photos** (`coverPhotos`)
* **Email Addresses** (`emailAddresses`)
* **Events** (`events`)
* **Genders** (`genders`)
* **IM Clients** (`imClients`)
* **Interests** (`interests`)
* **Locales** (`locales`)
* **Memberships** (`memberships`)
* **Metadata** (`metadata`)
* **Names** (`names`)
* **Nicknames** (`nicknames`)
* **Occupations** (`occupations`)
* **Organizations** (`organizations`)
* **Phone Numbers** (`phoneNumbers`)
* **Photos** (`photos`)
* **Relations** (`relations`)
* **Residences** (`residences`)
* **Sip Addresses** (`sipAddresses`)
* **Skills** (`skills`)
* **URLs** (`urls`)
* **User Defined** (`userDefined`)

| RAW Data | `rawData` | boolean | False | ✗ | Whether to return the data exactly in the way it got received from the API |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Fields | `fields` | multiOptions | [] | ✗ | A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. |  |

**Fields options:**

* ***** (`*`)
* **Addresses** (`addresses`)
* **Biographies** (`biographies`)
* **Birthdays** (`birthdays`)
* **Cover Photos** (`coverPhotos`)
* **Email Addresses** (`emailAddresses`)
* **Events** (`events`)
* **Genders** (`genders`)
* **IM Clients** (`imClients`)
* **Interests** (`interests`)
* **Locales** (`locales`)
* **Memberships** (`memberships`)
* **Metadata** (`metadata`)
* **Names** (`names`)
* **Nicknames** (`nicknames`)
* **Occupations** (`occupations`)
* **Organizations** (`organizations`)
* **Phone Numbers** (`phoneNumbers`)
* **Photos** (`photos`)
* **Relations** (`relations`)
* **Residences** (`residences`)
* **Sip Addresses** (`sipAddresses`)
* **Skills** (`skills`)
* **URLs** (`urls`)
* **User Defined** (`userDefined`)

| Use Query | `useQuery` | boolean | False | ✗ | Whether or not to use a query to filter the results |  |
| Query | `query` | string |  | ✗ | The plain-text query for the request. The query is used to match prefix phrases of the fields on a person. For example, a person with name "foo name" matches queries such as "f", "fo", "foo", "foo n", "nam", etc., but not "oo n". |  |
| RAW Data | `rawData` | boolean | False | ✗ | Whether to return the data exactly in the way it got received from the API |  |
| Options | `options` | collection | {} | ✗ | Sort people by when they were changed; older entries first | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort Order | `sortOrder` | options |  | Sort people by when they were changed; older entries first |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Fields | `fields` | multiOptions | [] | ✗ | A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. |  |

**Fields options:**

* ***** (`*`)
* **Addresses** (`addresses`)
* **Biographies** (`biographies`)
* **Birthdays** (`birthdays`)
* **Cover Photos** (`coverPhotos`)
* **Email Addresses** (`emailAddresses`)
* **Events** (`events`)
* **Genders** (`genders`)
* **IM Clients** (`imClients`)
* **Interests** (`interests`)
* **Locales** (`locales`)
* **Memberships** (`memberships`)
* **Metadata** (`metadata`)
* **Names** (`names`)
* **Nicknames** (`nicknames`)
* **Occupations** (`occupations`)
* **Organizations** (`organizations`)
* **Phone Numbers** (`phoneNumbers`)
* **Photos** (`photos`)
* **Relations** (`relations`)
* **Residences** (`residences`)
* **Sip Addresses** (`sipAddresses`)
* **Skills** (`skills`)
* **URLs** (`urls`)
* **User Defined** (`userDefined`)

| Update Fields | `updateFields` | collection | {} | ✗ | The etag field in the person is nedded to make sure the contact has not changed since your last read | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Etag | `etag` | string |  | The etag field in the person is nedded to make sure the contact has not changed since your last read |
| Family Name | `familyName` | string |  |  |
| Given Name | `givenName` | string |  |  |
| Addresses | `addressesUi` | fixedCollection | {} |  |
| Birthday | `birthday` | dateTime |  |  |
| Company | `companyUi` | fixedCollection | {} |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | The end user specified key of the user defined data |
| Emails | `emailsUi` | fixedCollection | {} | The type of the email address. The type can be custom or one of these predefined values. |
| Events | `eventsUi` | fixedCollection | {} | An event related to the person |
| File As | `fileAs` | string |  | The name that should be used to sort the person in a list |
| Group Names or IDs | `group` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Honorific Prefix | `honorificPrefix` | string |  |  |
| Honorific Suffix | `honorificSuffix` | string |  |  |
| Middle Name | `middleName` | string |  |  |
| Notes | `biographies` | string |  |  |
| Phone | `phoneUi` | fixedCollection | {} | The phone number |
| Relations | `relationsUi` | fixedCollection | {} | The name of the other person this relation refers to |

</details>


---

## Load Options Methods

- `getGroups`
- `for`
- `name`
- `value`

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Get Contact All Fields

**From workflow:** Google Contacts Get All Fields Test

**Parameters:**
```json
{
  "resource": "contact",
  "operation": "get",
  "contactId": "c123456789",
  "fields": [
    "*"
  ],
  "rawData": false
}
```

**Credentials:**
- googleContactsOAuth2Api: `Test Google Contacts OAuth2`

### Example 2: Get All Contacts Limit

**From workflow:** Google Contacts Get All Limit Test

**Parameters:**
```json
{
  "resource": "contact",
  "operation": "getAll",
  "returnAll": false,
  "limit": 1,
  "fields": [
    "names"
  ],
  "useQuery": false,
  "rawData": false
}
```

**Credentials:**
- googleContactsOAuth2Api: `Test Google Contacts OAuth2`

### Example 3: Get All Contacts Search

**From workflow:** Google Contacts Get All Search Test

**Parameters:**
```json
{
  "resource": "contact",
  "operation": "getAll",
  "returnAll": true,
  "fields": [
    "names",
    "emailAddresses"
  ],
  "useQuery": true,
  "query": "John",
  "rawData": false
}
```

**Credentials:**
- googleContactsOAuth2Api: `Test Google Contacts OAuth2`

### Example 4: Get All Contacts Connections

**From workflow:** Google Contacts Get All Connections Test

**Parameters:**
```json
{
  "resource": "contact",
  "operation": "getAll",
  "returnAll": true,
  "fields": [
    "names",
    "emailAddresses"
  ],
  "useQuery": false,
  "rawData": false
}
```

**Credentials:**
- googleContactsOAuth2Api: `Test Google Contacts OAuth2`

### Example 5: Delete Contact

**From workflow:** Google Contacts Delete Test

**Parameters:**
```json
{
  "resource": "contact",
  "operation": "delete",
  "contactId": "c123456789"
}
```

**Credentials:**
- googleContactsOAuth2Api: `Test Google Contacts OAuth2`


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
* Categories: Miscellaneous 

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleContacts
displayName: Google Contacts
description: Consume Google Contacts API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: googleContactsOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a contact
  params:
  - id: familyName
    name: Family Name
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - contact
    typeInfo:
      type: string
      displayName: Family Name
      name: familyName
  - id: givenName
    name: Given Name
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - contact
    typeInfo:
      type: string
      displayName: Given Name
      name: givenName
- id: delete
  name: Delete
  description: Delete a contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - contact
    typeInfo: &id002
      type: string
      displayName: Contact ID
      name: contactId
- id: get
  name: Get
  description: Get a contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: fields
    name: Fields
    type: multiOptions
    default: []
    required: false
    description: A field mask to restrict which fields on each person are returned.
      Multiple fields can be specified by separating them with commas.
    validation: &id003
      displayOptions:
        show:
          operation:
          - update
          resource:
          - contact
    typeInfo: &id004
      type: multiOptions
      displayName: Fields
      name: fields
      possibleValues:
      - value: '*'
        name: '*'
        description: ''
      - value: addresses
        name: Addresses
        description: ''
      - value: biographies
        name: Biographies
        description: ''
      - value: birthdays
        name: Birthdays
        description: ''
      - value: coverPhotos
        name: Cover Photos
        description: ''
      - value: emailAddresses
        name: Email Addresses
        description: ''
      - value: events
        name: Events
        description: ''
      - value: genders
        name: Genders
        description: ''
      - value: imClients
        name: IM Clients
        description: ''
      - value: interests
        name: Interests
        description: ''
      - value: locales
        name: Locales
        description: ''
      - value: memberships
        name: Memberships
        description: ''
      - value: metadata
        name: Metadata
        description: ''
      - value: names
        name: Names
        description: ''
      - value: nicknames
        name: Nicknames
        description: ''
      - value: occupations
        name: Occupations
        description: ''
      - value: organizations
        name: Organizations
        description: ''
      - value: phoneNumbers
        name: Phone Numbers
        description: ''
      - value: photos
        name: Photos
        description: ''
      - value: relations
        name: Relations
        description: ''
      - value: residences
        name: Residences
        description: ''
      - value: sipAddresses
        name: Sip Addresses
        description: ''
      - value: skills
        name: Skills
        description: ''
      - value: urls
        name: URLs
        description: ''
      - value: userDefined
        name: User Defined
        description: ''
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether to return the data exactly in the way it got received from
      the API
    validation: &id005
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - contact
    typeInfo: &id006
      type: boolean
      displayName: RAW Data
      name: rawData
- id: getAll
  name: Get Many
  description: Retrieve many contacts
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
          operation:
          - getAll
          resource:
          - contact
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - contact
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: fields
    name: Fields
    type: multiOptions
    default: []
    required: false
    description: A field mask to restrict which fields on each person are returned.
      Multiple fields can be specified by separating them with commas.
    validation: *id003
    typeInfo: *id004
  - id: useQuery
    name: Use Query
    type: boolean
    default: false
    required: false
    description: Whether or not to use a query to filter the results
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - contact
    typeInfo:
      type: boolean
      displayName: Use Query
      name: useQuery
  - id: query
    name: Query
    type: string
    default: ''
    required: false
    description: The plain-text query for the request. The query is used to match
      prefix phrases of the fields on a person. For example, a person with name "foo
      name" matches queries such as "f", "fo", "foo", "foo n", "nam", etc., but not
      "oo n".
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - contact
          useQuery:
          - true
    typeInfo:
      type: string
      displayName: Query
      name: query
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether to return the data exactly in the way it got received from
      the API
    validation: *id005
    typeInfo: *id006
- id: update
  name: Update
  description: Update a contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: fields
    name: Fields
    type: multiOptions
    default: []
    required: false
    description: A field mask to restrict which fields on each person are returned.
      Multiple fields can be specified by separating them with commas.
    validation: *id003
    typeInfo: *id004
examples:
- name: Get Contact All Fields
  parameters:
    resource: contact
    operation: get
    contactId: c123456789
    fields:
    - '*'
    rawData: false
  workflow: Google Contacts Get All Fields Test
- name: Get All Contacts Limit
  parameters:
    resource: contact
    operation: getAll
    returnAll: false
    limit: 1
    fields:
    - names
    useQuery: false
    rawData: false
  workflow: Google Contacts Get All Limit Test
- name: Get All Contacts Search
  parameters:
    resource: contact
    operation: getAll
    returnAll: true
    fields:
    - names
    - emailAddresses
    useQuery: true
    query: John
    rawData: false
  workflow: Google Contacts Get All Search Test
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
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/googleContacts.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Contacts Node",
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
            "contact"
          ],
          "default": "contact"
        },
        "operation": {
          "description": "Create a contact",
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
        "familyName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "givenName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The end user specified key of the user defined data",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "contactId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "fields": {
          "description": "A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas.",
          "type": "string",
          "default": []
        },
        "rawData": {
          "description": "Whether to return the data exactly in the way it got received from the API",
          "type": "boolean",
          "default": false
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
        "useQuery": {
          "description": "Whether or not to use a query to filter the results",
          "type": "boolean",
          "default": false
        },
        "query": {
          "description": "The plain-text query for the request. The query is used to match prefix phrases of the fields on a person. For example, a person with name \"foo name\" matches queries such as \"f\", \"fo\", \"foo\", \"foo n\", \"nam\", etc., but not \"oo n\".",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Sort people by when they were changed; older entries first",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "updateFields": {
          "description": "The etag field in the person is nedded to make sure the contact has not changed since your last read",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
      "name": "googleContactsOAuth2Api",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Get Contact All Fields",
      "value": {
        "resource": "contact",
        "operation": "get",
        "contactId": "c123456789",
        "fields": [
          "*"
        ],
        "rawData": false
      }
    },
    {
      "description": "Get All Contacts Limit",
      "value": {
        "resource": "contact",
        "operation": "getAll",
        "returnAll": false,
        "limit": 1,
        "fields": [
          "names"
        ],
        "useQuery": false,
        "rawData": false
      }
    },
    {
      "description": "Get All Contacts Search",
      "value": {
        "resource": "contact",
        "operation": "getAll",
        "returnAll": true,
        "fields": [
          "names",
          "emailAddresses"
        ],
        "useQuery": true,
        "query": "John",
        "rawData": false
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
