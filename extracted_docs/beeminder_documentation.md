---
title: "Node: Beeminder"
slug: "node-beeminder"
version: "1"
updated: "2026-01-08"
summary: "Consume Beeminder API"
node_type: "regular"
group: "['output']"
---

# Node: Beeminder

**Purpose.** Consume Beeminder API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:beeminder.png`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **beeminderApi**: N/A
- **beeminderOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `beeminderApi` | ✓ | {'show': {'authentication': ['apiToken']}} |
| `beeminderOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Charge Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a charge |

### Datapoint Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create datapoint for goal |
| Create All | `createAll` | Create multiple datapoints at once |
| Delete | `delete` | Delete a datapoint |
| Get | `get` | Get a single datapoint |
| Get Many | `getAll` | Get many datapoints for a goal |
| Update | `update` | Update a datapoint |

### Goal Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new goal |
| Get | `get` | Get a specific goal |
| Get Many | `getAll` | Get many goals |
| Get Archived | `getArchived` | Get archived goals |
| Update | `update` | Update a goal |
| Refresh | `refresh` | Refresh goal data |
| Short Circuit | `shortCircuit` | Short circuit pledge |
| Step Down | `stepDown` | Step down pledge |
| Cancel Step Down | `cancelStepDown` | Cancel step down |
| Uncle | `uncle` | Derail a goal and charge the pledge amount |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get user information |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | datapoint | ✓ | Resource to operate on |  |

**Resource options:**

