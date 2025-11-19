---
title: "Node: Google Ads"
slug: "node-googleads"
version: "1"
updated: "2025-11-13"
summary: "Use the Google Ads API"
node_type: "regular"
group: "['transform']"
---

# Node: Google Ads

**Purpose.** Use the Google Ads API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:googleAds.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleAdsOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **campaigsNotice** when resource=['campaign']: Divide field names expressed with <i>micros</i> by 1,000,000 to get the actual value

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleAdsOAuth2Api` | ✓ | - |

---

## Operations

### Campaign Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | campaign | ✗ | Resource to operate on |  |

**Resource options:**

* **Campaign** (`campaign`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | campaign | ✗ |  |  |

**Resource options:**

* **Campaign** (`campaign`)

| Operation | `operation` | options | getAll | ✗ | Get many campaigns linked to the specified account |  |
| Manager Customer ID | `managerCustomerId` | string |  | ✓ | e.g. 9998887777 |  |
| Client Customer ID | `clientCustomerId` | string |  | ✓ | e.g. 6665554444 |  |
| Campaign ID | `campaignId` | string |  | ✓ | ID of the campaign |  |
| Additional Options | `additionalOptions` | collection | {} | ✗ | Additional options for fetching campaigns | e.g. Add option |  |

<details>
<summary><strong>Additional Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date Range | `dateRange` | options | allTime | Filters statistics by period |
| Show Campaigns by Status | `campaignStatus` | options | all | Filters campaigns by status |

</details>


---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Get

**From workflow:** Google Ads Get

**Parameters:**
```json
{
  "operation": "get",
  "managerCustomerId": "111-222-3333",
  "clientCustomerId": "444-555-6666",
  "campaignId": "12345678901",
  "requestOptions": {}
}
```

**Credentials:**
- googleAdsOAuth2Api: `Google Ads account`

### Example 2: Get Many

**From workflow:** Google Ads Get Many

**Parameters:**
```json
{
  "managerCustomerId": "111-222-3333",
  "clientCustomerId": "444-555-6666",
  "additionalOptions": {},
  "requestOptions": {}
}
```

**Credentials:**
- googleAdsOAuth2Api: `Google Ads account`

### Example 3: With Options

**From workflow:** Google Ads Get Many

**Parameters:**
```json
{
  "managerCustomerId": "111-222-3333",
  "clientCustomerId": "444-555-6666",
  "additionalOptions": {
    "dateRange": "LAST_7_DAYS",
    "campaignStatus": "ENABLED"
  },
  "requestOptions": {}
}
```

**Credentials:**
- googleAdsOAuth2Api: `Google Ads account`

### Example 4: No Results

**From workflow:** Google Ads Get Many

**Parameters:**
```json
{
  "managerCustomerId": "111-222-3333",
  "clientCustomerId": "444-555-6666",
  "additionalOptions": {
    "campaignStatus": "REMOVED"
  },
  "requestOptions": {}
}
```

**Credentials:**
- googleAdsOAuth2Api: `Google Ads account`


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$credentials.developerToken}}`
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
* Categories: Analytics

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleAds
displayName: Google Ads
description: Use the Google Ads API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: googleAdsOAuth2Api
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: campaign
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: campaign
      name: Campaign
      description: ''
- id: operation
  name: Operation
  type: options
  default: getAll
  required: false
  description: Get many campaigns linked to the specified account
  validation:
    displayOptions:
      show:
        resource:
        - campaign
  typeInfo:
    type: options
    displayName: Operation
    name: operation
    possibleValues: []
- id: managerCustomerId
  name: Manager Customer ID
  type: string
  default: ''
  required: true
  description: ''
  placeholder: '9998887777'
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - campaign
  typeInfo:
    type: string
    displayName: Manager Customer ID
    name: managerCustomerId
- id: clientCustomerId
  name: Client Customer ID
  type: string
  default: ''
  required: true
  description: ''
  placeholder: '6665554444'
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - campaign
  typeInfo:
    type: string
    displayName: Client Customer ID
    name: clientCustomerId
- id: campaignId
  name: Campaign ID
  type: string
  default: ''
  required: true
  description: ID of the campaign
  validation:
    required: true
    displayOptions:
      show:
        operation:
        - get
        resource:
        - campaign
  typeInfo:
    type: string
    displayName: Campaign ID
    name: campaignId
