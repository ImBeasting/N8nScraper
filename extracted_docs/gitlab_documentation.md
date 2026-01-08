---
title: "Node: GitLab"
slug: "node-gitlab"
version: "1"
updated: "2026-01-08"
summary: "Retrieve data from GitLab API"
node_type: "regular"
group: "['input']"
---

# Node: GitLab

**Purpose.** Retrieve data from GitLab API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:gitlab.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **gitlabApi**: N/A
- **gitlabOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `gitlabApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `gitlabOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Issue Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new issue |
| Create Comment | `createComment` | Create a new comment on an issue |
| Edit | `edit` | Edit an issue |
| Get | `get` | Get the data of a single issue |
| Lock | `lock` | Lock an issue |

### Repository Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get the data of a single repository |
| Get Issues | `getIssues` | Returns issues of a repository |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Repositories | `getRepositories` | Returns the repositories of a user |

### Release Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new release |
| Delete | `delete` | Delete a release |
| Get | `get` | Get a release |
| Get Many | `getAll` | Get many releases |
| Update | `update` | Update a release |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new file in repository |
| Delete | `delete` | Delete a file in repository |
| Edit | `edit` | Edit a file in repository |
| Get | `get` | Get the data of a single file |
| List | `list` | List contents of a folder |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | issue | ✗ | Resource to operate on |  |

**Resource options:**

