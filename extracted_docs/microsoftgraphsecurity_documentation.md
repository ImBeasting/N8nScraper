---
title: "Node: Microsoft Graph Security"
slug: "node-microsoftgraphsecurity"
version: "1"
updated: "2025-11-13"
summary: "Consume the Microsoft Graph Security API"
node_type: "regular"
group: "['transform']"
---

# Node: Microsoft Graph Security

**Purpose.** Consume the Microsoft Graph Security API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:microsoftGraph.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftGraphSecurityOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `microsoftGraphSecurityOAuth2Api` | ✓ | - |

---

## Operations

### Securescorecontrolprofile Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a secure score control profile |
| Get Many | `getAll` | Get many secure score control profiles |
| Update | `update` | Update a secure score control profile |

### Securescore Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a secure score |
| Get Many | `getAll` | Get many secure scores |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | secureScore | ✗ | Resource to operate on |  |

**Resource options:**

* **Secure Score** (`secureScore`)
* **Secure Score Control Profile** (`secureScoreControlProfile`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Get** (`get`) - Get a secure score control profile
* **Get Many** (`getAll`) - Get many secure score control profiles
* **Update** (`update`) - Update a secure score control profile

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Secure Score Control Profile ID | `secureScoreControlProfileId` | string |  | ✓ | ID of the secure score control profile to retrieve |  |
| Secure Score ID | `secureScoreId` | string |  | ✓ | ID of the secure score to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">Query parameter</a> to filter results by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filter Query Parameter | `filter` | string |  | <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">Query parameter</a> to filter results by |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">Query parameter</a> to filter results by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filter Query Parameter | `filter` | string |  | <a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter">Query parameter</a> to filter results by |
| Include Control Scores | `includeControlScores` | boolean | False |  |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Secure Score Control Profile ID | `secureScoreControlProfileId` | string |  | ✓ | ID of the secure score control profile to update |  |
| Provider | `provider` | string |  | ✓ | Name of the provider of the security product or service | e.g. SecureScore |  |
| Vendor | `vendor` | string |  | ✓ | Name of the vendor of the security product or service | e.g. Microsoft |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Analyst driven setting on the control | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| State | `state` | options | Default | Analyst driven setting on the control |

</details>


---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Microsoft Graph Security

**From workflow:** Microsoft GraphSecurity SecureScoreControlProfile GetAll Test

**Parameters:**
```json
{
  "resource": "secureScoreControlProfile",
  "operation": "getAll",
  "returnAll": true
}
```

**Credentials:**
- microsoftGraphSecurityOAuth2Api: `Microsoft Graph Security OAuth2`

### Example 2: Microsoft Graph Security

**From workflow:** Microsoft GraphSecurity SecureScoreControlProfile Get Test

**Parameters:**
```json
{
  "resource": "secureScoreControlProfile",
  "operation": "get",
  "secureScoreControlProfileId": "test-control-profile-id"
}
```

**Credentials:**
- microsoftGraphSecurityOAuth2Api: `Microsoft Graph Security OAuth2`

### Example 3: Microsoft Graph Security

**From workflow:** Microsoft GraphSecurity SecureScoreControlProfile Update Test

**Parameters:**
```json
{
  "resource": "secureScoreControlProfile",
  "operation": "update",
  "secureScoreControlProfileId": "test-control-profile-id",
  "provider": "Microsoft",
  "vendor": "Microsoft",
  "updateFields": {
    "state": "Ignored"
  }
}
```

**Credentials:**
- microsoftGraphSecurityOAuth2Api: `Microsoft Graph Security OAuth2`

### Example 4: Microsoft Graph Security

**From workflow:** Microsoft GraphSecurity SecureScore GetAll Test

**Parameters:**
```json
{
  "resource": "secureScore",
  "operation": "getAll",
  "returnAll": true
}
```

**Credentials:**
- microsoftGraphSecurityOAuth2Api: `Microsoft Graph Security OAuth2`

### Example 5: Microsoft Graph Security

**From workflow:** Microsoft GraphSecurity SecureScore Get Test

**Parameters:**
```json
{
  "resource": "secureScore",
  "operation": "get",
  "secureScoreId": "test-secure-score-id"
}
```

**Credentials:**
- microsoftGraphSecurityOAuth2Api: `Microsoft Graph Security OAuth2`


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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: microsoftGraphSecurity
displayName: Microsoft Graph Security
description: Consume the Microsoft Graph Security API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: microsoftGraphSecurityOAuth2Api
  required: true
operations:
- id: get
  name: Get
  description: ''
  params:
  - id: secureScoreControlProfileId
    name: Secure Score Control Profile ID
    type: string
    default: ''
    required: true
    description: ID of the secure score control profile to retrieve
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - secureScoreControlProfile
          operation:
          - update
    typeInfo: &id006
      type: string
      displayName: Secure Score Control Profile ID
      name: secureScoreControlProfileId
  - id: secureScoreId
    name: Secure Score ID
    type: string
    default: ''
    required: true
    description: ID of the secure score to retrieve
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - secureScore
          operation:
          - get
    typeInfo:
      type: string
      displayName: Secure Score ID
      name: secureScoreId
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id001
      displayOptions:
        show:
          resource:
          - secureScore
          operation:
          - getAll
    typeInfo: &id002
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id003
      displayOptions:
        show:
          resource:
          - secureScore
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id004
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 1000
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
- id: update
  name: Update
  description: ''
  params:
  - id: secureScoreControlProfileId
    name: Secure Score Control Profile ID
    type: string
    default: ''
    required: true
    description: ID of the secure score control profile to update
    validation: *id005
    typeInfo: *id006
  - id: provider
    name: Provider
    type: string
    default: ''
    required: true
    description: Name of the provider of the security product or service
    placeholder: SecureScore
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - secureScoreControlProfile
          operation:
          - update
    typeInfo:
      type: string
      displayName: Provider
      name: provider
  - id: vendor
    name: Vendor
    type: string
    default: ''
    required: true
    description: Name of the vendor of the security product or service
    placeholder: Microsoft
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - secureScoreControlProfile
          operation:
          - update
    typeInfo:
      type: string
      displayName: Vendor
      name: vendor
examples:
- name: Microsoft Graph Security
  parameters:
    resource: secureScoreControlProfile
    operation: getAll
    returnAll: true
  workflow: Microsoft GraphSecurity SecureScoreControlProfile GetAll Test
- name: Microsoft Graph Security
  parameters:
    resource: secureScoreControlProfile
    operation: get
    secureScoreControlProfileId: test-control-profile-id
  workflow: Microsoft GraphSecurity SecureScoreControlProfile Get Test
- name: Microsoft Graph Security
  parameters:
    resource: secureScoreControlProfile
    operation: update
    secureScoreControlProfileId: test-control-profile-id
    provider: Microsoft
    vendor: Microsoft
    updateFields:
      state: Ignored
  workflow: Microsoft GraphSecurity SecureScoreControlProfile Update Test
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
  - field: filters
    text: Add Filter
  - field: provider
    text: SecureScore
  - field: vendor
    text: Microsoft
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/microsoftGraphSecurity.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft Graph Security Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
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
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "secureScore",
            "secureScoreControlProfile"
          ],
          "default": "secureScore"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "get",
            "getAll"
          ],
          "default": "get"
        },
        "secureScoreControlProfileId": {
          "description": "ID of the secure score control profile to update",
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
        "filters": {
          "description": "<a href=\"https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter\">Query parameter</a> to filter results by",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "provider": {
          "description": "Name of the provider of the security product or service",
          "type": "string",
          "default": "",
          "examples": [
            "SecureScore"
          ]
        },
        "vendor": {
          "description": "Name of the vendor of the security product or service",
          "type": "string",
          "default": "",
          "examples": [
            "Microsoft"
          ]
        },
        "updateFields": {
          "description": "Analyst driven setting on the control",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "secureScoreId": {
          "description": "ID of the secure score to retrieve",
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
      "name": "microsoftGraphSecurityOAuth2Api",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Microsoft Graph Security",
      "value": {
        "resource": "secureScoreControlProfile",
        "operation": "getAll",
        "returnAll": true
      }
    },
    {
      "description": "Microsoft Graph Security",
      "value": {
        "resource": "secureScoreControlProfile",
        "operation": "get",
        "secureScoreControlProfileId": "test-control-profile-id"
      }
    },
    {
      "description": "Microsoft Graph Security",
      "value": {
        "resource": "secureScoreControlProfile",
        "operation": "update",
        "secureScoreControlProfileId": "test-control-profile-id",
        "provider": "Microsoft",
        "vendor": "Microsoft",
        "updateFields": {
          "state": "Ignored"
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
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
