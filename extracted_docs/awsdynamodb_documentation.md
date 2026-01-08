---
title: "Node: AWS DynamoDB"
slug: "node-awsdynamodb"
version: "1"
updated: "2026-01-08"
summary: "Consume the AWS DynamoDB API"
node_type: "regular"
group: "['transform']"
---

# Node: AWS DynamoDB

**Purpose.** Consume the AWS DynamoDB API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:dynamodb.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Operations

### Item Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete an item |
| Get | `get` | Get an item |
| Get Many | `getAll` | Get many items |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | item | ✗ | Resource to operate on |  |

**Resource options:**

* **Item** (`item`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | upsert | ✗ | Create a new record, or update the current one if it already exists (upsert) |  |

**Operation options:**

* **Create or Update** (`upsert`) - Create a new record, or update the current one if it already exists (upsert)
* **Delete** (`delete`) - Delete an item
* **Get** (`get`) - Get an item
* **Get Many** (`getAll`) - Get many items

---

### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Data to Send | `dataToSend` | options | defineBelow | ✗ | Use when node input properties match destination column names |  |

**Data to Send options:**

* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names
* **Define Below for Each Column** (`defineBelow`) - Set the value for each destination column

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Fields to Send | `fieldsUi` | fixedCollection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `fieldValues` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✓ | Substitution tokens for attribute names in an expression. Only needed when the parameter "condition expression" is set. | e.g. Add Field | min:1, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Expression Attribute Values | `eavUi` | fixedCollection | {} | Substitution tokens for attribute names in an expression. Only needed when the parameter "condition expression" is set. |
| Condition Expression | `conditionExpression` | string |  | A condition that must be satisfied in order for a conditional upsert to succeed. <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html">View details</a>. |
| Expression Attribute Names | `eanUi` | fixedCollection | {} | One or more substitution tokens for attribute names in an expression. <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html">View details</a>. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return | `returnValues` | options | NONE | ✗ | The content of the old item is returned |  |

**Return options:**

* **Attribute Values** (`ALL_OLD`) - The content of the old item is returned
* **Nothing** (`NONE`) - Nothing is returned

| Keys | `keysUi` | fixedCollection | {} | ✗ | Item's primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key. | e.g. Add Key |  |

<details>
<summary><strong>Keys sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Key | `keyValues` |  |  |  |

</details>

| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | A condition that must be satisfied in order for a conditional delete to succeed | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Condition Expression | `conditionExpression` | string |  | A condition that must be satisfied in order for a conditional delete to succeed |
| Expression Attribute Names | `eanUi` | fixedCollection | {} | One or more substitution tokens for attribute names in an expression. Check <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html">Info</a>. |
| Expression Attribute Values | `expressionAttributeUi` | fixedCollection | {} | Substitution tokens for attribute names in an expression. Only needed when the parameter "condition expression" is set. |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Select | `select` | options | ALL_ATTRIBUTES | ✗ | Select them in Attributes to Select under Additional Fields |  |

**Select options:**

* **All Attributes** (`ALL_ATTRIBUTES`)
* **All Projected Attributes** (`ALL_PROJECTED_ATTRIBUTES`)
* **Specific Attributes** (`SPECIFIC_ATTRIBUTES`) - Select them in Attributes to Select under Additional Fields

| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Keys | `keysUi` | fixedCollection | {} | ✗ | Item's primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key. | e.g. Add Key |  |

<details>
<summary><strong>Keys sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Key | `keyValues` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | One or more substitution tokens for attribute names in an expression. <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html">View details</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attributes to Select | `projectionExpression` | string |  |  |
| Expression Attribute Names | `eanUi` | fixedCollection | {} | One or more substitution tokens for attribute names in an expression. <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html">View details</a>. |
| Read Type | `readType` | options | eventuallyConsistentRead | Type of read to perform on the table. <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html">View details</a>. |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Scan | `scan` | boolean | False | ✗ | Whether to do an scan or query. Check <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html" >differences</a>. |  |
| Key Condition Expression | `keyConditionExpression` | string |  | ✓ | Condition to determine the items to be retrieved. The condition must perform an equality test on a single partition key value, in this format: <code>partitionKeyName = :partitionkeyval</code> | e.g. id = :id |  |
| Expression Attribute Values | `eavUi` | fixedCollection | {} | ✓ | Substitution tokens for attribute names in an expression | e.g. Add Attribute Value | min:1, max:∞ |

<details>
<summary><strong>Expression Attribute Values sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Expression Attribute Vaue | `eavValues` |  |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Select | `select` | options | ALL_ATTRIBUTES | ✗ | Select them in Attributes to Select under Additional Fields |  |

**Select options:**

* **All Attributes** (`ALL_ATTRIBUTES`)
* **All Projected Attributes** (`ALL_PROJECTED_ATTRIBUTES`)
* **Count** (`COUNT`)
* **Specific Attributes** (`SPECIFIC_ATTRIBUTES`) - Select them in Attributes to Select under Additional Fields

| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Name of the index to query. It can be any secondary local or global index on the table. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Index Name | `indexName` | string |  | Name of the index to query. It can be any secondary local or global index on the table. |
| Attributes to Select | `projectionExpression` | string |  | Text that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas. |
| Filter Expression | `filterExpression` | string |  | Text that contains conditions that DynamoDB applies after the Query operation, but before the data is returned. Items that do not satisfy the FilterExpression criteria are not returned. |
| Expression Attribute Names | `eanUi` | fixedCollection | {} | One or more substitution tokens for attribute names in an expression. Check <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html">Info</a>. |

</details>


---

## Load Options Methods

- `getTables`

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
* Categories: Data & Storage, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: awsDynamoDb
displayName: AWS DynamoDB
description: Consume the AWS DynamoDB API
version: '1'
nodeType: regular
group:
- transform
operations:
- id: upsert
  name: Create or Update
  description: Create a new record, or update the current one if it already exists
    (upsert)
  params:
  - id: dataToSend
    name: Data to Send
    type: options
    default: defineBelow
    required: false
    description: Use when node input properties match destination column names
    validation:
      displayOptions:
        show:
          operation:
          - upsert
    typeInfo:
      type: options
      displayName: Data to Send
      name: dataToSend
      possibleValues:
      - value: autoMapInputData
        name: Auto-Map Input Data to Columns
        description: Use when node input properties match destination column names
      - value: defineBelow
        name: Define Below for Each Column
        description: Set the value for each destination column
  - id: inputsToIgnore
    name: Inputs to Ignore
    type: string
    default: ''
    required: false
    description: List of input properties to avoid sending, separated by commas. Leave
      empty to send all properties.
    placeholder: Enter properties...
    validation:
      displayOptions:
        show:
          operation:
          - upsert
          dataToSend:
          - autoMapInputData
    typeInfo:
      type: string
      displayName: Inputs to Ignore
      name: inputsToIgnore
  - id: fieldsUi
    name: Fields to Send
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Field
    validation:
      displayOptions:
        show:
          operation:
          - upsert
          dataToSend:
          - defineBelow
    typeInfo:
      type: fixedCollection
      displayName: Fields to Send
      name: fieldsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: fieldValues
        displayName: Field
        values:
        - displayName: Field ID
          name: fieldId
          type: string
          default: ''
        - displayName: Field Value
          name: fieldValue
          type: string
          default: ''
- id: delete
  name: Delete
  description: Delete an item
  params:
  - id: returnValues
    name: Return
    type: options
    default: NONE
    required: false
    description: The content of the old item is returned
    validation:
      displayOptions:
        show:
          resource:
          - item
          operation:
          - delete
    typeInfo:
      type: options
      displayName: Return
      name: returnValues
      possibleValues:
      - value: ALL_OLD
        name: Attribute Values
        description: The content of the old item is returned
      - value: NONE
        name: Nothing
        description: Nothing is returned
  - id: keysUi
    name: Keys
    type: fixedCollection
    default: {}
    required: false
    description: Item's primary key. For example, with a simple primary key, you only
      need to provide a value for the partition key. For a composite primary key,
      you must provide values for both the partition key and the sort key.
    placeholder: Add Key
    validation: &id003
      displayOptions:
        show:
          resource:
          - item
          operation:
          - get
    typeInfo: &id004
      type: fixedCollection
      displayName: Keys
      name: keysUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: keyValues
        displayName: Key
        values:
        - displayName: Key
          name: key
          type: string
          default: ''
        - displayName: Type
          name: type
          type: options
          value: B
          default: S
          options:
          - name: Binary
            value: B
            displayName: Binary
          - name: Number
            value: N
            displayName: Number
          - name: String
            value: S
            displayName: String
        - displayName: Value
          name: value
          type: string
          default: ''
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id001
      displayOptions:
        show:
          resource:
          - item
          operation:
          - getAll
          select:
          - ALL_PROJECTED_ATTRIBUTES
          - ALL_ATTRIBUTES
          - SPECIFIC_ATTRIBUTES
    typeInfo: &id002
      type: boolean
      displayName: Simplify
      name: simple
- id: get
  name: Get
  description: Get an item
  params:
  - id: select
    name: Select
    type: options
    default: ALL_ATTRIBUTES
    required: false
    description: Select them in Attributes to Select under Additional Fields
    validation: &id005
      displayOptions:
        show:
          resource:
          - item
          operation:
          - getAll
    typeInfo: &id006
      type: options
      displayName: Select
      name: select
      possibleValues:
      - value: ALL_ATTRIBUTES
        name: All Attributes
        description: ''
      - value: ALL_PROJECTED_ATTRIBUTES
        name: All Projected Attributes
        description: ''
      - value: COUNT
        name: Count
        description: ''
      - value: SPECIFIC_ATTRIBUTES
        name: Specific Attributes
        description: Select them in Attributes to Select under Additional Fields
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id001
    typeInfo: *id002
  - id: keysUi
    name: Keys
    type: fixedCollection
    default: {}
    required: false
    description: Item's primary key. For example, with a simple primary key, you only
      need to provide a value for the partition key. For a composite primary key,
      you must provide values for both the partition key and the sort key.
    placeholder: Add Key
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: Get many items
  params:
  - id: scan
    name: Scan
    type: boolean
    default: false
    required: false
    description: Whether to do an scan or query. Check <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html"
      >differences</a>.
    validation:
      displayOptions:
        show:
          resource:
          - item
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Scan
      name: scan
  - id: keyConditionExpression
    name: Key Condition Expression
    type: string
    default: ''
    required: true
    description: 'Condition to determine the items to be retrieved. The condition
      must perform an equality test on a single partition key value, in this format:
      <code>partitionKeyName = :partitionkeyval</code>'
    placeholder: id = :id
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - item
          operation:
          - getAll
          scan:
          - false
    typeInfo:
      type: string
      displayName: Key Condition Expression
      name: keyConditionExpression
  - id: eavUi
    name: Expression Attribute Values
    type: fixedCollection
    default: {}
    required: true
    description: Substitution tokens for attribute names in an expression
    placeholder: Add Attribute Value
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - item
          operation:
          - getAll
    typeInfo:
      type: fixedCollection
      displayName: Expression Attribute Values
      name: eavUi
      typeOptions:
        minValue: 1
        multipleValues: true
      subProperties:
      - name: eavValues
        displayName: Expression Attribute Vaue
        values:
        - displayName: Attribute
          name: attribute
          type: string
          default: ''
        - displayName: Type
          name: type
          type: options
          value: N
          default: S
          options:
          - name: Number
            value: N
            displayName: Number
          - name: String
            value: S
            displayName: String
        - displayName: Value
          name: value
          type: string
          default: ''
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
          - item
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: select
    name: Select
    type: options
    default: ALL_ATTRIBUTES
    required: false
    description: Select them in Attributes to Select under Additional Fields
    validation: *id005
    typeInfo: *id006
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
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
  - field: inputsToIgnore
    text: Enter properties...
  - field: fieldsUi
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: keysUi
    text: Add Key
  - field: additionalFields
    text: Add Field
  - field: keysUi
    text: Add Key
  - field: additionalFields
    text: Add Field
  - field: keyConditionExpression
    text: id = :id
  - field: eavUi
    text: Add Attribute Value
  - field: options
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
  "$id": "https://n8n.io/schemas/nodes/awsDynamoDb.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AWS DynamoDB Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "upsert",
        "delete",
        "get",
        "getAll"
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
            "item"
          ],
          "default": "item"
        },
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "iam",
            "assumeRole"
          ],
          "default": "iam"
        },
        "operation": {
          "description": "Create a new record, or update the current one if it already exists (upsert)",
          "type": "string",
          "enum": [
            "upsert",
            "delete",
            "get",
            "getAll"
          ],
          "default": "upsert"
        },
        "tableName": {
          "description": "Table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "dataToSend": {
          "description": "Use when node input properties match destination column names",
          "type": "string",
          "enum": [
            "autoMapInputData",
            "defineBelow"
          ],
          "default": "defineBelow"
        },
        "inputsToIgnore": {
          "description": "List of input properties to avoid sending, separated by commas. Leave empty to send all properties.",
          "type": "string",
          "default": "",
          "examples": [
            "Enter properties..."
          ]
        },
        "fieldsUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "additionalFields": {
          "description": "One or more substitution tokens for attribute names in an expression. <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html\">View details</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "returnValues": {
          "description": "The content of the old item is returned",
          "type": "string",
          "enum": [
            "ALL_OLD",
            "NONE"
          ],
          "default": "NONE"
        },
        "keysUi": {
          "description": "Item's primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Key"
          ]
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "select": {
          "description": "Select them in Attributes to Select under Additional Fields",
          "type": "string",
          "enum": [
            "ALL_ATTRIBUTES",
            "ALL_PROJECTED_ATTRIBUTES",
            "COUNT",
            "SPECIFIC_ATTRIBUTES"
          ],
          "default": "ALL_ATTRIBUTES"
        },
        "scan": {
          "description": "Whether to do an scan or query. Check <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html\" >differences</a>.",
          "type": "boolean",
          "default": false
        },
        "filterExpression": {
          "description": "A filter expression determines which items within the Scan results should be returned to you. All of the other results are discarded. Empty value will return all Scan results.",
          "type": "string",
          "default": ""
        },
        "keyConditionExpression": {
          "description": "Condition to determine the items to be retrieved. The condition must perform an equality test on a single partition key value, in this format: <code>partitionKeyName = :partitionkeyval</code>",
          "type": "string",
          "default": "",
          "examples": [
            "id = :id"
          ]
        },
        "eavUi": {
          "description": "Substitution tokens for attribute names in an expression",
          "type": "string",
          "default": {},
          "examples": [
            "Add Attribute Value"
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
        "options": {
          "description": "Name of the index to query. It can be any secondary local or global index on the table.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "aws": {
          "description": "",
          "type": "string"
        },
        "awsAssumeRole": {
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
    "version": "1"
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
