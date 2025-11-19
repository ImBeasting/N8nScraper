---
title: "Node: X (Formerly Twitter)"
slug: "node-x"
version: "2"
updated: "2025-11-13"
summary: "Consume the X API"
node_type: "regular"
group: "['output']"
---

# Node: X (Formerly Twitter)

**Purpose.** Consume the X API
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `{'light': 'file:x.svg', 'dark': 'file:x.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **twitterOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **noticeLocation**: Locations are not supported due to Twitter V2 API limitations
- **noticeAttachments**: Attachements are not supported due to Twitter V2 API limitations

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `twitterOAuth2Api` | ✓ | - |

---

## Operations

### Directmessage Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Send a direct message to a user |

### List Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Member | `add` | Add a member to a list |

### Tweet Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create, quote, or reply to a tweet |
| Delete | `delete` | Delete a tweet |
| Like | `like` | Like a tweet |
| Retweet | `retweet` | Retweet a tweet |
| Search | `search` | Search for tweets from the last seven days |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `searchUser` | Retrieve a user by username |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | tweet | ✗ | Send a direct message to a user |  |

**Resource options:**

* **Direct Message** (`directMessage`) - Send a direct message to a user
* **List** (`list`) - Add a user to a list
* **Tweet** (`tweet`) - Create, like, search, or delete a tweet
* **User** (`user`) - Search users by username

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Send a direct message to a user |  |

**Operation options:**

* **Create** (`create`) - Send a direct message to a user

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User | `user` | resourceLocator |  | ✓ | The user you want to send the message to | e.g. e.g. n8n |  |
| Text | `text` | string |  | ✓ | The text of the direct message. URL encoding is required. Max length of 10,000 characters. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The attachment ID to associate with the message | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment ID | `attachments` | string |  | The attachment ID to associate with the message |

</details>

| Text | `text` | string |  | ✓ | The text of the status update. URLs must be encoded. Links wrapped with the t.co shortener will affect character count |  |
| Options | `additionalFields` | collection | {} | ✓ | Location information for the tweet | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Location ID | `location` | string |  | Location information for the tweet |
| Media ID | `attachments` | string |  | The attachment ID to associate with the message |
| Quote a Tweet | `inQuoteToStatusId` | resourceLocator |  | The tweet being quoted |
| Reply to Tweet | `inReplyToStatusId` | resourceLocator |  | The tweet being replied to |

</details>


### Add Member parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List | `list` | resourceLocator |  | ✓ | The list you want to add the user to | e.g. e.g. 99923132 |  |
| User | `user` | resourceLocator |  | ✓ | The user you want to add to the list | e.g. e.g. n8n |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tweet | `tweetDeleteId` | resourceLocator |  | ✓ | The tweet to delete | e.g. e.g. 1187836157394112513 |  |

### Like parameters (`like`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tweet | `tweetId` | resourceLocator |  | ✓ | The tweet to like | e.g. e.g. 1187836157394112513 |  |

### Retweet parameters (`retweet`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tweet | `tweetId` | resourceLocator |  | ✓ | The tweet to retweet | e.g. e.g. 1187836157394112513 |  |

### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Search Text | `searchText` | string |  | ✓ | A UTF-8, URL-encoded search query of 500 characters maximum, including operators. Queries may additionally be limited by complexity. Check the searching examples <a href="https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators">here</a>. | e.g. e.g. automation |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Options | `additionalFields` | collection | {} | ✓ | The order in which to return results | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort Order | `sortOrder` | options | recency | The order in which to return results |
| After | `startTime` | dateTime |  | Tweets before this date will not be returned. This date must be within the last 7 days if you don't have Academic Research access. |
| Before | `endTime` | dateTime |  | Tweets after this date will not be returned. This date must be within the last 7 days if you don't have Academic Research access. |
| Tweet Fields | `tweetFieldsObject` | multiOptions | [] | The fields to add to each returned tweet object. Default fields are: ID, text, edit_history_tweet_ids. |

</details>


### Get parameters (`searchUser`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User | `user` | resourceLocator |  | ✓ | The user you want to search | e.g. e.g. n8n |  |
| Me | `me` | boolean | False | ✗ | Whether you want to search the authenticated user |  |

---

## Load Options Methods

- `getLanguages`
- `for`
- `name`
- `value`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ":" + $parameter["resource"]}}`

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
node: X
displayName: X (Formerly Twitter)
description: Consume the X API
version: '2'
nodeType: regular
group:
- output
credentials:
- name: twitterOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Send a direct message to a user
  params:
  - id: user
    name: User
    type: resourceLocator
    default: ''
    required: true
    description: The user you want to send the message to
    placeholder: e.g. n8n
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - searchUser
          resource:
          - user
        hide:
          me:
          - true
    typeInfo: &id004
      type: resourceLocator
      displayName: User
      name: user
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: The text of the direct message. URL encoding is required. Max length
      of 10,000 characters.
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - tweet
    typeInfo: &id002
      type: string
      displayName: Text
      name: text
      typeOptions:
        rows: 2
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: The text of the status update. URLs must be encoded. Links wrapped
      with the t.co shortener will affect character count
    validation: *id001
    typeInfo: *id002
