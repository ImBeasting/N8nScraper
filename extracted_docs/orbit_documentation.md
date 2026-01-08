---
title: "Node: Orbit"
slug: "node-orbit"
version: "1"
updated: "2026-01-08"
summary: "Consume Orbit API"
node_type: "regular"
group: "['output']"
---

# Node: Orbit

**Purpose.** Consume Orbit API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:orbit.svg', 'dark': 'file:orbit.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **orbitApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **deprecated**: Orbit has been shutdown and will no longer function from July 11th, You can read more <a target="_blank" href="https://orbit.love/blog/orbit-is-joining-postman">here</a>.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `orbitApi` | ✓ | - |

---

## Operations

### Activity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an activity for a member |
| Get Many | `getAll` | Get many activities |

### Member Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create or Update | `upsert` | Create a new member, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a member |
| Get | `get` | Get a member |
| Get Many | `getAll` | Get many members in a workspace |
| Lookup | `lookup` | Lookup a member by identity |
| Update | `update` | Update a member |

### Note Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a note |
| Get Many | `getAll` | Get many notes for a member |
| Update | `update` | Update a note |

### Post Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a post |
| Get Many | `getAll` | Get many posts |
| Delete | `delete` | Delete a post |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | member | ✗ | Resource to operate on |  |

**Resource options:**

