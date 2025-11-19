---
title: "Node: Strava"
slug: "node-strava"
version: "['1', '1.1']"
updated: "2025-11-13"
summary: "Consume Strava API"
node_type: "regular"
group: "['input']"
---

# Node: Strava

**Purpose.** Consume Strava API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:strava.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **stravaOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `stravaOAuth2Api` | ✓ | - |

---

## Operations

### Activity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new activity |
| Get | `get` | Get an activity |
| Get Comments | `getComments` | Get all activity comments |
| Get Kudos | `getKudos` | Get all activity kudos |
| Get Laps | `getLaps` | Get all activity laps |
| Get Many | `getAll` | Get many activities |
| Get Streams | `getStreams` | Get activity streams |
| Get Zones | `getZones` | Get all activity zones |
| Update | `update` | Update an activity |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | activity | ✗ | Resource to operate on |  |

**Resource options:**

* **Activity** (`activity`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a new activity |  |

**Operation options:**

* **Create** (`create`) - Create a new activity
* **Get** (`get`) - Get an activity
* **Get Comments** (`getComments`) - Get all activity comments
* **Get Kudos** (`getKudos`) - Get all activity kudos
* **Get Laps** (`getLaps`) - Get all activity laps
* **Get Many** (`getAll`) - Get many activities
* **Get Streams** (`getStreams`) - Get activity streams
* **Get Zones** (`getZones`) - Get all activity zones
* **Update** (`update`) - Update an activity

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | The name of the activity |  |
| Type | `type` | string |  | ✓ | Type of activity. For example - Run, Ride etc. |  |
| Sport Type | `sport_type` | options | Run | ✗ | Type of sport |  |

**Sport Type options:**

* **Alpine Ski** (`AlpineSki`)
* **Backcountry Ski** (`BackcountrySki`)
* **Badminton** (`Badminton`)
* **Canoeing** (`Canoeing`)
* **Crossfit** (`Crossfit`)
* **EBike Ride** (`EBikeRide`)
* **Elliptical** (`Elliptical`)
* **EMountain Bike Ride** (`EMountainBikeRide`)
* **Golf** (`Golf`)
* **Gravel Ride** (`GravelRide`)
* **Handcycle** (`Handcycle`)
* **HIIT** (`HighIntensityIntervalTraining`)
* **Hike** (`Hike`)
* **Ice Skate** (`IceSkate`)
* **Inline Skate** (`InlineSkate`)
* **Kayaking** (`Kayaking`)
* **Kitesurf** (`Kitesurf`)
* **Mountain Bike Ride** (`MountainBikeRide`)
* **Nordic Ski** (`NordicSki`)
* **Pickleball** (`Pickleball`)
* **Pilates** (`Pilates`)
* **Racquetball** (`Racquetball`)
* **Ride** (`Ride`)
* **Rock Climbing** (`RockClimbing`)
* **Roller Ski** (`RollerSki`)
* **Rowing** (`Rowing`)
* **Run** (`Run`)
* **Sail** (`Sail`)
* **Skateboard** (`Skateboard`)
* **Snowboard** (`Snowboard`)
* **Snowshoe** (`Snowshoe`)
* **Soccer** (`Soccer`)
* **Squash** (`Squash`)
* **Stair Stepper** (`StairStepper`)
* **Stand Up Paddling** (`StandUpPaddling`)
* **Surfing** (`Surfing`)
* **Swim** (`Swim`)
* **Table Tennis** (`TableTennis`)
* **Tennis** (`Tennis`)
* **Trail Run** (`TrailRun`)
* **Velomobile** (`Velomobile`)
* **Virtual Ride** (`VirtualRide`)
* **Virtual Row** (`VirtualRow`)
* **Virtual Run** (`VirtualRun`)
* **Walk** (`Walk`)
* **Weight Training** (`WeightTraining`)
* **Wheelchair** (`Wheelchair`)
* **Windsurf** (`Windsurf`)
* **Workout** (`Workout`)
* **Yoga** (`Yoga`)

| Start Date | `startDate` | dateTime |  | ✓ | ISO 8601 formatted date time |  |
| Elapsed Time (Seconds) | `elapsedTime` | number | 0 | ✓ | In seconds | min:0, max:∞ |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to mark as commute | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Commute | `commute` | boolean | False | Whether to mark as commute |
| Description | `description` | string |  | Description of the activity |
| Distance | `distance` | number | 0 | In meters |
| Trainer | `trainer` | boolean | False | Whether to mark as a trainer activity |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Activity ID | `activityId` | string |  | ✓ | ID or email of activity |  |

### Get Comments parameters (`getComments`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Activity ID | `activityId` | string |  | ✓ | ID or email of activity |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Get Kudos parameters (`getKudos`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Activity ID | `activityId` | string |  | ✓ | ID or email of activity |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Get Laps parameters (`getLaps`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Activity ID | `activityId` | string |  | ✓ | ID or email of activity |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Get Streams parameters (`getStreams`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Activity ID | `activityId` | string |  | ✓ | ID or email of activity |  |
| Keys | `keys` | multiOptions | [] | ✓ | Desired stream types to return |  |

**Keys options:**

* **Altitude** (`altitude`)
* **Cadence** (`cadence`)
* **Distance** (`distance`)
* **Gradient** (`grade_smooth`)
* **Heartrate** (`heartrate`)
* **Latitude / Longitude** (`latlng`)
* **Moving** (`moving`)
* **Temperature** (`temp`)
* **Time** (`time`)
* **Velocity** (`velocity_smooth`)
* **Watts** (`watts`)


### Get Zones parameters (`getZones`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Activity ID | `activityId` | string |  | ✓ | ID or email of activity |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Activity ID | `activityId` | string |  | ✓ | ID or email of activity |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Whether to mark as commute | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Commute | `commute` | boolean | False | Whether to mark as commute |
| Description | `description` | string |  | Description of the activity |
| Gear ID | `gear_id` | string |  | Identifier for the gear associated with the activity. ‘none’ clears gear from activity. |
| Mute Activity | `hide_from_home` | boolean | False | Do not publish to Home or Club feeds |
| Name | `name` | string |  | The name of the activity |
| Type | `type` | string |  | Type of activity. For example - Run, Ride etc. |
| Sport Type | `sport_type` | options | Run | Type of sport |
| Trainer | `trainer` | boolean | False | Whether to mark as a trainer activity |

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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: strava
displayName: Strava
description: Consume Strava API
version:
- '1'
- '1.1'
nodeType: regular
group:
- input
credentials:
- name: stravaOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a new activity
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the activity
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - activity
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: type
    name: Type
    type: string
    default: ''
    required: true
    description: Type of activity. For example - Run, Ride etc.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - activity
          operation:
          - create
    typeInfo:
      type: string
      displayName: Type
      name: type
  - id: sport_type
    name: Sport Type
    type: options
    default: Run
    required: false
    description: Type of sport
    validation:
      displayOptions:
        show:
          resource:
          - activity
          operation:
          - create
        hide: {}
    typeInfo:
      type: options
      displayName: Sport Type
      name: sport_type
      possibleValues:
      - value: AlpineSki
        name: Alpine Ski
        description: ''
      - value: BackcountrySki
        name: Backcountry Ski
        description: ''
      - value: Badminton
        name: Badminton
        description: ''
      - value: Canoeing
        name: Canoeing
        description: ''
      - value: Crossfit
        name: Crossfit
        description: ''
      - value: EBikeRide
        name: EBike Ride
        description: ''
      - value: Elliptical
        name: Elliptical
        description: ''
      - value: EMountainBikeRide
        name: EMountain Bike Ride
        description: ''
      - value: Golf
        name: Golf
        description: ''
      - value: GravelRide
        name: Gravel Ride
        description: ''
      - value: Handcycle
        name: Handcycle
        description: ''
      - value: HighIntensityIntervalTraining
        name: HIIT
        description: ''
      - value: Hike
        name: Hike
        description: ''
      - value: IceSkate
        name: Ice Skate
        description: ''
      - value: InlineSkate
        name: Inline Skate
        description: ''
      - value: Kayaking
        name: Kayaking
        description: ''
      - value: Kitesurf
        name: Kitesurf
        description: ''
      - value: MountainBikeRide
        name: Mountain Bike Ride
        description: ''
      - value: NordicSki
        name: Nordic Ski
        description: ''
      - value: Pickleball
        name: Pickleball
        description: ''
      - value: Pilates
        name: Pilates
        description: ''
      - value: Racquetball
        name: Racquetball
        description: ''
      - value: Ride
        name: Ride
        description: ''
      - value: RockClimbing
        name: Rock Climbing
        description: ''
      - value: RollerSki
        name: Roller Ski
        description: ''
      - value: Rowing
        name: Rowing
        description: ''
      - value: Run
        name: Run
        description: ''
      - value: Sail
        name: Sail
        description: ''
      - value: Skateboard
        name: Skateboard
        description: ''
      - value: Snowboard
        name: Snowboard
        description: ''
      - value: Snowshoe
        name: Snowshoe
        description: ''
      - value: Soccer
        name: Soccer
        description: ''
      - value: Squash
        name: Squash
        description: ''
      - value: StairStepper
        name: Stair Stepper
        description: ''
      - value: StandUpPaddling
        name: Stand Up Paddling
        description: ''
      - value: Surfing
        name: Surfing
        description: ''
      - value: Swim
        name: Swim
        description: ''
      - value: TableTennis
        name: Table Tennis
        description: ''
      - value: Tennis
        name: Tennis
        description: ''
      - value: TrailRun
        name: Trail Run
        description: ''
      - value: Velomobile
        name: Velomobile
        description: ''
      - value: VirtualRide
        name: Virtual Ride
        description: ''
      - value: VirtualRow
        name: Virtual Row
        description: ''
      - value: VirtualRun
        name: Virtual Run
        description: ''
      - value: Walk
        name: Walk
        description: ''
      - value: WeightTraining
        name: Weight Training
        description: ''
      - value: Wheelchair
        name: Wheelchair
        description: ''
      - value: Windsurf
        name: Windsurf
        description: ''
      - value: Workout
        name: Workout
        description: ''
      - value: Yoga
        name: Yoga
        description: ''
  - id: startDate
    name: Start Date
    type: dateTime
    default: ''
    required: true
    description: ISO 8601 formatted date time
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - activity
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: Start Date
      name: startDate
  - id: elapsedTime
    name: Elapsed Time (Seconds)
    type: number
    default: 0
    required: true
    description: In seconds
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - activity
          operation:
          - create
    typeInfo:
      type: number
      displayName: Elapsed Time (Seconds)
      name: elapsedTime
      typeOptions:
        minValue: 0
- id: get
  name: Get
  description: Get an activity
  params:
  - id: activityId
    name: Activity ID
    type: string
    default: ''
    required: true
    description: ID or email of activity
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - activity
          operation:
          - getComments
          - getLaps
          - getKudos
          - getZones
          - getStreams
    typeInfo: &id002
      type: string
      displayName: Activity ID
      name: activityId
- id: getComments
  name: Get Comments
  description: Get all activity comments
  params:
  - id: activityId
    name: Activity ID
    type: string
    default: ''
    required: true
    description: ID or email of activity
    validation: *id001
    typeInfo: *id002
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
          - activity
          operation:
          - getAll
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          resource:
          - activity
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
        maxValue: 100
- id: getKudos
  name: Get Kudos
  description: Get all activity kudos
  params:
  - id: activityId
    name: Activity ID
    type: string
    default: ''
    required: true
    description: ID or email of activity
    validation: *id001
    typeInfo: *id002
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: getLaps
  name: Get Laps
  description: Get all activity laps
  params:
  - id: activityId
    name: Activity ID
    type: string
    default: ''
    required: true
    description: ID or email of activity
    validation: *id001
    typeInfo: *id002
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: getAll
  name: Get Many
  description: Get many activities
  params:
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: getStreams
  name: Get Streams
  description: Get activity streams
  params:
  - id: activityId
    name: Activity ID
    type: string
    default: ''
    required: true
    description: ID or email of activity
    validation: *id001
    typeInfo: *id002
  - id: keys
    name: Keys
    type: multiOptions
    default: []
    required: true
    description: Desired stream types to return
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - activity
          operation:
          - getStreams
    typeInfo:
      type: multiOptions
      displayName: Keys
      name: keys
      possibleValues:
      - value: altitude
        name: Altitude
        description: ''
      - value: cadence
        name: Cadence
        description: ''
      - value: distance
        name: Distance
        description: ''
      - value: grade_smooth
        name: Gradient
        description: ''
      - value: heartrate
        name: Heartrate
        description: ''
      - value: latlng
        name: Latitude / Longitude
        description: ''
      - value: moving
        name: Moving
        description: ''
      - value: temp
        name: Temperature
        description: ''
      - value: time
        name: Time
        description: ''
      - value: velocity_smooth
        name: Velocity
        description: ''
      - value: watts
        name: Watts
        description: ''
- id: getZones
  name: Get Zones
  description: Get all activity zones
  params:
  - id: activityId
    name: Activity ID
    type: string
    default: ''
    required: true
    description: ID or email of activity
    validation: *id001
    typeInfo: *id002
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: update
  name: Update
  description: Update an activity
  params:
  - id: activityId
    name: Activity ID
    type: string
    default: ''
    required: true
    description: ID or email of activity
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
  "$id": "https://n8n.io/schemas/nodes/strava.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Strava Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "get",
        "getComments",
        "getKudos",
        "getLaps",
        "getAll",
        "getStreams",
        "getZones",
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
            "activity"
          ],
          "default": "activity"
        },
        "operation": {
          "description": "Create a new activity",
          "type": "string",
          "enum": [
            "create",
            "get",
            "getComments",
            "getKudos",
            "getLaps",
            "getAll",
            "getStreams",
            "getZones",
            "update"
          ],
          "default": "create"
        },
        "name": {
          "description": "The name of the activity",
          "type": "string",
          "default": ""
        },
        "type": {
          "description": "Type of activity. For example - Run, Ride etc.",
          "type": "string",
          "default": ""
        },
        "sport_type": {
          "description": "Type of sport",
          "type": "string",
          "enum": [
            "AlpineSki",
            "BackcountrySki",
            "Badminton",
            "Canoeing",
            "Crossfit",
            "EBikeRide",
            "Elliptical",
            "EMountainBikeRide",
            "Golf",
            "GravelRide",
            "Handcycle",
            "HighIntensityIntervalTraining",
            "Hike",
            "IceSkate",
            "InlineSkate",
            "Kayaking",
            "Kitesurf",
            "MountainBikeRide",
            "NordicSki",
            "Pickleball",
            "Pilates",
            "Racquetball",
            "Ride",
            "RockClimbing",
            "RollerSki",
            "Rowing",
            "Run",
            "Sail",
            "Skateboard",
            "Snowboard",
            "Snowshoe",
            "Soccer",
            "Squash",
            "StairStepper",
            "StandUpPaddling",
            "Surfing",
            "Swim",
            "TableTennis",
            "Tennis",
            "TrailRun",
            "Velomobile",
            "VirtualRide",
            "VirtualRow",
            "VirtualRun",
            "Walk",
            "WeightTraining",
            "Wheelchair",
            "Windsurf",
            "Workout",
            "Yoga"
          ],
          "default": "Run"
        },
        "startDate": {
          "description": "ISO 8601 formatted date time",
          "type": "string",
          "default": ""
        },
        "elapsedTime": {
          "description": "In seconds",
          "type": "number",
          "default": 0
        },
        "additionalFields": {
          "description": "Whether to mark as commute",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "activityId": {
          "description": "ID or email of activity",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Whether to mark as commute",
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
          "default": 50
        },
        "keys": {
          "description": "Desired stream types to return",
          "type": "string",
          "default": []
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
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "stravaOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
