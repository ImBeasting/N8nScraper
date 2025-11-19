---
title: "Node: Spreadsheet File"
slug: "node-spreadsheetfile"
version: "2"
updated: "2025-11-13"
summary: "Reads and writes data from a spreadsheet file like CSV, XLS, ODS, etc"
node_type: "regular"
group: "['transform']"
---

# Node: Spreadsheet File

**Purpose.** Reads and writes data from a spreadsheet file like CSV, XLS, ODS, etc


---

## Node Details

- **Icon:** `fa:table`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Read From File | `fromFile` | Reads data from a spreadsheet file |
| Write to File | `toFile` | Writes the workflow data to a spreadsheet file |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | fromFile | ✗ | Reads data from a spreadsheet file |  |

**Operation options:**

* **Read From File** (`fromFile`) - Reads data from a spreadsheet file
* **Write to File** (`toFile`) - Writes the workflow data to a spreadsheet file

---

### Read From File parameters (`fromFile`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Format | `fileFormat` | options | autodetect | ✗ | Comma-separated values |  |

**File Format options:**

* **Autodetect** (`autodetect`)
* **CSV** (`csv`) - Comma-separated values
* **HTML** (`html`) - HTML Table
* **ODS** (`ods`) - OpenDocument Spreadsheet
* **RTF** (`rtf`) - Rich Text Format
* **XLS** (`xls`) - Excel
* **XLSX** (`xlsx`) - Excel

| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input field containing the file data to be processed |  |
| Options | `options` | collection | {} | ✗ | Set the field delimiter, usually a comma | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Delimiter | `delimiter` | string | , | Set the field delimiter, usually a comma |
| Encoding | `encoding` | options | utf-8 |  |
| Exclude Byte Order Mark (BOM) | `enableBOM` | boolean | False | Whether to detect and exclude the byte-order-mark from the CSV Input if present |
| Preserve Quotes | `relaxQuotes` | boolean | False | Whether to handle unclosed quotes in CSV fields as part of the field's content instead of throwing a parsing error |
| Header Row | `headerRow` | boolean | True | Whether the first row of the file contains the header names |
| Include Empty Cells | `includeEmptyCells` | boolean | False | Whether to include empty cells when reading from file. They will be filled with an empty string. |
| Max Number of Rows to Load | `maxRowCount` | number |  | Stop handling records after the requested number of rows are read. Use -1 if you want to load all rows. |
| Range | `range` | string |  | The range to read from the table. If set to a number it will be the starting row. If set to string it will be used as A1-style notation range. |
| RAW Data | `rawData` | boolean | False | Whether to return RAW data, instead of parsing it |
| Read As String | `readAsString` | boolean | False | In some cases and file formats, it is necessary to read as string to ensure special characters are interpreted correctly |
| Sheet Name | `sheetName` | string | Sheet | Name of the sheet to read from in the spreadsheet (if supported). If not set, the first one will be chosen. |
| Starting Line | `fromLine` | number | 0 | Start handling records from the requested line number. Starts at 0. |

</details>


### Write to File parameters (`toFile`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Format | `fileFormat` | options | xls | ✗ | Comma-separated values |  |

**File Format options:**

* **CSV** (`csv`) - Comma-separated values
* **HTML** (`html`) - HTML Table
* **ODS** (`ods`) - OpenDocument Spreadsheet
* **RTF** (`rtf`) - Rich Text Format
* **XLS** (`xls`) - Excel
* **XLSX** (`xlsx`) - Excel

| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| Options | `options` | collection | {} | ✗ | Whether compression will be applied or not | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Compression | `compression` | boolean | False | Whether compression will be applied or not |
| File Name | `fileName` | string |  | File name to set in binary data. By default will "spreadsheet.&lt;fileFormat&gt;" be used. |
| Header Row | `headerRow` | boolean | True | Whether the first row of the file contains the header names |
| Sheet Name | `sheetName` | string | Sheet | Name of the sheet to create in the spreadsheet |

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
* Categories: Data & Storage, Core Nodes
* Aliases: _Excel, Excel, CSV, Sheet, Spreadsheet, xls, xlsx, ods

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: spreadsheetFile
displayName: Spreadsheet File
description: Reads and writes data from a spreadsheet file like CSV, XLS, ODS, etc
version: '2'
nodeType: regular
group:
- transform
operations:
- id: fromFile
  name: Read From File
  description: Reads data from a spreadsheet file
  params:
  - id: fileFormat
    name: File Format
    type: options
    default: autodetect
    required: false
    description: Comma-separated values
    validation: &id001
      displayOptions:
        show:
          operation:
          - toFile
    typeInfo: &id002
      type: options
      displayName: File Format
      name: fileFormat
      possibleValues:
      - value: csv
        name: CSV
        description: Comma-separated values
      - value: html
        name: HTML
        description: HTML Table
      - value: ods
        name: ODS
        description: OpenDocument Spreadsheet
      - value: rtf
        name: RTF
        description: Rich Text Format
      - value: xls
        name: XLS
        description: Excel
      - value: xlsx
        name: XLSX
        description: Excel
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input field containing the file data to be processed
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - toFile
    typeInfo: &id004
      type: string
      displayName: Put Output File in Field
      name: binaryPropertyName
- id: toFile
  name: Write to File
  description: Writes the workflow data to a spreadsheet file
  params:
  - id: fileFormat
    name: File Format
    type: options
    default: xls
    required: false
    description: Comma-separated values
    validation: *id001
    typeInfo: *id002
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: *id003
    typeInfo: *id004
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  - field: options
    text: Add option
  hints:
  - field: binaryPropertyName
    text: The name of the input field containing the file data to be processed
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/spreadsheetFile.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Spreadsheet File Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "fromFile",
        "toFile"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Reads data from a spreadsheet file",
          "type": "string",
          "enum": [
            "fromFile",
            "toFile"
          ],
          "default": "fromFile"
        },
        "fileFormat": {
          "description": "Comma-separated values",
          "type": "string",
          "enum": [
            "csv",
            "html",
            "ods",
            "rtf",
            "xls",
            "xlsx"
          ],
          "default": "xls"
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "Whether compression will be applied or not",
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
    "version": "2"
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 2 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
