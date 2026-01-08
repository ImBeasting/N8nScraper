---
title: "Node: GoToWebinar"
slug: "node-gotowebinar"
version: "1"
updated: "2026-01-08"
summary: "Consume the GoToWebinar API"
node_type: "regular"
group: "['transform']"
---

# Node: GoToWebinar

**Purpose.** Consume the GoToWebinar API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:gotowebinar.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **goToWebinarOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `goToWebinarOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** user-agent, Content-Type

---

## Operations

### Webinar Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a webinar |
| Delete | `delete` |  |
| Get | `get` | Get a webinar |
| Get Many | `getAll` | Get many webinars |
| Update | `update` | Update a webinar |

### Attendee Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get an attendee |
| Get Many | `getAll` | Get many attendees |
| Get Details | `getDetails` | Get details of an attendee |

### Coorganizer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a coorganizer |
| Delete | `delete` | Delete a coorganizer |
| Get Many | `getAll` | Get many coorganizers |
| Reinvite | `reinvite` | Reinvite a coorganizer |

### Panelist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a panelist |
| Delete | `delete` | Delete a panelist |
| Get Many | `getAll` | Get many panelists |
| Reinvite | `reinvite` | Reinvite a panelist |

### Registrant Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a registrant |
| Delete | `delete` | Delete a registrant |
| Get | `get` | Get a registrant |
| Get Many | `getAll` | Get many registrants |

### Session Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a session |
| Get Many | `getAll` | Get many sessions |
| Get Details | `getDetails` | Get details on a session |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | attendee | ✗ | Resource to operate on |  |

**Resource options:**

* **Attendee** (`attendee`)
* **Co-Organizer** (`coorganizer`)
* **Panelist** (`panelist`)
* **Registrant** (`registrant`)
* **Session** (`session`)
* **Webinar** (`webinar`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create a webinar
* **Delete** (`delete`)
* **Get** (`get`) - Get a webinar
* **Get Many** (`getAll`) - Get many webinars
* **Update** (`update`) - Update a webinar

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Subject | `subject` | string |  | ✓ |  |  |
| Time Range | `times` | fixedCollection | {} | ✓ | e.g. Add Time Range |  |

<details>
<summary><strong>Time Range sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Times Properties | `timesProperties` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |
| Experience Type | `experienceType` | options | CLASSIC |  |
| Is On-Demand | `isOnDemand` | boolean | False |  |
| Is Password Protected | `isPasswordProtected` | boolean | False |  |
| Timezone Name or ID | `timezone` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Webinar Type | `type` | options | single_session | Webinar with one single meeting |

</details>

| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | Key of the webinar that the co-organizer is hosting. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Is External | `isExternal` | boolean | False | ✓ | Whether the co-organizer has no GoToWebinar account |  |
| Organizer Key | `organizerKey` | string |  | ✗ | The co-organizer's organizer key for the webinar |  |
| Given Name | `givenName` | string |  | ✗ | The co-organizer's given name |  |
| Email | `email` | string |  | ✗ | The co-organizer's email address | e.g. name@email.com | email |
| Name | `name` | string |  | ✓ | Name of the panelist to create |  |
| Email | `email` | string |  | ✓ | Email address of the panelist to create | e.g. name@email.com | email |
| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | Key of the webinar that the panelist will present at. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | Key of the webinar of the registrant to create. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| First Name | `firstName` | string |  | ✗ | First name of the registrant to create |  |
| Last Name | `lastName` | string |  | ✗ | Last name of the registrant to create |  |
| Email | `email` | string |  | ✗ | Email address of the registrant to create | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Full address of the registrant to create | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Full Address | `fullAddress` | fixedCollection | {} | Full address of the registrant to create |
| Industry | `industry` | string |  | The type of industry the registrant's organization belongs to |
| Job Title | `jobTitle` | string |  |  |
| MultiChoice Responses | `multiChoiceResponses` | fixedCollection | {} | Set the answers to all questions |
| Number of Employees | `numberOfEmployees` | string |  | The size in employees of the registrant's organization |
| Organization | `organization` | string |  |  |
| Telephone | `phone` | string |  |  |
| Purchasing Role | `purchasingRole` | string |  | Registrant's role in purchasing the product |
| Purchasing Time Frame | `purchasingTimeFrame` | string |  | Time frame within which the product will be purchased |
| Questions and Comments | `questionsAndComments` | string |  | Questions or comments made by the registrant during registration |
| Resend Confirmation | `resendConfirmation` | boolean | False |  |
| Simple Responses | `simpleResponses` | fixedCollection | {} | Set the answers to all questions |
| Source | `source` | string |  | The source that led to the registration |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Webinar Key | `webinarKey` | string |  | ✓ | Key of the webinar to delete |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Send Cancellation E-Mails | `sendCancellationEmails` | boolean | False |  |

</details>

| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | Key of the webinar to delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Co-Organizer Key | `coorganizerKey` | string |  | ✗ | Key of the co-organizer to delete |  |
| Is External | `isExternal` | boolean | False | ✓ | By default only internal co-organizers (with a GoToWebinar account) can be deleted. If you want to use this call for external co-organizers you have to set this parameter to 'true'. |  |
| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | Key of the webinar to delete the panelist from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Panelist Key | `panelistKey` | string |  | ✓ | Key of the panelist to delete |  |
| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | Key of the webinar of the registrant to delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Registrant Key | `registrantKey` | string |  | ✓ | Key of the registrant to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Webinar Key | `webinarKey` | string |  | ✓ | Key of the webinar to retrieve |  |
| Registrant Key | `registrantKey` | string |  | ✓ | Registrant key of the attendee at the webinar session |  |
| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | Key of the webinar of the registrant to retrieve. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Registrant Key | `registrantKey` | string |  | ✓ | Key of the registrant to retrieve |  |
| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | Key of the webinar to which the session belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Session Key | `sessionKey` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:100 |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Start of the datetime range for the webinar | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Time Range | `times` | fixedCollection | {} | Start of the datetime range for the webinar |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:100 |
| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | Key of the webinar to retrieve all co-organizers from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:100 |
| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | Key of the webinar to retrieve all panelists from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:100 |
| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | The key of the webinar to retrieve registrants from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:100 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:100 |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Start of the datetime range for the session | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Time Range | `times` | fixedCollection | {} | Start of the datetime range for the session |
| Webinar Key Name or ID | `webinarKey` | options | {} | Webinar by which to filter the sessions to retrieve. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Webinar Key | `webinarKey` | string |  | ✓ | Key of the webinar to update |  |
| Notify Participants | `notifyParticipants` | boolean | False | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✓ | Whether the webinar may be watched anytime | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |
| Experience Type | `experienceType` | options | CLASSIC |  |
| Is On-Demand | `isOnDemand` | boolean | False | Whether the webinar may be watched anytime |
| Is Password Protected | `isPasswordProtected` | boolean | False | Whether the webinar requires a password for attendees to join |
| Times | `times` | fixedCollection | {} |  |
| Subject | `subject` | string |  | Name or topic of the webinar |
| Timezone Name or ID | `timezone` | options |  | Timezone where the webinar is to take place. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Webinar Type | `type` | options | single_session | Webinar with one single meeting |

</details>


### Get Details parameters (`getDetails`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Registrant Key | `registrantKey` | string |  | ✓ | Registrant key of the attendee at the webinar session |  |
| Details | `details` | options |  | ✓ | The details to retrieve for the attendee |  |

**Details options:**

* **Polls** (`polls`) - Poll answers from the attendee in a webinar session
* **Questions** (`questions`) - Questions asked by the attendee in a webinar session
* **Survey Answers** (`surveyAnswers`) - Survey answers from the attendee in a webinar session

| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | Key of the webinar to which the session belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Session Key | `sessionKey` | string |  | ✓ |  |  |
| Details | `details` | options | performance | ✗ | Performance details for a webinar session |  |

**Details options:**

* **Performance** (`performance`) - Performance details for a webinar session
* **Polls** (`polls`) - Questions and answers for polls from a webinar session
* **Questions** (`questions`) - Questions and answers for a past webinar session
* **Surveys** (`surveys`) - Surveys for a past webinar session


### Reinvite parameters (`reinvite`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Webinar Key | `webinarKey` | string |  | ✓ | By default only internal co-organizers (with a GoToWebinar account) can be deleted. If you want to use this call for external co-organizers you have to set this parameter to 'true'. |  |
| Co-Organizer Key | `coorganizerKey` | string |  | ✗ | Key of the co-organizer to reinvite |  |
| Is External | `isExternal` | boolean | False | ✓ | Whether the co-organizer has no GoToWebinar account |  |
| Webinar Key Name or ID | `webinarKey` | options | [] | ✓ | Key of the webinar to reinvite the panelist to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Panelist Key | `panelistKey` | string |  | ✓ | Key of the panelist to reinvite |  |

---

## Load Options Methods

- `getWebinars`

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
node: goToWebinar
displayName: GoToWebinar
description: Consume the GoToWebinar API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: goToWebinarOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - webinar
          operation:
          - create
    typeInfo:
      type: string
      displayName: Subject
      name: subject
  - id: times
    name: Time Range
    type: fixedCollection
    default: {}
    required: true
    description: ''
    placeholder: Add Time Range
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - webinar
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Time Range
      name: times
      typeOptions:
        multipleValues: true
      subProperties:
      - name: timesProperties
        displayName: Times Properties
        values:
        - displayName: Start Time
          name: startTime
          type: dateTime
          default: ''
          required: true
        - displayName: End Time
          name: endTime
          type: dateTime
          default: ''
          required: true
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: []
    required: true
    description: Key of the webinar that the co-organizer is hosting. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - session
          operation:
          - get
          - getDetails
    typeInfo: &id004
      type: options
      displayName: Webinar Key Name or ID
      name: webinarKey
      typeOptions:
        loadOptionsMethod: getWebinars
      possibleValues: []
  - id: isExternal
    name: Is External
    type: boolean
    default: false
    required: true
    description: Whether the co-organizer has no GoToWebinar account
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - coorganizer
          operation:
          - reinvite
    typeInfo: &id006
      type: boolean
      displayName: Is External
      name: isExternal
  - id: organizerKey
    name: Organizer Key
    type: string
    default: ''
    required: false
    description: The co-organizer's organizer key for the webinar
    validation:
      displayOptions:
        show:
          resource:
          - coorganizer
          operation:
          - create
          isExternal:
          - false
    typeInfo:
      type: string
      displayName: Organizer Key
      name: organizerKey
  - id: givenName
    name: Given Name
    type: string
    default: ''
    required: false
    description: The co-organizer's given name
    validation:
      displayOptions:
        show:
          resource:
          - coorganizer
          operation:
          - create
          isExternal:
          - true
    typeInfo:
      type: string
      displayName: Given Name
      name: givenName
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: The co-organizer's email address
    placeholder: name@email.com
    validation: &id001
      format: email
      displayOptions:
        show:
          resource:
          - registrant
          operation:
          - create
    typeInfo: &id002
      type: string
      displayName: Email
      name: email
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the panelist to create
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - panelist
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email address of the panelist to create
    placeholder: name@email.com
    validation: *id001
    typeInfo: *id002
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: []
    required: true
    description: Key of the webinar that the panelist will present at. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: []
    required: true
    description: Key of the webinar of the registrant to create. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: firstName
    name: First Name
    type: string
    default: ''
    required: false
    description: First name of the registrant to create
    validation:
      displayOptions:
        show:
          resource:
          - registrant
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
    required: false
    description: Last name of the registrant to create
    validation:
      displayOptions:
        show:
          resource:
          - registrant
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
    required: false
    description: Email address of the registrant to create
    placeholder: name@email.com
    validation: *id001
    typeInfo: *id002
- id: delete
  name: Delete
  description: ''
  params:
  - id: webinarKey
    name: Webinar Key
    type: string
    default: ''
    required: true
    description: Key of the webinar to delete
    validation: *id003
    typeInfo: *id004
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: []
    required: true
    description: Key of the webinar to delete. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: coorganizerKey
    name: Co-Organizer Key
    type: string
    default: ''
    required: false
    description: Key of the co-organizer to delete
    validation: &id018
      displayOptions:
        show:
          resource:
          - coorganizer
          operation:
          - reinvite
    typeInfo: &id019
      type: string
      displayName: Co-Organizer Key
      name: coorganizerKey
  - id: isExternal
    name: Is External
    type: boolean
    default: false
    required: true
    description: By default only internal co-organizers (with a GoToWebinar account)
      can be deleted. If you want to use this call for external co-organizers you
      have to set this parameter to 'true'.
    validation: *id005
    typeInfo: *id006
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: []
    required: true
    description: Key of the webinar to delete the panelist from. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: panelistKey
    name: Panelist Key
    type: string
    default: ''
    required: true
    description: Key of the panelist to delete
    validation: &id020
      required: true
      displayOptions:
        show:
          resource:
          - panelist
          operation:
          - reinvite
    typeInfo: &id021
      type: string
      displayName: Panelist Key
      name: panelistKey
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: []
    required: true
    description: Key of the webinar of the registrant to delete. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: registrantKey
    name: Registrant Key
    type: string
    default: ''
    required: true
    description: Key of the registrant to delete
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - registrant
          operation:
          - get
    typeInfo: &id008
      type: string
      displayName: Registrant Key
      name: registrantKey
- id: get
  name: Get
  description: ''
  params:
  - id: webinarKey
    name: Webinar Key
    type: string
    default: ''
    required: true
    description: Key of the webinar to retrieve
    validation: *id003
    typeInfo: *id004
  - id: registrantKey
    name: Registrant Key
    type: string
    default: ''
    required: true
    description: Registrant key of the attendee at the webinar session
    validation: *id007
    typeInfo: *id008
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: []
    required: true
    description: Key of the webinar of the registrant to retrieve. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: registrantKey
    name: Registrant Key
    type: string
    default: ''
    required: true
    description: Key of the registrant to retrieve
    validation: *id007
    typeInfo: *id008
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: &id013 []
    required: true
    description: Key of the webinar to which the session belongs. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: sessionKey
    name: Session Key
    type: string
    default: ''
    required: true
    description: ''
    validation: &id014
      required: true
      displayOptions:
        show:
          resource:
          - session
          operation:
          - get
          - getDetails
    typeInfo: &id015
      type: string
      displayName: Session Key
      name: sessionKey
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
    validation: &id009
      displayOptions:
        show:
          resource:
          - session
          operation:
          - getAll
    typeInfo: &id010
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: &id011
      displayOptions:
        show:
          resource:
          - session
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id012
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
    validation: *id009
    typeInfo: *id010
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: []
    required: true
    description: Key of the webinar to retrieve all co-organizers from. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id009
    typeInfo: *id010
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: []
    required: true
    description: Key of the webinar to retrieve all panelists from. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id009
    typeInfo: *id010
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: []
    required: true
    description: The key of the webinar to retrieve registrants from. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id009
    typeInfo: *id010
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id009
    typeInfo: *id010
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: *id011
    typeInfo: *id012
- id: update
  name: Update
  description: ''
  params:
  - id: webinarKey
    name: Webinar Key
    type: string
    default: ''
    required: true
    description: Key of the webinar to update
    validation: *id003
    typeInfo: *id004
  - id: notifyParticipants
    name: Notify Participants
    type: boolean
    default: false
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - webinar
          operation:
          - update
    typeInfo:
      type: boolean
      displayName: Notify Participants
      name: notifyParticipants
- id: getDetails
  name: Get Details
  description: ''
  params:
  - id: registrantKey
    name: Registrant Key
    type: string
    default: ''
    required: true
    description: Registrant key of the attendee at the webinar session
    validation: *id007
    typeInfo: *id008
  - id: details
    name: Details
    type: options
    default: ''
    required: true
    description: The details to retrieve for the attendee
    validation: &id016
      displayOptions:
        show:
          resource:
          - session
          operation:
          - getDetails
    typeInfo: &id017
      type: options
      displayName: Details
      name: details
      possibleValues:
      - value: performance
        name: Performance
        description: Performance details for a webinar session
      - value: polls
        name: Polls
        description: Questions and answers for polls from a webinar session
      - value: questions
        name: Questions
        description: Questions and answers for a past webinar session
      - value: surveys
        name: Surveys
        description: Surveys for a past webinar session
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: *id013
    required: true
    description: Key of the webinar to which the session belongs. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: sessionKey
    name: Session Key
    type: string
    default: ''
    required: true
    description: ''
    validation: *id014
    typeInfo: *id015
  - id: details
    name: Details
    type: options
    default: performance
    required: false
    description: Performance details for a webinar session
    validation: *id016
    typeInfo: *id017
- id: reinvite
  name: Reinvite
  description: ''
  params:
  - id: webinarKey
    name: Webinar Key
    type: string
    default: ''
    required: true
    description: By default only internal co-organizers (with a GoToWebinar account)
      can be deleted. If you want to use this call for external co-organizers you
      have to set this parameter to 'true'.
    validation: *id003
    typeInfo: *id004
  - id: coorganizerKey
    name: Co-Organizer Key
    type: string
    default: ''
    required: false
    description: Key of the co-organizer to reinvite
    validation: *id018
    typeInfo: *id019
  - id: isExternal
    name: Is External
    type: boolean
    default: false
    required: true
    description: Whether the co-organizer has no GoToWebinar account
    validation: *id005
    typeInfo: *id006
  - id: webinarKey
    name: Webinar Key Name or ID
    type: options
    default: []
    required: true
    description: Key of the webinar to reinvite the panelist to. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: panelistKey
    name: Panelist Key
    type: string
    default: ''
    required: true
    description: Key of the panelist to reinvite
    validation: *id020
    typeInfo: *id021
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - user-agent
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: times
    text: Add Time Range
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: email
    text: name@email.com
  - field: email
    text: name@email.com
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
  "$id": "https://n8n.io/schemas/nodes/goToWebinar.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GoToWebinar Node",
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
        "update",
        "getDetails",
        "reinvite"
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
            "attendee",
            "coorganizer",
            "panelist",
            "registrant",
            "session",
            "webinar"
          ],
          "default": "attendee"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "get",
            "getAll",
            "getDetails"
          ],
          "default": "get"
        },
        "subject": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "times": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Time Range"
          ]
        },
        "additionalFields": {
          "description": "Start of the datetime range for the session",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "webinarKey": {
          "description": "Key of the webinar to which the session belongs. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 10
        },
        "notifyParticipants": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "updateFields": {
          "description": "Whether the webinar may be watched anytime",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "sessionKey": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "registrantKey": {
          "description": "Key of the registrant to retrieve",
          "type": "string",
          "default": ""
        },
        "details": {
          "description": "Performance details for a webinar session",
          "type": "string",
          "enum": [
            "performance",
            "polls",
            "questions",
            "surveys"
          ],
          "default": "performance"
        },
        "isExternal": {
          "description": "Whether the co-organizer has no GoToWebinar account",
          "type": "boolean",
          "default": false
        },
        "organizerKey": {
          "description": "The co-organizer's organizer key for the webinar",
          "type": "string",
          "default": ""
        },
        "givenName": {
          "description": "The co-organizer's given name",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "Email address of the registrant to create",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "coorganizerKey": {
          "description": "Key of the co-organizer to reinvite",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "Name of the panelist to create",
          "type": "string",
          "default": ""
        },
        "panelistKey": {
          "description": "Key of the panelist to reinvite",
          "type": "string",
          "default": ""
        },
        "firstName": {
          "description": "First name of the registrant to create",
          "type": "string",
          "default": ""
        },
        "lastName": {
          "description": "Last name of the registrant to create",
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
      "name": "goToWebinarOAuth2Api",
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
