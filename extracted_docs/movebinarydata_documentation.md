---
title: "Node: Convert to/from binary data"
slug: "node-movebinarydata"
version: "['1', '1.1']"
updated: "2025-11-13"
summary: "Move data between binary and JSON properties"
node_type: "regular"
group: "['transform']"
---

# Node: Convert to/from binary data

**Purpose.** Move data between binary and JSON properties
**Subtitle.** ={{$parameter["mode"]==="binaryToJson" ? "Binary to JSON" : "JSON to Binary"}}


---

## Node Details

- **Icon:** `fa:exchange-alt`
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
| Mode | `mode` | options | binaryToJson | ✗ | Move data from Binary to JSON |  |

**Mode options:**

* **Binary to JSON** (`binaryToJson`) - Move data from Binary to JSON
* **JSON to Binary** (`jsonToBinary`) - Move data from JSON to Binary

| Set All Data | `setAllData` | boolean | True | ✗ | Whether all JSON data should be replaced with the data retrieved from binary key. Else the data will be written to a single key. |  |
| Source Key | `sourceKey` | string | data | ✓ | The name of the binary key to get data from. It is also possible to define deep keys by using dot-notation like for example: "level1.level2.currentKey". | e.g. data |  |
| Destination Key | `destinationKey` | string | data | ✓ | The name the JSON key to copy data to. It is also possible to define deep keys by using dot-notation like for example: "level1.level2.newKey". |  |
| Convert All Data | `convertAllData` | boolean | True | ✗ | Whether all JSON data should be converted to binary. Else only the data of one key will be converted. |  |
| Source Key | `sourceKey` | string | data | ✓ | The name of the JSON key to get data from. It is also possible to define deep keys by using dot-notation like for example: "level1.level2.currentKey". | e.g. data |  |
| Destination Key | `destinationKey` | string | data | ✓ | The name the binary key to copy data to. It is also possible to define deep keys by using dot-notation like for example: "level1.level2.newKey". | e.g. data |  |
| Options | `options` | collection | {} | ✗ | Whether to add special marker at the start of your text file. This marker helps some programs understand how to read the file correctly. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Add Byte Order Mark (BOM) | `addBOM` | boolean | False | Whether to add special marker at the start of your text file. This marker helps some programs understand how to read the file correctly. |
| Data Is Base64 | `dataIsBase64` | boolean | False | Whether to keep the binary data as base64 string |
| Encoding | `encoding` | options | utf8 | Choose the character set to use to encode the data |
| Strip BOM | `stripBOM` | boolean | True |  |
| File Name | `fileName` | string |  | The file name to set |
| JSON Parse | `jsonParse` | boolean | False | Whether to run JSON parse on the data to get proper object data |
| Keep Source | `keepSource` | boolean | False | Whether the source key should be kept. By default it will be deleted. |
| Keep As Base64 | `keepAsBase64` | boolean | False | Whether to keep the binary data as base64 string |
| MIME Type | `mimeType` | string | application/json | The mime-type to set. By default will the mime-type for JSON be set. |
| Use Raw Data | `useRawData` | boolean | False | Whether to use data as is and do not JSON.stringify it |

</details>


---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Binary to JSON - No Set All Data

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "setAllData": false,
  "options": {}
}
```

### Example 2: Binary to JSON

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "options": {}
}
```

### Example 3: JSON to Binary

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "mode": "jsonToBinary",
  "options": {}
}
```

### Example 4: JSON to Binary - No Convert All Data

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "mode": "jsonToBinary",
  "convertAllData": false,
  "sourceKey": "title",
  "options": {
    "fileName": "example.json"
  }
}
```

### Example 5: Binary to JSON - No Set All Data + Json Parse

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "setAllData": false,
  "options": {
    "jsonParse": true
  }
}
```


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["mode"]==="binaryToJson" ? "Binary to JSON" : "JSON to Binary"}}`

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
* Aliases: Move Binary Data

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: moveBinaryData
displayName: Convert to/from binary data
description: Move data between binary and JSON properties
version:
- '1'
- '1.1'
nodeType: regular
group:
- transform
params:
- id: mode
  name: Mode
  type: options
  default: binaryToJson
  required: false
  description: Move data from Binary to JSON
  typeInfo:
    type: options
    displayName: Mode
    name: mode
    possibleValues:
    - value: binaryToJson
      name: Binary to JSON
      description: Move data from Binary to JSON
    - value: jsonToBinary
      name: JSON to Binary
      description: Move data from JSON to Binary
- id: setAllData
  name: Set All Data
  type: boolean
  default: true
  required: false
  description: Whether all JSON data should be replaced with the data retrieved from
    binary key. Else the data will be written to a single key.
  validation:
    displayOptions:
      show:
        mode:
        - binaryToJson
  typeInfo:
    type: boolean
    displayName: Set All Data
    name: setAllData
- id: sourceKey
  name: Source Key
  type: string
  default: data
  required: true
  description: 'The name of the binary key to get data from. It is also possible to
    define deep keys by using dot-notation like for example: "level1.level2.currentKey".'
  placeholder: data
  validation: &id001
    required: true
    displayOptions:
      show:
        convertAllData:
        - false
        mode:
        - jsonToBinary
  typeInfo: &id002
    type: string
    displayName: Source Key
    name: sourceKey
