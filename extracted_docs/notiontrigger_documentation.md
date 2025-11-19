---
title: "Node: Notion Trigger"
slug: "node-notiontrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Notion events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Notion Trigger

**Purpose.** Starts the workflow when Notion events occur
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `{'light': 'file:notion.svg', 'dark': 'file:notion.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **notionApi**: N/A


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

- **notionNotice**: In Notion, make sure to <a href="https://www.notion.so/help/add-and-manage-connections-with-the-api" target="_blank">add your connection</a> to the pages you want to access.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `notionApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event | `event` | options | pageAddedToDatabase | ✓ |  |  |

**Event options:**

* **Page Added to Database** (`pageAddedToDatabase`)
* **Page Updated in Database** (`pagedUpdatedInDatabase`)

| Database | `databaseId` | resourceLocator |  | ✓ | The Notion Database to operate on | e.g. Select a Database... |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: notionTrigger
displayName: Notion Trigger
description: Starts the workflow when Notion events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: notionApi
  required: true
params:
- id: event
  name: Event
  type: options
  default: pageAddedToDatabase
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: pageAddedToDatabase
      name: Page Added to Database
      description: ''
    - value: pagedUpdatedInDatabase
      name: Page Updated in Database
      description: ''
- id: databaseId
  name: Database
  type: resourceLocator
  default: ''
  required: true
  description: The Notion Database to operate on
  placeholder: Select a Database...
  validation:
    required: true
    displayOptions:
      show:
        event:
        - pageAddedToDatabase
        - pagedUpdatedInDatabase
  typeInfo:
    type: resourceLocator
    displayName: Database
    name: databaseId
- id: simple
  name: Simplify
  type: boolean
  default: true
  required: false
  description: Whether to return a simplified version of the response instead of the
    raw data
  validation:
    displayOptions:
      show:
        event:
        - pageAddedToDatabase
        - pagedUpdatedInDatabase
  typeInfo:
    type: boolean
    displayName: Simplify
    name: simple
common_expressions:
- ={{$parameter["event"]}}
ui_elements:
  notices:
  - name: notionNotice
    text: In Notion, make sure to <a href="https://www.notion.so/help/add-and-manage-connections-with-the-api"
      target="_blank">add your connection</a> to the pages you want to access.
    conditions: null
  tooltips: []
  placeholders:
  - field: databaseId
    text: Select a Database...
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
  "$id": "https://n8n.io/schemas/nodes/notionTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Notion Trigger Node",
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
            "pageAddedToDatabase",
            "pagedUpdatedInDatabase"
          ],
          "default": "pageAddedToDatabase"
        },
        "databaseId": {
          "description": "The Notion Database to operate on",
          "type": "string",
          "examples": [
            "Select a Database..."
          ]
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
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
      "name": "notionApi",
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
