---
title: "Node: ClickUp Trigger"
slug: "node-clickuptrigger"
version: "1"
updated: "2025-11-13"
summary: "Handle ClickUp events via webhooks (Beta)"
node_type: "trigger"
group: "['trigger']"
---

# Node: ClickUp Trigger

**Purpose.** Handle ClickUp events via webhooks (Beta)


---

## Node Details

- **Icon:** `file:clickup.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **clickUpApi**: N/A
- **clickUpOAuth2Api**: N/A


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
| `clickUpApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `clickUpOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | accessToken | ✗ |  |  |

**Authentication options:**

* **Access Token** (`accessToken`)
* **OAuth2** (`oAuth2`)

| Team Name or ID | `team` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Events | `events` | multiOptions | [] | ✓ |  |  |

**Events options:**

* ***** (`*`)
* **folder.created** (`folderCreated`)
* **folder.deleted** (`folderDeleted`)
* **folder.updated** (`folderUpdated`)
* **goal.created** (`goalCreated`)
* **goal.deleted** (`goalDeleted`)
* **goal.updated** (`goalUpdated`)
* **keyResult.created** (`keyResultCreated`)
* **keyResult.deleted** (`keyResultDelete`)
* **keyResult.updated** (`keyResultUpdated`)
* **list.created** (`listCreated`)
* **list.deleted** (`listDeleted`)
* **list.updated** (`listUpdated`)
* **space.created** (`spaceCreated`)
* **space.deleted** (`spaceDeleted`)
* **space.updated** (`spaceUpdated`)
* **task.assignee.updated** (`taskAssigneeUpdated`)
* **task.comment.posted** (`taskCommentPosted`)
* **task.comment.updated** (`taskCommentUpdated`)
* **task.created** (`taskCreated`)
* **task.deleted** (`taskDeleted`)
* **task.dueDate.updated** (`taskDueDateUpdated`)
* **task.moved** (`taskMoved`)
* **task.status.updated** (`taskStatusUpdated`)
* **task.tag.updated** (`taskTagUpdated`)
* **task.timeEstimate.updated** (`taskTimeEstimateUpdated`)
* **task.timeTracked.updated** (`taskTimeTrackedUpdated`)
* **task.updated** (`taskUpdated`)

| Filters | `filters` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Folder ID | `folderId` | string |  |  |
| List ID | `listId` | string |  |  |
| Space ID | `spaceId` | string |  |  |
| Task ID | `taskId` | string |  |  |

</details>


---

## Load Options Methods

- `getTeams`

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
* Categories: Productivity, Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: clickUpTrigger
displayName: ClickUp Trigger
description: Handle ClickUp events via webhooks (Beta)
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: clickUpApi
  required: true
- name: clickUpOAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: accessToken
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: accessToken
      name: Access Token
      description: ''
    - value: oAuth2
      name: OAuth2
      description: ''
- id: team
  name: Team Name or ID
  type: options
  default: ''
  required: true
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Team Name or ID
    name: team
    typeOptions:
      loadOptionsMethod: getTeams
    possibleValues: []
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: ''
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
    - value: folderCreated
      name: folder.created
      description: ''
    - value: folderDeleted
      name: folder.deleted
      description: ''
    - value: folderUpdated
      name: folder.updated
      description: ''
    - value: goalCreated
      name: goal.created
      description: ''
    - value: goalDeleted
      name: goal.deleted
      description: ''
    - value: goalUpdated
      name: goal.updated
      description: ''
    - value: keyResultCreated
      name: keyResult.created
      description: ''
    - value: keyResultDelete
      name: keyResult.deleted
      description: ''
    - value: keyResultUpdated
      name: keyResult.updated
      description: ''
    - value: listCreated
      name: list.created
      description: ''
    - value: listDeleted
      name: list.deleted
      description: ''
    - value: listUpdated
      name: list.updated
      description: ''
    - value: spaceCreated
      name: space.created
      description: ''
    - value: spaceDeleted
      name: space.deleted
      description: ''
    - value: spaceUpdated
      name: space.updated
      description: ''
    - value: taskAssigneeUpdated
      name: task.assignee.updated
      description: ''
    - value: taskCommentPosted
      name: task.comment.posted
      description: ''
    - value: taskCommentUpdated
      name: task.comment.updated
      description: ''
    - value: taskCreated
      name: task.created
      description: ''
    - value: taskDeleted
      name: task.deleted
      description: ''
    - value: taskDueDateUpdated
      name: task.dueDate.updated
      description: ''
    - value: taskMoved
      name: task.moved
      description: ''
    - value: taskStatusUpdated
      name: task.status.updated
      description: ''
    - value: taskTagUpdated
      name: task.tag.updated
      description: ''
    - value: taskTimeEstimateUpdated
      name: task.timeEstimate.updated
      description: ''
    - value: taskTimeTrackedUpdated
      name: task.timeTracked.updated
      description: ''
    - value: taskUpdated
      name: task.updated
      description: ''
- id: filters
  name: Filters
  type: collection
  default: {}
  required: false
  description: ''
  placeholder: Add Field
  typeInfo:
    type: collection
    displayName: Filters
    name: filters
    subProperties:
    - displayName: Folder ID
      name: folderId
      type: string
      default: ''
    - displayName: List ID
      name: listId
      type: string
      default: ''
    - displayName: Space ID
      name: spaceId
      type: string
      default: ''
    - displayName: Task ID
      name: taskId
      type: string
      default: ''
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: filters
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
  "$id": "https://n8n.io/schemas/nodes/clickUpTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ClickUp Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
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
        "team": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "events": {
          "description": "",
          "type": "string",
          "default": []
        },
        "filters": {
          "description": "",
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
    "version": "1"
  },
  "credentials": [
    {
      "name": "clickUpApi",
      "required": true
    },
    {
      "name": "clickUpOAuth2Api",
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
