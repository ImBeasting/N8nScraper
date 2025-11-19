---
title: "Node: Elastic Security"
slug: "node-elasticsecurity"
version: "1"
updated: "2025-11-13"
summary: "Consume the Elastic Security API"
node_type: "regular"
group: "['transform']"
---

# Node: Elastic Security

**Purpose.** Consume the Elastic Security API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:elasticSecurity.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **elasticSecurityApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `elasticSecurityApi` | ✓ | - |

---

## Operations

### Connector Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a connector |

### Case Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a case |
| Delete | `delete` | Delete a case |
| Get | `get` | Get a case |
| Get Many | `getAll` | Retrieve many cases |
| Get Status | `getStatus` | Retrieve a summary of all case activity |
| Update | `update` | Update a case |

### Casecomment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a comment to a case |
| Get | `get` | Get a case comment |
| Get Many | `getAll` | Retrieve many case comments |
| Remove | `remove` | Remove a comment from a case |
| Update | `update` | Update a comment in a case |

### Casetag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a tag to a case |
| Remove | `remove` | Remove a tag from a case |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | case | ✗ | Resource to operate on |  |

**Resource options:**

* **Case** (`case`)
* **Case Comment** (`caseComment`)
* **Case Tag** (`caseTag`)
* **Connector** (`connector`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a connector |  |

**Operation options:**

* **Create** (`create`) - Create a connector

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Connector Name | `name` | string |  | ✓ | Connectors allow you to send Elastic Security cases into other systems (only ServiceNow, Jira, or IBM Resilient) |  |
| Connector Type | `connectorType` | options | .jira | ✓ |  |  |

**Connector Type options:**

* **IBM Resilient** (`.resilient`)
* **Jira** (`.jira`)
* **ServiceNow ITSM** (`.servicenow`)

| API URL | `apiUrl` | string |  | ✓ | URL of the third-party instance | url |
| Email | `email` | string |  | ✓ | Jira-registered email | e.g. name@email.com | email |
| API Token | `apiToken` | string |  | ✓ | Jira API token |  |
| Project Key | `projectKey` | string |  | ✓ | Jira Project Key |  |
| Username | `username` | string |  | ✓ | ServiceNow ITSM username |  |
| Password | `password` | string |  | ✓ | ServiceNow ITSM password |  |
| API Key ID | `apiKeyId` | string |  | ✓ | IBM Resilient API key ID |  |
| API Key Secret | `apiKeySecret` | string |  | ✓ | IBM Resilient API key secret |  |
| Organization ID | `orgId` | string |  | ✓ | IBM Resilient organization ID |  |
| Title | `title` | string |  | ✓ |  |  |
| Connector Name or ID | `connectorId` | options |  | ✓ | Connectors allow you to send Elastic Security cases into other systems (only ServiceNow, Jira, or IBM Resilient). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Connector Type | `connectorType` | options | .jira | ✓ |  |  |

**Connector Type options:**

* **IBM Resilient** (`.resilient`)
* **Jira** (`.jira`)
* **ServiceNow ITSM** (`.servicenow`)

| Issue Type | `issueType` | string |  | ✓ | Type of the Jira issue to create for this case | e.g. Task |  |
| Priority | `priority` | string |  | ✓ | Priority of the Jira issue to create for this case | e.g. High |  |
| Urgency | `urgency` | options | 1 | ✓ | Urgency of the ServiceNow ITSM issue to create for this case |  |

**Urgency options:**

* **Low** (``)
* **Medium** (``)
* **High** (``)

| Severity | `severity` | options | 1 | ✓ | Severity of the ServiceNow ITSM issue to create for this case |  |

**Severity options:**

* **Low** (``)
* **Medium** (``)
* **High** (``)

| Impact | `impact` | options | 1 | ✓ | Impact of the ServiceNow ITSM issue to create for this case |  |

**Impact options:**

* **Low** (``)
* **Medium** (``)
* **High** (``)

| Category | `category` | string |  | ✓ | Category of the ServiceNow ITSM issue to create for this case | e.g. Helpdesk |  |
| Issue Types | `issueTypes` | string |  | ✓ | Comma-separated list of numerical types of the IBM Resilient issue to create for this case | e.g. 123,456 |  |
| Severity Code | `severityCode` | number | 1 | ✓ | Severity code of the IBM Resilient issue to create for this case | min:0, max:∞ |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Valid application owner registered within the Cases Role Based Access Control system | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |
| Owner | `owner` | string |  | Valid application owner registered within the Cases Role Based Access Control system |
| Sync Alerts | `syncAlerts` | boolean | False | Whether to synchronize with alerts |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Case ID | `caseId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Case ID | `caseId` | string |  | ✓ |  |  |
| Case ID | `caseId` | string |  | ✓ | ID of the case containing the comment to retrieve |  |
| Comment ID | `commentId` | string |  | ✓ | ID of the case comment to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Status | `status` | options | open |  |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Sort | `sortOptions` | fixedCollection | {} | ✗ | e.g. Add Sort Options |  |

<details>
<summary><strong>Sort sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort Options | `sortOptionsProperties` |  |  |  |

</details>

| Case ID | `caseId` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Case ID | `caseId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Whether to synchronize with alerts | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |
| Status | `status` | options | open |  |
| Sync Alerts | `syncAlerts` | boolean | False | Whether to synchronize with alerts |
| Title | `title` | string |  |  |
| Version | `version` | string |  |  |

</details>

| Case ID | `caseId` | string |  | ✓ | ID of the case containing the comment to retrieve |  |
| Comment ID | `commentId` | string |  | ✓ |  |  |
| Comment | `comment` | string |  | ✓ | Text to replace current comment message |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Case ID | `caseId` | string |  | ✓ | ID of the case containing the comment to retrieve |  |
| Comment | `comment` | string |  | ✓ |  |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Valid application owner registered within the Cases Role Based Access Control system | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Owner | `owner` | string |  | Valid application owner registered within the Cases Role Based Access Control system |

</details>

| Case ID | `caseId` | string |  | ✓ |  |  |
| Tag Name or ID | `tag` | options |  | ✓ | Tag to attach to the case. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Case ID | `caseId` | string |  | ✓ | ID of the case containing the comment to remove |  |
| Comment ID | `commentId` | string |  | ✓ |  |  |
| Case ID | `caseId` | string |  | ✓ |  |  |
| Tag Name or ID | `tag` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

---

## Load Options Methods

- `getTags`
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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: elasticSecurity
displayName: Elastic Security
description: Consume the Elastic Security API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: elasticSecurityApi
  required: true
operations:
- id: create
  name: Create
  description: Create a connector
  params:
  - id: name
    name: Connector Name
    type: string
    default: ''
    required: true
    description: Connectors allow you to send Elastic Security cases into other systems
      (only ServiceNow, Jira, or IBM Resilient)
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - connector
          operation:
          - create
    typeInfo:
      type: string
      displayName: Connector Name
      name: name
  - id: connectorType
    name: Connector Type
    type: options
    default: .jira
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
    typeInfo: &id002
      type: options
      displayName: Connector Type
      name: connectorType
      possibleValues:
      - value: .resilient
        name: IBM Resilient
        description: ''
      - value: .jira
        name: Jira
        description: ''
      - value: .servicenow
        name: ServiceNow ITSM
        description: ''
  - id: apiUrl
    name: API URL
    type: string
    default: ''
    required: true
    description: URL of the third-party instance
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - connector
          operation:
          - create
    typeInfo:
      type: string
      displayName: API URL
      name: apiUrl
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Jira-registered email
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - connector
          operation:
          - create
          connectorType:
          - .jira
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: apiToken
    name: API Token
    type: string
    default: ''
    required: true
    description: Jira API token
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - connector
          operation:
          - create
          connectorType:
          - .jira
    typeInfo:
      type: string
      displayName: API Token
      name: apiToken
      typeOptions:
        password: true
  - id: projectKey
    name: Project Key
    type: string
    default: ''
    required: true
    description: Jira Project Key
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - connector
          operation:
          - create
          connectorType:
          - .jira
    typeInfo:
      type: string
      displayName: Project Key
      name: projectKey
  - id: username
    name: Username
    type: string
    default: ''
    required: true
    description: ServiceNow ITSM username
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - connector
          operation:
          - create
          connectorType:
          - .servicenow
    typeInfo:
      type: string
      displayName: Username
      name: username
  - id: password
    name: Password
    type: string
    default: ''
    required: true
    description: ServiceNow ITSM password
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - connector
          operation:
          - create
          connectorType:
          - .servicenow
    typeInfo:
      type: string
      displayName: Password
      name: password
      typeOptions:
        password: true
  - id: apiKeyId
    name: API Key ID
    type: string
    default: ''
    required: true
    description: IBM Resilient API key ID
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - connector
          operation:
          - create
          connectorType:
          - .resilient
    typeInfo:
      type: string
      displayName: API Key ID
      name: apiKeyId
      typeOptions:
        password: true
  - id: apiKeySecret
    name: API Key Secret
    type: string
    default: ''
    required: true
    description: IBM Resilient API key secret
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - connector
          operation:
          - create
          connectorType:
          - .resilient
    typeInfo:
      type: string
      displayName: API Key Secret
      name: apiKeySecret
      typeOptions:
        password: true
  - id: orgId
    name: Organization ID
    type: string
    default: ''
    required: true
    description: IBM Resilient organization ID
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - connector
          operation:
          - create
          connectorType:
          - .resilient
    typeInfo:
      type: string
      displayName: Organization ID
      name: orgId
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
          - case
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: connectorId
    name: Connector Name or ID
    type: options
    default: ''
    required: true
    description: Connectors allow you to send Elastic Security cases into other systems
      (only ServiceNow, Jira, or IBM Resilient). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
    typeInfo:
      type: options
      displayName: Connector Name or ID
      name: connectorId
      typeOptions:
        loadOptionsMethod: getConnectors
      possibleValues: []
  - id: connectorType
    name: Connector Type
    type: options
    default: .jira
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: issueType
    name: Issue Type
    type: string
    default: ''
    required: true
    description: Type of the Jira issue to create for this case
    placeholder: Task
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
          connectorType:
          - .jira
    typeInfo:
      type: string
      displayName: Issue Type
      name: issueType
  - id: priority
    name: Priority
    type: string
    default: ''
    required: true
    description: Priority of the Jira issue to create for this case
    placeholder: High
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
          connectorType:
          - .jira
    typeInfo:
      type: string
      displayName: Priority
      name: priority
  - id: urgency
    name: Urgency
    type: options
    default: 1
    required: true
    description: Urgency of the ServiceNow ITSM issue to create for this case
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
          connectorType:
          - .servicenow
    typeInfo:
      type: options
      displayName: Urgency
      name: urgency
      possibleValues:
      - value: Low
        name: Low
        description: ''
      - value: Medium
        name: Medium
        description: ''
      - value: High
        name: High
        description: ''
  - id: severity
    name: Severity
    type: options
    default: 1
    required: true
    description: Severity of the ServiceNow ITSM issue to create for this case
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
          connectorType:
          - .servicenow
    typeInfo:
      type: options
      displayName: Severity
      name: severity
      possibleValues:
      - value: Low
        name: Low
        description: ''
      - value: Medium
        name: Medium
        description: ''
      - value: High
        name: High
        description: ''
  - id: impact
    name: Impact
    type: options
    default: 1
    required: true
    description: Impact of the ServiceNow ITSM issue to create for this case
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
          connectorType:
          - .servicenow
    typeInfo:
      type: options
      displayName: Impact
      name: impact
      possibleValues:
      - value: Low
        name: Low
        description: ''
      - value: Medium
        name: Medium
        description: ''
      - value: High
        name: High
        description: ''
  - id: category
    name: Category
    type: string
    default: ''
    required: true
    description: Category of the ServiceNow ITSM issue to create for this case
    placeholder: Helpdesk
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
          connectorType:
          - .servicenow
    typeInfo:
      type: string
      displayName: Category
      name: category
  - id: issueTypes
    name: Issue Types
    type: string
    default: ''
    required: true
    description: Comma-separated list of numerical types of the IBM Resilient issue
      to create for this case
    placeholder: 123,456
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
          connectorType:
          - .resilient
    typeInfo:
      type: string
      displayName: Issue Types
      name: issueTypes
  - id: severityCode
    name: Severity Code
    type: number
    default: 1
    required: true
    description: Severity code of the IBM Resilient issue to create for this case
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
          connectorType:
          - .resilient
    typeInfo:
      type: number
      displayName: Severity Code
      name: severityCode
      typeOptions:
        minValue: 0
- id: delete
  name: Delete
  description: Delete a case
  params:
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - caseTag
          operation:
          - remove
    typeInfo: &id004
      type: string
      displayName: Case ID
      name: caseId
- id: get
  name: Get
  description: Get a case
  params:
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ID of the case containing the comment to retrieve
    validation: *id003
    typeInfo: *id004
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: ID of the case comment to retrieve
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - caseComment
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Comment ID
      name: commentId
- id: getAll
  name: Get Many
  description: Retrieve many cases
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
          - caseComment
          operation:
          - getAll
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          resource:
          - caseComment
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
  - id: sortOptions
    name: Sort
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Sort Options
    validation:
      displayOptions:
        show:
          resource:
          - case
          operation:
          - getAll
    typeInfo:
      type: fixedCollection
      displayName: Sort
      name: sortOptions
      subProperties:
      - name: sortOptionsProperties
        displayName: Sort Options
        values:
        - displayName: Sort Key
          name: sortField
          type: options
          value: createdAt
          default: createdAt
          options:
          - name: Created At
            value: createdAt
            displayName: Created At
          - name: Updated At
            value: updatedAt
            displayName: Updated At
        - displayName: Sort Order
          name: sortOrder
          type: options
          value: asc
          default: asc
          options:
          - name: Ascending
            value: asc
            displayName: Ascending
          - name: Descending
            value: desc
            displayName: Descending
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: getStatus
  name: Get Status
  description: Retrieve a summary of all case activity
- id: update
  name: Update
  description: Update a case
  params:
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ID of the case containing the comment to retrieve
    validation: *id003
    typeInfo: *id004
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: comment
    name: Comment
    type: string
    default: ''
    required: true
    description: Text to replace current comment message
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - caseComment
          operation:
          - update
    typeInfo: &id012
      type: string
      displayName: Comment
      name: comment
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id013
      displayOptions:
        show:
          resource:
          - caseComment
          operation:
          - update
    typeInfo: &id014
      type: boolean
      displayName: Simplify
      name: simple
- id: add
  name: Add
  description: Add a comment to a case
  params:
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ID of the case containing the comment to retrieve
    validation: *id003
    typeInfo: *id004
  - id: comment
    name: Comment
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id013
    typeInfo: *id014
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: tag
    name: Tag Name or ID
    type: options
    default: ''
    required: true
    description: Tag to attach to the case. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - caseTag
          operation:
          - remove
    typeInfo: &id016
      type: options
      displayName: Tag Name or ID
      name: tag
      typeOptions:
        loadOptionsMethod: getTags
      possibleValues: []
- id: remove
  name: Remove
  description: Remove a comment from a case
  params:
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ID of the case containing the comment to remove
    validation: *id003
    typeInfo: *id004
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: tag
    name: Tag Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id015
    typeInfo: *id016
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: email
    text: name@email.com
  - field: issueType
    text: Task
  - field: priority
    text: High
  - field: category
    text: Helpdesk
  - field: issueTypes
    text: 123,456
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: sortOptions
    text: Add Sort Options
  - field: updateFields
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
  "$id": "https://n8n.io/schemas/nodes/elasticSecurity.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Elastic Security Node",
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
        "getStatus",
        "update",
        "add",
        "remove"
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
            "case",
            "caseComment",
            "caseTag",
            "connector"
          ],
          "default": "case"
        },
        "operation": {
          "description": "Add a tag to a case",
          "type": "string",
          "enum": [
            "add",
            "remove"
          ],
          "default": "add"
        },
        "name": {
          "description": "Connectors allow you to send Elastic Security cases into other systems (only ServiceNow, Jira, or IBM Resilient)",
          "type": "string",
          "default": ""
        },
        "connectorType": {
          "description": "",
          "type": "string",
          "enum": [
            ".resilient",
            ".jira",
            ".servicenow"
          ],
          "default": ".jira"
        },
        "apiUrl": {
          "description": "URL of the third-party instance",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "email": {
          "description": "Jira-registered email",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "apiToken": {
          "description": "Jira API token",
          "type": "string",
          "default": ""
        },
        "projectKey": {
          "description": "Jira Project Key",
          "type": "string",
          "default": ""
        },
        "username": {
          "description": "ServiceNow ITSM username",
          "type": "string",
          "default": ""
        },
        "password": {
          "description": "ServiceNow ITSM password",
          "type": "string",
          "default": ""
        },
        "apiKeyId": {
          "description": "IBM Resilient API key ID",
          "type": "string",
          "default": ""
        },
        "apiKeySecret": {
          "description": "IBM Resilient API key secret",
          "type": "string",
          "default": ""
        },
        "orgId": {
          "description": "IBM Resilient organization ID",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "connectorId": {
          "description": "Connectors allow you to send Elastic Security cases into other systems (only ServiceNow, Jira, or IBM Resilient). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "issueType": {
          "description": "Type of the Jira issue to create for this case",
          "type": "string",
          "default": "",
          "examples": [
            "Task"
          ]
        },
        "priority": {
          "description": "Priority of the Jira issue to create for this case",
          "type": "string",
          "default": "",
          "examples": [
            "High"
          ]
        },
        "urgency": {
          "description": "Urgency of the ServiceNow ITSM issue to create for this case",
          "type": "string",
          "enum": [
            "Low",
            "Medium",
            "High"
          ],
          "default": 1
        },
        "severity": {
          "description": "Severity of the ServiceNow ITSM issue to create for this case",
          "type": "string",
          "enum": [
            "Low",
            "Medium",
            "High"
          ],
          "default": 1
        },
        "impact": {
          "description": "Impact of the ServiceNow ITSM issue to create for this case",
          "type": "string",
          "enum": [
            "Low",
            "Medium",
            "High"
          ],
          "default": 1
        },
        "category": {
          "description": "Category of the ServiceNow ITSM issue to create for this case",
          "type": "string",
          "default": "",
          "examples": [
            "Helpdesk"
          ]
        },
        "issueTypes": {
          "description": "Comma-separated list of numerical types of the IBM Resilient issue to create for this case",
          "type": "string",
          "default": "",
          "examples": [
            "123,456"
          ]
        },
        "severityCode": {
          "description": "Severity code of the IBM Resilient issue to create for this case",
          "type": "number",
          "default": 1
        },
        "additionalFields": {
          "description": "Valid application owner registered within the Cases Role Based Access Control system",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "caseId": {
          "description": "",
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
        },
        "filters": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "sortOptions": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Sort Options"
          ]
        },
        "updateFields": {
          "description": "Whether to synchronize with alerts",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "comment": {
          "description": "Text to replace current comment message",
          "type": "string",
          "default": ""
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "commentId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "tag": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
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
      "name": "elasticSecurityApi",
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
