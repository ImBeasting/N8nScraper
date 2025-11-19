---
title: "Node: Authentication"
slug: "node-authentication"
version: "['3', '4', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7']"
updated: "2025-11-13"
summary: "Read, update and write data to Google Sheets"
node_type: "regular"
group: "['input', 'output']"
---

# Node: Authentication

**Purpose.** Read, update and write data to Google Sheets
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `bot`
- **Group:** `['input', 'output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleApi**: N/A
- **googleSheetsOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **autoMapNotice** when operation=['append'], dataMode=['autoMapInputData']: In this mode, make sure the incoming data is named the same as the columns in your Sheet. (Use an 'Edit Fields' node before this node to change it if required.)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleApi` | ✓ | {'show': {'authentication': ['serviceAccount']}} |
| `googleSheetsOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Sheet Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Append or Update Row | `appendOrUpdate` | Append a new row or update an existing one (upsert) |
| Append Row | `append` | Create a new row in a sheet |
| Clear | `clear` | Delete all the contents or a part of a sheet |
| Create | `create` | Create a new sheet |
| Delete | `remove` | Permanently delete a sheet |
| Delete Rows or Columns | `delete` | Delete columns or rows from a sheet |
| Get Row(s) | `read` | Retrieve one or more rows from a sheet |
| Update Row | `update` | Update an existing row in a sheet |

### Spreadsheet Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a spreadsheet |
| Delete | `deleteSpreadsheet` | Delete a spreadsheet |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | sheet | ✗ | Resource to operate on |  |

**Resource options:**

* **Document** (`spreadsheet`)
* **Sheet Within Document** (`sheet`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | read | ✗ | Append a new row or update an existing one (upsert) |  |

**Operation options:**

* **Append or Update Row** (`appendOrUpdate`) - Append a new row or update an existing one (upsert)
* **Append Row** (`append`) - Create a new row in a sheet
* **Clear** (`clear`) - Delete all the contents or a part of a sheet
* **Create** (`create`) - Create a new sheet
* **Delete** (`remove`) - Permanently delete a sheet
* **Delete Rows or Columns** (`delete`) - Delete columns or rows from a sheet
* **Get Row(s)** (`read`) - Retrieve one or more rows from a sheet
* **Update Row** (`update`) - Update an existing row in a sheet

---

### Append or Update Row parameters (`appendOrUpdate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Sheet | `sheetName` | resourceLocator |  | ✓ | e.g. Sheet1 |  |
| Data Mode | `dataMode` | options | defineBelow | ✗ | Use when node input properties match destination column names |  |

**Data Mode options:**

* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names
* **Map Each Column Below** (`defineBelow`) - Set the value for each destination column
* **Nothing** (`nothing`) - Do not send anything

| Column to match on | `columnToMatchOn` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Used to find the correct row to update. Doesn't get changed. |  |
| Value of Column to Match On | `valueToMatchOn` | string |  | ✗ |  |  |
| Values to Send | `fieldsUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Values to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `values` |  |  |  |

</details>

| Columns | `columns` | resourceMapper |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | e.g. Add option |  |

### Append Row parameters (`append`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Sheet | `sheetName` | resourceLocator |  | ✓ | e.g. Sheet1 |  |
| Data Mode | `dataMode` | options | defineBelow | ✗ | Use when node input properties match destination column names |  |

**Data Mode options:**

* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names
* **Map Each Column Below** (`defineBelow`) - Set the value for each destination column
* **Nothing** (`nothing`) - Do not send anything

| Fields to Send | `fieldsUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `fieldValues` |  |  |  |

</details>

| Columns | `columns` | resourceMapper |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | Index of the row which contains the keys. Starts at 1. The incoming node data is matched to the keys for assignment. The matching is case sensitive. | e.g. Add option | min:1, max:∞ |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Data Location on Sheet | `locationDefine` | fixedCollection | 1 | Index of the row which contains the keys. Starts at 1. The incoming node data is matched to the keys for assignment. The matching is case sensitive. |

</details>


