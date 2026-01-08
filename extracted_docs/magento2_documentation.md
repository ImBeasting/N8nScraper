---
title: "Node: Magento 2"
slug: "node-magento2"
version: "1"
updated: "2026-01-08"
summary: "Consume Magento API"
node_type: "regular"
group: "['input']"
---

# Node: Magento 2

**Purpose.** Consume Magento API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:magento.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **magento2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `magento2Api` | ✓ | - |

---

## Operations

### Customer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new customer |
| Delete | `delete` | Delete a customer |
| Get | `get` | Get a customer |
| Get Many | `getAll` | Get many customers |
| Update | `update` | Update a customer |

### Invoice Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an invoice |

### Order Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Cancel | `cancel` | Cancel an order |
| Get | `get` | Get an order |
| Get Many | `getAll` | Get many orders |
| Ship | `ship` | Ship an order |

### Product Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a product |
| Delete | `delete` | Delete a product |
| Get | `get` | Get a product |
| Get Many | `getAll` | Get many products |
| Update | `update` | Update a product |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | customer | ✗ | Resource to operate on |  |

**Resource options:**

* **Customer** (`customer`)
* **Invoice** (`invoice`)
* **Order** (`order`)
* **Product** (`product`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a new customer |  |

**Operation options:**

* **Create** (`create`) - Create a new customer
* **Delete** (`delete`) - Delete a customer
* **Get** (`get`) - Get a customer
* **Get Many** (`getAll`) - Get many customers
* **Update** (`update`) - Update a customer

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | Email address of the user to create | e.g. name@email.com | email |
| First Name | `firstname` | string |  | ✓ | First name of the user to create |  |
| Last Name | `lastname` | string |  | ✓ | Last name of the user to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Order ID | `orderId` | string |  | ✓ |  |  |
| SKU | `sku` | string |  | ✓ | Stock-keeping unit of the product |  |
| Name | `name` | string |  | ✓ |  |  |
| Attribute Set Name or ID | `attributeSetId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Price | `price` | number | 0 | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Customer ID | `customerId` | string |  | ✓ |  |  |
| SKU | `sku` | string |  | ✓ | Stock-keeping unit of the product |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Customer ID | `customerId` | string |  | ✓ |  |  |
| Order ID | `orderId` | string |  | ✓ |  |  |
| SKU | `sku` | string |  | ✓ | Stock-keeping unit of the product |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Customer ID | `customerId` | string |  | ✗ | ID of the customer to update |  |
| Email | `email` | string |  | ✗ | e.g. name@email.com | email |
| First Name | `firstName` | string |  | ✗ |  |  |
| Last Name | `lastName` | string |  | ✗ |  |  |
| Website Name or ID | `website_id` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |
| SKU | `sku` | string |  | ✓ | Stock-keeping unit of the product |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |

### Cancel parameters (`cancel`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Order ID | `orderId` | string |  | ✓ |  |  |

### Ship parameters (`ship`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Order ID | `orderId` | string |  | ✓ |  |  |

---

## Load Options Methods

- `getCountries`
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
* Categories: Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: magento2
displayName: Magento 2
description: Consume Magento API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: magento2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a new customer
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email address of the user to create
    placeholder: name@email.com
    validation: &id011
      format: email
      displayOptions:
        show:
          resource:
          - customer
          operation:
          - update
    typeInfo: &id012
      type: string
      displayName: Email
      name: email
  - id: firstname
    name: First Name
    type: string
    default: ''
    required: true
    description: First name of the user to create
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - customer
          operation:
          - create
    typeInfo:
      type: string
      displayName: First Name
      name: firstname
  - id: lastname
    name: Last Name
    type: string
    default: ''
    required: true
    description: Last name of the user to create
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - customer
          operation:
          - create
    typeInfo:
      type: string
      displayName: Last Name
      name: lastname
  - id: orderId
    name: Order ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - order
          operation:
          - cancel
          - get
          - ship
    typeInfo: &id006
      type: string
      displayName: Order ID
      name: orderId
  - id: sku
    name: SKU
    type: string
    default: ''
    required: true
    description: Stock-keeping unit of the product
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - product
          operation:
          - delete
          - get
    typeInfo: &id002
      type: string
      displayName: SKU
      name: sku
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - product
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: attributeSetId
    name: Attribute Set Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      displayOptions:
        show:
          resource:
          - product
          operation:
          - create
    typeInfo:
      type: options
      displayName: Attribute Set Name or ID
      name: attributeSetId
      typeOptions:
        loadOptionsMethod: getAttributeSets
      possibleValues: []
  - id: price
    name: Price
    type: number
    default: 0
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - product
          operation:
          - create
    typeInfo:
      type: number
      displayName: Price
      name: price
- id: delete
  name: Delete
  description: Delete a customer
  params:
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - customer
          operation:
          - delete
          - get
    typeInfo: &id004
      type: string
      displayName: Customer ID
      name: customerId
  - id: sku
    name: SKU
    type: string
    default: ''
    required: true
    description: Stock-keeping unit of the product
    validation: *id001
    typeInfo: *id002
- id: get
  name: Get
  description: Get a customer
  params:
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: orderId
    name: Order ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: sku
    name: SKU
    type: string
    default: ''
    required: true
    description: Stock-keeping unit of the product
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many customers
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
          - product
          operation:
          - getAll
    typeInfo: &id008
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation: &id009
      displayOptions:
        show:
          resource:
          - product
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
        maxValue: 10
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
    default: 5
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
    default: 5
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
- id: update
  name: Update
  description: Update a customer
  params:
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: false
    description: ID of the customer to update
    validation: *id003
    typeInfo: *id004
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: ''
    placeholder: name@email.com
    validation: *id011
    typeInfo: *id012
  - id: firstName
    name: First Name
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - customer
          operation:
          - update
    typeInfo:
      type: string
      displayName: First Name
      name: firstName
  - id: lastName
    name: Last Name
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - customer
          operation:
          - update
    typeInfo:
      type: string
      displayName: Last Name
      name: lastName
  - id: website_id
    name: Website Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      displayOptions:
        show:
          resource:
          - customer
          operation:
          - update
    typeInfo:
      type: options
      displayName: Website Name or ID
      name: website_id
      typeOptions:
        loadOptionsMethod: getWebsites
      possibleValues: []
  - id: sku
    name: SKU
    type: string
    default: ''
    required: true
    description: Stock-keeping unit of the product
    validation: *id001
    typeInfo: *id002
- id: cancel
  name: Cancel
  description: Cancel an order
  params:
  - id: orderId
    name: Order ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
- id: ship
  name: Ship
  description: Ship an order
  params:
  - id: orderId
    name: Order ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
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
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: updateFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/magento2.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Magento 2 Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "get",
        "getAll",
        "update",
        "cancel",
        "ship"
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
            "order",
            "product"
          ],
          "default": "customer"
        },
        "operation": {
          "description": "Create a product",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "email": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "firstname": {
          "description": "First name of the user to create",
          "type": "string",
          "default": ""
        },
        "lastname": {
          "description": "Last name of the user to create",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "customerId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "firstName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "lastName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "website_id": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "",
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
          "default": 5
        },
        "orderId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "sku": {
          "description": "Stock-keeping unit of the product",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "attributeSetId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "price": {
          "description": "",
          "type": "number",
          "default": 0
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
      "name": "magento2Api",
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
