---
title: "Node: Slack Trigger"
slug: "node-slacktrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle Slack events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Slack Trigger

**Purpose.** Handle Slack events via webhooks
**Subtitle.** ={{$parameter["eventFilter"].join(", ")}}


---

## Node Details

- **Icon:** `file:slack.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **slackApi**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice**: Set up a webhook in your Slack app to enable this node. <a href="https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger/#configure-a-webhook-in-slack" target="_blank">More info</a>. We also recommend setting up a <a href="https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger/#verify-the-webhook" target="_blank">signing secret</a> to ensure the authenticity of requests.
- **notice** when trigger=['any_event', 'message', 'reaction_added', 'file_share', 'app_mention'], watchWorkspace=[True]: This will use one execution for every event in any channel your bot is in, use with caution

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `slackApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | hidden | accessToken | ✗ |  |  |
| Trigger On | `trigger` | multiOptions | [] | ✗ | Triggers on any event |  |

**Trigger On options:**

* **Any Event** (`any_event`) - Triggers on any event
* **Bot / App Mention** (`app_mention`) - When your bot or app is mentioned in a channel the app is added to
* **File Made Public** (`file_public`) - When a file is made public
* **File Shared** (`file_share`) - When a file is shared in a channel the app is added to
* **New Message Posted to Channel** (`message`) - When a message is posted to a channel the app is added to
* **New Public Channel Created** (`channel_created`) - When a new public channel is created
* **New User** (`team_join`) - When a new user is added to Slack
* **Reaction Added** (`reaction_added`) - When a reaction is added to a message the app is added to

| Watch Whole Workspace | `watchWorkspace` | boolean | False | ✗ | Whether to watch for the event in the whole workspace, rather than a specific channel |  |
| Channel to Watch | `channelId` | resourceLocator |  | ✓ | The Slack channel to listen to events from. Applies to events: Bot/App mention, File Shared, New Message Posted on Channel, Reaction Added. | e.g. Select a channel... |  |
| Download Files | `downloadFiles` | boolean | False | ✗ | Whether to download the files and add it to the output |  |
| Options | `options` | collection | {} | ✗ | Whether to resolve the IDs to their respective names and return them | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Resolve IDs | `resolveIds` | boolean | False | Whether to resolve the IDs to their respective names and return them |
| Usernames or IDs to Ignore | `userIds` | multiOptions | [] | A comma-separated string of encoded user IDs. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


---

## Load Options Methods

- `getUsers`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["eventFilter"].join(", ")}}`

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
node: slackTrigger
displayName: Slack Trigger
description: Handle Slack events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: slackApi
  required: true
params:
- id: authentication
  name: Authentication
  type: hidden
  default: accessToken
  required: false
  description: ''
  typeInfo:
    type: hidden
    displayName: Authentication
    name: authentication
- id: trigger
  name: Trigger On
  type: multiOptions
  default: []
  required: false
  description: Triggers on any event
  typeInfo:
    type: multiOptions
    displayName: Trigger On
    name: trigger
    possibleValues:
    - value: any_event
      name: Any Event
      description: Triggers on any event
    - value: app_mention
      name: Bot / App Mention
      description: When your bot or app is mentioned in a channel the app is added
        to
    - value: file_public
      name: File Made Public
      description: When a file is made public
    - value: file_share
      name: File Shared
      description: When a file is shared in a channel the app is added to
    - value: message
      name: New Message Posted to Channel
      description: When a message is posted to a channel the app is added to
    - value: channel_created
      name: New Public Channel Created
      description: When a new public channel is created
    - value: team_join
      name: New User
      description: When a new user is added to Slack
    - value: reaction_added
      name: Reaction Added
      description: When a reaction is added to a message the app is added to
- id: watchWorkspace
  name: Watch Whole Workspace
  type: boolean
  default: false
  required: false
  description: Whether to watch for the event in the whole workspace, rather than
    a specific channel
  validation:
    displayOptions:
      show:
        trigger:
        - any_event
        - message
        - reaction_added
        - file_share
        - app_mention
  typeInfo:
    type: boolean
    displayName: Watch Whole Workspace
    name: watchWorkspace
- id: channelId
  name: Channel to Watch
  type: resourceLocator
  default: ''
  required: true
  description: 'The Slack channel to listen to events from. Applies to events: Bot/App
    mention, File Shared, New Message Posted on Channel, Reaction Added.'
  placeholder: Select a channel...
  validation:
    required: true
    displayOptions:
      show:
        watchWorkspace:
        - false
  typeInfo:
    type: resourceLocator
    displayName: Channel to Watch
    name: channelId
- id: downloadFiles
  name: Download Files
  type: boolean
  default: false
  required: false
  description: Whether to download the files and add it to the output
  validation:
    displayOptions:
      show:
        trigger:
        - any_event
        - file_share
  typeInfo:
    type: boolean
    displayName: Download Files
    name: downloadFiles
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to resolve the IDs to their respective names and return them
  placeholder: Add Field
  typeInfo:
    type: collection
    displayName: Options
    name: options
    typeOptions:
      loadOptionsMethod: getUsers
    subProperties:
    - displayName: Resolve IDs
      name: resolveIds
      type: boolean
      description: Whether to resolve the IDs to their respective names and return
        them
      default: false
    - displayName: Usernames or IDs to Ignore
      name: userIds
      type: multiOptions
      description: A comma-separated string of encoded user IDs. Choose from the list,
        or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
      default: []
      typeOptions:
        loadOptionsMethod: getUsers
common_expressions:
- ={{$parameter["eventFilter"].join(", ")}}
ui_elements:
  notices:
  - name: notice
    text: Set up a webhook in your Slack app to enable this node. <a href="https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger/#configure-a-webhook-in-slack"
      target="_blank">More info</a>. We also recommend setting up a <a href="https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger/#verify-the-webhook"
      target="_blank">signing secret</a> to ensure the authenticity of requests.
    conditions: null
  - name: notice
    text: This will use one execution for every event in any channel your bot is in,
      use with caution
    conditions:
      show:
        trigger:
        - any_event
        - message
        - reaction_added
        - file_share
        - app_mention
        watchWorkspace:
        - true
  tooltips: []
  placeholders:
  - field: channelId
    text: Select a channel...
  - field: options
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/slackTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Slack Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "default": "accessToken"
        },
        "trigger": {
          "description": "Triggers on any event",
          "type": "string",
          "default": []
        },
        "watchWorkspace": {
          "description": "Whether to watch for the event in the whole workspace, rather than a specific channel",
          "type": "boolean",
          "default": false
        },
        "channelId": {
          "description": "The Slack channel to listen to events from. Applies to events: Bot/App mention, File Shared, New Message Posted on Channel, Reaction Added.",
          "type": "string",
          "examples": [
            "Select a channel..."
          ]
        },
        "downloadFiles": {
          "description": "Whether to download the files and add it to the output",
          "type": "boolean",
          "default": false
        },
        "options": {
          "description": "Whether to resolve the IDs to their respective names and return them",
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
      "name": "slackApi",
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
