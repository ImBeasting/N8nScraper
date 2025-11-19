---
title: "Node: Notion"
slug: "node-notion"
version: "['2', '2.1', '2.2']"
updated: "2025-11-13"
summary: "Consume Notion API"
node_type: "regular"
group: "['output']"
---

# Node: Notion

**Purpose.** Consume Notion API
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `{'light': 'file:notion.svg', 'dark': 'file:notion.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **notionApi**: N/A
- **notionOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notionNotice**: In Notion, make sure to <a href="https://www.notion.so/help/add-and-manage-connections-with-the-api" target="_blank">add your connection</a> to the pages you want to access.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `notionApi` | ✓ | {'show': {'authentication': ["// \t\t\t'apiKey", '//']}} |
| `notionOAuth2Api` | ✓ | {'show': {'authentication': ["// \t\t\t\t'oAuth2", '//']}} |

---

## Operations

### Block Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Append After | `append` | Append a block |
| Get Child Blocks | `getAll` | Get many child blocks |

### Database Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a database |
| Get Many | `getAll` | Get many databases |
| Search | `search` | Search databases using text search |

### Databasepage Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a page in a database |
| Get | `get` | Get a page in a database |
| Get Many | `getAll` | Get many pages in a database |
| Update | `update` | Update pages in a database |

### Page Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a page |
| Get | `get` | Get a page |
| Search | `search` | Text search of pages |
| Archive | `archive` | Archive a page |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a user |
| Get Many | `getAll` | Get many users |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | page | ✗ | Resource to operate on |  |

**Resource options:**

* **Block** (`block`)
* **Database** (`database`)
* **Database Page** (`databasePage`)
* **Page** (`page`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | append | ✗ | Append a block |  |

**Operation options:**

* **Append After** (`append`) - Append a block
* **Get Child Blocks** (`getAll`) - Get many child blocks

---

### Append After parameters (`append`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Block | `blockId` | resourceLocator |  | ✓ | The Notion Block to append blocks to | e.g. https://www.notion.so/My-Page-b4eeb113e118403ba450af65ac25f0b9 |  |

### Get Child Blocks parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Block | `blockId` | resourceLocator |  | ✓ | The Notion Block to get all children from | e.g. https://www.notion.so/My-Page-b4eeb113e118403ba450af65ac25f0b9 |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Also Fetch Nested Blocks | `fetchNestedBlocks` | boolean | False | ✗ |  |  |
| Simplify Output | `simplifyOutput` | boolean | True | ✗ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Database | `databaseId` | resourceLocator |  | ✓ | The Notion Database to operate on | e.g. Select a Database... |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Whether to download a file if a database's field contains it | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Download Files | `downloadFiles` | boolean | False | Whether to download a file if a database's field contains it |
| Filters | `filter` | fixedCollection | {} |  |
| Sort | `sort` | fixedCollection | {} | Whether or not to use the record's timestamp to sort the response |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Database | `databaseId` | resourceLocator |  | ✓ | The Notion Database to get | e.g. Select a Database... |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Database Page | `pageId` | resourceLocator |  | ✓ | The Notion Database Page to get | e.g. https://www.notion.so/My-Database-Page-b4eeb113e118403ba450af65ac25f0b9 |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Page Link or ID | `pageId` | string |  | ✓ | The Page URL from Notion's 'copy link' functionality (or just the ID contained within the URL) |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| User ID | `userId` | string |  | ✓ |  |  |

### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Search Text | `text` | string |  | ✗ | The text to search for |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | The direction to sort | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort | `sort` | fixedCollection | {} | The direction to sort |

</details>

| Search Text | `text` | string |  | ✗ | The text to search for |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | The name of the property to filter by | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filters | `filter` | fixedCollection | {} | The name of the property to filter by |
| Sort | `sort` | fixedCollection | {} | The direction to sort |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Database | `databaseId` | resourceLocator |  | ✓ | The Notion Database to operate on | e.g. Select a Database... |  |
| Title | `title` | string |  | ✗ | Page title. Appears at the top of the page and can be found via Quick Find. |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Properties | `propertiesUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Property |  |

<details>
<summary><strong>Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Property | `propertyValues` |  |  |  |

</details>

| Options | `options` | collection | {} | ✗ | Use an Emoji for the icon | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Icon Type | `iconType` | options | emoji | Use an Emoji for the icon |
| Icon | `icon` | string |  | Emoji or File URL to use as the icon |

</details>

