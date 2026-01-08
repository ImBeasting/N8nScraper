---
title: "Node: Zulip"
slug: "node-zulip"
version: "1"
updated: "2026-01-08"
summary: "Consume Zulip API"
node_type: "regular"
group: "['output']"
---

# Node: Zulip

**Purpose.** Consume Zulip API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:zulip.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **zulipApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `zulipApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a message |
| Get | `get` | Get a message |
| Send Private | `sendPrivate` | Send a private message |
| Send to Stream | `sendStream` | Send a message to stream |
| Update | `update` | Update a message |
| Upload a File | `updateFile` | Upload a file |

### Stream Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a stream |
| Delete | `delete` | Delete a stream |
| Get Many | `getAll` | Get many streams |
| Get Subscribed | `getSubscribed` | Get subscribed streams |
| Update | `update` | Update a stream |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a user |
| Deactivate | `deactivate` | Deactivate a user |
| Get | `get` | Get a user |
| Get Many | `getAll` | Get many users |
| Update | `update` | Update a user |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✗ | Resource to operate on |  |

**Resource options:**

* **Message** (`message`)
* **Stream** (`stream`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | sendPrivate | ✗ | Delete a message |  |

**Operation options:**

* **Delete** (`delete`) - Delete a message
* **Get** (`get`) - Get a message
* **Send Private** (`sendPrivate`) - Send a private message
* **Send to Stream** (`sendStream`) - Send a message to stream
* **Update** (`update`) - Update a message
* **Upload a File** (`updateFile`) - Upload a file

---

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | Unique identifier for the message |  |
| Stream ID | `streamId` | string |  | ✓ | ID of stream to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | Unique identifier for the message |  |
| User ID | `userId` | string |  | ✓ | The ID of user to get |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether the client supports computing gravatars URLs. If enabled, avatar_url will be included in the response only if there is a Zulip avatar, and will be null for users who are using gravatar as their avatar. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Client Gravatar | `clientGravatar` | boolean | False | Whether the client supports computing gravatars URLs. If enabled, avatar_url will be included in the response only if there is a Zulip avatar, and will be null for users who are using gravatar as their avatar. |
| Custom Profile Fields | `includeCustomProfileFields` | boolean | False | Whether the client wants custom profile field data to be included in the response |

</details>


### Send Private parameters (`sendPrivate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| To | `to` | multiOptions | [] | ✓ | The destination stream, or a comma-separated list containing the usernames (emails) of the recipients. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Content | `content` | string |  | ✓ | The content of the message |  |

### Send to Stream parameters (`sendStream`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Stream Name or ID | `stream` | options |  | ✓ | The destination stream, or a comma-separated list containing the usernames (emails) of the recipients. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Topic Name or ID | `topic` | options |  | ✓ | The topic of the message. Only required if type is stream, ignored otherwise. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Content | `content` | string |  | ✓ | The content of the message |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | Unique identifier for the message |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The content of the message | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content | `content` | string |  | The content of the message |
| Propagate Mode | `propagateMode` | options | changeOne | Which message(s) should be edited: just the one indicated in message_id, messages in the same topic that had been sent after this one, or all of them |
| Topic | `topic` | string |  | The topic of the message. Only required for stream messages. |

</details>

| Stream ID | `streamId` | string |  | ✓ | ID of stream to update |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | JSON format parameters for stream creation |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether the stream is limited to announcements | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Announcement Only | `isAnnouncementOnly` | boolean | False | Whether the stream is limited to announcements |
| Description | `description` | string |  | The new description for the stream |
| Is Private | `isPrivate` | boolean | False | Whether the stream is a private stream |
| History Public to Subscribers | `historyPublicToSubscribers` | boolean | False | Whether the streams message history should be available to newly subscribed members, or users can only access messages they actually received while subscribed to the stream |
| New Name | `newName` | string |  | The new name for the stream |
| Stream Post Policy | `streamPostPolicy` | options |  | Policy for which users can post messages to the stream |

</details>

| User ID | `userId` | string |  | ✓ | The ID of user to update |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | The users full name | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Full Name | `fullName` | string |  | The users full name |
| Is Admin | `isAdmin` | boolean | False | Whether the target user is an administrator |
| Is Guest | `isGuest` | boolean | False | Whether the target user is a guest |
| Profile Data | `profileData` | fixedCollection | {} | A dictionary containing the to be updated custom profile field data for the user |
| Role | `role` | options |  | Role for the user |

</details>


### Upload a File parameters (`updateFile`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Put Output File in Field | `dataBinaryProperty` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | JSON format parameters for stream creation |  |
| Subscriptions | `subscriptions` | fixedCollection | {} | ✓ | A list of dictionaries containing the the key name and value specifying the name of the stream to subscribe. If the stream does not exist a new stream is created. |  |

