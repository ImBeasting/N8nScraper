---
title: "Node: Google Chat"
slug: "node-googlechat"
version: "1"
updated: "2025-11-13"
summary: "Consume Google Chat API"
node_type: "regular"
group: "['input']"
---

# Node: Google Chat

**Purpose.** Consume Google Chat API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:googleChat.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleApi**: N/A
- **googleChatOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **jsonNotice** when resource=['message'], operation=['create'], jsonParameters=[True]: See <a href="https://developers.google.com/chat/reference/rest/v1/spaces.messages#Message" target="_blank">Google Chat Guide</a> To Creating Messages
- **jsonNotice** when resource=['message'], operation=['update'], jsonParameters=[True]: See <a href="https://developers.google.com/chat/reference/rest/v1/spaces.messages#Message" target="_blank">Google Chat Guide</a> To Creating Messages

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleApi` | ✓ | {'show': {'authentication': ['serviceAccount']}} |
| `googleChatOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Space Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a space |
| Get Many | `getAll` | Get many spaces the caller is a member of |

### Member Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a membership |
| Get Many | `getAll` | Get many memberships in a space |

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a message |
| Delete | `delete` | Delete a message |
| Get | `get` | Get a message |
| Send and Wait for Response | `` | Send a message and wait for response |
| Update | `update` | Update a message |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✓ | Resource to operate on |  |

**Resource options:**

