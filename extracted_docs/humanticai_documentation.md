---
title: "Node: Humantic AI"
slug: "node-humanticai"
version: "1"
updated: "2025-11-13"
summary: "Consume Humantic AI API"
node_type: "regular"
group: "['output']"
---

# Node: Humantic AI

**Purpose.** Consume Humantic AI API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:humanticai.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **humanticAiApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `humanticAiApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Profile Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a profile |
| Get | `get` | Retrieve a profile |
| Update | `update` | Update a profile |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | profile | ✗ | Resource to operate on |  |

**Resource options:**

* **Profile** (`profile`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a profile |  |

**Operation options:**

* **Create** (`create`) - Create a profile
* **Get** (`get`) - Retrieve a profile
* **Update** (`update`) - Update a profile

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✓ | The LinkedIn profile URL or email ID for creating a Humantic profile. If you are sending the resume, this should be a unique string. |  |
| Send Resume | `sendResume` | boolean | False | ✗ | Whether to send a resume for a resume based analysis |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✗ | e.g. The name of the input binary field containing the resume in PDF or DOCX format |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✓ | This value is the same as the User ID that was provided when the analysis was created. This could be a LinkedIn URL, email ID, or a unique string in case of resume based analysis. |  |
| Options | `options` | collection | {} | ✗ | Fetch the Humantic profile of the user for a particular persona type. Multiple persona values can be supported using comma as a delimiter. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Persona | `persona` | multiOptions | [] | Fetch the Humantic profile of the user for a particular persona type. Multiple persona values can be supported using comma as a delimiter. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✓ | This value is the same as the User ID that was provided when the analysis was created. Currently only supported for profiles created using LinkedIn URL. |  |
| Send Resume | `sendResume` | boolean | False | ✗ | Whether to send a resume for a resume of the user |  |
| Text | `text` | string |  | ✗ | Additional text written by the user |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✗ | e.g. The name of the input binary field containing the resume in PDF or DOCX format |  |

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
* Categories: Analytics

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: humanticAi
displayName: Humantic AI
description: Consume Humantic AI API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: humanticAiApi
  required: true
operations:
- id: create
  name: Create
  description: Create a profile
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: The LinkedIn profile URL or email ID for creating a Humantic profile.
      If you are sending the resume, this should be a unique string.
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - profile
    typeInfo: &id002
      type: string
      displayName: User ID
      name: userId
  - id: sendResume
    name: Send Resume
    type: boolean
    default: false
    required: false
    description: Whether to send a resume for a resume based analysis
    validation: &id003
      displayOptions:
        show:
          operation:
          - update
          resource:
          - profile
    typeInfo: &id004
      type: boolean
      displayName: Send Resume
      name: sendResume
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: false
    description: ''
    hint: The name of the input binary field containing the resume in PDF or DOCX
      format
    validation: &id005
      displayOptions:
        show:
          operation:
          - update
          resource:
          - profile
          sendResume:
          - true
    typeInfo: &id006
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
- id: get
  name: Get
  description: Retrieve a profile
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: This value is the same as the User ID that was provided when the
      analysis was created. This could be a LinkedIn URL, email ID, or a unique string
      in case of resume based analysis.
    validation: *id001
    typeInfo: *id002
- id: update
  name: Update
  description: Update a profile
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: This value is the same as the User ID that was provided when the
      analysis was created. Currently only supported for profiles created using LinkedIn
      URL.
    validation: *id001
    typeInfo: *id002
  - id: sendResume
    name: Send Resume
    type: boolean
    default: false
    required: false
    description: Whether to send a resume for a resume of the user
    validation: *id003
    typeInfo: *id004
  - id: text
    name: Text
    type: string
    default: ''
    required: false
    description: Additional text written by the user
    validation:
      displayOptions:
        show:
          operation:
          - update
          resource:
          - profile
          sendResume:
          - false
    typeInfo:
      type: string
      displayName: Text
      name: text
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: false
    description: ''
    hint: The name of the input binary field containing the resume in PDF or DOCX
      format
    validation: *id005
    typeInfo: *id006
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
  - field: options
    text: Add option
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the resume in PDF or DOCX
      format
  - field: binaryPropertyName
    text: The name of the input binary field containing the resume in PDF or DOCX
      format
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
  "$id": "https://n8n.io/schemas/nodes/humanticAi.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Humantic AI Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "get",
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
            "profile"
          ],
          "default": "profile"
        },
        "operation": {
          "description": "Create a profile",
          "type": "string",
          "enum": [
            "create",
            "get",
            "update"
          ],
          "default": "create"
        },
        "userId": {
          "description": "This value is the same as the User ID that was provided when the analysis was created. Currently only supported for profiles created using LinkedIn URL.",
          "type": "string",
          "default": ""
        },
        "sendResume": {
          "description": "Whether to send a resume for a resume of the user",
          "type": "boolean",
          "default": false
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "Fetch the Humantic profile of the user for a particular persona type. Multiple persona values can be supported using comma as a delimiter.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "text": {
          "description": "Additional text written by the user",
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
      "name": "humanticAiApi",
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
