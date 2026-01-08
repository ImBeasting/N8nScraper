---
title: "Node: GraphQL"
slug: "node-graphql"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Makes a GraphQL request and returns the received data"
node_type: "regular"
group: "['input']"
---

# Node: GraphQL

**Purpose.** Makes a GraphQL request and returns the received data


---

## Node Details

- **Icon:** `file:graphql.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **httpBasicAuth**: N/A
- **httpCustomAuth**: N/A
- **httpDigestAuth**: N/A
- **httpHeaderAuth**: N/A
- **httpQueryAuth**: N/A
- **oAuth1Api**: N/A
- **oAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `httpBasicAuth` | ✓ | {'show': {'authentication': ['basicAuth']}} |
| `httpCustomAuth` | ✓ | {'show': {'authentication': ['customAuth']}} |
| `httpDigestAuth` | ✓ | {'show': {'authentication': ['digestAuth']}} |
| `httpHeaderAuth` | ✓ | {'show': {'authentication': ['headerAuth']}} |
| `httpQueryAuth` | ✓ | {'show': {'authentication': ['queryAuth']}} |
| `oAuth1Api` | ✓ | {'show': {'authentication': ['oAuth1']}} |
| `oAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | none | ✗ | The way to authenticate |  |

**Authentication options:**

* **Basic Auth** (`basicAuth`)
* **Custom Auth** (`customAuth`)
* **Digest Auth** (`digestAuth`)
* **Header Auth** (`headerAuth`)
* **None** (`none`)
* **OAuth1** (`oAuth1`)
* **OAuth2** (`oAuth2`)
* **Query Auth** (`queryAuth`)

| HTTP Request Method | `requestMethod` | options | POST | ✗ | The underlying HTTP request method to use |  |

**HTTP Request Method options:**

* **GET** (`GET`)
* **POST** (`POST`)

| Endpoint | `endpoint` | string |  | ✓ | The GraphQL endpoint | e.g. http://example.com/graphql |  |
| Ignore SSL Issues (Insecure) | `allowUnauthorizedCerts` | boolean | False | ✗ | Whether to download the response even if SSL certificate validation is not possible |  |
| Request Format | `requestFormat` | options | graphql | ✓ | The format for the query payload |  |

**Request Format options:**

* **GraphQL (Raw)** (`graphql`)
* **JSON** (`json`)

| Query | `query` | string |  | ✓ | GraphQL query |  |
| Variables | `variables` | json |  | ✗ | Query variables as JSON object |  |
| Operation Name | `operationName` | string |  | ✗ | Name of operation to execute |  |
| Response Format | `responseFormat` | options | json | ✗ | The format in which the data gets returned from the URL |  |

**Response Format options:**

* **JSON** (`json`)
* **String** (`string`)

| Response Data Property Name | `dataPropertyName` | string | data | ✓ | Name of the property to which to write the response data |  |
| Headers | `headerParametersUi` | fixedCollection | {} | ✗ | The headers to send | e.g. Add Header |  |

<details>
<summary><strong>Headers sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Header | `parameter` |  |  |  |

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
* Categories: Data & Storage, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: graphql
displayName: GraphQL
description: Makes a GraphQL request and returns the received data
version:
- '1'
- '1.1'
nodeType: regular
group:
- input
credentials:
- name: httpBasicAuth
  required: true
- name: httpCustomAuth
  required: true
- name: httpDigestAuth
  required: true
- name: httpHeaderAuth
  required: true
- name: httpQueryAuth
  required: true
- name: oAuth1Api
  required: true
- name: oAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: none
  required: false
  description: The way to authenticate
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: basicAuth
      name: Basic Auth
      description: ''
    - value: customAuth
      name: Custom Auth
      description: ''
    - value: digestAuth
      name: Digest Auth
      description: ''
    - value: headerAuth
      name: Header Auth
      description: ''
    - value: none
      name: None
      description: ''
    - value: oAuth1
      name: OAuth1
      description: ''
    - value: oAuth2
      name: OAuth2
      description: ''
    - value: queryAuth
      name: Query Auth
      description: ''
- id: requestMethod
  name: HTTP Request Method
  type: options
  default: POST
  required: false
  description: The underlying HTTP request method to use
  typeInfo:
    type: options
    displayName: HTTP Request Method
    name: requestMethod
    possibleValues:
    - value: GET
      name: GET
      description: ''
    - value: POST
      name: POST
      description: ''
- id: endpoint
  name: Endpoint
  type: string
  default: ''
  required: true
  description: The GraphQL endpoint
  placeholder: http://example.com/graphql
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Endpoint
    name: endpoint
- id: allowUnauthorizedCerts
  name: Ignore SSL Issues (Insecure)
  type: boolean
  default: false
  required: false
  description: Whether to download the response even if SSL certificate validation
    is not possible
  typeInfo:
    type: boolean
    displayName: Ignore SSL Issues (Insecure)
    name: allowUnauthorizedCerts
