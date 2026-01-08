---
title: "Node: Date & Time"
slug: "node-date-&-time"
version: "2"
updated: "2026-01-08"
summary: "Allows you to manipulate date and time values"
node_type: "regular"
group: "['transform']"
---

# Node: Date & Time

**Purpose.** Allows you to manipulate date and time values
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `fa:clock`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice** when operation=['getCurrentDate']: You can also refer to the current date in n8n expressions by using <code>{{$now}}</code> or <code>{{$today}}</code>. <a target="_blank" href="https://docs.n8n.io/code/cookbook/luxon/">More info</a>
- **notice** when operation=['addToDate']: You can also do this using an expression, e.g. <code>{{your_date.plus(5, 'minutes')}}</code>. <a target='_blank' href='https://docs.n8n.io/code/cookbook/luxon/'>More info</a>
- **notice** when operation=['subtractFromDate']: You can also do this using an expression, e.g. <code>{{your_date.minus(5, 'minutes')}}</code>. <a target='_blank' href='https://docs.n8n.io/code/cookbook/luxon/'>More info</a>
- **notice** when operation=['formatDate']: You can also do this using an expression, e.g. <code>{{your_date.format('yyyy-MM-dd')}}</code>. <a target='_blank' href='https://docs.n8n.io/code/cookbook/luxon/'>More info</a>
- **notice** when operation=['roundDate']: You can also do this using an expression, e.g. <code>{{ your_date.beginningOf('month') }}</code> or <code>{{ your_date.endOfMonth() }}</code>. <a target='_blank' href='https://docs.n8n.io/code/cookbook/luxon/'>More info</a>

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add to a Date | `addToDate` |  |
| Extract Part of a Date | `extractDate` |  |
| Format a Date | `formatDate` |  |
| Get Current Date | `getCurrentDate` |  |
| Get Time Between Dates | `getTimeBetweenDates` |  |
| Round a Date | `roundDate` |  |
| Subtract From a Date | `subtractFromDate` |  |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getCurrentDate | ✗ | Operation to perform |  |

**Operation options:**

* **Add to a Date** (`addToDate`)
* **Extract Part of a Date** (`extractDate`)
* **Format a Date** (`formatDate`)
* **Get Current Date** (`getCurrentDate`)
* **Get Time Between Dates** (`getTimeBetweenDates`)
* **Round a Date** (`roundDate`)
* **Subtract From a Date** (`subtractFromDate`)

---

### Add to a Date parameters (`addToDate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Date to Add To | `magnitude` | string |  | ✓ | The date that you want to change |  |
| Time Unit to Add | `timeUnit` | options | days | ✓ | Time unit for Duration parameter below |  |

**Time Unit to Add options:**

* **Years** (`years`)
* **Quarters** (`quarters`)
* **Months** (`months`)
* **Weeks** (`weeks`)
* **Days** (`days`)
* **Hours** (`hours`)
* **Minutes** (`minutes`)
* **Seconds** (`seconds`)
* **Milliseconds** (`milliseconds`)

| Duration | `duration` | number | 0 | ✗ | The number of time units to add to the date |  |
| Output Field Name | `outputFieldName` | string | newDate | ✗ | Name of the field to put the output in |  |
| Options | `options` | collection | {} | ✗ | e.g. Add option |  |

### Format a Date parameters (`formatDate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Date | `date` | string |  | ✗ | The date that you want to format |  |
| Format | `format` | options | MM/dd/yyyy | ✗ | Example: 09/04/1986 |  |

**Format options:**

* **Custom Format** (`custom`)
* **MM/DD/YYYY** (`MM/dd/yyyy`) - Example: 09/04/1986
* **YYYY/MM/DD** (`yyyy/MM/dd`) - Example: 1986/04/09
* **MMMM DD YYYY** (`MMMM dd yyyy`) - Example: April 09 1986
* **MM-DD-YYYY** (`MM-dd-yyyy`) - Example: 09-04-1986
* **YYYY-MM-DD** (`yyyy-MM-dd`) - Example: 1986-04-09
* **Unix Timestamp** (`X`) - Example: 1672531200
* **Unix Ms Timestamp** (`x`) - Example: 1674691200000

