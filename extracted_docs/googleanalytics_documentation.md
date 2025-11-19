---
title: "Node: Google Analytics"
slug: "node-googleanalytics"
version: "2"
updated: "2025-11-13"
summary: "Use the Google Analytics API"
node_type: "regular"
group: "['transform']"
---

# Node: Google Analytics

**Purpose.** Use the Google Analytics API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:analytics.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleAnalyticsOAuth2**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleAnalyticsOAuth2` | ✓ | - |

---

## Operations

### Report Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Return the analytics data |

### Useractivity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Search | `search` | Return user activity data |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | report | ✗ | Resource to operate on |  |

**Resource options:**

* **Report** (`report`)
* **User Activity** (`userActivity`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Return the analytics data |  |

**Operation options:**

* **Get** (`get`) - Return the analytics data

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Property Type | `propertyType` | options | ga4 | ✗ | Google Analytics 4 is the latest version. Universal Analytics is an older version that is not fully functional after the end of June 2023. |  |

**Property Type options:**

* **Google Analytics 4** (`ga4`)
* **Universal Analytics** (`universal`)

| Property | `propertyId` | resourceLocator |  | ✓ | The Property of Google Analytics | e.g. Select a property... |  |
| Date Range | `dateRange` | options | last7days | ✓ |  |  |

**Date Range options:**

* **Last 7 Days** (`last7days`)
* **Last 30 Days** (`last30days`)
* **Today** (`today`)
* **Yesterday** (`yesterday`)
* **Last Complete Calendar Week** (`lastCalendarWeek`)
* **Last Complete Calendar Month** (`lastCalendarMonth`)
* **Custom** (`custom`)

| Start | `startDate` | dateTime |  | ✓ |  |  |
| End | `endDate` | dateTime |  | ✓ |  |  |
| Dimensions to split by | `dimensionsGA4` | fixedCollection | {} | ✗ | Dimensions are attributes of your data. For example, the dimension city indicates the city from which an event originates. Dimension values in report responses are strings; for example, the city could be "Paris" or "New York". Requests are allowed up to 9 dimensions. | e.g. Add Dimension |  |

<details>
<summary><strong>Dimensions to split by sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Values | `dimensionValues` |  |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Simplify Output | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | A currency code in ISO4217 format, such as "AED", "USD", "JPY". If the field is empty, the report uses the property's default currency. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Currency Code | `currencyCode` | string |  | A currency code in ISO4217 format, such as "AED", "USD", "JPY". If the field is empty, the report uses the property's default currency. |
| Metric Aggregation | `metricAggregations` | multiOptions | [] |  |
| Keep Empty Rows | `keepEmptyRows` | boolean | False | Whether false or unspecified, each row with all metrics equal to 0 will not be returned. If true, these rows will be returned if they are not separately removed by a filter. |
| Order By | `orderByUI` | fixedCollection | {} | Specifies how rows are ordered in the response |
| Return Property Quota | `returnPropertyQuota` | boolean | False | Whether to return the current state of this Analytics Property's quota. Quota is returned in PropertyQuota. |

</details>

| View | `viewId` | resourceLocator |  | ✓ | The View of Google Analytics | e.g. Select a view... |  |
| Date Range | `dateRange` | options | last7days | ✓ |  |  |

**Date Range options:**

* **Last 7 Days** (`last7days`)
* **Last 30 Days** (`last30days`)
* **Today** (`today`)
* **Yesterday** (`yesterday`)
* **Last Complete Calendar Week** (`lastCalendarWeek`)
* **Last Complete Calendar Month** (`lastCalendarMonth`)
* **Custom** (`custom`)

| Start | `startDate` | dateTime |  | ✓ |  |  |
| End | `endDate` | dateTime |  | ✓ |  |  |
| Dimensions to split by | `dimensionsUA` | fixedCollection | {} | ✗ | Dimensions are attributes of your data. For example, the dimension ga:city indicates the city, for example, "Paris" or "New York", from which a session originates. | e.g. Add Dimension |  |

<details>
<summary><strong>Dimensions to split by sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Values | `dimensionValues` |  |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Simplify Output | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Dimension Filters in the request | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Dimension Filters | `dimensionFiltersUi` | fixedCollection | {} | Dimension Filters in the request |
| Hide Totals | `hideTotals` | boolean | False | Whether to hide the total of all metrics for all the matching rows, for every date range |
| Hide Value Ranges | `hideValueRanges` | boolean | False | Whether to hide the minimum and maximum across all matching rows |
| Include Empty Rows | `includeEmptyRows` | boolean | False | Whether the response exclude rows if all the retrieved metrics are equal to zero |
| Use Resource Quotas | `useResourceQuotas` | boolean | False | Whether to enable resource based quotas |

</details>


### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| View Name or ID | `viewId` | options |  | ✓ | The view from Google Analytics. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. 123456 |  |
| User ID | `userId` | string |  | ✓ | ID of a user | e.g. 123456 |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Type of activites requested | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Activity Types | `activityTypes` | multiOptions | [] | Type of activites requested |

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
node: googleAnalytics
displayName: Google Analytics
description: Use the Google Analytics API
version: '2'
nodeType: regular
group:
- transform
credentials:
- name: googleAnalyticsOAuth2
  required: true
operations:
- id: get
  name: Get
  description: Return the analytics data
  params:
  - id: propertyType
    name: Property Type
    type: options
    default: ga4
    required: false
    description: Google Analytics 4 is the latest version. Universal Analytics is
      an older version that is not fully functional after the end of June 2023.
    validation:
      displayOptions:
        show:
          resource:
          - report
          operation:
          - get
    typeInfo:
      type: options
      displayName: Property Type
      name: propertyType
      possibleValues:
      - value: ga4
        name: Google Analytics 4
        description: ''
      - value: universal
        name: Universal Analytics
        description: ''
  - id: propertyId
    name: Property
    type: resourceLocator
    default: ''
    required: true
    description: The Property of Google Analytics
    hint: If this doesn't work, try changing the 'Property Type' field above
    placeholder: Select a property...
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - report
          operation:
          - get
          propertyType:
          - ga4
    typeInfo:
      type: resourceLocator
      displayName: Property
      name: propertyId
  - id: dateRange
    name: Date Range
    type: options
    default: last7days
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - report
          operation:
          - get
          propertyType:
          - universal
    typeInfo: &id002
      type: options
      displayName: Date Range
      name: dateRange
      possibleValues:
      - value: last7days
        name: Last 7 Days
        description: ''
      - value: last30days
        name: Last 30 Days
        description: ''
      - value: today
        name: Today
        description: ''
      - value: yesterday
        name: Yesterday
        description: ''
      - value: lastCalendarWeek
        name: Last Complete Calendar Week
        description: ''
      - value: lastCalendarMonth
        name: Last Complete Calendar Month
        description: ''
      - value: custom
        name: Custom
        description: ''
  - id: startDate
    name: Start
    type: dateTime
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - report
          operation:
          - get
          propertyType:
          - universal
          dateRange:
          - custom
    typeInfo: &id004
      type: dateTime
      displayName: Start
      name: startDate
  - id: endDate
    name: End
    type: dateTime
    default: ''
    required: true
    description: ''
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - report
          operation:
          - get
          propertyType:
          - universal
          dateRange:
          - custom
    typeInfo: &id006
      type: dateTime
      displayName: End
      name: endDate
  - id: dimensionsGA4
    name: Dimensions to split by
    type: fixedCollection
    default: {}
    required: false
    description: Dimensions are attributes of your data. For example, the dimension
      city indicates the city from which an event originates. Dimension values in
      report responses are strings; for example, the city could be "Paris" or "New
      York". Requests are allowed up to 9 dimensions.
    placeholder: Add Dimension
    validation:
      displayOptions:
        show:
          resource:
          - report
          operation:
          - get
          propertyType:
          - ga4
    typeInfo:
      type: fixedCollection
      displayName: Dimensions to split by
      name: dimensionsGA4
      typeOptions:
        multipleValues: true
      subProperties:
      - name: dimensionValues
        displayName: Values
        values: []
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id007
      displayOptions:
        show:
          operation:
          - search
          resource:
          - userActivity
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
          operation:
          - search
          resource:
          - userActivity
          returnAll:
          - false
    typeInfo: &id010
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: simple
    name: Simplify Output
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id011
      displayOptions:
        show:
          operation:
          - get
          resource:
          - report
          propertyType:
          - universal
    typeInfo: &id012
      type: boolean
      displayName: Simplify Output
      name: simple
  - id: viewId
    name: View
    type: resourceLocator
    default: ''
    required: true
    description: The View of Google Analytics
    hint: If this doesn't work, try changing the 'Property Type' field above
    placeholder: Select a view...
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - userActivity
          operation:
          - search
    typeInfo: &id014
      type: options
      displayName: View Name or ID
      name: viewId
      typeOptions:
        loadOptionsMethod: getViews
      possibleValues: []
  - id: dateRange
    name: Date Range
    type: options
    default: last7days
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: startDate
    name: Start
    type: dateTime
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: endDate
    name: End
    type: dateTime
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: dimensionsUA
    name: Dimensions to split by
    type: fixedCollection
    default: {}
    required: false
    description: Dimensions are attributes of your data. For example, the dimension
      ga:city indicates the city, for example, "Paris" or "New York", from which a
      session originates.
    placeholder: Add Dimension
    validation:
      displayOptions:
        show:
          resource:
          - report
          operation:
          - get
          propertyType:
          - universal
    typeInfo:
      type: fixedCollection
      displayName: Dimensions to split by
      name: dimensionsUA
      typeOptions:
        multipleValues: true
      subProperties:
      - name: dimensionValues
        displayName: Values
        values: []
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
  - id: simple
    name: Simplify Output
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id011
    typeInfo: *id012
- id: search
  name: Search
  description: Return user activity data
  params:
  - id: viewId
    name: View Name or ID
    type: options
    default: ''
    required: true
    description: The view from Google Analytics. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    hint: If there's nothing here, try changing the 'Property type' field above
    placeholder: '123456'
    validation: *id013
    typeInfo: *id014
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: ID of a user
    placeholder: '123456'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - userActivity
          operation:
          - search
    typeInfo:
      type: string
      displayName: User ID
      name: userId
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: propertyId
    text: Select a property...
  - field: metricsGA4
    text: Add Metric
  - field: dimensionsGA4
    text: Add Dimension
  - field: additionalFields
    text: Add Field
  - field: dimensionFiltersUI
    text: Add Filter
  - field: expression
    text: Add Expression
  - field: metricsFiltersUI
    text: Add Filter
  - field: viewId
    text: Select a view...
  - field: metricsUA
    text: Add metric
  - field: dimensionsUA
    text: Add Dimension
  - field: additionalFields
    text: Add Field
  - field: viewId
    text: '123456'
  - field: userId
    text: '123456'
  - field: additionalFields
    text: Add Field
  hints:
  - field: propertyId
    text: If this doesn't work, try changing the 'Property Type' field above
  - field: name
    text: If expression is specified, name can be any string that you would like
  - field: expression
    text: Comma separated list of values. Must be non-empty.
  - field: viewId
    text: If this doesn't work, try changing the 'Property Type' field above
  - field: metricsUA
    text: If expression is specified, name can be any string that you would like
  - field: viewId
    text: If there's nothing here, try changing the 'Property type' field above
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
  "$id": "https://n8n.io/schemas/nodes/googleAnalytics.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Analytics Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "search"
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
            "report",
            "userActivity"
          ],
          "default": "report"
        },
        "operation": {
          "description": "Return user activity data",
          "type": "string",
          "enum": [
            "search"
          ],
          "default": "search"
        },
        "propertyType": {
          "description": "Google Analytics 4 is the latest version. Universal Analytics is an older version that is not fully functional after the end of June 2023.",
          "type": "string",
          "enum": [
            "ga4",
            "universal"
          ],
          "default": "ga4"
        },
        "propertyId": {
          "description": "The Property of Google Analytics",
          "type": "string",
          "examples": [
            "Select a property..."
          ]
        },
        "dateRange": {
          "description": "",
          "type": "string",
          "enum": [
            "last7days",
            "last30days",
            "today",
            "yesterday",
            "lastCalendarWeek",
            "lastCalendarMonth",
            "custom"
          ],
          "default": "last7days"
        },
        "startDate": {
          "description": "",
          "type": "string"
        },
        "endDate": {
          "description": "",
          "type": "string"
        },
        "metricsGA4": {
          "description": "The quantitative measurements of a report. For example, the metric eventCount is the total number of events. Requests are allowed up to 10 metrics.",
          "type": "string",
          "default": "",
          "examples": [
            "Add Metric"
          ]
        },
        "dimensionsGA4": {
          "description": "Dimensions are attributes of your data. For example, the dimension city indicates the city from which an event originates. Dimension values in report responses are strings; for example, the city could be \"Paris\" or \"New York\". Requests are allowed up to 9 dimensions.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Dimension"
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
          "default": 100
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "additionalFields": {
          "description": "Type of activites requested",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "listName": {
          "description": "",
          "type": "string",
          "enum": [
            "active1DayUsers",
            "active28DayUsers",
            "active7DayUsers",
            "checkouts",
            "eventCount",
            "screenPageViews",
            "userEngagementDuration",
            "sessions",
            "sessionsPerUser",
            "totalUsers",
            "other",
            "custom"
          ],
          "default": "totalUsers"
        },
        "name": {
          "description": "",
          "type": "string",
          "default": "custom_metric"
        },
        "dimensionFiltersUI": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "expression": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Expression"
          ]
        },
        "metricsFiltersUI": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "viewId": {
          "description": "The view from Google Analytics. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "123456"
          ]
        },
        "metricsUA": {
          "description": "Metrics in the request",
          "type": "string",
          "default": "ga:users",
          "examples": [
            "Add metric"
          ]
        },
        "dimensionsUA": {
          "description": "Dimensions are attributes of your data. For example, the dimension ga:city indicates the city, for example, \"Paris\" or \"New York\", from which a session originates.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Dimension"
          ]
        },
        "userId": {
          "description": "ID of a user",
          "type": "string",
          "default": "",
          "examples": [
            "123456"
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
    "version": "2"
  },
  "credentials": [
    {
      "name": "googleAnalyticsOAuth2",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 2 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
