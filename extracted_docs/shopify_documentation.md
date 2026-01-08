---
title: "Node: Shopify"
slug: "node-shopify"
version: "1"
updated: "2026-01-08"
summary: "Consume Shopify API"
node_type: "regular"
group: "['output']"
---

# Node: Shopify

**Purpose.** Consume Shopify API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:shopify.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **shopifyApi**: N/A
- **shopifyAccessTokenApi**: N/A
- **shopifyOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **apiVersion**: Shopify API Version: 2024-07

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `shopifyApi` | ✓ | {'show': {'authentication': ['apiKey']}} |
| `shopifyAccessTokenApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `shopifyOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Order Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an order |
| Delete | `delete` | Delete an order |
| Get | `get` | Get an order |
| Get Many | `getAll` | Get many orders |
| Update | `update` | Update an order |

### Product Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a product |
| Delete | `delete` | Delete a product |
| Get | `get` | Get a product |
| Get Many | `getAll` | Get many products |
| Update | `update` | Update a product |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | order | ✗ | Resource to operate on |  |

**Resource options:**

* **Order** (`order`)
* **Product** (`product`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create an order |  |

**Operation options:**

* **Create** (`create`) - Create an order
* **Delete** (`delete`) - Delete an order
* **Get** (`get`) - Get an order
* **Get Many** (`getAll`) - Get many orders
* **Update** (`update`) - Update an order

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The amount that's deducted from the order total | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Billing Address | `billingAddressUi` | fixedCollection | {} |  |
| Discount Codes | `discountCodesUi` | fixedCollection | {} | The amount that's deducted from the order total |
| Email | `email` | string |  | The customer's email address |
| Fulfillment Status | `fulfillmentStatus` | options |  | Every line item in the order has been fulfilled |
| Inventory Behaviour | `inventoryBehaviour` | options | bypass | Do not claim inventory |
| Location Name or ID | `locationId` | options |  | The ID of the physical location where the order was processed. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Note | `note` | string |  | An optional note that a shop owner can attach to the order |
| Send Fulfillment Receipt | `sendFulfillmentReceipt` | boolean | False | Whether to send a shipping confirmation to the customer |
| Send Receipt | `sendReceipt` | boolean | False | Whether to send an order confirmation to the customer |
| Shipping Address | `shippingAddressUi` | fixedCollection | {} |  |
| Source Name | `sourceName` | string |  | Where the order originated. Can be set only during order creation, and is not writeable afterwards. |
| Tags | `tags` | string |  | Tags attached to the order, formatted as a string of comma-separated values |
| Test | `test` | boolean | False | Whether this is a test order |

</details>

| Line Items | `limeItemsUi` | fixedCollection | {} | ✗ | The ID of the product that the line item belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Line Item |  |

<details>
<summary><strong>Line Items sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Line Item | `lineItemValues` |  |  |  |

</details>

| Title | `title` | string |  | ✓ | The name of the product |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | A description of the product. Supports HTML formatting. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body HTML | `body_html` | string |  | A description of the product. Supports HTML formatting. |
| Handle | `handle` | string |  | A unique human-friendly string for the product. Automatically generated from the product's title. Used by the Liquid templating language to refer to objects. |
| Images | `images` | collection | {} | A list of product image objects, each one representing an image associated with the product |
| Options | `productOptions` | fixedCollection | {} | The custom product property names like Size, Color, and Material. You can add up to 3 options of up to 255 characters each. |
| Product Type | `product_type` | string |  | A categorization for the product used for filtering and searching products |
| Published At | `published_at` | dateTime |  | The date and time (ISO 8601 format) when the product was published. Can be set to null to unpublish the product from the Online Store channel. |
| Published Scope | `published_scope` | options |  | The product is published to both the Online Store channel and the Point of Sale channel |
| Tags | `tags` | string |  | A string of comma-separated tags that are used for filtering and search. A product can have up to 250 tags. Each tag can have up to 255 characters. |
| Template Suffix | `template_suffix` | string |  | The suffix of the Liquid template used for the product page. If this property is specified, then the product page uses a template called "product.suffix.liquid", where "suffix" is the value of this property. If this property is "" or null, then the product page uses the default template "product.liquid". (default: null) |
| Variants | `variants` | collection | {} | A list of product variants, each representing a different version of the product. |
| Vendor | `vendor` | string |  | The name of the product's vendor |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Order ID | `orderId` | string |  | ✓ |  |  |
| Product ID | `productId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Order ID | `orderId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | Fields the order will return, formatted as a string of comma-separated values. By default all the fields are returned. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Fields the order will return, formatted as a string of comma-separated values. By default all the fields are returned. |

</details>

| Product ID | `productId` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields the product will return, formatted as a string of comma-separated values. By default all the fields are returned. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Fields the product will return, formatted as a string of comma-separated values. By default all the fields are returned. |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:250 |
| Options | `options` | collection | {} | ✗ | Show orders attributed to a certain app, specified by the app ID. Set as current to show orders for the app currently consuming the API. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attribution App ID | `attributionAppId` | string |  | Show orders attributed to a certain app, specified by the app ID. Set as current to show orders for the app currently consuming the API. |
| Created At Min | `createdAtMin` | dateTime |  | Show orders created at or after date |
| Created At Max | `createdAtMax` | dateTime |  | Show orders created at or before date |
| Financial Status | `financialStatus` | options | any | Show orders of any financial status |
| Fulfillment Status | `fulfillmentStatus` | options | any | Show orders of any fulfillment status |
| Fields | `fields` | string |  | Fields the orders will return, formatted as a string of comma-separated values. By default all the fields are returned. |
| IDs | `ids` | string |  | Retrieve only orders specified by a comma-separated list of order IDs |
| Processed At Max | `processedAtMax` | dateTime |  | Show orders imported at or before date |
| Processed At Min | `processedAtMin` | dateTime |  | Show orders imported at or after date |
| Status | `status` | options | open | Show orders of any status, including archived orders |
| Since ID | `sinceId` | string |  | Show orders after the specified ID |
| Updated At Max | `updatedAtMax` | dateTime |  | Show orders last updated at or after date |
| Updated At Min | `updatedAtMin` | dateTime |  | Show orders last updated at or before date |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:250 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Filter results by product collection ID | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Collection ID | `collection_id` | string |  | Filter results by product collection ID |
| Created At Max | `created_at_max` | dateTime |  | Show products created before date |
| Created At Min | `created_at_min` | dateTime |  | Show products created after date |
| Fields | `fields` | string |  | Show only certain fields, specified by a comma-separated list of field names |
| Handle | `handle` | string |  | Filter results by product handle |
| IDs | `ids` | string |  | Return only products specified by a comma-separated list of product IDs |
| Presentment Currencies | `presentment_currencies` | string |  | Return presentment prices in only certain currencies, specified by a comma-separated list of ISO 4217 currency codes |
| Product Type | `product_type` | string |  | Filter results by product type |
| Published At Max | `published_at_max` | dateTime |  | Show products published before date |
| Published At Min | `published_at_min` | dateTime |  | Show products published after date |
| Published Status | `published_status` | options | any | Show all products |
| Title | `title` | string |  | Filter results by product title |
| Updated At Max | `updated_at_max` | dateTime |  | Show products last updated before date |
| Updated At Min | `updated_at_min` | dateTime |  | Show products last updated after date |
| Vendor | `vendor` | string |  | Filter results by product vendor |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Order ID | `orderId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The customer's email address | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  | The customer's email address |
| Location Name or ID | `locationId` | options |  | The ID of the physical location where the order was processed. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Note | `note` | string |  | An optional note that a shop owner can attach to the order |
| Shipping Address | `shippingAddressUi` | fixedCollection | {} |  |
| Source Name | `sourceName` | string |  | Where the order originated. Can be set only during order creation, and is not writeable afterwards. |
| Tags | `tags` | string |  | Tags attached to the order, formatted as a string of comma-separated values |

</details>

| Product ID | `productId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | A description of the product. Supports HTML formatting. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body HTML | `body_html` | string |  | A description of the product. Supports HTML formatting. |
| Handle | `handle` | string |  | A unique human-friendly string for the product. Automatically generated from the product's title. Used by the Liquid templating language to refer to objects. |
| Images | `images` | collection | {} | A list of product image objects, each one representing an image associated with the product |
| Options | `productOptions` | fixedCollection | {} | The custom product property names like Size, Color, and Material. You can add up to 3 options of up to 255 characters each. |
| Product Type | `product_type` | string |  | A categorization for the product used for filtering and searching products |
| Published At | `published_at` | dateTime |  | The date and time (ISO 8601 format) when the product was published. Can be set to null to unpublish the product from the Online Store channel. |
| Published Scope | `published_scope` | options |  | The product is published to both the Online Store channel and the Point of Sale channel |
| Tags | `tags` | string |  | A string of comma-separated tags that are used for filtering and search. A product can have up to 250 tags. Each tag can have up to 255 characters. |
| Template Suffix | `template_suffix` | string |  | The suffix of the Liquid template used for the product page. If this property is specified, then the product page uses a template called "product.suffix.liquid", where "suffix" is the value of this property. If this property is "" or null, then the product page uses the default template "product.liquid". (default: null) |
| Title | `title` | string |  | The name of the product |
| Variants | `variants` | collection | {} | A list of product variants, each representing a different version of the product. |
| Vendor | `vendor` | string |  | The name of the product's vendor |

</details>


---

## Load Options Methods

- `getProducts`

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
node: shopify
displayName: Shopify
description: Consume Shopify API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: shopifyApi
  required: true
- name: shopifyAccessTokenApi
  required: true
- name: shopifyOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create an order
  params:
  - id: limeItemsUi
    name: Line Items
    type: fixedCollection
    default: {}
    required: false
    description: The ID of the product that the line item belongs to. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    placeholder: Add Line Item
    validation:
      displayOptions:
        show:
          resource:
          - order
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Line Items
      name: limeItemsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: lineItemValues
        displayName: Line Item
        values:
        - displayName: Product Name or ID
          name: productId
          type: options
          description: The ID of the product that the line item belongs to. Choose
            from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: ''
          typeOptions:
            loadOptionsMethod: getProducts
        - displayName: Variant ID
          name: variantId
          type: string
          description: The ID of the product variant
          default: ''
        - displayName: Title
          name: title
          type: string
          description: The title of the product
          default: ''
        - displayName: Grams
          name: grams
          type: string
          description: The weight of the item in grams
          default: ''
        - displayName: Quantity
          name: quantity
          type: number
          description: The number of items that were purchased
          default: 1
          typeOptions:
            minValue: 1
        - displayName: Price
          name: price
          type: string
          default: ''
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The name of the product
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - product
    typeInfo:
      type: string
      displayName: Title
      name: title
- id: delete
  name: Delete
  description: Delete an order
  params:
  - id: orderId
    name: Order ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - order
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: Order ID
      name: orderId
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - product
          operation:
          - get
    typeInfo: &id004
      type: string
      displayName: Product ID
      name: productId
- id: get
  name: Get
  description: Get an order
  params:
  - id: orderId
    name: Order ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: Get many orders
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
          - product
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
          - product
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
        maxValue: 250
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
- id: update
  name: Update
  description: Update an order
  params:
  - id: orderId
    name: Order ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: productId
    name: Product ID
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
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: apiVersion
    text: 'Shopify API Version: 2024-07'
    conditions: null
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: limeItemsUi
    text: Add Line Item
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/shopify.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Shopify Node",
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
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "accessToken",
            "oAuth2",
            "apiKey"
          ],
          "default": "apiKey"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "order",
            "product"
          ],
          "default": "order"
        },
        "operation": {
          "description": "Create a product",
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
        "additionalFields": {
          "description": "Filter results by product collection ID",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "limeItemsUi": {
          "description": "The ID of the product that the line item belongs to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Line Item"
          ]
        },
        "orderId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Show orders attributed to a certain app, specified by the app ID. Set as current to show orders for the app currently consuming the API.",
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
          "default": 50
        },
        "updateFields": {
          "description": "A description of the product. Supports HTML formatting.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "title": {
          "description": "The name of the product",
          "type": "string",
          "default": ""
        },
        "productId": {
          "description": "",
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
      "name": "shopifyApi",
      "required": true
    },
    {
      "name": "shopifyAccessTokenApi",
      "required": true
    },
    {
      "name": "shopifyOAuth2Api",
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
