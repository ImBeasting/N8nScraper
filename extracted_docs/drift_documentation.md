---
title: "Node: Drift"
slug: "node-drift"
version: "1"
updated: "2026-01-08"
summary: "Consume Drift API"
node_type: "regular"
group: "['output']"
---

# Node: Drift

**Purpose.** Consume Drift API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:drift.svg', 'dark': 'file:drift.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **driftApi**: N/A
- **driftOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `driftApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `driftOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a contact |
| Custom Attributes | `getCustomAttributes` | Get custom attributes |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact |
| Update | `update` | Update a contact |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✗ | Resource to operate on |  |

**Resource options:**

* **Contact** (`contact`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a contact |  |

**Operation options:**

* **Create** (`create`) - Create a contact
* **Custom Attributes** (`getCustomAttributes`) - Get custom attributes
* **Delete** (`delete`) - Delete a contact
* **Get** (`get`) - Get a contact
* **Update** (`update`) - Update a contact

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | The email of the contact | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The name of the contact | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | The name of the contact |
| Phone | `phone` | string |  | The phone number associated with the contact |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | Unique identifier for the contact |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | Unique identifier for the contact |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ | Unique identifier for the contact |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The email of the contact | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  | The email of the contact |
| Name | `name` | string |  | The name of the contact |
| Phone | `phone` | string |  | The phone number associated with the contact |

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
* Categories: Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: drift
displayName: Drift
description: Consume Drift API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: driftApi
  required: true
- name: driftOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a contact
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email of the contact
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
    typeInfo:
      type: string
      displayName: Email
      name: email
- id: getCustomAttributes
  name: Custom Attributes
  description: Get custom attributes
- id: delete
  name: Delete
  description: Delete a contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the contact
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - delete
    typeInfo: &id002
      type: string
      displayName: Contact ID
      name: contactId
- id: get
  name: Get
  description: Get a contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the contact
    validation: *id001
    typeInfo: *id002
- id: update
  name: Update
  description: Update a contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the contact
    validation: *id001
    typeInfo: *id002
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
  - field: email
    text: name@email.com
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
  "$id": "https://n8n.io/schemas/nodes/drift.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Drift Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "getCustomAttributes",
        "delete",
        "get",
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
            "accessToken",
            "oAuth2"
          ],
          "default": "accessToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "contact"
          ],
          "default": "contact"
        },
        "operation": {
          "description": "Create a contact",
          "type": "string",
          "enum": [
            "create",
            "getCustomAttributes",
            "delete",
            "get",
            "update"
          ],
          "default": "create"
        },
        "email": {
          "description": "The email of the contact",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "additionalFields": {
          "description": "The name of the contact",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "contactId": {
          "description": "Unique identifier for the contact",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "The email of the contact",
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
      "name": "driftApi",
      "required": true
    },
    {
      "name": "driftOAuth2Api",
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
