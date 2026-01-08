---
title: "Node: Redis Trigger"
slug: "node-redistrigger"
version: "1"
updated: "2026-01-08"
summary: "Subscribe to redis channel"
node_type: "trigger"
group: "['trigger']"
---

# Node: Redis Trigger

**Purpose.** Subscribe to redis channel


---

## Node Details

- **Icon:** `file:redis.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **redis**: N/A


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
| `redis` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channels | `channels` | string |  | ✓ | Channels to subscribe to, multiple channels be defined with comma. Wildcard character(*) is supported. |  |
| Options | `options` | collection | {} | ✗ | Whether to try to parse the message to an object | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| JSON Parse Body | `jsonParseBody` | boolean | False | Whether to try to parse the message to an object |
| Only Message | `onlyMessage` | boolean | False | Whether to return only the message property |

</details>


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
* Categories: Communication, Development, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: redisTrigger
displayName: Redis Trigger
description: Subscribe to redis channel
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: redis
  required: true
params:
- id: channels
  name: Channels
  type: string
  default: ''
  required: true
  description: Channels to subscribe to, multiple channels be defined with comma.
    Wildcard character(*) is supported.
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Channels
    name: channels
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to try to parse the message to an object
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: JSON Parse Body
      name: jsonParseBody
      type: boolean
      description: Whether to try to parse the message to an object
      default: false
    - displayName: Only Message
      name: onlyMessage
      type: boolean
      description: Whether to return only the message property
      default: false
ui_elements:
  notices: []
  tooltips: []
  placeholders:
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
  "$id": "https://n8n.io/schemas/nodes/redisTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Redis Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "channels": {
          "description": "Channels to subscribe to, multiple channels be defined with comma. Wildcard character(*) is supported.",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Whether to try to parse the message to an object",
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
      "name": "redis",
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