### Clear parameters (`clear`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Sheet | `sheetName` | resourceLocator |  | ✓ | e.g. Sheet1 |  |
| Clear | `clear` | options | wholeSheet | ✗ | What to clear |  |

**Clear options:**

* **Whole Sheet** (`wholeSheet`)
* **Specific Rows** (`specificRows`)
* **Specific Columns** (`specificColumns`)
* **Specific Range** (`specificRange`)

| Keep First Row | `keepFirstRow` | boolean | False | ✗ |  |  |
| Start Row Number | `startIndex` | number | 1 | ✗ | The row number to delete from, The first row is 1 | min:1, max:∞ |
| Number of Rows to Delete | `rowsToDelete` | number | 1 | ✗ |  | min:1, max:∞ |
| Start Column | `startIndex` | string | A | ✗ | The column to delete |  |
| Number of Columns to Delete | `columnsToDelete` | number | 1 | ✗ |  | min:1, max:∞ |
| Range | `range` | string | A:F | ✓ | The table range to read from or to append data to. See the Google <a href="https://developers.google.com/sheets/api/guides/values#writing">documentation</a> for the details. If it contains multiple sheets it can also be added like this: "MySheet!A:F" |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string | n8n-sheet | ✓ | The name of the sheet |  |
| Options | `options` | collection | {} | ✗ | Whether the sheet is hidden in the UI, false if it's visible | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Hidden | `hidden` | boolean | False | Whether the sheet is hidden in the UI, false if it's visible |
| Right To Left | `rightToLeft` | boolean | False | Whether the sheet is an RTL sheet instead of an LTR sheet |
| Sheet ID | `sheetId` | number | 0 | The ID of the sheet. Must be non-negative. This field cannot be changed once set. |
| Sheet Index | `index` | number | 0 | The index of the sheet within the spreadsheet |
| Tab Color | `tabColor` | color | 0aa55c | The color of the tab in the UI |

</details>

| Title | `title` | string |  | ✗ | The title of the spreadsheet |  |
| Sheets | `sheetsUi` | fixedCollection | {} | ✗ | Title of the property to create | e.g. Add Sheet |  |

<details>
<summary><strong>Sheets sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sheet | `sheetValues` |  |  |  |

</details>

| Options | `options` | collection | {} | ✗ | The locale of the spreadsheet in one of the following formats:
				<ul>
					<li>en (639-1)</li>
					<li>fil (639-2 if no 639-1 format exists)</li>
					<li>en_US (combination of ISO language an country)</li>
				<ul> | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Locale | `locale` | string |  | The locale of the spreadsheet in one of the following formats:
				<ul>
					<li>en (639-1)</li>
					<li>fil (639-2 if no 639-1 format exists)</li>
					<li>en_US (combination of ISO language an country)</li>
				<ul> |
| Recalculation Interval | `autoRecalc` | options |  | Default value |

</details>


### Delete parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Sheet | `sheetName` | resourceLocator |  | ✓ | e.g. Sheet1 |  |

### Delete Rows or Columns parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Sheet | `sheetName` | resourceLocator |  | ✓ | e.g. Sheet1 |  |
| To Delete | `toDelete` | options | rows | ✗ | Rows to delete |  |

**To Delete options:**

* **Rows** (`rows`) - Rows to delete
* **Columns** (`columns`) - Columns to delete

| Start Row Number | `startIndex` | number | 2 | ✗ | The row number to delete from, The first row is 2 | min:1, max:∞ |
| Number of Rows to Delete | `numberToDelete` | number | 1 | ✗ |  | min:1, max:∞ |
| Start Column | `startIndex` | string | A | ✗ | The column to delete |  |
| Number of Columns to Delete | `numberToDelete` | number | 1 | ✗ |  | min:1, max:∞ |

### Get Row(s) parameters (`read`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Sheet | `sheetName` | resourceLocator |  | ✓ | e.g. Sheet1 |  |
| Options | `options` | collection | {} | ✗ | Whether to select the first row of the sheet or the first matching row (if filters are set) | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Return only First Matching Row | `returnFirstMatch` | boolean | False | Whether to select the first row of the sheet or the first matching row (if filters are set) |
| When Filter Has Multiple Matches | `returnAllMatches` | options | returnFirstMatch | Return only the first match |

