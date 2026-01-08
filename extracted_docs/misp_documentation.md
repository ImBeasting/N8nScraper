---
title: "Node: MISP"
slug: "node-misp"
version: "1"
updated: "2026-01-08"
summary: "Consume the MISP API"
node_type: "regular"
group: "['transform']"
---

# Node: MISP

**Purpose.** Consume the MISP API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:misp.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **mispApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `mispApi` | ✓ | - |

---

## Operations

### Warninglist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a warninglist |
| Get Many | `getAll` | Get many warninglists |

### Attribute Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an attribute |
| Delete | `delete` | Delete an attribute |
| Get | `get` | Get an attribute |
| Get Many | `getAll` | Get many attributes |
| Search | `search` | Get a filtered list of attributes |
| Update | `update` | Update an attribute |

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an event |
| Delete | `delete` | Delete an event |
| Get | `get` | Get an event |
| Get Many | `getAll` | Get many events |
| Publish | `publish` | Publish an event |
| Search | `search` | Get a filtered list of events |
| Unpublish | `unpublish` | Unpublish an event |
| Update | `update` | Update an event |

### Eventtag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a tag to an event |
| Remove | `remove` | Remove a tag from an event |

### Feed Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a feed |
| Disable | `disable` | Disable a feed |
| Enable | `enable` | Enable a feed |
| Get | `get` | Get a feed |
| Get Many | `getAll` | Get many feeds |
| Update | `update` | Update a feed |

### Galaxy Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a galaxy |
| Get | `get` | Get a galaxy |
| Get Many | `getAll` | Get many galaxies |

### Noticelist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a noticelist |
| Get Many | `getAll` | Get many noticelists |

### Object Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Search | `search` | Get a filtered list of objects |

### Organisation Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an organization |
| Delete | `delete` | Delete an organization |
| Get | `get` | Get an organization |
| Get Many | `getAll` | Get many organizations |
| Update | `update` | Update an organization |

### Tag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a tag |
| Delete | `delete` | Delete a tag |
| Get Many | `getAll` | Get many tags |
| Update | `update` | Update a tag |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a user |
| Delete | `delete` | Delete a user |
| Get | `get` | Get a user |
| Get Many | `getAll` | Get many users |
| Update | `update` | Update a user |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | attribute | ✗ | Resource to operate on |  |

**Resource options:**

