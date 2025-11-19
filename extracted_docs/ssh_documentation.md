---
title: "Node: SSH"
slug: "node-ssh"
version: "1"
updated: "2025-11-13"
summary: "Execute commands via SSH"
node_type: "regular"
group: "['input']"
---

# Node: SSH

**Purpose.** Execute commands via SSH
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `fa:terminal`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **sshPassword**: N/A
- **sshPrivateKey**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `sshPassword` | ✓ | {'show': {'authentication': ['password']}} |
| `sshPrivateKey` | ✓ | {'show': {'authentication': ['privateKey']}} |

---

## Operations

### Command Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Execute | `execute` | Execute a command |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Download | `download` | Download a file |
| Upload | `upload` | Upload a file |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | command | ✗ | Resource to operate on |  |

**Resource options:**

* **Command** (`command`)
* **File** (`file`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | execute | ✗ | Execute a command |  |

**Operation options:**

* **Execute** (`execute`) - Execute a command

---

### Execute parameters (`execute`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Command | `command` | string |  | ✗ | The command to be executed on a remote device |  |
| Working Directory | `cwd` | string | / | ✓ |  |  |

### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Path | `path` | string |  | ✓ | The file path of the file to download. Has to contain the full path including file name. | e.g. /home/user/invoice.txt |  |
| File Property | `binaryPropertyName` | string | data | ✓ | Object property name which holds binary data |  |
| Options | `options` | collection | {} | ✗ | Overrides the binary data file name | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Name | `fileName` | string |  | Overrides the binary data file name |

</details>


### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |
| Target Directory | `path` | string |  | ✓ | The directory to upload the file to. The name of the file does not need to be specified, it's taken from the binary data file name. To override this behavior, set the parameter "File Name" under options. | e.g. /home/user |  |
| Options | `options` | collection | {} | ✗ | Overrides the binary data file name | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Name | `fileName` | string |  | Overrides the binary data file name |

</details>


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
* Categories: Core Nodes, Development
* Aliases: remote

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: ssh
displayName: SSH
description: Execute commands via SSH
version: '1'
nodeType: regular
group:
- input
credentials:
- name: sshPassword
  required: true
- name: sshPrivateKey
  required: true
operations:
- id: execute
  name: Execute
  description: Execute a command
  params:
  - id: command
    name: Command
    type: string
    default: ''
    required: false
    description: The command to be executed on a remote device
    validation:
      displayOptions:
        show:
          resource:
          - command
          operation:
          - execute
    typeInfo:
      type: string
      displayName: Command
      name: command
  - id: cwd
    name: Working Directory
    type: string
    default: /
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - command
          operation:
          - execute
    typeInfo:
      type: string
      displayName: Working Directory
      name: cwd
- id: download
  name: Download
  description: Download a file
  params:
  - id: path
    name: Path
    type: string
    default: ''
    required: true
    description: The file path of the file to download. Has to contain the full path
      including file name.
    placeholder: /home/user/invoice.txt
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - download
    typeInfo: &id004
      type: string
      displayName: Path
      name: path
  - id: binaryPropertyName
    name: File Property
    type: string
    default: data
    required: true
    description: Object property name which holds binary data
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - download
    typeInfo: &id002
      type: string
      displayName: File Property
      name: binaryPropertyName
- id: upload
  name: Upload
  description: Upload a file
  params:
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be uploaded
    validation: *id001
    typeInfo: *id002
  - id: path
    name: Target Directory
    type: string
    default: ''
    required: true
    description: The directory to upload the file to. The name of the file does not
      need to be specified, it's taken from the binary data file name. To override
      this behavior, set the parameter "File Name" under options.
    placeholder: /home/user
    validation: *id003
    typeInfo: *id004
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: path
    text: /home/user
  - field: path
    text: /home/user/invoice.txt
  - field: options
    text: Add option
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be uploaded
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
  "$id": "https://n8n.io/schemas/nodes/ssh.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SSH Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "execute",
        "download",
        "upload"
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
            "password",
            "privateKey"
          ],
          "default": "password"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "command",
            "file"
          ],
          "default": "command"
        },
        "operation": {
          "description": "Download a file",
          "type": "string",
          "enum": [
            "download",
            "upload"
          ],
          "default": "upload"
        },
        "command": {
          "description": "The command to be executed on a remote device",
          "type": "string",
          "default": ""
        },
        "cwd": {
          "description": "",
          "type": "string",
          "default": "/"
        },
        "binaryPropertyName": {
          "description": "Object property name which holds binary data",
          "type": "string",
          "default": "data"
        },
        "path": {
          "description": "The file path of the file to download. Has to contain the full path including file name.",
          "type": "string",
          "default": "",
          "examples": [
            "/home/user/invoice.txt"
          ]
        },
        "options": {
          "description": "Overrides the binary data file name",
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
  "credentials": [
    {
      "name": "sshPassword",
      "required": true
    },
    {
      "name": "sshPrivateKey",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
