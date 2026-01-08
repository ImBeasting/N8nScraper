---
title: "Node: n8n Form"
slug: "node-form"
version: "['1', '2.3', '2.4', '2.5']"
updated: "2026-01-08"
summary: "Generate webforms in n8n and pass their responses to the workflow"
node_type: "regular"
group: "['input']"
---

# Node: n8n Form

**Purpose.** Generate webforms in n8n and pass their responses to the workflow


---

## Node Details

- **Icon:** `file:form.svg`
- **Group:** `['input']`
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
| Define Form | `defineForm` | options | fields | ✗ |  |  |

**Define Form options:**

* **Using Fields Below** (`fields`)
* **Using JSON** (`json`)

| Form Fields | `jsonOutput` | json | [\n  {\n     | ✗ | e.g. <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.form/" target="_blank">See docs</a> for field syntax |  |
| Form Elements | `formFields` | fixedCollection | {} | ✗ | e.g. Add Form Element |  |
| Limit Type | `limitType` | options | afterTimeInterval | ✗ | Sets the condition for the execution to resume. Can be a specified date or after some time. |  |

**Limit Type options:**

* **After Time Interval** (`afterTimeInterval`) - Waits for a certain amount of time
* **At Specified Time** (`atSpecifiedTime`) - Waits until the set date and time to continue

| Amount | `resumeAmount` | number | 1 | ✗ | The time to wait | min:0, max:∞ |
| Unit | `resumeUnit` | options | hours | ✗ | Unit of the interval value |  |

**Unit options:**

* **Minutes** (`minutes`)
* **Hours** (`hours`)
* **Days** (`days`)

| Max Date and Time | `maxDateAndTime` | dateTime |  | ✗ | Continue execution after the specified date and time |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `{{ $execution.resumeFormUrl }}`
- `{{ $input.all() }}`

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
* Aliases: _Form, form, table, submit, post, page, step, stage, multi

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: form
displayName: n8n Form
description: Generate webforms in n8n and pass their responses to the workflow
version:
- '1'
- '2.3'
- '2.4'
- '2.5'
nodeType: regular
group:
- input
params:
- id: defineForm
  name: Define Form
  type: options
  default: fields
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Define Form
    name: defineForm
    possibleValues:
    - value: fields
      name: Using Fields Below
      description: ''
    - value: json
      name: Using JSON
      description: ''
- id: jsonOutput
  name: Form Fields
  type: json
  default: '[\n  {\n    '
  required: false
  description: ''
  hint: <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.form/"
    target="_blank">See docs</a> for field syntax
  validation:
    displayOptions:
      show:
        defineForm:
        - json
  typeInfo:
    type: json
    displayName: Form Fields
    name: jsonOutput
    typeOptions:
      rows: 5
- id: formFields
  name: Form Elements
  type: fixedCollection
  default: {}
  required: false
  description: ''
  placeholder: Add Form Element
  typeInfo:
    type: fixedCollection
    displayName: Form Elements
    name: formFields
    typeOptions:
      multipleValues: true
    subProperties: []
- id: limitType
  name: Limit Type
  type: options
  default: afterTimeInterval
  required: false
  description: Sets the condition for the execution to resume. Can be a specified
    date or after some time.
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
  typeInfo:
    type: options
    displayName: Unit
    name: resumeUnit
    possibleValues:
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
  typeInfo:
    type: dateTime
    displayName: Max Date and Time
    name: maxDateAndTime
common_expressions:
- '{{ $execution.resumeFormUrl }}'
- '{{ $input.all() }}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: formFields
    text: Add Form Element
  hints:
  - field: jsonOutput
    text: <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.form/"
      target="_blank">See docs</a> for field syntax
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
  "$id": "https://n8n.io/schemas/nodes/form.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "n8n Form Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "defineForm": {
          "description": "",
          "type": "string",
          "enum": [
            "fields",
            "json"
          ],
          "default": "fields"
        },
        "jsonOutput": {
          "description": "",
          "type": "string",
          "default": "[\\n  {\\n    "
        },
        "formFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Form Element"
          ]
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
      "2.3",
      "2.4",
      "2.5"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2.3', '2.4', '2.5'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
