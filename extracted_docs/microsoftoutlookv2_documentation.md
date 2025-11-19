---
title: "Node: Microsoft Outlook"
slug: "node-microsoftoutlookv2"
version: "1.0"
updated: "2025-11-13"
summary: "Consume Microsoft Outlook API"
node_type: "regular"
group: "['transform']"
---

# Node: Microsoft Outlook

**Purpose.** Consume Microsoft Outlook API
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:outlook.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **filtersNotice** when returnAll=[True]: Fetching a lot of messages may take a long time. Consider using filters to speed things up

---

## Operations

### Messageattachment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add an attachment to a message |
| Download | `download` | Download an attachment from a message |
| Get | `get` | Retrieve information about an attachment of a message |
| Get Many | `getAll` | Retrieve information about the attachments of a message |

### Calendar Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new calendar |
| Delete | `delete` | Delete a calendar |
| Get | `get` | Retrieve a calendar |
| Get Many | `getAll` | List and search calendars |
| Update | `update` | Update a calendar |

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new contact |
| Delete | `delete` | Delete a contact |
| Get | `get` | Retrieve a contact |
| Get Many | `getAll` | List and search contacts |
| Update | `update` | Update a contact |

### Folder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a mail folder in the root folder of the user's mailbox |
| Delete | `delete` | Delete a folder |
| Get | `get` | Retrieve a folder |
| Get Many | `getAll` | Get many folders |
| Update | `update` | Update a folder |

### Foldermessage Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Retrieves the messages in a folder |

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new event |
| Delete | `delete` | Delete an event |
| Get | `get` | Retrieve an event |
| Get Many | `getAll` | List and search events |
| Update | `update` | Update an event |

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a message |
| Get | `get` | Retrieve a single message |
| Get Many | `getAll` | List and search messages |
| Move | `move` | Move a message to a folder |
| Reply | `reply` | Create a reply to a message |
| Send | `send` | Send a message |
| Send and Wait for Response | `` | Send a message and wait for response |
| Update | `update` | Update a message |

### Draft Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new email draft |
| Delete | `delete` | Delete an email draft |
| Get | `get` | Retrieve an email draft |
| Send | `send` | Send an existing email draft |
| Update | `update` | Update an email draft |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✗ | Resource to operate on |  |

**Resource options:**

* **Calendar** (`calendar`)
* **Contact** (`contact`)
* **Draft** (`draft`)
* **Event** (`event`)
* **Folder** (`folder`)
* **Folder Message** (`folderMessage`)
* **Message** (`message`)
* **Message Attachment** (`messageAttachment`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | add | ✗ | Add an attachment to a message |  |

**Operation options:**

* **Add** (`add`) - Add an attachment to a message
* **Download** (`download`) - Download an attachment from a message
* **Get** (`get`) - Retrieve information about an attachment of a message
* **Get Many** (`getAll`) - Retrieve information about the attachments of a message

---

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: MicrosoftOutlookV2
displayName: Microsoft Outlook
description: Consume Microsoft Outlook API
version: '1.0'
nodeType: regular
group:
- transform
operations:
- id: add
  name: Add
  description: Add an attachment to a message
- id: download
  name: Download
  description: Download an attachment from a message
- id: get
  name: Get
  description: Retrieve information about an attachment of a message
- id: getAll
  name: Get Many
  description: Retrieve information about the attachments of a message
- id: create
  name: Create
  description: Create a new calendar
- id: delete
  name: Delete
  description: Delete a calendar
- id: update
  name: Update
  description: Update a calendar
- id: move
  name: Move
  description: Move a message to a folder
- id: reply
  name: Reply
  description: Create a reply to a message
- id: send
  name: Send
  description: Send a message
- id: ''
  name: Send and Wait for Response
  description: Send a message and wait for response
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices:
  - name: filtersNotice
    text: Fetching a lot of messages may take a long time. Consider using filters
      to speed things up
    conditions:
      show:
        returnAll:
        - true
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  - field: binaryPropertyName
    text: e.g. data
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: name
    text: e.g. My Calendar
  - field: additionalFields
    text: Add Field
  - field: filtersUI
    text: Add Filters
  - field: additionalFields
    text: Add Field
  hints:
  - field: binaryPropertyName
    text: The name of the input field containing the binary file data to be attached
  - field: filters
    text: Search query to filter calendars. <a href="https://learn.microsoft.com/en-us/graph/filter-query-parameter">More
      info</a>.
  - field: filtersUI
    text: Search query to filter messages. <a href="https://learn.microsoft.com/en-us/graph/filter-query-parameter">More
      info</a>.
  - field: additionalFields
    text: The name of the input field containing the binary file data to be attached
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
  "$id": "https://n8n.io/schemas/nodes/MicrosoftOutlookV2.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Microsoft Outlook Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "add",
        "download",
        "get",
        "getAll",
        "create",
        "delete",
        "update",
        "move",
        "reply",
        "send",
        ""
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
            "calendar",
            "contact",
            "draft",
            "event",
            "folder",
            "folderMessage",
            "message",
            "messageAttachment"
          ],
          "default": "message"
        },
        "options": {
          "description": "The fields to add to the output",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
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
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data",
          "examples": [
            "e.g. data"
          ]
        },
        "operation": {
          "description": "Create a new email draft",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "send",
            "update"
          ],
          "default": "create"
        },
        "updateFields": {
          "description": "Specify the color to distinguish the calendar from the others",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "filters": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "name": {
          "description": "The name of the calendar to create",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. My Calendar"
          ]
        },
        "additionalFields": {
          "description": "Comma-separated list of email addresses of BCC recipients",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "output": {
          "description": "",
          "type": "string",
          "enum": [
            "simple",
            "raw",
            "fields"
          ],
          "default": "simple"
        },
        "fields": {
          "description": "The fields to add to the output",
          "type": "string",
          "default": []
        },
        "givenName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "surname": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "displayName": {
          "description": "Name of the folder",
          "type": "string",
          "default": ""
        },
        "filtersUI": {
          "description": "Only return messages that contains search term. Without specific message properties, the search is carried out on the default search properties of from, subject, and body. <a href=\"https://docs.microsoft.com/en-us/graph/query-parameters#search-parameter target=\"_blank\">More info</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filters"
          ]
        },
        "fromAllCalendars": {
          "description": "",
          "type": "boolean",
          "default": true
        },
        "subject": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "startDateTime": {
          "description": "",
          "type": "string"
        },
        "endDateTime": {
          "description": "",
          "type": "string"
        },
        "replyToSenderOnly": {
          "description": "Whether to reply to the sender only or to the entire list of recipients",
          "type": "boolean",
          "default": false
        },
        "message": {
          "description": "Message body content",
          "type": "string",
          "default": ""
        },
        "toRecipients": {
          "description": "Comma-separated list of email addresses of recipients",
          "type": "string",
          "default": ""
        },
        "bodyContent": {
          "description": "Message body content",
          "type": "string",
          "default": ""
        },
        "to": {
          "description": "Comma-separated list of email addresses of recipients",
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
    "version": "1.0"
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1.0 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
