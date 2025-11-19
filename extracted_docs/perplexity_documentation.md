---
title: "Node: Perplexity"
slug: "node-perplexity"
version: "1"
updated: "2025-11-13"
summary: "Interact with the Perplexity API to generate AI responses with citations"
node_type: "regular"
group: "['transform']"
---

# Node: Perplexity

**Purpose.** Interact with the Perplexity API to generate AI responses with citations
**Subtitle.** ={{ $parameter["operation"] + ": " + $parameter["resource"] }}


---

## Node Details

- **Icon:** `{'light': 'file:perplexity.svg', 'dark': 'file:perplexity.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **perplexityApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `perplexityApi` | ✓ | - |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | hidden | chat | ✗ | Resource to operate on |  |
---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | hidden | chat | ✗ |  |  |

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Role Assistant and User

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "model": {
    "__rl": true,
    "value": "sonar",
    "mode": "id"
  },
  "messages": {
    "message": [
      {
        "content": "test"
      },
      {
        "content": "test",
        "role": "assistant"
      },
      {
        "content": "aaa"
      }
    ]
  },
  "options": {
    "frequencyPenalty": 1,
    "maxTokens": 4,
    "temperature": 1.99,
    "topK": 4,
    "topP": 1,
    "presencePenalty": 2,
    "returnImages": false,
    "returnRelatedQuestions": false,
    "searchRecency": "month"
  },
  "requestOptions": {}
}
```

**Credentials:**
- perplexityApi: `Perplexity account`


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter["operation"] + ": " + $parameter["resource"] }}`

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
node: perplexity
displayName: Perplexity
description: Interact with the Perplexity API to generate AI responses with citations
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: perplexityApi
  required: true
params:
- id: resource
  name: Resource
  type: hidden
  default: chat
  required: false
  description: ''
  typeInfo:
    type: hidden
    displayName: Resource
    name: resource
examples:
- name: Role Assistant and User
  parameters:
    model:
      __rl: true
      value: sonar
      mode: id
    messages:
      message:
      - content: test
      - content: test
        role: assistant
      - content: aaa
    options:
      frequencyPenalty: 1
      maxTokens: 4
      temperature: 1.99
      topK: 4
      topP: 1
      presencePenalty: 2
      returnImages: false
      returnRelatedQuestions: false
      searchRecency: month
    requestOptions: {}
  workflow: Unnamed workflow
common_expressions:
- '={{ $parameter["operation"] + ": " + $parameter["resource"] }}'
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
  "$id": "https://n8n.io/schemas/nodes/perplexity.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Perplexity Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "default": "chat"
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
      "name": "perplexityApi",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Role Assistant and User",
      "value": {
        "model": {
          "__rl": true,
          "value": "sonar",
          "mode": "id"
        },
        "messages": {
          "message": [
            {
              "content": "test"
            },
            {
              "content": "test",
              "role": "assistant"
            },
            {
              "content": "aaa"
            }
          ]
        },
        "options": {
          "frequencyPenalty": 1,
          "maxTokens": 4,
          "temperature": 1.99,
          "topK": 4,
          "topP": 1,
          "presencePenalty": 2,
          "returnImages": false,
          "returnRelatedQuestions": false,
          "searchRecency": "month"
        },
        "requestOptions": {}
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
