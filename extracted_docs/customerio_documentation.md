---
title: "Node: Customer.io"
slug: "node-customerio"
version: "1"
updated: "2025-11-13"
summary: "Consume Customer.io API"
node_type: "regular"
group: "['output']"
---

# Node: Customer.io

**Purpose.** Consume Customer.io API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:customerio.svg', 'dark': 'file:customerio.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **customerIoApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `customerIoApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Campaign Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a campaign |
| Get Many | `getAll` | Get many campaigns |
| Get Metrics | `getMetrics` | Get metrics for a campaign |

### Customer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create or Update | `upsert` | Create a new customer, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a customer |

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Track | `track` | Track a customer event |
| Track Anonymous | `trackAnonymous` | Track an anonymous event |

### Segment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Customer | `add` | Add a customer to a segment |
| Remove Customer | `remove` | Remove a customer from a segment |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | customer | ✗ | Resource to operate on |  |

**Resource options:**

* **Customer** (`customer`)
* **Event** (`event`)
* **Campaign** (`campaign`)
* **Segment** (`segment`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Get** (`get`) - Get a campaign
* **Get Many** (`getAll`) - Get many campaigns
* **Get Metrics** (`getMetrics`) - Get metrics for a campaign

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign ID | `campaignId` | number | 0 | ✓ | The unique identifier for the campaign |  |

### Get Metrics parameters (`getMetrics`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign ID | `campaignId` | number | 0 | ✓ | The unique identifier for the campaign |  |
| Period | `period` | options | days | ✗ | Specify metric period |  |

**Period options:**

* **Hours** (`hours`)
* **Days** (`days`)
* **Weeks** (`weeks`)
* **Months** (`months`)

| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Integer specifying how many steps to return. Defaults to the maximum number of timeperiods available, or 12 when using the months period. Maximum timeperiods available are 24 hours, 45 days, 12 weeks and 120 months | e.g. Add Field | min:0, max:120 |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Steps | `steps` | number | 0 | Integer specifying how many steps to return. Defaults to the maximum number of timeperiods available, or 12 when using the months period. Maximum timeperiods available are 24 hours, 45 days, 12 weeks and 120 months |
| Type | `type` | options | empty | Specify metric type |

</details>


### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The unique identifier for the customer |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-companys---companies-api">here</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Property name | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Properties | `customProperties` | fixedCollection | {} | Property name |
| Email | `email` | string |  | The email address of the user |
| Created At | `createdAt` | dateTime |  | The UNIX timestamp from when the user was created |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The unique identifier for the customer |  |

### Track parameters (`track`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Customer ID | `customerId` | string |  | ✓ | The unique identifier for the customer |  |
| Event Name | `eventName` | string |  | ✗ | Name of the event to track |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Object of values to set as described <a href="https://customer.io/docs/api-triggered-data-format#basic-data-formatting">here</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Custom Properties | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Attributes | `customAttributes` | fixedCollection | {} | Custom Properties |
| Type | `type` | string |  | Used to change event type. For Page View events set to "page". |

</details>


### Track Anonymous parameters (`trackAnonymous`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event Name | `eventName` | string |  | ✓ | The unique identifier for the customer |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFieldsJson` | json |  | ✗ | Object of values to set as described <a href="https://customer.io/docs/api-triggered-data-format#basic-data-formatting">here</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Custom Properties | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Attributes | `customAttributes` | fixedCollection | {} | Custom Properties |

</details>


### Add Customer parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Segment ID | `segmentId` | number | 0 | ✓ | The unique identifier of the segment |  |
| Customer IDs | `customerIds` | string |  | ✓ | A list of customer IDs to add to the segment |  |

### Remove Customer parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Segment ID | `segmentId` | number | 0 | ✓ | The unique identifier of the segment |  |
| Customer IDs | `customerIds` | string |  | ✓ | A list of customer IDs to add to the segment |  |

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
node: customerIo
displayName: Customer.io
description: Consume Customer.io API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: customerIoApi
  required: true
operations:
- id: get
  name: Get
  description: ''
  params:
  - id: campaignId
    name: Campaign ID
    type: number
    default: 0
    required: true
    description: The unique identifier for the campaign
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - getMetrics
    typeInfo: &id002
      type: number
      displayName: Campaign ID
      name: campaignId
- id: getAll
  name: Get Many
  description: ''
