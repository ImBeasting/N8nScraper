---
title: "Node: Bannerbear"
slug: "node-bannerbear"
version: "1"
updated: "2026-01-08"
summary: "Consume Bannerbear API"
node_type: "regular"
group: "['output']"
---

# Node: Bannerbear

**Purpose.** Consume Bannerbear API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:bannerbear.png`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **bannerbearApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `bannerbearApi` | ✓ | - |

---

## Operations

### Image Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an image |
| Get | `get` | Get an image |

### Template Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a template |
| Get Many | `getAll` | Get many templates |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | image | ✗ | Resource to operate on |  |

**Resource options:**

* **Image** (`image`)
* **Template** (`template`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create an image |  |

**Operation options:**

* **Create** (`create`) - Create an image
* **Get** (`get`) - Get an image

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Template Name or ID | `templateId` | options |  | ✓ | The template ID you want to use. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Metadata that you need to store e.g. ID of a record in your DB | e.g. Add Field | min:1, max:10 |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Metadata | `metadata` | string |  | Metadata that you need to store e.g. ID of a record in your DB |
| Wait for Image | `waitForImage` | boolean | False | Whether to wait for the image to be proccesed before returning. If after three tries the images is not ready, an error will be thrown. Number of tries can be increased by setting "Wait Max Tries". |
| Wait Max Tries | `waitForImageMaxTries` | number | 3 | How often it should check if the image is available before it fails |
| Webhook URL | `webhookUrl` | string |  | A URL to POST the Image object to upon rendering completed |

</details>

| Modifications | `modificationsUi` | fixedCollection | {} | ✗ | The name of the item you want to change. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Modification |  |

<details>
<summary><strong>Modifications sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Modification | `modificationsValues` |  |  |  |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Image ID | `imageId` | string |  | ✓ | Unique identifier for the image |  |
| Template ID | `templateId` | string |  | ✓ | Unique identifier for the template |  |

---

## Load Options Methods

- `getTemplates`
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
node: bannerbear
displayName: Bannerbear
description: Consume Bannerbear API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: bannerbearApi
  required: true
operations:
- id: create
  name: Create
  description: Create an image
  params:
  - id: templateId
    name: Template Name or ID
    type: options
    default: ''
    required: true
    description: The template ID you want to use. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - template
          operation:
          - get
    typeInfo: &id002
      type: string
      displayName: Template ID
      name: templateId
  - id: modificationsUi
    name: Modifications
    type: fixedCollection
    default: {}
    required: false
    description: The name of the item you want to change. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    placeholder: Add Modification
    validation:
      displayOptions:
        show:
          resource:
          - image
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Modifications
      name: modificationsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: modificationsValues
        displayName: Modification
        values:
        - displayName: Name or ID
          name: name
          type: options
          description: The name of the item you want to change. Choose from the list,
            or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: ''
          typeOptions:
            loadOptionsMethod: getModificationNames
        - displayName: Text
          name: text
          type: string
          description: Replacement text you want to use
          default: ''
        - displayName: Color
          name: color
          type: color
          description: Color hex of object
          default: ''
        - displayName: Background
          name: background
          type: color
          description: Color hex of text background
          default: ''
        - displayName: Image URL
          name: imageUrl
          type: string
          description: Replacement image URL you want to use (must be publicly viewable)
          default: ''
- id: get
  name: Get
  description: Get an image
  params:
  - id: imageId
    name: Image ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the image
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - image
          operation:
          - get
    typeInfo:
      type: string
      displayName: Image ID
      name: imageId
  - id: templateId
    name: Template ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the template
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many templates
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
  - field: modificationsUi
    text: Add Modification
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
  "$id": "https://n8n.io/schemas/nodes/bannerbear.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Bannerbear Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "get",
        "getAll"
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
            "image",
            "template"
          ],
          "default": "image"
        },
        "operation": {
          "description": "Get a template",
          "type": "string",
          "enum": [
            "get",
            "getAll"
          ],
          "default": "get"
        },
        "templateId": {
          "description": "Unique identifier for the template",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Metadata that you need to store e.g. ID of a record in your DB",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "modificationsUi": {
          "description": "The name of the item you want to change. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Modification"
          ]
        },
        "imageId": {
          "description": "Unique identifier for the image",
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
      "name": "bannerbearApi",
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
