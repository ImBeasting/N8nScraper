---
title: "Node: Shopify Trigger"
slug: "node-shopifytrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle Shopify events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Shopify Trigger

**Purpose.** Handle Shopify events via webhooks
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:shopify.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **shopifyApi**: N/A
- **shopifyAccessTokenApi**: N/A
- **shopifyOAuth2Api**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `shopifyApi` | ✓ | {'show': {'authentication': ['apiKey']}} |
| `shopifyAccessTokenApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `shopifyOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | apiKey | ✗ |  |  |

**Authentication options:**

* **Access Token** (`accessToken`)
* **OAuth2** (`oAuth2`)
* **API Key** (`apiKey`)

| Trigger On | `topic` | options |  | ✗ |  |  |

**Trigger On options:**

* **App Uninstalled** (`app/uninstalled`)
* **Cart Created** (`carts/create`)
* **Cart Updated** (`carts/update`)
* **Checkout Created** (`checkouts/create`)
* **Checkout Delete** (`checkouts/delete`)
* **Checkout Update** (`checkouts/update`)
* **Collection Created** (`collections/create`)
* **Collection Deleted** (`collections/delete`)
* **Collection Listings Added** (`collection_listings/add`)
* **Collection Listings Removed** (`collection_listings/remove`)
* **Collection Listings Updated** (`collection_listings/update`)
* **Collection Updated** (`collections/update`)
* **Customer Created** (`customers/create`)
* **Customer Deleted** (`customers/delete`)
* **Customer Disabled** (`customers/disable`)
* **Customer Enabled** (`customers/enable`)
* **Customer Groups Created** (`customer_groups/create`)
* **Customer Groups Deleted** (`customer_groups/delete`)
* **Customer Groups Updated** (`customer_groups/update`)
* **Customer Updated** (`customers/update`)
* **Draft Orders Created** (`draft_orders/create`)
* **Draft Orders Deleted** (`draft_orders/delete`)
* **Draft Orders Updated** (`draft_orders/update`)
* **Fulfillment Created** (`fulfillments/create`)
* **Fulfillment Events Created** (`fulfillment_events/create`)
* **Fulfillment Events Deleted** (`fulfillment_events/delete`)
* **Fulfillment Updated** (`fulfillments/update`)
* **Inventory Items Created** (`inventory_items/create`)
* **Inventory Items Deleted** (`inventory_items/delete`)
* **Inventory Items Updated** (`inventory_items/update`)
* **Inventory Levels Connected** (`inventory_levels/connect`)
* **Inventory Levels Disconnected** (`inventory_levels/disconnect`)
* **Inventory Levels Updated** (`inventory_levels/update`)
* **Locale Created** (`locales/create`)
* **Locale Updated** (`locales/update`)
* **Location Created** (`locations/create`)
* **Location Deleted** (`locations/delete`)
* **Location Updated** (`locations/update`)
* **Order Cancelled** (`orders/cancelled`)
* **Order Created** (`orders/create`)
* **Order Fulfilled** (`orders/fulfilled`)
* **Order Paid** (`orders/paid`)
* **Order Partially Fulfilled** (`orders/partially_fulfilled`)
* **Order Transactions Created** (`order_transactions/create`)
* **Order Updated** (`orders/updated`)
* **Orders Deleted** (`orders/delete`)
* **Product Created** (`products/create`)
* **Product Deleted** (`products/delete`)
* **Product Listings Added** (`product_listings/add`)
* **Product Listings Removed** (`product_listings/remove`)
* **Product Listings Updated** (`product_listings/update`)
* **Product Updated** (`products/update`)
* **Refund Created** (`refunds/create`)
* **Shop Updated** (`shop/update`)
* **Tender Transactions Created** (`tender_transactions/create`)
* **Theme Created** (`themes/create`)
* **Theme Deleted** (`themes/delete`)
* **Theme Published** (`themes/publish`)
* **Theme Updated** (`themes/update`)


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["event"]}}`

---

## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |

---

## Notes & Caveats

* This node is part of n8n-nodes-base
* Categories: Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: shopifyTrigger
displayName: Shopify Trigger
description: Handle Shopify events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: shopifyApi
  required: true
- name: shopifyAccessTokenApi
  required: true
- name: shopifyOAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: apiKey
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: accessToken
      name: Access Token
      description: ''
    - value: oAuth2
      name: OAuth2
      description: ''
    - value: apiKey
      name: API Key
      description: ''
- id: topic
  name: Trigger On
  type: options
  default: ''
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Trigger On
    name: topic
    possibleValues:
    - value: app/uninstalled
      name: App Uninstalled
      description: ''
    - value: carts/create
      name: Cart Created
      description: ''
    - value: carts/update
      name: Cart Updated
      description: ''
    - value: checkouts/create
      name: Checkout Created
      description: ''
    - value: checkouts/delete
      name: Checkout Delete
      description: ''
    - value: checkouts/update
      name: Checkout Update
      description: ''
    - value: collections/create
      name: Collection Created
      description: ''
    - value: collections/delete
      name: Collection Deleted
      description: ''
    - value: collection_listings/add
      name: Collection Listings Added
      description: ''
    - value: collection_listings/remove
      name: Collection Listings Removed
      description: ''
    - value: collection_listings/update
      name: Collection Listings Updated
      description: ''
    - value: collections/update
      name: Collection Updated
      description: ''
    - value: customers/create
      name: Customer Created
      description: ''
    - value: customers/delete
      name: Customer Deleted
      description: ''
    - value: customers/disable
      name: Customer Disabled
      description: ''
    - value: customers/enable
      name: Customer Enabled
      description: ''
    - value: customer_groups/create
      name: Customer Groups Created
      description: ''
    - value: customer_groups/delete
      name: Customer Groups Deleted
      description: ''
    - value: customer_groups/update
      name: Customer Groups Updated
      description: ''
    - value: customers/update
      name: Customer Updated
      description: ''
    - value: draft_orders/create
      name: Draft Orders Created
      description: ''
    - value: draft_orders/delete
      name: Draft Orders Deleted
      description: ''
    - value: draft_orders/update
      name: Draft Orders Updated
      description: ''
    - value: fulfillments/create
      name: Fulfillment Created
      description: ''
    - value: fulfillment_events/create
      name: Fulfillment Events Created
      description: ''
    - value: fulfillment_events/delete
      name: Fulfillment Events Deleted
      description: ''
    - value: fulfillments/update
      name: Fulfillment Updated
      description: ''
    - value: inventory_items/create
      name: Inventory Items Created
      description: ''
    - value: inventory_items/delete
      name: Inventory Items Deleted
      description: ''
    - value: inventory_items/update
      name: Inventory Items Updated
      description: ''
    - value: inventory_levels/connect
      name: Inventory Levels Connected
      description: ''
    - value: inventory_levels/disconnect
      name: Inventory Levels Disconnected
      description: ''
    - value: inventory_levels/update
      name: Inventory Levels Updated
      description: ''
    - value: locales/create
      name: Locale Created
      description: ''
    - value: locales/update
      name: Locale Updated
      description: ''
    - value: locations/create
      name: Location Created
      description: ''
    - value: locations/delete
      name: Location Deleted
      description: ''
    - value: locations/update
      name: Location Updated
      description: ''
    - value: orders/cancelled
      name: Order Cancelled
      description: ''
    - value: orders/create
      name: Order Created
      description: ''
    - value: orders/fulfilled
      name: Order Fulfilled
      description: ''
    - value: orders/paid
      name: Order Paid
      description: ''
    - value: orders/partially_fulfilled
      name: Order Partially Fulfilled
      description: ''
    - value: order_transactions/create
      name: Order Transactions Created
      description: ''
    - value: orders/updated
      name: Order Updated
      description: ''
    - value: orders/delete
      name: Orders Deleted
      description: ''
    - value: products/create
      name: Product Created
      description: ''
    - value: products/delete
      name: Product Deleted
      description: ''
    - value: product_listings/add
      name: Product Listings Added
      description: ''
    - value: product_listings/remove
      name: Product Listings Removed
      description: ''
    - value: product_listings/update
      name: Product Listings Updated
      description: ''
    - value: products/update
      name: Product Updated
      description: ''
    - value: refunds/create
      name: Refund Created
      description: ''
    - value: shop/update
      name: Shop Updated
      description: ''
    - value: tender_transactions/create
      name: Tender Transactions Created
      description: ''
    - value: themes/create
      name: Theme Created
      description: ''
    - value: themes/delete
      name: Theme Deleted
      description: ''
    - value: themes/publish
      name: Theme Published
      description: ''
    - value: themes/update
      name: Theme Updated
      description: ''
common_expressions:
- ={{$parameter["event"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders: []
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/shopifyTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Shopify Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
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
        "topic": {
          "description": "",
          "type": "string",
          "enum": [
            "app/uninstalled",
            "carts/create",
            "carts/update",
            "checkouts/create",
            "checkouts/delete",
            "checkouts/update",
            "collections/create",
            "collections/delete",
            "collection_listings/add",
            "collection_listings/remove",
            "collection_listings/update",
            "collections/update",
            "customers/create",
            "customers/delete",
            "customers/disable",
            "customers/enable",
            "customer_groups/create",
            "customer_groups/delete",
            "customer_groups/update",
            "customers/update",
            "draft_orders/create",
            "draft_orders/delete",
            "draft_orders/update",
            "fulfillments/create",
            "fulfillment_events/create",
            "fulfillment_events/delete",
            "fulfillments/update",
            "inventory_items/create",
            "inventory_items/delete",
            "inventory_items/update",
            "inventory_levels/connect",
            "inventory_levels/disconnect",
            "inventory_levels/update",
            "locales/create",
            "locales/update",
            "locations/create",
            "locations/delete",
            "locations/update",
            "orders/cancelled",
            "orders/create",
            "orders/fulfilled",
            "orders/paid",
            "orders/partially_fulfilled",
            "order_transactions/create",
            "orders/updated",
            "orders/delete",
            "products/create",
            "products/delete",
            "product_listings/add",
            "product_listings/remove",
            "product_listings/update",
            "products/update",
            "refunds/create",
            "shop/update",
            "tender_transactions/create",
            "themes/create",
            "themes/delete",
            "themes/publish",
            "themes/update"
          ],
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
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
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
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
