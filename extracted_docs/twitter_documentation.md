---
title: "Node: X (Formerly Twitter)"
slug: "node-twitter"
version: "1"
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

- **twitterOAuth1Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `twitterOAuth1Api` | ✓ | - |

---

## Operations

### Directmessage Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a direct message |

### Tweet Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create or reply a tweet |
| Delete | `delete` | Delete a tweet |
| Like | `like` | Like a tweet |
| Retweet | `retweet` | Retweet a tweet |
| Search | `search` | Search tweets |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | tweet | ✗ | Resource to operate on |  |

**Resource options:**

* **Direct Message** (`directMessage`)
* **Tweet** (`tweet`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a direct message |  |

**Operation options:**

* **Create** (`create`) - Create a direct message

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✓ | The ID of the user who should receive the direct message |  |
| Text | `text` | string |  | ✓ | The text of your Direct Message. URL encode as necessary. Max length of 10,000 characters. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the binary property which contain data that should be added to the direct message as attachment | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment | `attachment` | string | data | Name of the binary property which contain data that should be added to the direct message as attachment |

</details>

| Text | `text` | string |  | ✓ | The text of the status update. URL encode as necessary. t.co link wrapping will affect character counts. |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Name of the binary properties which contain data which should be added to tweet as attachment. Multiple ones can be comma-separated. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments | `attachments` | string | data | Name of the binary properties which contain data which should be added to tweet as attachment. Multiple ones can be comma-separated. |
| Display Coordinates | `displayCoordinates` | boolean | False | Whether or not to put a pin on the exact coordinates a Tweet has been sent from |
| In Reply to Tweet | `inReplyToStatusId` | string |  | The ID of an existing status that the update is in reply to |
| Location | `locationFieldsUi` | fixedCollection | {} | Subscriber location information.n |
| Possibly Sensitive | `possiblySensitive` | boolean | False | Whether you are uploading Tweet media that might be considered sensitive content such as nudity, or medical procedures |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tweet ID | `tweetId` | string |  | ✓ | The ID of the tweet to delete |  |

### Like parameters (`like`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tweet ID | `tweetId` | string |  | ✓ | The ID of the tweet |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether the entities will be omitted | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Entities | `includeEntities` | boolean | False | Whether the entities will be omitted |

</details>


### Retweet parameters (`retweet`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tweet ID | `tweetId` | string |  | ✓ | The ID of the tweet |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether each tweet returned in a timeline will include a user object including only the status authors numerical ID | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Trim User | `trimUser` | boolean | False | Whether each tweet returned in a timeline will include a user object including only the status authors numerical ID |

</details>


### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Search Text | `searchText` | string |  | ✓ | A UTF-8, URL-encoded search query of 500 characters maximum, including operators. Queries may additionally be limited by complexity. Check the searching examples <a href="https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators">here</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Whether the entities node will be included | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Entities | `includeEntities` | boolean | False | Whether the entities node will be included |
| Language Name or ID | `lang` | options |  | Restricts tweets to the given language, given by an ISO 639-1 code. Language detection is best-effort. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Location | `locationFieldsUi` | fixedCollection | {} | Subscriber location information.n |
| Result Type | `resultType` | options | mixed | Include both popular and real time results in the response |
| Tweet Mode | `tweetMode` | options | compat | When the extended mode is selected, the response contains the entire untruncated text of the Tweet |
| Until | `until` | dateTime |  | Returns tweets created before the given date |

</details>


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
node: Twitter
displayName: X (Formerly Twitter)
description: Consume the X API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: twitterOAuth1Api
  required: true
operations:
- id: create
  name: Create
  description: Create a direct message
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: The ID of the user who should receive the direct message
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - directMessage
    typeInfo:
      type: string
      displayName: User ID
      name: userId
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: The text of your Direct Message. URL encode as necessary. Max length
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
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: The text of the status update. URL encode as necessary. t.co link
      wrapping will affect character counts.
    validation: *id001
    typeInfo: *id002
- id: delete
  name: Delete
  description: Delete a tweet
  params:
  - id: tweetId
    name: Tweet ID
    type: string
    default: ''
    required: true
    description: The ID of the tweet to delete
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - retweet
          resource:
          - tweet
    typeInfo: &id004
      type: string
      displayName: Tweet ID
      name: tweetId
- id: like
  name: Like
  description: Like a tweet
  params:
  - id: tweetId
    name: Tweet ID
    type: string
    default: ''
    required: true
    description: The ID of the tweet
    validation: *id003
    typeInfo: *id004
- id: retweet
  name: Retweet
  description: Retweet a tweet
  params:
  - id: tweetId
    name: Tweet ID
    type: string
    default: ''
    required: true
    description: The ID of the tweet
    validation: *id003
    typeInfo: *id004
- id: search
  name: Search
  description: Search tweets
  params:
  - id: searchText
    name: Search Text
    type: string
    default: ''
    required: true
    description: A UTF-8, URL-encoded search query of 500 characters maximum, including
      operators. Queries may additionally be limited by complexity. Check the searching
      examples <a href="https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators">here</a>.
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
          operation:
          - search
          resource:
          - tweet
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
          - search
          resource:
          - tweet
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
common_expressions:
- ={{$parameter["operation"] + ":" + $parameter["resource"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
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
  "$id": "https://n8n.io/schemas/nodes/Twitter.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "X (Formerly Twitter) Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "like",
        "retweet",
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
            "directMessage",
            "tweet"
          ],
          "default": "tweet"
        },
        "operation": {
          "description": "Create or reply a tweet",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "like",
            "retweet",
            "search"
          ],
          "default": "create"
        },
        "userId": {
          "description": "The ID of the user who should receive the direct message",
          "type": "string",
          "default": ""
        },
        "text": {
          "description": "The text of the status update. URL encode as necessary. t.co link wrapping will affect character counts.",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Whether each tweet returned in a timeline will include a user object including only the status authors numerical ID",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "tweetId": {
          "description": "The ID of the tweet",
          "type": "string",
          "default": ""
        },
        "searchText": {
          "description": "A UTF-8, URL-encoded search query of 500 characters maximum, including operators. Queries may additionally be limited by complexity. Check the searching examples <a href=\"https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators\">here</a>.",
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
          "default": 50
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
      "name": "twitterOAuth1Api",
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
