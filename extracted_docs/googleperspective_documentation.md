---
title: "Node: Google Perspective"
slug: "node-googleperspective"
version: "1"
updated: "2025-11-13"
summary: "Consume Google Perspective API"
node_type: "regular"
group: "['transform']"
---

# Node: Google Perspective

**Purpose.** Consume Google Perspective API
**Subtitle.** ={{$parameter["operation"]}}


---

## Node Details

- **Icon:** `{'light': 'file:googlePerspective.svg', 'dark': 'file:googlePerspective.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googlePerspectiveOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googlePerspectiveOAuth2Api` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

**Headers Used:** Content-Type

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Analyze Comment | `analyzeComment` |  |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | analyzeComment | ✗ | Operation to perform |  |

**Operation options:**

* **Analyze Comment** (`analyzeComment`)

---

### Analyze Comment parameters (`analyzeComment`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Text | `text` | string |  | ✓ |  |  |
| Attributes to Analyze | `requestedAttributesUi` | fixedCollection | {} | ✓ | Attribute to analyze in the text. Details <a href="https://developers.perspectiveapi.com/s/about-the-api-attributes-and-languages">here</a>. | e.g. Add Atrribute |  |

<details>
<summary><strong>Attributes to Analyze sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Properties | `requestedAttributesValues` |  |  |  |

</details>

| Options | `options` | collection | {} | ✗ | Languages of the text input. If unspecified, the API will auto-detect the comment language. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Language Name or ID | `languages` | options |  | Languages of the text input. If unspecified, the API will auto-detect the comment language. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


---

## Load Options Methods

- `getLanguages`
- `for`
- `name`
- `value`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"]}}`

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
* Categories: Analytics, Utility
* Aliases: Moderation

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googlePerspective
displayName: Google Perspective
description: Consume Google Perspective API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: googlePerspectiveOAuth2Api
  required: true
operations:
- id: analyzeComment
  name: Analyze Comment
  description: ''
  params:
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - analyzeComment
    typeInfo:
      type: string
      displayName: Text
      name: text
  - id: requestedAttributesUi
    name: Attributes to Analyze
    type: fixedCollection
    default: {}
    required: true
    description: Attribute to analyze in the text. Details <a href="https://developers.perspectiveapi.com/s/about-the-api-attributes-and-languages">here</a>.
    placeholder: Add Atrribute
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - analyzeComment
    typeInfo:
      type: fixedCollection
      displayName: Attributes to Analyze
      name: requestedAttributesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: requestedAttributesValues
        displayName: Properties
        values:
        - displayName: Attribute Name
          name: attributeName
          type: options
          description: Attribute to analyze in the text. Details <a href="https://developers.perspectiveapi.com/s/about-the-api-attributes-and-languages">here</a>.
          value: flirtation
          default: flirtation
          options:
          - name: Flirtation
            value: flirtation
            displayName: Flirtation
          - name: Identity Attack
            value: identity_attack
            displayName: Identity Attack
          - name: Insult
            value: insult
            displayName: Insult
          - name: Profanity
            value: profanity
            displayName: Profanity
          - name: Severe Toxicity
            value: severe_toxicity
            displayName: Severe Toxicity
          - name: Sexually Explicit
            value: sexually_explicit
            displayName: Sexually Explicit
          - name: Threat
            value: threat
            displayName: Threat
          - name: Toxicity
            value: toxicity
            displayName: Toxicity
        - displayName: Score Threshold
          name: scoreThreshold
          type: number
          description: Score above which to return results. At zero, all scores are
            returned.
          default: 0
          typeOptions:
            minValue: 0
            maxValue: 1
            numberPrecision: 2
common_expressions:
- ={{$parameter["operation"]}}
api_patterns:
  http_methods:
  - POST
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: requestedAttributesUi
    text: Add Atrribute
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
  "$id": "https://n8n.io/schemas/nodes/googlePerspective.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Perspective Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "analyzeComment"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "analyzeComment"
          ],
          "default": "analyzeComment"
        },
        "text": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "requestedAttributesUi": {
          "description": "Attribute to analyze in the text. Details <a href=\"https://developers.perspectiveapi.com/s/about-the-api-attributes-and-languages\">here</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Atrribute"
          ]
        },
        "options": {
          "description": "Languages of the text input. If unspecified, the API will auto-detect the comment language. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
      "name": "googlePerspectiveOAuth2Api",
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
