---
title: "Node: Zoom"
slug: "node-zoom"
version: "1"
updated: "2025-11-13"
summary: "Consume Zoom API"
node_type: "regular"
group: "['input']"
---

# Node: Zoom

**Purpose.** Consume Zoom API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:zoom.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **zoomApi**: N/A
- **zoomOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `zoomApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `zoomOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Meeting Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a meeting |
| Delete | `delete` | Delete a meeting |
| Get | `get` | Retrieve a meeting |
| Get Many | `getAll` | Retrieve many meetings |
| Update | `update` | Update a meeting |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | meeting | ✗ | Resource to operate on |  |

**Resource options:**

* **Meeting** (`meeting`)
* **Meeting Registrant** (`meetingRegistrant`)
* **Webinar** (`webinar`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a meeting |  |

**Operation options:**

* **Create** (`create`) - Create a meeting
* **Delete** (`delete`) - Delete a meeting
* **Get** (`get`) - Retrieve a meeting
* **Get Many** (`getAll`) - Retrieve many meetings
* **Update** (`update`) - Update a meeting

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Topic | `topic` | string |  | ✗ | Topic of the meeting |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Meeting agenda | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Agenda | `agenda` | string |  | Meeting agenda |
| Duration | `duration` | number | 0 | Meeting duration (minutes) |
| Password | `password` | string |  | Password to join the meeting with maximum 10 characters |
| Schedule For | `scheduleFor` | string |  | Schedule meeting for someone else from your account, provide their email ID |
| Settings | `settings` | collection | {} | Determine how participants can join audio portion of the meeting |
| Start Time | `startTime` | dateTime |  | Start time should be used only for scheduled or recurring meetings with fixed time |
| Timezone Name or ID | `timeZone` | options |  | Time zone used in the response. The default is the time zone of the calendar. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Type | `type` | options | 2 | Meeting type |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `meetingId` | string |  | ✓ | Meeting ID |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Meeting occurrence ID | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Occurrence ID | `occurrenceId` | string |  | Meeting occurrence ID |
| Schedule Reminder | `scheduleForReminder` | boolean | False | Whether to notify hosts and alternative hosts about meeting cancellation via email |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `meetingId` | string |  | ✓ | Meeting ID |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | To view meeting details of a particular occurrence of the recurring meeting | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Occurrence ID | `occurrenceId` | string |  | To view meeting details of a particular occurrence of the recurring meeting |
| Show Previous Occurrences | `showPreviousOccurrences` | boolean | False | Whether to view meeting details of all previous occurrences of the recurring meeting |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 30 | ✗ | Max number of results to return | min:1, max:300 |
| Filters | `filters` | collection | {} | ✗ | This includes all valid past meetings, live meetings and upcoming scheduled meetings | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Type | `type` | options | live | This includes all valid past meetings, live meetings and upcoming scheduled meetings |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `meetingId` | string |  | ✓ | Meeting ID |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Meeting agenda | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Agenda | `agenda` | string |  | Meeting agenda |
| Duration | `duration` | number | 0 | Meeting duration (minutes) |
| Password | `password` | string |  | Password to join the meeting with maximum 10 characters |
| Schedule For | `scheduleFor` | string |  | Schedule meeting for someone else from your account, provide their email ID |
| Settings | `settings` | collection | {} | Determine how participants can join audio portion of the meeting |
| Start Time | `startTime` | dateTime |  | Start time should be used only for scheduled or recurring meetings with fixed time |
| Timezone Name or ID | `timeZone` | options |  | Time zone used in the response. The default is the time zone of the calendar. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Topic | `topic` | string |  | Meeting topic |
| Type | `type` | options | 2 | Meeting type |

</details>


---

## Load Options Methods

- `getTimezones`
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
node: zoom
displayName: Zoom
description: Consume Zoom API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: zoomApi
  required: true
- name: zoomOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a meeting
  params:
  - id: topic
    name: Topic
    type: string
    default: ''
    required: false
    description: Topic of the meeting
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - meeting
    typeInfo:
      type: string
      displayName: Topic
      name: topic
- id: delete
  name: Delete
  description: Delete a meeting
  params:
  - id: meetingId
    name: ID
    type: string
    default: ''
    required: true
    description: Meeting ID
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - meeting
    typeInfo: &id002
      type: string
      displayName: ID
      name: meetingId
- id: get
  name: Get
  description: Retrieve a meeting
  params:
  - id: meetingId
    name: ID
    type: string
    default: ''
    required: true
    description: Meeting ID
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Retrieve many meetings
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
          - meeting
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 30
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - meeting
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 300
- id: update
  name: Update
  description: Update a meeting
  params:
  - id: meetingId
    name: ID
    type: string
    default: ''
    required: true
    description: Meeting ID
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
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/zoom.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Zoom Node",
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
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "accessToken",
            "oAuth2"
          ],
          "default": "accessToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "meeting",
            "meetingRegistrant",
            "webinar"
          ],
          "default": "meeting"
        },
        "operation": {
          "description": "Create a meeting",
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
        "topic": {
          "description": "Topic of the meeting",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Meeting occurrence ID",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "meetingId": {
          "description": "Meeting ID",
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
          "default": 30
        },
        "filters": {
          "description": "This includes all valid past meetings, live meetings and upcoming scheduled meetings",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "updateFields": {
          "description": "Meeting agenda",
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
      "name": "zoomApi",
      "required": true
    },
    {
      "name": "zoomOAuth2Api",
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
