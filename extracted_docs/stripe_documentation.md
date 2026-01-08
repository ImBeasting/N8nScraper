---
title: "Node: Stripe"
slug: "node-stripe"
version: "1"
updated: "2026-01-08"
summary: "Consume the Stripe API"
node_type: "regular"
group: "['transform']"
---

# Node: Stripe

**Purpose.** Consume the Stripe API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:stripe.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **stripeApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `stripeApi` | ✓ | - |

---

## Operations

### Token Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a token |

### Balance Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a balance |

### Customercard Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a customer card |
| Get | `get` | Get a customer card |
| Remove | `remove` | Remove a customer card |

### Charge Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a charge |
| Get | `get` | Get a charge |
| Get Many | `getAll` | Get many charges |
| Update | `update` | Update a charge |

### Coupon Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a coupon |
| Get Many | `getAll` | Get many coupons |

### Customer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a customer |
| Delete | `delete` | Delete a customer |
| Get | `get` | Get a customer |
| Get Many | `getAll` | Get many customers |
| Update | `update` | Update a customer |

### Meterevent Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a meter event |

### Source Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a source |
| Delete | `delete` | Delete a source |
| Get | `get` | Get a source |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | balance | ✗ | Resource to operate on |  |

**Resource options:**

* **Balance** (`balance`)
* **Charge** (`charge`)
* **Coupon** (`coupon`)
* **Customer** (`customer`)
* **Customer Card** (`customerCard`)
* **Meter Event** (`meterEvent`)
* **Source** (`source`)
* **Token** (`token`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a token |  |

**Operation options:**

* **Create** (`create`) - Create a token

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Type | `type` | options | cardToken | ✓ | Type of token to create |  |

**Type options:**

* **Card Token** (`cardToken`)

| Card Number | `number` | string |  | ✗ | e.g. 4242424242424242 |  |
| CVC | `cvc` | string |  | ✗ | Security code printed on the back of the card | e.g. 314 |  |
| Expiration Month | `expirationMonth` | string |  | ✗ | Number of the month when the card will expire | e.g. 10 |  |
| Expiration Year | `expirationYear` | string |  | ✗ | Year when the card will expire | e.g. 2022 |  |
| Customer ID | `customerId` | string |  | ✓ | ID of the customer to be associated with this charge |  |
| Amount | `amount` | number | 0 | ✓ | Amount in cents to be collected for this charge, e.g. enter <code>100</code> for $1.00 | min:0, max:99999999 |
| Currency Name or ID | `currency` | options |  | ✓ | Three-letter ISO currency code, e.g. <code>USD</code> or <code>EUR</code>. It must be a <a href="https://stripe.com/docs/currencies">Stripe-supported currency</a>. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Source ID | `source` | string |  | ✓ | ID of the customer's payment source to be charged |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Arbitrary text to describe the charge to create | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Arbitrary text to describe the charge to create |
| Metadata | `metadata` | fixedCollection | [] | Set of key-value pairs to attach to the charge to create |
| Receipt Email | `receipt_email` | string |  | Email address to which the receipt for this charge will be sent |
| Shipping | `shipping` | fixedCollection | [] | Shipping information for the charge |

</details>

| Apply | `duration` | options | once | ✓ | How long the discount will be in effect |  |

**Apply options:**

* **Forever** (`forever`)
* **Once** (`once`)

| Discount Type | `type` | options | percent | ✓ | Whether the coupon discount is a percentage or a fixed amount |  |

**Discount Type options:**

* **Fixed Amount (in Cents)** (`fixedAmount`)
* **Percent** (`percent`)

| Amount Off | `amountOff` | number | 0 | ✓ | Amount in cents to subtract from an invoice total, e.g. enter <code>100</code> for $1.00 | min:0, max:99999999 |
| Currency Name or ID | `currency` | options |  | ✓ | Three-letter ISO currency code, e.g. <code>USD</code> or <code>EUR</code>. It must be a <a href="https://stripe.com/docs/currencies">Stripe-supported currency</a>. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Percent Off | `percentOff` | number | 1 | ✓ | Percentage to apply with the coupon | min:1, max:100 |
| Name | `name` | string |  | ✓ | Full name or business name of the customer to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Address of the customer to create | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | fixedCollection | {} | Address of the customer to create |
| Description | `description` | string |  | Arbitrary text to describe the customer to create |
| Email | `email` | string |  | Email of the customer to create |
| Metadata | `metadata` | fixedCollection | {} | Set of key-value pairs to attach to the customer to create |
| Phone | `phone` | string |  | Telephone number of the customer to create |
| Shipping | `shipping` | fixedCollection | {} | Shipping information for the customer |

</details>

| Event Name | `eventName` | string |  | ✓ | The name of the meter event. Corresponds with the event_name field on a meter. |  |
| Customer ID | `customerId` | string |  | ✓ | The Stripe customer ID associated with this meter event |  |
| Value | `value` | number | 1 | ✓ | The value of the meter event. Must be an integer. Can be positive or negative. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | A unique identifier for the event. If not provided, one will be generated. Uniqueness is enforced within a rolling 24 hour window. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Identifier | `identifier` | string |  | A unique identifier for the event. If not provided, one will be generated. Uniqueness is enforced within a rolling 24 hour window. |
| Timestamp | `timestamp` | dateTime |  | The time of the event. Measured in seconds since the Unix epoch. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current time if not specified. |
| Custom Payload Properties | `customPayload` | fixedCollection | {} | Additional custom properties to include in the event payload. Use this for custom meter configurations with non-default payload keys. |

</details>

| Customer ID | `customerId` | string |  | ✓ | ID of the customer to attach the source to |  |
| Type | `type` | options | wechat | ✓ | Type of source (payment instrument) to create |  |

**Type options:**

* **WeChat** (`wechat`)

| Amount | `amount` | number | 0 | ✗ | Amount in cents to be collected for this charge, e.g. enter <code>100</code> for $1.00 | min:0, max:99999999 |
| Currency Name or ID | `currency` | options |  | ✗ | Three-letter ISO currency code, e.g. <code>USD</code> or <code>EUR</code>. It must be a <a href="https://stripe.com/docs/currencies">Stripe-supported currency</a>. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Set of key-value pairs to attach to the source to create | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Metadata | `metadata` | fixedCollection | {} | Set of key-value pairs to attach to the source to create |
| Statement Descriptor | `statement_descriptor` | string |  | Arbitrary text to display on the customer's statement |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Customer ID | `customerId` | string |  | ✓ | ID of the customer whose card to retrieve |  |
| Source ID | `sourceId` | string |  | ✓ | ID of the source to retrieve |  |
| Charge ID | `chargeId` | string |  | ✓ | ID of the charge to retrieve |  |
| Customer ID | `customerId` | string |  | ✓ | ID of the customer to retrieve |  |
| Source ID | `sourceId` | string |  | ✓ | ID of the source to retrieve |  |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Customer ID | `customerId` | string |  | ✓ | ID of the customer to be associated with this card |  |
| Card Token | `token` | string |  | ✓ | Token representing sensitive card information | e.g. tok_1IMfKdJhRTnqS5TKQVG1LI9o |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Customer ID | `customerId` | string |  | ✓ | ID of the customer whose card to remove |  |
| Card ID | `cardId` | string |  | ✓ | ID of the card to remove |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | Customer's email to filter by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  | Customer's email to filter by |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Charge ID | `chargeId` | string |  | ✓ | ID of the charge to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Arbitrary text to describe the charge to update | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Arbitrary text to describe the charge to update |
| Metadata | `metadata` | fixedCollection | {} | Set of key-value pairs to attach to the charge to update |
| Receipt Email | `receipt_email` | string |  | The email address to which the receipt for this charge will be sent |
| Shipping | `shipping` | fixedCollection | {} | Shipping information for the charge |

</details>

| Customer ID | `customerId` | string |  | ✓ | ID of the customer to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Address of the customer to update | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | fixedCollection | {} | Address of the customer to update |
| Description | `description` | string |  | Arbitrary text to describe the customer to create |
| Email | `email` | string |  | Email of the customer to create |
| Metadata | `metadata` | fixedCollection | {} | Set of key-value pairs to attach to the customer to create |
| Name | `name` | string |  | Full name or business name of the customer to create |
| Phone | `phone` | string |  | Telephone number of this customer |
| Shipping | `shipping` | fixedCollection | {} | Shipping information for the customer |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Customer ID | `customerId` | string |  | ✓ | ID of the customer to delete |  |
| Customer ID | `customerId` | string |  | ✓ | ID of the customer whose source to delete |  |
| Source ID | `sourceId` | string |  | ✓ | ID of the source to delete |  |

---

## Load Options Methods

- `getCustomers`

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
* Categories: Finance & Accounting, Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: stripe
displayName: Stripe
description: Consume the Stripe API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: stripeApi
  required: true
operations:
- id: create
  name: Create
  description: Create a token
  params:
  - id: type
    name: Type
    type: options
    default: cardToken
    required: true
    description: Type of token to create
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - source
          operation:
          - create
    typeInfo: &id002
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: wechat
        name: WeChat
        description: ''
  - id: number
    name: Card Number
    type: string
    default: ''
    required: false
    description: ''
    placeholder: '4242424242424242'
    validation:
      displayOptions:
        show:
          resource:
          - token
          operation:
          - create
          type:
          - cardToken
    typeInfo:
      type: string
      displayName: Card Number
      name: number
  - id: cvc
    name: CVC
    type: string
    default: ''
    required: false
    description: Security code printed on the back of the card
    placeholder: '314'
    validation:
      displayOptions:
        show:
          resource:
          - token
          operation:
          - create
          type:
          - cardToken
    typeInfo:
      type: string
      displayName: CVC
      name: cvc
  - id: expirationMonth
    name: Expiration Month
    type: string
    default: ''
    required: false
    description: Number of the month when the card will expire
    placeholder: '10'
    validation:
      displayOptions:
        show:
          resource:
          - token
          operation:
          - create
          type:
          - cardToken
    typeInfo:
      type: string
      displayName: Expiration Month
      name: expirationMonth
  - id: expirationYear
    name: Expiration Year
    type: string
    default: ''
    required: false
    description: Year when the card will expire
    placeholder: '2022'
    validation:
      displayOptions:
        show:
          resource:
          - token
          operation:
          - create
          type:
          - cardToken
    typeInfo:
      type: string
      displayName: Expiration Year
      name: expirationYear
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ID of the customer to be associated with this charge
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - source
          operation:
          - delete
    typeInfo: &id006
      type: string
      displayName: Customer ID
      name: customerId
  - id: amount
    name: Amount
    type: number
    default: 0
    required: true
    description: Amount in cents to be collected for this charge, e.g. enter <code>100</code>
      for $1.00
    validation: &id007
      displayOptions:
        show:
          resource:
          - source
          operation:
          - create
    typeInfo: &id008
      type: number
      displayName: Amount
      name: amount
      typeOptions:
        minValue: 0
        maxValue: 99999999
  - id: currency
    name: Currency Name or ID
    type: options
    default: ''
    required: true
    description: Three-letter ISO currency code, e.g. <code>USD</code> or <code>EUR</code>.
      It must be a <a href="https://stripe.com/docs/currencies">Stripe-supported currency</a>.
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id003
      displayOptions:
        show:
          resource:
          - source
          operation:
          - create
    typeInfo: &id004
      type: options
      displayName: Currency Name or ID
      name: currency
      typeOptions:
        loadOptionsMethod: getCurrencies
      possibleValues: []
  - id: source
    name: Source ID
    type: string
    default: ''
    required: true
    description: ID of the customer's payment source to be charged
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - charge
          operation:
          - create
    typeInfo:
      type: string
      displayName: Source ID
      name: source
  - id: duration
    name: Apply
    type: options
    default: once
    required: true
    description: How long the discount will be in effect
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - coupon
          operation:
          - create
    typeInfo:
      type: options
      displayName: Apply
      name: duration
      possibleValues:
      - value: forever
        name: Forever
        description: ''
      - value: once
        name: Once
        description: ''
  - id: type
    name: Discount Type
    type: options
    default: percent
    required: true
    description: Whether the coupon discount is a percentage or a fixed amount
    validation: *id001
    typeInfo: *id002
  - id: amountOff
    name: Amount Off
    type: number
    default: 0
    required: true
    description: Amount in cents to subtract from an invoice total, e.g. enter <code>100</code>
      for $1.00
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - coupon
          operation:
          - create
          type:
          - fixedAmount
    typeInfo:
      type: number
      displayName: Amount Off
      name: amountOff
      typeOptions:
        minValue: 0
        maxValue: 99999999
  - id: currency
    name: Currency Name or ID
    type: options
    default: ''
    required: true
    description: Three-letter ISO currency code, e.g. <code>USD</code> or <code>EUR</code>.
      It must be a <a href="https://stripe.com/docs/currencies">Stripe-supported currency</a>.
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: percentOff
    name: Percent Off
    type: number
    default: 1
    required: true
    description: Percentage to apply with the coupon
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - coupon
          operation:
          - create
          type:
          - percent
    typeInfo:
      type: number
      displayName: Percent Off
      name: percentOff
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Full name or business name of the customer to create
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - customer
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: eventName
    name: Event Name
    type: string
    default: ''
    required: true
    description: The name of the meter event. Corresponds with the event_name field
      on a meter.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - meterEvent
          operation:
          - create
    typeInfo:
      type: string
      displayName: Event Name
      name: eventName
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: The Stripe customer ID associated with this meter event
    validation: *id005
    typeInfo: *id006
  - id: value
    name: Value
    type: number
    default: 1
    required: true
    description: The value of the meter event. Must be an integer. Can be positive
      or negative.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - meterEvent
          operation:
          - create
    typeInfo:
      type: number
      displayName: Value
      name: value
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ID of the customer to attach the source to
    validation: *id005
    typeInfo: *id006
  - id: type
    name: Type
    type: options
    default: wechat
    required: true
    description: Type of source (payment instrument) to create
    validation: *id001
    typeInfo: *id002
  - id: amount
    name: Amount
    type: number
    default: 0
    required: false
    description: Amount in cents to be collected for this charge, e.g. enter <code>100</code>
      for $1.00
    validation: *id007
    typeInfo: *id008
  - id: currency
    name: Currency Name or ID
    type: options
    default: ''
    required: false
    description: Three-letter ISO currency code, e.g. <code>USD</code> or <code>EUR</code>.
      It must be a <a href="https://stripe.com/docs/currencies">Stripe-supported currency</a>.
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
- id: get
  name: Get
  description: Get a balance
  params:
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ID of the customer whose card to retrieve
    validation: *id005
    typeInfo: *id006
  - id: sourceId
    name: Source ID
    type: string
    default: ''
    required: true
    description: ID of the source to retrieve
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - source
          operation:
          - get
    typeInfo: &id010
      type: string
      displayName: Source ID
      name: sourceId
  - id: chargeId
    name: Charge ID
    type: string
    default: ''
    required: true
    description: ID of the charge to retrieve
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - charge
          operation:
          - update
    typeInfo: &id016
      type: string
      displayName: Charge ID
      name: chargeId
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ID of the customer to retrieve
    validation: *id005
    typeInfo: *id006
  - id: sourceId
    name: Source ID
    type: string
    default: ''
    required: true
    description: ID of the source to retrieve
    validation: *id009
    typeInfo: *id010
- id: add
  name: Add
  description: Add a customer card
  params:
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ID of the customer to be associated with this card
    validation: *id005
    typeInfo: *id006
  - id: token
    name: Card Token
    type: string
    default: ''
    required: true
    description: Token representing sensitive card information
    placeholder: tok_1IMfKdJhRTnqS5TKQVG1LI9o
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - customerCard
          operation:
          - add
    typeInfo:
      type: string
      displayName: Card Token
      name: token
      typeOptions:
        password: true
- id: remove
  name: Remove
  description: Remove a customer card
  params:
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ID of the customer whose card to remove
    validation: *id005
    typeInfo: *id006
  - id: cardId
    name: Card ID
    type: string
    default: ''
    required: true
    description: ID of the card to remove
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - customerCard
          operation:
          - remove
    typeInfo:
      type: string
      displayName: Card ID
      name: cardId
- id: getAll
  name: Get Many
  description: Get many charges
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
          - customer
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
          - customer
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
        maxValue: 1000
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
  description: Update a charge
  params:
  - id: chargeId
    name: Charge ID
    type: string
    default: ''
    required: true
    description: ID of the charge to update
    validation: *id015
    typeInfo: *id016
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ID of the customer to update
    validation: *id005
    typeInfo: *id006
- id: delete
  name: Delete
  description: Delete a customer
  params:
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ID of the customer to delete
    validation: *id005
    typeInfo: *id006
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ID of the customer whose source to delete
    validation: *id005
    typeInfo: *id006
  - id: sourceId
    name: Source ID
    type: string
    default: ''
    required: true
    description: ID of the source to delete
    validation: *id009
    typeInfo: *id010
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: number
    text: '4242424242424242'
  - field: cvc
    text: '314'
  - field: expirationMonth
    text: '10'
  - field: expirationYear
    text: '2022'
  - field: token
    text: tok_1IMfKdJhRTnqS5TKQVG1LI9o
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: updateFields
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
  "$id": "https://n8n.io/schemas/nodes/stripe.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Stripe Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "get",
        "add",
        "remove",
        "getAll",
        "update",
        "delete"
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
            "balance",
            "charge",
            "coupon",
            "customer",
            "customerCard",
            "meterEvent",
            "source",
            "token"
          ],
          "default": "balance"
        },
        "operation": {
          "description": "Create a source",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get"
          ],
          "default": "get"
        },
        "type": {
          "description": "Type of source (payment instrument) to create",
          "type": "string",
          "enum": [
            "wechat"
          ],
          "default": "wechat"
        },
        "number": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "4242424242424242"
          ]
        },
        "cvc": {
          "description": "Security code printed on the back of the card",
          "type": "string",
          "default": "",
          "examples": [
            "314"
          ]
        },
        "expirationMonth": {
          "description": "Number of the month when the card will expire",
          "type": "string",
          "default": "",
          "examples": [
            "10"
          ]
        },
        "expirationYear": {
          "description": "Year when the card will expire",
          "type": "string",
          "default": "",
          "examples": [
            "2022"
          ]
        },
        "customerId": {
          "description": "ID of the customer whose source to delete",
          "type": "string",
          "default": ""
        },
        "token": {
          "description": "Token representing sensitive card information",
          "type": "string",
          "default": "",
          "examples": [
            "tok_1IMfKdJhRTnqS5TKQVG1LI9o"
          ]
        },
        "cardId": {
          "description": "ID of the card to remove",
          "type": "string",
          "default": ""
        },
        "sourceId": {
          "description": "ID of the source to retrieve",
          "type": "string",
          "default": ""
        },
        "amount": {
          "description": "Amount in cents to be collected for this charge, e.g. enter <code>100</code> for $1.00",
          "type": "number",
          "default": 0
        },
        "currency": {
          "description": "Three-letter ISO currency code, e.g. <code>USD</code> or <code>EUR</code>. It must be a <a href=\"https://stripe.com/docs/currencies\">Stripe-supported currency</a>. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "source": {
          "description": "ID of the customer's payment source to be charged",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Set of key-value pairs to attach to the source to create",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "chargeId": {
          "description": "ID of the charge to update",
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
        "updateFields": {
          "description": "Address of the customer to update",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "duration": {
          "description": "How long the discount will be in effect",
          "type": "string",
          "enum": [
            "forever",
            "once"
          ],
          "default": "once"
        },
        "amountOff": {
          "description": "Amount in cents to subtract from an invoice total, e.g. enter <code>100</code> for $1.00",
          "type": "number",
          "default": 0
        },
        "percentOff": {
          "description": "Percentage to apply with the coupon",
          "type": "number",
          "default": 1
        },
        "name": {
          "description": "Full name or business name of the customer to create",
          "type": "string",
          "default": ""
        },
        "filters": {
          "description": "Customer's email to filter by",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "eventName": {
          "description": "The name of the meter event. Corresponds with the event_name field on a meter.",
          "type": "string",
          "default": ""
        },
        "value": {
          "description": "The value of the meter event. Must be an integer. Can be positive or negative.",
          "type": "number",
          "default": 1
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
      "name": "stripeApi",
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