- id: destinationKey
  name: Destination Key
  type: string
  default: data
  required: true
  description: 'The name the JSON key to copy data to. It is also possible to define
    deep keys by using dot-notation like for example: "level1.level2.newKey".'
  validation: &id003
    required: true
    displayOptions:
      show:
        mode:
        - jsonToBinary
  typeInfo: &id004
    type: string
    displayName: Destination Key
    name: destinationKey
- id: convertAllData
  name: Convert All Data
  type: boolean
  default: true
  required: false
  description: Whether all JSON data should be converted to binary. Else only the
    data of one key will be converted.
  validation:
    displayOptions:
      show:
        mode:
        - jsonToBinary
  typeInfo:
    type: boolean
    displayName: Convert All Data
    name: convertAllData
- id: sourceKey
  name: Source Key
  type: string
  default: data
  required: true
  description: 'The name of the JSON key to get data from. It is also possible to
    define deep keys by using dot-notation like for example: "level1.level2.currentKey".'
  placeholder: data
  validation: *id001
  typeInfo: *id002
- id: destinationKey
  name: Destination Key
  type: string
  default: data
  required: true
  description: 'The name the binary key to copy data to. It is also possible to define
    deep keys by using dot-notation like for example: "level1.level2.newKey".'
  placeholder: data
  validation: *id003
  typeInfo: *id004
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to add special marker at the start of your text file. This
    marker helps some programs understand how to read the file correctly.
  placeholder: Add option
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Add Byte Order Mark (BOM)
      name: addBOM
      type: boolean
      description: Whether to add special marker at the start of your text file. This
        marker helps some programs understand how to read the file correctly.
      default: false
      displayOptions:
        show: {}
    - displayName: Data Is Base64
      name: dataIsBase64
      type: boolean
      description: Whether to keep the binary data as base64 string
      default: false
      displayOptions:
        show: {}
        hide:
          useRawData:
          - true
    - displayName: Encoding
      name: encoding
      type: options
      description: Choose the character set to use to encode the data
      default: utf8
      displayOptions:
        show: {}
    - displayName: Strip BOM
      name: stripBOM
      type: boolean
      default: true
      displayOptions:
        show: {}
    - displayName: File Name
      name: fileName
      type: string
      description: The file name to set
      placeholder: example.json
      default: ''
      displayOptions:
        show: {}
    - displayName: JSON Parse
      name: jsonParse
      type: boolean
      description: Whether to run JSON parse on the data to get proper object data
      default: false
      displayOptions:
        show: {}
        hide:
          keepAsBase64:
          - true
    - displayName: Keep Source
      name: keepSource
      type: boolean
      description: Whether the source key should be kept. By default it will be deleted.
      default: false
    - displayName: Keep As Base64
      name: keepAsBase64
      type: boolean
      description: Whether to keep the binary data as base64 string
      default: false
      displayOptions:
        show: {}
        hide:
          jsonParse:
          - true
    - displayName: MIME Type
      name: mimeType
      type: string
      description: The mime-type to set. By default will the mime-type for JSON be
        set.
      placeholder: application/json
      default: application/json
      displayOptions:
        show: {}
    - displayName: Use Raw Data
      name: useRawData
      type: boolean
      description: Whether to use data as is and do not JSON.stringify it
      default: false
      displayOptions:
        show: {}
        hide:
          dataIsBase64:
          - true
examples:
- name: Binary to JSON - No Set All Data
  parameters:
    setAllData: false
    options: {}
  workflow: Unnamed workflow
- name: Binary to JSON
  parameters:
    options: {}
  workflow: Unnamed workflow
- name: JSON to Binary
  parameters:
    mode: jsonToBinary
    options: {}
  workflow: Unnamed workflow
common_expressions:
- '={{$parameter["mode"]==="binaryToJson" ? "Binary to JSON" : "JSON to Binary"}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: sourceKey
    text: data
  - field: sourceKey
    text: data
  - field: destinationKey
    text: data
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
  "$id": "https://n8n.io/schemas/nodes/moveBinaryData.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Convert to/from binary data Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "mode": {
          "description": "Move data from Binary to JSON",
          "type": "string",
          "enum": [
            "binaryToJson",
            "jsonToBinary"
          ],
          "default": "binaryToJson"
        },
        "setAllData": {
          "description": "Whether all JSON data should be replaced with the data retrieved from binary key. Else the data will be written to a single key.",
          "type": "boolean",
          "default": true
        },
        "sourceKey": {
          "description": "The name of the JSON key to get data from. It is also possible to define deep keys by using dot-notation like for example: \"level1.level2.currentKey\".",
          "type": "string",
          "default": "data",
          "examples": [
            "data"
          ]
        },
        "destinationKey": {
          "description": "The name the binary key to copy data to. It is also possible to define deep keys by using dot-notation like for example: \"level1.level2.newKey\".",
          "type": "string",
          "default": "data",
          "examples": [
            "data"
          ]
        },
        "convertAllData": {
          "description": "Whether all JSON data should be converted to binary. Else only the data of one key will be converted.",
          "type": "boolean",
          "default": true
        },
        "options": {
          "description": "Whether to add special marker at the start of your text file. This marker helps some programs understand how to read the file correctly.",
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
      "1.1"
    ]
  },
  "examples": [
    {
      "description": "Binary to JSON - No Set All Data",
      "value": {
        "setAllData": false,
        "options": {}
      }
    },
    {
      "description": "Binary to JSON",
      "value": {
        "options": {}
      }
    },
    {
      "description": "JSON to Binary",
      "value": {
        "mode": "jsonToBinary",
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
| ['1', '1.1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
