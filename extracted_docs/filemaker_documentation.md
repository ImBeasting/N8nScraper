---
title: "Node: FileMaker"
slug: "node-filemaker"
version: "1"
updated: "2025-11-13"
summary: "Retrieve data from the FileMaker data API"
node_type: "regular"
group: "['input']"
---

# Node: FileMaker

**Purpose.** Retrieve data from the FileMaker data API


---

## Node Details

- **Icon:** `file:filemaker.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **fileMaker**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `fileMaker` | ✓ | - |

---

## API Patterns

**HTTP Methods:** GET, POST, DELETE

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Action | `action` | options | record | ✗ |  |  |

**Action options:**

* **Login** (`login`)
* **Logout** (`logout`)
* **Create Record** (`create`)
* **Delete Record** (`delete`)
* **Duplicate Record** (`duplicate`)
* **Edit Record** (`edit`)
* **Find Records** (`find`)
* **Get Records** (`records`)
* **Get Records By ID** (`record`)
* **Perform Script** (`performscript`)

| Layout Name or ID | `layout` | options |  | ✓ | FileMaker Layout Name. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Layout Name |  |
| Record ID | `recid` | number |  | ✓ | Internal Record ID returned by get (recordid) | e.g. Record ID |  |
| Offset | `offset` | number | 1 | ✗ | The record number of the first record in the range of records | e.g. 0 |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | e.g. 100 | min:1, max:∞ |
| Get Portals | `getPortals` | boolean | False | ✗ | Whether to get portal data as well |  |
| Portals Name or ID | `portals` | options | [] | ✗ | The portal result set to return. Use the portal object name or portal table name. If this parameter is omitted, the API will return all portal objects and records in the layout. For best performance, pass the portal object name or portal table name. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Portals |  |
| Response Layout Name or ID | `responseLayout` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Queries | `queries` | fixedCollection | {} | ✗ | Search Field. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add query |  |

<details>
<summary><strong>Queries sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` |  |  |  |

</details>

| Sort Data? | `setSort` | boolean | False | ✗ | Whether to sort data |  |
| Sort | `sortParametersUi` | fixedCollection | {} | ✗ | Sort rules | e.g. Add Sort Rules |  |

<details>
<summary><strong>Sort sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Rules | `rules` |  |  |  |

</details>

| Before Find Script | `setScriptBefore` | boolean | False | ✗ | Whether to define a script to be run before the action specified by the API call and after the subsequent sort |  |
| Script Name or ID | `scriptBefore` | options |  | ✓ | The name of the FileMaker script to be run after the action specified by the API call and after the subsequent sort. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Script Name |  |
| Script Parameter | `scriptBeforeParam` | string |  | ✗ | A parameter for the FileMaker script | e.g. Script Parameters |  |
| Before Sort Script | `setScriptSort` | boolean | False | ✗ | Whether to define a script to be run after the action specified by the API call but before the subsequent sort |  |
| Script Name or ID | `scriptSort` | options |  | ✓ | The name of the FileMaker script to be run after the action specified by the API call but before the subsequent sort. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Script Name |  |
| Script Parameter | `scriptSortParam` | string |  | ✗ | A parameter for the FileMaker script | e.g. Script Parameters |  |
| After Sort Script | `setScriptAfter` | boolean | False | ✗ | Whether to define a script to be run after the action specified by the API call but before the subsequent sort |  |
| Script Name or ID | `scriptAfter` | options |  | ✓ | The name of the FileMaker script to be run after the action specified by the API call and after the subsequent sort. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Script Name |  |
| Script Parameter | `scriptAfterParam` | string |  | ✗ | A parameter for the FileMaker script | e.g. Script Parameters |  |
| fieldData | `fieldData` | string | {} | ✗ | Additional fields to add. | e.g. {"field1": "value", "field2": "value", ...} |  |
| Mod ID | `modId` | number |  | ✗ | The last modification ID. When you use modId, a record is edited only when the modId matches. |  |
| Fields | `fieldsParametersUi` | fixedCollection | {} | ✗ | Fields to define | e.g. Add field |  |