</details>


### Update Row parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Sheet | `sheetName` | resourceLocator |  | ✓ | e.g. Sheet1 |  |
| Data Mode | `dataMode` | options | defineBelow | ✗ | Use when node input properties match destination column names |  |

**Data Mode options:**

* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names
* **Map Each Column Below** (`defineBelow`) - Set the value for each destination column
* **Nothing** (`nothing`) - Do not send anything

| Column to match on | `columnToMatchOn` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Used to find the correct row to update. Doesn't get changed. |  |
| Value of Column to Match On | `valueToMatchOn` | string |  | ✗ |  |  |
| Values to Send | `fieldsUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Values to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `values` |  |  |  |

</details>

| Columns | `columns` | resourceMapper |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | e.g. Add option |  |

### Delete parameters (`deleteSpreadsheet`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Document | `documentId` | resourceLocator |  | ✓ |  |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ ["appendOrUpdate", "append"].includes($parameter["operation"]) && $parameter?.columns?.mappingMode === "defineBelow" && !$parameter?.columns?.schema?.length }}`
- `={{ $rawParameter.documentId?.startsWith("=") && $input.all().length > 1 }}`
- `={{ $rawParameter.sheetName?.startsWith("=") && $input.all().length > 1 }}`
- `={{$parameter["operation"] + ": " + $parameter["resource"]}}`
- `={{$parameter["operation"] === "append" && !$parameter["options"]["useAppend"]}}`

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
node: authentication
displayName: Authentication
description: Read, update and write data to Google Sheets
version:
- '3'
- '4'
- '4.1'
- '4.2'
- '4.3'
- '4.4'
- '4.5'
- '4.6'
- '4.7'
nodeType: regular
group:
- input
- output
credentials:
- name: googleApi
  required: true
- name: googleSheetsOAuth2Api
  required: true
operations:
- id: appendOrUpdate
  name: Append or Update Row
  description: Append a new row or update an existing one (upsert)
  params:
  - id: sheetName
    name: Sheet
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Sheet1
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - append
          - appendOrUpdate
          - clear
          - delete
          - read
          - remove
          - update
    typeInfo: &id002
      type: resourceLocator
      displayName: Sheet
      name: sheetName
  - id: dataMode
    name: Data Mode
    type: options
    default: defineBelow
    required: false
    description: Use when node input properties match destination column names
    validation: &id003
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - appendOrUpdate
        hide: {}
    typeInfo: &id004
      type: options
      displayName: Data Mode
      name: dataMode
      possibleValues:
      - value: autoMapInputData
        name: Auto-Map Input Data to Columns
        description: Use when node input properties match destination column names
      - value: defineBelow
        name: Map Each Column Below
        description: Set the value for each destination column
      - value: nothing
        name: Nothing
        description: Do not send anything
  - id: columnToMatchOn
    name: Column to match on
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    hint: Used to find the correct row to update. Doesn't get changed.
    validation: &id015
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - appendOrUpdate
        hide: {}
    typeInfo: &id016
      type: options
      displayName: Column to match on
      name: columnToMatchOn
      typeOptions:
        loadOptionsMethod: getSheetHeaderRowAndSkipEmpty
      possibleValues: []
  - id: valueToMatchOn
    name: Value of Column to Match On
    type: string
    default: ''
    required: false
    description: ''
    validation: &id017
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - appendOrUpdate
          dataMode:
          - defineBelow
        hide: {}
    typeInfo: &id018
      type: string
      displayName: Value of Column to Match On
      name: valueToMatchOn
  - id: fieldsUi
    name: Values to Send
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Field
    validation: &id005
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - appendOrUpdate
          dataMode:
          - defineBelow
        hide: {}
    typeInfo: &id006
      type: fixedCollection
      displayName: Values to Send
      name: fieldsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: values
        displayName: Field
        values:
        - displayName: Column
          name: column
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getSheetHeaderRowAndAddColumn
        - displayName: Column Name
          name: columnName
          type: string
          default: ''
          displayOptions:
            show:
              column:
              - newColumn
        - displayName: Value
          name: fieldValue
          type: string
          default: ''
  - id: columns
    name: Columns
    type: resourceMapper
    default: ''
    required: true
    description: ''
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - appendOrUpdate
        hide: {}
    typeInfo: &id008
      type: resourceMapper
      displayName: Columns
      name: columns