* **File** (`file`)
* **Issue** (`issue`)
* **Release** (`release`)
* **Repository** (`repository`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a new issue |  |

**Operation options:**

* **Create** (`create`) - Create a new issue
* **Create Comment** (`createComment`) - Create a new comment on an issue
* **Edit** (`edit`) - Edit an issue
* **Get** (`get`) - Get the data of a single issue
* **Lock** (`lock`) - Lock an issue

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ | The title of the issue |  |
| Body | `body` | string |  | ✗ | The body of the issue |  |
| Due Date | `due_date` | dateTime |  | ✗ | Due Date for issue |  |
| Labels | `labels` | collection |  | ✗ | Label to add to issue |  |

<details>
<summary><strong>Labels sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Label | `label` | string |  | Label to add to issue |

</details>

| Assignees | `assignee_ids` | collection | 0 | ✗ | User ID to assign issue to |  |

<details>
<summary><strong>Assignees sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee | `assignee` | number | 0 | User ID to assign issue to |

</details>

| Tag | `releaseTag` | string |  | ✓ | The tag of the release |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The name of the release |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | The name of the release |
| Description | `description` | string |  | The description of the release |
| Ref | `ref` | string |  | If Tag doesn’t exist, the release will be created from Ref. It can be a commit SHA, another tag name, or a branch name. |

</details>

| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| File Content | `fileContent` | string |  | ✓ | The text content of the file |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be written |  |
| Commit Message | `commitMessage` | string |  | ✓ |  |  |
| Branch | `branch` | string |  | ✓ | Name of the new branch to create. The commit is added to this branch. |  |
| Additional Parameters | `additionalParameters` | fixedCollection | {} | ✗ | Additional fields to add | e.g. Add Parameter |  |

<details>
<summary><strong>Additional Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Start Branch | `branchStart` |  |  |  |
| Author | `author` |  |  |  |
| Encoding | `encoding` |  |  |  |

</details>


### Create Comment parameters (`createComment`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Number | `issueNumber` | number | 0 | ✓ | The number of the issue on which to create the comment on |  |
| Body | `body` | string |  | ✗ | The body of the comment |  |

### Edit parameters (`edit`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Number | `issueNumber` | number | 0 | ✓ | The number of the issue edit |  |
| Edit Fields | `editFields` | collection | {} | ✗ | The title of the issue |  |

<details>
<summary><strong>Edit Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Title | `title` | string |  | The title of the issue |
| Body | `description` | string |  | The body of the issue |
| State | `state` | options | open | Set the state to "closed" |
| Labels | `labels` | collection |  | Label to add to issue |
| Assignees | `assignee_ids` | collection |  | User to assign issue too |
| Due Date | `due_date` | dateTime |  | Due Date for issue |

</details>

| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| File Content | `fileContent` | string |  | ✓ | The text content of the file |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be written |  |
| Commit Message | `commitMessage` | string |  | ✓ |  |  |
| Branch | `branch` | string |  | ✓ | Name of the new branch to create. The commit is added to this branch. |  |
| Additional Parameters | `additionalParameters` | fixedCollection | {} | ✗ | Additional fields to add | e.g. Add Parameter |  |

<details>
<summary><strong>Additional Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Start Branch | `branchStart` |  |  |  |
| Author | `author` |  |  |  |
| Encoding | `encoding` |  |  |  |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Number | `issueNumber` | number | 0 | ✓ | The number of the issue get data of |  |
| Project ID | `projectId` | string |  | ✓ | The ID or URL-encoded path of the project |  |
| Tag Name | `tag_name` | string |  | ✓ | The Git tag the release is associated with |  |
| As Binary Property | `asBinaryProperty` | boolean | True | ✗ | Whether to set the data of the file as binary property instead of returning the raw API response |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| Additional Parameters | `additionalParameters` | collection | {} | ✗ | Additional fields to add | e.g. Add Parameter |  |

<details>
<summary><strong>Additional Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Reference | `reference` | string |  | The name of the commit/branch/tag. Default: the repository’s default branch (usually main). |

</details>


### Lock parameters (`lock`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Number | `issueNumber` | number | 0 | ✓ | The number of the issue to lock |  |
| Lock Reason | `lockReason` | options | resolved | ✗ | The issue is Off-Topic |  |

**Lock Reason options:**

* **Off-Topic** (`off-topic`) - The issue is Off-Topic
* **Too Heated** (`too heated`) - The discussion is too heated
* **Resolved** (`resolved`) - The issue got resolved
* **Spam** (`spam`) - The issue is spam


### Get Issues parameters (`getIssues`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `getRepositoryIssuesFilters` | collection | {} | ✗ | Return only issues which are assigned to a specific user |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee | `assignee_username` | string |  | Return only issues which are assigned to a specific user |
| Creator | `author_username` | string |  | Return only issues which were created by a specific user |
| Search | `search` | string |  | Search issues against their title and description |
| Labels | `labels` | string |  | Return only issues with the given labels. Multiple lables can be separated by comma. |
| Updated After | `updated_after` | dateTime |  | Return only issues updated at or after this time |
| State | `state` | options | opened | Returns issues with any state |
| Sort | `order_by` | options | created_at | Sort by created date |
| Direction | `sort` | options | desc | Sort in ascending order |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project ID | `projectId` | string |  | ✓ | The ID or URL-encoded path of the project |  |
| Tag Name | `tag_name` | string |  | ✓ | The Git tag the release is associated with |  |
| Commit Message | `commitMessage` | string |  | ✓ |  |  |
| Branch | `branch` | string |  | ✓ | Name of the new branch to create. The commit is added to this branch. |  |
| Additional Parameters | `additionalParameters` | fixedCollection | {} | ✗ | Additional fields to add | e.g. Add Parameter |  |

<details>
<summary><strong>Additional Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Start Branch | `branchStart` |  |  |  |
| Author | `author` |  |  |  |
| Encoding | `encoding` |  |  |  |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project ID | `projectId` | string |  | ✓ | The ID or URL-encoded path of the project |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:100 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The field to use as order |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Order By | `order_by` | options | released_at | The field to use as order |
| Sort | `sort` | options | desc | The direction of the order. . |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project ID | `projectId` | string |  | ✓ | The ID or URL-encoded path of the project |  |
| Tag Name | `tag_name` | string |  | ✓ | The Git tag the release is associated with |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The release name |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | The release name |
| Description | `description` | string |  | The description of the release. You can use Markdown. |
| Milestones | `milestones` | string |  | The title of each milestone to associate with the release (provide a titles list spearated with comma) |
| Released At | `released_at` | dateTime |  | The date when the release is/was ready |

</details>


### List parameters (`list`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:100 |
| Path | `filePath` | string |  | ✗ | The path of the folder to list | e.g. docs/ |  |
| Page | `page` | number | 1 | ✗ | Page of results to display | min:1, max:1000 |
| Additional Parameters | `additionalParameters` | collection | {} | ✗ | Additional fields to add | e.g. Add Parameter |  |

<details>
<summary><strong>Additional Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Reference | `ref` | string |  | The name of the commit/branch/tag. Default: the repository’s default branch (usually main). |
| Recursive | `recursive` | boolean | False | Whether or not to get a recursive file tree. Default is false. |

</details>


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
node: gitlab
displayName: GitLab
description: Retrieve data from GitLab API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: gitlabApi
  required: true
- name: gitlabOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a new issue
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The title of the issue
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - issue
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: body
    name: Body
    type: string
    default: ''
    required: false
    description: The body of the issue
    validation: &id001
      displayOptions:
        show:
          operation:
          - createComment
          resource:
          - issue
    typeInfo: &id002
      type: string
      displayName: Body
      name: body
      typeOptions:
        rows: 5
  - id: due_date
    name: Due Date
    type: dateTime
    default: ''
    required: false
    description: Due Date for issue
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - issue
    typeInfo:
      type: dateTime
      displayName: Due Date
      name: due_date
  - id: releaseTag
    name: Tag
    type: string
    default: ''
    required: true
    description: The tag of the release
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - release
    typeInfo:
      type: string
      displayName: Tag
      name: releaseTag
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - create
          - edit
          resource:
          - file
    typeInfo: &id006
      type: boolean
      displayName: Binary File
      name: binaryData
  - id: fileContent
    name: File Content
    type: string
    default: ''
    required: true
    description: The text content of the file
    validation: &id007
      required: true
      displayOptions:
        show:
          binaryData:
          - false
          operation:
          - create
          - edit
          resource:
          - file
    typeInfo: &id008
      type: string
      displayName: File Content
      name: fileContent
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be written
    validation: &id009
      required: true
      displayOptions:
        show:
          binaryData:
          - true
          operation:
          - create
          - edit
          resource:
          - file
    typeInfo: &id010
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
  - id: commitMessage
    name: Commit Message
    type: string
    default: ''
    required: true
    description: ''
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - create
          - delete
          - edit
          resource:
          - file
    typeInfo: &id012
      type: string
      displayName: Commit Message
      name: commitMessage
  - id: branch
    name: Branch
    type: string
    default: ''
    required: true
    description: Name of the new branch to create. The commit is added to this branch.
    validation: &id013
      required: true
      displayOptions:
        show:
          operation:
          - create
          - delete
          - edit
          resource:
          - file
    typeInfo: &id014
      type: string
      displayName: Branch
      name: branch
  - id: additionalParameters
    name: Additional Parameters
    type: fixedCollection
    default: &id015 {}
    required: false
    description: Additional fields to add
    placeholder: Add Parameter
    validation: &id016
      displayOptions:
        show:
          operation:
          - create
          - delete
          - edit
          resource:
          - file
    typeInfo: &id017
      type: fixedCollection
      displayName: Additional Parameters
      name: additionalParameters
      subProperties:
      - name: branchStart
        displayName: Start Branch
        values:
        - displayName: Start Branch
          name: branchStart
          type: string
          description: Name of the base branch to create the new branch from
          default: ''
      - name: author
        displayName: Author
        values:
        - displayName: Name
          name: name
          type: string
          description: The name of the author of the commit
          default: ''
        - displayName: Email
          name: email
          type: string
          description: The email of the author of the commit
          placeholder: name@email.com
          default: ''
      - name: encoding
        displayName: Encoding
        values:
        - displayName: Encoding
          name: encoding
          type: string
          description: Change encoding to base64. Default is text.
          default: text
- id: createComment
  name: Create Comment
  description: Create a new comment on an issue
  params:
  - id: issueNumber
    name: Issue Number
    type: number
    default: 0
    required: true
    description: The number of the issue on which to create the comment on
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - lock
          resource:
          - issue
    typeInfo: &id004
      type: number
      displayName: Issue Number
      name: issueNumber
  - id: body
    name: Body
    type: string
    default: ''
    required: false
    description: The body of the comment
    validation: *id001
    typeInfo: *id002
- id: edit
  name: Edit
  description: Edit an issue
  params:
  - id: issueNumber
    name: Issue Number
    type: number
    default: 0
    required: true
    description: The number of the issue edit
    validation: *id003
    typeInfo: *id004
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
    validation: *id005
    typeInfo: *id006
  - id: fileContent
    name: File Content
    type: string
    default: ''
    required: true
    description: The text content of the file
    validation: *id007
    typeInfo: *id008
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be written
    validation: *id009
    typeInfo: *id010
  - id: commitMessage
    name: Commit Message
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: branch
    name: Branch
    type: string
    default: ''
    required: true
    description: Name of the new branch to create. The commit is added to this branch.
    validation: *id013
    typeInfo: *id014
  - id: additionalParameters
    name: Additional Parameters
    type: fixedCollection
    default: *id015
    required: false
    description: Additional fields to add
    placeholder: Add Parameter
    validation: *id016
    typeInfo: *id017
- id: get
  name: Get
  description: Get the data of a single issue
  params:
  - id: issueNumber
    name: Issue Number
    type: number
    default: 0
    required: true
    description: The number of the issue get data of
    validation: *id003
    typeInfo: *id004
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: The ID or URL-encoded path of the project
    validation: &id018
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - release
    typeInfo: &id019
      type: string
      displayName: Project ID
      name: projectId
  - id: tag_name
    name: Tag Name
    type: string
    default: ''
    required: true
    description: The Git tag the release is associated with
    validation: &id020
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - release
    typeInfo: &id021
      type: string
      displayName: Tag Name
      name: tag_name
  - id: asBinaryProperty
    name: As Binary Property
    type: boolean
    default: true
    required: false
    description: Whether to set the data of the file as binary property instead of
      returning the raw API response
    validation:
      displayOptions:
        show:
          operation:
          - get
          resource:
          - file
    typeInfo:
      type: boolean
      displayName: As Binary Property
      name: asBinaryProperty
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: *id009
    typeInfo: *id010
- id: lock
  name: Lock
  description: Lock an issue
  params:
  - id: issueNumber
    name: Issue Number
    type: number
    default: 0
    required: true
    description: The number of the issue to lock
    validation: *id003
    typeInfo: *id004
  - id: lockReason
    name: Lock Reason
    type: options
    default: resolved
    required: false
    description: The issue is Off-Topic
    validation:
      displayOptions:
        show:
          operation:
          - lock
          resource:
          - issue
    typeInfo:
      type: options
      displayName: Lock Reason
      name: lockReason
      possibleValues:
      - value: off-topic
        name: Off-Topic
        description: The issue is Off-Topic
      - value: too heated
        name: Too Heated
        description: The discussion is too heated
      - value: resolved
        name: Resolved
        description: The issue got resolved
      - value: spam
        name: Spam
        description: The issue is spam
- id: getIssues
  name: Get Issues
  description: Returns issues of a repository
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id022
      displayOptions:
        show:
          resource:
          - release
          - file
          - repository
          operation:
          - getAll
          - list
          - getIssues
    typeInfo: &id023
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 20
    required: false
    description: Max number of results to return
    validation: &id024
      displayOptions:
        show:
          resource:
          - release
          - file
          - repository
          operation:
          - getAll
          - list
          - getIssues
          returnAll:
          - false
    typeInfo: &id025
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
- id: getRepositories
  name: Get Repositories
  description: Returns the repositories of a user
- id: delete
  name: Delete
  description: Delete a release
  params:
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: The ID or URL-encoded path of the project
    validation: *id018
    typeInfo: *id019
  - id: tag_name
    name: Tag Name
    type: string
    default: ''
    required: true
    description: The Git tag the release is associated with
    validation: *id020
    typeInfo: *id021
  - id: commitMessage
    name: Commit Message
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: branch
    name: Branch
    type: string
    default: ''
    required: true
    description: Name of the new branch to create. The commit is added to this branch.
    validation: *id013
    typeInfo: *id014
  - id: additionalParameters
    name: Additional Parameters
    type: fixedCollection
    default: *id015
    required: false
    description: Additional fields to add
    placeholder: Add Parameter
    validation: *id016
    typeInfo: *id017
- id: getAll
  name: Get Many
  description: Get many releases
  params:
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: The ID or URL-encoded path of the project
    validation: *id018
    typeInfo: *id019
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id022
    typeInfo: *id023
  - id: limit
    name: Limit
    type: number
    default: 20
    required: false
    description: Max number of results to return
    validation: *id024
    typeInfo: *id025
- id: update
  name: Update
  description: Update a release
  params:
  - id: projectId
    name: Project ID
    type: string
    default: ''
    required: true
    description: The ID or URL-encoded path of the project
    validation: *id018
    typeInfo: *id019
  - id: tag_name
    name: Tag Name
    type: string
    default: ''
    required: true
    description: The Git tag the release is associated with
    validation: *id020
    typeInfo: *id021
- id: list
  name: List
  description: List contents of a folder
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id022
    typeInfo: *id023
  - id: limit
    name: Limit
    type: number
    default: 20
    required: false
    description: Max number of results to return
    validation: *id024
    typeInfo: *id025
  - id: filePath
    name: Path
    type: string
    default: ''
    required: false
    description: The path of the folder to list
    placeholder: docs/
    validation:
      displayOptions:
        show:
          resource:
          - file
          operation:
          - list
    typeInfo:
      type: string
      displayName: Path
      name: filePath
  - id: page
    name: Page
    type: number
    default: 1
    required: false
    description: Page of results to display
    validation:
      displayOptions:
        show:
          resource:
          - file
          operation:
          - list
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Page
      name: page
      typeOptions:
        minValue: 1
        maxValue: 1000
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
  - field: owner
    text: n8n-io
  - field: repository
    text: n8n
  - field: filePath
    text: docs/README.md
  - field: filePath
    text: docs/
  - field: additionalParameters
    text: Add Parameter
  - field: additionalParameters
    text: Add Parameter
  - field: additionalParameters
    text: Add Parameter
  hints:
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be written
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
  "$id": "https://n8n.io/schemas/nodes/gitlab.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GitLab Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "createComment",
        "edit",
        "get",
        "lock",
        "getIssues",
        "getRepositories",
        "delete",
        "getAll",
        "update",
        "list"
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
            "oAuth2"
          ],
          "default": "accessToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "file",
            "issue",
            "release",
            "repository",
            "user"
          ],
          "default": "issue"
        },
        "operation": {
          "description": "Create a new file in repository",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "edit",
            "get",
            "list"
          ],
          "default": "create"
        },
        "owner": {
          "description": "User, group or namespace of the project",
          "type": "string",
          "default": "",
          "examples": [
            "n8n-io"
          ]
        },
        "repository": {
          "description": "The name of the project",
          "type": "string",
          "default": "",
          "examples": [
            "n8n"
          ]
        },
        "title": {
          "description": "The title of the issue",
          "type": "string",
          "default": ""
        },
        "body": {
          "description": "The body of the comment",
          "type": "string",
          "default": ""
        },
        "due_date": {
          "description": "Due Date for issue",
          "type": "string",
          "default": ""
        },
        "labels": {
          "description": "Label to add to issue",
          "type": "string",
          "default": ""
        },
        "assignee_ids": {
          "description": "User ID to assign issue to",
          "type": "string",
          "default": 0
        },
        "issueNumber": {
          "description": "The number of the issue to lock",
          "type": "number",
          "default": 0
        },
        "editFields": {
          "description": "The title of the issue",
          "type": "string",
          "default": {}
        },
        "lockReason": {
          "description": "The issue is Off-Topic",
          "type": "string",
          "enum": [
            "off-topic",
            "too heated",
            "resolved",
            "spam"
          ],
          "default": "resolved"
        },
        "releaseTag": {
          "description": "The tag of the release",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The release name",
          "type": "string",
          "default": {}
        },
        "projectId": {
          "description": "The ID or URL-encoded path of the project",
          "type": "string",
          "default": ""
        },
        "tag_name": {
          "description": "The Git tag the release is associated with",
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
          "default": 20
        },
        "getRepositoryIssuesFilters": {
          "description": "Return only issues which are assigned to a specific user",
          "type": "string",
          "default": {}
        },
        "filePath": {
          "description": "The path of the folder to list",
          "type": "string",
          "default": "",
          "examples": [
            "docs/"
          ]
        },
        "page": {
          "description": "Page of results to display",
          "type": "number",
          "default": 1
        },
        "additionalParameters": {
          "description": "Additional fields to add",
          "type": "string",
          "default": {},
          "examples": [
            "Add Parameter"
          ]
        },
        "asBinaryProperty": {
          "description": "Whether to set the data of the file as binary property instead of returning the raw API response",
          "type": "boolean",
          "default": true
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "binaryData": {
          "description": "Whether the data to upload should be taken from binary field",
          "type": "boolean",
          "default": false
        },
        "fileContent": {
          "description": "The text content of the file",
          "type": "string",
          "default": ""
        },
        "commitMessage": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "branch": {
          "description": "Name of the new branch to create. The commit is added to this branch.",
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
      "name": "gitlabApi",
      "required": true
    },
    {
      "name": "gitlabOAuth2Api",
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
