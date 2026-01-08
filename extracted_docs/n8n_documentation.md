---
title: "Node: n8n"
slug: "node-n8n"
version: "1"
updated: "2026-01-08"
summary: "Handle events and perform actions on your n8n instance"
node_type: "regular"
group: "['transform']"
---

# Node: n8n

**Purpose.** Handle events and perform actions on your n8n instance
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:n8n.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **n8nApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `n8nApi` | ✓ | - |

---

## Operations

### Audit Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Generate | `generate` | Generate a security audit for this n8n instance |

### Credential Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a credential |
| Delete | `delete` | Delete a credential |
| Get Schema | `getSchema` | Get credential data schema for type |

### Execution Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get an execution |
| Get Many | `getAll` | Get many executions |
| Delete | `delete` | Delete an execution |

### Workflow Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Publish | `activate` | Publish a workflow |
| Create | `create` | Create a workflow |
| Unpublish | `deactivate` | Unpublish a workflow |
| Delete | `delete` | Delete a workflow |
| Get | `get` | Get a workflow |
| Get Many | `getAll` | Get many workflows |
| Get Version | `getVersion` | Get a workflow version |
| Update | `update` | Update a workflow |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | workflow | ✗ | Resource to operate on |  |

**Resource options:**

* **Audit** (`audit`)
* **Credential** (`credential`)
* **Execution** (`execution`)
* **Workflow** (`workflow`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Generate a security audit for this n8n instance |  |

**Operation options:**

* **Generate** (`generate`) - Generate a security audit for this n8n instance

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Name of the new credential | e.g. e.g. n8n account |  |
| Credential Type | `credentialTypeName` | string |  | ✓ | The available types depend on nodes installed on the n8n instance. Some built-in types include e.g. 'githubApi', 'notionApi', and 'slackApi'. | e.g. e.g. n8nApi |  |
| Data | `data` | json |  | ✓ | A valid JSON object with properties required for this Credential Type. To see the expected format, you can use 'Get Schema' operation. | e.g. // e.g. for n8nApi n{n  "apiKey": "my-n8n-api-key",n  "baseUrl": "https://<name>.app.n8n.cloud/api/v1",n} |  |
| Workflow Object | `workflowObject` | json | {  | ✓ | A valid JSON object with required fields: 'name', 'nodes', 'connections' and 'settings'. More information can be found in the <a href="https://docs.n8n.io/api/api-reference/#tag/workflow/paths/~1workflows/post">documentation</a>. | e.g. {n  "name": "My workflow",n  "nodes": [],n  "connections": {},n  "settings": {}n} |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Credential ID | `credentialId` | string |  | ✓ |  |  |
| Execution ID | `executionId` | string |  | ✓ |  |  |

### Get Schema parameters (`getSchema`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Credential Type | `credentialTypeName` | string |  | ✓ | The available types depend on nodes installed on the n8n instance. Some built-in types include e.g. 'githubApi', 'notionApi', and 'slackApi'. | e.g. e.g. n8nApi |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Execution ID | `executionId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | Whether to include the detailed execution data | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Execution Details | `activeWorkflows` | boolean | False | Whether to include the detailed execution data |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Filters | `filters` | collection | {} | ✗ | Workflow to filter the executions by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Status | `status` | options | success | Status to filter the executions by |

</details>

| Options | `options` | collection | {} | ✗ | Whether to include the detailed execution data | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Execution Details | `activeWorkflows` | boolean | False | Whether to include the detailed execution data |

</details>

| Return All | `returnAll` | boolean | True | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Filters | `filters` | collection | {} | ✗ | Include only workflows with these tags | e.g. Comma separated list of tags (empty value is ignored) |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Return Only Published Workflows | `activeWorkflows` | boolean | True |  |
| Tags | `tags` | string |  | Include only workflows with these tags |
| Name | `name` | string |  |  |
| Project ID | `projectId` | string |  |  |
| Exclude Pinned Data | `excludePinnedData` | boolean | False | Whether to exclude pinned data from the response |

</details>


### Publish parameters (`activate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The version ID of the workflow to publish | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Version ID | `versionId` | string |  | The version ID of the workflow to publish |
| Name | `name` | string |  | Published version name (will be overwritten) |
| Description | `description` | string |  | Published version description (will be overwritten) |

</details>


### Get Version parameters (`getVersion`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Version ID | `versionId` | string |  | ✓ | The version ID to retrieve |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workflow Object | `workflowObject` | json |  | ✓ | A valid JSON object with required fields: 'name', 'nodes', 'connections' and 'settings'. More information can be found in the <a href="https://docs.n8n.io/api/api-reference/#tag/workflow/paths/~1workflows~1%7bid%7d/put">documentation</a>. | e.g. {n  "name": "My workflow",n  "nodes": [],n  "connections": {},n  "settings": {}n} |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $credentials.baseUrl.replace(new RegExp("/$"), "") }}`
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
* Categories: Development, Core Nodes
* Aliases: Workflow, Execution

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: n8n
displayName: n8n
description: Handle events and perform actions on your n8n instance
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: n8nApi
  required: true
operations:
- id: generate
  name: Generate
  description: Generate a security audit for this n8n instance
- id: create
  name: Create
  description: ''
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the new credential
    placeholder: e.g. n8n account
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - credential
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: credentialTypeName
    name: Credential Type
    type: string
    default: ''
    required: true
    description: The available types depend on nodes installed on the n8n instance.
      Some built-in types include e.g. 'githubApi', 'notionApi', and 'slackApi'.
    placeholder: e.g. n8nApi
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - credential
          operation:
          - getSchema
    typeInfo: &id002
      type: string
      displayName: Credential Type
      name: credentialTypeName
  - id: data
    name: Data
    type: json
    default: ''
    required: true
    description: A valid JSON object with properties required for this Credential
      Type. To see the expected format, you can use 'Get Schema' operation.
    placeholder: '// e.g. for n8nApi n{n  "apiKey": "my-n8n-api-key",n  "baseUrl":
      "https://<name>.app.n8n.cloud/api/v1",n}'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - credential
          operation:
          - create
    typeInfo:
      type: json
      displayName: Data
      name: data
      typeOptions:
        alwaysOpenEditWindow: true
  - id: workflowObject
    name: Workflow Object
    type: json
    default: '{ '
    required: true
    description: 'A valid JSON object with required fields: ''name'', ''nodes'', ''connections''
      and ''settings''. More information can be found in the <a href="https://docs.n8n.io/api/api-reference/#tag/workflow/paths/~1workflows/post">documentation</a>.'
    placeholder: '{n  "name": "My workflow",n  "nodes": [],n  "connections": {},n  "settings":
      {}n}'
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - workflow
          operation:
          - update
    typeInfo: &id010
      type: json
      displayName: Workflow Object
      name: workflowObject
      typeOptions:
        alwaysOpenEditWindow: true
