---
title: "Node: TheHiveProject"
slug: "node-thehiveproject"
version: "1.0"
updated: "2025-11-13"
summary: "Consume TheHive 5 API"
node_type: "regular"
group: "['transform']"
---

# Node: TheHiveProject

**Purpose.** Consume TheHive 5 API
**Subtitle.** ={{$parameter["operation"]}} : {{$parameter["resource"]}}


---

## Node Details

- **Icon:** `file:thehiveproject.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Operations

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a task |
| Delete | `deleteTask` | Delete an task |
| Execute Responder | `executeResponder` | Execute responder on a task |
| Get | `get` | Get a task |
| Search | `search` | Search tasks |
| Update | `update` | Update a task |

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

### Page Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a page |
| Delete | `deletePage` | Delete a page |
| Search | `search` | Search pages |
| Update | `update` | Update a page |

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

### Comment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `add` | Create a comment in a case or alert |
| Delete | `deleteComment` | Delete a comment |
| Search | `search` | Search comments |
| Update | `update` | Update a comment |

### Query Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Execute Query | `executeQuery` | Execute a query |

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

* **Create** (`create`) - Create a task
* **Delete** (`deleteTask`) - Delete an task
* **Execute Responder** (`executeResponder`) - Execute responder on a task
* **Get** (`get`) - Get a task
* **Search** (`search`) - Search tasks
* **Update** (`update`) - Update a task

---

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: TheHive Observable Create

**From workflow:** TheHive Observable Create Test Workflow

**Parameters:**
```json
{
  "resource": "observable",
  "operation": "create",
  "createIn": "case",
  "id": {
    "__rl": true,
    "mode": "id",
    "value": "~123789"
  },
  "dataType": "domain",
  "data": "malicious.example.com",
  "observableFields": {
    "mappingMode": "defineBelow",
    "value": {
      "message": "Suspicious domain detected in analysis",
      "tags": "malware,suspicious",
      "tlp": 2,
      "pap": 2,
      "ioc": true,
      "sighted": false
    }
  }
}
```

**Credentials:**
- theHiveProjectApi: `TheHive API Credentials`

### Example 2: TheHive Case Create

**From workflow:** TheHive Case Create Test Workflow

**Parameters:**
```json
{
  "resource": "case",
  "operation": "create",
  "caseFields": {
    "mappingMode": "defineBelow",
    "value": {
      "title": "Test Case",
      "description": "Test case description",
      "severity": 2,
      "tags": "test,n8n",
      "tlp": 2,
      "pap": 2
    }
  }
}
```

**Credentials:**
- theHiveProjectApi: `TheHive API Credentials`

### Example 3: TheHive Task Create

**From workflow:** TheHive Task Create Test Workflow

**Parameters:**
```json
{
  "resource": "task",
  "operation": "create",
  "caseId": {
    "__rl": true,
    "mode": "id",
    "value": "~123789"
  },
  "taskFields": {
    "mappingMode": "defineBelow",
    "value": {
      "title": "Test Task",
      "description": "Test task description",
      "group": "Investigation",
      "flag": false,
      "mandatory": true
    }
  }
}
```

**Credentials:**
- theHiveProjectApi: `TheHive API Credentials`

### Example 4: TheHive Alert Create

**From workflow:** TheHive Alert Create Test Workflow

**Parameters:**
```json
{
  "resource": "alert",
  "operation": "create",
  "alertFields": {
    "mappingMode": "defineBelow",
    "value": {
      "title": "Test Alert",
      "description": "Test alert description",
      "type": "incident",
      "source": "n8n-test",
      "sourceRef": "test-ref-001",
      "severity": 2,
      "tags": "test,n8n",
      "follow": true
    }
  }
}
```

**Credentials:**
- theHiveProjectApi: `TheHive API Credentials`

### Example 5: TheHive Task Get

**From workflow:** TheHive Task Get Test Workflow

**Parameters:**
```json
{
  "resource": "task",
  "operation": "get",
  "taskId": {
    "__rl": true,
    "mode": "id",
    "value": "~654321"
  }
}
```

**Credentials:**
- theHiveProjectApi: `TheHive API Credentials`


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"]}}`

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
* Aliases: Security, Monitoring, Incident, Response, Alert

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: theHiveProject
displayName: TheHiveProject
description: Consume TheHive 5 API
version: '1.0'
nodeType: regular
group:
- transform
operations:
- id: create
  name: Create
  description: ''
- id: deleteTask
  name: Delete
  description: ''
- id: executeResponder
  name: Execute Responder
  description: ''
- id: get
  name: Get
  description: ''
- id: search
  name: Search
  description: ''
- id: update
  name: Update
  description: ''
- id: addAttachment
  name: Add Attachment
  description: ''
- id: deleteLog
  name: Delete
  description: ''
- id: deleteAttachment
  name: Delete Attachment
  description: ''
- id: deletePage
  name: Delete
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
- id: add
  name: Create
  description: ''
- id: deleteComment
  name: Delete
  description: ''
- id: executeQuery
  name: Execute Query
  description: ''
- id: deleteObservable
  name: Delete
  description: ''
