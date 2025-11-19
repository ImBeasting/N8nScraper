---
title: "Node: Workable Trigger"
slug: "node-workabletrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Workable events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Workable Trigger

**Purpose.** Starts the workflow when Workable events occur
**Subtitle.** ={{$parameter["triggerOn"]}}


---

## Node Details

- **Icon:** `file:workable.png`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **workableApi**: N/A


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
| `workableApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger On | `triggerOn` | options |  | ✓ |  |  |

**Trigger On options:**

* **Candidate Created** (`candidateCreated`)
* **Candidate Moved** (`candidateMoved`)

| Filters | `filters` | collection | {} | ✗ | Get notifications only for one job. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Job Name or ID | `job` | options |  | Get notifications only for one job. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Stage Name or ID | `stage` | options |  | Get notifications for specific stages. e.g. 'hired'. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


---

## Load Options Methods

- `getJobs`

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
* Categories: Miscellaneous

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: workableTrigger
displayName: Workable Trigger
description: Starts the workflow when Workable events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: workableApi
  required: true
params:
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
    - value: candidateCreated
      name: Candidate Created
      description: ''
    - value: candidateMoved
      name: Candidate Moved
      description: ''
- id: filters
  name: Filters
  type: collection
  default: {}
  required: false
  description: Get notifications only for one job. Choose from the list, or specify
    an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  placeholder: Add Filter
  typeInfo:
    type: collection
    displayName: Filters
    name: filters
    typeOptions:
      loadOptionsMethod: getJobs
    subProperties:
    - displayName: Job Name or ID
      name: job
      type: options
      description: Get notifications only for one job. Choose from the list, or specify
        an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
      default: ''
      typeOptions:
        loadOptionsMethod: getJobs
    - displayName: Stage Name or ID
      name: stage
      type: options
      description: Get notifications for specific stages. e.g. 'hired'. Choose from
        the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
      default: ''
      typeOptions:
        loadOptionsMethod: getStages
common_expressions:
- ={{$parameter["triggerOn"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/workableTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Workable Trigger Node",
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
            "candidateCreated",
            "candidateMoved"
          ],
          "default": ""
        },
        "filters": {
          "description": "Get notifications only for one job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
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
      "name": "workableApi",
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
