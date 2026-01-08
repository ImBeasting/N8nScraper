---
title: "Node: Emelia"
slug: "node-emelia"
version: "1"
updated: "2026-01-08"
summary: "Consume the Emelia API"
node_type: "regular"
group: "['input']"
---

# Node: Emelia

**Purpose.** Consume the Emelia API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:emelia.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **emeliaApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `emeliaApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

---

## Operations

### Campaign Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Contact | `addContact` | Add a contact to a campaign |
| Create | `create` | Create a campaign |
| Duplicate | `duplicate` | Duplicate a campaign |
| Get | `get` | Get a campaign |
| Get Many | `getAll` | Get many campaigns |
| Pause | `pause` | Pause a campaign |
| Start | `start` | Start a campaign |

### Contactlist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a contact list |
| Get Many | `getAll` | Get many contact lists |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | campaign | ✓ | Resource to operate on |  |

**Resource options:**

* **Campaign** (`campaign`)
* **Contact List** (`contactList`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Add Contact** (`addContact`) - Add a contact to a campaign
* **Create** (`create`) - Create a campaign
* **Duplicate** (`duplicate`) - Duplicate a campaign
* **Get** (`get`) - Get a campaign
* **Get Many** (`getAll`) - Get many campaigns
* **Pause** (`pause`) - Pause a campaign
* **Start** (`start`) - Start a campaign

---

### Add Contact parameters (`addContact`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign Name or ID | `campaignId` | options | [] | ✓ | The ID of the campaign to add the contact to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Contact Email | `contactEmail` | string |  | ✓ | The email of the contact to add to the campaign | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Filter by custom fields | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| First Name | `firstName` | string |  | First name of the contact to add |
| Last Contacted | `lastContacted` | dateTime |  | Last contacted date of the contact to add |
| Last Name | `lastName` | string |  | Last name of the contact to add |
| Last Open | `lastOpen` | dateTime |  | Last opened date of the contact to add |
| Last Replied | `lastReplied` | dateTime |  | Last replied date of the contact to add |
| Mails Sent | `mailsSent` | number | 0 | Number of emails sent to the contact to add |
| Phone Number | `phoneNumber` | string |  | Phone number of the contact to add |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign Name | `campaignName` | string |  | ✓ | The name of the campaign to create |  |

### Duplicate parameters (`duplicate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign Name or ID | `campaignId` | options |  | ✓ | The ID of the campaign to duplicate. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| New Campaign Name | `campaignName` | string |  | ✓ | The name of the new campaign to create |  |
| Options | `options` | collection | {} | ✗ | Whether to copy all the contacts from the original campaign | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Copy Contacts | `copyContacts` | boolean | False | Whether to copy all the contacts from the original campaign |
| Copy Email Provider | `copyProvider` | boolean | True | Whether to set the same email provider than the original campaign |
| Copy Email Sequence | `copyMails` | boolean | True | Whether to copy all the steps of the email sequence from the original campaign |
| Copy Global Settings | `copySettings` | boolean | True | Whether to copy all the general settings from the original campaign |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign ID | `campaignId` | string |  | ✓ | The ID of the campaign to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |

### Pause parameters (`pause`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign ID | `campaignId` | string |  | ✓ | The ID of the campaign to pause. The campaign must be in RUNNING mode. |  |

### Start parameters (`start`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign ID | `campaignId` | string |  | ✓ | The ID of the campaign to start. Email provider and contacts must be set. |  |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact List Name or ID | `contactListId` | options | [] | ✓ | The ID of the contact list to add the contact to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Contact Email | `contactEmail` | string |  | ✓ | The email of the contact to add to the contact list | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Filter by custom fields | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| First Name | `firstName` | string |  | First name of the contact to add |
| Last Contacted | `lastContacted` | dateTime |  | Last contacted date of the contact to add |
| Last Name | `lastName` | string |  | Last name of the contact to add |
| Last Open | `lastOpen` | dateTime |  | Last opened date of the contact to add |
| Last Replied | `lastReplied` | dateTime |  | Last replied date of the contact to add |
| Mails Sent | `mailsSent` | number | 0 | Number of emails sent to the contact to add |
| Phone Number | `phoneNumber` | string |  | Phone number of the contact to add |

