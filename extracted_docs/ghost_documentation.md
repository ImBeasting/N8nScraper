---
title: "Node: Ghost"
slug: "node-ghost"
version: "1"
updated: "2025-11-13"
summary: "Consume Ghost API"
node_type: "regular"
group: "['input']"
---

# Node: Ghost

**Purpose.** Consume Ghost API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:ghost.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **ghostAdminApi**: N/A
- **ghostContentApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `ghostAdminApi` | ✓ | {'show': {'source': ['adminApi']}} |
| `ghostContentApi` | ✓ | {'show': {'source': ['contentApi']}} |

---

## Operations

### Post Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a post |
| Get Many | `getAll` | Get many posts |
| Create | `create` | Create a post |
| Delete | `delete` | Delete a post |
| Update | `update` | Update a post |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | post | ✗ | Resource to operate on |  |

**Resource options:**

* **Post** (`post`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Get a post |  |

**Operation options:**

* **Get** (`get`) - Get a post
* **Get Many** (`getAll`) - Get many posts

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| By | `by` | options | id | ✓ | Get the post either by slug or ID |  |

**By options:**

* **ID** (`id`)
* **Slug** (`slug`)

| Identifier | `identifier` | string |  | ✓ | The ID or slug of the post to get |  |
| Options | `options` | collection | {} | ✗ | Limit the fields returned in the response object. E.g. for posts fields=title,url. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Limit the fields returned in the response object. E.g. for posts fields=title,url. |
| Formats | `formats` | multiOptions |  |  |

</details>

| Options | `options` | collection | {} | ✗ | Limit the fields returned in the response object. E.g. for posts fields=title,url. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Limit the fields returned in the response object. E.g. for posts fields=title,url. |
| Formats | `formats` | multiOptions |  |  |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Tells the API to return additional data related to the resource you have requested | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | multiOptions | [] | Tells the API to return additional data related to the resource you have requested |
| Fields | `fields` | string |  | Limit the fields returned in the response object. E.g. for posts fields=title,url. |
| Formats | `formats` | multiOptions |  | By default, only html is returned, however each post and page in Ghost has 2 available formats: html and plaintext |

</details>

| Options | `options` | collection | {} | ✗ | Tells the API to return additional data related to the resource you have requested | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | multiOptions | [] | Tells the API to return additional data related to the resource you have requested |
| Fields | `fields` | string |  | Limit the fields returned in the response object. E.g. for posts fields=title,url. |
| Formats | `formats` | multiOptions |  |  |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ | Post's title |  |
| Content Format | `contentFormat` | options | html | ✗ | The format of the post |  |

**Content Format options:**

* **HTML** (`html`)
* **Mobile Doc** (`mobileDoc`)
* **Lexical** (`lexical`)

| Content | `content` | string |  | ✗ | The content of the post to create |  |
| Content (JSON) | `content` | json |  | ✗ | Mobiledoc is the raw JSON format that Ghost uses to store post contents. <a href="https://ghost.org/docs/concepts/posts/#document-storage">Info</a>. |  |
| Content (JSON) | `content` | json |  | ✗ | Lexical is the JSON format returned by the Ghost Default editor |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Author Names or IDs | `authors` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Cannonical URL | `canonical_url` | string |  |  |
| Code Injection Foot | `codeinjection_foot` | string |  | The Code Injection allows you inject a small snippet into your Ghost site |
| Code Injection Head | `codeinjection_head` | string |  | The Code Injection allows you inject a small snippet into your Ghost site |
| Featured | `featured` | boolean | False |  |
| Meta Description | `meta_description` | string |  |  |
| Meta Title | `meta_title` | string |  |  |
| Open Graph Description | `og_description` | string |  |  |
| Open Graph Image | `og_image` | string |  | URL of the image |
| Open Graph Title | `og_title` | string |  |  |
| Published At | `published_at` | dateTime |  |  |
| Slug | `slug` | string |  |  |
| Status | `status` | options | draft |  |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Twitter Description | `twitter_description` | string |  |  |
| Twitter Image | `twitter_image` | string |  | URL of the image |
| Twitter Title | `twitter_title` | string |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Post ID | `postId` | string |  | ✓ | The ID of the post to delete |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Post ID | `postId` | string |  | ✗ | The ID of the post to update |  |
| Content Format | `contentFormat` | options | html | ✗ | The format of the post |  |

**Content Format options:**

* **HTML** (`html`)
* **Mobile Doc** (`mobileDoc`)
* **Lexical** (`lexical`)

| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Author Names or IDs | `authors` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Cannonical URL | `canonical_url` | string |  |  |
| Code Injection Foot | `codeinjection_foot` | string |  |  |
| Code Injection Head | `codeinjection_head` | string |  |  |
| Content | `content` | string |  |  |
| Content (JSON) | `contentJson` | json |  | Mobiledoc is the raw JSON format that Ghost uses to store post contents. <a href="https://ghost.org/docs/concepts/posts/#document-storage">Info.</a>. |
| Content (JSON) | `contentJson` | json |  | Lexical is the JSON format returned by the Ghost Default editor |
| Featured | `featured` | boolean | False |  |
| Meta Description | `meta_description` | string |  |  |
| Meta Title | `meta_title` | string |  |  |
| Open Graph Description | `og_description` | string |  |  |
| Open Graph Image | `og_image` | string |  | URL of the image |
| Open Graph Title | `og_title` | string |  |  |
| Published At | `published_at` | dateTime |  |  |
| Slug | `slug` | string |  |  |
| Status | `status` | options | draft |  |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Title | `title` | string |  | Post's title |
| Twitter Description | `twitter_description` | string |  |  |
| Twitter Image | `twitter_image` | string |  | URL of the image |
| Twitter Title | `twitter_title` | string |  |  |

</details>


---

## Load Options Methods

- `getAuthors`
- `for`
- `name`
- `value`

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
node: ghost
displayName: Ghost
description: Consume Ghost API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: ghostAdminApi
  required: true
- name: ghostContentApi
  required: true
operations:
- id: get
  name: Get
  description: Get a post
  params:
  - id: by
    name: By
    type: options
    default: id
    required: true
    description: Get the post either by slug or ID
    validation:
      required: true
      displayOptions:
        show:
          source:
          - contentApi
          - adminApi
          resource:
          - post
          operation:
          - get
    typeInfo:
      type: options
      displayName: By
      name: by
      possibleValues:
      - value: id
        name: ID
        description: ''
      - value: slug
        name: Slug
        description: ''
  - id: identifier
    name: Identifier
    type: string
    default: ''
    required: true
    description: The ID or slug of the post to get
    validation:
      required: true
      displayOptions:
        show:
          source:
          - contentApi
          - adminApi
          resource:
          - post
          operation:
          - get
    typeInfo:
      type: string
      displayName: Identifier
      name: identifier
- id: getAll
  name: Get Many
  description: Get many posts
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
          source:
          - contentApi
          - adminApi
          resource:
          - post
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          source:
          - adminApi
          - contentApi
          resource:
          - post
          operation:
          - getAll
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
- id: create
  name: Create
  description: Create a post
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Post's title
    validation:
      required: true
      displayOptions:
        show:
          source:
          - adminApi
          resource:
          - post
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: contentFormat
    name: Content Format
    type: options
    default: html
    required: false
    description: The format of the post
    validation: &id005
      displayOptions:
        show:
          source:
          - adminApi
          resource:
          - post
          operation:
          - update
    typeInfo: &id006
      type: options
      displayName: Content Format
      name: contentFormat
      possibleValues:
      - value: html
        name: HTML
        description: ''
      - value: mobileDoc
        name: Mobile Doc
        description: ''
      - value: lexical
        name: Lexical
        description: ''
  - id: content
    name: Content
    type: string
    default: ''
    required: false
    description: The content of the post to create
    validation: &id001
      displayOptions:
        show:
          source:
          - adminApi
          resource:
          - post
          operation:
          - create
          contentFormat:
          - lexical
    typeInfo: &id002
      type: json
      displayName: Content (JSON)
      name: content
  - id: content
    name: Content (JSON)
    type: json
    default: ''
    required: false
    description: Mobiledoc is the raw JSON format that Ghost uses to store post contents.
      <a href="https://ghost.org/docs/concepts/posts/#document-storage">Info</a>.
    validation: *id001
    typeInfo: *id002
  - id: content
    name: Content (JSON)
    type: json
    default: ''
    required: false
    description: Lexical is the JSON format returned by the Ghost Default editor
    validation: *id001
    typeInfo: *id002
- id: delete
  name: Delete
  description: Delete a post
  params:
  - id: postId
    name: Post ID
    type: string
    default: ''
    required: true
    description: The ID of the post to delete
    validation: &id003
      displayOptions:
        show:
          source:
          - adminApi
          resource:
          - post
          operation:
          - update
    typeInfo: &id004
      type: string
      displayName: Post ID
      name: postId
- id: update
  name: Update
  description: Update a post
  params:
  - id: postId
    name: Post ID
    type: string
    default: ''
    required: false
    description: The ID of the post to update
    validation: *id003
    typeInfo: *id004
  - id: contentFormat
    name: Content Format
    type: options
    default: html
    required: false
    description: The format of the post
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
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: updateFields
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
  "$id": "https://n8n.io/schemas/nodes/ghost.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Ghost Node",
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
        "update"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "source": {
          "description": "Pick where your data comes from, Content or Admin API",
          "type": "string",
          "enum": [
            "adminApi",
            "contentApi"
          ],
          "default": "contentApi"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "post"
          ],
          "default": "post"
        },
        "operation": {
          "description": "Create a post",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "get"
        },
        "title": {
          "description": "Post's title",
          "type": "string",
          "default": ""
        },
        "contentFormat": {
          "description": "The format of the post",
          "type": "string",
          "enum": [
            "html",
            "mobileDoc",
            "lexical"
          ],
          "default": "html"
        },
        "content": {
          "description": "Lexical is the JSON format returned by the Ghost Default editor",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "postId": {
          "description": "The ID of the post to update",
          "type": "string",
          "default": ""
        },
        "by": {
          "description": "Get the post either by slug or ID",
          "type": "string",
          "enum": [
            "id",
            "slug"
          ],
          "default": "id"
        },
        "identifier": {
          "description": "The ID or slug of the post to get",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Tells the API to return additional data related to the resource you have requested",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
          "default": 50
        },
        "updateFields": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
      "name": "ghostAdminApi",
      "required": true
    },
    {
      "name": "ghostContentApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
