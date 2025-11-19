---
title: "Node: Git"
slug: "node-git"
version: "1"
updated: "2025-11-13"
summary: "Control git."
node_type: "regular"
group: "['transform']"
---

# Node: Git

**Purpose.** Control git.


---

## Node Details

- **Icon:** `file:git.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **gitPassword**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `gitPassword` | ✓ | {'show': {'authentication': ['gitPassword']}} |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a file or folder to commit |
| Add Config | `addConfig` | Add configuration property |
| Clone | `clone` | Clone a repository |
| Commit | `commit` | Commit files or folders to git |
| Fetch | `fetch` | Fetch from remote repository |
| List Config | `listConfig` | Return current configuration |
| Log | `log` | Return git commit history |
| Pull | `pull` | Pull from remote repository |
| Push | `push` | Push to remote repository |
| Push Tags | `pushTags` | Push Tags to remote repository |
| Status | `status` | Return status of current repository |
| Switch Branch | `switchBranch` | Switch to a different branch |
| Tag | `tag` | Create a new tag |
| User Setup | `userSetup` | Set the user |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | log | ✗ | Add a file or folder to commit |  |

**Operation options:**

* **Add** (`add`) - Add a file or folder to commit
* **Add Config** (`addConfig`) - Add configuration property
* **Clone** (`clone`) - Clone a repository
* **Commit** (`commit`) - Commit files or folders to git
* **Fetch** (`fetch`) - Fetch from remote repository
* **List Config** (`listConfig`) - Return current configuration
* **Log** (`log`) - Return git commit history
* **Pull** (`pull`) - Pull from remote repository
* **Push** (`push`) - Push to remote repository
* **Push Tags** (`pushTags`) - Push Tags to remote repository
* **Status** (`status`) - Return status of current repository
* **Switch Branch** (`switchBranch`) - Switch to a different branch
* **Tag** (`tag`) - Create a new tag
* **User Setup** (`userSetup`) - Set the user

---

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Paths to Add | `pathsToAdd` | string |  | ✓ | Comma-separated list of paths (absolute or relative to Repository Path) of files or folders to add | e.g. README.md |  |

### Add Config parameters (`addConfig`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Key | `key` | string |  | ✓ | Name of the key to set | e.g. user.email |  |
| Value | `value` | string |  | ✓ | Value of the key to set | e.g. name@example.com |  |
| Options | `options` | collection | {} | ✗ | Append setting rather than set it in the local config | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Mode | `mode` | options | set | Append setting rather than set it in the local config |

</details>


### Clone parameters (`clone`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | none | ✗ | The way to authenticate |  |

**Authentication options:**

* **Authenticate** (`gitPassword`)
* **None** (`none`)

| New Repository Path | `repositoryPath` | string |  | ✓ | Local path to which the git repository should be cloned into | e.g. /tmp/repository |  |
| Source Repository | `sourceRepository` | string |  | ✓ | The URL or path of the repository to clone | e.g. https://github.com/n8n-io/n8n |  |

### Commit parameters (`commit`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message | `message` | string |  | ✗ | The commit message to use |  |
| Options | `options` | collection | {} | ✗ | The branch to switch to before committing. If empty or not set, will commit to current branch. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Branch | `branch` | string |  | The branch to switch to before committing. If empty or not set, will commit to current branch. |
| Paths to Add | `pathsToAdd` | string |  | Comma-separated list of paths (absolute or relative to Repository Path) of files or folders to commit. If not set will all "added" files and folders be committed. |

</details>


### Log parameters (`log`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | The path (absolute or relative to Repository Path) of file or folder to get the history of | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File | `file` | string | README.md | The path (absolute or relative to Repository Path) of file or folder to get the history of |

</details>


### Push parameters (`push`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | none | ✗ | The way to authenticate |  |

**Authentication options:**

* **Authenticate** (`gitPassword`)
* **None** (`none`)

| Options | `options` | collection | {} | ✗ | The branch to switch to before pushing. If empty or not set, will push current branch. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Branch | `branch` | string |  | The branch to switch to before pushing. If empty or not set, will push current branch. |
| Target Repository | `targetRepository` | string |  | The URL or path of the repository to push to |

</details>


### Switch Branch parameters (`switchBranch`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Branch Name | `branchName` | string |  | ✓ | The name of the branch to switch to | e.g. feature/new-feature |  |
| Options | `options` | collection | {} | ✗ | Whether to create the branch if it does not exist | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Create Branch If Not Exists | `createBranch` | boolean | True | Whether to create the branch if it does not exist |
| Start Point | `startPoint` | string |  | The commit/branch/tag to create the new branch from. If not set, creates from current HEAD. |
| Force Switch | `force` | boolean | False | Whether to force the branch switch, discarding any local changes |
| Set Upstream | `setUpstream` | boolean | False | Whether to set up tracking to a remote branch when creating a new branch |
| Remote Name | `remoteName` | string | origin | The name of the remote to track |

</details>


### Tag parameters (`tag`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | The name of the tag to create |  |

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: git
displayName: Git
description: Control git.
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: gitPassword
  required: true
operations:
- id: add
  name: Add
  description: Add a file or folder to commit
  params:
  - id: pathsToAdd
    name: Paths to Add
    type: string
    default: ''
    required: true
    description: Comma-separated list of paths (absolute or relative to Repository
      Path) of files or folders to add
    placeholder: README.md
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - add
    typeInfo:
      type: string
      displayName: Paths to Add
      name: pathsToAdd
- id: addConfig
  name: Add Config
  description: Add configuration property
  params:
  - id: key
    name: Key
    type: string
    default: ''
    required: true
    description: Name of the key to set
    placeholder: user.email
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - addConfig
    typeInfo:
      type: string
      displayName: Key
      name: key
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: Value of the key to set
    placeholder: name@example.com
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - addConfig
    typeInfo:
      type: string
      displayName: Value
      name: value
- id: clone
  name: Clone
  description: Clone a repository
  params:
  - id: authentication
    name: Authentication
    type: options
    default: none
    required: false
    description: The way to authenticate
    validation: &id001
      displayOptions:
        show:
          operation:
          - clone
          - push
    typeInfo: &id002
      type: options
      displayName: Authentication
      name: authentication
      possibleValues:
      - value: gitPassword
        name: Authenticate
        description: ''
      - value: none
        name: None
        description: ''
  - id: repositoryPath
    name: New Repository Path
    type: string
    default: ''
    required: true
    description: Local path to which the git repository should be cloned into
    placeholder: /tmp/repository
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - clone
    typeInfo:
      type: string
      displayName: New Repository Path
      name: repositoryPath
  - id: sourceRepository
    name: Source Repository
    type: string
    default: ''
    required: true
    description: The URL or path of the repository to clone
    placeholder: https://github.com/n8n-io/n8n
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - clone
    typeInfo:
      type: string
      displayName: Source Repository
      name: sourceRepository
- id: commit
  name: Commit
  description: Commit files or folders to git
  params:
  - id: message
    name: Message
    type: string
    default: ''
    required: false
    description: The commit message to use
    validation:
      displayOptions:
        show:
          operation:
          - commit
    typeInfo:
      type: string
      displayName: Message
      name: message
- id: fetch
  name: Fetch
  description: Fetch from remote repository
- id: listConfig
  name: List Config
  description: Return current configuration
- id: log
  name: Log
  description: Return git commit history
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          operation:
          - log
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - log
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
- id: pull
  name: Pull
  description: Pull from remote repository
- id: push
  name: Push
  description: Push to remote repository
  params:
  - id: authentication
    name: Authentication
    type: options
    default: none
    required: false
    description: The way to authenticate
    validation: *id001
    typeInfo: *id002
- id: pushTags
  name: Push Tags
  description: Push Tags to remote repository
- id: status
  name: Status
  description: Return status of current repository
- id: switchBranch
  name: Switch Branch
  description: Switch to a different branch
  params:
  - id: branchName
    name: Branch Name
    type: string
    default: ''
    required: true
    description: The name of the branch to switch to
    placeholder: feature/new-feature
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - switchBranch
    typeInfo:
      type: string
      displayName: Branch Name
      name: branchName
- id: tag
  name: Tag
  description: Create a new tag
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the tag to create
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - tag
    typeInfo:
      type: string
      displayName: Name
      name: name
- id: userSetup
  name: User Setup
  description: Set the user
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: repositoryPath
    text: /tmp/repository
  - field: repositoryPath
    text: /tmp/repository
  - field: pathsToAdd
    text: README.md
  - field: key
    text: user.email
  - field: value
    text: name@example.com
  - field: options
    text: Add option
  - field: sourceRepository
    text: https://github.com/n8n-io/n8n
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: branchName
    text: feature/new-feature
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
  "$id": "https://n8n.io/schemas/nodes/git.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Git Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "add",
        "addConfig",
        "clone",
        "commit",
        "fetch",
        "listConfig",
        "log",
        "pull",
        "push",
        "pushTags",
        "status",
        "switchBranch",
        "tag",
        "userSetup"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "The way to authenticate",
          "type": "string",
          "enum": [
            "gitPassword",
            "none"
          ],
          "default": "none"
        },
        "operation": {
          "description": "Add a file or folder to commit",
          "type": "string",
          "enum": [
            "add",
            "addConfig",
            "clone",
            "commit",
            "fetch",
            "listConfig",
            "log",
            "pull",
            "push",
            "pushTags",
            "status",
            "switchBranch",
            "tag",
            "userSetup"
          ],
          "default": "log"
        },
        "repositoryPath": {
          "description": "Local path to which the git repository should be cloned into",
          "type": "string",
          "default": "",
          "examples": [
            "/tmp/repository"
          ]
        },
        "name": {
          "description": "The name of the tag to create",
          "type": "string",
          "default": ""
        },
        "pathsToAdd": {
          "description": "Comma-separated list of paths (absolute or relative to Repository Path) of files or folders to add",
          "type": "string",
          "default": "",
          "examples": [
            "README.md"
          ]
        },
        "key": {
          "description": "Name of the key to set",
          "type": "string",
          "default": "",
          "examples": [
            "user.email"
          ]
        },
        "value": {
          "description": "Value of the key to set",
          "type": "string",
          "default": "",
          "examples": [
            "name@example.com"
          ]
        },
        "options": {
          "description": "Whether to create the branch if it does not exist",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "sourceRepository": {
          "description": "The URL or path of the repository to clone",
          "type": "string",
          "default": "",
          "examples": [
            "https://github.com/n8n-io/n8n"
          ]
        },
        "message": {
          "description": "The commit message to use",
          "type": "string",
          "default": ""
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
        },
        "branchName": {
          "description": "The name of the branch to switch to",
          "type": "string",
          "default": "",
          "examples": [
            "feature/new-feature"
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
      "name": "gitPassword",
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
