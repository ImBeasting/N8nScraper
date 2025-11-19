---
title: "Node: Vero"
slug: "node-vero"
version: "1"
updated: "2025-11-13"
summary: "Consume Vero API"
node_type: "regular"
group: "['output']"
---

# Node: Vero

**Purpose.** Consume Vero API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:vero.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **veroApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `veroApi` | ✓ | - |

---

## Operations

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Tags | `addTags` | Adds a tag to a users profile |
| Alias | `alias` | Change a users identifier |
| Create or Update | `create` | Create or update a user profile |
| Delete | `delete` | Delete a user |
| Re-Subscribe | `resubscribe` | Resubscribe a user |
| Remove Tags | `removeTags` | Removes a tag from a users profile |
| Unsubscribe | `unsubscribe` | Unsubscribe a user |

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Track | `track` | Track an event for a specific customer |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | user | ✗ | Create, update and manage the subscription status of your users |  |

**Resource options:**

* **User** (`user`) - Create, update and manage the subscription status of your users
* **Event** (`event`) - Track events based on actions your customers take in real time

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Adds a tag to a users profile |  |

**Operation options:**

* **Add Tags** (`addTags`) - Adds a tag to a users profile
* **Alias** (`alias`) - Change a users identifier
* **Create or Update** (`create`) - Create or update a user profile
* **Delete** (`delete`) - Delete a user
* **Re-Subscribe** (`resubscribe`) - Resubscribe a user
* **Remove Tags** (`removeTags`) - Removes a tag from a users profile
* **Unsubscribe** (`unsubscribe`) - Unsubscribe a user

---

### Add Tags parameters (`addTags`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The unique identifier of the user |  |
| Tags | `tags` | string |  | ✓ | Tags to add separated by "," |  |

### Alias parameters (`alias`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The old unique identifier of the user |  |
| New ID | `newId` | string |  | ✓ | The new unique identifier of the user |  |

### Create or Update parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The unique identifier of the customer |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The table to create the row in | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  | The table to create the row in |

</details>

| Data | `dataAttributesUi` | fixedCollection | {} | ✗ | Key value pairs that represent the custom user properties you want to update | e.g. Add Data |  |

<details>
<summary><strong>Data sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Data | `dataAttributesValues` |  |  |  |

</details>

| Data | `dataAttributesJson` | json |  | ✗ | Key value pairs that represent the custom user properties you want to update |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The unique identifier of the user |  |

### Re-Subscribe parameters (`resubscribe`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The unique identifier of the user |  |

### Remove Tags parameters (`removeTags`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The unique identifier of the user |  |
| Tags | `tags` | string |  | ✓ | Tags to remove separated by "," |  |

### Unsubscribe parameters (`unsubscribe`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The unique identifier of the user |  |

### Track parameters (`track`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| ID | `id` | string |  | ✓ | The unique identifier of the customer |  |
| Email | `email` | string |  | ✓ | e.g. name@email.com | email |
| Event Name | `eventName` | string |  | ✓ | The name of the event tracked |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ |  |  |
| Data | `dataAttributesUi` | fixedCollection | {} | ✗ | Key value pairs that represent any properties you want to track with this event | e.g. Add Data |  |

<details>
<summary><strong>Data sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Data | `dataAttributesValues` |  |  |  |

</details>

| Extra | `extraAttributesUi` | fixedCollection | {} | ✗ | Key value pairs that represent reserved, Vero-specific operators. Refer to the note on “deduplication” below. | e.g. Add Extra |  |

<details>
<summary><strong>Extra sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Extra | `extraAttributesValues` |  |  |  |

</details>

| Data | `dataAttributesJson` | json |  | ✗ | Key value pairs that represent the custom user properties you want to update |  |
| Extra | `extraAttributesJson` | json |  | ✗ | Key value pairs that represent reserved, Vero-specific operators. Refer to the note on “deduplication” below. |  |

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
* Categories: Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: vero
displayName: Vero
description: Consume Vero API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: veroApi
  required: true
operations:
- id: addTags
  name: Add Tags
  description: Adds a tag to a users profile
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the user
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - event
          operation:
          - track
    typeInfo: &id002
      type: string
      displayName: ID
      name: id
  - id: tags
    name: Tags
    type: string
    default: ''
    required: true
    description: Tags to add separated by ","
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - removeTags
    typeInfo: &id004
      type: string
      displayName: Tags
      name: tags
- id: alias
  name: Alias
  description: Change a users identifier
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The old unique identifier of the user
    validation: *id001
    typeInfo: *id002
  - id: newId
    name: New ID
    type: string
    default: ''
    required: true
    description: The new unique identifier of the user
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - alias
    typeInfo:
      type: string
      displayName: New ID
      name: newId
