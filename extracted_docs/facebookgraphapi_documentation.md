---
title: "Node: Facebook Graph API"
slug: "node-facebookgraphapi"
version: "1"
updated: "2025-11-13"
summary: "Interacts with Facebook using the Graph API"
node_type: "regular"
group: "['transform']"
---

# Node: Facebook Graph API

**Purpose.** Interacts with Facebook using the Graph API


---

## Node Details

- **Icon:** `file:facebook.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **facebookGraphApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `facebookGraphApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Host URL | `hostUrl` | options | graph.facebook.com | ✓ | The Host URL of the request. Almost all requests are passed to the graph.facebook.com host URL. The single exception is video uploads, which use graph-video.facebook.com. | url |

**Host URL options:**

* **Default** (`graph.facebook.com`)
* **Video Uploads** (`graph-video.facebook.com`)

| HTTP Request Method | `httpRequestMethod` | options | GET | ✓ | The HTTP Method to be used for the request |  |

**HTTP Request Method options:**

* **GET** (`GET`)
* **POST** (`POST`)
* **DELETE** (`DELETE`)

| Graph API Version | `graphApiVersion` | options |  | ✓ | The version of the Graph API to be used in the request |  |

**Graph API Version options:**

* **Default** (``)
* **v23.0** (`v23.0`)
* **v22.0** (`v22.0`)
* **v21.0** (`v21.0`)
* **v20.0** (`v20.0`)
* **v19.0** (`v19.0`)
* **v18.0** (`v18.0`)
* **v17.0** (`v17.0`)
* **v16.0** (`v16.0`)
* **v15.0** (`v15.0`)
* **v14.0** (`v14.0`)
* **v13.0** (`v13.0`)
* **v12.0** (`v12.0`)
* **v11.0** (`v11.0`)
* **v10.0** (`v10.0`)
* **v9.0** (`v9.0`)
* **v8.0** (`v8.0`)
* **v7.0** (`v7.0`)
* **v6.0** (`v6.0`)
* **v5.0** (`v5.0`)
* **v4.0** (`v4.0`)
* **v3.3** (`v3.3`)
* **v3.2** (`v3.2`)
* **v3.1** (`v3.1`)
* **v3.0** (`v3.0`)

| Node | `node` | string |  | ✓ | The node on which to operate. A node is an individual object with a unique ID. For example, there are many User node objects, each with a unique ID representing a person on Facebook. | e.g. me |  |
| Edge | `edge` | string |  | ✗ | Edge of the node on which to operate. Edges represent collections of objects which are attached to the node. | e.g. videos |  |
| Ignore SSL Issues (Insecure) | `allowUnauthorizedCerts` | boolean | False | ✗ | Whether to connect even if SSL certificate validation is not possible |  |
| Send Binary File | `sendBinaryData` | boolean | False | ✓ | Whether binary data should be sent as body |  |
| Input Binary Field | `binaryPropertyName` | string |  | ✗ | For Form-Data Multipart, they can be provided in the format: <code>"sendKey1:binaryProperty1,sendKey2:binaryProperty2</code> | e.g. file:data |  |
| Options | `options` | collection | {} | ✗ | The list of fields to request in the GET request | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | fixedCollection | {} | The list of fields to request in the GET request |
| Query Parameters | `queryParameters` | fixedCollection | {} | The query parameters to send |
| Query Parameters JSON | `queryParametersJson` | json | {} | The query parameters to send, defined as a JSON object |

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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: facebookGraphApi
displayName: Facebook Graph API
description: Interacts with Facebook using the Graph API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: facebookGraphApi
  required: true
params:
- id: hostUrl
  name: Host URL
  type: options
  default: graph.facebook.com
  required: true
  description: The Host URL of the request. Almost all requests are passed to the
    graph.facebook.com host URL. The single exception is video uploads, which use
    graph-video.facebook.com.
  validation:
    required: true
    format: url
  typeInfo:
    type: options
    displayName: Host URL
    name: hostUrl
    possibleValues:
    - value: graph.facebook.com
      name: Default
      description: ''
    - value: graph-video.facebook.com
      name: Video Uploads
      description: ''
