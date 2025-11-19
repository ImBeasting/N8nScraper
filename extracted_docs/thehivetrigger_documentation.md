---
title: "Node: TheHive Trigger"
slug: "node-thehivetrigger"
version: "['1', '2']"
updated: "2025-11-13"
summary: "Starts the workflow when TheHive events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: TheHive Trigger

**Purpose.** Starts the workflow when TheHive events occur


---

## Node Details

- **Icon:** `file:thehive.svg`
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

**Node-Specific Tips:**

- **notice**: You must set up the webhook in TheHive — instructions <a href="https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger/#configure-a-webhook-in-thehive" target="_blank">here</a>

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `events` | multiOptions | [] | ✓ | Events types |  |

**Events options:**

* ***** (`*`) - Any time any event is triggered (Wildcard Event)
* **Alert Created** (`alert_create`) - Triggered when an alert is created
* **Alert Deleted** (`alert_delete`) - Triggered when an alert is deleted
* **Alert Updated** (`alert_update`) - Triggered when an alert is updated
* **Case Created** (`case_create`) - Triggered when a case is created
* **Case Deleted** (`case_delete`) - Triggered when a case is deleted
* **Case Updated** (`case_update`) - Triggered when a case is updated
* **Log Created** (`case_task_log_create`) - Triggered when a task log is created
* **Log Deleted** (`case_task_log_delete`) - Triggered when a task log is deleted
* **Log Updated** (`case_task_log_update`) - Triggered when a task log is updated
* **Observable Created** (`case_artifact_create`) - Triggered when an observable is created
* **Observable Deleted** (`case_artifact_delete`) - Triggered when an observable is deleted
* **Observable Updated** (`case_artifact_update`) - Triggered when an observable is updated
* **Task Created** (`case_task_create`) - Triggered when a task is created
* **Task Deleted** (`case_task_delete`) - Triggered when a task is deleted
* **Task Updated** (`case_task_update`) - Triggered when a task is updated


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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: theHiveTrigger
displayName: TheHive Trigger
description: Starts the workflow when TheHive events occur
version:
- '1'
- '2'
nodeType: trigger
group:
- trigger
params:
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: Events types
  validation:
    required: true
    displayOptions:
      show: {}
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: '*'
      name: '*'
      description: Any time any event is triggered (Wildcard Event)
    - value: alert_create
      name: Alert Created
      description: Triggered when an alert is created
    - value: alert_delete
      name: Alert Deleted
      description: Triggered when an alert is deleted
    - value: alert_update
      name: Alert Updated
      description: Triggered when an alert is updated
    - value: case_create
      name: Case Created
      description: Triggered when a case is created
    - value: case_delete
      name: Case Deleted
      description: Triggered when a case is deleted
    - value: case_update
      name: Case Updated
      description: Triggered when a case is updated
    - value: case_task_log_create
      name: Log Created
      description: Triggered when a task log is created
    - value: case_task_log_delete
      name: Log Deleted
      description: Triggered when a task log is deleted
    - value: case_task_log_update
      name: Log Updated
      description: Triggered when a task log is updated
    - value: case_artifact_create
      name: Observable Created
      description: Triggered when an observable is created
    - value: case_artifact_delete
      name: Observable Deleted
      description: Triggered when an observable is deleted
    - value: case_artifact_update
      name: Observable Updated
      description: Triggered when an observable is updated
    - value: case_task_create
      name: Task Created
      description: Triggered when a task is created
    - value: case_task_delete
      name: Task Deleted
      description: Triggered when a task is deleted
    - value: case_task_update
      name: Task Updated
      description: Triggered when a task is updated
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: notice
    text: You must set up the webhook in TheHive — instructions <a href="https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger/#configure-a-webhook-in-thehive"
      target="_blank">here</a>
    conditions: null
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
  "$id": "https://n8n.io/schemas/nodes/theHiveTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TheHive Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "Events types",
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
      "1",
      "2"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
