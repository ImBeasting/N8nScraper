---
title: "Node: Execute Sub-workflow"
slug: "node-executeworkflow"
version: "['1', '1.1', '1.2', '1.3']"
updated: "2026-01-08"
summary: "Execute another workflow"
node_type: "regular"
group: "['transform']"
---

# Node: Execute Sub-workflow

**Purpose.** Execute another workflow
**Subtitle.** ={{"Workflow: " + $parameter["workflowId"]}}


---

## Node Details

- **Icon:** `fa:sign-in-alt`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **outdatedVersionWarning**: This node is out of date. Please upgrade by removing it and adding a new one
- **executeWorkflowNotice**: Any data you pass into this node will be output by the Execute Workflow Trigger. <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow/" target="_blank">More info</a>

---

## API Patterns

**HTTP Methods:** GET

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | hidden | call_workflow | ✗ |  |  |
| Source | `source` | options | database | ✗ | Load the workflow from the database by ID |  |

**Source options:**

* **Database** (`database`) - Load the workflow from the database by ID
* **Local File** (`localFile`) - Load the workflow from a locally saved file
* **Parameter** (`parameter`) - Load the workflow from a parameter
* **URL** (`url`) - Load the workflow from an URL

| Workflow ID | `workflowId` | string |  | ✓ | Note on using an expression here: if this node is set to run once with all items, they will all be sent to the <em>same</em> workflow. That workflow's ID will be calculated by evaluating the expression for the <strong>first input item</strong>. | e.g. Can be found in the URL of the workflow |  |
| Workflow Path | `workflowPath` | string |  | ✓ | The path to local JSON workflow file to execute | e.g. /data/workflow.json |  |
| Workflow JSON | `workflowJson` | json | \n\n\n | ✓ | The workflow JSON code to execute |  |
| Workflow URL | `workflowUrl` | string |  | ✓ | The URL from which to load the workflow from | e.g. https://example.com/workflow.json | url |
| Workflow Inputs | `workflowInputs` | resourceMapper |  | ✓ |  |  |
| Mode | `mode` | options | once | ✗ | Pass all items into a single execution of the sub-workflow |  |

**Mode options:**

* **Run once with all items** (`once`) - Pass all items into a single execution of the sub-workflow
* **Run once for each item** (`each`) - Call the sub-workflow individually for each item

