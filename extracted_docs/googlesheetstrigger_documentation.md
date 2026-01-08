---
title: "Node: Google Sheets Trigger"
slug: "node-googlesheetstrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when Google Sheets events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Google Sheets Trigger

**Purpose.** Starts the workflow when Google Sheets events occur
**Subtitle.** ={{($parameter["event"])}}


---

## Node Details

- **Icon:** `file:googleSheets.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **googleSheetsTriggerOAuth2Api**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleSheetsTriggerOAuth2Api` | ✓ | {'show': {'authentication': ['triggerOAuth2']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | hidden | triggerOAuth2 | ✗ |  |  |
| Trigger On | `event` | options | anyUpdate | ✓ | It will be triggered also by newly created columns (if the 'Columns to Watch' option is not set) |  |

**Trigger On options:**

* **Row Added** (`rowAdded`)
* **Row Updated** (`rowUpdate`)
* **Row Added or Updated** (`anyUpdate`)

| Include in Output | `includeInOutput` | options | new | ✗ | This option will be effective only when automatically executing the workflow |  |

**Include in Output options:**

* **New Version** (`new`)
* **Old Version** (`old`)
* **Both Versions** (`both`)

| Options | `options` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Columns to Watch | `columnsToWatch` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Data Location on Sheet | `dataLocationOnSheet` | fixedCollection |  | Manually specify the data range |
| Value Render | `valueRender` | options | UNFORMATTED_VALUE | Values will be calculated, but not formatted in the reply |
| DateTime Render | `dateTimeRenderOption` | options | SERIAL_NUMBER | Fields will be returned as doubles in "serial number" format (as popularized by Lotus 1-2-3) |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{($parameter["event"])}}`

---

## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |

---

## Notes & Caveats

* This node is part of n8n-nodes-base
* Categories: Data & Storage, Productivity
* Aliases: CSV, Spreadsheet, GS

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleSheetsTrigger
displayName: Google Sheets Trigger
description: Starts the workflow when Google Sheets events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: googleSheetsTriggerOAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: hidden
  default: triggerOAuth2
  required: false
  description: ''
  typeInfo:
    type: hidden
    displayName: Authentication
    name: authentication
- id: event
  name: Trigger On
  type: options
  default: anyUpdate
  required: true
  description: It will be triggered also by newly created columns (if the 'Columns
    to Watch' option is not set)
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Trigger On
    name: event
    possibleValues:
    - value: rowAdded
      name: Row Added
      description: ''
    - value: rowUpdate
      name: Row Updated
      description: ''
    - value: anyUpdate
      name: Row Added or Updated
      description: ''
- id: includeInOutput
  name: Include in Output
  type: options
  default: new
  required: false
  description: This option will be effective only when automatically executing the
    workflow
  validation:
    displayOptions:
      hide:
        event:
        - rowAdded
  typeInfo:
    type: options
    displayName: Include in Output
    name: includeInOutput
    possibleValues:
    - value: new
      name: New Version
      description: ''
    - value: old
      name: Old Version
      description: ''
    - value: both
      name: Both Versions
      description: ''
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  hint: First row is row 1
  placeholder: Add option
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: collection
    displayName: Options
    name: options
    typeOptions:
      loadOptionsMethod: getSheetHeaderRowAndSkipEmpty
    subProperties:
    - displayName: Columns to Watch
      name: columnsToWatch
      type: multiOptions
      description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
      default: []
      typeOptions:
        loadOptionsMethod: getSheetHeaderRowAndSkipEmpty
      displayOptions:
        show: {}
    - displayName: Data Location on Sheet
      name: dataLocationOnSheet
      type: fixedCollection
      description: Manually specify the data range
      placeholder: Select Range
      hint: First row is row 1
      value: specifyRangeA1
      default: ''
      options:
      - name: values
        displayName: Values
        values:
        - displayName: Range Definition
          name: rangeDefinition
          type: options
          description: Manually specify the data range
          value: specifyRangeA1
          default: ''
          options:
          - name: Specify Range (A1 Notation)
            description: Manually specify the data range
            value: specifyRangeA1
            displayName: Specify Range (a1 Notation)
          - name: Specify Range (Rows)
            description: Manually specify the data range
            value: specifyRange
            displayName: Specify Range (rows)
        - displayName: Header Row
          name: headerRow
          type: number
          description: Index of the row which contains the keys. Starts at 1. The
            incoming node data is matched to the keys for assignment. The matching
            is case sensitive.
          hint: First row is row 1
          default: 1
          typeOptions:
            minValue: 1
          displayOptions:
            show:
              rangeDefinition:
              - specifyRange
        - displayName: First Data Row
          name: firstDataRow
          type: number
          description: Index of the first row which contains the actual data and not
            the keys. Starts with 1.
          hint: First row is row 1
          default: 2
          typeOptions:
            minValue: 1
          displayOptions:
            show:
              rangeDefinition:
              - specifyRange
        - displayName: Range
          name: range
          type: string
          description: The table range to read from or to append data to. See the
            Google <a href="https://developers.google.com/sheets/api/guides/values#writing">documentation</a>
            for the details.
          placeholder: A:Z
          hint: You can specify both the rows and the columns, e.g. C4:E7
          default: ''
          displayOptions:
            show:
              rangeDefinition:
              - specifyRangeA1
      typeOptions:
        minValue: 1
      displayOptions:
        show:
          rangeDefinition:
          - specifyRange
    - displayName: Value Render
      name: valueRender
      type: options
      description: Values will be calculated, but not formatted in the reply
      value: UNFORMATTED_VALUE
      default: UNFORMATTED_VALUE
      options:
      - name: Unformatted
        description: Values will be calculated, but not formatted in the reply
        value: UNFORMATTED_VALUE
        displayName: Unformatted
      - name: Formatted
        description: Values will be formatted and calculated according to the cell's
          formatting (based on the spreadsheet's locale)
        value: FORMATTED_VALUE
        displayName: Formatted
      - name: Formula
        description: Values will not be calculated. The reply will include the formulas.
        value: FORMULA
        displayName: Formula
      displayOptions:
        hide: {}
    - displayName: DateTime Render
      name: dateTimeRenderOption
      type: options
      description: Fields will be returned as doubles in "serial number" format (as
        popularized by Lotus 1-2-3)
      value: SERIAL_NUMBER
      default: SERIAL_NUMBER
      options:
      - name: Serial Number
        description: Fields will be returned as doubles in "serial number" format
          (as popularized by Lotus 1-2-3)
        value: SERIAL_NUMBER
        displayName: Serial Number
      - name: Formatted String
        description: Fields will be rendered as strings in their given number format
          (which depends on the spreadsheet locale)
        value: FORMATTED_STRING
        displayName: Formatted String
      displayOptions:
        hide: {}
common_expressions:
- ={{($parameter["event"])}}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  hints:
  - field: options
    text: First row is row 1
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/googleSheetsTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Sheets Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "default": "triggerOAuth2"
        },
        "event": {
          "description": "It will be triggered also by newly created columns (if the 'Columns to Watch' option is not set)",
          "type": "string",
          "enum": [
            "rowAdded",
            "rowUpdate",
            "anyUpdate"
          ],
          "default": "anyUpdate"
        },
        "includeInOutput": {
          "description": "This option will be effective only when automatically executing the workflow",
          "type": "string",
          "enum": [
            "new",
            "old",
            "both"
          ],
          "default": "new"
        },
        "options": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
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
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
    "version": "1"
  },
  "credentials": [
    {
      "name": "googleSheetsTriggerOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
