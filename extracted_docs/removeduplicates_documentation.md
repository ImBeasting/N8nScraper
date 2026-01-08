---
title: "Node: Remove Duplicates"
slug: "node-removeduplicates"
version: "['2']"
updated: "2026-01-08"
summary: "Delete items with matching field values"
node_type: "regular"
group: "['transform']"
---

# Node: Remove Duplicates

**Purpose.** Delete items with matching field values


---

## Node Details

- **Icon:** `file:removeDuplicates.svg`
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
| Operation | `operation` | options | removeDuplicateInputItems | ✗ |  |  |
| Compare | `compare` | options | allFields | ✗ | The fields of the input items to compare to see if they are the same |  |
| Fields To Exclude | `fieldsToExclude` | string |  | ✗ | Fields in the input to exclude from the comparison | e.g. e.g. email, name |  |
| Fields To Compare | `fieldsToCompare` | string |  | ✗ | Fields in the input to add to the comparison | e.g. e.g. email, name |  |
| Keep Items Where | `logic` | options | removeItemsWithAlreadySeenKeyValues | ✗ | How to select input items to remove by comparing them with key values previously processed |  |
| Value to Dedupe On | `dedupeValue` | string |  | ✓ | Use an input field (or a combination of fields) that has a unique ID value | e.g. e.g. ID |  |
| Value to Dedupe On | `incrementalDedupeValue` | number |  | ✗ | Use an input field (or a combination of fields) that has an incremental value | e.g. e.g. ID |  |
| Value to Dedupe On | `dateDedupeValue` | dateTime |  | ✗ | Use an input field that has a date value in ISO format | e.g. e.g. 2024-08-09T13:44:16Z |  |
| Mode | `mode` | options | cleanDatabase | ✗ | How you want to modify the key values stored on the database. None of these modes removes input items. |  |
| Options | `options` | collection | {} | ✗ | Whether to disallow referencing child fields using `parent.child` in the field name | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Disable Dot Notation | `disableDotNotation` | boolean | False | Whether to disallow referencing child fields using `parent.child` in the field name |
| Remove Other Fields | `removeOtherFields` | boolean | False | Whether to remove any fields that are not being compared. If disabled, will keep the values from the first of the duplicates. |
| Scope | `scope` | options | node | If set to ‘workflow,’ key values will be shared across all nodes in the workflow. If set to ‘node,’ key values will be specific to this node. |
| History Size | `historySize` | number | 10000 |  |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter["operation"] === "removeItemsSeenInPreviousExecutions" && ($parameter["logic"] === "removeItemsWithAlreadySeenKeyValues" && $parameter["dedupeValue"] === undefined) || ($parameter["logic"] === "removeItemsUpToStoredIncrementalKey" && $parameter["incrementalDedupeValue"] === undefined) || ($parameter["logic"] === "removeItemsUpToStoredDate" && $parameter["dateDedupeValue"] === undefined) }}`

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
node: removeDuplicates
displayName: Remove Duplicates
description: Delete items with matching field values
version:
- '2'
nodeType: regular
group:
- transform
params:
- id: operation
  name: Operation
  type: options
  default: removeDuplicateInputItems
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Operation
    name: operation
    possibleValues: []
- id: compare
  name: Compare
  type: options
  default: allFields
  required: false
  description: The fields of the input items to compare to see if they are the same
  validation:
    displayOptions:
      show:
        operation:
        - removeDuplicateInputItems
  typeInfo:
    type: options
    displayName: Compare
    name: compare
    possibleValues: []
- id: fieldsToExclude
  name: Fields To Exclude
  type: string
  default: ''
  required: false
  description: Fields in the input to exclude from the comparison
  placeholder: e.g. email, name
  validation:
    displayOptions:
      show:
        compare:
        - allFieldsExcept
  typeInfo:
    type: string
    displayName: Fields To Exclude
    name: fieldsToExclude
- id: fieldsToCompare
  name: Fields To Compare
  type: string
  default: ''
  required: false
  description: Fields in the input to add to the comparison
  placeholder: e.g. email, name
  validation:
    displayOptions:
      show:
        compare:
        - selectedFields
  typeInfo:
    type: string
    displayName: Fields To Compare
    name: fieldsToCompare
- id: logic
  name: Keep Items Where
  type: options
  default: removeItemsWithAlreadySeenKeyValues
  required: false
  description: How to select input items to remove by comparing them with key values
    previously processed
  validation:
    displayOptions:
      show:
        operation:
        - removeItemsSeenInPreviousExecutions
  typeInfo:
    type: options
    displayName: Keep Items Where
    name: logic
    possibleValues: []
- id: dedupeValue
  name: Value to Dedupe On
  type: string
  default: ''
  required: true
  description: Use an input field (or a combination of fields) that has a unique ID
    value
  hint: The input field value to compare between items
  placeholder: e.g. ID
  validation:
    required: true
    displayOptions:
      show:
        logic:
        - removeItemsWithAlreadySeenKeyValues
  typeInfo:
    type: string
    displayName: Value to Dedupe On
    name: dedupeValue
- id: incrementalDedupeValue
  name: Value to Dedupe On
  type: number
  default: ''
  required: false
  description: Use an input field (or a combination of fields) that has an incremental
    value
  hint: The input field value to compare between items, an incremental value is expected
  placeholder: e.g. ID
  validation:
    displayOptions:
      show:
        logic:
        - removeItemsUpToStoredIncrementalKey
  typeInfo:
    type: number
    displayName: Value to Dedupe On
    name: incrementalDedupeValue
- id: dateDedupeValue
  name: Value to Dedupe On
  type: dateTime
  default: ''
  required: false
  description: Use an input field that has a date value in ISO format
  hint: The input field value to compare between items, a date is expected
  placeholder: e.g. 2024-08-09T13:44:16Z
  validation:
    displayOptions:
      show:
        logic:
        - removeItemsUpToStoredDate
  typeInfo:
    type: dateTime
    displayName: Value to Dedupe On
    name: dateDedupeValue
- id: mode
  name: Mode
  type: options
  default: cleanDatabase
  required: false
  description: How you want to modify the key values stored on the database. None
    of these modes removes input items.
  validation:
    displayOptions:
      show:
        operation:
        - clearDeduplicationHistory
  typeInfo:
    type: options
    displayName: Mode
    name: mode
    possibleValues: []
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to disallow referencing child fields using `parent.child` in
    the field name
  hint: The max number of past items to store for deduplication
  placeholder: Add Field
  validation:
    displayOptions:
      show:
        operation:
        - removeDuplicateInputItems
        - removeItemsSeenInPreviousExecutions
        - clearDeduplicationHistory
        - ''
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
      displayOptions:
        show: {}
        hide: {}
    - displayName: Remove Other Fields
      name: removeOtherFields
      type: boolean
      description: Whether to remove any fields that are not being compared. If disabled,
        will keep the values from the first of the duplicates.
      default: false
      displayOptions:
        show: {}
        hide: {}
    - displayName: Scope
      name: scope
      type: options
      description: If set to ‘workflow,’ key values will be shared across all nodes
        in the workflow. If set to ‘node,’ key values will be specific to this node.
      value: workflow
      default: node
      options:
      - name: Workflow
        description: Deduplication info will be shared by all the nodes in the workflow
        value: workflow
        displayName: Workflow
      - name: Node
        description: Deduplication info will be stored only for this node
        value: node
        displayName: Node
      displayOptions:
        show: {}
    - displayName: History Size
      name: historySize
      type: number
      hint: The max number of past items to store for deduplication
      default: 10000
      displayOptions:
        show: {}
common_expressions:
- ={{ $parameter["operation"] === "removeItemsSeenInPreviousExecutions" && ($parameter["logic"]
  === "removeItemsWithAlreadySeenKeyValues" && $parameter["dedupeValue"] === undefined)
  || ($parameter["logic"] === "removeItemsUpToStoredIncrementalKey" && $parameter["incrementalDedupeValue"]
  === undefined) || ($parameter["logic"] === "removeItemsUpToStoredDate" && $parameter["dateDedupeValue"]
  === undefined) }}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: fieldsToExclude
    text: e.g. email, name
  - field: fieldsToCompare
    text: e.g. email, name
  - field: dedupeValue
    text: e.g. ID
  - field: incrementalDedupeValue
    text: e.g. ID
  - field: dateDedupeValue
    text: e.g. 2024-08-09T13:44:16Z
  - field: options
    text: Add Field
  hints:
  - field: dedupeValue
    text: The input field value to compare between items
  - field: incrementalDedupeValue
    text: The input field value to compare between items, an incremental value is
      expected
  - field: dateDedupeValue
    text: The input field value to compare between items, a date is expected
  - field: options
    text: The max number of past items to store for deduplication
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
  "$id": "https://n8n.io/schemas/nodes/removeDuplicates.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Remove Duplicates Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "",
          "type": "string",
          "default": "removeDuplicateInputItems"
        },
        "compare": {
          "description": "The fields of the input items to compare to see if they are the same",
          "type": "string",
          "default": "allFields"
        },
        "fieldsToExclude": {
          "description": "Fields in the input to exclude from the comparison",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. email, name"
          ]
        },
        "fieldsToCompare": {
          "description": "Fields in the input to add to the comparison",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. email, name"
          ]
        },
        "logic": {
          "description": "How to select input items to remove by comparing them with key values previously processed",
          "type": "string",
          "default": "removeItemsWithAlreadySeenKeyValues"
        },
        "dedupeValue": {
          "description": "Use an input field (or a combination of fields) that has a unique ID value",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. ID"
          ]
        },
        "incrementalDedupeValue": {
          "description": "Use an input field (or a combination of fields) that has an incremental value",
          "type": "number",
          "default": "",
          "examples": [
            "e.g. ID"
          ]
        },
        "dateDedupeValue": {
          "description": "Use an input field that has a date value in ISO format",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. 2024-08-09T13:44:16Z"
          ]
        },
        "mode": {
          "description": "How you want to modify the key values stored on the database. None of these modes removes input items.",
          "type": "string",
          "default": "cleanDatabase"
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
    "version": [
      "2"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
