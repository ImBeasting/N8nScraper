---
title: "Node: Home Assistant"
slug: "node-homeassistant"
version: "1"
updated: "2026-01-08"
summary: "Consume Home Assistant API"
node_type: "regular"
group: "['output']"
---

# Node: Home Assistant

**Purpose.** Consume Home Assistant API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:homeAssistant.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **homeAssistantApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `homeAssistantApi` | ✓ | - |

---

## Operations

### Cameraproxy Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Screenshot | `getScreenshot` | Get the camera screenshot |

### Config Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get the configuration |
| Check Configuration | `check` | Check the configuration |

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an event |
| Get Many | `getAll` | Get many events |

### History Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many state changes |

### Log Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Error Logs | `getErroLogs` | Get a log for a specific entity |
| Get Logbook Entries | `getLogbookEntries` | Get all logs |

### Service Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Call | `call` | Call a service within a specific domain |
| Get Many | `getAll` | Get many services |

### State Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Get | `get` | Get a state for a specific entity |
| Get Many | `getAll` | Get many states |

### Template Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a template |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | config | ✗ | Resource to operate on |  |

**Resource options:**

* **Camera Proxy** (`cameraProxy`)
* **Config** (`config`)
* **Event** (`event`)
* **History** (`history`)
* **Log** (`log`)
* **Service** (`service`)
* **State** (`state`)
* **Template** (`template`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getScreenshot | ✗ | Get the camera screenshot |  |

**Operation options:**

* **Get Screenshot** (`getScreenshot`) - Get the camera screenshot

---

### Get Screenshot parameters (`getScreenshot`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Camera Entity Name or ID | `cameraEntityId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Entity Name or ID | `entityId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Event Type | `eventType` | string |  | ✓ | The Entity ID for which an event will be created |  |
| Event Attributes | `eventAttributes` | fixedCollection | {} | ✗ | Name of the attribute | e.g. Add Attribute |  |

<details>
<summary><strong>Event Attributes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attributes | `attributes` |  |  |  |

</details>

| Template | `template` | string |  | ✓ | Render a Home Assistant template. <a href="https://www.home-assistant.io/docs/configuration/templating/">See template docs for more information.</a>. |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The end of the period | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| End Time | `endTime` | dateTime |  | The end of the period |
| Entity IDs | `entityIds` | string |  | The entities IDs separated by comma |
| Minimal Response | `minimalResponse` | boolean | False | Whether to only return <code>last_changed</code> and state for states |
| Significant Changes Only | `significantChangesOnly` | boolean | False | Whether to only return significant state changes |
| Start Time | `startTime` | dateTime |  | The beginning of the period |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |

### Get Logbook Entries parameters (`getLogbookEntries`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The end of the period | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| End Time | `endTime` | dateTime |  | The end of the period |
| Entity ID | `entityId` | string |  |  |
| Start Time | `startTime` | dateTime |  | The beginning of the period |

</details>


### Call parameters (`call`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Domain Name or ID | `domain` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Service Name or ID | `service` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Service Attributes | `serviceAttributes` | fixedCollection | {} | ✗ | Name of the field | e.g. Add Attribute |  |

<details>
<summary><strong>Service Attributes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attributes | `attributes` |  |  |  |

</details>


### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Entity Name or ID | `entityId` | options |  | ✓ | The entity ID for which a state will be created. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| State | `state` | string |  | ✓ |  |  |
| State Attributes | `stateAttributes` | fixedCollection | {} | ✗ | Name of the attribute | e.g. Add Attribute |  |

<details>
<summary><strong>State Attributes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attributes | `attributes` |  |  |  |

</details>


---

## Load Options Methods

- `getAllEntities`

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
* Categories: Miscellaneous

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: homeAssistant
displayName: Home Assistant
description: Consume Home Assistant API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: homeAssistantApi
  required: true
operations:
- id: getScreenshot
  name: Get Screenshot
  description: Get the camera screenshot
  params:
  - id: cameraEntityId
    name: Camera Entity Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - getScreenshot
          resource:
          - cameraProxy
    typeInfo:
      type: options
      displayName: Camera Entity Name or ID
      name: cameraEntityId
      typeOptions:
        loadOptionsMethod: getCameraEntities
      possibleValues: []
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - getScreenshot
          resource:
          - cameraProxy
    typeInfo:
      type: string
      displayName: Put Output File in Field
      name: binaryPropertyName
- id: get
  name: Get
  description: Get the configuration
  params:
  - id: entityId
    name: Entity Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - upsert
          resource:
          - state
    typeInfo: &id006
      type: options
      displayName: Entity Name or ID
      name: entityId
      typeOptions:
        loadOptionsMethod: getAllEntities
      possibleValues: []
- id: check
  name: Check Configuration
  description: Check the configuration
- id: create
  name: Create
  description: Create an event
  params:
  - id: eventType
    name: Event Type
    type: string
    default: ''
    required: true
    description: The Entity ID for which an event will be created
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - event
    typeInfo:
      type: string
      displayName: Event Type
      name: eventType
  - id: eventAttributes
    name: Event Attributes
    type: fixedCollection
    default: {}
    required: false
    description: Name of the attribute
    placeholder: Add Attribute
    validation:
      displayOptions:
        show:
          resource:
          - event
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Event Attributes
      name: eventAttributes
      typeOptions:
        multipleValues: true
      subProperties:
      - name: attributes
        displayName: Attributes
        values:
        - displayName: Name
          name: name
          type: string
          description: Name of the attribute
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value of the attribute
          default: ''
  - id: template
    name: Template
    type: string
    default: ''
    required: true
    description: Render a Home Assistant template. <a href="https://www.home-assistant.io/docs/configuration/templating/">See
      template docs for more information.</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - template
          operation:
          - create
    typeInfo:
      type: string
      displayName: Template
      name: template
- id: getAll
  name: Get Many
  description: Get many events
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
          operation:
          - getAll
          resource:
          - state
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
          operation:
          - getAll
          resource:
          - state
          returnAll:
          - false
    typeInfo: &id004
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
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
- id: getErroLogs
  name: Get Error Logs
  description: Get a log for a specific entity
- id: getLogbookEntries
  name: Get Logbook Entries
  description: Get all logs
  params: []
- id: call
  name: Call
  description: Call a service within a specific domain
  params:
  - id: domain
    name: Domain Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - service
          operation:
          - call
    typeInfo:
      type: options
      displayName: Domain Name or ID
      name: domain
      typeOptions:
        loadOptionsMethod: getDomains
      possibleValues: []
  - id: service
    name: Service Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - service
          operation:
          - call
    typeInfo:
      type: options
      displayName: Service Name or ID
      name: service
      typeOptions:
        loadOptionsMethod: getDomainServices
      possibleValues: []
  - id: serviceAttributes
    name: Service Attributes
    type: fixedCollection
    default: {}
    required: false
    description: Name of the field
    placeholder: Add Attribute
    validation:
      displayOptions:
        show:
          resource:
          - service
          operation:
          - call
    typeInfo:
      type: fixedCollection
      displayName: Service Attributes
      name: serviceAttributes
      typeOptions:
        multipleValues: true
      subProperties:
      - name: attributes
        displayName: Attributes
        values:
        - displayName: Name
          name: name
          type: string
          description: Name of the field
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value of the field
          default: ''
- id: upsert
  name: Create or Update
  description: Create a new record, or update the current one if it already exists
    (upsert)
  params:
  - id: entityId
    name: Entity Name or ID
    type: options
    default: ''
    required: true
    description: The entity ID for which a state will be created. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id005
    typeInfo: *id006
  - id: state
    name: State
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - state
          operation:
          - upsert
    typeInfo:
      type: string
      displayName: State
      name: state
  - id: stateAttributes
    name: State Attributes
    type: fixedCollection
    default: {}
    required: false
    description: Name of the attribute
    placeholder: Add Attribute
    validation:
      displayOptions:
        show:
          resource:
          - state
          operation:
          - upsert
    typeInfo:
      type: fixedCollection
      displayName: State Attributes
      name: stateAttributes
      typeOptions:
        multipleValues: true
      subProperties:
      - name: attributes
        displayName: Attributes
        values:
        - displayName: Name
          name: name
          type: string
          description: Name of the attribute
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value of the attribute
          default: ''
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
  - field: eventAttributes
    text: Add Attribute
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: serviceAttributes
    text: Add Attribute
  - field: stateAttributes
    text: Add Attribute
  hints:
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/homeAssistant.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Home Assistant Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "getScreenshot",
        "get",
        "check",
        "create",
        "getAll",
        "getErroLogs",
        "getLogbookEntries",
        "call",
        "upsert"
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
            "cameraProxy",
            "config",
            "event",
            "history",
            "log",
            "service",
            "state",
            "template"
          ],
          "default": "config"
        },
        "operation": {
          "description": "Create a template",
          "type": "string",
          "enum": [
            "create"
          ],
          "default": "create"
        },
        "cameraEntityId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
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
        "eventType": {
          "description": "The Entity ID for which an event will be created",
          "type": "string",
          "default": ""
        },
        "eventAttributes": {
          "description": "Name of the attribute",
          "type": "string",
          "default": {},
          "examples": [
            "Add Attribute"
          ]
        },
        "additionalFields": {
          "description": "The end of the period",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "domain": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "service": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "serviceAttributes": {
          "description": "Name of the field",
          "type": "string",
          "default": {},
          "examples": [
            "Add Attribute"
          ]
        },
        "entityId": {
          "description": "The entity ID for which a state will be created. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "state": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "stateAttributes": {
          "description": "Name of the attribute",
          "type": "string",
          "default": {},
          "examples": [
            "Add Attribute"
          ]
        },
        "template": {
          "description": "Render a Home Assistant template. <a href=\"https://www.home-assistant.io/docs/configuration/templating/\">See template docs for more information.</a>.",
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
      "name": "homeAssistantApi",
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
