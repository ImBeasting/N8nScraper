---
title: "Node: Monday.com"
slug: "node-mondaycom"
version: "1"
updated: "2026-01-08"
summary: "Consume Monday.com API"
node_type: "regular"
group: "['output']"
---

# Node: Monday.com

**Purpose.** Consume Monday.com API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:mondayCom.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **mondayComApi**: N/A
- **mondayComOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `mondayComApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `mondayComOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**HTTP Methods:** POST

**Headers Used:** API-Version, Content-Type

---

## Operations

### Board Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Archive | `archive` | Archive a board |
| Create | `create` | Create a new board |
| Get | `get` | Get a board |
| Get Many | `getAll` | Get many boards |

### Boardcolumn Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new column |
| Get Many | `getAll` | Get many columns |

### Boardgroup Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a group in a board |
| Create | `create` | Create a group in a board |
| Get Many | `getAll` | Get list of groups in a board |

### Boarditem Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Update | `addUpdate` | Add an update to an item |
| Change Column Value | `changeColumnValue` | Change a column value for a board item |
| Change Multiple Column Values | `changeMultipleColumnValues` | Change multiple column values for a board item |
| Create | `create` | Create an item in a board's group |
| Delete | `delete` | Delete an item |
| Get | `get` | Get an item |
| Get By Column Value | `getByColumnValue` | Get items by column value |
| Get Many | `getAll` | Get many items |
| Move | `move` | Move item to group |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | board | ✗ | Resource to operate on |  |

**Resource options:**

