---
title: "Node: Sentry.io"
slug: "node-sentryio"
version: "1"
updated: "2025-11-13"
summary: "Consume Sentry.io API"
node_type: "regular"
group: "['output']"
---

# Node: Sentry.io

**Purpose.** Consume Sentry.io API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:sentryio.svg', 'dark': 'file:sentryio.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **sentryIoOAuth2Api**: N/A
- **sentryIoApi**: N/A
- **sentryIoServerApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `sentryIoOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |
| `sentryIoApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `sentryIoServerApi` | ✓ | {'show': {'authentication': ['accessTokenServer']}} |

---

## Operations

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get event by ID |
| Get Many | `getAll` | Get many events |

### Issue Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete an issue |
| Get | `get` | Get issue by ID |
| Get Many | `getAll` | Get many issues |
| Update | `update` | Update an issue |

### Organization Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an organization |
| Get | `get` | Get organization by slug |
| Get Many | `getAll` | Get many organizations |
| Update | `update` | Update an organization |

### Project Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new project |
| Delete | `delete` | Delete a project |
| Get | `get` | Get project by ID |
| Get Many | `getAll` | Get many projects |
| Update | `update` | Update a project |

### Release Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a release |
| Delete | `delete` | Delete a release |
| Get | `get` | Get release by version identifier |
| Get Many | `getAll` | Get many releases |
| Update | `update` | Update a release |

### Team Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new team |
| Delete | `delete` | Delete a team |
| Get | `get` | Get team by slug |
| Get Many | `getAll` | Get many teams |
| Update | `update` | Update a team |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | event | ✗ | Resource to operate on |  |

**Resource options:**

