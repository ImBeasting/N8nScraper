---
title: "Node: Gong"
slug: "node-gong"
version: "1"
updated: "2025-11-13"
summary: "Interact with Gong API"
node_type: "regular"
group: "['transform']"
---

# Node: Gong

**Purpose.** Interact with Gong API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:gong.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **gongApi**: N/A
- **gongOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `gongApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `gongOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Call Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | call | ✗ | Resource to operate on |  |

**Resource options:**

* **Call** (`call`)
* **User** (`user`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | accessToken | ✗ |  |  |

**Authentication options:**

* **Access Token** (`accessToken`)
* **OAuth2** (`oAuth2`)

| Resource | `resource` | options | call | ✗ |  |  |

**Resource options:**

* **Call** (`call`)
* **User** (`user`)

| Operation | `operation` | options | get | ✗ | Retrieve data for a specific user |  |
| User to Get | `user` | list |  | ✓ | e.g. e.g. 7782342274025937895 |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | rootProperty | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | body | {} | ✗ | An optional user creation time lower limit, if supplied the API will return only the users created at or after this time | e.g. e.g. 2018-02-18T02:30:00-07:00 or 2018-02-18T08:00:00Z |  |
| Call to Get | `call` | list |  | ✓ | e.g. e.g. 7782342274025937895 |  |
| Options | `options` | multiOptions | {} | ✗ | The Call properties to include in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a>. | e.g. Add Option |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | limit | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | body | {} | ✗ | Returns calls that started on or after the specified date and time. If not provided, list starts with earliest call. For web-conference calls recorded by Gong, the date denotes its scheduled time, otherwise, it denotes its actual start time. | e.g. e.g. 2018-02-18T02:30:00-07:00 or 2018-02-18T08:00:00Z |  |
| Options | `options` | multiOptions | {} | ✗ | The Call properties to include in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a>. | e.g. Add Option |  |
| Operation | `operation` | options | getAll | ✗ | Retrieve data for a specific call |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $credentials.baseUrl.replace(new RegExp("/$"), "") }}`
- `={{ $if($response.body?.records.cursor, { cursor: $response.body.records.cursor }, {}) }}`
- `={{$parameter["operation"] + ": " + $parameter["resource"]}}`
- `={{ $response.body.records.cursor }}`

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
* Categories: Development, Developer Tools

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: gong
displayName: Gong
description: Interact with Gong API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: gongApi
  required: true
- name: gongOAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: accessToken
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: accessToken
      name: Access Token
      description: ''
    - value: oAuth2
      name: OAuth2
      description: ''
- id: resource
  name: Resource
  type: options
  default: call
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: call
      name: Call
      description: ''
    - value: user
      name: User
      description: ''
- id: operation
  name: Operation
  type: options
  default: get
  required: false
  description: Retrieve data for a specific user
  validation: &id009
    displayOptions:
      show:
        resource:
        - call
  typeInfo: &id010
    type: options
    displayName: Operation
    name: operation
    possibleValues: []
- id: user
  name: User to Get
  type: list
  default: ''
  required: true
  description: ''
  placeholder: e.g. 7782342274025937895
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - user
        operation:
        - get
  typeInfo:
    type: list
    displayName: User to Get
    name: user
- id: returnAll
  name: Return All
  type: boolean
  default: false
  required: false
  description: Whether to return all results or only up to a given limit
  validation: &id001
    displayOptions:
      show:
        resource:
        - call
        operation:
        - getAll
  typeInfo: &id002
    type: boolean
    displayName: Return All
    name: returnAll
- id: limit
  name: Limit
  type: rootProperty
  default: 50
  required: false
  description: Max number of results to return
  validation: &id003
    displayOptions:
      show:
        resource:
        - call
        operation:
        - getAll
        returnAll:
        - false
  typeInfo: &id004
    type: limit
    displayName: Limit
    name: limit
    typeOptions:
      minValue: 1
- id: filters
  name: Filters
  type: body
  default: {}
  required: false
  description: An optional user creation time lower limit, if supplied the API will
    return only the users created at or after this time
  hint: Comma separated list of IDs, array of strings can be set in expression
  placeholder: e.g. 2018-02-18T02:30:00-07:00 or 2018-02-18T08:00:00Z
  validation: &id005
    displayOptions:
      show:
        resource:
        - call
        operation:
        - getAll
  typeInfo: &id006
    type: body
    displayName: Filters
    name: filters
- id: call
  name: Call to Get
  type: list
  default: ''
  required: true
  description: ''
  placeholder: e.g. 7782342274025937895
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - call
        operation:
        - get
  typeInfo:
    type: list
    displayName: Call to Get
    name: call
- id: options
  name: Options
  type: multiOptions
  default: {}
  required: false
  description: The Call properties to include in the returned results. Choose from
    a list, or specify IDs using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a>.
  placeholder: Add Option
  validation: &id007
    displayOptions:
      show:
        resource:
        - call
        operation:
        - getAll
  typeInfo: &id008
    type: multiOptions
    displayName: Options
    name: options
    possibleValues: []
- id: returnAll
  name: Return All
  type: boolean
  default: false
  required: false
  description: Whether to return all results or only up to a given limit
  validation: *id001
  typeInfo: *id002
- id: limit
  name: Limit
  type: limit
  default: 50
  required: false
  description: Max number of results to return
  validation: *id003
  typeInfo: *id004
- id: filters
  name: Filters
  type: body
  default: {}
  required: false
  description: Returns calls that started on or after the specified date and time.
    If not provided, list starts with earliest call. For web-conference calls recorded
    by Gong, the date denotes its scheduled time, otherwise, it denotes its actual
    start time.
  hint: Comma separated list of IDs, array of strings can be set in expression
  placeholder: e.g. 2018-02-18T02:30:00-07:00 or 2018-02-18T08:00:00Z
  validation: *id005
  typeInfo: *id006
- id: options
  name: Options
  type: multiOptions
  default: {}
  required: false
  description: The Call properties to include in the returned results. Choose from
    a list, or specify IDs using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a>.
  placeholder: Add Option
  validation: *id007
  typeInfo: *id008
- id: operation
  name: Operation
  type: options
  default: getAll
  required: false
  description: Retrieve data for a specific call
  validation: *id009
  typeInfo: *id010
common_expressions:
- ={{ $credentials.baseUrl.replace(new RegExp("/$"), "") }}
- '={{ $if($response.body?.records.cursor, { cursor: $response.body.records.cursor
  }, {}) }}'
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
- ={{ $response.body.records.cursor }}
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: user
    text: e.g. 7782342274025937895
  - field: filters
    text: e.g. 2018-02-18T02:30:00-07:00 or 2018-02-18T08:00:00Z
  - field: call
    text: e.g. 7782342274025937895
  - field: options
    text: Add Option
  - field: filters
    text: e.g. 2018-02-18T02:30:00-07:00 or 2018-02-18T08:00:00Z
  - field: options
    text: Add Option
  hints:
  - field: filters
    text: Comma separated list of IDs, array of strings can be set in expression
  - field: filters
    text: Comma separated list of IDs, array of strings can be set in expression
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
  "$id": "https://n8n.io/schemas/nodes/gong.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Gong Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "accessToken",
            "oAuth2"
          ],
          "default": "accessToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "call",
            "user"
          ],
          "default": "call"
        },
        "operation": {
          "description": "Retrieve data for a specific call",
          "type": "string",
          "default": "getAll"
        },
        "user": {
          "description": "",
          "type": "string",
          "examples": [
            "e.g. 7782342274025937895"
          ]
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "string",
          "default": 50
        },
        "filters": {
          "description": "Returns calls that started on or after the specified date and time. If not provided, list starts with earliest call. For web-conference calls recorded by Gong, the date denotes its scheduled time, otherwise, it denotes its actual start time.",
          "type": "string",
          "default": {},
          "examples": [
            "e.g. 2018-02-18T02:30:00-07:00 or 2018-02-18T08:00:00Z"
          ]
        },
        "call": {
          "description": "",
          "type": "string",
          "examples": [
            "e.g. 7782342274025937895"
          ]
        },
        "options": {
          "description": "The Call properties to include in the returned results. Choose from a list, or specify IDs using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Option"
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
      "name": "gongApi",
      "required": true
    },
    {
      "name": "gongOAuth2Api",
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