</details>


---

## Load Options Methods

- `getCampaigns`

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
node: emelia
displayName: Emelia
description: Consume the Emelia API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: emeliaApi
  required: true
operations:
- id: addContact
  name: Add Contact
  description: ''
  params:
  - id: campaignId
    name: Campaign Name or ID
    type: options
    default: []
    required: true
    description: The ID of the campaign to add the contact to. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - duplicate
    typeInfo: &id002
      type: options
      displayName: Campaign Name or ID
      name: campaignId
      typeOptions:
        loadOptionsMethod: getCampaigns
      possibleValues: []
  - id: contactEmail
    name: Contact Email
    type: string
    default: ''
    required: true
    description: The email of the contact to add to the campaign
    validation: &id009
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - contactList
          operation:
          - add
    typeInfo: &id010
      type: string
      displayName: Contact Email
      name: contactEmail
- id: create
  name: Create
  description: ''
  params:
  - id: campaignName
    name: Campaign Name
    type: string
    default: ''
    required: true
    description: The name of the campaign to create
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - duplicate
    typeInfo: &id004
      type: string
      displayName: New Campaign Name
      name: campaignName
- id: duplicate
  name: Duplicate
  description: ''
  params:
  - id: campaignId
    name: Campaign Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the campaign to duplicate. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: campaignName
    name: New Campaign Name
    type: string
    default: ''
    required: true
    description: The name of the new campaign to create
    validation: *id003
    typeInfo: *id004
- id: get
  name: Get
  description: ''
  params:
  - id: campaignId
    name: Campaign ID
    type: string
    default: ''
    required: true
    description: The ID of the campaign to retrieve
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: ''
  params:
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
          - contactList
          operation:
          - getAll
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
          - contactList
          operation:
          - getAll
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
- id: pause
  name: Pause
  description: ''
  params:
  - id: campaignId
    name: Campaign ID
    type: string
    default: ''
    required: true
    description: The ID of the campaign to pause. The campaign must be in RUNNING
      mode.
    validation: *id001
    typeInfo: *id002
- id: start
  name: Start
  description: ''
  params:
  - id: campaignId
    name: Campaign ID
    type: string
    default: ''
    required: true
    description: The ID of the campaign to start. Email provider and contacts must
      be set.
    validation: *id001
    typeInfo: *id002
- id: add
  name: Add
  description: ''
  params:
  - id: contactListId
    name: Contact List Name or ID
    type: options
    default: []
    required: true
    description: The ID of the contact list to add the contact to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - contactList
          operation:
          - add
    typeInfo:
      type: options
      displayName: Contact List Name or ID
      name: contactListId
      typeOptions:
        loadOptionsMethod: getContactLists
      possibleValues: []
  - id: contactEmail
    name: Contact Email
    type: string
    default: ''
    required: true
    description: The email of the contact to add to the contact list
    validation: *id009
    typeInfo: *id010
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - POST
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: options
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
  "$id": "https://n8n.io/schemas/nodes/emelia.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Emelia Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "addContact",
        "create",
        "duplicate",
        "get",
        "getAll",
        "pause",
        "start",
        "add"
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
            "contactList"
          ],
          "default": "campaign"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "add",
            "getAll"
          ],
          "default": "getAll"
        },
        "campaignId": {
          "description": "The ID of the campaign to duplicate. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "contactEmail": {
          "description": "The email of the contact to add to the contact list",
          "type": "string",
          "default": "",
          "format": "email"
        },
        "additionalFields": {
          "description": "Filter by custom fields",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "campaignName": {
          "description": "The name of the new campaign to create",
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
        "options": {
          "description": "Whether to copy all the contacts from the original campaign",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "contactListId": {
          "description": "The ID of the contact list to add the contact to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
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
      "name": "emeliaApi",
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
