---
title: "Node: Webhook"
slug: "node-webhook"
version: "['1', '1.1', '2', '2.1']"
updated: "2025-11-13"
summary: "Starts the workflow when a webhook is called"
node_type: "webhook"
group: "['trigger']"
---

# Node: Webhook

**Purpose.** Starts the workflow when a webhook is called


---

## Node Details

- **Icon:** `{'light': 'file:webhook.svg', 'dark': 'file:webhook.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['dynamic']`


---

## Trigger Properties

- **Event Trigger Description:** Waiting for you to call the Test URL
- **Activation Message:** You can now make calls to your production webhook URL.
- **Supports CORS:** True
- **Trigger Panel:**
```json
{
  "executionsHelp": "{\n\t\t\t\tinactive:\n\t\t\t\t\t'Webhooks have two modes: test and production. <br /> <br /> <b>Use test mode while you build your workflow</b>. Click the \\'listen\\' button, then make a request to the test URL. The executions will show up in the editor.<br /> <br /> <b>Use production mode to run your workflow automatically</b>. <a data-key=\"activate\">Activate</a> the workflow, then make requests to the production URL. These executions will show up in the executions list, but not in the editor.',\n\t\t\t\tactive:\n\t\t\t\t\t'Webhooks have two modes: test and production. <br /> <br /> <b>Use test mode while you build your workflow</b>. Click the \\'listen\\' button, then make a request to the test URL. The executions will show up in the editor.<br /> <br /> <b>Use production mode to run your workflow automatically</b>. Since the workflow is activated, you can make requests to the production URL. These executions will show up in the <a data-key=\"executions\">executions list</a>, but not in the editor.',\n\t\t\t}",
  "activationHint": "Once you"
}
```

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **webhookNotice** when responseMode=['responseNode']: Insert a 'Respond to Webhook' node to control when and how you respond. <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook/" target="_blank">More details</a>
- **webhookStreamingNotice** when responseMode=['streaming']: Insert a node that supports streaming (e.g. 'AI Agent') and enable streaming to stream directly to the response while the workflow is executed. <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook/" target="_blank">More details</a>
- **contentTypeNotice** when responseMode=['onReceived']: If you are sending back a response, add a "Content-Type" response header with the appropriate value to avoid unexpected behavior

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Allow Multiple HTTP Methods | `multipleMethods` | boolean | False | ✗ | Whether to allow the webhook to listen for multiple HTTP methods |  |
| HTTP Methods | `httpMethod` | multiOptions |  | ✗ | The HTTP methods to listen to |  |

**HTTP Methods options:**

* **DELETE** (`DELETE`)
* **GET** (`GET`)
* **HEAD** (`HEAD`)
* **PATCH** (`PATCH`)
* **POST** (`POST`)
* **PUT** (`PUT`)

| Path | `path` | string |  | ✗ | The path to listen to, dynamic values could be specified by using ':', e.g. 'your-path/:dynamic-value'. If dynamic values are set 'webhookId' would be prepended to path. | e.g. webhook |  |
| HTTP Method | `httpMethod` | options | GET | ✗ | The HTTP method to listen to |  |

**HTTP Method options:**

* **DELETE** (`DELETE`)
* **GET** (`GET`)
* **HEAD** (`HEAD`)
* **PATCH** (`PATCH`)
* **POST** (`POST`)
* **PUT** (`PUT`)

| Respond | `responseMode` | options | onReceived | ✗ | When and how to respond to the webhook |  |
| Respond | `responseMode` | options | onReceived | ✗ | Returns data in real time from streaming enabled nodes |  |

**Respond options:**

* **Streaming** (`streaming`) - Returns data in real time from streaming enabled nodes

| Response Code | `responseCode` | number | 200 | ✗ | The HTTP Response code to return | min:100, max:599 |
| Response Data | `responseData` | options | firstEntryJson | ✗ | Returns all the entries of the last node. Always returns an array. |  |

**Response Data options:**

* **All Entries** (`allEntries`) - Returns all the entries of the last node. Always returns an array.
* **First Entry JSON** (`firstEntryJson`) - Returns the JSON data of the first entry of the last node. Always returns a JSON object.
* **First Entry Binary** (`firstEntryBinary`) - Returns the binary data of the first entry of the last node. Always returns a binary file.
* **No Response Body** (`noData`) - Returns without a body

