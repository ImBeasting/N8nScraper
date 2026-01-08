---
title: "Node: Emelia Trigger"
slug: "node-emeliatrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle Emelia campaign activity events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Emelia Trigger

**Purpose.** Handle Emelia campaign activity events via webhooks
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:emelia.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **emeliaApi**: N/A


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
| `emeliaApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign Name or ID | `campaignId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Events | `events` | multiOptions | [] | ✓ |  |  |

**Events options:**

* **Email Bounced** (`bounced`)
* **Email Opened** (`opened`)
* **Email Replied** (`replied`)
* **Email Sent** (`sent`)
* **Link Clicked** (`clicked`)
* **Unsubscribed Contact** (`unsubscribed`)


---

## Load Options Methods

- `getCampaigns`
- `query`

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
* Categories: Communication, Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: emeliaTrigger
displayName: Emelia Trigger
description: Handle Emelia campaign activity events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: emeliaApi
  required: true
params:
- id: campaignId
  name: Campaign Name or ID
  type: options
  default: ''
  required: true
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Campaign Name or ID
    name: campaignId
    typeOptions:
      loadOptionsMethod: getCampaigns
    possibleValues: []
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: bounced
      name: Email Bounced
      description: ''
    - value: opened
      name: Email Opened
      description: ''
    - value: replied
      name: Email Replied
      description: ''
    - value: sent
      name: Email Sent
      description: ''
    - value: clicked
      name: Link Clicked
      description: ''
    - value: unsubscribed
      name: Unsubscribed Contact
      description: ''
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - POST
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
  "$id": "https://n8n.io/schemas/nodes/emeliaTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Emelia Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "campaignId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "events": {
          "description": "",
          "type": "string",
          "default": []
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
      "name": "emeliaApi",
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
