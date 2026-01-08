---
title: "Node: AWS Rekognition"
slug: "node-awsrekognition"
version: "1"
updated: "2026-01-08"
summary: "Sends data to AWS Rekognition"
node_type: "regular"
group: "['output']"
---

# Node: AWS Rekognition

**Purpose.** Sends data to AWS Rekognition
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:rekognition.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Analyze | `analyze` |  |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | image | ✗ | Resource to operate on |  |

**Resource options:**

* **Image** (`image`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | analyze | ✗ | Operation to perform |  |

**Operation options:**

* **Analyze** (`analyze`)

---

### Analyze parameters (`analyze`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Type | `type` | options | detectFaces | ✗ |  |  |

**Type options:**

* **Detect Faces** (`detectFaces`)
* **Detect Labels** (`detectLabels`)
* **Detect Moderation Labels** (`detectModerationLabels`)
* **Detect Text** (`detectText`)
* **Recognize Celebrity** (`recognizeCelebrity`)

| Binary File | `binaryData` | boolean | False | ✓ | Whether the image to analyze should be taken from binary field |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be written |  |
| Bucket | `bucket` | string |  | ✓ | Name of the S3 bucket |  |
| Name | `name` | string |  | ✓ | S3 object key name |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Height of the bounding box as a ratio of the overall image height | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Regions of Interest | `regionsOfInterestUi` | fixedCollection | {} | Height of the bounding box as a ratio of the overall image height |
| Version | `version` | string |  | If the bucket is versioning enabled, you can specify the object version |
| Word Filter | `wordFilterUi` | collection | {} | Sets the minimum height of the word bounding box. Words with bounding box heights lesser than this value will be excluded from the result. Value is relative to the video frame height. |
| Max Labels | `maxLabels` | number | 0 | Maximum number of labels you want the service to return in the response. The service returns the specified number of highest confidence labels. |
| Min Confidence | `minConfidence` | number | 0 | Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with a confidence level lower than this specified value. |
| Attributes | `attributes` | multiOptions | [] | An array of facial attributes you want to be returned |

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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: awsRekognition
displayName: AWS Rekognition
description: Sends data to AWS Rekognition
version: '1'
nodeType: regular
group:
- output
operations:
- id: analyze
  name: Analyze
  description: ''
  params:
  - id: type
    name: Type
    type: options
    default: detectFaces
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - analyze
          resource:
          - image
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: detectFaces
        name: Detect Faces
        description: ''
      - value: detectLabels
        name: Detect Labels
        description: ''
      - value: detectModerationLabels
        name: Detect Moderation Labels
        description: ''
      - value: detectText
        name: Detect Text
        description: ''
      - value: recognizeCelebrity
        name: Recognize Celebrity
        description: ''
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the image to analyze should be taken from binary field
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - analyze
          resource:
          - image
    typeInfo:
      type: boolean
      displayName: Binary File
      name: binaryData
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
          - analyze
          resource:
          - image
          binaryData:
          - true
    typeInfo:
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
  - id: bucket
    name: Bucket
    type: string
    default: ''
    required: true
    description: Name of the S3 bucket
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - analyze
          resource:
          - image
          binaryData:
          - false
    typeInfo:
      type: string
      displayName: Bucket
      name: bucket
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: S3 object key name
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - analyze
          resource:
          - image
          binaryData:
          - false
    typeInfo:
      type: string
      displayName: Name
      name: name
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
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be written
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
  "$id": "https://n8n.io/schemas/nodes/awsRekognition.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AWS Rekognition Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "analyze"
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
            "image"
          ],
          "default": "image"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "analyze"
          ],
          "default": "analyze"
        },
        "type": {
          "description": "",
          "type": "string",
          "enum": [
            "detectFaces",
            "detectLabels",
            "detectModerationLabels",
            "detectText",
            "recognizeCelebrity"
          ],
          "default": "detectFaces"
        },
        "binaryData": {
          "description": "Whether the image to analyze should be taken from binary field",
          "type": "boolean",
          "default": false
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "bucket": {
          "description": "Name of the S3 bucket",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "S3 object key name",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Height of the bounding box as a ratio of the overall image height",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "iam",
            "assumeRole"
          ],
          "default": "iam"
        },
        "aws": {
          "description": "",
          "type": "string"
        },
        "awsAssumeRole": {
          "description": "",
          "type": "string"
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
