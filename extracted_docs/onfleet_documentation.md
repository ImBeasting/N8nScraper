---
title: "Node: Onfleet"
slug: "node-onfleet"
version: "1"
updated: "2026-01-08"
summary: "Consume Onfleet API"
node_type: "regular"
group: "['input']"
---

# Node: Onfleet

**Purpose.** Consume Onfleet API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:Onfleet.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **onfleetApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `onfleetApi` | ✓ | - |

---

## API Patterns

**Headers Used:** User-Agent, Content-Type

---

## Operations

### Admin Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new Onfleet admin |
| Delete | `delete` | Delete an Onfleet admin |
| Get Many | `getAll` | Get many Onfleet admins |
| Update | `update` | Update an Onfleet admin |

### Container Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Tasks | `addTask` | Add task at index (or append) |
| Get | `get` | Get container information |
| Update Tasks | `updateTask` | Fully replace a container's tasks |

### Destination Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new destination |
| Get | `get` | Get a specific destination |

### Hub Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new Onfleet hub |
| Get Many | `getAll` | Get many Onfleet hubs |
| Update | `update` | Update an Onfleet hub |

### Organization Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get My Organization | `get` | Retrieve your own organization's details |
| Get Delegatee Details | `getDelegatee` | Retrieve the details of an organization with which you are connected |

### Recipient Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new Onfleet recipient |
| Get | `get` | Get a specific Onfleet recipient |
| Update | `update` | Update an Onfleet recipient |

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Clone | `clone` | Clone an Onfleet task |
| Complete | `complete` | Force-complete a started Onfleet task |
| Create | `create` | Create a new Onfleet task |
| Delete | `delete` | Delete an Onfleet task |
| Get | `get` | Get a specific Onfleet task |
| Get Many | `getAll` | Get many Onfleet tasks |
| Update | `update` | Update an Onfleet task |

### Team Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Auto-Dispatch | `autoDispatch` | Automatically dispatch tasks assigned to a team to on-duty drivers |
| Create | `create` | Create a new Onfleet team |
| Delete | `delete` | Delete an Onfleet team |
| Get | `get` | Get a specific Onfleet team |
| Get Many | `getAll` | Get many Onfleet teams |
| Get Time Estimates | `getTimeEstimates` | Get estimated times for upcoming tasks for a team, returns a selected driver |
| Update | `update` | Update an Onfleet team |

### Worker Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new Onfleet worker |
| Delete | `delete` | Delete an Onfleet worker |
| Get | `get` | Get a specific Onfleet worker |
| Get Many | `getAll` | Get many Onfleet workers |
| Get Schedule | `getSchedule` | Get a specific Onfleet worker schedule |
| Set Worker's Schedule | `setSchedule` | Set the worker's schedule |
| Update | `update` | Update an Onfleet worker |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | task | ✗ | The resource to perform operations on |  |

**Resource options:**

