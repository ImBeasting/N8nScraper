---
title: "Node: Clearbit"
slug: "node-clearbit"
version: "1"
updated: "2026-01-08"
summary: "Consume Clearbit API"
node_type: "regular"
group: "['output']"
---

# Node: Clearbit

**Purpose.** Consume Clearbit API
**Subtitle.** ={{$parameter["operation"] + ":" + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:clearbit.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **clearbitApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `clearbitApi` | ✓ | - |

---

## Operations

### Company Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Autocomplete | `autocomplete` | Auto-complete company names and retrieve logo and domain |
| Enrich | `enrich` | Look up person and company data based on an email or domain |

### Person Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Enrich | `enrich` | Look up a person and company data based on an email or domain |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | company | ✗ | The Company API allows you to look up a company by their domain |  |

**Resource options:**

* **Company** (`company`) - The Company API allows you to look up a company by their domain
* **Person** (`person`) - The Person API lets you retrieve social information associated with an email address, such as a person’s name, location and Twitter handle

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | enrich | ✗ | Auto-complete company names and retrieve logo and domain |  |

**Operation options:**

* **Autocomplete** (`autocomplete`) - Auto-complete company names and retrieve logo and domain
* **Enrich** (`enrich`) - Look up person and company data based on an email or domain

---

### Autocomplete parameters (`autocomplete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Name is the partial name of the company |  |

### Enrich parameters (`enrich`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Domain | `domain` | string |  | ✓ | The domain to look up |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The name of the company | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company Name | `companyName` | string |  | The name of the company |
| Facebook | `facebook` | string |  | The Facebook URL for the company |
| Linkedin | `linkedin` | string |  | The LinkedIn URL for the company |
| Twitter | `twitter` | string |  | The Twitter handle for the company |

</details>

| Email | `email` | string |  | ✓ | The email address to look up | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The name of the person’s employer | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company | `company` | string |  | The name of the person’s employer |
| Company Domain | `companyDomain` | string |  | The domain for the person’s employer |
| Facebook | `facebook` | string |  | The Facebook URL for the person |
| Family Name | `familyName` | string |  | Last name of person. If you have this, passing this is strongly recommended to improve match rates. |
| Given Name | `givenName` | string |  | First name of person |
| IP Address | `ipAddress` | string |  | IP address of the person. If you have this, passing this is strongly recommended to improve match rates. |
| Location | `location` | string |  | The city or country where the person resides |
| LinkedIn | `linkedIn` | string |  | The LinkedIn URL for the person |
| Twitter | `twitter` | string |  | The Twitter handle for the person |

</details>


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
node: clearbit
displayName: Clearbit
description: Consume Clearbit API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: clearbitApi
  required: true
operations:
- id: autocomplete
  name: Autocomplete
  description: Auto-complete company names and retrieve logo and domain
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name is the partial name of the company
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - company
          operation:
          - autocomplete
    typeInfo:
      type: string
      displayName: Name
      name: name
- id: enrich
  name: Enrich
  description: Look up person and company data based on an email or domain
  params:
  - id: domain
    name: Domain
    type: string
    default: ''
    required: true
    description: The domain to look up
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - company
          operation:
          - enrich
    typeInfo:
      type: string
      displayName: Domain
      name: domain
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email address to look up
    placeholder: name@email.com
    validation:
      required: true
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
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
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
  "$id": "https://n8n.io/schemas/nodes/clearbit.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Clearbit Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "autocomplete",
        "enrich"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "The Company API allows you to look up a company by their domain",
          "type": "string",
          "enum": [
            "company",
            "person"
          ],
          "default": "company"
        },
        "operation": {
          "description": "Look up a person and company data based on an email or domain",
          "type": "string",
          "enum": [
            "enrich"
          ],
          "default": "enrich"
        },
        "domain": {
          "description": "The domain to look up",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The name of the person\u2019s employer",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "name": {
          "description": "Name is the partial name of the company",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "The email address to look up",
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
      "name": "clearbitApi",
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