| Custom Format | `customFormat` | string |  | ✗ | e.g. yyyy-MM-dd |  |
| Output Field Name | `outputFieldName` | string | formattedDate | ✗ | Name of the field to put the output in |  |
| Options | `options` | collection | {} | ✗ | Format in which the input 'Date' is, it's helpful when the format is not recognized automatically. Use those <a href="https://moment.github.io/luxon/#/formatting?id=table-of-tokens&id=table-of-tokens" target="_blank">tokens</a> to define the format. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| From Date Format | `fromFormat` | string | e.g yyyyMMdd | Format in which the input 'Date' is, it's helpful when the format is not recognized automatically. Use those <a href="https://moment.github.io/luxon/#/formatting?id=table-of-tokens&id=table-of-tokens" target="_blank">tokens</a> to define the format. |
| Use Workflow Timezone | `timezone` | boolean | False | Whether to use the timezone of the input or the workflow's timezone |

</details>


### Get Current Date parameters (`getCurrentDate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Include Current Time | `includeTime` | boolean | True | ✗ | When deactivated, the time will be set to midnight |  |
| Output Field Name | `outputFieldName` | string | currentDate | ✗ | Name of the field to put the output in |  |
| Options | `options` | collection | {} | ✗ | The timezone to use. If not set, the timezone of the n8n instance will be used. Use ‘GMT’ for +00:00 timezone. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Timezone | `timezone` | string |  | The timezone to use. If not set, the timezone of the n8n instance will be used. Use ‘GMT’ for +00:00 timezone. |

</details>


### Get Time Between Dates parameters (`getTimeBetweenDates`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Start Date | `startDate` | string |  | ✗ |  |  |
| End Date | `endDate` | string |  | ✗ |  |  |
| Units | `units` | multiOptions |  | ✗ |  |  |

**Units options:**

* **Year** (`year`)
* **Month** (`month`)
* **Week** (`week`)
* **Day** (`day`)
* **Hour** (`hour`)
* **Minute** (`minute`)
* **Second** (`second`)
* **Millisecond** (`millisecond`)

| Output Field Name | `outputFieldName` | string | timeDifference | ✗ | Name of the field to put the output in |  |
| Options | `options` | collection | {} | ✗ | Whether to output the date as ISO string or not | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Output as ISO String | `isoString` | boolean | False | Whether to output the date as ISO string or not |

</details>


### Round a Date parameters (`roundDate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Date | `date` | string |  | ✗ | The date that you want to round |  |
| Mode | `mode` | options | roundDown | ✗ |  |  |

**Mode options:**

* **Round Down** (`roundDown`)
* **Round Up** (`roundUp`)

| To Nearest | `toNearest` | options | month | ✗ |  |  |

**To Nearest options:**

* **Year** (`year`)
* **Month** (`month`)
* **Week** (`week`)
* **Day** (`day`)
* **Hour** (`hour`)
* **Minute** (`minute`)
* **Second** (`second`)

| To | `to` | options | month | ✗ |  |  |

**To options:**

* **End of Month** (`month`)

| Output Field Name | `outputFieldName` | string | roundedDate | ✗ | Name of the field to put the output in |  |
| Options | `options` | collection | {} | ✗ | e.g. Add option |  |

### Subtract From a Date parameters (`subtractFromDate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Date to Subtract From | `magnitude` | string |  | ✓ | The date that you want to change |  |
| Time Unit to Subtract | `timeUnit` | options | days | ✓ | Time unit for Duration parameter below |  |

**Time Unit to Subtract options:**

* **Years** (`years`)
* **Quarters** (`quarters`)
* **Months** (`months`)
* **Weeks** (`weeks`)
* **Days** (`days`)
* **Hours** (`hours`)
* **Minutes** (`minutes`)
* **Seconds** (`seconds`)
* **Milliseconds** (`milliseconds`)