- id: append
  name: Append Row
  description: Create a new row in a sheet
  params:
  - id: sheetName
    name: Sheet
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Sheet1
    validation: *id001
    typeInfo: *id002
  - id: dataMode
    name: Data Mode
    type: options
    default: defineBelow
    required: false
    description: Use when node input properties match destination column names
    validation: *id003
    typeInfo: *id004
  - id: fieldsUi
    name: Fields to Send
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Field
    validation: *id005
    typeInfo: *id006
  - id: columns
    name: Columns
    type: resourceMapper
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
- id: clear
  name: Clear
  description: Delete all the contents or a part of a sheet
  params:
  - id: sheetName
    name: Sheet
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Sheet1
    validation: *id001
    typeInfo: *id002
  - id: clear
    name: Clear
    type: options
    default: wholeSheet
    required: false
    description: What to clear
    validation:
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - clear
        hide: {}
    typeInfo:
      type: options
      displayName: Clear
      name: clear
      possibleValues:
      - value: wholeSheet
        name: Whole Sheet
        description: ''
      - value: specificRows
        name: Specific Rows
        description: ''
      - value: specificColumns
        name: Specific Columns
        description: ''
      - value: specificRange
        name: Specific Range
        description: ''
  - id: keepFirstRow
    name: Keep First Row
    type: boolean
    default: false
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - clear
          clear:
          - wholeSheet
        hide: {}
    typeInfo:
      type: boolean
      displayName: Keep First Row
      name: keepFirstRow
  - id: startIndex
    name: Start Row Number
    type: number
    default: 1
    required: false
    description: The row number to delete from, The first row is 1
    validation: &id009
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - delete
          toDelete:
          - columns
        hide: {}
    typeInfo: &id010
      type: string
      displayName: Start Column
      name: startIndex
  - id: rowsToDelete
    name: Number of Rows to Delete
    type: number
    default: 1
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - clear
          clear:
          - specificRows
        hide: {}
    typeInfo:
      type: number
      displayName: Number of Rows to Delete
      name: rowsToDelete
      typeOptions:
        minValue: 1
  - id: startIndex
    name: Start Column
    type: string
    default: A
    required: false
    description: The column to delete
    validation: *id009
    typeInfo: *id010
  - id: columnsToDelete
    name: Number of Columns to Delete
    type: number
    default: 1
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - clear
          clear:
          - specificColumns
        hide: {}
    typeInfo:
      type: number
      displayName: Number of Columns to Delete
      name: columnsToDelete
      typeOptions:
        minValue: 1
  - id: range
    name: Range
    type: string
    default: A:F
    required: true
    description: 'The table range to read from or to append data to. See the Google
      <a href="https://developers.google.com/sheets/api/guides/values#writing">documentation</a>
      for the details. If it contains multiple sheets it can also be added like this:
      "MySheet!A:F"'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - clear
          clear:
          - specificRange
        hide: {}
    typeInfo:
      type: string
      displayName: Range
      name: range
- id: create
  name: Create
  description: Create a new sheet
  params:
  - id: title
    name: Title
    type: string
    default: n8n-sheet
    required: true
    description: The name of the sheet
    validation: &id011
      displayOptions:
        show:
          resource:
          - spreadsheet
          operation:
          - create
    typeInfo: &id012
      type: string
      displayName: Title
      name: title
  - id: title
    name: Title
    type: string
    default: ''
    required: false
    description: The title of the spreadsheet
    validation: *id011
    typeInfo: *id012
  - id: sheetsUi
    name: Sheets
    type: fixedCollection
    default: {}
    required: false
    description: Title of the property to create
    placeholder: Add Sheet
    validation:
      displayOptions:
        show:
          resource:
          - spreadsheet
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Sheets
      name: sheetsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: sheetValues
        displayName: Sheet
        values:
        - displayName: Title
          name: title
          type: string
          description: Title of the property to create
          default: ''
        - displayName: Hidden
          name: hidden
          type: boolean
          description: Whether the Sheet should be hidden in the UI
          default: false
