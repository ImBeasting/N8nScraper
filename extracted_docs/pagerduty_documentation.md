---
title: "Node: PagerDuty"
slug: "node-pagerduty"
version: "1"
updated: "2025-11-13"
summary: "Consume PagerDuty API"
node_type: "regular"
group: "['output']"
---

# Node: PagerDuty

**Purpose.** Consume PagerDuty API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:pagerDuty.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **pagerDutyApi**: N/A
- **pagerDutyOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `pagerDutyApi` | ✓ | {'show': {'authentication': ['apiToken']}} |
| `pagerDutyOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Incident Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an incident |
| Get | `get` | Get an incident |
| Get Many | `getAll` | Get many incidents |
| Update | `update` | Update an incident |

### Incidentnote Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a incident note |
| Get Many | `getAll` | Get many incident's notes |

### Logentry Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a log entry |
| Get Many | `getAll` | Get many log entries |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a user |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | incident | ✗ | Resource to operate on |  |

**Resource options:**

* **Incident** (`incident`)
* **Incident Note** (`incidentNote`)
* **Log Entry** (`logEntry`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create an incident |  |

**Operation options:**

* **Create** (`create`) - Create an incident
* **Get** (`get`) - Get an incident
* **Get Many** (`getAll`) - Get many incidents
* **Update** (`update`) - Update an incident

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ | A succinct description of the nature, symptoms, cause, or effect of the incident |  |
| Service Name or ID | `serviceId` | options |  | ✓ | The incident will be created on this service. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Email | `email` | string |  | ✓ | The email address of a valid user associated with the account making the request | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Delegate this incident to the specified escalation policy. Cannot be specified if an assignee is given. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Escalation Policy Name or ID | `escalationPolicyId` | options |  | Delegate this incident to the specified escalation policy. Cannot be specified if an assignee is given. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Incident Details | `details` | string |  | Additional details about the incident which will go in the body |
| Incident Key | `incidentKey` | string |  | Sending subsequent requests referencing the same service and with the same incident_key will result in those requests being rejected if an open incident matches that incident_key |
| Priority Name or ID | `priorityId` | options |  | The incident will be created on this service. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Urgency | `urgency` | options |  | The urgency of the incident |

</details>

| Conference Bridge | `conferenceBridgeUi` | fixedCollection | {} | ✗ | Phone numbers should be formatted like +1 415-555-1212,,,,1234#, where a comma (,) represents a one-second wait and pound (#) completes access code input | e.g. Add Conference Bridge |  |

<details>
<summary><strong>Conference Bridge sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conference Bridge | `conferenceBridgeValues` |  |  |  |

</details>

| Incident ID | `incidentId` | string |  | ✓ | Unique identifier for the incident |  |
| Content | `content` | string |  | ✓ | The note content |  |
| Email | `email` | string |  | ✓ | The email address of a valid user associated with the account making the request | e.g. name@email.com | email |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Incident ID | `incidentId` | string |  | ✓ | Unique identifier for the incident |  |
| Log Entry ID | `logEntryId` | string |  | ✓ | Unique identifier for the log entry |  |
| User ID | `userId` | string |  | ✓ | Unique identifier for the user |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | When set to all, the since and until parameters and defaults are ignored | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date Range | `dateRange` | options |  | When set to all, the since and until parameters and defaults are ignored |
| Incident Key | `incidentKey` | string |  | Incident de-duplication key. Incidents with child alerts do not have an incident key; querying by incident key will return incidents whose alerts have alert_key matching the given incident key. |
| Include | `include` | multiOptions | [] | Additional details to include |
| Service Names or IDs | `serviceIds` | multiOptions | [] | Returns only the incidents associated with the passed service(s). Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Since | `since` | dateTime |  | The start of the date range over which you want to search. (the limit on date ranges is 6 months). |
| Sort By | `sortBy` | string |  | Used to specify both the field you wish to sort the results on (incident_number/created_at/resolved_at/urgency), as well as the direction (asc/desc) of the results. The sort_by field and direction should be separated by a colon. A maximum of two fields can be included, separated by a comma. |
| Statuses | `statuses` | multiOptions | [] | Returns only the incidents associated with the passed service(s) |
| Team IDs | `teamIds` | string |  | Team IDs. Only results related to these teams will be returned. Account must have the teams ability to use this parameter. (multiples IDs can be added separated by comma) |
| Timezone Name or ID | `timeZone` | options |  | Time zone in which dates in the result will be rendered. If not set dates will return UTC. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Until | `until` | dateTime |  | The end of the date range over which you want to search. (the limit on date ranges is 6 months). |
| Urgencies | `urgencies` | multiOptions | [] | Urgencies of the incidents to be returned. Defaults to all urgencies. Account must have the urgencies ability to do this |
| User IDs | `userIds` | string |  | Returns only the incidents currently assigned to the passed user(s). This expects one or more user IDs (multiple IDs can be added separated by comma). |

</details>

| Incident ID | `incidentId` | string |  | ✓ | Unique identifier for the incident |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Additional details to include | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | multiOptions | [] | Additional details to include |
| Is Overview | `isOverview` | boolean | False | Whether to return a subset of log entries that show only the most important changes to the incident |
| Since | `since` | dateTime |  | The start of the date range over which you want to search. (the limit on date ranges is 6 months). |
| Timezone Name or ID | `timeZone` | options |  | Time zone in which dates in the result will be rendered. If not set dates will return UTC. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Until | `until` | dateTime |  | The end of the date range over which you want to search. (the limit on date ranges is 6 months). |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Incident ID | `incidentId` | string |  | ✓ | Unique identifier for the incident |  |
| Email | `email` | string |  | ✓ | The email address of a valid user associated with the account making the request | e.g. name@email.com | email |
| Update Fields | `updateFields` | collection | {} | ✗ | Escalate the incident to this level in the escalation policy | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Escalation Level | `escalationLevel` | number | 0 | Escalate the incident to this level in the escalation policy |
| Escalation Policy Name or ID | `escalationPolicyId` | options |  | Delegate this incident to the specified escalation policy. Cannot be specified if an assignee is given. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Priority Name or ID | `priorityId` | options |  | The incident will be created on this service. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Resolution | `resolution` | string |  | The resolution for this incident if status is set to resolved |
| Status | `status` | options |  | The new status of the incident |
| Title | `title` | string |  | A succinct description of the nature, symptoms, cause, or effect of the incident |
| Urgency | `urgency` | options |  | The urgency of the incident |

</details>

| Conference Bridge | `conferenceBridgeUi` | fixedCollection | {} | ✗ | Phone numbers should be formatted like +1 415-555-1212,,,,1234#, where a comma (,) represents a one-second wait and pound (#) completes access code input | e.g. Add Conference Bridge |  |

<details>
<summary><strong>Conference Bridge sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conference Bridge | `conferenceBridgeValues` |  |  |  |

</details>


---

## Load Options Methods

- `getEscalationPolicies`
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
* Categories: Communication, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: pagerDuty
displayName: PagerDuty
description: Consume PagerDuty API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: pagerDutyApi
  required: true
- name: pagerDutyOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create an incident
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: A succinct description of the nature, symptoms, cause, or effect
      of the incident
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - incident
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: serviceId
    name: Service Name or ID
    type: options
    default: ''
    required: true
    description: The incident will be created on this service. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - incident
          operation:
          - create
    typeInfo:
      type: options
      displayName: Service Name or ID
      name: serviceId
      typeOptions:
        loadOptionsMethod: getServices
      possibleValues: []
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email address of a valid user associated with the account making
      the request
    placeholder: name@email.com
    validation: &id001
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - incidentNote
          operation:
          - create
    typeInfo: &id002
      type: string
      displayName: Email
      name: email
  - id: conferenceBridgeUi
    name: Conference Bridge
    type: fixedCollection
    default: {}
    required: false
    description: Phone numbers should be formatted like +1 415-555-1212,,,,1234#,
      where a comma (,) represents a one-second wait and pound (#) completes access
      code input
    placeholder: Add Conference Bridge
    validation: &id009
      displayOptions:
        show:
          resource:
          - incident
          operation:
          - update
    typeInfo: &id010
      type: fixedCollection
      displayName: Conference Bridge
      name: conferenceBridgeUi
      typeOptions:
        multipleValues: false
      subProperties:
      - name: conferenceBridgeValues
        displayName: Conference Bridge
        values:
        - displayName: Conference Number
          name: conferenceNumber
          type: string
          description: Phone numbers should be formatted like +1 415-555-1212,,,,1234#,
            where a comma (,) represents a one-second wait and pound (#) completes
            access code input
          default: ''
        - displayName: Conference URL
          name: conferenceUrl
          type: string
          description: An URL for the conference bridge. This could be a link to a
            web conference or Slack channel.
          default: ''
  - id: incidentId
    name: Incident ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the incident
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - incidentNote
          operation:
          - getAll
    typeInfo: &id004
      type: string
      displayName: Incident ID
      name: incidentId
  - id: content
    name: Content
    type: string
    default: ''
    required: true
    description: The note content
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - incidentNote
          operation:
          - create
    typeInfo:
      type: string
      displayName: Content
      name: content
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email address of a valid user associated with the account making
      the request
    placeholder: name@email.com
    validation: *id001
    typeInfo: *id002
- id: get
  name: Get
  description: Get an incident
  params:
  - id: incidentId
    name: Incident ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the incident
    validation: *id003
    typeInfo: *id004
  - id: logEntryId
    name: Log Entry ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the log entry
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - logEntry
          operation:
          - get
    typeInfo:
      type: string
      displayName: Log Entry ID
      name: logEntryId
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the user
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
    typeInfo:
      type: string
      displayName: User ID
      name: userId
- id: getAll
  name: Get Many
  description: Get many incidents
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id005
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - logEntry
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - logEntry
          returnAll:
          - false
    typeInfo: &id008
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: incidentId
    name: Incident ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the incident
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: update
  name: Update
  description: Update an incident
  params:
  - id: incidentId
    name: Incident ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the incident
    validation: *id003
    typeInfo: *id004
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email address of a valid user associated with the account making
      the request
    placeholder: name@email.com
    validation: *id001
    typeInfo: *id002
  - id: conferenceBridgeUi
    name: Conference Bridge
    type: fixedCollection
    default: {}
    required: false
    description: Phone numbers should be formatted like +1 415-555-1212,,,,1234#,
      where a comma (,) represents a one-second wait and pound (#) completes access
      code input
    placeholder: Add Conference Bridge
    validation: *id009
    typeInfo: *id010
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
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: conferenceBridgeUi
    text: Add Conference Bridge
  - field: options
    text: Add Field
  - field: email
    text: name@email.com
  - field: updateFields
    text: Add Field
  - field: conferenceBridgeUi
    text: Add Conference Bridge
  - field: email
    text: name@email.com
  - field: options
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
  "$id": "https://n8n.io/schemas/nodes/pagerDuty.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "PagerDuty Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
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
            "apiToken",
            "oAuth2"
          ],
          "default": "apiToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "incident",
            "incidentNote",
            "logEntry",
            "user"
          ],
          "default": "incident"
        },
        "operation": {
          "description": "Get a user",
          "type": "string",
          "enum": [
            "get"
          ],
          "default": "get"
        },
        "title": {
          "description": "A succinct description of the nature, symptoms, cause, or effect of the incident",
          "type": "string",
          "default": ""
        },
        "serviceId": {
          "description": "The incident will be created on this service. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "The email address of a valid user associated with the account making the request",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "additionalFields": {
          "description": "Delegate this incident to the specified escalation policy. Cannot be specified if an assignee is given. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "conferenceBridgeUi": {
          "description": "Phone numbers should be formatted like +1 415-555-1212,,,,1234#, where a comma (,) represents a one-second wait and pound (#) completes access code input",
          "type": "string",
          "default": {},
          "examples": [
            "Add Conference Bridge"
          ]
        },
        "incidentId": {
          "description": "Unique identifier for the incident",
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
        "options": {
          "description": "Additional details to include",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "Escalate the incident to this level in the escalation policy",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "content": {
          "description": "The note content",
          "type": "string",
          "default": ""
        },
        "logEntryId": {
          "description": "Unique identifier for the log entry",
          "type": "string",
          "default": ""
        },
        "userId": {
          "description": "Unique identifier for the user",
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
      "name": "pagerDutyApi",
      "required": true
    },
    {
      "name": "pagerDutyOAuth2Api",
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
