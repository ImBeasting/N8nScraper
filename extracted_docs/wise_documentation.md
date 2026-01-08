---
title: "Node: Wise"
slug: "node-wise"
version: "1"
updated: "2026-01-08"
summary: "Consume the Wise API"
node_type: "regular"
group: "['transform']"
---

# Node: Wise

**Purpose.** Consume the Wise API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:wise.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **wiseApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `wiseApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** GET

**Common Endpoints:**
- `{rootUrl}{endpoint}`

**Headers Used:** user-agent

---

## Operations

### Transfer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a transfer |
| Delete | `delete` | Delete a transfer |
| Execute | `execute` | Execute a transfer |
| Get | `get` | Get a transfer |
| Get Many | `getAll` | Get many transfers |

### Account Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Balances | `getBalances` | Retrieve balances for all account currencies of this user |
| Get Currencies | `getCurrencies` | Retrieve currencies in the borderless account of this user |
| Get Statement | `getStatement` | Retrieve the statement for the borderless account of this user |

### Exchangerate Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get an exchange rate |

### Profile Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a profile |
| Get Many | `getAll` | Get many profiles |

### Quote Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a quote |
| Get | `get` | Get a quote |

### Recipient Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many recipients |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | account | ✗ | Resource to operate on |  |

**Resource options:**

* **Account** (`account`)
* **Exchange Rate** (`exchangeRate`)
* **Profile** (`profile`)
* **Quote** (`quote`)
* **Recipient** (`recipient`)
* **Transfer** (`transfer`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create a transfer
* **Delete** (`delete`) - Delete a transfer
* **Execute** (`execute`) - Execute a transfer
* **Get** (`get`) - Get a transfer
* **Get Many** (`getAll`) - Get many transfers

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Profile Name or ID | `profileId` | options | [] | ✓ | ID of the user profile to retrieve the balance of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Quote ID | `quoteId` | string |  | ✓ | ID of the quote based on which to create the transfer |  |
| Target Account Name or ID | `targetAccountId` | options | [] | ✓ | ID of the account that will receive the funds. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Reference text to show in the recipient's bank statement | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Reference | `reference` | string |  | Reference text to show in the recipient's bank statement |

</details>

| Profile Name or ID | `profileId` | options | [] | ✓ | ID of the user profile to create the quote under. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Target Account Name or ID | `targetAccountId` | options | [] | ✓ | ID of the account that will receive the funds. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Amount Type | `amountType` | options | source | ✗ | Whether the amount is to be sent or received |  |

**Amount Type options:**

* **Source** (`source`)
* **Target** (`target`)

| Amount | `amount` | number | 1 | ✗ | Amount of funds for the quote to create | min:1, max:∞ |
| Source Currency | `sourceCurrency` | string |  | ✗ | Code of the currency to send for the quote to create |  |
| Target Currency | `targetCurrency` | string |  | ✗ | Code of the currency to receive for the quote to create |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Transfer ID | `transferId` | string |  | ✓ | ID of the transfer to delete |  |

### Execute parameters (`execute`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Profile Name or ID | `profileId` | options | [] | ✓ | ID of the user profile to execute the transfer under. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Transfer ID | `transferId` | string |  | ✓ | ID of the transfer to execute |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Transfer ID | `transferId` | string |  | ✓ | ID of the transfer to retrieve |  |
| Download Receipt | `downloadReceipt` | boolean | False | ✓ | Whether to download the transfer receipt as a PDF file. Only for executed transfers, having status 'Outgoing Payment Sent'. |  |
| Put Output File in Field | `binaryProperty` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| File Name | `fileName` | string |  | ✓ | Name of the file that will be downloaded | e.g. data.pdf |  |
| Source Currency | `source` | string |  | ✗ | Code of the source currency to retrieve the exchange rate for |  |
| Target Currency | `target` | string |  | ✗ | Code of the target currency to retrieve the exchange rate for |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Range of time to retrieve the exchange rate for | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Interval | `interval` | options | day |  |
| Range | `range` | fixedCollection | {} | Range of time to retrieve the exchange rate for |
| Time | `time` | dateTime |  | Point in time to retrieve the exchange rate for |

</details>

| Profile Name or ID | `profileId` | options | [] | ✓ | ID of the user profile to retrieve. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Quote ID | `quoteId` | string |  | ✓ | ID of the quote to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Profile Name or ID | `profileId` | options | [] | ✓ | ID of the user profile to retrieve. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | Range of time for filtering the transfers | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Range | `range` | fixedCollection | {} | Range of time for filtering the transfers |
| Source Currency | `sourceCurrency` | string |  | Code of the source currency for filtering the transfers |
| Status | `status` | options | processing |  |
| Target Currency | `targetCurrency` | string |  | Code of the target currency for filtering the transfers |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |

### Get Balances parameters (`getBalances`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Profile Name or ID | `profileId` | options | [] | ✓ | ID of the user profile to retrieve the balance of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Get Statement parameters (`getStatement`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Profile Name or ID | `profileId` | options | [] | ✗ | ID of the user profile whose account to retrieve the statement of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Borderless Account Name or ID | `borderlessAccountId` | options | [] | ✓ | ID of the borderless account to retrieve the statement of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Currency | `currency` | string |  | ✗ | Code of the currency of the borderless account to retrieve the statement of |  |
| Format | `format` | options | json | ✗ | File format to retrieve the statement in |  |

**Format options:**

* **JSON** (`json`)
* **CSV** (`csv`)
* **PDF** (`pdf`)
* **XML (CAMT.053)** (`xml`)

| Put Output File in Field | `binaryProperty` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| File Name | `fileName` | string |  | ✓ | Name of the file that will be downloaded | e.g. data.pdf |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Line style to retrieve the statement in | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Line Style | `lineStyle` | options | COMPACT | Line style to retrieve the statement in |
| Range | `range` | fixedCollection | {} |  |

</details>


---

## Load Options Methods

- `getBorderlessAccounts`
- `profileId`

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
* Categories: Finance & Accounting
* Aliases: Currency

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: wise
displayName: Wise
description: Consume the Wise API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: wiseApi
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: profileId
    name: Profile Name or ID
    type: options
    default: []
    required: true
    description: ID of the user profile to retrieve the balance of. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - quote
          operation:
          - create
    typeInfo: &id002
      type: options
      displayName: Profile Name or ID
      name: profileId
      typeOptions:
        loadOptionsMethod: getProfiles
      possibleValues: []
  - id: quoteId
    name: Quote ID
    type: string
    default: ''
    required: true
    description: ID of the quote based on which to create the transfer
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - quote
          operation:
          - get
    typeInfo: &id008
      type: string
      displayName: Quote ID
      name: quoteId
  - id: targetAccountId
    name: Target Account Name or ID
    type: options
    default: []
    required: true
    description: ID of the account that will receive the funds. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - quote
          operation:
          - create
    typeInfo: &id004
      type: options
      displayName: Target Account Name or ID
      name: targetAccountId
      typeOptions:
        loadOptionsMethod: getRecipients
      possibleValues: []
  - id: profileId
    name: Profile Name or ID
    type: options
    default: []
    required: true
    description: ID of the user profile to create the quote under. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: targetAccountId
    name: Target Account Name or ID
    type: options
    default: []
    required: true
    description: ID of the account that will receive the funds. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: amountType
    name: Amount Type
    type: options
    default: source
    required: false
    description: Whether the amount is to be sent or received
    validation:
      displayOptions:
        show:
          resource:
          - quote
          operation:
          - create
    typeInfo:
      type: options
      displayName: Amount Type
      name: amountType
      possibleValues:
      - value: source
        name: Source
        description: ''
      - value: target
        name: Target
        description: ''
  - id: amount
    name: Amount
    type: number
    default: 1
    required: false
    description: Amount of funds for the quote to create
    validation:
      displayOptions:
        show:
          resource:
          - quote
          operation:
          - create
    typeInfo:
      type: number
      displayName: Amount
      name: amount
      typeOptions:
        minValue: 1
  - id: sourceCurrency
    name: Source Currency
    type: string
    default: ''
    required: false
    description: Code of the currency to send for the quote to create
    validation:
      displayOptions:
        show:
          resource:
          - quote
          operation:
          - create
    typeInfo:
      type: string
      displayName: Source Currency
      name: sourceCurrency
  - id: targetCurrency
    name: Target Currency
    type: string
    default: ''
    required: false
    description: Code of the currency to receive for the quote to create
    validation:
      displayOptions:
        show:
          resource:
          - quote
          operation:
          - create
    typeInfo:
      type: string
      displayName: Target Currency
      name: targetCurrency
- id: delete
  name: Delete
  description: ''
  params:
  - id: transferId
    name: Transfer ID
    type: string
    default: ''
    required: true
    description: ID of the transfer to delete
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - transfer
          operation:
          - get
    typeInfo: &id006
      type: string
      displayName: Transfer ID
      name: transferId
- id: execute
  name: Execute
  description: ''
  params:
  - id: profileId
    name: Profile Name or ID
    type: options
    default: []
    required: true
    description: ID of the user profile to execute the transfer under. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: transferId
    name: Transfer ID
    type: string
    default: ''
    required: true
    description: ID of the transfer to execute
    validation: *id005
    typeInfo: *id006
- id: get
  name: Get
  description: ''
  params:
  - id: transferId
    name: Transfer ID
    type: string
    default: ''
    required: true
    description: ID of the transfer to retrieve
    validation: *id005
    typeInfo: *id006
  - id: downloadReceipt
    name: Download Receipt
    type: boolean
    default: false
    required: true
    description: Whether to download the transfer receipt as a PDF file. Only for
      executed transfers, having status 'Outgoing Payment Sent'.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - transfer
          operation:
          - get
    typeInfo:
      type: boolean
      displayName: Download Receipt
      name: downloadReceipt
  - id: binaryProperty
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - account
          operation:
          - getStatement
          format:
          - csv
          - pdf
          - xml
    typeInfo: &id014
      type: string
      displayName: Put Output File in Field
      name: binaryProperty
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: true
    description: Name of the file that will be downloaded
    placeholder: data.pdf
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - account
          operation:
          - getStatement
          format:
          - csv
          - pdf
          - xml
    typeInfo: &id016
      type: string
      displayName: File Name
      name: fileName
  - id: source
    name: Source Currency
    type: string
    default: ''
    required: false
    description: Code of the source currency to retrieve the exchange rate for
    validation:
      displayOptions:
        show:
          resource:
          - exchangeRate
          operation:
          - get
    typeInfo:
      type: string
      displayName: Source Currency
      name: source
  - id: target
    name: Target Currency
    type: string
    default: ''
    required: false
    description: Code of the target currency to retrieve the exchange rate for
    validation:
      displayOptions:
        show:
          resource:
          - exchangeRate
          operation:
          - get
    typeInfo:
      type: string
      displayName: Target Currency
      name: target
  - id: profileId
    name: Profile Name or ID
    type: options
    default: []
    required: true
    description: ID of the user profile to retrieve. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: quoteId
    name: Quote ID
    type: string
    default: ''
    required: true
    description: ID of the quote to retrieve
    validation: *id007
    typeInfo: *id008
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: profileId
    name: Profile Name or ID
    type: options
    default: []
    required: true
    description: ID of the user profile to retrieve. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
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
          - recipient
          operation:
          - getAll
    typeInfo: &id010
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation: &id011
      displayOptions:
        show:
          resource:
          - recipient
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
        maxValue: 1000
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
    default: 5
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
- id: getBalances
  name: Get Balances
  description: Retrieve balances for all account currencies of this user
  params:
  - id: profileId
    name: Profile Name or ID
    type: options
    default: []
    required: true
    description: ID of the user profile to retrieve the balance of. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
- id: getCurrencies
  name: Get Currencies
  description: Retrieve currencies in the borderless account of this user
- id: getStatement
  name: Get Statement
  description: Retrieve the statement for the borderless account of this user
  params:
  - id: profileId
    name: Profile Name or ID
    type: options
    default: []
    required: false
    description: ID of the user profile whose account to retrieve the statement of.
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: borderlessAccountId
    name: Borderless Account Name or ID
    type: options
    default: []
    required: true
    description: ID of the borderless account to retrieve the statement of. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - account
          operation:
          - getStatement
    typeInfo:
      type: options
      displayName: Borderless Account Name or ID
      name: borderlessAccountId
      typeOptions:
        loadOptionsMethod: getBorderlessAccounts
      possibleValues: []
  - id: currency
    name: Currency
    type: string
    default: ''
    required: false
    description: Code of the currency of the borderless account to retrieve the statement
      of
    validation:
      displayOptions:
        show:
          resource:
          - account
          operation:
          - getStatement
    typeInfo:
      type: string
      displayName: Currency
      name: currency
  - id: format
    name: Format
    type: options
    default: json
    required: false
    description: File format to retrieve the statement in
    validation:
      displayOptions:
        show:
          resource:
          - account
          operation:
          - getStatement
    typeInfo:
      type: options
      displayName: Format
      name: format
      possibleValues:
      - value: json
        name: JSON
        description: ''
      - value: csv
        name: CSV
        description: ''
      - value: pdf
        name: PDF
        description: ''
      - value: xml
        name: XML (CAMT.053)
        description: ''
  - id: binaryProperty
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: *id013
    typeInfo: *id014
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: true
    description: Name of the file that will be downloaded
    placeholder: data.pdf
    validation: *id015
    typeInfo: *id016
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - GET
  endpoints:
  - '{rootUrl}{endpoint}'
  headers:
  - user-agent
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: fileName
    text: data.pdf
  - field: filters
    text: Add Filter
  - field: fileName
    text: data.pdf
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  hints:
  - field: binaryProperty
    text: The name of the output binary field to put the file in
  - field: binaryProperty
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/wise.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Wise Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "execute",
        "get",
        "getAll",
        "getBalances",
        "getCurrencies",
        "getStatement"
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
            "account",
            "exchangeRate",
            "profile",
            "quote",
            "recipient",
            "transfer"
          ],
          "default": "account"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "getAll"
        },
        "profileId": {
          "description": "ID of the user profile to create the quote under. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "quoteId": {
          "description": "ID of the quote to retrieve",
          "type": "string",
          "default": ""
        },
        "targetAccountId": {
          "description": "ID of the account that will receive the funds. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "additionalFields": {
          "description": "Range of time to retrieve the exchange rate for",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "transferId": {
          "description": "ID of the transfer to retrieve",
          "type": "string",
          "default": ""
        },
        "downloadReceipt": {
          "description": "Whether to download the transfer receipt as a PDF file. Only for executed transfers, having status 'Outgoing Payment Sent'.",
          "type": "boolean",
          "default": false
        },
        "binaryProperty": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "fileName": {
          "description": "Name of the file that will be downloaded",
          "type": "string",
          "default": "",
          "examples": [
            "data.pdf"
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
        "filters": {
          "description": "Range of time for filtering the transfers",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "borderlessAccountId": {
          "description": "ID of the borderless account to retrieve the statement of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "currency": {
          "description": "Code of the currency of the borderless account to retrieve the statement of",
          "type": "string",
          "default": ""
        },
        "format": {
          "description": "File format to retrieve the statement in",
          "type": "string",
          "enum": [
            "json",
            "csv",
            "pdf",
            "xml"
          ],
          "default": "json"
        },
        "source": {
          "description": "Code of the source currency to retrieve the exchange rate for",
          "type": "string",
          "default": ""
        },
        "target": {
          "description": "Code of the target currency to retrieve the exchange rate for",
          "type": "string",
          "default": ""
        },
        "amountType": {
          "description": "Whether the amount is to be sent or received",
          "type": "string",
          "enum": [
            "source",
            "target"
          ],
          "default": "source"
        },
        "amount": {
          "description": "Amount of funds for the quote to create",
          "type": "number",
          "default": 1
        },
        "sourceCurrency": {
          "description": "Code of the currency to send for the quote to create",
          "type": "string",
          "default": ""
        },
        "targetCurrency": {
          "description": "Code of the currency to receive for the quote to create",
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
      "name": "wiseApi",
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
