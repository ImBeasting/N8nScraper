---
title: "Node: Action Network"
slug: "node-actionnetwork"
version: "1"
updated: "2026-01-08"
summary: "Consume the Action Network API"
node_type: "regular"
group: "['transform']"
---

# Node: Action Network

**Purpose.** Consume the Action Network API
**Subtitle.** ={{$parameter["resource"] + ": " + $parameter["operation"]}}


---

## Node Details

- **Icon:** `file:actionNetwork.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **actionNetworkApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `actionNetworkApi` | ✓ | - |

---

## Operations

### Tag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a tag |
| Get | `get` | Get a tag |
| Get Many | `getAll` | Get many tags |

### Attendance Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an attendance |
| Get | `get` | Get an attendance |
| Get Many | `getAll` | Get many attendances |

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an event |
| Get | `get` | Get an event |
| Get Many | `getAll` | Get many events |

### Person Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a person |
| Get | `get` | Get a person |
| Get Many | `getAll` | Get many people |
| Update | `update` | Update a person |

### Persontag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a person tag |
| Remove | `remove` | Remove a person tag |

### Petition Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a petition |
| Get | `get` | Get a petition |
| Get Many | `getAll` | Get many petitions |
| Update | `update` | Update a petition |

### Signature Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a signature |
| Get | `get` | Get a signature |
| Get Many | `getAll` | Get many signatures |
| Update | `update` | Update a signature |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | attendance | ✗ | Resource to operate on |  |

**Resource options:**

* **Attendance** (`attendance`)
* **Event** (`event`)
* **Person** (`person`)
* **Person Tag** (`personTag`)
* **Petition** (`petition`)
* **Signature** (`signature`)
* **Tag** (`tag`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create a tag
* **Get** (`get`) - Get a tag
* **Get Many** (`getAll`) - Get many tags

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Name of the tag to create |  |
| Person ID | `personId` | string |  | ✓ | ID of the person to create an attendance for |  |
| Event ID | `eventId` | string |  | ✓ | ID of the event to create an attendance for |  |
| Origin System | `originSystem` | string |  | ✓ | Source where the event originated |  |
| Title | `title` | string |  | ✓ | Title of the event to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Email Address | `email_addresses` | fixedCollection | {} | ✗ | Person’s email addresses | e.g. Add Email Address Field | email |

<details>
<summary><strong>Email Address sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email Addresses Fields | `email_addresses_fields` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Origin System | `originSystem` | string |  | ✓ | Source where the petition originated |  |
| Title | `title` | string |  | ✓ | Title of the petition to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Petition ID | `petitionId` | string |  | ✓ | ID of the petition to sign |  |
| Person ID | `personId` | string |  | ✓ | ID of the person whose signature to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Comments to leave when signing this petition | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Comments | `comments` | string |  | Comments to leave when signing this petition |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tag ID | `tagId` | string |  | ✓ | ID of the tag to retrieve |  |
| Event ID | `eventId` | string |  | ✓ | ID of the event whose attendance to retrieve |  |
| Attendance ID | `attendanceId` | string |  | ✓ | ID of the attendance to retrieve |  |
| Event ID | `eventId` | string |  | ✓ | ID of the event to retrieve |  |
| Person ID | `personId` | string |  | ✓ | ID of the person to retrieve |  |
| Petition ID | `petitionId` | string |  | ✓ | ID of the petition to retrieve |  |
| Petition ID | `petitionId` | string |  | ✓ | ID of the petition whose signature to retrieve |  |
| Signature ID | `signatureId` | string |  | ✓ | ID of the signature to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Event ID | `eventId` | string |  | ✓ | ID of the event to create an attendance for |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 25 | ✗ | Max number of results to return | min:1, max:25 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Petition ID | `petitionId` | string |  | ✓ | ID of the petition whose signatures to retrieve |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Person ID | `personId` | string |  | ✓ | ID of the person to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |
| Petition ID | `petitionId` | string |  | ✓ | ID of the petition to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |
| Petition ID | `petitionId` | string |  | ✓ | ID of the petition whose signature to update |  |
| Signature ID | `signatureId` | string |  | ✓ | ID of the signature to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Comments to leave when signing this petition | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Comments | `comments` | string |  | Comments to leave when signing this petition |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tag Name or ID | `tagId` | options | [] | ✓ | ID of the tag to add. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Person ID | `personId` | string |  | ✓ | ID of the person to add the tag to |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tag Name or ID | `tagId` | options | [] | ✓ | ID of the tag whose tagging to delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Tagging Name or ID | `taggingId` | options | [] | ✓ | ID of the tagging to remove. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["resource"] + ": " + $parameter["operation"]}}`

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
* Categories: Sales, Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: actionNetwork
displayName: Action Network
description: Consume the Action Network API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: actionNetworkApi
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the tag to create
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - tag
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: personId
    name: Person ID
    type: string
    default: ''
    required: true
    description: ID of the person to create an attendance for
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - signature
          operation:
          - create
    typeInfo: &id006
      type: string
      displayName: Person ID
      name: personId
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: ID of the event to create an attendance for
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - event
          operation:
          - get
    typeInfo: &id008
      type: string
      displayName: Event ID
      name: eventId
  - id: originSystem
    name: Origin System
    type: string
    default: ''
    required: true
    description: Source where the event originated
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - petition
          operation:
          - create
    typeInfo: &id002
      type: string
      displayName: Origin System
      name: originSystem
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the event to create
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - petition
          operation:
          - create
    typeInfo: &id004
      type: string
      displayName: Title
      name: title
  - id: email_addresses
    name: Email Address
    type: fixedCollection
    default: {}
    required: false
    description: Person’s email addresses
    placeholder: Add Email Address Field
    validation:
      format: email
      displayOptions:
        show:
          resource:
          - person
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Email Address
      name: email_addresses
      subProperties:
      - name: email_addresses_fields
        displayName: Email Addresses Fields
        values:
        - displayName: Address
          name: address
          type: string
          description: Person's email address
          default: ''
        - displayName: Primary
          name: primary
          type: hidden
          description: Whether this is the person's primary email address
          default: true
        - displayName: Status
          name: status
          type: options
          description: Subscription status of this email address
          value: bouncing
          default: subscribed
          options:
          - name: Bouncing
            value: bouncing
            displayName: Bouncing
          - name: Previous Bounce
            value: previous bounce
            displayName: Previous Bounce
          - name: Previous Spam Complaint
            value: previous spam complaint
            displayName: Previous Spam Complaint
          - name: Spam Complaint
            value: spam complaint
            displayName: Spam Complaint
          - name: Subscribed
            value: subscribed
            displayName: Subscribed
          - name: Unsubscribed
            value: unsubscribed
            displayName: Unsubscribed
  - id: originSystem
    name: Origin System
    type: string
    default: ''
    required: true
    description: Source where the petition originated
    validation: *id001
    typeInfo: *id002
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the petition to create
    validation: *id003
    typeInfo: *id004
  - id: petitionId
    name: Petition ID
    type: string
    default: ''
    required: true
    description: ID of the petition to sign
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - signature
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Petition ID
      name: petitionId
  - id: personId
    name: Person ID
    type: string
    default: ''
    required: true
    description: ID of the person whose signature to create
    validation: *id005
    typeInfo: *id006
