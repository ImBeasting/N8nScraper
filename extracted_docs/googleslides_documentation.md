---
title: "Node: Google Slides"
slug: "node-googleslides"
version: "['1', '2']"
updated: "2026-01-08"
summary: "Consume the Google Slides API"
node_type: "regular"
group: "['input', 'output']"
---

# Node: Google Slides

**Purpose.** Consume the Google Slides API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:googleslides.svg`
- **Group:** `['input', 'output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleApi**: N/A
- **googleSlidesOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleApi` | ✓ | {'show': {'authentication': ['serviceAccount']}} |
| `googleSlidesOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Presentation Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a presentation |
| Get | `get` | Get a presentation |
| Get Slides | `getSlides` | Get presentation slides |
| Replace Text | `replaceText` | Replace text in a presentation |

### Page Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a page |
| Get Thumbnail | `getThumbnail` | Get a thumbnail |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | presentation | ✗ | Resource to operate on |  |

**Resource options:**

* **Page** (`page`)
* **Presentation** (`presentation`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a presentation |  |

**Operation options:**

* **Create** (`create`) - Create a presentation
* **Get** (`get`) - Get a presentation
* **Get Slides** (`getSlides`) - Get presentation slides
* **Replace Text** (`replaceText`) - Replace text in a presentation

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ | Title of the presentation to create |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Presentation ID | `presentationId` | string |  | ✓ | ID of the presentation to retrieve. Found in the presentation URL: <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code> | e.g. 1wZtNFZ8MO-WKrxhYrOLMvyiqSgFwdSz5vn8_l_7eNqw |  |
| Page Object ID | `pageObjectId` | string |  | ✓ | ID of the page object to retrieve |  |

### Get Slides parameters (`getSlides`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Presentation ID | `presentationId` | string |  | ✓ | ID of the presentation to retrieve. Found in the presentation URL: <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code> | e.g. 1wZtNFZ8MO-WKrxhYrOLMvyiqSgFwdSz5vn8_l_7eNqw |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |

### Replace Text parameters (`replaceText`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Presentation ID | `presentationId` | string |  | ✓ | ID of the presentation to retrieve. Found in the presentation URL: <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code> | e.g. 1wZtNFZ8MO-WKrxhYrOLMvyiqSgFwdSz5vn8_l_7eNqw |  |
| Texts To Replace | `textUi` | fixedCollection | {} | ✗ | Whether the search should respect case. True : the search is case sensitive. False : the search is case insensitive. | e.g. Add Text |  |

<details>
<summary><strong>Texts To Replace sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Text | `textValues` |  |  |  |

</details>

| Options | `options` | collection | {} | ✗ | The revision ID of the presentation required for the write request. If specified and the requiredRevisionId doesn't exactly match the presentation's current revisionId, the request will not be processed and will return a 400 bad request error. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Revision ID | `revisionId` | string |  | The revision ID of the presentation required for the write request. If specified and the requiredRevisionId doesn't exactly match the presentation's current revisionId, the request will not be processed and will return a 400 bad request error. |

</details>


### Get Thumbnail parameters (`getThumbnail`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Presentation ID | `presentationId` | string |  | ✓ | ID of the presentation to retrieve. Found in the presentation URL: <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code> | e.g. 1wZtNFZ8MO-WKrxhYrOLMvyiqSgFwdSz5vn8_l_7eNqw |  |
| Page Object ID | `pageObjectId` | string |  | ✓ | ID of the page object to retrieve |  |
| Download | `download` | boolean | False | ✗ | Name of the binary property to which to write the data of the read page |  |
| Put Output File in Field | `binaryProperty` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |

---

## Load Options Methods

- `getPages`

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
node: googleSlides
displayName: Google Slides
description: Consume the Google Slides API
version:
- '1'
- '2'
nodeType: regular
group:
- input
- output
credentials:
- name: googleApi
  required: true
- name: googleSlidesOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a presentation
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the presentation to create
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - presentation
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
- id: get
  name: Get
  description: Get a presentation
  params:
  - id: presentationId
    name: Presentation ID
    type: string
    default: ''
    required: true
    description: 'ID of the presentation to retrieve. Found in the presentation URL:
      <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code>'
    placeholder: 1wZtNFZ8MO-WKrxhYrOLMvyiqSgFwdSz5vn8_l_7eNqw
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - presentation
          - page
          operation:
          - get
          - getThumbnail
          - getSlides
          - replaceText
    typeInfo: &id002
      type: string
      displayName: Presentation ID
      name: presentationId
  - id: pageObjectId
    name: Page Object ID
    type: string
    default: ''
    required: true
    description: ID of the page object to retrieve
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - page
          operation:
          - get
          - getThumbnail
    typeInfo: &id004
      type: string
      displayName: Page Object ID
      name: pageObjectId
- id: getSlides
  name: Get Slides
  description: Get presentation slides
  params:
  - id: presentationId
    name: Presentation ID
    type: string
    default: ''
    required: true
    description: 'ID of the presentation to retrieve. Found in the presentation URL:
      <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code>'
    placeholder: 1wZtNFZ8MO-WKrxhYrOLMvyiqSgFwdSz5vn8_l_7eNqw
    validation: *id001
    typeInfo: *id002
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
          - getSlides
          resource:
          - presentation
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
          - getSlides
          resource:
          - presentation
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
- id: replaceText
  name: Replace Text
  description: Replace text in a presentation
  params:
  - id: presentationId
    name: Presentation ID
    type: string
    default: ''
    required: true
    description: 'ID of the presentation to retrieve. Found in the presentation URL:
      <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code>'
    placeholder: 1wZtNFZ8MO-WKrxhYrOLMvyiqSgFwdSz5vn8_l_7eNqw
    validation: *id001
    typeInfo: *id002
  - id: textUi
    name: Texts To Replace
    type: fixedCollection
    default: {}
    required: false
    description: 'Whether the search should respect case. True : the search is case
      sensitive. False : the search is case insensitive.'
    placeholder: Add Text
    validation:
      displayOptions:
        show:
          resource:
          - presentation
          operation:
          - replaceText
    typeInfo:
      type: fixedCollection
      displayName: Texts To Replace
      name: textUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: textValues
        displayName: Text
        values:
        - displayName: Match Case
          name: matchCase
          type: boolean
          description: 'Whether the search should respect case. True : the search
            is case sensitive. False : the search is case insensitive.'
          default: false
        - displayName: Slide Names or IDs
          name: pageObjectIds
          type: multiOptions
          description: If non-empty, limits the matches to slide elements only on
            the given slides. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: []
          typeOptions:
            loadOptionsMethod: getPages
        - displayName: Search For
          name: text
          type: string
          description: The text to search for in the slide
          default: ''
        - displayName: Replace With
          name: replaceText
          type: string
          description: The text that will replace the matched text
          default: ''
- id: getThumbnail
  name: Get Thumbnail
  description: Get a thumbnail
  params:
  - id: presentationId
    name: Presentation ID
    type: string
    default: ''
    required: true
    description: 'ID of the presentation to retrieve. Found in the presentation URL:
      <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code>'
    placeholder: 1wZtNFZ8MO-WKrxhYrOLMvyiqSgFwdSz5vn8_l_7eNqw
    validation: *id001
    typeInfo: *id002
  - id: pageObjectId
    name: Page Object ID
    type: string
    default: ''
    required: true
    description: ID of the page object to retrieve
    validation: *id003
    typeInfo: *id004
  - id: download
    name: Download
    type: boolean
    default: false
    required: false
    description: Name of the binary property to which to write the data of the read
      page
    validation:
      displayOptions:
        show:
          resource:
          - page
          operation:
          - getThumbnail
    typeInfo:
      type: boolean
      displayName: Download
      name: download
  - id: binaryProperty
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - page
          operation:
          - getThumbnail
          download:
          - true
    typeInfo:
      type: string
      displayName: Put Output File in Field
      name: binaryProperty
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
  - field: presentationId
    text: 1wZtNFZ8MO-WKrxhYrOLMvyiqSgFwdSz5vn8_l_7eNqw
  - field: textUi
    text: Add Text
  - field: options
    text: Add option
  hints:
  - field: binaryProperty
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/googleSlides.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Slides Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "get",
        "getSlides",
        "replaceText",
        "getThumbnail"
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
            "oAuth2",
            "serviceAccount"
          ],
          "default": "serviceAccount"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "page",
            "presentation"
          ],
          "default": "presentation"
        },
        "operation": {
          "description": "Get a page",
          "type": "string",
          "enum": [
            "get",
            "getThumbnail"
          ],
          "default": "get"
        },
        "title": {
          "description": "Title of the presentation to create",
          "type": "string",
          "default": ""
        },
        "presentationId": {
          "description": "ID of the presentation to retrieve. Found in the presentation URL: <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code>",
          "type": "string",
          "default": "",
          "examples": [
            "1wZtNFZ8MO-WKrxhYrOLMvyiqSgFwdSz5vn8_l_7eNqw"
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
        },
        "pageObjectId": {
          "description": "ID of the page object to retrieve",
          "type": "string",
          "default": ""
        },
        "textUi": {
          "description": "Whether the search should respect case. True : the search is case sensitive. False : the search is case insensitive.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Text"
          ]
        },
        "options": {
          "description": "The revision ID of the presentation required for the write request. If specified and the requiredRevisionId doesn't exactly match the presentation's current revisionId, the request will not be processed and will return a 400 bad request error.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "download": {
          "description": "Name of the binary property to which to write the data of the read page",
          "type": "boolean",
          "default": false
        },
        "binaryProperty": {
          "description": "",
          "type": "string",
          "default": "data"
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
    "version": [
      "1",
      "2"
    ]
  },
  "credentials": [
    {
      "name": "googleApi",
      "required": true
    },
    {
      "name": "googleSlidesOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
