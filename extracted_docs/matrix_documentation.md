---
title: "Node: Matrix"
slug: "node-matrix"
version: "1"
updated: "2026-01-08"
summary: "Consume Matrix API"
node_type: "regular"
group: "['output']"
---

# Node: Matrix

**Purpose.** Consume Matrix API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:matrix.png`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **matrixApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `matrixApi` | ✓ | - |

---

## Operations

### Account Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Me | `me` | Get current user's account information |

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get single event by ID |

### Media Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Upload | `upload` | Send media to a chat room |

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Send a message to a room |
| Get Many | `getAll` | Get many messages from a room |

### Room Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | New chat room with defined settings |
| Invite | `invite` | Invite a user to a room |
| Join | `join` | Join a new room |
| Kick | `kick` | Kick a user from a room |
| Leave | `leave` | Leave a room |

### Roommember Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many members |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✗ | Resource to operate on |  |

**Resource options:**

* **Account** (`account`)
* **Event** (`event`)
* **Media** (`media`)
* **Message** (`message`)
* **Room** (`room`)
* **Room Member** (`roomMember`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | me | ✗ | Get current user's account information |  |

**Operation options:**

* **Me** (`me`) - Get current user's account information

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Room ID | `roomId` | string |  | ✓ | The room related to the event | e.g. !123abc:matrix.org |  |
| Event ID | `eventId` | string |  | ✓ | The room related to the event | e.g. $1234abcd:matrix.org |  |

### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Room Name or ID | `roomId` | options |  | ✓ | Room ID to post. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |
| Media Type | `mediaType` | options | image | ✓ | General file | e.g. mxc://matrix.org/uploaded-media-uri |  |

**Media Type options:**

* **File** (`file`) - General file
* **Image** (`image`) - Image media type
* **Audio** (`audio`) - Audio media type
* **Video** (`video`) - Video media type

| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the file being uploaded | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Name | `fileName` | string |  | Name of the file being uploaded |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Room Name or ID | `roomId` | options |  | ✓ | The channel to send the message to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. !123abc:matrix.org |  |
| Text | `text` | string |  | ✗ | The text to send | e.g. Hello from n8n! |  |
| Message Type | `messageType` | options | m.text | ✗ | Perform an action (similar to /me in IRC) |  |

**Message Type options:**

* **Emote** (`m.emote`) - Perform an action (similar to /me in IRC)
* **Notice** (`m.notice`) - Send a notice
* **Text** (`m.text`) - Send a text message

| Message Format | `messageFormat` | options | plain | ✗ | Text only |  |

**Message Format options:**

* **Plain Text** (`plain`) - Text only
* **HTML** (`org.matrix.custom.html`) - HTML-formatted text

| Fallback Text | `fallbackText` | string |  | ✗ | A plain text message to display in case the HTML cannot be rendered by the Matrix client |  |
| Room Name | `roomName` | string |  | ✓ | e.g. My new room |  |
| Preset | `preset` | options | public_chat | ✓ | Open and public chat | e.g. My new room |  |

**Preset options:**

* **Private Chat** (`private_chat`)
* **Public Chat** (`public_chat`) - Open and public chat

| Room Alias | `roomAlias` | string |  | ✗ | e.g. coolest-room-around |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Room Name or ID | `roomId` | options |  | ✓ | The token to start returning events from. This token can be obtained from a prev_batch token returned for each room by the sync API. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Other Options | `otherOptions` | collection | {} | ✗ | A JSON RoomEventFilter to filter returned events with. More information can be found on this <a href="https://matrix.org/docs/spec/client_server/r0.6.0">page</a>. | e.g. Add option |  |

<details>
<summary><strong>Other Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filter | `filter` | string |  | A JSON RoomEventFilter to filter returned events with. More information can be found on this <a href="https://matrix.org/docs/spec/client_server/r0.6.0">page</a>. |

</details>

| Room Name or ID | `roomId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Filters | `filters` | collection | {} | ✗ | Filtering options | e.g. Add filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Membership | `notMembership` | options |  | Excludes members whose membership is other than selected (uses OR filter with membership) |
| Membership | `membership` | options |  | Only fetch users with selected membership status (uses OR filter with exclude membership) |

</details>


### Invite parameters (`invite`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Room Name or ID | `roomId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| User ID | `userId` | string |  | ✓ | The fully qualified user ID of the invitee | e.g. @cheeky_monkey:matrix.org |  |

### Join parameters (`join`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Room ID or Alias | `roomIdOrAlias` | string |  | ✓ |  |  |

### Kick parameters (`kick`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Room Name or ID | `roomId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| User ID | `userId` | string |  | ✓ | The fully qualified user ID | e.g. @cheeky_monkey:matrix.org |  |
| Reason | `reason` | string |  | ✗ | Reason for kick | e.g. Telling unfunny jokes |  |

