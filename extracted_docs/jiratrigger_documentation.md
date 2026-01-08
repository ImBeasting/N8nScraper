---
title: "Node: Jira Trigger"
slug: "node-jiratrigger"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Starts the workflow when Jira events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Jira Trigger

**Purpose.** Starts the workflow when Jira events occur


---

## Node Details

- **Icon:** `file:jira.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **jiraSoftwareCloudApi**: N/A
- **jiraSoftwareServerApi**: N/A
- **jiraSoftwareServerPatApi**: N/A
- **httpQueryAuth**: N/A
- **httpQueryAuth**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

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
| `httpQueryAuth` | Optional | {'show': {'authenticateWebhook': [True]}} |
| `httpQueryAuth` | Optional | {'show': {'incomingAuthentication': ['queryAuth']}} |

---

## API Patterns

**Headers Used:** no-check, X-Atlassian-Token, Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Jira Version | `jiraVersion` | options | cloud | ✗ |  |  |

**Jira Version options:**

* **Cloud** (`cloud`)
* **Server (Self Hosted)** (`server`)
* **Server (Pat) (Self Hosted)** (`serverPat`)

| Authenticate Incoming Webhook | `authenticateWebhook` | boolean | False | ✗ | Whether authentication should be activated for the incoming webhooks (makes it more secure) |  |
| Authenticate Webhook With | `incomingAuthentication` | options | none | ✗ | If authentication should be activated for the webhook (makes it more secure) |  |

**Authenticate Webhook With options:**

* **Query Auth** (`queryAuth`)
* **None** (`none`)

| Events | `events` | multiOptions | [] | ✓ | The events to listen to |  |

**Events options:**

* ***** (`*`)
* **Board Configuration Changed** (`board_configuration_changed`)
* **Board Created** (`board_created`)
* **Board Deleted** (`board_deleted`)
* **Board Updated** (`board_updated`)
* **Comment Created** (`comment_created`)
* **Comment Deleted** (`comment_deleted`)
* **Comment Updated** (`comment_updated`)
* **Issue Created** (`jira:issue_created`)
* **Issue Deleted** (`jira:issue_deleted`)
* **Issue Link Created** (`issuelink_created`)
* **Issue Link Deleted** (`issuelink_deleted`)
* **Issue Updated** (`jira:issue_updated`)
* **Option Attachments Changed** (`option_attachments_changed`)
* **Option Issue Links Changed** (`option_issuelinks_changed`)
* **Option Subtasks Changed** (`option_subtasks_changed`)
* **Option Timetracking Changed** (`option_timetracking_changed`)
* **Option Unassigned Issues Changed** (`option_unassigned_issues_changed`)
* **Option Voting Changed** (`option_voting_changed`)
* **Option Watching Changed** (`option_watching_changed`)
* **Project Created** (`project_created`)
* **Project Deleted** (`project_deleted`)
* **Project Updated** (`project_updated`)
* **Sprint Closed** (`sprint_closed`)
* **Sprint Created** (`sprint_created`)
* **Sprint Deleted** (`sprint_deleted`)
* **Sprint Started** (`sprint_started`)
* **Sprint Updated** (`sprint_updated`)
* **User Created** (`user_created`)
* **User Deleted** (`user_deleted`)
* **User Updated** (`user_updated`)
* **Version Created** (`jira:version_created`)
* **Version Deleted** (`jira:version_deleted`)
* **Version Moved** (`jira:version_moved`)
* **Version Released** (`jira:version_released`)
* **Version Unreleased** (`jira:version_unreleased`)
* **Version Updated** (`jira:version_updated`)
* **Worklog Created** (`worklog_created`)
* **Worklog Deleted** (`worklog_deleted`)
* **Worklog Updated** (`worklog_updated`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether a request with empty body will be sent to the URL. Leave unchecked if you want to receive JSON. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Body | `excludeBody` | boolean | False | Whether a request with empty body will be sent to the URL. Leave unchecked if you want to receive JSON. |
| Filter | `filter` | string |  | You can specify a JQL query to send only events triggered by matching issues. The JQL filter only applies to events under the Issue and Comment columns. |
| Include Fields | `includeFields` | multiOptions | [] |  |

</details>


---

## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |

---

## Notes & Caveats

* This node is part of n8n-nodes-base
* Categories: Development, Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: jiraTrigger
displayName: Jira Trigger
description: Starts the workflow when Jira events occur
version:
- '1'
- '1.1'
nodeType: trigger
group:
- trigger
credentials:
- name: jiraSoftwareCloudApi
  required: true
- name: jiraSoftwareServerApi
  required: true
- name: jiraSoftwareServerPatApi
  required: true
- name: httpQueryAuth
  required: false
- name: httpQueryAuth
  required: false
params:
- id: jiraVersion
  name: Jira Version
  type: options
  default: cloud
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Jira Version
    name: jiraVersion
    possibleValues:
    - value: cloud
      name: Cloud
      description: ''
    - value: server
      name: Server (Self Hosted)
      description: ''
    - value: serverPat
      name: Server (Pat) (Self Hosted)
      description: ''
- id: authenticateWebhook
  name: Authenticate Incoming Webhook
  type: boolean
  default: false
  required: false
  description: Whether authentication should be activated for the incoming webhooks
    (makes it more secure)
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: boolean
    displayName: Authenticate Incoming Webhook
    name: authenticateWebhook
- id: incomingAuthentication
  name: Authenticate Webhook With
  type: options
  default: none
  required: false
  description: If authentication should be activated for the webhook (makes it more
    secure)
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: options
    displayName: Authenticate Webhook With
    name: incomingAuthentication
    possibleValues:
    - value: queryAuth
      name: Query Auth
      description: ''
    - value: none
      name: None
      description: ''
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: The events to listen to
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: '*'
      name: '*'
      description: ''
    - value: board_configuration_changed
      name: Board Configuration Changed
      description: ''
    - value: board_created
      name: Board Created
      description: ''
    - value: board_deleted
      name: Board Deleted
      description: ''
    - value: board_updated
      name: Board Updated
      description: ''
    - value: comment_created
      name: Comment Created
      description: ''
    - value: comment_deleted
      name: Comment Deleted
      description: ''
    - value: comment_updated
      name: Comment Updated
      description: ''
    - value: jira:issue_created
      name: Issue Created
      description: ''
    - value: jira:issue_deleted
      name: Issue Deleted
      description: ''
    - value: issuelink_created
      name: Issue Link Created
      description: ''
    - value: issuelink_deleted
      name: Issue Link Deleted
      description: ''
    - value: jira:issue_updated
      name: Issue Updated
      description: ''
    - value: option_attachments_changed
      name: Option Attachments Changed
      description: ''
    - value: option_issuelinks_changed
      name: Option Issue Links Changed
      description: ''
    - value: option_subtasks_changed
      name: Option Subtasks Changed
      description: ''
    - value: option_timetracking_changed
      name: Option Timetracking Changed
      description: ''
    - value: option_unassigned_issues_changed
      name: Option Unassigned Issues Changed
      description: ''
    - value: option_voting_changed
      name: Option Voting Changed
      description: ''
    - value: option_watching_changed
      name: Option Watching Changed
      description: ''
    - value: project_created
      name: Project Created
      description: ''
    - value: project_deleted
      name: Project Deleted
      description: ''
    - value: project_updated
      name: Project Updated
      description: ''
    - value: sprint_closed
      name: Sprint Closed
      description: ''
    - value: sprint_created
      name: Sprint Created
      description: ''
    - value: sprint_deleted
      name: Sprint Deleted
      description: ''
    - value: sprint_started
      name: Sprint Started
      description: ''
    - value: sprint_updated
      name: Sprint Updated
      description: ''
    - value: user_created
      name: User Created
      description: ''
    - value: user_deleted
      name: User Deleted
      description: ''
    - value: user_updated
      name: User Updated
      description: ''
    - value: jira:version_created
      name: Version Created
      description: ''
    - value: jira:version_deleted
      name: Version Deleted
      description: ''
    - value: jira:version_moved
      name: Version Moved
      description: ''
    - value: jira:version_released
      name: Version Released
      description: ''
    - value: jira:version_unreleased
      name: Version Unreleased
      description: ''
    - value: jira:version_updated
      name: Version Updated
      description: ''
    - value: worklog_created
      name: Worklog Created
      description: ''
    - value: worklog_deleted
      name: Worklog Deleted
      description: ''
    - value: worklog_updated
      name: Worklog Updated
      description: ''
- id: additionalFields
  name: Additional Fields
  type: collection
  default: {}
  required: false
  description: Whether a request with empty body will be sent to the URL. Leave unchecked
    if you want to receive JSON.
  placeholder: Add Field
  typeInfo:
    type: collection
    displayName: Additional Fields
    name: additionalFields
    subProperties:
    - displayName: Exclude Body
      name: excludeBody
      type: boolean
      description: Whether a request with empty body will be sent to the URL. Leave
        unchecked if you want to receive JSON.
      default: false
    - displayName: Filter
      name: filter
      type: string
      description: You can specify a JQL query to send only events triggered by matching
        issues. The JQL filter only applies to events under the Issue and Comment
        columns.
      placeholder: Project = JRA AND resolution = Fixed
      default: ''
    - displayName: Include Fields
      name: includeFields
      type: multiOptions
      value: attachment.id
      default: []
      options:
      - name: Attachment ID
        value: attachment.id
        displayName: Attachment Id
      - name: Board ID
        value: board.id
        displayName: Board Id
      - name: Comment ID
        value: comment.id
        displayName: Comment Id
      - name: Issue ID
        value: issue.id
        displayName: Issue Id
      - name: Merge Version ID
        value: mergeVersion.id
        displayName: Merge Version Id
      - name: Modified User Account ID
        value: modifiedUser.accountId
        displayName: Modified User Account Id
      - name: Modified User Key
        value: modifiedUser.key
        displayName: Modified User Key
      - name: Modified User Name
        value: modifiedUser.name
        displayName: Modified User Name
      - name: Project ID
        value: project.id
        displayName: Project Id
      - name: Project Key
        value: project.key
        displayName: Project Key
      - name: Propery Key
        value: property.key
        displayName: Propery Key
      - name: Sprint ID
        value: sprint.id
        displayName: Sprint Id
      - name: Version ID
        value: version.id
        displayName: Version Id
      - name: Worklog ID
        value: worklog.id
        displayName: Worklog Id
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/jiraTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Jira Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
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
        "authenticateWebhook": {
          "description": "Whether authentication should be activated for the incoming webhooks (makes it more secure)",
          "type": "boolean",
          "default": false
        },
        "incomingAuthentication": {
          "description": "If authentication should be activated for the webhook (makes it more secure)",
          "type": "string",
          "enum": [
            "queryAuth",
            "none"
          ],
          "default": "none"
        },
        "events": {
          "description": "The events to listen to",
          "type": "string",
          "default": []
        },
        "additionalFields": {
          "description": "Whether a request with empty body will be sent to the URL. Leave unchecked if you want to receive JSON.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
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
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
    "version": [
      "1",
      "1.1"
    ]
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
    },
    {
      "name": "httpQueryAuth",
      "required": false
    },
    {
      "name": "httpQueryAuth",
      "required": false
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