* **Attribute** (`attribute`)
* **Event** (`event`)
* **Event Tag** (`eventTag`)
* **Feed** (`feed`)
* **Galaxy** (`galaxy`)
* **Noticelist** (`noticelist`)
* **Object** (`object`)
* **Organisation** (`organisation`)
* **Tag** (`tag`)
* **User** (`user`)
* **Warninglist** (`warninglist`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Get** (`get`) - Get a warninglist
* **Get Many** (`getAll`) - Get many warninglists

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Warninglist ID | `warninglistId` | string |  | ✓ | Numeric ID of the warninglist |  |
| Attribute ID | `attributeId` | string |  | ✓ | UUID or numeric ID of the attribute |  |
| Event ID | `eventId` | string |  | ✓ | UUID or numeric ID of the event |  |
| Feed ID | `feedId` | string |  | ✓ | UUID or numeric ID of the feed |  |
| Galaxy ID | `galaxyId` | string |  | ✓ | UUID or numeric ID of the galaxy |  |
| Noticelist ID | `noticelistId` | string |  | ✓ | Numeric ID of the noticelist |  |
| Organisation ID | `organisationId` | string |  | ✓ | UUID or numeric ID of the organisation |  |
| User ID | `userId` | string |  | ✓ | Numeric ID of the user |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event UUID | `eventId` | string |  | ✓ | UUID of the event to attach the attribute to |  |
| Type | `type` | options | text | ✓ |  |  |

**Type options:**

* **Text** (`text`)
* **URL** (`url`)
* **Comment** (`comment`)

| Value | `value` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Who will be able to see this event once published | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Distribution | `distribution` | options | 0 | Who will be able to see this event once published |
| Sharing Group Name or ID | `sharing_group_id` | options |  | Use only for when <code>Sharing Group</code> is selected in <code>Distribution</code>. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Organization Name or ID | `org_id` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Information | `information` | string |  | ✓ | Information on the event - max 65535 characters |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Analysis maturity level of the event | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Analysis | `analysis` | options | 0 | Analysis maturity level of the event |
| Distribution | `distribution` | options | 0 | Who will be able to see this event once published |
| Sharing Group Name or ID | `sharing_group_id` | options |  | Use only for when <code>Sharing Group</code> is selected in <code>Distribution</code>. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Threat Level ID | `threat_level_id` | options | 1 |  |

</details>

| Name | `name` | string |  | ✓ |  |  |
| Provider | `provider` | string |  | ✓ |  |  |
| URL | `url` | string |  | ✓ | e.g. https://example.com | url |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Who will be able to see this event once published | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Distribution | `distribution` | options | 0 | Who will be able to see this event once published |
| Rules | `json` | string |  | Filter rules for the feed |

</details>

| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Created by Email | `created_by_email` | string |  |  |
| Description | `description` | string |  |  |
| Nationality | `nationality` | string |  |  |
| Sector | `sector` | string |  |  |
| Type | `type` | string |  |  |
| User Count | `usercount` | number | 0 |  |

</details>

| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Hex color code for the tag | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Color | `colour` | color |  | Hex color code for the tag |

</details>

| Email | `email` | string |  | ✓ | e.g. name@email.com | email |
| Role ID | `role_id` | string |  | ✓ | Role IDs are available in the MISP dashboard at /roles/index |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| GPG Key | `gpgkey` | string |  |  |
| Inviter Email or ID | `invited_by` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Organization Name or ID | `org_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Attribute ID | `attributeId` | string |  | ✓ | UUID or numeric ID of the attribute |  |
| Event ID | `eventId` | string |  | ✓ | UUID or numeric ID of the event |  |
| Galaxy ID | `galaxyId` | string |  | ✓ | UUID or numeric ID of the galaxy |  |
| Organisation ID | `organisationId` | string |  | ✓ | UUID or numeric ID of the organisation |  |
| Tag ID | `tagId` | string |  | ✓ | Numeric ID of the attribute |  |
| User ID | `userId` | string |  | ✓ | Numeric ID of the user |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Attribute ID | `attributeId` | string |  | ✓ | ID of the attribute to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Who will be able to see this event once published | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Distribution | `distribution` | options | 0 | Who will be able to see this event once published |
| Sharing Group Name or ID | `sharing_group_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Use only for when <code>Sharing Group</code> is selected in <code>Distribution</code>. |

</details>

| Event ID | `eventId` | string |  | ✓ | UUID or numeric ID of the event |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Analysis maturity level of the event | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Analysis | `analysis` | options | 0 | Analysis maturity level of the event |
| Distribution | `distribution` | options | 0 | Who will be able to see this event once published |
| Information | `information` | string |  | Information on the event - max 65535 characters |
| Sharing Group Name or ID | `sharing_group_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Use only for when <code>Sharing Group</code> is selected in <code>Distribution</code>. |
| Threat Level ID | `threat_level_id` | options | 1 |  |

</details>

| Feed ID | `feedId` | string |  | ✓ | ID of the feed to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Who will be able to see this event once published | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Distribution | `distribution` | options | 0 | Who will be able to see this event once published |
| Name | `name` | string |  |  |
| Provider | `provider` | string |  |  |
| Rules | `rules` | json |  | Filter rules for the feed |
| URL | `url` | string |  |  |

</details>

| Organisation ID | `organisationId` | string |  | ✓ | ID of the organisation to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |
| Name | `name` | string |  |  |
| Nationality | `nationality` | string |  |  |
| Sector | `sector` | string |  |  |
| Type | `type` | string |  |  |

</details>

| Tag ID | `tagId` | string |  | ✓ | ID of the tag to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Hex color code for the tag | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Color | `colour` | color |  | Hex color code for the tag |
| Name | `name` | string |  |  |

</details>

| User ID | `userId` | string |  | ✓ | ID of the user to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  |  |
| GPG Key | `gpgkey` | string |  |  |
| Inviter Name or ID | `invited_by` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Organization Name or ID | `org_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>


### Publish parameters (`publish`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event ID | `eventId` | string |  | ✓ | UUID or numeric ID of the event |  |

### Unpublish parameters (`unpublish`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event ID | `eventId` | string |  | ✓ | UUID or numeric ID of the event |  |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event ID | `eventId` | string |  | ✓ | UUID or numeric ID of the event |  |
| Tag Name or ID | `tagId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event ID | `eventId` | string |  | ✓ | UUID or numeric ID of the event |  |
| Tag Name or ID | `tagId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Disable parameters (`disable`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Feed ID | `feedId` | string |  | ✓ | UUID or numeric ID of the feed |  |

### Enable parameters (`enable`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Feed ID | `feedId` | string |  | ✓ | UUID or numeric ID of the feed |  |

---

## Load Options Methods

- `getOrgs`
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
node: misp
displayName: MISP
description: Consume the MISP API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: mispApi
  required: true
operations:
- id: get
  name: Get
  description: ''
  params:
  - id: warninglistId
    name: Warninglist ID
    type: string
    default: ''
    required: true
    description: Numeric ID of the warninglist
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - warninglist
          operation:
          - get
    typeInfo:
      type: string
      displayName: Warninglist ID
      name: warninglistId
  - id: attributeId
    name: Attribute ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the attribute
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - attribute
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Attribute ID
      name: attributeId
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the event
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - eventTag
          operation:
          - remove
    typeInfo: &id006
      type: string
      displayName: Event ID
      name: eventId
  - id: feedId
    name: Feed ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the feed
    validation: &id017
      required: true
      displayOptions:
        show:
          resource:
          - feed
          operation:
          - update
    typeInfo: &id018
      type: string
      displayName: Feed ID
      name: feedId
  - id: galaxyId
    name: Galaxy ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the galaxy
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - galaxy
          operation:
          - get
    typeInfo: &id012
      type: string
      displayName: Galaxy ID
      name: galaxyId
  - id: noticelistId
    name: Noticelist ID
    type: string
    default: ''
    required: true
    description: Numeric ID of the noticelist
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - noticelist
          operation:
          - get
    typeInfo:
      type: string
      displayName: Noticelist ID
      name: noticelistId
  - id: organisationId
    name: Organisation ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the organisation
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - organisation
          operation:
          - update
    typeInfo: &id014
      type: string
      displayName: Organisation ID
      name: organisationId
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: Numeric ID of the user
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - update
    typeInfo: &id016
      type: string
      displayName: User ID
      name: userId
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
    validation: &id001
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
    typeInfo: &id002
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id003
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id004
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
- id: create
  name: Create
  description: ''
  params:
  - id: eventId
    name: Event UUID
    type: string
    default: ''
    required: true
    description: UUID of the event to attach the attribute to
    validation: *id005
    typeInfo: *id006
  - id: type
    name: Type
    type: options
    default: text
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - attribute
          operation:
          - create
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: text
        name: Text
        description: ''
      - value: url
        name: URL
        description: ''
      - value: comment
        name: Comment
        description: ''
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - attribute
          operation:
          - create
    typeInfo:
      type: string
      displayName: Value
      name: value
  - id: org_id
    name: Organization Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - event
          operation:
          - create
    typeInfo:
      type: options
      displayName: Organization Name or ID
      name: org_id
      typeOptions:
        loadOptionsMethod: getOrgs
      possibleValues: []
  - id: information
    name: Information
    type: string
    default: ''
    required: true
    description: Information on the event - max 65535 characters
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - event
          operation:
          - create
    typeInfo:
      type: string
      displayName: Information
      name: information
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - tag
          operation:
          - create
    typeInfo: &id008
      type: string
      displayName: Name
      name: name
  - id: provider
    name: Provider
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - feed
          operation:
          - create
    typeInfo:
      type: string
      displayName: Provider
      name: provider
  - id: url
    name: URL
    type: string
    default: ''
    required: true
    description: ''
    placeholder: https://example.com
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - feed
          operation:
          - create
    typeInfo:
      type: string
      displayName: URL
      name: url
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: ''
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: role_id
    name: Role ID
    type: string
    default: ''
    required: true
    description: Role IDs are available in the MISP dashboard at /roles/index
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Role ID
      name: role_id
- id: delete
  name: Delete
  description: ''
  params:
  - id: attributeId
    name: Attribute ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the attribute
    validation: *id009
    typeInfo: *id010
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the event
    validation: *id005
    typeInfo: *id006
  - id: galaxyId
    name: Galaxy ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the galaxy
    validation: *id011
    typeInfo: *id012
  - id: organisationId
    name: Organisation ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the organisation
    validation: *id013
    typeInfo: *id014
  - id: tagId
    name: Tag ID
    type: string
    default: ''
    required: true
    description: Numeric ID of the attribute
    validation: &id019
      required: true
      displayOptions:
        show:
          resource:
          - tag
          operation:
          - update
    typeInfo: &id020
      type: string
      displayName: Tag ID
      name: tagId
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: Numeric ID of the user
    validation: *id015
    typeInfo: *id016
- id: search
  name: Search
  description: ''
- id: update
  name: Update
  description: ''
  params:
  - id: attributeId
    name: Attribute ID
    type: string
    default: ''
    required: true
    description: ID of the attribute to update
    validation: *id009
    typeInfo: *id010
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the event
    validation: *id005
    typeInfo: *id006
  - id: feedId
    name: Feed ID
    type: string
    default: ''
    required: true
    description: ID of the feed to update
    validation: *id017
    typeInfo: *id018
  - id: organisationId
    name: Organisation ID
    type: string
    default: ''
    required: true
    description: ID of the organisation to update
    validation: *id013
    typeInfo: *id014
  - id: tagId
    name: Tag ID
    type: string
    default: ''
    required: true
    description: ID of the tag to update
    validation: *id019
    typeInfo: *id020
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: ID of the user to update
    validation: *id015
    typeInfo: *id016
- id: publish
  name: Publish
  description: ''
  params:
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the event
    validation: *id005
    typeInfo: *id006
- id: unpublish
  name: Unpublish
  description: ''
  params:
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the event
    validation: *id005
    typeInfo: *id006
- id: add
  name: Add
  description: ''
  params:
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the event
    validation: *id005
    typeInfo: *id006
  - id: tagId
    name: Tag Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id019
    typeInfo: *id020
- id: remove
  name: Remove
  description: ''
  params:
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the event
    validation: *id005
    typeInfo: *id006
  - id: tagId
    name: Tag Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id019
    typeInfo: *id020
- id: disable
  name: Disable
  description: ''
  params:
  - id: feedId
    name: Feed ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the feed
    validation: *id017
    typeInfo: *id018
- id: enable
  name: Enable
  description: ''
  params:
  - id: feedId
    name: Feed ID
    type: string
    default: ''
    required: true
    description: UUID or numeric ID of the feed
    validation: *id017
    typeInfo: *id018
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
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: url
    text: https://example.com
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
  - field: email
    text: name@email.com
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
  "$id": "https://n8n.io/schemas/nodes/misp.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MISP Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll",
        "create",
        "delete",
        "search",
        "update",
        "publish",
        "unpublish",
        "add",
        "remove",
        "disable",
        "enable"
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
            "attribute",
            "event",
            "eventTag",
            "feed",
            "galaxy",
            "noticelist",
            "object",
            "organisation",
            "tag",
            "user",
            "warninglist"
          ],
          "default": "attribute"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "warninglistId": {
          "description": "Numeric ID of the warninglist",
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
        "eventId": {
          "description": "UUID or numeric ID of the event",
          "type": "string",
          "default": ""
        },
        "type": {
          "description": "",
          "type": "string",
          "enum": [
            "text",
            "url",
            "comment"
          ],
          "default": "text"
        },
        "value": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "attributeId": {
          "description": "ID of the attribute to update",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "org_id": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "information": {
          "description": "Information on the event - max 65535 characters",
          "type": "string",
          "default": ""
        },
        "tagId": {
          "description": "ID of the tag to update",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "provider": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "url": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "url",
          "examples": [
            "https://example.com"
          ]
        },
        "feedId": {
          "description": "ID of the feed to update",
          "type": "string",
          "default": ""
        },
        "galaxyId": {
          "description": "UUID or numeric ID of the galaxy",
          "type": "string",
          "default": ""
        },
        "noticelistId": {
          "description": "Numeric ID of the noticelist",
          "type": "string",
          "default": ""
        },
        "organisationId": {
          "description": "ID of the organisation to update",
          "type": "string",
          "default": ""
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
        "role_id": {
          "description": "Role IDs are available in the MISP dashboard at /roles/index",
          "type": "string",
          "default": ""
        },
        "userId": {
          "description": "ID of the user to update",
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
      "name": "mispApi",
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
