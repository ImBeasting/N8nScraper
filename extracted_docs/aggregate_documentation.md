---
title: "Node: Aggregate"
slug: "node-aggregate"
version: "1"
updated: "2026-01-08"
summary: "Combine a field from many items into a list in a single item"
node_type: "regular"
group: "['transform']"
---

# Node: Aggregate

**Purpose.** Combine a field from many items into a list in a single item


---

## Node Details

- **Icon:** `file:aggregate.svg`
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
| Aggregate | `aggregate` | options | aggregateIndividualFields | ✗ |  |  |

**Aggregate options:**

* **Individual Fields** (`aggregateIndividualFields`)
* **All Item Data (Into a Single List)** (`aggregateAllItemData`)

| Fields To Aggregate | `fieldsToAggregate` | fixedCollection |  | ✗ | The name of a field in the input items to aggregate together | e.g. Add Field To Aggregate |  |

<details>
<summary><strong>Fields To Aggregate sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| fieldToAggregate | `fieldToAggregate` |  |  |  |

</details>

| Put Output in Field | `destinationFieldName` | string | data | ✗ | The name of the output field to put the data in |  |
| Include | `include` | options | allFields | ✗ |  |  |

**Include options:**

* **All Fields** (`allFields`)
* **Specified Fields** (`specifiedFields`)
* **All Fields Except** (`allFieldsExcept`)

| Fields To Exclude | `fieldsToExclude` | string |  | ✗ | e.g. e.g. email, name |  |
| Fields To Include | `fieldsToInclude` | string |  | ✗ | e.g. e.g. email, name |  |
| Options | `options` | collection | {} | ✗ | Whether to disallow referencing child fields using `parent.child` in the field name | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Disable Dot Notation | `disableDotNotation` | boolean | False | Whether to disallow referencing child fields using `parent.child` in the field name |
| Merge Lists | `mergeLists` | boolean | False | Whether to merge the output into a single flat list (rather than a list of lists), if the field to aggregate is a list |
| Include Binaries | `includeBinaries` | boolean | False | Whether to include the binary data in the new item |
| Keep Only Unique Binaries | `keepOnlyUnique` | boolean | False | Whether to keep only unique binaries by comparing mime types, file types, file sizes and file extensions |
| Keep Missing And Null Values | `keepMissing` | boolean | False | Whether to add a null entry to the aggregated list when there is a missing or null value |

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
* Aliases: Aggregate, Combine, Flatten, Transform, Array, List, Item

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: aggregate
displayName: Aggregate
description: Combine a field from many items into a list in a single item
version: '1'
nodeType: regular
group:
- transform
params:
- id: aggregate
  name: Aggregate
  type: options
  default: aggregateIndividualFields
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Aggregate
    name: aggregate
    possibleValues:
    - value: aggregateIndividualFields
      name: Individual Fields
      description: ''
    - value: aggregateAllItemData
      name: All Item Data (Into a Single List)
      description: ''
- id: fieldsToAggregate
  name: Fields To Aggregate
  type: fixedCollection
  default: ''
  required: false
  description: The name of a field in the input items to aggregate together
  hint: Enter the field name as text
  placeholder: Add Field To Aggregate
  validation:
    displayOptions:
      show:
        aggregate:
        - aggregateIndividualFields
  typeInfo:
    type: fixedCollection
    displayName: Fields To Aggregate
    name: fieldsToAggregate
    typeOptions:
      multipleValues: true
    subProperties:
    - name: fieldToAggregate
      values:
      - displayName: Input Field Name
        name: fieldToAggregate
        type: string
        description: The name of a field in the input items to aggregate together
        placeholder: e.g. id
        hint: Enter the field name as text
        default: ''
      - displayName: Rename Field
        name: renameField
        type: boolean
        description: Whether to give the field a different name in the output
        default: false
      - displayName: Output Field Name
        name: outputFieldName
        type: string
        description: The name of the field to put the aggregated data in. Leave blank
          to use the input field name.
        default: ''
        displayOptions:
          show:
            renameField:
            - true
- id: destinationFieldName
  name: Put Output in Field
  type: string
  default: data
  required: false
  description: The name of the output field to put the data in
  validation:
    displayOptions:
      show:
        aggregate:
        - aggregateAllItemData
  typeInfo:
    type: string
    displayName: Put Output in Field
    name: destinationFieldName
- id: include
  name: Include
  type: options
  default: allFields
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        aggregate:
        - aggregateAllItemData
  typeInfo:
    type: options
    displayName: Include
    name: include
    possibleValues:
    - value: allFields
      name: All Fields
      description: ''
    - value: specifiedFields
      name: Specified Fields
      description: ''
    - value: allFieldsExcept
      name: All Fields Except
      description: ''
- id: fieldsToExclude
  name: Fields To Exclude
  type: string
  default: ''
  required: false
  description: ''
  placeholder: e.g. email, name
  validation:
    displayOptions:
      show:
        aggregate:
        - aggregateAllItemData
        include:
        - allFieldsExcept
  typeInfo:
    type: string
    displayName: Fields To Exclude
    name: fieldsToExclude
- id: fieldsToInclude
  name: Fields To Include
  type: string
  default: ''
  required: false
  description: ''
  placeholder: e.g. email, name
  validation:
    displayOptions:
      show:
        aggregate:
        - aggregateAllItemData
        include:
        - specifiedFields
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
  validation:
    displayOptions:
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
        hide: {}
    - displayName: Merge Lists
      name: mergeLists
      type: boolean
      description: Whether to merge the output into a single flat list (rather than
        a list of lists), if the field to aggregate is a list
      default: false
      displayOptions:
        hide: {}
    - displayName: Include Binaries
      name: includeBinaries
      type: boolean
      description: Whether to include the binary data in the new item
      default: false
    - displayName: Keep Only Unique Binaries
      name: keepOnlyUnique
      type: boolean
      description: Whether to keep only unique binaries by comparing mime types, file
        types, file sizes and file extensions
      default: false
      displayOptions:
        show:
          includeBinaries:
          - true
    - displayName: Keep Missing And Null Values
      name: keepMissing
      type: boolean
      description: Whether to add a null entry to the aggregated list when there is
        a missing or null value
      default: false
      displayOptions:
        hide: {}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: fieldsToAggregate
    text: Add Field To Aggregate
  - field: fieldsToExclude
    text: e.g. email, name
  - field: fieldsToInclude
    text: e.g. email, name
  - field: options
    text: Add Field
  hints:
  - field: fieldsToAggregate
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
  "$id": "https://n8n.io/schemas/nodes/aggregate.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Aggregate Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "aggregate": {
          "description": "",
          "type": "string",
          "enum": [
            "aggregateIndividualFields",
            "aggregateAllItemData"
          ],
          "default": "aggregateIndividualFields"
        },
        "fieldsToAggregate": {
          "description": "The name of a field in the input items to aggregate together",
          "type": "string",
          "default": "",
          "examples": [
            "Add Field To Aggregate"
          ]
        },
        "destinationFieldName": {
          "description": "The name of the output field to put the data in",
          "type": "string",
          "default": "data"
        },
        "include": {
          "description": "",
          "type": "string",
          "enum": [
            "allFields",
            "specifiedFields",
            "allFieldsExcept"
          ],
          "default": "allFields"
        },
        "fieldsToExclude": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. email, name"
          ]
        },
        "fieldsToInclude": {
          "description": "",
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
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
