---
title: "Node: HighLevel"
slug: "node-resource"
version: "2"
updated: "2026-01-08"
summary: "Consume HighLevel API"
node_type: "regular"
group: "['transform']"
---

# Node: HighLevel

**Purpose.** Consume HighLevel API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:highLevel.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **highLevelOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **contactCreateNotice** when resource=['contact'], operation=['create']: Create a new contact or update an existing one if email or phone matches (upsert)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `highLevelOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Calendar Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Book Appointment | `bookAppointment` | Book appointment in a calendar |
| Get Free Slots | `getFreeSlots` | Get free slots of a calendar |

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Opportunity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✓ | Resource to operate on |  |

**Resource options:**

* **Contact** (`contact`)
* **Opportunity** (`opportunity`)
* **Task** (`task`)
* **Calendar** (`calendar`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | bookAppointment | ✗ | Operation to perform |  |

**Operation options:**

* **Book Appointment** (`bookAppointment`) - Book appointment in a calendar
* **Get Free Slots** (`getFreeSlots`) - Get free slots of a calendar

---

### Book Appointment parameters (`bookAppointment`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Calendar ID | `calendarId` | string |  | ✓ |  |  |
| Location ID | `locationId` | string |  | ✓ |  |  |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Start Time | `startTime` | string |  | ✓ | Example: 2021-06-23T03:30:00+05:30 |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Example: 2021-06-23T04:30:00+05:30 | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| End Time | `endTime` | string |  | Example: 2021-06-23T04:30:00+05:30 |
| Title | `title` | string |  |  |
| Appointment Status | `appointmentStatus` | options | new | The status of the appointment. Allowed values: new, confirmed, cancelled, showed, noshow, invalid. |
| Assigned User ID | `assignedUserId` | string |  |  |
| Address | `address` | string |  |  |
| Ignore Date Range | `ignoreDateRange` | boolean | False |  |
| Notify | `toNotify` | boolean | True |  |

</details>


### Get Free Slots parameters (`getFreeSlots`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Calendar ID | `calendarId` | string |  | ✓ |  |  |
| Start Date | `startDate` | number |  | ✓ | The start date for fetching free calendar slots. Example: 1548898600000. |  |
| End Date | `endDate` | number |  | ✓ | The end date for fetching free calendar slots. Example: 1601490599999. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The timezone to use for the returned slots. Example: America/Chihuahua. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Timezone | `timezone` | string |  | The timezone to use for the returned slots. Example: America/Chihuahua. |
| User ID | `userId` | string |  | User ID to filter the slots (optional) |
| User IDs | `userIds` | collection | {} | Comma-separated list of user IDs to filter the slots |
| Apply Look Busy | `enableLookBusy` | boolean | False | Apply Look Busy to the slots |

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: resource
displayName: HighLevel
description: Consume HighLevel API
version: '2'
nodeType: regular
group:
- transform
credentials:
- name: highLevelOAuth2Api
  required: true
operations:
- id: bookAppointment
  name: Book Appointment
  description: ''
  params:
  - id: calendarId
    name: Calendar ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - calendar
          operation:
          - getFreeSlots
    typeInfo: &id002
      type: string
      displayName: Calendar ID
      name: calendarId
  - id: locationId
    name: Location ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - calendar
          operation:
          - bookAppointment
    typeInfo:
      type: string
      displayName: Location ID
      name: locationId
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - getAll
    typeInfo:
      type: options
      displayName: Contact Email or ID
      name: contactId
      typeOptions:
        loadOptionsMethod: getContacts
      possibleValues: []
  - id: startTime
    name: Start Time
    type: string
    default: ''
    required: true
    description: 'Example: 2021-06-23T03:30:00+05:30'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - calendar
          operation:
          - bookAppointment
    typeInfo:
      type: string
      displayName: Start Time
      name: startTime
- id: getFreeSlots
  name: Get Free Slots
  description: ''
  params:
  - id: calendarId
    name: Calendar ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: startDate
    name: Start Date
    type: number
    default: ''
    required: true
    description: 'The start date for fetching free calendar slots. Example: 1548898600000.'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - calendar
          operation:
          - getFreeSlots
    typeInfo:
      type: number
      displayName: Start Date
      name: startDate
  - id: endDate
    name: End Date
    type: number
    default: ''
    required: true
    description: 'The end date for fetching free calendar slots. Example: 1601490599999.'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - calendar
          operation:
          - getFreeSlots
    typeInfo:
      type: number
      displayName: End Date
      name: endDate
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
  - name: contactCreateNotice
    text: Create a new contact or update an existing one if email or phone matches
      (upsert)
    conditions:
      show:
        resource:
        - contact
        operation:
        - create
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: phone
    text: '+491234567890'
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: options
    text: Add option
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  hints:
  - field: additionalFields
    text: Comma separated list of tags, array of strings can be set in expression
  - field: updateFields
    text: Comma separated list of tags, array of strings can be set in expression
  - field: contactId
    text: There can only be one opportunity for each contact
  - field: additionalFields
    text: Comma separated list of tags, array of strings can be set in expression
  - field: opportunityId
    text: You cannot update an opportunity's pipeline ID.
  - field: updateFields
    text: Select 'Pipeline Name or ID' first to see stages
  - field: filters
    text: Select 'Pipeline Name or ID' first to see stages
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
  "$id": "https://n8n.io/schemas/nodes/resource.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HighLevel Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "bookAppointment",
        "getFreeSlots"
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
            "contact",
            "opportunity",
            "task",
            "calendar"
          ],
          "default": "contact"
        },
        "calendarId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "locationId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "contactId": {
          "description": "Contact the task belongs to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "startTime": {
          "description": "Example: 2021-06-23T03:30:00+05:30",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "startDate": {
          "description": "The start date for fetching free calendar slots. Example: 1548898600000.",
          "type": "number",
          "default": ""
        },
        "endDate": {
          "description": "The end date for fetching free calendar slots. Example: 1601490599999.",
          "type": "number",
          "default": ""
        },
        "operation": {
          "description": "",
          "type": "string",
          "default": "create"
        },
        "email": {
          "description": "Lookup Contact by Email. If Email is not found it will try to find a contact by phone.",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "phone": {
          "description": "Lookup Contact by Phone. It will first try to find a contact by Email and than by Phone.",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 20
        },
        "filters": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "options": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "name": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "status": {
          "description": "",
          "type": "string",
          "enum": [
            "open",
            "won",
            "lost",
            "abandoned"
          ],
          "default": "open"
        },
        "opportunityId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "dueDate": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "completed": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "taskId": {
          "description": "",
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
    "version": "2"
  },
  "credentials": [
    {
      "name": "highLevelOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 2 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
