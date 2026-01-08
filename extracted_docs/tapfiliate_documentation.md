---
title: "Node: Tapfiliate"
slug: "node-tapfiliate"
version: "1"
updated: "2026-01-08"
summary: "Consume Tapfiliate API"
node_type: "regular"
group: "['transform']"
---

# Node: Tapfiliate

**Purpose.** Consume Tapfiliate API
**Subtitle.** ={{$parameter["operation"] + ":" + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:tapfiliate.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **tapfiliateApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `tapfiliateApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Api-Key

---

## Operations

### Affiliate Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an affiliate |
| Delete | `delete` | Delete an affiliate |
| Get | `get` | Get an affiliate by ID |
| Get Many | `getAll` | Get many affiliates |

### Affiliatemetadata Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add metadata to affiliate |
| Remove | `remove` | Remove metadata from affiliate |
| Update | `update` | Update affiliate's metadata |

### Programaffiliate Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add affiliate to program |
| Approve | `approve` | Approve an affiliate for a program |
| Disapprove | `disapprove` | Disapprove an affiliate |
| Get | `get` | Get an affiliate in a program |
| Get Many | `getAll` | Get many affiliates in program |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | affiliate | ✓ | Resource to operate on |  |

**Resource options:**

* **Affiliate** (`affiliate`)
* **Affiliate Metadata** (`affiliateMetadata`)
* **Program Affiliate** (`programAffiliate`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create an affiliate |  |

**Operation options:**

* **Create** (`create`) - Create an affiliate
* **Delete** (`delete`) - Delete an affiliate
* **Get** (`get`) - Get an affiliate by ID
* **Get Many** (`getAll`) - Get many affiliates

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | The affiliate’s email | e.g. name@email.com | email |
| First Name | `firstname` | string |  | ✓ | The affiliate’s firstname |  |
| Last Name | `lastname` | string |  | ✓ | The affiliate’s lastname |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The country’s ISO_3166-1 code. <a href="https://en.wikipedia.org/wiki/ISO_3166-1">Codes</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressUi` | fixedCollection | {} | The country’s ISO_3166-1 code. <a href="https://en.wikipedia.org/wiki/ISO_3166-1">Codes</a>. |
| Company Name | `companyName` | string |  | The affiliate’s company data |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Affiliate ID | `affiliateId` | string |  | ✓ | The ID of the affiliate |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Affiliate ID | `affiliateId` | string |  | ✓ | The ID of the affiliate |  |
| Program Name or ID | `programId` | options |  | ✓ | The ID of the Program to add the affiliate to. This ID can be found as part of the URL when viewing the program on the platform. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Affiliate ID | `affiliateId` | string |  | ✓ | The ID of the affiliate |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | Retrieves affiliates for a certain affiliate group | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Affiliate Group ID | `affiliate_group_id` | string |  | Retrieves affiliates for a certain affiliate group |
| Click ID | `click_id` | string |  |  |
| Email | `email` | string |  | An email address, |
| Parent ID | `parentId` | string |  | Retrieves children for a certain parent affiliate |
| Referral Code | `referral_code` | string |  | An affiliate’s referral code. This corresponds to the value of ref= in their referral link. |
| Source ID | `source_id` | string |  |  |

</details>

| Program Name or ID | `programId` | options |  | ✓ | The ID of the Program to add the affiliate to. This ID can be found as part of the URL when viewing the program on the platform. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | Retrieves affiliates for a certain affiliate group | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Affiliate Group ID | `affiliate_group_id` | string |  | Retrieves affiliates for a certain affiliate group |
| Email | `email` | string |  | An email address |
| Parent ID | `parentId` | string |  | Retrieves children for a certain parent affiliate |
| Source ID | `source_id` | string |  |  |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Affiliate ID | `affiliateId` | string |  | ✓ | The ID of the affiliate |  |
| Metadata | `metadataUi` | fixedCollection | {} | ✗ | Meta data | e.g. Add Metadata |  |

<details>
<summary><strong>Metadata sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Metadata | `metadataValues` |  |  |  |

</details>

| Program Name or ID | `programId` | options |  | ✓ | The ID of the Program to add the affiliate to. This ID can be found as part of the URL when viewing the program on the platform. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Affiliate ID | `affiliateId` | string |  | ✓ | The ID of the affiliate |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | An optional approval status | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Approved | `approved` | boolean | True | An optional approval status |
| Coupon | `coupon` | string |  | An optional coupon for this affiliate |

</details>


### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Affiliate ID | `affiliateId` | string |  | ✓ | The ID of the affiliate |  |
| Key | `key` | string |  | ✗ | Name of the metadata key to remove |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Affiliate ID | `affiliateId` | string |  | ✓ | The ID of the affiliate |  |
| Key | `key` | string |  | ✗ | Name of the metadata key to update |  |
| Value | `value` | string |  | ✗ | Value to set for the metadata key |  |

### Approve parameters (`approve`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Program Name or ID | `programId` | options |  | ✗ | The ID of the Program to add the affiliate to. This ID can be found as part of the URL when viewing the program on the platform. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Affiliate ID | `affiliateId` | string |  | ✗ | The ID of the affiliate |  |

### Disapprove parameters (`disapprove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Program Name or ID | `programId` | options |  | ✗ | The ID of the Program to add the affiliate to. This ID can be found as part of the URL when viewing the program on the platform. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Affiliate ID | `affiliateId` | string |  | ✗ | The ID of the affiliate |  |

---

## Load Options Methods

- `getPrograms`
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
node: tapfiliate
displayName: Tapfiliate
description: Consume Tapfiliate API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: tapfiliateApi
  required: true
operations:
- id: create
  name: Create
  description: Create an affiliate
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The affiliate’s email
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - create
          resource:
          - affiliate
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: firstname
    name: First Name
    type: string
    default: ''
    required: true
    description: The affiliate’s firstname
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - affiliate
    typeInfo:
      type: string
      displayName: First Name
      name: firstname
  - id: lastname
    name: Last Name
    type: string
    default: ''
    required: true
    description: The affiliate’s lastname
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - affiliate
    typeInfo:
      type: string
      displayName: Last Name
      name: lastname
- id: delete
  name: Delete
  description: Delete an affiliate
  params:
  - id: affiliateId
    name: Affiliate ID
    type: string
    default: ''
    required: true
    description: The ID of the affiliate
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - programAffiliate
          operation:
          - get
    typeInfo: &id002
      type: string
      displayName: Affiliate ID
      name: affiliateId
- id: get
  name: Get
  description: Get an affiliate by ID
  params:
  - id: affiliateId
    name: Affiliate ID
    type: string
    default: ''
    required: true
    description: The ID of the affiliate
    validation: *id001
    typeInfo: *id002
  - id: programId
    name: Program Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the Program to add the affiliate to. This ID can be found
      as part of the URL when viewing the program on the platform. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - programAffiliate
    typeInfo: &id004
      type: options
      displayName: Program Name or ID
      name: programId
      typeOptions:
        loadOptionsMethod: getPrograms
      possibleValues: []
  - id: affiliateId
    name: Affiliate ID
    type: string
    default: ''
    required: true
    description: The ID of the affiliate
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many affiliates
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
          - programAffiliate
          operation:
          - getAll
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          resource:
          - programAffiliate
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
        maxValue: 1000
  - id: programId
    name: Program Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the Program to add the affiliate to. This ID can be found
      as part of the URL when viewing the program on the platform. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: add
  name: Add
  description: Add metadata to affiliate
  params:
  - id: affiliateId
    name: Affiliate ID
    type: string
    default: ''
    required: true
    description: The ID of the affiliate
    validation: *id001
    typeInfo: *id002
  - id: metadataUi
    name: Metadata
    type: fixedCollection
    default: {}
    required: false
    description: Meta data
    placeholder: Add Metadata
    validation:
      displayOptions:
        show:
          resource:
          - affiliateMetadata
          operation:
          - add
    typeInfo:
      type: fixedCollection
      displayName: Metadata
      name: metadataUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: metadataValues
        displayName: Metadata
        values:
        - displayName: Key
          name: key
          type: string
          description: Name of the metadata key to add
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value to set for the metadata key
          default: ''
  - id: programId
    name: Program Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the Program to add the affiliate to. This ID can be found
      as part of the URL when viewing the program on the platform. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: affiliateId
    name: Affiliate ID
    type: string
    default: ''
    required: true
    description: The ID of the affiliate
    validation: *id001
    typeInfo: *id002
- id: remove
  name: Remove
  description: Remove metadata from affiliate
  params:
  - id: affiliateId
    name: Affiliate ID
    type: string
    default: ''
    required: true
    description: The ID of the affiliate
    validation: *id001
    typeInfo: *id002
  - id: key
    name: Key
    type: string
    default: ''
    required: false
    description: Name of the metadata key to remove
    validation: &id009
      displayOptions:
        show:
          resource:
          - affiliateMetadata
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Key
      name: key
- id: update
  name: Update
  description: Update affiliate's metadata
  params:
  - id: affiliateId
    name: Affiliate ID
    type: string
    default: ''
    required: true
    description: The ID of the affiliate
    validation: *id001
    typeInfo: *id002
  - id: key
    name: Key
    type: string
    default: ''
    required: false
    description: Name of the metadata key to update
    validation: *id009
    typeInfo: *id010
  - id: value
    name: Value
    type: string
    default: ''
    required: false
    description: Value to set for the metadata key
    validation:
      displayOptions:
        show:
          resource:
          - affiliateMetadata
          operation:
          - update
    typeInfo:
      type: string
      displayName: Value
      name: value
- id: approve
  name: Approve
  description: Approve an affiliate for a program
  params:
  - id: programId
    name: Program Name or ID
    type: options
    default: ''
    required: false
    description: The ID of the Program to add the affiliate to. This ID can be found
      as part of the URL when viewing the program on the platform. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: affiliateId
    name: Affiliate ID
    type: string
    default: ''
    required: false
    description: The ID of the affiliate
    validation: *id001
    typeInfo: *id002
- id: disapprove
  name: Disapprove
  description: Disapprove an affiliate
  params:
  - id: programId
    name: Program Name or ID
    type: options
    default: ''
    required: false
    description: The ID of the Program to add the affiliate to. This ID can be found
      as part of the URL when viewing the program on the platform. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: affiliateId
    name: Affiliate ID
    type: string
    default: ''
    required: false
    description: The ID of the affiliate
    validation: *id001
    typeInfo: *id002
common_expressions:
- ={{$parameter["operation"] + ":" + $parameter["resource"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Api-Key
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: metadataUi
    text: Add Metadata
  - field: additionalFields
    text: Add Field
  - field: filters
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
  "$id": "https://n8n.io/schemas/nodes/tapfiliate.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Tapfiliate Node",
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
        "add",
        "remove",
        "update",
        "approve",
        "disapprove"
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
            "affiliate",
            "affiliateMetadata",
            "programAffiliate"
          ],
          "default": "affiliate"
        },
        "operation": {
          "description": "Add affiliate to program",
          "type": "string",
          "enum": [
            "add",
            "approve",
            "disapprove",
            "get",
            "getAll"
          ],
          "default": "add"
        },
        "email": {
          "description": "The affiliate\u2019s email",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "firstname": {
          "description": "The affiliate\u2019s firstname",
          "type": "string",
          "default": ""
        },
        "lastname": {
          "description": "The affiliate\u2019s lastname",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "An optional approval status",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "affiliateId": {
          "description": "The ID of the affiliate",
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
          "default": 100
        },
        "filters": {
          "description": "Retrieves affiliates for a certain affiliate group",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "metadataUi": {
          "description": "Meta data",
          "type": "string",
          "default": {},
          "examples": [
            "Add Metadata"
          ]
        },
        "key": {
          "description": "Name of the metadata key to update",
          "type": "string",
          "default": ""
        },
        "value": {
          "description": "Value to set for the metadata key",
          "type": "string",
          "default": ""
        },
        "programId": {
          "description": "The ID of the Program to add the affiliate to. This ID can be found as part of the URL when viewing the program on the platform. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
      "name": "tapfiliateApi",
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