### Leave parameters (`leave`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Room Name or ID | `roomId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

---

## Load Options Methods

- `getChannels`

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
node: matrix
displayName: Matrix
description: Consume Matrix API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: matrixApi
  required: true
operations:
- id: me
  name: Me
  description: Get current user's account information
- id: get
  name: Get
  description: Get single event by ID
  params:
  - id: roomId
    name: Room ID
    type: string
    default: ''
    required: true
    description: The room related to the event
    placeholder: '!123abc:matrix.org'
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - roomMember
          operation:
          - getAll
    typeInfo: &id002
      type: options
      displayName: Room Name or ID
      name: roomId
      typeOptions:
        loadOptionsMethod: getChannels
      possibleValues: []
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: The room related to the event
    placeholder: $1234abcd:matrix.org
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - event
    typeInfo:
      type: string
      displayName: Event ID
      name: eventId
- id: upload
  name: Upload
  description: Send media to a chat room
  params:
  - id: roomId
    name: Room Name or ID
    type: options
    default: ''
    required: true
    description: Room ID to post. Choose from the list, or specify an ID using an
      <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be uploaded
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - media
          operation:
          - upload
    typeInfo:
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
  - id: mediaType
    name: Media Type
    type: options
    default: image
    required: true
    description: General file
    placeholder: mxc://matrix.org/uploaded-media-uri
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - media
          operation:
          - upload
    typeInfo:
      type: options
      displayName: Media Type
      name: mediaType
      possibleValues:
      - value: file
        name: File
        description: General file
      - value: image
        name: Image
        description: Image media type
      - value: audio
        name: Audio
        description: Audio media type
      - value: video
        name: Video
        description: Video media type
- id: create
  name: Create
  description: Send a message to a room
  params:
  - id: roomId
    name: Room Name or ID
    type: options
    default: ''
    required: true
    description: The channel to send the message to. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    placeholder: '!123abc:matrix.org'
    validation: *id001
    typeInfo: *id002
  - id: text
    name: Text
    type: string
    default: ''
    required: false
    description: The text to send
    placeholder: Hello from n8n!
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - message
    typeInfo:
      type: string
      displayName: Text
      name: text
  - id: messageType
    name: Message Type
    type: options
    default: m.text
    required: false
    description: Perform an action (similar to /me in IRC)
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - message
    typeInfo:
      type: options
      displayName: Message Type
      name: messageType
      possibleValues:
      - value: m.emote
        name: Emote
        description: Perform an action (similar to /me in IRC)
      - value: m.notice
        name: Notice
        description: Send a notice
      - value: m.text
        name: Text
        description: Send a text message
  - id: messageFormat
    name: Message Format
    type: options
    default: plain
    required: false
    description: Text only
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - message
    typeInfo:
      type: options
      displayName: Message Format
      name: messageFormat
      possibleValues:
      - value: plain
        name: Plain Text
        description: Text only
      - value: org.matrix.custom.html
        name: HTML
        description: HTML-formatted text
  - id: fallbackText
    name: Fallback Text
    type: string
    default: ''
    required: false
    description: A plain text message to display in case the HTML cannot be rendered
      by the Matrix client
    validation:
      displayOptions:
        show:
          resource:
          - message
          operation:
          - create
          messageFormat:
          - org.matrix.custom.html
    typeInfo:
      type: string
      displayName: Fallback Text
      name: fallbackText
  - id: roomName
    name: Room Name
    type: string
    default: ''
    required: true
    description: ''
    placeholder: My new room
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - room
          operation:
          - create
    typeInfo:
      type: string
      displayName: Room Name
      name: roomName
  - id: preset
    name: Preset
    type: options
    default: public_chat
    required: true
    description: Open and public chat
    placeholder: My new room
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - room
          operation:
          - create
    typeInfo:
      type: options
      displayName: Preset
      name: preset
      possibleValues:
      - value: private_chat
        name: Private Chat
        description: ''
      - value: public_chat
        name: Public Chat
        description: Open and public chat
  - id: roomAlias
    name: Room Alias
    type: string
    default: ''
    required: false
    description: ''
    placeholder: coolest-room-around
    validation:
      displayOptions:
        show:
          resource:
          - room
          operation:
          - create
    typeInfo:
      type: string
      displayName: Room Alias
      name: roomAlias
- id: getAll
  name: Get Many
  description: Get many messages from a room
  params:
  - id: roomId
    name: Room Name or ID
    type: options
    default: ''
    required: true
    description: The token to start returning events from. This token can be obtained
      from a prev_batch token returned for each room by the sync API. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - getAll
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
          resource:
          - message
          operation:
          - getAll
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: roomId
    name: Room Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
