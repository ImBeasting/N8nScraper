---
title: "Node: Webex by Cisco"
slug: "node-ciscowebex"
version: "1"
updated: "2025-11-13"
summary: "Consume the Cisco Webex API"
node_type: "regular"
group: "['transform']"
---

# Node: Webex by Cisco

**Purpose.** Consume the Cisco Webex API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:ciscoWebex.png`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **ciscoWebexOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `ciscoWebexOAuth2Api` | ✓ | - |

---

## Operations

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a message |
| Delete | `delete` | Delete a message |
| Get | `get` | Get a message |
| Get Many | `getAll` | Get many messages |
| Update | `update` | Update a message |

### Meeting Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a meeting |
| Delete | `delete` | Delete a meeting |
| Get | `get` | Get a meeting |
| Get Many | `getAll` | Get many meetings |
| Update | `update` | Update a meeting |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✗ | Resource to operate on |  |

**Resource options:**

* **Meeting** (`meeting`)
* **Meeeting Transcript** (`meetingTranscript`)
* **Message** (`message`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create a message
* **Delete** (`delete`) - Delete a message
* **Get** (`get`) - Get a message
* **Get Many** (`getAll`) - Get many messages
* **Update** (`update`) - Update a message

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Destination | `destination` | options | room | ✓ |  |  |

**Destination options:**

* **Room** (`room`)
* **Person** (`person`)

| Room Name or ID | `roomId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Specify Person By | `specifyPersonBy` | options | email | ✓ |  |  |

**Specify Person By options:**

* **Email** (`email`)
* **ID** (`id`)

| Person ID | `toPersonId` | string |  | ✓ |  |  |
| Person Email | `toPersonEmail` | string |  | ✓ |  | email |
| Text | `text` | string |  | ✓ | The message, in plain text |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | The URL to open | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `attachmentsUi` | fixedCollection | {} | The URL to open |
| File | `fileUi` | fixedCollection | {} | The field in the node input containing the binary file data |
| Markdown | `markdown` | string |  | The message in markdown format. When used the text parameter is used to provide alternate text for UI clients that do not support rich text. |

</details>