* **Event** (`event`)
* **Issue** (`issue`)
* **Organization** (`organization`)
* **Project** (`project`)
* **Release** (`release`)
* **Team** (`team`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Get event by ID |  |

**Operation options:**

* **Get** (`get`) - Get event by ID
* **Get Many** (`getAll`) - Get many events

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the events belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Project Slug Name or ID | `projectSlug` | options |  | ✓ | The slug of the project the events belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Event ID | `eventId` | string |  | ✓ | The ID of the event to retrieve (either the numeric primary-key or the hexadecimal ID as reported by the raven client) |  |
| Issue ID | `issueId` | string |  | ✓ | ID of issue to get | e.g. 1234 |  |
| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the team should be created for. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the events belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Project Slug Name or ID | `projectSlug` | options |  | ✓ | The slug of the project to retrieve. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the release belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Version | `version` | string |  | ✓ | The version identifier of the release |  |
| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the team belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Team Slug Name or ID | `teamSlug` | options |  | ✓ | The slug of the team to get. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the events belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Project Slug Name or ID | `projectSlug` | options |  | ✓ | The slug of the project the events belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Full | `full` | boolean | True | ✗ | Whether the event payload will include the full event body, including the stack trace |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the issues belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Project Slug Name or ID | `projectSlug` | options |  | ✓ | The slug of the project the issues belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | An optional Sentry structured search query. If not provided, an implied "is:unresolved" is assumed. Info <a href="https://docs.sentry.io/product/sentry-basics/search/">here</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | An optional Sentry structured search query. If not provided, an implied "is:unresolved" is assumed. Info <a href="https://docs.sentry.io/product/sentry-basics/search/">here</a>. |
| Stats Period | `statsPeriod` | options |  | Time period of stats |
| Short ID Lookup | `shortIdLookUp` | boolean | True | Whether short IDs are looked up by this function as well. This can cause the return value of the function to return an event issue of a different project which is why this is an opt-in. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to restrict results to organizations which you have membership | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Member | `member` | boolean | True | Whether to restrict results to organizations which you have membership |
| Owner | `owner` | boolean | True | Whether to restrict results to organizations which you are the owner |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the releases belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | This parameter can be used to create a “starts with” filter for the version | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | This parameter can be used to create a “starts with” filter for the version |

</details>

| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization for which the teams should be listed. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue ID | `issueId` | string |  | ✓ | ID of issue to get | e.g. 1234 |  |
| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the project belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Project Slug Name or ID | `projectSlug` | options |  | ✓ | The slug of the project to delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the release belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Version | `version` | string |  | ✓ | The version identifier of the release |  |
| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the team belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Team Slug Name or ID | `teamSlug` | options |  | ✓ | The slug of the team to delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue ID | `issueId` | string |  | ✓ | ID of issue to get | e.g. 1234 |  |
| Update Fields | `additionalFields` | collection | {} | ✗ | The actor ID (or username) of the user or team that should be assigned to this issue | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assigned To | `assignedTo` | string |  | The actor ID (or username) of the user or team that should be assigned to this issue |
| Has Seen | `hasSeen` | boolean | True | Whether this API call is invoked with a user context this allows changing of the flag that indicates if the user has seen the event |
| Is Bookmarked | `isBookmarked` | boolean | True | Whether this API call is invoked with a user context this allows changing of the bookmark flag |
| Is Public | `isPublic` | boolean | True | Whether to set the issue to public or private |
| Is Subscribed | `isSubscribed` | boolean | True |  |
| Status | `status` | options |  | The new status for the issue |

</details>

| Slug Name or ID | `organization_slug` | options |  | ✓ | The slug of the organization to update. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The new name of the organization | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | The new name of the organization |
| Slug | `slug` | string |  | The new URL slug for this organization |

</details>

| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the project belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Project Slug Name or ID | `projectSlug` | options |  | ✓ | The slug of the project to update. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The new platform for the updated project | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Bookmarked | `isBookmarked` | boolean | False | The new platform for the updated project |
| Digests Maximum Delay | `digestsMaxDelay` | number | 1800 | Maximum interval to digest alerts |
| Digests Minimun Delay | `digestsMinDelay` | number | 60 | Minium interval to digest alerts |
| Name | `name` | string |  | The new name for the updated project |
| Slug | `slug` | string |  | The new slug for the updated project |
| Team | `team` | string |  | The new team name |
| Platform | `platform` | string |  | The new platform for the updated project |

</details>

| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the release belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Version | `version` | string |  | ✓ | A version identifier for this release. Can be a version number, a commit hash etc. |  |
| Update Fields | `updateFields` | collection | {} | ✓ | An optional list of commit data to be associated with the release | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Commits | `commits` | fixedCollection | {} | An optional list of commit data to be associated with the release |
| Date Released | `dateReleased` | dateTime |  | An optional date that indicates when the release went live. If not provided the current time is assumed. |
| Ref | `ref` | string |  | A URL that points to the release. This can be the path to an online interface to the sourcecode for instance. |
| Refs | `refs` | fixedCollection | {} | An optional way to indicate the start and end commits for each repository included in a release |
| URL | `url` | string |  | A URL that points to the release. This can be the path to an online interface to the sourcecode for instance. |

</details>

| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the team belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Team Slug Name or ID | `teamSlug` | options |  | ✓ | The slug of the team to update. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The new name of the team | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | The new name of the team |
| Slug | `slug` | string |  | The new slug of the team. Must be unique and available. |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | The slug of the organization the team should be created for |  |
| Agree to Terms | `agreeTerms` | boolean | False | ✗ | Whether you agree to the applicable terms of service and privacy policy of Sentry.io |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The unique URL slug for this organization. If this is not provided a slug is automatically generated based on the name. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Slug | `slug` | string |  | The unique URL slug for this organization. If this is not provided a slug is automatically generated based on the name. |

</details>

| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the events belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Team Slug Name or ID | `teamSlug` | options |  | ✓ | The slug of the team to create a new project for. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Name | `name` | string |  | ✓ | The name for the new project |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Optionally a slug for the new project. If it’s not provided a slug is generated from the name. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Slug | `slug` | string |  | Optionally a slug for the new project. If it’s not provided a slug is generated from the name. |

</details>

| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the release belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Version | `version` | string |  | ✓ | A version identifier for this release. Can be a version number, a commit hash etc. |  |
| URL | `url` | string |  | ✓ | A URL that points to the release. This can be the path to an online interface to the sourcecode for instance. | url |
| Project Names or IDs | `projects` | multiOptions | [] | ✓ | A list of project slugs that are involved in this release. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | An optional date that indicates when the release went live. If not provided the current time is assumed. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date Released | `dateReleased` | dateTime |  | An optional date that indicates when the release went live. If not provided the current time is assumed. |
| Commits | `commits` | fixedCollection | {} | An optional list of commit data to be associated with the release |
| Refs | `refs` | fixedCollection | {} | An optional way to indicate the start and end commits for each repository included in a release |

</details>

| Organization Slug Name or ID | `organizationSlug` | options |  | ✓ | The slug of the organization the team belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Name | `name` | string |  | ✓ | The name of the team |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The optional slug for this team. If not provided it will be auto generated from the name. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Slug | `slug` | string |  | The optional slug for this team. If not provided it will be auto generated from the name. |

</details>


---

## Load Options Methods

- `getOrganizations`

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
node: sentryIo
displayName: Sentry.io
description: Consume Sentry.io API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: sentryIoOAuth2Api
  required: true
- name: sentryIoApi
  required: true
- name: sentryIoServerApi
  required: true
operations:
- id: get
  name: Get
  description: Get event by ID
  params:
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the events belong to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - team
          operation:
          - delete
    typeInfo: &id002
      type: options
      displayName: Organization Slug Name or ID
      name: organizationSlug
      typeOptions:
        loadOptionsMethod: getOrganizations
      possibleValues: []
  - id: projectSlug
    name: Project Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the project the events belong to. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - project
          operation:
          - delete
    typeInfo: &id004
      type: options
      displayName: Project Slug Name or ID
      name: projectSlug
      typeOptions:
        loadOptionsMethod: getProjects
      possibleValues: []
  - id: eventId
    name: Event ID
    type: string
    default: ''
    required: true
    description: The ID of the event to retrieve (either the numeric primary-key or
      the hexadecimal ID as reported by the raven client)
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - event
          operation:
          - get
    typeInfo:
      type: string
      displayName: Event ID
      name: eventId
  - id: issueId
    name: Issue ID
    type: string
    default: ''
    required: true
    description: ID of issue to get
    placeholder: '1234'
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Issue ID
      name: issueId
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the team should be created for. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the events belong to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: projectSlug
    name: Project Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the project to retrieve. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the release belongs to. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: version
    name: Version
    type: string
    default: ''
    required: true
    description: The version identifier of the release
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - release
          operation:
          - update
    typeInfo: &id012
      type: string
      displayName: Version
      name: version
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the team belongs to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: teamSlug
    name: Team Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the team to get. Choose from the list, or specify an
      ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - team
          operation:
          - delete
    typeInfo: &id014
      type: options
      displayName: Team Slug Name or ID
      name: teamSlug
      typeOptions:
        loadOptionsMethod: getTeams
      possibleValues: []
- id: getAll
  name: Get Many
  description: Get many events
  params:
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the events belong to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: projectSlug
    name: Project Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the project the events belong to. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: full
    name: Full
    type: boolean
    default: true
    required: false
    description: Whether the event payload will include the full event body, including
      the stack trace
    validation:
      displayOptions:
        show:
          resource:
          - event
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Full
      name: full
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
          - team
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
          - team
          returnAll:
          - false
    typeInfo: &id008
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the issues belong to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: projectSlug
    name: Project Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the project the issues belong to. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
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
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the releases belong to. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
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
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization for which the teams should be listed.
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
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
- id: delete
  name: Delete
  description: Delete an issue
  params:
  - id: issueId
    name: Issue ID
    type: string
    default: ''
    required: true
    description: ID of issue to get
    placeholder: '1234'
    validation: *id009
    typeInfo: *id010
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the project belong to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: projectSlug
    name: Project Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the project to delete. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the release belongs to. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: version
    name: Version
    type: string
    default: ''
    required: true
    description: The version identifier of the release
    validation: *id011
    typeInfo: *id012
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the team belongs to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: teamSlug
    name: Team Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the team to delete. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id013
    typeInfo: *id014
- id: update
  name: Update
  description: Update an issue
  params:
  - id: issueId
    name: Issue ID
    type: string
    default: ''
    required: true
    description: ID of issue to get
    placeholder: '1234'
    validation: *id009
    typeInfo: *id010
  - id: organization_slug
    name: Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization to update. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - organization
          operation:
          - update
    typeInfo:
      type: options
      displayName: Slug Name or ID
      name: organization_slug
      typeOptions:
        loadOptionsMethod: getOrganizations
      possibleValues: []
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the project belong to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: projectSlug
    name: Project Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the project to update. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the release belongs to. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: version
    name: Version
    type: string
    default: ''
    required: true
    description: A version identifier for this release. Can be a version number, a
      commit hash etc.
    validation: *id011
    typeInfo: *id012
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the team belongs to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: teamSlug
    name: Team Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the team to update. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id013
    typeInfo: *id014
- id: create
  name: Create
  description: Create an organization
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The slug of the organization the team should be created for
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - team
          operation:
          - create
    typeInfo: &id016
      type: string
      displayName: Name
      name: name
  - id: agreeTerms
    name: Agree to Terms
    type: boolean
    default: false
    required: false
    description: Whether you agree to the applicable terms of service and privacy
      policy of Sentry.io
    validation:
      displayOptions:
        show:
          resource:
          - organization
          operation:
          - create
    typeInfo:
      type: boolean
      displayName: Agree to Terms
      name: agreeTerms
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the events belong to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: teamSlug
    name: Team Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the team to create a new project for. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id013
    typeInfo: *id014
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name for the new project
    validation: *id015
    typeInfo: *id016
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the release belongs to. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: version
    name: Version
    type: string
    default: ''
    required: true
    description: A version identifier for this release. Can be a version number, a
      commit hash etc.
    validation: *id011
    typeInfo: *id012
  - id: url
    name: URL
    type: string
    default: ''
    required: true
    description: A URL that points to the release. This can be the path to an online
      interface to the sourcecode for instance.
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - release
          operation:
          - create
    typeInfo:
      type: string
      displayName: URL
      name: url
  - id: projects
    name: Project Names or IDs
    type: multiOptions
    default: []
    required: true
    description: A list of project slugs that are involved in this release. Choose
      from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - release
          operation:
          - create
    typeInfo:
      type: multiOptions
      displayName: Project Names or IDs
      name: projects
      typeOptions:
        loadOptionsMethod: getProjects
      possibleValues: []
  - id: organizationSlug
    name: Organization Slug Name or ID
    type: options
    default: ''
    required: true
    description: The slug of the organization the team belongs to. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the team
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
  - field: issueId
    text: '1234'
  - field: additionalFields
    text: Add Field
  - field: issueId
    text: '1234'
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/sentryIo.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Sentry.io Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll",
        "delete",
        "update",
        "create"
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
            "accessToken",
            "oAuth2",
            "accessTokenServer"
          ],
          "default": "accessToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "event",
            "issue",
            "organization",
            "project",
            "release",
            "team"
          ],
          "default": "event"
        },
        "operation": {
          "description": "Create a new team",
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
        "organizationSlug": {
          "description": "The slug of the organization the team belongs to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "projectSlug": {
          "description": "The slug of the project to delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "full": {
          "description": "Whether the event payload will include the full event body, including the stack trace",
          "type": "boolean",
          "default": true
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
        "eventId": {
          "description": "The ID of the event to retrieve (either the numeric primary-key or the hexadecimal ID as reported by the raven client)",
          "type": "string",
          "default": ""
        },
        "issueId": {
          "description": "ID of issue to get",
          "type": "string",
          "default": "",
          "examples": [
            "1234"
          ]
        },
        "additionalFields": {
          "description": "The optional slug for this team. If not provided it will be auto generated from the name.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "name": {
          "description": "The name of the team",
          "type": "string",
          "default": ""
        },
        "agreeTerms": {
          "description": "Whether you agree to the applicable terms of service and privacy policy of Sentry.io",
          "type": "boolean",
          "default": false
        },
        "organization_slug": {
          "description": "The slug of the organization to update. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "The new name of the team",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "teamSlug": {
          "description": "The slug of the team to delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "version": {
          "description": "A version identifier for this release. Can be a version number, a commit hash etc.",
          "type": "string",
          "default": ""
        },
        "url": {
          "description": "A URL that points to the release. This can be the path to an online interface to the sourcecode for instance.",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "projects": {
          "description": "A list of project slugs that are involved in this release. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
      "name": "sentryIoOAuth2Api",
      "required": true
    },
    {
      "name": "sentryIoApi",
      "required": true
    },
    {
      "name": "sentryIoServerApi",
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
