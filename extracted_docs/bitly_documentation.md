---
title: "Node: Bitly"
slug: "node-bitly"
version: "1"
updated: "2026-01-08"
summary: "Consume Bitly API"
node_type: "regular"
group: "['output']"
---

# Node: Bitly

**Purpose.** Consume Bitly API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:bitly.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **bitlyApi**: N/A
- **bitlyOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `bitlyApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `bitlyOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Link Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a link |
| Get | `get` | Get a link |
| Update | `update` | Update a link |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | link | ✗ | Resource to operate on |  |

**Resource options:**

* **Link** (`link`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a link |  |

**Operation options:**

* **Create** (`create`) - Create a link
* **Get** (`get`) - Get a link
* **Update** (`update`) - Update a link

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Long URL | `longUrl` | string |  | ✓ | e.g. https://example.com | url |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Domain | `domain` | string | bit.ly |  |
| Group Name or ID | `group` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Title | `title` | string |  |  |

</details>

| Deeplinks | `deeplink` | fixedCollection | {} | ✗ | e.g. Add Deep Link |  |

<details>
<summary><strong>Deeplinks sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Deep Link | `deeplinkUi` |  |  |  |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bitlink | `id` | string |  | ✓ | e.g. bit.ly/22u3ypK |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bitlink | `id` | string |  | ✓ | e.g. bit.ly/22u3ypK |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Archived | `archived` | boolean | False |  |
| Group Name or ID | `group` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Long URL | `longUrl` | string |  |  |
| Tag Names or IDs | `tags` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Title | `title` | string |  |  |

</details>

| Deeplinks | `deeplink` | fixedCollection | {} | ✗ | e.g. Add Deep Link |  |

<details>
<summary><strong>Deeplinks sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Deep Link | `deeplinkUi` |  |  |  |

</details>


---

## Load Options Methods

- `getGroups`
- `for`
- `name`
- `value`

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
* Categories: Utility

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: bitly
displayName: Bitly
description: Consume Bitly API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: bitlyApi
  required: true
- name: bitlyOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a link
  params:
  - id: longUrl
    name: Long URL
    type: string
    default: ''
    required: true
    description: ''
    placeholder: https://example.com
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - link
          operation:
          - create
    typeInfo:
      type: string
      displayName: Long URL
      name: longUrl
  - id: deeplink
    name: Deeplinks
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Deep Link
    validation: &id003
      displayOptions:
        show:
          resource:
          - link
          operation:
          - update
    typeInfo: &id004
      type: fixedCollection
      displayName: Deeplinks
      name: deeplink
      typeOptions:
        multipleValues: true
      subProperties:
      - name: deeplinkUi
        displayName: Deep Link
        values:
        - displayName: App ID
          name: appId
          type: string
          default: ''
        - displayName: App URI Path
          name: appUriPath
          type: string
          default: ''
        - displayName: Install Type
          name: installType
          type: string
          default: ''
        - displayName: Install URL
          name: installUrl
          type: string
          default: ''
- id: get
  name: Get
  description: Get a link
  params:
  - id: id
    name: Bitlink
    type: string
    default: ''
    required: true
    description: ''
    placeholder: bit.ly/22u3ypK
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - link
          operation:
          - get
    typeInfo: &id002
      type: string
      displayName: Bitlink
      name: id
- id: update
  name: Update
  description: Update a link
  params:
  - id: id
    name: Bitlink
    type: string
    default: ''
    required: true
    description: ''
    placeholder: bit.ly/22u3ypK
    validation: *id001
    typeInfo: *id002
  - id: deeplink
    name: Deeplinks
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Deep Link
    validation: *id003
    typeInfo: *id004
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
  - field: longUrl
    text: https://example.com
  - field: additionalFields
    text: Add Field
  - field: deeplink
    text: Add Deep Link
  - field: id
    text: bit.ly/22u3ypK
  - field: updateFields
    text: Add Field
  - field: deeplink
    text: Add Deep Link
  - field: id
    text: bit.ly/22u3ypK
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
  "$id": "https://n8n.io/schemas/nodes/bitly.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Bitly Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
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
            "link"
          ],
          "default": "link"
        },
        "operation": {
          "description": "Create a link",
          "type": "string",
          "enum": [
            "create",
            "get",
            "update"
          ],
          "default": "create"
        },
        "longUrl": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "url",
          "examples": [
            "https://example.com"
          ]
        },
        "additionalFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "deeplink": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Deep Link"
          ]
        },
        "id": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "bit.ly/22u3ypK"
          ]
        },
        "updateFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
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
      "name": "bitlyApi",
      "required": true
    },
    {
      "name": "bitlyOAuth2Api",
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
