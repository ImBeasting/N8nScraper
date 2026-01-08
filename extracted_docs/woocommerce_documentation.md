---
title: "Node: WooCommerce"
slug: "node-woocommerce"
version: "1"
updated: "2026-01-08"
summary: "Consume WooCommerce API"
node_type: "regular"
group: "['output']"
---

# Node: WooCommerce

**Purpose.** Consume WooCommerce API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:wooCommerce.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **wooCommerceApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `wooCommerceApi` | ✓ | - |

---

## Operations

### Customer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a customer |
| Delete | `delete` | Delete a customer |
| Get | `get` | Retrieve a customer |
| Get Many | `getAll` | Retrieve many customers |
| Update | `update` | Update a customer |

### Product Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a product |
| Delete | `delete` | Delete a product |
| Get | `get` | Get a product |
| Get Many | `getAll` | Get many products |
| Update | `update` | Update a product |

### Order Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a order |
| Delete | `delete` | Delete a order |
| Get | `get` | Get a order |
| Get Many | `getAll` | Get many orders |
| Update | `update` | Update a order |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | product | ✗ | Resource to operate on |  |

**Resource options:**

* **Customer** (`customer`)
* **Order** (`order`)
* **Product** (`product`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a customer |  |

**Operation options:**

* **Create** (`create`) - Create a customer
* **Delete** (`delete`) - Delete a customer
* **Get** (`get`) - Retrieve a customer
* **Get Many** (`getAll`) - Retrieve many customers
* **Update** (`update`) - Update a customer

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Name | `name` | string |  | ✓ | Product name |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | If managing stock, this controls if backorders are allowed | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Backorders | `backorders` | options | no | If managing stock, this controls if backorders are allowed |
| Button Text | `buttonText` | string |  | Product external button text. Only for external products. |
| Catalog Visibility | `catalogVisibility` | options | visible |  |
| Category Names or IDs | `categories` | multiOptions | [] | List of categories. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Cross Sell IDs | `crossSellIds` | string |  | List of cross-sell products IDs. Multiple can be added separated by ,. |
| Date On Sale From | `dateOnSaleFrom` | dateTime |  | Start date of sale price, in the site's timezone |
| Date On Sale To | `dateOnSaleTo` | dateTime |  | Ennd date of sale price, in the site's timezone |
| Description | `description` | string |  | Product description |
| Downloadable | `downloadable` | boolean | False | Whether the product is downloadable |
| External URL | `externalUrl` | string |  | Product external URL. Only for external products. |
| Featured | `featured` | boolean | False | Whether the product is featured |
| Manage Stock | `manageStock` | boolean | False | Stock management at product level |
| Menu Order | `menuOrder` | number | 1 | Menu order, used to custom sort products |
| Parent ID | `parentId` | string |  | Product parent ID |
| Purchase Note | `purchaseNote` | string |  | Optional note to send the customer after purchase |
| Regular Price | `regularPrice` | string |  | Product regular price |
| Reviews Allowed | `reviewsAllowed` | boolean | True | Whether to allow reviews |
| Sale Price | `salePrice` | string |  | Product sale price |
| Shipping Class | `shippingClass` | string |  | Shipping class slug |
| Short Description | `shortDescription` | string |  | Product short description |
| SKU | `sku` | string |  | Unique identifier |
| Slug | `slug` | string |  | Product slug |
| Sold Individually | `soldIndividually` | boolean | False | Whether to allow one item to be bought in a single order |
| Status | `status` | options | publish | A named status for the product |
| Stock Quantity | `stockQuantity` | number | 1 |  |
| Stock Status | `stockStatus` | options | instock | Controls the stock status of the product |
| Tag Names or IDs | `tags` | multiOptions | [] | List of tags. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Tax Class | `taxClass` | string |  |  |
| Tax Status | `taxStatus` | options | taxable |  |
| Type | `type` | options | simple | Product type |
| Upsell IDs | `upsellIds` | string |  | List of up-sell products IDs. Multiple can be added separated by ,. |
| Virtual | `virtual` | boolean | False | Whether the product is virtual |
| Weight | `weight` | string |  | Product weight |

</details>

| Dimensions | `dimensionsUi` | fixedCollection | {} | ✗ | Product dimensions | e.g. Add Dimension |  |

<details>
<summary><strong>Dimensions sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Dimension | `dimensionsValues` |  |  |  |

</details>

| Images | `imagesUi` | fixedCollection | {} | ✗ | Product Image | e.g. Add Image |  |

<details>
<summary><strong>Images sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Image | `imagesValues` |  |  |  |

</details>

| Metadata | `metadataUi` | fixedCollection | {} | ✗ | Meta data | e.g. Add Metadata |  |

<details>
<summary><strong>Metadata sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Metadata | `metadataValues` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Currency the order was created with | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Currency | `currency` | string |  | Currency the order was created with |
| Customer ID | `customerId` | string |  | User ID who owns the order. 0 for guests. |
| Customer Note | `customerNote` | string |  | Note left by customer during checkout |
| Parent ID | `parentId` | string |  | Parent order ID |
| Payment Method ID | `paymentMethodId` | string |  |  |
| Payment Method Title | `paymentMethodTitle` | string |  |  |
| Set Paid | `setPaid` | boolean | False | Whether the order is paid. It will set the status to processing and reduce stock items. |
| Status | `status` | options | pending | A named status for the order |
| Transaction ID | `transactionID` | string |  | Unique transaction ID |

</details>

| Billing | `billingUi` | fixedCollection | {} | ✗ | Billing address | e.g. Add Billing |  |

<details>
<summary><strong>Billing sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `billingValues` |  |  |  |

</details>

| Coupon Lines | `couponLinesUi` | fixedCollection | {} | ✗ | Coupons line data | e.g. Add Coupon Line |  |

<details>
<summary><strong>Coupon Lines sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Coupon Line | `couponLinesValues` |  |  |  |

</details>

| Fee Lines | `feeLinesUi` | fixedCollection | {} | ✗ | Fee line data | e.g. Add Fee Line |  |

<details>
<summary><strong>Fee Lines sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fee Line | `feeLinesValues` |  |  |  |

</details>

| Line Items | `lineItemsUi` | fixedCollection | {} | ✗ | Line item data | e.g. Add Line Item |  |

<details>
<summary><strong>Line Items sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Line Item | `lineItemsValues` |  |  |  |

</details>

| Metadata | `metadataUi` | fixedCollection | {} | ✗ | Meta data | e.g. Add Metadata |  |

<details>
<summary><strong>Metadata sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Metadata | `metadataValues` |  |  |  |

</details>

| Shipping | `shippingUi` | fixedCollection | {} | ✗ | Shipping address | e.g. Add Shipping |  |

<details>
<summary><strong>Shipping sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `shippingValues` |  |  |  |

</details>

| Shipping Lines | `shippingLinesUi` | fixedCollection | {} | ✗ | Shipping line data | e.g. Add Shipping Line |  |

<details>
<summary><strong>Shipping Lines sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fee Line | `shippingLinesValues` |  |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Customer ID | `customerId` | string |  | ✓ | ID of the customer to delete |  |
| Product ID | `productId` | string |  | ✗ |  |  |
| Order ID | `orderId` | string |  | ✗ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Customer ID | `customerId` | string |  | ✓ | ID of the customer to retrieve |  |
| Product ID | `productId` | string |  | ✗ |  |  |
| Order ID | `orderId` | string |  | ✗ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Email address to filter customers by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  | Email address to filter customers by |
| Sort Order | `order` | options | asc | Order to sort customers in |
| Order By | `orderby` | options | id | Field to sort customers by |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Limit response to resources published after a given ISO8601 compliant date | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| After | `after` | dateTime |  | Limit response to resources published after a given ISO8601 compliant date |
| Before | `before` | dateTime |  | Limit response to resources published before a given ISO8601 compliant date |
| Category Name or ID | `category` | options |  | Limit result set to products assigned a specific category ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Context | `context` | options | view | Scope under which the request is made; determines fields present in response |
| Featured | `featured` | boolean | False | Whether to limit the result set to featured products |
| Max Price | `maxPrice` | string |  | Limit result set to products based on a maximun price |
| Min Price | `minPrice` | string |  | Limit result set to products based on a minimum price |
| Order | `order` | options | desc | Order sort attribute ascending or descending |
| Order By | `orderBy` | options | id | Sort collection by object attribute |
| Search | `search` | string |  | Limit results to those matching a string |
| SKU | `sku` | string |  | Limit result set to products with a specific SKU |
| Slug | `slug` | string |  | Limit result set to products with a specific slug |
| Status | `status` | options | any | Limit result set to products assigned a specific status |
| Stock Status | `stockStatus` | options |  | Controls the stock status of the product |
| Tag Name or ID | `tag` | options | [] | Limit result set to products assigned a specific tag ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Tax Class | `taxClass` | options |  | Limit result set to products with a specific tax class |
| Type | `type` | options | simple | Product type |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Limit response to resources published after a given ISO8601 compliant date | e.g. Add option | min:0, max:10 |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| After | `after` | dateTime |  | Limit response to resources published after a given ISO8601 compliant date |
| Before | `before` | dateTime |  | Limit response to resources published before a given ISO8601 compliant date |
| Customer | `customer` | string |  | Limit result set to orders assigned a specific customer |
| Decimal Points | `decimalPoints` | number | 2 | Number of decimal points to use in each resource |
| Order | `order` | options | desc | Order sort attribute ascending or descending |
| Product | `product` | string |  | Limit result set to orders assigned a specific product |
| Order By | `orderBy` | options | id | Sort collection by object attribute |
| Search | `search` | string |  | Limit results to those matching a string |
| Status | `status` | options | any | Limit result set to orders assigned a specific status |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Customer ID | `customerId` | string |  | ✓ | ID of the customer to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |
| Product ID | `productId` | string |  | ✗ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | If managing stock, this controls if backorders are allowed | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Backorders | `backorders` | options | no | If managing stock, this controls if backorders are allowed |
| Button Text | `buttonText` | string |  | Product external button text. Only for external products. |
| Catalog Visibility | `catalogVisibility` | options | visible |  |
| Category Names or IDs | `categories` | multiOptions | [] | List of categories. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Cross Sell IDs | `crossSellIds` | string |  | List of cross-sell products IDs. Multiple can be added separated by ,. |
| Date On Sale From | `dateOnSaleFrom` | dateTime |  | Start date of sale price, in the site's timezone |
| Date On Sale To | `dateOnSaleTo` | dateTime |  | Ennd date of sale price, in the site's timezone |
| Description | `description` | string |  | Product description |
| Downloadable | `downloadable` | boolean | False | Whether the product is downloadable |
| External URL | `externalUrl` | string |  | Product external URL. Only for external products. |
| Featured | `featured` | boolean | False | Whether the product is featured |
| Manage Stock | `manageStock` | boolean | False | Stock management at product level |
| Menu Order | `menuOrder` | number | 1 | Menu order, used to custom sort products |
| Name | `name` | string |  | Product name |
| Parent ID | `parentId` | string |  | Product parent ID |
| Purchase Note | `purchaseNote` | string |  | Optional note to send the customer after purchase |
| Regular Price | `regularPrice` | string |  | Product regular price |
| Reviews Allowed | `reviewsAllowed` | boolean | True | Whether to allow reviews |
| Sale Price | `salePrice` | string |  | Product sale price |
| Shipping Class | `shippingClass` | string |  | Shipping class slug |
| Short Description | `shortDescription` | string |  | Product short description |
| SKU | `sku` | string |  | Unique identifier |
| Slug | `slug` | string |  | Product slug |
| Sold Individually | `soldIndividually` | boolean | False | Whether to allow one item to be bought in a single order |
| Status | `status` | options | publish | A named status for the product |
| Stock Quantity | `stockQuantity` | number | 1 |  |
| Stock Status | `stockStatus` | options | instock | Controls the stock status of the product |
| Tag Names or IDs | `tags` | multiOptions | [] | List of tags. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Tax Class | `taxClass` | string |  |  |
| Tax Status | `taxStatus` | options | taxable |  |
| Type | `type` | options | simple | Product type |
| Upsell IDs | `upsellIds` | string |  | List of up-sell products IDs. Multiple can be added separated by ,. |
| Virtual | `virtual` | boolean | False | Whether the product is virtual |
| Weight | `weight` | string |  | Product weight |

</details>

| Dimensions | `dimensionsUi` | fixedCollection | {} | ✗ | Product dimensions | e.g. Add Dimension |  |

<details>
<summary><strong>Dimensions sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Dimension | `dimensionsValues` |  |  |  |

</details>

| Images | `imagesUi` | fixedCollection | {} | ✗ | Product Image | e.g. Add Image |  |

<details>
<summary><strong>Images sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Image | `imagesValues` |  |  |  |

</details>

| Metadata | `metadataUi` | fixedCollection | {} | ✗ | Meta data | e.g. Add Metadata |  |

<details>
<summary><strong>Metadata sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Metadata | `metadataValues` |  |  |  |

</details>

| Order ID | `orderId` | string |  | ✗ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Currency the order was created with | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Currency | `currency` | string |  | Currency the order was created with |
| Customer ID | `customerId` | string |  | User ID who owns the order. 0 for guests. |
| Customer Note | `customerNote` | string |  | Note left by customer during checkout |
| Parent ID | `parentId` | string |  | Parent order ID |
| Payment Method ID | `paymentMethodId` | string |  |  |
| Payment Method Title | `paymentMethodTitle` | string |  |  |
| Status | `status` | options | pending | A named status for the order |
| Transaction ID | `transactionID` | string |  | Unique transaction ID |

</details>

| Billing | `billingUi` | fixedCollection | {} | ✗ | Billing address | e.g. Add Billing |  |

<details>
<summary><strong>Billing sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `billingValues` |  |  |  |

</details>

| Coupon Lines | `couponLinesUi` | fixedCollection | {} | ✗ | Coupons line data | e.g. Add Coupon Line |  |

<details>
<summary><strong>Coupon Lines sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Coupon Line | `couponLinesValues` |  |  |  |

</details>

| Fee Lines | `feeLinesUi` | fixedCollection | {} | ✗ | Fee line data | e.g. Add Fee Line |  |

<details>
<summary><strong>Fee Lines sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fee Line | `feeLinesValues` |  |  |  |

</details>

| Line Items | `lineItemsUi` | fixedCollection | {} | ✗ | Line item data | e.g. Add Line Item |  |

<details>
<summary><strong>Line Items sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Line Item | `lineItemsValues` |  |  |  |

</details>

| Metadata | `metadataUi` | fixedCollection | {} | ✗ | Meta data | e.g. Add Metadata |  |

<details>
<summary><strong>Metadata sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Metadata | `metadataValues` |  |  |  |

</details>

| Shipping | `shippingUi` | fixedCollection | {} | ✗ | Shipping address | e.g. Add Shipping |  |

<details>
<summary><strong>Shipping sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `shippingValues` |  |  |  |

</details>

| Shipping Lines | `shippingLinesUi` | fixedCollection | {} | ✗ | Shipping line data | e.g. Add Shipping Line |  |

<details>
<summary><strong>Shipping Lines sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fee Line | `shippingLinesValues` |  |  |  |

</details>


---

## Load Options Methods

- `getCategories`

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
node: wooCommerce
displayName: WooCommerce
description: Consume WooCommerce API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: wooCommerceApi
  required: true
operations:
- id: create
  name: Create
  description: Create a customer
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: ''
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - customer
          operation:
          - create
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Product name
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - product
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: dimensionsUi
    name: Dimensions
    type: fixedCollection
    default: {}
    required: false
    description: Product dimensions
    placeholder: Add Dimension
    validation: &id013
      displayOptions:
        show:
          resource:
          - product
          operation:
          - update
    typeInfo: &id014
      type: fixedCollection
      displayName: Dimensions
      name: dimensionsUi
      typeOptions:
        multipleValues: false
      subProperties:
      - name: dimensionsValues
        displayName: Dimension
        values:
        - displayName: Height
          name: height
          type: string
          description: Product height
          default: ''
        - displayName: Length
          name: length
          type: string
          description: Product length
          default: ''
        - displayName: Width
          name: width
          type: string
          description: Product width
          default: ''
  - id: imagesUi
    name: Images
    type: fixedCollection
    default: {}
    required: false
    description: Product Image
    placeholder: Add Image
    validation: &id015
      displayOptions:
        show:
          resource:
          - product
          operation:
          - update
    typeInfo: &id016
      type: fixedCollection
      displayName: Images
      name: imagesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: imagesValues
        displayName: Image
        values:
        - displayName: Alt
          name: alt
          type: string
          description: Image alternative text
          default: ''
        - displayName: Src
          name: src
          type: string
          description: Image URL
          default: ''
        - displayName: Name
          name: name
          type: string
          description: Image name
          default: ''
  - id: metadataUi
    name: Metadata
    type: fixedCollection
    default: {}
    required: false
    description: Meta data
    placeholder: Add Metadata
    validation: &id001
      displayOptions:
        show:
          resource:
          - order
          operation:
          - update
    typeInfo: &id002
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
  - id: billingUi
    name: Billing
    type: fixedCollection
    default: {}
    required: false
    description: Billing address
    placeholder: Add Billing
    validation: &id017
      displayOptions:
        show:
          resource:
          - order
          operation:
          - update
    typeInfo: &id018
      type: fixedCollection
      displayName: Billing
      name: billingUi
      typeOptions:
        multipleValues: false
      subProperties:
      - name: billingValues
        displayName: Address
        values:
        - displayName: First Name
          name: firstName
          type: string
          default: ''
        - displayName: Last Name
          name: lastName
          type: string
          default: ''
        - displayName: Company
          name: company
          type: string
          default: ''
        - displayName: Address Line 1
          name: address_1
          type: string
          default: ''
        - displayName: Address Line 2
          name: address_2
          type: string
          default: ''
        - displayName: City
          name: city
          type: string
          description: ISO code or name of the state, province or district
          default: ''
        - displayName: Postal Code
          name: postalCode
          type: string
          default: ''
        - displayName: Country
          name: country
          type: string
          default: ''
        - displayName: Email
          name: email
          type: string
          placeholder: name@email.com
          default: ''
        - displayName: Phone
          name: phone
          type: string
          default: ''
  - id: couponLinesUi
    name: Coupon Lines
    type: fixedCollection
    default: {}
    required: false
    description: Coupons line data
    placeholder: Add Coupon Line
    validation: &id019
      displayOptions:
        show:
          resource:
          - order
          operation:
          - update
    typeInfo: &id020
      type: fixedCollection
      displayName: Coupon Lines
      name: couponLinesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: couponLinesValues
        displayName: Coupon Line
        values:
        - displayName: Code
          name: code
          type: string
          description: Coupon code
          default: ''
        - displayName: Metadata
          name: metadataUi
          type: fixedCollection
          description: Meta data
          placeholder: Add Metadata
          default: {}
          options:
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
          typeOptions:
            multipleValues: true
  - id: feeLinesUi
    name: Fee Lines
    type: fixedCollection
    default: {}
    required: false
    description: Fee line data
    placeholder: Add Fee Line
    validation: &id021
      displayOptions:
        show:
          resource:
          - order
          operation:
          - update
    typeInfo: &id022
      type: fixedCollection
      displayName: Fee Lines
      name: feeLinesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: feeLinesValues
        displayName: Fee Line
        values:
        - displayName: Name
          name: name
          type: string
          description: Fee name
          default: ''
        - displayName: Tax Class
          name: taxClass
          type: string
          description: Tax class of fee
          default: ''
        - displayName: Tax Status
          name: taxStatus
          type: options
          description: Tax class of fee
          value: taxable
          default: ''
          options:
          - name: Taxable
            value: taxable
            displayName: Taxable
          - name: None
            value: none
            displayName: None
        - displayName: Total
          name: total
          type: string
          description: Line total (after discounts)
          default: ''
        - displayName: Metadata
          name: metadataUi
          type: fixedCollection
          description: Meta data
          placeholder: Add Metadata
          default: {}
          options:
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
          typeOptions:
            multipleValues: true
  - id: lineItemsUi
    name: Line Items
    type: fixedCollection
    default: {}
    required: false
    description: Line item data
    placeholder: Add Line Item
    validation: &id023
      displayOptions:
        show:
          resource:
          - order
          operation:
          - update
    typeInfo: &id024
      type: fixedCollection
      displayName: Line Items
      name: lineItemsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: lineItemsValues
        displayName: Line Item
        values:
        - displayName: Name
          name: name
          type: string
          description: Product name
          default: ''
        - displayName: Product ID
          name: productId
          type: number
          default: 0
        - displayName: Variation ID
          name: variationId
          type: number
          description: Variation ID, if applicable
          default: 0
        - displayName: Quantity
          name: quantity
          type: number
          description: Quantity ordered
          default: 1
        - displayName: Tax Class
          name: taxClass
          type: string
          description: Slug of the tax class of product
          default: ''
        - displayName: Subtotal
          name: subtotal
          type: string
          description: Line subtotal (before discounts)
          default: ''
        - displayName: Total
          name: total
          type: string
          description: Line total (after discounts)
          default: ''
        - displayName: Metadata
          name: metadataUi
          type: fixedCollection
          description: Meta data
          placeholder: Add Metadata
          default: {}
          options:
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
          typeOptions:
            multipleValues: true
  - id: metadataUi
    name: Metadata
    type: fixedCollection
    default: {}
    required: false
    description: Meta data
    placeholder: Add Metadata
    validation: *id001
    typeInfo: *id002
  - id: shippingUi
    name: Shipping
    type: fixedCollection
    default: {}
    required: false
    description: Shipping address
    placeholder: Add Shipping
    validation: &id025
      displayOptions:
        show:
          resource:
          - order
          operation:
          - update
    typeInfo: &id026
      type: fixedCollection
      displayName: Shipping
      name: shippingUi
      typeOptions:
        multipleValues: false
      subProperties:
      - name: shippingValues
        displayName: Address
        values:
        - displayName: First Name
          name: firstName
          type: string
          default: ''
        - displayName: Last Name
          name: lastName
          type: string
          default: ''
        - displayName: Company
          name: company
          type: string
          default: ''
        - displayName: Address Line 1
          name: address_1
          type: string
          default: ''
        - displayName: Address Line 2
          name: address_2
          type: string
          default: ''
        - displayName: City
          name: city
          type: string
          description: ISO code or name of the state, province or district
          default: ''
        - displayName: Postal Code
          name: postalCode
          type: string
          default: ''
        - displayName: Country
          name: country
          type: string
          default: ''
  - id: shippingLinesUi
    name: Shipping Lines
    type: fixedCollection
    default: {}
    required: false
    description: Shipping line data
    placeholder: Add Shipping Line
    validation: &id027
      displayOptions:
        show:
          resource:
          - order
          operation:
          - update
    typeInfo: &id028
      type: fixedCollection
      displayName: Shipping Lines
      name: shippingLinesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: shippingLinesValues
        displayName: Fee Line
        values:
        - displayName: Method Title
          name: methodTitle
          type: string
          description: Shipping method name
          default: ''
        - displayName: Method ID
          name: method ID
          type: string
          description: Shipping method ID
          default: ''
        - displayName: Total
          name: total
          type: string
          description: Line total (after discounts)
          default: ''
        - displayName: Metadata
          name: metadataUi
          type: fixedCollection
          description: Meta data
          placeholder: Add Metadata
          default: {}
          options:
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
          typeOptions:
            multipleValues: true
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
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - customer
          operation:
          - update
    typeInfo: &id004
      type: string
      displayName: Customer ID
      name: customerId
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: false
    description: ''
    validation: &id005
      displayOptions:
        show:
          resource:
          - product
          operation:
          - delete
    typeInfo: &id006
      type: string
      displayName: Product ID
      name: productId
  - id: orderId
    name: Order ID
    type: string
    default: ''
    required: false
    description: ''
    validation: &id007
      displayOptions:
        show:
          resource:
          - order
          operation:
          - delete
    typeInfo: &id008
      type: string
      displayName: Order ID
      name: orderId
- id: get
  name: Get
  description: Retrieve a customer
  params:
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ID of the customer to retrieve
    validation: *id003
    typeInfo: *id004
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: orderId
    name: Order ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id007
    typeInfo: *id008
- id: getAll
  name: Get Many
  description: Retrieve many customers
  params:
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
          - order
          operation:
          - getAll
    typeInfo: &id010
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id011
      displayOptions:
        show:
          resource:
          - order
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
        maxValue: 100
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
- id: update
  name: Update
  description: Update a customer
  params:
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ID of the customer to update
    validation: *id003
    typeInfo: *id004
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: dimensionsUi
    name: Dimensions
    type: fixedCollection
    default: {}
    required: false
    description: Product dimensions
    placeholder: Add Dimension
    validation: *id013
    typeInfo: *id014
  - id: imagesUi
    name: Images
    type: fixedCollection
    default: {}
    required: false
    description: Product Image
    placeholder: Add Image
    validation: *id015
    typeInfo: *id016
  - id: metadataUi
    name: Metadata
    type: fixedCollection
    default: {}
    required: false
    description: Meta data
    placeholder: Add Metadata
    validation: *id001
    typeInfo: *id002
  - id: orderId
    name: Order ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: billingUi
    name: Billing
    type: fixedCollection
    default: {}
    required: false
    description: Billing address
    placeholder: Add Billing
    validation: *id017
    typeInfo: *id018
  - id: couponLinesUi
    name: Coupon Lines
    type: fixedCollection
    default: {}
    required: false
    description: Coupons line data
    placeholder: Add Coupon Line
    validation: *id019
    typeInfo: *id020
  - id: feeLinesUi
    name: Fee Lines
    type: fixedCollection
    default: {}
    required: false
    description: Fee line data
    placeholder: Add Fee Line
    validation: *id021
    typeInfo: *id022
  - id: lineItemsUi
    name: Line Items
    type: fixedCollection
    default: {}
    required: false
    description: Line item data
    placeholder: Add Line Item
    validation: *id023
    typeInfo: *id024
  - id: metadataUi
    name: Metadata
    type: fixedCollection
    default: {}
    required: false
    description: Meta data
    placeholder: Add Metadata
    validation: *id001
    typeInfo: *id002
  - id: shippingUi
    name: Shipping
    type: fixedCollection
    default: {}
    required: false
    description: Shipping address
    placeholder: Add Shipping
    validation: *id025
    typeInfo: *id026
  - id: shippingLinesUi
    name: Shipping Lines
    type: fixedCollection
    default: {}
    required: false
    description: Shipping line data
    placeholder: Add Shipping Line
    validation: *id027
    typeInfo: *id028
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
  - field: email
    text: name@email.com
  - field: filters
    text: Add Filter
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: dimensionsUi
    text: Add Dimension
  - field: imagesUi
    text: Add Image
  - field: metadataUi
    text: Add Metadata
  - field: updateFields
    text: Add Field
  - field: dimensionsUi
    text: Add Dimension
  - field: imagesUi
    text: Add Image
  - field: metadataUi
    text: Add Metadata
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: billingUi
    text: Add Billing
  - field: couponLinesUi
    text: Add Coupon Line
  - field: feeLinesUi
    text: Add Fee Line
  - field: lineItemsUi
    text: Add Line Item
  - field: metadataUi
    text: Add Metadata
  - field: shippingUi
    text: Add Shipping
  - field: shippingLinesUi
    text: Add Shipping Line
  - field: updateFields
    text: Add Field
  - field: billingUi
    text: Add Billing
  - field: couponLinesUi
    text: Add Coupon Line
  - field: feeLinesUi
    text: Add Fee Line
  - field: lineItemsUi
    text: Add Line Item
  - field: metadataUi
    text: Add Metadata
  - field: shippingUi
    text: Add Shipping
  - field: shippingLinesUi
    text: Add Shipping Line
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
  "$id": "https://n8n.io/schemas/nodes/wooCommerce.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "WooCommerce Node",
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
            "customer",
            "order",
            "product"
          ],
          "default": "product"
        },
        "operation": {
          "description": "Create a order",
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
        "email": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "customerId": {
          "description": "ID of the customer to update",
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
          "description": "Email address to filter customers by",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "additionalFields": {
          "description": "Currency the order was created with",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "Currency the order was created with",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "name": {
          "description": "Product name",
          "type": "string",
          "default": ""
        },
        "dimensionsUi": {
          "description": "Product dimensions",
          "type": "string",
          "default": {},
          "examples": [
            "Add Dimension"
          ]
        },
        "imagesUi": {
          "description": "Product Image",
          "type": "string",
          "default": {},
          "examples": [
            "Add Image"
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
        "productId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Limit response to resources published after a given ISO8601 compliant date",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "billingUi": {
          "description": "Billing address",
          "type": "string",
          "default": {},
          "examples": [
            "Add Billing"
          ]
        },
        "couponLinesUi": {
          "description": "Coupons line data",
          "type": "string",
          "default": {},
          "examples": [
            "Add Coupon Line"
          ]
        },
        "feeLinesUi": {
          "description": "Fee line data",
          "type": "string",
          "default": {},
          "examples": [
            "Add Fee Line"
          ]
        },
        "lineItemsUi": {
          "description": "Line item data",
          "type": "string",
          "default": {},
          "examples": [
            "Add Line Item"
          ]
        },
        "shippingUi": {
          "description": "Shipping address",
          "type": "string",
          "default": {},
          "examples": [
            "Add Shipping"
          ]
        },
        "shippingLinesUi": {
          "description": "Shipping line data",
          "type": "string",
          "default": {},
          "examples": [
            "Add Shipping Line"
          ]
        },
        "orderId": {
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
      "name": "wooCommerceApi",
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
