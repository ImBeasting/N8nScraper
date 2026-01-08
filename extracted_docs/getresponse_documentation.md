---
title: "Node: GetResponse"
slug: "node-getresponse"
version: "1"
updated: "2026-01-08"
summary: "Consume GetResponse API"
node_type: "regular"
group: "['input']"
---

# Node: GetResponse

**Purpose.** Consume GetResponse API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:getResponse.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **getResponseApi**: N/A
- **getResponseOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `getResponseApi` | ✓ | {'show': {'authentication': ['apiKey']}} |
| `getResponseOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new contact |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact |
| Get Many | `getAll` | Get many contacts |
| Update | `update` | Update contact properties |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✗ | Resource to operate on |  |

**Resource options:**

* **Contact** (`contact`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Create a new contact |  |

**Operation options:**

* **Create** (`create`) - Create a new contact
* **Delete** (`delete`) - Delete a contact
* **Get** (`get`) - Get a contact
* **Get Many** (`getAll`) - Get many contacts
* **Update** (`update`) - Update contact properties

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✗ | e.g. name@email.com | email |
| Campaign Name or ID | `campaignId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The end user specified key of the user defined data. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | The end user specified key of the user defined data. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Day Of Cycle | `dayOfCycle` | string |  | The day on which the contact is in the Autoresponder cycle. null indicates the contacts is not in the cycle. |
| IP Address | `ipAddress` | string |  | The contact's IP address. IPv4 and IPv6 formats are accepted. |
| Name | `name` | string |  |  |
| Note | `note` | string |  |  |
| Scoring | `scoring` | number |  | Contact scoring, pass null to remove the score from a contact |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | ID of contact to delete |  |
| Options | `options` | collection | {} | ✗ | This makes it possible to pass the IP from which the contact unsubscribed. Used only if the messageId was send. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| IP Address | `ipAddress` | string |  | This makes it possible to pass the IP from which the contact unsubscribed. Used only if the messageId was send. |
| Message ID | `messageId` | string |  | The ID of a message (such as a newsletter, an autoresponder, or an RSS-newsletter). When passed, this method will simulate the unsubscribe process, as if the contact clicked the unsubscribe link in a given message. |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | Unique identifier for a particular contact |  |
| Options | `options` | collection | {} | ✗ | List of fields that should be returned. ID is always returned. Fields should be separated by comma | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | List of fields that should be returned. ID is always returned. Fields should be separated by comma |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:∞ |
| Options | `options` | collection | {} | ✗ | Search contacts by campaign ID | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Campaign ID | `campaignId` | string |  | Search contacts by campaign ID |
| Change On From | `changeOnFrom` | dateTime |  | Search contacts edited from this date |
| Change On To | `changeOnTo` | dateTime |  | Search contacts edited to this date |
| Created On From | `createdOnFrom` | dateTime |  | Count data from this date |
| Created On To | `createdOnTo` | dateTime |  | Count data from this date |
| Exact Match | `exactMatch` | boolean | False | Whether to search for contacts with the exact value of the email and name provided in the query string. Without this flag, matching is done via a standard 'like' comparison, which may sometimes be slow. |
| Fields | `fields` | string |  | List of fields that should be returned. ID is always returned. Fields should be separated by comma |
| Name | `name` | string |  | Search contacts by name |
| Origin | `origin` | options |  | Search contacts by origin |
| Sort By | `sortBy` | options |  |  |
| Sort Order | `sortOrder` | options |  |  |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | Unique identifier for a particular contact |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Campaign Name or ID | `campaignId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | The end user specified key of the user defined data. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Day Of Cycle | `dayOfCycle` | string |  | The day on which the contact is in the Autoresponder cycle. null indicates the contacts is not in the cycle. |
| Email | `email` | string |  |  |
| IP Address | `ipAddress` | string |  | The contact's IP address. IPv4 and IPv6 formats are accepted. |
| Name | `name` | string |  |  |
| Note | `note` | string |  |  |
| Scoring | `scoring` | number |  | Contact scoring, pass null to remove the score from a contact |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>


---

## Load Options Methods

- `getCampaigns`
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
* Categories: Communication, Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: getResponse
displayName: GetResponse
description: Consume GetResponse API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: getResponseApi
  required: true
- name: getResponseOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a new contact
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: ''
    placeholder: name@email.com
    validation:
      format: email
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: campaignId
    name: Campaign Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
    typeInfo:
      type: options
      displayName: Campaign Name or ID
      name: campaignId
      typeOptions:
        loadOptionsMethod: getCampaigns
      possibleValues: []
- id: delete
  name: Delete
  description: Delete a contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of contact to delete
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: Contact ID
      name: contactId
- id: get
  name: Get
  description: Get a contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Unique identifier for a particular contact
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many contacts
  params:
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
          - contact
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 20
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          resource:
          - contact
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
- id: update
  name: Update
  description: Update contact properties
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Unique identifier for a particular contact
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
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: options
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
  "$id": "https://n8n.io/schemas/nodes/getResponse.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GetResponse Node",
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
        "update"
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
            "apiKey",
            "oAuth2"
          ],
          "default": "apiKey"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "contact"
          ],
          "default": "contact"
        },
        "operation": {
          "description": "Create a new contact",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "get"
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
        "campaignId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The end user specified key of the user defined data. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "contactId": {
          "description": "Unique identifier for a particular contact",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Search contacts by campaign ID",
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
          "default": 20
        },
        "updateFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
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
      "name": "getResponseApi",
      "required": true
    },
    {
      "name": "getResponseOAuth2Api",
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
