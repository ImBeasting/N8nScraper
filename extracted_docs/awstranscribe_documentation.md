---
title: "Node: AWS Transcribe"
slug: "node-awstranscribe"
version: "1"
updated: "2025-11-13"
summary: "Sends data to AWS Transcribe"
node_type: "regular"
group: "['output']"
---

# Node: AWS Transcribe

**Purpose.** Sends data to AWS Transcribe
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:transcribe.svg`
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

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a transcription job |
| Delete | `delete` | Delete a transcription job |
| Get | `get` | Get a transcription job |
| Get Many | `getAll` | Get many transcription jobs |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | transcriptionJob | ✗ | Resource to operate on |  |

**Resource options:**

* **Transcription Job** (`transcriptionJob`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a transcription job |  |

**Operation options:**

* **Create** (`create`) - Create a transcription job
* **Delete** (`delete`) - Delete a transcription job
* **Get** (`get`) - Get a transcription job
* **Get Many** (`getAll`) - Get many transcription jobs

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Job Name | `transcriptionJobName` | string |  | ✗ | The name of the job |  |
| Media File URI | `mediaFileUri` | string |  | ✗ | The S3 object location of the input media file |  |
| Detect Language | `detectLanguage` | boolean | False | ✗ | Whether to set this field to true to enable automatic language identification |  |
| Language | `languageCode` | options | en-US | ✗ | Language used in the input media file |  |

**Language options:**

* **American English** (`en-US`)
* **British English** (`en-GB`)
* **German** (`de-DE`)
* **Indian English** (`en-IN`)
* **Irish English** (`en-IE`)
* **Russian** (`ru-RU`)
* **Spanish** (`es-ES`)

| Options | `options` | collection | {} | ✗ | Instructs Amazon Transcribe to process each audiochannel separately and then merge the transcription output of each channel into a single transcription. You can't set both Max Speaker Labels and Channel Identification in the same request. If you set both, your request returns a BadRequestException. | e.g. Add option | min:2, max:10 |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Channel Identification | `channelIdentification` | boolean | False | Instructs Amazon Transcribe to process each audiochannel separately and then merge the transcription output of each channel into a single transcription. You can't set both Max Speaker Labels and Channel Identification in the same request. If you set both, your request returns a BadRequestException. |
| Max Alternatives | `maxAlternatives` | number | 2 | The number of alternative transcriptions that the service should return |
| Max Speaker Labels | `maxSpeakerLabels` | number | 2 | The maximum number of speakers to identify in the input audio. If there are more speakers in the audio than this number, multiple speakers are identified as a single speaker. |
| Vocabulary Name | `vocabularyName` | string |  | Name of vocabulary to use when processing the transcription job |
| Vocabulary Filter Name | `vocabularyFilterName` | string |  | The name of the vocabulary filter to use when transcribing the audio. The filter that you specify must have the same language code as the transcription job. |
| Vocabulary Filter Method | `vocabularyFilterMethod` | options | remove | <p>Set to mask to remove filtered text from the transcript and replace it with three asterisks ("***") as placeholder text.</p><p>Set to remove to remove filtered text from the transcript without using placeholder text. Set to tag to mark the word in the transcription output that matches the vocabulary filter. When you set the filter method to tag, the words matching your vocabulary filter are not masked or removed.</p> |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Job Name | `transcriptionJobName` | string |  | ✗ | The name of the job |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Job Name | `transcriptionJobName` | string |  | ✗ | The name of the job |  |
| Return Transcript | `returnTranscript` | boolean | True | ✗ | By default, the response only contains metadata about the transcript. Enable this option to retrieve the transcript instead. |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Return only transcription jobs whose name contains the specified string | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Job Name Contains | `jobNameContains` | string |  | Return only transcription jobs whose name contains the specified string |
| Status | `status` | options | COMPLETED | Return only transcription jobs with the specified status |

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
node: awsTranscribe
displayName: AWS Transcribe
description: Sends data to AWS Transcribe
version: '1'
nodeType: regular
group:
- output
credentials:
- name: aws
  required: true
operations:
- id: create
  name: Create
  description: Create a transcription job
  params:
  - id: transcriptionJobName
    name: Job Name
    type: string
    default: ''
    required: false
    description: The name of the job
    validation: &id001
      displayOptions:
        show:
          resource:
          - transcriptionJob
          operation:
          - create
          - get
          - delete
    typeInfo: &id002
      type: string
      displayName: Job Name
      name: transcriptionJobName
  - id: mediaFileUri
    name: Media File URI
    type: string
    default: ''
    required: false
    description: The S3 object location of the input media file
    validation:
      displayOptions:
        show:
          resource:
          - transcriptionJob
          operation:
          - create
    typeInfo:
      type: string
      displayName: Media File URI
      name: mediaFileUri
  - id: detectLanguage
    name: Detect Language
    type: boolean
    default: false
    required: false
    description: Whether to set this field to true to enable automatic language identification
    validation:
      displayOptions:
        show:
          resource:
          - transcriptionJob
          operation:
          - create
    typeInfo:
      type: boolean
      displayName: Detect Language
      name: detectLanguage
  - id: languageCode
    name: Language
    type: options
    default: en-US
    required: false
    description: Language used in the input media file
    validation:
      displayOptions:
        show:
          resource:
          - transcriptionJob
          operation:
          - create
          detectLanguage:
          - false
    typeInfo:
      type: options
      displayName: Language
      name: languageCode
      possibleValues:
      - value: en-US
        name: American English
        description: ''
      - value: en-GB
        name: British English
        description: ''
      - value: de-DE
        name: German
        description: ''
      - value: en-IN
        name: Indian English
        description: ''
      - value: en-IE
        name: Irish English
        description: ''
      - value: ru-RU
        name: Russian
        description: ''
      - value: es-ES
        name: Spanish
        description: ''
- id: delete
  name: Delete
  description: Delete a transcription job
  params:
  - id: transcriptionJobName
    name: Job Name
    type: string
    default: ''
    required: false
    description: The name of the job
    validation: *id001
    typeInfo: *id002
- id: get
  name: Get
  description: Get a transcription job
  params:
  - id: transcriptionJobName
    name: Job Name
    type: string
    default: ''
    required: false
    description: The name of the job
    validation: *id001
    typeInfo: *id002
  - id: returnTranscript
    name: Return Transcript
    type: boolean
    default: true
    required: false
    description: By default, the response only contains metadata about the transcript.
      Enable this option to retrieve the transcript instead.
    validation:
      displayOptions:
        show:
          resource:
          - transcriptionJob
          operation:
          - get
    typeInfo:
      type: boolean
      displayName: Return Transcript
      name: returnTranscript
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation:
      displayOptions:
        show:
          resource:
          - transcriptionJob
          operation:
          - get
          returnTranscript:
          - true
    typeInfo:
      type: boolean
      displayName: Simplify
      name: simple
- id: getAll
  name: Get Many
  description: Get many transcription jobs
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
          resource:
          - transcriptionJob
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 20
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          resource:
          - transcriptionJob
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
  - field: options
    text: Add option
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/awsTranscribe.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AWS Transcribe Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
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
            "transcriptionJob"
          ],
          "default": "transcriptionJob"
        },
        "operation": {
          "description": "Create a transcription job",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll"
          ],
          "default": "create"
        },
        "transcriptionJobName": {
          "description": "The name of the job",
          "type": "string",
          "default": ""
        },
        "mediaFileUri": {
          "description": "The S3 object location of the input media file",
          "type": "string",
          "default": ""
        },
        "detectLanguage": {
          "description": "Whether to set this field to true to enable automatic language identification",
          "type": "boolean",
          "default": false
        },
        "languageCode": {
          "description": "Language used in the input media file",
          "type": "string",
          "enum": [
            "en-US",
            "en-GB",
            "de-DE",
            "en-IN",
            "en-IE",
            "ru-RU",
            "es-ES"
          ],
          "default": "en-US"
        },
        "options": {
          "description": "Instructs Amazon Transcribe to process each audiochannel separately and then merge the transcription output of each channel into a single transcription. You can't set both Max Speaker Labels and Channel Identification in the same request. If you set both, your request returns a BadRequestException.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "returnTranscript": {
          "description": "By default, the response only contains metadata about the transcript. Enable this option to retrieve the transcript instead.",
          "type": "boolean",
          "default": true
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 20
        },
        "filters": {
          "description": "Return only transcription jobs whose name contains the specified string",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
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
      "name": "aws",
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
