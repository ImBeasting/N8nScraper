---
title: "Node: MailerLite Trigger"
slug: "node-mailerlite"
version: "['2']"
updated: "2025-11-13"
summary: "Starts the workflow when MailerLite events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: MailerLite Trigger

**Purpose.** Starts the workflow when MailerLite events occur
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:MailerLite.svg`
- **Group:** `['trigger']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **mailerLiteApi**: N/A


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
| `mailerLiteApi` | ✓ | - |

---

## Operations

### Subscriber Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new subscriber |
| Get | `get` | Get an subscriber |
| Get Many | `getAll` | Get many subscribers |
| Update | `update` | Update an subscriber |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | subscriber | ✗ | Resource to operate on |  |

**Resource options:**

* **Subscriber** (`subscriber`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a new subscriber |  |

**Operation options:**

* **Create** (`create`) - Create a new subscriber
* **Get** (`get`) - Get an subscriber
* **Get Many** (`getAll`) - Get many subscribers
* **Update** (`update`) - Update an subscriber

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | Email of new subscriber | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Filter by custom fields | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Status | `status` | options |  |  |
| Subscribed At | `subscribed_at` | dateTime |  |  |
| IP Address | `ip_address` | string |  |  |
| Opted In At | `opted_in_at` | dateTime |  |  |
| Opt In IP | `optin_ip` | string |  |  |
| Unsubscribed At | `unsubscribed_at` | dateTime |  |  |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Subscriber Email | `subscriberId` | string |  | ✓ | Email of subscriber to get |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Status | `status` | options |  |  |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Subscriber Email | `subscriberId` | string |  | ✓ | Email of subscriber |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Filter by custom fields | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Status | `status` | options |  |  |
| Subscribed At | `subscribed_at` | dateTime |  |  |
| IP Address | `ip_address` | string |  |  |
| Opted In At | `opted_in_at` | dateTime |  |  |
| Opt In IP | `optin_ip` | string |  |  |
| Unsubscribed At | `unsubscribed_at` | dateTime |  |  |

</details>


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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: mailerLite
displayName: MailerLite Trigger
description: Starts the workflow when MailerLite events occur
version:
- '2'
nodeType: trigger
group:
- trigger
credentials:
- name: mailerLiteApi
  required: true
operations:
- id: create
  name: Create
  description: Create a new subscriber
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email of new subscriber
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - subscriber
          operation:
          - create
    typeInfo:
      type: string
      displayName: Email
      name: email
- id: get
  name: Get
  description: Get an subscriber
  params:
  - id: subscriberId
    name: Subscriber Email
    type: string
    default: ''
    required: true
    description: Email of subscriber to get
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - subscriber
          operation:
          - get
    typeInfo: &id002
      type: string
      displayName: Subscriber Email
      name: subscriberId
- id: getAll
  name: Get Many
  description: Get many subscribers
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          resource:
          - subscriber
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          resource:
          - subscriber
          operation:
          - getAll
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
- id: update
  name: Update
  description: Update an subscriber
  params:
  - id: subscriberId
    name: Subscriber Email
    type: string
    default: ''
    required: true
    description: Email of subscriber
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/mailerLite.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MailerLite Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
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
            "subscriber"
          ],
          "default": "subscriber"
        },
        "operation": {
          "description": "Create a new subscriber",
          "type": "string",
          "enum": [
            "create",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "email": {
          "description": "Email of new subscriber",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "subscriberId": {
          "description": "Email of subscriber to get",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Filter by custom fields",
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
        "filters": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
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
      "2"
    ]
  },
  "credentials": [
    {
      "name": "mailerLiteApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
