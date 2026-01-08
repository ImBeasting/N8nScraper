---
title: "Node: Set"
slug: "node-set"
version: "['3', '3.1', '3.2', '3.3', '3.4']"
updated: "2026-01-08"
summary: "Add or edit fields on an input item and optionally remove other fields"
node_type: "regular"
group: "['input']"
---

# Node: Set

**Purpose.** Add or edit fields on an input item and optionally remove other fields
**Subtitle.** ={{$parameter["mode"]}}


---

## Node Details

- **Icon:** `fa:pen`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **duplicateWarning** when duplicateItem=[True]: Item duplication is set in the node settings. This option will be ignored when the workflow runs automatically.

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Mode | `mode` | options | manual | ✗ | Edit item fields one by one |  |

**Mode options:**

* **Manual Mapping** (`manual`) - Edit item fields one by one
* **JSON** (`raw`) - Customize item output with JSON

| Duplicate Item | `duplicateItem` | boolean | False | ✗ | Whether this item should be duplicated a set number of times |  |
| Duplicate Item Count | `duplicateCount` | number | 0 | ✗ | How many times the item should be duplicated, mainly used for testing and debugging | min:0, max:∞ |
| Include in Output | `include` | options | all | ✗ | How to select the fields you want to include in your output items |  |

**Include in Output options:**

* **All Input Fields** (``) - Also include all unchanged fields from the input
* **No Input Fields** (``) - Include only the fields specified above
* **Selected Input Fields** (``) - Also include the fields listed in the parameter “Fields to Include”
* **All Input Fields Except** (``) - Exclude the fields listed in the parameter “Fields to Exclude”

| Include Other Input Fields | `includeOtherFields` | boolean | False | ✗ | Whether to pass to the output all the input fields (along with the fields set in 'Fields to Set') |  |
| Input Fields to Include | `include` | options | all | ✗ | How to select the fields you want to include in your output items |  |

**Input Fields to Include options:**

* **All** (``) - Also include all unchanged fields from the input
* **Selected** (``) - Also include the fields listed in the parameter “Fields to Include”
* **All Except** (``) - Exclude the fields listed in the parameter “Fields to Exclude”

| Fields to Include | `includeFields` | string |  | ✗ | Comma-separated list of the field names you want to include in the output. You can drag the selected fields from the input panel. | e.g. e.g. fieldToInclude1,fieldToInclude2 |  |
| Fields to Exclude | `excludeFields` | string |  | ✗ | Comma-separated list of the field names you want to exclude from the output. You can drag the selected fields from the input panel. | e.g. e.g. fieldToExclude1,fieldToExclude2 |  |
| Fields to Include | `includeFields` | string |  | ✗ | Comma-separated list of the field names you want to include in the output. You can drag the selected fields from the input panel. | e.g. e.g. fieldToInclude1,fieldToInclude2 |  |
| Fields to Exclude | `excludeFields` | string |  | ✗ | Comma-separated list of the field names you want to exclude from the output. You can drag the selected fields from the input panel. | e.g. e.g. fieldToExclude1,fieldToExclude2 |  |
| Options | `options` | collection | {} | ✗ | Whether binary data should be included if present in the input item | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Binary File | `includeBinary` | boolean | True | Whether binary data should be included if present in the input item |
| Strip Binary Data | `stripBinary` | boolean | True | Whether binary data should be stripped from the input item. Only applies when "Include Other Input Fields" is enabled. |
| Ignore Type Conversion Errors | `ignoreConversionErrors` | boolean | False | Whether to ignore field type errors and apply a less strict type conversion |
| Support Dot Notation | `dotNotation` | boolean | True | By default, dot-notation is used in property names. This means that "a.b" will set the property "b" underneath "a" so { "a": { "b": value} }. If that is not intended this can be deactivated, it will then set { "a.b": value } instead. |

</details>

| Fields to Set | `fields` | fixedCollection | {} | ✗ | Edit existing fields or add new ones to modify the output data | e.g. Add Field |  |

<details>
<summary><strong>Fields to Set sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Values | `values` |  |  |  |

</details>