- id: delete
  name: Delete
  description: ''
  params:
  - id: credentialId
    name: Credential ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - credential
          operation:
          - delete
    typeInfo:
      type: string
      displayName: Credential ID
      name: credentialId
  - id: executionId
    name: Execution ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - execution
          operation:
          - get
    typeInfo: &id004
      type: string
      displayName: Execution ID
      name: executionId
- id: getSchema
  name: Get Schema
  description: ''
  params:
  - id: credentialTypeName
    name: Credential Type
    type: string
    default: ''
    required: true
    description: The available types depend on nodes installed on the n8n instance.
      Some built-in types include e.g. 'githubApi', 'notionApi', and 'slackApi'.
    placeholder: e.g. n8nApi
    validation: *id001
    typeInfo: *id002
- id: get
  name: Get
  description: ''
  params:
  - id: executionId
    name: Execution ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id005
      displayOptions:
        show:
          resource:
          - workflow
          operation:
          - getAll
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          resource:
          - workflow
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id008
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 250
  - id: returnAll
    name: Return All
    type: boolean
    default: true
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: activate
  name: Publish
  description: ''
  params: []
- id: deactivate
  name: Unpublish
  description: ''
- id: getVersion
  name: Get Version
  description: ''
  params:
  - id: versionId
    name: Version ID
    type: string
    default: ''
    required: true
    description: The version ID to retrieve
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - workflow
          operation:
          - getVersion
    typeInfo:
      type: string
      displayName: Version ID
      name: versionId
