---
title: "Node: Uplead"
slug: "node-uplead"
version: "1"
updated: "2025-11-13"
summary: "Consume Uplead API"
node_type: "regular"
group: "['output']"
---

# Node: Uplead

**Purpose.** Consume Uplead API
**Subtitle.** ={{$parameter["operation"] + ":" + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:uplead.png`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **upleadApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `upleadApi` | ✓ | - |

---

## Operations

### Company Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Enrich | `enrich` | Enrich a company |

### Person Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Enrich | `enrich` | Enrich a person |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | company | ✗ | Company API lets you lookup company data via a domain name or company name |  |

**Resource options:**

* **Company** (`company`) - Company API lets you lookup company data via a domain name or company name
* **Person** (`person`) - Person API lets you lookup a person based on an email address OR based on a domain name + first name + last name

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | enrich | ✗ | Operation to perform |  |

**Operation options:**

* **Enrich** (`enrich`) - Enrich a company

---

### Enrich parameters (`enrich`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company | `company` | string |  | ✗ | The name of the company (e.g – amazon) |  |
| Domain | `domain` | string |  | ✗ | The domain name (e.g – amazon.com) |  |
| Email | `email` | string |  | ✗ | Email address (e.g – mbenioff@salesforce.com) | e.g. name@email.com | email |
| First Name | `firstname` | string |  | ✗ | First name of the person (e.g – Marc) |  |
| Last Name | `lastname` | string |  | ✗ | Last name of the person (e.g – Benioff) |  |
| Domain | `domain` | string |  | ✗ | The domain name (e.g – salesforce.com) |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ":" + $parameter["resource"]}}`

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
node: uplead
displayName: Uplead
description: Consume Uplead API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: upleadApi
  required: true
operations:
- id: enrich
  name: Enrich
  description: ''
  params:
  - id: company
    name: Company
    type: string
    default: ''
    required: false
    description: The name of the company (e.g – amazon)
    validation:
      displayOptions:
        show:
          resource:
          - company
          operation:
          - enrich
    typeInfo:
      type: string
      displayName: Company
      name: company
  - id: domain
    name: Domain
    type: string
    default: ''
    required: false
    description: The domain name (e.g – amazon.com)
    validation: &id001
      displayOptions:
        show:
          resource:
          - person
          operation:
          - enrich
    typeInfo: &id002
      type: string
      displayName: Domain
      name: domain
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: Email address (e.g – mbenioff@salesforce.com)
    placeholder: name@email.com
    validation:
      format: email
      displayOptions:
        show:
          resource:
          - person
          operation:
          - enrich
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: firstname
    name: First Name
    type: string
    default: ''
    required: false
    description: First name of the person (e.g – Marc)
    validation:
      displayOptions:
        show:
          resource:
          - person
          operation:
          - enrich
    typeInfo:
      type: string
      displayName: First Name
      name: firstname
  - id: lastname
    name: Last Name
    type: string
    default: ''
    required: false
    description: Last name of the person (e.g – Benioff)
    validation:
      displayOptions:
        show:
          resource:
          - person
          operation:
          - enrich
    typeInfo:
      type: string
      displayName: Last Name
      name: lastname
  - id: domain
    name: Domain
    type: string
    default: ''
    required: false
    description: The domain name (e.g – salesforce.com)
    validation: *id001
    typeInfo: *id002
common_expressions:
- ={{$parameter["operation"] + ":" + $parameter["resource"]}}
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
  "$id": "https://n8n.io/schemas/nodes/uplead.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Uplead Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "enrich"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Company API lets you lookup company data via a domain name or company name",
          "type": "string",
          "enum": [
            "company",
            "person"
          ],
          "default": "company"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "enrich"
          ],
          "default": "enrich"
        },
        "company": {
          "description": "The name of the company (e.g \u2013 amazon)",
          "type": "string",
          "default": ""
        },
        "domain": {
          "description": "The domain name (e.g \u2013 salesforce.com)",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "Email address (e.g \u2013 mbenioff@salesforce.com)",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "firstname": {
          "description": "First name of the person (e.g \u2013 Marc)",
          "type": "string",
          "default": ""
        },
        "lastname": {
          "description": "Last name of the person (e.g \u2013 Benioff)",
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
      "name": "upleadApi",
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
