---
title: "Node: Date & Time"
slug: "node-datetime"
version: "1"
updated: "2026-01-08"
summary: "Allows you to manipulate date and time values"
node_type: "regular"
group: "['transform']"
---

# Node: Date & Time

**Purpose.** Allows you to manipulate date and time values
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `fa:clock`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **noticeDateTime**: More powerful date functionality is available in <a href='https://docs.n8n.io/code/cookbook/luxon/' target='_blank'>expressions</a>,</br> e.g. <code>{{ $now.plus(1, 'week') }}</code>

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add time to Date Value |
| Subtract | `subtract` | Subtract time from Date Value |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | add | ✓ | Add time to Date Value |  |

**Operation options:**

* **Add** (`add`) - Add time to Date Value
* **Subtract** (`subtract`) - Subtract time from Date Value

---

---

## Load Options Methods

- `getTimezones`
- `for`
- `name`
- `value`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `{{ $now.plus(1, 'week') }}`
- `={{$parameter["action"]}}`

---

## Execution Settings

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |
| Always Output Data | `alwaysOutputData` | boolean | False | If active, will output a single, empty item when the output would have been empty. Use to prevent the workflow finishing on this node |
| Execute Once | `executeOnce` | boolean | False | If active, the node executes only once, with data from the first item it receives |
| Retry On Fail | `retryOnFail` | boolean | False | If active, the node tries to execute again when it fails |
| Max. Tries | `maxTries` | number | 3 | Number of times to attempt to execute the node before failing the execution *(Only visible when 'Retry On Fail' is enabled)* (min: 2, max: 5) |
| Wait Between Tries (ms) | `waitBetweenTries` | number | 1000 | How long to wait between each attempt (in milliseconds) *(Only visible when 'Retry On Fail' is enabled)* (min: 0, max: 5000) |
| On Error | `onError` | options | stopWorkflow | Action to take when the node execution fails |

**On Error Options:**

* **Stop Workflow** (`stopWorkflow`) — Halt execution and fail workflow
* **Continue** (`continueRegularOutput`) — Pass error message as item in regular output
* **Continue (using error output)** (`continueErrorOutput`) — Pass item to an extra `error` output

---

## Notes & Caveats

* This node is part of n8n-nodes-base

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: dateTime
displayName: Date & Time
description: Allows you to manipulate date and time values
version: '1'
nodeType: regular
group:
- transform
operations:
- id: add
  name: Add
  description: Add time to Date Value
- id: subtract
  name: Subtract
  description: Subtract time from Date Value
common_expressions:
- '{{ $now.plus(1, ''week'') }}'
- ={{$parameter["action"]}}
ui_elements:
  notices:
  - name: noticeDateTime
    text: More powerful date functionality is available in <a href='https://docs.n8n.io/code/cookbook/luxon/'
      target='_blank'>expressions</a>,</br> e.g. <code>{{ $now.plus(1, 'week') }}</code>
    conditions: null
  tooltips: []
  placeholders:
  - field: toFormat
    text: YYYY-MM-DD
  - field: options
    text: Add option
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
  executable:
    alwaysOutputData:
      name: Always Output Data
      field_id: alwaysOutputData
      type: boolean
      default: false
      description: If active, will output a single, empty item when the output would
        have been empty. Use to prevent the workflow finishing on this node
    executeOnce:
      name: Execute Once
      field_id: executeOnce
      type: boolean
      default: false
      description: If active, the node executes only once, with data from the first
        item it receives
    retryOnFail:
      name: Retry On Fail
      field_id: retryOnFail
      type: boolean
      default: false
      description: If active, the node tries to execute again when it fails
    maxTries:
      name: Max. Tries
      field_id: maxTries
      type: number
      default: 3
      min: 2
      max: 5
      description: Number of times to attempt to execute the node before failing the
        execution
      displayOptions:
        show:
          retryOnFail:
          - true
    waitBetweenTries:
      name: Wait Between Tries (ms)
      field_id: waitBetweenTries
      type: number
      default: 1000
      min: 0
      max: 5000
      description: How long to wait between each attempt (in milliseconds)
      displayOptions:
        show:
          retryOnFail:
          - true
    onError:
      name: On Error
      field_id: onError
      type: options
      default: stopWorkflow
      description: Action to take when the node execution fails
      options:
      - name: Stop Workflow
        value: stopWorkflow
        description: Halt execution and fail workflow
      - name: Continue
        value: continueRegularOutput
        description: Pass error message as item in regular output
      - name: Continue (using error output)
        value: continueErrorOutput
        description: Pass item to an extra `error` output
  note: Executable nodes have both common and executable settings

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/dateTime.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Date & Time Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "add",
        "subtract"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "action": {
          "description": "Add or subtract time from a date",
          "type": "string",
          "enum": [
            "calculate",
            "format"
          ],
          "default": "format"
        },
        "value": {
          "description": "The date string or timestamp from which you want to add/subtract time",
          "type": "string",
          "default": ""
        },
        "dataPropertyName": {
          "description": "Name of the output property to which to write the converted date",
          "type": "string",
          "default": "data"
        },
        "custom": {
          "description": "Whether a predefined format should be selected or custom format entered",
          "type": "boolean",
          "default": false
        },
        "toFormat": {
          "description": "Example: 09/04/1986",
          "type": "string",
          "enum": [
            "MM/DD/YYYY",
            "YYYY/MM/DD",
            "MMMM DD YYYY",
            "MM-DD-YYYY",
            "YYYY-MM-DD",
            "X",
            "x"
          ],
          "default": "MM/DD/YYYY"
        },
        "options": {
          "description": "Format for parsing the value as a date. If unrecognized, specify the <a href=\"https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datetime/#faqs\">format</a> for the value.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "operation": {
          "description": "Add time to Date Value",
          "type": "string",
          "enum": [
            "add",
            "subtract"
          ],
          "default": "add"
        },
        "duration": {
          "description": "E.g. enter \u201c10\u201d then select \u201cDays\u201d if you want to add 10 days to Date Value.",
          "type": "number",
          "default": 0
        },
        "timeUnit": {
          "description": "Time unit for Duration parameter above",
          "type": "string",
          "enum": [
            "quarters",
            "years",
            "months",
            "weeks",
            "days",
            "hours",
            "minutes",
            "seconds",
            "milliseconds"
          ],
          "default": "days"
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
        },
        "alwaysOutputData": {
          "type": "boolean",
          "default": false,
          "description": "If active, will output a single, empty item when the output would have been empty. Use to prevent the workflow finishing on this node"
        },
        "executeOnce": {
          "type": "boolean",
          "default": false,
          "description": "If active, the node executes only once, with data from the first item it receives"
        },
        "retryOnFail": {
          "type": "boolean",
          "default": false,
          "description": "If active, the node tries to execute again when it fails"
        },
        "maxTries": {
          "type": "number",
          "default": 3,
          "description": "Number of times to attempt to execute the node before failing the execution",
          "minimum": 2,
          "maximum": 5
        },
        "waitBetweenTries": {
          "type": "number",
          "default": 1000,
          "description": "How long to wait between each attempt (in milliseconds)",
          "minimum": 0,
          "maximum": 5000
        },
        "onError": {
          "type": "options",
          "default": "stopWorkflow",
          "description": "Action to take when the node execution fails",
          "enum": [
            "stopWorkflow",
            "continueRegularOutput",
            "continueErrorOutput"
          ]
        }
      }
    }
  },
  "metadata": {
    "nodeType": "regular",
    "version": "1"
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
