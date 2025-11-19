---
title: "Node: Dropcontact"
slug: "node-dropcontact"
version: "1"
updated: "2025-11-13"
summary: "Find B2B emails and enrich contacts"
node_type: "regular"
group: "['transform']"
---

# Node: Dropcontact

**Purpose.** Find B2B emails and enrich contacts
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:dropcontact.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **dropcontactApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `dropcontactApi` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Enrich | `enrich` | Find B2B emails and enrich your contact from his name and his website |
| Fetch Request | `fetchRequest` |  |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✓ | Resource to operate on |  |

**Resource options:**

* **Contact** (`contact`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | enrich | ✓ | Find B2B emails and enrich your contact from his name and his website |  |

**Operation options:**

* **Enrich** (`enrich`) - Find B2B emails and enrich your contact from his name and his website
* **Fetch Request** (`fetchRequest`)

---

### Enrich parameters (`enrich`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✗ | e.g. name@email.com | email |
| Simplify Output (Faster) | `simplify` | boolean | False | ✗ | When off, waits for the contact data before completing. Waiting time can be adjusted with Extend Wait Time option. When on, returns a request_id that can be used later in the Fetch Request operation. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company SIREN Number | `num_siren` | string |  |  |
| Company SIRET Code | `siret` | string |  |  |
| Company Name | `company` | string |  |  |
| Country | `country` | string |  |  |
| First Name | `first_name` | string |  |  |
| Full Name | `full_name` | string |  |  |
| Last Name | `last_name` | string |  |  |
| LinkedIn Profile | `linkedin` | string |  |  |
| Phone Number | `phone` | string |  |  |
| Website | `website` | string |  |  |

</details>

| Options | `options` | collection | {} | ✗ | When not simplifying the response, data will be fetched in two steps. This parameter controls how long to wait (in seconds) before trying the second step. | e.g. Add option | min:1, max:∞ |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Data Fetch Wait Time | `waitTime` | number | 45 | When not simplifying the response, data will be fetched in two steps. This parameter controls how long to wait (in seconds) before trying the second step. |
| French Company Enrich | `siren` | boolean | False | Whether you want the <a href="https://en.wikipedia.org/wiki/SIREN_code" target="_blank">SIREN number</a>, NAF code, TVA number, company address and informations about the company leader. Only applies to french companies. |
| Language | `language` | options | en | Whether the response is in English or French |

</details>


### Fetch Request parameters (`fetchRequest`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Request ID | `requestId` | string |  | ✓ |  |  |

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
node: dropcontact
displayName: Dropcontact
description: Find B2B emails and enrich contacts
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: dropcontactApi
  required: true
operations:
- id: enrich
  name: Enrich
  description: Find B2B emails and enrich your contact from his name and his website
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: ''
    placeholder: name@email.com
    validation:
      format: email
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - enrich
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: simplify
    name: Simplify Output (Faster)
    type: boolean
    default: false
    required: false
    description: When off, waits for the contact data before completing. Waiting time
      can be adjusted with Extend Wait Time option. When on, returns a request_id
      that can be used later in the Fetch Request operation.
    validation:
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - enrich
    typeInfo:
      type: boolean
      displayName: Simplify Output (Faster)
      name: simplify
- id: fetchRequest
  name: Fetch Request
  description: ''
  params:
  - id: requestId
    name: Request ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - fetchRequest
    typeInfo:
      type: string
      displayName: Request ID
      name: requestId
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/dropcontact.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Dropcontact Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "enrich",
        "fetchRequest"
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
            "contact"
          ],
          "default": "contact"
        },
        "operation": {
          "description": "Find B2B emails and enrich your contact from his name and his website",
          "type": "string",
          "enum": [
            "enrich",
            "fetchRequest"
          ],
          "default": "enrich"
        },
        "requestId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "simplify": {
          "description": "When off, waits for the contact data before completing. Waiting time can be adjusted with Extend Wait Time option. When on, returns a request_id that can be used later in the Fetch Request operation.",
          "type": "boolean",
          "default": false
        },
        "additionalFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "options": {
          "description": "When not simplifying the response, data will be fetched in two steps. This parameter controls how long to wait (in seconds) before trying the second step.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
      "name": "dropcontactApi",
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
