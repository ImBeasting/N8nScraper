---
title: "Node: Adalo"
slug: "node-adalo"
version: "1"
updated: "2026-01-08"
summary: "Consume Adalo API"
node_type: "regular"
group: "['transform']"
---

# Node: Adalo

**Purpose.** Consume Adalo API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["collectionId"]}}


---

## Node Details

- **Icon:** `file:adalo.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **adaloApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `adaloApi` | ✓ | - |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | collection | ✗ | Resource to operate on |  |

**Resource options:**

* **Collection** (`collection`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | collection | ✗ |  |  |

**Resource options:**

* **Collection** (`collection`)

| Operation | `operation` | options | getAll | ✗ | Create a row |  |
| Collection ID | `collectionId` | string |  | ✓ | Open your Adalo application and click on the three buttons beside the collection name, then select API Documentation | e.g. You can find information about app's collections on https://app.adalo.com/apps/<strong>your-app-id</strong>/api-docs |  |
| Row ID | `rowId` | string |  | ✓ |  |  |
| Data to Send | `dataToSend` | options | defineBelow | ✗ | Use when node input properties match destination column names |  |

**Data to Send options:**

* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names
* **Define Below for Each Column** (`defineBelow`) - Set the value for each destination column

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Fields to Send | `fieldsUi` | fixedCollection | {} | ✗ | Field must be defined in the collection, otherwise it will be ignored. If field defined in the collection is not set here, it will be set to null. | e.g. Add Field |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `fieldValues` |  |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["limit"]}}`
- `={{$parameter["operation"] + ": " + $parameter["collectionId"]}}`
- `={{ { "success": true } }}`
- `={{$parameter["returnAll"]}}`

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
node: adalo
displayName: Adalo
description: Consume Adalo API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: adaloApi
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: collection
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: collection
      name: Collection
      description: ''
- id: operation
  name: Operation
  type: options
  default: getAll
  required: false
  description: Create a row
  typeInfo:
    type: options
    displayName: Operation
    name: operation
    possibleValues: []
- id: collectionId
  name: Collection ID
  type: string
  default: ''
  required: true
  description: Open your Adalo application and click on the three buttons beside the
    collection name, then select API Documentation
  hint: You can find information about app's collections on https://app.adalo.com/apps/<strong>your-app-id</strong>/api-docs
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - collection
  typeInfo:
    type: string
    displayName: Collection ID
    name: collectionId
- id: rowId
  name: Row ID
  type: string
  default: ''
  required: true
  description: ''
  validation:
    required: true
    displayOptions:
      show:
        operation:
        - get
        - delete
        - update
        resource:
        - collection
  typeInfo:
    type: string
    displayName: Row ID
    name: rowId
- id: dataToSend
  name: Data to Send
  type: options
  default: defineBelow
  required: false
  description: Use when node input properties match destination column names
  validation:
    displayOptions:
      show:
        operation:
        - create
        - update
        resource:
        - collection
  typeInfo:
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
  validation:
    displayOptions:
      show:
        operation:
        - create
        - update
        dataToSend:
        - autoMapInputData
        resource:
        - collection
  typeInfo:
    type: string
    displayName: Inputs to Ignore
    name: inputsToIgnore
- id: fieldsUi
  name: Fields to Send
  type: fixedCollection
  default: {}
  required: false
  description: Field must be defined in the collection, otherwise it will be ignored.
    If field defined in the collection is not set here, it will be set to null.
  placeholder: Add Field
  validation:
    displayOptions:
      show:
        operation:
        - create
        - update
        dataToSend:
        - defineBelow
        resource:
        - collection
  typeInfo:
    type: fixedCollection
    displayName: Fields to Send
    name: fieldsUi
    typeOptions:
      multipleValues: true
    subProperties:
    - name: fieldValues
      displayName: Field
      values:
      - displayName: Field ID
        name: fieldId
        type: string
        default: ''
      - displayName: Field Value
        name: fieldValue
        type: string
        default: ''
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
        resource:
        - collection
  typeInfo:
    type: boolean
    displayName: Return All
    name: returnAll
- id: limit
  name: Limit
  type: number
  default: 100
  required: false
  description: Max number of results to return
  validation:
    displayOptions:
      show:
        operation:
        - getAll
        resource:
        - collection
        returnAll:
        - false
  typeInfo:
    type: number
    displayName: Limit
    name: limit
    typeOptions:
      minValue: 1
      maxValue: 100
common_expressions:
- ={{$parameter["limit"]}}
- '={{$parameter["operation"] + ": " + $parameter["collectionId"]}}'
- '={{ { "success": true } }}'
- ={{$parameter["returnAll"]}}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: inputsToIgnore
    text: Enter properties...
  - field: fieldsUi
    text: Add Field
  hints:
  - field: collectionId
    text: You can find information about app's collections on https://app.adalo.com/apps/<strong>your-app-id</strong>/api-docs
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
  "$id": "https://n8n.io/schemas/nodes/adalo.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Adalo Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "collection"
          ],
          "default": "collection"
        },
        "operation": {
          "description": "Create a row",
          "type": "string",
          "default": "getAll"
        },
        "collectionId": {
          "description": "Open your Adalo application and click on the three buttons beside the collection name, then select API Documentation",
          "type": "string",
          "default": ""
        },
        "rowId": {
          "description": "",
          "type": "string",
          "default": ""
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
          "description": "Field must be defined in the collection, otherwise it will be ignored. If field defined in the collection is not set here, it will be set to null.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
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
      "name": "adaloApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
