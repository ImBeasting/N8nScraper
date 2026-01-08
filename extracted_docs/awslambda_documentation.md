---
title: "Node: AWS Lambda"
slug: "node-awslambda"
version: "1"
updated: "2026-01-08"
summary: "Invoke functions on AWS Lambda"
node_type: "regular"
group: "['output']"
---

# Node: AWS Lambda

**Purpose.** Invoke functions on AWS Lambda
**Subtitle.** ={{$parameter["function"]}}


---

## Node Details

- **Icon:** `file:lambda.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Invoke | `invoke` | Invoke a function |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | invoke | ✗ | Invoke a function |  |

**Operation options:**

* **Invoke** (`invoke`) - Invoke a function

---

### Invoke parameters (`invoke`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Function Name or ID | `function` | options |  | ✓ | The function you want to invoke. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Qualifier | `qualifier` | string | $LATEST | ✓ | Specify a version or alias to invoke a published version of the function |  |
| Invocation Type | `invocationType` | options | RequestResponse | ✗ | Invoke the function synchronously and wait for the response |  |

**Invocation Type options:**

* **Wait for Results** (`RequestResponse`) - Invoke the function synchronously and wait for the response
* **Continue Workflow** (`Event`) - Invoke the function and immediately continue the workflow

| JSON Input | `payload` | string |  | ✗ | The JSON that you want to provide to your Lambda function as input |  |

---

## Load Options Methods

- `getFunctions`
- `for`
- `name`
- `value`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["function"]}}`

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
node: awsLambda
displayName: AWS Lambda
description: Invoke functions on AWS Lambda
version: '1'
nodeType: regular
group:
- output
operations:
- id: invoke
  name: Invoke
  description: Invoke a function
  params:
  - id: function
    name: Function Name or ID
    type: options
    default: ''
    required: true
    description: The function you want to invoke. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - invoke
    typeInfo:
      type: options
      displayName: Function Name or ID
      name: function
      typeOptions:
        loadOptionsMethod: getFunctions
      possibleValues: []
  - id: qualifier
    name: Qualifier
    type: string
    default: $LATEST
    required: true
    description: Specify a version or alias to invoke a published version of the function
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - invoke
    typeInfo:
      type: string
      displayName: Qualifier
      name: qualifier
  - id: invocationType
    name: Invocation Type
    type: options
    default: RequestResponse
    required: false
    description: Invoke the function synchronously and wait for the response
    validation:
      displayOptions:
        show:
          operation:
          - invoke
    typeInfo:
      type: options
      displayName: Invocation Type
      name: invocationType
      possibleValues:
      - value: RequestResponse
        name: Wait for Results
        description: Invoke the function synchronously and wait for the response
      - value: Event
        name: Continue Workflow
        description: Invoke the function and immediately continue the workflow
  - id: payload
    name: JSON Input
    type: string
    default: ''
    required: false
    description: The JSON that you want to provide to your Lambda function as input
    validation:
      displayOptions:
        show:
          operation:
          - invoke
    typeInfo:
      type: string
      displayName: JSON Input
      name: payload
common_expressions:
- ={{$parameter["function"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
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
  "$id": "https://n8n.io/schemas/nodes/awsLambda.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AWS Lambda Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "invoke"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Invoke a function",
          "type": "string",
          "enum": [
            "invoke"
          ],
          "default": "invoke"
        },
        "function": {
          "description": "The function you want to invoke. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "qualifier": {
          "description": "Specify a version or alias to invoke a published version of the function",
          "type": "string",
          "default": "$LATEST"
        },
        "invocationType": {
          "description": "Invoke the function synchronously and wait for the response",
          "type": "string",
          "enum": [
            "RequestResponse",
            "Event"
          ],
          "default": "RequestResponse"
        },
        "payload": {
          "description": "The JSON that you want to provide to your Lambda function as input",
          "type": "string",
          "default": ""
        },
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "iam",
            "assumeRole"
          ],
          "default": "iam"
        },
        "aws": {
          "description": "",
          "type": "string"
        },
        "awsAssumeRole": {
          "description": "",
          "type": "string"
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
