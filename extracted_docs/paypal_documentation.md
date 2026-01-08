---
title: "Node: PayPal"
slug: "node-paypal"
version: "1"
updated: "2026-01-08"
summary: "Consume PayPal API"
node_type: "regular"
group: "['output']"
---

# Node: PayPal

**Purpose.** Consume PayPal API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:paypal.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **payPalApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `payPalApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

---

## Operations

### Payout Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a batch payout |
| Get | `get` | Show batch payout details |

### Payoutitem Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Cancel | `cancel` | Cancels an unclaimed payout item |
| Get | `get` | Show payout item details |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | payout | ✗ | Resource to operate on |  |

**Resource options:**

* **Payout** (`payout`)
* **Payout Item** (`payoutItem`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a batch payout |  |

**Operation options:**

* **Create** (`create`) - Create a batch payout
* **Get** (`get`) - Show batch payout details

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Sender Batch ID | `senderBatchId` | string |  | ✓ | A sender-specified ID number. Tracks the payout in an accounting system. |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Items | `itemsUi` | fixedCollection | {} | ✓ | The unencrypted phone number | e.g. Add Item |  |

<details>
<summary><strong>Items sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Item | `itemsValues` |  |  |  |

</details>

| Items | `itemsJson` | json |  | ✗ | An array of individual payout items |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The subject line for the email that PayPal sends when payment for a payout item completes. The subject line is the same for all recipients. Max length: 255 characters. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email Subject | `emailSubject` | string |  | The subject line for the email that PayPal sends when payment for a payout item completes. The subject line is the same for all recipients. Max length: 255 characters. |
| Email Message | `emailMessage` | string |  | The email message that PayPal sends when the payout item completes. The message is the same for all recipients. |
| Note | `note` | string |  | The payouts and item-level notes are concatenated in the email. Max length: 1000 characters. |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Payout Batch ID | `payoutBatchId` | string |  | ✓ | The ID of the payout for which to show details |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:1000 |
| Payout Item ID | `payoutItemId` | string |  | ✓ | The ID of the payout item for which to show details |  |

### Cancel parameters (`cancel`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Payout Item ID | `payoutItemId` | string |  | ✓ | The ID of the payout item to cancel |  |

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
* Categories: Finance & Accounting, Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: payPal
displayName: PayPal
description: Consume PayPal API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: payPalApi
  required: true
operations:
- id: create
  name: Create
  description: Create a batch payout
  params:
  - id: senderBatchId
    name: Sender Batch ID
    type: string
    default: ''
    required: true
    description: A sender-specified ID number. Tracks the payout in an accounting
      system.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - payout
          operation:
          - create
    typeInfo:
      type: string
      displayName: Sender Batch ID
      name: senderBatchId
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - payout
          operation:
          - create
    typeInfo:
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: itemsUi
    name: Items
    type: fixedCollection
    default: {}
    required: true
    description: The unencrypted phone number
    placeholder: Add Item
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - payout
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: fixedCollection
      displayName: Items
      name: itemsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: itemsValues
        displayName: Item
        values:
        - displayName: Recipient Type
          name: recipientType
          type: options
          description: The unencrypted phone number
          value: phone
          default: email
          options:
          - name: Phone
            description: The unencrypted phone number
            value: phone
            displayName: Phone
          - name: Email
            description: The unencrypted email
            value: email
            displayName: Email
          - name: PayPal ID
            description: The encrypted PayPal account number
            value: paypalId
            displayName: Pay Pal Id
        - displayName: Receiver Value
          name: receiverValue
          type: string
          description: 'The receiver of the payment. Corresponds to the recipient_type
            value in the request. Max length: 127 characters.'
          default: ''
          required: true
        - displayName: Currency
          name: currency
          type: options
          value: AUD
          default: USD
          options:
          - name: Australian Dollar
            value: AUD
            displayName: Australian Dollar
          - name: Brazilian Real
            value: BRL
            displayName: Brazilian Real
          - name: Canadian Dollar
            value: CAD
            displayName: Canadian Dollar
          - name: Czech Koruna
            value: CZK
            displayName: Czech Koruna
          - name: Danish Krone
            value: DKK
            displayName: Danish Krone
          - name: Euro
            value: EUR
            displayName: Euro
          - name: United States Dollar
            value: USD
            displayName: United States Dollar
        - displayName: Amount
          name: amount
          type: string
          description: The value, which might be
          default: ''
          required: true
        - displayName: Note
          name: note
          type: string
          description: The sender-specified note for notifications. Supports up to
            4000 ASCII characters and 1000 non-ASCII characters.
          default: ''
        - displayName: Sender Item ID
          name: senderItemId
          type: string
          description: The sender-specified ID number. Tracks the payout in an accounting
            system.
          default: ''
        - displayName: Recipient Wallet
          name: recipientWallet
          type: options
          description: PayPal Wallet
          value: paypal
          default: paypal
          options:
          - name: PayPal
            description: PayPal Wallet
            value: paypal
            displayName: Pay Pal
          - name: Venmo
            description: Venmo Wallet
            value: venmo
            displayName: Venmo
  - id: itemsJson
    name: Items
    type: json
    default: ''
    required: false
    description: An array of individual payout items
    validation:
      displayOptions:
        show:
          resource:
          - payout
          operation:
          - create
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Items
      name: itemsJson
      typeOptions:
        alwaysOpenEditWindow: true
- id: get
  name: Get
  description: Show batch payout details
  params:
  - id: payoutBatchId
    name: Payout Batch ID
    type: string
    default: ''
    required: true
    description: The ID of the payout for which to show details
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - payout
          operation:
          - get
    typeInfo:
      type: string
      displayName: Payout Batch ID
      name: payoutBatchId
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          resource:
          - payout
          operation:
          - get
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          resource:
          - payout
          operation:
          - get
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 1000
  - id: payoutItemId
    name: Payout Item ID
    type: string
    default: ''
    required: true
    description: The ID of the payout item for which to show details
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - payoutItem
          operation:
          - cancel
    typeInfo: &id002
      type: string
      displayName: Payout Item ID
      name: payoutItemId
- id: cancel
  name: Cancel
  description: Cancels an unclaimed payout item
  params:
  - id: payoutItemId
    name: Payout Item ID
    type: string
    default: ''
    required: true
    description: The ID of the payout item to cancel
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - POST
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: itemsUi
    text: Add Item
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
  "$id": "https://n8n.io/schemas/nodes/payPal.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "PayPal Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "get",
        "cancel"
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
            "payout",
            "payoutItem"
          ],
          "default": "payout"
        },
        "operation": {
          "description": "Cancels an unclaimed payout item",
          "type": "string",
          "enum": [
            "cancel",
            "get"
          ],
          "default": "get"
        },
        "senderBatchId": {
          "description": "A sender-specified ID number. Tracks the payout in an accounting system.",
          "type": "string",
          "default": ""
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "itemsUi": {
          "description": "The unencrypted phone number",
          "type": "string",
          "default": {},
          "examples": [
            "Add Item"
          ]
        },
        "itemsJson": {
          "description": "An array of individual payout items",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The subject line for the email that PayPal sends when payment for a payout item completes. The subject line is the same for all recipients. Max length: 255 characters.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "payoutBatchId": {
          "description": "The ID of the payout for which to show details",
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
          "default": 100
        },
        "payoutItemId": {
          "description": "The ID of the payout item to cancel",
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
      "name": "payPalApi",
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
