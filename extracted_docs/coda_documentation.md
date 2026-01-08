---
title: "Node: Coda"
slug: "node-coda"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Consume Coda API"
node_type: "regular"
group: "['output']"
---

# Node: Coda

**Purpose.** Consume Coda API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:coda.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **codaApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `codaApi` | ✓ | - |

---

## Operations

### Table Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create Row | `createRow` | Create/Insert a row |
| Delete Row | `deleteRow` | Delete one or multiple rows |
| Get All Columns | `getAllColumns` | Get all columns in a table |
| Get All Rows | `getAllRows` | Get all rows in a table |
| Get Column | `getColumn` | Get a column |
| Get Row | `getRow` | Get a row |
| Push Button | `pushButton` | Pushes a button |

### Formula Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a formula |
| Get Many | `getAll` | Get many formulas |

### Control Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a control |
| Get Many | `getAll` | Get many controls |

### View Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete Row | `deleteViewRow` | Delete view row |
| Get | `get` | Get a view |
| Get Columns | `getAllViewColumns` | Get all views columns |
| Get Many | `getAll` | Get many views |
| Get Rows | `getAllViewRows` | Get all views rows |
| Push Button | `pushViewButton` | Push view button |
| Update Row | `updateViewRow` | Update a view row |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | table | ✗ | Controls provide a user-friendly way to input a value that can affect other parts of the doc |  |

**Resource options:**

* **Control** (`control`) - Controls provide a user-friendly way to input a value that can affect other parts of the doc
* **Formula** (`formula`) - Formulas can be great for performing one-off computations
* **Table** (`table`) - Access data of tables in documents
* **View** (`view`) - Access data of views in documents

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | createRow | ✗ | Create/Insert a row |  |

**Operation options:**

* **Create Row** (`createRow`) - Create/Insert a row
* **Delete Row** (`deleteRow`) - Delete one or multiple rows
* **Get All Columns** (`getAllColumns`) - Get all columns in a table
* **Get All Rows** (`getAllRows`) - Get all rows in a table
* **Get Column** (`getColumn`) - Get a column
* **Get Row** (`getRow`) - Get a row
* **Push Button** (`pushButton`) - Pushes a button

---

### Create Row parameters (`createRow`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Table Name or ID | `tableId` | options |  | ✓ | The table to create the row in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Options | `options` | collection | {} | ✗ | Whether the API will not attempt to parse the data in any way | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Disable Parsing | `disableParsing` | boolean | False | Whether the API will not attempt to parse the data in any way |
| Key Columns | `keyColumns` | string |  | Optional column IDs, URLs, or names (fragile and discouraged), specifying columns to be used as upsert keys. If more than one separate by a comma (,). |

</details>


### Delete Row parameters (`deleteRow`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Table Name or ID | `tableId` | options |  | ✓ | The table to delete the row in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Row ID | `rowId` | string |  | ✓ | Row IDs to delete |  |

### Get All Columns parameters (`getAllColumns`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Table Name or ID | `tableId` | options |  | ✓ | The table to get the row from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Get All Rows parameters (`getAllRows`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Table Name or ID | `tableId` | options |  | ✓ | The table to get the rows from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Query used to filter returned rows, specified as &lt;column_id_or_name&gt;:&lt;value&gt;. If you'd like to use a column name instead of an ID, you must quote it (e.g., "My Column":123). Also note that value is a JSON value; if you'd like to use a string, you must surround it in quotes (e.g., "groceries"). | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | Query used to filter returned rows, specified as &lt;column_id_or_name&gt;:&lt;value&gt;. If you'd like to use a column name instead of an ID, you must quote it (e.g., "My Column":123). Also note that value is a JSON value; if you'd like to use a string, you must surround it in quotes (e.g., "groceries"). |
| RAW Data | `rawData` | boolean | False | Whether to return the data exactly in the way it got received from the API |
| Sort By | `sortBy` | options |  | Specifies the sort order of the rows returned. If left unspecified, rows are returned by creation time ascending. |
| Use Column Names | `useColumnNames` | boolean | False | Whether to use column names instead of column IDs in the returned output. This is generally discouraged as it is fragile. If columns are renamed, code using original names may throw errors. |
| ValueFormat | `valueFormat` | options |  | The format that cell values are returned as |
| Visible Only | `visibleOnly` | boolean | False | Whether to return only visible rows and columns for the table |

</details>


### Get Column parameters (`getColumn`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Table Name or ID | `tableId` | options |  | ✓ | The table to get the row from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Column ID | `columnId` | string |  | ✓ | The table to get the row from |  |

### Get Row parameters (`getRow`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Table Name or ID | `tableId` | options |  | ✓ | The table to get the row from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Row ID | `rowId` | string |  | ✓ | ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected |  |
| Options | `options` | collection | {} | ✗ | Whether to return the data exactly in the way it got received from the API | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| RAW Data | `rawData` | boolean | False | Whether to return the data exactly in the way it got received from the API |
| Use Column Names | `useColumnNames` | boolean | False | Whether to use column names instead of column IDs in the returned output. This is generally discouraged as it is fragile. If columns are renamed, code using original names may throw errors. |
| ValueFormat | `valueFormat` | options |  | The format that cell values are returned as |

