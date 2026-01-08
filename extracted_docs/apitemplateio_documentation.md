---
title: "Node: APITemplate.io"
slug: "node-apitemplateio"
version: "1"
updated: "2026-01-08"
summary: "Consume the APITemplate.io API"
node_type: "regular"
group: "['transform']"
---

# Node: APITemplate.io

**Purpose.** Consume the APITemplate.io API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:apiTemplateIo.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **apiTemplateIoApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `apiTemplateIoApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** GET

**Headers Used:** user-agent

---

## Operations

### Image Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an image |

### Pdf Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a pdf |

### Account Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get an account |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | image | ✗ | Resource to operate on |  |

**Resource options:**

* **Account** (`account`)
* **Image** (`image`)
* **PDF** (`pdf`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✓ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create an image

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Template Name or ID | `imageTemplateId` | options |  | ✓ | ID of the image template to use. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Template Name or ID | `pdfTemplateId` | options |  | ✓ | ID of the PDF template to use. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Download | `download` | boolean | False | ✗ | Name of the binary property to which to write the data of the read file |  |
| Put Output File in Field | `binaryProperty` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| Overrides (JSON) | `overridesJson` | json |  | ✗ | e.g. [ {"name": "text_1", "text": "hello world", "textBackgroundColor": "rgba(246, 243, 243, 0)" } ] |  |
| Properties (JSON) | `propertiesJson` | json |  | ✗ | e.g. { "name": "text_1" } |  |
| Overrides | `overridesUi` | fixedCollection | {} | ✗ | Name of the property | e.g. Add Override |  |

<details>
<summary><strong>Overrides sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Override | `overrideValues` |  |  |  |

</details>

| Properties | `propertiesUi` | fixedCollection | {} | ✗ | Name of the property | e.g. Add Property |  |

<details>
<summary><strong>Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Property | `propertyValues` |  |  |  |

</details>

| Options | `options` | collection | {} | ✗ | The name of the downloaded image/pdf. It has to include the extension. For example: report.pdf | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Name | `fileName` | string |  | The name of the downloaded image/pdf. It has to include the extension. For example: report.pdf |

</details>


---

## Load Options Methods

- `getImageTemplates`

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
node: apiTemplateIo
displayName: APITemplate.io
description: Consume the APITemplate.io API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: apiTemplateIoApi
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: imageTemplateId
    name: Template Name or ID
    type: options
    default: ''
    required: true
    description: ID of the image template to use. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - image
          operation:
          - create
    typeInfo:
      type: options
      displayName: Template Name or ID
      name: imageTemplateId
      typeOptions:
        loadOptionsMethod: getImageTemplates
      possibleValues: []
  - id: pdfTemplateId
    name: Template Name or ID
    type: options
    default: ''
    required: true
    description: ID of the PDF template to use. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - pdf
          operation:
          - create
    typeInfo:
      type: options
      displayName: Template Name or ID
      name: pdfTemplateId
      typeOptions:
        loadOptionsMethod: getPdfTemplates
      possibleValues: []
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - pdf
          - image
          operation:
          - create
    typeInfo:
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: download
    name: Download
    type: boolean
    default: false
    required: false
    description: Name of the binary property to which to write the data of the read
      file
    validation:
      displayOptions:
        show:
          resource:
          - pdf
          - image
          operation:
          - create
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
          - pdf
          - image
          operation:
          - create
          download:
          - true
    typeInfo:
      type: string
      displayName: Put Output File in Field
      name: binaryProperty
  - id: overridesJson
    name: Overrides (JSON)
    type: json
    default: ''
    required: false
    description: ''
    placeholder: '[ {"name": "text_1", "text": "hello world", "textBackgroundColor":
      "rgba(246, 243, 243, 0)" } ]'
    validation:
      displayOptions:
        show:
          resource:
          - image
          operation:
          - create
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Overrides (JSON)
      name: overridesJson
  - id: propertiesJson
    name: Properties (JSON)
    type: json
    default: ''
    required: false
    description: ''
    placeholder: '{ "name": "text_1" }'
    validation:
      displayOptions:
        show:
          resource:
          - pdf
          operation:
          - create
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Properties (JSON)
      name: propertiesJson
  - id: overridesUi
    name: Overrides
    type: fixedCollection
    default: {}
    required: false
    description: Name of the property
    placeholder: Add Override
    validation:
      displayOptions:
        show:
          resource:
          - image
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: fixedCollection
      displayName: Overrides
      name: overridesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: overrideValues
        displayName: Override
        values:
        - displayName: Properties
          name: propertiesUi
          type: fixedCollection
          description: Name of the property
          placeholder: Add Property
          default: {}
          options:
          - name: propertyValues
            displayName: Property
            values:
            - displayName: Key
              name: key
              type: string
              description: Name of the property
              default: ''
            - displayName: Value
              name: value
              type: string
              description: Value to the property
              default: ''
          typeOptions:
            multipleValues: true
  - id: propertiesUi
    name: Properties
    type: fixedCollection
    default: {}
    required: false
    description: Name of the property
    placeholder: Add Property
    validation:
      displayOptions:
        show:
          resource:
          - pdf
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: fixedCollection
      displayName: Properties
      name: propertiesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: propertyValues
        displayName: Property
        values:
        - displayName: Key
          name: key
          type: string
          description: Name of the property
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value to the property
          default: ''
- id: get
  name: Get
  description: ''
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - GET
  endpoints: []
  headers:
  - user-agent
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: overridesJson
    text: '[ {"name": "text_1", "text": "hello world", "textBackgroundColor": "rgba(246,
      243, 243, 0)" } ]'
  - field: propertiesJson
    text: '{ "name": "text_1" }'
  - field: overridesUi
    text: Add Override
  - field: propertiesUi
    text: Add Property
  - field: options
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/apiTemplateIo.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "APITemplate.io Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "get"
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
            "account",
            "image",
            "pdf"
          ],
          "default": "image"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "get"
          ],
          "default": "get"
        },
        "imageTemplateId": {
          "description": "ID of the image template to use. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "pdfTemplateId": {
          "description": "ID of the PDF template to use. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "download": {
          "description": "Name of the binary property to which to write the data of the read file",
          "type": "boolean",
          "default": false
        },
        "binaryProperty": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "overridesJson": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "[ {\"name\": \"text_1\", \"text\": \"hello world\", \"textBackgroundColor\": \"rgba(246, 243, 243, 0)\" } ]"
          ]
        },
        "propertiesJson": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "{ \"name\": \"text_1\" }"
          ]
        },
        "overridesUi": {
          "description": "Name of the property",
          "type": "string",
          "default": {},
          "examples": [
            "Add Override"
          ]
        },
        "propertiesUi": {
          "description": "Name of the property",
          "type": "string",
          "default": {},
          "examples": [
            "Add Property"
          ]
        },
        "options": {
          "description": "The name of the downloaded image/pdf. It has to include the extension. For example: report.pdf",
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
      "name": "apiTemplateIoApi",
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
