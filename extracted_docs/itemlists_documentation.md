---
title: "Node: Item Lists"
slug: "node-itemlists"
version: "1.0"
updated: "2026-01-08"
summary: "Helper for working with lists of items and transforming arrays"
node_type: "regular"
group: "['input']"
---

# Node: Item Lists

**Purpose.** Helper for working with lists of items and transforming arrays
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:itemLists.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Operations

### Itemlist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Concatenate Items | `concatenateItems` | Combine fields into a list in a single new item |
| Limit | `limit` | Remove items if there are too many |
| Remove Duplicates | `removeDuplicates` | Remove extra items that are similar |
| Sort | `sort` | Change the item order |
| Split Out Items | `splitOutItems` | Turn a list or values of object's properties inside item(s) into separate items |
| Summarize | `summarize` | Aggregate items together (pivot table) |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | hidden | itemList | ✗ | Resource to operate on |  |
---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | splitOutItems | ✗ | Combine fields into a list in a single new item |  |

**Operation options:**

* **Concatenate Items** (`concatenateItems`) - Combine fields into a list in a single new item
* **Limit** (`limit`) - Remove items if there are too many
* **Remove Duplicates** (`removeDuplicates`) - Remove extra items that are similar
* **Sort** (`sort`) - Change the item order
* **Split Out Items** (`splitOutItems`) - Turn a list or values of object's properties inside item(s) into separate items
* **Summarize** (`summarize`) - Aggregate items together (pivot table)

---

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ": " + $parameter["resource"]}}`

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
* Aliases: Aggregate, Dedupe, Deduplicate, Duplicates, Limit, Remove, Slice, Sort, Split, Unique, JSON, Transform, Array, List, Object, Item, Map, Format, Nested, Iterate, Summarise, Summarize, Group, Pivot, Sum, Count, Min, Max

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: itemLists
displayName: Item Lists
description: Helper for working with lists of items and transforming arrays
version: '1.0'
nodeType: regular
group:
- input
operations:
- id: concatenateItems
  name: Concatenate Items
  description: Combine fields into a list in a single new item
- id: limit
  name: Limit
  description: Remove items if there are too many
- id: removeDuplicates
  name: Remove Duplicates
  description: Remove extra items that are similar
- id: sort
  name: Sort
  description: Change the item order
- id: splitOutItems
  name: Split Out Items
  description: Turn a list or values of object's properties inside item(s) into separate
    items
- id: summarize
  name: Summarize
  description: Aggregate items together (pivot table)
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: fieldsToExclude
    text: e.g. email, name
  - field: fieldsToCompare
    text: e.g. email, name
  - field: options
    text: Add Field
  - field: fieldsToAggregate
    text: Add Field To Aggregate
  - field: fieldsToExclude
    text: e.g. email, name
  - field: fieldsToInclude
    text: e.g. email, name
  - field: options
    text: Add Field
  - field: sortFieldsUi
    text: Add Field To Sort By
  - field: options
    text: Add Field
  - field: fieldToSplitOut
    text: Drag fields from the left or type their names
  - field: fieldsToInclude
    text: e.g. email, name
  - field: options
    text: Add Field
  - field: fieldsToSummarize
    text: Add Field
  - field: fieldsToSplitBy
    text: e.g. country, city
  - field: fieldsToSplitBy
    text: e.g. country, city
  hints:
  - field: fieldsToAggregate
    text: Enter the field name as text
  - field: sortFieldsUi
    text: Enter the field name as text
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
  "$id": "https://n8n.io/schemas/nodes/itemLists.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Item Lists Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "concatenateItems",
        "limit",
        "removeDuplicates",
        "sort",
        "splitOutItems",
        "summarize"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "default": "itemList"
        },
        "maxItems": {
          "description": "If there are more items than this number, some are removed",
          "type": "number",
          "default": 1
        },
        "keep": {
          "description": "When removing items, whether to keep the ones at the start or the ending",
          "type": "string",
          "enum": [
            "firstItems",
            "lastItems"
          ],
          "default": "firstItems"
        },
        "compare": {
          "description": "The fields of the input items to compare to see if they are the same",
          "type": "string",
          "enum": [
            "allFields",
            "allFieldsExcept",
            "selectedFields"
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
        "fieldsToCompare": {
          "description": "Fields in the input to add to the comparison",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. email, name"
          ]
        },
        "options": {
          "description": "The field in the output under which to put the split field contents",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
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
        "disableDotNotation": {
          "description": "Whether to disallow referencing child fields using `parent.child` in the field name",
          "type": "boolean",
          "default": false
        },
        "operation": {
          "description": "Combine fields into a list in a single new item",
          "type": "string",
          "enum": [
            "concatenateItems",
            "limit",
            "removeDuplicates",
            "sort",
            "splitOutItems",
            "summarize"
          ],
          "default": "splitOutItems"
        },
        "type": {
          "description": "The fields of the input items to compare to see if they are the same",
          "type": "string",
          "enum": [
            "simple",
            "random",
            "code"
          ],
          "default": "simple"
        },
        "sortFieldsUi": {
          "description": "The field to sort by",
          "type": "string",
          "default": "",
          "examples": [
            "Add Field To Sort By"
          ]
        },
        "code": {
          "description": "Javascript code to determine the order of any two items",
          "type": "string",
          "default": "// The two items to compare are in the variables a and b\n// Access the fields in a.json and b.json\n// Return -1 if a should go before b\n// Return 1 if b should go before a\n// Return 0 if there's no difference\n\nfieldName = 'myField';\n\nif (a.json[fieldName] < b.json[fieldName]) {\nreturn -1;\n}\nif (a.json[fieldName] > b.json[fieldName]) {\nreturn 1;\n}\nreturn 0;"
        },
        "fieldToSplitOut": {
          "description": "The name of the input fields to break out into separate items. Separate multiple field names by commas. For binary data, use $binary.",
          "type": "string",
          "default": "",
          "examples": [
            "Drag fields from the left or type their names"
          ]
        },
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
    "version": "1.0"
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1.0 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
