---
title: "Node: Postgres Trigger"
slug: "node-postgrestrigger"
version: "1"
updated: "2025-11-13"
summary: "Listens to Postgres messages"
node_type: "trigger"
group: "['trigger']"
---

# Node: Postgres Trigger

**Purpose.** Listens to Postgres messages


---

## Node Details

- **Icon:** `file:postgres.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **postgres**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False
- **Trigger Panel:**
```json
{
  "executionsHelp": "{\n\t\t\t\tinactive:\n\t\t\t\t\t\"<b>While building your workflow</b>, click the 'execute step' button, then trigger a Postgres event. This will trigger an execution, which will show up in this editor.<br /> <br /><b>Once you're happy with your workflow</b>, <a data-key='activate'>activate</a> it. Then every time a change is detected, the workflow will execute. These executions will show up in the <a data-key='executions'>executions list</a>, but not in the editor.\",\n\t\t\t\tactive:\n\t\t\t\t\t\"<b>While building your workflow</b>, click the 'execute step' button, then trigger a Postgres event. This will trigger an execution, which will show up in this editor.<br /> <br /><b>Your workflow will also execute automatically</b>, since it's activated. Every time a change is detected, this node will trigger an execution. These executions will show up in the <a data-key='executions'>executions list</a>, but not in the editor.\",\n\t\t\t}",
  "activationHint": "Once you"
}
```

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `postgres` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Listen For | `triggerMode` | options | createTrigger | ✗ | Insert, update or delete |  |

**Listen For options:**

* **Table Row Change Events** (`createTrigger`) - Insert, update or delete
* **Advanced** (`listenTrigger`) - Listen to existing Postgres channel

| Schema Name | `schema` | resourceLocator |  | ✓ | e.g. Select a schema |  |
| Table Name | `tableName` | resourceLocator |  | ✓ | e.g. Select a table |  |
| Channel Name | `channelName` | string |  | ✓ | Name of the channel to listen to | e.g. e.g. n8n_channel |  |
| Event to listen for | `firesOn` | options | INSERT | ✗ |  |  |

**Event to listen for options:**

* **Insert** (`INSERT`)
* **Update** (`UPDATE`)
* **Delete** (`DELETE`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the channel to listen to | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Channel Name | `channelName` | string |  | Name of the channel to listen to |
| Function Name | `functionName` | string |  | Name of the function to create |
| Replace if Exists | `replaceIfExists` | boolean | False | Whether to replace an existing function and trigger with the same name |
| Trigger Name | `triggerName` | string |  | Name of the trigger to create |

</details>

| Options | `options` | collection | {} | ✗ | Number of seconds reserved for connecting to the database | e.g. Add option | min:0, max:∞ |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Connection Timeout | `connectionTimeout` | number | 30 | Number of seconds reserved for connecting to the database |
| Delay Closing Idle Connection | `delayClosingIdleConnection` | number | 0 | Number of seconds to wait before idle connection would be eligible for closing |

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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: postgresTrigger
displayName: Postgres Trigger
description: Listens to Postgres messages
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: postgres
  required: true
params:
- id: triggerMode
  name: Listen For
  type: options
  default: createTrigger
  required: false
  description: Insert, update or delete
  typeInfo:
    type: options
    displayName: Listen For
    name: triggerMode
    possibleValues:
    - value: createTrigger
      name: Table Row Change Events
      description: Insert, update or delete
    - value: listenTrigger
      name: Advanced
      description: Listen to existing Postgres channel
- id: schema
  name: Schema Name
  type: resourceLocator
  default: ''
  required: true
  description: ''
  placeholder: Select a schema
  validation:
    required: true
    displayOptions:
      show:
        triggerMode:
        - createTrigger
  typeInfo:
    type: resourceLocator
    displayName: Schema Name
    name: schema
- id: tableName
  name: Table Name
  type: resourceLocator
  default: ''
  required: true
  description: ''
  placeholder: Select a table
  validation:
    required: true
    displayOptions:
      show:
        triggerMode:
        - createTrigger
  typeInfo:
    type: resourceLocator
    displayName: Table Name
    name: tableName
- id: channelName
  name: Channel Name
  type: string
  default: ''
  required: true
  description: Name of the channel to listen to
  placeholder: e.g. n8n_channel
  validation:
    required: true
    displayOptions:
      show:
        triggerMode:
        - listenTrigger
  typeInfo:
    type: string
    displayName: Channel Name
    name: channelName
- id: firesOn
  name: Event to listen for
  type: options
  default: INSERT
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        triggerMode:
        - createTrigger
  typeInfo:
    type: options
    displayName: Event to listen for
    name: firesOn
    possibleValues:
    - value: INSERT
      name: Insert
      description: ''
    - value: UPDATE
      name: Update
      description: ''
    - value: DELETE
      name: Delete
      description: ''
- id: additionalFields
  name: Additional Fields
  type: collection
  default: {}
  required: false
  description: Name of the channel to listen to
  placeholder: Add Field
  validation:
    displayOptions:
      show:
        triggerMode:
        - createTrigger
  typeInfo:
    type: collection
    displayName: Additional Fields
    name: additionalFields
    subProperties:
    - displayName: Channel Name
      name: channelName
      type: string
      description: Name of the channel to listen to
      placeholder: e.g. n8n_channel
      default: ''
    - displayName: Function Name
      name: functionName
      type: string
      description: Name of the function to create
      placeholder: e.g. n8n_trigger_function()
      default: ''
    - displayName: Replace if Exists
      name: replaceIfExists
      type: boolean
      description: Whether to replace an existing function and trigger with the same
        name
      default: false
    - displayName: Trigger Name
      name: triggerName
      type: string
      description: Name of the trigger to create
      placeholder: e.g. n8n_trigger
      default: ''
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Number of seconds reserved for connecting to the database
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    typeOptions:
      minValue: 0
    subProperties:
    - displayName: Connection Timeout
      name: connectionTimeout
      type: number
      description: Number of seconds reserved for connecting to the database
      default: 30
    - displayName: Delay Closing Idle Connection
      name: delayClosingIdleConnection
      type: number
      description: Number of seconds to wait before idle connection would be eligible
        for closing
      default: 0
      typeOptions:
        minValue: 0
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: schema
    text: Select a schema
  - field: tableName
    text: Select a table
  - field: channelName
    text: e.g. n8n_channel
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add option
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
  "$id": "https://n8n.io/schemas/nodes/postgresTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Postgres Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "triggerMode": {
          "description": "Insert, update or delete",
          "type": "string",
          "enum": [
            "createTrigger",
            "listenTrigger"
          ],
          "default": "createTrigger"
        },
        "schema": {
          "description": "",
          "type": "string",
          "examples": [
            "Select a schema"
          ]
        },
        "tableName": {
          "description": "",
          "type": "string",
          "examples": [
            "Select a table"
          ]
        },
        "channelName": {
          "description": "Name of the channel to listen to",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. n8n_channel"
          ]
        },
        "firesOn": {
          "description": "",
          "type": "string",
          "enum": [
            "INSERT",
            "UPDATE",
            "DELETE"
          ],
          "default": "INSERT"
        },
        "additionalFields": {
          "description": "Name of the channel to listen to",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "options": {
          "description": "Number of seconds reserved for connecting to the database",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
      "name": "postgres",
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
