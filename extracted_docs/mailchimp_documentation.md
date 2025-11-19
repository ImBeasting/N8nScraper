---
title: "Node: Mailchimp"
slug: "node-mailchimp"
version: "1"
updated: "2025-11-13"
summary: "Consume Mailchimp API"
node_type: "regular"
group: "['output']"
---

# Node: Mailchimp

**Purpose.** Consume Mailchimp API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:mailchimp.svg', 'dark': 'file:mailchimp.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **mailchimpApi**: N/A
- **mailchimpOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `mailchimpApi` | ✓ | {'show': {'authentication': ['apiKey']}} |
| `mailchimpOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**HTTP Methods:** GET

---

## Operations

### Member Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new member on list |
| Delete | `delete` | Delete a member on list |
| Get | `get` | Get a member on list |
| Get Many | `getAll` | Get many members on a list |
| Update | `update` | Update a new member on list |

### Membertag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Add tags from a list member |
| Delete | `delete` | Remove tags from a list member |

### Listgroup Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many groups |

### Campaign Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a campaign |
| Get | `get` | Get a campaign |
| Get Many | `getAll` | Get many campaigns |
| Replicate | `replicate` | Replicate a campaign |
| Resend | `resend` | Creates a Resend to Non-Openers version of this campaign |
| Send | `send` | Send a campaign |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | member | ✓ | Resource to operate on |  |

**Resource options:**

* **Campaign** (`campaign`)
* **List Group** (`listGroup`)
* **Member** (`member`)
* **Member Tag** (`memberTag`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✓ | Create a new member on list |  |

**Operation options:**

* **Create** (`create`) - Create a new member on list
* **Delete** (`delete`) - Delete a member on list
* **Get** (`get`) - Get a member on list
* **Get Many** (`getAll`) - Get many members on a list
* **Update** (`update`) - Update a new member on list

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `list` | options |  | ✓ | List of lists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Email | `email` | string |  | ✓ | Email address for a subscriber | e.g. name@email.com | email |
| Status | `status` | options |  | ✓ | Subscriber's current status |  |

**Status options:**

* **Cleaned** (`cleaned`)
* **Pending** (`pending`)
* **Subscribed** (`subscribed`)
* **Transactional** (`transactional`)
* **Unsubscribed** (`unsubscribed`)

| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | Type of email this member asked to get | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email Type | `emailType` | options |  | Type of email this member asked to get |
| Language | `language` | string |  | If set/detected, the subscriber's language |
| Opt-in IP | `ipOptIn` | string |  | The IP address the subscriber used to confirm their opt-in status |
| Signup IP | `ipSignup` | string |  | IP address the subscriber signed up from |
| Signup Timestamp | `timestampSignup` | dateTime |  | The date and time the subscriber signed up for the list in ISO 8601 format |
| Tags | `tags` | string |  | The tags that are associated with a member separeted by , |
| Vip | `vip` | boolean | False | Vip status for subscribers |
| Opt-in Timestamp | `timestampOpt` | dateTime |  | The date and time the subscribe confirmed their opt-in status in ISO 8601 format |

</details>

| Location | `locationFieldsUi` | fixedCollection | {} | ✓ | Subscriber location information.n | e.g. Add Location |  |

<details>
<summary><strong>Location sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Location | `locationFieldsValues` |  |  |  |

</details>

| Merge Fields | `mergeFieldsUi` | fixedCollection | {} | ✓ | An individual merge var and value for a member | e.g. Add Merge Fields |  |

<details>
<summary><strong>Merge Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `mergeFieldsValues` |  |  |  |

</details>

| Merge Fields | `mergeFieldsJson` | json |  | ✗ |  |  |
| Location | `locationJson` | json |  | ✗ |  |  |
| Interest Groups | `groupsUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Interest Group |  |

<details>
<summary><strong>Interest Groups sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Group | `groupsValues` |  |  |  |

</details>

