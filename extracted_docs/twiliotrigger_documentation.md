---
title: "Node: Twilio Trigger"
slug: "node-twiliotrigger"
version: "['1']"
updated: "2025-11-13"
summary: "Starts the workflow on a Twilio update"
node_type: "trigger"
group: "['trigger']"
---

# Node: Twilio Trigger

**Purpose.** Starts the workflow on a Twilio update
**Subtitle.** =Updates: {{$parameter["updates"].join(", ")}}


---

## Node Details

- **Icon:** `file:twilio.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **twilioApi**: N/A


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

- **callTriggerNotice** when updates=['com.twilio.voice.insights.call-summary.complete']: The 'New Call' event may take up to thirty minutes to be triggered

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `twilioApi` | ✓ | - |

---

## API Patterns

**Common Endpoints:**
- `https://events.twilio.com/v1/{endpoint}`

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger On | `updates` | multiOptions | [] | ✓ | When an SMS message is received |  |

**Trigger On options:**

* **New SMS** (`com.twilio.messaging.inbound-message.received`) - When an SMS message is received
* **New Call** (`com.twilio.voice.insights.call-summary.complete`) - When a call is received


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
* Categories: Communication, Development
* Aliases: SMS, Phone, Voice

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: twilioTrigger
displayName: Twilio Trigger
description: Starts the workflow on a Twilio update
version:
- '1'
nodeType: trigger
group:
- trigger
credentials:
- name: twilioApi
  required: true
params:
- id: updates
  name: Trigger On
  type: multiOptions
  default: []
  required: true
  description: When an SMS message is received
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Trigger On
    name: updates
    possibleValues:
    - value: com.twilio.messaging.inbound-message.received
      name: New SMS
      description: When an SMS message is received
    - value: com.twilio.voice.insights.call-summary.complete
      name: New Call
      description: When a call is received
api_patterns:
  http_methods: []
  endpoints:
  - https://events.twilio.com/v1/{endpoint}
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices:
  - name: callTriggerNotice
    text: The 'New Call' event may take up to thirty minutes to be triggered
    conditions:
      show:
        updates:
        - com.twilio.voice.insights.call-summary.complete
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
  "$id": "https://n8n.io/schemas/nodes/twilioTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Twilio Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "updates": {
          "description": "When an SMS message is received",
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
    "version": [
      "1"
    ]
  },
  "credentials": [
    {
      "name": "twilioApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
