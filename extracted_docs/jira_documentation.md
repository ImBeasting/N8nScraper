---
title: "Node: Jira Software"
slug: "node-jira"
version: "1"
updated: "2026-01-08"
summary: "Consume Jira Software API"
node_type: "regular"
group: "['output']"
---

# Node: Jira Software

**Purpose.** Consume Jira Software API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:jira.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **jiraSoftwareCloudApi**: N/A
- **jiraSoftwareServerApi**: N/A
- **jiraSoftwareServerPatApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `jiraSoftwareCloudApi` | ✓ | {'show': {'jiraVersion': ['cloud']}} |
| `jiraSoftwareServerApi` | ✓ | {'show': {'jiraVersion': ['server']}} |
| `jiraSoftwareServerPatApi` | ✓ | {'show': {'jiraVersion': ['serverPat']}} |

---

## API Patterns

**Headers Used:** no-check, X-Atlassian-Token, Content-Type

---

## Operations

### Issue Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Changelog | `changelog` | Get issue changelog |
| Create | `create` | Create a new issue |
| Delete | `delete` | Delete an issue |
| Get | `get` | Get an issue |
| Get Many | `getAll` | Get many issues |
| Notify | `notify` | Create an email notification for an issue and add it to the mail queue |
| Status | `transitions` | Return either all transitions or a transition that can be performed by the user on an issue, based on the issue's status |
| Update | `update` | Update an issue |

### Issueattachment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add attachment to issue |
| Get | `get` | Get an attachment |
| Get Many | `getAll` | Get many attachments |
| Remove | `remove` | Remove an attachment |

### Issuecomment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add comment to issue |
| Get | `get` | Get a comment |
| Get Many | `getAll` | Get many comments |
| Remove | `remove` | Remove a comment |
| Update | `update` | Update a comment |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new user |
| Delete | `delete` | Delete a user |
| Get | `get` | Retrieve a user |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | issue | ✗ | Creates an issue or, where the option to create subtasks is enabled in Jira, a subtask |  |

**Resource options:**

* **Issue** (`issue`) - Creates an issue or, where the option to create subtasks is enabled in Jira, a subtask
* **Issue Attachment** (`issueAttachment`) - Add, remove, and get an attachment from an issue
* **Issue Comment** (`issueComment`) - Get, create, update, and delete a comment from an issue
* **User** (`user`) - Get, create and delete a user

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Get issue changelog |  |

**Operation options:**

* **Changelog** (`changelog`) - Get issue changelog
* **Create** (`create`) - Create a new issue
* **Delete** (`delete`) - Delete an issue
* **Get** (`get`) - Get an issue
* **Get Many** (`getAll`) - Get many issues
* **Notify** (`notify`) - Create an email notification for an issue and add it to the mail queue
* **Status** (`transitions`) - Return either all transitions or a transition that can be performed by the user on an issue, based on the issue's status
* **Update** (`update`) - Update an issue

---

### Changelog parameters (`changelog`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Key | `issueKey` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Project | `project` | resourceLocator |  | ✓ | e.g. Select a Project... |  |
| Issue Type | `issueType` | resourceLocator |  | ✓ | e.g. Select an Issue Type... |  |
| Summary | `summary` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee | `assignee` | resourceLocator |  |  |
| Description | `description` | string |  |  |
| Component Names or IDs | `componentIds` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Value of the field to set |
| Label Names or IDs | `labels` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Labels | `serverLabels` | string | [] |  |
| Parent Issue Key | `parentIssueKey` | string |  |  |
| Priority | `priority` | resourceLocator |  |  |
| Reporter | `reporter` | resourceLocator |  |  |
| Update History | `updateHistory` | boolean | False | Whether the project in which the issue is created is added to the user's Recently viewed project list, as shown under Projects in Jira |

</details>

