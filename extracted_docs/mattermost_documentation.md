---
title: "Node: Mattermost"
slug: "node-mattermost"
version: "1.0"
updated: "2026-01-08"
summary: "Sends data to Mattermost"
node_type: "regular"
group: "['output']"
---

# Node: Mattermost

**Purpose.** Sends data to Mattermost
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:mattermost.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Operations

### Channel Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add User | `addUser` | Add a user to a channel |
| Create | `create` | Create a new channel |
| Delete | `delete` | Soft delete a channel |
| Member | `members` | Get a page of members for a channel |
| Restore | `restore` | Restores a soft deleted channel |
| Search | `search` | Search for a channel |
| Statistics | `statistics` | Get statistics for a channel |

### Reaction Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Add a reaction to a post |
| Delete | `delete` | Remove a reaction from a post |
| Get Many | `getAll` | Get many reactions to one or more posts |

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Soft delete a post, by marking the post as deleted in the database |
| Post | `post` | Post a message into a channel |
| Post Ephemeral | `postEphemeral` | Post an ephemeral message into a channel |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new user |
| Deactive | `deactive` | Deactivates the user and revokes all its sessions by archiving its user object |
| Get By Email | `getByEmail` | Get a user by email |
| Get By ID | `getById` | Get a user by ID |
| Get Many | `getAll` | Retrieve many users |
| Invite | `invite` | Invite user to team |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✗ | Resource to operate on |  |

**Resource options:**

* **Channel** (`channel`)
* **Message** (`message`)
* **Reaction** (`reaction`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Add a user to a channel |  |

**Operation options:**

* **Add User** (`addUser`) - Add a user to a channel
* **Create** (`create`) - Create a new channel
* **Delete** (`delete`) - Soft delete a channel
* **Member** (`members`) - Get a page of members for a channel
* **Restore** (`restore`) - Restores a soft deleted channel
* **Search** (`search`) - Search for a channel
* **Statistics** (`statistics`) - Get statistics for a channel

---

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
* Categories: Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: mattermost
displayName: Mattermost
description: Sends data to Mattermost
version: '1.0'
nodeType: regular
group:
- output
operations:
- id: addUser
  name: Add User
  description: Add a user to a channel
- id: create
  name: Create
  description: Create a new channel
- id: delete
  name: Delete
  description: Soft delete a channel
- id: members
  name: Member
  description: Get a page of members for a channel
- id: restore
  name: Restore
  description: Restores a soft deleted channel
- id: search
  name: Search
  description: Search for a channel
- id: statistics
  name: Statistics
  description: Get statistics for a channel
- id: getAll
  name: Get Many
  description: Get many reactions to one or more posts
- id: post
  name: Post
  description: Post a message into a channel
- id: postEphemeral
  name: Post Ephemeral
  description: Post an ephemeral message into a channel
- id: deactive
  name: Deactive
  description: Deactivates the user and revokes all its sessions by archiving its
    user object
- id: getByEmail
  name: Get By Email
  description: Get a user by email
- id: getById
  name: Get By ID
  description: Get a user by ID
- id: invite
  name: Invite
  description: Invite user to team
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
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
  "$id": "https://n8n.io/schemas/nodes/mattermost.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Mattermost Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "addUser",
        "create",
        "delete",
        "members",
        "restore",
        "search",
        "statistics",
        "getAll",
        "post",
        "postEphemeral",
        "deactive",
        "getByEmail",
        "getById",
        "invite"
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
            "channel",
            "message",
            "reaction",
            "user"
          ],
          "default": "message"
        },
        "operation": {
          "description": "Create a new user",
          "type": "string",
          "enum": [
            "create",
            "deactive",
            "getByEmail",
            "getById",
            "getAll",
            "invite"
          ],
          "default": ""
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
    "version": "1.0"
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1.0 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