| Duration | `duration` | number | 0 | ✗ | The number of time units to subtract from the date |  |
| Output Field Name | `outputFieldName` | string | newDate | ✗ | Name of the field to put the output in |  |
| Options | `options` | collection | {} | ✗ | e.g. Add option |  |

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
node: Date & Time
displayName: Date & Time
description: Allows you to manipulate date and time values
version: '2'
nodeType: regular
group:
- transform
operations:
- id: addToDate
  name: Add to a Date
  description: ''
  params:
  - id: magnitude
    name: Date to Add To
    type: string
    default: ''
    required: true
    description: The date that you want to change
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - subtractFromDate
    typeInfo: &id006
      type: string
      displayName: Date to Subtract From
      name: magnitude
  - id: timeUnit
    name: Time Unit to Add
    type: options
    default: days
    required: true
    description: Time unit for Duration parameter below
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - subtractFromDate
    typeInfo: &id008
      type: options
      displayName: Time Unit to Subtract
      name: timeUnit
      possibleValues:
      - value: years
        name: Years
        description: ''
      - value: quarters
        name: Quarters
        description: ''
      - value: months
        name: Months
        description: ''
      - value: weeks
        name: Weeks
        description: ''
      - value: days
        name: Days
        description: ''
      - value: hours
        name: Hours
        description: ''
      - value: minutes
        name: Minutes
        description: ''
      - value: seconds
        name: Seconds
        description: ''
      - value: milliseconds
        name: Milliseconds
        description: ''
  - id: duration
    name: Duration
    type: number
    default: 0
    required: false
    description: The number of time units to add to the date
    validation: &id009
      displayOptions:
        show:
          operation:
          - subtractFromDate
    typeInfo: &id010
      type: number
      displayName: Duration
      name: duration
  - id: outputFieldName
    name: Output Field Name
    type: string
    default: newDate
    required: false
    description: Name of the field to put the output in
    validation: &id001
      displayOptions:
        show:
          operation:
          - getTimeBetweenDates
    typeInfo: &id002
      type: unknown
      displayName: Output Field Name
      name: outputFieldName
- id: extractDate
  name: Extract Part of a Date
  description: ''
- id: formatDate
  name: Format a Date
  description: ''
  params:
  - id: date
    name: Date
    type: string
    default: ''
    required: false
    description: The date that you want to format
    validation: &id003
      displayOptions:
        show:
          operation:
          - roundDate
    typeInfo: &id004
      type: unknown
      displayName: Date
      name: date
  - id: format
    name: Format
    type: options
    default: MM/dd/yyyy
    required: false
    description: 'Example: 09/04/1986'
    validation:
      displayOptions:
        show:
          operation:
          - formatDate
    typeInfo:
      type: options
      displayName: Format
      name: format
      possibleValues:
      - value: custom
        name: Custom Format
        description: ''
      - value: MM/dd/yyyy
        name: MM/DD/YYYY
        description: 'Example: 09/04/1986'
      - value: yyyy/MM/dd
        name: YYYY/MM/DD
        description: 'Example: 1986/04/09'
      - value: MMMM dd yyyy
        name: MMMM DD YYYY
        description: 'Example: April 09 1986'
      - value: MM-dd-yyyy
        name: MM-DD-YYYY
        description: 'Example: 09-04-1986'
      - value: yyyy-MM-dd
        name: YYYY-MM-DD
        description: 'Example: 1986-04-09'
      - value: X
        name: Unix Timestamp
        description: 'Example: 1672531200'
      - value: x
        name: Unix Ms Timestamp
        description: 'Example: 1674691200000'
  - id: customFormat
    name: Custom Format
    type: string
    default: ''
    required: false
    description: ''
    hint: List of special tokens <a target="_blank" href="https://moment.github.io/luxon/#/formatting?id=table-of-tokens">More
      info</a>
    placeholder: yyyy-MM-dd
    validation:
      displayOptions:
        show:
          format:
          - custom
          operation:
          - formatDate
    typeInfo:
      type: string
      displayName: Custom Format
      name: customFormat
  - id: outputFieldName
    name: Output Field Name
    type: string
    default: formattedDate
    required: false
    description: Name of the field to put the output in
    validation: *id001
    typeInfo: *id002
- id: getCurrentDate
  name: Get Current Date
  description: ''
  params:
  - id: includeTime
    name: Include Current Time
    type: boolean
    default: true
    required: false
    description: When deactivated, the time will be set to midnight
    validation:
      displayOptions:
        show:
          operation:
          - getCurrentDate
    typeInfo:
      type: boolean
      displayName: Include Current Time
      name: includeTime
  - id: outputFieldName
    name: Output Field Name
    type: string
    default: currentDate
    required: false
    description: Name of the field to put the output in
    validation: *id001
    typeInfo: *id002
