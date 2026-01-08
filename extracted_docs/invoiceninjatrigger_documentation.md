---
title: "Node: Invoice Ninja Trigger"
slug: "node-invoiceninjatrigger"
version: "['1', '2']"
updated: "2026-01-08"
summary: "Starts the workflow when Invoice Ninja events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Invoice Ninja Trigger

**Purpose.** Starts the workflow when Invoice Ninja events occur


---

## Node Details

- **Icon:** `file:invoiceNinja.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **invoiceNinjaApi**: N/A


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
| `invoiceNinjaApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| API Version | `apiVersion` | options | v4 | ✗ |  |  |

**API Version options:**

* **Version 4** (`v4`)
* **Version 5** (`v5`)

| Event | `event` | options |  | ✓ |  |  |

**Event options:**

* **Client Created** (`create_client`)
* **Invoice Created** (`create_invoice`)
* **Payment Created** (`create_payment`)
* **Quote Created** (`create_quote`)
* **Vendor Created** (`create_vendor`)


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
* Categories: Finance & Accounting

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: invoiceNinjaTrigger
displayName: Invoice Ninja Trigger
description: Starts the workflow when Invoice Ninja events occur
version:
- '1'
- '2'
nodeType: trigger
group:
- trigger
credentials:
- name: invoiceNinjaApi
  required: true
params:
- id: apiVersion
  name: API Version
  type: options
  default: v4
  required: false
  description: ''
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: options
    displayName: API Version
    name: apiVersion
    possibleValues:
    - value: v4
      name: Version 4
      description: ''
    - value: v5
      name: Version 5
      description: ''
- id: event
  name: Event
  type: options
  default: ''
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: create_client
      name: Client Created
      description: ''
    - value: create_invoice
      name: Invoice Created
      description: ''
    - value: create_payment
      name: Payment Created
      description: ''
    - value: create_quote
      name: Quote Created
      description: ''
    - value: create_vendor
      name: Vendor Created
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
  "$id": "https://n8n.io/schemas/nodes/invoiceNinjaTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Invoice Ninja Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "apiVersion": {
          "description": "",
          "type": "string",
          "enum": [
            "v4",
            "v5"
          ],
          "default": "v4"
        },
        "event": {
          "description": "",
          "type": "string",
          "enum": [
            "create_client",
            "create_invoice",
            "create_payment",
            "create_quote",
            "create_vendor"
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
    "version": [
      "1",
      "2"
    ]
  },
  "credentials": [
    {
      "name": "invoiceNinjaApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
