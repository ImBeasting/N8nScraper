---
title: "Node: Brandfetch"
slug: "node-brandfetch"
version: "1"
updated: "2026-01-08"
summary: "Consume Brandfetch API"
node_type: "regular"
group: "['output']"
---

# Node: Brandfetch

**Purpose.** Consume Brandfetch API
**Subtitle.** ={{$parameter["operation"]}}


---

## Node Details

- **Icon:** `file:brandfetch.png`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **brandfetchApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `brandfetchApi` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Color | `color` | Return a company's colors |
| Company | `company` | Return a company's data |
| Font | `font` | Return a company's fonts |
| Industry | `industry` | Return a company's industry |
| Logo | `logo` | Return a company's logo & icon |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | logo | ✗ | Return a company's colors |  |

**Operation options:**

* **Color** (`color`) - Return a company's colors
* **Company** (`company`) - Return a company's data
* **Font** (`font`) - Return a company's fonts
* **Industry** (`industry`) - Return a company's industry
* **Logo** (`logo`) - Return a company's logo & icon

---

### Logo parameters (`logo`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Download | `download` | boolean | False | ✓ | Name of the binary property to which to write the data of the read file |  |
| Image Type | `imageTypes` | multiOptions |  | ✓ |  |  |

**Image Type options:**

* **Icon** (`icon`)
* **Logo** (`logo`)

| Image Format | `imageFormats` | multiOptions |  | ✓ | The image format in which the logo should be returned as |  |

**Image Format options:**

* **PNG** (`png`)
* **SVG** (`svg`)


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
* Categories: Utility, Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: Brandfetch
displayName: Brandfetch
description: Consume Brandfetch API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: brandfetchApi
  required: true
operations:
- id: color
  name: Color
  description: Return a company's colors
- id: company
  name: Company
  description: Return a company's data
- id: font
  name: Font
  description: Return a company's fonts
- id: industry
  name: Industry
  description: Return a company's industry
- id: logo
  name: Logo
  description: Return a company's logo & icon
  params:
  - id: download
    name: Download
    type: boolean
    default: false
    required: true
    description: Name of the binary property to which to write the data of the read
      file
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - logo
    typeInfo:
      type: boolean
      displayName: Download
      name: download
  - id: imageTypes
    name: Image Type
    type: multiOptions
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - logo
          download:
          - true
    typeInfo:
      type: multiOptions
      displayName: Image Type
      name: imageTypes
      possibleValues:
      - value: icon
        name: Icon
        description: ''
      - value: logo
        name: Logo
        description: ''
  - id: imageFormats
    name: Image Format
    type: multiOptions
    default: ''
    required: true
    description: The image format in which the logo should be returned as
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - logo
          download:
          - true
    typeInfo:
      type: multiOptions
      displayName: Image Format
      name: imageFormats
      possibleValues:
      - value: png
        name: PNG
        description: ''
      - value: svg
        name: SVG
        description: ''
common_expressions:
- ={{$parameter["operation"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders: []
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
  "$id": "https://n8n.io/schemas/nodes/Brandfetch.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Brandfetch Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "color",
        "company",
        "font",
        "industry",
        "logo"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Return a company's colors",
          "type": "string",
          "enum": [
            "color",
            "company",
            "font",
            "industry",
            "logo"
          ],
          "default": "logo"
        },
        "domain": {
          "description": "The domain name of the company",
          "type": "string",
          "default": ""
        },
        "download": {
          "description": "Name of the binary property to which to write the data of the read file",
          "type": "boolean",
          "default": false
        },
        "imageTypes": {
          "description": "",
          "type": "string"
        },
        "imageFormats": {
          "description": "The image format in which the logo should be returned as",
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
  },
  "credentials": [
    {
      "name": "brandfetchApi",
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
