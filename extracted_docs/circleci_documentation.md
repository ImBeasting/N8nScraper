---
title: "Node: CircleCI"
slug: "node-circleci"
version: "1"
updated: "2026-01-08"
summary: "Consume CircleCI API"
node_type: "regular"
group: "['output']"
---

# Node: CircleCI

**Purpose.** Consume CircleCI API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:circleCi.svg', 'dark': 'file:circleCi.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **circleCiApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `circleCiApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Circle-Token

---

## Operations

### Pipeline Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a pipeline |
| Get Many | `getAll` | Get many pipelines |
| Trigger | `trigger` | Trigger a pipeline |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | pipeline | ✗ | Resource to operate on |  |

**Resource options:**

* **Pipeline** (`pipeline`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Get a pipeline |  |

**Operation options:**

* **Get** (`get`) - Get a pipeline
* **Get Many** (`getAll`) - Get many pipelines
* **Trigger** (`trigger`) - Trigger a pipeline

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Provider | `vcs` | options |  | ✗ | Source control system |  |

**Provider options:**

* **Bitbucket** (`bitbucket`)
* **GitHub** (`github`)

| Project Slug | `projectSlug` | string |  | ✗ | Project slug in the form org-name/repo-name | e.g. n8n-io/n8n |  |
| Pipeline Number | `pipelineNumber` | number | 1 | ✗ | The number of the pipeline | min:1, max:∞ |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Provider | `vcs` | options |  | ✗ | Source control system |  |

**Provider options:**

* **Bitbucket** (`bitbucket`)
* **GitHub** (`github`)

| Project Slug | `projectSlug` | string |  | ✗ | Project slug in the form org-name/repo-name | e.g. n8n-io/n8n |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Filters | `filters` | collection | {} | ✗ | The name of a vcs branch | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Branch | `branch` | string |  | The name of a vcs branch |

</details>


### Trigger parameters (`trigger`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Provider | `vcs` | options |  | ✗ | Source control system |  |

**Provider options:**

* **Bitbucket** (`bitbucket`)
* **GitHub** (`github`)

| Project Slug | `projectSlug` | string |  | ✗ | Project slug in the form org-name/repo-name | e.g. n8n-io/n8n |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that branch and tag are mutually exclusive. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Branch | `branch` | string |  | The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that branch and tag are mutually exclusive. |
| Tag | `tag` | string |  | The tag used by the pipeline. The commit that this tag points to was used for the pipeline. Note that branch and tag are mutually exclusive |

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
node: circleCi
displayName: CircleCI
description: Consume CircleCI API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: circleCiApi
  required: true
operations:
- id: get
  name: Get
  description: Get a pipeline
  params:
  - id: vcs
    name: Provider
    type: options
    default: ''
    required: false
    description: Source control system
    validation: &id001
      displayOptions:
        show:
          operation:
          - get
          - getAll
          - trigger
          resource:
          - pipeline
    typeInfo: &id002
      type: options
      displayName: Provider
      name: vcs
      possibleValues:
      - value: bitbucket
        name: Bitbucket
        description: ''
      - value: github
        name: GitHub
        description: ''
  - id: projectSlug
    name: Project Slug
    type: string
    default: ''
    required: false
    description: Project slug in the form org-name/repo-name
    placeholder: n8n-io/n8n
    validation: &id003
      displayOptions:
        show:
          operation:
          - get
          - getAll
          - trigger
          resource:
          - pipeline
    typeInfo: &id004
      type: string
      displayName: Project Slug
      name: projectSlug
  - id: pipelineNumber
    name: Pipeline Number
    type: number
    default: 1
    required: false
    description: The number of the pipeline
    validation:
      displayOptions:
        show:
          operation:
          - get
          resource:
          - pipeline
    typeInfo:
      type: number
      displayName: Pipeline Number
      name: pipelineNumber
      typeOptions:
        minValue: 1
- id: getAll
  name: Get Many
  description: Get many pipelines
  params:
  - id: vcs
    name: Provider
    type: options
    default: ''
    required: false
    description: Source control system
    validation: *id001
    typeInfo: *id002
  - id: projectSlug
    name: Project Slug
    type: string
    default: ''
    required: false
    description: Project slug in the form org-name/repo-name
    placeholder: n8n-io/n8n
    validation: *id003
    typeInfo: *id004
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
          - pipeline
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
          - pipeline
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
- id: trigger
  name: Trigger
  description: Trigger a pipeline
  params:
  - id: vcs
    name: Provider
    type: options
    default: ''
    required: false
    description: Source control system
    validation: *id001
    typeInfo: *id002
  - id: projectSlug
    name: Project Slug
    type: string
    default: ''
    required: false
    description: Project slug in the form org-name/repo-name
    placeholder: n8n-io/n8n
    validation: *id003
    typeInfo: *id004
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Circle-Token
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: projectSlug
    text: n8n-io/n8n
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/circleCi.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CircleCI Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll",
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
            "pipeline"
          ],
          "default": "pipeline"
        },
        "operation": {
          "description": "Get a pipeline",
          "type": "string",
          "enum": [
            "get",
            "getAll",
            "trigger"
          ],
          "default": "get"
        },
        "vcs": {
          "description": "Source control system",
          "type": "string",
          "enum": [
            "bitbucket",
            "github"
          ],
          "default": ""
        },
        "projectSlug": {
          "description": "Project slug in the form org-name/repo-name",
          "type": "string",
          "default": "",
          "examples": [
            "n8n-io/n8n"
          ]
        },
        "pipelineNumber": {
          "description": "The number of the pipeline",
          "type": "number",
          "default": 1
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
        "filters": {
          "description": "The name of a vcs branch",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "additionalFields": {
          "description": "The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that branch and tag are mutually exclusive.",
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
    "version": "1"
  },
  "credentials": [
    {
      "name": "circleCiApi",
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