| Parent Page | `pageId` | resourceLocator |  | ✓ | The Notion Database Page to create a child page for | e.g. https://www.notion.so/My-Page-b4eeb113e118403aa450af65ac25f0b9 |  |
| Title | `title` | string |  | ✓ | Page title. Appears at the top of the page and can be found via Quick Find. |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Use an Emoji for the icon | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Icon Type | `iconType` | options | emoji | Use an Emoji for the icon |
| Icon | `icon` | string |  | Emoji or File URL to use as the icon |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Database Page | `pageId` | resourceLocator |  | ✓ | The Notion Database Page to update | e.g. https://www.notion.so/My-Database-Page-b4eeb113e118403ba450af65ac25f0b9 |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Properties | `propertiesUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Property |  |

<details>
<summary><strong>Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Property | `propertyValues` |  |  |  |

</details>

| Options | `options` | collection | {} | ✗ | Use an Emoji for the icon | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Icon Type | `iconType` | options | emoji | Use an Emoji for the icon |
| Icon | `icon` | string |  | Emoji or File URL to use as the icon |

</details>


### Archive parameters (`archive`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Page | `pageId` | resourceLocator |  | ✓ | The Notion Page to archive | e.g. https://www.notion.so/My-Page-b4eeb113e118403aa450af65ac25f0b9 |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

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
node: notion
displayName: Notion
description: Consume Notion API
version:
- '2'
- '2.1'
- '2.2'
nodeType: regular
group:
- output
credentials:
- name: notionApi
  required: true
- name: notionOAuth2Api
  required: true
operations:
- id: append
  name: Append After
  description: Append a block
  params:
  - id: blockId
    name: Block
    type: resourceLocator
    default: ''
    required: true
    description: The Notion Block to append blocks to
    placeholder: https://www.notion.so/My-Page-b4eeb113e118403ba450af65ac25f0b9
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - block
          operation:
          - getAll
        hide: {}
    typeInfo: &id002
      type: resourceLocator
      displayName: Block
      name: blockId
- id: getAll
  name: Get Child Blocks
  description: Get many child blocks
  params:
  - id: blockId
    name: Block
    type: resourceLocator
    default: ''
    required: true
    description: The Notion Block to get all children from
    placeholder: https://www.notion.so/My-Page-b4eeb113e118403ba450af65ac25f0b9
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id003
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: fetchNestedBlocks
    name: Also Fetch Nested Blocks
    type: boolean
    default: false
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - block
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Also Fetch Nested Blocks
      name: fetchNestedBlocks
  - id: simplifyOutput
    name: Simplify Output
    type: boolean
    default: true
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - block
          operation:
          - getAll
        hide: {}
    typeInfo:
      type: boolean
      displayName: Simplify Output
      name: simplifyOutput
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id007
      displayOptions:
        show:
          resource:
          - page
          operation:
          - search
    typeInfo: &id008
      type: boolean
      displayName: Simplify
      name: simple
  - id: databaseId
    name: Database
    type: resourceLocator
    default: ''
    required: true
    description: The Notion Database to operate on
    placeholder: Select a Database...
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - databasePage
          operation:
          - getAll
    typeInfo: &id010
      type: resourceLocator
      displayName: Database
      name: databaseId
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: get
  name: Get
  description: Get a database
  params:
  - id: databaseId
    name: Database
    type: resourceLocator
    default: ''
    required: true
    description: The Notion Database to get
    placeholder: Select a Database...
    validation: *id009
    typeInfo: *id010
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
  - id: pageId
    name: Database Page
    type: resourceLocator
    default: ''
    required: true
    description: The Notion Database Page to get
    placeholder: https://www.notion.so/My-Database-Page-b4eeb113e118403ba450af65ac25f0b9
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - page
          operation:
          - get
    typeInfo: &id012
      type: string
      displayName: Page Link or ID
      name: pageId
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
  - id: pageId
    name: Page Link or ID
    type: string
    default: ''
    required: true
    description: The Page URL from Notion's 'copy link' functionality (or just the
      ID contained within the URL)
    validation: *id011
    typeInfo: *id012
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
    typeInfo:
      type: string
      displayName: User ID
      name: userId
