---
title: "Node: Pushbullet"
slug: "node-pushbullet"
version: "1"
updated: "2026-01-08"
summary: "Consume Pushbullet API"
node_type: "regular"
group: "['input']"
---

# Node: Pushbullet

**Purpose.** Consume Pushbullet API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:pushbullet.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **pushbulletOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `pushbulletOAuth2Api` | ✓ | - |

---

## Operations

### Push Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a push |
| Delete | `delete` | Delete a push |
| Get Many | `getAll` | Get many pushes |
| Update | `update` | Update a push |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | push | ✗ | Resource to operate on |  |

**Resource options:**

* **Push** (`push`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a push |  |

**Operation options:**

* **Create** (`create`) - Create a push
* **Delete** (`delete`) - Delete a push
* **Get Many** (`getAll`) - Get many pushes
* **Update** (`update`) - Update a push

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Type | `type` | options | note | ✓ |  |  |

**Type options:**

* **File** (`file`)
* **Link** (`link`)
* **Note** (`note`)

| Title | `title` | string |  | ✓ | Title of the push |  |
| Body | `body` | string |  | ✓ | Body of the push |  |
| URL | `url` | string |  | ✓ | URL of the push | url |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be written |  |
| Target | `target` | options | default | ✓ | Send the push to all subscribers to your channel that has this tag |  |

**Target options:**

* **Channel Tag** (`channel_tag`) - Send the push to all subscribers to your channel that has this tag
* **Default** (`default`) - Broadcast it to all of the user's devices
* **Device ID** (`device_iden`) - Send the push to a specific device
* **Email** (`email`) - Send the push to this email address

| Value | `value` | string |  | ✓ | The value to be set depending on the target selected. For example, if the target selected is email then this field would take the email address of the person you are trying to send the push to. |  |
| Value Name or ID | `value` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Push ID | `pushId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Filters | `filters` | collection | {} | ✗ | Don't return deleted pushes | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Active | `active` | boolean | False | Don't return deleted pushes |
| Modified After | `modified_after` | dateTime |  | Request pushes modified after this timestamp |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Push ID | `pushId` | string |  | ✓ |  |  |
| Dismissed | `dismissed` | boolean | False | ✓ | Whether to mark a push as having been dismissed by the user, will cause any notifications for the push to be hidden if possible |  |

---

## Load Options Methods

- `getDevices`

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
node: pushbullet
displayName: Pushbullet
description: Consume Pushbullet API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: pushbulletOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a push
  params:
  - id: type
    name: Type
    type: options
    default: note
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - push
          operation:
          - create
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: file
        name: File
        description: ''
      - value: link
        name: Link
        description: ''
      - value: note
        name: Note
        description: ''
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the push
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - push
          operation:
          - create
          type:
          - note
          - link
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: body
    name: Body
    type: string
    default: ''
    required: true
    description: Body of the push
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - push
          operation:
          - create
          type:
          - note
          - link
          - file
    typeInfo:
      type: string
      displayName: Body
      name: body
  - id: url
    name: URL
    type: string
    default: ''
    required: true
    description: URL of the push
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - push
          operation:
          - create
          type:
          - link
    typeInfo:
      type: string
      displayName: URL
      name: url
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be written
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - push
          operation:
          - create
          type:
          - file
    typeInfo:
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
  - id: target
    name: Target
    type: options
    default: default
    required: true
    description: Send the push to all subscribers to your channel that has this tag
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - push
          operation:
          - create
    typeInfo:
      type: options
      displayName: Target
      name: target
      possibleValues:
      - value: channel_tag
        name: Channel Tag
        description: Send the push to all subscribers to your channel that has this
          tag
      - value: default
        name: Default
        description: Broadcast it to all of the user's devices
      - value: device_iden
        name: Device ID
        description: Send the push to a specific device
      - value: email
        name: Email
        description: Send the push to this email address
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: The value to be set depending on the target selected. For example,
      if the target selected is email then this field would take the email address
      of the person you are trying to send the push to.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - push
          operation:
          - create
          target:
          - device_iden
    typeInfo: &id002
      type: options
      displayName: Value Name or ID
      name: value
      typeOptions:
        loadOptionsMethod: getDevices
      possibleValues: []
  - id: value
    name: Value Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
- id: delete
  name: Delete
  description: Delete a push
  params:
  - id: pushId
    name: Push ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - push
          operation:
          - update
    typeInfo: &id004
      type: string
      displayName: Push ID
      name: pushId
- id: getAll
  name: Get Many
  description: Get many pushes
  params:
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
          - push
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
          - push
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
- id: update
  name: Update
  description: Update a push
  params:
  - id: pushId
    name: Push ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: dismissed
    name: Dismissed
    type: boolean
    default: false
    required: true
    description: Whether to mark a push as having been dismissed by the user, will
      cause any notifications for the push to be hidden if possible
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - push
          operation:
          - update
    typeInfo:
      type: boolean
      displayName: Dismissed
      name: dismissed
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
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be written
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
  "$id": "https://n8n.io/schemas/nodes/pushbullet.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Pushbullet Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
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
            "push"
          ],
          "default": "push"
        },
        "operation": {
          "description": "Create a push",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "type": {
          "description": "",
          "type": "string",
          "enum": [
            "file",
            "link",
            "note"
          ],
          "default": "note"
        },
        "title": {
          "description": "Title of the push",
          "type": "string",
          "default": ""
        },
        "body": {
          "description": "Body of the push",
          "type": "string",
          "default": ""
        },
        "url": {
          "description": "URL of the push",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "target": {
          "description": "Send the push to all subscribers to your channel that has this tag",
          "type": "string",
          "enum": [
            "channel_tag",
            "default",
            "device_iden",
            "email"
          ],
          "default": "default"
        },
        "value": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "pushId": {
          "description": "",
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
          "default": 100
        },
        "filters": {
          "description": "Don't return deleted pushes",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "dismissed": {
          "description": "Whether to mark a push as having been dismissed by the user, will cause any notifications for the push to be hidden if possible",
          "type": "boolean",
          "default": false
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
      "name": "pushbulletOAuth2Api",
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
