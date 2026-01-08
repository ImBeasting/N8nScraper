---
title: "Node: TheHive 5 Trigger"
slug: "node-thehiveprojecttrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when TheHive events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: TheHive 5 Trigger

**Purpose.** Starts the workflow when TheHive events occur


---

## Node Details

- **Icon:** `file:thehiveproject.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice**: You must set up the webhook in TheHive — instructions <a href="https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger/#configure-a-webhook-in-thehive" target="_blank">here</a>

---

## Operations

### Page Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a page |
| Delete | `deletePage` | Delete a page |
| Search | `search` | Search pages |
| Update | `update` | Update a page |

### Observable Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an observable |
| Delete | `deleteObservable` | Delete an observable |
| Execute Analyzer | `executeAnalyzer` | Execute analyzer on an observable |
| Execute Responder | `executeResponder` | Execute responder on an observable |
| Get | `get` | Get an observable |
| Search | `search` | Search observables |
| Update | `update` | Update an observable |

### Case Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Attachment | `addAttachment` | Add attachment to a case |
| Create | `create` | Create a case |
| Delete Attachment | `deleteAttachment` | Delete attachment from a case |
| Delete Case | `deleteCase` | Delete an case |
| Execute Responder | `executeResponder` | Execute responder on a case |
| Get | `get` | Get a case |
| Get Attachment | `getAttachment` | Get attachment from a case |
| Get Timeline | `getTimeline` | Get timeline of a case |
| Search | `search` | Search cases |
| Update | `update` | Update a case |

### Alert Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an alert |
| Delete | `deleteAlert` | Delete an alert |
| Execute Responder | `executeResponder` | Execute responder on an alert |
| Get | `get` | Get an alert |
| Merge Into Case | `merge` | Merge an alert into a case |
| Promote to Case | `promote` | Promote an alert to a case |
| Search | `search` | Search alerts |
| Update | `update` | Update an alert |
| Update Status | `status` | Update an alert status |

### Log Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Attachment | `addAttachment` | Add attachment to a task log |
| Create | `create` | Create a task log |
| Delete | `deleteLog` | Delete task log |
| Delete Attachment | `deleteAttachment` | Delete attachment from a task log |
| Execute Responder | `executeResponder` | Execute responder on a task log |
| Get | `get` | Get a task log |
| Search | `search` | Search task logs |

### Query Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Execute Query | `executeQuery` | Execute a query |

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a task |
| Delete | `deleteTask` | Delete an task |
| Execute Responder | `executeResponder` | Execute responder on a task |
| Get | `get` | Get a task |
| Search | `search` | Search tasks |
| Update | `update` | Update a task |

### Comment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `add` | Create a comment in a case or alert |
| Delete | `deleteComment` | Delete a comment |
| Search | `search` | Search comments |
| Update | `update` | Update a comment |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | alert | ✓ | Resource to operate on |  |

**Resource options:**

* **Alert** (`alert`)
* **Case** (`case`)
* **Comment** (`comment`)
* **Observable** (`observable`)
* **Page** (`page`)
* **Query** (`query`)
* **Task** (`task`)
* **Task Log** (`log`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✓ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create a page
* **Delete** (`deletePage`) - Delete a page
* **Search** (`search`) - Search pages
* **Update** (`update`) - Update a page

---

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"]}}`

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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: theHiveProjectTrigger
displayName: TheHive 5 Trigger
description: Starts the workflow when TheHive events occur
version: '1'
nodeType: trigger
group:
- trigger
operations:
- id: create
  name: Create
  description: ''
- id: deletePage
  name: Delete
  description: ''
- id: search
  name: Search
  description: ''
- id: update
  name: Update
  description: ''
- id: deleteObservable
  name: Delete
  description: ''
- id: executeAnalyzer
  name: Execute Analyzer
  description: ''
- id: executeResponder
  name: Execute Responder
  description: ''
- id: get
  name: Get
  description: ''
- id: addAttachment
  name: Add Attachment
  description: ''
- id: deleteAttachment
  name: Delete Attachment
  description: ''
- id: deleteCase
  name: Delete Case
  description: ''
- id: getAttachment
  name: Get Attachment
  description: ''
- id: getTimeline
  name: Get Timeline
  description: ''
- id: deleteAlert
  name: Delete
  description: ''
- id: merge
  name: Merge Into Case
  description: ''
- id: promote
  name: Promote to Case
  description: ''
