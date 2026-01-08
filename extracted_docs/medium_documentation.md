---
title: "Node: Medium"
slug: "node-medium"
version: "1"
updated: "2026-01-08"
summary: "Consume Medium API"
node_type: "regular"
group: "['output']"
---

# Node: Medium

**Purpose.** Consume Medium API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:medium.png`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **mediumApi**: N/A
- **mediumOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `mediumApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `mediumOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type, Accept-Charset

---

## Operations

### Post Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a post |

### Publication Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many publications |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | post | ✗ | Resource to operate on |  |

**Resource options:**

* **Post** (`post`)
* **Publication** (`publication`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a post |  |

**Operation options:**

* **Create** (`create`) - Create a post

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Publication | `publication` | boolean | False | ✗ | Whether you are posting for a publication |  |
| Publication Name or ID | `publicationId` | options |  | ✗ | Publication IDs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Title | `title` | string |  | ✓ | Title of the post. Max Length : 100 characters. | e.g. My Open Source Contribution |  |
| Content Format | `contentFormat` | options |  | ✓ | The format of the content to be posted |  |

**Content Format options:**

* **HTML** (`html`)
* **Markdown** (`markdown`)

| Content | `content` | string |  | ✓ | The body of the post, in a valid semantic HTML fragment, or Markdown | e.g. My open source contribution |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The original home of this content, if it was originally published elsewhere | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Canonical Url | `canonicalUrl` | string |  | The original home of this content, if it was originally published elsewhere |
| License | `license` | options | all-rights-reserved | License of the post |
| Notify Followers | `notifyFollowers` | boolean | False | Whether to notify followers that the user has published |
| Publish Status | `publishStatus` | options | public | The status of the post |
| Tags | `tags` | string |  | Comma-separated strings to be used as tags for post classification. Max allowed tags: 5. Max tag length: 25 characters. |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |

---

## Load Options Methods

- `getPublications`

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
* Categories: Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: medium
displayName: Medium
description: Consume Medium API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: mediumApi
  required: true
- name: mediumOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a post
  params:
  - id: publication
    name: Publication
    type: boolean
    default: false
    required: false
    description: Whether you are posting for a publication
    validation:
      displayOptions:
        show:
          resource:
          - post
          operation:
          - create
    typeInfo:
      type: boolean
      displayName: Publication
      name: publication
  - id: publicationId
    name: Publication Name or ID
    type: options
    default: ''
    required: false
    description: Publication IDs. Choose from the list, or specify an ID using an
      <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      displayOptions:
        show:
          resource:
          - post
          operation:
          - create
          publication:
          - true
    typeInfo:
      type: options
      displayName: Publication Name or ID
      name: publicationId
      typeOptions:
        loadOptionsMethod: getPublications
      possibleValues: []
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: 'Title of the post. Max Length : 100 characters.'
    placeholder: My Open Source Contribution
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - post
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: contentFormat
    name: Content Format
    type: options
    default: ''
    required: true
    description: The format of the content to be posted
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - post
    typeInfo:
      type: options
      displayName: Content Format
      name: contentFormat
      possibleValues:
      - value: html
        name: HTML
        description: ''
      - value: markdown
        name: Markdown
        description: ''
  - id: content
    name: Content
    type: string
    default: ''
    required: true
    description: The body of the post, in a valid semantic HTML fragment, or Markdown
    placeholder: My open source contribution
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - post
    typeInfo:
      type: string
      displayName: Content
      name: content
- id: getAll
  name: Get Many
  description: Get many publications
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
          - publication
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - publication
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 200
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  - Accept-Charset
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: title
    text: My Open Source Contribution
  - field: content
    text: My open source contribution
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
  "$id": "https://n8n.io/schemas/nodes/medium.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Medium Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "getAll"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "accessToken",
            "oAuth2"
          ],
          "default": "accessToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "post",
            "publication"
          ],
          "default": "post"
        },
        "operation": {
          "description": "Get many publications",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "publication"
        },
        "publication": {
          "description": "Whether you are posting for a publication",
          "type": "boolean",
          "default": false
        },
        "publicationId": {
          "description": "Publication IDs. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "Title of the post. Max Length : 100 characters.",
          "type": "string",
          "default": "",
          "examples": [
            "My Open Source Contribution"
          ]
        },
        "contentFormat": {
          "description": "The format of the content to be posted",
          "type": "string",
          "enum": [
            "html",
            "markdown"
          ],
          "default": ""
        },
        "content": {
          "description": "The body of the post, in a valid semantic HTML fragment, or Markdown",
          "type": "string",
          "default": "",
          "examples": [
            "My open source contribution"
          ]
        },
        "additionalFields": {
          "description": "The original home of this content, if it was originally published elsewhere",
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
      "name": "mediumApi",
      "required": true
    },
    {
      "name": "mediumOAuth2Api",
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
