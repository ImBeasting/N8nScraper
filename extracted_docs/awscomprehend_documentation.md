---
title: "Node: AWS Comprehend"
slug: "node-awscomprehend"
version: "1"
updated: "2026-01-08"
summary: "Sends data to Amazon Comprehend"
node_type: "regular"
group: "['output']"
---

# Node: AWS Comprehend

**Purpose.** Sends data to Amazon Comprehend
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:comprehend.svg`
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
| Detect Dominant Language | `detectDominantLanguage` | Identify the dominant language |
| Detect Entities | `detectEntities` | Inspects text for named entities, and returns information about them |
| Detect Sentiment | `detectSentiment` | Analyse the sentiment of the text |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | text | ✗ | The resource to perform |  |

**Resource options:**

* **Text** (`text`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | detectDominantLanguage | ✗ | Identify the dominant language |  |

**Operation options:**

* **Detect Dominant Language** (`detectDominantLanguage`) - Identify the dominant language
* **Detect Entities** (`detectEntities`) - Inspects text for named entities, and returns information about them
* **Detect Sentiment** (`detectSentiment`) - Analyse the sentiment of the text

---

### Detect Dominant Language parameters (`detectDominantLanguage`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

### Detect Entities parameters (`detectEntities`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Language Code | `languageCode` | options | en | ✗ | The language code for text |  |

**Language Code options:**

* **Arabic** (`ar`)
* **Chinese** (`zh`)
* **Chinese (T)** (`zh-TW`)
* **English** (`en`)
* **French** (`fr`)
* **German** (`de`)
* **Hindi** (`hi`)
* **Italian** (`it`)
* **Japanese** (`ja`)
* **Korean** (`ko`)
* **Portuguese** (`pt`)
* **Spanish** (`es`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | The Amazon Resource Name of an endpoint that is associated with a custom entity recognition model | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Endpoint Arn | `endpointArn` | string |  | The Amazon Resource Name of an endpoint that is associated with a custom entity recognition model |

</details>


### Detect Sentiment parameters (`detectSentiment`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Language Code | `languageCode` | options | en | ✗ | The language code for text |  |

**Language Code options:**

* **Arabic** (`ar`)
* **Chinese** (`zh`)
* **Chinese (T)** (`zh-TW`)
* **English** (`en`)
* **French** (`fr`)
* **German** (`de`)
* **Hindi** (`hi`)
* **Italian** (`it`)
* **Japanese** (`ja`)
* **Korean** (`ko`)
* **Portuguese** (`pt`)
* **Spanish** (`es`)


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
node: awsComprehend
displayName: AWS Comprehend
description: Sends data to Amazon Comprehend
version: '1'
nodeType: regular
group:
- output
operations:
- id: detectDominantLanguage
  name: Detect Dominant Language
  description: Identify the dominant language
  params:
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
          - text
          operation:
          - detectDominantLanguage
    typeInfo:
      type: boolean
      displayName: Simplify
      name: simple
- id: detectEntities
  name: Detect Entities
  description: Inspects text for named entities, and returns information about them
  params:
  - id: languageCode
    name: Language Code
    type: options
    default: en
    required: false
    description: The language code for text
    validation: &id001
      displayOptions:
        show:
          resource:
          - text
          operation:
          - detectSentiment
          - detectEntities
    typeInfo: &id002
      type: options
      displayName: Language Code
      name: languageCode
      possibleValues:
      - value: ar
        name: Arabic
        description: ''
      - value: zh
        name: Chinese
        description: ''
      - value: zh-TW
        name: Chinese (T)
        description: ''
      - value: en
        name: English
        description: ''
      - value: fr
        name: French
        description: ''
      - value: de
        name: German
        description: ''
      - value: hi
        name: Hindi
        description: ''
      - value: it
        name: Italian
        description: ''
      - value: ja
        name: Japanese
        description: ''
      - value: ko
        name: Korean
        description: ''
      - value: pt
        name: Portuguese
        description: ''
      - value: es
        name: Spanish
        description: ''
- id: detectSentiment
  name: Detect Sentiment
  description: Analyse the sentiment of the text
  params:
  - id: languageCode
    name: Language Code
    type: options
    default: en
    required: false
    description: The language code for text
    validation: *id001
    typeInfo: *id002
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
  "$id": "https://n8n.io/schemas/nodes/awsComprehend.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AWS Comprehend Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "detectDominantLanguage",
        "detectEntities",
        "detectSentiment"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "The resource to perform",
          "type": "string",
          "enum": [
            "text"
          ],
          "default": "text"
        },
        "operation": {
          "description": "Identify the dominant language",
          "type": "string",
          "enum": [
            "detectDominantLanguage",
            "detectEntities",
            "detectSentiment"
          ],
          "default": "detectDominantLanguage"
        },
        "languageCode": {
          "description": "The language code for text",
          "type": "string",
          "enum": [
            "ar",
            "zh",
            "zh-TW",
            "en",
            "fr",
            "de",
            "hi",
            "it",
            "ja",
            "ko",
            "pt",
            "es"
          ],
          "default": "en"
        },
        "text": {
          "description": "The text to send",
          "type": "string",
          "default": ""
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "additionalFields": {
          "description": "The Amazon Resource Name of an endpoint that is associated with a custom entity recognition model",
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