| Property Name | `responseBinaryPropertyName` | string | data | ✓ | Name of the binary property to return |  |
| Options | `options` | collection | {} | ✗ | Whether the webhook will receive binary data | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Binary File | `binaryData` | boolean | False | Whether the webhook will receive binary data |
| Put Output File in Field | `binaryPropertyName` | string | data | If the data gets received via "Form-Data Multipart" it will be the prefix and a number starting with 0 will be attached to it |
| Field Name for Binary Data | `binaryPropertyName` | string | data | The name of the output field to put any binary file data in. Only relevant if binary data is received. |
| Ignore Bots | `ignoreBots` | boolean | False | Whether to ignore requests from bots like link previewers and web crawlers |
| IP(s) Whitelist | `ipWhitelist` | string |  | Comma-separated list of allowed IP addresses. Leave empty to allow all IPs. |
| No Response Body | `noResponseBody` | boolean | False | Whether to send any body in the response |
| Raw Body | `rawBody` | boolean | False | Raw body (binary) |
| Raw Body | `rawBody` | boolean | False | Whether to return the raw body |
| Response Data | `responseData` | string |  | Custom response data to send |
| Response Content-Type | `responseContentType` | string |  | Set a custom content-type to return if another one as the "application/json" should be returned |
| Response Headers | `responseHeaders` | fixedCollection | {} | Add headers to the webhook response |
| Property Name | `responsePropertyName` | string | data | Name of the property to return the data of instead of the whole JSON |

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
* Categories: Development, Core Nodes
* Aliases: HTTP, API, Build, WH

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: webhook
displayName: Webhook
description: Starts the workflow when a webhook is called
version:
- '1'
- '1.1'
- '2'
- '2.1'
nodeType: webhook
group:
- trigger
params:
- id: multipleMethods
  name: Allow Multiple HTTP Methods
  type: boolean
  default: false
  required: false
  description: Whether to allow the webhook to listen for multiple HTTP methods
  typeInfo:
    type: boolean
    displayName: Allow Multiple HTTP Methods
    name: multipleMethods
- id: httpMethod
  name: HTTP Methods
  type: multiOptions
  default: ''
  required: false
  description: The HTTP methods to listen to
  validation: &id001
    displayOptions:
      show:
        multipleMethods:
        - true
  typeInfo: &id002
    type: options
    displayName: HTTP Method
    name: httpMethod
    possibleValues:
    - value: DELETE
      name: DELETE
      description: ''
    - value: GET
      name: GET
      description: ''
    - value: HEAD
      name: HEAD
      description: ''
    - value: PATCH
      name: PATCH
      description: ''
    - value: POST
      name: POST
      description: ''
    - value: PUT
      name: PUT
      description: ''
- id: path
  name: Path
  type: string
  default: ''
  required: false
  description: The path to listen to, dynamic values could be specified by using ':',
    e.g. 'your-path/:dynamic-value'. If dynamic values are set 'webhookId' would be
    prepended to path.
  placeholder: webhook
  typeInfo:
    type: string
    displayName: Path
    name: path
- id: httpMethod
  name: HTTP Method
  type: options
  default: GET
  required: false
  description: The HTTP method to listen to
  validation: *id001
  typeInfo: *id002
- id: responseMode
  name: Respond
  type: options
  default: onReceived
  required: false
  description: When and how to respond to the webhook
  validation: &id003
    displayOptions:
      hide: {}
  typeInfo: &id004
    type: options
    displayName: Respond
    name: responseMode
    possibleValues:
    - value: streaming
      name: Streaming
      description: Returns data in real time from streaming enabled nodes
- id: responseMode
  name: Respond
  type: options
  default: onReceived
  required: false
  description: Returns data in real time from streaming enabled nodes
  validation: *id003
  typeInfo: *id004
- id: responseCode
  name: Response Code
  type: number
  default: 200
  required: false
  description: The HTTP Response code to return
  validation:
    displayOptions:
      hide:
        responseMode:
        - responseNode
  typeInfo:
    type: number
    displayName: Response Code
    name: responseCode
    typeOptions:
      minValue: 100
      maxValue: 599
- id: responseData
  name: Response Data
  type: options
  default: firstEntryJson
  required: false
  description: Returns all the entries of the last node. Always returns an array.
  validation:
    displayOptions:
      show:
        responseMode:
        - lastNode
  typeInfo:
    type: options
    displayName: Response Data
    name: responseData
    possibleValues:
    - value: allEntries
      name: All Entries
      description: Returns all the entries of the last node. Always returns an array.
    - value: firstEntryJson
      name: First Entry JSON
      description: Returns the JSON data of the first entry of the last node. Always
        returns a JSON object.
    - value: firstEntryBinary
      name: First Entry Binary
      description: Returns the binary data of the first entry of the last node. Always
        returns a binary file.
    - value: noData
      name: No Response Body
      description: Returns without a body
