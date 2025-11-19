---
title: "Node: RSS Feed Trigger"
slug: "node-rssfeedreadtrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts a workflow when an RSS feed is updated"
node_type: "trigger"
group: "['trigger']"
---

# Node: RSS Feed Trigger

**Purpose.** Starts a workflow when an RSS feed is updated
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `fa:rss`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`


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

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Feed URL | `feedUrl` | string | https://blog.n8n.io/rss/ | ✓ | URL of the RSS feed to poll | url |

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
* Categories: Core Nodes

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: rssFeedReadTrigger
displayName: RSS Feed Trigger
description: Starts a workflow when an RSS feed is updated
version: '1'
nodeType: trigger
group:
- trigger
params:
- id: feedUrl
  name: Feed URL
  type: string
  default: https://blog.n8n.io/rss/
  required: true
  description: URL of the RSS feed to poll
  validation:
    required: true
    format: url
  typeInfo:
    type: string
    displayName: Feed URL
    name: feedUrl
common_expressions:
- ={{$parameter["event"]}}
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
  "$id": "https://n8n.io/schemas/nodes/rssFeedReadTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "RSS Feed Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "feedUrl": {
          "description": "URL of the RSS feed to poll",
          "type": "string",
          "default": "https://blog.n8n.io/rss/",
          "format": "url"
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
