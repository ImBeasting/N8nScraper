---
title: "Node: Disqus"
slug: "node-disqus"
version: "1"
updated: "2026-01-08"
summary: "Access data on Disqus"
node_type: "regular"
group: "['input']"
---

# Node: Disqus

**Purpose.** Access data on Disqus
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:disqus.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **disqusApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `disqusApi` | ✓ | - |

---

## Operations

### Forum Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Return forum details |
| Get All Categories | `getCategories` | Return a list of categories within a forum |
| Get All Threads | `getThreads` | Return a list of threads within a forum |
| Get All Posts | `getPosts` | Return a list of posts within a forum |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | forum | ✗ | Resource to operate on |  |

**Resource options:**

* **Forum** (`forum`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Return forum details |  |

**Operation options:**

* **Get** (`get`) - Return forum details
* **Get All Categories** (`getCategories`) - Return a list of categories within a forum
* **Get All Threads** (`getThreads`) - Return a list of threads within a forum
* **Get All Posts** (`getPosts`) - Return a list of posts within a forum

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Forum Name | `id` | string |  | ✓ | The short name(aka ID) of the forum to get |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | You may specify relations to include with your response | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attach | `attach` | multiOptions | [] |  |
| Related | `related` | multiOptions | [] | You may specify relations to include with your response |

</details>


### Get All Categories parameters (`getCategories`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Forum Name | `id` | string |  | ✓ | The short name(aka ID) of the forum to get Categories |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | You may specify order to sort your response | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Order | `order` | options | asc | You may specify order to sort your response |

</details>


### Get All Threads parameters (`getThreads`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Forum Name | `id` | string |  | ✓ | The short name(aka ID) of the forum to get Threads |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | You may specify relations to include with your response | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Related | `related` | multiOptions | [] | You may specify relations to include with your response |
| Include | `include` | multiOptions | [] | You may specify relations to include with your response |
| Order | `order` | options | asc | You may specify order to sort your response |
| Since | `since` | dateTime |  | Unix timestamp (or ISO datetime standard) |
| Thread | `thread` | string |  | Looks up a thread by ID. You may pass us the "ident" query type instead of an ID by including "forum". You may pass us the "link" query type to filter by URL. You must pass the "forum" if you do not have the Pro API Access addon. |

</details>


### Get All Posts parameters (`getPosts`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Forum Name | `id` | string |  | ✓ | The short name(aka ID) of the forum to get |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | You may specify filters for your response | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filters | `filters` | multiOptions | [] | You may specify filters for your response |
| Include | `include` | multiOptions | [] | You may specify relations to include with your response |
| Order | `order` | options | asc | You may specify order to sort your response |
| Query | `query` | string |  | You may specify query forChoices: asc, desc your response |
| Related | `related` | multiOptions | [] | You may specify relations to include with your response |
| Since | `since` | dateTime |  | Unix timestamp (or ISO datetime standard) |

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
* Categories: Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: disqus
displayName: Disqus
description: Access data on Disqus
version: '1'
nodeType: regular
group:
- input
credentials:
- name: disqusApi
  required: true
operations:
- id: get
  name: Get
  description: Return forum details
  params:
  - id: id
    name: Forum Name
    type: string
    default: ''
    required: true
    description: The short name(aka ID) of the forum to get
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - getThreads
          resource:
          - forum
    typeInfo: &id002
      type: string
      displayName: Forum Name
      name: id
- id: getCategories
  name: Get All Categories
  description: Return a list of categories within a forum
  params:
  - id: id
    name: Forum Name
    type: string
    default: ''
    required: true
    description: The short name(aka ID) of the forum to get Categories
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id003
      displayOptions:
        show:
          resource:
          - forum
          operation:
          - getThreads
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          resource:
          - forum
          operation:
          - getThreads
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
- id: getThreads
  name: Get All Threads
  description: Return a list of threads within a forum
  params:
  - id: id
    name: Forum Name
    type: string
    default: ''
    required: true
    description: The short name(aka ID) of the forum to get Threads
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: getPosts
  name: Get All Posts
  description: Return a list of posts within a forum
  params:
  - id: id
    name: Forum Name
    type: string
    default: ''
    required: true
    description: The short name(aka ID) of the forum to get
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
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
  "$id": "https://n8n.io/schemas/nodes/disqus.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Disqus Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getCategories",
        "getThreads",
        "getPosts"
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
            "forum"
          ],
          "default": "forum"
        },
        "operation": {
          "description": "Return forum details",
          "type": "string",
          "enum": [
            "get",
            "getCategories",
            "getThreads",
            "getPosts"
          ],
          "default": "get"
        },
        "id": {
          "description": "The short name(aka ID) of the forum to get Threads",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "You may specify relations to include with your response",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
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
      "name": "disqusApi",
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
