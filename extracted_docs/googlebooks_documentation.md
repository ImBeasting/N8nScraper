---
title: "Node: Google Books"
slug: "node-googlebooks"
version: "['1', '2']"
updated: "2025-11-13"
summary: "Read data from Google Books"
node_type: "regular"
group: "['input', 'output']"
---

# Node: Google Books

**Purpose.** Read data from Google Books
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:googlebooks.svg`
- **Group:** `['input', 'output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleApi**: N/A
- **googleBooksOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleApi` | ✓ | {'show': {'authentication': ['serviceAccount']}} |
| `googleBooksOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Bookshelf Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve a specific bookshelf resource for the specified user |
| Get Many | `getAll` | Get many public bookshelf resource for the specified user |

### Bookshelfvolume Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a volume to a bookshelf |
| Clear | `clear` | Clears all volumes from a bookshelf |
| Get Many | `getAll` | Get many volumes in a specific bookshelf for the specified user |
| Move | `move` | Moves a volume within a bookshelf |
| Remove | `remove` | Removes a volume from a bookshelf |

### Volume Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a volume resource based on ID |
| Get Many | `getAll` | Get many volumes filtered by query |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | bookshelf | ✗ | Resource to operate on |  |

**Resource options:**

* **Bookshelf** (`bookshelf`)
* **Bookshelf Volume** (`bookshelfVolume`)
* **Volume** (`volume`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Retrieve a specific bookshelf resource for the specified user |  |

**Operation options:**

* **Get** (`get`) - Retrieve a specific bookshelf resource for the specified user
* **Get Many** (`getAll`) - Get many public bookshelf resource for the specified user

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| My Library | `myLibrary` | boolean | False | ✓ |  |  |
| User ID | `userId` | string |  | ✓ | ID of user |  |
| Bookshelf ID | `shelfId` | string |  | ✓ | ID of the bookshelf |  |
| Volume ID | `volumeId` | string |  | ✓ | ID of the volume |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| My Library | `myLibrary` | boolean | False | ✓ |  |  |
| Search Query | `searchQuery` | string |  | ✓ | Full-text search query string |  |
| User ID | `userId` | string |  | ✓ | ID of user |  |
| Bookshelf ID | `shelfId` | string |  | ✓ | ID of the bookshelf |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 40 | ✗ | Max number of results to return | min:1, max:40 |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bookshelf ID | `shelfId` | string |  | ✓ | ID of the bookshelf |  |
| Volume ID | `volumeId` | string |  | ✓ | ID of the volume |  |

### Clear parameters (`clear`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bookshelf ID | `shelfId` | string |  | ✓ | ID of the bookshelf |  |

### Move parameters (`move`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bookshelf ID | `shelfId` | string |  | ✓ | ID of the bookshelf |  |
| Volume ID | `volumeId` | string |  | ✓ | ID of the volume |  |
| Volume Position | `volumePosition` | string |  | ✓ | Position on shelf to move the item (0 puts the item before the current first item, 1 puts it between the first and the second and so on) |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bookshelf ID | `shelfId` | string |  | ✓ | ID of the bookshelf |  |
| Volume ID | `volumeId` | string |  | ✓ | ID of the volume |  |

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
* Categories: Miscellaneous

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleBooks
displayName: Google Books
description: Read data from Google Books
version:
- '1'
- '2'
nodeType: regular
group:
- input
- output
credentials:
- name: googleApi
  required: true
- name: googleBooksOAuth2Api
  required: true
operations:
- id: get
  name: Get
  description: Retrieve a specific bookshelf resource for the specified user
  params:
  - id: myLibrary
    name: My Library
    type: boolean
    default: false
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - get
          - getAll
          resource:
          - bookshelf
          - bookshelfVolume
    typeInfo: &id002
      type: boolean
      displayName: My Library
      name: myLibrary
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: ID of user
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - get
          - getAll
          resource:
          - bookshelf
          - bookshelfVolume
        hide:
          myLibrary:
          - true
    typeInfo: &id004
      type: string
      displayName: User ID
      name: userId
  - id: shelfId
    name: Bookshelf ID
    type: string
    default: ''
    required: true
    description: ID of the bookshelf
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - bookshelfVolume
    typeInfo: &id006
      type: string
      displayName: Bookshelf ID
      name: shelfId
  - id: volumeId
    name: Volume ID
    type: string
    default: ''
    required: true
    description: ID of the volume
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - add
          - move
          - remove
          - get
          resource:
          - bookshelfVolume
          - volume
    typeInfo: &id008
      type: string
      displayName: Volume ID
      name: volumeId
- id: getAll
  name: Get Many
  description: Get many public bookshelf resource for the specified user
  params:
  - id: myLibrary
    name: My Library
    type: boolean
    default: false
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: searchQuery
    name: Search Query
    type: string
    default: ''
    required: true
    description: Full-text search query string
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - volume
    typeInfo:
      type: string
      displayName: Search Query
      name: searchQuery
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: ID of user
    validation: *id003
    typeInfo: *id004
  - id: shelfId
    name: Bookshelf ID
    type: string
    default: ''
    required: true
    description: ID of the bookshelf
    validation: *id005
    typeInfo: *id006
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
    default: 40
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
        maxValue: 40
- id: add
  name: Add
  description: Add a volume to a bookshelf
  params:
  - id: shelfId
    name: Bookshelf ID
    type: string
    default: ''
    required: true
    description: ID of the bookshelf
    validation: *id005
    typeInfo: *id006
  - id: volumeId
    name: Volume ID
    type: string
    default: ''
    required: true
    description: ID of the volume
    validation: *id007
    typeInfo: *id008
- id: clear
  name: Clear
  description: Clears all volumes from a bookshelf
  params:
  - id: shelfId
    name: Bookshelf ID
    type: string
    default: ''
    required: true
    description: ID of the bookshelf
    validation: *id005
    typeInfo: *id006
- id: move
  name: Move
  description: Moves a volume within a bookshelf
  params:
  - id: shelfId
    name: Bookshelf ID
    type: string
    default: ''
    required: true
    description: ID of the bookshelf
    validation: *id005
    typeInfo: *id006
  - id: volumeId
    name: Volume ID
    type: string
    default: ''
    required: true
    description: ID of the volume
    validation: *id007
    typeInfo: *id008
  - id: volumePosition
    name: Volume Position
    type: string
    default: ''
    required: true
    description: Position on shelf to move the item (0 puts the item before the current
      first item, 1 puts it between the first and the second and so on)
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - move
          resource:
          - bookshelfVolume
    typeInfo:
      type: string
      displayName: Volume Position
      name: volumePosition
- id: remove
  name: Remove
  description: Removes a volume from a bookshelf
  params:
  - id: shelfId
    name: Bookshelf ID
    type: string
    default: ''
    required: true
    description: ID of the bookshelf
    validation: *id005
    typeInfo: *id006
  - id: volumeId
    name: Volume ID
    type: string
    default: ''
    required: true
    description: ID of the volume
    validation: *id007
    typeInfo: *id008
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
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
  "$id": "https://n8n.io/schemas/nodes/googleBooks.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Books Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll",
        "add",
        "clear",
        "move",
        "remove"
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
            "serviceAccount",
            "oAuth2"
          ],
          "default": "serviceAccount"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "bookshelf",
            "bookshelfVolume",
            "volume"
          ],
          "default": "bookshelf"
        },
        "operation": {
          "description": "Get a volume resource based on ID",
          "type": "string",
          "enum": [
            "get",
            "getAll"
          ],
          "default": "get"
        },
        "myLibrary": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "searchQuery": {
          "description": "Full-text search query string",
          "type": "string",
          "default": ""
        },
        "userId": {
          "description": "ID of user",
          "type": "string",
          "default": ""
        },
        "shelfId": {
          "description": "ID of the bookshelf",
          "type": "string",
          "default": ""
        },
        "volumeId": {
          "description": "ID of the volume",
          "type": "string",
          "default": ""
        },
        "volumePosition": {
          "description": "Position on shelf to move the item (0 puts the item before the current first item, 1 puts it between the first and the second and so on)",
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
          "default": 40
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
      "2"
    ]
  },
  "credentials": [
    {
      "name": "googleApi",
      "required": true
    },
    {
      "name": "googleBooksOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
