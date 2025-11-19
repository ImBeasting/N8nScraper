---
title: "Node: SeaTable Trigger"
slug: "node-seatable-trigger"
version: "2"
updated: "2025-11-13"
summary: "Starts the workflow when SeaTable events occur"
node_type: "trigger"
group: "['output']"
---

# Node: SeaTable Trigger

**Purpose.** Starts the workflow when SeaTable events occur
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:seaTable.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **seaTableApi**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice**: Hint: Link, files, images or digital signatures have to be added separately.
- **notice**: In this mode, make sure the incoming data fields are named the same as the columns in SeaTable. (Use an "Edit Fields" node before this node to change them if required.)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `seaTableApi` | ✓ | - |

---

## API Patterns

**Common Endpoints:**
- `{resolveBaseUri(ctx)}/api/v2.1/dtable/app-access-token/`

---

## Operations

### Link Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Create a link between two rows in a link column |
| List | `list` | List all links of a specific row |
| Remove | `remove` | Remove a link between two rows from a link column |

### Row Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new row |
| Delete | `remove` | Delete a row |
| Get | `get` | Get the content of a row |
| Get Many | `list` | Get many rows from a table or a table view |
| Lock | `lock` | Lock a row to prevent further changes |
| Search | `search` | Search one or multiple rows |
| Unlock | `unlock` | Remove the lock from a row |
| Update | `update` | Update the content of a row |

### Base Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Snapshot | `snapshot` | Create a snapshot of the base |
| Metadata | `metadata` | Get the complete metadata of the base |
| Collaborator | `collaborator` | Get the username from the email or name of a collaborator |

### Asset Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Public URL | `getPublicURL` | Get the public URL from asset path |
| Upload | `upload` | Add a file/image to an existing row |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | row | ✗ | Resource to operate on |  |

**Resource options:**

