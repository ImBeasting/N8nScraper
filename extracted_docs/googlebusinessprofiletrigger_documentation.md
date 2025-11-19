---
title: "Node: Google Business Profile Trigger"
slug: "node-googlebusinessprofiletrigger"
version: "1"
updated: "2025-11-13"
summary: "Fetches reviews from Google Business Profile and starts the workflow on specified polling intervals."
node_type: "trigger"
group: "['trigger']"
---

# Node: Google Business Profile Trigger

**Purpose.** Fetches reviews from Google Business Profile and starts the workflow on specified polling intervals.
**Subtitle.** ={{"Google Business Profile Trigger"}}


---

## Node Details

- **Icon:** `file:googleBusinessProfile.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **googleBusinessProfileOAuth2Api**: N/A


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
| `googleBusinessProfileOAuth2Api` | ✓ | - |

---

## API Patterns

**Common Endpoints:**
- `callToAction.url`

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event | `event` | options | reviewAdded | ✓ |  |  |

**Event options:**

* **Review Added** (`reviewAdded`)

| Account | `account` | resourceLocator |  | ✓ | The Google Business Profile account | e.g. e.g. accounts/0123456789 |  |
| Location | `location` | resourceLocator |  | ✓ | The specific location or business associated with the account | e.g. e.g. locations/0123456789 |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{"Google Business Profile Trigger"}}`

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
* Aliases: Google My Business, GMB, My Business

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleBusinessProfileTrigger
displayName: Google Business Profile Trigger
description: Fetches reviews from Google Business Profile and starts the workflow
  on specified polling intervals.
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: googleBusinessProfileOAuth2Api
  required: true
params:
- id: event
  name: Event
  type: options
  default: reviewAdded
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: reviewAdded
      name: Review Added
      description: ''
- id: account
  name: Account
  type: resourceLocator
  default: ''
  required: true
  description: The Google Business Profile account
  hint: Enter the account name
  placeholder: e.g. accounts/0123456789
  validation:
    required: true
    displayOptions:
      show:
        event:
        - reviewAdded
  typeInfo:
    type: resourceLocator
    displayName: Account
    name: account
- id: location
  name: Location
  type: resourceLocator
  default: ''
  required: true
  description: The specific location or business associated with the account
  hint: Enter the location name
  placeholder: e.g. locations/0123456789
  validation:
    required: true
    displayOptions:
      show:
        event:
        - reviewAdded
  typeInfo:
    type: resourceLocator
    displayName: Location
    name: location
common_expressions:
- ={{"Google Business Profile Trigger"}}
api_patterns:
  http_methods: []
  endpoints:
  - callToAction.url
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: account
    text: e.g. accounts/0123456789
  - field: location
    text: e.g. locations/0123456789
  hints:
  - field: account
    text: Enter the account name
  - field: location
    text: Enter the location name
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
  "$id": "https://n8n.io/schemas/nodes/googleBusinessProfileTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Business Profile Trigger Node",
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
            "reviewAdded"
          ],
          "default": "reviewAdded"
        },
        "account": {
          "description": "The Google Business Profile account",
          "type": "string",
          "examples": [
            "e.g. accounts/0123456789"
          ]
        },
        "location": {
          "description": "The specific location or business associated with the account",
          "type": "string",
          "examples": [
            "e.g. locations/0123456789"
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
      "name": "googleBusinessProfileOAuth2Api",
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
