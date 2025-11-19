---
title: "Node: Google Cloud Natural Language"
slug: "node-googlecloudnaturallanguage"
version: "1"
updated: "2025-11-13"
summary: "Consume Google Cloud Natural Language API"
node_type: "regular"
group: "['input', 'output']"
---

# Node: Google Cloud Natural Language

**Purpose.** Consume Google Cloud Natural Language API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:googlecloudnaturallanguage.png`
- **Group:** `['input', 'output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleCloudNaturalLanguageOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleCloudNaturalLanguageOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Document Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Analyze Sentiment | `analyzeSentiment` | Analyze sentiment |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | document | ✗ | Resource to operate on |  |

**Resource options:**

* **Document** (`document`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | analyzeSentiment | ✗ | Operation to perform |  |

**Operation options:**

* **Analyze Sentiment** (`analyzeSentiment`) - Analyze sentiment

---

### Analyze Sentiment parameters (`analyzeSentiment`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Source | `source` | options | content | ✓ | The source of the document: a string containing the content or a Google Cloud Storage URI |  |

**Source options:**

* **Content** (`content`)
* **Google Cloud Storage URI** (`gcsContentUri`)

| Content | `content` | string |  | ✓ | The content of the input in string format. Cloud audit logging exempt since it is based on user data. |  |
| Google Cloud Storage URI | `gcsContentUri` | string |  | ✓ | The Google Cloud Storage URI where the file content is located. This URI must be of the form: <code>gs://bucket_name/object_name</code>. For more details, see <a href="https://cloud.google.com/storage/docs/reference-uris.">reference</a>. |  |
| Options | `options` | collection | {} | ✗ | The type of input document | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Document Type | `documentType` | options | PLAIN_TEXT | The type of input document |
| Encoding Type | `encodingType` | options | UTF16 | The encoding type used by the API to calculate sentence offsets |
| Language | `language` | options | en | The language of the document (if not specified, the language is automatically detected). Both ISO and BCP-47 language codes are accepted. |

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
* Categories: Analytics

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleCloudNaturalLanguage
displayName: Google Cloud Natural Language
description: Consume Google Cloud Natural Language API
version: '1'
nodeType: regular
group:
- input
- output
credentials:
- name: googleCloudNaturalLanguageOAuth2Api
  required: true
operations:
- id: analyzeSentiment
  name: Analyze Sentiment
  description: ''
  params:
  - id: source
    name: Source
    type: options
    default: content
    required: true
    description: 'The source of the document: a string containing the content or a
      Google Cloud Storage URI'
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - analyzeSentiment
    typeInfo:
      type: options
      displayName: Source
      name: source
      possibleValues:
      - value: content
        name: Content
        description: ''
      - value: gcsContentUri
        name: Google Cloud Storage URI
        description: ''
  - id: content
    name: Content
    type: string
    default: ''
    required: true
    description: The content of the input in string format. Cloud audit logging exempt
      since it is based on user data.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - analyzeSentiment
          source:
          - content
    typeInfo:
      type: string
      displayName: Content
      name: content
  - id: gcsContentUri
    name: Google Cloud Storage URI
    type: string
    default: ''
    required: true
    description: 'The Google Cloud Storage URI where the file content is located.
      This URI must be of the form: <code>gs://bucket_name/object_name</code>. For
      more details, see <a href="https://cloud.google.com/storage/docs/reference-uris.">reference</a>.'
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - analyzeSentiment
          source:
          - gcsContentUri
    typeInfo:
      type: string
      displayName: Google Cloud Storage URI
      name: gcsContentUri
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
  "$id": "https://n8n.io/schemas/nodes/googleCloudNaturalLanguage.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Cloud Natural Language Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "analyzeSentiment"
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
            "document"
          ],
          "default": "document"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "analyzeSentiment"
          ],
          "default": "analyzeSentiment"
        },
        "source": {
          "description": "The source of the document: a string containing the content or a Google Cloud Storage URI",
          "type": "string",
          "enum": [
            "content",
            "gcsContentUri"
          ],
          "default": "content"
        },
        "content": {
          "description": "The content of the input in string format. Cloud audit logging exempt since it is based on user data.",
          "type": "string",
          "default": ""
        },
        "gcsContentUri": {
          "description": "The Google Cloud Storage URI where the file content is located. This URI must be of the form: <code>gs://bucket_name/object_name</code>. For more details, see <a href=\"https://cloud.google.com/storage/docs/reference-uris.\">reference</a>.",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "The type of input document",
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
      "name": "googleCloudNaturalLanguageOAuth2Api",
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