| Interest Groups | `groupJson` | json |  | ✗ |  |  |
| List Name or ID | `list` | options |  | ✓ | List of lists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Email | `email` | string |  | ✓ | Email address of the subscriber | e.g. name@email.com | email |
| Tags | `tags` | string | [] | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | Whether automations based on the tags in the request will not fire | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Is Syncing | `isSyncing` | boolean | False | Whether automations based on the tags in the request will not fire |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `list` | options |  | ✓ | List of lists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Email | `email` | string |  | ✓ | Member's email | e.g. name@email.com | email |
| List Name or ID | `list` | options |  | ✓ | List of lists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Email | `email` | string |  | ✓ | Email address of the subscriber | e.g. name@email.com | email |
| Tags | `tags` | string | [] | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | Whether automations based on the tags in the request will not fire | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Is Syncing | `isSyncing` | boolean | False | Whether automations based on the tags in the request will not fire |

</details>

| Campaign ID | `campaignId` | string |  | ✓ | List of Campaigns |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `list` | options |  | ✓ | List of lists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Email | `email` | string |  | ✓ | Member's email | e.g. name@email.com | email |
| Options | `options` | collection | {} | ✗ | A comma-separated list of fields to return | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | A comma-separated list of fields to return |
| Exclude Fields | `excludeFields` | string |  | A comma-separated list of fields to exclude |

</details>

| Campaign ID | `campaignId` | string |  | ✓ | List of Campaigns |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `list` | options |  | ✓ | List of lists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 500 | ✗ | Max number of results to return | min:1, max:1000 |
| Options | `options` | collection | {} | ✗ | Restrict results to subscribers whose information changed before the set timeframe | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Before Last Changed | `beforeLastChanged` | dateTime |  | Restrict results to subscribers whose information changed before the set timeframe |
| Before Timestamp Opt | `beforeTimestampOpt` | dateTime |  | Restrict results to subscribers who opted-in before the set timeframe |
| Fields | `fields` | string |  | A comma-separated list of fields to return. |
| Exclude Fields | `excludeFields` | string |  | A comma-separated list of fields to exclude. |
| Email Type | `emailType` | options |  | Type of email this member asked to get |
| Status | `status` | options |  | Subscriber's current status |
| Since Last Changed | `sinceLastChanged` | dateTime |  | Restrict results to subscribers whose information changed after the set timeframe |

</details>

| List Name or ID | `list` | options |  | ✓ | List of lists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Group Category Name or ID | `groupCategory` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 500 | ✗ | Max number of results to return | min:1, max:1000 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:1000 |
| Options | `options` | collection | {} | ✗ | Restrict the response to campaigns created before the set time | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Before Create Time | `beforeCreateTime` | dateTime |  | Restrict the response to campaigns created before the set time |
| Before Send Time | `beforeSendTime` | dateTime |  | Restrict the response to campaigns sent before the set time |
| Exclude Field Names or IDs | `excludeFields` | multiOptions | [] | A comma-separated list of fields to exclude. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Field Names or IDs | `fields` | multiOptions |  | A comma-separated list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| List Name or ID | `listId` | options |  | List of lists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Since Create Time | `sinceCreateTime` | dateTime |  | Restrict the response to campaigns created after the set time |
| Since Send Time | `sinceSendTime` | dateTime |  | Restrict the response to campaigns sent after the set time |
| Sort Direction | `sortDirection` | options |  | Determines the order direction for sorted results |
| Sort Field | `sortField` | options |  | Returns files sorted by the specified field |
| Status | `status` | options |  | The status of the campaign |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| List Name or ID | `list` | options |  | ✓ | List of lists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Email | `email` | string |  | ✓ | Email address of the subscriber | e.g. name@email.com | email |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Update Fields | `updateFields` | collection | {} | ✓ | Type of email this member asked to get | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email Type | `emailType` | options |  | Type of email this member asked to get |
| Interest Groups | `groupsUi` | fixedCollection | {} | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Language | `language` | string |  | If set/detected, the subscriber's language |
| Merge Fields | `mergeFieldsUi` | fixedCollection | {} | An individual merge var and value for a member |
| Opt-in IP | `ipOptIn` | string |  | The IP address the subscriber used to confirm their opt-in status |
| Signup IP | `ipSignup` | string |  | IP address the subscriber signed up from |
| Signup Timestamp | `timestampSignup` | dateTime |  | The date and time the subscriber signed up for the list in ISO 8601 format |
| Skip Merge Validation | `skipMergeValidation` | boolean | False | Whether member data will be accepted without merge field values, even if the merge field is usually required |
| Status | `status` | options |  | Subscriber's current status |
| Vip | `vip` | boolean | False | Vip status for subscribers |
| Location | `locationFieldsUi` | fixedCollection | {} | Subscriber location information.n |
| Opt-in Timestamp | `timestampOpt` | dateTime |  | The date and time the subscribe confirmed their opt-in status in ISO 8601 format |

