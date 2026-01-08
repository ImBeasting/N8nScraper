---
title: "Node: NocoDB"
slug: "node-nocodb"
version: "['1', '2', '3']"
updated: "2026-01-08"
summary: "Read, update, write and delete data from NocoDB"
node_type: "regular"
group: "['input']"
---

# Node: NocoDB

**Purpose.** Read, update, write and delete data from NocoDB
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:nocodb.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **nocoDb**: N/A
- **nocoDbApiToken**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **info** when dataToSend=['autoMapInputData']: In this mode, make sure the incoming data fields are named the same as the columns in NocoDB. (Use an 'Edit Fields' node before this node to change them if required.)
- **info** when operation=['update'], version=[3]: This operation requires the primary key to be included for each row.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `nocoDb` | ✓ | {'show': {'authentication': ['nocoDb']}} |
| `nocoDbApiToken` | ✓ | {'show': {'authentication': ['nocoDbApiToken']}} |

---

## Operations

### Row Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a row |
| Delete | `delete` | Delete a row |
| Get | `get` | Retrieve a row |
| Get Many | `getAll` | Retrieve many rows |
| Update | `update` | Update a row |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | row | ✗ | Resource to operate on |  |

**Resource options:**

* **Row** (`row`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Create a row |  |

**Operation options:**

* **Create** (`create`) - Create a row
* **Delete** (`delete`) - Delete a row
* **Get** (`get`) - Retrieve a row
* **Get Many** (`getAll`) - Retrieve many rows
* **Update** (`update`) - Update a row

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Data to Send | `dataToSend` | options | defineBelow | ✗ | Use when node input properties match destination column names |  |

**Data to Send options:**

* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names
* **Define Below for Each Column** (`defineBelow`) - Set the value for each destination column

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Fields to Send | `fieldsUi` | fixedCollection | {} | ✗ | Whether the field data to set is binary and should be taken from a binary property | e.g. Add Field |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `fieldValues` |  |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Primary Key Type | `primaryKey` | options | id | ✗ | Default, added when table was created from UI by those options: Create new table / Import from Excel / Import from CSV |  |

**Primary Key Type options:**

* **Default** (`id`) - Default, added when table was created from UI by those options: Create new table / Import from Excel / Import from CSV
* **Imported From Airtable** (`ncRecordId`) - Select if table was imported from Airtable
* **Custom** (`custom`) - When connecting to existing external database as existing primary key field is retained as is, enter the name of the primary key field below

| Primary Key Type | `primaryKey` | options | id | ✗ | Default, added when table was created from UI by those options: Create new table / Import from Excel / Import from CSV |  |

**Primary Key Type options:**

* **Default** (`id`) - Default, added when table was created from UI by those options: Create new table / Import from Excel / Import from CSV
* **Imported From Airtable** (`ncRecordId`) - Select if table was imported from Airtable
* **Custom** (`custom`) - When connecting to existing external database as existing primary key field is retained as is, enter the name of the primary key field below

| Field Name | `customPrimaryKey` | string |  | ✗ |  |  |
| Field Name | `customPrimaryKey` | string |  | ✗ |  |  |
| Row ID Value | `id` | string |  | ✓ | The value of the ID field |  |
| Row ID Value | `id` | string |  | ✓ | The value of the ID field |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Row ID Value | `id` | string |  | ✓ | The value of the ID field |  |
| Row ID Value | `id` | string |  | ✓ | The value of the ID field |  |
| Download Attachments | `downloadAttachments` | boolean | False | ✗ | Whether the attachment fields define in 'Download Fields' will be downloaded |  |
| Download Fields | `downloadFieldNames` | string |  | ✓ | Name of the fields of type 'attachment' that should be downloaded. Multiple ones can be defined separated by comma. Case sensitive. |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Download Attachments | `downloadAttachments` | boolean | False | ✗ | Whether the attachment fields define in 'Download Fields' will be downloaded |  |
| Download Fields | `downloadFieldNames` | string |  | ✓ | Name of the fields of type 'attachment' that should be downloaded. Multiple ones can be defined separated by comma. Case sensitive. |  |
| Options | `options` | collection | {} | ✗ | The select fields of the returned rows | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| View ID | `viewId` | string |  | The select fields of the returned rows |
| Fields | `fields` | string | [] | The select fields of the returned rows |
| Sort | `sort` | fixedCollection | {} | The sorting rules for the returned rows |
| Filter By Formula | `where` | string |  | A formula used to filter rows |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Primary Key Type | `primaryKey` | options | id | ✗ | Default, added when table was created from UI by those options: Create new table / Import from Excel / Import from CSV |  |

**Primary Key Type options:**

* **Default** (`id`) - Default, added when table was created from UI by those options: Create new table / Import from Excel / Import from CSV
* **Imported From Airtable** (`ncRecordId`) - Select if table was imported from Airtable
* **Custom** (`custom`) - When connecting to existing external database as existing primary key field is retained as is, enter the name of the primary key field below

| Field Name | `customPrimaryKey` | string |  | ✗ |  |  |
| Row ID Value | `id` | string |  | ✓ | The value of the ID field |  |
| Data to Send | `dataToSend` | options | defineBelow | ✗ | Use when node input properties match destination column names |  |

**Data to Send options:**

* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names
* **Define Below for Each Column** (`defineBelow`) - Set the value for each destination column

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Fields to Send | `fieldsUi` | fixedCollection | {} | ✗ | Whether the field data to set is binary and should be taken from a binary property | e.g. Add Field |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `fieldValues` |  |  |  |

</details>


---

## Load Options Methods

- `getWorkspaces`

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
node: nocoDb
displayName: NocoDB
description: Read, update, write and delete data from NocoDB
version:
- '1'
- '2'
- '3'
nodeType: regular
group:
- input
credentials:
- name: nocoDb
  required: true
- name: nocoDbApiToken
  required: true
operations:
- id: create
  name: Create
  description: Create a row
  params:
  - id: dataToSend
    name: Data to Send
    type: options
    default: defineBelow
    required: false
    description: Use when node input properties match destination column names
    validation: &id011
      displayOptions:
        show:
          operation:
          - create
          - update
    typeInfo: &id012
      type: options
      displayName: Data to Send
      name: dataToSend
      possibleValues:
      - value: autoMapInputData
        name: Auto-Map Input Data to Columns
        description: Use when node input properties match destination column names
      - value: defineBelow
        name: Define Below for Each Column
        description: Set the value for each destination column
  - id: inputsToIgnore
    name: Inputs to Ignore
    type: string
    default: ''
    required: false
    description: List of input properties to avoid sending, separated by commas. Leave
      empty to send all properties.
    placeholder: Enter properties...
    validation: &id013
      displayOptions:
        show:
          operation:
          - create
          - update
          dataToSend:
          - autoMapInputData
    typeInfo: &id014
      type: string
      displayName: Inputs to Ignore
      name: inputsToIgnore
  - id: fieldsUi
    name: Fields to Send
    type: fixedCollection
    default: &id015 {}
    required: false
    description: Whether the field data to set is binary and should be taken from
      a binary property
    placeholder: Add Field
    validation: &id016
      displayOptions:
        show:
          operation:
          - create
          - update
          dataToSend:
          - defineBelow
    typeInfo: &id017
      type: fixedCollection
      displayName: Fields to Send
      name: fieldsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: fieldValues
        displayName: Field
        values:
        - displayName: Field Name
          name: fieldName
          type: string
          default: ''
        - displayName: Is Binary File
          name: binaryData
          type: boolean
          description: Whether the field data to set is binary and should be taken
            from a binary property
          default: false
        - displayName: Field Value
          name: fieldValue
          type: string
          default: ''
          displayOptions:
            show:
              binaryData:
              - false
        - displayName: Take Input From Field
          name: binaryProperty
          type: string
          description: The field containing the binary file data to be uploaded
          default: ''
          displayOptions:
            show:
              binaryData:
              - true
- id: delete
  name: Delete
  description: Delete a row
  params:
  - id: primaryKey
    name: Primary Key Type
    type: options
    default: id
    required: false
    description: 'Default, added when table was created from UI by those options:
      Create new table / Import from Excel / Import from CSV'
    validation: &id001
      displayOptions:
        show:
          version:
          - 3
          operation:
          - delete
    typeInfo: &id002
      type: options
      displayName: Primary Key Type
      name: primaryKey
      possibleValues:
      - value: id
        name: Default
        description: 'Default, added when table was created from UI by those options:
          Create new table / Import from Excel / Import from CSV'
      - value: ncRecordId
        name: Imported From Airtable
        description: Select if table was imported from Airtable
      - value: custom
        name: Custom
        description: When connecting to existing external database as existing primary
          key field is retained as is, enter the name of the primary key field below
  - id: primaryKey
    name: Primary Key Type
    type: options
    default: id
    required: false
    description: 'Default, added when table was created from UI by those options:
      Create new table / Import from Excel / Import from CSV'
    validation: *id001
    typeInfo: *id002
  - id: customPrimaryKey
    name: Field Name
    type: string
    default: ''
    required: false
    description: ''
    validation: &id003
      displayOptions:
        show:
          version:
          - 3
          operation:
          - delete
          primaryKey:
          - custom
    typeInfo: &id004
      type: string
      displayName: Field Name
      name: customPrimaryKey
  - id: customPrimaryKey
    name: Field Name
    type: string
    default: ''
    required: false
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Row ID Value
    type: string
    default: ''
    required: true
    description: The value of the ID field
    validation: &id005
      required: true
      displayOptions:
        show:
          version:
          - 3
          operation:
          - delete
          - get
    typeInfo: &id006
      type: string
      displayName: Row ID Value
      name: id
  - id: id
    name: Row ID Value
    type: string
    default: ''
    required: true
    description: The value of the ID field
    validation: *id005
    typeInfo: *id006
- id: get
  name: Get
  description: Retrieve a row
  params:
  - id: id
    name: Row ID Value
    type: string
    default: ''
    required: true
    description: The value of the ID field
    validation: *id005
    typeInfo: *id006
  - id: id
    name: Row ID Value
    type: string
    default: ''
    required: true
    description: The value of the ID field
    validation: *id005
    typeInfo: *id006
  - id: downloadAttachments
    name: Download Attachments
    type: boolean
    default: false
    required: false
    description: Whether the attachment fields define in 'Download Fields' will be
      downloaded
    validation: &id007
      displayOptions:
        show:
          operation:
          - get
    typeInfo: &id008
      type: boolean
      displayName: Download Attachments
      name: downloadAttachments
  - id: downloadFieldNames
    name: Download Fields
    type: string
    default: ''
    required: true
    description: Name of the fields of type 'attachment' that should be downloaded.
      Multiple ones can be defined separated by comma. Case sensitive.
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - get
          downloadAttachments:
          - true
    typeInfo: &id010
      type: string
      displayName: Download Fields
      name: downloadFieldNames
- id: getAll
  name: Get Many
  description: Retrieve many rows
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: downloadAttachments
    name: Download Attachments
    type: boolean
    default: false
    required: false
    description: Whether the attachment fields define in 'Download Fields' will be
      downloaded
    validation: *id007
    typeInfo: *id008
  - id: downloadFieldNames
    name: Download Fields
    type: string
    default: ''
    required: true
    description: Name of the fields of type 'attachment' that should be downloaded.
      Multiple ones can be defined separated by comma. Case sensitive.
    validation: *id009
    typeInfo: *id010
- id: update
  name: Update
  description: Update a row
  params:
  - id: primaryKey
    name: Primary Key Type
    type: options
    default: id
    required: false
    description: 'Default, added when table was created from UI by those options:
      Create new table / Import from Excel / Import from CSV'
    validation: *id001
    typeInfo: *id002
  - id: customPrimaryKey
    name: Field Name
    type: string
    default: ''
    required: false
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Row ID Value
    type: string
    default: ''
    required: true
    description: The value of the ID field
    validation: *id005
    typeInfo: *id006
  - id: dataToSend
    name: Data to Send
    type: options
    default: defineBelow
    required: false
    description: Use when node input properties match destination column names
    validation: *id011
    typeInfo: *id012
  - id: inputsToIgnore
    name: Inputs to Ignore
    type: string
    default: ''
    required: false
    description: List of input properties to avoid sending, separated by commas. Leave
      empty to send all properties.
    placeholder: Enter properties...
    validation: *id013
    typeInfo: *id014
  - id: fieldsUi
    name: Fields to Send
    type: fixedCollection
    default: *id015
    required: false
    description: Whether the field data to set is binary and should be taken from
      a binary property
    placeholder: Add Field
    validation: *id016
    typeInfo: *id017
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: info
    text: In this mode, make sure the incoming data fields are named the same as the
      columns in NocoDB. (Use an 'Edit Fields' node before this node to change them
      if required.)
    conditions:
      show:
        dataToSend:
        - autoMapInputData
  - name: info
    text: This operation requires the primary key to be included for each row.
    conditions:
      show:
        operation:
        - update
        version:
        - 3
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  - field: inputsToIgnore
    text: Enter properties...
  - field: fieldsUi
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/nocoDb.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "NocoDB Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "get",
        "getAll",
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
            "nocoDbApiToken",
            "nocoDb"
          ],
          "default": "nocoDb"
        },
        "version": {
          "description": "",
          "type": "string",
          "enum": [
            "Before v0.90.0",
            "v0.90.0 Onwards",
            "v0.200.0 Onwards"
          ],
          "default": 1
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "row"
          ],
          "default": "row"
        },
        "operation": {
          "description": "Create a row",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "get"
        },
        "workspaceId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": "none"
        },
        "projectId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "table": {
          "description": "The name of the table",
          "type": "string",
          "default": ""
        },
        "primaryKey": {
          "description": "Default, added when table was created from UI by those options: Create new table / Import from Excel / Import from CSV",
          "type": "string",
          "enum": [
            "id",
            "ncRecordId",
            "custom"
          ],
          "default": "id"
        },
        "customPrimaryKey": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "id": {
          "description": "The value of the ID field",
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
        "downloadAttachments": {
          "description": "Whether the attachment fields define in 'Download Fields' will be downloaded",
          "type": "boolean",
          "default": false
        },
        "downloadFieldNames": {
          "description": "Name of the fields of type 'attachment' that should be downloaded. Multiple ones can be defined separated by comma. Case sensitive.",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "The select fields of the returned rows",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "dataToSend": {
          "description": "Use when node input properties match destination column names",
          "type": "string",
          "enum": [
            "autoMapInputData",
            "defineBelow"
          ],
          "default": "defineBelow"
        },
        "inputsToIgnore": {
          "description": "List of input properties to avoid sending, separated by commas. Leave empty to send all properties.",
          "type": "string",
          "default": "",
          "examples": [
            "Enter properties..."
          ]
        },
        "fieldsUi": {
          "description": "Whether the field data to set is binary and should be taken from a binary property",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
      "1",
      "2",
      "3"
    ]
  },
  "credentials": [
    {
      "name": "nocoDb",
      "required": true
    },
    {
      "name": "nocoDbApiToken",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2', '3'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
