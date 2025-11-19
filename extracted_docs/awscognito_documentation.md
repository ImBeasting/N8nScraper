---
title: "Node: AWS Cognito"
slug: "node-awscognito"
version: "1"
updated: "2025-11-13"
summary: "Sends data to AWS Cognito"
node_type: "regular"
group: "['output']"
---

# Node: AWS Cognito

**Purpose.** Sends data to AWS Cognito
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:cognito.svg', 'dark': 'file:cognito.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **aws**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `aws` | ✓ | - |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | user | ✗ | Resource to operate on |  |

**Resource options:**

* **Group** (`group`)
* **User** (`user`)
* **User Pool** (`userPool`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | user | ✗ |  |  |

**Resource options:**

* **Group** (`group`)
* **User** (`user`)
* **User Pool** (`userPool`)


---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: getAllGroups

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "group",
  "userPool": {
    "__rl": true,
    "value": "eu-central-1_KkXQgdCJv",
    "mode": "list",
    "cachedResultName": "AWS test"
  },
  "returnAll": true,
  "includeUsers": true,
  "requestOptions": {}
}
```

**Credentials:**
- aws: `AWS account Central Europe`

### Example 2: AWS Cognito1

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "group",
  "operation": "delete",
  "userPool": {
    "__rl": true,
    "value": "eu-central-1_qqle3XBUA",
    "mode": "list",
    "cachedResultName": "UserPoolThree"
  },
  "group": {
    "__rl": true,
    "value": "MyNewGroup22",
    "mode": "list",
    "cachedResultName": "MyNewGroup22"
  },
  "requestOptions": {}
}
```

**Credentials:**
- aws: `AWS account Central Europe`

### Example 3: updateGroup

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "group",
  "operation": "update",
  "userPool": {
    "__rl": true,
    "value": "eu-central-1_KkXQgdCJv",
    "mode": "list",
    "cachedResultName": "AWS test"
  },
  "group": {
    "__rl": true,
    "value": "MyNewTesttttt",
    "mode": "list",
    "cachedResultName": "MyNewTesttttt"
  },
  "additionalFields": {
    "description": "Updated description"
  },
  "requestOptions": {}
}
```

**Credentials:**
- aws: `AWS account Central Europe`

### Example 4: AWS Cognito1

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "group",
  "operation": "get",
  "userPool": {
    "__rl": true,
    "value": "eu-central-1_qqle3XBUA",
    "mode": "list",
    "cachedResultName": "UserPoolThree"
  },
  "group": {
    "__rl": true,
    "value": "MyNewGroup2",
    "mode": "list",
    "cachedResultName": "MyNewGroup2"
  },
  "requestOptions": {}
}
```

**Credentials:**
- aws: `AWS account Central Europe`

### Example 5: createGroup

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "group",
  "operation": "create",
  "userPool": {
    "__rl": true,
    "value": "eu-central-1_qqle3XBUA",
    "mode": "list",
    "cachedResultName": "UserPoolThree"
  },
  "newGroupName": "MyNewGroup11",
  "additionalFields": {},
  "requestOptions": {}
}
```

**Credentials:**
- aws: `AWS account Central Europe`


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$credentials.region}}`
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
node: awsCognito
displayName: AWS Cognito
description: Sends data to AWS Cognito
version: '1'
nodeType: regular
group:
- output
credentials:
- name: aws
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: user
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: group
      name: Group
      description: ''
    - value: user
      name: User
      description: ''
    - value: userPool
      name: User Pool
      description: ''
examples:
- name: getAllGroups
  parameters:
    resource: group
    userPool:
      __rl: true
      value: eu-central-1_KkXQgdCJv
      mode: list
      cachedResultName: AWS test
    returnAll: true
    includeUsers: true
    requestOptions: {}
  workflow: Unnamed workflow
- name: AWS Cognito1
  parameters:
    resource: group
    operation: delete
    userPool:
      __rl: true
      value: eu-central-1_qqle3XBUA
      mode: list
      cachedResultName: UserPoolThree
    group:
      __rl: true
      value: MyNewGroup22
      mode: list
      cachedResultName: MyNewGroup22
    requestOptions: {}
  workflow: Unnamed workflow
- name: updateGroup
  parameters:
    resource: group
    operation: update
    userPool:
      __rl: true
      value: eu-central-1_KkXQgdCJv
      mode: list
      cachedResultName: AWS test
    group:
      __rl: true
      value: MyNewTesttttt
      mode: list
      cachedResultName: MyNewTesttttt
    additionalFields:
      description: Updated description
    requestOptions: {}
  workflow: Unnamed workflow
common_expressions:
- ={{$credentials.region}}
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
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
  "$id": "https://n8n.io/schemas/nodes/awsCognito.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AWS Cognito Node",
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
          "enum": [
            "group",
            "user",
            "userPool"
          ],
          "default": "user"
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
      "name": "aws",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "getAllGroups",
      "value": {
        "resource": "group",
        "userPool": {
          "__rl": true,
          "value": "eu-central-1_KkXQgdCJv",
          "mode": "list",
          "cachedResultName": "AWS test"
        },
        "returnAll": true,
        "includeUsers": true,
        "requestOptions": {}
      }
    },
    {
      "description": "AWS Cognito1",
      "value": {
        "resource": "group",
        "operation": "delete",
        "userPool": {
          "__rl": true,
          "value": "eu-central-1_qqle3XBUA",
          "mode": "list",
          "cachedResultName": "UserPoolThree"
        },
        "group": {
          "__rl": true,
          "value": "MyNewGroup22",
          "mode": "list",
          "cachedResultName": "MyNewGroup22"
        },
        "requestOptions": {}
      }
    },
    {
      "description": "updateGroup",
      "value": {
        "resource": "group",
        "operation": "update",
        "userPool": {
          "__rl": true,
          "value": "eu-central-1_KkXQgdCJv",
          "mode": "list",
          "cachedResultName": "AWS test"
        },
        "group": {
          "__rl": true,
          "value": "MyNewTesttttt",
          "mode": "list",
          "cachedResultName": "MyNewTesttttt"
        },
        "additionalFields": {
          "description": "Updated description"
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