* **Charge** (`charge`)
* **Datapoint** (`datapoint`)
* **Goal** (`goal`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✓ | Create a charge |  |

**Operation options:**

* **Create** (`create`) - Create a charge

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Amount | `amount` | number | 0 | ✓ | Charge amount in USD |  |
| Goal Slug | `slug` | string |  | ✓ | Unique identifier for the goal |  |
| Goal Title | `title` | string |  | ✓ | Human-readable title for the goal |  |
| Goal Type | `goal_type` | options | hustler | ✓ | Type of goal. <a href="https://api.beeminder.com/#attributes-2">More info here.</a>. |  |

**Goal Type options:**

* **Hustler** (`hustler`)
* **Biker** (`biker`)
* **Fatloser** (`fatloser`)
* **Gainer** (`gainer`)
* **Inboxer** (`inboxer`)
* **Drinker** (`drinker`)
* **Custom** (`custom`)

| Goal Units | `gunits` | string |  | ✓ | Units for the goal (e.g., "hours", "pages", "pounds") |  |
| Value | `value` | number | 1 | ✓ | Datapoint value to send |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Defaults to "now" if none is passed in, or the existing timestamp if the datapoint is being updated rather than created | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Comment | `comment` | string |  |  |
| Timestamp | `timestamp` | dateTime |  | Defaults to "now" if none is passed in, or the existing timestamp if the datapoint is being updated rather than created |
| Request ID | `requestid` | string |  | String to uniquely identify a datapoint |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Charge explanation | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Note | `note` | string |  | Charge explanation |
| Dry Run | `dryrun` | boolean | False | Whether to test charge creation without actually charging |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Target date for the goal | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Goal Date | `goaldate` | dateTime |  | Target date for the goal |
| Goal Value | `goalval` | number |  | Target value for the goal |
| Rate | `rate` | number |  | Rate of progress (units per day) |
| Initial Value | `initval` | number | 0 | Initial value for today's date |
| Secret | `secret` | boolean | False | Whether the goal is secret |
| Data Public | `datapublic` | boolean | False | Whether the data is public |
| Data Source | `datasource` | options | manual | Data source for the goal |
| Dry Run | `dryrun` | boolean | False | Whether to test the endpoint without actually creating a goal |
| Tags | `tags` | json | [] | Array of alphanumeric tags for the goal. Replaces existing tags. |

</details>


### Create All parameters (`createAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Datapoints | `datapoints` | json | [] | ✓ | Array of datapoint objects to create. Each object should contain value and optionally timestamp, comment, etc. | e.g. [{"value": 1, "comment": "First datapoint"}, {"value": 2, "comment": "Second datapoint"}] |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Datapoint ID | `datapointId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Goal Name or ID | `goalName` | options |  | ✓ | The name of the goal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Datapoint ID | `datapointId` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include datapoints in the response | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Datapoints | `datapoints` | boolean | False | Whether to include datapoints in the response |
| Emaciated | `emaciated` | boolean | False | Whether to include the goal attributes called road, roadall, and fullroad will be stripped from the goal object |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include associations in the response | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Associations | `associations` | boolean | False | Whether to include associations in the response |
| Diff Since | `diff_since` | dateTime |  | Only goals and datapoints that have been created or updated since the timestamp will be returned |
| Skinny | `skinny` | boolean | False | Whether to return minimal user data |
| Emaciated | `emaciated` | boolean | False | Whether to include the goal attributes called road, roadall, and fullroad will be stripped from any goal objects returned with the user |
| Datapoints Count | `datapoints_count` | number |  | Number of datapoints to include |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 30 | ✗ | Max number of results to return | min:1, max:300 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the goal attributes called road, roadall, and fullroad will be stripped from the goal objects | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Emaciated | `emaciated` | boolean | False | Whether to include the goal attributes called road, roadall, and fullroad will be stripped from the goal objects |

</details>

| Options | `options` | collection | {} | ✗ | Attribute to sort on | e.g. Add field | min:1, max:∞ |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort | `sort` | string | id | Attribute to sort on |
| Page | `page` | number | 1 | Used to paginate results, 1-indexed, meaning page 1 is the first page |
| Per Page | `per` | number | 25 | Number of results per page. Default 25. Ignored without page parameter. Must be non-negative |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Goal Name or ID | `goalName` | options |  | ✓ | The name of the goal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Datapoint ID | `datapointId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Human-readable title for the goal | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Title | `title` | string |  | Human-readable title for the goal |
| Y-Axis | `yaxis` | string |  | Y-axis label for the goal graph |
| Tmin | `tmin` | string |  | Minimum date for the goal in format yyyy-mm-dd |
| Tmax | `tmax` | string |  | Maximum date for the goal in format yyyy-mm-dd |
| Secret | `secret` | boolean | False | Whether the goal is secret |
| Data Public | `datapublic` | boolean | False | Whether the data is public |
| Road All | `roadall` | json | [] | Array of arrays defining the bright red line. Each sub-array contains [date, value, rate] with exactly one field null. |
| Data Source | `datasource` | options |  | Data source for the goal. Use empty string for manual entry. |
| Tags | `tags` | json | [] | Array of alphanumeric tags for the goal. Replaces existing tags. |

</details>

| Update Fields | `updateFields` | collection | {} | ✗ | Datapoint value to send | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Value | `value` | number | 1 | Datapoint value to send |
| Comment | `comment` | string |  |  |
| Timestamp | `timestamp` | dateTime |  | Defaults to "now" if none is passed in, or the existing timestamp if the datapoint is being updated rather than created |

</details>


### Get Archived parameters (`getArchived`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the goal attributes called road, roadall, and fullroad will be stripped from the goal objects | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Emaciated | `emaciated` | boolean | False | Whether to include the goal attributes called road, roadall, and fullroad will be stripped from the goal objects |

</details>


### Refresh parameters (`refresh`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Goal Name or ID | `goalName` | options |  | ✓ | The name of the goal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Short Circuit parameters (`shortCircuit`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Goal Name or ID | `goalName` | options |  | ✓ | The name of the goal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Step Down parameters (`stepDown`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Goal Name or ID | `goalName` | options |  | ✓ | The name of the goal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Cancel Step Down parameters (`cancelStepDown`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Goal Name or ID | `goalName` | options |  | ✓ | The name of the goal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Uncle parameters (`uncle`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Goal Name or ID | `goalName` | options |  | ✓ | The name of the goal to derail. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

---

## Load Options Methods

- `getGoals`
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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: beeminder
displayName: Beeminder
description: Consume Beeminder API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: beeminderApi
  required: true
- name: beeminderOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a charge
  params:
  - id: amount
    name: Amount
    type: number
    default: 0
    required: true
    description: Charge amount in USD
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - charge
          operation:
          - create
    typeInfo:
      type: number
      displayName: Amount
      name: amount
  - id: slug
    name: Goal Slug
    type: string
    default: ''
    required: true
    description: Unique identifier for the goal
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - goal
          operation:
          - create
    typeInfo:
      type: string
      displayName: Goal Slug
      name: slug
  - id: title
    name: Goal Title
    type: string
    default: ''
    required: true
    description: Human-readable title for the goal
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - goal
          operation:
          - create
    typeInfo:
      type: string
      displayName: Goal Title
      name: title
  - id: goal_type
    name: Goal Type
    type: options
    default: hustler
    required: true
    description: Type of goal. <a href="https://api.beeminder.com/#attributes-2">More
      info here.</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - goal
          operation:
          - create
    typeInfo:
      type: options
      displayName: Goal Type
      name: goal_type
      possibleValues:
      - value: hustler
        name: Hustler
        description: ''
      - value: biker
        name: Biker
        description: ''
      - value: fatloser
        name: Fatloser
        description: ''
      - value: gainer
        name: Gainer
        description: ''
      - value: inboxer
        name: Inboxer
        description: ''
      - value: drinker
        name: Drinker
        description: ''
      - value: custom
        name: Custom
        description: ''
  - id: gunits
    name: Goal Units
    type: string
    default: ''
    required: true
    description: Units for the goal (e.g., "hours", "pages", "pounds")
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - goal
          operation:
          - create
    typeInfo:
      type: string
      displayName: Goal Units
      name: gunits
  - id: value
    name: Value
    type: number
    default: 1
    required: true
    description: Datapoint value to send
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - datapoint
          operation:
          - create
    typeInfo:
      type: number
      displayName: Value
      name: value
- id: createAll
  name: Create All
  description: Create multiple datapoints at once
  params:
  - id: datapoints
    name: Datapoints
    type: json
    default: '[]'
    required: true
    description: Array of datapoint objects to create. Each object should contain
      value and optionally timestamp, comment, etc.
    placeholder: '[{"value": 1, "comment": "First datapoint"}, {"value": 2, "comment":
      "Second datapoint"}]'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - datapoint
          operation:
          - createAll
    typeInfo:
      type: json
      displayName: Datapoints
      name: datapoints
- id: delete
  name: Delete
  description: Delete a datapoint
  params:
  - id: datapointId
    name: Datapoint ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - datapoint
          operation:
          - update
          - delete
          - get
    typeInfo: &id002
      type: string
      displayName: Datapoint ID
      name: datapointId
- id: get
  name: Get
  description: Get a single datapoint
  params:
  - id: goalName
    name: Goal Name or ID
    type: options
    default: ''
    required: true
    description: The name of the goal. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - goal
          operation:
          - get
          - update
          - refresh
          - shortCircuit
          - stepDown
          - cancelStepDown
    typeInfo: &id004
      type: options
      displayName: Goal Name or ID
      name: goalName
      typeOptions:
        loadOptionsMethod: getGoals
      possibleValues: []
  - id: datapointId
    name: Datapoint ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many datapoints for a goal
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
          - datapoint
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
          - datapoint
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
  description: Update a datapoint
  params:
  - id: goalName
    name: Goal Name or ID
    type: options
    default: ''
    required: true
    description: The name of the goal. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: datapointId
    name: Datapoint ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
- id: getArchived
  name: Get Archived
  description: Get archived goals
  params: []
- id: refresh
  name: Refresh
  description: Refresh goal data
  params:
  - id: goalName
    name: Goal Name or ID
    type: options
    default: ''
    required: true
    description: The name of the goal. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
- id: shortCircuit
  name: Short Circuit
  description: Short circuit pledge
  params:
  - id: goalName
    name: Goal Name or ID
    type: options
    default: ''
    required: true
    description: The name of the goal. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
- id: stepDown
  name: Step Down
  description: Step down pledge
  params:
  - id: goalName
    name: Goal Name or ID
    type: options
    default: ''
    required: true
    description: The name of the goal. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
- id: cancelStepDown
  name: Cancel Step Down
  description: ''
  params:
  - id: goalName
    name: Goal Name or ID
    type: options
    default: ''
    required: true
    description: The name of the goal. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
- id: uncle
  name: Uncle
  description: Derail a goal and charge the pledge amount
  params:
  - id: goalName
    name: Goal Name or ID
    type: options
    default: ''
    required: true
    description: The name of the goal to derail. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
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
  - field: datapoints
    text: '[{"value": 1, "comment": "First datapoint"}, {"value": 2, "comment": "Second
      datapoint"}]'
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
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add field
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
  "$id": "https://n8n.io/schemas/nodes/beeminder.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Beeminder Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "createAll",
        "delete",
        "get",
        "getAll",
        "update",
        "getArchived",
        "refresh",
        "shortCircuit",
        "stepDown",
        "cancelStepDown",
        "uncle"
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
            "charge",
            "datapoint",
            "goal",
            "user"
          ],
          "default": "datapoint"
        },
        "operation": {
          "description": "Get user information",
          "type": "string",
          "enum": [
            "get"
          ],
          "default": "get"
        },
        "goalName": {
          "description": "The name of the goal. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "amount": {
          "description": "Charge amount in USD",
          "type": "number",
          "default": 0
        },
        "datapoints": {
          "description": "Array of datapoint objects to create. Each object should contain value and optionally timestamp, comment, etc.",
          "type": "string",
          "default": "[]",
          "examples": [
            "[{\"value\": 1, \"comment\": \"First datapoint\"}, {\"value\": 2, \"comment\": \"Second datapoint\"}]"
          ]
        },
        "slug": {
          "description": "Unique identifier for the goal",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "Human-readable title for the goal",
          "type": "string",
          "default": ""
        },
        "goal_type": {
          "description": "Type of goal. <a href=\"https://api.beeminder.com/#attributes-2\">More info here.</a>.",
          "type": "string",
          "enum": [
            "hustler",
            "biker",
            "fatloser",
            "gainer",
            "inboxer",
            "drinker",
            "custom"
          ],
          "default": "hustler"
        },
        "gunits": {
          "description": "Units for the goal (e.g., \"hours\", \"pages\", \"pounds\")",
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
        "value": {
          "description": "Datapoint value to send",
          "type": "number",
          "default": 1
        },
        "datapointId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Whether to include the goal attributes called road, roadall, and fullroad will be stripped from the goal objects",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "Datapoint value to send",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "options": {
          "description": "Attribute to sort on",
          "type": "string",
          "default": {},
          "examples": [
            "Add field"
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
      "name": "beeminderApi",
      "required": true
    },
    {
      "name": "beeminderOAuth2Api",
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
