---
title: "Node: LoneScale"
slug: "node-lonescale"
version: "1"
updated: "2026-01-08"
summary: "Create List, add / delete items"
node_type: "regular"
group: "['transform']"
---

# Node: LoneScale

**Purpose.** Create List, add / delete items
**Subtitle.** ={{$parameter["resource"] + ": " + $parameter["operation"]}}


---

## Node Details

- **Icon:** `{'light': 'file:loneScale.svg', 'dark': 'file:loneScale.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **loneScaleApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `loneScaleApi` | ✓ | - |

---

## API Patterns

**Headers Used:** X-API-KEY, Content-Type

---

## Operations

### List Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a list |

### Item Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `add` | Create an item |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | list | ✓ | Manipulate list |  |

**Resource options:**

* **List** (`list`) - Manipulate list
* **Item** (`item`) - Manipulate item

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a list |  |

**Operation options:**

* **Create** (`create`) - Create a list

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Name of your list | e.g. list name |  |
| Type | `type` | options | COMPANY | ✓ | Create a list of companies |  |

**Type options:**

* **Company** (`COMPANY`) - Create a list of companies
* **Contact** (`PEOPLE`) - Create a list of contacts


### Create parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| First Name | `first_name` | string |  | ✓ | Contact first name |  |
| Last Name | `last_name` | string |  | ✓ | Contact last name |  |
| Company Name | `company_name` | string |  | ✗ | Contact company name |  |
| Additional Fields | `peopleAdditionalFields` | collection | {} | ✗ | Contact full name | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Full Name | `full_name` | string |  | Contact full name |
| Contact Email | `email` | string |  |  |
| Company Name | `company_name` | string |  | Contact company name |
| Current Position | `current_position` | string |  | Contact current position |
| Company Domain | `domain` | string |  | Contact company domain |
| Linkedin Url | `linkedin_url` | string |  | Contact Linkedin URL |
| Contact Location | `location` | string |  |  |
| Contact ID | `contact_id` | string |  | Contact ID from your source |

</details>

| Additional Fields | `companyAdditionalFields` | collection | {} | ✗ | Company Linkedin URL | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Linkedin Url | `linkedin_url` | string |  | Company Linkedin URL |
| Company Domain | `domain` | string |  | Company company domain |
| Contact Location | `location` | string |  |  |
| Contact ID | `contact_id` | string |  | Contact ID from your source |

</details>


---

## Load Options Methods

- `getLists`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["resource"] + ": " + $parameter["operation"]}}`

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
node: lonescale
displayName: LoneScale
description: Create List, add / delete items
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: loneScaleApi
  required: true
operations:
- id: create
  name: Create
  description: Create a list
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of your list
    placeholder: list name
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - list
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: type
    name: Type
    type: options
    default: COMPANY
    required: true
    description: Create a list of companies
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - list
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: COMPANY
        name: Company
        description: Create a list of companies
      - value: PEOPLE
        name: Contact
        description: Create a list of contacts
- id: add
  name: Create
  description: Create an item
  params:
  - id: first_name
    name: First Name
    type: string
    default: ''
    required: true
    description: Contact first name
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - add
          resource:
          - item
          type:
          - PEOPLE
    typeInfo:
      type: string
      displayName: First Name
      name: first_name
  - id: last_name
    name: Last Name
    type: string
    default: ''
    required: true
    description: Contact last name
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - add
          resource:
          - item
          type:
          - PEOPLE
    typeInfo:
      type: string
      displayName: Last Name
      name: last_name
  - id: company_name
    name: Company Name
    type: string
    default: ''
    required: false
    description: Contact company name
    validation:
      displayOptions:
        show:
          operation:
          - add
          resource:
          - item
          type:
          - COMPANY
    typeInfo:
      type: string
      displayName: Company Name
      name: company_name
common_expressions:
- '={{$parameter["resource"] + ": " + $parameter["operation"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - X-API-KEY
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: peopleAdditionalFields
    text: Add Field
  - field: companyAdditionalFields
    text: Add Field
  - field: name
    text: list name
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
  "$id": "https://n8n.io/schemas/nodes/lonescale.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "LoneScale Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "add"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Manipulate list",
          "type": "string",
          "enum": [
            "list",
            "item"
          ],
          "default": "list"
        },
        "operation": {
          "description": "Create an item",
          "type": "string",
          "enum": [
            "add"
          ],
          "default": "add"
        },
        "type": {
          "description": "Create a list of companies",
          "type": "string",
          "enum": [
            "COMPANY",
            "PEOPLE"
          ],
          "default": "COMPANY"
        },
        "list": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "first_name": {
          "description": "Contact first name",
          "type": "string",
          "default": ""
        },
        "last_name": {
          "description": "Contact last name",
          "type": "string",
          "default": ""
        },
        "company_name": {
          "description": "Contact company name",
          "type": "string",
          "default": ""
        },
        "peopleAdditionalFields": {
          "description": "Contact full name",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "companyAdditionalFields": {
          "description": "Company Linkedin URL",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "name": {
          "description": "Name of your list",
          "type": "string",
          "default": "",
          "examples": [
            "list name"
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
      "name": "loneScaleApi",
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
