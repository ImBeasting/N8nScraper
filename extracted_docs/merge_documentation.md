---
title: "Node: Merge"
slug: "node-merge"
version: "['2', '2.1']"
updated: "2026-01-08"
summary: "Merges data of multiple streams once data from both is available"
node_type: "regular"
group: "['transform']"
---

# Node: Merge

**Purpose.** Merges data of multiple streams once data from both is available
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:merge.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main', 'Main']`
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
| Mode | `mode` | options | append | ✗ | All items of input 1, then all items of input 2 |  |

**Mode options:**

* **Append** (`append`) - All items of input 1, then all items of input 2
* **Combine** (`combine`) - Merge matching items together
* **Choose Branch** (`chooseBranch`) - Output input data, without modifying it

| Combination Mode | `combinationMode` | options | mergeByFields | ✗ | Combine items with the same field values |  |

**Combination Mode options:**

* **Merge By Fields** (`mergeByFields`) - Combine items with the same field values
* **Merge By Position** (`mergeByPosition`) - Combine items based on their order
* **Multiplex** (`multiplex`) - All possible item combinations (cross join)

| Fields to Match | `mergeByFields` | fixedCollection |  | ✗ | e.g. Add Fields to Match |  |

<details>
<summary><strong>Fields to Match sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Values | `values` |  |  |  |

</details>

| Output Type | `joinMode` | options | keepMatches | ✗ | Items that match, merged together (inner join) |  |

**Output Type options:**

* **Keep Matches** (`keepMatches`) - Items that match, merged together (inner join)
* **Keep Non-Matches** (`keepNonMatches`) - Items that don't match
* **Keep Everything** (`keepEverything`) - Items that match merged together, plus items that don't match (outer join)
* **Enrich Input 1** (`enrichInput1`) - All of input 1, with data from input 2 added in (left join)
* **Enrich Input 2** (`enrichInput2`) - All of input 2, with data from input 1 added in (right join)

| Output Data From | `outputDataFrom` | options | both | ✗ |  |  |

**Output Data From options:**

* **Both Inputs Merged Together** (`both`)
* **Input 1** (`input1`)
* **Input 2** (`input2`)

| Output Data From | `outputDataFrom` | options | both | ✗ |  |  |

**Output Data From options:**

* **Both Inputs Appended Together** (`both`)
* **Input 1** (`input1`)
* **Input 2** (`input2`)

| Output Type | `chooseBranchMode` | options | waitForBoth | ✗ |  |  |

**Output Type options:**

* **Wait for Both Inputs to Arrive** (`waitForBoth`)

| Output | `output` | options | input1 | ✗ |  |  |

**Output options:**

* **Input 1 Data** (`input1`)
* **Input 2 Data** (`input2`)
* **A Single, Empty Item** (`empty`)

