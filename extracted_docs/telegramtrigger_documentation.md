---
title: "Node: Telegram Trigger"
slug: "node-telegramtrigger"
version: "['1', '1.1', '1.2']"
updated: "2025-11-13"
summary: "Starts the workflow on a Telegram update"
node_type: "trigger"
group: "['trigger']"
---

# Node: Telegram Trigger

**Purpose.** Starts the workflow on a Telegram update
**Subtitle.** =Updates: {{$parameter["updates"].join(", ")}}


---

## Node Details

- **Icon:** `file:telegram.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **telegramApi**: N/A


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

- **telegramTriggerNotice**: Due to Telegram API limitations, you can use just one Telegram trigger for each bot at a time
- **attachmentNotice**: Every uploaded attachment, even if sent in a group, will trigger a separate event. You can identify that an attachment belongs to a certain group by <code>media_group_id</code> .

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `telegramApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger On | `updates` | multiOptions | [] | ✓ | All updates |  |

**Trigger On options:**

* ***** (`*`) - All updates
* **Callback Query** (`callback_query`) - Trigger on new incoming callback query
* **Channel Post** (`channel_post`) - Trigger on new incoming channel post of any kind — text, photo, sticker, etc
* **Edited Channel Post** (`edited_channel_post`) - Trigger on new version of a channel post that is known to the bot and was edited
* **Edited Message** (`edited_message`) - Trigger on new version of a channel post that is known to the bot and was edited
* **Inline Query** (`inline_query`) - Trigger on new incoming inline query
* **Message** (`message`) - Trigger on new incoming message of any kind — text, photo, sticker, etc
* **Poll** (`poll`) - Trigger on new poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot.
* **Pre-Checkout Query** (`pre_checkout_query`) - Trigger on new incoming pre-checkout query. Contains full information about checkout.
* **Shipping Query** (`shipping_query`) - Trigger on new incoming shipping query. Only for invoices with flexible price.

| Additional Fields | `additionalFields` | collection | {} | ✗ | Telegram delivers the image in multiple sizes. By default, just the large image would be downloaded. If you want to change the size, set the field 'Image Size'. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Download Images/Files | `download` | boolean | False | Telegram delivers the image in multiple sizes. By default, just the large image would be downloaded. If you want to change the size, set the field 'Image Size'. |
| Image Size | `imageSize` | options | large | The size of the image to be downloaded |
| Restrict to Chat IDs | `chatIds` | string |  | The chat IDs to restrict the trigger to. Multiple can be defined separated by comma. |
| Restrict to User IDs | `userIds` | string |  | The user IDs to restrict the trigger to. Multiple can be defined separated by comma. |

</details>


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
node: telegramTrigger
displayName: Telegram Trigger
description: Starts the workflow on a Telegram update
version:
- '1'
- '1.1'
- '1.2'
nodeType: trigger
group:
- trigger
credentials:
- name: telegramApi
  required: true
params:
- id: updates
  name: Trigger On
  type: multiOptions
  default: []
  required: true
  description: All updates
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Trigger On
    name: updates
    possibleValues:
    - value: '*'
      name: '*'
      description: All updates
    - value: callback_query
      name: Callback Query
      description: Trigger on new incoming callback query
    - value: channel_post
      name: Channel Post
      description: Trigger on new incoming channel post of any kind — text, photo,
        sticker, etc
    - value: edited_channel_post
      name: Edited Channel Post
      description: Trigger on new version of a channel post that is known to the bot
        and was edited
    - value: edited_message
      name: Edited Message
      description: Trigger on new version of a channel post that is known to the bot
        and was edited
    - value: inline_query
      name: Inline Query
      description: Trigger on new incoming inline query
    - value: message
      name: Message
      description: Trigger on new incoming message of any kind — text, photo, sticker,
        etc
    - value: poll
      name: Poll
      description: Trigger on new poll state. Bots receive only updates about stopped
        polls and polls, which are sent by the bot.
    - value: pre_checkout_query
      name: Pre-Checkout Query
      description: Trigger on new incoming pre-checkout query. Contains full information
        about checkout.
    - value: shipping_query
      name: Shipping Query
      description: Trigger on new incoming shipping query. Only for invoices with
        flexible price.
- id: additionalFields
  name: Additional Fields
  type: collection
  default: {}
  required: false
  description: Telegram delivers the image in multiple sizes. By default, just the
    large image would be downloaded. If you want to change the size, set the field
    'Image Size'.
  placeholder: Add Field
  validation:
    displayOptions:
      show:
        download:
        - true
  typeInfo:
    type: collection
    displayName: Additional Fields
    name: additionalFields
    subProperties:
    - displayName: Download Images/Files
      name: download
      type: boolean
      description: Telegram delivers the image in multiple sizes. By default, just
        the large image would be downloaded. If you want to change the size, set the
        field 'Image Size'.
      default: false
    - displayName: Image Size
      name: imageSize
      type: options
      description: The size of the image to be downloaded
      value: small
      default: large
      options:
      - name: Small
        value: small
        displayName: Small
      - name: Medium
        value: medium
        displayName: Medium
      - name: Large
        value: large
        displayName: Large
      - name: Extra Large
        value: extraLarge
        displayName: Extra Large
      displayOptions:
        show:
          download:
          - true
    - displayName: Restrict to Chat IDs
      name: chatIds
      type: string
      description: The chat IDs to restrict the trigger to. Multiple can be defined
        separated by comma.
      default: ''
      displayOptions:
        show: {}
    - displayName: Restrict to User IDs
      name: userIds
      type: string
      description: The user IDs to restrict the trigger to. Multiple can be defined
        separated by comma.
      default: ''
      displayOptions:
        show: {}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: telegramTriggerNotice
    text: Due to Telegram API limitations, you can use just one Telegram trigger for
      each bot at a time
    conditions: null
  - name: attachmentNotice
    text: Every uploaded attachment, even if sent in a group, will trigger a separate
      event. You can identify that an attachment belongs to a certain group by <code>media_group_id</code>
      .
    conditions: null
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/telegramTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Telegram Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "updates": {
          "description": "All updates",
          "type": "string",
          "default": []
        },
        "additionalFields": {
          "description": "Telegram delivers the image in multiple sizes. By default, just the large image would be downloaded. If you want to change the size, set the field 'Image Size'.",
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
    "version": [
      "1",
      "1.1",
      "1.2"
    ]
  },
  "credentials": [
    {
      "name": "telegramApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1', '1.2'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
