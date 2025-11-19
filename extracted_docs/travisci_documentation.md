---
title: "Node: TravisCI"
slug: "node-travisci"
version: "1"
updated: "2025-11-13"
summary: "Consume TravisCI API"
node_type: "regular"
group: "['output']"
---

# Node: TravisCI

**Purpose.** Consume TravisCI API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:travisci.png`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **travisCiApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `travisCiApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Travis-API-Version, Content-Type

---

## Operations

### Build Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Cancel | `cancel` | Cancel a build |
| Get | `get` | Get a build |
| Get Many | `getAll` | Get many builds |
| Restart | `restart` | Restart a build |
| Trigger | `trigger` | Trigger a build |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | build | ✗ | Resource to operate on |  |

**Resource options:**

* **Build** (`build`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | cancel | ✗ | Cancel a build |  |

**Operation options:**

* **Cancel** (`cancel`) - Cancel a build
* **Get** (`get`) - Get a build
* **Get Many** (`getAll`) - Get many builds
* **Restart** (`restart`) - Restart a build
* **Trigger** (`trigger`) - Trigger a build

---

### Cancel parameters (`cancel`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Build ID | `buildId` | string |  | ✗ | Value uniquely identifying the build |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Build ID | `buildId` | string |  | ✗ | Value uniquely identifying the build |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | List of attributes to eager load | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | string |  | List of attributes to eager load |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | List of attributes to eager load | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | string |  | List of attributes to eager load |
| Order | `order` | options | asc | You may specify order to sort your response |
| Sort By | `sortBy` | options | number |  |

</details>


### Restart parameters (`restart`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Build ID | `buildId` | string |  | ✗ | Value uniquely identifying the build |  |

### Trigger parameters (`trigger`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Slug | `slug` | string |  | ✗ | Same as {ownerName}/{repositoryName} | e.g. n8n-io/n8n |  |
| Branch | `branch` | string |  | ✗ | Branch requested to be built | e.g. master |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Travis-ci status message attached to the request | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Message | `message` | string |  | Travis-ci status message attached to the request |
| Merge Mode | `mergeMode` | options |  |  |

</details>


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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: travisCi
displayName: TravisCI
description: Consume TravisCI API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: travisCiApi
  required: true
operations:
- id: cancel
  name: Cancel
  description: Cancel a build
  params:
  - id: buildId
    name: Build ID
    type: string
    default: ''
    required: false
    description: Value uniquely identifying the build
    validation: &id001
      displayOptions:
        show:
          operation:
          - restart
          resource:
          - build
    typeInfo: &id002
      type: string
      displayName: Build ID
      name: buildId
- id: get
  name: Get
  description: Get a build
  params:
  - id: buildId
    name: Build ID
    type: string
    default: ''
    required: false
    description: Value uniquely identifying the build
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many builds
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
          resource:
          - build
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
          - build
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
- id: restart
  name: Restart
  description: Restart a build
  params:
  - id: buildId
    name: Build ID
    type: string
    default: ''
    required: false
    description: Value uniquely identifying the build
    validation: *id001
    typeInfo: *id002
- id: trigger
  name: Trigger
  description: Trigger a build
  params:
  - id: slug
    name: Slug
    type: string
    default: ''
    required: false
    description: Same as {ownerName}/{repositoryName}
    placeholder: n8n-io/n8n
    validation:
      displayOptions:
        show:
          operation:
          - trigger
          resource:
          - build
    typeInfo:
      type: string
      displayName: Slug
      name: slug
  - id: branch
    name: Branch
    type: string
    default: ''
    required: false
    description: Branch requested to be built
    placeholder: master
    validation:
      displayOptions:
        show:
          operation:
          - trigger
          resource:
          - build
    typeInfo:
      type: string
      displayName: Branch
      name: branch
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Travis-API-Version
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: slug
    text: n8n-io/n8n
  - field: branch
    text: master
  - field: additionalFields
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
  "$id": "https://n8n.io/schemas/nodes/travisCi.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TravisCI Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "cancel",
        "get",
        "getAll",
        "restart",
        "trigger"
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
            "build"
          ],
          "default": "build"
        },
        "operation": {
          "description": "Cancel a build",
          "type": "string",
          "enum": [
            "cancel",
            "get",
            "getAll",
            "restart",
            "trigger"
          ],
          "default": "cancel"
        },
        "buildId": {
          "description": "Value uniquely identifying the build",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Travis-ci status message attached to the request",
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
        },
        "slug": {
          "description": "Same as {ownerName}/{repositoryName}",
          "type": "string",
          "default": "",
          "examples": [
            "n8n-io/n8n"
          ]
        },
        "branch": {
          "description": "Branch requested to be built",
          "type": "string",
          "default": "",
          "examples": [
            "master"
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
      "name": "travisCiApi",
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
