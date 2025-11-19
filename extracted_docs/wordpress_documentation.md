---
title: "Node: Wordpress"
slug: "node-wordpress"
version: "1"
updated: "2025-11-13"
summary: "Consume Wordpress API"
node_type: "regular"
group: "['output']"
---

# Node: Wordpress

**Purpose.** Consume Wordpress API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:wordpress.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **wordpressApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `wordpressApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type, User-Agent

---

## Operations

### Post Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a post |
| Get | `get` | Get a post |
| Get Many | `getAll` | Get many posts |
| Update | `update` | Update a post |

### Page Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a page |
| Get | `get` | Get a page |
| Get Many | `getAll` | Get many pages |
| Update | `update` | Update a page |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a user |
| Get | `get` | Get a user |
| Get Many | `getAll` | Get many users |
| Update | `update` | Update a user |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | post | ✗ | Resource to operate on |  |

**Resource options:**

* **Post** (`post`)
* **Page** (`page`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a post |  |

**Operation options:**

* **Create** (`create`) - Create a post
* **Get** (`get`) - Get a post
* **Get Many** (`getAll`) - Get many posts
* **Update** (`update`) - Update a post

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ | The title for the post |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The ID for the author of the object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Author Name or ID | `authorId` | options |  | The ID for the author of the object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Content | `content` | string |  | The content for the post |
| Slug | `slug` | string |  | An alphanumeric identifier for the object unique to its type |
| Password | `password` | string |  | A password to protect access to the content and excerpt |
| Status | `status` | options | draft | A named status for the post |
| Date | `date` | dateTime |  | The date the post was published, in the site's timezone |
| Comment Status | `commentStatus` | options | open | Whether or not comments are open on the post |
| Ping Status | `pingStatus` | options | open | If the a message should be send to announce the post |
| Format | `format` | options | standard | Whether or not comments are open on the post |
| Sticky | `sticky` | boolean | False | Whether or not the object should be treated as sticky |
| Category Names or IDs | `categories` | multiOptions | [] | The terms assigned to the object in the category taxonomy. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Tag Names or IDs | `tags` | multiOptions | [] | The terms assigned to the object in the post_tag taxonomy. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Template | `postTemplate` | fixedCollection | {} | Whether site uses elementor page builder |

</details>

| Title | `title` | string |  | ✓ | The title for the page |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The ID for the author of the object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Author Name or ID | `authorId` | options |  | The ID for the author of the object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Parent ID | `parent` | number |  | The ID for the parent of the post |
| Content | `content` | string |  | The content for the page |
| Slug | `slug` | string |  | An alphanumeric identifier for the object unique to its type |
| Password | `password` | string |  | A password to protect access to the content and excerpt |
| Status | `status` | options | draft | A named status for the page |
| Comment Status | `commentStatus` | options | open | Whether or not comments are open on the page |
| Ping Status | `pingStatus` | options | open | If the a message should be send to announce the page |
| Template | `pageTemplate` | fixedCollection | {} | Whether site uses elementor page builder |
| Menu Order | `menuOrder` | number | 0 | The order of the page in relation to other pages |
| Featured Media ID | `featuredMediaId` | number |  | The ID of the featured media for the page |

</details>

| Username | `username` | string |  | ✓ | Login name for the user |  |
| Name | `name` | string |  | ✓ | Display name for the user |  |
| First Name | `firstName` | string |  | ✓ | First name for the user |  |
| Last Name | `lastName` | string |  | ✓ | Last name for the user |  |
| Email | `email` | string |  | ✓ | The email address for the user | e.g. name@email.com | email |
| Password | `password` | string |  | ✓ | Password for the user (never included) |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | URL of the user | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| URL | `url` | string |  | URL of the user |
| Description | `description` | string |  | Description of the user |
| Nickname | `nickname` | string |  | The nickname for the user |
| Slug | `slug` | string |  | An alphanumeric identifier for the user |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Post ID | `postId` | string |  | ✓ | Unique identifier for the object |  |
| Options | `options` | collection | {} | ✗ | The password for the post if it is password protected | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Password | `password` | string |  | The password for the post if it is password protected |
| Context | `context` | options | view | Scope under which the request is made; determines fields present in response |

</details>

| Page ID | `pageId` | string |  | ✓ | Unique identifier for the object |  |
| Options | `options` | collection | {} | ✗ | The password for the page if it is password protected | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Password | `password` | string |  | The password for the page if it is password protected |
| Context | `context` | options | view | Scope under which the request is made; determines fields present in response |

</details>

| User ID | `userId` | string |  | ✓ | Unique identifier for the user |  |
| Options | `options` | collection | {} | ✗ | Scope under which the request is made; determines fields present in response | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Context | `context` | options | view | Scope under which the request is made; determines fields present in response |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Options | `options` | collection | {} | ✗ | Limit response to posts published after a given ISO8601 compliant date | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| After | `after` | dateTime |  | Limit response to posts published after a given ISO8601 compliant date |
| Author Names or IDs | `author` | multiOptions | [] | Limit result set to posts assigned to specific authors. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Before | `before` | dateTime |  | Limit response to posts published before a given ISO8601 compliant date |
| Category Names or IDs | `categories` | multiOptions | [] | Limit result set to all items that have the specified term assigned in the categories taxonomy. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Context | `context` | options | view | Scope under which the request is made; determines fields present in response |
| Exclude Categories | `excludedCategories` | multiOptions | [] | Limit result set to all items except those that have the specified term assigned in the categories taxonomy. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Exclude Tags | `excludedTags` | multiOptions | [] | Limit result set to all items except those that have the specified term assigned in the tags taxonomy. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Order | `order` | options | desc | Order sort attribute ascending or descending |
| Order By | `orderBy` | options | id | Sort collection by object attribute |
| Search | `search` | string |  | Limit results to those matching a string |
| Status | `status` | options | publish | The status of the post |
| Sticky | `sticky` | boolean | False | Whether to limit the result set to items that are sticky |
| Tag Names or IDs | `tags` | multiOptions | [] | Limit result set to all items that have the specified term assigned in the tags taxonomy. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Options | `options` | collection | {} | ✗ | Limit response to pages published after a given ISO8601 compliant date | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| After | `after` | dateTime |  | Limit response to pages published after a given ISO8601 compliant date |
| Author Names or IDs | `author` | multiOptions | [] | Limit result set to pages assigned to specific authors. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Before | `before` | dateTime |  | Limit response to pages published before a given ISO8601 compliant date |
| Context | `context` | options | view | Scope under which the request is made; determines fields present in response |
| Menu Order | `menuOrder` | number | 0 | Limit result set to items with a specific menu order value |
| Order | `order` | options | desc | Order sort attribute ascending or descending |
| Order By | `orderBy` | options | id | Sort collection by object attribute |
| Page | `page` | number | 1 | Current page of the collection |
| Parent Page ID | `parent` | number |  | Limit result set to items with a particular parent page ID |
| Search | `search` | string |  | Limit results to those matching a string |
| Status | `status` | options | publish | The status of the page |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Options | `options` | collection | {} | ✗ | Scope under which the request is made; determines fields present in response | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Context | `context` | options | view | Scope under which the request is made; determines fields present in response |
| Order By | `orderBy` | options | id | Sort collection by object attribute |
| Order | `order` | options | desc | Order sort attribute ascending or descending |
| Search | `search` | string |  | Limit results to those matching a string |
| Who | `who` | options | authors | Limit result set to users who are considered authors |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Post ID | `postId` | string |  | ✓ | Unique identifier for the object |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The ID for the author of the object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Author Name or ID | `authorId` | options |  | The ID for the author of the object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Title | `title` | string |  | The title for the post |
| Content | `content` | string |  | The content for the post |
| Slug | `slug` | string |  | An alphanumeric identifier for the object unique to its type |
| Password | `password` | string |  | A password to protect access to the content and excerpt |
| Status | `status` | options | draft | A named status for the post |
| Date | `date` | dateTime |  | The date the post was published, in the site's timezone |
| Comment Status | `commentStatus` | options | open | Whether or not comments are open on the post |
| Ping Status | `pingStatus` | options | open | Whether or not comments are open on the post |
| Format | `format` | options | standard | The format of the post |
| Sticky | `sticky` | boolean | False | Whether or not the object should be treated as sticky |
| Category Names or IDs | `categories` | multiOptions | [] | The terms assigned to the object in the category taxonomy. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Tag Names or IDs | `tags` | multiOptions | [] | The terms assigned to the object in the post_tag taxonomy. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Template | `postTemplate` | fixedCollection | {} | Whether site uses elementor page builder |

</details>

| Page ID | `pageId` | string |  | ✓ | Unique identifier for the object |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The ID for the author of the object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Author Name or ID | `authorId` | options |  | The ID for the author of the object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Parent ID | `parent` | number |  | The ID for the parent of the post |
| Title | `title` | string |  | The title for the page |
| Content | `content` | string |  | The content for the page |
| Slug | `slug` | string |  | An alphanumeric identifier for the object unique to its type |
| Password | `password` | string |  | A password to protect access to the content and excerpt |
| Status | `status` | options | draft | A named status for the page |
| Comment Status | `commentStatus` | options | open | Whether or not comments are open on the page |
| Ping Status | `pingStatus` | options | open | Whether or not comments are open on the page |
| Template | `pageTemplate` | fixedCollection | {} | Whether site uses elementor page builder |
| Menu Order | `menuOrder` | number | 0 | The order of the page in relation to other pages |
| Comment Status | `commentStatus` | options | open | Whether or not comments are open on the page |
| Featured Media ID | `featuredMediaId` | number |  | The ID of the featured media for the page |

</details>

| User ID | `userId` | string |  | ✓ | Unique identifier for the user |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Login name for the user | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Username | `username` | string |  | Login name for the user |
| Name | `name` | string |  | Display name for the user |
| First Name | `firstName` | string |  | First name for the user |
| Last Name | `lastName` | string |  | Last name for the user |
| Email | `email` | string |  | The email address for the user |
| Password | `password` | string |  | Password for the user (never included) |
| URL | `url` | string |  | URL of the user |
| Description | `description` | string |  | Description of the user |
| Nickname | `nickname` | string |  | The nickname for the user |
| Slug | `slug` | string |  | An alphanumeric identifier for the user |

</details>


---

## Load Options Methods

- `getCategories`

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Page > Create

**From workflow:** Wordpress Test - Pages

**Parameters:**
```json
{
  "resource": "page",
  "title": "A new page",
  "additionalFields": {
    "content": "Some content",
    "status": "draft",
    "commentStatus": "closed",
    "pingStatus": "closed",
    "menuOrder": 1
  }
}
```

**Credentials:**
- wordpressApi: `Wordpress (localhost)`

### Example 2: Page > Get

**From workflow:** Wordpress Test - Pages

**Parameters:**
```json
{
  "resource": "page",
  "operation": "get",
  "pageId": "2",
  "options": {}
}
```

**Credentials:**
- wordpressApi: `Wordpress (localhost)`

### Example 3: Page > Get Many

**From workflow:** Wordpress Test - Pages

**Parameters:**
```json
{
  "resource": "page",
  "operation": "getAll",
  "limit": 1,
  "options": {}
}
```

**Credentials:**
- wordpressApi: `Wordpress (localhost)`

### Example 4: Page > Update

**From workflow:** Wordpress Test - Pages

**Parameters:**
```json
{
  "resource": "page",
  "operation": "update",
  "pageId": "2",
  "updateFields": {
    "title": "New Title",
    "content": "Updated Content",
    "slug": "new-slug"
  }
}
```

**Credentials:**
- wordpressApi: `Wordpress (localhost)`

### Example 5: Page > Get Many (With Filters)

**From workflow:** Wordpress Test - Pages

**Parameters:**
```json
{
  "resource": "page",
  "operation": "getAll",
  "limit": 1,
  "options": {
    "before": "2026-01-01T00:00:00"
  }
}
```

**Credentials:**
- wordpressApi: `Wordpress (localhost)`


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
* Categories: Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: wordpress
displayName: Wordpress
description: Consume Wordpress API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: wordpressApi
  required: true
operations:
- id: create
  name: Create
  description: Create a post
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The title for the post
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - page
          operation:
          - create
    typeInfo: &id002
      type: string
      displayName: Title
      name: title
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The title for the page
    validation: *id001
    typeInfo: *id002
  - id: username
    name: Username
    type: string
    default: ''
    required: true
    description: Login name for the user
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Username
      name: username
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Display name for the user
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: firstName
    name: First Name
    type: string
    default: ''
    required: true
    description: First name for the user
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: First Name
      name: firstName
  - id: lastName
    name: Last Name
    type: string
    default: ''
    required: true
    description: Last name for the user
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Last Name
      name: lastName
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email address for the user
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: password
    name: Password
    type: string
    default: ''
    required: true
    description: Password for the user (never included)
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Password
      name: password
      typeOptions:
        password: true
- id: get
  name: Get
  description: Get a post
  params:
  - id: postId
    name: Post ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the object
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - post
          operation:
          - delete
    typeInfo: &id008
      type: string
      displayName: Post ID
      name: postId
  - id: pageId
    name: Page ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the object
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - page
          operation:
          - delete
    typeInfo: &id010
      type: string
      displayName: Page ID
      name: pageId
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the user
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
    typeInfo: &id012
      type: string
      displayName: User ID
      name: userId
- id: getAll
  name: Get Many
  description: Get many posts
  params:
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
    default: 5
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
        maxValue: 10
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
    default: 5
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
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
    default: 5
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: update
  name: Update
  description: Update a post
  params:
  - id: postId
    name: Post ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the object
    validation: *id007
    typeInfo: *id008
  - id: pageId
    name: Page ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the object
    validation: *id009
    typeInfo: *id010
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the user
    validation: *id011
    typeInfo: *id012
examples:
- name: Page > Create
  parameters:
    resource: page
    title: A new page
    additionalFields:
      content: Some content
      status: draft
      commentStatus: closed
      pingStatus: closed
      menuOrder: 1
  workflow: Wordpress Test - Pages
- name: Page > Get
  parameters:
    resource: page
    operation: get
    pageId: '2'
    options: {}
  workflow: Wordpress Test - Pages
- name: Page > Get Many
  parameters:
    resource: page
    operation: getAll
    limit: 1
    options: {}
  workflow: Wordpress Test - Pages
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  - User-Agent
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: options
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
  "$id": "https://n8n.io/schemas/nodes/wordpress.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Wordpress Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "get",
        "getAll",
        "update"
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
            "post",
            "page",
            "user"
          ],
          "default": "post"
        },
        "operation": {
          "description": "Create a user",
          "type": "string",
          "enum": [
            "create",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "title": {
          "description": "The title for the page",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "URL of the user",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "postId": {
          "description": "Unique identifier for the object",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Login name for the user",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "options": {
          "description": "Scope under which the request is made; determines fields present in response",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
        "pageId": {
          "description": "Unique identifier for the object",
          "type": "string",
          "default": ""
        },
        "username": {
          "description": "Login name for the user",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "Display name for the user",
          "type": "string",
          "default": ""
        },
        "firstName": {
          "description": "First name for the user",
          "type": "string",
          "default": ""
        },
        "lastName": {
          "description": "Last name for the user",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "The email address for the user",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "password": {
          "description": "Password for the user (never included)",
          "type": "string",
          "default": ""
        },
        "userId": {
          "description": "Unique identifier for the user",
          "type": "string",
          "default": ""
        },
        "reassign": {
          "description": "Reassign the deleted user's posts and links to this user ID",
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
      "name": "wordpressApi",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Page > Create",
      "value": {
        "resource": "page",
        "title": "A new page",
        "additionalFields": {
          "content": "Some content",
          "status": "draft",
          "commentStatus": "closed",
          "pingStatus": "closed",
          "menuOrder": 1
        }
      }
    },
    {
      "description": "Page > Get",
      "value": {
        "resource": "page",
        "operation": "get",
        "pageId": "2",
        "options": {}
      }
    },
    {
      "description": "Page > Get Many",
      "value": {
        "resource": "page",
        "operation": "getAll",
        "limit": 1,
        "options": {}
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