* **Attachment** (`attachment`)
* **Incoming Webhook** (`incomingWebhook`)
* **Media** (`media`)
* **Member** (`member`)
* **Message** (`message`)
* **Space** (`space`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Get a space |  |

**Operation options:**

* **Get** (`get`) - Get a space
* **Get Many** (`getAll`) - Get many spaces the caller is a member of

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Space ID | `spaceId` | string |  | ✓ | Resource name of the space, in the form "spaces/*" |  |
| Member ID | `memberId` | string |  | ✓ | Member to be retrieved in the form "spaces/*/members/*" |  |
| Message ID | `messageId` | string |  | ✓ | Resource name of the message to be retrieved, in the form "spaces//messages/" |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Space Name or ID | `spaceId` | options | [] | ✓ | The name of the space for which to retrieve members, in the form "spaces/*". Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ | Whether to pass the message object as JSON |  |
| Message | `messageUi` | collection | {} | ✓ | Rich, formatted and interactive cards that can be used to display UI elements such as: formatted texts, buttons, clickable images | e.g. Add Message |  |

<details>
<summary><strong>Message sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Text | `text` | string |  |  |
| Cards | `cards` | fixedCollection |  | Rich, formatted and interactive cards that can be used to display UI elements such as: formatted texts, buttons, clickable images |

</details>

| Message (JSON) | `messageJson` | json |  | ✓ | Message input as JSON Object or JSON String |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Thread identifier which groups messages into a single thread. Has no effect if thread field, corresponding to an existing thread, is set in message. Example: spaces/AAAAMpdlehY/threads/MZ8fXhZXGkk. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Thread Key | `threadKey` | string |  | Thread identifier which groups messages into a single thread. Has no effect if thread field, corresponding to an existing thread, is set in message. Example: spaces/AAAAMpdlehY/threads/MZ8fXhZXGkk. |
| Request ID | `requestId` | string |  | A unique request ID for this message. If a message has already been created in the space with this request ID, the subsequent request will return the existing message and no new message will be created. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | Resource name of the message to be deleted, in the form "spaces//messages/" |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | Resource name of the message to be updated, in the form "spaces//messages/" |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ | Whether to pass the update fields object as JSON |  |
| Update Fields | `updateFieldsUi` | collection | {} | ✓ | Rich, formatted and interactive cards that can be used to display UI elements such as: formatted texts, buttons, clickable images | e.g. Add option |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Text | `text` | string |  |  |
| Cards | `cards` | fixedCollection |  | Rich, formatted and interactive cards that can be used to display UI elements such as: formatted texts, buttons, clickable images |

</details>

| Update Fields (JSON) | `updateFieldsJson` | json |  | ✓ | Message input as JSON Object or JSON String |  |

---

## Load Options Methods

- `getSpaces`
- `for`
- `name`
- `value`

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
* Categories: Communication, HITL
* Aliases: human, form, wait, hitl, approval

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleChat
displayName: Google Chat
description: Consume Google Chat API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: googleApi
  required: true
- name: googleChatOAuth2Api
  required: true
operations:
- id: get
  name: Get
  description: Get a space
  params:
  - id: spaceId
    name: Space ID
    type: string
    default: ''
    required: true
    description: Resource name of the space, in the form "spaces/*"
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - getAll
    typeInfo: &id002
      type: options
      displayName: Space Name or ID
      name: spaceId
      typeOptions:
        loadOptionsMethod: getSpaces
      possibleValues: []
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: Member to be retrieved in the form "spaces/*/members/*"
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - get
    typeInfo:
      type: string
      displayName: Member ID
      name: memberId
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: Resource name of the message to be retrieved, in the form "spaces//messages/"
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - update
    typeInfo: &id004
      type: string
      displayName: Message ID
      name: messageId
- id: getAll
  name: Get Many
  description: Get many spaces the caller is a member of
  params:
  - id: spaceId
    name: Space Name or ID
    type: options
    default: []
    required: true
    description: The name of the space for which to retrieve members, in the form
      "spaces/*". Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
- id: create
  name: Create
  description: Create a message
  params:
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: Whether to pass the message object as JSON
    validation: &id005
      displayOptions:
        show:
          resource:
          - message
          operation:
          - update
    typeInfo: &id006
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: messageJson
    name: Message (JSON)
    type: json
    default: ''
    required: true
    description: Message input as JSON Object or JSON String
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - create
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Message (JSON)
      name: messageJson
      typeOptions:
        alwaysOpenEditWindow: true
- id: delete
  name: Delete
  description: Delete a message
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: Resource name of the message to be deleted, in the form "spaces//messages/"
    validation: *id003
    typeInfo: *id004
- id: ''
  name: Send and Wait for Response
  description: Send a message and wait for response
- id: update
  name: Update
  description: Update a message
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: Resource name of the message to be updated, in the form "spaces//messages/"
    validation: *id003
    typeInfo: *id004
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: Whether to pass the update fields object as JSON
    validation: *id005
    typeInfo: *id006
  - id: updateFieldsJson
    name: Update Fields (JSON)
    type: json
    default: ''
    required: true
    description: Message input as JSON Object or JSON String
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - update
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Update Fields (JSON)
      name: updateFieldsJson
      typeOptions:
        alwaysOpenEditWindow: true
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices:
  - name: jsonNotice
    text: See <a href="https://developers.google.com/chat/reference/rest/v1/spaces.messages#Message"
      target="_blank">Google Chat Guide</a> To Creating Messages
    conditions:
      show:
        resource:
        - message
        operation:
        - create
        jsonParameters:
        - true
  - name: jsonNotice
    text: See <a href="https://developers.google.com/chat/reference/rest/v1/spaces.messages#Message"
      target="_blank">Google Chat Guide</a> To Creating Messages
    conditions:
      show:
        resource:
        - message
        operation:
        - update
        jsonParameters:
        - true
  tooltips: []
  placeholders:
  - field: messageUi
    text: Add Message
  - field: additionalFields
    text: Add Field
  - field: updateFieldsUi
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
  "$id": "https://n8n.io/schemas/nodes/googleChat.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Chat Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll",
        "create",
        "delete",
        "",
        "update"
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
            "oAuth2",
            "serviceAccount"
          ],
          "default": "serviceAccount"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "attachment",
            "incomingWebhook",
            "media",
            "member",
            "message",
            "space"
          ],
          "default": "message"
        },
        "operation": {
          "description": "Create a message",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "Send and Wait for Response",
            "update"
          ],
          "default": "create"
        },
        "spaceId": {
          "description": "The name of the space for which to retrieve members, in the form \"spaces/*\". Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "memberId": {
          "description": "Member to be retrieved in the form \"spaces/*/members/*\"",
          "type": "string",
          "default": ""
        },
        "jsonParameters": {
          "description": "Whether to pass the update fields object as JSON",
          "type": "boolean",
          "default": false
        },
        "messageUi": {
          "description": "Rich, formatted and interactive cards that can be used to display UI elements such as: formatted texts, buttons, clickable images",
          "type": "string",
          "default": {},
          "examples": [
            "Add Message"
          ]
        },
        "messageJson": {
          "description": "Message input as JSON Object or JSON String",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Thread identifier which groups messages into a single thread. Has no effect if thread field, corresponding to an existing thread, is set in message. Example: spaces/AAAAMpdlehY/threads/MZ8fXhZXGkk.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "messageId": {
          "description": "Resource name of the message to be updated, in the form \"spaces//messages/\"",
          "type": "string",
          "default": ""
        },
        "updateFieldsUi": {
          "description": "Rich, formatted and interactive cards that can be used to display UI elements such as: formatted texts, buttons, clickable images",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "updateFieldsJson": {
          "description": "Message input as JSON Object or JSON String",
          "type": "string",
          "default": ""
        },
        "default": {
          "description": "",
          "type": "string"
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
      "name": "googleApi",
      "required": true
    },
    {
      "name": "googleChatOAuth2Api",
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