| Options | `options` | collection | {} | ✗ | Whether to disallow referencing child fields using `parent.child` in the field name | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Disable Dot Notation | `disableDotNotation` | boolean | False | Whether to disallow referencing child fields using `parent.child` in the field name |
| Fuzzy Compare | `fuzzyCompare` | boolean | False | Whether to tolerate small type differences when comparing fields. E.g. the number 3 and the string '3' are treated as the same. |
| Include Any Unpaired Items | `includeUnpaired` | boolean | False | If there are different numbers of items in input 1 and input 2, whether to include the ones at the end with nothing to pair with |
| Multiple Matches | `multipleMatches` | options | all | Output multiple items if there are multiple matches |
| Multiple Matches | `multipleMatches` | options | all | Output multiple items if there are multiple matches |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter["mode"] === "chooseBranch" ? [0, 1] : 1 }}`

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
node: Merge
displayName: Merge
description: Merges data of multiple streams once data from both is available
version:
- '2'
- '2.1'
nodeType: regular
group:
- transform
params:
- id: mode
  name: Mode
  type: options
  default: append
  required: false
  description: All items of input 1, then all items of input 2
  typeInfo:
    type: options
    displayName: Mode
    name: mode
    possibleValues:
    - value: append
      name: Append
      description: All items of input 1, then all items of input 2
    - value: combine
      name: Combine
      description: Merge matching items together
    - value: chooseBranch
      name: Choose Branch
      description: Output input data, without modifying it
- id: combinationMode
  name: Combination Mode
  type: options
  default: mergeByFields
  required: false
  description: Combine items with the same field values
  validation:
    displayOptions:
      show:
        mode:
        - combine
  typeInfo:
    type: options
    displayName: Combination Mode
    name: combinationMode
    possibleValues:
    - value: mergeByFields
      name: Merge By Fields
      description: Combine items with the same field values
    - value: mergeByPosition
      name: Merge By Position
      description: Combine items based on their order
    - value: multiplex
      name: Multiplex
      description: All possible item combinations (cross join)
- id: mergeByFields
  name: Fields to Match
  type: fixedCollection
  default: ''
  required: false
  description: ''
  hint: Enter the field name as text
  placeholder: Add Fields to Match
  validation:
    displayOptions:
      show:
        mode:
        - combine
        combinationMode:
        - mergeByFields
  typeInfo:
    type: fixedCollection
    displayName: Fields to Match
    name: mergeByFields
    typeOptions:
      multipleValues: true
    subProperties:
    - name: values
      displayName: Values
      values:
      - displayName: Input 1 Field
        name: field1
        type: string
        placeholder: e.g. id
        hint: Enter the field name as text
        default: ''
      - displayName: Input 2 Field
        name: field2
        type: string
        placeholder: e.g. id
        hint: Enter the field name as text
        default: ''
- id: joinMode
  name: Output Type
  type: options
  default: keepMatches
  required: false
  description: Items that match, merged together (inner join)
  validation:
    displayOptions:
      show:
        mode:
        - combine
        combinationMode:
        - mergeByFields
  typeInfo:
    type: options
    displayName: Output Type
    name: joinMode
    possibleValues:
    - value: keepMatches
      name: Keep Matches
      description: Items that match, merged together (inner join)
    - value: keepNonMatches
      name: Keep Non-Matches
      description: Items that don't match
    - value: keepEverything
      name: Keep Everything
      description: Items that match merged together, plus items that don't match (outer
        join)
    - value: enrichInput1
      name: Enrich Input 1
      description: All of input 1, with data from input 2 added in (left join)
    - value: enrichInput2
      name: Enrich Input 2
      description: All of input 2, with data from input 1 added in (right join)
- id: outputDataFrom
  name: Output Data From
  type: options
  default: both
  required: false
  description: ''
  validation: &id001
    displayOptions:
      show:
        mode:
        - combine
        combinationMode:
        - mergeByFields
        joinMode:
        - keepNonMatches
  typeInfo: &id002
    type: options
    displayName: Output Data From
    name: outputDataFrom
    possibleValues:
    - value: both
      name: Both Inputs Appended Together
      description: ''
    - value: input1
      name: Input 1
      description: ''
    - value: input2
      name: Input 2
      description: ''
- id: outputDataFrom
  name: Output Data From
  type: options
  default: both
  required: false
  description: ''
  validation: *id001
  typeInfo: *id002
- id: chooseBranchMode
  name: Output Type
  type: options
  default: waitForBoth
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        mode:
        - chooseBranch
  typeInfo:
    type: options
    displayName: Output Type
    name: chooseBranchMode
    possibleValues:
    - value: waitForBoth
      name: Wait for Both Inputs to Arrive
      description: ''
- id: output
  name: Output
  type: options
  default: input1
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        mode:
        - chooseBranch
        chooseBranchMode:
        - waitForBoth
  typeInfo:
    type: options
    displayName: Output
    name: output
    possibleValues:
    - value: input1
      name: Input 1 Data
      description: ''
    - value: input2
      name: Input 2 Data
      description: ''
    - value: empty
      name: A Single, Empty Item
      description: ''
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to disallow referencing child fields using `parent.child` in
    the field name
  placeholder: Add option
  validation:
    displayOptions:
      show: {}
      hide: {}
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
    - displayName: Fuzzy Compare
      name: fuzzyCompare
      type: boolean
      description: Whether to tolerate small type differences when comparing fields.
        E.g. the number 3 and the string '3' are treated as the same.
      default: false
    - displayName: Include Any Unpaired Items
      name: includeUnpaired
      type: boolean
      description: If there are different numbers of items in input 1 and input 2,
        whether to include the ones at the end with nothing to pair with
      default: false
      displayOptions:
        show: {}
    - displayName: Multiple Matches
      name: multipleMatches
      type: options
      description: Output multiple items if there are multiple matches
      value: all
      default: all
      options:
      - name: Include All Matches
        description: Output multiple items if there are multiple matches
        value: all
        displayName: Include All Matches
      - name: Include First Match Only
        description: Only ever output a single item per match
        value: first
        displayName: Include First Match Only
      displayOptions:
        show: {}
    - displayName: Multiple Matches
      name: multipleMatches
      type: options
      description: Output multiple items if there are multiple matches
      value: all
      default: all
      options:
      - name: Include All Matches
        description: Output multiple items if there are multiple matches
        value: all
        displayName: Include All Matches
      - name: Include First Match Only
        description: Only ever output a single item per match
        value: first
        displayName: Include First Match Only
      displayOptions:
        show: {}
common_expressions:
- '={{ $parameter["mode"] === "chooseBranch" ? [0, 1] : 1 }}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: mergeByFields
    text: Add Fields to Match
  - field: options
    text: Add option
  hints:
  - field: mergeByFields
    text: Enter the field name as text
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
  "$id": "https://n8n.io/schemas/nodes/Merge.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Merge Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "mode": {
          "description": "All items of input 1, then all items of input 2",
          "type": "string",
          "enum": [
            "append",
            "combine",
            "chooseBranch"
          ],
          "default": "append"
        },
        "combinationMode": {
          "description": "Combine items with the same field values",
          "type": "string",
          "enum": [
            "mergeByFields",
            "mergeByPosition",
            "multiplex"
          ],
          "default": "mergeByFields"
        },
        "mergeByFields": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Add Fields to Match"
          ]
        },
        "joinMode": {
          "description": "Items that match, merged together (inner join)",
          "type": "string",
          "enum": [
            "keepMatches",
            "keepNonMatches",
            "keepEverything",
            "enrichInput1",
            "enrichInput2"
          ],
          "default": "keepMatches"
        },
        "outputDataFrom": {
          "description": "",
          "type": "string",
          "enum": [
            "both",
            "input1",
            "input2"
          ],
          "default": "both"
        },
        "chooseBranchMode": {
          "description": "",
          "type": "string",
          "enum": [
            "waitForBoth"
          ],
          "default": "waitForBoth"
        },
        "output": {
          "description": "",
          "type": "string",
          "enum": [
            "input1",
            "input2",
            "empty"
          ],
          "default": "input1"
        },
        "options": {
          "description": "Whether to disallow referencing child fields using `parent.child` in the field name",
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
      "2",
      "2.1"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2', '2.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