| Title | `title` | string |  | ✓ | Meeting title. The title can be a maximum of 128 characters long. |  |
| Start | `start` | dateTime |  | ✓ | Date and time for the start of the meeting. Acceptable <a href="https://datatracker.ietf.org/doc/html/rfc2445"> format</a>. |  |
| End | `end` | dateTime |  | ✓ | Date and time for the end of the meeting. Acceptable <a href="https://datatracker.ietf.org/doc/html/rfc2445"> format</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Meeting agenda. The agenda can be a maximum of 1300 characters long. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Agenda | `agenda` | string |  | Meeting agenda. The agenda can be a maximum of 1300 characters long. |
| Allow Any User To Be Co-Host | `allowAnyUserToBeCoHost` | boolean | False | Whether or not to allow any attendee with a host account on the target site to become a co-host when joining the meeting |
| Allow Authenticated Devices | `allowAuthenticatedDevices` | boolean | False | Whether or not to allow authenticated video devices in the meeting's organization to start or join the meeting without a prompt |
| Allow First User To Be Co-Host | `allowFirstUserToBeCoHost` | boolean | False | Whether or not to allow the first attendee of the meeting with a host account on the target site to become a co-host |
| Auto Accept Request | `autoAcceptRequest` | boolean | False | Whether or not meeting registration request is accepted automatically |
| Enable Connect Audio Before Host | `enableConnectAudioBeforeHost` | boolean | False | Whether or not to allow any attendee to connect audio in the meeting before the host joins the meeting |
| Enabled Auto Record Meeting | `enabledAutoRecordMeeting` | boolean | False | Whether or not meeting is recorded automatically |
| Enabled Join Before Host | `enabledJoinBeforeHost` | boolean | False | Whether or not to allow any attendee to join the meeting before the host joins the meeting |
| Exclude Password | `excludePassword` | boolean | False | Whether or not to exclude password from the meeting email invitation |
| Host Email | `hostEmail` | string |  | Email address for the meeting host. Can only be set if you're an admin. |
| Integration Tags | `integrationTags` | string |  | External keys created by an integration application in its own domain. They could be Zendesk ticket IDs, Jira IDs, Salesforce Opportunity IDs, etc. |
| Invitees | `inviteesUi` | fixedCollection | {} | Email address of meeting invitee |
| Join Before Host Minutes | `joinBeforeHostMinutes` | options | 0 | The number of minutes an attendee can join the meeting before the meeting start time and the host joins |
| Public Meeting | `publicMeeting` | boolean | False | Whether or not to allow the meeting to be listed on the public calendar |
| Recurrence | `recurrence` | string |  | Rule for how the meeting should recur. Acceptable <a href="https://datatracker.ietf.org/doc/html/rfc2445"> format</a>. |
| Required Registration Info | `requireRegistrationInfo` | multiOptions | [] | Data required for meeting registration |
| Reminder Time | `reminderTime` | number | 1 | The number of minutes before the meeting begins, for sending an email reminder to the host |
| Send Email | `sendEmail` | boolean | True | Whether or not to send emails to host and invitees |
| Site URL | `siteUrl` | options |  | URL of the Webex site which the meeting is created on. If not specified, the meeting is created on user's preferred site. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | ID of the message to delete |  |
| Meeting ID | `meetingId` | string |  | ✓ | ID of the meeting |  |
| Options | `options` | collection | {} | ✗ | Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Host Email | `hostEmail` | string |  | Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. |
| Send Email | `sendEmail` | boolean | True | Whether or not to send emails to host and invitees |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | ID of the message to retrieve |  |
| Meeting ID | `meetingId` | string |  | ✓ | ID of the meeting |  |
| Options | `options` | collection | {} | ✗ | Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Host Email | `hostEmail` | string |  | Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. |
| Password | `password` | string |  | Meeting password. It's required when the meeting is protected by a password and the current user is not privileged to view it if they are not a host, co-host or invitee of the meeting. |
| Send Email | `sendEmail` | boolean | True | Whether or not to send emails to host and invitees. It is an optional field and default value is true. |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Room Name or ID | `roomId` | options |  | ✓ | List messages in a room, by ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | List messages sent before a date and time | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Before | `before` | dateTime |  | List messages sent before a date and time |
| Before Message | `beforeMessage` | string |  | List messages sent before a message, by ID |
| Parent Message ID | `parentId` | string |  | List messages with a parent, by ID |
| Mentioned Person | `mentionedPeople` | string |  | List only messages with certain person mentioned. Enter their ID. You can use 'me' as a shorthand for yourself |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Start date and time (inclusive) for the meeting. Acceptable <a href="https://datatracker.ietf.org/doc/html/rfc2445"> format</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| From | `from` | dateTime |  | Start date and time (inclusive) for the meeting. Acceptable <a href="https://datatracker.ietf.org/doc/html/rfc2445"> format</a>. |
| Host Email | `hostEmail` | string |  | Email address for the meeting host |
| Integration Tag | `integrationTag` | string |  | External tag created by another application, e.g. Zendesk ticket ID or Jira ID |
| Limit to Current Meetings | `current` | boolean | True | Whether to return just the current meeting or all meetings |
| Meeting Number | `meetingNumber` | string |  | Meeting number for the meeting objects being requested |
| Meeting Type | `meetingType` | options | meetingSeries | Master of a scheduled series of meetings which consists of one or more scheduled meeting based on a recurrence rule |
| Participant Email | `participantEmail` | string |  | Email of a person that must be a meeting participant |
| Site URL | `siteUrl` | options |  | URL of the Webex site which the API lists meetings from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| State | `state` | options |  | Meeting state for the meeting objects being requested |
| To | `to` | dateTime |  | End date and time (inclusive) for the meeting. Acceptable <a href="https://datatracker.ietf.org/doc/html/rfc2445"> format</a>. |
| Weblink | `webLink` | string |  | URL encoded link to information page for the meeting objects being requested |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message ID | `messageId` | string |  | ✓ | ID of the message to update |  |
| Is Markdown | `markdown` | boolean | False | ✓ | Whether the message uses markdown |  |
| Text | `text` | string |  | ✓ | The message, in plain text |  |
| Markdown | `markdownText` | string |  | ✓ | The message, in Markdown format. The maximum message length is 7439 bytes. |  |
| Meeting ID | `meetingId` | string |  | ✓ | ID of the meeting |  |
| Update Fields | `updateFields` | collection | {} | ✓ | The meeting's agenda. Cannot be longer that 1300 characters. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Agenda | `agenda` | string |  | The meeting's agenda. Cannot be longer that 1300 characters. |
| Allow Any User To Be Co-Host | `allowAnyUserToBeCoHost` | boolean | False | Whether or not to allow any attendee with a host account on the target site to become a co-host when joining the meeting |
| Allow Authenticated Devices | `allowAuthenticatedDevices` | boolean | False | Whether or not to allow authenticated video devices in the meeting's organization to start or join the meeting without a prompt |
| Allow First User To Be Co-Host | `allowFirstUserToBeCoHost` | boolean | False | Whether or not to allow the first attendee of the meeting with a host account on the target site to become a co-host |
| Enable Connect Audio Before Host | `enableConnectAudioBeforeHost` | boolean | False | Whether or not to allow any attendee to connect audio in the meeting before the host joins the meeting |
| Enabled Auto Record Meeting | `enabledAutoRecordMeeting` | boolean | False | Whether or not meeting is recorded automatically |
| Enabled Join Before Host | `enabledJoinBeforeHost` | boolean | False | Whether or not to allow any attendee to join the meeting before the host joins the meeting |
| End | `end` | dateTime |  | Date and time for the end of the meeting. Acceptable <a href="https://datatracker.ietf.org/doc/html/rfc2445"> format</a>. |
| Exclude Password | `excludePassword` | boolean | False | Whether or not to exclude password from the meeting email invitation |
| Host Email | `hostEmail` | string |  | Email address for the meeting host. This attribute should only be set if the user or application calling the API has the admin-level scopes. |
| Invitees | `inviteesUi` | fixedCollection | {} | Email address of meeting invitee |
| Join Before Host Minutes | `joinBeforeHostMinutes` | options | 0 | The number of minutes an attendee can join the meeting before the meeting start time and the host joins |
| Password | `password` | string |  | Meeting password. Must conform to the site's password complexity settings. If not specified, a random password conforming to the site's password rules will be generated automatically |
| Public Meeting | `publicMeeting` | boolean | False | Whether or not to allow the meeting to be listed on the public calendar |
| Recurrence | `recurrence` | string |  | Meeting series recurrence rule (conforming with RFC 2445), applying only to meeting series |
| Required Registration Info | `requireRegistrationInfo` | multiOptions | [] | Data required for meeting registration |
| Reminder Time | `reminderTime` | number | 1 | The number of minutes before the meeting begins, for sending an email reminder to the host |
| Send Email | `sendEmail` | boolean | False | Whether or not to send emails to host and invitees. It is an optional field and default value is true. |
| Site URL | `siteUrl` | options |  | URL of the Webex site which the meeting is created on. If not specified, the meeting is created on user's preferred site. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Start | `start` | dateTime |  | Date and time for the start of the meeting. Acceptable <a href="https://datatracker.ietf.org/doc/html/rfc2445"> format</a>. |
| Title | `title` | string |  | Meeting title |

