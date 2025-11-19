---
title: "Node: HTML"
slug: "node-html"
version: "['1', '1.1', '1.2']"
updated: "2025-11-13"
summary: "Work with HTML"
node_type: "regular"
group: "['transform']"
---

# Node: HTML

**Purpose.** Work with HTML
**Subtitle.** ={{ $parameter["operation"] }}


---

## Node Details

- **Icon:** `{'light': 'file:html.svg', 'dark': 'file:html.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice** when operation=['generateHtmlTemplate']: <b>Tips</b>: Type ctrl+space for completions. Use <code>{{ }}</code> for expressions and <code>&lt;style&gt;</code> tags for CSS. JS in <code>&lt;script&gt;</code> tags is included but not executed in n8n.

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Generate HTML Template | `generateHtmlTemplate` |  |
| Extract HTML Content | `extractHtmlContent` |  |
| Convert to HTML Table | `convertToHtmlTable` |  |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | generateHtmlTemplate | ✗ | Operation to perform |  |

**Operation options:**

* **Generate HTML Template** (`generateHtmlTemplate`) - Generate HTML template
* **Extract HTML Content** (`extractHtmlContent`) - Extract HTML Content
* **Convert to HTML Table** (`convertToHtmlTable`) - Convert to HTML Table

---

### Generate HTML Template parameters (`generateHtmlTemplate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| HTML Template | `html` | string |  | ✗ | HTML template to render |  |

### Extract HTML Content parameters (`extractHtmlContent`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Source Data | `sourceData` | options | json | ✗ | If HTML should be read from binary or JSON data |  |

**Source Data options:**

* **Binary** (`binary`)
* **JSON** (`json`)

| Input Binary Field | `dataPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be extracted |  |
| JSON Property | `dataPropertyName` | string | data | ✓ | Name of the JSON property in which the HTML to extract the data from can be found. The property can either contain a string or an array of strings. |  |
| Options | `options` | collection | {} | ✗ | Whether to remove automatically all spaces and newlines from the beginning and end of the values | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Trim Values | `trimValues` | boolean | True | Whether to remove automatically all spaces and newlines from the beginning and end of the values |
| Clean Up Text | `cleanUpText` | boolean | True | Whether to remove leading and trailing whitespaces, line breaks (newlines) and condense multiple consecutive whitespaces into a single space |

</details>


### Convert to HTML Table parameters (`convertToHtmlTable`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Options | `options` | collection | {} | ✗ | Whether to capitalize the headers | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Capitalize Headers | `capitalize` | boolean | False | Whether to capitalize the headers |
| Custom Styling | `customStyling` | boolean | False | Whether to use custom styling |
| Caption | `caption` | string |  | Caption to add to the table |
| Table Attributes | `tableAttributes` | string |  | Attributes to attach to the table |
| Header Attributes | `headerAttributes` | string |  | Attributes to attach to the table header |
| Row Attributes | `rowAttributes` | string |  | Attributes to attach to the table row |
| Cell Attributes | `cellAttributes` | string |  | Attributes to attach to the table cell |

</details>


---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: HTML

**From workflow:** html extract fix

**Parameters:**
```json
{
  "operation": "extractHtmlContent",
  "extractionValues": {
    "values": [
      {
        "key": "data",
        "cssSelector": "html"
      }
    ]
  },
  "options": {
    "cleanUpText": true
  }
}
```

### Example 2: HTML2

**From workflow:** html extract fix

**Parameters:**
```json
{
  "operation": "extractHtmlContent",
  "extractionValues": {
    "values": [
      {
        "key": "data",
        "cssSelector": "html",
        "skipSelectors": "img, a"
      }
    ]
  },
  "options": {}
}
```

### Example 3: HTML3

**From workflow:** html extract fix

**Parameters:**
```json
{
  "operation": "extractHtmlContent",
  "extractionValues": {
    "values": [
      {
        "key": "data",
        "cssSelector": "p",
        "returnArray": true
      }
    ]
  },
  "options": {}
}
```

### Example 4: HTML1

**From workflow:** html extract fix

**Parameters:**
```json
{
  "operation": "extractHtmlContent",
  "extractionValues": {
    "values": [
      {
        "key": "data",
        "cssSelector": "=html"
      }
    ]
  },
  "options": {
    "trimValues": true
  }
}
```

### Example 5: HTML4

**From workflow:** html extract fix

**Parameters:**
```json
{
  "operation": "extractHtmlContent",
  "extractionValues": {
    "values": [
      {
        "key": "data",
        "cssSelector": "div",
        "returnValue": "attribute"
      }
    ]
  },
  "options": {}
}
```


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter["operation"] }}`

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
* Categories: Core Nodes
* Aliases: extract, template, table

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: html
displayName: HTML
description: Work with HTML
version:
- '1'
- '1.1'
- '1.2'
nodeType: regular
group:
- transform
operations:
- id: generateHtmlTemplate
  name: Generate HTML Template
  description: ''
  params:
  - id: html
    name: HTML Template
    type: string
    default: ''
    required: false
    description: HTML template to render
    validation:
      displayOptions:
        show:
          operation:
          - generateHtmlTemplate
    typeInfo:
      type: string
      displayName: HTML Template
      name: html
