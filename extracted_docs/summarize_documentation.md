---
title: "Node: Summarize"
slug: "node-summarize"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Sum, count, max, etc. across items"
node_type: "regular"
group: "['transform']"
---

# Node: Summarize

**Purpose.** Sum, count, max, etc. across items


---

## Node Details

- **Icon:** `file:summarize.svg`
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
| Fields to Summarize | `fieldsToSummarize` | fixedCollection | count | ✗ | How to combine the values of the field you want to summarize | e.g. Add Field |  |

<details>
<summary><strong>Fields to Summarize sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| values | `values` |  |  |  |

</details>

| Fields to Split By | `fieldsToSplitBy` | string |  | ✗ | The name of the input fields that you want to split the summary by | e.g. e.g. country, city |  |
| Fields to Group By | `fieldsToSplitBy` | string |  | ✗ | The name of the input fields that you want to split the summary by | e.g. e.g. country, city |  |
| Options | `options` | collection | {} | ✗ | Whether to continue if field to summarize can't be found in any items and return single empty item, otherwise an error would be thrown | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Continue if Field Not Found | `continueIfFieldNotFound` | boolean | False | Whether to continue if field to summarize can't be found in any items and return single empty item, otherwise an error would be thrown |
| Disable Dot Notation | `disableDotNotation` | boolean | False | Whether to disallow referencing child fields using `parent.child` in the field name |
| Output Format | `outputFormat` | options | separateItems |  |
| Ignore items without valid fields to group by | `skipEmptySplitFields` | boolean | False |  |

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
* Aliases: Append, Array, Average, Concatenate, Count, Group, Item, List, Max, Min, Pivot, Sum, Summarise, Summarize, Transform, Unique

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: summarize
displayName: Summarize
description: Sum, count, max, etc. across items
version:
- '1'
- '1.1'
nodeType: regular
group:
- transform
params:
- id: fieldsToSummarize
  name: Fields to Summarize
  type: fixedCollection
  default: count
  required: false
  description: How to combine the values of the field you want to summarize
  hint: Enter the field name as text
  placeholder: Add Field
  validation:
    displayOptions:
      hide:
        aggregation:
        - countUnique
        - count
        - max
        - min
  typeInfo:
    type: fixedCollection
    displayName: Fields to Summarize
    name: fieldsToSummarize
    typeOptions:
      multipleValues: true
    subProperties:
    - name: values
      values:
      - displayName: Aggregation
        name: aggregation
        type: options
        description: How to combine the values of the field you want to summarize
        value: append
        default: count
        options:
        - name: Append
          value: append
          displayName: Append
        - name: Average
          value: average
          displayName: Average
        - name: Concatenate
          value: concatenate
          displayName: Concatenate
        - name: Count
          value: count
          displayName: Count
        - name: Count Unique
          value: countUnique
          displayName: Count Unique
        - name: Max
          value: max
          displayName: Max
        - name: Min
          value: min
          displayName: Min
        - name: Sum
          value: sum
          displayName: Sum
      - displayName: Field
        name: field
        type: string
        description: The name of an input field that you want to summarize
        placeholder: e.g. cost
        hint: Enter the field name as text
        default: ''
        displayOptions:
          hide:
            aggregation:
            - countUnique
            - count
            - max
            - min
      - displayName: Field
        name: field
        type: string
        description: The name of an input field that you want to summarize. The field
          should contain numerical values; null, undefined, empty strings would be
          ignored.
        placeholder: e.g. cost
        hint: Enter the field name as text
        default: ''
        displayOptions:
          show: {}
      - displayName: Field
        name: field
        type: string
        description: The name of an input field that you want to summarize; null,
          undefined, empty strings would be ignored
        placeholder: e.g. cost
        hint: Enter the field name as text
        default: ''
        displayOptions:
          show:
            aggregation:
            - countUnique
            - count
            - max
            - min
      - displayName: Include Empty Values
        name: includeEmpty
        type: boolean
        default: false
        displayOptions:
          show:
            aggregation:
            - append
            - concatenate
            - count
            - countUnique
      - displayName: Separator
        name: separateBy
        type: options
        hint: What to insert between values
        value: ','
        default: ','
        options:
        - name: Comma
          value: ','
          displayName: Comma
        - name: Comma and Space
          value: ','
          displayName: Comma And Space
        - name: New Line
          value: n
          displayName: New Line
        - name: None
          displayName: None
        - name: Space
          displayName: Space
        - name: Other
          value: other
          displayName: Other
        displayOptions:
          show:
            aggregation:
            - concatenate
      - displayName: Custom Separator
        name: customSeparator
        type: string
        default: ''
        displayOptions:
          show:
            aggregation:
            - concatenate
            separateBy:
            - other
- id: fieldsToSplitBy
  name: Fields to Split By
  type: string
  default: ''
  required: false
  description: The name of the input fields that you want to split the summary by
  hint: Enter the name of the fields as text (separated by commas)
  placeholder: e.g. country, city
  validation: &id001
    displayOptions:
      show: {}
  typeInfo: &id002
    type: string
    displayName: Fields to Group By
    name: fieldsToSplitBy
- id: fieldsToSplitBy
  name: Fields to Group By
  type: string
  default: ''
  required: false
  description: The name of the input fields that you want to split the summary by
  hint: Enter the name of the fields as text (separated by commas)
  placeholder: e.g. country, city
  validation: *id001
  typeInfo: *id002
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to continue if field to summarize can't be found in any items
    and return single empty item, otherwise an error would be thrown
  placeholder: Add option
  validation:
    displayOptions:
      hide: {}
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Continue if Field Not Found
      name: continueIfFieldNotFound
      type: boolean
      description: Whether to continue if field to summarize can't be found in any
        items and return single empty item, otherwise an error would be thrown
      default: false
      displayOptions:
        hide: {}
    - displayName: Disable Dot Notation
      name: disableDotNotation
      type: boolean
      description: Whether to disallow referencing child fields using `parent.child`
        in the field name
      default: false
    - displayName: Output Format
      name: outputFormat
      type: options
      value: separateItems
      default: separateItems
      options:
      - name: Each Split in a Separate Item
        value: separateItems
        displayName: Each Split In A Separate Item
      - name: All Splits in a Single Item
        value: singleItem
        displayName: All Splits In A Single Item
    - displayName: Ignore items without valid fields to group by
      name: skipEmptySplitFields
      type: boolean
      default: false
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: fieldsToSummarize
    text: Add Field
  - field: fieldsToSplitBy
    text: e.g. country, city
  - field: fieldsToSplitBy
    text: e.g. country, city
  - field: options
    text: Add option
  hints:
  - field: fieldsToSummarize
    text: Enter the field name as text
  - field: fieldsToSplitBy
    text: Enter the name of the fields as text (separated by commas)
  - field: fieldsToSplitBy
    text: Enter the name of the fields as text (separated by commas)
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
  "$id": "https://n8n.io/schemas/nodes/summarize.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Summarize Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "fieldsToSummarize": {
          "description": "How to combine the values of the field you want to summarize",
          "type": "string",
          "default": "count",
          "examples": [
            "Add Field"
          ]
        },
        "fieldsToSplitBy": {
          "description": "The name of the input fields that you want to split the summary by",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. country, city"
          ]
        },
        "options": {
          "description": "Whether to continue if field to summarize can't be found in any items and return single empty item, otherwise an error would be thrown",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
      "1",
      "1.1"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