* **Admin** (`admin`)
* **Container** (`container`)
* **Destination** (`destination`)
* **Hub** (`hub`)
* **Organization** (`organization`)
* **Recipient** (`recipient`)
* **Task** (`task`)
* **Team** (`team`)
* **Webhook** (`webhook`)
* **Worker** (`worker`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Create a new Onfleet admin |  |

**Operation options:**

* **Create** (`create`) - Create a new Onfleet admin
* **Delete** (`delete`) - Delete an Onfleet admin
* **Get Many** (`getAll`) - Get many Onfleet admins
* **Update** (`update`) - Update an Onfleet admin

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Options | `options` | collection | {} | ✗ | Whether to skip validation for this recipient's phone number | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Skip Recipient Phone Number Validation | `recipientSkipPhoneNumberValidation` | boolean | False | Whether to skip validation for this recipient's phone number |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Override the recipient name for this task only | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Recipient Name Override | `recipientName` | string |  | Override the recipient name for this task only |
| Recipient Notes Override | `recipientNotes` | string |  | Override the recipient notes for this task only |
| Recipient Skip SMS Notifications Override | `recipientSkipSMSNotifications` | boolean | False | Whether to override the recipient notification settings for this task |
| Use Merchant For Proxy Override | `useMerchantForProxy` | boolean | False | Whether to override the organization ID with the merchant's org ID for this task |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Vehicle | `vehicle` | fixedCollection | {} |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team ID | `id` | string |  | ✓ | The ID of the team object for lookup |  |
| Worker ID | `id` | string |  | ✓ | The ID of the worker object for lookup |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 64 | ✗ | Max number of results to return | min:1, max:64 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 64 | ✗ | Max number of results to return | min:1, max:64 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 64 | ✗ | Max number of results to return | min:1, max:64 |
| Filters | `filters` | collection | {} | ✗ | The starting time of the range. Tasks created or completed at or after this time will be included. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| From | `from` | dateTime |  | The starting time of the range. Tasks created or completed at or after this time will be included. |
| State | `state` | multiOptions |  | The state of the tasks |
| To | `to` | dateTime |  | The ending time of the range. Defaults to current time if not specified. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 64 | ✗ | Max number of results to return | min:1, max:64 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 64 | ✗ | Max number of results to return | min:1, max:64 |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Field |  |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Field |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |
| Hub ID | `id` | string |  | ✓ | The ID of the hub object for lookup |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |
| Recipient ID | `id` | string |  | ✓ | The ID of the recipient object for lookup |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Update Fields |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |
| Team ID | `id` | string |  | ✓ | The ID of the team object for lookup |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |
| Worker ID | `id` | string |  | ✓ | The ID of the worker object for lookup |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |

### Add Tasks parameters (`addTask`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Options | `options` | collection | {} | ✗ | e.g. Add option |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Get By | `getBy` | options | id | ✓ | The variable that is used for looking up a recipient |  |

**Get By options:**

* **ID** (`id`)
* **Phone** (`phone`)
* **Name** (`name`)

| Recipient ID | `id` | string |  | ✓ | The ID of the recipient object for lookup |  |
| Name | `name` | string |  | ✓ | The name of the recipient for lookup |  |
| Phone | `phone` | string |  | ✓ | The phone of the recipient for lookup |  |
| Team ID | `id` | string |  | ✓ | The ID of the team object for lookup |  |
| Worker ID | `id` | string |  | ✓ | The ID of the worker object for lookup |  |
| Options | `options` | collection | {} | ✗ | Whether a more detailed response is needed, includes basic worker duty event, traveled distance (meters) and time analytics | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Analytics | `analytics` | boolean | True | Whether a more detailed response is needed, includes basic worker duty event, traveled distance (meters) and time analytics |

</details>


### Update Tasks parameters (`updateTask`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Options | `options` | collection | {} | ✗ | e.g. Add option |  |

### Get Delegatee Details parameters (`getDelegatee`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Organization ID | `id` | string |  | ✓ | The ID of the delegatees for lookup |  |

### Clone parameters (`clone`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Override Fields | `overrideFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Override Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Barcodes | `includeBarcodes` | boolean | False |  |
| Include Dependencies | `includeDependencies` | boolean | False |  |
| Include Metadata | `includeMetadata` | boolean | False |  |

</details>


### Complete parameters (`complete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Complete as a Success | `success` | boolean | True | ✓ | Whether the task's completion was successful |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Completion Notes | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Completion Notes |

</details>


### Auto-Dispatch parameters (`autoDispatch`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team ID | `id` | string |  | ✓ | The ID of the team object for lookup |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Ending Route | `endingRoute` | fixedCollection | {} |  |
| Schedule Time Window | `scheduleTimeWindow` | fixedCollection | {} |  |
| Task Time Window | `taskTimeWindow` | fixedCollection | {} |  |

</details>


### Get Time Estimates parameters (`getTimeEstimates`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team ID | `id` | string |  | ✓ | The ID of the team object for lookup |  |
| Filters | `filters` | collection | {} | ✓ | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Drop Off | `dropOff` | fixedCollection | {} |  |
| Pick Up | `pickUp` | fixedCollection | {} |  |

</details>


### Get Schedule parameters (`getSchedule`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Worker ID | `id` | string |  | ✓ | The ID of the worker object for lookup |  |

### Set Worker's Schedule parameters (`setSchedule`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Worker ID | `id` | string |  | ✓ | The ID of the worker object for lookup |  |
| Schedule | `schedule` | fixedCollection | {} | ✓ | e.g. Add Schedule |  |

<details>
<summary><strong>Schedule sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Schedule Properties | `scheduleProperties` |  |  |  |

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
* Categories: Miscellaneous

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: onfleet
displayName: Onfleet
description: Consume Onfleet API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: onfleetApi
  required: true
operations:
- id: create
  name: Create
  description: Create a new Onfleet admin
  params: []
- id: delete
  name: Delete
  description: Delete an Onfleet admin
  params:
  - id: id
    name: Team ID
    type: string
    default: ''
    required: true
    description: The ID of the team object for lookup
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - worker
          operation:
          - get
          - getSchedule
          - setSchedule
          - update
          - delete
    typeInfo: &id002
      type: string
      displayName: Worker ID
      name: id
  - id: id
    name: Worker ID
    type: string
    default: ''
    required: true
    description: The ID of the worker object for lookup
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many Onfleet admins
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id003
      displayOptions:
        show:
          resource:
          - worker
          operation:
          - getAll
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 64
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          resource:
          - worker
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 64
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 64
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 64
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 64
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 64
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: update
  name: Update
  description: Update an Onfleet admin
  params:
  - id: id
    name: Hub ID
    type: string
    default: ''
    required: true
    description: The ID of the hub object for lookup
    validation: *id001
    typeInfo: *id002
  - id: id
    name: Recipient ID
    type: string
    default: ''
    required: true
    description: The ID of the recipient object for lookup
    validation: *id001
    typeInfo: *id002
  - id: id
    name: Team ID
    type: string
    default: ''
    required: true
    description: The ID of the team object for lookup
    validation: *id001
    typeInfo: *id002
  - id: id
    name: Worker ID
    type: string
    default: ''
    required: true
    description: The ID of the worker object for lookup
    validation: *id001
    typeInfo: *id002
- id: addTask
  name: Add Tasks
  description: Add task at index (or append)
  params: []
- id: get
  name: Get
  description: Get container information
  params:
  - id: getBy
    name: Get By
    type: options
    default: id
    required: true
    description: The variable that is used for looking up a recipient
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - recipient
          operation:
          - get
    typeInfo:
      type: options
      displayName: Get By
      name: getBy
      possibleValues:
      - value: id
        name: ID
        description: ''
      - value: phone
        name: Phone
        description: ''
      - value: name
        name: Name
        description: ''
  - id: id
    name: Recipient ID
    type: string
    default: ''
    required: true
    description: The ID of the recipient object for lookup
    validation: *id001
    typeInfo: *id002
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the recipient for lookup
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - recipient
          operation:
          - get
          getBy:
          - name
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: phone
    name: Phone
    type: string
    default: ''
    required: true
    description: The phone of the recipient for lookup
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - recipient
          operation:
          - get
          getBy:
          - phone
    typeInfo:
      type: string
      displayName: Phone
      name: phone
  - id: id
    name: Team ID
    type: string
    default: ''
    required: true
    description: The ID of the team object for lookup
    validation: *id001
    typeInfo: *id002
  - id: id
    name: Worker ID
    type: string
    default: ''
    required: true
    description: The ID of the worker object for lookup
    validation: *id001
    typeInfo: *id002
- id: updateTask
  name: Update Tasks
  description: Fully replace a container's tasks
  params: []
- id: getDelegatee
  name: Get Delegatee Details
  description: Retrieve the details of an organization with which you are connected
  params:
  - id: id
    name: Organization ID
    type: string
    default: ''
    required: true
    description: The ID of the delegatees for lookup
    validation: *id001
    typeInfo: *id002
- id: clone
  name: Clone
  description: Clone an Onfleet task
  params: []
- id: complete
  name: Complete
  description: Force-complete a started Onfleet task
  params:
  - id: success
    name: Complete as a Success
    type: boolean
    default: true
    required: true
    description: Whether the task's completion was successful
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - complete
    typeInfo:
      type: boolean
      displayName: Complete as a Success
      name: success
- id: autoDispatch
  name: Auto-Dispatch
  description: Automatically dispatch tasks assigned to a team to on-duty drivers
  params:
  - id: id
    name: Team ID
    type: string
    default: ''
    required: true
    description: The ID of the team object for lookup
    validation: *id001
    typeInfo: *id002
- id: getTimeEstimates
  name: Get Time Estimates
  description: Get estimated times for upcoming tasks for a team, returns a selected
    driver
  params:
  - id: id
    name: Team ID
    type: string
    default: ''
    required: true
    description: The ID of the team object for lookup
    validation: *id001
    typeInfo: *id002
- id: getSchedule
  name: Get Schedule
  description: Get a specific Onfleet worker schedule
  params:
  - id: id
    name: Worker ID
    type: string
    default: ''
    required: true
    description: The ID of the worker object for lookup
    validation: *id001
    typeInfo: *id002
- id: setSchedule
  name: Set Worker's Schedule
  description: Set the worker's schedule
  params:
  - id: id
    name: Worker ID
    type: string
    default: ''
    required: true
    description: The ID of the worker object for lookup
    validation: *id001
    typeInfo: *id002
  - id: schedule
    name: Schedule
    type: fixedCollection
    default: {}
    required: true
    description: ''
    placeholder: Add Schedule
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - worker
          operation:
          - setSchedule
    typeInfo:
      type: fixedCollection
      displayName: Schedule
      name: schedule
      typeOptions:
        multipleValues: true
      subProperties:
      - name: scheduleProperties
        displayName: Schedule Properties
        values:
        - displayName: Shifts
          name: shifts
          type: fixedCollection
          placeholder: Add Shift
          default: {}
          required: true
          options:
          - name: shiftsProperties
            displayName: Shifts Properties
            values: []
          typeOptions:
            multipleValues: true
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - User-Agent
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: destination
    text: Add Destination
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Update Fields
  - field: options
    text: Add Field
  - field: filters
    text: Add Filter
  - field: overrideFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: filters
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: schedule
    text: Add Schedule
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
  "$id": "https://n8n.io/schemas/nodes/onfleet.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Onfleet Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "getAll",
        "update",
        "addTask",
        "get",
        "updateTask",
        "getDelegatee",
        "clone",
        "complete",
        "autoDispatch",
        "getTimeEstimates",
        "getSchedule",
        "setSchedule"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "The resource to perform operations on",
          "type": "string",
          "enum": [
            "admin",
            "container",
            "destination",
            "hub",
            "organization",
            "recipient",
            "task",
            "team",
            "webhook",
            "worker"
          ],
          "default": "task"
        },
        "operation": {
          "description": "Create a new Onfleet worker",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "getSchedule",
            "setSchedule",
            "update"
          ],
          "default": "get"
        },
        "id": {
          "description": "The ID of the worker object for lookup",
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
          "default": 64
        },
        "additionalFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "options": {
          "description": "Whether a more detailed response is needed, includes basic worker duty event, traveled distance (meters) and time analytics",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "destination": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Destination"
          ]
        },
        "getBy": {
          "description": "The variable that is used for looking up a recipient",
          "type": "string",
          "enum": [
            "id",
            "phone",
            "name"
          ],
          "default": "id"
        },
        "name": {
          "description": "The name of the recipient for lookup",
          "type": "string",
          "default": ""
        },
        "phone": {
          "description": "The phone of the recipient for lookup",
          "type": "string",
          "default": ""
        },
        "success": {
          "description": "Whether the task's completion was successful",
          "type": "boolean",
          "default": true
        },
        "filters": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "overrideFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "schedule": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Schedule"
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
      "name": "onfleetApi",
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