</details>

| Merge Fields | `mergeFieldsJson` | json |  | ✗ |  |  |
| Location | `locationJson` | json |  | ✗ |  |  |
| Interest Groups | `groupJson` | json |  | ✗ |  |  |

### Replicate parameters (`replicate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign ID | `campaignId` | string |  | ✓ | List of Campaigns |  |

### Resend parameters (`resend`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign ID | `campaignId` | string |  | ✓ | List of Campaigns |  |

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Campaign ID | `campaignId` | string |  | ✓ | List of Campaigns |  |

---

## Load Options Methods

- `getLists`
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
* Categories: Marketing, Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: mailchimp
displayName: Mailchimp
description: Consume Mailchimp API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: mailchimpApi
  required: true
- name: mailchimpOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a new member on list
  params:
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: List of lists. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - listGroup
          operation:
          - getAll
    typeInfo: &id002
      type: options
      displayName: List Name or ID
      name: list
      typeOptions:
        loadOptionsMethod: getLists
      possibleValues: []
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email address for a subscriber
    placeholder: name@email.com
    validation: &id003
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - memberTag
          operation:
          - create
          - delete
    typeInfo: &id004
      type: string
      displayName: Email
      name: email
  - id: status
    name: Status
    type: options
    default: ''
    required: true
    description: Subscriber's current status
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - create
    typeInfo:
      type: options
      displayName: Status
      name: status
      possibleValues:
      - value: cleaned
        name: Cleaned
        description: ''
      - value: pending
        name: Pending
        description: ''
      - value: subscribed
        name: Subscribed
        description: ''
      - value: transactional
        name: Transactional
        description: ''
      - value: unsubscribed
        name: Unsubscribed
        description: ''
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id014
      displayOptions:
        show:
          resource:
          - member
          operation:
          - update
    typeInfo: &id015
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: locationFieldsUi
    name: Location
    type: fixedCollection
    default: {}
    required: true
    description: Subscriber location information.n
    placeholder: Add Location
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: fixedCollection
      displayName: Location
      name: locationFieldsUi
      subProperties:
      - name: locationFieldsValues
        displayName: Location
        values:
        - displayName: Latitude
          name: latitude
          type: string
          description: The location latitude
          default: ''
          required: true
        - displayName: Longitude
          name: longitude
          type: string
          description: The location longitude
          default: ''
          required: true
  - id: mergeFieldsUi
    name: Merge Fields
    type: fixedCollection
    default: {}
    required: true
    description: An individual merge var and value for a member
    placeholder: Add Merge Fields
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: fixedCollection
      displayName: Merge Fields
      name: mergeFieldsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: mergeFieldsValues
        displayName: Field
        values:
        - displayName: Field Name or ID
          name: name
          type: options
          description: Merge Field name. Choose from the list, or specify an ID using
            an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: ''
          required: true
          typeOptions:
            loadOptionsMethod: getMergeFields
        - displayName: Field Value
          name: value
          type: string
          description: Merge field value
          default: ''
          required: true
  - id: mergeFieldsJson
    name: Merge Fields
    type: json
    default: ''
    required: false
    description: ''
    validation: &id016
      displayOptions:
        show:
          resource:
          - member
          operation:
          - update
          jsonParameters:
          - true
    typeInfo: &id017
      type: json
      displayName: Merge Fields
      name: mergeFieldsJson
      typeOptions:
        alwaysOpenEditWindow: true
  - id: locationJson
    name: Location
    type: json
    default: ''
    required: false
    description: ''
    validation: &id018
      displayOptions:
        show:
          resource:
          - member
          operation:
          - update
          jsonParameters:
          - true
    typeInfo: &id019
      type: json
      displayName: Location
      name: locationJson
      typeOptions:
        alwaysOpenEditWindow: true
  - id: groupsUi
    name: Interest Groups
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Interest Group
    validation:
      displayOptions:
        show:
          resource:
          - member
          operation:
          - create
          jsonParameters:
          - false
    typeInfo:
      type: fixedCollection
      displayName: Interest Groups
      name: groupsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: groupsValues
        displayName: Group
        values:
        - displayName: Category Name or ID
          name: categoryId
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getGroupCategories
        - displayName: Category Field ID
          name: categoryFieldId
          type: string
          default: ''
        - displayName: Value
          name: value
          type: boolean
          default: false
  - id: groupJson
    name: Interest Groups
    type: json
    default: ''
    required: false
    description: ''
    validation: &id020
      displayOptions:
        show:
          resource:
          - member
          operation:
          - update
          jsonParameters:
          - true
    typeInfo: &id021
      type: json
      displayName: Interest Groups
      name: groupJson
      typeOptions:
        alwaysOpenEditWindow: true
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: List of lists. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email address of the subscriber
    placeholder: name@email.com
    validation: *id003
    typeInfo: *id004
  - id: tags
    name: Tags
    type: string
    default: &id005 []
    required: false
    description: ''
    validation: &id006
      displayOptions:
        show:
          resource:
          - memberTag
          operation:
          - create
          - delete
    typeInfo: &id007
      type: string
      displayName: Tags
      name: tags
      typeOptions:
        multipleValues: true