- id: httpRequestMethod
  name: HTTP Request Method
  type: options
  default: GET
  required: true
  description: The HTTP Method to be used for the request
  validation:
    required: true
  typeInfo:
    type: options
    displayName: HTTP Request Method
    name: httpRequestMethod
    possibleValues:
    - value: GET
      name: GET
      description: ''
    - value: POST
      name: POST
      description: ''
    - value: DELETE
      name: DELETE
      description: ''
- id: graphApiVersion
  name: Graph API Version
  type: options
  default: ''
  required: true
  description: The version of the Graph API to be used in the request
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Graph API Version
    name: graphApiVersion
    possibleValues:
    - value: Default
      name: Default
      description: ''
    - value: v23.0
      name: v23.0
      description: ''
    - value: v22.0
      name: v22.0
      description: ''
    - value: v21.0
      name: v21.0
      description: ''
    - value: v20.0
      name: v20.0
      description: ''
    - value: v19.0
      name: v19.0
      description: ''
    - value: v18.0
      name: v18.0
      description: ''
    - value: v17.0
      name: v17.0
      description: ''
    - value: v16.0
      name: v16.0
      description: ''
    - value: v15.0
      name: v15.0
      description: ''
    - value: v14.0
      name: v14.0
      description: ''
    - value: v13.0
      name: v13.0
      description: ''
    - value: v12.0
      name: v12.0
      description: ''
    - value: v11.0
      name: v11.0
      description: ''
    - value: v10.0
      name: v10.0
      description: ''
    - value: v9.0
      name: v9.0
      description: ''
    - value: v8.0
      name: v8.0
      description: ''
    - value: v7.0
      name: v7.0
      description: ''
    - value: v6.0
      name: v6.0
      description: ''
    - value: v5.0
      name: v5.0
      description: ''
    - value: v4.0
      name: v4.0
      description: ''
    - value: v3.3
      name: v3.3
      description: ''
    - value: v3.2
      name: v3.2
      description: ''
    - value: v3.1
      name: v3.1
      description: ''
    - value: v3.0
      name: v3.0
      description: ''
- id: node
  name: Node
  type: string
  default: ''
  required: true
  description: The node on which to operate. A node is an individual object with a
    unique ID. For example, there are many User node objects, each with a unique ID
    representing a person on Facebook.
  placeholder: me
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Node
    name: node
- id: edge
  name: Edge
  type: string
  default: ''
  required: false
  description: Edge of the node on which to operate. Edges represent collections of
    objects which are attached to the node.
  placeholder: videos
  typeInfo:
    type: string
    displayName: Edge
    name: edge
- id: allowUnauthorizedCerts
  name: Ignore SSL Issues (Insecure)
  type: boolean
  default: false
  required: false
  description: Whether to connect even if SSL certificate validation is not possible
  typeInfo:
    type: boolean
    displayName: Ignore SSL Issues (Insecure)
    name: allowUnauthorizedCerts
- id: sendBinaryData
  name: Send Binary File
  type: boolean
  default: false
  required: true
  description: Whether binary data should be sent as body
  validation:
    required: true
    displayOptions:
      show:
        httpRequestMethod:
        - POST
        - PUT
  typeInfo:
    type: boolean
    displayName: Send Binary File
    name: sendBinaryData
