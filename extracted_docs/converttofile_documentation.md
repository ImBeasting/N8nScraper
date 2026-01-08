---
title: "Node: Convert to File"
slug: "node-converttofile"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Convert JSON data to binary data"
node_type: "regular"
group: "['input']"
---

# Node: Convert to File

**Purpose.** Convert JSON data to binary data


---

## Node Details

- **Icon:** `{'light': 'file:convertToFile.svg', 'dark': 'file:convertToFile.dark.svg'}`
- **Group:** `['input']`
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
| Convert to CSV | `csv` | Transform input data into a CSV file |
| Convert to HTML | `html` | Transform input data into a table in an HTML file |
| Convert to ICS | `iCal` | Converts each input item to an ICS event file |
| Convert to JSON | `toJson` | Transform input data into a single or multiple JSON files |
| Convert to ODS | `ods` | Transform input data into an ODS file |
| Convert to RTF | `rtf` | Transform input data into a table in an RTF file |
| Convert to Text File | `toText` | Transform input data string into a file |
| Convert to XLS | `xls` | Transform input data into an Excel file |
| Convert to XLSX | `xlsx` | Transform input data into an Excel file |
| Move Base64 String to File | `toBinary` | Convert a base64-encoded string into its original file format |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | csv | ✗ | Transform input data into a CSV file |  |

**Operation options:**

* **Convert to CSV** (`csv`) - Transform input data into a CSV file
* **Convert to HTML** (`html`) - Transform input data into a table in an HTML file
* **Convert to ICS** (`iCal`) - Converts each input item to an ICS event file
* **Convert to JSON** (`toJson`) - Transform input data into a single or multiple JSON files
* **Convert to ODS** (`ods`) - Transform input data into an ODS file
* **Convert to RTF** (`rtf`) - Transform input data into a table in an RTF file
* **Convert to Text File** (`toText`) - Transform input data string into a file
* **Convert to XLS** (`xls`) - Transform input data into an Excel file
* **Convert to XLSX** (`xlsx`) - Transform input data into an Excel file
* **Move Base64 String to File** (`toBinary`) - Convert a base64-encoded string into its original file format

---

### Convert to JSON parameters (`toJson`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Mode | `mode` | options | once | ✗ |  |  |

**Mode options:**

* **All Items to One File** (`once`)
* **Each Item to Separate File** (`each`)


### Move Base64 String to File parameters (`toBinary`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Base64 Input Field | `sourceProperty` | string |  | ✓ | The name of the input field that contains the base64 string to convert to a file. Use dot-notation for deep fields (e.g. 'level1.level2.currentKey'). | e.g. e.g data |  |
| Options | `options` | collection | {} | ✗ | Whether to add special marker at the start of your text file. This marker helps some programs understand how to read the file correctly. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Add Byte Order Mark (BOM) | `addBOM` | boolean | False | Whether to add special marker at the start of your text file. This marker helps some programs understand how to read the file correctly. |
| Data Is Base64 | `dataIsBase64` | boolean | True | Whether the data is already base64 encoded |
| Encoding | `encoding` | options | utf8 | Choose the character set to use to encode the data |
| File Name | `fileName` | string |  | Name of the output file |
| MIME Type | `mimeType` | string |  | The MIME type of the output file. <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types" target="_blank">Common MIME types</a>. |

</details>


---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Convert to File2

**From workflow:** Test ConvertToFile

**Parameters:**
```json
{
  "operation": "toBinary",
  "sourceProperty": "base64",
  "options": {}
}
```

### Example 2: Convert to Text File

**From workflow:** Test ConvertToFile

**Parameters:**
```json
{
  "operation": "toText",
  "sourceProperty": "notes",
  "options": {}
}
```

### Example 3: Convert to JSON (with Formatting)

**From workflow:** Test ConvertToFile

**Parameters:**
```json
{
  "operation": "toJson",
  "options": {
    "format": true
  }
}
```

### Example 4: Convert to JSON

**From workflow:** Test ConvertToFile

**Parameters:**
```json
{
  "operation": "toJson",
  "options": {}
}
```

### Example 5: Convert to CSV

**From workflow:** Test ConvertToFile