<details>
<summary><strong>Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` |  |  |  |

</details>

| Script Name or ID | `script` | options |  | ✓ | The name of the FileMaker script to be run. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Script Name |  |
| Script Parameter | `scriptParam` | string |  | ✗ | A parameter for the FileMaker script | e.g. Script Parameters |  |

---

## Load Options Methods

- `getLayouts`

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
* Categories: Development, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: filemaker
displayName: FileMaker
description: Retrieve data from the FileMaker data API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: fileMaker
  required: true
params:
- id: action
  name: Action
  type: options
  default: record
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Action
    name: action
    possibleValues:
    - value: login
      name: Login
      description: ''
    - value: logout
      name: Logout
      description: ''
    - value: create
      name: Create Record
      description: ''
    - value: delete
      name: Delete Record
      description: ''
    - value: duplicate
      name: Duplicate Record
      description: ''
    - value: edit
      name: Edit Record
      description: ''
    - value: find
      name: Find Records
      description: ''
    - value: records
      name: Get Records
      description: ''
    - value: record
      name: Get Records By ID
      description: ''
    - value: performscript
      name: Perform Script
      description: ''
- id: layout
  name: Layout Name or ID
  type: options
  default: ''
  required: true
  description: FileMaker Layout Name. Choose from the list, or specify an ID using
    an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  placeholder: Layout Name
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Layout Name or ID
    name: layout
    typeOptions:
      loadOptionsMethod: getLayouts
    possibleValues: []
- id: recid
  name: Record ID
  type: number
  default: ''
  required: true
  description: Internal Record ID returned by get (recordid)
  placeholder: Record ID
  validation:
    required: true
    displayOptions:
      show:
        action:
        - record
        - edit
        - delete
        - duplicate
  typeInfo:
    type: number
    displayName: Record ID
    name: recid
- id: offset
  name: Offset
  type: number
  default: 1
  required: false
  description: The record number of the first record in the range of records
  placeholder: '0'
  validation:
    displayOptions:
      show:
        action:
        - find
        - records
  typeInfo:
    type: number
    displayName: Offset
    name: offset
- id: limit
  name: Limit
  type: number
  default: 100
  required: false
  description: Max number of results to return
  placeholder: '100'
  validation:
    displayOptions:
      show:
        action:
        - find
        - records
  typeInfo:
    type: number
    displayName: Limit
    name: limit
    typeOptions:
      minValue: 1
- id: getPortals
  name: Get Portals
  type: boolean
  default: false
  required: false
  description: Whether to get portal data as well
  validation:
    displayOptions:
      show:
        action:
        - record
        - records
        - find
  typeInfo:
    type: boolean
    displayName: Get Portals
    name: getPortals
- id: portals
  name: Portals Name or ID
  type: options
  default: []
  required: false
  description: The portal result set to return. Use the portal object name or portal
    table name. If this parameter is omitted, the API will return all portal objects
    and records in the layout. For best performance, pass the portal object name or
    portal table name. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  placeholder: Portals
  validation:
    displayOptions:
      show:
        action:
        - record
        - records
        - find
        getPortals:
        - true
  typeInfo:
    type: options
    displayName: Portals Name or ID
    name: portals
    typeOptions:
      multipleValues: true
      loadOptionsMethod: getPortals
    possibleValues: []
- id: responseLayout
  name: Response Layout Name or ID
  type: options
  default: ''
  required: false
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    displayOptions:
      show:
        action:
        - find
  typeInfo:
    type: options
    displayName: Response Layout Name or ID
    name: responseLayout
    typeOptions:
      loadOptionsMethod: getResponseLayouts
    possibleValues: []
- id: queries
  name: Queries
  type: fixedCollection
  default: {}
  required: false
  description: Search Field. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  placeholder: Add query
  validation:
    displayOptions:
      show:
        action:
        - find
  typeInfo:
    type: fixedCollection
    displayName: Queries
    name: queries
    typeOptions:
      multipleValues: true
    subProperties:
    - name: query
      displayName: Query
      values:
      - displayName: Fields
        name: fields
        type: fixedCollection
        description: Search Field. Choose from the list, or specify an ID using an
          <a href="https://docs.n8n.io/code/expressions/">expression</a>.
        placeholder: Add field
        default: {}
        options:
        - name: field
          displayName: Field
          values:
          - displayName: Field Name or ID
            name: name
            type: options
            description: Search Field. Choose from the list, or specify an ID using
              an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
            default: ''
            options: []
            typeOptions:
              loadOptionsMethod: getFields
          - displayName: Value
            name: value
            type: string
            description: Value to search
            default: ''
        typeOptions:
          multipleValues: true
      - displayName: Omit
        name: omit
        type: boolean
        default: false
- id: setSort
  name: Sort Data?
  type: boolean
  default: false
  required: false
  description: Whether to sort data
  validation:
    displayOptions:
      show:
        action:
        - find
        - record
        - records
  typeInfo:
    type: boolean
    displayName: Sort Data?
    name: setSort
- id: sortParametersUi
  name: Sort
  type: fixedCollection
  default: {}
  required: false
  description: Sort rules
  placeholder: Add Sort Rules
  validation:
    displayOptions:
      show:
        setSort:
        - true
        action:
        - find
        - records
  typeInfo:
    type: fixedCollection
    displayName: Sort
    name: sortParametersUi
    typeOptions:
      multipleValues: true
    subProperties:
    - name: rules
      displayName: Rules
      values:
      - displayName: Field Name or ID
        name: name
        type: options
        description: Field Name. Choose from the list, or specify an ID using an <a
          href="https://docs.n8n.io/code/expressions/">expression</a>.
        default: ''
        options: []
        typeOptions:
          loadOptionsMethod: getFields
      - displayName: Order
        name: value
        type: options
        description: Sort order
        value: ascend
        default: ascend
        options:
        - name: Ascend
          value: ascend
          displayName: Ascend
        - name: Descend
          value: descend
          displayName: Descend
- id: setScriptBefore
  name: Before Find Script
  type: boolean
  default: false
  required: false
  description: Whether to define a script to be run before the action specified by
    the API call and after the subsequent sort
  validation:
    displayOptions:
      show:
        action:
        - find
        - record
        - records
  typeInfo:
    type: boolean
    displayName: Before Find Script
    name: setScriptBefore
- id: scriptBefore
  name: Script Name or ID
  type: options
  default: ''
  required: true
  description: The name of the FileMaker script to be run after the action specified
    by the API call and after the subsequent sort. Choose from the list, or specify
    an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  placeholder: Script Name
  validation:
    required: true
    displayOptions:
      show:
        action:
        - find
        - record
        - records
        setScriptBefore:
        - true
  typeInfo:
    type: options
    displayName: Script Name or ID
    name: scriptBefore
    typeOptions:
      loadOptionsMethod: getScripts
    possibleValues: []
- id: scriptBeforeParam
  name: Script Parameter
  type: string
  default: ''
  required: false
  description: A parameter for the FileMaker script
  placeholder: Script Parameters
  validation:
    displayOptions:
      show:
        action:
        - find
        - record
        - records
        setScriptBefore:
        - true
  typeInfo:
    type: string
    displayName: Script Parameter
    name: scriptBeforeParam
- id: setScriptSort
  name: Before Sort Script
  type: boolean
  default: false
  required: false
  description: Whether to define a script to be run after the action specified by
    the API call but before the subsequent sort
  validation:
    displayOptions:
      show:
        action:
        - find
        - record
        - records
  typeInfo:
    type: boolean
    displayName: Before Sort Script
    name: setScriptSort
- id: scriptSort
  name: Script Name or ID
  type: options
  default: ''
  required: true
  description: The name of the FileMaker script to be run after the action specified
    by the API call but before the subsequent sort. Choose from the list, or specify
    an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  placeholder: Script Name
  validation:
    required: true
    displayOptions:
      show:
        action:
        - find
        - record
        - records
        setScriptSort:
        - true
  typeInfo:
    type: options
    displayName: Script Name or ID
    name: scriptSort
    typeOptions:
      loadOptionsMethod: getScripts
    possibleValues: []
- id: scriptSortParam
  name: Script Parameter
  type: string
  default: ''
  required: false
  description: A parameter for the FileMaker script
  placeholder: Script Parameters
  validation:
    displayOptions:
      show:
        action:
        - find
        - record
        - records
        setScriptSort:
        - true
  typeInfo:
    type: string
    displayName: Script Parameter
    name: scriptSortParam
- id: setScriptAfter
  name: After Sort Script
  type: boolean
  default: false
  required: false
  description: Whether to define a script to be run after the action specified by
    the API call but before the subsequent sort
  validation:
    displayOptions:
      show:
        action:
        - find
        - record
        - records
  typeInfo:
    type: boolean
    displayName: After Sort Script
    name: setScriptAfter
- id: scriptAfter
  name: Script Name or ID
  type: options
  default: ''
  required: true
  description: The name of the FileMaker script to be run after the action specified
    by the API call and after the subsequent sort. Choose from the list, or specify
    an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  placeholder: Script Name
  validation:
    required: true
    displayOptions:
      show:
        action:
        - find
        - record
        - records
        setScriptAfter:
        - true
  typeInfo:
    type: options
    displayName: Script Name or ID
    name: scriptAfter
    typeOptions:
      loadOptionsMethod: getScripts
    possibleValues: []
- id: scriptAfterParam
  name: Script Parameter
  type: string
  default: ''
  required: false
  description: A parameter for the FileMaker script
  placeholder: Script Parameters
  validation:
    displayOptions:
      show:
        action:
        - find
        - record
        - records
        setScriptAfter:
        - true
  typeInfo:
    type: string
    displayName: Script Parameter
    name: scriptAfterParam
- id: fieldData
  name: fieldData
  type: string
  default: '{}'
  required: false
  description: Additional fields to add.
  placeholder: '{"field1": "value", "field2": "value", ...}'
  validation:
    displayOptions:
      show:
        action:
        - create
        - edit
        - ''
  typeInfo:
    type: string
    displayName: fieldData
    name: fieldData
- id: modId
  name: Mod ID
  type: number
  default: ''
  required: false
  description: The last modification ID. When you use modId, a record is edited only
    when the modId matches.
  validation:
    displayOptions:
      show:
        action:
        - edit
  typeInfo:
    type: number
    displayName: Mod ID
    name: modId
- id: fieldsParametersUi
  name: Fields
  type: fixedCollection
  default: {}
  required: false
  description: Fields to define
  placeholder: Add field
  validation:
    displayOptions:
      show:
        action:
        - create
        - edit
  typeInfo:
    type: fixedCollection
    displayName: Fields
    name: fieldsParametersUi
    typeOptions:
      multipleValues: true
    subProperties:
    - name: fields
      displayName: Fields
      values:
      - displayName: Field Name or ID
        name: name
        type: options
        description: Field Name. Choose from the list, or specify an ID using an <a
          href="https://docs.n8n.io/code/expressions/">expression</a>.
        default: ''
        options: []
        typeOptions:
          loadOptionsMethod: getFields
      - displayName: Value
        name: value
        type: string
        default: ''
- id: script
  name: Script Name or ID
  type: options
  default: ''
  required: true
  description: The name of the FileMaker script to be run. Choose from the list, or
    specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  placeholder: Script Name
  validation:
    required: true
    displayOptions:
      show:
        action:
        - performscript
  typeInfo:
    type: options
    displayName: Script Name or ID
    name: script
    typeOptions:
      loadOptionsMethod: getScripts
    possibleValues: []
- id: scriptParam
  name: Script Parameter
  type: string
  default: ''
  required: false
  description: A parameter for the FileMaker script
  placeholder: Script Parameters
  validation:
    displayOptions:
      show:
        action:
        - performscript
  typeInfo:
    type: string
    displayName: Script Parameter
    name: scriptParam
api_patterns:
  http_methods:
  - GET
  - POST
  - DELETE
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: layout
    text: Layout Name
  - field: recid
    text: Record ID
  - field: offset
    text: '0'
  - field: limit
    text: '100'
  - field: portals
    text: Portals
  - field: queries
    text: Add query
  - field: sortParametersUi
    text: Add Sort Rules
  - field: scriptBefore
    text: Script Name
  - field: scriptBeforeParam
    text: Script Parameters
  - field: scriptSort
    text: Script Name
  - field: scriptSortParam
    text: Script Parameters
  - field: scriptAfter
    text: Script Name
  - field: scriptAfterParam
    text: Script Parameters
  - field: fieldData
    text: '{"field1": "value", "field2": "value", ...}'
  - field: fieldsParametersUi
    text: Add field
  - field: script
    text: Script Name
  - field: scriptParam
    text: Script Parameters
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
  "$id": "https://n8n.io/schemas/nodes/filemaker.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "FileMaker Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "action": {
          "description": "",
          "type": "string",
          "enum": [
            "login",
            "logout",
            "create",
            "delete",
            "duplicate",
            "edit",
            "find",
            "records",
            "record",
            "performscript"
          ],
          "default": "record"
        },
        "layout": {
          "description": "FileMaker Layout Name. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "Layout Name"
          ]
        },
        "recid": {
          "description": "Internal Record ID returned by get (recordid)",
          "type": "number",
          "default": "",
          "examples": [
            "Record ID"
          ]
        },
        "offset": {
          "description": "The record number of the first record in the range of records",
          "type": "number",
          "default": 1,
          "examples": [
            "0"
          ]
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100,
          "examples": [
            "100"
          ]
        },
        "getPortals": {
          "description": "Whether to get portal data as well",
          "type": "boolean",
          "default": false
        },
        "portals": {
          "description": "The portal result set to return. Use the portal object name or portal table name. If this parameter is omitted, the API will return all portal objects and records in the layout. For best performance, pass the portal object name or portal table name. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": [],
          "examples": [
            "Portals"
          ]
        },
        "responseLayout": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "queries": {
          "description": "Search Field. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add query"
          ]
        },
        "setSort": {
          "description": "Whether to sort data",
          "type": "boolean",
          "default": false
        },
        "sortParametersUi": {
          "description": "Sort rules",
          "type": "string",
          "default": {},
          "examples": [
            "Add Sort Rules"
          ]
        },
        "setScriptBefore": {
          "description": "Whether to define a script to be run before the action specified by the API call and after the subsequent sort",
          "type": "boolean",
          "default": false
        },
        "scriptBefore": {
          "description": "The name of the FileMaker script to be run after the action specified by the API call and after the subsequent sort. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "Script Name"
          ]
        },
        "scriptBeforeParam": {
          "description": "A parameter for the FileMaker script",
          "type": "string",
          "default": "",
          "examples": [
            "Script Parameters"
          ]
        },
        "setScriptSort": {
          "description": "Whether to define a script to be run after the action specified by the API call but before the subsequent sort",
          "type": "boolean",
          "default": false
        },
        "scriptSort": {
          "description": "The name of the FileMaker script to be run after the action specified by the API call but before the subsequent sort. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "Script Name"
          ]
        },
        "scriptSortParam": {
          "description": "A parameter for the FileMaker script",
          "type": "string",
          "default": "",
          "examples": [
            "Script Parameters"
          ]
        },
        "setScriptAfter": {
          "description": "Whether to define a script to be run after the action specified by the API call but before the subsequent sort",
          "type": "boolean",
          "default": false
        },
        "scriptAfter": {
          "description": "The name of the FileMaker script to be run after the action specified by the API call and after the subsequent sort. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "Script Name"
          ]
        },
        "scriptAfterParam": {
          "description": "A parameter for the FileMaker script",
          "type": "string",
          "default": "",
          "examples": [
            "Script Parameters"
          ]
        },
        "fieldData": {
          "description": "Additional fields to add.",
          "type": "string",
          "default": "{}",
          "examples": [
            "{\"field1\": \"value\", \"field2\": \"value\", ...}"
          ]
        },
        "modId": {
          "description": "The last modification ID. When you use modId, a record is edited only when the modId matches.",
          "type": "number",
          "default": ""
        },
        "fieldsParametersUi": {
          "description": "Fields to define",
          "type": "string",
          "default": {},
          "examples": [
            "Add field"
          ]
        },
        "script": {
          "description": "The name of the FileMaker script to be run. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "Script Name"
          ]
        },
        "scriptParam": {
          "description": "A parameter for the FileMaker script",
          "type": "string",
          "default": "",
          "examples": [
            "Script Parameters"
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
  },
  "credentials": [
    {
      "name": "fileMaker",
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
