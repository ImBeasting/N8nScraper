---
title: "Node: Linear"
slug: "node-linear"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Consume Linear API"
node_type: "regular"
group: "['output']"
---

# Node: Linear

**Purpose.** Consume Linear API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:linear.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **linearApi**: N/A
- **linearOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `linearApi` | ✓ | {'show': {'authentication': ['apiToken']}} |
| `linearOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**HTTP Methods:** POST

**Common Endpoints:**
- `https://api.linear.app/graphql`

**Headers Used:** Content-Type

---

## Operations

### Comment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Comment | `addComment` | Add a comment to an issue |

### Issue Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Link | `addLink` | Add a link to an issue |
| Create | `create` | Create an issue |
| Delete | `delete` | Delete an issue |
| Get | `get` | Get an issue |
| Get Many | `getAll` | Get many issues |
| Update | `update` | Update an issue |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | issue | ✗ | Resource to operate on |  |

**Resource options:**

* **Comment** (`comment`)
* **Issue** (`issue`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | addComment | ✗ | Add a comment to an issue |  |

**Operation options:**

* **Add Comment** (`addComment`) - Add a comment to an issue

---

### Add Comment parameters (`addComment`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue ID | `issueId` | string |  | ✓ |  |  |
| Comment | `comment` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the parent comment if this is a reply | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Parent Comment ID | `parentId` | string |  | ID of the parent comment if this is a reply |

</details>


### Add Link parameters (`addLink`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue ID | `issueId` | string |  | ✓ |  |  |
| Link | `link` | string |  | ✓ |  |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Team Name or ID | `teamId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Title | `title` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigneeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Description | `description` | string |  |  |
| Priority | `priorityId` | options | 0 |  |
| State Name or ID | `stateId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue ID | `issueId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue ID | `issueId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Issue ID | `issueId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigneeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Description | `description` | string |  |  |
| Priority Name/ID | `priorityId` | options | 0 |  |
| State Name or ID | `stateId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Team Name or ID | `teamId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Title | `title` | string |  |  |

</details>

| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigneeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Description | `description` | string |  |  |
| Priority Name/ID | `priorityId` | options | 0 |  |
| State Name or ID | `stateId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Team Name or ID | `teamId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Title | `title` | string |  |  |

</details>


---

## Load Options Methods

- `getTeams`
- `query`
- `variables`

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Add Comment

**From workflow:** Linear Test Workflow

**Parameters:**
```json
{
  "resource": "comment",
  "issueId": "test-17",
  "comment": "test",
  "additionalFields": {}
}
```

**Credentials:**
- linearApi: `86-88`

### Example 2: Add Comment - with parent

**From workflow:** Linear Test Workflow

**Parameters:**
```json
{
  "resource": "comment",
  "issueId": "test-17",
  "comment": "Add to parent",
  "additionalFields": {
    "parentId": "ff12069e-fac8-4b18-8455-cc6b29fa1e77"
  }
}
```

**Credentials:**
- linearApi: `86-88`

### Example 3: Add link to issue

**From workflow:** Linear Test Workflow

**Parameters:**
```json
{
  "operation": "addLink",
  "issueId": "test-17",
  "link": "https://n8n.io"
}
```

**Credentials:**
- linearApi: `86-88`

### Example 4: Create Issue

**From workflow:** Linear Test Workflow

**Parameters:**
```json
{
  "teamId": "0a2994c1-5d99-48aa-ab22-8b5ba4711ebc",
  "title": "This is a test issue",
  "additionalFields": {
    "assigneeId": "1c51f0c4-c552-4614-a534-8de1752ba7d7",
    "description": "test description",
    "priorityId": 3,
    "stateId": "65a87a3a-5729-4d82-96bf-badccbeb49af"
  }
}
```

**Credentials:**
- linearApi: `86-88`

### Example 5: Issue Get Many

**From workflow:** Linear Test Workflow

**Parameters:**
```json
{
  "operation": "getAll",
  "limit": 1
}
```

**Credentials:**
- linearApi: `86-88`


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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: linear
displayName: Linear
description: Consume Linear API
version:
- '1'
- '1.1'
nodeType: regular
group:
- output
credentials:
- name: linearApi
  required: true
- name: linearOAuth2Api
  required: true
operations:
- id: addComment
  name: Add Comment
  description: Add a comment to an issue
  params:
  - id: issueId
    name: Issue ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: Issue ID
      name: issueId
  - id: comment
    name: Comment
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - comment
          operation:
          - addComment
    typeInfo:
      type: string
      displayName: Comment
      name: comment
- id: addLink
  name: Add Link
  description: Add a link to an issue
  params:
  - id: issueId
    name: Issue ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: link
    name: Link
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
          - addLink
    typeInfo:
      type: string
      displayName: Link
      name: link
- id: create
  name: Create
  description: Create an issue
  params:
  - id: teamId
    name: Team Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - create
    typeInfo:
      type: options
      displayName: Team Name or ID
      name: teamId
      typeOptions:
        loadOptionsMethod: getTeams
      possibleValues: []
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
          - issue
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
- id: delete
  name: Delete
  description: Delete an issue
  params:
  - id: issueId
    name: Issue ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
- id: get
  name: Get
  description: Get an issue
  params:
  - id: issueId
    name: Issue ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
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
    validation:
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          resource:
          - issue
          operation:
          - getAll
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
- id: update
  name: Update
  description: Update an issue
  params:
  - id: issueId
    name: Issue ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
examples:
- name: Add Comment
  parameters:
    resource: comment
    issueId: test-17
    comment: test
    additionalFields: {}
  workflow: Linear Test Workflow
- name: Add Comment - with parent
  parameters:
    resource: comment
    issueId: test-17
    comment: Add to parent
    additionalFields:
      parentId: ff12069e-fac8-4b18-8455-cc6b29fa1e77
  workflow: Linear Test Workflow
- name: Add link to issue
  parameters:
    operation: addLink
    issueId: test-17
    link: https://n8n.io
  workflow: Linear Test Workflow
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - POST
  endpoints:
  - https://api.linear.app/graphql
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
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
  "$id": "https://n8n.io/schemas/nodes/linear.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Linear Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "addComment",
        "addLink",
        "create",
        "delete",
        "get",
        "getAll",
        "update"
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
            "apiToken",
            "oAuth2"
          ],
          "default": "apiToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "comment",
            "issue"
          ],
          "default": "issue"
        },
        "operation": {
          "description": "Add a link to an issue",
          "type": "string",
          "enum": [
            "addLink",
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "issueId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "comment": {
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
        "teamId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "title": {
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
        "updateFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "link": {
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
    "version": [
      "1",
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "linearApi",
      "required": true
    },
    {
      "name": "linearOAuth2Api",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Add Comment",
      "value": {
        "resource": "comment",
        "issueId": "test-17",
        "comment": "test",
        "additionalFields": {}
      }
    },
    {
      "description": "Add Comment - with parent",
      "value": {
        "resource": "comment",
        "issueId": "test-17",
        "comment": "Add to parent",
        "additionalFields": {
          "parentId": "ff12069e-fac8-4b18-8455-cc6b29fa1e77"
        }
      }
    },
    {
      "description": "Add link to issue",
      "value": {
        "operation": "addLink",
        "issueId": "test-17",
        "link": "https://n8n.io"
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