* **Row** (`row`)
* **Base** (`base`)
* **Link** (`link`)
* **Asset** (`asset`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | add | ✗ | Create a link between two rows in a link column |  |

**Operation options:**

* **Add** (`add`) - Create a link between two rows in a link column
* **List** (`list`) - List all links of a specific row
* **Remove** (`remove`) - Remove a link between two rows from a link column

---

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Columns to Send | `columnsUi` | fixedCollection |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Column |  |

<details>
<summary><strong>Columns to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Column | `columnValues` |  |  |  |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["event"]}}`
- `={{$parameter["resource"] + ": " + $parameter["operation"]}}`

---

## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |

---

## Notes & Caveats

* This node is part of n8n-nodes-base

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: SeaTable Trigger
displayName: SeaTable Trigger
description: Starts the workflow when SeaTable events occur
version: '2'
nodeType: trigger
group:
- output
credentials:
- name: seaTableApi
  required: true
operations:
- id: add
  name: Add
  description: Create a link between two rows in a link column
- id: list
  name: List
  description: List all links of a specific row
- id: remove
  name: Remove
  description: Remove a link between two rows from a link column
- id: create
  name: Create
  description: Create a new row
- id: get
  name: Get
  description: Get the content of a row
- id: lock
  name: Lock
  description: Lock a row to prevent further changes
- id: search
  name: Search
  description: Search one or multiple rows
- id: unlock
  name: Unlock
  description: Remove the lock from a row
- id: update
  name: Update
  description: Update the content of a row
  params:
  - id: inputsToIgnore
    name: Inputs to Ignore
    type: string
    default: ''
    required: false
    description: List of input properties to avoid sending, separated by commas. Leave
      empty to send all properties.
    placeholder: Enter properties...
    validation:
      displayOptions:
        show: {}
    typeInfo:
      type: string
      displayName: Inputs to Ignore
      name: inputsToIgnore
  - id: columnsUi
    name: Columns to Send
    type: fixedCollection
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Column
    validation:
      displayOptions:
        show: {}
    typeInfo:
      type: fixedCollection
      displayName: Columns to Send
      name: columnsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: columnValues
        displayName: Column
        values:
        - displayName: Column Name or ID
          name: columnName
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getTableUpdateAbleColumns
        - displayName: Column Value
          name: columnValue
          type: string
          default: ''
- id: snapshot
  name: Snapshot
  description: Create a snapshot of the base
- id: metadata
  name: Metadata
  description: Get the complete metadata of the base
- id: collaborator
  name: Collaborator
  description: Get the username from the email or name of a collaborator
- id: getPublicURL
  name: Public URL
  description: Get the public URL from asset path
- id: upload
  name: Upload
  description: Add a file/image to an existing row
common_expressions:
- ={{$parameter["event"]}}
- '={{$parameter["resource"] + ": " + $parameter["operation"]}}'
api_patterns:
  http_methods: []
  endpoints:
  - '{resolveBaseUri(ctx)}/api/v2.1/dtable/app-access-token/'
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: notice
    text: 'Hint: Link, files, images or digital signatures have to be added separately.'
    conditions: null
  - name: notice
    text: In this mode, make sure the incoming data fields are named the same as the
      columns in SeaTable. (Use an "Edit Fields" node before this node to change them
      if required.)
    conditions:
      show: {}
  tooltips: []
  placeholders:
  - field: tableName
    text: Select a table
  - field: options
    text: Add Option
  - field: inputsToIgnore
    text: Enter properties...
  - field: columnsUi
    text: Add Column
  - field: tableName
    text: Select a table
  - field: inputsToIgnore
    text: Enter properties...
  - field: columnsUi
    text: Add Column
  - field: searchString
    text: Enter the name or the email or the collaborator
  - field: assetPath
    text: /images/2023-09/logo.png
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/SeaTable Trigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SeaTable Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "add",
        "list",
        "remove",
        "create",
        "get",
        "lock",
        "search",
        "unlock",
        "update",
        "snapshot",
        "metadata",
        "collaborator",
        "getPublicURL",
        "upload"
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
            "row",
            "base",
            "link",
            "asset"
          ],
          "default": "row"
        },
        "tableName": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": "",
          "examples": [
            "Select a table"
          ]
        },
        "linkColumn": {
          "description": "Choose from the list of specify the Link Column by using an expression. You have to provide it in the way \"column_name:::link_id:::other_table_id:::column_key\".",
          "type": "string",
          "default": ""
        },
        "rowId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "linkColumnSourceId": {
          "description": "Provide the row ID of table you selected",
          "type": "string",
          "default": ""
        },
        "linkColumnTargetId": {
          "description": "Provide the row ID of table you want to link",
          "type": "string",
          "default": ""
        },
        "operation": {
          "description": "Get the public URL from asset path",
          "type": "string",
          "enum": [
            "getPublicURL",
            "upload"
          ],
          "default": "upload"
        },
        "viewName": {
          "description": "The name of SeaTable view to access, or specify by using an expression. Provide it in the way \"col.name:::col.type\".",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "string",
          "default": {},
          "examples": [
            "Add Option"
          ]
        },
        "fieldsToSend": {
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
        "columnsUi": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": "",
          "examples": [
            "Add Column"
          ]
        },
        "searchColumn": {
          "description": "Select the column to be searched. Not all column types are supported for search. Choose from the list, or specify a name using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "searchTerm": {
          "description": "What to look for?",
          "type": "string",
          "default": ""
        },
        "apply_default": {
          "description": "Whether to use the column default values to populate new rows during creation (only available for normal backend)",
          "type": "boolean",
          "default": false
        },
        "bigdata": {
          "description": "Whether write to Big Data backend (true) or not (false). True requires the activation of the Big Data backend in the base.",
          "type": "boolean",
          "default": false
        },
        "searchString": {
          "description": "SeaTable identifies users with a unique username like 244b43hr6fy54bb4afa2c2cb7369d244@auth.local. Get this username from an email or the name of a collaborator.",
          "type": "string",
          "default": "",
          "examples": [
            "Enter the name or the email or the collaborator"
          ]
        },
        "assetPath": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "/images/2023-09/logo.png"
          ]
        },
        "uploadColumn": {
          "description": "Choose from the list, or specify the name using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "dataPropertyName": {
          "description": "Name of the binary property which contains the data for the file to be written",
          "type": "string",
          "default": "data"
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
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
    "version": "2"
  },
  "credentials": [
    {
      "name": "seaTableApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 2 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
