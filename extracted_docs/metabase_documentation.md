---
title: "Node: Metabase"
slug: "node-metabase"
version: "1"
updated: "2025-11-13"
summary: "Use the Metabase API"
node_type: "regular"
group: "['transform']"
---

# Node: Metabase

**Purpose.** Use the Metabase API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:metabase.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **metabaseApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `metabaseApi` | ✓ | - |

---

## Operations

### Questions Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a specific question |
| Get Many | `getAll` | Get many questions |

### Metrics Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a specific metric |
| Get Many | `getAll` | Get many metrics |

### Databases Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `addNewDatasource` | Add a new datasource to the metabase instance |

### Alerts Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get specific alert |
| Get Many | `getAll` | Get many alerts |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | questions | ✗ | Resource to operate on |  |

**Resource options:**

* **Alert** (`alerts`)
* **Database** (`databases`)
* **Metric** (`metrics`)
* **Question** (`questions`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Get a specific question |  |

**Operation options:**

* **Get** (`get`) - Get a specific question
* **Get Many** (`getAll`) - Get many questions

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Question ID | `questionId` | string |  | ✓ | e.g. 0 |  |
| Metric ID | `metricId` | string |  | ✓ | e.g. 0 |  |
| Alert ID | `alertId` | string |  | ✓ | e.g. 0 |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

### Add parameters (`addNewDatasource`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Engine | `engine` | options | postgres | ✓ | e.g. PostgreSQL |  |

**Engine options:**

* **H2** (`h2`)
* **MongoDB** (`mongo`)
* **Mysql** (`mysql`)
* **PostgreSQL** (`postgres`)
* **Redshift** (`redshift`)
* **Sqlite** (`sqlite`)

| Host | `host` | string |  | ✓ | e.g. localhost:5432 |  |
| Name | `name` | string |  | ✓ | e.g. Database 1 |  |
| Port | `port` | number | 5432 | ✓ | e.g. 5432 |  |
| User | `user` | string |  | ✓ | e.g. Admin |  |
| Password | `password` | string |  | ✓ | e.g. password |  |
| Database Name | `dbName` | string |  | ✗ | e.g. Users |  |
| File Path | `filePath` | string |  | ✓ | e.g. file:/Users/admin/Desktop/Users |  |
| Full Sync | `fullSync` | boolean | True | ✓ |  |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$credentials.url.replace(new RegExp("/$"), "")}}`
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
* Categories: Development, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: metabase
displayName: Metabase
description: Use the Metabase API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: metabaseApi
  required: true
operations:
- id: get
  name: Get
  description: Get a specific question
  params:
  - id: questionId
    name: Question ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: '0'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - questions
          operation:
          - get
          - resultData
    typeInfo:
      type: string
      displayName: Question ID
      name: questionId
  - id: metricId
    name: Metric ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: '0'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - metrics
          operation:
          - get
    typeInfo:
      type: string
      displayName: Metric ID
      name: metricId
  - id: alertId
    name: Alert ID
    type: string
    default: ''
    required: true
    description: ''
    placeholder: '0'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - alerts
          operation:
          - get
    typeInfo:
      type: string
      displayName: Alert ID
      name: alertId
- id: getAll
  name: Get Many
  description: Get many questions
  params:
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation:
      displayOptions:
        show:
          resource:
          - databases
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Simplify
      name: simple
- id: addNewDatasource
  name: Add
  description: Add a new datasource to the metabase instance
  params:
  - id: engine
    name: Engine
    type: options
    default: postgres
    required: true
    description: ''
    placeholder: PostgreSQL
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - databases
          operation:
          - addNewDatasource
    typeInfo:
      type: options
      displayName: Engine
      name: engine
      possibleValues:
      - value: h2
        name: H2
        description: ''
      - value: mongo
        name: MongoDB
        description: ''
      - value: mysql
        name: Mysql
        description: ''
      - value: postgres
        name: PostgreSQL
        description: ''
      - value: redshift
        name: Redshift
        description: ''
      - value: sqlite
        name: Sqlite
        description: ''
  - id: host
    name: Host
    type: string
    default: ''
    required: true
    description: ''
    placeholder: localhost:5432
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - databases
          operation:
          - addNewDatasource
          engine:
          - postgres
          - redshift
          - mysql
          - mongo
    typeInfo:
      type: string
      displayName: Host
      name: host
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    placeholder: Database 1
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - databases
          operation:
          - addNewDatasource
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: port
    name: Port
    type: number
    default: 5432
    required: true
    description: ''
    placeholder: '5432'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - databases
          operation:
          - addNewDatasource
          engine:
          - postgres
          - redshift
          - mysql
          - mongo
    typeInfo:
      type: number
      displayName: Port
      name: port
  - id: user
    name: User
    type: string
    default: ''
    required: true
    description: ''
    placeholder: Admin
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - databases
          operation:
          - addNewDatasource
          engine:
          - postgres
          - redshift
          - mysql
          - mongo
    typeInfo:
      type: string
      displayName: User
      name: user
  - id: password
    name: Password
    type: string
    default: ''
    required: true
    description: ''
    placeholder: password
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - databases
          operation:
          - addNewDatasource
          engine:
          - postgres
          - redshift
          - mysql
          - mongo
    typeInfo:
      type: string
      displayName: Password
      name: password
      typeOptions:
        password: true
  - id: dbName
    name: Database Name
    type: string
    default: ''
    required: false
    description: ''
    placeholder: Users
    validation:
      displayOptions:
        show:
          resource:
          - databases
          operation:
          - addNewDatasource
          engine:
          - postgres
          - redshift
          - mysql
          - mongo
    typeInfo:
      type: string
      displayName: Database Name
      name: dbName
  - id: filePath
    name: File Path
    type: string
    default: ''
    required: true
    description: ''
    placeholder: file:/Users/admin/Desktop/Users
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - databases
          operation:
          - addNewDatasource
          engine:
          - h2
          - sqlite
    typeInfo:
      type: string
      displayName: File Path
      name: filePath
  - id: fullSync
    name: Full Sync
    type: boolean
    default: true
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - databases
          operation:
          - addNewDatasource
    typeInfo:
      type: boolean
      displayName: Full Sync
      name: fullSync
common_expressions:
- ={{$credentials.url.replace(new RegExp("/$"), "")}}
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: questionId
    text: '0'
  - field: metricId
    text: '0'
  - field: databaseId
    text: '0'
  - field: engine
    text: PostgreSQL
  - field: host
    text: localhost:5432
  - field: name
    text: Database 1
  - field: port
    text: '5432'
  - field: user
    text: Admin
  - field: password
    text: password
  - field: dbName
    text: Users
  - field: filePath
    text: file:/Users/admin/Desktop/Users
  - field: alertId
    text: '0'
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
  "$id": "https://n8n.io/schemas/nodes/metabase.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Metabase Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll",
        "addNewDatasource"
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
            "alerts",
            "databases",
            "metrics",
            "questions"
          ],
          "default": "questions"
        },
        "operation": {
          "description": "Get specific alert",
          "type": "string",
          "enum": [
            "get",
            "getAll"
          ],
          "default": "getAll"
        },
        "questionId": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "0"
          ]
        },
        "format": {
          "description": "",
          "type": "string",
          "enum": [
            "csv",
            "json",
            "xlsx"
          ],
          "default": "csv"
        },
        "metricId": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "0"
          ]
        },
        "databaseId": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "0"
          ]
        },
        "engine": {
          "description": "",
          "type": "string",
          "enum": [
            "h2",
            "mongo",
            "mysql",
            "postgres",
            "redshift",
            "sqlite"
          ],
          "default": "postgres",
          "examples": [
            "PostgreSQL"
          ]
        },
        "host": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "localhost:5432"
          ]
        },
        "name": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Database 1"
          ]
        },
        "port": {
          "description": "",
          "type": "number",
          "default": 5432,
          "examples": [
            "5432"
          ]
        },
        "user": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Admin"
          ]
        },
        "password": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "password"
          ]
        },
        "dbName": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Users"
          ]
        },
        "filePath": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "file:/Users/admin/Desktop/Users"
          ]
        },
        "fullSync": {
          "description": "",
          "type": "boolean",
          "default": true
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "alertId": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "0"
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
      "name": "metabaseApi",
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
