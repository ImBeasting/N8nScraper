---
title: "Node: XML"
slug: "node-xml"
version: "1"
updated: "2025-11-13"
summary: "Convert data from and to XML"
node_type: "regular"
group: "['transform']"
---

# Node: XML

**Purpose.** Convert data from and to XML
**Subtitle.** ={{$parameter["mode"]==="jsonToxml" ? "JSON to XML" : "XML to JSON"}}


---

## Node Details

- **Icon:** `fa:file-code`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **xmlNotice** when mode=['xmlToJson']: If your XML is inside a binary file, use the 'Extract from File' node to convert it to text first

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Mode | `mode` | options | xmlToJson | ✗ | Converts data from JSON to XML |  |

**Mode options:**

* **JSON to XML** (`jsonToxml`) - Converts data from JSON to XML
* **XML to JSON** (`xmlToJson`) - Converts data from XML to JSON

| Property Name | `dataPropertyName` | string | data | ✓ | Name of the property to which to contains the converted XML data |  |
| Options | `options` | collection | {} | ✗ | Whether to allow using characters from the Unicode surrogate blocks | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Allow Surrogate Chars | `allowSurrogateChars` | boolean | False | Whether to allow using characters from the Unicode surrogate blocks |
| Attribute Key | `attrkey` | string | $ | Prefix that is used to access the attributes |
| Cdata | `cdata` | boolean | False | Whether to wrap text nodes in &lt;![CDATA[ ... ]]&gt; instead of escaping when necessary. Does not add &lt;![CDATA[ ... ]]&gt; if it is not required. |
| Character Key | `charkey` | string | _ | Prefix that is used to access the character content |
| Headless | `headless` | boolean | False | Whether to omit the XML header |
| Root Name | `rootName` | string | root | Root element name to be used |

</details>

| Property Name | `dataPropertyName` | string | data | ✓ | Name of the property which contains the XML data to convert |  |
| Options | `options` | collection | {} | ✗ | Prefix that is used to access the attributes | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attribute Key | `attrkey` | string | $ | Prefix that is used to access the attributes |
| Character Key | `charkey` | string | _ | Prefix that is used to access the character content |
| Explicit Array | `explicitArray` | boolean | False | Whether to always put child nodes in an array if true; otherwise an array is created only if there is more than one |
| Explicit Root | `explicitRoot` | boolean | True | Whether to set this if you want to get the root node in the resulting object |
| Ignore Attributes | `ignoreAttrs` | boolean | False | Whether to ignore all XML attributes and only create text nodes |
| Merge Attributes | `mergeAttrs` | boolean | True | Whether to merge attributes and child elements as properties of the parent, instead of keying attributes off a child attribute object. This option is ignored if ignoreAttrs is true. |
| Normalize | `normalize` | boolean | False | Whether to trim whitespaces inside text nodes |
| Normalize Tags | `normalizeTags` | boolean | False | Whether to normalize all tag names to lowercase |
| Trim | `trim` | boolean | False | Whether to trim the whitespace at the beginning and end of text nodes |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["mode"]==="jsonToxml" ? "JSON to XML" : "XML to JSON"}}`

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
* Aliases: Parse

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: xml
displayName: XML
description: Convert data from and to XML
version: '1'
nodeType: regular
group:
- transform
params:
- id: mode
  name: Mode
  type: options
  default: xmlToJson
  required: false
  description: Converts data from JSON to XML
  typeInfo:
    type: options
    displayName: Mode
    name: mode
    possibleValues:
    - value: jsonToxml
      name: JSON to XML
      description: Converts data from JSON to XML
    - value: xmlToJson
      name: XML to JSON
      description: Converts data from XML to JSON
- id: dataPropertyName
  name: Property Name
  type: string
  default: data
  required: true
  description: Name of the property to which to contains the converted XML data
  validation: &id001
    required: true
    displayOptions:
      show:
        mode:
        - xmlToJson
  typeInfo: &id002
    type: string
    displayName: Property Name
    name: dataPropertyName
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to allow using characters from the Unicode surrogate blocks
  placeholder: Add option
  validation: &id003
    displayOptions:
      show:
        mode:
        - xmlToJson
  typeInfo: &id004
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Attribute Key
      name: attrkey
      type: string
      description: Prefix that is used to access the attributes
      default: $
    - displayName: Character Key
      name: charkey
      type: string
      description: Prefix that is used to access the character content
      default: _
    - displayName: Explicit Array
      name: explicitArray
      type: boolean
      description: Whether to always put child nodes in an array if true; otherwise
        an array is created only if there is more than one
      default: false
    - displayName: Explicit Root
      name: explicitRoot
      type: boolean
      description: Whether to set this if you want to get the root node in the resulting
        object
      default: true
    - displayName: Ignore Attributes
      name: ignoreAttrs
      type: boolean
      description: Whether to ignore all XML attributes and only create text nodes
      default: false
    - displayName: Merge Attributes
      name: mergeAttrs
      type: boolean
      description: Whether to merge attributes and child elements as properties of
        the parent, instead of keying attributes off a child attribute object. This
        option is ignored if ignoreAttrs is true.
      default: true
    - displayName: Normalize
      name: normalize
      type: boolean
      description: Whether to trim whitespaces inside text nodes
      default: false
    - displayName: Normalize Tags
      name: normalizeTags
      type: boolean
      description: Whether to normalize all tag names to lowercase
      default: false
    - displayName: Trim
      name: trim
      type: boolean
      description: Whether to trim the whitespace at the beginning and end of text
        nodes
      default: false
- id: dataPropertyName
  name: Property Name
  type: string
  default: data
  required: true
  description: Name of the property which contains the XML data to convert
  validation: *id001
  typeInfo: *id002
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Prefix that is used to access the attributes
  placeholder: Add option
  validation: *id003
  typeInfo: *id004
common_expressions:
- '={{$parameter["mode"]==="jsonToxml" ? "JSON to XML" : "XML to JSON"}}'
ui_elements:
  notices:
  - name: xmlNotice
    text: If your XML is inside a binary file, use the 'Extract from File' node to
      convert it to text first
    conditions:
      show:
        mode:
        - xmlToJson
  tooltips: []
  placeholders:
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/xml.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "XML Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "mode": {
          "description": "Converts data from JSON to XML",
          "type": "string",
          "enum": [
            "jsonToxml",
            "xmlToJson"
          ],
          "default": "xmlToJson"
        },
        "dataPropertyName": {
          "description": "Name of the property which contains the XML data to convert",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "Prefix that is used to access the attributes",
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
