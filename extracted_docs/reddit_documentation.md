---
title: "Node: Reddit"
slug: "node-reddit"
version: "1"
updated: "2025-11-13"
summary: "Consume the Reddit API"
node_type: "regular"
group: "['transform']"
---

# Node: Reddit

**Purpose.** Consume the Reddit API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:reddit.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **redditOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `redditOAuth2Api` | ✓ | {'show': {'resource': ['postComment', 'post', 'profile']}} |

---

## API Patterns

**Headers Used:** user-agent

---

## Operations

### Postcomment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a top-level comment in a post |
| Get Many | `getAll` | Retrieve many comments in a post |
| Delete | `delete` | Remove a comment from a post |
| Reply | `reply` | Write a reply to a comment in a post |

### Profile Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a profile |

### Subreddit Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve background information about a subreddit |
| Get Many | `getAll` | Retrieve information about many subreddits |

### Post Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Submit a post to a subreddit |
| Delete | `delete` | Delete a post from a subreddit |
| Get | `get` | Get a post from a subreddit |
| Get Many | `getAll` | Get many posts from a subreddit |
| Search | `search` | Search posts in a subreddit or in all of Reddit |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a user |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | post | ✗ | Resource to operate on |  |

**Resource options:**

* **Post** (`post`)
* **Post Comment** (`postComment`)
* **Profile** (`profile`)
* **Subreddit** (`subreddit`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a top-level comment in a post |  |

**Operation options:**

* **Create** (`create`) - Create a top-level comment in a post
* **Get Many** (`getAll`) - Retrieve many comments in a post
* **Delete** (`delete`) - Remove a comment from a post
* **Reply** (`reply`) - Write a reply to a comment in a post

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Post ID | `postId` | string |  | ✓ | ID of the post to write the comment to. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code> | e.g. l0me7x |  |
| Comment Text | `commentText` | string |  | ✓ | Text of the comment. Markdown supported. |  |
| Subreddit | `subreddit` | string |  | ✓ | Subreddit to create the post in |  |
| Kind | `kind` | options | self | ✗ | The kind of the post to create |  |

**Kind options:**

* **Text Post** (`self`)
* **Link Post** (`link`)
* **Image Post** (`image`)

| Title | `title` | string |  | ✓ | Title of the post, up to 300 characters long |  |
| URL | `url` | string |  | ✓ | URL of the post | url |
| Text | `text` | string |  | ✓ | Text of the post. Markdown supported. |  |
| Resubmit | `resubmit` | boolean | False | ✗ | Whether the URL will be posted even if it was already posted to the subreddit before. Otherwise, the re-posting will trigger an error. |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Subreddit | `subreddit` | string |  | ✓ | The name of subreddit where the post is |  |
| Post ID | `postId` | string |  | ✓ | ID of the post to get all comments from. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code> | e.g. l0me7x |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | The keyword for the subreddit search | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Keyword | `keyword` | string |  | The keyword for the subreddit search |
| Trending | `trending` | boolean | False | Whether to fetch currently trending subreddits in all of Reddit |

</details>

| Subreddit | `subreddit` | string |  | ✓ | The name of subreddit to retrieve the posts from |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Category of the posts to retrieve | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Category | `category` | options | top | Category of the posts to retrieve |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Comment ID | `commentId` | string |  | ✓ | ID of the comment to remove. Found in the comment URL:<code>/r/[subreddit_name]/comments/[post_id]/[post_title]/[comment_id]</code> | e.g. gla7fmt |  |
| Post ID | `postId` | string |  | ✓ | ID of the post to delete. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code> | e.g. gla7fmt |  |

### Reply parameters (`reply`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Comment ID | `commentId` | string |  | ✓ | ID of the comment to reply to. To be found in the comment URL: <code>www.reddit.com/r/[subreddit_name]/comments/[post_id]/[post_title]/[comment_id]</code> | e.g. gl9iroa |  |
| Reply Text | `replyText` | string |  | ✓ | Text of the reply. Markdown supported. |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Details | `details` | options | identity | ✓ | Details of my account to retrieve |  |

**Details options:**

* **Blocked Users** (`blockedUsers`) - Return the blocked users of the logged-in user
* **Friends** (`friends`) - Return the friends of the logged-in user
* **Identity** (`identity`) - Return the identity of the logged-in user
* **Karma** (`karma`) - Return the subreddit karma for the logged-in user
* **Preferences** (`prefs`) - Return the settings preferences of the logged-in user
* **Saved** (`saved`) - Return the saved posts for the user
* **Trophies** (`trophies`) - Return the trophies of the logged-in user

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Content | `content` | options | about | ✓ | Subreddit content to retrieve |  |

**Content options:**

* **About** (`about`)
* **Rules** (`rules`)

| Subreddit | `subreddit` | string |  | ✓ | The name of subreddit to retrieve the content from |  |
| Subreddit | `subreddit` | string |  | ✓ | The name of subreddit to retrieve the post from |  |
| Post ID | `postId` | string |  | ✓ | ID of the post to retrieve. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code> | e.g. l0me7x |  |
| Username | `username` | string |  | ✓ | Reddit ID of the user to retrieve |  |
| Details | `details` | options | about | ✓ | Details of the user to retrieve |  |

**Details options:**

* **About** (`about`)
* **Comments** (`comments`)
* **Gilded** (`gilded`)
* **Overview** (`overview`)
* **Submitted** (`submitted`)

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |

### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Location | `location` | options | subreddit | ✗ | Location where to search for posts |  |

**Location options:**

* **All Reddit** (`allReddit`) - Search for posts in all of Reddit
* **Subreddit** (`subreddit`) - Search for posts in a specific subreddit

| Subreddit | `subreddit` | string |  | ✓ | The name of subreddit to search in |  |
| Keyword | `keyword` | string |  | ✓ | The keyword for the search |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The category to sort results by | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort | `sort` | options | relevance | The category to sort results by |

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
* Categories: Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: reddit
displayName: Reddit
description: Consume the Reddit API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: redditOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a top-level comment in a post
  params:
  - id: postId
    name: Post ID
    type: string
    default: ''
    required: true
    description: 'ID of the post to write the comment to. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code>'
    placeholder: l0me7x
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - post
          operation:
          - get
    typeInfo: &id004
      type: string
      displayName: Post ID
      name: postId
  - id: commentText
    name: Comment Text
    type: string
    default: ''
    required: true
    description: Text of the comment. Markdown supported.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - postComment
          operation:
          - create
    typeInfo:
      type: string
      displayName: Comment Text
      name: commentText
  - id: subreddit
    name: Subreddit
    type: string
    default: ''
    required: true
    description: Subreddit to create the post in
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - post
          operation:
          - search
          location:
          - subreddit
    typeInfo: &id002
      type: string
      displayName: Subreddit
      name: subreddit
  - id: kind
    name: Kind
    type: options
    default: self
    required: false
    description: The kind of the post to create
    validation:
      displayOptions:
        show:
          resource:
          - post
          operation:
          - create
    typeInfo:
      type: options
      displayName: Kind
      name: kind
      possibleValues:
      - value: self
        name: Text Post
        description: ''
      - value: link
        name: Link Post
        description: ''
      - value: image
        name: Image Post
        description: ''
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the post, up to 300 characters long
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - post
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: url
    name: URL
    type: string
    default: ''
    required: true
    description: URL of the post
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - post
          operation:
          - create
          kind:
          - link
          - image
    typeInfo:
      type: string
      displayName: URL
      name: url
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: Text of the post. Markdown supported.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - post
          operation:
          - create
          kind:
          - self
    typeInfo:
      type: string
      displayName: Text
      name: text
  - id: resubmit
    name: Resubmit
    type: boolean
    default: false
    required: false
    description: Whether the URL will be posted even if it was already posted to the
      subreddit before. Otherwise, the re-posting will trigger an error.
    validation:
      displayOptions:
        show:
          resource:
          - post
          operation:
          - create
          kind:
          - link
          - image
    typeInfo:
      type: boolean
      displayName: Resubmit
      name: resubmit
- id: getAll
  name: Get Many
  description: Retrieve many comments in a post
  params:
  - id: subreddit
    name: Subreddit
    type: string
    default: ''
    required: true
    description: The name of subreddit where the post is
    validation: *id001
    typeInfo: *id002
  - id: postId
    name: Post ID
    type: string
    default: ''
    required: true
    description: 'ID of the post to get all comments from. Found in the post URL:
      <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code>'
    placeholder: l0me7x
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id005
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
          details:
          - overview
          - submitted
          - comments
          - gilded
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
          details:
          - comments
          - gilded
          - overview
          - submitted
          returnAll:
          - false
    typeInfo: &id008
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
  - id: subreddit
    name: Subreddit
    type: string
    default: ''
    required: true
    description: The name of subreddit to retrieve the posts from
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: delete
  name: Delete
  description: Remove a comment from a post
  params:
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: ID of the comment to remove. Found in the comment URL:<code>/r/[subreddit_name]/comments/[post_id]/[post_title]/[comment_id]</code>
    placeholder: gla7fmt
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - postComment
          operation:
          - reply
    typeInfo: &id010
      type: string
      displayName: Comment ID
      name: commentId
  - id: postId
    name: Post ID
    type: string
    default: ''
    required: true
    description: 'ID of the post to delete. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code>'
    placeholder: gla7fmt
    validation: *id003
    typeInfo: *id004
- id: reply
  name: Reply
  description: Write a reply to a comment in a post
  params:
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: 'ID of the comment to reply to. To be found in the comment URL: <code>www.reddit.com/r/[subreddit_name]/comments/[post_id]/[post_title]/[comment_id]</code>'
    placeholder: gl9iroa
    validation: *id009
    typeInfo: *id010
  - id: replyText
    name: Reply Text
    type: string
    default: ''
    required: true
    description: Text of the reply. Markdown supported.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - postComment
          operation:
          - reply
    typeInfo:
      type: string
      displayName: Reply Text
      name: replyText
- id: get
  name: Get
  description: ''
  params:
  - id: details
    name: Details
    type: options
    default: identity
    required: true
    description: Details of my account to retrieve
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
    typeInfo: &id012
      type: options
      displayName: Details
      name: details
      possibleValues:
      - value: about
        name: About
        description: ''
      - value: comments
        name: Comments
        description: ''
      - value: gilded
        name: Gilded
        description: ''
      - value: overview
        name: Overview
        description: ''
      - value: submitted
        name: Submitted
        description: ''
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
  - id: content
    name: Content
    type: options
    default: about
    required: true
    description: Subreddit content to retrieve
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - subreddit
          operation:
          - get
    typeInfo:
      type: options
      displayName: Content
      name: content
      possibleValues:
      - value: about
        name: About
        description: ''
      - value: rules
        name: Rules
        description: ''
  - id: subreddit
    name: Subreddit
    type: string
    default: ''
    required: true
    description: The name of subreddit to retrieve the content from
    validation: *id001
    typeInfo: *id002
  - id: subreddit
    name: Subreddit
    type: string
    default: ''
    required: true
    description: The name of subreddit to retrieve the post from
    validation: *id001
    typeInfo: *id002
  - id: postId
    name: Post ID
    type: string
    default: ''
    required: true
    description: 'ID of the post to retrieve. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code>'
    placeholder: l0me7x
    validation: *id003
    typeInfo: *id004
  - id: username
    name: Username
    type: string
    default: ''
    required: true
    description: Reddit ID of the user to retrieve
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
      displayName: Username
      name: username
  - id: details
    name: Details
    type: options
    default: about
    required: true
    description: Details of the user to retrieve
    validation: *id011
    typeInfo: *id012
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: search
  name: Search
  description: Search posts in a subreddit or in all of Reddit
  params:
  - id: location
    name: Location
    type: options
    default: subreddit
    required: false
    description: Location where to search for posts
    validation:
      displayOptions:
        show:
          resource:
          - post
          operation:
          - search
    typeInfo:
      type: options
      displayName: Location
      name: location
      possibleValues:
      - value: allReddit
        name: All Reddit
        description: Search for posts in all of Reddit
      - value: subreddit
        name: Subreddit
        description: Search for posts in a specific subreddit
  - id: subreddit
    name: Subreddit
    type: string
    default: ''
    required: true
    description: The name of subreddit to search in
    validation: *id001
    typeInfo: *id002
  - id: keyword
    name: Keyword
    type: string
    default: ''
    required: true
    description: The keyword for the search
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - post
          operation:
          - search
    typeInfo:
      type: string
      displayName: Keyword
      name: keyword
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - user-agent
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: postId
    text: l0me7x
  - field: postId
    text: l0me7x
  - field: commentId
    text: gla7fmt
  - field: commentId
    text: gl9iroa
  - field: filters
    text: Add Field
  - field: postId
    text: gla7fmt
  - field: postId
    text: l0me7x
  - field: filters
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
  "$id": "https://n8n.io/schemas/nodes/reddit.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Reddit Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "getAll",
        "delete",
        "reply",
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
            "post",
            "postComment",
            "profile",
            "subreddit",
            "user"
          ],
          "default": "post"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "get"
          ],
          "default": "get"
        },
        "postId": {
          "description": "ID of the post to retrieve. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code>",
          "type": "string",
          "default": "",
          "examples": [
            "l0me7x"
          ]
        },
        "commentText": {
          "description": "Text of the comment. Markdown supported.",
          "type": "string",
          "default": ""
        },
        "subreddit": {
          "description": "The name of subreddit to search in",
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
        "commentId": {
          "description": "ID of the comment to reply to. To be found in the comment URL: <code>www.reddit.com/r/[subreddit_name]/comments/[post_id]/[post_title]/[comment_id]</code>",
          "type": "string",
          "default": "",
          "examples": [
            "gl9iroa"
          ]
        },
        "replyText": {
          "description": "Text of the reply. Markdown supported.",
          "type": "string",
          "default": ""
        },
        "details": {
          "description": "Details of the user to retrieve",
          "type": "string",
          "enum": [
            "about",
            "comments",
            "gilded",
            "overview",
            "submitted"
          ],
          "default": "about"
        },
        "content": {
          "description": "Subreddit content to retrieve",
          "type": "string",
          "enum": [
            "about",
            "rules"
          ],
          "default": "about"
        },
        "filters": {
          "description": "Category of the posts to retrieve",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "kind": {
          "description": "The kind of the post to create",
          "type": "string",
          "enum": [
            "self",
            "link",
            "image"
          ],
          "default": "self"
        },
        "title": {
          "description": "Title of the post, up to 300 characters long",
          "type": "string",
          "default": ""
        },
        "url": {
          "description": "URL of the post",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "text": {
          "description": "Text of the post. Markdown supported.",
          "type": "string",
          "default": ""
        },
        "resubmit": {
          "description": "Whether the URL will be posted even if it was already posted to the subreddit before. Otherwise, the re-posting will trigger an error.",
          "type": "boolean",
          "default": false
        },
        "location": {
          "description": "Location where to search for posts",
          "type": "string",
          "enum": [
            "allReddit",
            "subreddit"
          ],
          "default": "subreddit"
        },
        "keyword": {
          "description": "The keyword for the search",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The category to sort results by",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "username": {
          "description": "Reddit ID of the user to retrieve",
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
      "name": "redditOAuth2Api",
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