| Username | `username` | string |  | ✓ |  |  |
| Email Address | `emailAddress` | string |  | ✓ |  | email |
| Display Name | `displayName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Password for the user. If a password is not set, a random password is generated. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Password | `password` | string |  | Password for the user. If a password is not set, a random password is generated. |
| Notification | `notification` | boolean | False | Whether to send the user an email confirmation that they have been added to Jira |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Key | `issueKey` | string |  | ✓ |  |  |
| Delete Subtasks | `deleteSubtasks` | boolean | False | ✓ |  |  |
| Account ID | `accountId` | string |  | ✗ | Account ID of the user to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Key | `issueKey` | string |  | ✓ |  |  |
| Simplify | `simplifyOutput` | boolean | False | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | <p>Use expand to include additional information about the issues in the response. This parameter accepts a comma-separated list. Expand options include:
				<ul>
					<li><code>renderedFields</code> Returns field values rendered in HTML format.</li>
					<li><code>names</code> Returns the display name of each field.</li>
					<li><code>schema</code> Returns the schema describing a field type.</li>
					<li><code>transitions</code> Returns all possible transitions for the issue.</li>
					<li><code>editmeta</code> Returns information about how each field can be edited.</li>
					<li><code>changelog</code> Returns a list of recent updates to an issue, sorted by date, starting from the most recent.</li>
					<li><code>versionedRepresentations</code> Returns a JSON array for each version of a field's value, with the highest number representing the most recent version. Note: When included in the request, the fields parameter is ignored.</li>
				</ul> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Expand | `expand` | string |  | <p>Use expand to include additional information about the issues in the response. This parameter accepts a comma-separated list. Expand options include:
				<ul>
					<li><code>renderedFields</code> Returns field values rendered in HTML format.</li>
					<li><code>names</code> Returns the display name of each field.</li>
					<li><code>schema</code> Returns the schema describing a field type.</li>
					<li><code>transitions</code> Returns all possible transitions for the issue.</li>
					<li><code>editmeta</code> Returns information about how each field can be edited.</li>
					<li><code>changelog</code> Returns a list of recent updates to an issue, sorted by date, starting from the most recent.</li>
					<li><code>versionedRepresentations</code> Returns a JSON array for each version of a field's value, with the highest number representing the most recent version. Note: When included in the request, the fields parameter is ignored.</li>
				</ul> |
| Fields | `fields` | string |  | A list of fields to return for the issue. This parameter accepts a comma-separated list. Use it to retrieve a subset of fields. Allowed values: <code>*all</code> Returns all fields. <code>*navigable</code> Returns navigable fields. Any issue field, prefixed with a minus to exclude. |
| Fields By Key | `fieldsByKey` | boolean | False | Whether fields in fields are referenced by keys rather than IDs. This parameter is useful where fields have been added by a connect app and a field's key may differ from its ID. |
| Properties | `properties` | string |  | A list of issue properties to return for the issue. This parameter accepts a comma-separated list. Allowed values: <code>*all</code> Returns all issue properties. Any issue property key, prefixed with a minus to exclude. Examples: <code>*all</code> Returns all properties. <code>*all</code>,-prop1 Returns all properties except prop1. <code>prop1,prop2</code> Returns prop1 and prop2 properties. This parameter may be specified multiple times. For example, properties=prop1,prop2& properties=prop3. |
| Update History | `updateHistory` | boolean | False | Whether the project in which the issue is created is added to the user's Recently viewed project list, as shown under Projects in Jira. This also populates the JQL issues search lastViewed field. |

</details>

| Attachment ID | `attachmentId` | string |  | ✓ | The ID of the attachment |  |
| Download | `download` | boolean | False | ✓ |  |  |
| Put Output File in Field | `binaryProperty` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| Issue Key | `issueKey` | string |  | ✓ | The ID or key of the issue |  |
| Comment ID | `commentId` | string |  | ✓ | The ID of the comment |  |
| Options | `options` | collection | {} | ✗ | Use expand to include additional information about comments in the response. This parameter accepts Rendered Body, which returns the comment body rendered in HTML. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Expand | `expand` | options |  | Use expand to include additional information about comments in the response. This parameter accepts Rendered Body, which returns the comment body rendered in HTML. |

</details>

| Account ID | `accountId` | string |  | ✗ | Account ID of the user to retrieve |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Include more information about the user | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Expand | `expand` | multiOptions | [] | Include more information about the user |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Returns a list of recent updates to an issue, sorted by date, starting from the most recent | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Expand | `expand` | multiOptions | [] | Returns a list of recent updates to an issue, sorted by date, starting from the most recent |
| Fields | `fields` | string | *navigable | A list of fields to return for each issue, use it to retrieve a subset of fields. This parameter accepts a comma-separated list. Expand options include: <code>*all</code> Returns all fields. <code>*navigable</code> Returns navigable fields. Any issue field, prefixed with a minus to exclude. |
| Fields By Key | `fieldsByKey` | boolean | False | Whether fields in fields are referenced by keys rather than IDs. This parameter is useful where fields have been added by a connect app and a field's key may differ from its ID. |
| JQL | `jql` | string |  | A JQL expression |

</details>

| Issue Key | `issueKey` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Download | `download` | boolean | False | ✓ |  |  |
| Put Output File in Field | `binaryProperty` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| Issue Key | `issueKey` | string |  | ✓ | The ID or key of the issue |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Use expand to include additional information about comments in the response. This parameter accepts Rendered Body, which returns the comment body rendered in HTML. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Expand | `expand` | options | renderedBody | Use expand to include additional information about comments in the response. This parameter accepts Rendered Body, which returns the comment body rendered in HTML. |
| Order By | `orderBy` | options | +created | Order comments by the created date |

</details>


### Notify parameters (`notify`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Key | `issueKey` | string |  | ✓ |  |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The HTML body of the email notification for the issue | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| HTML Body | `htmlBody` | string |  | The HTML body of the email notification for the issue |
| Subject | `subject` | string |  | The subject of the email notification for the issue. If this is not specified, then the subject is set to the issue key and summary. |
| Text Body | `textBody` | string |  | The subject of the email notification for the issue. If this is not specified, then the subject is set to the issue key and summary. |

</details>

| Notification Recipients | `notificationRecipientsUi` | fixedCollection | {} | ✗ | The recipients of the email notification for the issue | e.g. Add Recipients |  |

<details>
<summary><strong>Notification Recipients sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Recipients | `notificationRecipientsValues` |  |  |  |

</details>

| Notification Recipients | `notificationRecipientsJson` | json |  | ✗ | The recipients of the email notification for the issue |  |
| Notification Recipients Restrictions | `notificationRecipientsRestrictionsUi` | fixedCollection | {} | ✗ | Restricts the notifications to users with the specified permissions | e.g. Add Recipients Restriction |  |

<details>
<summary><strong>Notification Recipients Restrictions sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Recipients Restrictions | `notificationRecipientsRestrictionsValues` |  |  |  |

</details>

| Notification Recipients Restrictions | `notificationRecipientsRestrictionsJson` | json |  | ✗ | Restricts the notifications to users with the specified permissions |  |

### Status parameters (`transitions`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Key | `issueKey` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Use expand to include additional information about transitions in the response. This parameter accepts transitions.fields, which returns information about the fields in the transition screen for each transition. Fields hidden from the screen are not returned. Use this information to populate the fields and update fields in Transition issue. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Expand | `expand` | string |  | Use expand to include additional information about transitions in the response. This parameter accepts transitions.fields, which returns information about the fields in the transition screen for each transition. Fields hidden from the screen are not returned. Use this information to populate the fields and update fields in Transition issue. |
| Transition ID | `transitionId` | string |  | The ID of the transition |
| Skip Remote Only Condition | `skipRemoteOnlyCondition` | boolean | False | Whether transitions with the condition Hide From User Condition are included in the response |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Key | `issueKey` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Value of the field to set | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee | `assignee` | resourceLocator |  |  |
| Description | `description` | string |  |  |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Value of the field to set |
| Issue Type | `issueType` | string |  | Issue Types |
| Label Names or IDs | `labels` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Labels | `serverLabels` | string | [] |  |
| Parent Issue Key | `parentIssueKey` | string |  |  |
| Priority | `priority` | resourceLocator |  |  |
| Reporter | `reporter` | resourceLocator |  |  |
| Summary | `summary` | string |  |  |
| Status | `statusId` | resourceLocator |  |  |

</details>

| Issue Key | `issueKey` | string |  | ✓ | The Issue Comment key |  |
| Comment ID | `commentId` | string |  | ✓ | The ID of the comment |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Comment | `comment` | string |  | ✗ | Comment's text |  |
| Document Format (JSON) | `commentJson` | json |  | ✗ | The Atlassian Document Format (ADF). Online builder can be found <a href="https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/">here</a>. |  |
| Options | `options` | collection | {} | ✗ | Use expand to include additional information about comments in the response. This parameter accepts Rendered Body, which returns the comment body rendered in HTML. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Expand | `expand` | options | renderedBody | Use expand to include additional information about comments in the response. This parameter accepts Rendered Body, which returns the comment body rendered in HTML. |
| Use Wiki Markup | `wikiMarkup` | boolean | False | Whether to enable parsing of wikiformatting for this comment. Default is false. |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue Key | `issueKey` | string |  | ✓ |  |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be written |  |
| Issue Key | `issueKey` | string |  | ✓ | issueComment Key |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Comment | `comment` | string |  | ✗ | Comment's text |  |
| Document Format (JSON) | `commentJson` | json |  | ✗ | The Atlassian Document Format (ADF). Online builder can be found <a href="https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/">here</a>. |  |
| Options | `options` | collection | {} | ✗ | Use expand to include additional information about comments in the response. This parameter accepts Rendered Body, which returns the comment body rendered in HTML. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Expand | `expand` | options | [] | Use expand to include additional information about comments in the response. This parameter accepts Rendered Body, which returns the comment body rendered in HTML. |
| Use Wiki Markup | `wikiMarkup` | boolean | False | Whether to enable parsing of wikiformatting for this comment. Default is false. |

</details>


### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Attachment ID | `attachmentId` | string |  | ✓ | The ID of the attachment |  |
| Issue Key | `issueKey` | string |  | ✓ | The ID or key of the issue |  |
| Comment ID | `commentId` | string |  | ✓ | The ID of the comment |  |

---

## Load Options Methods

- `getLabels`
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
* Categories: Development, Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: jira
displayName: Jira Software
description: Consume Jira Software API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: jiraSoftwareCloudApi
  required: true
- name: jiraSoftwareServerApi
  required: true
- name: jiraSoftwareServerPatApi
  required: true
operations:
- id: changelog
  name: Changelog
  description: Get issue changelog
  params:
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - issueComment
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: Issue Key
      name: issueKey
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
          - issueComment
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
          - issueComment
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
        maxValue: 100
- id: create
  name: Create
  description: Create a new issue
  params:
  - id: project
    name: Project
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select a Project...
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - create
    typeInfo:
      type: resourceLocator
      displayName: Project
      name: project
  - id: issueType
    name: Issue Type
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select an Issue Type...
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - create
    typeInfo:
      type: resourceLocator
      displayName: Issue Type
      name: issueType
  - id: summary
    name: Summary
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - create
    typeInfo:
      type: string
      displayName: Summary
      name: summary
  - id: username
    name: Username
    type: string
    default: ''
    required: true
    description: ''
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
      displayName: Username
      name: username
  - id: emailAddress
    name: Email Address
    type: string
    default: ''
    required: true
    description: ''
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
      displayName: Email Address
      name: emailAddress
  - id: displayName
    name: Display Name
    type: string
    default: ''
    required: true
    description: ''
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
      displayName: Display Name
      name: displayName
- id: delete
  name: Delete
  description: Delete an issue
  params:
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: deleteSubtasks
    name: Delete Subtasks
    type: boolean
    default: false
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - delete
    typeInfo:
      type: boolean
      displayName: Delete Subtasks
      name: deleteSubtasks
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: false
    description: Account ID of the user to delete
    validation: &id003
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
    typeInfo: &id004
      type: string
      displayName: Account ID
      name: accountId
- id: get
  name: Get
  description: Get an issue
  params:
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: simplifyOutput
    name: Simplify
    type: boolean
    default: false
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation:
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - get
    typeInfo:
      type: boolean
      displayName: Simplify
      name: simplifyOutput
  - id: attachmentId
    name: Attachment ID
    type: string
    default: ''
    required: true
    description: The ID of the attachment
    validation: &id021
      required: true
      displayOptions:
        show:
          resource:
          - issueAttachment
          operation:
          - remove
    typeInfo: &id022
      type: string
      displayName: Attachment ID
      name: attachmentId
  - id: download
    name: Download
    type: boolean
    default: false
    required: true
    description: ''
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - issueAttachment
          operation:
          - getAll
    typeInfo: &id010
      type: boolean
      displayName: Download
      name: download
  - id: binaryProperty
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - issueAttachment
          operation:
          - getAll
          download:
          - true
    typeInfo: &id012
      type: string
      displayName: Put Output File in Field
      name: binaryProperty
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: The ID or key of the issue
    validation: *id001
    typeInfo: *id002
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: The ID of the comment
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - issueComment
          operation:
          - update
    typeInfo: &id014
      type: string
      displayName: Comment ID
      name: commentId
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: false
    description: Account ID of the user to retrieve
    validation: *id003
    typeInfo: *id004
- id: getAll
  name: Get Many
  description: Get many issues
  params:
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
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: ''
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
  - id: download
    name: Download
    type: boolean
    default: false
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: binaryProperty
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: *id011
    typeInfo: *id012
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: The ID or key of the issue
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: notify
  name: Notify
  description: Create an email notification for an issue and add it to the mail queue
  params:
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id015
      displayOptions:
        show:
          resource:
          - issueComment
          operation:
          - update
    typeInfo: &id016
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: notificationRecipientsUi
    name: Notification Recipients
    type: fixedCollection
    default: {}
    required: false
    description: The recipients of the email notification for the issue
    placeholder: Add Recipients
    validation:
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - notify
          jsonParameters:
          - false
    typeInfo:
      type: fixedCollection
      displayName: Notification Recipients
      name: notificationRecipientsUi
      typeOptions:
        multipleValues: false
      subProperties:
      - name: notificationRecipientsValues
        displayName: Recipients
        values:
        - displayName: Reporter
          name: reporter
          type: boolean
          description: Whether the notification should be sent to the issue's reporter
          default: false
        - displayName: Assignee
          name: assignee
          type: boolean
          description: Whether the notification should be sent to the issue's assignees
          default: false
        - displayName: Watchers
          name: watchers
          type: boolean
          description: Whether the notification should be sent to the issue's assignees
          default: false
        - displayName: Voters
          name: voters
          type: boolean
          description: Whether the notification should be sent to the issue's voters
          default: false
        - displayName: User Names or IDs
          name: users
          type: multiOptions
          description: List of users to receive the notification. Choose from the
            list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: []
          typeOptions:
            loadOptionsMethod: getUsers
        - displayName: Group Names or IDs
          name: groups
          type: multiOptions
          description: List of groups to receive the notification. Choose from the
            list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: []
          typeOptions:
            loadOptionsMethod: getGroups
  - id: notificationRecipientsJson
    name: Notification Recipients
    type: json
    default: ''
    required: false
    description: The recipients of the email notification for the issue
    validation:
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - notify
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Notification Recipients
      name: notificationRecipientsJson
      typeOptions:
        alwaysOpenEditWindow: true
  - id: notificationRecipientsRestrictionsUi
    name: Notification Recipients Restrictions
    type: fixedCollection
    default: {}
    required: false
    description: Restricts the notifications to users with the specified permissions
    placeholder: Add Recipients Restriction
    validation:
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - notify
          jsonParameters:
          - false
    typeInfo:
      type: fixedCollection
      displayName: Notification Recipients Restrictions
      name: notificationRecipientsRestrictionsUi
      typeOptions:
        multipleValues: false
      subProperties:
      - name: notificationRecipientsRestrictionsValues
        displayName: Recipients Restrictions
        values:
        - displayName: User Names or IDs
          name: users
          type: multiOptions
          description: List of users to receive the notification. Choose from the
            list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: []
          typeOptions:
            loadOptionsMethod: getUsers
        - displayName: Group Names or IDs
          name: groups
          type: multiOptions
          description: List of groups to receive the notification. Choose from the
            list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: []
          typeOptions:
            loadOptionsMethod: getGroups
  - id: notificationRecipientsRestrictionsJson
    name: Notification Recipients Restrictions
    type: json
    default: ''
    required: false
    description: Restricts the notifications to users with the specified permissions
    validation:
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - notify
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Notification Recipients Restrictions
      name: notificationRecipientsRestrictionsJson
      typeOptions:
        alwaysOpenEditWindow: true
- id: transitions
  name: Status
  description: Return either all transitions or a transition that can be performed
    by the user on an issue, based on the issue's status
  params:
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
- id: update
  name: Update
  description: Update an issue
  params:
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: The Issue Comment key
    validation: *id001
    typeInfo: *id002
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: The ID of the comment
    validation: *id013
    typeInfo: *id014
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: comment
    name: Comment
    type: string
    default: ''
    required: false
    description: Comment's text
    validation: &id017
      displayOptions:
        show:
          resource:
          - issueComment
          operation:
          - update
          jsonParameters:
          - false
    typeInfo: &id018
      type: string
      displayName: Comment
      name: comment
  - id: commentJson
    name: Document Format (JSON)
    type: json
    default: ''
    required: false
    description: The Atlassian Document Format (ADF). Online builder can be found
      <a href="https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/">here</a>.
    validation: &id019
      displayOptions:
        show:
          resource:
          - issueComment
          operation:
          - update
          jsonParameters:
          - true
    typeInfo: &id020
      type: json
      displayName: Document Format (JSON)
      name: commentJson
- id: add
  name: Add
  description: Add attachment to issue
  params:
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be written
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - issueAttachment
          operation:
          - add
    typeInfo:
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: issueComment Key
    validation: *id001
    typeInfo: *id002
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: comment
    name: Comment
    type: string
    default: ''
    required: false
    description: Comment's text
    validation: *id017
    typeInfo: *id018
  - id: commentJson
    name: Document Format (JSON)
    type: json
    default: ''
    required: false
    description: The Atlassian Document Format (ADF). Online builder can be found
      <a href="https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/">here</a>.
    validation: *id019
    typeInfo: *id020
- id: remove
  name: Remove
  description: Remove an attachment
  params:
  - id: attachmentId
    name: Attachment ID
    type: string
    default: ''
    required: true
    description: The ID of the attachment
    validation: *id021
    typeInfo: *id022
  - id: issueKey
    name: Issue Key
    type: string
    default: ''
    required: true
    description: The ID or key of the issue
    validation: *id001
    typeInfo: *id002
  - id: commentId
    name: Comment ID
    type: string
    default: ''
    required: true
    description: The ID of the comment
    validation: *id013
    typeInfo: *id014
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - no-check
  - X-Atlassian-Token
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: project
    text: Select a Project...
  - field: issueType
    text: Select an Issue Type...
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: notificationRecipientsUi
    text: Add Recipients
  - field: notificationRecipientsRestrictionsUi
    text: Add Recipients Restriction
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add option
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be written
  - field: binaryProperty
    text: The name of the output binary field to put the file in
  - field: binaryProperty
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
  "$id": "https://n8n.io/schemas/nodes/jira.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Jira Software Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "changelog",
        "create",
        "delete",
        "get",
        "getAll",
        "notify",
        "transitions",
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
        "jiraVersion": {
          "description": "",
          "type": "string",
          "enum": [
            "cloud",
            "server",
            "serverPat"
          ],
          "default": "cloud"
        },
        "resource": {
          "description": "Creates an issue or, where the option to create subtasks is enabled in Jira, a subtask",
          "type": "string",
          "enum": [
            "issue",
            "issueAttachment",
            "issueComment",
            "user"
          ],
          "default": "issue"
        },
        "operation": {
          "description": "Create a new user",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get"
          ],
          "default": "create"
        },
        "project": {
          "description": "",
          "type": "string",
          "examples": [
            "Select a Project..."
          ]
        },
        "issueType": {
          "description": "",
          "type": "string",
          "examples": [
            "Select an Issue Type..."
          ]
        },
        "summary": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Include more information about the user",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "issueKey": {
          "description": "The Issue Comment key",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Value of the field to set",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "deleteSubtasks": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "simplifyOutput": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": false
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
        "options": {
          "description": "Use expand to include additional information about comments in the response. This parameter accepts Rendered Body, which returns the comment body rendered in HTML.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "notificationRecipientsUi": {
          "description": "The recipients of the email notification for the issue",
          "type": "string",
          "default": {},
          "examples": [
            "Add Recipients"
          ]
        },
        "notificationRecipientsJson": {
          "description": "The recipients of the email notification for the issue",
          "type": "string",
          "default": ""
        },
        "notificationRecipientsRestrictionsUi": {
          "description": "Restricts the notifications to users with the specified permissions",
          "type": "string",
          "default": {},
          "examples": [
            "Add Recipients Restriction"
          ]
        },
        "notificationRecipientsRestrictionsJson": {
          "description": "Restricts the notifications to users with the specified permissions",
          "type": "string",
          "default": ""
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "attachmentId": {
          "description": "The ID of the attachment",
          "type": "string",
          "default": ""
        },
        "download": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "binaryProperty": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "comment": {
          "description": "Comment's text",
          "type": "string",
          "default": ""
        },
        "commentJson": {
          "description": "The Atlassian Document Format (ADF). Online builder can be found <a href=\"https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/\">here</a>.",
          "type": "string",
          "default": ""
        },
        "commentId": {
          "description": "The ID of the comment",
          "type": "string",
          "default": ""
        },
        "username": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "emailAddress": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "email"
        },
        "displayName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "accountId": {
          "description": "Account ID of the user to retrieve",
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
      "name": "jiraSoftwareCloudApi",
      "required": true
    },
    {
      "name": "jiraSoftwareServerApi",
      "required": true
    },
    {
      "name": "jiraSoftwareServerPatApi",
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
