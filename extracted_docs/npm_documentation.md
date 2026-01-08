---
title: "Node: Npm"
slug: "node-npm"
version: "1"
updated: "2026-01-08"
summary: "Consume NPM registry API"
node_type: "regular"
group: "['input']"
---

# Node: Npm

**Purpose.** Consume NPM registry API
**Subtitle.** ={{ $parameter["operation"] + ": " + $parameter["resource"] }}


---

## Node Details

- **Icon:** `file:npm.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **npmApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `npmApi` | Optional | - |

---

## Operations

### Package Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Metadata | `getMetadata` | Returns all the metadata for a package at a specific version |

### Disttag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get All | `getMany` | Returns all the dist-tags for a package |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | package | ✗ | Resource to operate on |  |

**Resource options:**

* **Package** (`package`)
* **Distribution Tag** (`distTag`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getMetadata | ✗ | Returns all the metadata for a package at a specific version |  |

**Operation options:**

* **Get Metadata** (`getMetadata`) - Returns all the metadata for a package at a specific version

---

### Get Metadata parameters (`getMetadata`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Package Name | `packageName` | string |  | ✓ |  |  |
| Package Version | `packageVersion` | string | latest | ✓ |  |  |

### Get All parameters (`getMany`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Package Name | `packageName` | string |  | ✓ |  |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $credentials.registryUrl }}`
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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: npm
displayName: Npm
description: Consume NPM registry API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: npmApi
  required: false
operations:
- id: getMetadata
  name: Get Metadata
  description: Returns all the metadata for a package at a specific version
  params:
  - id: packageName
    name: Package Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - distTag
          operation:
          - getMany
          - update
    typeInfo: &id002
      type: string
      displayName: Package Name
      name: packageName
  - id: packageVersion
    name: Package Version
    type: string
    default: latest
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - distTag
          operation:
          - update
    typeInfo:
      type: string
      displayName: Package Version
      name: packageVersion
- id: getMany
  name: Get All
  description: Returns all the dist-tags for a package
  params:
  - id: packageName
    name: Package Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
common_expressions:
- ={{ $credentials.registryUrl }}
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
  "$id": "https://n8n.io/schemas/nodes/npm.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Npm Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "getMetadata",
        "getMany"
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
            "package",
            "distTag"
          ],
          "default": "package"
        },
        "operation": {
          "description": "Returns all the dist-tags for a package",
          "type": "string",
          "enum": [
            "getMany"
          ],
          "default": "getMany"
        },
        "packageName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "packageVersion": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "query": {
          "description": "The query text used to search for packages",
          "type": "string",
          "default": ""
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 10
        },
        "offset": {
          "description": "Offset to return results from",
          "type": "number",
          "default": 0
        },
        "distTagName": {
          "description": "",
          "type": "string",
          "default": "latest"
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
      "name": "npmApi",
      "required": false
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
