---
title: "Node: Chargebee"
slug: "node-chargebee"
version: "1"
updated: "2025-11-13"
summary: "Retrieve data from Chargebee API"
node_type: "regular"
group: "['input']"
---

# Node: Chargebee

**Purpose.** Retrieve data from Chargebee API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:chargebee.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **chargebeeApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `chargebeeApi` | ✓ | - |

---

## Operations

### Customer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a customer |

### Invoice Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| List | `list` | Return the invoices |
| PDF Invoice URL | `pdfUrl` | Get URL for the invoice PDF |

### Subscription Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Cancel | `cancel` | Cancel a subscription |
| Delete | `delete` | Delete a subscription |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | invoice | ✗ | Resource to operate on |  |

**Resource options:**

* **Customer** (`customer`)
* **Invoice** (`invoice`)
* **Subscription** (`subscription`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a customer |  |

**Operation options:**

* **Create** (`create`) - Create a customer

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Properties | `properties` | collection | {} | ✗ | Properties to set on the new user | e.g. Add Property |  |

<details>
<summary><strong>Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| User ID | `id` | string |  | ID for the new customer. If not given, this will be auto-generated. |
| First Name | `first_name` | string |  | The first name of the customer |
| Last Name | `last_name` | string |  | The last name of the customer |
| Email | `email` | string |  | The email address of the customer |
| Phone | `phone` | string |  | The phone number of the customer |
| Company | `company` | string |  | The company of the customer |
| Custom Properties | `customProperties` | fixedCollection | {} | Adds a custom property to set also values which have not been predefined |

</details>


### List parameters (`list`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Max Results | `maxResults` | number | 10 | ✗ | Max. amount of results to return(< 100). | min:1, max:100 |
| Filters | `filters` | fixedCollection | {} | ✗ | Filter for invoices | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Invoice Date | `date` |  |  |  |
| Invoice Amount | `total` |  |  |  |

</details>


### PDF Invoice URL parameters (`pdfUrl`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Invoice ID | `invoiceId` | string |  | ✓ | The ID of the invoice to get |  |

### Cancel parameters (`cancel`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Subscription ID | `subscriptionId` | string |  | ✓ | The ID of the subscription to cancel |  |
| Schedule End of Term | `endOfTerm` | boolean | False | ✗ | Whether it will not cancel it directly in will instead schedule the cancelation for the end of the term |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Subscription ID | `subscriptionId` | string |  | ✓ | The ID of the subscription to delete |  |

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
* Categories: Finance & Accounting

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: chargebee
displayName: Chargebee
description: Retrieve data from Chargebee API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: chargebeeApi
  required: true
operations:
- id: create
  name: Create
  description: Create a customer
  params: []
- id: list
  name: List
  description: Return the invoices
  params:
  - id: maxResults
    name: Max Results
    type: number
    default: 10
    required: false
    description: Max. amount of results to return(< 100).
    validation:
      displayOptions:
        show:
          operation:
          - list
          resource:
          - invoice
    typeInfo:
      type: number
      displayName: Max Results
      name: maxResults
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: filters
    name: Filters
    type: fixedCollection
    default: {}
    required: false
    description: Filter for invoices
    placeholder: Add Filter
    validation:
      displayOptions:
        show:
          operation:
          - list
          resource:
          - invoice
    typeInfo:
      type: fixedCollection
      displayName: Filters
      name: filters
      typeOptions:
        multipleValues: true
      subProperties:
      - name: date
        displayName: Invoice Date
        values:
        - displayName: Operation
          name: operation
          type: options
          description: Operation to decide where the data should be mapped to
          value: is
          default: after
          noDataExpression: true
          options:
          - name: Is
            value: is
            displayName: Is
          - name: Is Not
            value: is_not
            displayName: Is Not
          - name: After
            value: after
            displayName: After
          - name: Before
            value: before
            displayName: Before
        - displayName: Date
          name: value
          type: dateTime
          description: Query date
          default: ''
      - name: total
        displayName: Invoice Amount
        values:
        - displayName: Operation
          name: operation
          type: options
          description: Operation to decide where the data should be mapped to
          value: gte
          default: gt
          noDataExpression: true
          options:
          - name: Greater Equal Than
            value: gte
            displayName: Greater Equal Than
          - name: Greater Than
            value: gt
            displayName: Greater Than
          - name: Is
            value: is
            displayName: Is
          - name: Is Not
            value: is_not
            displayName: Is Not
          - name: Less Equal Than
            value: lte
            displayName: Less Equal Than
          - name: Less Than
            value: lt
            displayName: Less Than
        - displayName: Amount
          name: value
          type: number
          description: Query amount
          default: 0
          typeOptions:
            numberPrecision: 2
- id: pdfUrl
  name: PDF Invoice URL
  description: Get URL for the invoice PDF
  params:
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: The ID of the invoice to get
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - pdfUrl
          resource:
          - invoice
    typeInfo:
      type: string
      displayName: Invoice ID
      name: invoiceId
- id: cancel
  name: Cancel
  description: Cancel a subscription
  params:
  - id: subscriptionId
    name: Subscription ID
    type: string
    default: ''
    required: true
    description: The ID of the subscription to cancel
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - delete
          resource:
          - subscription
    typeInfo: &id002
      type: string
      displayName: Subscription ID
      name: subscriptionId
  - id: endOfTerm
    name: Schedule End of Term
    type: boolean
    default: false
    required: false
    description: Whether it will not cancel it directly in will instead schedule the
      cancelation for the end of the term
    validation:
      displayOptions:
        show:
          operation:
          - cancel
          resource:
          - subscription
    typeInfo:
      type: boolean
      displayName: Schedule End of Term
      name: endOfTerm
- id: delete
  name: Delete
  description: Delete a subscription
  params:
  - id: subscriptionId
    name: Subscription ID
    type: string
    default: ''
    required: true
    description: The ID of the subscription to delete
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: properties
    text: Add Property
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/chargebee.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Chargebee Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "list",
        "pdfUrl",
        "cancel",
        "delete"
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
            "invoice",
            "subscription"
          ],
          "default": "invoice"
        },
        "operation": {
          "description": "Cancel a subscription",
          "type": "string",
          "enum": [
            "cancel",
            "delete"
          ],
          "default": "delete"
        },
        "properties": {
          "description": "Properties to set on the new user",
          "type": "string",
          "default": {},
          "examples": [
            "Add Property"
          ]
        },
        "maxResults": {
          "description": "Max. amount of results to return(< 100).",
          "type": "number",
          "default": 10
        },
        "filters": {
          "description": "Filter for invoices",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "invoiceId": {
          "description": "The ID of the invoice to get",
          "type": "string",
          "default": ""
        },
        "subscriptionId": {
          "description": "The ID of the subscription to delete",
          "type": "string",
          "default": ""
        },
        "endOfTerm": {
          "description": "Whether it will not cancel it directly in will instead schedule the cancelation for the end of the term",
          "type": "boolean",
          "default": false
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
      "name": "chargebeeApi",
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