**Parameters:**
```json
{
  "options": {}
}
```


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
* Aliases: CSV, Spreadsheet, Excel, xls, xlsx, ods, tabular, encode, encoding, Move Binary Data, Binary, File, JSON, HTML, ICS, iCal, RTF, 64, Base64

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: convertToFile
displayName: Convert to File
description: Convert JSON data to binary data
version:
- '1'
- '1.1'
nodeType: regular
group:
- input
operations:
- id: csv
  name: Convert to CSV
  description: Transform input data into a CSV file
- id: html
  name: Convert to HTML
  description: Transform input data into a table in an HTML file
- id: iCal
  name: Convert to ICS
  description: Converts each input item to an ICS event file
- id: toJson
  name: Convert to JSON
  description: Transform input data into a single or multiple JSON files
  params:
  - id: mode
    name: Mode
    type: options
    default: once
    required: false
    description: ''
    typeInfo:
      type: options
      displayName: Mode
      name: mode
      possibleValues:
      - value: once
        name: All Items to One File
        description: ''
      - value: each
        name: Each Item to Separate File
        description: ''
- id: ods
  name: Convert to ODS
  description: Transform input data into an ODS file
- id: rtf
  name: Convert to RTF
  description: Transform input data into a table in an RTF file
- id: toText
  name: Convert to Text File
  description: Transform input data string into a file
- id: xls
  name: Convert to XLS
  description: Transform input data into an Excel file
- id: xlsx
  name: Convert to XLSX
  description: Transform input data into an Excel file
- id: toBinary
  name: Move Base64 String to File
  description: Convert a base64-encoded string into its original file format
  params:
  - id: sourceProperty
    name: Base64 Input Field
    type: string
    default: ''
    required: true
    description: The name of the input field that contains the base64 string to convert
      to a file. Use dot-notation for deep fields (e.g. 'level1.level2.currentKey').
    placeholder: e.g data
    validation:
      required: true
    typeInfo:
      type: string
      displayName: Base64 Input Field
      name: sourceProperty
examples:
- name: Convert to File2
  parameters:
    operation: toBinary
    sourceProperty: base64
    options: {}
  workflow: Test ConvertToFile
- name: Convert to Text File
  parameters:
    operation: toText
    sourceProperty: notes
    options: {}
  workflow: Test ConvertToFile
- name: Convert to JSON (with Formatting)
  parameters:
    operation: toJson
    options:
      format: true
  workflow: Test ConvertToFile
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: binaryPropertyName
    text: e.g data
  - field: options
    text: Add option
  - field: sourceProperty
    text: e.g data
  - field: options
    text: Add option
  hints:
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
  "$id": "https://n8n.io/schemas/nodes/convertToFile.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Convert to File Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "csv",
        "html",
        "iCal",
        "toJson",
        "ods",
        "rtf",
        "toText",
        "xls",
        "xlsx",
        "toBinary"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Transform input data into a CSV file",
          "type": "string",
          "enum": [
            "csv",
            "html",
            "iCal",
            "toJson",
            "ods",
            "rtf",
            "toText",
            "xls",
            "xlsx",
            "toBinary"
          ],
          "default": "csv"
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data",
          "examples": [
            "e.g data"
          ]
        },
        "options": {
          "description": "Whether to add special marker at the start of your text file. This marker helps some programs understand how to read the file correctly.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "sourceProperty": {
          "description": "The name of the input field that contains the base64 string to convert to a file. Use dot-notation for deep fields (e.g. 'level1.level2.currentKey').",
          "type": "string",
          "default": "",
          "examples": [
            "e.g data"
          ]
        },
        "mode": {
          "description": "",
          "type": "string",
          "enum": [
            "once",
            "each"
          ],
          "default": "once"
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
      "1.1"
    ]
  },
  "examples": [
    {
      "description": "Convert to File2",
      "value": {
        "operation": "toBinary",
        "sourceProperty": "base64",
        "options": {}
      }
    },
    {
      "description": "Convert to Text File",
      "value": {
        "operation": "toText",
        "sourceProperty": "notes",
        "options": {}
      }
    },
    {
      "description": "Convert to JSON (with Formatting)",
      "value": {
        "operation": "toJson",
        "options": {
          "format": true
        }
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
