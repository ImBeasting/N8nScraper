---
title: "Node: WooCommerce Trigger"
slug: "node-woocommercetrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle WooCommerce events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: WooCommerce Trigger

**Purpose.** Handle WooCommerce events via webhooks


---

## Node Details

- **Icon:** `file:wooCommerce.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **wooCommerceApi**: N/A


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
| `wooCommerceApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event | `event` | options |  | ✓ | Determines which resource events the webhook is triggered for |  |

**Event options:**

* **coupon.created** (`coupon.created`)
* **coupon.deleted** (`coupon.deleted`)
* **coupon.updated** (`coupon.updated`)
* **customer.created** (`customer.created`)
* **customer.deleted** (`customer.deleted`)
* **customer.updated** (`customer.updated`)
* **order.created** (`order.created`)
* **order.deleted** (`order.deleted`)
* **order.updated** (`order.updated`)
* **product.created** (`product.created`)
* **product.deleted** (`product.deleted`)
* **product.updated** (`product.updated`)


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
node: wooCommerceTrigger
displayName: WooCommerce Trigger
description: Handle WooCommerce events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: wooCommerceApi
  required: true
params:
- id: event
  name: Event
  type: options
  default: ''
  required: true
  description: Determines which resource events the webhook is triggered for
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: coupon.created
      name: coupon.created
      description: ''
    - value: coupon.deleted
      name: coupon.deleted
      description: ''
    - value: coupon.updated
      name: coupon.updated
      description: ''
    - value: customer.created
      name: customer.created
      description: ''
    - value: customer.deleted
      name: customer.deleted
      description: ''
    - value: customer.updated
      name: customer.updated
      description: ''
    - value: order.created
      name: order.created
      description: ''
    - value: order.deleted
      name: order.deleted
      description: ''
    - value: order.updated
      name: order.updated
      description: ''
    - value: product.created
      name: product.created
      description: ''
    - value: product.deleted
      name: product.deleted
      description: ''
    - value: product.updated
      name: product.updated
      description: ''
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
  "$id": "https://n8n.io/schemas/nodes/wooCommerceTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "WooCommerce Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "event": {
          "description": "Determines which resource events the webhook is triggered for",
          "type": "string",
          "enum": [
            "coupon.created",
            "coupon.deleted",
            "coupon.updated",
            "customer.created",
            "customer.deleted",
            "customer.updated",
            "order.created",
            "order.deleted",
            "order.updated",
            "product.created",
            "product.deleted",
            "product.updated"
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
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
