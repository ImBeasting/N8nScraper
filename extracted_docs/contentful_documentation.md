---
title: "Node: Contentful"
slug: "node-contentful"
version: "1"
updated: "2026-01-08"
summary: "Consume Contentful API"
node_type: "regular"
group: "['input']"
---

# Node: Contentful

**Purpose.** Consume Contentful API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:contentful.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **contentfulApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `contentfulApi` | ✓ | - |

---

## Operations

### Resource.Value Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` |  |
| Get Many | `getAll` |  |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | entry | ✗ | Resource to operate on |  |
---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Operation to perform |  |

**Operation options:**

* **Get** (`get`)
* **Get Many** (`getAll`)

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Environment ID | `environmentId` | string | master | ✗ | The ID for the Contentful environment (e.g. master, staging, etc.). Depending on your plan, you might not have environments. In that case use "master". |  |
| Content Type ID | `contentTypeId` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether the data should be returned RAW instead of parsed | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| RAW Data | `rawData` | boolean | False | Whether the data should be returned RAW instead of parsed |

</details>

| Environment ID | `environmentId` | string | master | ✗ | The ID for the Contentful environment (e.g. master, staging, etc.). Depending on your plan, you might not have environments. In that case use "master". |  |
| Entry ID | `entryId` | string |  | ✓ |  |  |
| Asset ID | `assetId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Environment ID | `environmentId` | string | master | ✗ | The ID for the Contentful environment (e.g. master, staging, etc.). Depending on your plan, you might not have environments. In that case use "master". |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | To search for entries with a specific content type | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content Type ID | `content_type` | string |  | To search for entries with a specific content type |
| Equal | `equal` | string |  | Search for all data that matches the condition: {attribute}={value}. Attribute can use dot notation. |
| Exclude | `exclude` | string |  | Search for all data that matches the condition: {attribute}[nin]={value}. Attribute can use dot notation. |
| Exist | `exist` | string |  | Search for all data that matches the condition: {attribute}[exists]={value}. Attribute can use dot notation. |
| Fields | `select` | string |  | The select operator allows you to choose what fields to return from an entity. You can choose multiple values by combining comma-separated operators. |
| Include | `include` | string |  | Search for all data that matches the condition: {attribute}[in]={value}. Attribute can use dot notation. |
| Not Equal | `notEqual` | string |  | Search for all data that matches the condition: {attribute}[ne]={value}. Attribute can use dot notation. |
| Order | `order` | string |  | You can order items in the response by specifying the order search parameter. You can use sys properties (such as sys.createdAt) or field values (such as fields.myCustomDateField) for ordering. |
| Query | `query` | string |  | Full-text search is case insensitive and might return more results than expected. A query will only take values with more than 1 character. |
| RAW Data | `rawData` | boolean | False | Whether the data should be returned RAW instead of parsed |

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
* Categories: Marketing, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: contentful
displayName: Contentful
description: Consume Contentful API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: contentfulApi
  required: true
operations:
- id: get
  name: Get
  description: ''
  params:
  - id: environmentId
    name: Environment ID
    type: string
    default: master
    required: false
    description: The ID for the Contentful environment (e.g. master, staging, etc.).
      Depending on your plan, you might not have environments. In that case use "master".
    validation: &id001
      displayOptions:
        show:
          resource:
          - resource.value
          operation:
          - get
          - getAll
    typeInfo: &id002
      type: string
      displayName: Environment ID
      name: environmentId
  - id: contentTypeId
    name: Content Type ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - resource.value
          operation:
          - get
    typeInfo:
      type: string
      displayName: Content Type ID
      name: contentTypeId
  - id: environmentId
    name: Environment ID
    type: string
    default: master
    required: false
    description: The ID for the Contentful environment (e.g. master, staging, etc.).
      Depending on your plan, you might not have environments. In that case use "master".
    validation: *id001
    typeInfo: *id002
  - id: entryId
    name: Entry ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - resource.value
          operation:
          - get
    typeInfo:
      type: string
      displayName: Entry ID
      name: entryId
  - id: assetId
    name: Asset ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - resource.value
          operation:
          - get
    typeInfo:
      type: string
      displayName: Asset ID
      name: assetId
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: environmentId
    name: Environment ID
    type: string
    default: master
    required: false
    description: The ID for the Contentful environment (e.g. master, staging, etc.).
      Depending on your plan, you might not have environments. In that case use "master".
    validation: *id001
    typeInfo: *id002
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
          - getAll
          resource:
          - resource.value
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
          - getAll
          resource:
          - resource.value
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
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
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/contentful.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Contentful Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "source": {
          "description": "Pick where your data comes from, delivery or preview API",
          "type": "string",
          "enum": [
            "deliveryApi",
            "previewApi"
          ],
          "default": "deliveryApi"
        },
        "resource": {
          "description": "",
          "type": "string",
          "default": "entry"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "get",
            "getAll"
          ],
          "default": "getAll"
        },
        "environmentId": {
          "description": "The ID for the Contentful environment (e.g. master, staging, etc.). Depending on your plan, you might not have environments. In that case use \"master\".",
          "type": "string",
          "default": "master"
        },
        "contentTypeId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "To search for entries with a specific content type",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
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
        "entryId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "assetId": {
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
    "version": "1"
  },
  "credentials": [
    {
      "name": "contentfulApi",
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