| Options | `options` | collection | {} | ✗ | Whether the main workflow should wait for the sub-workflow to complete its execution before proceeding | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Wait For Sub-Workflow Completion | `waitForSubWorkflow` | boolean | True | Whether the main workflow should wait for the sub-workflow to complete its execution before proceeding |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $rawParameter.workflowId.startsWith("=") && $parameter.mode === "once" && $nodeVersion >= 1.2 }}`
- `={{"Workflow: " + $parameter["workflowId"]}}`

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
* Categories: Core Nodes
* Aliases: n8n, call, sub, workflow, sub-workflow, subworkflow

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: executeWorkflow
displayName: Execute Sub-workflow
description: Execute another workflow
version:
- '1'
- '1.1'
- '1.2'
- '1.3'
nodeType: regular
group:
- transform
params:
- id: operation
  name: Operation
  type: hidden
  default: call_workflow
  required: false
  description: ''
  typeInfo:
    type: hidden
    displayName: Operation
    name: operation
- id: source
  name: Source
  type: options
  default: database
  required: false
  description: Load the workflow from the database by ID
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: options
    displayName: Source
    name: source
    possibleValues:
    - value: database
      name: Database
      description: Load the workflow from the database by ID
    - value: localFile
      name: Local File
      description: Load the workflow from a locally saved file
    - value: parameter
      name: Parameter
      description: Load the workflow from a parameter
    - value: url
      name: URL
      description: Load the workflow from an URL
- id: workflowId
  name: Workflow ID
  type: string
  default: ''
  required: true
  description: 'Note on using an expression here: if this node is set to run once
    with all items, they will all be sent to the <em>same</em> workflow. That workflow''s
    ID will be calculated by evaluating the expression for the <strong>first input
    item</strong>.'
  hint: Can be found in the URL of the workflow
  validation:
    required: true
    displayOptions:
      show:
        source:
        - database
  typeInfo:
    type: string
    displayName: Workflow ID
    name: workflowId
- id: workflowPath
  name: Workflow Path
  type: string
  default: ''
  required: true
  description: The path to local JSON workflow file to execute
  placeholder: /data/workflow.json
  validation:
    required: true
    displayOptions:
      show:
        source:
        - localFile
  typeInfo:
    type: string
    displayName: Workflow Path
    name: workflowPath
- id: workflowJson
  name: Workflow JSON
  type: json
  default: \n\n\n
  required: true
  description: The workflow JSON code to execute
  validation:
    required: true
    displayOptions:
      show:
        source:
        - parameter
  typeInfo:
    type: json
    displayName: Workflow JSON
    name: workflowJson
    typeOptions:
      rows: 10
- id: workflowUrl
  name: Workflow URL
  type: string
  default: ''
  required: true
  description: The URL from which to load the workflow from
  placeholder: https://example.com/workflow.json
  validation:
    required: true
    format: url
    displayOptions:
      show:
        source:
        - url
  typeInfo:
    type: string
    displayName: Workflow URL
    name: workflowUrl
- id: workflowInputs
  name: Workflow Inputs
  type: resourceMapper
  default: ''
  required: true
  description: ''
  validation:
    required: true
    displayOptions:
      show:
        source:
        - database
      hide:
        workflowId:
        - ''
  typeInfo:
    type: resourceMapper
    displayName: Workflow Inputs
    name: workflowInputs
- id: mode
  name: Mode
  type: options
  default: once
  required: false
  description: Pass all items into a single execution of the sub-workflow
  typeInfo:
    type: options
    displayName: Mode
    name: mode
    possibleValues:
    - value: once
      name: Run once with all items
      description: Pass all items into a single execution of the sub-workflow
    - value: each
      name: Run once for each item
      description: Call the sub-workflow individually for each item
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether the main workflow should wait for the sub-workflow to complete
    its execution before proceeding
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Wait For Sub-Workflow Completion
      name: waitForSubWorkflow
      type: boolean
      description: Whether the main workflow should wait for the sub-workflow to complete
        its execution before proceeding
      default: true
common_expressions:
- ={{ $rawParameter.workflowId.startsWith("=") && $parameter.mode === "once" && $nodeVersion
  >= 1.2 }}
- '={{"Workflow: " + $parameter["workflowId"]}}'
api_patterns:
  http_methods:
  - GET
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: outdatedVersionWarning
    text: This node is out of date. Please upgrade by removing it and adding a new
      one
    conditions:
      show: {}
  - name: executeWorkflowNotice
    text: Any data you pass into this node will be output by the Execute Workflow
      Trigger. <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow/"
      target="_blank">More info</a>
    conditions:
      show: {}
  tooltips: []
  placeholders:
  - field: workflowPath
    text: /data/workflow.json
  - field: workflowUrl
    text: https://example.com/workflow.json
  - field: options
    text: Add option
  hints:
  - field: workflowId
    text: Can be found in the URL of the workflow
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
  "$id": "https://n8n.io/schemas/nodes/executeWorkflow.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Execute Sub-workflow Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "",
          "type": "string",
          "default": "call_workflow"
        },
        "source": {
          "description": "Load the workflow from the database by ID",
          "type": "string",
          "enum": [
            "database",
            "localFile",
            "parameter",
            "url"
          ],
          "default": "database"
        },
        "workflowId": {
          "description": "Note on using an expression here: if this node is set to run once with all items, they will all be sent to the <em>same</em> workflow. That workflow's ID will be calculated by evaluating the expression for the <strong>first input item</strong>.",
          "type": "string",
          "default": ""
        },
        "workflowPath": {
          "description": "The path to local JSON workflow file to execute",
          "type": "string",
          "default": "",
          "examples": [
            "/data/workflow.json"
          ]
        },
        "workflowJson": {
          "description": "The workflow JSON code to execute",
          "type": "string",
          "default": "\\n\\n\\n"
        },
        "workflowUrl": {
          "description": "The URL from which to load the workflow from",
          "type": "string",
          "default": "",
          "format": "url",
          "examples": [
            "https://example.com/workflow.json"
          ]
        },
        "workflowInputs": {
          "description": "",
          "type": "string"
        },
        "mode": {
          "description": "Pass all items into a single execution of the sub-workflow",
          "type": "string",
          "enum": [
            "once",
            "each"
          ],
          "default": "once"
        },
        "options": {
          "description": "Whether the main workflow should wait for the sub-workflow to complete its execution before proceeding",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
      "1.1",
      "1.2",
      "1.3"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1', '1.2', '1.3'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
