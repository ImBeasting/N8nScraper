---
title: "Node: Microsoft Excel 365"
slug: "node-microsoftexcel"
version: "['2', '2.1', '2.2']"
updated: "2026-01-08"
summary: "Consume Microsoft Excel API"
node_type: "regular"
group: "['input']"
---

# Node: Microsoft Excel 365

**Purpose.** Consume Microsoft Excel API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:excel.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftExcelOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice**: This node connects to the Microsoft 365 cloud platform. Use the 'Extract from File' and 'Convert to File' nodes to directly manipulate spreadsheet files (.xls, .csv, etc). <a href="https://n8n.io/workflows/890-read-in-an-excel-spreadsheet-file/" target="_blank">More info</a>.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `microsoftExcelOAuth2Api` | ✓ | - |

---

## Operations

### Table Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Append | `append` | Add rows to the end of the table |
| Convert to Range | `convertToRange` | Convert a table to a range |
| Create | `addTable` | Add a table based on range |
| Delete | `deleteTable` | Delete a table |
| Get Columns | `getColumns` | Retrieve a list of table columns |
| Get Rows | `getRows` | Retrieve a list of table rows |
| Lookup | `lookup` | Look for rows that match a given value in a column |

### Workbook Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Sheet | `addWorksheet` | Add a new sheet to the workbook |
| Delete | `deleteWorkbook` | Delete workbook |
| Get Many | `getAll` | Get workbooks |

### Worksheet Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Append | `append` | Append data to sheet |
| Append or Update | `upsert` | Append a new row or update the current one if it already exists (upsert) |
| Clear | `clear` | Clear sheet |
| Delete | `deleteWorksheet` | Delete sheet |
| Get Many | `getAll` | Get a list of sheets |
| Get Rows | `readRows` | Retrieve a list of sheet rows |
| Update | `update` | Update rows of a sheet or sheet range |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | workbook | ✗ | Represents an Excel table |  |

**Resource options:**

* **Table** (`table`) - Represents an Excel table
* **Workbook** (`workbook`) - A workbook is the top level object which contains one or more worksheets
* **Sheet** (`worksheet`) - A sheet is a grid of cells which can contain data, tables, charts, etc

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | append | ✗ | Add rows to the end of the table |  |

**Operation options:**

* **Append** (`append`) - Add rows to the end of the table
* **Convert to Range** (`convertToRange`) - Convert a table to a range
* **Create** (`addTable`) - Add a table based on range
* **Delete** (`deleteTable`) - Delete a table
* **Get Columns** (`getColumns`) - Retrieve a list of table columns
* **Get Rows** (`getRows`) - Retrieve a list of table rows
* **Lookup** (`lookup`) - Look for rows that match a given value in a column

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: microsoftExcel
displayName: Microsoft Excel 365
description: Consume Microsoft Excel API
version:
- '2'
- '2.1'
- '2.2'
nodeType: regular
group:
- input
credentials:
- name: microsoftExcelOAuth2Api
  required: true
operations:
- id: append
  name: Append
  description: Add rows to the end of the table
- id: convertToRange
  name: Convert to Range
  description: Convert a table to a range
- id: addTable
  name: Create
  description: Add a table based on range
- id: deleteTable
  name: Delete
  description: Delete a table
- id: getColumns
  name: Get Columns
  description: Retrieve a list of table columns
- id: getRows
  name: Get Rows
  description: Retrieve a list of table rows
- id: lookup
  name: Lookup
  description: Look for rows that match a given value in a column
- id: addWorksheet
  name: Add Sheet
  description: Add a new sheet to the workbook
- id: deleteWorkbook
  name: Delete
  description: Delete workbook
- id: getAll
  name: Get Many
  description: Get workbooks
- id: upsert
  name: Append or Update
  description: Append a new row or update the current one if it already exists (upsert)
- id: clear
  name: Clear
  description: Clear sheet
- id: deleteWorksheet
  name: Delete
  description: Delete sheet
- id: readRows
  name: Get Rows
  description: Retrieve a list of sheet rows
- id: update
  name: Update
  description: Update rows of a sheet or sheet range
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices:
  - name: notice
    text: This node connects to the Microsoft 365 cloud platform. Use the 'Extract
      from File' and 'Convert to File' nodes to directly manipulate spreadsheet files
      (.xls, .csv, etc). <a href="https://n8n.io/workflows/890-read-in-an-excel-spreadsheet-file/"
      target="_blank">More info</a>.
    conditions: null
  tooltips: []
  placeholders: []
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
  "$id": "https://n8n.io/schemas/nodes/microsoftExcel.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft Excel 365 Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "append",
        "convertToRange",
        "addTable",
        "deleteTable",
        "getColumns",
        "getRows",
        "lookup",
        "addWorksheet",
        "deleteWorkbook",
        "getAll",
        "upsert",
        "clear",
        "deleteWorksheet",
        "readRows",
        "update"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Represents an Excel table",
          "type": "string",
          "enum": [
            "table",
            "workbook",
            "worksheet"
          ],
          "default": "workbook"
        },
        "operation": {
          "description": "Append data to sheet",
          "type": "string",
          "enum": [
            "append",
            "upsert",
            "clear",
            "deleteWorksheet",
            "getAll",
            "readRows",
            "update"
          ],
          "default": "getAll"
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
      "2",
      "2.1",
      "2.2"
    ]
  },
  "credentials": [
    {
      "name": "microsoftExcelOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2', '2.1', '2.2'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
