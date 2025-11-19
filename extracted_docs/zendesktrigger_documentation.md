---
title: "Node: Zendesk Trigger"
slug: "node-zendesktrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle Zendesk events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Zendesk Trigger

**Purpose.** Handle Zendesk events via webhooks


---

## Node Details

- **Icon:** `file:zendesk.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **zendeskApi**: N/A
- **zendeskOAuth2Api**: N/A


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
| `zendeskApi` | ✓ | {'show': {'authentication': ['apiToken']}} |
| `zendeskOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Changed | `changed` |  |
| Changed From | `value_previous` |  |
| Changed To | `value` |  |
| Greater Than | `greater_than` |  |
| Is | `is` |  |
| Is Not | `is_not` |  |
| Less Than | `less_than` |  |
| Not Changed | `not_changed` |  |
| Not Changed From | `not_value_previous` |  |
| Not Changed To | `not_value` |  |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | ticket | ✗ | Resource to operate on |  |

**Resource options:**

* **Ticket** (`ticket`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | is | ✗ | Operation to perform |  |

**Operation options:**

* **Changed** (`changed`)
* **Changed From** (`value_previous`)
* **Changed To** (`value`)
* **Greater Than** (`greater_than`)
* **Is** (`is`)
* **Is Not** (`is_not`)
* **Less Than** (`less_than`)
* **Not Changed** (`not_changed`)
* **Not Changed From** (`not_value_previous`)
* **Not Changed To** (`not_value`)

---

---

## Load Options Methods

- `getFields`
- `for`
- `if`
- `name`
- `value`

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
* Categories: Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: zendeskTrigger
displayName: Zendesk Trigger
description: Handle Zendesk events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: zendeskApi
  required: true
- name: zendeskOAuth2Api
  required: true
operations:
- id: changed
  name: Changed
  description: ''
- id: value_previous
  name: Changed From
  description: ''
- id: value
  name: Changed To
  description: ''
- id: greater_than
  name: Greater Than
  description: ''
- id: is
  name: Is
  description: ''
- id: is_not
  name: Is Not
  description: ''
- id: less_than
  name: Less Than
  description: ''
- id: not_changed
  name: Not Changed
  description: ''
- id: not_value_previous
  name: Not Changed From
  description: ''
- id: not_value
  name: Not Changed To
  description: ''
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  - field: conditions
    text: Add Condition
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
  "$id": "https://n8n.io/schemas/nodes/zendeskTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Zendesk Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "changed",
        "value_previous",
        "value",
        "greater_than",
        "is",
        "is_not",
        "less_than",
        "not_changed",
        "not_value_previous",
        "not_value"
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
            "apiToken",
            "oAuth2"
          ],
          "default": "apiToken"
        },
        "service": {
          "description": "",
          "type": "string",
          "enum": [
            "support"
          ],
          "default": "support"
        },
        "options": {
          "description": "The fields to return the values of. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "conditions": {
          "description": "The condition to set",
          "type": "string",
          "default": {},
          "examples": [
            "Add Condition"
          ]
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "ticket"
          ],
          "default": "ticket"
        },
        "field": {
          "description": "",
          "type": "string",
          "enum": [
            "assignee",
            "group",
            "priority",
            "status",
            "type"
          ],
          "default": "status"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "changed",
            "value_previous",
            "value",
            "is",
            "is_not",
            "not_changed",
            "not_value_previous",
            "not_value"
          ],
          "default": "is"
        },
        "value": {
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
      "name": "zendeskApi",
      "required": true
    },
    {
      "name": "zendeskOAuth2Api",
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