</details>


---

## Load Options Methods

- `getRooms`
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
* Categories: Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: ciscoWebex
displayName: Webex by Cisco
description: Consume the Cisco Webex API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: ciscoWebexOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: destination
    name: Destination
    type: options
    default: room
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - create
    typeInfo:
      type: options
      displayName: Destination
      name: destination
      possibleValues:
      - value: room
        name: Room
        description: ''
      - value: person
        name: Person
        description: ''
  - id: roomId
    name: Room Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - getAll
    typeInfo: &id006
      type: options
      displayName: Room Name or ID
      name: roomId
      typeOptions:
        loadOptionsMethod: getRooms
      possibleValues: []
  - id: specifyPersonBy
    name: Specify Person By
    type: options
    default: email
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - create
          destination:
          - person
    typeInfo:
      type: options
      displayName: Specify Person By
      name: specifyPersonBy
      possibleValues:
      - value: email
        name: Email
        description: ''
      - value: id
        name: ID
        description: ''
  - id: toPersonId
    name: Person ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - create
          specifyPersonBy:
          - id
    typeInfo:
      type: string
      displayName: Person ID
      name: toPersonId
  - id: toPersonEmail
    name: Person Email
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - message
          operation:
          - create
          specifyPersonBy:
          - email
    typeInfo:
      type: string
      displayName: Person Email
      name: toPersonEmail
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: The message, in plain text
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - update
          markdown:
          - false
    typeInfo: &id012
      type: string
      displayName: Text
      name: text
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Meeting title. The title can be a maximum of 128 characters long.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - meeting
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: start
    name: Start
    type: dateTime
    default: ''
    required: true
    description: Date and time for the start of the meeting. Acceptable <a href="https://datatracker.ietf.org/doc/html/rfc2445">
      format</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - meeting
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: Start
      name: start
  - id: end
    name: End
    type: dateTime
    default: ''
    required: true
    description: Date and time for the end of the meeting. Acceptable <a href="https://datatracker.ietf.org/doc/html/rfc2445">
      format</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - meeting
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: End
      name: end