- id: add
  name: Add Member
  description: Add a member to a list
  params:
  - id: list
    name: List
    type: resourceLocator
    default: ''
    required: true
    description: The list you want to add the user to
    placeholder: e.g. 99923132
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - add
          resource:
          - list
    typeInfo:
      type: resourceLocator
      displayName: List
      name: list
  - id: user
    name: User
    type: resourceLocator
    default: ''
    required: true
    description: The user you want to add to the list
    placeholder: e.g. n8n
    validation: *id003
    typeInfo: *id004
- id: delete
  name: Delete
  description: Delete a tweet
  params:
  - id: tweetDeleteId
    name: Tweet
    type: resourceLocator
    default: ''
    required: true
    description: The tweet to delete
    placeholder: e.g. 1187836157394112513
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - tweet
          operation:
          - delete
    typeInfo:
      type: resourceLocator
      displayName: Tweet
      name: tweetDeleteId
- id: like
  name: Like
  description: Like a tweet
  params:
  - id: tweetId
    name: Tweet
    type: resourceLocator
    default: ''
    required: true
    description: The tweet to like
    placeholder: e.g. 1187836157394112513
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - retweet
          resource:
          - tweet
    typeInfo: &id006
      type: resourceLocator
      displayName: Tweet
      name: tweetId
- id: retweet
  name: Retweet
  description: Retweet a tweet
  params:
  - id: tweetId
    name: Tweet
    type: resourceLocator
    default: ''
    required: true
    description: The tweet to retweet
    placeholder: e.g. 1187836157394112513
    validation: *id005
    typeInfo: *id006
- id: search
  name: Search
  description: Search for tweets from the last seven days
  params:
  - id: searchText
    name: Search Text
    type: string
    default: ''
    required: true
    description: A UTF-8, URL-encoded search query of 500 characters maximum, including
      operators. Queries may additionally be limited by complexity. Check the searching
      examples <a href="https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators">here</a>.
    placeholder: e.g. automation
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - search
          resource:
          - tweet
    typeInfo:
      type: string
      displayName: Search Text
      name: searchText
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
          - tweet
          operation:
          - search
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
          resource:
          - tweet
          operation:
          - search
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
- id: searchUser
  name: Get
  description: Retrieve a user by username
  params:
  - id: user
    name: User
    type: resourceLocator
    default: ''
    required: true
    description: The user you want to search
    placeholder: e.g. n8n
    validation: *id003
    typeInfo: *id004
  - id: me
    name: Me
    type: boolean
    default: false
    required: false
    description: Whether you want to search the authenticated user
    validation:
      displayOptions:
        show:
          operation:
          - searchUser
          resource:
          - user
    typeInfo:
      type: boolean
      displayName: Me
      name: me
common_expressions:
- ={{$parameter["operation"] + ":" + $parameter["resource"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: noticeLocation
    text: Locations are not supported due to Twitter V2 API limitations
    conditions:
      show: {}
  - name: noticeAttachments
    text: Attachements are not supported due to Twitter V2 API limitations
    conditions:
      show: {}
  tooltips: []
  placeholders:
  - field: user
    text: e.g. n8n
  - field: additionalFields
    text: Add Field
  - field: list
    text: e.g. 99923132
  - field: user
    text: e.g. n8n
  - field: additionalFields
    text: Add Field
  - field: tweetDeleteId
    text: e.g. 1187836157394112513
  - field: tweetId
    text: e.g. 1187836157394112513
  - field: searchText
    text: e.g. automation
  - field: additionalFields
    text: Add Field
  - field: tweetId
    text: e.g. 1187836157394112513
  - field: user
    text: e.g. n8n
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
  "$id": "https://n8n.io/schemas/nodes/X.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "X (Formerly Twitter) Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "add",
        "delete",
        "like",
        "retweet",
        "search",
        "searchUser"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Send a direct message to a user",
          "type": "string",
          "enum": [
            "directMessage",
            "list",
            "tweet",
            "user"
          ],
          "default": "tweet"
        },
        "operation": {
          "description": "Retrieve a user by username",
          "type": "string",
          "enum": [
            "searchUser"
          ],
          "default": "searchUser"
        },
        "user": {
          "description": "The user you want to search",
          "type": "string",
          "examples": [
            "e.g. n8n"
          ]
        },
        "text": {
          "description": "The text of the status update. URLs must be encoded. Links wrapped with the t.co shortener will affect character count",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The order in which to return results",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "list": {
          "description": "The list you want to add the user to",
          "type": "string",
          "examples": [
            "e.g. 99923132"
          ]
        },
        "tweetDeleteId": {
          "description": "The tweet to delete",
          "type": "string",
          "examples": [
            "e.g. 1187836157394112513"
          ]
        },
        "tweetId": {
          "description": "The tweet to retweet",
          "type": "string",
          "examples": [
            "e.g. 1187836157394112513"
          ]
        },
        "searchText": {
          "description": "A UTF-8, URL-encoded search query of 500 characters maximum, including operators. Queries may additionally be limited by complexity. Check the searching examples <a href=\"https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators\">here</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. automation"
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
        "me": {
          "description": "Whether you want to search the authenticated user",
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
    "version": "2"
  },
  "credentials": [
    {
      "name": "twitterOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 2 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
