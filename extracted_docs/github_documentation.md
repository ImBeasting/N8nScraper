---
title: "Node: GitHub"
slug: "node-github"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Consume GitHub API"
node_type: "regular"
group: "['input']"
---

# Node: GitHub

**Purpose.** Consume GitHub API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:github.svg', 'dark': 'file:github.dark.svg'}`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **githubApi**: N/A
- **githubOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **webhookNotice** when resource=['workflow'], operation=['dispatchAndWait']: Your execution will pause until a webhook is called. This URL will be generated at runtime and passed to your Github workflow as a resumeUrl input.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `githubApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `githubOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** User-Agent

---

## Operations

### Organization Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Repositories | `getRepositories` | Returns all repositories of an organization |

### Issue Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new issue |
| Create Comment | `createComment` | Create a new comment on an issue |
| Edit | `edit` | Edit an issue |
| Get | `get` | Get the data of a single issue |
| Lock | `lock` | Lock an issue |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new file in repository |
| Delete | `delete` | Delete a file in repository |
| Edit | `edit` | Edit a file in repository |
| Get | `get` | Get the data of a single file |
| List | `list` | List contents of a folder |

### Repository Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get the data of a single repository |
| Get Issues | `getIssues` | Returns issues of a repository |
| Get License | `getLicense` | Returns the contents of the repository's license file, if one is detected |
| Get Profile | `getProfile` | Get the community profile of a repository with metrics, health score, description, license, etc |
| Get Pull Requests | `getPullRequests` | Returns pull requests of a repository |
| List Popular Paths | `listPopularPaths` | Get the top 10 popular content paths over the last 14 days |
| List Referrers | `listReferrers` | Get the top 10 referrering domains over the last 14 days |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Repositories | `getRepositories` | Returns the repositories of a user |
| Get Issues | `getUserIssues` | Returns the issues assigned to the user |
| Invite | `invite` | Invites a user to an organization |

### Release Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Creates a new release |
| Delete | `delete` | Delete a release |
| Get | `get` | Get a release |
| Get Many | `getAll` | Get many repository releases |
| Update | `update` | Update a release |

### Review Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Creates a new review |
| Get | `get` | Get a review for a pull request |
| Get Many | `getAll` | Get many reviews for a pull request |
| Update | `update` | Update a review |

### Workflow Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Disable | `disable` | Disable a workflow |
| Dispatch | `dispatch` | Dispatch a workflow event |
| Dispatch and Wait for Completion | `dispatchAndWait` | Dispatch a workflow event and wait for a webhook to be called before proceeding |
| Enable | `enable` | Enable a workflow |
| Get | `get` | Get a workflow |
| Get Usage | `getUsage` | Get the usage of a workflow |
| List | `list` | List workflows |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | issue | ✗ | Resource to operate on |  |

**Resource options:**

