---
title: "Node: Jenkins"
slug: "node-jenkins"
version: "1"
updated: "2026-01-08"
summary: "Consume Jenkins API"
node_type: "regular"
group: "['output']"
---

# Node: Jenkins

**Purpose.** Consume Jenkins API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:jenkins.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **jenkinsApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **triggerParamsNotice** when resource=['job'], operation=['triggerParams']: Make sure the job is setup to support triggering with parameters. <a href="https://wiki.jenkins.io/display/JENKINS/Parameterized+Build" target="_blank">More info</a>
- **createNotice** when resource=['job'], operation=['create']: To get the XML of an existing job, add ‘config.xml’ to the end of the job URL
- **instanceNotice** when resource=['instance']: Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `jenkinsApi` | ✓ | - |

---

## Operations

### Job Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Copy | `copy` | Copy a specific job |
| Create | `create` | Create a new job |
| Trigger | `trigger` | Trigger a specific job |
| Trigger with Parameters | `triggerParams` | Trigger a specific job |

### Instance Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Cancel Quiet Down | `cancelQuietDown` | Cancel quiet down state |
| Quiet Down | `quietDown` | Put Jenkins in quiet mode, no builds can be started, Jenkins is ready for shutdown |
| Restart | `restart` | Restart Jenkins immediately on environments where it is possible |
| Safely Restart | `safeRestart` | Restart Jenkins once no jobs are running on environments where it is possible |
| Safely Shutdown | `safeExit` | Shutdown once no jobs are running |
| Shutdown | `exit` | Shutdown Jenkins immediately |

### Build Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | List Builds |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | job | ✗ | Resource to operate on |  |

**Resource options:**

