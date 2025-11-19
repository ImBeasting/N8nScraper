---
title: "Node: Schedule Trigger"
slug: "node-scheduletrigger"
version: "['1', '1.1', '1.2']"
updated: "2025-11-13"
summary: "Triggers the workflow on a given schedule"
node_type: "trigger"
group: "['trigger', 'schedule']"
---

# Node: Schedule Trigger

**Purpose.** Triggers the workflow on a given schedule


---

## Node Details

- **Icon:** `fa:clock`
- **Group:** `['trigger', 'schedule']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** Your schedule trigger will now trigger executions on the schedule you have defined.
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice**: This workflow will run on the schedule you define here once you <a data-key="activate">activate</a> it.<br><br>For testing, you can also trigger it manually: by going back to the canvas and clicking 'execute workflow'

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger Rules | `rule` | fixedCollection | days | ✗ | Number of seconds between each workflow trigger | e.g. Add Rule |  |

<details>
<summary><strong>Trigger Rules sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Trigger Interval | `interval` |  |  |  |

</details>


---

## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |

---

## Notes & Caveats

* This node is part of n8n-nodes-base
* Categories: Core Nodes
* Aliases: Time, Scheduler, Polling, Cron, Interval

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: scheduleTrigger
displayName: Schedule Trigger
description: Triggers the workflow on a given schedule
version:
- '1'
- '1.1'
- '1.2'
nodeType: trigger
group:
- trigger
- schedule
params:
- id: rule
  name: Trigger Rules
  type: fixedCollection
  default: days
  required: false
  description: Number of seconds between each workflow trigger
  hint: If a month doesn’t have this day, the node won’t trigger
  placeholder: Add Rule
  validation:
    displayOptions:
      show:
        field:
        - seconds
  typeInfo:
    type: fixedCollection
    displayName: Trigger Rules
    name: rule
    typeOptions:
      multipleValues: true
    subProperties:
    - name: interval
      displayName: Trigger Interval
      values:
      - displayName: Trigger Interval
        name: field
        type: options
        value: seconds
        default: days
        options:
        - name: Seconds
          value: seconds
          displayName: Seconds
        - name: Minutes
          value: minutes
          displayName: Minutes
        - name: Hours
          value: hours
          displayName: Hours
        - name: Days
          value: days
          displayName: Days
        - name: Weeks
          value: weeks
          displayName: Weeks
        - name: Months
          value: months
          displayName: Months
        - name: Custom (Cron)
          value: cronExpression
          displayName: Custom (cron)
      - displayName: Seconds Between Triggers
        name: secondsInterval
        type: number
        description: Number of seconds between each workflow trigger
        default: 30
        displayOptions:
          show:
            field:
            - seconds
      - displayName: Minutes Between Triggers
        name: minutesInterval
        type: number
        description: Number of minutes between each workflow trigger
        default: 5
        displayOptions:
          show:
            field:
            - minutes
      - displayName: Hours Between Triggers
        name: hoursInterval
        type: number
        description: Number of hours between each workflow trigger
        default: 1
        displayOptions:
          show:
            field:
            - hours
      - displayName: Days Between Triggers
        name: daysInterval
        type: number
        description: Number of days between each workflow trigger
        default: 1
        displayOptions:
          show:
            field:
            - days
      - displayName: Weeks Between Triggers
        name: weeksInterval
        type: number
        description: Would run every week unless specified otherwise
        default: 1
        displayOptions:
          show:
            field:
            - weeks
      - displayName: Months Between Triggers
        name: monthsInterval
        type: number
        description: Would run every month unless specified otherwise
        default: 1
        displayOptions:
          show:
            field:
            - months
      - displayName: Trigger at Day of Month
        name: triggerAtDayOfMonth
        type: number
        description: The day of the month to trigger (1-31)
        hint: If a month doesn’t have this day, the node won’t trigger
        default: 1
        typeOptions:
          minValue: 1
          maxValue: 31
        displayOptions:
          show:
            field:
            - months
      - displayName: Trigger on Weekdays
        name: triggerAtDay
        type: multiOptions
        options:
        - name: Monday
          displayName: Monday
        - name: Tuesday
          displayName: Tuesday
        - name: Wednesday
          displayName: Wednesday
        - name: Thursday
          displayName: Thursday
        - name: Friday
          displayName: Friday
        - name: Saturday
          displayName: Saturday
        - name: Sunday
          displayName: Sunday
        typeOptions:
          maxValue: 7
        displayOptions:
          show:
            field:
            - weeks
      - displayName: Trigger at Hour
        name: triggerAtHour
        type: options
        description: The hour of the day to trigger
        default: 0
        options:
        - displayName: Midnight
          name: Midnight
        - displayName: 1am
          name: 1am
        - displayName: 2am
          name: 2am
        - displayName: 3am
          name: 3am
        - displayName: 4am
          name: 4am
        - displayName: 5am
          name: 5am
        - displayName: 6am
          name: 6am
        - displayName: 7am
          name: 7am
        - displayName: 8am
          name: 8am
        - displayName: 9am
          name: 9am
        - displayName: 10am
          name: 10am
        - displayName: 11am
          name: 11am
        - displayName: Noon
          name: Noon
        - displayName: 1pm
          name: 1pm
        - displayName: 2pm
          name: 2pm
        - displayName: 3pm
          name: 3pm
        - displayName: 4pm
          name: 4pm
        - displayName: 5pm
          name: 5pm
        - displayName: 6pm
          name: 6pm
        - displayName: 7pm
          name: 7pm
        - displayName: 8pm
          name: 8pm
        - displayName: 9pm
          name: 9pm
        - displayName: 10pm
          name: 10pm
        - displayName: 11pm
          name: 11pm
        displayOptions:
          show:
            field:
            - days
            - weeks
            - months
      - displayName: Trigger at Minute
        name: triggerAtMinute
        type: number
        description: The minute past the hour to trigger (0-59)
        default: 0
        typeOptions:
          minValue: 0
          maxValue: 59
        displayOptions:
          show:
            field:
            - hours
            - days
            - weeks
            - months
      - displayName: You can find help generating your cron expression <a href="https://crontab.guru/examples.html"
          target="_blank">here</a>
        name: notice
        type: notice
        default: ''
        displayOptions:
          show:
            field:
            - cronExpression
      - displayName: Expression
        name: expression
        type: string
        placeholder: eg. 0 15 * 1 sun
        hint: 'Format: [Second] [Minute] [Hour] [Day of Month] [Month] [Day of Week]'
        default: ''
        displayOptions:
          show:
            field:
            - cronExpression
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: notice
    text: 'This workflow will run on the schedule you define here once you <a data-key="activate">activate</a>
      it.<br><br>For testing, you can also trigger it manually: by going back to the
      canvas and clicking ''execute workflow'''
    conditions: null
  tooltips: []
  placeholders:
  - field: rule
    text: Add Rule
  hints:
  - field: rule
    text: If a month doesn’t have this day, the node won’t trigger
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/scheduleTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Schedule Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "rule": {
          "description": "Number of seconds between each workflow trigger",
          "type": "string",
          "default": "days",
          "examples": [
            "Add Rule"
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
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
    "version": [
      "1",
      "1.1",
      "1.2"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1', '1.2'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