* **Board** (`board`)
* **Board Column** (`boardColumn`)
* **Board Group** (`boardGroup`)
* **Board Item** (`boardItem`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Archive a board |  |

**Operation options:**

* **Archive** (`archive`) - Archive a board
* **Create** (`create`) - Create a new board
* **Get** (`get`) - Get a board
* **Get Many** (`getAll`) - Get many boards

---

### Archive parameters (`archive`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board Name or ID | `boardId` | options |  | ✓ | Board unique identifiers. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | The board's name |  |
| Kind | `kind` | options |  | ✓ | The board's kind (public / private / share) |  |

**Kind options:**

* **Share** (`share`)
* **Public** (`public`)
* **Private** (`private`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Optional board template ID | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Template ID | `templateId` | number | 0 | Optional board template ID |

</details>

| Board Name or ID | `boardId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Title | `title` | string |  | ✓ |  |  |
| Column Type | `columnType` | options |  | ✓ |  |  |

**Column Type options:**

* **Checkbox** (`checkbox`)
* **Country** (`country`)
* **Date** (`date`)
* **Dropdown** (`dropdown`)
* **Email** (`email`)
* **Hour** (`hour`)
* **Link** (`Link`)
* **Long Text** (`longText`)
* **Numbers** (`numbers`)
* **People** (`people`)
* **Person** (`person`)
* **Phone** (`phone`)
* **Rating** (`rating`)
* **Status** (`status`)
* **Tags** (`tags`)
* **Team** (`team`)
* **Text** (`text`)
* **Timeline** (`timeline`)
* **Timezone** (`timezone`)
* **Week** (`week`)
* **World Clock** (`worldClock`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | The new column's defaults | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Defauls | `defaults` | json |  | The new column's defaults |

</details>

| Board Name or ID | `boardId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Name | `name` | string |  | ✓ | The group name |  |
| Board Name or ID | `boardId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Group Name or ID | `groupId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Name | `name` | string |  | ✓ | The new item's name |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The column values of the new item | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Column Values | `columnValues` | json |  | The column values of the new item |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board Name or ID | `boardId` | options |  | ✓ | Board unique identifiers. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Item ID | `itemId` | string |  | ✓ | Item's ID (Multiple can be added separated by comma) |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Board Name or ID | `boardId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Board Name or ID | `boardId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Board Name or ID | `boardId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Group Name or ID | `groupId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board Name or ID | `boardId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Group Name or ID | `groupId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Item ID | `itemId` | string |  | ✓ | Item's ID |  |

### Add Update parameters (`addUpdate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Item ID | `itemId` | string |  | ✓ | The unique identifier of the item to add update to |  |
| Update Text | `value` | string |  | ✓ | The update text to add |  |

### Change Column Value parameters (`changeColumnValue`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board Name or ID | `boardId` | options |  | ✓ | The unique identifier of the board. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Item ID | `itemId` | string |  | ✓ | The unique identifier of the item to change column of |  |
| Column Name or ID | `columnId` | options |  | ✓ | The column's unique identifier. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Value | `value` | json |  | ✓ | The column value in JSON format. Documentation can be found <a href="https://monday.com/developers/v2#mutations-section-columns-change-column-value">here</a>. |  |

### Change Multiple Column Values parameters (`changeMultipleColumnValues`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board Name or ID | `boardId` | options |  | ✓ | The unique identifier of the board. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Item ID | `itemId` | string |  | ✓ | Item's ID |  |
| Column Values | `columnValues` | json |  | ✓ | The column fields and values in JSON format. Documentation can be found <a href="https://monday.com/developers/v2#mutations-section-columns-change-multiple-column-values">here</a>. |  |

### Get By Column Value parameters (`getByColumnValue`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board Name or ID | `boardId` | options |  | ✓ | The unique identifier of the board. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Column Name or ID | `columnId` | options |  | ✓ | The column's unique identifier. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Column Value | `columnValue` | string |  | ✓ | The column value to search items by |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Move parameters (`move`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Board Name or ID | `boardId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Item ID | `itemId` | string |  | ✓ | The item's ID |  |
| Group Name or ID | `groupId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

---

## Load Options Methods

- `getBoards`
- `query`
- `boards`
- `limit`

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
node: mondayCom
displayName: Monday.com
description: Consume Monday.com API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: mondayComApi
  required: true
- name: mondayComOAuth2Api
  required: true
operations:
- id: archive
  name: Archive
  description: Archive a board
  params:
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: Board unique identifiers. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - boardItem
          operation:
          - move
    typeInfo: &id002
      type: options
      displayName: Board Name or ID
      name: boardId
      typeOptions:
        loadOptionsMethod: getBoards
      possibleValues: []
- id: create
  name: Create
  description: Create a new board
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The board's name
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - boardItem
    typeInfo: &id004
      type: string
      displayName: Name
      name: name
  - id: kind
    name: Kind
    type: options
    default: ''
    required: true
    description: The board's kind (public / private / share)
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - board
    typeInfo:
      type: options
      displayName: Kind
      name: kind
      possibleValues:
      - value: share
        name: Share
        description: ''
      - value: public
        name: Public
        description: ''
      - value: private
        name: Private
        description: ''
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - boardColumn
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: columnType
    name: Column Type
    type: options
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - boardColumn
          operation:
          - create
    typeInfo:
      type: options
      displayName: Column Type
      name: columnType
      possibleValues:
      - value: checkbox
        name: Checkbox
        description: ''
      - value: country
        name: Country
        description: ''
      - value: date
        name: Date
        description: ''
      - value: dropdown
        name: Dropdown
        description: ''
      - value: email
        name: Email
        description: ''
      - value: hour
        name: Hour
        description: ''
      - value: Link
        name: Link
        description: ''
      - value: longText
        name: Long Text
        description: ''
      - value: numbers
        name: Numbers
        description: ''
      - value: people
        name: People
        description: ''
      - value: person
        name: Person
        description: ''
      - value: phone
        name: Phone
        description: ''
      - value: rating
        name: Rating
        description: ''
      - value: status
        name: Status
        description: ''
      - value: tags
        name: Tags
        description: ''
      - value: team
        name: Team
        description: ''
      - value: text
        name: Text
        description: ''
      - value: timeline
        name: Timeline
        description: ''
      - value: timezone
        name: Timezone
        description: ''
      - value: week
        name: Week
        description: ''
      - value: worldClock
        name: World Clock
        description: ''
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The group name
    validation: *id003
    typeInfo: *id004
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: groupId
    name: Group Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - boardItem
          operation:
          - move
    typeInfo: &id006
      type: options
      displayName: Group Name or ID
      name: groupId
      typeOptions:
        loadOptionsMethod: getGroups
      possibleValues: []
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The new item's name
    validation: *id003
    typeInfo: *id004
- id: get
  name: Get
  description: Get a board
  params:
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: Board unique identifiers. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: itemId
    name: Item ID
    type: string
    default: ''
    required: true
    description: Item's ID (Multiple can be added separated by comma)
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - move
          resource:
          - boardItem
    typeInfo: &id012
      type: string
      displayName: Item ID
      name: itemId
- id: getAll
  name: Get Many
  description: Get many boards
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
          - boardItem
          operation:
          - getByColumnValue
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
          resource:
          - boardItem
          operation:
          - getByColumnValue
          returnAll:
          - false
    typeInfo: &id010
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: groupId
    name: Group Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
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
- id: delete
  name: Delete
  description: Delete a group in a board
  params:
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: groupId
    name: Group Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
  - id: itemId
    name: Item ID
    type: string
    default: ''
    required: true
    description: Item's ID
    validation: *id011
    typeInfo: *id012
- id: addUpdate
  name: Add Update
  description: Add an update to an item
  params:
  - id: itemId
    name: Item ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the item to add update to
    validation: *id011
    typeInfo: *id012
  - id: value
    name: Update Text
    type: string
    default: ''
    required: true
    description: The update text to add
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - boardItem
          operation:
          - changeColumnValue
    typeInfo: &id014
      type: json
      displayName: Value
      name: value
- id: changeColumnValue
  name: Change Column Value
  description: Change a column value for a board item
  params:
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The unique identifier of the board. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: itemId
    name: Item ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the item to change column of
    validation: *id011
    typeInfo: *id012
  - id: columnId
    name: Column Name or ID
    type: options
    default: ''
    required: true
    description: The column's unique identifier. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - boardItem
          operation:
          - getByColumnValue
    typeInfo: &id016
      type: options
      displayName: Column Name or ID
      name: columnId
      typeOptions:
        loadOptionsMethod: getColumns
      possibleValues: []
  - id: value
    name: Value
    type: json
    default: ''
    required: true
    description: The column value in JSON format. Documentation can be found <a href="https://monday.com/developers/v2#mutations-section-columns-change-column-value">here</a>.
    validation: *id013
    typeInfo: *id014
- id: changeMultipleColumnValues
  name: Change Multiple Column Values
  description: Change multiple column values for a board item
  params:
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The unique identifier of the board. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: itemId
    name: Item ID
    type: string
    default: ''
    required: true
    description: Item's ID
    validation: *id011
    typeInfo: *id012
  - id: columnValues
    name: Column Values
    type: json
    default: ''
    required: true
    description: The column fields and values in JSON format. Documentation can be
      found <a href="https://monday.com/developers/v2#mutations-section-columns-change-multiple-column-values">here</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - boardItem
          operation:
          - changeMultipleColumnValues
    typeInfo:
      type: json
      displayName: Column Values
      name: columnValues
      typeOptions:
        alwaysOpenEditWindow: true
- id: getByColumnValue
  name: Get By Column Value
  description: Get items by column value
  params:
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: The unique identifier of the board. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: columnId
    name: Column Name or ID
    type: options
    default: ''
    required: true
    description: The column's unique identifier. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id015
    typeInfo: *id016
  - id: columnValue
    name: Column Value
    type: string
    default: ''
    required: true
    description: The column value to search items by
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - boardItem
          operation:
          - getByColumnValue
    typeInfo:
      type: string
      displayName: Column Value
      name: columnValue
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
- id: move
  name: Move
  description: Move item to group
  params:
  - id: boardId
    name: Board Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: itemId
    name: Item ID
    type: string
    default: ''
    required: true
    description: The item's ID
    validation: *id011
    typeInfo: *id012
  - id: groupId
    name: Group Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id005
    typeInfo: *id006
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - POST
  endpoints: []
  headers:
  - API-Version
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
  "$id": "https://n8n.io/schemas/nodes/mondayCom.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Monday.com Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "archive",
        "create",
        "get",
        "getAll",
        "delete",
        "addUpdate",
        "changeColumnValue",
        "changeMultipleColumnValues",
        "getByColumnValue",
        "move"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "accessToken",
            "oAuth2"
          ],
          "default": "accessToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "board",
            "boardColumn",
            "boardGroup",
            "boardItem"
          ],
          "default": "board"
        },
        "operation": {
          "description": "Add an update to an item",
          "type": "string",
          "enum": [
            "addUpdate",
            "changeColumnValue",
            "changeMultipleColumnValues",
            "create",
            "delete",
            "get",
            "getByColumnValue",
            "getAll",
            "move"
          ],
          "default": "create"
        },
        "boardId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "The new item's name",
          "type": "string",
          "default": ""
        },
        "kind": {
          "description": "The board's kind (public / private / share)",
          "type": "string",
          "enum": [
            "share",
            "public",
            "private"
          ],
          "default": ""
        },
        "additionalFields": {
          "description": "The column values of the new item",
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
        "title": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "columnType": {
          "description": "",
          "type": "string",
          "enum": [
            "checkbox",
            "country",
            "date",
            "dropdown",
            "email",
            "hour",
            "Link",
            "longText",
            "numbers",
            "people",
            "person",
            "phone",
            "rating",
            "status",
            "tags",
            "team",
            "text",
            "timeline",
            "timezone",
            "week",
            "worldClock"
          ],
          "default": ""
        },
        "groupId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "itemId": {
          "description": "The item's ID",
          "type": "string",
          "default": ""
        },
        "value": {
          "description": "The column value in JSON format. Documentation can be found <a href=\"https://monday.com/developers/v2#mutations-section-columns-change-column-value\">here</a>.",
          "type": "string",
          "default": ""
        },
        "columnId": {
          "description": "The column's unique identifier. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "columnValues": {
          "description": "The column fields and values in JSON format. Documentation can be found <a href=\"https://monday.com/developers/v2#mutations-section-columns-change-multiple-column-values\">here</a>.",
          "type": "string",
          "default": ""
        },
        "columnValue": {
          "description": "The column value to search items by",
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
      "name": "mondayComApi",
      "required": true
    },
    {
      "name": "mondayComOAuth2Api",
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
