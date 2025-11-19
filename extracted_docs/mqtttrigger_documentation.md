---
title: "Node: MQTT Trigger"
slug: "node-mqtttrigger"
version: "1"
updated: "2025-11-13"
summary: "Listens to MQTT events"
node_type: "trigger"
group: "['trigger']"
---

# Node: MQTT Trigger

**Purpose.** Listens to MQTT events


---

## Node Details

- **Icon:** `file:mqtt.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **mqtt**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False
- **Trigger Panel:**
```json
{
  "executionsHelp": "{\n\t\t\t\tinactive:\n\t\t\t\t\t\"<b>While building your workflow</b>, click the 'execute step' button, then trigger an MQTT event. This will trigger an execution, which will show up in this editor.<br /> <br /><b>Once you're happy with your workflow</b>, <a data-key='activate'>activate</a> it. Then every time a change is detected, the workflow will execute. These executions will show up in the <a data-key='executions'>executions list</a>, but not in the editor.\",\n\t\t\t\tactive:\n\t\t\t\t\t\"<b>While building your workflow</b>, click the 'execute step' button, then trigger an MQTT event. This will trigger an execution, which will show up in this editor.<br /> <br /><b>Your workflow will also execute automatically</b>, since it's activated. Every time a change is detected, this node will trigger an execution. These executions will show up in the <a data-key='executions'>executions list</a>, but not in the editor.\",\n\t\t\t}",
  "activationHint": "Once you\u2019ve finished building your workflow, <a data-key="
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
| `mqtt` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Topics | `topics` | string |  | ✗ | Topics to subscribe to, multiple can be defined with comma. Wildcard characters are supported (+ - for single level and # - for multi level). By default all subscription used QoS=0. To set a different QoS, write the QoS desired after the topic preceded by a colom. For Example: topicA:1,topicB:2 |  |
| Options | `options` | collection | {} | ✗ | Whether to try parse the message to an object | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| JSON Parse Body | `jsonParseBody` | boolean | False | Whether to try parse the message to an object |
| Only Message | `onlyMessage` | boolean | False | Whether to return only the message property |
| Parallel Processing | `parallelProcessing` | boolean | True | Whether to process messages in parallel or by keeping the message in order |

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
* Categories: Communication, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: mqttTrigger
displayName: MQTT Trigger
description: Listens to MQTT events
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: mqtt
  required: true
params:
- id: topics
  name: Topics
  type: string
  default: ''
  required: false
  description: 'Topics to subscribe to, multiple can be defined with comma. Wildcard
    characters are supported (+ - for single level and # - for multi level). By default
    all subscription used QoS=0. To set a different QoS, write the QoS desired after
    the topic preceded by a colom. For Example: topicA:1,topicB:2'
  typeInfo:
    type: string
    displayName: Topics
    name: topics
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to try parse the message to an object
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: JSON Parse Body
      name: jsonParseBody
      type: boolean
      description: Whether to try parse the message to an object
      default: false
    - displayName: Only Message
      name: onlyMessage
      type: boolean
      description: Whether to return only the message property
      default: false
    - displayName: Parallel Processing
      name: parallelProcessing
      type: boolean
      description: Whether to process messages in parallel or by keeping the message
        in order
      default: true
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
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
  "$id": "https://n8n.io/schemas/nodes/mqttTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MQTT Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "topics": {
          "description": "Topics to subscribe to, multiple can be defined with comma. Wildcard characters are supported (+ - for single level and # - for multi level). By default all subscription used QoS=0. To set a different QoS, write the QoS desired after the topic preceded by a colom. For Example: topicA:1,topicB:2",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Whether to try parse the message to an object",
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
      "name": "mqtt",
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