- id: requestFormat
  name: Request Format
  type: options
  default: graphql
  required: true
  description: The format for the query payload
  validation:
    required: true
    displayOptions:
      show:
        requestMethod:
        - POST
  typeInfo:
    type: options
    displayName: Request Format
    name: requestFormat
    possibleValues:
    - value: graphql
      name: GraphQL (Raw)
      description: ''
    - value: json
      name: JSON
      description: ''
- id: query
  name: Query
  type: string
  default: ''
  required: true
  description: GraphQL query
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Query
    name: query
    typeOptions:
      rows: 6
- id: variables
  name: Variables
  type: json
  default: ''
  required: false
  description: Query variables as JSON object
  validation:
    displayOptions:
      show:
        requestFormat:
        - json
        requestMethod:
        - POST
  typeInfo:
    type: json
    displayName: Variables
    name: variables
- id: operationName
  name: Operation Name
  type: string
  default: ''
  required: false
  description: Name of operation to execute
  validation:
    displayOptions:
      show:
        requestFormat:
        - json
        requestMethod:
        - POST
  typeInfo:
    type: string
    displayName: Operation Name
    name: operationName
- id: responseFormat
  name: Response Format
  type: options
  default: json
  required: false
  description: The format in which the data gets returned from the URL
  typeInfo:
    type: options
    displayName: Response Format
    name: responseFormat
    possibleValues:
    - value: json
      name: JSON
      description: ''
    - value: string
      name: String
      description: ''
- id: dataPropertyName
  name: Response Data Property Name
  type: string
  default: data
  required: true
  description: Name of the property to which to write the response data
  validation:
    required: true
    displayOptions:
      show:
        responseFormat:
        - string
  typeInfo:
    type: string
    displayName: Response Data Property Name
    name: dataPropertyName
- id: headerParametersUi
  name: Headers
  type: fixedCollection
  default: {}
  required: false
  description: The headers to send
  placeholder: Add Header
  typeInfo:
    type: fixedCollection
    displayName: Headers
    name: headerParametersUi
    typeOptions:
      multipleValues: true
    subProperties:
    - name: parameter
      displayName: Header
      values:
      - displayName: Name
        name: name
        type: string
        description: Name of the header
        default: ''
      - displayName: Value
        name: value
        type: string
        description: Value to set for the header
        default: ''
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: endpoint
    text: http://example.com/graphql
  - field: headerParametersUi
    text: Add Header
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
  "$id": "https://n8n.io/schemas/nodes/graphql.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GraphQL Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "The way to authenticate",
          "type": "string",
          "enum": [
            "basicAuth",
            "customAuth",
            "digestAuth",
            "headerAuth",
            "none",
            "oAuth1",
            "oAuth2",
            "queryAuth"
          ],
          "default": "none"
        },
        "requestMethod": {
          "description": "The underlying HTTP request method to use",
          "type": "string",
          "enum": [
            "GET",
            "POST"
          ],
          "default": "POST"
        },
        "endpoint": {
          "description": "The GraphQL endpoint",
          "type": "string",
          "default": "",
          "examples": [
            "http://example.com/graphql"
          ]
        },
        "allowUnauthorizedCerts": {
          "description": "Whether to download the response even if SSL certificate validation is not possible",
          "type": "boolean",
          "default": false
        },
        "requestFormat": {
          "description": "The format for the query payload",
          "type": "string",
          "enum": [
            "graphql",
            "json"
          ],
          "default": "graphql"
        },
        "query": {
          "description": "GraphQL query",
          "type": "string",
          "default": ""
        },
        "variables": {
          "description": "Query variables as JSON object",
          "type": "string",
          "default": ""
        },
        "operationName": {
          "description": "Name of operation to execute",
          "type": "string",
          "default": ""
        },
        "responseFormat": {
          "description": "The format in which the data gets returned from the URL",
          "type": "string",
          "enum": [
            "json",
            "string"
          ],
          "default": "json"
        },
        "dataPropertyName": {
          "description": "Name of the property to which to write the response data",
          "type": "string",
          "default": "data"
        },
        "headerParametersUi": {
          "description": "The headers to send",
          "type": "string",
          "default": {},
          "examples": [
            "Add Header"
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
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "httpBasicAuth",
      "required": true
    },
    {
      "name": "httpCustomAuth",
      "required": true
    },
    {
      "name": "httpDigestAuth",
      "required": true
    },
    {
      "name": "httpHeaderAuth",
      "required": true
    },
    {
      "name": "httpQueryAuth",
      "required": true
    },
    {
      "name": "oAuth1Api",
      "required": true
    },
    {
      "name": "oAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
