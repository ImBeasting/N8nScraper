---
title: "Node: Microsoft SharePoint"
slug: "node-microsoftsharepoint"
version: "1"
updated: "2025-11-13"
summary: "Interact with Microsoft SharePoint API"
node_type: "regular"
group: "['transform']"
---

# Node: Microsoft SharePoint

**Purpose.** Interact with Microsoft SharePoint API
**Subtitle.** ={{ $parameter["operation"] + ": " + $parameter["resource"] }}


---

## Node Details

- **Icon:** `{'light': 'file:microsoftSharePoint.svg', 'dark': 'file:microsoftSharePoint.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftSharePointOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `microsoftSharePointOAuth2Api` | ✓ | - |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | file | ✗ | Resource to operate on |  |

**Resource options:**

* **File** (`file`)
* **Item** (`item`)
* **List** (`list`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | file | ✗ |  |  |

**Resource options:**

* **File** (`file`)
* **Item** (`item`)
* **List** (`list`)


---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Microsoft SharePoint

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "operation": "update",
  "site": {
    "__rl": true,
    "value": "site1",
    "mode": "list",
    "cachedResultName": "site1"
  },
  "folder": {
    "__rl": true,
    "value": "folder1",
    "mode": "list",
    "cachedResultName": "folder1"
  },
  "file": {
    "__rl": true,
    "value": "item1",
    "mode": "list",
    "cachedResultName": "file1.json"
  },
  "fileName": "file2.json",
  "changeFileContent": true,
  "fileContents": "data",
  "requestOptions": {}
}
```

**Credentials:**
- microsoftSharePointOAuth2Api: `Microsoft SharePoint account`

### Example 2: Microsoft SharePoint

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "operation": "upload",
  "site": {
    "__rl": true,
    "value": "site1",
    "mode": "list",
    "cachedResultName": "site1"
  },
  "folder": {
    "__rl": true,
    "value": "folder1",
    "mode": "list",
    "cachedResultName": "folder1"
  },
  "fileName": "file1.json",
  "fileContents": "data",
  "requestOptions": {}
}
```

**Credentials:**
- microsoftSharePointOAuth2Api: `Microsoft SharePoint account`

### Example 3: Microsoft SharePoint

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "site": {
    "__rl": true,
    "value": "site1",
    "mode": "list",
    "cachedResultName": "site1"
  },
  "folder": {
    "__rl": true,
    "value": "folder1",
    "mode": "list",
    "cachedResultName": "folder1"
  },
  "file": {
    "__rl": true,
    "value": "item1",
    "mode": "list",
    "cachedResultName": "file.json"
  },
  "requestOptions": {}
}
```

**Credentials:**
- microsoftSharePointOAuth2Api: `Microsoft SharePoint account`

### Example 4: Microsoft SharePoint

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "item",
  "site": {
    "__rl": true,
    "value": "site1",
    "mode": "list",
    "cachedResultName": "site1"
  },
  "list": {
    "__rl": true,
    "value": "list1",
    "mode": "list",
    "cachedResultName": "list1"
  },
  "filter": "fields/Title eq 'item1'",
  "returnAll": true,
  "options": {
    "fields": [
      "contentType",
      "createdDateTime",
      "createdBy",
      "fields",
      "id",
      "lastModifiedDateTime",
      "lastModifiedBy",
      "parentReference",
      "webUrl"
    ]
  },
  "simplify": false,
  "requestOptions": {}
}
```

**Credentials:**
- microsoftSharePointOAuth2Api: `Microsoft SharePoint account`

### Example 5: Microsoft SharePoint

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "item",
  "operation": "delete",
  "site": {
    "__rl": true,
    "value": "site1",
    "mode": "list",
    "cachedResultName": "site1"
  },
  "list": {
    "__rl": true,
    "value": "list1",
    "mode": "list",
    "cachedResultName": "list1"
  },
  "item": {
    "__rl": true,
    "value": "item1",
    "mode": "list",
    "cachedResultName": "item1"
  },
  "requestOptions": {}
}
```

**Credentials:**
- microsoftSharePointOAuth2Api: `Microsoft SharePoint account`


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter["operation"] + ": " + $parameter["resource"] }}`

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: microsoftSharePoint
displayName: Microsoft SharePoint
description: Interact with Microsoft SharePoint API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: microsoftSharePointOAuth2Api
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: file
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: file
      name: File
      description: ''
    - value: item
      name: Item
      description: ''
    - value: list
      name: List
      description: ''
examples:
- name: Microsoft SharePoint
  parameters:
    operation: update
    site:
      __rl: true
      value: site1
      mode: list
      cachedResultName: site1
    folder:
      __rl: true
      value: folder1
      mode: list
      cachedResultName: folder1
    file:
      __rl: true
      value: item1
      mode: list
      cachedResultName: file1.json
    fileName: file2.json
    changeFileContent: true
    fileContents: data
    requestOptions: {}
  workflow: Unnamed workflow
- name: Microsoft SharePoint
  parameters:
    operation: upload
    site:
      __rl: true
      value: site1
      mode: list
      cachedResultName: site1
    folder:
      __rl: true
      value: folder1
      mode: list
      cachedResultName: folder1
    fileName: file1.json
    fileContents: data
    requestOptions: {}
  workflow: Unnamed workflow
- name: Microsoft SharePoint
  parameters:
    site:
      __rl: true
      value: site1
      mode: list
      cachedResultName: site1
    folder:
      __rl: true
      value: folder1
      mode: list
      cachedResultName: folder1
    file:
      __rl: true
      value: item1
      mode: list
      cachedResultName: file.json
    requestOptions: {}
  workflow: Unnamed workflow
common_expressions:
- '={{ $parameter["operation"] + ": " + $parameter["resource"] }}'
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
  "$id": "https://n8n.io/schemas/nodes/microsoftSharePoint.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft SharePoint Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "file",
            "item",
            "list"
          ],
          "default": "file"
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
      "name": "microsoftSharePointOAuth2Api",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Microsoft SharePoint",
      "value": {
        "operation": "update",
        "site": {
          "__rl": true,
          "value": "site1",
          "mode": "list",
          "cachedResultName": "site1"
        },
        "folder": {
          "__rl": true,
          "value": "folder1",
          "mode": "list",
          "cachedResultName": "folder1"
        },
        "file": {
          "__rl": true,
          "value": "item1",
          "mode": "list",
          "cachedResultName": "file1.json"
        },
        "fileName": "file2.json",
        "changeFileContent": true,
        "fileContents": "data",
        "requestOptions": {}
      }
    },
    {
      "description": "Microsoft SharePoint",
      "value": {
        "operation": "upload",
        "site": {
          "__rl": true,
          "value": "site1",
          "mode": "list",
          "cachedResultName": "site1"
        },
        "folder": {
          "__rl": true,
          "value": "folder1",
          "mode": "list",
          "cachedResultName": "folder1"
        },
        "fileName": "file1.json",
        "fileContents": "data",
        "requestOptions": {}
      }
    },
    {
      "description": "Microsoft SharePoint",
      "value": {
        "site": {
          "__rl": true,
          "value": "site1",
          "mode": "list",
          "cachedResultName": "site1"
        },
        "folder": {
          "__rl": true,
          "value": "folder1",
          "mode": "list",
          "cachedResultName": "folder1"
        },
        "file": {
          "__rl": true,
          "value": "item1",
          "mode": "list",
          "cachedResultName": "file.json"
        },
        "requestOptions": {}
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