- id: get
  name: Get
  description: ''
  params:
  - id: tagId
    name: Tag ID
    type: string
    default: ''
    required: true
    description: ID of the tag to retrieve
    validation: &id017
      required: true
      displayOptions:
        show:
          resource:
          - personTag
          operation:
          - remove
    typeInfo: &id018
      type: options
      displayName: Tag Name or ID
      name: tagId
      typeOptions:
        loadOptionsMethod: getTags
      possibleValues: []
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: ID of the event whose attendance to retrieve
    validation: *id007
    typeInfo: *id008
  - id: attendanceId
    name: Attendance ID
    type: string
    default: ''
    required: true
    description: ID of the attendance to retrieve
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - attendance
          operation:
          - get
    typeInfo:
      type: string
      displayName: Attendance ID
      name: attendanceId
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: ID of the event to retrieve
    validation: *id007
    typeInfo: *id008
  - id: personId
    name: Person ID
    type: string
    default: ''
    required: true
    description: ID of the person to retrieve
    validation: *id005
    typeInfo: *id006
  - id: petitionId
    name: Petition ID
    type: string
    default: ''
    required: true
    description: ID of the petition to retrieve
    validation: *id009
    typeInfo: *id010
  - id: petitionId
    name: Petition ID
    type: string
    default: ''
    required: true
    description: ID of the petition whose signature to retrieve
    validation: *id009
    typeInfo: *id010
  - id: signatureId
    name: Signature ID
    type: string
    default: ''
    required: true
    description: ID of the signature to retrieve
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - signature
          operation:
          - update
    typeInfo: &id016
      type: string
      displayName: Signature ID
      name: signatureId
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
    validation: &id011
      displayOptions:
        show:
          resource:
          - signature
          operation:
          - getAll
    typeInfo: &id012
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id013
      displayOptions:
        show:
          resource:
          - signature
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id014
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: ID of the event to create an attendance for
    validation: *id007
    typeInfo: *id008
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 25
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: petitionId
    name: Petition ID
    type: string
    default: ''
    required: true
    description: ID of the petition whose signatures to retrieve
    validation: *id009
    typeInfo: *id010
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
- id: update
  name: Update
  description: ''
  params:
  - id: personId
    name: Person ID
    type: string
    default: ''
    required: true
    description: ID of the person to update
    validation: *id005
    typeInfo: *id006
  - id: petitionId
    name: Petition ID
    type: string
    default: ''
    required: true
    description: ID of the petition to update
    validation: *id009
    typeInfo: *id010
  - id: petitionId
    name: Petition ID
    type: string
    default: ''
    required: true
    description: ID of the petition whose signature to update
    validation: *id009
    typeInfo: *id010
  - id: signatureId
    name: Signature ID
    type: string
    default: ''
    required: true
    description: ID of the signature to update
    validation: *id015
    typeInfo: *id016
