---
title: "Node: Switch"
slug: "node-switch"
version: "['3', '3.1', '3.2', '3.3']"
updated: "2025-11-13"
summary: "Route items depending on defined expression or rules"
node_type: "regular"
group: "['transform']"
---

# Node: Switch

**Purpose.** Route items depending on defined expression or rules
**Subtitle.** =mode: {{((template: capitalize))($parameter["mode"])}}


---

## Node Details

- **Icon:** `fa:map-signs`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['dynamic']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Mode | `mode` | options | rules | ✗ | Build a matching rule for each output |  |

**Mode options:**

* **Rules** (`rules`) - Build a matching rule for each output
* **Expression** (`expression`) - Write an expression to return the output index

| Number of Outputs | `numberOutputs` | number | 4 | ✗ | How many outputs to create |  |
| Output Index | `output` | number | ={{}} | ✗ | The output index to send the input item to. Use an expression to calculate which input item should be routed to which output. The expression must return a number. | e.g. The index to route the item to, starts at 0 |  |
| Routing Rules | `rules` | fixedCollection | {} | ✗ | The label of output to which to send data to if rule matches | e.g. Add Routing Rule |  |
| Options | `options` | collection | {} | ✗ | If no rule matches the item will be sent to this output, by default they will be ignored | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fallback Output | `fallbackOutput` | options | none | If no rule matches the item will be sent to this output, by default they will be ignored |
| Ignore Case | `ignoreCase` | boolean | True | Whether to ignore letter case when evaluating conditions |
| Rename Fallback Output | `renameFallbackOutput` | string |  |  |
| Send data to all matching outputs | `allMatchingOutputs` | boolean | False | Whether to send data to all outputs meeting conditions (and not just the first one) |

</details>

| Convert types where required | `looseTypeValidation` | boolean | True | ✗ | If the type of an expression doesn't match the type of the comparison, n8n will try to cast the expression to the required type. E.g. for booleans <code>"false"</code> or <code>0</code> will be cast to <code>false</code> |  |

---

## Load Options Methods

- `getFallbackOutputOptions`
- `name`
- `value`
- `description`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{!$parameter.options.ignoreCase}}`
- `={{}}`
- `={{ $nodeVersion >= 3.2 ? 2 : 1 }}`

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
node: Switch
displayName: Switch
description: Route items depending on defined expression or rules
version:
- '3'
- '3.1'
- '3.2'
- '3.3'
nodeType: regular
group:
- transform
params:
- id: mode
  name: Mode
  type: options
  default: rules
  required: false
  description: Build a matching rule for each output
  typeInfo:
    type: options
    displayName: Mode
    name: mode
    possibleValues:
    - value: rules
      name: Rules
      description: Build a matching rule for each output
    - value: expression
      name: Expression
      description: Write an expression to return the output index
- id: numberOutputs
  name: Number of Outputs
  type: number
  default: 4
  required: false
  description: How many outputs to create
  validation:
    displayOptions:
      show:
        mode:
        - expression
  typeInfo:
    type: number
    displayName: Number of Outputs
    name: numberOutputs
- id: output
  name: Output Index
  type: number
  default: ={{}}
  required: false
  description: The output index to send the input item to. Use an expression to calculate
    which input item should be routed to which output. The expression must return
    a number.
  hint: The index to route the item to, starts at 0
  validation:
    displayOptions:
      show:
        mode:
        - expression
  typeInfo:
    type: number
    displayName: Output Index
    name: output
- id: rules
  name: Routing Rules
  type: fixedCollection
  default: {}
  required: false
  description: The label of output to which to send data to if rule matches
  placeholder: Add Routing Rule
  validation:
    displayOptions:
      show:
        mode:
        - rules
  typeInfo:
    type: fixedCollection
    displayName: Routing Rules
    name: rules
    typeOptions:
      multipleValues: true
    subProperties: []
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: If no rule matches the item will be sent to this output, by default
    they will be ignored
  placeholder: Add option
  validation:
    displayOptions:
      show:
        mode:
        - rules
  typeInfo:
    type: collection
    displayName: Options
    name: options
    typeOptions:
      loadOptionsMethod: getFallbackOutputOptions
    subProperties:
    - displayName: Fallback Output
      name: fallbackOutput
      type: options
      description: If no rule matches the item will be sent to this output, by default
        they will be ignored
      default: none
      typeOptions:
        loadOptionsMethod: getFallbackOutputOptions
    - displayName: Ignore Case
      name: ignoreCase
      type: boolean
      description: Whether to ignore letter case when evaluating conditions
      default: true
    - displayName: Rename Fallback Output
      name: renameFallbackOutput
      type: string
      placeholder: e.g. Fallback
      default: ''
      displayOptions:
        show:
          fallbackOutput:
          - extra
    - displayName: Send data to all matching outputs
      name: allMatchingOutputs
      type: boolean
      description: Whether to send data to all outputs meeting conditions (and not
        just the first one)
      default: false
- id: looseTypeValidation
  name: Convert types where required
  type: boolean
  default: true
  required: false
  description: If the type of an expression doesn't match the type of the comparison,
    n8n will try to cast the expression to the required type. E.g. for booleans <code>"false"</code>
    or <code>0</code> will be cast to <code>false</code>
  typeInfo:
    type: boolean
    displayName: Convert types where required
    name: looseTypeValidation
common_expressions:
- ={{!$parameter.options.ignoreCase}}
- ={{}}
- '={{ $nodeVersion >= 3.2 ? 2 : 1 }}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: rules
    text: Add Routing Rule
  - field: options
    text: Add option
  hints:
  - field: output
    text: The index to route the item to, starts at 0
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
  "$id": "https://n8n.io/schemas/nodes/Switch.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Switch Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "mode": {
          "description": "Build a matching rule for each output",
          "type": "string",
          "enum": [
            "rules",
            "expression"
          ],
          "default": "rules"
        },
        "numberOutputs": {
          "description": "How many outputs to create",
          "type": "number",
          "default": 4
        },
        "output": {
          "description": "The output index to send the input item to. Use an expression to calculate which input item should be routed to which output. The expression must return a number.",
          "type": "number",
          "default": "={{}}"
        },
        "rules": {
          "description": "The label of output to which to send data to if rule matches",
          "type": "string",
          "default": {},
          "examples": [
            "Add Routing Rule"
          ]
        },
        "options": {
          "description": "If no rule matches the item will be sent to this output, by default they will be ignored",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "looseTypeValidation": {
          "description": "If the type of an expression doesn't match the type of the comparison, n8n will try to cast the expression to the required type. E.g. for booleans <code>\"false\"</code> or <code>0</code> will be cast to <code>false</code>",
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
      "3",
      "3.1",
      "3.2",
      "3.3"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['3', '3.1', '3.2', '3.3'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