- id: delete
  name: Delete
  description: Delete a member on list
  params:
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: List of lists. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Member's email
    placeholder: name@email.com
    validation: *id003
    typeInfo: *id004
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: List of lists. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email address of the subscriber
    placeholder: name@email.com
    validation: *id003
    typeInfo: *id004
  - id: tags
    name: Tags
    type: string
    default: *id005
    required: false
    description: ''
    validation: *id006
    typeInfo: *id007
  - id: campaignId
    name: Campaign ID
    type: string
    default: ''
    required: true
    description: List of Campaigns
    validation: &id008
      required: true
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - send
          - get
          - delete
          - replicate
          - resend
    typeInfo: &id009
      type: string
      displayName: Campaign ID
      name: campaignId
- id: get
  name: Get
  description: Get a member on list
  params:
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: List of lists. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Member's email
    placeholder: name@email.com
    validation: *id003
    typeInfo: *id004
  - id: campaignId
    name: Campaign ID
    type: string
    default: ''
    required: true
    description: List of Campaigns
    validation: *id008
    typeInfo: *id009
- id: getAll
  name: Get Many
  description: Get many members on a list
  params:
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: List of lists. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id010
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - getAll
    typeInfo: &id011
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 500
    required: false
    description: Max number of results to return
    validation: &id012
      displayOptions:
        show:
          resource:
          - campaign
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id013
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 1000
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: List of lists. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: groupCategory
    name: Group Category Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - listGroup
          operation:
          - getAll
    typeInfo:
      type: options
      displayName: Group Category Name or ID
      name: groupCategory
      typeOptions:
        loadOptionsMethod: getGroupCategories
      possibleValues: []
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id010
    typeInfo: *id011
  - id: limit
    name: Limit
    type: number
    default: 500
    required: false
    description: Max number of results to return
    validation: *id012
    typeInfo: *id013
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id010
    typeInfo: *id011
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation: *id012
    typeInfo: *id013
