---
title: "Node: Code"
slug: "node-code"
version: "['1', '2']"
updated: "2026-01-08"
summary: "Run custom JavaScript or Python code"
node_type: "regular"
group: "['transform']"
---

# Node: Code

**Purpose.** Run custom JavaScript or Python code


---

## Node Details

- **Icon:** `file:code.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice** when language=['javaScript']: Type <code>$</code> for a list of <a target="_blank" href="https://docs.n8n.io/code-examples/methods-variables-reference/">special vars/methods</a>. Debug by using <code>console.log()</code> statements and viewing their output in the browser console.
- **notice** when language=['pythonNative']: (template: PRINT_INSTRUCTION)<br><br>The Python option does not support <code>_</code> syntax and helpers, except for <code>_items</code> in all-items mode and <code>_item</code> in per-item mode.

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Mode | `mode` | options | runOnceForAllItems | ✗ | Run this code only once, no matter how many input items there are |  |

**Mode options:**

* **Run Once for All Items** (`runOnceForAllItems`) - Run this code only once, no matter how many input items there are
* **Run Once for Each Item** (`runOnceForEachItem`) - Run this code as many times as there are input items

| Language | `language` | options | javaScript | ✗ |  |  |

**Language options:**

* **JavaScript** (`javaScript`) - Code in JavaScript
* **Python** (`pythonNative`) - Code in Python


---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Sample Data

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "jsCode": "return[\n  { value: 1 },\n  { value: 2 },\n]"
}
```

### Example 2: Run Once for All Items

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "jsCode": "// Loop over input items and add a new field\n// called 'myNewField' to the JSON of each one\nlet sum = 0;\nfor (const item of $input.all()) {\n  sum += item.json.value;\n}\n\nreturn [ {sum} ];"
}
```

### Example 3: Run Once for All Items (Legacy Syntax)

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "jsCode": "// Loop over input items and add a new field\n// called 'myNewField' to the JSON of each one\nlet sum = 0;\nfor (const item of items) {\n  sum += item.json.value;\n}\n\nreturn [ {sum} ];"
}
```

### Example 4: Run Once for Each Item

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "mode": "runOnceForEachItem",
  "jsCode": "// Add a new field called 'myNewField' to the\n// JSON of the item\n$input.item.json.myNewField = $input.item.json.value;\n\nreturn $input.item;"
}
```

### Example 5: Run Once for Each Item  (Legacy Syntax)

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "mode": "runOnceForEachItem",
  "jsCode": "// Add a new field called 'myNewField' to the\n// JSON of the item\nitem.json.myNewField = item.json.value;\n\nreturn item;"
}
```


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
* Categories: Development, Core Nodes
* Aliases: cpde, Javascript, JS, Python, Script, Custom Code, Function

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: code
displayName: Code
description: Run custom JavaScript or Python code
version:
- '1'
- '2'
nodeType: regular
group:
- transform
params:
- id: mode
  name: Mode
  type: options
  default: runOnceForAllItems
  required: false
  description: Run this code only once, no matter how many input items there are
  typeInfo:
    type: options
    displayName: Mode
    name: mode
    possibleValues:
    - value: runOnceForAllItems
      name: Run Once for All Items
      description: Run this code only once, no matter how many input items there are
    - value: runOnceForEachItem
      name: Run Once for Each Item
      description: Run this code as many times as there are input items
- id: language
  name: Language
  type: options
  default: javaScript
  required: false
  description: ''
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: options
    displayName: Language
    name: language
    possibleValues:
    - value: javaScript
      name: JavaScript
      description: ''
    - value: pythonNative
      name: Python
      description: ''
examples:
- name: Sample Data
  parameters:
    jsCode: "return[\n  { value: 1 },\n  { value: 2 },\n]"
  workflow: Unnamed workflow
- name: Run Once for All Items
  parameters:
    jsCode: "// Loop over input items and add a new field\n// called 'myNewField'\
      \ to the JSON of each one\nlet sum = 0;\nfor (const item of $input.all()) {\n\
      \  sum += item.json.value;\n}\n\nreturn [ {sum} ];"
  workflow: Unnamed workflow
- name: Run Once for All Items (Legacy Syntax)
  parameters:
    jsCode: "// Loop over input items and add a new field\n// called 'myNewField'\
      \ to the JSON of each one\nlet sum = 0;\nfor (const item of items) {\n  sum\
      \ += item.json.value;\n}\n\nreturn [ {sum} ];"
  workflow: Unnamed workflow
ui_elements:
  notices:
  - name: notice
    text: Type <code>$</code> for a list of <a target="_blank" href="https://docs.n8n.io/code-examples/methods-variables-reference/">special
      vars/methods</a>. Debug by using <code>console.log()</code> statements and viewing
      their output in the browser console.
    conditions:
      show:
        language:
        - javaScript
  - name: notice
    text: '(template: PRINT_INSTRUCTION)<br><br>The Python option does not support
      <code>_</code> syntax and helpers, except for <code>_items</code> in all-items
      mode and <code>_item</code> in per-item mode.'
    conditions:
      show:
        language:
        - pythonNative
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
  "$id": "https://n8n.io/schemas/nodes/code.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Code Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "mode": {
          "description": "Run this code only once, no matter how many input items there are",
          "type": "string",
          "enum": [
            "runOnceForAllItems",
            "runOnceForEachItem"
          ],
          "default": "runOnceForAllItems"
        },
        "language": {
          "description": "",
          "type": "string",
          "enum": [
            "javaScript",
            "pythonNative"
          ],
          "default": "javaScript"
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
      "2"
    ]
  },
  "examples": [
    {
      "description": "Sample Data",
      "value": {
        "jsCode": "return[\n  { value: 1 },\n  { value: 2 },\n]"
      }
    },
    {
      "description": "Run Once for All Items",
      "value": {
        "jsCode": "// Loop over input items and add a new field\n// called 'myNewField' to the JSON of each one\nlet sum = 0;\nfor (const item of $input.all()) {\n  sum += item.json.value;\n}\n\nreturn [ {sum} ];"
      }
    },
    {
      "description": "Run Once for All Items (Legacy Syntax)",
      "value": {
        "jsCode": "// Loop over input items and add a new field\n// called 'myNewField' to the JSON of each one\nlet sum = 0;\nfor (const item of items) {\n  sum += item.json.value;\n}\n\nreturn [ {sum} ];"
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