- id: getMetrics
  name: Get Metrics
  description: ''
  params:
  - id: campaignId
    name: Campaign ID
    type: number
    default: 0
    required: true
    description: The unique identifier for the campaign
    validation: *id001
    typeInfo: *id002
  - id: period
    name: Period
    type: options
    default: days
    required: false
    description: Specify metric period
    validation:
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - getMetrics
    typeInfo:
      type: options
      displayName: Period
      name: period
      possibleValues:
      - value: hours
        name: Hours
        description: ''
      - value: days
        name: Days
        description: ''
      - value: weeks
        name: Weeks
        description: ''
      - value: months
        name: Months
        description: ''
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id003
      displayOptions:
        show:
          resource:
          - event
          operation:
          - trackAnonymous
    typeInfo: &id004
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
- id: upsert
  name: Create or Update
  description: Create a new customer, or update the current one if it already exists
    (upsert)
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The unique identifier for the customer
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - customer
          operation:
          - upsert
    typeInfo: &id006
      type: string
      displayName: ID
      name: id
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Object of values to set as described <a href="https://github.com/agilecrm/rest-api#1-companys---companies-api">here</a>
    validation: &id007
      displayOptions:
        show:
          resource:
          - event
          operation:
          - trackAnonymous
          jsonParameters:
          - true
    typeInfo: &id008
      type: json
      displayName: Additional Fields
      name: additionalFieldsJson
      typeOptions:
        alwaysOpenEditWindow: true
- id: delete
  name: Delete
  description: Delete a customer
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The unique identifier for the customer
    validation: *id005
    typeInfo: *id006
- id: track
  name: Track
  description: Track a customer event
  params:
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: The unique identifier for the customer
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - event
          operation:
          - track
    typeInfo:
      type: string
      displayName: Customer ID
      name: customerId
  - id: eventName
    name: Event Name
    type: string
    default: ''
    required: false
    description: Name of the event to track
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - event
          operation:
          - trackAnonymous
    typeInfo: &id010
      type: string
      displayName: Event Name
      name: eventName
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Object of values to set as described <a href="https://customer.io/docs/api-triggered-data-format#basic-data-formatting">here</a>
    validation: *id007
    typeInfo: *id008
- id: trackAnonymous
  name: Track Anonymous
  description: Track an anonymous event
  params:
  - id: eventName
    name: Event Name
    type: string
    default: ''
    required: true
    description: The unique identifier for the customer
    validation: *id009
    typeInfo: *id010
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: additionalFieldsJson
    name: Additional Fields
    type: json
    default: ''
    required: false
    description: Object of values to set as described <a href="https://customer.io/docs/api-triggered-data-format#basic-data-formatting">here</a>
    validation: *id007
    typeInfo: *id008
- id: add
  name: Add Customer
  description: ''
  params:
  - id: segmentId
    name: Segment ID
    type: number
    default: 0
    required: true
    description: The unique identifier of the segment
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - segment
          operation:
          - add
          - remove
    typeInfo: &id012
      type: number
      displayName: Segment ID
      name: segmentId
  - id: customerIds
    name: Customer IDs
    type: string
    default: ''
    required: true
    description: A list of customer IDs to add to the segment
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - segment
          operation:
          - add
          - remove
    typeInfo: &id014
      type: string
      displayName: Customer IDs
      name: customerIds
- id: remove
  name: Remove Customer
  description: ''
  params:
  - id: segmentId
    name: Segment ID
    type: number
    default: 0
    required: true
    description: The unique identifier of the segment
    validation: *id011
    typeInfo: *id012
  - id: customerIds
    name: Customer IDs
    type: string
    default: ''
    required: true
    description: A list of customer IDs to add to the segment
    validation: *id013
    typeInfo: *id014
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
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
  "$id": "https://n8n.io/schemas/nodes/customerIo.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Customer.io Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll",
        "getMetrics",
        "upsert",
        "delete",
        "track",
        "trackAnonymous",
        "add",
        "remove"
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
            "customer",
            "event",
            "campaign",
            "segment"
          ],
          "default": "customer"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "add",
            "remove"
          ],
          "default": "add"
        },
        "campaignId": {
          "description": "The unique identifier for the campaign",
          "type": "number",
          "default": 0
        },
        "period": {
          "description": "Specify metric period",
          "type": "string",
          "enum": [
            "hours",
            "days",
            "weeks",
            "months"
          ],
          "default": "days"
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "additionalFields": {
          "description": "Custom Properties",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "id": {
          "description": "The unique identifier for the customer",
          "type": "string",
          "default": ""
        },
        "additionalFieldsJson": {
          "description": "Object of values to set as described <a href=\"https://customer.io/docs/api-triggered-data-format#basic-data-formatting\">here</a>",
          "type": "string",
          "default": ""
        },
        "customerId": {
          "description": "The unique identifier for the customer",
          "type": "string",
          "default": ""
        },
        "eventName": {
          "description": "The unique identifier for the customer",
          "type": "string",
          "default": ""
        },
        "segmentId": {
          "description": "The unique identifier of the segment",
          "type": "number",
          "default": 0
        },
        "customerIds": {
          "description": "A list of customer IDs to add to the segment",
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
      "name": "customerIoApi",
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