- id: search
  name: Search
  description: Search databases using text search
  params:
  - id: text
    name: Search Text
    type: string
    default: ''
    required: false
    description: The text to search for
    validation: &id013
      displayOptions:
        show:
          resource:
          - page
          operation:
          - search
    typeInfo: &id014
      type: string
      displayName: Search Text
      name: text
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
  - id: text
    name: Search Text
    type: string
    default: ''
    required: false
    description: The text to search for
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
- id: create
  name: Create
  description: Create a page in a database
  params:
  - id: databaseId
    name: Database
    type: resourceLocator
    default: ''
    required: true
    description: The Notion Database to operate on
    placeholder: Select a Database...
    validation: *id009
    typeInfo: *id010
  - id: title
    name: Title
    type: string
    default: ''
    required: false
    description: Page title. Appears at the top of the page and can be found via Quick
      Find.
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - page
          operation:
          - create
    typeInfo: &id016
      type: string
      displayName: Title
      name: title
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
  - id: propertiesUi
    name: Properties
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Property
    validation: &id017
      displayOptions:
        show:
          resource:
          - databasePage
          operation:
          - update
    typeInfo: &id018
      type: fixedCollection
      displayName: Properties
      name: propertiesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: propertyValues
        displayName: Property
        values:
        - displayName: Key Name or ID
          name: key
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getDatabaseIdFromPage
        - displayName: Type
          name: type
          type: hidden
          default: ={{$parameter[
        - displayName: Title
          name: title
          type: string
          default: ''
          displayOptions:
            show:
              type:
              - title
        - displayName: Rich Text
          name: richText
          type: boolean
          default: false
          displayOptions:
            show:
              type:
              - rich_text
        - displayName: Text
          name: textContent
          type: string
          default: ''
          displayOptions:
            show:
              type:
              - rich_text
              richText:
              - false
        - displayName: Phone Number
          name: phoneValue
          type: string
          description: Phone number. No structure is enforced.
          default: ''
          displayOptions:
            show:
              type:
              - phone_number
        - displayName: Option Names or IDs
          name: multiSelectValue
          type: multiOptions
          description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: []
          typeOptions:
            loadOptionsMethod: getDatabaseOptionsFromPage
          displayOptions:
            show:
              type:
              - multi_select
        - displayName: Option Name or ID
          name: selectValue
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getDatabaseOptionsFromPage
          displayOptions:
            show:
              type:
              - select
        - displayName: Status Name or ID
          name: statusValue
          type: options
          description: Name of the option you want to set. Choose from the list, or
            specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: ''
          typeOptions:
            loadOptionsMethod: getDatabaseOptionsFromPage
          displayOptions:
            show:
              type:
              - status
        - displayName: Email
          name: emailValue
          type: string
          default: ''
          displayOptions:
            show:
              type:
              - email
        - displayName: Ignore If Empty
          name: ignoreIfEmpty
          type: boolean
          default: false
          displayOptions:
            show:
              type:
              - url
        - displayName: URL
          name: urlValue
          type: string
          description: Web address
          default: ''
          displayOptions:
            show:
              type:
              - url
        - displayName: User Names or IDs
          name: peopleValue
          type: multiOptions
          description: List of users. Multiples can be defined separated by comma.
            Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: []
          typeOptions:
            loadOptionsMethod: getUsers
          displayOptions:
            show:
              type:
              - people
        - displayName: Relation IDs
          name: relationValue
          type: string
          description: List of databases that belong to another database. Multiples
            can be defined separated by comma.
          default: []
          typeOptions:
            multipleValues: true
          displayOptions:
            show:
              type:
              - relation
        - displayName: Checked
          name: checkboxValue
          type: boolean
          description: Whether or not the checkbox is checked. <code>true</code> represents
            checked. <code>false</code> represents unchecked.
          default: false
          displayOptions:
            show:
              type:
              - checkbox
        - displayName: Number
          name: numberValue
          type: number
          description: Number value
          default: 0
          displayOptions:
            show:
              type:
              - number
        - displayName: Range
          name: range
          type: boolean
          description: Whether or not you want to define a date range
          default: false
          displayOptions:
            show:
              type:
              - date
        - displayName: Include Time
          name: includeTime
          type: boolean
          description: Whether or not to include the time in the date
          default: true
          displayOptions:
            show:
              type:
              - date
        - displayName: Date
          name: date
          type: dateTime
          description: An ISO 8601 format date, with optional time
          default: ''
          displayOptions:
            show:
              range:
              - false
              type:
              - date
        - displayName: Date Start
          name: dateStart
          type: dateTime
          description: An ISO 8601 format date, with optional time
          default: ''
          displayOptions:
            show:
              range:
              - true
              type:
              - date
        - displayName: Date End
          name: dateEnd
          type: dateTime
          description: An ISO 8601 formatted date, with optional time. Represents
            the end of a date range.
          default: ''
          displayOptions:
            show:
              range:
              - true
              type:
              - date
        - displayName: Timezone Name or ID
          name: timezone
          type: options
          description: Time zone to use. By default n8n timezone is used. Choose from
            the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: default
          typeOptions:
            loadOptionsMethod: getTimezones
          displayOptions:
            show:
              type:
              - date
        - displayName: File URLs
          name: fileUrls
          type: fixedCollection
          description: Link to externally hosted file
          placeholder: Add File
          default: {}
          options:
          - name: fileUrl
            displayName: File
            values:
            - displayName: Name
              name: name
              type: string
              default: ''
            - displayName: File URL
              name: url
              type: string
              description: Link to externally hosted file
              default: ''
          typeOptions:
            multipleValues: true
          displayOptions:
            show:
              type:
              - files
            hide: {}
  - id: pageId
    name: Parent Page
    type: resourceLocator
    default: ''
    required: true
    description: The Notion Database Page to create a child page for
    placeholder: https://www.notion.so/My-Page-b4eeb113e118403aa450af65ac25f0b9
    validation: *id011
    typeInfo: *id012
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Page title. Appears at the top of the page and can be found via Quick
      Find.
    validation: *id015
    typeInfo: *id016
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
- id: update
  name: Update
  description: Update pages in a database
  params:
  - id: pageId
    name: Database Page
    type: resourceLocator
    default: ''
    required: true
    description: The Notion Database Page to update
    placeholder: https://www.notion.so/My-Database-Page-b4eeb113e118403ba450af65ac25f0b9
    validation: *id011
    typeInfo: *id012
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
  - id: propertiesUi
    name: Properties
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Property
    validation: *id017
    typeInfo: *id018
- id: archive
  name: Archive
  description: Archive a page
  params:
  - id: pageId
    name: Page
    type: resourceLocator
    default: ''
    required: true
    description: The Notion Page to archive
    placeholder: https://www.notion.so/My-Page-b4eeb113e118403aa450af65ac25f0b9
    validation: *id011
    typeInfo: *id012
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices:
  - name: notionNotice
    text: In Notion, make sure to <a href="https://www.notion.so/help/add-and-manage-connections-with-the-api"
      target="_blank">add your connection</a> to the pages you want to access.
    conditions: null
  tooltips: []
  placeholders:
  - field: blockId
    text: https://www.notion.so/My-Page-b4eeb113e118403ba450af65ac25f0b9
  - field: blockId
    text: https://www.notion.so/My-Page-b4eeb113e118403ba450af65ac25f0b9
  - field: databaseId
    text: Select a Database...
  - field: options
    text: Add Field
  - field: databaseId
    text: Select a Database...
  - field: propertiesUi
    text: Add Property
  - field: options
    text: Add option
  - field: pageId
    text: https://www.notion.so/My-Database-Page-b4eeb113e118403ba450af65ac25f0b9
  - field: propertiesUi
    text: Add Property
  - field: options
    text: Add option
  - field: pageId
    text: https://www.notion.so/My-Database-Page-b4eeb113e118403ba450af65ac25f0b9
  - field: databaseId
    text: Select a Database...
  - field: options
    text: Add Field
  - field: pageId
    text: https://www.notion.so/My-Page-b4eeb113e118403aa450af65ac25f0b9
  - field: pageId
    text: https://www.notion.so/My-Page-b4eeb113e118403aa450af65ac25f0b9
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/notion.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Notion Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "append",
        "getAll",
        "get",
        "search",
        "create",
        "update",
        "archive"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "The resource to operate on.",
          "type": "string",
          "enum": [
            "apiKey",
            "oAuth2"
          ],
          "default": "apiKey"
        },
        "Credentials": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "block",
            "database",
            "databasePage",
            "page",
            "user"
          ],
          "default": "page"
        },
        "operation": {
          "description": "Get a user",
          "type": "string",
          "enum": [
            "get",
            "getAll"
          ],
          "default": "get"
        },
        "blockId": {
          "description": "The Notion Block to get all children from",
          "type": "string",
          "examples": [
            "https://www.notion.so/My-Page-b4eeb113e118403ba450af65ac25f0b9"
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
        "fetchNestedBlocks": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "simplifyOutput": {
          "description": "",
          "type": "boolean",
          "default": true
        },
        "databaseId": {
          "description": "The Notion Database to operate on",
          "type": "string",
          "examples": [
            "Select a Database..."
          ]
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "text": {
          "description": "The text to search for",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "The name of the property to filter by",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "title": {
          "description": "Page title. Appears at the top of the page and can be found via Quick Find.",
          "type": "string",
          "default": ""
        },
        "propertiesUi": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Property"
          ]
        },
        "pageId": {
          "description": "The Page URL from Notion's 'copy link' functionality (or just the ID contained within the URL)",
          "type": "string",
          "default": ""
        },
        "userId": {
          "description": "",
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
    "version": [
      "2",
      "2.1",
      "2.2"
    ]
  },
  "credentials": [
    {
      "name": "notionApi",
      "required": true
    },
    {
      "name": "notionOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2', '2.1', '2.2'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