- id: update
  name: Update
  description: ''
  params:
  - id: workflowObject
    name: Workflow Object
    type: json
    default: ''
    required: true
    description: 'A valid JSON object with required fields: ''name'', ''nodes'', ''connections''
      and ''settings''. More information can be found in the <a href="https://docs.n8n.io/api/api-reference/#tag/workflow/paths/~1workflows~1%7bid%7d/put">documentation</a>.'
    placeholder: '{n  "name": "My workflow",n  "nodes": [],n  "connections": {},n  "settings":
      {}n}'
    validation: *id009
    typeInfo: *id010
common_expressions:
- ={{ $credentials.baseUrl.replace(new RegExp("/$"), "") }}
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
  - field: additionalOptions
    text: Add Filter
  - field: name
    text: e.g. n8n account
  - field: credentialTypeName
    text: e.g. n8nApi
  - field: data
    text: '// e.g. for n8nApi n{n  "apiKey": "my-n8n-api-key",n  "baseUrl": "https://<name>.app.n8n.cloud/api/v1",n}'
  - field: credentialTypeName
    text: e.g. n8nApi
  - field: filters
    text: Add Filter
  - field: options
    text: Add option
  - field: workflowId
    text: Select a Workflow...
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: workflowObject
    text: '{n  "name": "My workflow",n  "nodes": [],n  "connections": {},n  "settings":
      {}n}'
  - field: workflowObject
    text: '{n  "name": "My workflow",n  "nodes": [],n  "connections": {},n  "settings":
      {}n}'
  hints:
  - field: filters
    text: Comma separated list of tags (empty value is ignored)
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
  "$id": "https://n8n.io/schemas/nodes/n8n.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "n8n Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "generate",
        "create",
        "delete",
        "getSchema",
        "get",
        "getAll",
        "activate",
        "deactivate",
        "getVersion",
        "update"
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
            "audit",
            "credential",
            "execution",
            "workflow"
          ],
          "default": "workflow"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "activate",
            "create",
            "deactivate",
            "delete",
            "get",
            "getAll",
            "getVersion",
            "update"
          ],
          "default": "getAll"
        },
        "additionalOptions": {
          "description": "Risk categories to include in the audit",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "name": {
          "description": "Name of the new credential",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. n8n account"
          ]
        },
        "credentialTypeName": {
          "description": "The available types depend on nodes installed on the n8n instance. Some built-in types include e.g. 'githubApi', 'notionApi', and 'slackApi'.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. n8nApi"
          ]
        },
        "data": {
          "description": "A valid JSON object with properties required for this Credential Type. To see the expected format, you can use 'Get Schema' operation.",
          "type": "string",
          "default": "",
          "examples": [
            "// e.g. for n8nApi n{n  \"apiKey\": \"my-n8n-api-key\",n  \"baseUrl\": \"https://<name>.app.n8n.cloud/api/v1\",n}"
          ]
        },
        "credentialId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "executionId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": true
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
        },
        "filters": {
          "description": "Include only workflows with these tags",
          "type": "string",
          "default": {}
        },
        "options": {
          "description": "Whether to include the detailed execution data",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "workflowId": {
          "description": "Workflow to filter the executions by",
          "type": "string",
          "examples": [
            "Select a Workflow..."
          ]
        },
        "additionalFields": {
          "description": "The version ID of the workflow to publish",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "workflowObject": {
          "description": "A valid JSON object with required fields: 'name', 'nodes', 'connections' and 'settings'. More information can be found in the <a href=\"https://docs.n8n.io/api/api-reference/#tag/workflow/paths/~1workflows~1%7bid%7d/put\">documentation</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "{n  \"name\": \"My workflow\",n  \"nodes\": [],n  \"connections\": {},n  \"settings\": {}n}"
          ]
        },
        "versionId": {
          "description": "The version ID to retrieve",
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
      "name": "n8nApi",
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
