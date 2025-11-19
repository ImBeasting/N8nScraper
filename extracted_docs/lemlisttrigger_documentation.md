---
title: "Node: Lemlist Trigger"
slug: "node-lemlisttrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle Lemlist events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Lemlist Trigger

**Purpose.** Handle Lemlist events via webhooks
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:lemlist.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **lemlistApi**: N/A


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
| `lemlistApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event | `event` | options |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | We'll call this hook only for this campaignId. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Campaign Name or ID | `campaignId` | options |  | We'll call this hook only for this campaignId. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Is First | `isFirst` | boolean | False | Whether to call this hook only the first time this activity happened |

</details>


---

## Load Options Methods

- `getCampaigns`

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
* Categories: Communication, Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: lemlistTrigger
displayName: Lemlist Trigger
description: Handle Lemlist events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: lemlistApi
  required: true
params:
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
    possibleValues: []
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: We'll call this hook only for this campaignId. Choose from the list,
    or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  placeholder: Add Field
  typeInfo:
    type: collection
    displayName: Options
    name: options
    typeOptions:
      loadOptionsMethod: getCampaigns
    subProperties:
    - displayName: Campaign Name or ID
      name: campaignId
      type: options
      description: We'll call this hook only for this campaignId. Choose from the
        list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
      default: ''
      typeOptions:
        loadOptionsMethod: getCampaigns
    - displayName: Is First
      name: isFirst
      type: boolean
      description: Whether to call this hook only the first time this activity happened
      default: false
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
  placeholders:
  - field: options
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
  "$id": "https://n8n.io/schemas/nodes/lemlistTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Lemlist Trigger Node",
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
          "default": ""
        },
        "options": {
          "description": "We'll call this hook only for this campaignId. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
      "name": "lemlistApi",
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
