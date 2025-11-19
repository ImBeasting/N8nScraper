---
title: "Node: Webflow Trigger"
slug: "node-webflowtrigger"
version: "2"
updated: "2025-11-13"
summary: "Handle Webflow events via webhooks"
node_type: "trigger"
group: "['transform']"
---

# Node: Webflow Trigger

**Purpose.** Handle Webflow events via webhooks


---

## Node Details

- **Icon:** `file:webflow.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **webflowOAuth2Api**: N/A


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
| `webflowOAuth2Api` | ✓ | - |

---

## Operations

### Item Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an item |
| Delete | `deleteItem` | Delete an item |
| Get | `get` | Get an item |
| Get Many | `getAll` | Get many items |
| Update | `update` | Update an item |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | item | ✗ | Resource to operate on |  |

**Resource options:**

* **Item** (`item`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create an item
* **Delete** (`deleteItem`) - Delete an item
* **Get** (`get`) - Get an item
* **Get Many** (`getAll`) - Get many items
* **Update** (`update`) - Update an item

---

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ": " + $parameter["resource"]}}`

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
* Categories: Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: webflowTrigger
displayName: Webflow Trigger
description: Handle Webflow events via webhooks
version: '2'
nodeType: trigger
group:
- transform
credentials:
- name: webflowOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: ''
- id: deleteItem
  name: Delete
  description: ''
- id: get
  name: Get
  description: ''
- id: getAll
  name: Get Many
  description: ''
- id: update
  name: Update
  description: ''
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: fieldsUi
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/webflowTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Webflow Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "deleteItem",
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
            "item"
          ],
          "default": "item"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "create",
            "deleteItem",
            "get",
            "getAll",
            "update"
          ],
          "default": "get"
        },
        "siteId": {
          "description": "ID of the site containing the collection whose items to add to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "collectionId": {
          "description": "ID of the collection to add an item to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "itemId": {
          "description": "ID of the item to update",
          "type": "string",
          "default": ""
        },
        "live": {
          "description": "Whether the item should be published on the live site",
          "type": "boolean",
          "default": false
        },
        "fieldsUi": {
          "description": "Field to set for the item to create. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
          "default": 100
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
    "version": "2"
  },
  "credentials": [
    {
      "name": "webflowOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 2 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
