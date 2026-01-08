---
title: "Node: Gumroad Trigger"
slug: "node-gumroadtrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle Gumroad events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Gumroad Trigger

**Purpose.** Handle Gumroad events via webhooks


---

## Node Details

- **Icon:** `file:gumroad.png`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **gumroadApi**: N/A


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
| `gumroadApi` | ✓ | - |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options |  | ✓ | When subscribed to this resource, you will be notified of cancellations of the user's subscribers |  |

**Resource options:**

* **Cancellation** (`cancellation`) - When subscribed to this resource, you will be notified of cancellations of the user's subscribers
* **Dispute** (`dispute`) - When subscribed to this resource, you will be notified of the disputes raised against user's sales
* **Dispute Won** (`dispute_won`) - When subscribed to this resource, you will be notified of the sale disputes won
* **Refund** (`refund`) - When subscribed to this resource, you will be notified of refunds to the user's sales
* **Sale** (`sale`) - When subscribed to this resource, you will be notified of the user's sales

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options |  | ✓ | When subscribed to this resource, you will be notified of cancellations of the user's subscribers |  |

**Resource options:**

* **Cancellation** (`cancellation`) - When subscribed to this resource, you will be notified of cancellations of the user's subscribers
* **Dispute** (`dispute`) - When subscribed to this resource, you will be notified of the disputes raised against user's sales
* **Dispute Won** (`dispute_won`) - When subscribed to this resource, you will be notified of the sale disputes won
* **Refund** (`refund`) - When subscribed to this resource, you will be notified of refunds to the user's sales
* **Sale** (`sale`) - When subscribed to this resource, you will be notified of the user's sales


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
node: gumroadTrigger
displayName: Gumroad Trigger
description: Handle Gumroad events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: gumroadApi
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: ''
  required: true
  description: When subscribed to this resource, you will be notified of cancellations
    of the user's subscribers
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: cancellation
      name: Cancellation
      description: When subscribed to this resource, you will be notified of cancellations
        of the user's subscribers
    - value: dispute
      name: Dispute
      description: When subscribed to this resource, you will be notified of the disputes
        raised against user's sales
    - value: dispute_won
      name: Dispute Won
      description: When subscribed to this resource, you will be notified of the sale
        disputes won
    - value: refund
      name: Refund
      description: When subscribed to this resource, you will be notified of refunds
        to the user's sales
    - value: sale
      name: Sale
      description: When subscribed to this resource, you will be notified of the user's
        sales
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
  "$id": "https://n8n.io/schemas/nodes/gumroadTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Gumroad Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "When subscribed to this resource, you will be notified of cancellations of the user's subscribers",
          "type": "string",
          "enum": [
            "cancellation",
            "dispute",
            "dispute_won",
            "refund",
            "sale"
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
      "name": "gumroadApi",
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
