---
title: "Node: Lemlist"
slug: "node-lemlist"
version: "2"
updated: "2025-11-13"
summary: "Consume the Lemlist API"
node_type: "regular"
group: "['transform']"
---

# Node: Lemlist

**Purpose.** Consume the Lemlist API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:lemlist.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **lemlistApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `lemlistApi` | ✓ | - |

---

## Operations

### Unsubscribe Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add an email to an unsubscribe list |
| Delete | `delete` | Delete an email from an unsubscribe list |
| Get Many | `getAll` | Get many unsubscribed emails |

### Activity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many activities |

### Campaign Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many campaigns |
| Get Stats | `getStats` | Get campaign stats |

### Enrich Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Fetches a previously completed enrichment |
| Enrich Lead | `enrichLead` | Enrich a lead using an email or LinkedIn URL |
| Enrich Person | `enrichPerson` | Enrich a person using an email or LinkedIn URL |

### Lead Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a lead |
| Delete | `delete` | Delete a lead |
| Get | `get` | Get a lead |
| Unsubscribe | `unsubscribe` | Unsubscribe a lead |

### Team Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a team |
| Get Credits | `getCredits` | Get team credits |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | activity | ✗ | Resource to operate on |  |

**Resource options:**

* **Activity** (`activity`)
* **Campaign** (`campaign`)
* **Enrichment** (`enrich`)
* **Lead** (`lead`)
* **Team** (`team`)
* **Unsubscribe** (`unsubscribe`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | add | ✗ | Operation to perform |  |

**Operation options:**

* **Add** (`add`) - Add an email to an unsubscribe list
* **Delete** (`delete`) - Delete an email from an unsubscribe list
* **Get Many** (`getAll`) - Get many unsubscribed emails

---

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✗ | Email to add to the unsubscribes | e.g. name@email.com | email |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✗ | Email to delete from the unsubscribes | e.g. name@email.com | email |
| Campaign Name or ID | `campaignId` | options | [] | ✓ | ID of the campaign to remove the lead from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Email | `email` | string |  | ✗ | Email of the lead to delete | e.g. name@email.com | email |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | ID of the campaign to retrieve activity for. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Campaign Name or ID | `campaignId` | options |  | ID of the campaign to retrieve activity for. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Is First | `isFirst` | boolean | False |  |
| Lead ID | `leadId` | string |  |  |
| Type | `type` | options | emailsOpened | Type of activity to retrieve |
| Version | `version` | string | v2 |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Version | `version` | string | v2 |  |

</details>


### Get Stats parameters (`getStats`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign Name or ID | `campaignId` | options | [] | ✓ | ID of the campaign to get stats for. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Start Date | `startDate` | dateTime |  | ✓ | e.g. e.g. 2024-09-03 00:00:00Z |  |
| End Date | `endDate` | dateTime |  | ✓ | e.g. e.g. 2024-09-03 00:00:00Z |  |
| Timezone | `timezone` | string |  | ✓ | e.g. e.g. Europe/Paris |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Enrichment ID | `enrichId` | string |  | ✓ | ID of the enrichment to retrieve |  |
| Email | `email` | string |  | ✗ | Email of the lead to retrieve | e.g. name@email.com | email |

### Enrich Lead parameters (`enrichLead`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Lead ID | `leadId` | string |  | ✓ |  |  |
| Find Email | `findEmail` | boolean | False | ✗ |  | email |
| Verify Email | `verifyEmail` | boolean | False | ✗ |  | email |
| LinkedIn Enrichment | `linkedinEnrichment` | boolean | False | ✗ |  |  |
| Find Phone | `findPhone` | boolean | False | ✗ |  |  |

### Enrich Person parameters (`enrichPerson`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Find Email | `findEmail` | boolean | False | ✗ |  | email |
| Verify Email | `verifyEmail` | boolean | False | ✗ |  | email |
| LinkedIn Enrichment | `linkedinEnrichment` | boolean | False | ✗ |  |  |
| Find Phone | `findPhone` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  |  |
| First Name | `firstName` | string |  |  |
| Last Name | `lastName` | string |  |  |
| LinkedIn Url | `linkedinUrl` | string |  |  |
| Company Name | `companyName` | string |  |  |
| Company Domain | `companyDomain` | string |  |  |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign Name or ID | `campaignId` | options | [] | ✓ | ID of the campaign to create the lead under. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Email | `email` | string |  | ✗ | Email of the lead to create | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Company name of the lead to create | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company Name | `companyName` | string |  | Company name of the lead to create |
| Company Domain | `companyDomain` | string |  | Company domain of the lead to create |
| Deduplicate | `deduplicate` | boolean | False | Whether to do not insert if this email is already present in another campaign |
| Find Email | `findEmail` | boolean | False | Whether to find verified email |
| Find Phone | `findPhone` | boolean | False | Whether to find phone number |
| First Name | `firstName` | string |  | First name of the lead to create |
| Icebreaker | `icebreaker` | string |  | Icebreaker of the lead to create |
| Job Title | `jobTitle` | string |  | Job title of the lead to create |
| Last Name | `lastName` | string |  | Last name of the lead to create |
| LinkedIn Enrichment | `linkedinEnrichment` | boolean | False | Whether to run the LinkedIn enrichment |
| LinkedIn URL | `linkedinUrl` | string |  | LinkedIn URL of the lead to create |
| Phone | `phone` | string |  | Phone number of the lead to create |
| Picture URL | `picture` | string |  | Picture URL of the lead to create |
| Verify Email | `verifyEmail` | boolean | False | Whether to verify existing email (debounce) |

</details>


### Unsubscribe parameters (`unsubscribe`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign Name or ID | `campaignId` | options | [] | ✓ | ID of the campaign to unsubscribe the lead from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Email | `email` | string |  | ✗ | Email of the lead to unsubscribe | e.g. name@email.com | email |

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: lemlist
displayName: Lemlist
description: Consume the Lemlist API
version: '2'
nodeType: regular
group:
- transform
credentials:
- name: lemlistApi
  required: true
operations:
- id: add
  name: Add
  description: ''
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email to add to the unsubscribes
    placeholder: name@email.com
    validation: &id001
      format: email
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - unsubscribe
    typeInfo: &id002
      type: string
      displayName: Email
      name: email
- id: delete
  name: Delete
  description: ''
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email to delete from the unsubscribes
    placeholder: name@email.com
    validation: *id001
    typeInfo: *id002
  - id: campaignId
    name: Campaign Name or ID
    type: options
    default: []
    required: true
    description: ID of the campaign to remove the lead from. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - unsubscribe
    typeInfo: &id008
      type: options
      displayName: Campaign Name or ID
      name: campaignId
      typeOptions:
        loadOptionsMethod: getCampaigns
      possibleValues: []
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email of the lead to delete
    placeholder: name@email.com
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
    validation: &id003
      displayOptions:
        show:
          resource:
          - campaign
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
          - campaign
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
        maxValue: 1000
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
- id: getStats
  name: Get Stats
  description: ''
  params:
  - id: campaignId
    name: Campaign Name or ID
    type: options
    default: []
    required: true
    description: ID of the campaign to get stats for. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
  - id: startDate
    name: Start Date
    type: dateTime
    default: ''
    required: true
    description: ''
    placeholder: e.g. 2024-09-03 00:00:00Z
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - getStats
    typeInfo:
      type: dateTime
      displayName: Start Date
      name: startDate
  - id: endDate
    name: End Date
    type: dateTime
    default: ''
    required: true
    description: ''
    placeholder: e.g. 2024-09-03 00:00:00Z
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - getStats
    typeInfo:
      type: dateTime
      displayName: End Date
      name: endDate
  - id: timezone
    name: Timezone
    type: string
    default: ''
    required: true
    description: ''
    placeholder: e.g. Europe/Paris
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - getStats
    typeInfo:
      type: string
      displayName: Timezone
      name: timezone
- id: get
  name: Get
  description: ''
  params:
  - id: enrichId
    name: Enrichment ID
    type: string
    default: ''
    required: true
    description: ID of the enrichment to retrieve
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - enrich
          operation:
          - get
    typeInfo:
      type: string
      displayName: Enrichment ID
      name: enrichId
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email of the lead to retrieve
    placeholder: name@email.com
    validation: *id001
    typeInfo: *id002
- id: enrichLead
  name: Enrich Lead
  description: ''
  params:
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - enrich
          operation:
          - enrichLead
    typeInfo:
      type: string
      displayName: Lead ID
      name: leadId
  - id: findEmail
    name: Find Email
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id009
      format: email
      displayOptions:
        show:
          resource:
          - enrich
          operation:
          - enrichLead
          - enrichPerson
    typeInfo: &id010
      type: boolean
      displayName: Find Email
      name: findEmail
  - id: verifyEmail
    name: Verify Email
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id011
      format: email
      displayOptions:
        show:
          resource:
          - enrich
          operation:
          - enrichLead
          - enrichPerson
    typeInfo: &id012
      type: boolean
      displayName: Verify Email
      name: verifyEmail
  - id: linkedinEnrichment
    name: LinkedIn Enrichment
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id013
      displayOptions:
        show:
          resource:
          - enrich
          operation:
          - enrichLead
          - enrichPerson
    typeInfo: &id014
      type: boolean
      displayName: LinkedIn Enrichment
      name: linkedinEnrichment
  - id: findPhone
    name: Find Phone
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id015
      displayOptions:
        show:
          resource:
          - enrich
          operation:
          - enrichLead
          - enrichPerson
    typeInfo: &id016
      type: boolean
      displayName: Find Phone
      name: findPhone
- id: enrichPerson
  name: Enrich Person
  description: ''
  params:
  - id: findEmail
    name: Find Email
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: verifyEmail
    name: Verify Email
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: linkedinEnrichment
    name: LinkedIn Enrichment
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id013
    typeInfo: *id014
  - id: findPhone
    name: Find Phone
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id015
    typeInfo: *id016
- id: create
  name: Create
  description: ''
  params:
  - id: campaignId
    name: Campaign Name or ID
    type: options
    default: []
    required: true
    description: ID of the campaign to create the lead under. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email of the lead to create
    placeholder: name@email.com
    validation: *id001
    typeInfo: *id002
- id: unsubscribe
  name: Unsubscribe
  description: ''
  params:
  - id: campaignId
    name: Campaign Name or ID
    type: options
    default: []
    required: true
    description: ID of the campaign to unsubscribe the lead from. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email of the lead to unsubscribe
    placeholder: name@email.com
    validation: *id001
    typeInfo: *id002
- id: getCredits
  name: Get Credits
  description: ''
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: email
    text: name@email.com
  - field: email
    text: name@email.com
  - field: filters
    text: Add Filter
  - field: filters
    text: Add Filter
  - field: startDate
    text: e.g. 2024-09-03 00:00:00Z
  - field: endDate
    text: e.g. 2024-09-03 00:00:00Z
  - field: timezone
    text: e.g. Europe/Paris
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
  "$id": "https://n8n.io/schemas/nodes/lemlist.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Lemlist Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "add",
        "delete",
        "getAll",
        "getStats",
        "get",
        "enrichLead",
        "enrichPerson",
        "create",
        "unsubscribe",
        "getCredits"
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
            "activity",
            "campaign",
            "enrich",
            "lead",
            "team",
            "unsubscribe"
          ],
          "default": "activity"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "get",
            "getCredits"
          ],
          "default": "get"
        },
        "email": {
          "description": "Email of the lead to unsubscribe",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
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
        "filters": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "campaignId": {
          "description": "ID of the campaign to unsubscribe the lead from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "startDate": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. 2024-09-03 00:00:00Z"
          ]
        },
        "endDate": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. 2024-09-03 00:00:00Z"
          ]
        },
        "timezone": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Europe/Paris"
          ]
        },
        "enrichId": {
          "description": "ID of the enrichment to retrieve",
          "type": "string",
          "default": ""
        },
        "leadId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "findEmail": {
          "description": "",
          "type": "boolean",
          "default": false,
          "format": "email"
        },
        "verifyEmail": {
          "description": "",
          "type": "boolean",
          "default": false,
          "format": "email"
        },
        "linkedinEnrichment": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "findPhone": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "additionalFields": {
          "description": "Company name of the lead to create",
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
    "version": "2"
  },
  "credentials": [
    {
      "name": "lemlistApi",
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
