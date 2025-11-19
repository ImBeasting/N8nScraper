---
title: "Node: Rename Keys"
slug: "node-renamekeys"
version: "1"
updated: "2025-11-13"
summary: "Update item field names"
node_type: "regular"
group: "['transform']"
---

# Node: Rename Keys

**Purpose.** Update item field names


---

## Node Details

- **Icon:** `fa:edit`
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
| Keys | `keys` | fixedCollection | {} | ✗ | Adds a key which should be renamed | e.g. Add new key |  |

<details>
<summary><strong>Keys sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Key | `key` |  |  |  |

</details>

| Additional Options | `additionalOptions` | collection | {} | ✗ | Adds a regular expression | e.g. Add option |  |

<details>
<summary><strong>Additional Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Regex | `regexReplacement` | fixedCollection | {} | Adds a regular expression |

</details>


---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Rename Keys

**From workflow:** node-268-node-unit-test-rename-keys

**Parameters:**
```json
{
  "keys": {
    "key": [
      {
        "currentKey": "=propertyName",
        "newKey": "test"
      }
    ]
  },
  "additionalOptions": {}
}
```

### Example 2: Rename Keys with dot notation

**From workflow:** node-268-node-unit-test-rename-keys

**Parameters:**
```json
{
  "keys": {
    "key": [
      {
        "currentKey": "=propertyName.newPropertyName",
        "newKey": "test.dot"
      }
    ]
  },
  "additionalOptions": {}
}
```

### Example 3: Rename Keys with undefined

**From workflow:** node-268-node-unit-test-rename-keys

**Parameters:**
```json
{
  "keys": {
    "key": [
      {
        "currentKey": "=propertyName.newPropertyName"
      }
    ]
  },
  "additionalOptions": {}
}
```

### Example 4: Rename Keys with Regex

**From workflow:** node-268-node-unit-test-rename-keys