<details>
<summary><strong>Subscriptions sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Subscription Properties | `properties` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✓ | If announce is True and one of the streams specified in subscriptions has to be created (i.e. doesnt exist to begin with), an announcement will be made notifying that a new stream was created. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Announce | `announce` | boolean | False | If announce is True and one of the streams specified in subscriptions has to be created (i.e. doesnt exist to begin with), an announcement will be made notifying that a new stream was created. |
| Authorization Errors Fatal | `authorizationErrorsFatal` | boolean | False | Whether authorization errors (such as when the requesting user is not authorized to access a private stream) should be considered fatal or not. When True, an authorization error is reported as such. When set to False, the returned JSON payload indicates that there was an authorization error, but the response is still considered a successful one. |
| History Public to Subscribers | `historyPublicToSubscribers` | boolean | False | Whether the streams message history should be available to newly subscribed members, or users can only access messages they actually received while subscribed to the stream |
| Invite Only | `inviteOnly` | boolean | False | Whether the streams specified in subscriptions are invite-only or not |
| Principals | `principals` | fixedCollection | {} | A list of email addresses of the users that will be subscribed/unsubscribed to the streams specified in the subscriptions argument. If not provided, then the requesting user/bot is subscribed. |
| Stream Post Policy | `streamPostPolicy` | options |  | Policy for which users can post messages to the stream |

</details>

| Email | `email` | string |  | ✓ | The email address of the new user | e.g. name@email.com | email |
| Full Name | `fullName` | string |  | ✓ | The full name of the new user |  |
| Password | `password` | string |  | ✓ | The password of the new user |  |
| Short Name | `shortName` | string |  | ✓ | The short name of the new user. Not user-visible. |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include all active streams. The user must have administrative privileges to use this parameter. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include All Active | `includeAllActive` | boolean | True | Whether to include all active streams. The user must have administrative privileges to use this parameter. |
| Include Default | `includeDefault` | boolean | True | Whether to include all default streams for the users realm |
| Include Owner Subscribed | `includeOwnersubscribed` | boolean | True | Whether the user is a bot, include all streams that the bots owner is subscribed to |
| Include Public | `includePublic` | boolean | True | Whether to include all public streams |
| Include Subscribed | `includeSubscribed` | boolean | True | Whether to include all streams that the user is subscribed to |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether the client supports computing gravatars URLs. If enabled, avatar_url will be included in the response only if there is a Zulip avatar, and will be null for users who are using gravatar as their avatar. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Client Gravatar | `clientGravatar` | boolean | False | Whether the client supports computing gravatars URLs. If enabled, avatar_url will be included in the response only if there is a Zulip avatar, and will be null for users who are using gravatar as their avatar. |
| Custom Profile Fields | `includeCustomProfileFields` | boolean | False | Whether the client wants custom profile field data to be included in the response |

</details>


### Get Subscribed parameters (`getSubscribed`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether each returned stream object should include a subscribers field containing a list of the user IDs of its subscribers | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Subscribers | `includeSubscribers` | boolean | True | Whether each returned stream object should include a subscribers field containing a list of the user IDs of its subscribers |

</details>


### Deactivate parameters (`deactivate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✓ | The ID of user to deactivate |  |

---

## Load Options Methods

- `getStreams`

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
node: zulip
displayName: Zulip
description: Consume Zulip API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: zulipApi
  required: true
operations:
- id: delete
  name: Delete
  description: Delete a message
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the message
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - delete
    typeInfo: &id002
      type: string
      displayName: Message ID
      name: messageId
  - id: streamId
    name: Stream ID
    type: string
    default: ''
    required: true
    description: ID of stream to delete
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - stream
          operation:
          - delete
    typeInfo: &id006
      type: string
      displayName: Stream ID
      name: streamId
- id: get
  name: Get
  description: Get a message
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the message
    validation: *id001
    typeInfo: *id002
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: The ID of user to get
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - deactivate
    typeInfo: &id008
      type: string
      displayName: User ID
      name: userId
- id: sendPrivate
  name: Send Private
  description: Send a private message
  params:
  - id: to
    name: To
    type: multiOptions
    default: []
    required: true
    description: The destination stream, or a comma-separated list containing the
      usernames (emails) of the recipients. Choose from the list, or specify IDs using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - sendPrivate
    typeInfo:
      type: multiOptions
      displayName: To
      name: to
      typeOptions:
        loadOptionsMethod: getUsers
      possibleValues: []
  - id: content
    name: Content
    type: string
    default: ''
    required: true
    description: The content of the message
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - sendStream
    typeInfo: &id004
      type: string
      displayName: Content
      name: content
- id: sendStream
  name: Send to Stream
  description: Send a message to stream
  params:
  - id: stream
    name: Stream Name or ID
    type: options
    default: ''
    required: true
    description: The destination stream, or a comma-separated list containing the
      usernames (emails) of the recipients. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - sendStream
    typeInfo:
      type: options
      displayName: Stream Name or ID
      name: stream
      typeOptions:
        loadOptionsMethod: getStreams
      possibleValues: []
  - id: topic
    name: Topic Name or ID
    type: options
    default: ''
    required: true
    description: The topic of the message. Only required if type is stream, ignored
      otherwise. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - sendStream
    typeInfo:
      type: options
      displayName: Topic Name or ID
      name: topic
      typeOptions:
        loadOptionsMethod: getTopics
      possibleValues: []
  - id: content
    name: Content
    type: string
    default: ''
    required: true
    description: The content of the message
    validation: *id003
    typeInfo: *id004
