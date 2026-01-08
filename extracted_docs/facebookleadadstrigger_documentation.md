---
title: "Node: Facebook Lead Ads Trigger"
slug: "node-facebookleadadstrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle Facebook Lead Ads events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Facebook Lead Ads Trigger

**Purpose.** Handle Facebook Lead Ads events via webhooks
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:facebook.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **facebookLeadAdsOAuth2Api**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **facebookLeadAdsNotice**: Due to Facebook API limitations, you can use just one Facebook Lead Ads trigger for each Facebook App

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `facebookLeadAdsOAuth2Api` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

**Headers Used:** content-type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event | `event` | options | newLead | ✓ |  |  |

**Event options:**

* **New Lead** (`newLead`)

| Page | `page` | resourceLocator |  | ✓ | The page linked to the form for retrieving new leads | e.g. 121637951029080 |  |
| Form | `form` | resourceLocator |  | ✓ | The form to monitor for fetching lead details upon submission | e.g. 121637951029080 |  |
| Options | `options` | collection | {} | ✗ | Whether to return a simplified version of the webhook event instead of all fields | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Simplify Output | `simplifyOutput` | boolean | True | Whether to return a simplified version of the webhook event instead of all fields |

</details>


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
* Categories: Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: facebookLeadAdsTrigger
displayName: Facebook Lead Ads Trigger
description: Handle Facebook Lead Ads events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: facebookLeadAdsOAuth2Api
  required: true
params:
- id: event
  name: Event
  type: options
  default: newLead
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: newLead
      name: New Lead
      description: ''
- id: page
  name: Page
  type: resourceLocator
  default: ''
  required: true
  description: The page linked to the form for retrieving new leads
  placeholder: '121637951029080'
  validation:
    required: true
  typeInfo:
    type: resourceLocator
    displayName: Page
    name: page
- id: form
  name: Form
  type: resourceLocator
  default: ''
  required: true
  description: The form to monitor for fetching lead details upon submission
  placeholder: '121637951029080'
  validation:
    required: true
  typeInfo:
    type: resourceLocator
    displayName: Form
    name: form
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to return a simplified version of the webhook event instead
    of all fields
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Simplify Output
      name: simplifyOutput
      type: boolean
      description: Whether to return a simplified version of the webhook event instead
        of all fields
      default: true
common_expressions:
- ={{$parameter["event"]}}
api_patterns:
  http_methods:
  - POST
  endpoints: []
  headers:
  - content-type
  query_params: []
ui_elements:
  notices:
  - name: facebookLeadAdsNotice
    text: Due to Facebook API limitations, you can use just one Facebook Lead Ads
      trigger for each Facebook App
    conditions: null
  tooltips: []
  placeholders:
  - field: page
    text: '121637951029080'
  - field: form
    text: '121637951029080'
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/facebookLeadAdsTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Facebook Lead Ads Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "event": {
          "description": "",
          "type": "string",
          "enum": [
            "newLead"
          ],
          "default": "newLead"
        },
        "page": {
          "description": "The page linked to the form for retrieving new leads",
          "type": "string",
          "examples": [
            "121637951029080"
          ]
        },
        "form": {
          "description": "The form to monitor for fetching lead details upon submission",
          "type": "string",
          "examples": [
            "121637951029080"
          ]
        },
        "options": {
          "description": "Whether to return a simplified version of the webhook event instead of all fields",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
    "version": "1"
  },
  "credentials": [
    {
      "name": "facebookLeadAdsOAuth2Api",
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