- id: getTimeBetweenDates
  name: Get Time Between Dates
  description: ''
  params:
  - id: startDate
    name: Start Date
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - getTimeBetweenDates
    typeInfo:
      type: string
      displayName: Start Date
      name: startDate
  - id: endDate
    name: End Date
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - getTimeBetweenDates
    typeInfo:
      type: string
      displayName: End Date
      name: endDate
  - id: units
    name: Units
    type: multiOptions
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - getTimeBetweenDates
    typeInfo:
      type: multiOptions
      displayName: Units
      name: units
      possibleValues:
      - value: year
        name: Year
        description: ''
      - value: month
        name: Month
        description: ''
      - value: week
        name: Week
        description: ''
      - value: day
        name: Day
        description: ''
      - value: hour
        name: Hour
        description: ''
      - value: minute
        name: Minute
        description: ''
      - value: second
        name: Second
        description: ''
      - value: millisecond
        name: Millisecond
        description: ''
  - id: outputFieldName
    name: Output Field Name
    type: string
    default: timeDifference
    required: false
    description: Name of the field to put the output in
    validation: *id001
    typeInfo: *id002
- id: roundDate
  name: Round a Date
  description: ''
  params:
  - id: date
    name: Date
    type: string
    default: ''
    required: false
    description: The date that you want to round
    validation: *id003
    typeInfo: *id004
  - id: mode
    name: Mode
    type: options
    default: roundDown
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - roundDate
    typeInfo:
      type: options
      displayName: Mode
      name: mode
      possibleValues:
      - value: roundDown
        name: Round Down
        description: ''
      - value: roundUp
        name: Round Up
        description: ''
  - id: toNearest
    name: To Nearest
    type: options
    default: month
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - roundDate
          mode:
          - roundDown
    typeInfo:
      type: options
      displayName: To Nearest
      name: toNearest
      possibleValues:
      - value: year
        name: Year
        description: ''
      - value: month
        name: Month
        description: ''
      - value: week
        name: Week
        description: ''
      - value: day
        name: Day
        description: ''
      - value: hour
        name: Hour
        description: ''
      - value: minute
        name: Minute
        description: ''
      - value: second
        name: Second
        description: ''
  - id: to
    name: To
    type: options
    default: month
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - roundDate
          mode:
          - roundUp
    typeInfo:
      type: options
      displayName: To
      name: to
      possibleValues:
      - value: month
        name: End of Month
        description: ''
  - id: outputFieldName
    name: Output Field Name
    type: string
    default: roundedDate
    required: false
    description: Name of the field to put the output in
    validation: *id001
    typeInfo: *id002