- id: extractHtmlContent
  name: Extract HTML Content
  description: ''
  params:
  - id: sourceData
    name: Source Data
    type: options
    default: json
    required: false
    description: If HTML should be read from binary or JSON data
    validation:
      displayOptions:
        show:
          operation:
          - extractHtmlContent
    typeInfo:
      type: options
      displayName: Source Data
      name: sourceData
      possibleValues:
      - value: binary
        name: Binary
        description: ''
      - value: json
        name: JSON
        description: ''
  - id: dataPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be extracted
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - extractHtmlContent
          sourceData:
          - json
    typeInfo: &id002
      type: string
      displayName: JSON Property
      name: dataPropertyName
  - id: dataPropertyName
    name: JSON Property
    type: string
    default: data
    required: true
    description: Name of the JSON property in which the HTML to extract the data from
      can be found. The property can either contain a string or an array of strings.
    validation: *id001
    typeInfo: *id002
- id: convertToHtmlTable
  name: Convert to HTML Table
  description: ''
  params: []
examples:
- name: HTML
  parameters:
    operation: extractHtmlContent
    extractionValues:
      values:
      - key: data
        cssSelector: html
    options:
      cleanUpText: true
  workflow: html extract fix
- name: HTML2
  parameters:
    operation: extractHtmlContent
    extractionValues:
      values:
      - key: data
        cssSelector: html
        skipSelectors: img, a
    options: {}
  workflow: html extract fix
- name: HTML3
  parameters:
    operation: extractHtmlContent
    extractionValues:
      values:
      - key: data
        cssSelector: p
        returnArray: true
    options: {}
  workflow: html extract fix
common_expressions:
- ={{ $parameter["operation"] }}
ui_elements:
  notices:
  - name: notice
    text: '<b>Tips</b>: Type ctrl+space for completions. Use <code>{{ }}</code> for
      expressions and <code>&lt;style&gt;</code> tags for CSS. JS in <code>&lt;script&gt;</code>
      tags is included but not executed in n8n.'
    conditions:
      show:
        operation:
        - generateHtmlTemplate
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  - field: options
    text: Add option
  hints:
  - field: dataPropertyName
    text: The name of the input binary field containing the file to be extracted
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
  "$id": "https://n8n.io/schemas/nodes/html.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HTML Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "generateHtmlTemplate",
        "extractHtmlContent",
        "convertToHtmlTable"
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
            "generateHtmlTemplate",
            "extractHtmlContent",
            "convertToHtmlTable"
          ],
          "default": "generateHtmlTemplate"
        },
        "html": {
          "description": "HTML template to render",
          "type": "string"
        },
        "sourceData": {
          "description": "If HTML should be read from binary or JSON data",
          "type": "string",
          "enum": [
            "binary",
            "json"
          ],
          "default": "json"
        },
        "dataPropertyName": {
          "description": "Name of the JSON property in which the HTML to extract the data from can be found. The property can either contain a string or an array of strings.",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "Whether to capitalize the headers",
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
    "version": [
      "1",
      "1.1",
      "1.2"
    ]
  },
  "examples": [
    {
      "description": "HTML",
      "value": {
        "operation": "extractHtmlContent",
        "extractionValues": {
          "values": [
            {
              "key": "data",
              "cssSelector": "html"
            }
          ]
        },
        "options": {
          "cleanUpText": true
        }
      }
    },
    {
      "description": "HTML2",
      "value": {
        "operation": "extractHtmlContent",
        "extractionValues": {
          "values": [
            {
              "key": "data",
              "cssSelector": "html",
              "skipSelectors": "img, a"
            }
          ]
        },
        "options": {}
      }
    },
    {
      "description": "HTML3",
      "value": {
        "operation": "extractHtmlContent",
        "extractionValues": {
          "values": [
            {
              "key": "data",
              "cssSelector": "p",
              "returnArray": true
            }
          ]
        },
        "options": {}
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1', '1.2'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