- id: binaryPropertyName
  name: Input Binary Field
  type: string
  default: ''
  required: false
  description: 'For Form-Data Multipart, they can be provided in the format: <code>"sendKey1:binaryProperty1,sendKey2:binaryProperty2</code>'
  hint: The name of the input binary field containing the file to be uploaded
  placeholder: file:data
  validation:
    displayOptions:
      show:
        httpRequestMethod:
        - POST
        - PUT
      hide:
        sendBinaryData:
        - false
  typeInfo:
    type: string
    displayName: Input Binary Field
    name: binaryPropertyName
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: The list of fields to request in the GET request
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
    - displayName: Fields
      name: fields
      type: fixedCollection
      description: The list of fields to request in the GET request
      placeholder: Add Field
      default: {}
      options:
      - name: field
        displayName: Field
        values:
        - displayName: Name
          name: name
          type: string
          description: Name of the field
          default: ''
      typeOptions:
        multipleValues: true
      displayOptions:
        show: {}
    - displayName: Query Parameters
      name: queryParameters
      type: fixedCollection
      description: The query parameters to send
      placeholder: Add Parameter
      default: {}
      options:
      - name: parameter
        displayName: Parameter
        values:
        - displayName: Name
          name: name
          type: string
          description: Name of the parameter
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value of the parameter
          default: ''
      typeOptions:
        multipleValues: true
    - displayName: Query Parameters JSON
      name: queryParametersJson
      type: json
      description: The query parameters to send, defined as a JSON object
      placeholder: '{"field_name": "field_value"}'
      default: '{}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: node
    text: me
  - field: edge
    text: videos
  - field: binaryPropertyName
    text: file:data
  - field: options
    text: Add option
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be uploaded
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
  "$id": "https://n8n.io/schemas/nodes/facebookGraphApi.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Facebook Graph API Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "hostUrl": {
          "description": "The Host URL of the request. Almost all requests are passed to the graph.facebook.com host URL. The single exception is video uploads, which use graph-video.facebook.com.",
          "type": "string",
          "enum": [
            "graph.facebook.com",
            "graph-video.facebook.com"
          ],
          "default": "graph.facebook.com",
          "format": "url"
        },
        "httpRequestMethod": {
          "description": "The HTTP Method to be used for the request",
          "type": "string",
          "enum": [
            "GET",
            "POST",
            "DELETE"
          ],
          "default": "GET"
        },
        "graphApiVersion": {
          "description": "The version of the Graph API to be used in the request",
          "type": "string",
          "enum": [
            "Default",
            "v23.0",
            "v22.0",
            "v21.0",
            "v20.0",
            "v19.0",
            "v18.0",
            "v17.0",
            "v16.0",
            "v15.0",
            "v14.0",
            "v13.0",
            "v12.0",
            "v11.0",
            "v10.0",
            "v9.0",
            "v8.0",
            "v7.0",
            "v6.0",
            "v5.0",
            "v4.0",
            "v3.3",
            "v3.2",
            "v3.1",
            "v3.0"
          ],
          "default": ""
        },
        "node": {
          "description": "The node on which to operate. A node is an individual object with a unique ID. For example, there are many User node objects, each with a unique ID representing a person on Facebook.",
          "type": "string",
          "default": "",
          "examples": [
            "me"
          ]
        },
        "edge": {
          "description": "Edge of the node on which to operate. Edges represent collections of objects which are attached to the node.",
          "type": "string",
          "default": "",
          "examples": [
            "videos"
          ]
        },
        "allowUnauthorizedCerts": {
          "description": "Whether to connect even if SSL certificate validation is not possible",
          "type": "boolean",
          "default": false
        },
        "sendBinaryData": {
          "description": "Whether binary data should be sent as body",
          "type": "boolean",
          "default": false
        },
        "binaryPropertyName": {
          "description": "For Form-Data Multipart, they can be provided in the format: <code>\"sendKey1:binaryProperty1,sendKey2:binaryProperty2</code>",
          "type": "string",
          "default": "",
          "examples": [
            "file:data"
          ]
        },
        "options": {
          "description": "The list of fields to request in the GET request",
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
    "version": "1"
  },
  "credentials": [
    {
      "name": "facebookGraphApi",
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
