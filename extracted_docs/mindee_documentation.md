---
title: "Node: Mindee"
slug: "node-mindee"
version: "['1', '2', '3']"
updated: "2026-01-08"
summary: "Consume Mindee API"
node_type: "regular"
group: "['input']"
---

# Node: Mindee

**Purpose.** Consume Mindee API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:mindee.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **mindeeReceiptApi**: N/A
- **mindeeInvoiceApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `mindeeReceiptApi` | ✓ | {'show': {'resource': ['receipt']}} |
| `mindeeInvoiceApi` | ✓ | {'show': {'resource': ['invoice']}} |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Predict | `predict` |  |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | receipt | ✗ | Resource to operate on |  |

**Resource options:**

* **Invoice** (`invoice`)
* **Receipt** (`receipt`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | predict | ✗ | Operation to perform |  |

**Operation options:**

* **Predict** (`predict`)

---

### Predict parameters (`predict`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |

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
* Categories: Utility

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: mindee
displayName: Mindee
description: Consume Mindee API
version:
- '1'
- '2'
- '3'
nodeType: regular
group:
- input
credentials:
- name: mindeeReceiptApi
  required: true
- name: mindeeInvoiceApi
  required: true
operations:
- id: predict
  name: Predict
  description: ''
  params:
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be uploaded
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - predict
          resource:
          - receipt
          - invoice
    typeInfo:
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders: []
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be uploaded
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
  "$id": "https://n8n.io/schemas/nodes/mindee.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Mindee Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "predict"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "apiVersion": {
          "description": "Which Mindee API Version to use",
          "type": "string",
          "enum": [
            "1",
            "3",
            "4"
          ],
          "default": 1
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "invoice",
            "receipt"
          ],
          "default": "receipt"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "predict"
          ],
          "default": "predict"
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "rawData": {
          "description": "Whether to return the data exactly in the way it got received from the API",
          "type": "boolean",
          "default": false
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
      "2",
      "3"
    ]
  },
  "credentials": [
    {
      "name": "mindeeReceiptApi",
      "required": true
    },
    {
      "name": "mindeeInvoiceApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2', '3'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