- id: delete
  name: Delete
  description: ''
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ID of the message to delete
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: Message ID
      name: messageId
  - id: meetingId
    name: Meeting ID
    type: string
    default: ''
    required: true
    description: ID of the meeting
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - meeting
          operation:
          - update
    typeInfo: &id004
      type: string
      displayName: Meeting ID
      name: meetingId
- id: get
  name: Get
  description: ''
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ID of the message to retrieve
    validation: *id001
    typeInfo: *id002
  - id: meetingId
    name: Meeting ID
    type: string
    default: ''
    required: true
    description: ID of the meeting
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: roomId
    name: Room Name or ID
    type: options
    default: ''
    required: true
    description: List messages in a room, by ID. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id007
      displayOptions:
        show:
          resource:
          - meeting
          operation:
          - getAll
    typeInfo: &id008
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id009
      displayOptions:
        show:
          resource:
          - meeting
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id010
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id007
    typeInfo: *id008
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
- id: update
  name: Update
  description: ''
  params:
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: ID of the message to update
    validation: *id001
    typeInfo: *id002
  - id: markdown
    name: Is Markdown
    type: boolean
    default: false
    required: true
    description: Whether the message uses markdown
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - update
    typeInfo:
      type: boolean
      displayName: Is Markdown
      name: markdown
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: The message, in plain text
    validation: *id011
    typeInfo: *id012
  - id: markdownText
    name: Markdown
    type: string
    default: ''
    required: true
    description: The message, in Markdown format. The maximum message length is 7439
      bytes.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - update
          markdown:
          - true
    typeInfo:
      type: string
      displayName: Markdown
      name: markdownText
  - id: meetingId
    name: Meeting ID
    type: string
    default: ''
    required: true
    description: ID of the meeting
    validation: *id003
    typeInfo: *id004
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
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: filters
    text: Add Filter
  - field: updateFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/ciscoWebex.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Webex by Cisco Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "get",
        "getAll",
        "update"
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
            "meeting",
            "meetingTranscript",
            "message"
          ],
          "default": "message"
        },
        "destination": {
          "description": "",
          "type": "string",
          "enum": [
            "room",
            "person"
          ],
          "default": "room"
        },
        "roomId": {
          "description": "List messages in a room, by ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "specifyPersonBy": {
          "description": "",
          "type": "string",
          "enum": [
            "email",
            "id"
          ],
          "default": "email"
        },
        "toPersonId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "toPersonEmail": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "email"
        },
        "text": {
          "description": "The message, in plain text",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Meeting agenda. The agenda can be a maximum of 1300 characters long.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "messageId": {
          "description": "ID of the message to update",
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
          "default": 50
        },
        "filters": {
          "description": "Start date and time (inclusive) for the meeting. Acceptable <a href=\"https://datatracker.ietf.org/doc/html/rfc2445\"> format</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "markdown": {
          "description": "Whether the message uses markdown",
          "type": "boolean",
          "default": false
        },
        "markdownText": {
          "description": "The message, in Markdown format. The maximum message length is 7439 bytes.",
          "type": "string",
          "default": ""
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "title": {
          "description": "Meeting title. The title can be a maximum of 128 characters long.",
          "type": "string",
          "default": ""
        },
        "start": {
          "description": "Date and time for the start of the meeting. Acceptable <a href=\"https://datatracker.ietf.org/doc/html/rfc2445\"> format</a>.",
          "type": "string",
          "default": ""
        },
        "end": {
          "description": "Date and time for the end of the meeting. Acceptable <a href=\"https://datatracker.ietf.org/doc/html/rfc2445\"> format</a>.",
          "type": "string",
          "default": ""
        },
        "meetingId": {
          "description": "ID of the meeting",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "updateFields": {
          "description": "The meeting's agenda. Cannot be longer that 1300 characters.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
      "name": "ciscoWebexOAuth2Api",
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
