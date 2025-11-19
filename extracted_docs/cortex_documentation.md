---
title: "Node: Cortex"
slug: "node-cortex"
version: "1"
updated: "2025-11-13"
summary: "Apply the Cortex analyzer/responder on the given entity"
node_type: "regular"
group: "['transform']"
---

# Node: Cortex

**Purpose.** Apply the Cortex analyzer/responder on the given entity
**Subtitle.** ={{$parameter["operation"]+ ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:cortex.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **cortexApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `cortexApi` | ✓ | - |

---

## Operations

### Analyzer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Execute | `execute` | Execute Analyzer |

### Responder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Execute | `execute` | Execute Responder |

### Job Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get job details |
| Report | `report` | Get job report |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | analyzer | ✓ | Choose a resource |  |

**Resource options:**

* **Analyzer** (`analyzer`)
* **Job** (`job`)
* **Responder** (`responder`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | execute | ✓ | Choose an operation |  |

**Operation options:**

* **Execute** (`execute`) - Execute Analyzer

---

### Execute parameters (`execute`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Analyzer Type Name or ID | `analyzer` | options |  | ✓ | Choose the analyzer. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Observable Type Name or ID | `observableType` | options |  | ✓ | Choose the observable type. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Observable Value | `observableValue` | string |  | ✓ | Enter the observable value |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| TLP | `tlp` | options | 2 | ✗ | The TLP of the analyzed observable |  |

**TLP options:**

* **White** (``)
* **Green** (``)
* **Amber** (``)
* **Red** (``)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to force bypassing the cache | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Force | `force` | boolean | False | Whether to force bypassing the cache |
| Timeout (Seconds) | `timeout` | number | 3 | Timeout to wait for the report in case it is not available at the time the query was made |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Job ID | `jobId` | string |  | ✓ | ID of the job |  |

### Report parameters (`report`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Job ID | `jobId` | string |  | ✓ | ID of the job |  |

---

## Load Options Methods

- `loadActiveAnalyzers`
- `for`
- `name`
- `value`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"]+ ": " + $parameter["resource"]}}`

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
* Categories: Development, Analytics

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: cortex
displayName: Cortex
description: Apply the Cortex analyzer/responder on the given entity
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: cortexApi
  required: true
operations:
- id: execute
  name: Execute
  description: Execute Analyzer
  params:
  - id: analyzer
    name: Analyzer Type Name or ID
    type: options
    default: ''
    required: true
    description: Choose the analyzer. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - analyzer
          operation:
          - execute
    typeInfo:
      type: options
      displayName: Analyzer Type Name or ID
      name: analyzer
      typeOptions:
        loadOptionsMethod: loadActiveAnalyzers
      possibleValues: []
  - id: observableType
    name: Observable Type Name or ID
    type: options
    default: ''
    required: true
    description: Choose the observable type. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - analyzer
          operation:
          - execute
        hide:
          analyzer:
          - ''
    typeInfo:
      type: options
      displayName: Observable Type Name or ID
      name: observableType
      typeOptions:
        loadOptionsMethod: loadObservableOptions
      possibleValues: []
  - id: observableValue
    name: Observable Value
    type: string
    default: ''
    required: true
    description: Enter the observable value
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - analyzer
          operation:
          - execute
        hide:
          observableType:
          - file
          analyzer:
          - ''
    typeInfo:
      type: string
      displayName: Observable Value
      name: observableValue
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation:
      required: true
      displayOptions:
        show:
          observableType:
          - file
          resource:
          - analyzer
          operation:
          - execute
    typeInfo:
      type: string
      displayName: Put Output File in Field
      name: binaryPropertyName
  - id: tlp
    name: TLP
    type: options
    default: 2
    required: false
    description: The TLP of the analyzed observable
    validation:
      displayOptions:
        show:
          resource:
          - analyzer
          operation:
          - execute
        hide:
          observableType:
          - ''
          analyzer:
          - ''
    typeInfo:
      type: options
      displayName: TLP
      name: tlp
      possibleValues:
      - value: White
        name: White
        description: ''
      - value: Green
        name: Green
        description: ''
      - value: Amber
        name: Amber
        description: ''
      - value: Red
        name: Red
        description: ''
- id: get
  name: Get
  description: Get job details
  params:
  - id: jobId
    name: Job ID
    type: string
    default: ''
    required: true
    description: ID of the job
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - job
          operation:
          - get
          - report
    typeInfo: &id002
      type: string
      displayName: Job ID
      name: jobId
- id: report
  name: Report
  description: Get job report
  params:
  - id: jobId
    name: Job ID
    type: string
    default: ''
    required: true
    description: ID of the job
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"]+ ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: parameters
    text: Add Parameter
  - field: parameters
    text: Add Parameter
  - field: parameters
    text: Add Parameter
  - field: parameters
    text: Add Parameter
  hints:
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/cortex.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Cortex Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "execute",
        "get",
        "report"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Choose a resource",
          "type": "string",
          "enum": [
            "analyzer",
            "job",
            "responder"
          ],
          "default": "analyzer"
        },
        "operation": {
          "description": "Choose an operation",
          "type": "string",
          "enum": [
            "get",
            "report"
          ],
          "default": "get"
        },
        "analyzer": {
          "description": "Choose the analyzer. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "observableType": {
          "description": "Choose the observable type. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "observableValue": {
          "description": "Enter the observable value",
          "type": "string",
          "default": ""
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "tlp": {
          "description": "The TLP of the analyzed observable",
          "type": "string",
          "enum": [
            "White",
            "Green",
            "Amber",
            "Red"
          ],
          "default": 2
        },
        "additionalFields": {
          "description": "Whether to force bypassing the cache",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "responder": {
          "description": "Choose the responder. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "entityType": {
          "description": "Choose the Data type. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "jsonObject": {
          "description": "Choose between providing JSON object or seperated attributes",
          "type": "boolean",
          "default": false
        },
        "objectData": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "parameters": {
          "description": "Date and time of the begin of the case default=now",
          "type": "string",
          "default": "",
          "examples": [
            "Add Parameter"
          ]
        },
        "jobId": {
          "description": "ID of the job",
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
      "name": "cortexApi",
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