- id: create
  name: Create or Update
  description: Create or update a user profile
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the customer
    validation: *id001
    typeInfo: *id002
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: &id005
      displayOptions:
        show:
          resource:
          - event
          operation:
          - track
    typeInfo: &id006
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: dataAttributesUi
    name: Data
    type: fixedCollection
    default: {}
    required: false
    description: Key value pairs that represent the custom user properties you want
      to update
    placeholder: Add Data
    validation: &id007
      displayOptions:
        show:
          resource:
          - event
          operation:
          - track
          jsonParameters:
          - false
    typeInfo: &id008
      type: fixedCollection
      displayName: Data
      name: dataAttributesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: dataAttributesValues
        displayName: Data
        values:
        - displayName: Key
          name: key
          type: string
          description: Name of the property to set
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value of the property to set
          default: ''
  - id: dataAttributesJson
    name: Data
    type: json
    default: ''
    required: false
    description: Key value pairs that represent the custom user properties you want
      to update
    validation: &id009
      displayOptions:
        show:
          resource:
          - event
          operation:
          - track
          jsonParameters:
          - true
    typeInfo: &id010
      type: json
      displayName: Data
      name: dataAttributesJson
      typeOptions:
        alwaysOpenEditWindow: true
- id: delete
  name: Delete
  description: Delete a user
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the user
    validation: *id001
    typeInfo: *id002
- id: resubscribe
  name: Re-Subscribe
  description: Resubscribe a user
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the user
    validation: *id001
    typeInfo: *id002
- id: removeTags
  name: Remove Tags
  description: Removes a tag from a users profile
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the user
    validation: *id001
    typeInfo: *id002
  - id: tags
    name: Tags
    type: string
    default: ''
    required: true
    description: Tags to remove separated by ","
    validation: *id003
    typeInfo: *id004
- id: unsubscribe
  name: Unsubscribe
  description: Unsubscribe a user
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the user
    validation: *id001
    typeInfo: *id002
- id: track
  name: Track
  description: Track an event for a specific customer
  params:
  - id: id
    name: ID
    type: string
    default: ''
    required: true
    description: The unique identifier of the customer
    validation: *id001
    typeInfo: *id002
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: ''
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - event
          operation:
          - track
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: eventName
    name: Event Name
    type: string
    default: ''
    required: true
    description: The name of the event tracked
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - event
          operation:
          - track
    typeInfo:
      type: string
      displayName: Event Name
      name: eventName
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: dataAttributesUi
    name: Data
    type: fixedCollection
    default: {}
    required: false
    description: Key value pairs that represent any properties you want to track with
      this event
    placeholder: Add Data
    validation: *id007
    typeInfo: *id008
  - id: extraAttributesUi
    name: Extra
    type: fixedCollection
    default: {}
    required: false
    description: Key value pairs that represent reserved, Vero-specific operators.
      Refer to the note on “deduplication” below.
    placeholder: Add Extra
    validation:
      displayOptions:
        show:
          resource:
          - event
          operation:
          - track
          jsonParameters:
          - false
    typeInfo:
      type: fixedCollection
      displayName: Extra
      name: extraAttributesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: extraAttributesValues
        displayName: Extra
        values:
        - displayName: Key
          name: key
          type: string
          description: Name of the property to set
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value of the property to set
          default: ''
  - id: dataAttributesJson
    name: Data
    type: json
    default: ''
    required: false
    description: Key value pairs that represent the custom user properties you want
      to update
    validation: *id009
    typeInfo: *id010
  - id: extraAttributesJson
    name: Extra
    type: json
    default: ''
    required: false
    description: Key value pairs that represent reserved, Vero-specific operators.
      Refer to the note on “deduplication” below.
    validation:
      displayOptions:
        show:
          resource:
          - event
          operation:
          - track
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Extra
      name: extraAttributesJson
      typeOptions:
        alwaysOpenEditWindow: true
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
  - field: dataAttributesUi
    text: Add Data
  - field: email
    text: name@email.com
  - field: dataAttributesUi
    text: Add Data
  - field: extraAttributesUi
    text: Add Extra
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
  "$id": "https://n8n.io/schemas/nodes/vero.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Vero Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "addTags",
        "alias",
        "create",
        "delete",
        "resubscribe",
        "removeTags",
        "unsubscribe",
        "track"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "Create, update and manage the subscription status of your users",
          "type": "string",
          "enum": [
            "user",
            "event"
          ],
          "default": "user"
        },
        "operation": {
          "description": "Track an event for a specific customer",
          "type": "string",
          "enum": [
            "track"
          ],
          "default": "track"
        },
        "id": {
          "description": "The unique identifier of the customer",
          "type": "string",
          "default": ""
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "additionalFields": {
          "description": "The table to create the row in",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "dataAttributesUi": {
          "description": "Key value pairs that represent any properties you want to track with this event",
          "type": "string",
          "default": {},
          "examples": [
            "Add Data"
          ]
        },
        "dataAttributesJson": {
          "description": "Key value pairs that represent the custom user properties you want to update",
          "type": "string",
          "default": ""
        },
        "newId": {
          "description": "The new unique identifier of the user",
          "type": "string",
          "default": ""
        },
        "tags": {
          "description": "Tags to remove separated by \",\"",
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
        "eventName": {
          "description": "The name of the event tracked",
          "type": "string",
          "default": ""
        },
        "extraAttributesUi": {
          "description": "Key value pairs that represent reserved, Vero-specific operators. Refer to the note on \u201cdeduplication\u201d below.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Extra"
          ]
        },
        "extraAttributesJson": {
          "description": "Key value pairs that represent reserved, Vero-specific operators. Refer to the note on \u201cdeduplication\u201d below.",
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
      "name": "veroApi",
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
