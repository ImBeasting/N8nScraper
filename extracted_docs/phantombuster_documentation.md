---
title: "Node: Phantombuster"
slug: "node-phantombuster"
version: "1"
updated: "2026-01-08"
summary: "Consume Phantombuster API"
node_type: "regular"
group: "['input']"
---

# Node: Phantombuster

**Purpose.** Consume Phantombuster API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:phantombuster.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **phantombusterApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `phantombusterApi` | ✓ | - |

---

## Operations

### Agent Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete an agent by ID |
| Get | `get` | Get an agent by ID |
| Get Many | `getAll` | Get many agents of the current user's organization |
| Get Output | `getOutput` | Get the output of the most recent container of an agent |
| Launch | `launch` | Add an agent to the launch queue |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | agent | ✗ | Resource to operate on |  |

**Resource options:**

* **Agent** (`agent`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | launch | ✗ | Delete an agent by ID |  |

**Operation options:**

* **Delete** (`delete`) - Delete an agent by ID
* **Get** (`get`) - Get an agent by ID
* **Get Many** (`getAll`) - Get many agents of the current user's organization
* **Get Output** (`getOutput`) - Get the output of the most recent container of an agent
* **Launch** (`launch`) - Add an agent to the launch queue

---

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Agent Name or ID | `agentId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Agent ID | `agentId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 25 | ✗ | Max number of results to return | min:1, max:50 |

### Get Output parameters (`getOutput`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Agent Name or ID | `agentId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Resolve Data | `resolveData` | boolean | True | ✗ | By default the outpout is presented as string. If this option gets activated, it will resolve the data automatically. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | If set, the output will be retrieved from the container after the specified previous container ID | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Prev Container ID | `prevContainerId` | string |  | If set, the output will be retrieved from the container after the specified previous container ID |
| Prev Status | `prevStatus` | options |  | If set, allows to define which status was previously retrieved on user-side |
| Pre Runtime Event Index | `prevRuntimeEventIndex` | number | 0 | If set, the container's runtime events will be returned in the response starting from the provided previous runtime event index |

</details>


### Launch parameters (`launch`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Agent Name or ID | `agentId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Resolve Data | `resolveData` | boolean | True | ✗ | By default the launch just include the container ID. If this option gets activated, it will resolve the data automatically. |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Agent argument. Can either be a JSON string or a plain object. The argument can be retrieved with buster.argument in the agent’s script. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Arguments (JSON) | `argumentsJson` | json |  | Agent argument. Can either be a JSON string or a plain object. The argument can be retrieved with buster.argument in the agent’s script. |
| Arguments | `argumentsUi` | fixedCollection | {} | Name of the argument key to add |
| Bonus Argument | `bonusArgumentUi` | fixedCollection | {} | Name of the argument key to add |
| Bonus Argument (JSON) | `bonusArgumentJson` | string |  | Agent bonus argument. Can either be a JSON string or a plain object. This bonus argument is single-use, it will only be used for the current launch. If present, it will be merged with the original argument, resulting in an effective argument that can be retrieved with buster.argument in the agent’s script. |
| Manual Launch | `manualLaunch` | boolean | False | Whether the agent will be considered as "launched manually" |
| Max Instance Count | `maxInstanceCount` | number | 0 | If set, the agent will only be launched if the number of already running instances is below the specified number |
| Save Argument | `saveArgument` | string |  | If true, argument will be saved as the default launch options for the agent |

</details>


---

## Load Options Methods

- `getAgents`
- `for`
- `name`
- `value`

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Phantombuster

**From workflow:** Phantombuster Launch With JSON Arguments Test

**Parameters:**
```json
{
  "resource": "agent",
  "operation": "launch",
  "agentId": "test-agent-123",
  "jsonParameters": true,
  "resolveData": false,
  "additionalFields": {
    "argumentsJson": "{\"complexKey\":\"complexValue\",\"nestedObject\":{\"nested\":\"value\"}}"
  }
}
```

**Credentials:**
- phantombusterApi: `Phantombuster API`

### Example 2: Phantombuster

**From workflow:** Phantombuster Launch With Bonus Arguments Test

**Parameters:**
```json
{
  "resource": "agent",
  "operation": "launch",
  "agentId": "test-agent-123",
  "jsonParameters": false,
  "resolveData": false,
  "additionalFields": {
    "argumentsUi": {
      "argumentValues": [
        {
          "key": "testKey",
          "value": "testValue"
        }
      ]
    },
    "bonusArgumentUi": {
      "bonusArgumentValue": [
        {
          "key": "bonusKey",
          "value": "bonusValue"
        }
      ]
    }
  }
}
```

**Credentials:**
- phantombusterApi: `Phantombuster API`

### Example 3: Phantombuster

**From workflow:** Phantombuster Launch With Arguments No Bonus Test

**Parameters:**
```json
{
  "resource": "agent",
  "operation": "launch",
  "agentId": "test-agent-123",
  "jsonParameters": false,
  "resolveData": false,
  "additionalFields": {
    "argumentsUi": {
      "argumentValues": [
        {
          "key": "testKey",
          "value": "testValue"
        }
      ]
    }
  }
}
```

**Credentials:**
- phantombusterApi: `Phantombuster API`

### Example 4: Phantombuster

**From workflow:** Phantombuster Launch Without Arguments Test

**Parameters:**
```json
{
  "resource": "agent",
  "operation": "launch",
  "agentId": "test-agent-123",
  "jsonParameters": false,
  "resolveData": false
}
```

**Credentials:**
- phantombusterApi: `Phantombuster API`


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
* Categories: Sales, Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: phantombuster
displayName: Phantombuster
description: Consume Phantombuster API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: phantombusterApi
  required: true
operations:
- id: delete
  name: Delete
  description: Delete an agent by ID
  params:
  - id: agentId
    name: Agent Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - launch
          resource:
          - agent
    typeInfo: &id002
      type: options
      displayName: Agent Name or ID
      name: agentId
      typeOptions:
        loadOptionsMethod: getAgents
      possibleValues: []
- id: get
  name: Get
  description: Get an agent by ID
  params:
  - id: agentId
    name: Agent ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many agents of the current user's organization
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
          - agent
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 25
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - agent
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 50
- id: getOutput
  name: Get Output
  description: Get the output of the most recent container of an agent
  params:
  - id: agentId
    name: Agent Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: resolveData
    name: Resolve Data
    type: boolean
    default: true
    required: false
    description: By default the outpout is presented as string. If this option gets
      activated, it will resolve the data automatically.
    validation: &id003
      displayOptions:
        show:
          operation:
          - launch
          resource:
          - agent
    typeInfo: &id004
      type: boolean
      displayName: Resolve Data
      name: resolveData
- id: launch
  name: Launch
  description: Add an agent to the launch queue
  params:
  - id: agentId
    name: Agent Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: resolveData
    name: Resolve Data
    type: boolean
    default: true
    required: false
    description: By default the launch just include the container ID. If this option
      gets activated, it will resolve the data automatically.
    validation: *id003
    typeInfo: *id004
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - launch
          resource:
          - agent
    typeInfo:
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
examples:
- name: Phantombuster
  parameters:
    resource: agent
    operation: launch
    agentId: test-agent-123
    jsonParameters: true
    resolveData: false
    additionalFields:
      argumentsJson: '{"complexKey":"complexValue","nestedObject":{"nested":"value"}}'
  workflow: Phantombuster Launch With JSON Arguments Test
- name: Phantombuster
  parameters:
    resource: agent
    operation: launch
    agentId: test-agent-123
    jsonParameters: false
    resolveData: false
    additionalFields:
      argumentsUi:
        argumentValues:
        - key: testKey
          value: testValue
      bonusArgumentUi:
        bonusArgumentValue:
        - key: bonusKey
          value: bonusValue
  workflow: Phantombuster Launch With Bonus Arguments Test
- name: Phantombuster
  parameters:
    resource: agent
    operation: launch
    agentId: test-agent-123
    jsonParameters: false
    resolveData: false
    additionalFields:
      argumentsUi:
        argumentValues:
        - key: testKey
          value: testValue
  workflow: Phantombuster Launch With Arguments No Bonus Test
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
  placeholders:
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/phantombuster.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Phantombuster Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "delete",
        "get",
        "getAll",
        "getOutput",
        "launch"
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
            "agent"
          ],
          "default": "agent"
        },
        "operation": {
          "description": "Delete an agent by ID",
          "type": "string",
          "enum": [
            "delete",
            "get",
            "getAll",
            "getOutput",
            "launch"
          ],
          "default": "launch"
        },
        "agentId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
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
          "default": 25
        },
        "resolveData": {
          "description": "By default the launch just include the container ID. If this option gets activated, it will resolve the data automatically.",
          "type": "boolean",
          "default": true
        },
        "additionalFields": {
          "description": "Agent argument. Can either be a JSON string or a plain object. The argument can be retrieved with buster.argument in the agent\u2019s script.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "jsonParameters": {
          "description": "",
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
    "version": "1"
  },
  "credentials": [
    {
      "name": "phantombusterApi",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Phantombuster",
      "value": {
        "resource": "agent",
        "operation": "launch",
        "agentId": "test-agent-123",
        "jsonParameters": true,
        "resolveData": false,
        "additionalFields": {
          "argumentsJson": "{\"complexKey\":\"complexValue\",\"nestedObject\":{\"nested\":\"value\"}}"
        }
      }
    },
    {
      "description": "Phantombuster",
      "value": {
        "resource": "agent",
        "operation": "launch",
        "agentId": "test-agent-123",
        "jsonParameters": false,
        "resolveData": false,
        "additionalFields": {
          "argumentsUi": {
            "argumentValues": [
              {
                "key": "testKey",
                "value": "testValue"
              }
            ]
          },
          "bonusArgumentUi": {
            "bonusArgumentValue": [
              {
                "key": "bonusKey",
                "value": "bonusValue"
              }
            ]
          }
        }
      }
    },
    {
      "description": "Phantombuster",
      "value": {
        "resource": "agent",
        "operation": "launch",
        "agentId": "test-agent-123",
        "jsonParameters": false,
        "resolveData": false,
        "additionalFields": {
          "argumentsUi": {
            "argumentValues": [
              {
                "key": "testKey",
                "value": "testValue"
              }
            ]
          }
        }
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
