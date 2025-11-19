---
title: "Node: PostHog"
slug: "node-posthog"
version: "1"
updated: "2025-11-13"
summary: "Consume PostHog API"
node_type: "regular"
group: "['input']"
---

# Node: PostHog

**Purpose.** Consume PostHog API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:postHog.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **postHogApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `postHogApi` | ✓ | - |

---

## API Patterns

**Common Endpoints:**
- `{base}{path}`

**Headers Used:** Content-Type

---

## Operations

### Alias Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an alias |

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an event |

### Identity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an identity |

### Track Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Page | `page` | Track a page |
| Screen | `screen` | Track a screen |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | event | ✗ | Resource to operate on |  |

**Resource options:**

* **Alias** (`alias`)
* **Event** (`event`)
* **Identity** (`identity`)
* **Track** (`track`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create an alias |  |

**Operation options:**

* **Create** (`create`) - Create an alias

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Alias | `alias` | string |  | ✓ | The name of the alias |  |
| Distinct ID | `distinctId` | string |  | ✓ | The user's distinct ID |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | If not set, it'll automatically be set to the current time | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Context | `contextUi` | fixedCollection | {} |  |
| Timestamp | `timestamp` | dateTime |  | If not set, it'll automatically be set to the current time |

</details>

| Event | `eventName` | string |  | ✓ | The name of the event |  |
| Distinct ID | `distinctId` | string |  | ✓ | The user's distinct ID |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | If not set, it'll automatically be set to the current time | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Properties | `propertiesUi` | fixedCollection | {} |  |
| Timestamp | `timestamp` | dateTime |  | If not set, it'll automatically be set to the current time |

</details>

| Distinct ID | `distinctId` | string |  | ✓ | The identity's distinct ID |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | If not set, it'll automatically be set to the current time | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Properties | `propertiesUi` | fixedCollection | {} |  |
| Message ID | `messageId` | string |  |  |
| Timestamp | `timestamp` | dateTime |  | If not set, it'll automatically be set to the current time |

</details>


### Page parameters (`page`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ |  |  |
| Distinct ID | `distinctId` | string |  | ✓ | The user's distinct ID |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | If not set, it'll automatically be set to the current time | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Category | `category` | string |  |  |
| Context | `contextUi` | fixedCollection | {} |  |
| Message ID | `messageId` | string |  |  |
| Properties | `propertiesUi` | fixedCollection | {} |  |
| Timestamp | `timestamp` | dateTime |  | If not set, it'll automatically be set to the current time |

</details>


### Screen parameters (`screen`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ |  |  |
| Distinct ID | `distinctId` | string |  | ✓ | The user's distinct ID |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | If not set, it'll automatically be set to the current time | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Category | `category` | string |  |  |
| Context | `contextUi` | fixedCollection | {} |  |
| Message ID | `messageId` | string |  |  |
| Properties | `propertiesUi` | fixedCollection | {} |  |
| Timestamp | `timestamp` | dateTime |  | If not set, it'll automatically be set to the current time |

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
* Categories: Analytics, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: postHog
displayName: PostHog
description: Consume PostHog API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: postHogApi
  required: true
operations:
- id: create
  name: Create
  description: Create an alias
  params:
  - id: alias
    name: Alias
    type: string
    default: ''
    required: true
    description: The name of the alias
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - alias
          operation:
          - create
    typeInfo:
      type: string
      displayName: Alias
      name: alias
  - id: distinctId
    name: Distinct ID
    type: string
    default: ''
    required: true
    description: The user's distinct ID
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - track
          operation:
          - page
          - screen
    typeInfo: &id002
      type: string
      displayName: Distinct ID
      name: distinctId
  - id: eventName
    name: Event
    type: string
    default: ''
    required: true
    description: The name of the event
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - event
          operation:
          - create
    typeInfo:
      type: string
      displayName: Event
      name: eventName
  - id: distinctId
    name: Distinct ID
    type: string
    default: ''
    required: true
    description: The user's distinct ID
    validation: *id001
    typeInfo: *id002
  - id: distinctId
    name: Distinct ID
    type: string
    default: ''
    required: true
    description: The identity's distinct ID
    validation: *id001
    typeInfo: *id002
- id: page
  name: Page
  description: Track a page
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - track
          operation:
          - page
          - screen
    typeInfo: &id004
      type: string
      displayName: Name
      name: name
  - id: distinctId
    name: Distinct ID
    type: string
    default: ''
    required: true
    description: The user's distinct ID
    validation: *id001
    typeInfo: *id002
- id: screen
  name: Screen
  description: Track a screen
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: distinctId
    name: Distinct ID
    type: string
    default: ''
    required: true
    description: The user's distinct ID
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints:
  - '{base}{path}'
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
  "$id": "https://n8n.io/schemas/nodes/postHog.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "PostHog Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "page",
        "screen"
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
            "alias",
            "event",
            "identity",
            "track"
          ],
          "default": "event"
        },
        "operation": {
          "description": "Track a page",
          "type": "string",
          "enum": [
            "page",
            "screen"
          ],
          "default": "page"
        },
        "alias": {
          "description": "The name of the alias",
          "type": "string",
          "default": ""
        },
        "distinctId": {
          "description": "The user's distinct ID",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "If not set, it'll automatically be set to the current time",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "eventName": {
          "description": "The name of the event",
          "type": "string",
          "default": ""
        },
        "name": {
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
      "name": "postHogApi",
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
