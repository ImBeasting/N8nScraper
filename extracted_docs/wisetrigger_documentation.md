---
title: "Node: Wise Trigger"
slug: "node-wisetrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle Wise events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Wise Trigger

**Purpose.** Handle Wise events via webhooks
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:wise.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **wiseApi**: N/A


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
| `wiseApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** GET

**Common Endpoints:**
- `{rootUrl}{endpoint}`

**Headers Used:** user-agent

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Profile Name or ID | `profileId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Event | `event` | options |  | ✓ | Triggered every time a balance account is credited |  |

**Event options:**

* **Balance Credit** (`balanceCredit`) - Triggered every time a balance account is credited
* **Balance Update** (`balanceUpdate`) - Triggered every time a balance account is credited or debited
* **Transfer Active Case** (`transferActiveCases`) - Triggered every time a transfer's list of active cases is updated
* **Transfer State Changed** (`tranferStateChange`) - Triggered every time a transfer's status is updated


---

## Load Options Methods

- `getProfiles`

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
* Categories: Finance & Accounting

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: wiseTrigger
displayName: Wise Trigger
description: Handle Wise events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: wiseApi
  required: true
params:
- id: profileId
  name: Profile Name or ID
  type: options
  default: ''
  required: true
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Profile Name or ID
    name: profileId
    typeOptions:
      loadOptionsMethod: getProfiles
    possibleValues: []
- id: event
  name: Event
  type: options
  default: ''
  required: true
  description: Triggered every time a balance account is credited
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: balanceCredit
      name: Balance Credit
      description: Triggered every time a balance account is credited
    - value: balanceUpdate
      name: Balance Update
      description: Triggered every time a balance account is credited or debited
    - value: transferActiveCases
      name: Transfer Active Case
      description: Triggered every time a transfer's list of active cases is updated
    - value: tranferStateChange
      name: Transfer State Changed
      description: Triggered every time a transfer's status is updated
common_expressions:
- ={{$parameter["event"]}}
api_patterns:
  http_methods:
  - GET
  endpoints:
  - '{rootUrl}{endpoint}'
  headers:
  - user-agent
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
  "$id": "https://n8n.io/schemas/nodes/wiseTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Wise Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "profileId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "event": {
          "description": "Triggered every time a balance account is credited",
          "type": "string",
          "enum": [
            "balanceCredit",
            "balanceUpdate",
            "transferActiveCases",
            "tranferStateChange"
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
      "name": "wiseApi",
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