- id: update
  name: Update
  description: Update a new member on list
  params:
  - id: list
    name: List Name or ID
    type: options
    default: ''
    required: true
    description: List of lists. Choose from the list, or specify an ID using an <a
      href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email address of the subscriber
    placeholder: name@email.com
    validation: *id003
    typeInfo: *id004
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id014
    typeInfo: *id015
  - id: mergeFieldsJson
    name: Merge Fields
    type: json
    default: ''
    required: false
    description: ''
    validation: *id016
    typeInfo: *id017
  - id: locationJson
    name: Location
    type: json
    default: ''
    required: false
    description: ''
    validation: *id018
    typeInfo: *id019
  - id: groupJson
    name: Interest Groups
    type: json
    default: ''
    required: false
    description: ''
    validation: *id020
    typeInfo: *id021
- id: replicate
  name: Replicate
  description: Replicate a campaign
  params:
  - id: campaignId
    name: Campaign ID
    type: string
    default: ''
    required: true
    description: List of Campaigns
    validation: *id008
    typeInfo: *id009
- id: resend
  name: Resend
  description: Creates a Resend to Non-Openers version of this campaign
  params:
  - id: campaignId
    name: Campaign ID
    type: string
    default: ''
    required: true
    description: List of Campaigns
    validation: *id008
    typeInfo: *id009
- id: send
  name: Send
  description: Send a campaign
  params:
  - id: campaignId
    name: Campaign ID
    type: string
    default: ''
    required: true
    description: List of Campaigns
    validation: *id008
    typeInfo: *id009
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - GET
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: email
    text: name@email.com
  - field: options
    text: Add option
  - field: locationFieldsUi
    text: Add Location
  - field: mergeFieldsUi
    text: Add Merge Fields
  - field: groupsUi
    text: Add Interest Group
  - field: email
    text: name@email.com
  - field: email
    text: name@email.com
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: email
    text: name@email.com
  - field: updateFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: options
    text: Add option
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/mailchimp.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Mailchimp Node",
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
        "replicate",
        "resend",
        "send"
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
            "campaign",
            "listGroup",
            "member",
            "memberTag"
          ],
          "default": "member"
        },
        "operation": {
          "description": "Delete a campaign",
          "type": "string",
          "enum": [
            "delete",
            "get",
            "getAll",
            "replicate",
            "resend",
            "send"
          ],
          "default": "getAll"
        },
        "list": {
          "description": "List of lists. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
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
        "status": {
          "description": "Subscriber's current status",
          "type": "string",
          "enum": [
            "cleaned",
            "pending",
            "subscribed",
            "transactional",
            "unsubscribed"
          ],
          "default": ""
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "options": {
          "description": "Restrict the response to campaigns created before the set time",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "locationFieldsUi": {
          "description": "Subscriber location information.n",
          "type": "string",
          "default": {},
          "examples": [
            "Add Location"
          ]
        },
        "mergeFieldsUi": {
          "description": "An individual merge var and value for a member",
          "type": "string",
          "default": {},
          "examples": [
            "Add Merge Fields"
          ]
        },
        "mergeFieldsJson": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "locationJson": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "groupsUi": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Interest Group"
          ]
        },
        "groupJson": {
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
          "default": 10
        },
        "updateFields": {
          "description": "Type of email this member asked to get",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "tags": {
          "description": "",
          "type": "string",
          "default": []
        },
        "groupCategory": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "campaignId": {
          "description": "List of Campaigns",
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
      "name": "mailchimpApi",
      "required": true
    },
    {
      "name": "mailchimpOAuth2Api",
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
