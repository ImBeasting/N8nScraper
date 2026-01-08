---
title: "Node: Compare Datasets"
slug: "node-comparedatasets"
version: "['1', '2', '2.1', '2.2', '2.3']"
updated: "2026-01-08"
summary: "Compare two inputs for changes"
node_type: "regular"
group: "['transform']"
---

# Node: Compare Datasets

**Purpose.** Compare two inputs for changes


---

## Node Details

- **Icon:** `file:compare.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main', 'Main']`
- **Outputs:** `['Main', 'Main', 'Main', 'Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **infoBox**: Items from different branches are paired together when the fields below match. If paired, the rest of the fields are compared to determine whether the items are the same or different

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Fields to Match | `mergeByFields` | fixedCollection |  | ✗ | e.g. Add Fields to Match |  |

<details>
<summary><strong>Fields to Match sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Values | `values` |  |  |  |

</details>

| When There Are Differences | `resolve` | options | preferInput2 | ✗ | Output uses different inputs for different fields |  |

**When There Are Differences options:**

* **Use Input A Version** (`preferInput1`)
* **Use Input B Version** (`preferInput2`)
* **Use a Mix of Versions** (`mix`) - Output uses different inputs for different fields
* **Include Both Versions** (`includeBoth`) - Output contains all data (but structure more complex)

| When There Are Differences | `resolve` | options | includeBoth | ✗ | Output uses different inputs for different fields |  |

**When There Are Differences options:**

* **Use Input A Version** (`preferInput1`)
* **Use Input B Version** (`preferInput2`)
* **Use a Mix of Versions** (`mix`) - Output uses different inputs for different fields
* **Include Both Versions** (`includeBoth`) - Output contains all data (but structure more complex)

| Fuzzy Compare | `fuzzyCompare` | boolean | False | ✗ | Whether to tolerate small type differences when comparing fields. E.g. the number 3 and the string '3' are treated as the same. |  |
| Prefer | `preferWhenMix` | options | input1 | ✗ |  |  |

**Prefer options:**

* **Input A Version** (`input1`)
* **Input B Version** (`input2`)

| For Everything Except | `exceptWhenMix` | string |  | ✗ | e.g. e.g. id, country |  |
| Options | `options` | collection | {} | ✗ | Fields that shouldn't be included when checking whether two items are the same | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields to Skip Comparing | `skipFields` | string |  | Fields that shouldn't be included when checking whether two items are the same |
| Fuzzy Compare | `fuzzyCompare` | boolean | False | Whether to tolerate small type differences when comparing fields. E.g. the number 3 and the string '3' are treated as the same. |
| Disable Dot Notation | `disableDotNotation` | boolean | False | Whether to disallow referencing child fields using `parent.child` in the field name |
| Multiple Matches | `multipleMatches` | options | first | Only ever output a single item per match |

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
* Aliases: Join, Concatenate, Compare, Dataset, Split, Sync, Syncing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: compareDatasets
displayName: Compare Datasets
description: Compare two inputs for changes
version:
- '1'
- '2'
- '2.1'
- '2.2'
- '2.3'
nodeType: regular
group:
- transform
params:
- id: mergeByFields
  name: Fields to Match
  type: fixedCollection
  default: ''
  required: false
  description: ''
  hint: Enter the field name as text
  placeholder: Add Fields to Match
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
      - displayName: Input A Field
        name: field1
        type: string
        placeholder: e.g. id
        hint: Enter the field name as text
        default: ''
      - displayName: Input B Field
        name: field2
        type: string
        placeholder: e.g. id
        hint: Enter the field name as text
        default: ''
- id: resolve
  name: When There Are Differences
  type: options
  default: preferInput2
  required: false
  description: Output uses different inputs for different fields
  validation: &id001
    displayOptions:
      hide: {}
  typeInfo: &id002
    type: options
    displayName: When There Are Differences
    name: resolve
    possibleValues:
    - value: preferInput1
      name: Use Input A Version
      description: ''
    - value: preferInput2
      name: Use Input B Version
      description: ''
    - value: mix
      name: Use a Mix of Versions
      description: Output uses different inputs for different fields
    - value: includeBoth
      name: Include Both Versions
      description: Output contains all data (but structure more complex)
- id: resolve
  name: When There Are Differences
  type: options
  default: includeBoth
  required: false
  description: Output uses different inputs for different fields
  validation: *id001
  typeInfo: *id002
- id: fuzzyCompare
  name: Fuzzy Compare
  type: boolean
  default: false
  required: false
  description: Whether to tolerate small type differences when comparing fields. E.g.
    the number 3 and the string '3' are treated as the same.
  validation:
    displayOptions:
      hide: {}
  typeInfo:
    type: boolean
    displayName: Fuzzy Compare
    name: fuzzyCompare
- id: preferWhenMix
  name: Prefer
  type: options
  default: input1
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        resolve:
        - mix
  typeInfo:
    type: options
    displayName: Prefer
    name: preferWhenMix
    possibleValues:
    - value: input1
      name: Input A Version
      description: ''
    - value: input2
      name: Input B Version
      description: ''
- id: exceptWhenMix
  name: For Everything Except
  type: string
  default: ''
  required: false
  description: ''
  hint: Enter the names of the input fields as text, separated by commas
  placeholder: e.g. id, country
  validation:
    displayOptions:
      show:
        resolve:
        - mix
  typeInfo:
    type: string
    displayName: For Everything Except
    name: exceptWhenMix
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Fields that shouldn't be included when checking whether two items are
    the same
  hint: Enter the field names as text, separated by commas
  placeholder: Add option
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Fields to Skip Comparing
      name: skipFields
      type: string
      description: Fields that shouldn't be included when checking whether two items
        are the same
      placeholder: e.g. updated_at, updated_by
      hint: Enter the field names as text, separated by commas
      default: ''
    - displayName: Fuzzy Compare
      name: fuzzyCompare
      type: boolean
      description: Whether to tolerate small type differences when comparing fields.
        E.g. the number 3 and the string '3' are treated as the same.
      default: false
      displayOptions:
        show: {}
    - displayName: Disable Dot Notation
      name: disableDotNotation
      type: boolean
      description: Whether to disallow referencing child fields using `parent.child`
        in the field name
      default: false
    - displayName: Multiple Matches
      name: multipleMatches
      type: options
      description: Only ever output a single item per match
      value: first
      default: first
      options:
      - name: Include First Match Only
        description: Only ever output a single item per match
        value: first
        displayName: Include First Match Only
      - name: Include All Matches
        description: Output multiple items if there are multiple matches
        value: all
        displayName: Include All Matches
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: infoBox
    text: Items from different branches are paired together when the fields below
      match. If paired, the rest of the fields are compared to determine whether the
      items are the same or different
    conditions: null
  tooltips: []
  placeholders:
  - field: mergeByFields
    text: Add Fields to Match
  - field: exceptWhenMix
    text: e.g. id, country
  - field: options
    text: Add option
  hints:
  - field: mergeByFields
    text: Enter the field name as text
  - field: exceptWhenMix
    text: Enter the names of the input fields as text, separated by commas
  - field: options
    text: Enter the field names as text, separated by commas
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
  "$id": "https://n8n.io/schemas/nodes/compareDatasets.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Compare Datasets Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "mergeByFields": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Add Fields to Match"
          ]
        },
        "resolve": {
          "description": "Output uses different inputs for different fields",
          "type": "string",
          "enum": [
            "preferInput1",
            "preferInput2",
            "mix",
            "includeBoth"
          ],
          "default": "includeBoth"
        },
        "fuzzyCompare": {
          "description": "Whether to tolerate small type differences when comparing fields. E.g. the number 3 and the string '3' are treated as the same.",
          "type": "boolean",
          "default": false
        },
        "preferWhenMix": {
          "description": "",
          "type": "string",
          "enum": [
            "input1",
            "input2"
          ],
          "default": "input1"
        },
        "exceptWhenMix": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. id, country"
          ]
        },
        "options": {
          "description": "Fields that shouldn't be included when checking whether two items are the same",
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
      "2",
      "2.1",
      "2.2",
      "2.3"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2', '2.1', '2.2', '2.3'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
