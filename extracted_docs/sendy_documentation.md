---
title: "Node: Sendy"
slug: "node-sendy"
version: "1"
updated: "2025-11-13"
summary: "Consume Sendy API"
node_type: "regular"
group: "['input']"
---

# Node: Sendy

**Purpose.** Consume Sendy API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:sendy.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **sendyApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `sendyApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Campaign Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a campaign |

### Subscriber Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a subscriber to a list |
| Count | `count` | Count subscribers |
| Delete | `delete` | Delete a subscriber from a list |
| Remove | `remove` | Unsubscribe user from a list |
| Status | `status` | Get the status of subscriber |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | subscriber | ✗ | Resource to operate on |  |

**Resource options:**

* **Campaign** (`campaign`)
* **Subscriber** (`subscriber`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a campaign |  |

**Operation options:**

* **Create** (`create`) - Create a campaign

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From Name | `fromName` | string |  | ✗ | The 'From name' of your campaign |  |
| From Email | `fromEmail` | string |  | ✗ | The 'From email' of your campaign | email |
| Reply To | `replyTo` | string |  | ✗ | The 'Reply to' of your campaign |  |
| Title | `title` | string |  | ✗ | The 'Title' of your campaign |  |
| Subject | `subject` | string |  | ✗ | The 'Subject' of your campaign |  |
| HTML Text | `htmlText` | string |  | ✗ | The 'HTML version' of your campaign |  |
| Send Campaign | `sendCampaign` | boolean | False | ✗ | Whether to send the campaign as well and not just create a draft. Default is false. |  |
| Brand ID | `brandId` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Lists to exclude from your campaign. List IDs should be single or comma-separated. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude List IDs | `excludeListIds` | string |  | Lists to exclude from your campaign. List IDs should be single or comma-separated. |
| Exclude Segment IDs | `excludeSegmentIds` | string |  | Segments to exclude from your campaign. Segment IDs should be single or comma-separated. |
| List IDs | `listIds` | string |  | List IDs should be single or comma-separated |
| Plain Text | `plainText` | string |  | The 'Plain text version' of your campaign |
| Querystring | `queryString` | string |  | Google Analytics tags |
| Segment IDs | `segmentIds` | string |  | Segment IDs should be single or comma-separated |
| Track Clicks | `trackClicks` | boolean | True | Whether to disable clicks tracking. Default is true. |
| Track Opens | `trackOpens` | boolean | True | Whether to disable opens tracking. Default is true. |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✗ | Email address of the subscriber | e.g. name@email.com | email |
| List ID | `listId` | string |  | ✗ | The list ID you want to subscribe a user to. This encrypted & hashed ID can be found under View all lists section named ID. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | User's 2 letter country code | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Country | `country` | string |  | User's 2 letter country code |
| GDPR | `gdpr` | boolean | False | Whether you're signing up EU users in a GDPR compliant manner |
| Honeypot | `hp` | boolean | False | Include this 'honeypot' field to prevent spambots from signing up via this API call. When spambots fills in this field, this API call will exit, preventing them from signing up fake addresses to your form. This parameter is only supported in Sendy 3.0 onwards. |
| IP Address | `ipaddress` | string |  | User's IP address |
| Name | `name` | string |  | User's name |
| Referrer | `referrer` | string |  | The URL where the user signed up from |
| Silent | `silent` | boolean | False | Set to "true" if your list is 'Double opt-in' but you want to bypass that and signup the user to the list as 'Single Opt-in instead' (optional) |

</details>


### Count parameters (`count`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List ID | `listId` | string |  | ✗ | The list ID you want to subscribe a user to. This encrypted & hashed ID can be found under View all lists section named ID. |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✗ | Email address of the subscriber | e.g. name@email.com | email |
| List ID | `listId` | string |  | ✗ | The list ID you want to subscribe a user to. This encrypted & hashed ID can be found under View all lists section named ID. |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✗ | Email address of the subscriber | e.g. name@email.com | email |
| List ID | `listId` | string |  | ✗ | The list ID you want to subscribe a user to. This encrypted & hashed ID can be found under View all lists section named ID. |  |

### Status parameters (`status`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✗ | Email address of the subscriber | e.g. name@email.com | email |
| List ID | `listId` | string |  | ✗ | The list ID you want to subscribe a user to. This encrypted & hashed ID can be found under View all lists section named ID. |  |

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
* Categories: Communication, Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: sendy
displayName: Sendy
description: Consume Sendy API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: sendyApi
  required: true
operations:
- id: create
  name: Create
  description: Create a campaign
  params:
  - id: fromName
    name: From Name
    type: string
    default: ''
    required: false
    description: The 'From name' of your campaign
    validation:
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - create
    typeInfo:
      type: string
      displayName: From Name
      name: fromName
  - id: fromEmail
    name: From Email
    type: string
    default: ''
    required: false
    description: The 'From email' of your campaign
    validation:
      format: email
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - create
    typeInfo:
      type: string
      displayName: From Email
      name: fromEmail
  - id: replyTo
    name: Reply To
    type: string
    default: ''
    required: false
    description: The 'Reply to' of your campaign
    validation:
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - create
    typeInfo:
      type: string
      displayName: Reply To
      name: replyTo
  - id: title
    name: Title
    type: string
    default: ''
    required: false
    description: The 'Title' of your campaign
    validation:
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: subject
    name: Subject
    type: string
    default: ''
    required: false
    description: The 'Subject' of your campaign
    validation:
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - create
    typeInfo:
      type: string
      displayName: Subject
      name: subject
  - id: htmlText
    name: HTML Text
    type: string
    default: ''
    required: false
    description: The 'HTML version' of your campaign
    validation:
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - create
    typeInfo:
      type: string
      displayName: HTML Text
      name: htmlText
  - id: sendCampaign
    name: Send Campaign
    type: boolean
    default: false
    required: false
    description: Whether to send the campaign as well and not just create a draft.
      Default is false.
    validation:
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - create
    typeInfo:
      type: boolean
      displayName: Send Campaign
      name: sendCampaign
  - id: brandId
    name: Brand ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - campaign
          sendCampaign:
          - false
    typeInfo:
      type: string
      displayName: Brand ID
      name: brandId
- id: add
  name: Add
  description: Add a subscriber to a list
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email address of the subscriber
    placeholder: name@email.com
    validation: &id003
      format: email
      displayOptions:
        show:
          resource:
          - subscriber
          operation:
          - status
    typeInfo: &id004
      type: string
      displayName: Email
      name: email
  - id: listId
    name: List ID
    type: string
    default: ''
    required: false
    description: The list ID you want to subscribe a user to. This encrypted & hashed
      ID can be found under View all lists section named ID.
    validation: &id001
      displayOptions:
        show:
          resource:
          - subscriber
          operation:
          - status
    typeInfo: &id002
      type: string
      displayName: List ID
      name: listId
- id: count
  name: Count
  description: Count subscribers
  params:
  - id: listId
    name: List ID
    type: string
    default: ''
    required: false
    description: The list ID you want to subscribe a user to. This encrypted & hashed
      ID can be found under View all lists section named ID.
    validation: *id001
    typeInfo: *id002
- id: delete
  name: Delete
  description: Delete a subscriber from a list
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email address of the subscriber
    placeholder: name@email.com
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List ID
    type: string
    default: ''
    required: false
    description: The list ID you want to subscribe a user to. This encrypted & hashed
      ID can be found under View all lists section named ID.
    validation: *id001
    typeInfo: *id002
- id: remove
  name: Remove
  description: Unsubscribe user from a list
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email address of the subscriber
    placeholder: name@email.com
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List ID
    type: string
    default: ''
    required: false
    description: The list ID you want to subscribe a user to. This encrypted & hashed
      ID can be found under View all lists section named ID.
    validation: *id001
    typeInfo: *id002
- id: status
  name: Status
  description: Get the status of subscriber
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email address of the subscriber
    placeholder: name@email.com
    validation: *id003
    typeInfo: *id004
  - id: listId
    name: List ID
    type: string
    default: ''
    required: false
    description: The list ID you want to subscribe a user to. This encrypted & hashed
      ID can be found under View all lists section named ID.
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: email
    text: name@email.com
  - field: email
    text: name@email.com
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
  "$id": "https://n8n.io/schemas/nodes/sendy.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Sendy Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "add",
        "count",
        "delete",
        "remove",
        "status"
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
            "campaign",
            "subscriber"
          ],
          "default": "subscriber"
        },
        "operation": {
          "description": "Add a subscriber to a list",
          "type": "string",
          "enum": [
            "add",
            "count",
            "delete",
            "remove",
            "status"
          ],
          "default": "add"
        },
        "fromName": {
          "description": "The 'From name' of your campaign",
          "type": "string",
          "default": ""
        },
        "fromEmail": {
          "description": "The 'From email' of your campaign",
          "type": "string",
          "default": "",
          "format": "email"
        },
        "replyTo": {
          "description": "The 'Reply to' of your campaign",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "The 'Title' of your campaign",
          "type": "string",
          "default": ""
        },
        "subject": {
          "description": "The 'Subject' of your campaign",
          "type": "string",
          "default": ""
        },
        "htmlText": {
          "description": "The 'HTML version' of your campaign",
          "type": "string",
          "default": ""
        },
        "sendCampaign": {
          "description": "Whether to send the campaign as well and not just create a draft. Default is false.",
          "type": "boolean",
          "default": false
        },
        "brandId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "User's 2 letter country code",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "email": {
          "description": "Email address of the subscriber",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "listId": {
          "description": "The list ID you want to subscribe a user to. This encrypted & hashed ID can be found under View all lists section named ID.",
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
      "name": "sendyApi",
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
