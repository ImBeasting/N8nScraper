---
title: "Node: Respond to Webhook"
slug: "node-respondtowebhook"
version: "['1', '1.1', '1.2', '1.3', '1.4', '1.5']"
updated: "2026-01-08"
summary: "Returns data for Webhook"
node_type: "regular"
group: "['transform']"
---

# Node: Respond to Webhook

**Purpose.** Returns data for Webhook


---

## Node Details

- **Icon:** `{'light': 'file:webhook.svg', 'dark': 'file:webhook.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['dynamic']`

---

## Authentication

- **jwtAuth**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **generalNotice**: Verify that the "Webhook" node's "Respond" parameter is set to "Using Respond to Webhook Node". <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook/" target="_blank">More details
- **webhookNotice** when respondWith=['json', 'text', 'jwt']: When using expressions, note that this node will only run for the first item in the input data
- **contentTypeNotice** when respondWith=['text']: To avoid unexpected behavior, add a "Content-Type" response header with the appropriate value

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `jwtAuth` | ✓ | {'show': {'respondWith': ['jwt']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Enable Response Output Branch | `enableResponseOutput` | boolean | False | ✗ | Whether to provide an additional output branch with the response sent to the webhook |  |
| Credentials | `credentials` | credentials |  | ✗ |  |  |
| Redirect URL | `redirectURL` | string |  | ✓ | The URL to redirect to | e.g. e.g. http://www.n8n.io | url |
| Response Body | `responseBody` | json | {\n   | ✗ | The HTTP response JSON data |  |
| Payload | `payload` | json | {\n   | ✗ | The payload to include in the JWT token |  |
| Response Body | `responseBody` | string |  | ✗ | The HTTP response text data | e.g. e.g. Workflow completed |  |
| Response Data Source | `responseDataSource` | options | automatically | ✗ | Use if input data will contain a single piece of binary data |  |

**Response Data Source options:**

* **Choose Automatically From Input** (`automatically`) - Use if input data will contain a single piece of binary data
* **Specify Myself** (`set`) - Enter the name of the input field the binary data will be in

| Input Field Name | `inputFieldName` | string | data | ✓ | The name of the node input field with the binary data |  |
| Options | `options` | collection | {} | ✗ | The HTTP response code to return. Defaults to 200. | e.g. Add option | min:100, max:599 |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Response Code | `responseCode` | number | 200 | The HTTP response code to return. Defaults to 200. |
| Response Headers | `responseHeaders` | fixedCollection | {} | Add headers to the webhook response |
| Put Response in Field | `responseKey` | string |  | The name of the response field to put all items in |
| Enable Streaming | `enableStreaming` | boolean | True | Whether to enable streaming to the response |

</details>


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
* Categories: Core Nodes, Utility

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: respondToWebhook
displayName: Respond to Webhook
description: Returns data for Webhook
version:
- '1'
- '1.1'
- '1.2'
- '1.3'
- '1.4'
- '1.5'
nodeType: regular
group:
- transform
credentials:
- name: jwtAuth
  required: true
params:
- id: enableResponseOutput
  name: Enable Response Output Branch
  type: boolean
  default: false
  required: false
  description: Whether to provide an additional output branch with the response sent
    to the webhook
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: boolean
    displayName: Enable Response Output Branch
    name: enableResponseOutput
- id: credentials
  name: Credentials
  type: credentials
  default: ''
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        respondWith:
        - jwt
  typeInfo:
    type: credentials
    displayName: Credentials
    name: credentials
- id: redirectURL
  name: Redirect URL
  type: string
  default: ''
  required: true
  description: The URL to redirect to
  placeholder: e.g. http://www.n8n.io
  validation:
    required: true
    format: url
    displayOptions:
      show:
        respondWith:
        - redirect
  typeInfo:
    type: string
    displayName: Redirect URL
    name: redirectURL
- id: responseBody
  name: Response Body
  type: json
  default: '{\n  '
  required: false
  description: The HTTP response JSON data
  validation: &id001
    displayOptions:
      show:
        respondWith:
        - text
  typeInfo: &id002
    type: string
    displayName: Response Body
    name: responseBody
    typeOptions:
      rows: 2
- id: payload
  name: Payload
  type: json
  default: '{\n  '
  required: false
  description: The payload to include in the JWT token
  validation:
    displayOptions:
      show:
        respondWith:
        - jwt
  typeInfo:
    type: json
    displayName: Payload
    name: payload
    typeOptions:
      rows: 4
- id: responseBody
  name: Response Body
  type: string
  default: ''
  required: false
  description: The HTTP response text data
  placeholder: e.g. Workflow completed
  validation: *id001
  typeInfo: *id002
- id: responseDataSource
  name: Response Data Source
  type: options
  default: automatically
  required: false
  description: Use if input data will contain a single piece of binary data
  validation:
    displayOptions:
      show:
        respondWith:
        - binary
  typeInfo:
    type: options
    displayName: Response Data Source
    name: responseDataSource
    possibleValues:
    - value: automatically
      name: Choose Automatically From Input
      description: Use if input data will contain a single piece of binary data
    - value: set
      name: Specify Myself
      description: Enter the name of the input field the binary data will be in
- id: inputFieldName
  name: Input Field Name
  type: string
  default: data
  required: true
  description: The name of the node input field with the binary data
  validation:
    required: true
    displayOptions:
      show:
        respondWith:
        - binary
        responseDataSource:
        - set
  typeInfo:
    type: string
    displayName: Input Field Name
    name: inputFieldName
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: The HTTP response code to return. Defaults to 200.
  placeholder: Add option
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: collection
    displayName: Options
    name: options
    typeOptions:
      minValue: 100
      maxValue: 599
    subProperties:
    - displayName: Response Code
      name: responseCode
      type: number
      description: The HTTP response code to return. Defaults to 200.
      default: 200
      typeOptions:
        minValue: 100
        maxValue: 599
    - displayName: Response Headers
      name: responseHeaders
      type: fixedCollection
      description: Add headers to the webhook response
      placeholder: Add Response Header
      default: {}
      options:
      - name: entries
        displayName: Entries
        values:
        - displayName: Name
          name: name
          type: string
          description: Name of the header
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value of the header
          default: ''
      typeOptions:
        multipleValues: true
    - displayName: Put Response in Field
      name: responseKey
      type: string
      description: The name of the response field to put all items in
      placeholder: e.g. data
      default: ''
      displayOptions:
        show: {}
    - displayName: Enable Streaming
      name: enableStreaming
      type: boolean
      description: Whether to enable streaming to the response
      default: true
      displayOptions:
        show: {}
ui_elements:
  notices:
  - name: generalNotice
    text: Verify that the "Webhook" node's "Respond" parameter is set to "Using Respond
      to Webhook Node". <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook/"
      target="_blank">More details
    conditions: null
  - name: webhookNotice
    text: When using expressions, note that this node will only run for the first
      item in the input data
    conditions:
      show:
        respondWith:
        - json
        - text
        - jwt
  - name: contentTypeNotice
    text: To avoid unexpected behavior, add a "Content-Type" response header with
      the appropriate value
    conditions:
      show:
        respondWith:
        - text
  tooltips: []
  placeholders:
  - field: redirectURL
    text: e.g. http://www.n8n.io
  - field: responseBody
    text: e.g. Workflow completed
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
  "$id": "https://n8n.io/schemas/nodes/respondToWebhook.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Respond to Webhook Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "enableResponseOutput": {
          "description": "Whether to provide an additional output branch with the response sent to the webhook",
          "type": "boolean",
          "default": false
        },
        "credentials": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "redirectURL": {
          "description": "The URL to redirect to",
          "type": "string",
          "default": "",
          "format": "url",
          "examples": [
            "e.g. http://www.n8n.io"
          ]
        },
        "responseBody": {
          "description": "The HTTP response text data",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Workflow completed"
          ]
        },
        "payload": {
          "description": "The payload to include in the JWT token",
          "type": "string",
          "default": "{\\n  "
        },
        "responseDataSource": {
          "description": "Use if input data will contain a single piece of binary data",
          "type": "string",
          "enum": [
            "automatically",
            "set"
          ],
          "default": "automatically"
        },
        "inputFieldName": {
          "description": "The name of the node input field with the binary data",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "The HTTP response code to return. Defaults to 200.",
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
    "version": [
      "1",
      "1.1",
      "1.2",
      "1.3",
      "1.4",
      "1.5"
    ]
  },
  "credentials": [
    {
      "name": "jwtAuth",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1', '1.2', '1.3', '1.4', '1.5'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