**Parameters:**
```json
{
  "additionalOptions": {
    "regexReplacement": {
      "replacements": [
        {
          "searchRegex": "reg",
          "replaceRegex": "test",
          "options": {}
        }
      ]
    }
  }
}
```


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter.additionalOptions.regexReplacement.replacements && $parameter.additionalOptions.regexReplacement.replacements.some(r => r.searchRegex && /(\\.\\*\\+|\\)\\*\\+|\\+\\*|\\*.*\\*|\\+.*\\+|\\?.*\\?|\\{[0-9]+,\\}|\\*{2,}|\\+{2,}|\\?{2,}|[a-zA-Z0-9]{4,}[\\*\\+]|\\([^)]*\\|[^)]*\\)[\\*\\+])/.test(r.searchRegex)) }}`

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
node: renameKeys
displayName: Rename Keys
description: Update item field names
version: '1'
nodeType: regular
group:
- transform
params:
- id: keys
  name: Keys
  type: fixedCollection
  default: {}
  required: false
  description: Adds a key which should be renamed
  placeholder: Add new key
  typeInfo:
    type: fixedCollection
    displayName: Keys
    name: keys
    typeOptions:
      multipleValues: true
    subProperties:
    - name: key
      displayName: Key
      values:
      - displayName: Current Key Name
        name: currentKey
        type: string
        description: 'The current name of the key. It is also possible to define deep
          keys by using dot-notation like for example: "level1.level2.currentKey".'
        placeholder: currentKey
        default: ''
      - displayName: New Key Name
        name: newKey
        type: string
        description: 'The name the key should be renamed to. It is also possible to
          define deep keys by using dot-notation like for example: "level1.level2.newKey".'
        placeholder: newKey
        default: ''
- id: additionalOptions
  name: Additional Options
  type: collection
  default: {}
  required: false
  description: Adds a regular expression
  hint: Learn more and test RegEx <a href="https://regex101.com/">here</a>
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Additional Options
    name: additionalOptions
    typeOptions:
      multipleValues: true
    subProperties:
    - displayName: Regex
      name: regexReplacement
      type: fixedCollection
      description: Adds a regular expression
      placeholder: Add new regular expression
      hint: Learn more and test RegEx <a href="https://regex101.com/">here</a>
      default: {}
      options:
      - name: replacements
        displayName: Replacement
        values:
        - displayName: Be aware that by using regular expression previously renamed
            keys can be affected
          name: regExNotice
          type: notice
          default: ''
        - displayName: Regular Expression
          name: searchRegex
          type: string
          description: Regex to match the key name
          placeholder: e.g. [N-n]ame
          hint: Learn more and test RegEx <a href="https://regex101.com/">here</a>
          default: ''
        - displayName: Replace With
          name: replaceRegex
          type: string
          description: The name the key/s should be renamed to. It's possible to use
            regex captures e.g. $1, $2, ...
          placeholder: replacedName
          default: ''
        - displayName: Options
          name: options
          type: collection
          description: Whether to use case insensitive match
          placeholder: Add Regex Option
          hint: Specify number for depth level (-1 for unlimited, 0 for top level
            only)
          default: {}
          options:
          - displayName: Case Insensitive
            name: caseInsensitive
            type: boolean
            description: Whether to use case insensitive match
            default: false
          - displayName: Max Depth
            name: depth
            type: number
            description: Maximum depth to replace keys
            hint: Specify number for depth level (-1 for unlimited, 0 for top level
              only)
      typeOptions:
        multipleValues: true
examples:
- name: Rename Keys
  parameters:
    keys:
      key:
      - currentKey: =propertyName
        newKey: test
    additionalOptions: {}
  workflow: node-268-node-unit-test-rename-keys
- name: Rename Keys with dot notation
  parameters:
    keys:
      key:
      - currentKey: =propertyName.newPropertyName
        newKey: test.dot
    additionalOptions: {}
  workflow: node-268-node-unit-test-rename-keys
- name: Rename Keys with undefined
  parameters:
    keys:
      key:
      - currentKey: =propertyName.newPropertyName
    additionalOptions: {}
  workflow: node-268-node-unit-test-rename-keys
common_expressions:
- ={{ $parameter.additionalOptions.regexReplacement.replacements && $parameter.additionalOptions.regexReplacement.replacements.some(r
  => r.searchRegex && /(\\.\\*\\+|\\)\\*\\+|\\+\\*|\\*.*\\*|\\+.*\\+|\\?.*\\?|\\{[0-9]+,\\}|\\*{2,}|\\+{2,}|\\?{2,}|[a-zA-Z0-9]{4,}[\\*\\+]|\\([^)]*\\|[^)]*\\)[\\*\\+])/.test(r.searchRegex))
  }}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: keys
    text: Add new key
  - field: additionalOptions
    text: Add option
  hints:
  - field: additionalOptions
    text: Learn more and test RegEx <a href="https://regex101.com/">here</a>
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
  "$id": "https://n8n.io/schemas/nodes/renameKeys.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Rename Keys Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "keys": {
          "description": "Adds a key which should be renamed",
          "type": "string",
          "default": {},
          "examples": [
            "Add new key"
          ]
        },
        "additionalOptions": {
          "description": "Adds a regular expression",
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
  "examples": [
    {
      "description": "Rename Keys",
      "value": {
        "keys": {
          "key": [
            {
              "currentKey": "=propertyName",
              "newKey": "test"
            }
          ]
        },
        "additionalOptions": {}
      }
    },
    {
      "description": "Rename Keys with dot notation",
      "value": {
        "keys": {
          "key": [
            {
              "currentKey": "=propertyName.newPropertyName",
              "newKey": "test.dot"
            }
          ]
        },
        "additionalOptions": {}
      }
    },
    {
      "description": "Rename Keys with undefined",
      "value": {
        "keys": {
          "key": [
            {
              "currentKey": "=propertyName.newPropertyName"
            }
          ]
        },
        "additionalOptions": {}
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
