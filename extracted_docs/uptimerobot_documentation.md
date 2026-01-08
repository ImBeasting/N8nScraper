---
title: "Node: UptimeRobot"
slug: "node-uptimerobot"
version: "1"
updated: "2026-01-08"
summary: "Consume UptimeRobot API"
node_type: "regular"
group: "['output']"
---

# Node: UptimeRobot

**Purpose.** Consume UptimeRobot API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:uptimerobot.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **uptimeRobotApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `uptimeRobotApi` | ✓ | - |

---

## Operations

### Account Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get account details |

### Monitor Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a monitor |
| Delete | `delete` | Delete a monitor |
| Get | `get` | Get a monitor |
| Get Many | `getAll` | Get many monitors |
| Reset | `reset` | Reset a monitor |
| Update | `update` | Update a monitor |

### Alertcontact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an alert contact |
| Delete | `delete` | Delete an alert contact |
| Get | `get` | Get an alert contact |
| Get Many | `getAll` | Get many alert contacts |
| Update | `update` | Update an alert contact |

### Maintenancewindow Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a maintenance window |
| Delete | `delete` | Delete a maintenance window |
| Get | `get` | Get a maintenance window |
| Get Many | `getAll` | Get many a maintenance windows |
| Update | `update` | Update a maintenance window |

### Publicstatuspage Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a public status page |
| Delete | `delete` | Delete a public status page |
| Get | `get` | Get a public status page |
| Get Many | `getAll` | Get many public status pages |
| Update | `update` | Update a public status page |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | account | ✗ | Resource to operate on |  |

**Resource options:**