* **Activity** (`activity`)
* **Member** (`member`)
* **Note** (`note`)
* **Post** (`post`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create an activity for a member |  |

**Operation options:**

* **Create** (`create`) - Create an activity for a member
* **Get Many** (`getAll`) - Get many activities

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Member ID | `memberId` | string |  | ✓ |  |  |
| Title | `title` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | A user-defined way to group activities of the same nature. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Activity Type Name or ID | `activityType` | options | Deprecated | A user-defined way to group activities of the same nature. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | A description of the activity; displayed in the timeline |
| Key | `key` | string |  | Supply a key that must be unique or leave blank to have one generated |
| Link | `link` | string |  | A URL for the activity; displayed in the timeline |
| Link Text | `linkText` | string |  | The text for the timeline link |
| Occurred At | `occurredAt` | dateTime |  | The date and time the activity occurred; defaults to now |

</details>

| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Member ID | `memberId` | string |  | ✓ |  |  |
| Note | `note` | string |  | ✓ |  |  |
| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Member ID | `memberId` | string |  | ✓ |  |  |
| URL | `url` | string |  | ✓ | Supply any URL and Orbit will do its best job to parse out a title, description, and image | url |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Occurred At | `publishedAt` | dateTime |  |  |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Filters | `filters` | collection | {} | ✗ | When set the post will be filtered by the member ID | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Member ID | `memberId` | string |  | When set the post will be filtered by the member ID |

</details>

| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Resolve Identities | `resolveIdentities` | boolean | False | ✗ | By default, the response just includes the reference of the identity. When set to true the identities will be resolved automatically. |  |
| Options | `options` | collection | {} | ✗ | Name of the field the response will be sorted by | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort By | `sort` | string |  | Name of the field the response will be sorted by |
| Sort Direction | `direction` | options |  |  |

</details>

| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Member ID | `memberId` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Resolve Member | `resolveMember` | boolean | False | ✗ |  |  |
| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Filters | `filters` | collection | {} | ✗ | When set the post will be filtered by the member ID | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Member ID | `memberId` | string |  | When set the post will be filtered by the member ID |

</details>


### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Identity | `identityUi` | fixedCollection | {} | ✓ | The identity is used to find the member. If no member exists, a new member will be created and linked to the provided identity. | e.g. Add Identity |  |

<details>
<summary><strong>Identity sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Identity | `identityValue` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Adds tags to member; comma-separated string or array | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Bio | `bio` | string |  |  |
| Birthday | `birthday` | dateTime |  |  |
| Company | `company` | string |  |  |
| Location | `location` | string |  |  |
| Name | `name` | string |  |  |
| Pronouns | `pronouns` | string |  |  |
| Shipping Address | `shippingAddress` | string |  |  |
| Slug | `slug` | string |  |  |
| Tags to Add | `tagsToAdd` | string |  | Adds tags to member; comma-separated string or array |
| Tag List | `tagList` | string |  | Replaces all tags for the member; comma-separated string or array |
| T-Shirt | `tShirt` | string |  |  |
| Teammate | `teammate` | boolean | False |  |
| URL | `url` | string |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Member ID | `memberId` | string |  | ✓ |  |  |
| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Member ID | `memberId` | string |  | ✓ |  |  |
| Post ID | `postId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Member ID | `memberId` | string |  | ✓ |  |  |
| Resolve Identities | `resolveIdentities` | boolean | False | ✗ | By default, the response just includes the reference of the identity. When set to true the identities will be resolved automatically. |  |

### Lookup parameters (`lookup`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Source | `source` | options |  | ✓ | Set to github, twitter, email, discourse or the source of any identities you've manually created |  |

**Source options:**

* **Discourse** (`discourse`)
* **Email** (`email`)
* **GitHub** (`github`)
* **Twitter** (`twitter`)

| Search By | `searchBy` | options |  | ✓ |  |  |

**Search By options:**

* **Username** (`username`)
* **ID** (`id`)

| ID | `id` | string |  | ✓ | The username at the source |  |
| Username | `username` | string |  | ✓ | The username at the source |  |
| Email | `email` | string |  | ✓ | The email address | e.g. name@email.com | email |
| Host | `host` | string |  | ✓ |  |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Member ID | `memberId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Adds tags to member; comma-separated string or array | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Bio | `bio` | string |  |  |
| Birthday | `birthday` | dateTime |  |  |
| Company | `company` | string |  |  |
| Location | `location` | string |  |  |
| Name | `name` | string |  |  |
| Pronouns | `pronouns` | string |  |  |
| Shipping Address | `shippingAddress` | string |  |  |
| Slug | `slug` | string |  |  |
| Tags to Add | `tagsToAdd` | string |  | Adds tags to member; comma-separated string or array |
| Tag List | `tagList` | string |  | Replaces all tags for the member; comma-separated string or array |
| T-Shirt | `tShirt` | string |  |  |
| Teammate | `teammate` | boolean | False |  |
| URL | `url` | string |  |  |

</details>

| Workspace Name or ID | `workspaceId` | options | Deprecated | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Member ID | `memberId` | string |  | ✓ |  |  |
| Note ID | `noteId` | string |  | ✓ |  |  |
| Note | `note` | string |  | ✓ |  |  |

---

## Load Options Methods

- `getWorkspaces`
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
* Categories: Analytics

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: orbit
displayName: Orbit
description: Consume Orbit API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: orbitApi
  required: true
operations:
- id: create
  name: Create
  description: Create an activity for a member
  params:
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - post
          operation:
          - delete
    typeInfo: &id002
      type: options
      displayName: Workspace Name or ID
      name: workspaceId
      typeOptions:
        loadOptionsMethod: getWorkspaces
      possibleValues: []
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - post
          operation:
          - delete
    typeInfo: &id004
      type: string
      displayName: Member ID
      name: memberId
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
          - activity
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: note
    name: Note
    type: string
    default: ''
    required: true
    description: ''
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - note
          operation:
          - update
    typeInfo: &id012
      type: string
      displayName: Note
      name: note
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: url
    name: URL
    type: string
    default: ''
    required: true
    description: Supply any URL and Orbit will do its best job to parse out a title,
      description, and image
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - post
          operation:
          - create
    typeInfo:
      type: string
      displayName: URL
      name: url
- id: getAll
  name: Get Many
  description: Get many activities
  params:
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id005
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - post
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
          operation:
          - getAll
          resource:
          - post
          returnAll:
          - false
    typeInfo: &id008
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
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
  - id: resolveIdentities
    name: Resolve Identities
    type: boolean
    default: false
    required: false
    description: By default, the response just includes the reference of the identity.
      When set to true the identities will be resolved automatically.
    validation: &id009
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - member
    typeInfo: &id010
      type: boolean
      displayName: Resolve Identities
      name: resolveIdentities
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: memberId
    name: Member ID
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
  - id: resolveMember
    name: Resolve Member
    type: boolean
    default: false
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - note
    typeInfo:
      type: boolean
      displayName: Resolve Member
      name: resolveMember
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
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
- id: upsert
  name: Create or Update
  description: Create a new member, or update the current one if it already exists
    (upsert)
  params:
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: identityUi
    name: Identity
    type: fixedCollection
    default: {}
    required: true
    description: The identity is used to find the member. If no member exists, a new
      member will be created and linked to the provided identity.
    placeholder: Add Identity
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - upsert
    typeInfo:
      type: fixedCollection
      displayName: Identity
      name: identityUi
      typeOptions:
        multipleValues: false
      subProperties:
      - name: identityValue
        displayName: Identity
        values:
        - displayName: Source
          name: source
          type: options
          description: Set to github, twitter, email, discourse or the source of any
            identities you've manually created
          value: discourse
          default: ''
          options:
          - name: Discourse
            value: discourse
            displayName: Discourse
          - name: Email
            value: email
            displayName: Email
          - name: GitHub
            value: github
            displayName: Git Hub
          - name: Twitter
            value: twitter
            displayName: Twitter
        - displayName: Search By
          name: searchBy
          type: options
          value: username
          default: ''
          required: true
          options:
          - name: Username
            value: username
            displayName: Username
          - name: ID
            value: id
            displayName: Id
          displayOptions:
            show:
              source:
              - discourse
              - github
              - twitter
        - displayName: ID
          name: id
          type: string
          description: The username at the source
          default: ''
          required: true
          displayOptions:
            show:
              searchBy:
              - id
              source:
              - discourse
              - github
              - twitter
        - displayName: Username
          name: username
          type: string
          description: The username at the source
          default: ''
          required: true
          displayOptions:
            show:
              searchBy:
              - username
              source:
              - discourse
              - github
              - twitter
        - displayName: Email
          name: email
          type: string
          placeholder: name@email.com
          default: ''
          required: true
          displayOptions:
            show:
              source:
              - email
        - displayName: Host
          name: host
          type: string
          default: ''
          required: true
          displayOptions:
            show:
              source:
              - discourse
- id: delete
  name: Delete
  description: Delete a member
  params:
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: postId
    name: Post ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - delete
          resource:
          - post
    typeInfo:
      type: string
      displayName: Post ID
      name: postId
- id: get
  name: Get
  description: Get a member
  params:
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: resolveIdentities
    name: Resolve Identities
    type: boolean
    default: false
    required: false
    description: By default, the response just includes the reference of the identity.
      When set to true the identities will be resolved automatically.
    validation: *id009
    typeInfo: *id010
- id: lookup
  name: Lookup
  description: Lookup a member by identity
  params:
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: source
    name: Source
    type: options
    default: ''
    required: true
    description: Set to github, twitter, email, discourse or the source of any identities
      you've manually created
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - lookup
    typeInfo:
      type: options
      displayName: Source
      name: source
      possibleValues:
      - value: discourse
        name: Discourse
        description: ''
      - value: email
        name: Email
        description: ''
      - value: github
        name: GitHub
        description: ''
      - value: twitter
        name: Twitter
        description: ''
  - id: searchBy
    name: Search By
    type: options
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - lookup
          source:
          - discourse
          - github
          - twitter
    typeInfo:
      type: options
      displayName: Search By
      name: searchBy
      possibleValues:
      - value: username
        name: Username
        description: ''
      - value: id
        name: ID
        description: ''
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The username at the source
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - lookup
          searchBy:
          - id
          source:
          - discourse
          - github
          - twitter
    typeInfo:
      type: string
      displayName: ID
      name: id
  - id: username
    name: Username
    type: string
    default: ''
    required: true
    description: The username at the source
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - lookup
          searchBy:
          - username
          source:
          - discourse
          - github
          - twitter
    typeInfo:
      type: string
      displayName: Username
      name: username
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email address
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - member
          operation:
          - lookup
          source:
          - email
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: host
    name: Host
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - member
          operation:
          - lookup
          source:
          - discourse
    typeInfo:
      type: string
      displayName: Host
      name: host
- id: update
  name: Update
  description: Update a member
  params:
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: workspaceId
    name: Workspace Name or ID
    type: options
    default: Deprecated
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: memberId
    name: Member ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: noteId
    name: Note ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - note
          operation:
          - update
    typeInfo:
      type: string
      displayName: Note ID
      name: noteId
  - id: note
    name: Note
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: deprecated
    text: Orbit has been shutdown and will no longer function from July 11th, You
      can read more <a target="_blank" href="https://orbit.love/blog/orbit-is-joining-postman">here</a>.
    conditions: null
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: options
    text: Add option
  - field: email
    text: name@email.com
  - field: updateFields
    text: Add Field
  - field: identityUi
    text: Add Identity
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/orbit.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Orbit Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "getAll",
        "upsert",
        "delete",
        "get",
        "lookup",
        "update"
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
            "member",
            "note",
            "post"
          ],
          "default": "member"
        },
        "operation": {
          "description": "Create a post",
          "type": "string",
          "enum": [
            "create",
            "getAll",
            "delete"
          ],
          "default": "create"
        },
        "workspaceId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": "Deprecated"
        },
        "memberId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "",
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
          "default": 100
        },
        "filters": {
          "description": "When set the post will be filtered by the member ID",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "resolveIdentities": {
          "description": "By default, the response just includes the reference of the identity. When set to true the identities will be resolved automatically.",
          "type": "boolean",
          "default": false
        },
        "options": {
          "description": "Name of the field the response will be sorted by",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "source": {
          "description": "Set to github, twitter, email, discourse or the source of any identities you've manually created",
          "type": "string",
          "enum": [
            "discourse",
            "email",
            "github",
            "twitter"
          ],
          "default": ""
        },
        "searchBy": {
          "description": "",
          "type": "string",
          "enum": [
            "username",
            "id"
          ],
          "default": ""
        },
        "id": {
          "description": "The username at the source",
          "type": "string",
          "default": ""
        },
        "username": {
          "description": "The username at the source",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "The email address",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "host": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Adds tags to member; comma-separated string or array",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "identityUi": {
          "description": "The identity is used to find the member. If no member exists, a new member will be created and linked to the provided identity.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Identity"
          ]
        },
        "note": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "resolveMember": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "noteId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "url": {
          "description": "Supply any URL and Orbit will do its best job to parse out a title, description, and image",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "postId": {
          "description": "",
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
      "name": "orbitApi",
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
