---
title: "Node: ConvertKit Trigger"
slug: "node-convertkittrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle ConvertKit events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: ConvertKit Trigger

**Purpose.** Handle ConvertKit events via webhooks
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:convertKit.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **convertKitApi**: N/A


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
| `convertKitApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event | `event` | options |  | ✓ | The events that can trigger the webhook and whether they are enabled |  |

**Event options:**

* **Form Subscribe** (`formSubscribe`)
* **Link Click** (`linkClick`)
* **Product Purchase** (`productPurchase`)
* **Purchase Created** (`purchaseCreate`)
* **Sequence Complete** (`courseComplete`)
* **Sequence Subscribe** (`courseSubscribe`)
* **Subscriber Activated** (`subscriberActivate`)
* **Subscriber Unsubscribe** (`subscriberUnsubscribe`)
* **Tag Add** (`tagAdd`)
* **Tag Remove** (`tagRemove`)

| Form Name or ID | `formId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Sequence Name or ID | `courseId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Initiating Link | `link` | string |  | ✓ | The URL of the initiating link |  |
| Product ID | `productId` | string |  | ✓ |  |  |
| Tag Name or ID | `tagId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

---

## Load Options Methods

- `getTags`

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
* Categories: Marketing, Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: convertKitTrigger
displayName: ConvertKit Trigger
description: Handle ConvertKit events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: convertKitApi
  required: true
params:
- id: event
  name: Event
  type: options
  default: ''
  required: true
  description: The events that can trigger the webhook and whether they are enabled
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: formSubscribe
      name: Form Subscribe
      description: ''
    - value: linkClick
      name: Link Click
      description: ''
    - value: productPurchase
      name: Product Purchase
      description: ''
    - value: purchaseCreate
      name: Purchase Created
      description: ''
    - value: courseComplete
      name: Sequence Complete
      description: ''
    - value: courseSubscribe
      name: Sequence Subscribe
      description: ''
    - value: subscriberActivate
      name: Subscriber Activated
      description: ''
    - value: subscriberUnsubscribe
      name: Subscriber Unsubscribe
      description: ''
    - value: tagAdd
      name: Tag Add
      description: ''
    - value: tagRemove
      name: Tag Remove
      description: ''
- id: formId
  name: Form Name or ID
  type: options
  default: ''
  required: true
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
    displayOptions:
      show:
        event:
        - formSubscribe
  typeInfo:
    type: options
    displayName: Form Name or ID
    name: formId
    typeOptions:
      loadOptionsMethod: getForms
    possibleValues: []
- id: courseId
  name: Sequence Name or ID
  type: options
  default: ''
  required: true
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
    displayOptions:
      show:
        event:
        - courseSubscribe
        - courseComplete
  typeInfo:
    type: options
    displayName: Sequence Name or ID
    name: courseId
    typeOptions:
      loadOptionsMethod: getSequences
    possibleValues: []
- id: link
  name: Initiating Link
  type: string
  default: ''
  required: true
  description: The URL of the initiating link
  validation:
    required: true
    displayOptions:
      show:
        event:
        - linkClick
  typeInfo:
    type: string
    displayName: Initiating Link
    name: link
- id: productId
  name: Product ID
  type: string
  default: ''
  required: true
  description: ''
  validation:
    required: true
    displayOptions:
      show:
        event:
        - productPurchase
  typeInfo:
    type: string
    displayName: Product ID
    name: productId
- id: tagId
  name: Tag Name or ID
  type: options
  default: ''
  required: true
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
    displayOptions:
      show:
        event:
        - tagAdd
        - tagRemove
  typeInfo:
    type: options
    displayName: Tag Name or ID
    name: tagId
    typeOptions:
      loadOptionsMethod: getTags
    possibleValues: []
common_expressions:
- ={{$parameter["event"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
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
  "$id": "https://n8n.io/schemas/nodes/convertKitTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ConvertKit Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "event": {
          "description": "The events that can trigger the webhook and whether they are enabled",
          "type": "string",
          "enum": [
            "formSubscribe",
            "linkClick",
            "productPurchase",
            "purchaseCreate",
            "courseComplete",
            "courseSubscribe",
            "subscriberActivate",
            "subscriberUnsubscribe",
            "tagAdd",
            "tagRemove"
          ],
          "default": ""
        },
        "formId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "courseId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "link": {
          "description": "The URL of the initiating link",
          "type": "string",
          "default": ""
        },
        "productId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "tagId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
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
      "name": "convertKitApi",
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