| Fields to Set | `assignments` | assignmentCollection | {} | ✗ |  |  |
| JSON | `jsonOutput` | json | {\n   | ✗ |  |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["mode"]}}`

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
node: set
displayName: Set
description: Add or edit fields on an input item and optionally remove other fields
version:
- '3'
- '3.1'
- '3.2'
- '3.3'
- '3.4'
nodeType: regular
group:
- input
params:
- id: mode
  name: Mode
  type: options
  default: manual
  required: false
  description: Edit item fields one by one
  typeInfo:
    type: options
    displayName: Mode
    name: mode
    possibleValues:
    - value: manual
      name: Manual Mapping
      description: Edit item fields one by one
    - value: raw
      name: JSON
      description: Customize item output with JSON
- id: duplicateItem
  name: Duplicate Item
  type: boolean
  default: false
  required: false
  description: Whether this item should be duplicated a set number of times
  typeInfo:
    type: boolean
    displayName: Duplicate Item
    name: duplicateItem
- id: duplicateCount
  name: Duplicate Item Count
  type: number
  default: 0
  required: false
  description: How many times the item should be duplicated, mainly used for testing
    and debugging
  validation:
    displayOptions:
      show:
        duplicateItem:
        - true
  typeInfo:
    type: number
    displayName: Duplicate Item Count
    name: duplicateCount
    typeOptions:
      minValue: 0
- id: include
  name: Include in Output
  type: options
  default: all
  required: false
  description: How to select the fields you want to include in your output items
  validation: &id001
    displayOptions:
      hide: {}
  typeInfo: &id002
    type: options
    displayName: Input Fields to Include
    name: include
    possibleValues:
    - value: All
      name: All
      description: Also include all unchanged fields from the input
    - value: Selected
      name: Selected
      description: Also include the fields listed in the parameter “Fields to Include”
    - value: All Except
      name: All Except
      description: Exclude the fields listed in the parameter “Fields to Exclude”
- id: includeOtherFields
  name: Include Other Input Fields
  type: boolean
  default: false
  required: false
  description: Whether to pass to the output all the input fields (along with the
    fields set in 'Fields to Set')
  validation:
    displayOptions:
      hide: {}
  typeInfo:
    type: boolean
    displayName: Include Other Input Fields
    name: includeOtherFields
- id: include
  name: Input Fields to Include
  type: options
  default: all
  required: false
  description: How to select the fields you want to include in your output items
  validation: *id001
  typeInfo: *id002
- id: includeFields
  name: Fields to Include
  type: string
  default: ''
  required: false
  description: Comma-separated list of the field names you want to include in the
    output. You can drag the selected fields from the input panel.
  placeholder: e.g. fieldToInclude1,fieldToInclude2
  validation: &id003
    displayOptions:
      show:
        include:
        - selected
      hide: {}
  typeInfo: &id004
    type: string
    displayName: Fields to Include
    name: includeFields
- id: excludeFields
  name: Fields to Exclude
  type: string
  default: ''
  required: false
  description: Comma-separated list of the field names you want to exclude from the
    output. You can drag the selected fields from the input panel.
  placeholder: e.g. fieldToExclude1,fieldToExclude2
  validation: &id005
    displayOptions:
      show:
        include:
        - except
      hide: {}
  typeInfo: &id006
    type: string
    displayName: Fields to Exclude
    name: excludeFields
- id: includeFields
  name: Fields to Include
  type: string
  default: ''
  required: false
  description: Comma-separated list of the field names you want to include in the
    output. You can drag the selected fields from the input panel.
  placeholder: e.g. fieldToInclude1,fieldToInclude2
  validation: *id003
  typeInfo: *id004
- id: excludeFields
  name: Fields to Exclude
  type: string
  default: ''
  required: false
  description: Comma-separated list of the field names you want to exclude from the
    output. You can drag the selected fields from the input panel.
  placeholder: e.g. fieldToExclude1,fieldToExclude2
  validation: *id005
  typeInfo: *id006
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether binary data should be included if present in the input item
  placeholder: Add option
  validation:
    displayOptions:
      hide: {}
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Include Binary File
      name: includeBinary
      type: boolean
      description: Whether binary data should be included if present in the input
        item
      default: true
      displayOptions:
        hide: {}
    - displayName: Strip Binary Data
      name: stripBinary
      type: boolean
      description: Whether binary data should be stripped from the input item. Only
        applies when "Include Other Input Fields" is enabled.
      default: true
      displayOptions:
        show: {}
    - displayName: Ignore Type Conversion Errors
      name: ignoreConversionErrors
      type: boolean
      description: Whether to ignore field type errors and apply a less strict type
        conversion
      default: false
      displayOptions:
        show: {}
    - displayName: Support Dot Notation
      name: dotNotation
      type: boolean
      description: 'By default, dot-notation is used in property names. This means
        that "a.b" will set the property "b" underneath "a" so { "a": { "b": value}
        }. If that is not intended this can be deactivated, it will then set { "a.b":
        value } instead.'
      default: true
- id: fields
  name: Fields to Set
  type: fixedCollection
  default: {}
  required: false
  description: Edit existing fields or add new ones to modify the output data
  placeholder: Add Field
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: fixedCollection
    displayName: Fields to Set
    name: fields
    typeOptions:
      multipleValues: true
    subProperties:
    - name: values
      displayName: Values
      values:
      - displayName: Name
        name: name
        type: string
        description: 'Name of the field to set the value of. Supports dot-notation.
          Example: data.person[0].name.'
        placeholder: e.g. fieldName
        default: ''
      - displayName: Type
        name: type
        type: options
        description: The field value type
        value: stringValue
        default: stringValue
        options:
        - name: String
          value: stringValue
          displayName: String
        - name: Number
          value: numberValue
          displayName: Number
        - name: Boolean
          value: booleanValue
          displayName: Boolean
        - name: Array
          value: arrayValue
          displayName: Array
        - name: Object
          value: objectValue
          displayName: Object
      - displayName: Value
        name: stringValue
        type: string
        validateType: string
        default: ''
        displayOptions:
          show:
            type:
            - stringValue
      - displayName: Value
        name: numberValue
        type: string
        validateType: number
        default: ''
        displayOptions:
          show:
            type:
            - numberValue
      - displayName: Value
        name: booleanValue
        type: options
        validateType: boolean
        value: 'true'
        default: 'true'
        options:
        - name: 'True'
          value: 'true'
          displayName: 'True'
        - name: 'False'
          value: 'false'
          displayName: 'False'
        displayOptions:
          show:
            type:
            - booleanValue
      - displayName: Value
        name: arrayValue
        type: string
        placeholder: e.g. [ arrayItem1, arrayItem2, arrayItem3 ]
        validateType: array
        default: ''
        displayOptions:
          show:
            type:
            - arrayValue
      - displayName: Value
        name: objectValue
        type: json
        validateType: object
        default: ={}
        typeOptions:
          rows: 2
        displayOptions:
          show:
            type:
            - objectValue
- id: assignments
  name: Fields to Set
  type: assignmentCollection
  default: {}
  required: false
  description: ''
  validation:
    displayOptions:
      hide: {}
  typeInfo:
    type: assignmentCollection
    displayName: Fields to Set
    name: assignments
- id: jsonOutput
  name: JSON
  type: json
  default: '{\n  '
  required: false
  description: ''
  typeInfo:
    type: json
    displayName: JSON
    name: jsonOutput
    typeOptions:
      rows: 5
common_expressions:
- ={{$parameter["mode"]}}
ui_elements:
  notices:
  - name: duplicateWarning
    text: Item duplication is set in the node settings. This option will be ignored
      when the workflow runs automatically.
    conditions:
      show:
        duplicateItem:
        - true
  tooltips: []
  placeholders:
  - field: includeFields
    text: e.g. fieldToInclude1,fieldToInclude2
  - field: excludeFields
    text: e.g. fieldToExclude1,fieldToExclude2
  - field: includeFields
    text: e.g. fieldToInclude1,fieldToInclude2
  - field: excludeFields
    text: e.g. fieldToExclude1,fieldToExclude2
  - field: options
    text: Add option
  - field: fields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/set.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Set Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "mode": {
          "description": "Edit item fields one by one",
          "type": "string",
          "enum": [
            "manual",
            "raw"
          ],
          "default": "manual"
        },
        "duplicateItem": {
          "description": "Whether this item should be duplicated a set number of times",
          "type": "boolean",
          "default": false
        },
        "duplicateCount": {
          "description": "How many times the item should be duplicated, mainly used for testing and debugging",
          "type": "number",
          "default": 0
        },
        "include": {
          "description": "How to select the fields you want to include in your output items",
          "type": "string",
          "enum": [
            "All",
            "Selected",
            "All Except"
          ],
          "default": "all"
        },
        "includeOtherFields": {
          "description": "Whether to pass to the output all the input fields (along with the fields set in 'Fields to Set')",
          "type": "boolean",
          "default": false
        },
        "includeFields": {
          "description": "Comma-separated list of the field names you want to include in the output. You can drag the selected fields from the input panel.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. fieldToInclude1,fieldToInclude2"
          ]
        },
        "excludeFields": {
          "description": "Comma-separated list of the field names you want to exclude from the output. You can drag the selected fields from the input panel.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. fieldToExclude1,fieldToExclude2"
          ]
        },
        "options": {
          "description": "Whether binary data should be included if present in the input item",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "fields": {
          "description": "Edit existing fields or add new ones to modify the output data",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "assignments": {
          "description": "",
          "type": "string",
          "default": {}
        },
        "jsonOutput": {
          "description": "",
          "type": "string",
          "default": "{\\n  "
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
      "3.3",
      "3.4"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['3', '3.1', '3.2', '3.3', '3.4'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
