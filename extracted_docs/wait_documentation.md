---
title: "Node: Wait"
slug: "node-wait"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Wait before continue with execution"
node_type: "regular"
group: "['organization']"
---

# Node: Wait

**Purpose.** Wait before continue with execution


---

## Node Details

- **Icon:** `fa:pause-circle`
- **Group:** `['organization']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Limit Wait Time | `limitWaitTime` | boolean | False | ✗ | Whether to limit the time this node should wait for a user response before execution resumes |  |
| Limit Type | `limitType` | options | afterTimeInterval | ✗ | Sets the condition for the execution to resume. Can be a specified date or after some time. |  |

**Limit Type options:**

* **After Time Interval** (`afterTimeInterval`) - Waits for a certain amount of time
* **At Specified Time** (`atSpecifiedTime`) - Waits until the set date and time to continue

| Amount | `resumeAmount` | number | 1 | ✗ | The time to wait | min:0, max:∞ |
| Unit | `resumeUnit` | options | hours | ✗ | Unit of the interval value |  |

**Unit options:**

* **Seconds** (`seconds`)
* **Minutes** (`minutes`)
* **Hours** (`hours`)
* **Days** (`days`)

| Max Date and Time | `maxDateAndTime` | dateTime |  | ✗ | Continue execution after the specified date and time |  |

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Wait

**From workflow:** [Unit Test] Wait Node

**Parameters:**
```json
{
  "amount": 42,
  "unit": "seconds"
}
```


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["responseData"]}}`
- `={{$parameter["responseMode"] === "lastNode" ? "noData" : undefined}}`
- `={{$parameter["responseMode"]}}`
- `{{ $execution.resumeFormUrl }}`
- `={{$parameter["options"]["webhookSuffix"] || ""}}`

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
* Categories: Core Nodes
* Aliases: pause, sleep, delay, timeout

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: wait
displayName: Wait
description: Wait before continue with execution
version:
- '1'
- '1.1'
nodeType: regular
group:
- organization
params:
- id: limitWaitTime
  name: Limit Wait Time
  type: boolean
  default: false
  required: false
  description: Whether to limit the time this node should wait for a user response
    before execution resumes
  validation:
    displayOptions:
      show:
        resume:
        - webhook
        - form
  typeInfo:
    type: boolean
    displayName: Limit Wait Time
    name: limitWaitTime
- id: limitType
  name: Limit Type
  type: options
  default: afterTimeInterval
  required: false
  description: Sets the condition for the execution to resume. Can be a specified
    date or after some time.
  validation:
    displayOptions:
      show:
        limitWaitTime:
        - true
        resume:
        - webhook
        - form
  typeInfo:
    type: options
    displayName: Limit Type
    name: limitType
    possibleValues:
    - value: afterTimeInterval
      name: After Time Interval
      description: Waits for a certain amount of time
    - value: atSpecifiedTime
      name: At Specified Time
      description: Waits until the set date and time to continue
- id: resumeAmount
  name: Amount
  type: number
  default: 1
  required: false
  description: The time to wait
  validation:
    displayOptions:
      show:
        limitType:
        - afterTimeInterval
        limitWaitTime:
        - true
        resume:
        - webhook
        - form
  typeInfo:
    type: number
    displayName: Amount
    name: resumeAmount
    typeOptions:
      minValue: 0
      numberPrecision: 2
- id: resumeUnit
  name: Unit
  type: options
  default: hours
  required: false
  description: Unit of the interval value
  validation:
    displayOptions:
      show:
        limitType:
        - afterTimeInterval
        limitWaitTime:
        - true
        resume:
        - webhook
        - form
  typeInfo:
    type: options
    displayName: Unit
    name: resumeUnit
    possibleValues:
    - value: seconds
      name: Seconds
      description: ''
    - value: minutes
      name: Minutes
      description: ''
    - value: hours
      name: Hours
      description: ''
    - value: days
      name: Days
      description: ''
- id: maxDateAndTime
  name: Max Date and Time
  type: dateTime
  default: ''
  required: false
  description: Continue execution after the specified date and time
  validation:
    displayOptions:
      show:
        limitType:
        - atSpecifiedTime
        limitWaitTime:
        - true
        resume:
        - webhook
        - form
  typeInfo:
    type: dateTime
    displayName: Max Date and Time
    name: maxDateAndTime
examples:
- name: Wait
  parameters:
    amount: 42
    unit: seconds
  workflow: '[Unit Test] Wait Node'
common_expressions:
- ={{$parameter["responseData"]}}
- '={{$parameter["responseMode"] === "lastNode" ? "noData" : undefined}}'
- ={{$parameter["responseMode"]}}
- '{{ $execution.resumeFormUrl }}'
- ={{$parameter["options"]["webhookSuffix"] || ""}}
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
  "$id": "https://n8n.io/schemas/nodes/wait.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Wait Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "limitWaitTime": {
          "description": "Whether to limit the time this node should wait for a user response before execution resumes",
          "type": "boolean",
          "default": false
        },
        "limitType": {
          "description": "Sets the condition for the execution to resume. Can be a specified date or after some time.",
          "type": "string",
          "enum": [
            "afterTimeInterval",
            "atSpecifiedTime"
          ],
          "default": "afterTimeInterval"
        },
        "resumeAmount": {
          "description": "The time to wait",
          "type": "number",
          "default": 1
        },
        "resumeUnit": {
          "description": "Unit of the interval value",
          "type": "string",
          "enum": [
            "seconds",
            "minutes",
            "hours",
            "days"
          ],
          "default": "hours"
        },
        "maxDateAndTime": {
          "description": "Continue execution after the specified date and time",
          "type": "string",
          "default": ""
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
    "version": [
      "1",
      "1.1"
    ]
  },
  "examples": [
    {
      "description": "Wait",
      "value": {
        "amount": 42,
        "unit": "seconds"
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