- id: update
  name: Update
  description: Update a message
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the message
    validation: *id001
    typeInfo: *id002
  - id: streamId
    name: Stream ID
    type: string
    default: ''
    required: true
    description: ID of stream to update
    validation: *id005
    typeInfo: *id006
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id009
      displayOptions:
        show:
          resource:
          - stream
          operation:
          - update
    typeInfo: &id010
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: JSON format parameters for stream creation
    validation: &id011
      displayOptions:
        show:
          resource:
          - stream
          operation:
          - update
          jsonParameters:
          - true
    typeInfo: &id012
      type: json
      displayName: Additional Fields
      name: additionalFieldsJson
      typeOptions:
        alwaysOpenEditWindow: true
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: The ID of user to update
    validation: *id007
    typeInfo: *id008
- id: updateFile
  name: Upload a File
  description: ''
  params:
  - id: dataBinaryProperty
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - updateFile
    typeInfo:
      type: string
      displayName: Put Output File in Field
      name: dataBinaryProperty
- id: create
  name: Create
  description: Create a stream
  params:
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: JSON format parameters for stream creation
    validation: *id011
    typeInfo: *id012
  - id: subscriptions
    name: Subscriptions
    type: fixedCollection
    default: {}
    required: true
    description: A list of dictionaries containing the the key name and value specifying
      the name of the stream to subscribe. If the stream does not exist a new stream
      is created.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - stream
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: fixedCollection
      displayName: Subscriptions
      name: subscriptions
      typeOptions:
        multipleValues: true
      subProperties:
      - name: properties
        displayName: Subscription Properties
        values:
        - displayName: Name
          name: name
          type: string
          description: Name of Subscription
          default: ''
          required: true
        - displayName: Description
          name: description
          type: string
          description: Description of Subscription
          default: ''
          required: true
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email address of the new user
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: fullName
    name: Full Name
    type: string
    default: ''
    required: true
    description: The full name of the new user
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Full Name
      name: fullName
  - id: password
    name: Password
    type: string
    default: ''
    required: true
    description: The password of the new user
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Password
      name: password
      typeOptions:
        password: true
  - id: shortName
    name: Short Name
    type: string
    default: ''
    required: true
    description: The short name of the new user. Not user-visible.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Short Name
      name: shortName
- id: getAll
  name: Get Many
  description: Get many streams
  params: []
- id: getSubscribed
  name: Get Subscribed
  description: Get subscribed streams
  params: []
- id: deactivate
  name: Deactivate
  description: Deactivate a user
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: The ID of user to deactivate
    validation: *id007
    typeInfo: *id008
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  hints:
  - field: dataBinaryProperty
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/zulip.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Zulip Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "delete",
        "get",
        "sendPrivate",
        "sendStream",
        "update",
        "updateFile",
        "create",
        "getAll",
        "getSubscribed",
        "deactivate"
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
            "message",
            "stream",
            "user"
          ],
          "default": "message"
        },
        "operation": {
          "description": "Create a user",
          "type": "string",
          "enum": [
            "create",
            "deactivate",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "to": {
          "description": "The destination stream, or a comma-separated list containing the usernames (emails) of the recipients. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "content": {
          "description": "The content of the message",
          "type": "string",
          "default": ""
        },
        "stream": {
          "description": "The destination stream, or a comma-separated list containing the usernames (emails) of the recipients. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "topic": {
          "description": "The topic of the message. Only required if type is stream, ignored otherwise. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "messageId": {
          "description": "Unique identifier for the message",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "The content of the message",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "dataBinaryProperty": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "additionalFieldsJson": {
          "description": "JSON format parameters for stream creation",
          "type": "string",
          "default": ""
        },
        "subscriptions": {
          "description": "A list of dictionaries containing the the key name and value specifying the name of the stream to subscribe. If the stream does not exist a new stream is created.",
          "type": "string",
          "default": {}
        },
        "additionalFields": {
          "description": "The users full name",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "streamId": {
          "description": "ID of stream to delete",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "The email address of the new user",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "fullName": {
          "description": "The full name of the new user",
          "type": "string",
          "default": ""
        },
        "password": {
          "description": "The password of the new user",
          "type": "string",
          "default": ""
        },
        "shortName": {
          "description": "The short name of the new user. Not user-visible.",
          "type": "string",
          "default": ""
        },
        "userId": {
          "description": "The ID of user to deactivate",
          "type": "string",
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
    "version": "1"
  },
  "credentials": [
    {
      "name": "zulipApi",
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