</details>


### Push Button parameters (`pushButton`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Table Name or ID | `tableId` | options |  | ✓ | The table to get the row from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Row ID | `rowId` | string |  | ✓ | ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected |  |
| Column Name or ID | `columnId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Formula ID | `formulaId` | string |  | ✓ | The formula to get the row from |  |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Control ID | `controlId` | string |  | ✓ | The control to get the row from |  |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| View ID | `viewId` | string |  | ✓ | The view to get the row from |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Delete Row parameters (`deleteViewRow`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| View Name or ID | `viewId` | options |  | ✓ | The view to get the row from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Row Name or ID | `rowId` | options |  | ✓ | The view to get the row from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Get Columns parameters (`getAllViewColumns`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| View Name or ID | `viewId` | options |  | ✓ | The table to get the rows from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Get Rows parameters (`getAllViewRows`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| View Name or ID | `viewId` | options |  | ✓ | The table to get the rows from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Query used to filter returned rows, specified as &lt;column_id_or_name&gt;:&lt;value&gt;. If you'd like to use a column name instead of an ID, you must quote it (e.g., "My Column":123). Also note that value is a JSON value; if you'd like to use a string, you must surround it in quotes (e.g., "groceries"). | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | Query used to filter returned rows, specified as &lt;column_id_or_name&gt;:&lt;value&gt;. If you'd like to use a column name instead of an ID, you must quote it (e.g., "My Column":123). Also note that value is a JSON value; if you'd like to use a string, you must surround it in quotes (e.g., "groceries"). |
| Use Column Names | `useColumnNames` | boolean | False | Whether to use column names instead of column IDs in the returned output. This is generally discouraged as it is fragile. If columns are renamed, code using original names may throw errors. |
| ValueFormat | `valueFormat` | options |  | The format that cell values are returned as |
| RAW Data | `rawData` | boolean | False | Whether to return the data exactly in the way it got received from the API |
| Sort By | `sortBy` | options |  | Specifies the sort order of the rows returned. If left unspecified, rows are returned by creation time ascending. |

</details>


### Push Button parameters (`pushViewButton`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| View Name or ID | `viewId` | options |  | ✓ | The view to get the row from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Row Name or ID | `rowId` | options |  | ✓ | The view to get the row from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Column Name or ID | `columnId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Update Row parameters (`updateViewRow`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc Name or ID | `docId` | options |  | ✓ | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| View Name or ID | `viewId` | options |  | ✓ | The view to get the row from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Row Name or ID | `rowId` | options |  | ✓ | The view to get the row from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Key Name | `keyName` | string | columns | ✓ | The view to get the row from |  |
| Options | `options` | collection | {} | ✗ | Whether the API will not attempt to parse the data in any way | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Disable Parsing | `disableParsing` | boolean | False | Whether the API will not attempt to parse the data in any way |

</details>


---

## Load Options Methods

- `getDocs`

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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: coda
displayName: Coda
description: Consume Coda API
version:
- '1'
- '1.1'
nodeType: regular
group:
- output
credentials:
- name: codaApi
  required: true
operations:
- id: createRow
  name: Create Row
  description: Create/Insert a row
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - view
          operation:
          - updateViewRow
    typeInfo: &id002
      type: options
      displayName: Doc Name or ID
      name: docId
      typeOptions:
        loadOptionsMethod: getDocs
      possibleValues: []
  - id: tableId
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: The table to create the row in. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - table
          operation:
          - getAllColumns
    typeInfo: &id004
      type: options
      displayName: Table Name or ID
      name: tableId
      typeOptions:
        loadOptionsMethod: getTables
      possibleValues: []
- id: deleteRow
  name: Delete Row
  description: Delete one or multiple rows
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: tableId
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: The table to delete the row in. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: rowId
    name: Row ID
    type: string
    default: ''
    required: true
    description: Row IDs to delete
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - view
          operation:
          - updateViewRow
    typeInfo: &id010
      type: options
      displayName: Row Name or ID
      name: rowId
      typeOptions:
        loadOptionsMethod: getViewRows
      possibleValues: []
- id: getAllColumns
  name: Get All Columns
  description: Get all columns in a table
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: tableId
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: The table to get the row from. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id005
      displayOptions:
        show:
          resource:
          - view
          operation:
          - getAllViewColumns
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          resource:
          - view
          operation:
          - getAllViewColumns
          returnAll:
          - false
    typeInfo: &id008
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
- id: getAllRows
  name: Get All Rows
  description: Get all rows in a table
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: tableId
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: The table to get the rows from. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: getColumn
  name: Get Column
  description: Get a column
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: tableId
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: The table to get the row from. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: columnId
    name: Column ID
    type: string
    default: ''
    required: true
    description: The table to get the row from
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - view
          operation:
          - pushViewButton
    typeInfo: &id012
      type: options
      displayName: Column Name or ID
      name: columnId
      typeOptions:
        loadOptionsMethod: getViewColumns
      possibleValues: []
- id: getRow
  name: Get Row
  description: Get a row
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: tableId
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: The table to get the row from. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: rowId
    name: Row ID
    type: string
    default: ''
    required: true
    description: ID or name of the row. Names are discouraged because they're easily
      prone to being changed by users. If you're using a name, be sure to URI-encode
      it. If there are multiple rows with the same value in the identifying column,
      an arbitrary one will be selected
    validation: *id009
    typeInfo: *id010
- id: pushButton
  name: Push Button
  description: Pushes a button
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: tableId
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: The table to get the row from. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: rowId
    name: Row ID
    type: string
    default: ''
    required: true
    description: ID or name of the row. Names are discouraged because they're easily
      prone to being changed by users. If you're using a name, be sure to URI-encode
      it. If there are multiple rows with the same value in the identifying column,
      an arbitrary one will be selected
    validation: *id009
    typeInfo: *id010
  - id: columnId
    name: Column Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id011
    typeInfo: *id012
- id: get
  name: Get
  description: Get a formula
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: formulaId
    name: Formula ID
    type: string
    default: ''
    required: true
    description: The formula to get the row from
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - formula
          operation:
          - get
    typeInfo:
      type: string
      displayName: Formula ID
      name: formulaId
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: controlId
    name: Control ID
    type: string
    default: ''
    required: true
    description: The control to get the row from
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - control
          operation:
          - get
    typeInfo:
      type: string
      displayName: Control ID
      name: controlId
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: viewId
    name: View ID
    type: string
    default: ''
    required: true
    description: The view to get the row from
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - view
          operation:
          - updateViewRow
    typeInfo: &id014
      type: options
      displayName: View Name or ID
      name: viewId
      typeOptions:
        loadOptionsMethod: getViews
      possibleValues: []
- id: getAll
  name: Get Many
  description: Get many formulas
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: deleteViewRow
  name: Delete Row
  description: Delete view row
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: viewId
    name: View Name or ID
    type: options
    default: ''
    required: true
    description: The view to get the row from. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id013
    typeInfo: *id014
  - id: rowId
    name: Row Name or ID
    type: options
    default: ''
    required: true
    description: The view to get the row from. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
- id: getAllViewColumns
  name: Get Columns
  description: Get all views columns
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: viewId
    name: View Name or ID
    type: options
    default: ''
    required: true
    description: The table to get the rows from. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: getAllViewRows
  name: Get Rows
  description: Get all views rows
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: viewId
    name: View Name or ID
    type: options
    default: ''
    required: true
    description: The table to get the rows from. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: pushViewButton
  name: Push Button
  description: Push view button
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: viewId
    name: View Name or ID
    type: options
    default: ''
    required: true
    description: The view to get the row from. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id013
    typeInfo: *id014
  - id: rowId
    name: Row Name or ID
    type: options
    default: ''
    required: true
    description: The view to get the row from. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: columnId
    name: Column Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id011
    typeInfo: *id012
- id: updateViewRow
  name: Update Row
  description: ''
  params:
  - id: docId
    name: Doc Name or ID
    type: options
    default: ''
    required: true
    description: ID of the doc. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: viewId
    name: View Name or ID
    type: options
    default: ''
    required: true
    description: The view to get the row from. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id013
    typeInfo: *id014
  - id: rowId
    name: Row Name or ID
    type: options
    default: ''
    required: true
    description: The view to get the row from. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: keyName
    name: Key Name
    type: string
    default: columns
    required: true
    description: The view to get the row from
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - view
          operation:
          - updateViewRow
    typeInfo:
      type: string
      displayName: Key Name
      name: keyName
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/coda.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Coda Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "createRow",
        "deleteRow",
        "getAllColumns",
        "getAllRows",
        "getColumn",
        "getRow",
        "pushButton",
        "get",
        "getAll",
        "deleteViewRow",
        "getAllViewColumns",
        "getAllViewRows",
        "pushViewButton",
        "updateViewRow"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Controls provide a user-friendly way to input a value that can affect other parts of the doc",
          "type": "string",
          "enum": [
            "control",
            "formula",
            "table",
            "view"
          ],
          "default": "table"
        },
        "operation": {
          "description": "Delete view row",
          "type": "string",
          "enum": [
            "deleteViewRow",
            "get",
            "getAllViewColumns",
            "getAll",
            "getAllViewRows",
            "pushViewButton",
            "updateViewRow"
          ],
          "default": "get"
        },
        "docId": {
          "description": "ID of the doc. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "tableId": {
          "description": "The table to get the row from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Whether the API will not attempt to parse the data in any way",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "rowId": {
          "description": "The view to get the row from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 50
        },
        "columnId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "formulaId": {
          "description": "The formula to get the row from",
          "type": "string",
          "default": ""
        },
        "controlId": {
          "description": "The control to get the row from",
          "type": "string",
          "default": ""
        },
        "viewId": {
          "description": "The view to get the row from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "keyName": {
          "description": "The view to get the row from",
          "type": "string",
          "default": "columns"
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
  "credentials": [
    {
      "name": "codaApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