* **Build** (`build`)
* **Instance** (`instance`)
* **Job** (`job`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | trigger | ✗ | Copy a specific job |  |

**Operation options:**

* **Copy** (`copy`) - Copy a specific job
* **Create** (`create`) - Create a new job
* **Trigger** (`trigger`) - Trigger a specific job
* **Trigger with Parameters** (`triggerParams`) - Trigger a specific job

---

### Copy parameters (`copy`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Job Name or ID | `job` | options |  | ✓ | Name of the job. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| New Job Name | `newJob` | string |  | ✓ | Name of the new Jenkins job |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| New Job Name | `newJob` | string |  | ✓ | Name of the new Jenkins job |  |
| XML | `xml` | string |  | ✓ | XML of Jenkins config |  |

### Trigger parameters (`trigger`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Job Name or ID | `job` | options |  | ✓ | Name of the job. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Trigger with Parameters parameters (`triggerParams`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Job Name or ID | `job` | options |  | ✓ | Name of the job. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Parameters | `param` | fixedCollection | {} | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Parameter |  |

<details>
<summary><strong>Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Parameters | `params` |  |  |  |

</details>


### Quiet Down parameters (`quietDown`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Reason | `reason` | string |  | ✗ | Freeform reason for quiet down mode |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Job Name or ID | `job` | options |  | ✓ | Name of the job. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |

---

## Load Options Methods

- `getJobs`

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
node: jenkins
displayName: Jenkins
description: Consume Jenkins API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: jenkinsApi
  required: true
operations:
- id: copy
  name: Copy
  description: Copy a specific job
  params:
  - id: job
    name: Job Name or ID
    type: options
    default: ''
    required: true
    description: Name of the job. Choose from the list, or specify an ID using an
      <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - build
          operation:
          - getAll
    typeInfo: &id004
      type: options
      displayName: Job Name or ID
      name: job
      typeOptions:
        loadOptionsMethod: getJobs
      possibleValues: []
  - id: newJob
    name: New Job Name
    type: string
    default: ''
    required: true
    description: Name of the new Jenkins job
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - job
          operation:
          - copy
          - create
    typeInfo: &id002
      type: string
      displayName: New Job Name
      name: newJob
- id: create
  name: Create
  description: Create a new job
  params:
  - id: newJob
    name: New Job Name
    type: string
    default: ''
    required: true
    description: Name of the new Jenkins job
    validation: *id001
    typeInfo: *id002
  - id: xml
    name: XML
    type: string
    default: ''
    required: true
    description: XML of Jenkins config
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - job
          operation:
          - create
    typeInfo:
      type: string
      displayName: XML
      name: xml
- id: trigger
  name: Trigger
  description: Trigger a specific job
  params:
  - id: job
    name: Job Name or ID
    type: options
    default: ''
    required: true
    description: Name of the job. Choose from the list, or specify an ID using an
      <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
- id: triggerParams
  name: Trigger with Parameters
  description: Trigger a specific job
  params:
  - id: job
    name: Job Name or ID
    type: options
    default: ''
    required: true
    description: Name of the job. Choose from the list, or specify an ID using an
      <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: param
    name: Parameters
    type: fixedCollection
    default: {}
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Parameter
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - job
          operation:
          - triggerParams
    typeInfo:
      type: fixedCollection
      displayName: Parameters
      name: param
      typeOptions:
        multipleValues: true
      subProperties:
      - name: params
        displayName: Parameters
        values:
        - displayName: Name or ID
          name: name
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getJobParameters
        - displayName: Value
          name: value
          type: string
          default: ''
- id: cancelQuietDown
  name: Cancel Quiet Down
  description: Cancel quiet down state
- id: quietDown
  name: Quiet Down
  description: Put Jenkins in quiet mode, no builds can be started, Jenkins is ready
    for shutdown
  params:
  - id: reason
    name: Reason
    type: string
    default: ''
    required: false
    description: Freeform reason for quiet down mode
    validation:
      displayOptions:
        show:
          resource:
          - instance
          operation:
          - quietDown
    typeInfo:
      type: string
      displayName: Reason
      name: reason
- id: restart
  name: Restart
  description: Restart Jenkins immediately on environments where it is possible
- id: safeRestart
  name: Safely Restart
  description: Restart Jenkins once no jobs are running on environments where it is
    possible
- id: safeExit
  name: Safely Shutdown
  description: Shutdown once no jobs are running
- id: exit
  name: Shutdown
  description: Shutdown Jenkins immediately
- id: getAll
  name: Get Many
  description: List Builds
  params:
  - id: job
    name: Job Name or ID
    type: options
    default: ''
    required: true
    description: Name of the job. Choose from the list, or specify an ID using an
      <a href="https://docs.n8n.io/code/expressions/">expression</a>.
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
          resource:
          - build
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
          resource:
          - build
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
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: triggerParamsNotice
    text: Make sure the job is setup to support triggering with parameters. <a href="https://wiki.jenkins.io/display/JENKINS/Parameterized+Build"
      target="_blank">More info</a>
    conditions:
      show:
        resource:
        - job
        operation:
        - triggerParams
  - name: createNotice
    text: To get the XML of an existing job, add ‘config.xml’ to the end of the job
      URL
    conditions:
      show:
        resource:
        - job
        operation:
        - create
  - name: instanceNotice
    text: Instance operation can shutdown Jenkins instance and make it unresponsive.
      Some commands may not be available depending on instance implementation.
    conditions:
      show:
        resource:
        - instance
  tooltips: []
  placeholders:
  - field: param
    text: Add Parameter
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
  "$id": "https://n8n.io/schemas/nodes/jenkins.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Jenkins Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "copy",
        "create",
        "trigger",
        "triggerParams",
        "cancelQuietDown",
        "quietDown",
        "restart",
        "safeRestart",
        "safeExit",
        "exit",
        "getAll"
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
            "build",
            "instance",
            "job"
          ],
          "default": "job"
        },
        "operation": {
          "description": "List Builds",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "getAll"
        },
        "job": {
          "description": "Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "param": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Parameter"
          ]
        },
        "newJob": {
          "description": "Name of the new Jenkins job",
          "type": "string",
          "default": ""
        },
        "xml": {
          "description": "XML of Jenkins config",
          "type": "string",
          "default": ""
        },
        "reason": {
          "description": "Freeform reason for quiet down mode",
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
      "name": "jenkinsApi",
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
