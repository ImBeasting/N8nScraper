---
title: "Node: AWS SNS Trigger"
slug: "node-awssnstrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle AWS SNS events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: AWS SNS Trigger

**Purpose.** Handle AWS SNS events via webhooks
**Subtitle.** ={{$parameter["topic"].split(':')[5]}}


---

## Node Details

- **Icon:** `file:sns.svg`
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
| Topic | `topic` | resourceLocator |  | ✓ | e.g. Select a topic... |  |
| Authentication | `authentication` | options | iam | ✗ |  |  |

**Authentication options:**

* **AWS (IAM)** (`iam`)
* **AWS (Assume Role)** (`assumeRole`)

| Aws | `aws` |  |  | ✓ |  |  |
| Aws Assume Role | `awsAssumeRole` |  |  | ✓ |  |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["topic"].split(\':\')[5]}}`

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
* Categories: Development, Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: awsSnsTrigger
displayName: AWS SNS Trigger
description: Handle AWS SNS events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
params:
- id: topic
  name: Topic
  type: resourceLocator
  default: ''
  required: true
  description: ''
  placeholder: Select a topic...
  validation:
    required: true
  typeInfo:
    type: resourceLocator
    displayName: Topic
    name: topic
- id: authentication
  name: Authentication
  type: options
  default: iam
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: iam
      name: AWS (IAM)
      description: ''
    - value: assumeRole
      name: AWS (Assume Role)
      description: ''
- id: aws
  name: Aws
  type: ''
  default: ''
  required: true
  description: ''
  validation:
    required: true
    displayOptions:
      show:
        authentication:
        - iam
  typeInfo:
    type: unknown
    displayName: Aws
    name: aws
- id: awsAssumeRole
  name: Aws Assume Role
  type: ''
  default: ''
  required: true
  description: ''
  validation:
    required: true
    displayOptions:
      show:
        authentication:
        - assumeRole
  typeInfo:
    type: unknown
    displayName: Aws Assume Role
    name: awsAssumeRole
common_expressions:
- ={{$parameter["topic"].split(\':\')[5]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: topic
    text: Select a topic...
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
  "$id": "https://n8n.io/schemas/nodes/awsSnsTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AWS SNS Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "topic": {
          "description": "",
          "type": "string",
          "examples": [
            "Select a topic..."
          ]
        },
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "iam",
            "assumeRole"
          ],
          "default": "iam"
        },
        "aws": {
          "description": "",
          "type": "string"
        },
        "awsAssumeRole": {
          "description": "",
          "type": "string"
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
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