* **Account** (`account`)
* **Alert Contact** (`alertContact`)
* **Maintenance Window** (`maintenanceWindow`)
* **Monitor** (`monitor`)
* **Public Status Page** (`publicStatusPage`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Get account details |  |

**Operation options:**

* **Get** (`get`) - Get account details

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The ID of the monitor |  |
| ID | `id` | string |  | ✓ | The ID of the alert contact |  |
| ID | `id` | string |  | ✓ | The ID of the maintenance window |  |
| ID | `id` | string |  | ✓ | The ID of the public status page |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Friendly Name | `friendlyName` | string |  | ✓ | The friendly name of the monitor |  |
| Type | `type` | options |  | ✓ | The type of the monitor |  |

**Type options:**

* **Heartbeat** (``)
* **HTTP(S)** (``)
* **Keyword** (``)
* **Ping** (``)
* **Port** (``)

| URL | `url` | string |  | ✓ | The URL/IP of the monitor | url |
| Friendly Name | `friendlyName` | string |  | ✓ | The friendly name of the alert contact |  |
| Type | `type` | options |  | ✓ | The type of the alert contact |  |

**Type options:**

* **Boxcar** (``)
* **E-Mail** (``)
* **Pushbullet** (``)
* **Pushover** (``)
* **SMS** (``)
* **Twitter DM** (``)
* **Webhook** (``)
* **HipChat** (``)
* **Slack** (``)
* **Zapier** (``)

| Value | `value` | string |  | ✓ | The correspondent value for the alert contact type |  |
| Duration (Minutes) | `duration` | number | 1 | ✓ | The maintenance window activation period (minutes) |  |
| Friendly Name | `friendlyName` | string |  | ✓ | The friendly name of the maintenance window |  |
| Type | `type` | options |  | ✓ | The type of the maintenance window |  |

**Type options:**

* **Once** (``)
* **Daily** (``)
* **Weekly** (``)
* **Monthly** (``)

| Week Day | `weekDay` | options |  | ✗ |  |  |

**Week Day options:**

* **Monday** (``)
* **Tuesday** (``)
* **Wednesday** (``)
* **Thursday** (``)
* **Friday** (``)
* **Saturday** (``)
* **Sunday** (``)

| Month Day | `monthDay` | number | 1 | ✗ |  | min:1, max:30 |
| Start Time | `start_time` | dateTime |  | ✓ | The maintenance window start datetime |  |
| Friendly Name | `friendlyName` | string |  | ✓ | The friendly name of the status page |  |
| Monitor IDs | `monitors` | string |  | ✓ | Monitor IDs to be displayed in status page (the values are separated with a dash (-) or 0 for all monitors) |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The domain or subdomain that the status page will run on | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Domain | `custom_domain` | string |  | The domain or subdomain that the status page will run on |
| Password | `password` | string |  | The password for the status page |
| Sort | `sort` | options |  | The sorting of the status page |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The ID of the monitor |  |
| ID | `id` | string |  | ✓ | The ID of the alert contact |  |
| ID | `id` | string |  | ✓ | The ID of the maintenance window |  |
| ID | `id` | string |  | ✓ | The ID of the public status page |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Whether the alert contacts set for the monitor to be returned | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Alert Contacts | `alert_contacts` | boolean | False | Whether the alert contacts set for the monitor to be returned |
| Logs | `logs` | boolean | False | Whether the logs of each monitor will be returned |
| Maintenance Window | `mwindow` | boolean | False | Whether to return the maintenance windows for the monitors |
| Monitor IDs | `monitors` | string |  | Monitors IDs separated with dash, e.g. 15830-32696-83920 |
| Response Times | `response_times` | boolean | False | Whether the response time data of each monitor will be returned |
| Search | `search` | string |  | A keyword to be matched against URL and friendly name |
| Statuses | `statuses` | multiOptions | [] |  |
| Types | `types` | multiOptions | [] | Select monitor types |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Alert contact IDs separated with dash, e.g. 236-1782-4790 | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Alert Contact IDs | `alert_contacts` | string |  | Alert contact IDs separated with dash, e.g. 236-1782-4790 |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Maintenance windows IDs separated with dash, e.g. 236-1782-4790 | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Maintenance Window IDs | `mwindow` | string |  | Maintenance windows IDs separated with dash, e.g. 236-1782-4790 |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Public status pages IDs separated with dash, e.g. 236-1782-4790 | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Public Status Page IDs | `psps` | string |  | Public status pages IDs separated with dash, e.g. 236-1782-4790 |

</details>


### Reset parameters (`reset`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The ID of the monitor |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The ID of the monitor |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The friendly name of the monitor | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Friendly Name | `friendly_name` | string |  | The friendly name of the monitor |
| HTTP Auth Type | `http_auth_type` | options |  | The authentication type for password-protected web pages |
| HTTP Method | `http_method` | options |  | The HTTP method to be used |
| HTTP Password | `http_password` | string |  | The password used for password-protected web pages |
| HTTP Username | `http_username` | string |  | The username used for password-protected web pages |
| Interval | `interval` | number |  | The interval for the monitoring check |
| Port | `port` | number |  | The monitored port |
| Status | `status` | options |  | Select monitor statuses |
| Sub Type | `sub_type` | options |  | Specify which pre-defined port/service or custom port is monitored |
| URL | `url` | string |  | The URL/IP of the monitor |

</details>

| ID | `id` | string |  | ✓ | The ID of the alert contact |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The friendly name of the alert contact | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Friendly Name | `friendly_name` | string |  | The friendly name of the alert contact |
| Value | `value` | string |  | The correspondent value for the alert contact type (can only be used if it is a Webhook alert contact) |

</details>

| ID | `id` | string |  | ✓ | The ID of the maintenance window |  |
| Duration (Minutes) | `duration` | number |  | ✓ | The maintenance window activation period (minutes) |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The friendly name of the maintenance window | e.g. Add Field | min:1, max:30 |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Friendly Name | `friendly_name` | string |  | The friendly name of the maintenance window |
| Start Time | `start_time` | dateTime |  | The maintenance window start datetime |
| Type | `type` | options |  | The type of the maintenance window |
| Week Day | `weekDay` | options |  |  |
| Month Day | `monthDay` | number | 1 |  |

</details>

| ID | `id` | string |  | ✓ | The ID of the public status page |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The domain or subdomain that the status page will run on | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Domain | `custom_domain` | string |  | The domain or subdomain that the status page will run on |
| Friendly Name | `friendly_name` | string |  | The friendly name of the status page |
| Monitor IDs | `monitors` | string |  | Monitor IDs to be displayed in status page (the values are separated with a dash (-) or 0 for all monitors) |
| Password | `password` | string |  | The password for the status page |
| Sort | `sort` | options |  | The sorting of the status page |

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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: uptimeRobot
displayName: UptimeRobot
description: Consume UptimeRobot API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: uptimeRobotApi
  required: true
operations:
- id: get
  name: Get
  description: Get account details
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the monitor
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - publicStatusPage
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: ID
      name: id
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the alert contact
    validation: *id001
    typeInfo: *id002
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the maintenance window
    validation: *id001
    typeInfo: *id002
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the public status page
    validation: *id001
    typeInfo: *id002
- id: create
  name: Create
  description: Create a monitor
  params:
  - id: friendlyName
    name: Friendly Name
    type: string
    default: ''
    required: true
    description: The friendly name of the monitor
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - publicStatusPage
          operation:
          - create
    typeInfo: &id004
      type: string
      displayName: Friendly Name
      name: friendlyName
  - id: type
    name: Type
    type: options
    default: ''
    required: true
    description: The type of the monitor
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - maintenanceWindow
          operation:
          - create
    typeInfo: &id006
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: Once
        name: Once
        description: ''
      - value: Daily
        name: Daily
        description: ''
      - value: Weekly
        name: Weekly
        description: ''
      - value: Monthly
        name: Monthly
        description: ''
  - id: url
    name: URL
    type: string
    default: ''
    required: true
    description: The URL/IP of the monitor
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - monitor
          operation:
          - create
    typeInfo:
      type: string
      displayName: URL
      name: url
  - id: friendlyName
    name: Friendly Name
    type: string
    default: ''
    required: true
    description: The friendly name of the alert contact
    validation: *id003
    typeInfo: *id004
  - id: type
    name: Type
    type: options
    default: ''
    required: true
    description: The type of the alert contact
    validation: *id005
    typeInfo: *id006
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: The correspondent value for the alert contact type
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - alertContact
          operation:
          - create
    typeInfo:
      type: string
      displayName: Value
      name: value
  - id: duration
    name: Duration (Minutes)
    type: number
    default: 1
    required: true
    description: The maintenance window activation period (minutes)
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - maintenanceWindow
          operation:
          - update
    typeInfo: &id012
      type: number
      displayName: Duration (Minutes)
      name: duration
  - id: friendlyName
    name: Friendly Name
    type: string
    default: ''
    required: true
    description: The friendly name of the maintenance window
    validation: *id003
    typeInfo: *id004
  - id: type
    name: Type
    type: options
    default: ''
    required: true
    description: The type of the maintenance window
    validation: *id005
    typeInfo: *id006
  - id: weekDay
    name: Week Day
    type: options
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - maintenanceWindow
          operation:
          - create
          type:
          - 3
    typeInfo:
      type: options
      displayName: Week Day
      name: weekDay
      possibleValues:
      - value: Monday
        name: Monday
        description: ''
      - value: Tuesday
        name: Tuesday
        description: ''
      - value: Wednesday
        name: Wednesday
        description: ''
      - value: Thursday
        name: Thursday
        description: ''
      - value: Friday
        name: Friday
        description: ''
      - value: Saturday
        name: Saturday
        description: ''
      - value: Sunday
        name: Sunday
        description: ''
  - id: monthDay
    name: Month Day
    type: number
    default: 1
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - maintenanceWindow
          operation:
          - create
          type:
          - 4
    typeInfo:
      type: number
      displayName: Month Day
      name: monthDay
      typeOptions:
        minValue: 1
        maxValue: 30
  - id: start_time
    name: Start Time
    type: dateTime
    default: ''
    required: true
    description: The maintenance window start datetime
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - maintenanceWindow
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: Start Time
      name: start_time
  - id: friendlyName
    name: Friendly Name
    type: string
    default: ''
    required: true
    description: The friendly name of the status page
    validation: *id003
    typeInfo: *id004
  - id: monitors
    name: Monitor IDs
    type: string
    default: ''
    required: true
    description: Monitor IDs to be displayed in status page (the values are separated
      with a dash (-) or 0 for all monitors)
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - publicStatusPage
          operation:
          - create
    typeInfo:
      type: string
      displayName: Monitor IDs
      name: monitors
- id: delete
  name: Delete
  description: Delete a monitor
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the monitor
    validation: *id001
    typeInfo: *id002
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the alert contact
    validation: *id001
    typeInfo: *id002
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the maintenance window
    validation: *id001
    typeInfo: *id002
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the public status page
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many monitors
  params:
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
          - publicStatusPage
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
          - publicStatusPage
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
        maxValue: 100
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
- id: reset
  name: Reset
  description: Reset a monitor
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the monitor
    validation: *id001
    typeInfo: *id002
- id: update
  name: Update
  description: Update a monitor
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the monitor
    validation: *id001
    typeInfo: *id002
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the alert contact
    validation: *id001
    typeInfo: *id002
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the maintenance window
    validation: *id001
    typeInfo: *id002
  - id: duration
    name: Duration (Minutes)
    type: number
    default: ''
    required: true
    description: The maintenance window activation period (minutes)
    validation: *id011
    typeInfo: *id012
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The ID of the public status page
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
  - field: filters
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
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
  "$id": "https://n8n.io/schemas/nodes/uptimeRobot.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "UptimeRobot Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "create",
        "delete",
        "getAll",
        "reset",
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
            "account",
            "alertContact",
            "maintenanceWindow",
            "monitor",
            "publicStatusPage"
          ],
          "default": "account"
        },
        "operation": {
          "description": "Create a public status page",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "getAll"
        },
        "friendlyName": {
          "description": "The friendly name of the status page",
          "type": "string",
          "default": ""
        },
        "type": {
          "description": "The type of the maintenance window",
          "type": "string",
          "enum": [
            "Once",
            "Daily",
            "Weekly",
            "Monthly"
          ],
          "default": ""
        },
        "url": {
          "description": "The URL/IP of the monitor",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "id": {
          "description": "The ID of the public status page",
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
          "description": "Public status pages IDs separated with dash, e.g. 236-1782-4790",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "The domain or subdomain that the status page will run on",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "value": {
          "description": "The correspondent value for the alert contact type",
          "type": "string",
          "default": ""
        },
        "duration": {
          "description": "The maintenance window activation period (minutes)",
          "type": "number",
          "default": ""
        },
        "weekDay": {
          "description": "",
          "type": "string",
          "enum": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "default": ""
        },
        "monthDay": {
          "description": "",
          "type": "number",
          "default": 1
        },
        "start_time": {
          "description": "The maintenance window start datetime",
          "type": "string",
          "default": ""
        },
        "monitors": {
          "description": "Monitor IDs to be displayed in status page (the values are separated with a dash (-) or 0 for all monitors)",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The domain or subdomain that the status page will run on",
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
      "name": "uptimeRobotApi",
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