- id: remove
  name: Delete
  description: Permanently delete a sheet
  params:
  - id: sheetName
    name: Sheet
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Sheet1
    validation: *id001
    typeInfo: *id002
- id: delete
  name: Delete Rows or Columns
  description: Delete columns or rows from a sheet
  params:
  - id: sheetName
    name: Sheet
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Sheet1
    validation: *id001
    typeInfo: *id002
  - id: toDelete
    name: To Delete
    type: options
    default: rows
    required: false
    description: Rows to delete
    validation:
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - delete
        hide: {}
    typeInfo:
      type: options
      displayName: To Delete
      name: toDelete
      possibleValues:
      - value: rows
        name: Rows
        description: Rows to delete
      - value: columns
        name: Columns
        description: Columns to delete
  - id: startIndex
    name: Start Row Number
    type: number
    default: 2
    required: false
    description: The row number to delete from, The first row is 2
    validation: *id009
    typeInfo: *id010
  - id: numberToDelete
    name: Number of Rows to Delete
    type: number
    default: 1
    required: false
    description: ''
    validation: &id013
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - delete
          toDelete:
          - columns
        hide: {}
    typeInfo: &id014
      type: number
      displayName: Number of Columns to Delete
      name: numberToDelete
      typeOptions:
        minValue: 1
  - id: startIndex
    name: Start Column
    type: string
    default: A
    required: false
    description: The column to delete
    validation: *id009
    typeInfo: *id010
  - id: numberToDelete
    name: Number of Columns to Delete
    type: number
    default: 1
    required: false
    description: ''
    validation: *id013
    typeInfo: *id014
- id: read
  name: Get Row(s)
  description: Retrieve one or more rows from a sheet
  params:
  - id: sheetName
    name: Sheet
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Sheet1
    validation: *id001
    typeInfo: *id002
- id: update
  name: Update Row
  description: Update an existing row in a sheet
  params:
  - id: sheetName
    name: Sheet
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Sheet1
    validation: *id001
    typeInfo: *id002
  - id: dataMode
    name: Data Mode
    type: options
    default: defineBelow
    required: false
    description: Use when node input properties match destination column names
    validation: *id003
    typeInfo: *id004
  - id: columnToMatchOn
    name: Column to match on
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    hint: Used to find the correct row to update. Doesn't get changed.
    validation: *id015
    typeInfo: *id016
  - id: valueToMatchOn
    name: Value of Column to Match On
    type: string
    default: ''
    required: false
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: fieldsUi
    name: Values to Send
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Field
    validation: *id005
    typeInfo: *id006
  - id: columns
    name: Columns
    type: resourceMapper
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
- id: deleteSpreadsheet
  name: Delete
  description: Delete a spreadsheet
  params:
  - id: documentId
    name: Document
    type: resourceLocator
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - spreadsheet
          operation:
          - deleteSpreadsheet
    typeInfo:
      type: resourceLocator
      displayName: Document
      name: documentId
common_expressions:
- ={{ ["appendOrUpdate", "append"].includes($parameter["operation"]) && $parameter?.columns?.mappingMode
  === "defineBelow" && !$parameter?.columns?.schema?.length }}