- id: subtractFromDate
  name: Subtract From a Date
  description: ''
  params:
  - id: magnitude
    name: Date to Subtract From
    type: string
    default: ''
    required: true
    description: The date that you want to change
    validation: *id005
    typeInfo: *id006
  - id: timeUnit
    name: Time Unit to Subtract
    type: options
    default: days
    required: true
    description: Time unit for Duration parameter below
    validation: *id007
    typeInfo: *id008
  - id: duration
    name: Duration
    type: number
    default: 0
    required: false
    description: The number of time units to subtract from the date
    validation: *id009
    typeInfo: *id010
  - id: outputFieldName
    name: Output Field Name
    type: string
    default: newDate
    required: false
    description: Name of the field to put the output in
    validation: *id001
    typeInfo: *id002
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: notice
    text: You can also refer to the current date in n8n expressions by using <code>{{$now}}</code>
      or <code>{{$today}}</code>. <a target="_blank" href="https://docs.n8n.io/code/cookbook/luxon/">More
      info</a>
    conditions:
      show:
        operation:
        - getCurrentDate
  - name: notice
    text: You can also do this using an expression, e.g. <code>{{your_date.plus(5,
      'minutes')}}</code>. <a target='_blank' href='https://docs.n8n.io/code/cookbook/luxon/'>More
      info</a>
    conditions:
      show:
        operation:
        - addToDate
  - name: notice
    text: You can also do this using an expression, e.g. <code>{{your_date.minus(5,
      'minutes')}}</code>. <a target='_blank' href='https://docs.n8n.io/code/cookbook/luxon/'>More
      info</a>
    conditions:
      show:
        operation:
        - subtractFromDate
  - name: notice
    text: You can also do this using an expression, e.g. <code>{{your_date.format('yyyy-MM-dd')}}</code>.
      <a target='_blank' href='https://docs.n8n.io/code/cookbook/luxon/'>More info</a>
    conditions:
      show:
        operation:
        - formatDate
  - name: notice
    text: You can also do this using an expression, e.g. <code>{{ your_date.beginningOf('month')
      }}</code> or <code>{{ your_date.endOfMonth() }}</code>. <a target='_blank' href='https://docs.n8n.io/code/cookbook/luxon/'>More
      info</a>
    conditions:
      show:
        operation:
        - roundDate
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: customFormat
    text: yyyy-MM-dd
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  hints:
  - field: customFormat
    text: List of special tokens <a target="_blank" href="https://moment.github.io/luxon/#/formatting?id=table-of-tokens">More
      info</a>
  - field: options
    text: Tokens are case sensitive
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
  "$id": "https://n8n.io/schemas/nodes/Date & Time.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Date & Time Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "addToDate",
        "extractDate",
        "formatDate",
        "getCurrentDate",
        "getTimeBetweenDates",
        "roundDate",
        "subtractFromDate"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "addToDate",
            "extractDate",
            "formatDate",
            "getCurrentDate",
            "getTimeBetweenDates",
            "roundDate",
            "subtractFromDate"
          ],
          "default": "getCurrentDate"
        },
        "includeTime": {
          "description": "When deactivated, the time will be set to midnight",
          "type": "boolean",
          "default": true
        },
        "outputFieldName": {
          "description": "",
          "type": "string"
        },
        "options": {
          "description": "",
          "type": "string"
        },
        "magnitude": {
          "description": "The date that you want to change",
          "type": "string",
          "default": ""
        },
        "timeUnit": {
          "description": "Time unit for Duration parameter below",
          "type": "string",
          "enum": [
            "years",
            "quarters",
            "months",
            "weeks",
            "days",
            "hours",
            "minutes",
            "seconds",
            "milliseconds"
          ],
          "default": "days"
        },
        "duration": {
          "description": "The number of time units to subtract from the date",
          "type": "number",
          "default": 0
        },
        "date": {
          "description": "",
          "type": "string"
        },
        "format": {
          "description": "Example: 09/04/1986",
          "type": "string",
          "enum": [
            "custom",
            "MM/dd/yyyy",
            "yyyy/MM/dd",
            "MMMM dd yyyy",
            "MM-dd-yyyy",
            "yyyy-MM-dd",
            "X",
            "x"
          ],
          "default": "MM/dd/yyyy"
        },
        "customFormat": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "yyyy-MM-dd"
          ]
        },
        "mode": {
          "description": "",
          "type": "string",
          "enum": [
            "roundDown",
            "roundUp"
          ],
          "default": "roundDown"
        },
        "toNearest": {
          "description": "",
          "type": "string",
          "enum": [
            "year",
            "month",
            "week",
            "day",
            "hour",
            "minute",
            "second"
          ],
          "default": "month"
        },
        "to": {
          "description": "",
          "type": "string",
          "enum": [
            "month"
          ],
          "default": "month"
        },
        "startDate": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "endDate": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "units": {
          "description": "",
          "type": "string"
        },
        "notice": {
          "description": "",
          "type": "string"
        },
        "part": {
          "description": "",
          "type": "string"
        },
        "Year": {
          "description": "",
          "type": "string"
        },
        "Month": {
          "description": "",
          "type": "string"
        },
        "Week": {
          "description": "",
          "type": "string"
        },
        "Day": {
          "description": "",
          "type": "string"
        },
        "Hour": {
          "description": "",
          "type": "string"
        },
        "Minute": {
          "description": "",
          "type": "string"
        },
        "Second": {
          "description": "",
          "type": "string"
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 2 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
