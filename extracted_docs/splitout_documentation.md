---
title: "Node: Split Out"
slug: "node-splitout"
version: "1"
updated: "2025-11-13"
summary: "Turn a list inside item(s) into separate items"
node_type: "regular"
group: "['transform']"
---

# Node: Split Out

**Purpose.** Turn a list inside item(s) into separate items


---

## Node Details

- **Icon:** `file:splitOut.svg`
- **Group:** `['transform']`
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
| Fields To Split Out | `fieldToSplitOut` | string |  | ✓ | The name of the input fields to break out into separate items. Separate multiple field names by commas. For binary data, use $binary. | e.g. Drag fields from the left or type their names |  |
| Include | `include` | options | noOtherFields | ✗ | Whether to copy any other fields into the new items |  |

**Include options:**

* **No Other Fields** (`noOtherFields`)
* **All Other Fields** (`allOtherFields`)
* **Selected Other Fields** (`selectedOtherFields`)

| Fields To Include | `fieldsToInclude` | string |  | ✗ | Fields in the input items to aggregate together | e.g. e.g. email, name |  |
| Options | `options` | collection | {} | ✗ | Whether to disallow referencing child fields using `parent.child` in the field name | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Disable Dot Notation | `disableDotNotation` | boolean | False | Whether to disallow referencing child fields using `parent.child` in the field name |
| Destination Field Name | `destinationFieldName` | string |  | The field in the output under which to put the split field contents |
| Include Binary | `includeBinary` | boolean | False | Whether to include the binary data in the new items |

</details>


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
* Aliases: Split, Nested, Transform, Array, List, Item

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: splitOut
displayName: Split Out
description: Turn a list inside item(s) into separate items
version: '1'
nodeType: regular
group:
- transform
params:
- id: fieldToSplitOut
  name: Fields To Split Out
  type: string
  default: ''
  required: true
  description: The name of the input fields to break out into separate items. Separate
    multiple field names by commas. For binary data, use $binary.
  hint: Use $binary to split out the input item by binary data
  placeholder: Drag fields from the left or type their names
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Fields To Split Out
    name: fieldToSplitOut
- id: include
  name: Include
  type: options
  default: noOtherFields
  required: false
  description: Whether to copy any other fields into the new items
  typeInfo:
    type: options
    displayName: Include
    name: include
    possibleValues:
    - value: noOtherFields
      name: No Other Fields
      description: ''
    - value: allOtherFields
      name: All Other Fields
      description: ''
    - value: selectedOtherFields
      name: Selected Other Fields
      description: ''
- id: fieldsToInclude
  name: Fields To Include
  type: string
  default: ''
  required: false
  description: Fields in the input items to aggregate together
  placeholder: e.g. email, name
  validation:
    displayOptions:
      show:
        include:
        - selectedOtherFields
  typeInfo:
    type: string
    displayName: Fields To Include
    name: fieldsToInclude
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to disallow referencing child fields using `parent.child` in
    the field name
  placeholder: Add Field
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Disable Dot Notation
      name: disableDotNotation
      type: boolean
      description: Whether to disallow referencing child fields using `parent.child`
        in the field name
      default: false
    - displayName: Destination Field Name
      name: destinationFieldName
      type: string
      description: The field in the output under which to put the split field contents
      default: ''
    - displayName: Include Binary
      name: includeBinary
      type: boolean
      description: Whether to include the binary data in the new items
      default: false
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: fieldToSplitOut
    text: Drag fields from the left or type their names
  - field: fieldsToInclude
    text: e.g. email, name
  - field: options
    text: Add Field
  hints:
  - field: fieldToSplitOut
    text: Use $binary to split out the input item by binary data
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
  "$id": "https://n8n.io/schemas/nodes/splitOut.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Split Out Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "fieldToSplitOut": {
          "description": "The name of the input fields to break out into separate items. Separate multiple field names by commas. For binary data, use $binary.",
          "type": "string",
          "default": "",
          "examples": [
            "Drag fields from the left or type their names"
          ]
        },
        "include": {
          "description": "Whether to copy any other fields into the new items",
          "type": "string",
          "enum": [
            "noOtherFields",
            "allOtherFields",
            "selectedOtherFields"
          ],
          "default": "noOtherFields"
        },
        "fieldsToInclude": {
          "description": "Fields in the input items to aggregate together",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. email, name"
          ]
        },
        "options": {
          "description": "Whether to disallow referencing child fields using `parent.child` in the field name",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
