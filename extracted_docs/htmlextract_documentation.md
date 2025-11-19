---
title: "Node: HTML Extract"
slug: "node-htmlextract"
version: "1"
updated: "2025-11-13"
summary: "Extracts data from HTML"
node_type: "regular"
group: "['transform']"
---

# Node: HTML Extract

**Purpose.** Extracts data from HTML
**Subtitle.** ={{$parameter["sourceData"] + ": " + $parameter["dataPropertyName"]}}


---

## Node Details

- **Icon:** `fa:cut`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Source Data | `sourceData` | options | json | ✗ | If HTML should be read from binary or JSON data |  |

**Source Data options:**

* **Binary** (`binary`)
* **JSON** (`json`)

| Input Binary Field | `dataPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be extracted |  |
| JSON Property | `dataPropertyName` | string | data | ✓ | Name of the JSON property in which the HTML to extract the data from can be found. The property can either contain a string or an array of strings. |  |
| Extraction Values | `extractionValues` | fixedCollection | {} | ✗ | The key under which the extracted value should be saved | e.g. Add Value |  |

<details>
<summary><strong>Extraction Values sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Values | `values` |  |  |  |

</details>

| Options | `options` | collection | {} | ✗ | Whether to remove automatically all spaces and newlines from the beginning and end of the values | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Trim Values | `trimValues` | boolean | True | Whether to remove automatically all spaces and newlines from the beginning and end of the values |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["sourceData"] + ": " + $parameter["dataPropertyName"]}}`

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: htmlExtract
displayName: HTML Extract
description: Extracts data from HTML
version: '1'
nodeType: regular
group:
- transform
params:
- id: sourceData
  name: Source Data
  type: options
  default: json
  required: false
  description: If HTML should be read from binary or JSON data
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
- id: extractionValues
  name: Extraction Values
  type: fixedCollection
  default: {}
  required: false
  description: The key under which the extracted value should be saved
  placeholder: Add Value
  validation:
    displayOptions:
      show:
        returnValue:
        - attribute
  typeInfo:
    type: fixedCollection
    displayName: Extraction Values
    name: extractionValues
    typeOptions:
      multipleValues: true
    subProperties:
    - name: values
      displayName: Values
      values:
      - displayName: Key
        name: key
        type: string
        description: The key under which the extracted value should be saved
        default: ''
      - displayName: CSS Selector
        name: cssSelector
        type: string
        description: The CSS selector to use
        placeholder: .price
        default: ''
      - displayName: Return Value
        name: returnValue
        type: options
        description: Get an attribute value like "class" from an element
        value: attribute
        default: text
        options:
        - name: Attribute
          description: Get an attribute value like "class" from an element
          value: attribute
          displayName: Attribute
        - name: HTML
          description: Get the HTML the element contains
          value: html
          displayName: Html
        - name: Text
          description: Get only the text content of the element
          value: text
          displayName: Text
        - name: Value
          description: Get value of an input, select or textarea
          value: value
          displayName: Value
      - displayName: Attribute
        name: attribute
        type: string
        description: The name of the attribute to return the value off
        placeholder: class
        default: ''
        displayOptions:
          show:
            returnValue:
            - attribute
      - displayName: Return Array
        name: returnArray
        type: boolean
        description: Whether to return the values as an array so if multiple ones
          get found they also get returned separately. If not set all will be returned
          as a single string.
        default: false
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to remove automatically all spaces and newlines from the beginning
    and end of the values
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Trim Values
      name: trimValues
      type: boolean
      description: Whether to remove automatically all spaces and newlines from the
        beginning and end of the values
      default: true
common_expressions:
- '={{$parameter["sourceData"] + ": " + $parameter["dataPropertyName"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: extractionValues
    text: Add Value
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
  "$id": "https://n8n.io/schemas/nodes/htmlExtract.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HTML Extract Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
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
        "extractionValues": {
          "description": "The key under which the extracted value should be saved",
          "type": "string",
          "default": {},
          "examples": [
            "Add Value"
          ]
        },
        "options": {
          "description": "Whether to remove automatically all spaces and newlines from the beginning and end of the values",
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