* **File** (`file`)
* **Issue** (`issue`)
* **Organization** (`organization`)
* **Release** (`release`)
* **Repository** (`repository`)
* **Review** (`review`)
* **User** (`user`)
* **Workflow** (`workflow`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getRepositories | ✗ | Returns all repositories of an organization |  |

**Operation options:**

* **Get Repositories** (`getRepositories`) - Returns all repositories of an organization

---

### Get Repositories parameters (`getRepositories`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| File Content | `fileContent` | string |  | ✓ | The text content of the file |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be written |  |
| Commit Message | `commitMessage` | string |  | ✓ |  |  |
| Additional Parameters | `additionalParameters` | fixedCollection | {} | ✗ | Additional fields to add | e.g. Add Parameter |  |

<details>
<summary><strong>Additional Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Author | `author` |  |  |  |
| Branch | `branch` |  |  |  |
| Committer | `committer` |  |  |  |

</details>

| Title | `title` | string |  | ✓ | The title of the issue |  |
| Body | `body` | string |  | ✗ | The body of the issue |  |
| Labels | `labels` | collection |  | ✗ | Label to add to issue |  |

<details>
<summary><strong>Labels sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Label | `label` | string |  | Label to add to issue |

</details>

| Assignees | `assignees` | collection |  | ✗ | User to assign issue too |  |

<details>
<summary><strong>Assignees sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee | `assignee` | string |  | User to assign issue too |

</details>

| Tag | `releaseTag` | string |  | ✓ | The tag of the release |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The name of the issue |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | The name of the issue |
| Body | `body` | string |  | The body of the release |
| Draft | `draft` | boolean | False | Whether to create a draft (unpublished) release, "false" to create a published one |
| Prerelease | `prerelease` | boolean | False | Whether to point out that the release is non-production ready |
| Target Commitish | `target_commitish` | string |  | Specifies the commitish value that determines where the Git tag is created from. Can be any branch or commit SHA. Unused if the Git tag already exists. Default: the repository's default branch(usually master). |

</details>

| PR Number | `pullRequestNumber` | number | 0 | ✓ | The number of the pull request to review |  |
| Event | `event` | options | approve | ✗ | Approve the pull request |  |

**Event options:**

* **Approve** (`approve`) - Approve the pull request
* **Request Change** (`requestChanges`) - Request code changes
* **Comment** (`comment`) - Add a comment without approval or change requests
* **Pending** (`pending`) - You will need to submit the pull request review when you are ready

| Body | `body` | string |  | ✗ | The body of the review (required for events Request Changes or Comment) |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The SHA of the commit that needs a review, if different from the latest | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Commit ID | `commitId` | string |  | The SHA of the commit that needs a review, if different from the latest |

</details>


### Create Comment parameters (`createComment`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Number | `issueNumber` | number | 0 | ✓ | The number of the issue on which to create the comment on |  |
| Body | `body` | string |  | ✗ | The body of the comment |  |

### Edit parameters (`edit`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| File Content | `fileContent` | string |  | ✓ | The text content of the file |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be written |  |
| Commit Message | `commitMessage` | string |  | ✓ |  |  |
| Additional Parameters | `additionalParameters` | fixedCollection | {} | ✗ | Additional fields to add | e.g. Add Parameter |  |

<details>
<summary><strong>Additional Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Author | `author` |  |  |  |
| Branch | `branch` |  |  |  |
| Committer | `committer` |  |  |  |

</details>

| Issue Number | `issueNumber` | number | 0 | ✓ | The number of the issue edit |  |
| Edit Fields | `editFields` | collection | {} | ✗ | User to assign issue to |  |

<details>
<summary><strong>Edit Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignees | `assignees` | collection |  | User to assign issue to |
| Body | `body` | string |  | The body of the issue |
| Labels | `labels` | collection |  | Label to add to issue |
| State | `state` | options | open | Set the state to "closed" |
| State Reason | `state_reason` | options | completed | Issue is completed |
| Title | `title` | string |  | The title of the issue |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workflow | `workflowId` | resourceLocator |  | ✓ | The workflow to dispatch | e.g. Select a workflow... |  |
| As Binary Property | `asBinaryProperty` | boolean | True | ✗ | Whether to set the data of the file as binary property instead of returning the raw API response |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| Additional Parameters | `additionalParameters` | collection | {} | ✗ | Additional fields to add | e.g. Add Parameter |  |

<details>
<summary><strong>Additional Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Reference | `reference` | string |  | The name of the commit/branch/tag. Default: the repository’s default branch (usually master). |

</details>

| Issue Number | `issueNumber` | number | 0 | ✓ | The issue number to get data for |  |
| Release ID | `release_id` | string |  | ✓ |  |  |
| PR Number | `pullRequestNumber` | number | 0 | ✓ | The number of the pull request |  |
| Review ID | `reviewId` | string |  | ✓ | ID of the review |  |

### Lock parameters (`lock`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Number | `issueNumber` | number | 0 | ✓ | The issue number to lock |  |
| Lock Reason | `lockReason` | options | resolved | ✗ | The issue is Off-Topic |  |

**Lock Reason options:**

* **Off-Topic** (`off-topic`) - The issue is Off-Topic
* **Too Heated** (`too heated`) - The discussion is too heated
* **Resolved** (`resolved`) - The issue got resolved
* **Spam** (`spam`) - The issue is spam


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Commit Message | `commitMessage` | string |  | ✓ |  |  |
| Additional Parameters | `additionalParameters` | fixedCollection | {} | ✗ | Additional fields to add | e.g. Add Parameter |  |

<details>
<summary><strong>Additional Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Author | `author` |  |  |  |
| Branch | `branch` |  |  |  |
| Committer | `committer` |  |  |  |

</details>

| Release ID | `release_id` | string |  | ✓ |  |  |

### List parameters (`list`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Path | `filePath` | string |  | ✗ | The path of the folder to list | e.g. docs/ |  |

### Get Issues parameters (`getIssues`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `getRepositoryIssuesFilters` | collection | {} | ✗ | Return only issues which are assigned to a specific user |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee | `assignee` | string |  | Return only issues which are assigned to a specific user |
| Creator | `creator` | string |  | Return only issues which were created by a specific user |
| Mentioned | `mentioned` | string |  | Return only issues in which a specific user was mentioned |
| Labels | `labels` | string |  | Return only issues with the given labels. Multiple labels can be separated by comma. |
| Updated Since | `since` | dateTime |  | Return only issues updated at or after this time |
| State | `state` | options | open | Returns issues with any state |
| Sort | `sort` | options | created | Sort by created date |
| Direction | `direction` | options | desc | Sort in ascending order |

</details>


### Get Pull Requests parameters (`getPullRequests`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return. Maximum value is <a href="https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-pull-requests">100</a>. | min:1, max:100 |
| Filters | `getRepositoryPullRequestsFilters` | collection | {} | ✗ | Returns pull requests with any state |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| State | `state` | options | open | Returns pull requests with any state |
| Sort | `sort` | options | created | Sort by created date |
| Direction | `direction` | options | desc | Sort in ascending order |

</details>


### Get Issues parameters (`getUserIssues`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `getUserIssuesFilters` | collection | {} | ✗ | Return only issues in which a specific user was mentioned |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Mentioned | `mentioned` | string |  | Return only issues in which a specific user was mentioned |
| Labels | `labels` | string |  | Return only issues with the given labels. Multiple labels can be separated by comma. |
| Updated Since | `since` | dateTime |  | Return only issues updated at or after this time |
| State | `state` | options | open | Returns issues with any state |
| Sort | `sort` | options | created | Sort by created date |
| Direction | `direction` | options | desc | Sort in ascending order |

</details>


### Invite parameters (`invite`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Organization | `organization` | string |  | ✓ | The GitHub organization that the user is being invited to |  |
| Email | `email` | string |  | ✓ | The email address of the invited user | e.g. name@email.com | email |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| PR Number | `pullRequestNumber` | number | 0 | ✓ | The number of the pull request |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Release ID | `release_id` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The body of the release |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body | `body` | string |  | The body of the release |
| Draft | `draft` | boolean | False | Whether to create a draft (unpublished) release, "false" to create a published one |
| Name | `name` | string |  | The name of the release |
| Prerelease | `prerelease` | boolean | False | Whether to point out that the release is non-production ready |
| Tag Name | `tag_name` | string |  | The name of the tag |
| Target Commitish | `target_commitish` | string |  | Specifies the commitish value that determines where the Git tag is created from. Can be any branch or commit SHA. Unused if the Git tag already exists. Default: the repository's default branch(usually master). |

</details>

| PR Number | `pullRequestNumber` | number | 0 | ✓ | The number of the pull request |  |
| Review ID | `reviewId` | string |  | ✓ | ID of the review |  |
| Body | `body` | string |  | ✗ | The body of the review |  |

### Disable parameters (`disable`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workflow | `workflowId` | resourceLocator |  | ✓ | The workflow to dispatch | e.g. Select a workflow... |  |

### Dispatch parameters (`dispatch`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workflow | `workflowId` | resourceLocator |  | ✓ | The workflow to dispatch | e.g. Select a workflow... |  |
| Ref | `ref` | string | main | ✓ | The git reference for the workflow dispatch (branch or tag name) |  |
| Inputs | `inputs` | json | {} | ✗ | JSON object with input parameters for the workflow |  |

### Dispatch and Wait for Completion parameters (`dispatchAndWait`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workflow | `workflowId` | resourceLocator |  | ✓ | The workflow to dispatch | e.g. Select a workflow... |  |
| Ref | `ref` | string | main | ✓ | The git reference for the workflow dispatch (branch or tag name) |  |
| Inputs | `inputs` | json | {} | ✗ | JSON object with input parameters for the workflow |  |

### Enable parameters (`enable`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workflow | `workflowId` | resourceLocator |  | ✓ | The workflow to dispatch | e.g. Select a workflow... |  |

### Get Usage parameters (`getUsage`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Workflow | `workflowId` | resourceLocator |  | ✓ | The workflow to dispatch | e.g. Select a workflow... |  |

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Get Organization Repositories

**From workflow:** Github Organization getRepositories Test Workflow

**Parameters:**
```json
{
  "resource": "organization",
  "operation": "getRepositories",
  "owner": {
    "__rl": true,
    "value": "testorg",
    "mode": "name"
  },
  "returnAll": true
}
```

**Credentials:**
- githubApi: `Test Credentials`

### Example 2: Get User Issues Filtered

**From workflow:** Github User getUserIssues Filtered Test Workflow

**Parameters:**
```json
{
  "resource": "user",
  "operation": "getUserIssues",
  "returnAll": true,
  "getUserIssuesFilters": {
    "state": "closed",
    "labels": "enhancement"
  }
}
```

**Credentials:**
- githubApi: `Test Credentials`

### Example 3: Get Repository Issues Limited

**From workflow:** Github Repository getIssues Limit Test Workflow

**Parameters:**
```json
{
  "resource": "repository",
  "operation": "getIssues",
  "owner": {
    "__rl": true,
    "value": "testowner",
    "mode": "name"
  },
  "repository": {
    "__rl": true,
    "value": "testrepo",
    "mode": "name"
  },
  "returnAll": false,
  "limit": 1,
  "getRepositoryIssuesFilters": {}
}
```

**Credentials:**
- githubApi: `Test Credentials`

### Example 4: Get User Repositories Limited

**From workflow:** Github User getRepositories Limit Test Workflow

**Parameters:**
```json
{
  "resource": "user",
  "operation": "getRepositories",
  "owner": {
    "__rl": true,
    "value": "testuser",
    "mode": "name"
  },
  "returnAll": false,
  "limit": 1
}
```

**Credentials:**
- githubApi: `Test Credentials`

### Example 5: Get Repository Issues Filtered

**From workflow:** Github Repository getIssues Filtered Test Workflow

**Parameters:**
```json
{
  "resource": "repository",
  "operation": "getIssues",
  "owner": {
    "__rl": true,
    "value": "testowner",
    "mode": "name"
  },
  "repository": {
    "__rl": true,
    "value": "testrepo",
    "mode": "name"
  },
  "returnAll": true,
  "getRepositoryIssuesFilters": {
    "state": "closed",
    "labels": "bug",
    "assignee": "testuser"
  }
}
```

**Credentials:**
- githubApi: `Test Credentials`


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
node: github
displayName: GitHub
description: Consume GitHub API
version:
- '1'
- '1.1'
nodeType: regular
group:
- input
credentials:
- name: githubApi
  required: true
- name: githubOAuth2Api
  required: true
operations:
- id: getRepositories
  name: Get Repositories
  description: Returns all repositories of an organization
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
          operation:
          - getUserIssues
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
          operation:
          - getUserIssues
          returnAll:
          - false
    typeInfo: &id004
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
  description: Create a new issue
  params:
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - create
          - edit
          resource:
          - file
    typeInfo: &id008
      type: boolean
      displayName: Binary File
      name: binaryData
  - id: fileContent
    name: File Content
    type: string
    default: ''
    required: true
    description: The text content of the file
    validation: &id009
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
    typeInfo: &id010
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
    validation: &id011
      required: true
      displayOptions:
        show:
          asBinaryProperty:
          - true
          operation:
          - get
          resource:
          - file
    typeInfo: &id012
      type: string
      displayName: Put Output File in Field
      name: binaryPropertyName
  - id: commitMessage
    name: Commit Message
    type: string
    default: ''
    required: true
    description: ''
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
      displayName: Commit Message
      name: commitMessage
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
          - get
          resource:
          - file
    typeInfo: &id017
      type: collection
      displayName: Additional Parameters
      name: additionalParameters
      subProperties:
      - displayName: Reference
        name: reference
        type: string
        description: 'The name of the commit/branch/tag. Default: the repository’s
          default branch (usually master).'
        placeholder: master
        default: ''
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
    validation: &id005
      displayOptions:
        show:
          operation:
          - update
          resource:
          - review
    typeInfo: &id006
      type: string
      displayName: Body
      name: body
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
  - id: pullRequestNumber
    name: PR Number
    type: number
    default: 0
    required: true
    description: The number of the pull request to review
    validation: &id020
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - review
    typeInfo: &id021
      type: number
      displayName: PR Number
      name: pullRequestNumber
  - id: event
    name: Event
    type: options
    default: approve
    required: false
    description: Approve the pull request
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - review
    typeInfo:
      type: options
      displayName: Event
      name: event
      possibleValues:
      - value: approve
        name: Approve
        description: Approve the pull request
      - value: requestChanges
        name: Request Change
        description: Request code changes
      - value: comment
        name: Comment
        description: Add a comment without approval or change requests
      - value: pending
        name: Pending
        description: You will need to submit the pull request review when you are
          ready
  - id: body
    name: Body
    type: string
    default: ''
    required: false
    description: The body of the review (required for events Request Changes or Comment)
    validation: *id005
    typeInfo: *id006
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
    validation: &id018
      required: true
      displayOptions:
        show:
          operation:
          - lock
          resource:
          - issue
    typeInfo: &id019
      type: number
      displayName: Issue Number
      name: issueNumber
  - id: body
    name: Body
    type: string
    default: ''
    required: false
    description: The body of the comment
    validation: *id005
    typeInfo: *id006
- id: edit
  name: Edit
  description: Edit an issue
  params:
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
    validation: *id007
    typeInfo: *id008
  - id: fileContent
    name: File Content
    type: string
    default: ''
    required: true
    description: The text content of the file
    validation: *id009
    typeInfo: *id010
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be written
    validation: *id011
    typeInfo: *id012
  - id: commitMessage
    name: Commit Message
    type: string
    default: ''
    required: true
    description: ''
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
  - id: issueNumber
    name: Issue Number
    type: number
    default: 0
    required: true
    description: The number of the issue edit
    validation: *id018
    typeInfo: *id019
- id: get
  name: Get
  description: Get the data of a single issue
  params:
  - id: workflowId
    name: Workflow
    type: resourceLocator
    default: ''
    required: true
    description: The workflow to dispatch
    placeholder: Select a workflow...
    validation: &id026
      required: true
      displayOptions:
        show:
          resource:
          - workflow
          operation:
          - disable
          - dispatch
          - dispatchAndWait
          - get
          - getUsage
          - enable
    typeInfo: &id027
      type: resourceLocator
      displayName: Workflow
      name: workflowId
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
    validation: *id011
    typeInfo: *id012
  - id: issueNumber
    name: Issue Number
    type: number
    default: 0
    required: true
    description: The issue number to get data for
    validation: *id018
    typeInfo: *id019
  - id: release_id
    name: Release ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id022
      required: true
      displayOptions:
        show:
          resource:
          - release
          operation:
          - get
          - delete
          - update
    typeInfo: &id023
      type: string
      displayName: Release ID
      name: release_id
  - id: pullRequestNumber
    name: PR Number
    type: number
    default: 0
    required: true
    description: The number of the pull request
    validation: *id020
    typeInfo: *id021
  - id: reviewId
    name: Review ID
    type: string
    default: ''
    required: true
    description: ID of the review
    validation: &id024
      required: true
      displayOptions:
        show:
          operation:
          - get
          - update
          resource:
          - review
    typeInfo: &id025
      type: string
      displayName: Review ID
      name: reviewId
- id: lock
  name: Lock
  description: Lock an issue
  params:
  - id: issueNumber
    name: Issue Number
    type: number
    default: 0
    required: true
    description: The issue number to lock
    validation: *id018
    typeInfo: *id019
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
- id: delete
  name: Delete
  description: Delete a file in repository
  params:
  - id: commitMessage
    name: Commit Message
    type: string
    default: ''
    required: true
    description: ''
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
  - id: release_id
    name: Release ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id022
    typeInfo: *id023
- id: list
  name: List
  description: List contents of a folder
  params:
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
- id: getLicense
  name: Get License
  description: Returns the contents of the repository's license file, if one is detected
- id: getProfile
  name: Get Profile
  description: Get the community profile of a repository with metrics, health score,
    description, license, etc
- id: getPullRequests
  name: Get Pull Requests
  description: Returns pull requests of a repository
  params:
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
    description: Max number of results to return. Maximum value is <a href="https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-pull-requests">100</a>.
    validation: *id003
    typeInfo: *id004
- id: listPopularPaths
  name: List Popular Paths
  description: Get the top 10 popular content paths over the last 14 days
- id: listReferrers
  name: List Referrers
  description: Get the top 10 referrering domains over the last 14 days
- id: getUserIssues
  name: Get Issues
  description: Returns the issues assigned to the user
  params:
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
- id: invite
  name: Invite
  description: Invites a user to an organization
  params:
  - id: organization
    name: Organization
    type: string
    default: ''
    required: true
    description: The GitHub organization that the user is being invited to
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - invite
          resource:
          - user
    typeInfo:
      type: string
      displayName: Organization
      name: organization
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email address of the invited user
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - invite
          resource:
          - user
    typeInfo:
      type: string
      displayName: Email
      name: email
- id: getAll
  name: Get Many
  description: Get many repository releases
  params:
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
  - id: pullRequestNumber
    name: PR Number
    type: number
    default: 0
    required: true
    description: The number of the pull request
    validation: *id020
    typeInfo: *id021
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
- id: update
  name: Update
  description: Update a release
  params:
  - id: release_id
    name: Release ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id022
    typeInfo: *id023
  - id: pullRequestNumber
    name: PR Number
    type: number
    default: 0
    required: true
    description: The number of the pull request
    validation: *id020
    typeInfo: *id021
  - id: reviewId
    name: Review ID
    type: string
    default: ''
    required: true
    description: ID of the review
    validation: *id024
    typeInfo: *id025
  - id: body
    name: Body
    type: string
    default: ''
    required: false
    description: The body of the review
    validation: *id005
    typeInfo: *id006
- id: disable
  name: Disable
  description: Disable a workflow
  params:
  - id: workflowId
    name: Workflow
    type: resourceLocator
    default: ''
    required: true
    description: The workflow to dispatch
    placeholder: Select a workflow...
    validation: *id026
    typeInfo: *id027
- id: dispatch
  name: Dispatch
  description: Dispatch a workflow event
  params:
  - id: workflowId
    name: Workflow
    type: resourceLocator
    default: ''
    required: true
    description: The workflow to dispatch
    placeholder: Select a workflow...
    validation: *id026
    typeInfo: *id027
  - id: ref
    name: Ref
    type: string
    default: main
    required: true
    description: The git reference for the workflow dispatch (branch or tag name)
    validation: &id028
      required: true
      displayOptions:
        show:
          resource:
          - workflow
          operation:
          - dispatch
          - dispatchAndWait
    typeInfo: &id029
      type: string
      displayName: Ref
      name: ref
  - id: inputs
    name: Inputs
    type: json
    default: '{}'
    required: false
    description: JSON object with input parameters for the workflow
    validation: &id030
      displayOptions:
        show:
          resource:
          - workflow
          operation:
          - dispatch
          - dispatchAndWait
    typeInfo: &id031
      type: json
      displayName: Inputs
      name: inputs
- id: dispatchAndWait
  name: Dispatch and Wait for Completion
  description: Dispatch a workflow event and wait for a webhook to be called before
    proceeding
  params:
  - id: workflowId
    name: Workflow
    type: resourceLocator
    default: ''
    required: true
    description: The workflow to dispatch
    placeholder: Select a workflow...
    validation: *id026
    typeInfo: *id027
  - id: ref
    name: Ref
    type: string
    default: main
    required: true
    description: The git reference for the workflow dispatch (branch or tag name)
    validation: *id028
    typeInfo: *id029
  - id: inputs
    name: Inputs
    type: json
    default: '{}'
    required: false
    description: JSON object with input parameters for the workflow
    validation: *id030
    typeInfo: *id031
- id: enable
  name: Enable
  description: Enable a workflow
  params:
  - id: workflowId
    name: Workflow
    type: resourceLocator
    default: ''
    required: true
    description: The workflow to dispatch
    placeholder: Select a workflow...
    validation: *id026
    typeInfo: *id027
- id: getUsage
  name: Get Usage
  description: Get the usage of a workflow
  params:
  - id: workflowId
    name: Workflow
    type: resourceLocator
    default: ''
    required: true
    description: The workflow to dispatch
    placeholder: Select a workflow...
    validation: *id026
    typeInfo: *id027
examples:
- name: Get Organization Repositories
  parameters:
    resource: organization
    operation: getRepositories
    owner:
      __rl: true
      value: testorg
      mode: name
    returnAll: true
  workflow: Github Organization getRepositories Test Workflow
- name: Get User Issues Filtered
  parameters:
    resource: user
    operation: getUserIssues
    returnAll: true
    getUserIssuesFilters:
      state: closed
      labels: enhancement
  workflow: Github User getUserIssues Filtered Test Workflow
- name: Get Repository Issues Limited
  parameters:
    resource: repository
    operation: getIssues
    owner:
      __rl: true
      value: testowner
      mode: name
    repository:
      __rl: true
      value: testrepo
      mode: name
    returnAll: false
    limit: 1
    getRepositoryIssuesFilters: {}
  workflow: Github Repository getIssues Limit Test Workflow
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - User-Agent
  query_params: []
ui_elements:
  notices:
  - name: webhookNotice
    text: Your execution will pause until a webhook is called. This URL will be generated
      at runtime and passed to your Github workflow as a resumeUrl input.
    conditions:
      show:
        resource:
        - workflow
        operation:
        - dispatchAndWait
  tooltips: []
  placeholders:
  - field: owner
    text: Select an owner...
  - field: repository
    text: Select an Repository...
  - field: workflowId
    text: Select a workflow...
  - field: filePath
    text: docs/README.md
  - field: filePath
    text: docs/
  - field: additionalParameters
    text: Add Parameter
  - field: additionalParameters
    text: Add Parameter
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be written
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/github.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GitHub Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "getRepositories",
        "create",
        "createComment",
        "edit",
        "get",
        "lock",
        "delete",
        "list",
        "getIssues",
        "getLicense",
        "getProfile",
        "getPullRequests",
        "listPopularPaths",
        "listReferrers",
        "getUserIssues",
        "invite",
        "getAll",
        "update",
        "disable",
        "dispatch",
        "dispatchAndWait",
        "enable",
        "getUsage"
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
            "organization",
            "release",
            "repository",
            "review",
            "user",
            "workflow"
          ],
          "default": "issue"
        },
        "operation": {
          "description": "Disable a workflow",
          "type": "string",
          "enum": [
            "disable",
            "dispatch",
            "dispatchAndWait",
            "enable",
            "get",
            "getUsage",
            "list"
          ],
          "default": "dispatch"
        },
        "owner": {
          "description": "",
          "type": "string",
          "examples": [
            "Select an owner..."
          ]
        },
        "repository": {
          "description": "",
          "type": "string",
          "examples": [
            "Select an Repository..."
          ]
        },
        "workflowId": {
          "description": "The workflow to dispatch",
          "type": "string",
          "examples": [
            "Select a workflow..."
          ]
        },
        "ref": {
          "description": "The git reference for the workflow dispatch (branch or tag name)",
          "type": "string",
          "default": "main"
        },
        "inputs": {
          "description": "JSON object with input parameters for the workflow",
          "type": "string",
          "default": "{}"
        },
        "filePath": {
          "description": "The path of the folder to list",
          "type": "string",
          "default": "",
          "examples": [
            "docs/"
          ]
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
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "commitMessage": {
          "description": "",
          "type": "string",
          "default": ""
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
        "title": {
          "description": "The title of the issue",
          "type": "string",
          "default": ""
        },
        "body": {
          "description": "The body of the review",
          "type": "string",
          "default": ""
        },
        "labels": {
          "description": "Label to add to issue",
          "type": "string",
          "default": ""
        },
        "assignees": {
          "description": "User to assign issue too",
          "type": "string",
          "default": ""
        },
        "issueNumber": {
          "description": "The issue number to lock",
          "type": "number",
          "default": 0
        },
        "editFields": {
          "description": "User to assign issue to",
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
          "description": "The SHA of the commit that needs a review, if different from the latest",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "release_id": {
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
        "getRepositoryIssuesFilters": {
          "description": "Return only issues which are assigned to a specific user",
          "type": "string",
          "default": {}
        },
        "getRepositoryPullRequestsFilters": {
          "description": "Returns pull requests with any state",
          "type": "string",
          "default": {}
        },
        "pullRequestNumber": {
          "description": "The number of the pull request to review",
          "type": "number",
          "default": 0
        },
        "reviewId": {
          "description": "ID of the review",
          "type": "string",
          "default": ""
        },
        "event": {
          "description": "Approve the pull request",
          "type": "string",
          "enum": [
            "approve",
            "requestChanges",
            "comment",
            "pending"
          ],
          "default": "approve"
        },
        "organization": {
          "description": "The GitHub organization that the user is being invited to",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "The email address of the invited user",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "getUserIssuesFilters": {
          "description": "Return only issues in which a specific user was mentioned",
          "type": "string",
          "default": {}
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
    "version": [
      "1",
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "githubApi",
      "required": true
    },
    {
      "name": "githubOAuth2Api",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Get Organization Repositories",
      "value": {
        "resource": "organization",
        "operation": "getRepositories",
        "owner": {
          "__rl": true,
          "value": "testorg",
          "mode": "name"
        },
        "returnAll": true
      }
    },
    {
      "description": "Get User Issues Filtered",
      "value": {
        "resource": "user",
        "operation": "getUserIssues",
        "returnAll": true,
        "getUserIssuesFilters": {
          "state": "closed",
          "labels": "enhancement"
        }
      }
    },
    {
      "description": "Get Repository Issues Limited",
      "value": {
        "resource": "repository",
        "operation": "getIssues",
        "owner": {
          "__rl": true,
          "value": "testowner",
          "mode": "name"
        },
        "repository": {
          "__rl": true,
          "value": "testrepo",
          "mode": "name"
        },
        "returnAll": false,
        "limit": 1,
        "getRepositoryIssuesFilters": {}
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
