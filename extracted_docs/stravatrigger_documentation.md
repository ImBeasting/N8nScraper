---
title: "Node: Strava Trigger"
slug: "node-stravatrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Strava events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Strava Trigger

**Purpose.** Starts the workflow when Strava events occur


---

## Node Details

- **Icon:** `file:strava.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **stravaOAuth2Api**: N/A


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
| `stravaOAuth2Api` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Object | `object` | options | * | ✗ |  |  |

**Object options:**

* **[All]** (`*`)
* **Activity** (`activity`)
* **Athlete** (`athlete`)

| Event | `event` | options | * | ✗ |  |  |

**Event options:**

* **[All]** (`*`)
* **Created** (`create`)
* **Deleted** (`delete`)
* **Updated** (`update`)

| Resolve Data | `resolveData` | boolean | True | ✗ | By default the webhook-data only contain the Object ID. If this option gets activated, it will resolve the data automatically. |  |
| Options | `options` | collection | {} | ✗ | Strava allows just one subscription at all times. If you want to delete the current subscription to make room for a new subscription with the current parameters, set this parameter to true. Keep in mind this is a destructive operation. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Delete If Exist | `deleteIfExist` | boolean | False | Strava allows just one subscription at all times. If you want to delete the current subscription to make room for a new subscription with the current parameters, set this parameter to true. Keep in mind this is a destructive operation. |

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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: stravaTrigger
displayName: Strava Trigger
description: Starts the workflow when Strava events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: stravaOAuth2Api
  required: true
params:
- id: object
  name: Object
  type: options
  default: '*'
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Object
    name: object
    possibleValues:
    - value: '*'
      name: '[All]'
      description: ''
    - value: activity
      name: Activity
      description: ''
    - value: athlete
      name: Athlete
      description: ''
- id: event
  name: Event
  type: options
  default: '*'
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: '*'
      name: '[All]'
      description: ''
    - value: create
      name: Created
      description: ''
    - value: delete
      name: Deleted
      description: ''
    - value: update
      name: Updated
      description: ''
- id: resolveData
  name: Resolve Data
  type: boolean
  default: true
  required: false
  description: By default the webhook-data only contain the Object ID. If this option
    gets activated, it will resolve the data automatically.
  typeInfo:
    type: boolean
    displayName: Resolve Data
    name: resolveData
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Strava allows just one subscription at all times. If you want to delete
    the current subscription to make room for a new subscription with the current
    parameters, set this parameter to true. Keep in mind this is a destructive operation.
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Delete If Exist
      name: deleteIfExist
      type: boolean
      description: Strava allows just one subscription at all times. If you want to
        delete the current subscription to make room for a new subscription with the
        current parameters, set this parameter to true. Keep in mind this is a destructive
        operation.
      default: false
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
  "$id": "https://n8n.io/schemas/nodes/stravaTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Strava Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "object": {
          "description": "",
          "type": "string",
          "enum": [
            "*",
            "activity",
            "athlete"
          ],
          "default": "*"
        },
        "event": {
          "description": "",
          "type": "string",
          "enum": [
            "*",
            "create",
            "delete",
            "update"
          ],
          "default": "*"
        },
        "resolveData": {
          "description": "By default the webhook-data only contain the Object ID. If this option gets activated, it will resolve the data automatically.",
          "type": "boolean",
          "default": true
        },
        "options": {
          "description": "Strava allows just one subscription at all times. If you want to delete the current subscription to make room for a new subscription with the current parameters, set this parameter to true. Keep in mind this is a destructive operation.",
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
      "name": "stravaOAuth2Api",
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
