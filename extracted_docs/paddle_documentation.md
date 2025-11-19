---
title: "Node: Paddle"
slug: "node-paddle"
version: "1"
updated: "2025-11-13"
summary: "Consume Paddle API"
node_type: "regular"
group: "['output']"
---

# Node: Paddle

**Purpose.** Consume Paddle API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:paddle.png`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **paddleApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `paddleApi` | ✓ | - |

---

## API Patterns

**Headers Used:** content-type

---

## Operations

### Coupon Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a coupon |
| Get Many | `getAll` | Get many coupons |
| Update | `update` | Update a coupon |

### Payment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many payments |
| Reschedule | `reschedule` | Reschedule payment |

### Plan Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a plan |
| Get Many | `getAll` | Get many plans |

### Product Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many products |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many users |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | coupon | ✗ | Resource to operate on |  |

**Resource options:**

* **Coupon** (`coupon`)
* **Payment** (`payment`)
* **Plan** (`plan`)
* **Product** (`product`)
* **Order** (`order`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a coupon |  |

**Operation options:**

* **Create** (`create`) - Create a coupon
* **Get Many** (`getAll`) - Get many coupons
* **Update** (`update`) - Update a coupon

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Coupon Type | `couponType` | options | checkout | ✗ | Either product (valid for specified products or subscription plans) or checkout (valid for any checkout) |  |

**Coupon Type options:**

* **Checkout** (`checkout`)
* **Product** (`product`)

| Product Names or IDs | `productIds` | multiOptions | [] | ✓ | Comma-separated list of product IDs. Required if coupon_type is product. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Discount Type | `discountType` | options | flat | ✗ | Either flat or percentage |  |

**Discount Type options:**

* **Flat** (`flat`)
* **Percentage** (`percentage`)

| Discount Amount Currency | `discountAmount` | number | 1 | ✗ | Discount amount in currency | min:1, max:∞ |
| Discount Amount % | `discountAmount` | number | 1 | ✗ | Discount amount in percentage | min:1, max:100 |
| Currency | `currency` | options | EUR | ✗ | The currency must match the balance currency specified in your account |  |

**Currency options:**

* **ARS** (`ARS`)
* **AUD** (`AUD`)
* **BRL** (`BRL`)
* **CAD** (`CAD`)
* **CHF** (`CHF`)
* **CNY** (`CNY`)
* **CZK** (`CZK`)
* **DKK** (`DKK`)
* **EUR** (`EUR`)
* **GBP** (`GBP`)
* **HKD** (`HKD`)
* **HUF** (`HUF`)
* **INR** (`INR`)
* **JPY** (`JPY`)
* **KRW** (`KRW`)
* **MXN** (`MXN`)
* **NOK** (`NOK`)
* **NZD** (`NZD`)
* **PLN** (`PLN`)
* **RUB** (`RUB`)
* **SEK** (`SEK`)
* **SGD** (`SGD`)
* **THB** (`THB`)
* **TWD** (`TWD`)
* **USD** (`USD`)
* **ZAR** (`ZAR`)

| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Attributes in JSON form |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Number of times a coupon can be used in a checkout. This will be set to 999,999 by default, if not specified. | e.g. Add Field | min:1, max:50 |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Allowed Uses | `allowedUses` | number | 1 | Number of times a coupon can be used in a checkout. This will be set to 999,999 by default, if not specified. |
| Coupon Code | `couponCode` | string |  | Will be randomly generated if not specified |
| Coupon Prefix | `couponPrefix` | string |  | Prefix for generated codes. Not valid if coupon_code is specified. |
| Description | `description` | string |  | Description of the coupon. This will be displayed in the Seller Dashboard. |
| Expires | `expires` | dateTime |  | The coupon will expire on the date at 00:00:00 UTC |
| Group | `group` | string |  | The name of the coupon group this coupon should be assigned to |
| Number of Coupons | `numberOfCoupons` | number | 1 | Number of coupons to generate. Not valid if coupon_code is specified. |
| Recurring | `recurring` | boolean | False | If the coupon is used on subscription products, this indicates whether the discount should apply to recurring payments after the initial purchase |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Product ID | `productId` | string |  | ✓ | The specific product/subscription ID |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Attributes in JSON form |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Payment starting from date | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date From | `from` | dateTime |  | Payment starting from date |
| Date To | `to` | dateTime |  | Payment up until date |
| Is Paid | `isPaid` | boolean | False | Whether payment is paid |
| Plan ID | `plan` | string |  | Filter: The product/plan ID (single or comma-separated values) |
| Subscription ID | `subscriptionId` | number |  | A specific user subscription ID |
| State | `state` | options | active | Filter: The user subscription status. Returns all active, past_due, trialing and paused subscription plans if not specified. |
| One Off Charge | `isOneOffCharge` | boolean | False |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✓ | Max number of results to return | min:1, max:200 |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Attributes in JSON form |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Filter: The subscription plan ID | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Plan ID | `planId` | string |  | Filter: The subscription plan ID |
| Subscription ID | `subscriptionId` | string |  | A specific user subscription ID |
| State | `state` | options | active | Filter: The user subscription status. Returns all active, past_due, trialing and paused subscription plans if not specified. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Update By | `updateBy` | options | couponCode | ✗ | Either flat or percentage |  |

**Update By options:**

* **Coupon Code** (`couponCode`)
* **Group** (`group`)

| Coupon Code | `couponCode` | string |  | ✗ | Identify the coupon to update |  |
| Group | `group` | string |  | ✗ | The name of the group of coupons you want to update |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Attributes in JSON form |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Number of times a coupon can be used in a checkout. This will be set to 999,999 by default, if not specified. | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Allowed Uses | `allowedUses` | number | 1 | Number of times a coupon can be used in a checkout. This will be set to 999,999 by default, if not specified. |
| Discount | `discount` | fixedCollection | {} | The currency must match the balance currency specified in your account |
| Expires | `expires` | dateTime |  | The coupon will expire on the date at 00:00:00 UTC |
| New Coupon Code | `newCouponCode` | string |  | New code to rename the coupon to |
| New Group Name | `newGroup` | string |  | New group name to move coupon to |
| Product IDs | `productIds` | string |  | Comma-separated list of products e.g. 499531,1234,123546. If blank then remove associated products. |
| Recurring | `recurring` | boolean | False | If the coupon is used on subscription products, this indicates whether the discount should apply to recurring payments after the initial purchase |

</details>


### Reschedule parameters (`reschedule`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Payment Name or ID | `paymentId` | options |  | ✓ | The upcoming subscription payment ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Date | `date` | dateTime |  | ✗ | Date you want to move the payment to |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Plan ID | `planId` | string |  | ✓ | Filter: The subscription plan ID |  |

---

## Load Options Methods

- `getPayments`

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
* Categories: Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: paddle
displayName: Paddle
description: Consume Paddle API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: paddleApi
  required: true
operations:
- id: create
  name: Create
  description: Create a coupon
  params:
  - id: couponType
    name: Coupon Type
    type: options
    default: checkout
    required: false
    description: Either product (valid for specified products or subscription plans)
      or checkout (valid for any checkout)
    validation:
      displayOptions:
        show:
          resource:
          - coupon
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: options
      displayName: Coupon Type
      name: couponType
      possibleValues:
      - value: checkout
        name: Checkout
        description: ''
      - value: product
        name: Product
        description: ''
  - id: productIds
    name: Product Names or IDs
    type: multiOptions
    default: []
    required: true
    description: Comma-separated list of product IDs. Required if coupon_type is product.
      Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - coupon
          operation:
          - create
          couponType:
          - product
          jsonParameters:
          - false
    typeInfo:
      type: multiOptions
      displayName: Product Names or IDs
      name: productIds
      typeOptions:
        loadOptionsMethod: getProducts
      possibleValues: []
  - id: discountType
    name: Discount Type
    type: options
    default: flat
    required: false
    description: Either flat or percentage
    validation:
      displayOptions:
        show:
          resource:
          - coupon
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: options
      displayName: Discount Type
      name: discountType
      possibleValues:
      - value: flat
        name: Flat
        description: ''
      - value: percentage
        name: Percentage
        description: ''
  - id: discountAmount
    name: Discount Amount Currency
    type: number
    default: 1
    required: false
    description: Discount amount in currency
    validation: &id001
      displayOptions:
        show:
          resource:
          - coupon
          operation:
          - create
          discountType:
          - percentage
          jsonParameters:
          - false
    typeInfo: &id002
      type: number
      displayName: Discount Amount %
      name: discountAmount
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: discountAmount
    name: Discount Amount %
    type: number
    default: 1
    required: false
    description: Discount amount in percentage
    validation: *id001
    typeInfo: *id002
  - id: currency
    name: Currency
    type: options
    default: EUR
    required: false
    description: The currency must match the balance currency specified in your account
    validation:
      displayOptions:
        show:
          resource:
          - coupon
          operation:
          - create
          discountType:
          - flat
          jsonParameters:
          - false
    typeInfo:
      type: options
      displayName: Currency
      name: currency
      possibleValues:
      - value: ARS
        name: ARS
        description: ''
      - value: AUD
        name: AUD
        description: ''
      - value: BRL
        name: BRL
        description: ''
      - value: CAD
        name: CAD
        description: ''
      - value: CHF
        name: CHF
        description: ''
      - value: CNY
        name: CNY
        description: ''
      - value: CZK
        name: CZK
        description: ''
      - value: DKK
        name: DKK
        description: ''
      - value: EUR
        name: EUR
        description: ''
      - value: GBP
        name: GBP
        description: ''
      - value: HKD
        name: HKD
        description: ''
      - value: HUF
        name: HUF
        description: ''
      - value: INR
        name: INR
        description: ''
      - value: JPY
        name: JPY
        description: ''
      - value: KRW
        name: KRW
        description: ''
      - value: MXN
        name: MXN
        description: ''
      - value: NOK
        name: NOK
        description: ''
      - value: NZD
        name: NZD
        description: ''
      - value: PLN
        name: PLN
        description: ''
      - value: RUB
        name: RUB
        description: ''
      - value: SEK
        name: SEK
        description: ''
      - value: SGD
        name: SGD
        description: ''
      - value: THB
        name: THB
        description: ''
      - value: TWD
        name: TWD
        description: ''
      - value: USD
        name: USD
        description: ''
      - value: ZAR
        name: ZAR
        description: ''
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id007
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
    typeInfo: &id008
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Attributes in JSON form
    validation: &id009
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
          jsonParameters:
          - true
    typeInfo: &id010
      type: json
      displayName: Additional Fields
      name: additionalFieldsJson
      typeOptions:
        alwaysOpenEditWindow: true
- id: getAll
  name: Get Many
  description: Get many coupons
  params:
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: true
    description: The specific product/subscription ID
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - coupon
          operation:
          - getAll
    typeInfo:
      type: string
      displayName: Product ID
      name: productId
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id003
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 200
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Attributes in JSON form
    validation: *id009
    typeInfo: *id010
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 100
    required: true
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Attributes in JSON form
    validation: *id009
    typeInfo: *id010
- id: update
  name: Update
  description: Update a coupon
  params:
  - id: updateBy
    name: Update By
    type: options
    default: couponCode
    required: false
    description: Either flat or percentage
    validation:
      displayOptions:
        show:
          resource:
          - coupon
          operation:
          - update
          jsonParameters:
          - false
    typeInfo:
      type: options
      displayName: Update By
      name: updateBy
      possibleValues:
      - value: couponCode
        name: Coupon Code
        description: ''
      - value: group
        name: Group
        description: ''
  - id: couponCode
    name: Coupon Code
    type: string
    default: ''
    required: false
    description: Identify the coupon to update
    validation:
      displayOptions:
        show:
          resource:
          - coupon
          operation:
          - update
          updateBy:
          - couponCode
          jsonParameters:
          - false
    typeInfo:
      type: string
      displayName: Coupon Code
      name: couponCode
  - id: group
    name: Group
    type: string
    default: ''
    required: false
    description: The name of the group of coupons you want to update
    validation:
      displayOptions:
        show:
          resource:
          - coupon
          operation:
          - update
          updateBy:
          - group
          jsonParameters:
          - false
    typeInfo:
      type: string
      displayName: Group
      name: group
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Attributes in JSON form
    validation: *id009
    typeInfo: *id010
- id: reschedule
  name: Reschedule
  description: Reschedule payment
  params:
  - id: paymentId
    name: Payment Name or ID
    type: options
    default: ''
    required: true
    description: The upcoming subscription payment ID. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - payment
          operation:
          - reschedule
    typeInfo:
      type: options
      displayName: Payment Name or ID
      name: paymentId
      typeOptions:
        loadOptionsMethod: getPayments
      possibleValues: []
  - id: date
    name: Date
    type: dateTime
    default: ''
    required: false
    description: Date you want to move the payment to
    validation:
      displayOptions:
        show:
          resource:
          - payment
          operation:
          - reschedule
    typeInfo:
      type: dateTime
      displayName: Date
      name: date
- id: get
  name: Get
  description: Get a plan
  params:
  - id: planId
    name: Plan ID
    type: string
    default: ''
    required: true
    description: 'Filter: The subscription plan ID'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - plan
          operation:
          - get
    typeInfo:
      type: string
      displayName: Plan ID
      name: planId
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - content-type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
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
  "$id": "https://n8n.io/schemas/nodes/paddle.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Paddle Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "getAll",
        "update",
        "reschedule",
        "get"
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
            "coupon",
            "payment",
            "plan",
            "product",
            "order",
            "user"
          ],
          "default": "coupon"
        },
        "operation": {
          "description": "Get many users",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "getAll"
        },
        "couponType": {
          "description": "Either product (valid for specified products or subscription plans) or checkout (valid for any checkout)",
          "type": "string",
          "enum": [
            "checkout",
            "product"
          ],
          "default": "checkout"
        },
        "productIds": {
          "description": "Comma-separated list of product IDs. Required if coupon_type is product. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "discountType": {
          "description": "Either flat or percentage",
          "type": "string",
          "enum": [
            "flat",
            "percentage"
          ],
          "default": "flat"
        },
        "discountAmount": {
          "description": "Discount amount in percentage",
          "type": "number",
          "default": 1
        },
        "currency": {
          "description": "The currency must match the balance currency specified in your account",
          "type": "string",
          "enum": [
            "ARS",
            "AUD",
            "BRL",
            "CAD",
            "CHF",
            "CNY",
            "CZK",
            "DKK",
            "EUR",
            "GBP",
            "HKD",
            "HUF",
            "INR",
            "JPY",
            "KRW",
            "MXN",
            "NOK",
            "NZD",
            "PLN",
            "RUB",
            "SEK",
            "SGD",
            "THB",
            "TWD",
            "USD",
            "ZAR"
          ],
          "default": "EUR"
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "additionalFieldsJson": {
          "description": "Attributes in JSON form",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Filter: The subscription plan ID",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "productId": {
          "description": "The specific product/subscription ID",
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
        "updateBy": {
          "description": "Either flat or percentage",
          "type": "string",
          "enum": [
            "couponCode",
            "group"
          ],
          "default": "couponCode"
        },
        "couponCode": {
          "description": "Identify the coupon to update",
          "type": "string",
          "default": ""
        },
        "group": {
          "description": "The name of the group of coupons you want to update",
          "type": "string",
          "default": ""
        },
        "paymentId": {
          "description": "The upcoming subscription payment ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "date": {
          "description": "Date you want to move the payment to",
          "type": "string",
          "default": ""
        },
        "planId": {
          "description": "Filter: The subscription plan ID",
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
      "name": "paddleApi",
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
