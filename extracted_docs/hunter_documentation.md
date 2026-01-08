---
title: "Node: Hunter"
slug: "node-hunter"
version: "1"
updated: "2026-01-08"
summary: "Consume Hunter API"
node_type: "regular"
group: "['output']"
---

# Node: Hunter

**Purpose.** Consume Hunter API
**Subtitle.** ={{$parameter["operation"]}}


---

## Node Details

- **Icon:** `file:hunter.png`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **hunterApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `hunterApi` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Domain Search | `domainSearch` | Get every email address found on the internet using a given domain name, with sources |
| Email Finder | `emailFinder` | Generate or retrieve the most likely email address from a domain name, a first name and a last name |
| Email Verifier | `emailVerifier` | Verify the deliverability of an email address |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | domainSearch | ✗ | Get every email address found on the internet using a given domain name, with sources |  |

**Operation options:**

* **Domain Search** (`domainSearch`) - Get every email address found on the internet using a given domain name, with sources
* **Email Finder** (`emailFinder`) - Generate or retrieve the most likely email address from a domain name, a first name and a last name
* **Email Verifier** (`emailVerifier`) - Verify the deliverability of an email address

---

### Domain Search parameters (`domainSearch`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Domain | `domain` | string |  | ✓ | Domain name from which you want to find the email addresses. For example, "stripe.com". |  |
| Only Emails | `onlyEmails` | boolean | True | ✗ | Whether to return only the found emails | email |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Type | `type` | options |  |  |
| Seniority | `seniority` | multiOptions | [] |  |
| Department | `department` | multiOptions | [] |  |

</details>


### Email Finder parameters (`emailFinder`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Domain | `domain` | string |  | ✓ | Domain name from which you want to find the email addresses. For example, "stripe.com". |  |
| First Name | `firstname` | string |  | ✓ | The person's first name. It doesn't need to be in lowercase. |  |
| Last Name | `lastname` | string |  | ✓ | The person's last name. It doesn't need to be in lowercase. |  |

### Email Verifier parameters (`emailVerifier`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | The email address you want to verify | e.g. name@email.com | email |

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
* Categories: Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: hunter
displayName: Hunter
description: Consume Hunter API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: hunterApi
  required: true
operations:
- id: domainSearch
  name: Domain Search
  description: Get every email address found on the internet using a given domain
    name, with sources
  params:
  - id: domain
    name: Domain
    type: string
    default: ''
    required: true
    description: Domain name from which you want to find the email addresses. For
      example, "stripe.com".
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - emailFinder
    typeInfo: &id002
      type: string
      displayName: Domain
      name: domain
  - id: onlyEmails
    name: Only Emails
    type: boolean
    default: true
    required: false
    description: Whether to return only the found emails
    validation:
      format: email
      displayOptions:
        show:
          operation:
          - domainSearch
    typeInfo:
      type: boolean
      displayName: Only Emails
      name: onlyEmails
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          operation:
          - domainSearch
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - domainSearch
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
- id: emailFinder
  name: Email Finder
  description: Generate or retrieve the most likely email address from a domain name,
    a first name and a last name
  params:
  - id: domain
    name: Domain
    type: string
    default: ''
    required: true
    description: Domain name from which you want to find the email addresses. For
      example, "stripe.com".
    validation: *id001
    typeInfo: *id002
  - id: firstname
    name: First Name
    type: string
    default: ''
    required: true
    description: The person's first name. It doesn't need to be in lowercase.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - emailFinder
    typeInfo:
      type: string
      displayName: First Name
      name: firstname
  - id: lastname
    name: Last Name
    type: string
    default: ''
    required: true
    description: The person's last name. It doesn't need to be in lowercase.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - emailFinder
    typeInfo:
      type: string
      displayName: Last Name
      name: lastname
- id: emailVerifier
  name: Email Verifier
  description: Verify the deliverability of an email address
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email address you want to verify
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - emailVerifier
    typeInfo:
      type: string
      displayName: Email
      name: email
common_expressions:
- ={{$parameter["operation"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/hunter.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Hunter Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "domainSearch",
        "emailFinder",
        "emailVerifier"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Get every email address found on the internet using a given domain name, with sources",
          "type": "string",
          "enum": [
            "domainSearch",
            "emailFinder",
            "emailVerifier"
          ],
          "default": "domainSearch"
        },
        "domain": {
          "description": "Domain name from which you want to find the email addresses. For example, \"stripe.com\".",
          "type": "string",
          "default": ""
        },
        "onlyEmails": {
          "description": "Whether to return only the found emails",
          "type": "boolean",
          "default": true,
          "format": "email"
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
        },
        "filters": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "firstname": {
          "description": "The person's first name. It doesn't need to be in lowercase.",
          "type": "string",
          "default": ""
        },
        "lastname": {
          "description": "The person's last name. It doesn't need to be in lowercase.",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "The email address you want to verify",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
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
      "name": "hunterApi",
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
