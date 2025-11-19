---
title: "Node: LinkedIn"
slug: "node-linkedin"
version: "1"
updated: "2025-11-13"
summary: "Consume LinkedIn API"
node_type: "regular"
group: "['input']"
---

# Node: LinkedIn

**Purpose.** Consume LinkedIn API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:linkedin.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **linkedInOAuth2Api**: N/A
- **linkedInCommunityManagementOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `linkedInOAuth2Api` | ✓ | {'show': {'authentication': ['standard']}} |
| `linkedInCommunityManagementOAuth2Api` | ✓ | {'show': {'authentication': ['communityManagement']}} |

---

## API Patterns

**Headers Used:** LinkedIn-Version, X-Restli-Protocol-Version

---

## Operations

### Post Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new post |

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
| Operation | `operation` | options | create | ✗ | Create a new post |  |

**Operation options:**

* **Create** (`create`) - Create a new post

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Person Name or ID | `person` | options |  | ✓ | Person as which the post should be posted as. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Organization URN | `organization` | string |  | ✗ | URN of Organization as which the post should be posted as | e.g. 1234567 |  |
| Text | `text` | string |  | ✗ | The primary content of the post |  |
| Media Category | `shareMediaCategory` | options | NONE | ✗ | The post does not contain any media, and will only consist of text |  |

**Media Category options:**

* **None** (`NONE`) - The post does not contain any media, and will only consist of text
* **Article** (`ARTICLE`) - The post contains an article URL
* **Image** (`IMAGE`) - The post contains an image

| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be written |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Provide a short description for your image or article | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Provide a short description for your image or article |
| Original URL | `originalUrl` | string |  | Provide the URL of the article you would like to share here |
| Input Binary Field | `thumbnailBinaryPropertyName` | string | data |  |
| Title | `title` | string |  | Customize the title of your image or article |
| Visibility | `visibility` | options | PUBLIC | Dictate if post will be seen by the public or only connections |

</details>


---

## Load Options Methods

- `getPersonUrn`
- `if`

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
* Categories: Marketing, Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: linkedIn
displayName: LinkedIn
description: Consume LinkedIn API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: linkedInOAuth2Api
  required: true
- name: linkedInCommunityManagementOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a new post
  params:
  - id: person
    name: Person Name or ID
    type: options
    default: ''
    required: true
    description: Person as which the post should be posted as. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          postAs:
          - person
          resource:
          - post
    typeInfo:
      type: options
      displayName: Person Name or ID
      name: person
      typeOptions:
        loadOptionsMethod: getPersonUrn
      possibleValues: []
  - id: organization
    name: Organization URN
    type: string
    default: ''
    required: false
    description: URN of Organization as which the post should be posted as
    placeholder: '1234567'
    validation:
      displayOptions:
        show:
          operation:
          - create
          postAs:
          - organization
          resource:
          - post
    typeInfo:
      type: string
      displayName: Organization URN
      name: organization
  - id: text
    name: Text
    type: string
    default: ''
    required: false
    description: The primary content of the post
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - post
    typeInfo:
      type: string
      displayName: Text
      name: text
  - id: shareMediaCategory
    name: Media Category
    type: options
    default: NONE
    required: false
    description: The post does not contain any media, and will only consist of text
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - post
    typeInfo:
      type: options
      displayName: Media Category
      name: shareMediaCategory
      possibleValues:
      - value: NONE
        name: None
        description: The post does not contain any media, and will only consist of
          text
      - value: ARTICLE
        name: Article
        description: The post contains an article URL
      - value: IMAGE
        name: Image
        description: The post contains an image
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be written
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - post
          shareMediaCategory:
          - IMAGE
    typeInfo:
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - LinkedIn-Version
  - X-Restli-Protocol-Version
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: organization
    text: '1234567'
  - field: additionalFields
    text: Add Field
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be written
  - field: additionalFields
    text: The name of the input binary field containing the file for the article thumbnail
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
  "$id": "https://n8n.io/schemas/nodes/linkedIn.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "LinkedIn Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create"
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
            "standard",
            "communityManagement"
          ],
          "default": "standard"
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
          "description": "Create a new post",
          "type": "string",
          "enum": [
            "create"
          ],
          "default": "create"
        },
        "postAs": {
          "description": "If to post on behalf of a user or an organization",
          "type": "string",
          "enum": [
            "person",
            "organization"
          ],
          "default": "person"
        },
        "person": {
          "description": "Person as which the post should be posted as. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "organization": {
          "description": "URN of Organization as which the post should be posted as",
          "type": "string",
          "default": "",
          "examples": [
            "1234567"
          ]
        },
        "text": {
          "description": "The primary content of the post",
          "type": "string",
          "default": ""
        },
        "shareMediaCategory": {
          "description": "The post does not contain any media, and will only consist of text",
          "type": "string",
          "enum": [
            "NONE",
            "ARTICLE",
            "IMAGE"
          ],
          "default": "NONE"
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "additionalFields": {
          "description": "Provide a short description for your image or article",
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
      "name": "linkedInOAuth2Api",
      "required": true
    },
    {
      "name": "linkedInCommunityManagementOAuth2Api",
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
