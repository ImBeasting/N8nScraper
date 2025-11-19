---
title: "Node: Microsoft Teams Trigger"
slug: "node-microsoftteamstrigger"
version: "1"
updated: "2025-11-13"
summary: "Triggers workflows in n8n based on events from Microsoft Teams, such as new messages or team updates, using specified configurations."
node_type: "trigger"
group: "['trigger']"
---

# Node: Microsoft Teams Trigger

**Purpose.** Triggers workflows in n8n based on events from Microsoft Teams, such as new messages or team updates, using specified configurations.
**Subtitle.** Microsoft Teams Trigger


---

## Node Details

- **Icon:** `file:teams.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **microsoftTeamsOAuth2Api**: N/A


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
| `microsoftTeamsOAuth2Api` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger On | `event` | options | newChannelMessage | ✗ | A new channel is created |  |

**Trigger On options:**

* **New Channel** (`newChannel`) - A new channel is created
* **New Channel Message** (`newChannelMessage`) - A message is posted to a channel
* **New Chat** (`newChat`) - A new chat is created
* **New Chat Message** (`newChatMessage`) - A message is posted to a chat
* **New Team Member** (`newTeamMember`) - A new member is added to a team

| Watch All Teams | `watchAllTeams` | boolean | False | ✗ | Whether to watch for the event in all the available teams |  |
| Team | `teamId` | resourceLocator |  | ✓ | Select a team from the list, enter an ID or a URL | e.g. Select a team... |  |
| Watch All Channels | `watchAllChannels` | boolean | False | ✗ | Whether to watch for the event in all the available channels |  |
| Channel | `channelId` | resourceLocator |  | ✓ | Select a channel from the list, enter an ID or a URL | e.g. Select a channel... |  |
| Watch All Chats | `watchAllChats` | boolean | False | ✗ | Whether to watch for the event in all the available chats |  |
| Chat | `chatId` | resourceLocator |  | ✓ | Select a chat from the list, enter an ID or a URL | e.g. Select a chat... |  |

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
node: microsoftTeamsTrigger
displayName: Microsoft Teams Trigger
description: Triggers workflows in n8n based on events from Microsoft Teams, such
  as new messages or team updates, using specified configurations.
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: microsoftTeamsOAuth2Api
  required: true
params:
- id: event
  name: Trigger On
  type: options
  default: newChannelMessage
  required: false
  description: A new channel is created
  typeInfo:
    type: options
    displayName: Trigger On
    name: event
    possibleValues:
    - value: newChannel
      name: New Channel
      description: A new channel is created
    - value: newChannelMessage
      name: New Channel Message
      description: A message is posted to a channel
    - value: newChat
      name: New Chat
      description: A new chat is created
    - value: newChatMessage
      name: New Chat Message
      description: A message is posted to a chat
    - value: newTeamMember
      name: New Team Member
      description: A new member is added to a team
- id: watchAllTeams
  name: Watch All Teams
  type: boolean
  default: false
  required: false
  description: Whether to watch for the event in all the available teams
  validation:
    displayOptions:
      show:
        event:
        - newChannel
        - newChannelMessage
        - newTeamMember
  typeInfo:
    type: boolean
    displayName: Watch All Teams
    name: watchAllTeams
- id: teamId
  name: Team
  type: resourceLocator
  default: ''
  required: true
  description: Select a team from the list, enter an ID or a URL
  placeholder: Select a team...
  validation:
    required: true
    displayOptions:
      show:
        event:
        - newChannel
        - newChannelMessage
        - newTeamMember
        watchAllTeams:
        - false
  typeInfo:
    type: resourceLocator
    displayName: Team
    name: teamId
- id: watchAllChannels
  name: Watch All Channels
  type: boolean
  default: false
  required: false
  description: Whether to watch for the event in all the available channels
  validation:
    displayOptions:
      show:
        event:
        - newChannelMessage
        watchAllTeams:
        - false
  typeInfo:
    type: boolean
    displayName: Watch All Channels
    name: watchAllChannels
- id: channelId
  name: Channel
  type: resourceLocator
  default: ''
  required: true
  description: Select a channel from the list, enter an ID or a URL
  placeholder: Select a channel...
  validation:
    required: true
    displayOptions:
      show:
        event:
        - newChannelMessage
        watchAllTeams:
        - false
        watchAllChannels:
        - false
  typeInfo:
    type: resourceLocator
    displayName: Channel
    name: channelId
- id: watchAllChats
  name: Watch All Chats
  type: boolean
  default: false
  required: false
  description: Whether to watch for the event in all the available chats
  validation:
    displayOptions:
      show:
        event:
        - newChatMessage
  typeInfo:
    type: boolean
    displayName: Watch All Chats
    name: watchAllChats
- id: chatId
  name: Chat
  type: resourceLocator
  default: ''
  required: true
  description: Select a chat from the list, enter an ID or a URL
  placeholder: Select a chat...
  validation:
    required: true
    displayOptions:
      show:
        event:
        - newChatMessage
        watchAllChats:
        - false
  typeInfo:
    type: resourceLocator
    displayName: Chat
    name: chatId
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: teamId
    text: Select a team...
  - field: channelId
    text: Select a channel...
  - field: chatId
    text: Select a chat...
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
  "$id": "https://n8n.io/schemas/nodes/microsoftTeamsTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft Teams Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "event": {
          "description": "A new channel is created",
          "type": "string",
          "enum": [
            "newChannel",
            "newChannelMessage",
            "newChat",
            "newChatMessage",
            "newTeamMember"
          ],
          "default": "newChannelMessage"
        },
        "watchAllTeams": {
          "description": "Whether to watch for the event in all the available teams",
          "type": "boolean",
          "default": false
        },
        "teamId": {
          "description": "Select a team from the list, enter an ID or a URL",
          "type": "string",
          "examples": [
            "Select a team..."
          ]
        },
        "watchAllChannels": {
          "description": "Whether to watch for the event in all the available channels",
          "type": "boolean",
          "default": false
        },
        "channelId": {
          "description": "Select a channel from the list, enter an ID or a URL",
          "type": "string",
          "examples": [
            "Select a channel..."
          ]
        },
        "watchAllChats": {
          "description": "Whether to watch for the event in all the available chats",
          "type": "boolean",
          "default": false
        },
        "chatId": {
          "description": "Select a chat from the list, enter an ID or a URL",
          "type": "string",
          "examples": [
            "Select a chat..."
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
      "name": "microsoftTeamsOAuth2Api",
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
