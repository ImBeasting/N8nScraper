---
title: "Node: RabbitMQ Trigger"
slug: "node-rabbitmqtrigger"
version: "1"
updated: "2026-01-08"
summary: "Listens to RabbitMQ messages"
node_type: "trigger"
group: "['trigger']"
---

# Node: RabbitMQ Trigger

**Purpose.** Listens to RabbitMQ messages


---

## Node Details

- **Icon:** `file:rabbitmq.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **rabbitmq**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False
- **Trigger Panel:**
```json
{
  "executionsHelp": "{\n\t\t\t\tinactive:\n\t\t\t\t\t\"<b>While building your workflow</b>, click the 'execute step' button, then trigger a Rabbit MQ event. This will trigger an execution, which will show up in this editor.<br /> <br /><b>Once you're happy with your workflow</b>, publish it. Then every time a change is detected, the workflow will execute. These executions will show up in the <a data-key='executions'>executions list</a>, but not in the editor.\",\n\t\t\t\tactive:\n\t\t\t\t\t\"<b>While building your workflow</b>, click the 'execute step' button, then trigger a Rabbit MQ event. This will trigger an execution, which will show up in this editor.<br /> <br /><b>Your workflow will also execute automatically</b>, since it's activated. Every time a change is detected, this node will trigger an execution. These executions will show up in the <a data-key='executions'>executions list</a>, but not in the editor.\",\n\t\t\t}",
  "activationHint": "Once you\u2019ve finished building your workflow, publish it to have it also listen continuously (you just won\u2019t see those executions here)."
}
```

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **laterMessageNode**: To delete an item from the queue, insert a RabbitMQ node later in the workflow and use the 'Delete from queue' operation

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `rabbitmq` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Queue / Topic | `queue` | string |  | ✗ | The name of the queue to read from | e.g. queue-name |  |
| Options | `options` | collection | {} | ✗ | Whether to save the content as binary | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content Is Binary | `contentIsBinary` | boolean | False | Whether to save the content as binary |
| Delete From Queue When | `acknowledge` | options | immediately | After the workflow execution finished. No matter if the execution was successful or not. |
| JSON Parse Body | `jsonParseBody` | boolean | False | Whether to parse the body to an object |
| Only Content | `onlyContent` | boolean | False | Whether to return only the content property |
| Parallel Message Processing Limit | `parallelMessages` | number |  | Max number of executions at a time. Use -1 for no limit. |
| Binding | `binding` | fixedCollection | {} | Add binding to queu |

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
node: rabbitmqTrigger
displayName: RabbitMQ Trigger
description: Listens to RabbitMQ messages
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: rabbitmq
  required: true
params:
- id: queue
  name: Queue / Topic
  type: string
  default: ''
  required: false
  description: The name of the queue to read from
  placeholder: queue-name
  typeInfo:
    type: string
    displayName: Queue / Topic
    name: queue
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to save the content as binary
  placeholder: Add option
  validation:
    displayOptions:
      hide:
        contentIsBinary:
        - true
  typeInfo:
    type: collection
    displayName: Options
    name: options
    typeOptions:
      multipleValues: true
    subProperties:
    - displayName: Content Is Binary
      name: contentIsBinary
      type: boolean
      description: Whether to save the content as binary
      default: false
    - displayName: Delete From Queue When
      name: acknowledge
      type: options
      description: After the workflow execution finished. No matter if the execution
        was successful or not.
      value: executionFinishes
      default: immediately
      options:
      - name: Execution Finishes
        description: After the workflow execution finished. No matter if the execution
          was successful or not.
        value: executionFinishes
        displayName: Execution Finishes
      - name: Execution Finishes Successfully
        description: After the workflow execution finished successfully
        value: executionFinishesSuccessfully
        displayName: Execution Finishes Successfully
      - name: Immediately
        description: As soon as the message got received
        value: immediately
        displayName: Immediately
      - name: Specified Later in Workflow
        description: Using a RabbitMQ node to remove the item from the queue
        value: laterMessageNode
        displayName: Specified Later In Workflow
    - displayName: JSON Parse Body
      name: jsonParseBody
      type: boolean
      description: Whether to parse the body to an object
      default: false
      displayOptions:
        hide:
          contentIsBinary:
          - true
    - displayName: Only Content
      name: onlyContent
      type: boolean
      description: Whether to return only the content property
      default: false
      displayOptions:
        hide:
          contentIsBinary:
          - true
    - displayName: Parallel Message Processing Limit
      name: parallelMessages
      type: number
      description: Max number of executions at a time. Use -1 for no limit.
      displayOptions:
        hide:
          acknowledge:
          - immediately
    - displayName: Binding
      name: binding
      type: fixedCollection
      description: Add binding to queu
      placeholder: Add Binding
      default: {}
      options:
      - name: bindings
        displayName: Binding
        values:
        - displayName: Exchange
          name: exchange
          type: string
          placeholder: exchange
          default: ''
        - displayName: RoutingKey
          name: routingKey
          type: string
          placeholder: routing-key
          default: ''
      typeOptions:
        multipleValues: true
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: laterMessageNode
    text: To delete an item from the queue, insert a RabbitMQ node later in the workflow
      and use the 'Delete from queue' operation
    conditions:
      show: {}
  tooltips: []
  placeholders:
  - field: queue
    text: queue-name
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
  "$id": "https://n8n.io/schemas/nodes/rabbitmqTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "RabbitMQ Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "queue": {
          "description": "The name of the queue to read from",
          "type": "string",
          "default": "",
          "examples": [
            "queue-name"
          ]
        },
        "options": {
          "description": "Whether to save the content as binary",
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
      "name": "rabbitmq",
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