- id: executeAnalyzer
  name: Execute Analyzer
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
examples:
- name: TheHive Observable Create
  parameters:
    resource: observable
    operation: create
    createIn: case
    id:
      __rl: true
      mode: id
      value: ~123789
    dataType: domain
    data: malicious.example.com
    observableFields:
      mappingMode: defineBelow
      value:
        message: Suspicious domain detected in analysis
        tags: malware,suspicious
        tlp: 2
        pap: 2
        ioc: true
        sighted: false
  workflow: TheHive Observable Create Test Workflow
- name: TheHive Case Create
  parameters:
    resource: case
    operation: create
    caseFields:
      mappingMode: defineBelow
      value:
        title: Test Case
        description: Test case description
        severity: 2
        tags: test,n8n
        tlp: 2
        pap: 2
  workflow: TheHive Case Create Test Workflow
- name: TheHive Task Create
  parameters:
    resource: task
    operation: create
    caseId:
      __rl: true
      mode: id
      value: ~123789
    taskFields:
      mappingMode: defineBelow
      value:
        title: Test Task
        description: Test task description
        group: Investigation
        flag: false
        mandatory: true
  workflow: TheHive Task Create Test Workflow
common_expressions:
- ={{$parameter["operation"]}}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: filters
    text: Add Filter
  - field: sort
    text: Add Sort Rule
  - field: options
    text: Add option
  - field: observableUi
    text: Add Observable
  hints:
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
  "$id": "https://n8n.io/schemas/nodes/theHiveProject.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TheHiveProject Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "deleteTask",
        "executeResponder",
        "get",
        "search",
        "update",
        "addAttachment",
        "deleteLog",
        "deleteAttachment",
        "deletePage",
        "deleteAlert",
        "merge",
        "promote",
        "status",
        "add",
        "deleteComment",
        "executeQuery",
        "deleteObservable",
        "executeAnalyzer",
        "deleteCase",
        "getAttachment",
        "getTimeline"
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
        "id": {
          "description": "",
          "type": "string"
        },
        "taskUpdateFields": {
          "description": "",
          "type": "string"
        },
        "allCases": {
          "description": "Whether to search in all cases or only in a selected case",
          "type": "boolean",
          "default": true
        },
        "filters": {
          "description": "Field is between two values ('From' is inclusive, 'To' is exclusive)",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "sort": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Sort Rule"
          ]
        },
        "taskFields": {
          "description": "",
          "type": "string"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "addAttachment",
            "create",
            "deleteAttachment",
            "deleteCase",
            "executeResponder",
            "get",
            "getAttachment",
            "getTimeline",
            "search",
            "update"
          ],
          "default": "create"
        },
        "attachmentId": {
          "description": "ID of the attachment. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
        "options": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "searchInKnowledgeBase": {
          "description": "Whether to search in knowledge base or only in the selected case",
          "type": "boolean",
          "default": true
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
        "alertUpdateFields": {
          "description": "",
          "type": "string"
        },
        "status": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
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
        "message": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "searchIn": {
          "description": "Whether to search for comments in all alerts and cases or in a specific case or alert",
          "type": "string",
          "enum": [
            "all",
            "alert",
            "case"
          ],
          "default": "all"
        },
        "addTo": {
          "description": "",
          "type": "string",
          "enum": [
            "alert",
            "case"
          ],
          "default": "alert"
        },
        "queryJson": {
          "description": "Search for objects with filtering and sorting capabilities",
          "type": "string",
          "default": "=[\\n  {\\n    "
        },
        "analyzers": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
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
        "caseUpdateFields": {
          "description": "",
          "type": "string"
        },
        "caseFields": {
          "description": "",
          "type": "string"
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
    "version": "1.0"
  },
  "examples": [
    {
      "description": "TheHive Observable Create",
      "value": {
        "resource": "observable",
        "operation": "create",
        "createIn": "case",
        "id": {
          "__rl": true,
          "mode": "id",
          "value": "~123789"
        },
        "dataType": "domain",
        "data": "malicious.example.com",
        "observableFields": {
          "mappingMode": "defineBelow",
          "value": {
            "message": "Suspicious domain detected in analysis",
            "tags": "malware,suspicious",
            "tlp": 2,
            "pap": 2,
            "ioc": true,
            "sighted": false
          }
        }
      }
    },
    {
      "description": "TheHive Case Create",
      "value": {
        "resource": "case",
        "operation": "create",
        "caseFields": {
          "mappingMode": "defineBelow",
          "value": {
            "title": "Test Case",
            "description": "Test case description",
            "severity": 2,
            "tags": "test,n8n",
            "tlp": 2,
            "pap": 2
          }
        }
      }
    },
    {
      "description": "TheHive Task Create",
      "value": {
        "resource": "task",
        "operation": "create",
        "caseId": {
          "__rl": true,
          "mode": "id",
          "value": "~123789"
        },
        "taskFields": {
          "mappingMode": "defineBelow",
          "value": {
            "title": "Test Task",
            "description": "Test task description",
            "group": "Investigation",
            "flag": false,
            "mandatory": true
          }
        }
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1.0 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
