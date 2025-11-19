---
title: "Node: Venafi TLS Protect Datacenter Trigger"
slug: "node-venafitlsprotectdatacentertrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Venafi events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Venafi TLS Protect Datacenter Trigger

**Purpose.** Starts the workflow when Venafi events occur
**Subtitle.** ={{$parameter["triggerOn"]}}


---

## Node Details

- **Icon:** `file:../venafi.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **venafiTlsProtectDatacenterApi**: N/A


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
| `venafiTlsProtectDatacenterApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger On | `triggerOn` | options | certificateExpired | ✓ |  |  |

**Trigger On options:**

* **Certificate Expired** (`certificateExpired`)


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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: venafiTlsProtectDatacenterTrigger
displayName: Venafi TLS Protect Datacenter Trigger
description: Starts the workflow when Venafi events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: venafiTlsProtectDatacenterApi
  required: true
params:
- id: triggerOn
  name: Trigger On
  type: options
  default: certificateExpired
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Trigger On
    name: triggerOn
    possibleValues:
    - value: certificateExpired
      name: Certificate Expired
      description: ''
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
  "$id": "https://n8n.io/schemas/nodes/venafiTlsProtectDatacenterTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Venafi TLS Protect Datacenter Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "triggerOn": {
          "description": "",
          "type": "string",
          "enum": [
            "certificateExpired"
          ],
          "default": "certificateExpired"
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
      "name": "venafiTlsProtectDatacenterApi",
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