- ={{ $rawParameter.documentId?.startsWith("=") && $input.all().length > 1 }}
- ={{ $rawParameter.sheetName?.startsWith("=") && $input.all().length > 1 }}
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
- ={{$parameter["operation"] === "append" && !$parameter["options"]["useAppend"]}}
ui_elements:
  notices:
  - name: autoMapNotice
    text: In this mode, make sure the incoming data is named the same as the columns
      in your Sheet. (Use an 'Edit Fields' node before this node to change it if required.)
    conditions:
      show:
        operation:
        - append
        dataMode:
        - autoMapInputData
      hide: {}
  tooltips: []
  placeholders:
  - field: sheetName
    text: Sheet1
  - field: fieldsUi
    text: Add Field
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: fieldsUi
    text: Add Field
  - field: options
    text: Add option
  - field: fieldsUi
    text: Add Field
  - field: options
    text: Add option
  - field: sheetsUi
    text: Add Sheet
  - field: options
    text: Add option
  hints:
  - field: columnToMatchOn
    text: Used to find the correct row to update. Doesn't get changed.
  - field: columnToMatchOn
    text: Used to find the correct row to update. Doesn't get changed.
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
  "$id": "https://n8n.io/schemas/nodes/authentication.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Authentication Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "appendOrUpdate",
        "append",
        "clear",
        "create",
        "remove",
        "delete",
        "read",
        "update",
        "deleteSpreadsheet"
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
          "enum": [
            "spreadsheet",
            "sheet"
          ],
          "default": "sheet"
        },
        "operation": {
          "description": "Create a spreadsheet",
          "type": "string",
          "enum": [
            "create",
            "deleteSpreadsheet"
          ],
          "default": "create"
        },
        "documentId": {
          "description": "",
          "type": "string"
        },
        "sheetName": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Sheet1"
          ]
        },
        "dataMode": {
          "description": "Use when node input properties match destination column names",
          "type": "string",
          "enum": [
            "autoMapInputData",
            "defineBelow",
            "nothing"
          ],
          "default": "defineBelow"
        },
        "fieldsUi": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "columns": {
          "description": "",
          "type": "string"
        },
        "options": {
          "description": "The locale of the spreadsheet in one of the following formats:\n\t\t\t\t<ul>\n\t\t\t\t\t<li>en (639-1)</li>\n\t\t\t\t\t<li>fil (639-2 if no 639-1 format exists)</li>\n\t\t\t\t\t<li>en_US (combination of ISO language an country)</li>\n\t\t\t\t<ul>",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "handlingExtraData": {
          "description": "Create a new column for extra data",
          "type": "string",
          "enum": [
            "insertInNewColumn",
            "ignoreIt",
            "error"
          ],
          "default": "insertInNewColumn"
        },
        "clear": {
          "description": "What to clear",
          "type": "string",
          "enum": [
            "wholeSheet",
            "specificRows",
            "specificColumns",
            "specificRange"
          ],
          "default": "wholeSheet"
        },
        "keepFirstRow": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "startIndex": {
          "description": "The column to delete",
          "type": "string",
          "default": "A"
        },
        "rowsToDelete": {
          "description": "",
          "type": "number",
          "default": 1
        },
        "columnsToDelete": {
          "description": "",
          "type": "number",
          "default": 1
        },
        "range": {
          "description": "The table range to read from or to append data to. See the Google <a href=\"https://developers.google.com/sheets/api/guides/values#writing\">documentation</a> for the details. If it contains multiple sheets it can also be added like this: \"MySheet!A:F\"",
          "type": "string",
          "default": "A:F"
        },
        "title": {
          "description": "The title of the spreadsheet",
          "type": "string",
          "default": ""
        },
        "toDelete": {
          "description": "Rows to delete",
          "type": "string",
          "enum": [
            "rows",
            "columns"
          ],
          "default": "rows"
        },
        "numberToDelete": {
          "description": "",
          "type": "number",
          "default": 1
        },
        "columnToMatchOn": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "valueToMatchOn": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "sheetsUi": {
          "description": "Title of the property to create",
          "type": "string",
          "default": {},
          "examples": [
            "Add Sheet"
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
      "3",
      "4",
      "4.1",
      "4.2",
      "4.3",
      "4.4",
      "4.5",
      "4.6",
      "4.7"
    ]
  },
  "credentials": [
    {
      "name": "googleApi",
      "required": true
    },
    {
      "name": "googleSheetsOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['3', '4', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
