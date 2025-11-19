---
title: "Node: Extract from File"
slug: "node-extractfromfile"
version: "1"
updated: "2025-11-13"
summary: "Convert binary data to JSON"
node_type: "regular"
group: "['input']"
---

# Node: Extract from File

**Purpose.** Convert binary data to JSON


---

## Node Details

- **Icon:** `{'light': 'file:extractFromFile.svg', 'dark': 'file:extractFromFile.dark.svg'}`
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
| Extract From CSV | `csv` | Transform a CSV file into output items |
| Extract From HTML | `html` | Transform a table in an HTML file into output items |
| Extract From ICS | `fromIcs` | Transform a ICS file into output items |
| Extract From JSON | `fromJson` | Transform a JSON file into output items |
| Extract From ODS | `ods` | Transform an ODS file into output items |
| Extract From PDF | `pdf` | Extracts the content and metadata from a PDF file |
| Extract From RTF | `rtf` | Transform a table in an RTF file into output items |
| Extract From Text File | `text` | Extracts the content of a text file |
| Extract From XML | `xml` | Extracts the content of an XML file |
| Extract From XLS | `xls` | Transform an Excel file into output items |
| Extract From XLSX | `xlsx` | Transform an Excel file into output items |
| Move File to Base64 String | `binaryToPropery` | Convert a file into a base64-encoded string |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | csv | ✗ | Transform a CSV file into output items |  |

**Operation options:**

* **Extract From CSV** (`csv`) - Transform a CSV file into output items
* **Extract From HTML** (`html`) - Transform a table in an HTML file into output items
* **Extract From ICS** (`fromIcs`) - Transform a ICS file into output items
* **Extract From JSON** (`fromJson`) - Transform a JSON file into output items
* **Extract From ODS** (`ods`) - Transform an ODS file into output items
* **Extract From PDF** (`pdf`) - Extracts the content and metadata from a PDF file
* **Extract From RTF** (`rtf`) - Transform a table in an RTF file into output items
* **Extract From Text File** (`text`) - Extracts the content of a text file
* **Extract From XML** (`xml`) - Extracts the content of an XML file
* **Extract From XLS** (`xls`) - Transform an Excel file into output items
* **Extract From XLSX** (`xlsx`) - Transform an Excel file into output items
* **Move File to Base64 String** (`binaryToPropery`) - Convert a file into a base64-encoded string

---

### Extract From PDF parameters (`pdf`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Options | `options` | collection | {} | ✗ | Whether to join the text from all pages or return an array of text from each page | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Join Pages | `joinPages` | boolean | True | Whether to join the text from all pages or return an array of text from each page |
| Keep Source | `keepSource` | options | json | Include JSON data of the input item |
| Max Pages | `maxPages` | number | 0 | Maximum number of pages to include |
| Password | `password` | string |  | Prowide password, if the PDF is encrypted |

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
* Aliases: CSV, Spreadsheet, Excel, xls, xlsx, ods, tabular, decode, decoding, Move Binary Data, Binary, File, PDF, JSON, HTML, ICS, iCal, txt, Text, RTF, XML, 64, Base64, Convert

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: extractFromFile
displayName: Extract from File
description: Convert binary data to JSON
version: '1'
nodeType: regular
group:
- input
operations:
- id: csv
  name: Extract From CSV
  description: Transform a CSV file into output items
- id: html
  name: Extract From HTML
  description: Transform a table in an HTML file into output items
- id: fromIcs
  name: Extract From ICS
  description: Transform a ICS file into output items
- id: fromJson
  name: Extract From JSON
  description: Transform a JSON file into output items
- id: ods
  name: Extract From ODS
  description: Transform an ODS file into output items
- id: pdf
  name: Extract From PDF
  description: Extracts the content and metadata from a PDF file
  params: []
- id: rtf
  name: Extract From RTF
  description: Transform a table in an RTF file into output items
- id: text
  name: Extract From Text File
  description: Extracts the content of a text file
- id: xml
  name: Extract From XML
  description: Extracts the content of an XML file
- id: xls
  name: Extract From XLS
  description: Transform an Excel file into output items
- id: xlsx
  name: Extract From XLSX
  description: Transform an Excel file into output items
- id: binaryToPropery
  name: Move File to Base64 String
  description: Convert a file into a base64-encoded string
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: binaryPropertyName
    text: e.g data
  - field: destinationKey
    text: e.g data
  - field: options
    text: Add option
  - field: options
    text: Add option
  hints:
  - field: binaryPropertyName
    text: The name of the input field containing the file data to be processed
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
  "$id": "https://n8n.io/schemas/nodes/extractFromFile.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Extract from File Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "csv",
        "html",
        "fromIcs",
        "fromJson",
        "ods",
        "pdf",
        "rtf",
        "text",
        "xml",
        "xls",
        "xlsx",
        "binaryToPropery"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Transform a CSV file into output items",
          "type": "string",
          "enum": [
            "csv",
            "html",
            "fromIcs",
            "fromJson",
            "ods",
            "pdf",
            "rtf",
            "text",
            "xml",
            "xls",
            "xlsx",
            "binaryToPropery"
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
        "destinationKey": {
          "description": "The name of the output field that will contain the extracted data",
          "type": "string",
          "default": "data",
          "examples": [
            "e.g data"
          ]
        },
        "options": {
          "description": "Whether to join the text from all pages or return an array of text from each page",
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
    "version": "1"
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
