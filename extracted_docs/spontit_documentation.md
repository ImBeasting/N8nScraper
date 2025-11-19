---
title: "Node: Spontit"
slug: "node-spontit"
version: "1"
updated: "2025-11-13"
summary: "Consume Spontit API"
node_type: "regular"
group: "['output']"
---

# Node: Spontit

**Purpose.** Consume Spontit API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:spontit.png`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **spontitApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `spontitApi` | ✓ | - |

---

## API Patterns

**Headers Used:** X-Authorization, X-UserId

---

## Operations

### Push Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a push notification |

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
| Operation | `operation` | options | create | ✗ | Create a push notification |  |

**Operation options:**

* **Create** (`create`) - Create a push notification

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Content | `content` | string |  | ✗ | To provide text in a push, supply one of either "content" or "pushContent" (or both). Limited to 2500 characters. (Required if a value for "pushContent" is not provided). |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The name of a channel you created. If you have not yet created a channel, simply don't provide this value and the push will be sent to your main account. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Channel Name | `channelName` | string |  | The name of a channel you created. If you have not yet created a channel, simply don't provide this value and the push will be sent to your main account. |
| Expiration Stamp | `expirationStamp` | dateTime |  | A Unix timestamp. When to automatically expire your push notification. The default is 10 days after pushing. The push will become unaccessible within 15-30 minutes of the selected time, but will remain on all device screens until dismissed or clicked. |
| iOS DeepLink | `iOSDeepLink` | string |  | An iOS deep link. Use this to deep link into other apps. Alternatively, you can provide a universal link in the link attribute and set openLinkInApp to false. |
| Link | `link` | string |  | A link that can be attached to your push. Must be a valid URL. |
| Open In Home Feed | `openInHomeFeed` | boolean | False | Whether the notification opens to the home feed or to a standalone page with the notification. The default (openInHomeFeed=False) is to open the notification on a standalone page. |
| Open Link In App | `openLinkInApp` | boolean | False | Whether to open the provided link within the iOS app or in Safari. Android PWA opens all links in the default web browser. |
| Push To Emails | `pushToEmails` | string |  | <p>Emails (strings) to whom to send the notification. If all three attributes 'pushToFollowers', 'pushToPhoneNumbers' and 'pushToEmails' are not supplied, then everyone who follows the channel will receive the push notification.</p><p>If 'pushToFollowers' is supplied, only those listed in the array will receive the push notification.</p><p>If one of the userIds supplied does not follow the specified channel, then that userId value will be ignored.</p><p>See the "Followers" section to learn how to list the userIds of those who follow one of your channels.</p>. |
| Push To Followers | `pushToFollowers` | string |  | <p>User IDs (strings) to whom to send the notification. If all three attributes 'pushToFollowers', 'pushToPhoneNumbers' and 'pushToEmails' are not supplied, then everyone who follows the channel will receive the push notification.</p><p>If 'pushToFollowers' is supplied, only those listed in the array will receive the push notification.</p><p>If one of the userIds supplied does not follow the specified channel, then that userId value will be ignored.</p><p>See the "Followers" section to learn how to list the userIds of those who follow one of your channels.</p>. |
| Push To Phone Numbers | `pushToPhoneNumbers` | string |  | <p>Phone numbers (strings) to whom to send the notification. If all three attributes 'pushToFollowers', 'pushToPhoneNumbers' and 'pushToEmails' are not supplied, then everyone who follows the channel will receive the push notification.</p><p>If 'pushToFollowers' is supplied, only those listed in the array will receive the push notification.</p><p>If one of the userIds supplied does not follow the specified channel, then that userId value will be ignored.</p><p>See the "Followers" section to learn how to list the userIds of those who follow one of your channels.</p>. |
| Schedule | `schedule` | dateTime |  | A Unix timestamp. Schedule a push to be sent at a later date and time. |
| Subtitle | `subtitle` | string |  | The subtitle of your push. Limited to 20 characters. Only appears on iOS devices. |
| Title | `pushTitle` | string |  | The title of push. Appears in bold at the top. Limited to 100 characters. |

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
* Categories: Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: spontit
displayName: Spontit
description: Consume Spontit API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: spontitApi
  required: true
operations:
- id: create
  name: Create
  description: Create a push notification
  params:
  - id: content
    name: Content
    type: string
    default: ''
    required: false
    description: To provide text in a push, supply one of either "content" or "pushContent"
      (or both). Limited to 2500 characters. (Required if a value for "pushContent"
      is not provided).
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - push
    typeInfo:
      type: string
      displayName: Content
      name: content
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - X-Authorization
  - X-UserId
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
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
  "$id": "https://n8n.io/schemas/nodes/spontit.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Spontit Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create"
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
          "description": "Create a push notification",
          "type": "string",
          "enum": [
            "create"
          ],
          "default": "create"
        },
        "content": {
          "description": "To provide text in a push, supply one of either \"content\" or \"pushContent\" (or both). Limited to 2500 characters. (Required if a value for \"pushContent\" is not provided).",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "The name of a channel you created. If you have not yet created a channel, simply don't provide this value and the push will be sent to your main account.",
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
      "name": "spontitApi",
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
