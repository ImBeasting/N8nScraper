---
title: "Node: Quick Base"
slug: "node-quickbase"
version: "1"
updated: "2025-11-13"
summary: "Integrate with the Quick Base RESTful API"
node_type: "regular"
group: "['input']"
---

# Node: Quick Base

**Purpose.** Integrate with the Quick Base RESTful API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:quickbase.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **quickbaseApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `quickbaseApi` | ✓ | - |

---

## API Patterns

**Headers Used:** QB-Realm-Hostname, User-Agent

---

## Operations

### Field Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many fields |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a file |
| Download | `download` | Download a file |

### Record Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a record |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a record |
| Get Many | `getAll` | Get many records |
| Update | `update` | Update a record |

### Report Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a report |
| Run | `run` | Run a report |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | record | ✗ | Resource to operate on |  |

**Resource options:**

* **Field** (`field`)
* **File** (`file`)
* **Record** (`record`)
* **Report** (`report`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Get many fields |  |

**Operation options:**

* **Get Many** (`getAll`) - Get many fields

---

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table ID | `tableId` | string |  | ✓ | The table identifier |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Whether to get back the custom permissions for the field(s) | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Field Perms | `includeFieldPerms` | boolean | False | Whether to get back the custom permissions for the field(s) |

</details>

| Table ID | `tableId` | string |  | ✓ | The table identifier |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | An array of field IDs for the fields that should be returned in the response. If empty, the default columns on the table will be returned. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Select | `select` | multiOptions | [] | An array of field IDs for the fields that should be returned in the response. If empty, the default columns on the table will be returned. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sort By | `sortByUi` | fixedCollection | {} | The unique identifier of a field in a table. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Where | `where` | string |  | The filter, using the <a href="https://help.quickbase.com/api-guide/componentsquery.html">Quick Base query language</a>, which determines the records to return |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table ID | `tableId` | string |  | ✓ | The table identifier |  |
| Record ID | `recordId` | string |  | ✓ | The unique identifier of the record |  |
| Field ID | `fieldId` | string |  | ✓ | The unique identifier of the field |  |
| Version Number | `versionNumber` | number | 1 | ✓ | The file attachment version number |  |
| Table ID | `tableId` | string |  | ✓ | The table identifier |  |
| Where | `where` | string |  | ✓ | The filter to delete records. To delete all records specify a filter that will include all records, for example {3.GT.0} where 3 is the ID of the Record ID field. |  |

### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table ID | `tableId` | string |  | ✓ | The table identifier |  |
| Record ID | `recordId` | string |  | ✓ | The unique identifier of the record |  |
| Field ID | `fieldId` | string |  | ✓ | The unique identifier of the field |  |
| Version Number | `versionNumber` | number | 1 | ✓ | The file attachment version number |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be written |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table ID | `tableId` | string |  | ✓ | The table identifier |  |
| Columns | `columns` | string |  | ✓ | Comma-separated list of the properties which should used as columns for the new rows | e.g. Select Fields... |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Specify an array of field IDs that will return data for any updates or added record. Record ID (FID 3) is always returned if any field ID is requested. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Return Field Names or IDs | `fields` | multiOptions | [] | Specify an array of field IDs that will return data for any updates or added record. Record ID (FID 3) is always returned if any field ID is requested. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Use Field IDs | `useFieldIDs` | boolean | False | Whether to use Field IDs instead of Field Names in Columns |

</details>


### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table ID | `tableId` | string |  | ✓ | The table identifier |  |
| Columns | `columns` | string |  | ✓ | Comma-separated list of the properties which should used as columns for the new rows | e.g. id,name,description |  |
| Update Key | `updateKey` | string |  | ✗ | Update can use the key field on the table, or any other supported unique field |  |
| Merge Field Name or ID | `mergeFieldId` | options |  | ✗ | <p>You're updating records in a Quick Base table with data from an external file. In order for a merge like this to work, Quick Base needs a way to match records in the source data with corresponding records in the destination table.</p><p>You make this possible by choosing the field in the app table that holds unique matching values. This is called a merge field.</p>. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Specify an array of field IDs that will return data for any updates or added record. Record ID (FID 3) is always returned if any field ID is requested. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field Names or IDs | `fields` | multiOptions | [] | Specify an array of field IDs that will return data for any updates or added record. Record ID (FID 3) is always returned if any field ID is requested. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Use Field IDs | `useFieldIDs` | boolean | False | Whether to use Field IDs instead of Field Names in Columns |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table ID | `tableId` | string |  | ✓ | The table identifier |  |
| Columns | `columns` | string |  | ✓ | Comma-separated list of the properties which should used as columns for the new rows | e.g. id,name,description |  |
| Update Key | `updateKey` | string |  | ✗ | Update can use the key field on the table, or any other supported unique field |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Specify an array of field IDs that will return data for any updates or added record. Record ID (FID 3) is always returned if any field ID is requested. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field Names or IDs | `fields` | multiOptions | [] | Specify an array of field IDs that will return data for any updates or added record. Record ID (FID 3) is always returned if any field ID is requested. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Use Field IDs | `useFieldIDs` | boolean | False | Whether to use Field IDs instead of Field Names in Columns |
| Merge Field ID | `mergeFieldId` | options |  | You're updating records in a Quick Base table with data from an external file. In order for a merge like this to work,
			// 	Quick Base needs a way to match records in the source data with corresponding records in the destination table. You make this possible by
			// 	choosing the field in the app table that holds unique matching values. This is called a merge field. |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table ID | `tableId` | string |  | ✓ | The table identifier |  |
| Report ID | `reportId` | string |  | ✓ | The identifier of the report, unique to the table |  |

### Run parameters (`run`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table ID | `tableId` | string |  | ✓ | The table identifier |  |
| Report ID | `reportId` | string |  | ✓ | The identifier of the report, unique to the table |  |
| Return All | `returnAll` | boolean | True | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |

---

## Load Options Methods

- `getTableFields`

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
* Categories: Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: quickbase
displayName: Quick Base
description: Integrate with the Quick Base RESTful API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: quickbaseApi
  required: true
operations:
- id: getAll
  name: Get Many
  description: Get many fields
  params:
  - id: tableId
    name: Table ID
    type: string
    default: ''
    required: true
    description: The table identifier
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - report
          operation:
          - run
    typeInfo: &id002
      type: string
      displayName: Table ID
      name: tableId
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id003
      displayOptions:
        show:
          resource:
          - report
          operation:
          - run
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          resource:
          - report
          operation:
          - run
        hide:
          returnAll:
          - true
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: tableId
    name: Table ID
    type: string
    default: ''
    required: true
    description: The table identifier
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: delete
  name: Delete
  description: Delete a file
  params:
  - id: tableId
    name: Table ID
    type: string
    default: ''
    required: true
    description: The table identifier
    validation: *id001
    typeInfo: *id002
  - id: recordId
    name: Record ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the record
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - download
          - delete
    typeInfo: &id008
      type: string
      displayName: Record ID
      name: recordId
  - id: fieldId
    name: Field ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the field
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - download
          - delete
    typeInfo: &id010
      type: string
      displayName: Field ID
      name: fieldId
  - id: versionNumber
    name: Version Number
    type: number
    default: 1
    required: true
    description: The file attachment version number
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - download
          - delete
    typeInfo: &id012
      type: number
      displayName: Version Number
      name: versionNumber
  - id: tableId
    name: Table ID
    type: string
    default: ''
    required: true
    description: The table identifier
    validation: *id001
    typeInfo: *id002
  - id: where
    name: Where
    type: string
    default: ''
    required: true
    description: The filter to delete records. To delete all records specify a filter
      that will include all records, for example {3.GT.0} where 3 is the ID of the
      Record ID field.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - record
          operation:
          - delete
    typeInfo:
      type: string
      displayName: Where
      name: where
- id: download
  name: Download
  description: Download a file
  params:
  - id: tableId
    name: Table ID
    type: string
    default: ''
    required: true
    description: The table identifier
    validation: *id001
    typeInfo: *id002
  - id: recordId
    name: Record ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the record
    validation: *id007
    typeInfo: *id008
  - id: fieldId
    name: Field ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the field
    validation: *id009
    typeInfo: *id010
  - id: versionNumber
    name: Version Number
    type: number
    default: 1
    required: true
    description: The file attachment version number
    validation: *id011
    typeInfo: *id012
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be written
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - download
    typeInfo:
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
- id: create
  name: Create
  description: Create a record
  params:
  - id: tableId
    name: Table ID
    type: string
    default: ''
    required: true
    description: The table identifier
    validation: *id001
    typeInfo: *id002
  - id: columns
    name: Columns
    type: string
    default: ''
    required: true
    description: Comma-separated list of the properties which should used as columns
      for the new rows
    placeholder: Select Fields...
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - record
          operation:
          - upsert
    typeInfo: &id014
      type: string
      displayName: Columns
      name: columns
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id015
      displayOptions:
        show:
          resource:
          - record
          operation:
          - upsert
    typeInfo: &id016
      type: boolean
      displayName: Simplify
      name: simple
- id: upsert
  name: Create or Update
  description: Create a new record, or update the current one if it already exists
    (upsert)
  params:
  - id: tableId
    name: Table ID
    type: string
    default: ''
    required: true
    description: The table identifier
    validation: *id001
    typeInfo: *id002
  - id: columns
    name: Columns
    type: string
    default: ''
    required: true
    description: Comma-separated list of the properties which should used as columns
      for the new rows
    placeholder: id,name,description
    validation: *id013
    typeInfo: *id014
  - id: updateKey
    name: Update Key
    type: string
    default: ''
    required: false
    description: Update can use the key field on the table, or any other supported
      unique field
    validation: &id017
      displayOptions:
        show:
          resource:
          - record
          operation:
          - upsert
    typeInfo: &id018
      type: string
      displayName: Update Key
      name: updateKey
  - id: mergeFieldId
    name: Merge Field Name or ID
    type: options
    default: ''
    required: false
    description: <p>You're updating records in a Quick Base table with data from an
      external file. In order for a merge like this to work, Quick Base needs a way
      to match records in the source data with corresponding records in the destination
      table.</p><p>You make this possible by choosing the field in the app table that
      holds unique matching values. This is called a merge field.</p>. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      displayOptions:
        show:
          resource:
          - record
          operation:
          - upsert
    typeInfo:
      type: options
      displayName: Merge Field Name or ID
      name: mergeFieldId
      typeOptions:
        loadOptionsMethod: getUniqueTableFields
      possibleValues: []
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id015
    typeInfo: *id016
- id: update
  name: Update
  description: Update a record
  params:
  - id: tableId
    name: Table ID
    type: string
    default: ''
    required: true
    description: The table identifier
    validation: *id001
    typeInfo: *id002
  - id: columns
    name: Columns
    type: string
    default: ''
    required: true
    description: Comma-separated list of the properties which should used as columns
      for the new rows
    placeholder: id,name,description
    validation: *id013
    typeInfo: *id014
  - id: updateKey
    name: Update Key
    type: string
    default: ''
    required: false
    description: Update can use the key field on the table, or any other supported
      unique field
    validation: *id017
    typeInfo: *id018
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id015
    typeInfo: *id016
- id: get
  name: Get
  description: Get a report
  params:
  - id: tableId
    name: Table ID
    type: string
    default: ''
    required: true
    description: The table identifier
    validation: *id001
    typeInfo: *id002
  - id: reportId
    name: Report ID
    type: string
    default: ''
    required: true
    description: The identifier of the report, unique to the table
    validation: &id019
      required: true
      displayOptions:
        show:
          resource:
          - report
          operation:
          - run
    typeInfo: &id020
      type: string
      displayName: Report ID
      name: reportId
- id: run
  name: Run
  description: Run a report
  params:
  - id: tableId
    name: Table ID
    type: string
    default: ''
    required: true
    description: The table identifier
    validation: *id001
    typeInfo: *id002
  - id: reportId
    name: Report ID
    type: string
    default: ''
    required: true
    description: The identifier of the report, unique to the table
    validation: *id019
    typeInfo: *id020
  - id: returnAll
    name: Return All
    type: boolean
    default: true
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - QB-Realm-Hostname
  - User-Agent
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: options
    text: Add Field
  - field: columns
    text: Select Fields...
  - field: options
    text: Add option
  - field: options
    text: Add Field
  - field: columns
    text: id,name,description
  - field: options
    text: Add option
  - field: columns
    text: id,name,description
  - field: options
    text: Add option
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be written
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
  "$id": "https://n8n.io/schemas/nodes/quickbase.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Quick Base Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "getAll",
        "delete",
        "download",
        "create",
        "upsert",
        "update",
        "get",
        "run"
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
            "field",
            "file",
            "record",
            "report"
          ],
          "default": "record"
        },
        "operation": {
          "description": "Get a report",
          "type": "string",
          "enum": [
            "get",
            "run"
          ],
          "default": "get"
        },
        "tableId": {
          "description": "The table identifier",
          "type": "string",
          "default": ""
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": true
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
        },
        "options": {
          "description": "Specify an array of field IDs that will return data for any updates or added record. Record ID (FID 3) is always returned if any field ID is requested. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "recordId": {
          "description": "The unique identifier of the record",
          "type": "string",
          "default": ""
        },
        "fieldId": {
          "description": "The unique identifier of the field",
          "type": "string",
          "default": ""
        },
        "versionNumber": {
          "description": "The file attachment version number",
          "type": "number",
          "default": 1
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "columns": {
          "description": "Comma-separated list of the properties which should used as columns for the new rows",
          "type": "string",
          "default": "",
          "examples": [
            "id,name,description"
          ]
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "where": {
          "description": "The filter to delete records. To delete all records specify a filter that will include all records, for example {3.GT.0} where 3 is the ID of the Record ID field.",
          "type": "string",
          "default": ""
        },
        "updateKey": {
          "description": "Update can use the key field on the table, or any other supported unique field",
          "type": "string",
          "default": ""
        },
        "mergeFieldId": {
          "description": "<p>You're updating records in a Quick Base table with data from an external file. In order for a merge like this to work, Quick Base needs a way to match records in the source data with corresponding records in the destination table.</p><p>You make this possible by choosing the field in the app table that holds unique matching values. This is called a merge field.</p>. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "reportId": {
          "description": "The identifier of the report, unique to the table",
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
    "version": "1"
  },
  "credentials": [
    {
      "name": "quickbaseApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