- id: responseBinaryPropertyName
  name: Property Name
  type: string
  default: data
  required: true
  description: Name of the binary property to return
  validation:
    required: true
    displayOptions:
      show:
        responseData:
        - firstEntryBinary
  typeInfo:
    type: string
    displayName: Property Name
    name: responseBinaryPropertyName
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether the webhook will receive binary data
  hint: The name of the output binary field to put the file in
  placeholder: Add option
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: collection
    displayName: Options
    name: options
    typeOptions:
      multipleValues: true
    subProperties:
    - displayName: Binary File
      name: binaryData
      type: boolean
      description: Whether the webhook will receive binary data
      default: false
      displayOptions:
        show: {}
    - displayName: Put Output File in Field
      name: binaryPropertyName
      type: string
      description: If the data gets received via "Form-Data Multipart" it will be
        the prefix and a number starting with 0 will be attached to it
      hint: The name of the output binary field to put the file in
      default: data
      displayOptions:
        show:
          binaryData:
          - true
    - displayName: Field Name for Binary Data
      name: binaryPropertyName
      type: string
      description: The name of the output field to put any binary file data in. Only
        relevant if binary data is received.
      default: data
      displayOptions:
        hide: {}
    - displayName: Ignore Bots
      name: ignoreBots
      type: boolean
      description: Whether to ignore requests from bots like link previewers and web
        crawlers
      default: false
    - displayName: IP(s) Whitelist
      name: ipWhitelist
      type: string
      description: Comma-separated list of allowed IP addresses. Leave empty to allow
        all IPs.
      placeholder: e.g. 127.0.0.1
      default: ''
    - displayName: No Response Body
      name: noResponseBody
      type: boolean
      description: Whether to send any body in the response
      default: false
      displayOptions:
        show: {}
        hide:
          rawBody:
          - true
    - displayName: Raw Body
      name: rawBody
      type: boolean
      description: Raw body (binary)
      default: false
      displayOptions:
        show: {}
        hide:
          binaryData:
          - true
          noResponseBody:
          - true
    - displayName: Raw Body
      name: rawBody
      type: boolean
      description: Whether to return the raw body
      default: false
      displayOptions:
        hide:
          noResponseBody:
          - true
    - displayName: Response Data
      name: responseData
      type: string
      description: Custom response data to send
      placeholder: success
      default: ''
      displayOptions:
        show: {}
        hide:
          noResponseBody:
          - true
    - displayName: Response Content-Type
      name: responseContentType
      type: string
      description: Set a custom content-type to return if another one as the "application/json"
        should be returned
      placeholder: application/xml
      default: ''
      displayOptions:
        show: {}
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
    - displayName: Property Name
      name: responsePropertyName
      type: string
      description: Name of the property to return the data of instead of the whole
        JSON
      default: data
      displayOptions:
        show: {}
ui_elements:
  notices:
  - name: webhookNotice
    text: Insert a 'Respond to Webhook' node to control when and how you respond.
      <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook/"
      target="_blank">More details</a>
    conditions:
      show:
        responseMode:
        - responseNode
  - name: webhookStreamingNotice
    text: Insert a node that supports streaming (e.g. 'AI Agent') and enable streaming
      to stream directly to the response while the workflow is executed. <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook/"
      target="_blank">More details</a>
    conditions:
      show:
        responseMode:
        - streaming
  - name: contentTypeNotice
    text: If you are sending back a response, add a "Content-Type" response header
      with the appropriate value to avoid unexpected behavior
    conditions:
      show:
        responseMode:
        - onReceived
  tooltips: []
  placeholders:
  - field: path
    text: webhook
  - field: options
    text: Add option
  hints:
  - field: options
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/webhook.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Webhook Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "multipleMethods": {
          "description": "Whether to allow the webhook to listen for multiple HTTP methods",
          "type": "boolean",
          "default": false
        },
        "httpMethod": {
          "description": "The HTTP method to listen to",
          "type": "string",
          "enum": [
            "DELETE",
            "GET",
            "HEAD",
            "PATCH",
            "POST",
            "PUT"
          ],
          "default": "GET"
        },
        "path": {
          "description": "The path to listen to, dynamic values could be specified by using ':', e.g. 'your-path/:dynamic-value'. If dynamic values are set 'webhookId' would be prepended to path.",
          "type": "string",
          "default": "",
          "examples": [
            "webhook"
          ]
        },
        "responseMode": {
          "description": "Returns data in real time from streaming enabled nodes",
          "type": "string",
          "enum": [
            "streaming"
          ],
          "default": "onReceived"
        },
        "responseCode": {
          "description": "The HTTP Response code to return",
          "type": "number",
          "default": 200
        },
        "responseData": {
          "description": "Returns all the entries of the last node. Always returns an array.",
          "type": "string",
          "enum": [
            "allEntries",
            "firstEntryJson",
            "firstEntryBinary",
            "noData"
          ],
          "default": "firstEntryJson"
        },
        "responseBinaryPropertyName": {
          "description": "Name of the binary property to return",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "Whether the webhook will receive binary data",
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
    "nodeType": "webhook",
    "version": [
      "1",
      "1.1",
      "2",
      "2.1"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1', '2', '2.1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
