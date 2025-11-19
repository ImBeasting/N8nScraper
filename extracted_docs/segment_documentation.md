---
title: "Node: Segment"
slug: "node-segment"
version: "1"
updated: "2025-11-13"
summary: "Consume Segment API"
node_type: "regular"
group: "['output']"
---

# Node: Segment

**Purpose.** Consume Segment API
**Subtitle.** ={{$parameter["operation"] + ":" + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:segment.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **segmentApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `segmentApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Group Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a user to a group |

### Identify Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an identity |

### Track Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Event | `event` | Record the actions your users perform. Every action triggers an event, which can also have associated properties. |
| Page | `page` | Record page views on your website, along with optional extra information about the page being viewed |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | identify | ✗ | Group lets you associate an identified user with a group |  |

**Resource options:**

* **Group** (`group`) - Group lets you associate an identified user with a group
* **Identify** (`identify`) - Identify lets you tie a user to their actions
* **Track** (`track`) - Track lets you record events

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | add | ✗ | Add a user to a group |  |

**Operation options:**

* **Add** (`add`) - Add a user to a group

---

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✗ |  |  |
| Group ID | `groupId` | string |  | ✓ | A Group ID is the unique identifier which you recognize a group by in your own database |  |
| Traits | `traits` | fixedCollection | {} | ✗ | e.g. Add Trait |  |

<details>
<summary><strong>Traits sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Trait | `traitsUi` |  |  |  |

</details>

| Context | `context` | fixedCollection | {} | ✗ | Whether a user is active | e.g. Add Context |  |

<details>
<summary><strong>Context sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Context | `contextUi` |  |  |  |

</details>

| Integration | `integrations` | fixedCollection | {} | ✗ | e.g. Add Integration |  |

<details>
<summary><strong>Integration sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Integration | `integrationsUi` |  |  |  |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✗ |  |  |
| Traits | `traits` | fixedCollection | {} | ✗ | e.g. Add Trait |  |

<details>
<summary><strong>Traits sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Trait | `traitsUi` |  |  |  |

</details>

| Context | `context` | fixedCollection | {} | ✗ | Whether a user is active | e.g. Add Context |  |

<details>
<summary><strong>Context sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Context | `contextUi` |  |  |  |

</details>

| Integration | `integrations` | fixedCollection | {} | ✗ | e.g. Add Integration |  |

<details>
<summary><strong>Integration sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Integration | `integrationsUi` |  |  |  |

</details>


### Event parameters (`event`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✗ |  |  |
| Event | `event` | string |  | ✓ | Name of the action that a user has performed |  |
| Context | `context` | fixedCollection | {} | ✗ | Whether a user is active | e.g. Add Context |  |

<details>
<summary><strong>Context sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Context | `contextUi` |  |  |  |

</details>

| Integration | `integrations` | fixedCollection | {} | ✗ | e.g. Add Integration |  |

<details>
<summary><strong>Integration sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Integration | `integrationsUi` |  |  |  |

</details>

| Properties | `properties` | fixedCollection | {} | ✗ | e.g. Add Properties |  |

<details>
<summary><strong>Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Property | `propertiesUi` |  |  |  |

</details>


### Page parameters (`page`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✗ |  |  |
| Name | `name` | string |  | ✗ | Name of the page For example, most sites have a “Signup” page that can be useful to tag, so you can see users as they move through your funnel |  |
| Context | `context` | fixedCollection | {} | ✗ | Whether a user is active | e.g. Add Context |  |

<details>
<summary><strong>Context sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Context | `contextUi` |  |  |  |

</details>

| Integration | `integrations` | fixedCollection | {} | ✗ | e.g. Add Integration |  |

<details>
<summary><strong>Integration sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Integration | `integrationsUi` |  |  |  |

</details>

| Properties | `properties` | fixedCollection | {} | ✗ | e.g. Add Properties |  |

<details>
<summary><strong>Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Property | `propertiesUi` |  |  |  |

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
* Categories: Analytics, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: segment
displayName: Segment
description: Consume Segment API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: segmentApi
  required: true
operations:
- id: add
  name: Add
  description: Add a user to a group
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: false
    description: ''
    validation: &id001
      displayOptions:
        show:
          resource:
          - track
          operation:
          - page
    typeInfo: &id002
      type: string
      displayName: User ID
      name: userId
  - id: groupId
    name: Group ID
    type: string
    default: ''
    required: true
    description: A Group ID is the unique identifier which you recognize a group by
      in your own database
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - group
          operation:
          - add
    typeInfo:
      type: string
      displayName: Group ID
      name: groupId
  - id: traits
    name: Traits
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Trait
    validation: &id003
      displayOptions:
        show:
          resource:
          - identify
          operation:
          - create
    typeInfo: &id004
      type: fixedCollection
      displayName: Traits
      name: traits
      typeOptions:
        multipleValues: true
      subProperties:
      - name: traitsUi
        displayName: Trait
        values:
        - displayName: Key
          name: key
          type: string
          default: ''
        - displayName: Value
          name: value
          type: string
          default: ''
  - id: context
    name: Context
    type: fixedCollection
    default: {}
    required: false
    description: Whether a user is active
    placeholder: Add Context
    validation: &id005
      displayOptions:
        show:
          resource:
          - track
          operation:
          - page
    typeInfo: &id006
      type: fixedCollection
      displayName: Context
      name: context
      typeOptions:
        multipleValues: false
      subProperties:
      - name: contextUi
        displayName: Context
        values:
        - displayName: Active
          name: active
          type: boolean
          description: Whether a user is active
          default: false
        - displayName: IP
          name: ip
          type: string
          description: Current user’s IP address
          default: ''
        - displayName: Locale
          name: locate
          type: string
          description: Locale string for the current user, for example en-US
          default: ''
        - displayName: Page
          name: page
          type: string
          description: Dictionary of information about the current page in the browser,
            containing hash, path, referrer, search, title and URL
          default: ''
        - displayName: Timezone
          name: timezone
          type: string
          description: Timezones are sent as tzdata strings to add user timezone information
            which might be stripped from the timestamp, for example America/New_York
          default: ''
        - displayName: App
          name: app
          type: fixedCollection
          placeholder: Add App
          default: {}
          options:
          - name: appUi
            displayName: App
            values:
            - displayName: Name
              name: name
              type: string
              default: ''
            - displayName: Version
              name: version
              type: string
              default: ''
            - displayName: Build
              name: build
              type: string
              default: ''
          typeOptions:
            multipleValues: false
        - displayName: Campaign
          name: campaign
          type: fixedCollection
          placeholder: Campaign App
          default: {}
          options:
          - name: campaignUi
            displayName: Campaign
            values:
            - displayName: Name
              name: name
              type: string
              default: ''
            - displayName: Source
              name: source
              type: string
              default: ''
            - displayName: Medium
              name: medium
              type: string
              default: ''
            - displayName: Term
              name: term
              type: string
              default: ''
            - displayName: Content
              name: content
              type: string
              default: ''
          typeOptions:
            multipleValues: false
        - displayName: Device
          name: device
          type: fixedCollection
          placeholder: Add Device
          default: {}
          options:
          - name: deviceUi
            displayName: Device
            values:
            - displayName: ID
              name: id
              type: string
              default: ''
            - displayName: Manufacturer
              name: manufacturer
              type: string
              default: ''
            - displayName: Model
              name: model
              type: string
              default: ''
            - displayName: Name
              name: name
              type: string
              default: ''
            - displayName: Type
              name: type
              type: string
              default: ''
            - displayName: Version
              name: version
              type: string
              default: ''
          typeOptions:
            multipleValues: false
  - id: integrations
    name: Integration
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Integration
    validation: &id007
      displayOptions:
        show:
          resource:
          - track
          operation:
          - page
    typeInfo: &id008
      type: fixedCollection
      displayName: Integration
      name: integrations
      typeOptions:
        multipleValues: false
      subProperties:
      - name: integrationsUi
        displayName: Integration
        values:
        - displayName: All
          name: all
          type: boolean
          default: true
        - displayName: Salesforce
          name: salesforce
          type: boolean
          default: false
- id: create
  name: Create
  description: Create an identity
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: traits
    name: Traits
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Trait
    validation: *id003
    typeInfo: *id004
  - id: context
    name: Context
    type: fixedCollection
    default: {}
    required: false
    description: Whether a user is active
    placeholder: Add Context
    validation: *id005
    typeInfo: *id006
  - id: integrations
    name: Integration
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Integration
    validation: *id007
    typeInfo: *id008
- id: event
  name: Event
  description: Record the actions your users perform. Every action triggers an event,
    which can also have associated properties.
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: event
    name: Event
    type: string
    default: ''
    required: true
    description: Name of the action that a user has performed
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - track
          operation:
          - event
    typeInfo:
      type: string
      displayName: Event
      name: event
  - id: context
    name: Context
    type: fixedCollection
    default: {}
    required: false
    description: Whether a user is active
    placeholder: Add Context
    validation: *id005
    typeInfo: *id006
  - id: integrations
    name: Integration
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Integration
    validation: *id007
    typeInfo: *id008
  - id: properties
    name: Properties
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Properties
    validation: &id009
      displayOptions:
        show:
          resource:
          - track
          operation:
          - page
    typeInfo: &id010
      type: fixedCollection
      displayName: Properties
      name: properties
      typeOptions:
        multipleValues: true
      subProperties:
      - name: propertiesUi
        displayName: Property
        values:
        - displayName: Key
          name: key
          type: string
          default: ''
        - displayName: Value
          name: value
          type: string
          default: ''
- id: page
  name: Page
  description: Record page views on your website, along with optional extra information
    about the page being viewed
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: name
    name: Name
    type: string
    default: ''
    required: false
    description: Name of the page For example, most sites have a “Signup” page that
      can be useful to tag, so you can see users as they move through your funnel
    validation:
      displayOptions:
        show:
          resource:
          - track
          operation:
          - page
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: context
    name: Context
    type: fixedCollection
    default: {}
    required: false
    description: Whether a user is active
    placeholder: Add Context
    validation: *id005
    typeInfo: *id006
  - id: integrations
    name: Integration
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Integration
    validation: *id007
    typeInfo: *id008
  - id: properties
    name: Properties
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Properties
    validation: *id009
    typeInfo: *id010
common_expressions:
- ={{$parameter["operation"] + ":" + $parameter["resource"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: traits
    text: Add Trait
  - field: context
    text: Add Context
  - field: integrations
    text: Add Integration
  - field: traits
    text: Add Trait
  - field: context
    text: Add Context
  - field: integrations
    text: Add Integration
  - field: context
    text: Add Context
  - field: integrations
    text: Add Integration
  - field: properties
    text: Add Properties
  - field: context
    text: Add Context
  - field: integrations
    text: Add Integration
  - field: properties
    text: Add Properties
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
  "$id": "https://n8n.io/schemas/nodes/segment.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Segment Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "add",
        "create",
        "event",
        "page"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Group lets you associate an identified user with a group",
          "type": "string",
          "enum": [
            "group",
            "identify",
            "track"
          ],
          "default": "identify"
        },
        "operation": {
          "description": "Record the actions your users perform. Every action triggers an event, which can also have associated properties.",
          "type": "string",
          "enum": [
            "event",
            "page"
          ],
          "default": "event"
        },
        "userId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "groupId": {
          "description": "A Group ID is the unique identifier which you recognize a group by in your own database",
          "type": "string",
          "default": ""
        },
        "traits": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Trait"
          ]
        },
        "context": {
          "description": "Whether a user is active",
          "type": "string",
          "default": {},
          "examples": [
            "Add Context"
          ]
        },
        "integrations": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Integration"
          ]
        },
        "event": {
          "description": "Name of the action that a user has performed",
          "type": "string",
          "default": ""
        },
        "properties": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Properties"
          ]
        },
        "name": {
          "description": "Name of the page For example, most sites have a \u201cSignup\u201d page that can be useful to tag, so you can see users as they move through your funnel",
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
      "name": "segmentApi",
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
