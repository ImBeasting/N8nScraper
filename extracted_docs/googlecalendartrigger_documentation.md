---
title: "Node: Google Calendar Trigger"
slug: "node-googlecalendartrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Google Calendar events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Google Calendar Trigger

**Purpose.** Starts the workflow when Google Calendar events occur
**Subtitle.** ={{$parameter["triggerOn"]}}


---

## Node Details

- **Icon:** `file:googleCalendar.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **googleCalendarOAuth2Api**: N/A


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
| `googleCalendarOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Calendar | `calendarId` | resourceLocator |  | ✓ | Google Calendar to operate on | e.g. Select a Calendar... |  |
| Trigger On | `triggerOn` | options |  | ✓ |  |  |

**Trigger On options:**

* **Event Cancelled** (`eventCancelled`)
* **Event Created** (`eventCreated`)
* **Event Ended** (`eventEnded`)
* **Event Started** (`eventStarted`)
* **Event Updated** (`eventUpdated`)

| Options | `options` | collection | {} | ✗ | Free text search terms to filter events that match these terms in any field, except for extended properties | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Match Term | `matchTerm` | string |  | Free text search terms to filter events that match these terms in any field, except for extended properties |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["triggerOn"]}}`

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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleCalendarTrigger
displayName: Google Calendar Trigger
description: Starts the workflow when Google Calendar events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: googleCalendarOAuth2Api
  required: true
params:
- id: calendarId
  name: Calendar
  type: resourceLocator
  default: ''
  required: true
  description: Google Calendar to operate on
  placeholder: Select a Calendar...
  validation:
    required: true
  typeInfo:
    type: resourceLocator
    displayName: Calendar
    name: calendarId
- id: triggerOn
  name: Trigger On
  type: options
  default: ''
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Trigger On
    name: triggerOn
    possibleValues:
    - value: eventCancelled
      name: Event Cancelled
      description: ''
    - value: eventCreated
      name: Event Created
      description: ''
    - value: eventEnded
      name: Event Ended
      description: ''
    - value: eventStarted
      name: Event Started
      description: ''
    - value: eventUpdated
      name: Event Updated
      description: ''
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Free text search terms to filter events that match these terms in any
    field, except for extended properties
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Match Term
      name: matchTerm
      type: string
      description: Free text search terms to filter events that match these terms
        in any field, except for extended properties
      default: ''
common_expressions:
- ={{$parameter["triggerOn"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: calendarId
    text: Select a Calendar...
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
  "$id": "https://n8n.io/schemas/nodes/googleCalendarTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Calendar Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "calendarId": {
          "description": "Google Calendar to operate on",
          "type": "string",
          "examples": [
            "Select a Calendar..."
          ]
        },
        "triggerOn": {
          "description": "",
          "type": "string",
          "enum": [
            "eventCancelled",
            "eventCreated",
            "eventEnded",
            "eventStarted",
            "eventUpdated"
          ],
          "default": ""
        },
        "options": {
          "description": "Free text search terms to filter events that match these terms in any field, except for extended properties",
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
      "name": "googleCalendarOAuth2Api",
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