- id: add
  name: Add
  description: ''
  params:
  - id: tagId
    name: Tag Name or ID
    type: options
    default: []
    required: true
    description: ID of the tag to add. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id017
    typeInfo: *id018
  - id: personId
    name: Person ID
    type: string
    default: ''
    required: true
    description: ID of the person to add the tag to
    validation: *id005
    typeInfo: *id006
- id: remove
  name: Remove
  description: ''
  params:
  - id: tagId
    name: Tag Name or ID
    type: options
    default: []
    required: true
    description: ID of the tag whose tagging to delete. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id017
    typeInfo: *id018
  - id: taggingId
    name: Tagging Name or ID
    type: options
    default: []
    required: true
    description: ID of the tagging to remove. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - personTag
          operation:
          - remove
    typeInfo:
      type: options
      displayName: Tagging Name or ID
      name: taggingId
      typeOptions:
        loadOptionsMethod: getTaggings
      possibleValues: []
common_expressions:
- '={{$parameter["resource"] + ": " + $parameter["operation"]}}'
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
  - field: email_addresses
    text: Add Email Address Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
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
  "$id": "https://n8n.io/schemas/nodes/actionNetwork.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Action Network Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "get",
        "getAll",
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
            "attendance",
            "event",
            "person",
            "personTag",
            "petition",
            "signature",
            "tag"
          ],
          "default": "attendance"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "create",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "name": {
          "description": "Name of the tag to create",
          "type": "string",
          "default": ""
        },
        "tagId": {
          "description": "ID of the tag whose tagging to delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
          "default": 50
        },
        "personId": {
          "description": "ID of the person whose signature to create",
          "type": "string",
          "default": ""
        },
        "eventId": {
          "description": "ID of the event to retrieve",
          "type": "string",
          "default": ""
        },
        "attendanceId": {
          "description": "ID of the attendance to retrieve",
          "type": "string",
          "default": ""
        },
        "originSystem": {
          "description": "Source where the petition originated",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "Title of the petition to create",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Comments to leave when signing this petition",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "email_addresses": {
          "description": "Person\u2019s email addresses",
          "type": "string",
          "default": {},
          "format": "email",
          "examples": [
            "Add Email Address Field"
          ]
        },
        "updateFields": {
          "description": "Comments to leave when signing this petition",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "taggingId": {
          "description": "ID of the tagging to remove. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "petitionId": {
          "description": "ID of the petition whose signature to update",
          "type": "string",
          "default": ""
        },
        "signatureId": {
          "description": "ID of the signature to update",
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
      "name": "actionNetworkApi",
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