- id: invite
  name: Invite
  description: Invite a user to a room
  params:
  - id: roomId
    name: Room Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: The fully qualified user ID of the invitee
    placeholder: '@cheeky_monkey:matrix.org'
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - room
          operation:
          - kick
    typeInfo: &id004
      type: string
      displayName: User ID
      name: userId
- id: join
  name: Join
  description: Join a new room
  params:
  - id: roomIdOrAlias
    name: Room ID or Alias
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - room
          operation:
          - join
    typeInfo:
      type: string
      displayName: Room ID or Alias
      name: roomIdOrAlias
- id: kick
  name: Kick
  description: Kick a user from a room
  params:
  - id: roomId
    name: Room Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: The fully qualified user ID
    placeholder: '@cheeky_monkey:matrix.org'
    validation: *id003
    typeInfo: *id004
  - id: reason
    name: Reason
    type: string
    default: ''
    required: false
    description: Reason for kick
    placeholder: Telling unfunny jokes
    validation:
      displayOptions:
        show:
          resource:
          - room
          operation:
          - kick
    typeInfo:
      type: string
      displayName: Reason
      name: reason
- id: leave
  name: Leave
  description: Leave a room
  params:
  - id: roomId
    name: Room Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: roomId
    text: '!123abc:matrix.org'
  - field: eventId
    text: $1234abcd:matrix.org
  - field: mediaType
    text: mxc://matrix.org/uploaded-media-uri
  - field: additionalFields
    text: Add Field
  - field: roomId
    text: '!123abc:matrix.org'
  - field: text
    text: Hello from n8n!
  - field: otherOptions
    text: Add option
  - field: roomName
    text: My new room
  - field: preset
    text: My new room
  - field: roomAlias
    text: coolest-room-around
  - field: userId
    text: '@cheeky_monkey:matrix.org'
  - field: userId
    text: '@cheeky_monkey:matrix.org'
  - field: reason
    text: Telling unfunny jokes
  - field: filters
    text: Add filter
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
  "$id": "https://n8n.io/schemas/nodes/matrix.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Matrix Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "me",
        "get",
        "upload",
        "create",
        "getAll",
        "invite",
        "join",
        "kick",
        "leave"
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
            "account",
            "event",
            "media",
            "message",
            "room",
            "roomMember"
          ],
          "default": "message"
        },
        "operation": {
          "description": "Get many members",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "getAll"
        },
        "roomId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "eventId": {
          "description": "The room related to the event",
          "type": "string",
          "default": "",
          "examples": [
            "$1234abcd:matrix.org"
          ]
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "mediaType": {
          "description": "General file",
          "type": "string",
          "enum": [
            "file",
            "image",
            "audio",
            "video"
          ],
          "default": "image",
          "examples": [
            "mxc://matrix.org/uploaded-media-uri"
          ]
        },
        "additionalFields": {
          "description": "Name of the file being uploaded",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "text": {
          "description": "The text to send",
          "type": "string",
          "default": "",
          "examples": [
            "Hello from n8n!"
          ]
        },
        "messageType": {
          "description": "Perform an action (similar to /me in IRC)",
          "type": "string",
          "enum": [
            "m.emote",
            "m.notice",
            "m.text"
          ],
          "default": "m.text"
        },
        "messageFormat": {
          "description": "Text only",
          "type": "string",
          "enum": [
            "plain",
            "org.matrix.custom.html"
          ],
          "default": "plain"
        },
        "fallbackText": {
          "description": "A plain text message to display in case the HTML cannot be rendered by the Matrix client",
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
        "otherOptions": {
          "description": "A JSON RoomEventFilter to filter returned events with. More information can be found on this <a href=\"https://matrix.org/docs/spec/client_server/r0.6.0\">page</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "roomName": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "My new room"
          ]
        },
        "preset": {
          "description": "Open and public chat",
          "type": "string",
          "enum": [
            "private_chat",
            "public_chat"
          ],
          "default": "public_chat",
          "examples": [
            "My new room"
          ]
        },
        "roomAlias": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "coolest-room-around"
          ]
        },
        "roomIdOrAlias": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "userId": {
          "description": "The fully qualified user ID",
          "type": "string",
          "default": "",
          "examples": [
            "@cheeky_monkey:matrix.org"
          ]
        },
        "reason": {
          "description": "Reason for kick",
          "type": "string",
          "default": "",
          "examples": [
            "Telling unfunny jokes"
          ]
        },
        "filters": {
          "description": "Filtering options",
          "type": "string",
          "default": {},
          "examples": [
            "Add filter"
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
      "name": "matrixApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