- id: status
  name: Update Status
  description: ''
- id: deleteLog
  name: Delete
  description: ''
- id: executeQuery
  name: Execute Query
  description: ''
- id: deleteTask
  name: Delete
  description: ''
- id: add
  name: Create
  description: ''
- id: deleteComment
  name: Delete
  description: ''
common_expressions:
- ={{$parameter["operation"]}}
ui_elements:
  notices:
  - name: notice
    text: You must set up the webhook in TheHive — instructions <a href="https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger/#configure-a-webhook-in-thehive"
      target="_blank">here</a>
    conditions: null
  tooltips: []
  placeholders:
  - field: filters
    text: Add Filter
  - field: options
    text: Add option
  - field: filters
    text: Add Filter
  - field: sort
    text: Add Sort Rule
  - field: observableUi
    text: Add Observable
  hints:
  - field: filters
    text: The field to filter on, supports dot notation
  - field: observableUi
    text: The name of the input binary field containing the file to be written
  - field: queryJson
    text: The query should be an array of operations with the required selection and
      optional filtering, sorting, and pagination. See <a href="https://docs.strangebee.com/thehive/api-docs/#operation/Query%20API"
      target="_blank">Query API</a> for more information.
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
  "$id": "https://n8n.io/schemas/nodes/theHiveProjectTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TheHive 5 Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "deletePage",
        "search",
        "update",
        "deleteObservable",
        "executeAnalyzer",
        "executeResponder",
        "get",
        "addAttachment",
        "deleteAttachment",
        "deleteCase",
        "getAttachment",
        "getTimeline",
        "deleteAlert",
        "merge",
        "promote",
        "status",
        "deleteLog",
        "executeQuery",
        "deleteTask",
        "add",
        "deleteComment"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "Events types",
          "type": "string",
          "default": []
        },
        "filters": {
          "description": "Field is between two values ('From' is inclusive, 'To' is exclusive)",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "options": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "alert",
            "case",
            "comment",
            "observable",
            "page",
            "query",
            "task",
            "log"
          ],
          "default": "alert"
        },
        "searchInKnowledgeBase": {
          "description": "Whether to search in knowledge base or only in the selected case",
          "type": "boolean",
          "default": true
        },
        "sort": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Sort Rule"
          ]
        },
        "location": {
          "description": "",
          "type": "string",
          "enum": [
            "case",
            "knowledgeBase"
          ],
          "default": "case"
        },
        "content": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "category": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "add",
            "deleteComment",
            "search",
            "update"
          ],
          "default": "add"
        },
        "searchIn": {
          "description": "Whether to search for observables in all alerts and cases or in a specific case or alert",
          "type": "string",
          "enum": [
            "all",
            "alert",
            "case"
          ],
          "default": "all"
        },
        "observableUpdateFields": {
          "description": "",
          "type": "string"
        },
        "createIn": {
          "description": "",
          "type": "string",
          "enum": [
            "case",
            "alert"
          ],
          "default": "case"
        },
        "id": {
          "description": "",
          "type": "string"
        },
        "dataType": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": "file"
        },
        "data": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "observableFields": {
          "description": "",
          "type": "string"
        },
        "analyzers": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "attachmentId": {
          "description": "ID of the attachment. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "caseUpdateFields": {
          "description": "",
          "type": "string"
        },
        "caseFields": {
          "description": "",
          "type": "string"
        },
        "alertUpdateFields": {
          "description": "",
          "type": "string"
        },
        "alertFields": {
          "description": "",
          "type": "string"
        },
        "observableUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Observable"
          ]
        },
        "status": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "allTasks": {
          "description": "Whether to search in all tasks or only in selected task",
          "type": "boolean",
          "default": true
        },
        "logFields": {
          "description": "",
          "type": "string"
        },
        "queryJson": {
          "description": "Search for objects with filtering and sorting capabilities",
          "type": "string",
          "default": "=[\\n  {\\n    "
        },
        "allCases": {
          "description": "Whether to search in all cases or only in a selected case",
          "type": "boolean",
          "default": true
        },
        "taskUpdateFields": {
          "description": "",
          "type": "string"
        },
        "taskFields": {
          "description": "",
          "type": "string"
        },
        "message": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "addTo": {
          "description": "",
          "type": "string",
          "enum": [
            "alert",
            "case"
          ],
          "default": "alert"
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
