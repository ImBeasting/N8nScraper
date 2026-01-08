---
title: "Node: Webex by Cisco Trigger"
slug: "node-ciscowebextrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when Cisco Webex events occur."
node_type: "trigger"
group: "['trigger']"
---

# Node: Webex by Cisco Trigger

**Purpose.** Starts the workflow when Cisco Webex events occur.
**Subtitle.** ={{$parameter["resource"] + ":" + $parameter["event"]}}


---

## Node Details

- **Icon:** `file:ciscoWebex.png`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **ciscoWebexOAuth2Api**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `ciscoWebexOAuth2Api` | ✓ | - |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | meeting | ✓ | Resource to operate on |  |

**Resource options:**

* **[All]** (`all`)
* **Attachment Action** (`attachmentAction`)
* **Meeting** (`meeting`)
* **Membership** (`membership`)
* **Message** (`message`)
* **Telephony Call** (`telephonyCall`)
* **Recording** (`recording`)
* **Room** (`room`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | meeting | ✓ |  |  |

**Resource options:**

* **[All]** (`all`)
* **Attachment Action** (`attachmentAction`)
* **Meeting** (`meeting`)
* **Membership** (`membership`)
* **Message** (`message`)
* **Telephony Call** (`telephonyCall`)
* **Recording** (`recording`)
* **Room** (`room`)

| Resolve Data | `resolveData` | boolean | True | ✗ | By default the response only contain a reference to the data the user inputed. If this option gets activated, it will resolve the data automatically. |  |
| Filters | `filters` | collection | {} | ✗ | Whether to limit to messages which contain file content attachments | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Has Files | `hasFiles` | boolean | False | Whether to limit to messages which contain file content attachments |
| Is Locked | `isLocked` | boolean | False | Whether to limit to rooms that are locked |
| Is Moderator | `isModerator` | boolean | False | Whether to limit to moderators of a room |
| Mentioned People | `mentionedPeople` | string |  | Limit to messages which contain these mentioned people, by person ID; accepts me as a shorthand for your own person ID; separate multiple values with commas |
| Message ID | `messageId` | string |  | Limit to a particular message, by ID |
| Owned By | `ownedBy` | string |  |  |
| Person Email | `personEmail` | string |  | Limit to a particular person, by email |
| Person Email | `personEmail` | string |  | Limit to a particular person, by email |
| Person ID | `personId` | string |  | Limit to a particular person, by ID |
| Person ID | `personId` | string |  | Limit to a particular person, by ID |
| Person ID | `personId` | string |  | Limit to a particular person, by ID |
| Room ID | `roomId` | string |  | Limit to a particular room, by ID |
| Room ID | `roomId` | string |  | Limit to a particular room, by ID |
| Room ID | `roomId` | string |  | Limit to a particular room, by ID |
| Room Type | `roomType` | options |  | Limit to a particular room type |
| Type | `type` | options |  | Limit to a particular room type |
| Call Type | `callType` | options |  | Limit to a particular call type |
| Person ID | `personId` | string |  | Limit to a particular person, by ID |
| Personality | `personality` | options |  | Limit to a particular call personality |
| State | `state` | options |  | Limit to a particular call state |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["resource"] + ":" + $parameter["event"]}}`

---

## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |

---

## Notes & Caveats

* This node is part of n8n-nodes-base
* Categories: Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: ciscoWebexTrigger
displayName: Webex by Cisco Trigger
description: Starts the workflow when Cisco Webex events occur.
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: ciscoWebexOAuth2Api
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: meeting
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: all
      name: '[All]'
      description: ''
    - value: attachmentAction
      name: Attachment Action
      description: ''
    - value: meeting
      name: Meeting
      description: ''
    - value: membership
      name: Membership
      description: ''
    - value: message
      name: Message
      description: ''
    - value: telephonyCall
      name: Telephony Call
      description: ''
    - value: recording
      name: Recording
      description: ''
    - value: room
      name: Room
      description: ''
- id: resolveData
  name: Resolve Data
  type: boolean
  default: true
  required: false
  description: By default the response only contain a reference to the data the user
    inputed. If this option gets activated, it will resolve the data automatically.
  validation:
    displayOptions:
      show:
        resource:
        - attachmentAction
  typeInfo:
    type: boolean
    displayName: Resolve Data
    name: resolveData
- id: filters
  name: Filters
  type: collection
  default: {}
  required: false
  description: Whether to limit to messages which contain file content attachments
  placeholder: Add Filter
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: collection
    displayName: Filters
    name: filters
    subProperties:
    - displayName: Has Files
      name: hasFiles
      type: boolean
      description: Whether to limit to messages which contain file content attachments
      default: false
      displayOptions:
        show: {}
    - displayName: Is Locked
      name: isLocked
      type: boolean
      description: Whether to limit to rooms that are locked
      default: false
      displayOptions:
        show: {}
    - displayName: Is Moderator
      name: isModerator
      type: boolean
      description: Whether to limit to moderators of a room
      default: false
      displayOptions:
        show: {}
    - displayName: Mentioned People
      name: mentionedPeople
      type: string
      description: Limit to messages which contain these mentioned people, by person
        ID; accepts me as a shorthand for your own person ID; separate multiple values
        with commas
      default: ''
      displayOptions:
        show: {}
    - displayName: Message ID
      name: messageId
      type: string
      description: Limit to a particular message, by ID
      default: ''
      displayOptions:
        show: {}
    - displayName: Owned By
      name: ownedBy
      type: string
      default: ''
      displayOptions:
        show: {}
    - displayName: Person Email
      name: personEmail
      type: string
      description: Limit to a particular person, by email
      default: ''
      displayOptions:
        show: {}
    - displayName: Person Email
      name: personEmail
      type: string
      description: Limit to a particular person, by email
      default: ''
      displayOptions:
        show: {}
    - displayName: Person ID
      name: personId
      type: string
      description: Limit to a particular person, by ID
      default: ''
      displayOptions:
        show: {}
    - displayName: Person ID
      name: personId
      type: string
      description: Limit to a particular person, by ID
      default: ''
      displayOptions:
        show: {}
    - displayName: Person ID
      name: personId
      type: string
      description: Limit to a particular person, by ID
      default: ''
      displayOptions:
        show: {}
    - displayName: Room ID
      name: roomId
      type: string
      description: Limit to a particular room, by ID
      default: ''
      displayOptions:
        show: {}
    - displayName: Room ID
      name: roomId
      type: string
      description: Limit to a particular room, by ID
      default: ''
      displayOptions:
        show: {}
    - displayName: Room ID
      name: roomId
      type: string
      description: Limit to a particular room, by ID
      default: ''
      displayOptions:
        show: {}
    - displayName: Room Type
      name: roomType
      type: options
      description: Limit to a particular room type
      value: direct
      default: ''
      options:
      - name: Direct
        value: direct
        displayName: Direct
      - name: Group
        value: group
        displayName: Group
      displayOptions:
        show: {}
    - displayName: Type
      name: type
      type: options
      description: Limit to a particular room type
      value: direct
      default: ''
      options:
      - name: Direct
        value: direct
        displayName: Direct
      - name: Group
        value: group
        displayName: Group
      displayOptions:
        show: {}
    - displayName: Call Type
      name: callType
      type: options
      description: Limit to a particular call type
      value: emergency
      default: ''
      options:
      - name: Emergency
        value: emergency
        displayName: Emergency
      - name: External
        value: external
        displayName: External
      - name: Location
        value: location
        displayName: Location
      - name: Disconnected
        value: disconnected
        displayName: Disconnected
      - name: Organization
        value: organization
        displayName: Organization
      - name: Other
        value: other
        displayName: Other
      - name: Repair
        value: repair
        displayName: Repair
      displayOptions:
        show: {}
    - displayName: Person ID
      name: personId
      type: string
      description: Limit to a particular person, by ID
      default: ''
      displayOptions:
        show: {}
    - displayName: Personality
      name: personality
      type: options
      description: Limit to a particular call personality
      value: clickToDial
      default: ''
      options:
      - name: Click To Dial
        value: clickToDial
        displayName: Click To Dial
      - name: Originator
        value: originator
        displayName: Originator
      - name: Terminator
        value: terminator
        displayName: Terminator
      displayOptions:
        show: {}
    - displayName: State
      name: state
      type: options
      description: Limit to a particular call state
      value: alerting
      default: ''
      options:
      - name: Alerting
        value: alerting
        displayName: Alerting
      - name: Connected
        value: connected
        displayName: Connected
      - name: Connecting
        value: connecting
        displayName: Connecting
      - name: Disconnected
        value: disconnected
        displayName: Disconnected
      - name: Held
        value: held
        displayName: Held
      - name: Remote Held
        value: remoteHeld
        displayName: Remote Held
      displayOptions:
        show: {}
common_expressions:
- ={{$parameter["resource"] + ":" + $parameter["event"]}}
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/ciscoWebexTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Webex by Cisco Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "all",
            "attachmentAction",
            "meeting",
            "membership",
            "message",
            "telephonyCall",
            "recording",
            "room"
          ],
          "default": "meeting"
        },
        "resolveData": {
          "description": "By default the response only contain a reference to the data the user inputed. If this option gets activated, it will resolve the data automatically.",
          "type": "boolean",
          "default": true
        },
        "filters": {
          "description": "Whether to limit to messages which contain file content attachments",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
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
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
    "version": "1"
  },
  "credentials": [
    {
      "name": "ciscoWebexOAuth2Api",
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
