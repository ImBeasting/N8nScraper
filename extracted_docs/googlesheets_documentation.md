---
title: "Node: Google Sheets"
slug: "node-googlesheets"
version: "['1', '2']"
updated: "2025-11-13"
summary: "Read, update and write data to Google Sheets"
node_type: "regular"
group: "['input', 'output']"
---

# Node: Google Sheets

**Purpose.** Read, update and write data to Google Sheets
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:googleSheets.svg`
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

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleApi` | ✓ | {'show': {'authentication': ['serviceAccount']}} |
| `googleSheetsOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Sheet Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Append | `append` | Append data to a sheet |
| Clear | `clear` | Clear data from a sheet |
| Create | `create` | Create a new sheet |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete columns and rows from a sheet |
| Lookup | `lookup` | Look up a specific column value and return the matching row |
| Read | `read` | Read data from a sheet |
| Remove | `remove` | Remove a sheet |
| Update | `update` | Update rows in a sheet |

### Spreadsheet Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a spreadsheet |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | sheet | ✗ | Resource to operate on |  |

**Resource options:**

* **Spreadsheet** (`spreadsheet`)
* **Sheet** (`sheet`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | read | ✗ | Append data to a sheet |  |

**Operation options:**

* **Append** (`append`) - Append data to a sheet
* **Clear** (`clear`) - Clear data from a sheet
* **Create** (`create`) - Create a new sheet
* **Create or Update** (`upsert`) - Create a new record, or update the current one if it already exists (upsert)
* **Delete** (`delete`) - Delete columns and rows from a sheet
* **Lookup** (`lookup`) - Look up a specific column value and return the matching row
* **Read** (`read`) - Read data from a sheet
* **Remove** (`remove`) - Remove a sheet
* **Update** (`update`) - Update rows in a sheet

---

### Append parameters (`append`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Options | `options` | collection | {} | ✗ | By default, the workflow stops executing if the lookup/read does not return values | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Continue If Empty | `continue` | boolean | False | By default, the workflow stops executing if the lookup/read does not return values |
| Return All Matches | `returnAllMatches` | boolean | False | By default only the first result gets returned. If options gets set all found matches get returned. |
| Use Header Names as JSON Paths | `usePathForKeyRow` | boolean | False | Whether you want to match the headers as path, for example, the row header "category.name" will match the "category" object and get the field "name" from it. By default "category.name" will match with the field with exact name, not nested object. |
| Value Input Mode | `valueInputMode` | options | RAW | The values will not be parsed and will be stored as-is |
| Value Render Mode | `valueRenderMode` | options | UNFORMATTED_VALUE | Values will be calculated & formatted in the reply according to the cell's formatting.Formatting is based on the spreadsheet's locale, not the requesting user's locale.For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return "$1.23" |
| Value Render Mode | `valueRenderMode` | options | UNFORMATTED_VALUE | Values will be calculated & formatted in the reply according to the cell's formatting.Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return "$1.23". |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✗ | The title of the spreadsheet |  |
| Sheets | `sheetsUi` | fixedCollection | {} | ✗ | Whether the Sheet should be hidden in the UI | e.g. Add Sheet |  |

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

| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | The number of columns in the grid | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Grid Properties | `gridProperties` | collection | {} | The number of columns in the grid |
| Hidden | `hidden` | boolean | False | Whether the sheet is hidden in the UI, false if it's visible |
| Right To Left | `rightToLeft` | boolean | False | Whether the sheet is an RTL sheet instead of an LTR sheet |
| Sheet ID | `sheetId` | number | 0 | The ID of the sheet. Must be non-negative. This field cannot be changed once set. |
| Sheet Index | `index` | number | 0 | The index of the sheet within the spreadsheet |
| Tab Color | `tabColor` | color | 0aa55c | The color of the tab in the UI |
| Title | `title` | string |  | The Sheet name |

</details>


### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| RAW Data | `rawData` | boolean | False | ✗ | Whether the data supplied is RAW instead of parsed into keys |  |
| Data Property | `dataProperty` | string | data | ✗ | The name of the property from which to read the RAW data |  |
| Key | `key` | string | id | ✗ | The name of the key to identify which data should be updated in the sheet |  |
| Options | `options` | collection | {} | ✗ | By default, the workflow stops executing if the lookup/read does not return values | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Continue If Empty | `continue` | boolean | False | By default, the workflow stops executing if the lookup/read does not return values |
| Return All Matches | `returnAllMatches` | boolean | False | By default only the first result gets returned. If options gets set all found matches get returned. |
| Use Header Names as JSON Paths | `usePathForKeyRow` | boolean | False | Whether you want to match the headers as path, for example, the row header "category.name" will match the "category" object and get the field "name" from it. By default "category.name" will match with the field with exact name, not nested object. |
| Value Input Mode | `valueInputMode` | options | RAW | The values will not be parsed and will be stored as-is |
| Value Render Mode | `valueRenderMode` | options | UNFORMATTED_VALUE | Values will be calculated & formatted in the reply according to the cell's formatting.Formatting is based on the spreadsheet's locale, not the requesting user's locale.For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return "$1.23" |
| Value Render Mode | `valueRenderMode` | options | UNFORMATTED_VALUE | Values will be calculated & formatted in the reply according to the cell's formatting.Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return "$1.23". |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| To Delete | `toDelete` | fixedCollection | {} | ✓ | Deletes columns and rows from a sheet | e.g. Add Columns/Rows to delete |  |

<details>
<summary><strong>To Delete sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Columns | `columns` |  |  |  |
| Rows | `rows` |  |  |  |

</details>


### Lookup parameters (`lookup`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Lookup Column | `lookupColumn` | string |  | ✓ | The name of the column in which to look for value | e.g. Email |  |
| Lookup Value | `lookupValue` | string |  | ✗ | The value to look for in column | e.g. frank@example.com |  |
| Options | `options` | collection | {} | ✗ | By default, the workflow stops executing if the lookup/read does not return values | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Continue If Empty | `continue` | boolean | False | By default, the workflow stops executing if the lookup/read does not return values |
| Return All Matches | `returnAllMatches` | boolean | False | By default only the first result gets returned. If options gets set all found matches get returned. |
| Use Header Names as JSON Paths | `usePathForKeyRow` | boolean | False | Whether you want to match the headers as path, for example, the row header "category.name" will match the "category" object and get the field "name" from it. By default "category.name" will match with the field with exact name, not nested object. |
| Value Input Mode | `valueInputMode` | options | RAW | The values will not be parsed and will be stored as-is |
| Value Render Mode | `valueRenderMode` | options | UNFORMATTED_VALUE | Values will be calculated & formatted in the reply according to the cell's formatting.Formatting is based on the spreadsheet's locale, not the requesting user's locale.For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return "$1.23" |
| Value Render Mode | `valueRenderMode` | options | UNFORMATTED_VALUE | Values will be calculated & formatted in the reply according to the cell's formatting.Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return "$1.23". |

</details>


### Read parameters (`read`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| RAW Data | `rawData` | boolean | False | ✗ | Whether the data should be returned RAW instead of parsed into keys according to their header |  |
| Data Property | `dataProperty` | string | data | ✗ | The name of the property into which to write the RAW data |  |
| Options | `options` | collection | {} | ✗ | By default, the workflow stops executing if the lookup/read does not return values | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Continue If Empty | `continue` | boolean | False | By default, the workflow stops executing if the lookup/read does not return values |
| Return All Matches | `returnAllMatches` | boolean | False | By default only the first result gets returned. If options gets set all found matches get returned. |
| Use Header Names as JSON Paths | `usePathForKeyRow` | boolean | False | Whether you want to match the headers as path, for example, the row header "category.name" will match the "category" object and get the field "name" from it. By default "category.name" will match with the field with exact name, not nested object. |
| Value Input Mode | `valueInputMode` | options | RAW | The values will not be parsed and will be stored as-is |
| Value Render Mode | `valueRenderMode` | options | UNFORMATTED_VALUE | Values will be calculated & formatted in the reply according to the cell's formatting.Formatting is based on the spreadsheet's locale, not the requesting user's locale.For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return "$1.23" |
| Value Render Mode | `valueRenderMode` | options | UNFORMATTED_VALUE | Values will be calculated & formatted in the reply according to the cell's formatting.Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return "$1.23". |

</details>


### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Sheet ID | `id` | string |  | ✓ | The ID of the sheet to delete |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| RAW Data | `rawData` | boolean | False | ✗ | Whether the data supplied is RAW instead of parsed into keys |  |
| Data Property | `dataProperty` | string | data | ✗ | The name of the property from which to read the RAW data |  |
| Key | `key` | string | id | ✗ | The name of the key to identify which data should be updated in the sheet |  |
| Options | `options` | collection | {} | ✗ | By default, the workflow stops executing if the lookup/read does not return values | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Continue If Empty | `continue` | boolean | False | By default, the workflow stops executing if the lookup/read does not return values |
| Return All Matches | `returnAllMatches` | boolean | False | By default only the first result gets returned. If options gets set all found matches get returned. |
| Use Header Names as JSON Paths | `usePathForKeyRow` | boolean | False | Whether you want to match the headers as path, for example, the row header "category.name" will match the "category" object and get the field "name" from it. By default "category.name" will match with the field with exact name, not nested object. |
| Value Input Mode | `valueInputMode` | options | RAW | The values will not be parsed and will be stored as-is |
| Value Render Mode | `valueRenderMode` | options | UNFORMATTED_VALUE | Values will be calculated & formatted in the reply according to the cell's formatting.Formatting is based on the spreadsheet's locale, not the requesting user's locale.For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return "$1.23" |
| Value Render Mode | `valueRenderMode` | options | UNFORMATTED_VALUE | Values will be calculated & formatted in the reply according to the cell's formatting.Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return "$1.23". |

</details>


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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleSheets
displayName: Google Sheets
description: Read, update and write data to Google Sheets
version:
- '1'
- '2'
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
- id: append
  name: Append
  description: Append data to a sheet
  params: []
- id: clear
  name: Clear
  description: Clear data from a sheet
- id: create
  name: Create
  description: Create a new sheet
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: false
    description: The title of the spreadsheet
    validation:
      displayOptions:
        show:
          resource:
          - spreadsheet
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: sheetsUi
    name: Sheets
    type: fixedCollection
    default: {}
    required: false
    description: Whether the Sheet should be hidden in the UI
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
        - displayName: Sheet Properties
          name: propertiesUi
          type: collection
          description: Whether the Sheet should be hidden in the UI
          placeholder: Add Property
          default: {}
          options:
          - displayName: Hidden
            name: hidden
            type: boolean
            description: Whether the Sheet should be hidden in the UI
            default: false
          - displayName: Title
            name: title
            type: string
            description: Title of the property to create
            default: ''
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation:
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - create
    typeInfo:
      type: boolean
      displayName: Simplify
      name: simple
- id: upsert
  name: Create or Update
  description: Create a new record, or update the current one if it already exists
    (upsert)
  params:
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether the data supplied is RAW instead of parsed into keys
    validation: &id001
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - update
          - upsert
    typeInfo: &id002
      type: boolean
      displayName: RAW Data
      name: rawData
  - id: dataProperty
    name: Data Property
    type: string
    default: data
    required: false
    description: The name of the property from which to read the RAW data
    validation: &id003
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - update
          - upsert
          rawData:
          - true
    typeInfo: &id004
      type: string
      displayName: Data Property
      name: dataProperty
  - id: key
    name: Key
    type: string
    default: id
    required: false
    description: The name of the key to identify which data should be updated in the
      sheet
    validation: &id005
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - update
          - upsert
          rawData:
          - false
    typeInfo: &id006
      type: string
      displayName: Key
      name: key
- id: delete
  name: Delete
  description: Delete columns and rows from a sheet
  params:
  - id: toDelete
    name: To Delete
    type: fixedCollection
    default: {}
    required: true
    description: Deletes columns and rows from a sheet
    placeholder: Add Columns/Rows to delete
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - delete
    typeInfo:
      type: fixedCollection
      displayName: To Delete
      name: toDelete
      typeOptions:
        multipleValues: true
      subProperties:
      - name: columns
        displayName: Columns
        values:
        - displayName: Sheet Name or ID
          name: sheetId
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          required: true
          options: []
          typeOptions:
            loadOptionsMethod: getSheets
        - displayName: Start Index
          name: startIndex
          type: number
          description: The start index (0 based and inclusive) of column to delete
          default: 0
          typeOptions:
            minValue: 0
        - displayName: Amount
          name: amount
          type: number
          description: Number of columns to delete
          default: 1
          typeOptions:
            minValue: 1
      - name: rows
        displayName: Rows
        values:
        - displayName: Sheet Name or ID
          name: sheetId
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          required: true
          options: []
          typeOptions:
            loadOptionsMethod: getSheets
        - displayName: Start Index
          name: startIndex
          type: number
          description: The start index (0 based and inclusive) of row to delete
          default: 0
          typeOptions:
            minValue: 0
        - displayName: Amount
          name: amount
          type: number
          description: Number of rows to delete
          default: 1
          typeOptions:
            minValue: 1
- id: lookup
  name: Lookup
  description: Look up a specific column value and return the matching row
  params:
  - id: lookupColumn
    name: Lookup Column
    type: string
    default: ''
    required: true
    description: The name of the column in which to look for value
    placeholder: Email
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - lookup
    typeInfo:
      type: string
      displayName: Lookup Column
      name: lookupColumn
  - id: lookupValue
    name: Lookup Value
    type: string
    default: ''
    required: false
    description: The value to look for in column
    placeholder: frank@example.com
    validation:
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - lookup
    typeInfo:
      type: string
      displayName: Lookup Value
      name: lookupValue
- id: read
  name: Read
  description: Read data from a sheet
  params:
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether the data should be returned RAW instead of parsed into keys
      according to their header
    validation: *id001
    typeInfo: *id002
  - id: dataProperty
    name: Data Property
    type: string
    default: data
    required: false
    description: The name of the property into which to write the RAW data
    validation: *id003
    typeInfo: *id004
- id: remove
  name: Remove
  description: Remove a sheet
  params:
  - id: id
    name: Sheet ID
    type: string
    default: ''
    required: true
    description: The ID of the sheet to delete
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - sheet
          operation:
          - remove
    typeInfo:
      type: string
      displayName: Sheet ID
      name: id
- id: update
  name: Update
  description: Update rows in a sheet
  params:
  - id: rawData
    name: RAW Data
    type: boolean
    default: false
    required: false
    description: Whether the data supplied is RAW instead of parsed into keys
    validation: *id001
    typeInfo: *id002
  - id: dataProperty
    name: Data Property
    type: string
    default: data
    required: false
    description: The name of the property from which to read the RAW data
    validation: *id003
    typeInfo: *id004
  - id: key
    name: Key
    type: string
    default: id
    required: false
    description: The name of the key to identify which data should be updated in the
      sheet
    validation: *id005
    typeInfo: *id006
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: toDelete
    text: Add Columns/Rows to delete
  - field: lookupColumn
    text: Email
  - field: lookupValue
    text: frank@example.com
  - field: options
    text: Add option
  - field: sheetsUi
    text: Add Sheet
  - field: options
    text: Add option
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/googleSheets.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Sheets Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "append",
        "clear",
        "create",
        "upsert",
        "delete",
        "lookup",
        "read",
        "remove",
        "update"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "serviceAccount",
            "oAuth2"
          ],
          "default": "serviceAccount"
        },
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
            "create"
          ],
          "default": "create"
        },
        "sheetId": {
          "description": "The ID of the Google Spreadsheet. Found as part of the sheet URL https://docs.google.com/spreadsheets/d/{ID}/.",
          "type": "string",
          "default": ""
        },
        "range": {
          "description": "The table range to read from or to append data to. See the Google <a href=\"https://developers.google.com/sheets/api/guides/values#writing\">documentation</a> for the details. If it contains multiple sheets it can also be added like this: \"MySheet!A:F\"",
          "type": "string",
          "default": "A:F"
        },
        "toDelete": {
          "description": "Deletes columns and rows from a sheet",
          "type": "string",
          "default": {},
          "examples": [
            "Add Columns/Rows to delete"
          ]
        },
        "rawData": {
          "description": "Whether the data supplied is RAW instead of parsed into keys",
          "type": "boolean",
          "default": false
        },
        "dataProperty": {
          "description": "The name of the property from which to read the RAW data",
          "type": "string",
          "default": "data"
        },
        "dataStartRow": {
          "description": "Index of the first row which contains the actual data and not the keys. Starts with 0.",
          "type": "number",
          "default": 1
        },
        "keyRow": {
          "description": "Index of the row which contains the keys. Starts at 0. The incoming node data is matched to the keys for assignment. The matching is case sensitive.",
          "type": "number",
          "default": 0
        },
        "lookupColumn": {
          "description": "The name of the column in which to look for value",
          "type": "string",
          "default": "",
          "examples": [
            "Email"
          ]
        },
        "lookupValue": {
          "description": "The value to look for in column",
          "type": "string",
          "default": "",
          "examples": [
            "frank@example.com"
          ]
        },
        "key": {
          "description": "The name of the key to identify which data should be updated in the sheet",
          "type": "string",
          "default": "id"
        },
        "options": {
          "description": "The number of columns in the grid",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "title": {
          "description": "The title of the spreadsheet",
          "type": "string",
          "default": ""
        },
        "sheetsUi": {
          "description": "Whether the Sheet should be hidden in the UI",
          "type": "string",
          "default": {},
          "examples": [
            "Add Sheet"
          ]
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "id": {
          "description": "The ID of the sheet to delete",
          "type": "string",
          "default": ""
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
      "2"
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
| ['1', '2'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
