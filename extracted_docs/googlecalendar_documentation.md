---
title: "Node: Google Calendar"
slug: "node-googlecalendar"
version: "['1', '1.1', '1.2', '1.3']"
updated: "2026-01-08"
summary: "Consume Google Calendar API"
node_type: "regular"
group: "['input']"
---

# Node: Google Calendar

**Purpose.** Consume Google Calendar API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:googleCalendar.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleCalendarOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **useN8nTimeZone**: This node will use the time zone set in n8n’s settings, but you can override this in the workflow settings

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleCalendarOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Calendar Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Availability | `availability` | If a time-slot is available in a calendar |

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Add a event to calendar |
| Delete | `delete` | Delete an event |
| Get | `get` | Retrieve an event |
| Get Many | `getAll` | Retrieve many events from a calendar |
| Update | `update` | Update an event |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | event | ✗ | Resource to operate on |  |

**Resource options:**

* **Calendar** (`calendar`)
* **Event** (`event`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | availability | ✗ | If a time-slot is available in a calendar |  |

**Operation options:**

* **Availability** (`availability`) - If a time-slot is available in a calendar

---

### Availability parameters (`availability`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Start Time | `timeMin` | dateTime |  | ✓ | Start of the interval |  |
| End Time | `timeMax` | dateTime |  | ✓ | End of the interval |  |
| Options | `options` | collection | {} | ✗ | Returns if there are any events in the given time or not | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Output Format | `outputFormat` | options | availability | Returns if there are any events in the given time or not |
| Timezone | `timezone` | resourceLocator |  | Time zone used in the response. By default n8n timezone is used. |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Start | `start` | dateTime |  | ✓ | Start time of the event |  |
| End | `end` | dateTime |  | ✓ | End time of the event |  |
| Use Default Reminders | `useDefaultReminders` | boolean | True | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether the event is all day or not | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| All Day | `allday` | options | no | Whether the event is all day or not |
| Attendees | `attendees` | string |  | The attendees of the event. Multiple ones can be separated by comma. |
| Color Name or ID | `color` | options |  | The color of the event. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Conference Data | `conferenceDataUi` | fixedCollection | {} | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Description | `description` | string |  |  |
| Guests Can Invite Others | `guestsCanInviteOthers` | boolean | True | Whether attendees other than the organizer can invite others to the event |
| Guests Can Modify | `guestsCanModify` | boolean | False | Whether attendees other than the organizer can modify the event |
| Guests Can See Other Guests | `guestsCanSeeOtherGuests` | boolean | True | Whether attendees other than the organizer can see who the event's attendees are |
| ID | `id` | string |  | Opaque identifier of the event |
| Location | `location` | string |  | Geographic location of the event as free-form text |
| Max Attendees | `maxAttendees` | number | 0 | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. |
| Repeat Frequency | `repeatFrecuency` | options |  |  |
| Repeat How Many Times? | `repeatHowManyTimes` | number | 1 |  |
| Repeat Until | `repeatUntil` | dateTime |  |  |
| RRULE | `rrule` | string |  | Recurrence rule. When set, the parameters Repeat Frequency, Repeat How Many Times and Repeat Until are ignored. |
| Send Updates | `sendUpdates` | options |  | Notifications are sent to all guests |
| Show Me As | `showMeAs` | options | opaque | The event does not block time on the calendar |
| Summary | `summary` | string |  | Title of the event |
| Visibility | `visibility` | options | default | The event is private. This value is provided for compatibility reasons. |

</details>

| Reminders | `remindersUi` | fixedCollection | {} | ✗ | If the event doesn't use the default reminders, this lists the reminders specific to the event | e.g. Add Reminder |  |

<details>
<summary><strong>Reminders sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Reminder | `remindersValues` |  |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event ID | `eventId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | Notifications are sent to all guests | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Send Updates | `sendUpdates` | options |  | Notifications are sent to all guests |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event ID | `eventId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Max Attendees | `maxAttendees` | number | 0 | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. |
| Return Next Instance of Recurring Event | `returnNextInstance` | boolean | False | Whether to return the next instance of a recurring event instead of the event itself |
| Timezone | `timeZone` | resourceLocator |  | Time zone used in the response. The default is the time zone of the calendar. |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | At least some part of the event must be after this time, use <a href="https://docs.n8n.io/code/cookbook/luxon/" target="_blank">expression</a> to set a date, or switch to fixed mode to choose date from widget | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| After | `timeMin` | dateTime |  | At least some part of the event must be after this time, use <a href="https://docs.n8n.io/code/cookbook/luxon/" target="_blank">expression</a> to set a date, or switch to fixed mode to choose date from widget |
| Before | `timeMax` | dateTime |  | At least some part of the event must be before this time, use <a href="https://docs.n8n.io/code/cookbook/luxon/" target="_blank">expression</a> to set a date, or switch to fixed mode to choose date from widget |
| Expand Events | `singleEvents` | boolean | False | Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves |
| Fields | `fields` | string |  | Specify fields to return, by default a predefined by Google set of commonly used fields would be returned. To return all fields, use '*', <a href='https://developers.google.com/calendar/api/guides/performance#partial' target='_blank'>More info</a>. |
| iCalUID | `iCalUID` | string |  | Specifies event ID in the iCalendar format to be included in the response |
| Max Attendees | `maxAttendees` | number | 0 | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. |
| Order By | `orderBy` | options |  | Order by the start date/time (ascending). This is only available when querying single events (i.e. the parameter singleEvents is True). |
| Query | `query` | string |  | Free text search terms to find events that match these terms in any field, except for extended properties |
| Recurring Event Handling | `recurringEventHandling` | options | expand | Return all instances of recurring event for specified time range |
| Show Deleted | `showDeleted` | boolean | False | Whether to include deleted events (with status equals "cancelled") in the result |
| Show Hidden Invitations | `showHiddenInvitations` | boolean | False | Whether to include hidden invitations in the result |
| Timezone | `timeZone` | resourceLocator |  | Time zone used in the response. The default is the time zone of the calendar. |
| Updated Min | `updatedMin` | dateTime |  | Lower bound for an event's last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event ID | `eventId` | string |  | ✓ |  |  |
| Use Default Reminders | `useDefaultReminders` | boolean | True | ✗ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Whether the event is all day or not | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| All Day | `allday` | options | no | Whether the event is all day or not |
| Attendees | `attendeesUi` | fixedCollection | add | The attendees of the event. Multiple ones can be separated by comma. |
| Attendees | `attendees` | string |  | The attendees of the event. Multiple ones can be separated by comma. |
| Color Name or ID | `color` | options |  | The color of the event. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  |  |
| End | `end` | dateTime |  | End time of the event |
| Guests Can Invite Others | `guestsCanInviteOthers` | boolean | True | Whether attendees other than the organizer can invite others to the event |
| Guests Can Modify | `guestsCanModify` | boolean | False | Whether attendees other than the organizer can modify the event |
| Guests Can See Other Guests | `guestsCanSeeOtherGuests` | boolean | True | Whether attendees other than the organizer can see who the event's attendees are |
| ID | `id` | string |  | Opaque identifier of the event |
| Location | `location` | string |  | Geographic location of the event as free-form text |
| Max Attendees | `maxAttendees` | number | 0 | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. |
| Repeat Frequency | `repeatFrecuency` | options |  |  |
| Repeat How Many Times? | `repeatHowManyTimes` | number | 1 |  |
| Repeat Until | `repeatUntil` | dateTime |  |  |
| RRULE | `rrule` | string |  | Recurrence rule. When set, the parameters Repeat Frequency, Repeat How Many Times and Repeat Until are ignored. |
| Send Updates | `sendUpdates` | options |  | Notifications are sent to all guests |
| Show Me As | `showMeAs` | options | opaque | The event does not block time on the calendar |
| Start | `start` | dateTime |  | Start time of the event |
| Summary | `summary` | string |  | Title of the event |
| Visibility | `visibility` | options | default | The event is private. This value is provided for compatibility reasons. |

</details>

| Reminders | `remindersUi` | fixedCollection | {} | ✗ | If the event doesn't use the default reminders, this lists the reminders specific to the event | e.g. Add Reminder |  |

<details>
<summary><strong>Reminders sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Reminder | `remindersValues` |  |  |  |

</details>


---

## Load Options Methods

- `getConferenceSolutions`

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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleCalendar
displayName: Google Calendar
description: Consume Google Calendar API
version:
- '1'
- '1.1'
- '1.2'
- '1.3'
nodeType: regular
group:
- input
credentials:
- name: googleCalendarOAuth2Api
  required: true
operations:
- id: availability
  name: Availability
  description: If a time-slot is available in a calendar
  params:
  - id: timeMin
    name: Start Time
    type: dateTime
    default: ''
    required: true
    description: Start of the interval
    validation:
      displayOptions:
        show: {}
    typeInfo:
      type: dateTime
      displayName: After
      name: timeMin
  - id: timeMax
    name: End Time
    type: dateTime
    default: ''
    required: true
    description: End of the interval
    validation:
      displayOptions:
        show: {}
    typeInfo:
      type: dateTime
      displayName: Before
      name: timeMax
- id: create
  name: Create
  description: Add a event to calendar
  params:
  - id: start
    name: Start
    type: dateTime
    default: ''
    required: true
    description: Start time of the event
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - event
    typeInfo:
      type: dateTime
      displayName: Start
      name: start
  - id: end
    name: End
    type: dateTime
    default: ''
    required: true
    description: End time of the event
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - event
    typeInfo:
      type: dateTime
      displayName: End
      name: end
  - id: useDefaultReminders
    name: Use Default Reminders
    type: boolean
    default: true
    required: false
    description: ''
    validation: &id003
      displayOptions:
        show:
          operation:
          - update
          resource:
          - event
    typeInfo: &id004
      type: boolean
      displayName: Use Default Reminders
      name: useDefaultReminders
  - id: remindersUi
    name: Reminders
    type: fixedCollection
    default: {}
    required: false
    description: If the event doesn't use the default reminders, this lists the reminders
      specific to the event
    placeholder: Add Reminder
    validation: &id005
      displayOptions:
        show:
          resource:
          - event
          operation:
          - update
          useDefaultReminders:
          - false
    typeInfo: &id006
      type: fixedCollection
      displayName: Reminders
      name: remindersUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: remindersValues
        displayName: Reminder
        values:
        - displayName: Method
          name: method
          type: options
          value: email
          default: ''
          options:
          - name: Email
            value: email
            displayName: Email
          - name: Popup
            value: popup
            displayName: Popup
        - displayName: Minutes Before
          name: minutes
          type: number
          default: 0
          typeOptions:
            minValue: 0
            maxValue: 40320
- id: delete
  name: Delete
  description: Delete an event
  params:
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - event
    typeInfo: &id002
      type: string
      displayName: Event ID
      name: eventId
- id: get
  name: Get
  description: Retrieve an event
  params:
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Retrieve many events from a calendar
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
          - getAll
          resource:
          - event
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - event
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
- id: update
  name: Update
  description: Update an event
  params:
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: useDefaultReminders
    name: Use Default Reminders
    type: boolean
    default: true
    required: false
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: remindersUi
    name: Reminders
    type: fixedCollection
    default: {}
    required: false
    description: If the event doesn't use the default reminders, this lists the reminders
      specific to the event
    placeholder: Add Reminder
    validation: *id005
    typeInfo: *id006
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
  - name: useN8nTimeZone
    text: This node will use the time zone set in n8n’s settings, but you can override
      this in the workflow settings
    conditions: null
  tooltips: []
  placeholders:
  - field: calendar
    text: Select a Calendar...
  - field: options
    text: Add option
  - field: calendar
    text: Select a Calendar...
  - field: additionalFields
    text: Add Field
  - field: remindersUi
    text: Add Reminder
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: updateFields
    text: Add Field
  - field: remindersUi
    text: Add Reminder
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
  "$id": "https://n8n.io/schemas/nodes/googleCalendar.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Calendar Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "availability",
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
            "calendar",
            "event"
          ],
          "default": "event"
        },
        "operation": {
          "description": "Add a event to calendar",
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
        "calendar": {
          "description": "Google Calendar to operate on",
          "type": "string",
          "examples": [
            "Select a Calendar..."
          ]
        },
        "timeMin": {
          "description": "At least some part of the event must be after this time, use <a href=\"https://docs.n8n.io/code/cookbook/luxon/\" target=\"_blank\">expression</a> to set a date, or switch to fixed mode to choose date from widget",
          "type": "string",
          "default": "={{ $now }}"
        },
        "timeMax": {
          "description": "At least some part of the event must be before this time, use <a href=\"https://docs.n8n.io/code/cookbook/luxon/\" target=\"_blank\">expression</a> to set a date, or switch to fixed mode to choose date from widget",
          "type": "string",
          "default": "={{ $now.plus({ week: 1 }) }}"
        },
        "options": {
          "description": "At least some part of the event must be after this time, use <a href=\"https://docs.n8n.io/code/cookbook/luxon/\" target=\"_blank\">expression</a> to set a date, or switch to fixed mode to choose date from widget",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "start": {
          "description": "Start time of the event",
          "type": "string",
          "default": ""
        },
        "end": {
          "description": "End time of the event",
          "type": "string",
          "default": ""
        },
        "useDefaultReminders": {
          "description": "",
          "type": "boolean",
          "default": true
        },
        "additionalFields": {
          "description": "Whether the event is all day or not",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "remindersUi": {
          "description": "If the event doesn't use the default reminders, this lists the reminders specific to the event",
          "type": "string",
          "default": {},
          "examples": [
            "Add Reminder"
          ]
        },
        "eventId": {
          "description": "",
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
        "modifyTarget": {
          "description": "",
          "type": "string",
          "enum": [
            "instance",
            "event"
          ],
          "default": "instance"
        },
        "updateFields": {
          "description": "Whether the event is all day or not",
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
    "version": [
      "1",
      "1.1",
      "1.2",
      "1.3"
    ]
  },
  "credentials": [
    {
      "name": "googleCalendarOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1', '1.2', '1.3'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
