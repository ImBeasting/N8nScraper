---
title: "Node: Sort"
slug: "node-sort"
version: "1"
updated: "2026-01-08"
summary: "Change items order"
node_type: "regular"
group: "['transform']"
---

# Node: Sort

**Purpose.** Change items order


---

## Node Details

- **Icon:** `file:sort.svg`
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
| Type | `type` | options | simple | ✗ | The type of sorting to perform |  |

**Type options:**

* **Simple** (`simple`)
* **Random** (`random`)
* **Code** (`code`)

| Fields To Sort By | `sortFieldsUi` | fixedCollection |  | ✓ | The field to sort by | e.g. Add Field To Sort By |  |

<details>
<summary><strong>Fields To Sort By sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| sortField | `sortField` |  |  |  |

</details>

| Code | `code` | string | // The two items to compare are in the variables a and b
	// Access the fields in a.json and b.json
	// Return -1 if a should go before b
	// Return 1 if b should go before a
	// Return 0 if there's no difference

	fieldName = 'myField';

	if (a.json[fieldName] < b.json[fieldName]) {
	return -1;
	}
	if (a.json[fieldName] > b.json[fieldName]) {
	return 1;
	}
	return 0; | ✗ | Javascript code to determine the order of any two items |  |
| Options | `options` | collection | {} | ✗ | Whether to disallow referencing child fields using `parent.child` in the field name | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Disable Dot Notation | `disableDotNotation` | boolean | False | Whether to disallow referencing child fields using `parent.child` in the field name |

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
* Aliases: Sort, Order, Transform, Array, List, Item, Random

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: sort
displayName: Sort
description: Change items order
version: '1'
nodeType: regular
group:
- transform
params:
- id: type
  name: Type
  type: options
  default: simple
  required: false
  description: The type of sorting to perform
  typeInfo:
    type: options
    displayName: Type
    name: type
    possibleValues:
    - value: simple
      name: Simple
      description: ''
    - value: random
      name: Random
      description: ''
    - value: code
      name: Code
      description: ''
- id: sortFieldsUi
  name: Fields To Sort By
  type: fixedCollection
  default: ''
  required: true
  description: The field to sort by
  hint: Enter the field name as text
  placeholder: Add Field To Sort By
  validation:
    required: true
    displayOptions:
      show:
        type:
        - simple
  typeInfo:
    type: fixedCollection
    displayName: Fields To Sort By
    name: sortFieldsUi
    typeOptions:
      multipleValues: true
    subProperties:
    - name: sortField
      values:
      - displayName: Field Name
        name: fieldName
        type: string
        description: The field to sort by
        placeholder: e.g. id
        hint: Enter the field name as text
        default: ''
        required: true
      - displayName: Order
        name: order
        type: options
        description: The order to sort by
        value: ascending
        default: ascending
        options:
        - name: Ascending
          value: ascending
          displayName: Ascending
        - name: Descending
          value: descending
          displayName: Descending
- id: code
  name: Code
  type: string
  default: "// The two items to compare are in the variables a and b\n\t// Access\
    \ the fields in a.json and b.json\n\t// Return -1 if a should go before b\n\t\
    // Return 1 if b should go before a\n\t// Return 0 if there's no difference\n\n\
    \tfieldName = 'myField';\n\n\tif (a.json[fieldName] < b.json[fieldName]) {\n\t\
    return -1;\n\t}\n\tif (a.json[fieldName] > b.json[fieldName]) {\n\treturn 1;\n\
    \t}\n\treturn 0;"
  required: false
  description: Javascript code to determine the order of any two items
  validation:
    displayOptions:
      show:
        type:
        - code
  typeInfo:
    type: string
    displayName: Code
    name: code
    typeOptions:
      rows: 10
      alwaysOpenEditWindow: true
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
      show:
        type:
        - simple
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
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: sortFieldsUi
    text: Add Field To Sort By
  - field: options
    text: Add Field
  hints:
  - field: sortFieldsUi
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
  "$id": "https://n8n.io/schemas/nodes/sort.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Sort Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "type": {
          "description": "The type of sorting to perform",
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
          "default": "// The two items to compare are in the variables a and b\n\t// Access the fields in a.json and b.json\n\t// Return -1 if a should go before b\n\t// Return 1 if b should go before a\n\t// Return 0 if there's no difference\n\n\tfieldName = 'myField';\n\n\tif (a.json[fieldName] < b.json[fieldName]) {\n\treturn -1;\n\t}\n\tif (a.json[fieldName] > b.json[fieldName]) {\n\treturn 1;\n\t}\n\treturn 0;"
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