- id: additionalOptions
  name: Additional Options
  type: collection
  default: {}
  required: false
  description: Additional options for fetching campaigns
  placeholder: Add option
  validation:
    displayOptions:
      show:
        resource:
        - campaign
        operation:
        - getAll
  typeInfo:
    type: collection
    displayName: Additional Options
    name: additionalOptions
    subProperties:
    - displayName: Date Range
      name: dateRange
      type: options
      description: Filters statistics by period
      value: allTime
      default: allTime
      options:
      - name: All Time
        description: Fetch statistics for all period
        value: allTime
        displayName: All Time
      - name: Today
        description: Today only
        value: TODAY
        displayName: Today
      - name: Yesterday
        description: Yesterday only
        value: YESTERDAY
        displayName: Yesterday
      - name: Last 7 Days
        description: Last 7 days, not including today
        value: LAST_7_DAYS
        displayName: Last 7 Days
      - name: Last Business Week
        description: The 5 day business week, Monday through Friday, of the previous
          business week
        value: LAST_BUSINESS_WEEK
        displayName: Last Business Week
      - name: This Month
        description: All days in the current month
        value: THIS_MONTH
        displayName: This Month
      - name: Last Month
        description: All days in the previous month
        value: LAST_MONTH
        displayName: Last Month
      - name: Last 14 Days
        description: The last 14 days not including today
        value: LAST_14_DAYS
        displayName: Last 14 Days
      - name: Last 30 Days
        description: The last 30 days not including today
        value: LAST_30_DAYS
        displayName: Last 30 Days
    - displayName: Show Campaigns by Status
      name: campaignStatus
      type: options
      description: Filters campaigns by status
      value: all
      default: all
      options:
      - name: All
        description: Fetch all campaigns regardless of status
        value: all
        displayName: All
      - name: Enabled
        description: Filter only active campaigns
        value: ENABLED
        displayName: Enabled
      - name: Paused
        description: Filter only paused campaigns
        value: PAUSED
        displayName: Paused
      - name: Removed
        description: Filter only removed campaigns
        value: REMOVED
        displayName: Removed
examples:
- name: Get
  parameters:
    operation: get
    managerCustomerId: 111-222-3333
    clientCustomerId: 444-555-6666
    campaignId: '12345678901'
    requestOptions: {}
  workflow: Google Ads Get
- name: Get Many
  parameters:
    managerCustomerId: 111-222-3333
    clientCustomerId: 444-555-6666
    additionalOptions: {}
    requestOptions: {}
  workflow: Google Ads Get Many
- name: With Options
  parameters:
    managerCustomerId: 111-222-3333
    clientCustomerId: 444-555-6666
    additionalOptions:
      dateRange: LAST_7_DAYS
      campaignStatus: ENABLED
    requestOptions: {}
  workflow: Google Ads Get Many
common_expressions:
- ={{$credentials.developerToken}}
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices:
  - name: campaigsNotice
    text: Divide field names expressed with <i>micros</i> by 1,000,000 to get the
      actual value
    conditions:
      show:
        resource:
        - campaign
  tooltips: []
  placeholders:
  - field: managerCustomerId
    text: '9998887777'
  - field: clientCustomerId
    text: '6665554444'
  - field: additionalOptions
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/googleAds.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Ads Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "campaign"
          ],
          "default": "campaign"
        },
        "operation": {
          "description": "Get many campaigns linked to the specified account",
          "type": "string",
          "default": "getAll"
        },
        "managerCustomerId": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "9998887777"
          ]
        },
        "clientCustomerId": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "6665554444"
          ]
        },
        "campaignId": {
          "description": "ID of the campaign",
          "type": "string",
          "default": ""
        },
        "additionalOptions": {
          "description": "Additional options for fetching campaigns",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
      "name": "googleAdsOAuth2Api",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Get",
      "value": {
        "operation": "get",
        "managerCustomerId": "111-222-3333",
        "clientCustomerId": "444-555-6666",
        "campaignId": "12345678901",
        "requestOptions": {}
      }
    },
    {
      "description": "Get Many",
      "value": {
        "managerCustomerId": "111-222-3333",
        "clientCustomerId": "444-555-6666",
        "additionalOptions": {},
        "requestOptions": {}
      }
    },
    {
      "description": "With Options",
      "value": {
        "managerCustomerId": "111-222-3333",
        "clientCustomerId": "444-555-6666",
        "additionalOptions": {
          "dateRange": "LAST_7_DAYS",
          "campaignStatus": "ENABLED"
        },
        "requestOptions": {}
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
