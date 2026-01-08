---
title: "Node: Storyblok"
slug: "node-storyblok"
version: "1"
updated: "2026-01-08"
summary: "Consume Storyblok API"
node_type: "regular"
group: "['output']"
---

# Node: Storyblok

**Purpose.** Consume Storyblok API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:storyblok.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **storyblokContentApi**: N/A
- **storyblokManagementApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `storyblokContentApi` | ✓ | {'show': {'source': ['contentApi']}} |
| `storyblokManagementApi` | ✓ | {'show': {'source': ['managementApi']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Story Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a story |
| Get Many | `getAll` | Get many stories |
| Create | `create` | Create a story |
| Delete | `delete` | Delete a story |
| Publish | `publish` | Publish a story |
| Unpublish | `unpublish` | Unpublish a story |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | story | ✗ | Resource to operate on |  |

**Resource options:**

* **Story** (`story`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Get a story |  |

**Operation options:**

* **Get** (`get`) - Get a story
* **Get Many** (`getAll`) - Get many stories

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Identifier | `identifier` | string |  | ✓ | The ID or slug of the story to get |  |
| Space Name or ID | `space` | options |  | ✓ | The name of the space. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Story ID | `storyId` | string |  | ✓ | Numeric ID of the story |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Filter by slug | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Starts With | `starts_with` | string |  | Filter by slug |

</details>

| Space Name or ID | `space` | options |  | ✓ | The name of the space. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Filter by slug | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Starts With | `starts_with` | string |  | Filter by slug |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Space Name or ID | `space` | options |  | ✓ | The name of the space. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Story ID | `storyId` | string |  | ✓ | Numeric ID of the story |  |

### Publish parameters (`publish`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Space Name or ID | `space` | options |  | ✓ | The name of the space. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Story ID | `storyId` | string |  | ✓ | Numeric ID of the story |  |
| Options | `options` | collection | {} | ✗ | Numeric ID of release | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Release ID | `releaseId` | string |  | Numeric ID of release |
| Language | `language` | string |  | Language code to publish the story individually (must be enabled in the space settings) |

</details>


### Unpublish parameters (`unpublish`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Space Name or ID | `space` | options |  | ✓ | The name of the space. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Story ID | `storyId` | string |  | ✓ | Numeric ID of the story |  |

---

## Load Options Methods

- `getSpaces`

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
* Categories: Data & Storage, Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: storyblok
displayName: Storyblok
description: Consume Storyblok API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: storyblokContentApi
  required: true
- name: storyblokManagementApi
  required: true
operations:
- id: get
  name: Get
  description: Get a story
  params:
  - id: identifier
    name: Identifier
    type: string
    default: ''
    required: true
    description: The ID or slug of the story to get
    validation:
      required: true
      displayOptions:
        show:
          source:
          - contentApi
          resource:
          - story
          operation:
          - get
    typeInfo:
      type: string
      displayName: Identifier
      name: identifier
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: The name of the space. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          source:
          - managementApi
          resource:
          - story
          operation:
          - unpublish
    typeInfo: &id002
      type: options
      displayName: Space Name or ID
      name: space
      typeOptions:
        loadOptionsMethod: getSpaces
      possibleValues: []
  - id: storyId
    name: Story ID
    type: string
    default: ''
    required: true
    description: Numeric ID of the story
    validation: &id007
      required: true
      displayOptions:
        show:
          source:
          - managementApi
          resource:
          - story
          operation:
          - unpublish
    typeInfo: &id008
      type: string
      displayName: Story ID
      name: storyId
- id: getAll
  name: Get Many
  description: Get many stories
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id003
      displayOptions:
        show:
          source:
          - managementApi
          resource:
          - story
          operation:
          - getAll
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          source:
          - managementApi
          resource:
          - story
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: The name of the space. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: create
  name: Create
  description: Create a story
- id: delete
  name: Delete
  description: Delete a story
  params:
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: The name of the space. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: storyId
    name: Story ID
    type: string
    default: ''
    required: true
    description: Numeric ID of the story
    validation: *id007
    typeInfo: *id008
- id: publish
  name: Publish
  description: Publish a story
  params:
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: The name of the space. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: storyId
    name: Story ID
    type: string
    default: ''
    required: true
    description: Numeric ID of the story
    validation: *id007
    typeInfo: *id008
- id: unpublish
  name: Unpublish
  description: Unpublish a story
  params:
  - id: space
    name: Space Name or ID
    type: options
    default: ''
    required: true
    description: The name of the space. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: storyId
    name: Story ID
    type: string
    default: ''
    required: true
    description: Numeric ID of the story
    validation: *id007
    typeInfo: *id008
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: filters
    text: Add Filter
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/storyblok.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Storyblok Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll",
        "create",
        "delete",
        "publish",
        "unpublish"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "source": {
          "description": "Pick where your data comes from, Content or Management API",
          "type": "string",
          "enum": [
            "contentApi",
            "managementApi"
          ],
          "default": "contentApi"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "story"
          ],
          "default": "story"
        },
        "operation": {
          "description": "Create a story",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "publish",
            "unpublish"
          ],
          "default": "get"
        },
        "identifier": {
          "description": "The ID or slug of the story to get",
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
        },
        "filters": {
          "description": "Filter by slug",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "space": {
          "description": "The name of the space. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "The name you give this story.",
          "type": "string",
          "default": ""
        },
        "slug": {
          "description": "The slug/path you give this story.",
          "type": "string",
          "default": ""
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "additionalFields": {
          "description": "Add Content",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "storyId": {
          "description": "Numeric ID of the story",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Numeric ID of release",
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
    "version": "1"
  },
  "credentials": [
    {
      "name": "storyblokContentApi",
      "required": true
    },
    {
      "name": "storyblokManagementApi",
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
