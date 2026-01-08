---
title: "Node: HTTP Request"
slug: "node-http-request"
version: "['3', '4', '4.1', '4.2', '4.3']"
updated: "2026-01-08"
summary: "Makes an HTTP request and returns the response data"
node_type: "regular"
group: "['output']"
---

# Node: HTTP Request

**Purpose.** Makes an HTTP request and returns the response data
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `{'light': 'file:httprequest.svg', 'dark': 'file:httprequest.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **httpSslAuth**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **googleApiWarning** when nodeCredentialType=['googleApi']: Make sure you have specified the scope(s) for the Service Account in the credential
- **provideSslCertificatesNotice** when provideSslCertificates=[True]: Provide certificates in node's 'Credential for SSL Certificates' parameter
- **infoMessage**: You can view the raw requests this node makes in your browser's developer console

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `httpSslAuth` | ✓ | {'show': {'provideSslCertificates': [True]}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Curl Import | `curlImport` | curlImport |  | ✗ |  | url |
| Method | `method` | options | GET | ✗ | The request method to use |  |

**Method options:**

* **DELETE** (`DELETE`)
* **GET** (`GET`)
* **HEAD** (`HEAD`)
* **OPTIONS** (`OPTIONS`)
* **PATCH** (`PATCH`)
* **POST** (`POST`)
* **PUT** (`PUT`)

| URL | `url` | string |  | ✓ | The URL to make the request to | e.g. http://example.com/index.html | url |
| Authentication | `authentication` | options | none | ✗ | We've already implemented auth for many services so that you don't have to set it up manually |  |

**Authentication options:**

* **None** (`none`)
* **Predefined Credential Type** (`predefinedCredentialType`) - We've already implemented auth for many services so that you don't have to set it up manually
* **Generic Credential Type** (`genericCredentialType`) - Fully customizable. Choose between basic, header, OAuth2, etc.

| Credential Type | `nodeCredentialType` | credentialsSelect |  | ✓ |  |  |
| Generic Auth Type | `genericAuthType` | credentialsSelect |  | ✓ |  |  |
| SSL Certificates | `provideSslCertificates` | boolean | False | ✗ |  |  |
| SSL Certificate | `sslCertificate` | credentials |  | ✗ |  |  |
| Send Query Parameters | `sendQuery` | boolean | False | ✗ | Whether the request has query params or not |  |
| Specify Query Parameters | `specifyQuery` | options | keypair | ✗ |  |  |

**Specify Query Parameters options:**

* **Using Fields Below** (`keypair`)
* **Using JSON** (`json`)

| Query Parameters | `queryParameters` | fixedCollection |  | ✗ | e.g. Add Parameter |  |

<details>
<summary><strong>Query Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Parameter | `parameters` |  |  |  |

</details>

| JSON | `jsonQuery` | json |  | ✗ |  |  |
| Send Headers | `sendHeaders` | boolean | False | ✗ | Whether the request has headers or not |  |
| Specify Headers | `specifyHeaders` | options | keypair | ✗ |  |  |

**Specify Headers options:**

* **Using Fields Below** (`keypair`)
* **Using JSON** (`json`)

| Header Parameters | `headerParameters` | fixedCollection |  | ✗ | e.g. Add Parameter |  |

<details>
<summary><strong>Header Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Parameter | `parameters` |  |  |  |

</details>

| JSON | `jsonHeaders` | json |  | ✗ |  |  |
| Send Body | `sendBody` | boolean | False | ✗ | Whether the request has a body or not |  |
| Body Content Type | `contentType` | options | json | ✗ | Content-Type to use to send body parameters |  |

**Body Content Type options:**

* **Form Urlencoded** (`form-urlencoded`)
* **Form-Data** (`multipart-form-data`)
* **JSON** (`json`)
* **n8n Binary File** (`binaryData`)
* **Raw** (`raw`)

| Specify Body | `specifyBody` | options | keypair | ✗ | The body can be specified using explicit fields (<code>keypair</code>) or using a JavaScript object (<code>json</code>) |  |

**Specify Body options:**

* **Using Fields Below** (`keypair`)
* **Using JSON** (`json`)

| Body Parameters | `bodyParameters` | fixedCollection |  | ✗ | ID of the field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Parameter |  |

<details>
<summary><strong>Body Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Parameter | `parameters` |  |  |  |

</details>

| JSON | `jsonBody` | json |  | ✗ |  |  |
| Body Parameters | `bodyParameters` | fixedCollection | formData | ✗ | ID of the field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Parameter |  |

<details>
<summary><strong>Body Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Parameter | `parameters` |  |  |  |

</details>

| Specify Body | `specifyBody` | options | keypair | ✗ |  |  |

**Specify Body options:**

* **Using Fields Below** (`keypair`)
* **Using Single Field** (`string`)

| Body Parameters | `bodyParameters` | fixedCollection |  | ✗ | ID of the field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Parameter |  |

<details>
<summary><strong>Body Parameters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Parameter | `parameters` |  |  |  |

</details>

| Body | `body` | string |  | ✗ | e.g. field1=value1&field2=value2 |  |
| Input Data Field Name | `inputDataFieldName` | string |  | ✗ | The name of the incoming field containing the binary file data to be processed |  |
| Content Type | `rawContentType` | string |  | ✗ | e.g. text/html |  |
| Body | `body` | string |  | ✗ |  |  |
| Options | `options` | collection | {} | ✓ | Input will be split in batches to throttle requests. -1 for disabled. 0 will be treated as 1. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Batching | `batching` | fixedCollection | 50 | Input will be split in batches to throttle requests. -1 for disabled. 0 will be treated as 1. |
| Ignore SSL Issues (Insecure) | `allowUnauthorizedCerts` | boolean | False | Whether to download the response even if SSL certificate validation is not possible |
| Array Format in Query Parameters | `queryParameterArrays` | options | brackets | e.g. foo=bar&foo=qux |
| Lowercase Headers | `lowercaseHeaders` | boolean | True | Whether to lowercase header names |
| Redirects | `redirect` | fixedCollection | False | Whether to follow all redirects |
| Redirects | `redirect` | fixedCollection | True | Whether to follow all redirects |
| Response | `response` | fixedCollection | False | Whether to return the full response (headers and response status code) data instead of only the body |
| Pagination | `pagination` | fixedCollection | updateAParameterInEachRequest | If pagination should be used |
| Proxy | `proxy` | string |  | HTTP proxy to use |
| Timeout | `timeout` | number | 10000 | Time in ms to wait for the server to send response headers (and start the response body) before aborting the request |

</details>

| Optimize Response | `optimizeResponse` | boolean | False | ✗ | Whether the optimize the tool response to reduce amount of data passed to the LLM that could lead to better result and reduce cost |  |
| Expected Response Type | `responseType` | options | json | ✗ |  |  |

**Expected Response Type options:**

* **JSON** (`json`)
* **HTML** (`html`)
* **Text** (`text`)

| Field Containing Data | `dataField` | string |  | ✗ | Specify the name of the field in the response containing the data | e.g. e.g. records |  |
| Include Fields | `fieldsToInclude` | options | all | ✗ | What fields response object should include |  |

**Include Fields options:**

* **All** (`all`) - Include all fields
* **Selected** (`selected`) - Include only fields specified below
* **Except** (`except`) - Exclude fields specified below

| Fields | `fields` | string |  | ✗ | Comma-separated list of the field names. Supports dot notation. You can drag the selected fields from the input panel. | e.g. e.g. field1,field2 |  |
| Selector (CSS) | `cssSelector` | string | body | ✗ | Select specific element(e.g. body) or multiple elements(e.g. div) of chosen type in the response HTML. | e.g. e.g. body |  |
| Return Only Content | `onlyContent` | boolean | False | ✗ | Whether to return only content of html elements, stripping html tags and attributes | e.g. Uses less tokens and may be easier for model to understand |  |
| Elements To Omit | `elementsToOmit` | string |  | ✗ | Comma-separated list of selectors that would be excluded when extracting content | e.g. e.g. img, .className, #ItemId |  |
| Truncate Response | `truncateResponse` | boolean | False | ✗ | e.g. Helps save tokens |  |
| Max Response Characters | `maxLength` | number | 1000 | ✗ |  | min:1, max:∞ |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["method"] + ": " + $parameter["url"]}}`
- `={{false}}`
- `={{ Array.isArray($response.body) ? $response.body.length : !!$response.body }}`

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
node: HTTP Request
displayName: HTTP Request
description: Makes an HTTP request and returns the response data
version:
- '3'
- '4'
- '4.1'
- '4.2'
- '4.3'
nodeType: regular
group:
- output
credentials:
- name: httpSslAuth
  required: true
params:
- id: curlImport
  name: Curl Import
  type: curlImport
  default: ''
  required: false
  description: ''
  validation:
    format: url
  typeInfo:
    type: curlImport
    displayName: Curl Import
    name: curlImport
- id: method
  name: Method
  type: options
  default: GET
  required: false
  description: The request method to use
  typeInfo:
    type: options
    displayName: Method
    name: method
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
    - value: OPTIONS
      name: OPTIONS
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
- id: url
  name: URL
  type: string
  default: ''
  required: true
  description: The URL to make the request to
  placeholder: http://example.com/index.html
  validation:
    required: true
    format: url
  typeInfo:
    type: string
    displayName: URL
    name: url
- id: authentication
  name: Authentication
  type: options
  default: none
  required: false
  description: We've already implemented auth for many services so that you don't
    have to set it up manually
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: none
      name: None
      description: ''
    - value: predefinedCredentialType
      name: Predefined Credential Type
      description: We've already implemented auth for many services so that you don't
        have to set it up manually
    - value: genericCredentialType
      name: Generic Credential Type
      description: Fully customizable. Choose between basic, header, OAuth2, etc.
- id: nodeCredentialType
  name: Credential Type
  type: credentialsSelect
  default: ''
  required: true
  description: ''
  validation:
    required: true
    displayOptions:
      show:
        authentication:
        - predefinedCredentialType
  typeInfo:
    type: credentialsSelect
    displayName: Credential Type
    name: nodeCredentialType
- id: genericAuthType
  name: Generic Auth Type
  type: credentialsSelect
  default: ''
  required: true
  description: ''
  validation:
    required: true
    displayOptions:
      show:
        authentication:
        - genericCredentialType
  typeInfo:
    type: credentialsSelect
    displayName: Generic Auth Type
    name: genericAuthType
- id: provideSslCertificates
  name: SSL Certificates
  type: boolean
  default: false
  required: false
  description: ''
  typeInfo:
    type: boolean
    displayName: SSL Certificates
    name: provideSslCertificates
- id: sslCertificate
  name: SSL Certificate
  type: credentials
  default: ''
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        provideSslCertificates:
        - true
  typeInfo:
    type: credentials
    displayName: SSL Certificate
    name: sslCertificate
- id: sendQuery
  name: Send Query Parameters
  type: boolean
  default: false
  required: false
  description: Whether the request has query params or not
  typeInfo:
    type: boolean
    displayName: Send Query Parameters
    name: sendQuery
- id: specifyQuery
  name: Specify Query Parameters
  type: options
  default: keypair
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        sendQuery:
        - true
  typeInfo:
    type: options
    displayName: Specify Query Parameters
    name: specifyQuery
    possibleValues:
    - value: keypair
      name: Using Fields Below
      description: ''
    - value: json
      name: Using JSON
      description: ''
- id: queryParameters
  name: Query Parameters
  type: fixedCollection
  default: ''
  required: false
  description: ''
  placeholder: Add Parameter
  validation:
    displayOptions:
      show:
        sendQuery:
        - true
        specifyQuery:
        - keypair
  typeInfo:
    type: fixedCollection
    displayName: Query Parameters
    name: queryParameters
    typeOptions:
      multipleValues: true
    subProperties:
    - name: parameters
      displayName: Parameter
      values:
      - displayName: Name
        name: name
        type: string
        default: ''
      - displayName: Value
        name: value
        type: string
        default: ''
- id: jsonQuery
  name: JSON
  type: json
  default: ''
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        sendQuery:
        - true
        specifyQuery:
        - json
  typeInfo:
    type: json
    displayName: JSON
    name: jsonQuery
- id: sendHeaders
  name: Send Headers
  type: boolean
  default: false
  required: false
  description: Whether the request has headers or not
  typeInfo:
    type: boolean
    displayName: Send Headers
    name: sendHeaders
- id: specifyHeaders
  name: Specify Headers
  type: options
  default: keypair
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        sendHeaders:
        - true
  typeInfo:
    type: options
    displayName: Specify Headers
    name: specifyHeaders
    possibleValues:
    - value: keypair
      name: Using Fields Below
      description: ''
    - value: json
      name: Using JSON
      description: ''
- id: headerParameters
  name: Header Parameters
  type: fixedCollection
  default: ''
  required: false
  description: ''
  placeholder: Add Parameter
  validation:
    displayOptions:
      show:
        sendHeaders:
        - true
        specifyHeaders:
        - keypair
  typeInfo:
    type: fixedCollection
    displayName: Header Parameters
    name: headerParameters
    typeOptions:
      multipleValues: true
    subProperties:
    - name: parameters
      displayName: Parameter
      values:
      - displayName: Name
        name: name
        type: string
        default: ''
      - displayName: Value
        name: value
        type: string
        default: ''
- id: jsonHeaders
  name: JSON
  type: json
  default: ''
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        sendHeaders:
        - true
        specifyHeaders:
        - json
  typeInfo:
    type: json
    displayName: JSON
    name: jsonHeaders
- id: sendBody
  name: Send Body
  type: boolean
  default: false
  required: false
  description: Whether the request has a body or not
  typeInfo:
    type: boolean
    displayName: Send Body
    name: sendBody
- id: contentType
  name: Body Content Type
  type: options
  default: json
  required: false
  description: Content-Type to use to send body parameters
  validation:
    displayOptions:
      show:
        sendBody:
        - true
  typeInfo:
    type: options
    displayName: Body Content Type
    name: contentType
    possibleValues:
    - value: form-urlencoded
      name: Form Urlencoded
      description: ''
    - value: multipart-form-data
      name: Form-Data
      description: ''
    - value: json
      name: JSON
      description: ''
    - value: binaryData
      name: n8n Binary File
      description: ''
    - value: raw
      name: Raw
      description: ''
- id: specifyBody
  name: Specify Body
  type: options
  default: keypair
  required: false
  description: The body can be specified using explicit fields (<code>keypair</code>)
    or using a JavaScript object (<code>json</code>)
  validation: &id003
    displayOptions:
      show:
        sendBody:
        - true
        contentType:
        - form-urlencoded
  typeInfo: &id004
    type: options
    displayName: Specify Body
    name: specifyBody
    possibleValues:
    - value: keypair
      name: Using Fields Below
      description: ''
    - value: string
      name: Using Single Field
      description: ''
- id: bodyParameters
  name: Body Parameters
  type: fixedCollection
  default: ''
  required: false
  description: ID of the field to set. Choose from the list, or specify an ID using
    an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  placeholder: Add Parameter
  validation: &id001
    displayOptions:
      show:
        sendBody:
        - true
        contentType:
        - form-urlencoded
        specifyBody:
        - keypair
  typeInfo: &id002
    type: fixedCollection
    displayName: Body Parameters
    name: bodyParameters
    typeOptions:
      multipleValues: true
    subProperties:
    - name: parameters
      displayName: Parameter
      values:
      - displayName: Name
        name: name
        type: string
        description: ID of the field to set. Choose from the list, or specify an ID
          using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
        default: ''
      - displayName: Value
        name: value
        type: string
        description: Value of the field to set
        default: ''
- id: jsonBody
  name: JSON
  type: json
  default: ''
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        sendBody:
        - true
        contentType:
        - json
        specifyBody:
        - json
  typeInfo:
    type: json
    displayName: JSON
    name: jsonBody
- id: bodyParameters
  name: Body Parameters
  type: fixedCollection
  default: formData
  required: false
  description: ID of the field to set. Choose from the list, or specify an ID using
    an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  placeholder: Add Parameter
  validation: *id001
  typeInfo: *id002
- id: specifyBody
  name: Specify Body
  type: options
  default: keypair
  required: false
  description: ''
  validation: *id003
  typeInfo: *id004
- id: bodyParameters
  name: Body Parameters
  type: fixedCollection
  default: ''
  required: false
  description: ID of the field to set. Choose from the list, or specify an ID using
    an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  placeholder: Add Parameter
  validation: *id001
  typeInfo: *id002
- id: body
  name: Body
  type: string
  default: ''
  required: false
  description: ''
  placeholder: field1=value1&field2=value2
  validation: &id005
    displayOptions:
      show:
        sendBody:
        - true
        contentType:
        - raw
  typeInfo: &id006
    type: string
    displayName: Body
    name: body
- id: inputDataFieldName
  name: Input Data Field Name
  type: string
  default: ''
  required: false
  description: The name of the incoming field containing the binary file data to be
    processed
  validation:
    displayOptions:
      show:
        sendBody:
        - true
        contentType:
        - binaryData
  typeInfo:
    type: string
    displayName: Input Data Field Name
    name: inputDataFieldName
- id: rawContentType
  name: Content Type
  type: string
  default: ''
  required: false
  description: ''
  placeholder: text/html
  validation:
    displayOptions:
      show:
        sendBody:
        - true
        contentType:
        - raw
  typeInfo:
    type: string
    displayName: Content Type
    name: rawContentType
- id: body
  name: Body
  type: string
  default: ''
  required: false
  description: ''
  validation: *id005
  typeInfo: *id006
- id: options
  name: Options
  type: collection
  default: {}
  required: true
  description: Input will be split in batches to throttle requests. -1 for disabled.
    0 will be treated as 1.
  hint: Use expression mode and $response to access response data
  placeholder: Add option
  validation:
    required: true
    displayOptions:
      show: {}
  typeInfo:
    type: collection
    displayName: Options
    name: options
    typeOptions:
      multipleValues: false
    subProperties:
    - displayName: Batching
      name: batching
      type: fixedCollection
      description: Input will be split in batches to throttle requests. -1 for disabled.
        0 will be treated as 1.
      placeholder: Add Batching
      default: 50
      options:
      - name: batch
        displayName: Batching
        values:
        - displayName: Items per Batch
          name: batchSize
          type: number
          description: Input will be split in batches to throttle requests. -1 for
            disabled. 0 will be treated as 1.
          default: 50
          typeOptions: {}
        - displayName: Batch Interval (ms)
          name: batchInterval
          type: number
          description: Time (in milliseconds) between each batch of requests. 0 for
            disabled.
          default: 1000
          typeOptions:
            minValue: 0
      typeOptions:
        multipleValues: false
    - displayName: Ignore SSL Issues (Insecure)
      name: allowUnauthorizedCerts
      type: boolean
      description: Whether to download the response even if SSL certificate validation
        is not possible
      default: false
      noDataExpression: true
    - displayName: Array Format in Query Parameters
      name: queryParameterArrays
      type: options
      description: e.g. foo=bar&foo=qux
      value: repeat
      default: brackets
      options:
      - name: No Brackets
        description: e.g. foo=bar&foo=qux
        value: repeat
        displayName: No Brackets
      - name: Brackets Only
        description: e.g. foo[]=bar&foo[]=qux
        value: brackets
        displayName: Brackets Only
      - name: Brackets with Indices
        description: e.g. foo[0]=bar&foo[1]=qux
        value: indices
        displayName: Brackets With Indices
      displayOptions:
        show: {}
    - displayName: Lowercase Headers
      name: lowercaseHeaders
      type: boolean
      description: Whether to lowercase header names
      default: true
    - displayName: Redirects
      name: redirect
      type: fixedCollection
      description: Whether to follow all redirects
      placeholder: Add Redirect
      default: false
      noDataExpression: true
      options:
      - name: redirect
        displayName: Redirect
        values:
        - displayName: Follow Redirects
          name: followRedirects
          type: boolean
          description: Whether to follow all redirects
          default: false
          noDataExpression: true
        - displayName: Max Redirects
          name: maxRedirects
          type: number
          description: Max number of redirects to follow
          default: 21
          displayOptions:
            show:
              followRedirects:
              - true
      typeOptions:
        multipleValues: false
      displayOptions:
        show:
          followRedirects:
          - true
    - displayName: Redirects
      name: redirect
      type: fixedCollection
      description: Whether to follow all redirects
      placeholder: Add Redirect
      default: true
      noDataExpression: true
      options:
      - name: redirect
        displayName: Redirect
        values:
        - displayName: Follow Redirects
          name: followRedirects
          type: boolean
          description: Whether to follow all redirects
          default: true
          noDataExpression: true
        - displayName: Max Redirects
          name: maxRedirects
          type: number
          description: Max number of redirects to follow
          default: 21
          displayOptions:
            show:
              followRedirects:
              - true
      typeOptions:
        multipleValues: false
      displayOptions:
        show:
          followRedirects:
          - true
    - displayName: Response
      name: response
      type: fixedCollection
      description: Whether to return the full response (headers and response status
        code) data instead of only the body
      placeholder: Add response
      value: autodetect
      default: false
      required: true
      noDataExpression: true
      options:
      - name: response
        displayName: Response
        values:
        - displayName: Include Response Headers and Status
          name: fullResponse
          type: boolean
          description: Whether to return the full response (headers and response status
            code) data instead of only the body
          default: false
        - displayName: Never Error
          name: neverError
          type: boolean
          description: Whether to succeeds also when status code is not 2xx
          default: false
        - displayName: Response Format
          name: responseFormat
          type: options
          description: The format in which the data gets returned from the URL
          value: autodetect
          default: autodetect
          noDataExpression: true
          options:
          - name: Autodetect
            value: autodetect
            displayName: Autodetect
          - name: File
            value: file
            displayName: File
          - name: JSON
            value: json
            displayName: Json
          - name: Text
            value: text
            displayName: Text
        - displayName: Put Output in Field
          name: outputPropertyName
          type: string
          description: Name of the binary property to which to write the data of the
            read file
          default: data
          required: true
          displayOptions:
            show:
              responseFormat:
              - file
              - text
      typeOptions:
        multipleValues: false
      displayOptions:
        show:
          responseFormat:
          - file
          - text
    - displayName: Pagination
      name: pagination
      type: fixedCollection
      description: If pagination should be used
      placeholder: Add pagination
      hint: Use expression mode and $response to access response data
      value: 'off'
      default: updateAParameterInEachRequest
      noDataExpression: true
      options:
      - name: pagination
        displayName: Pagination
        values:
        - displayName: Pagination Mode
          name: paginationMode
          type: options
          description: If pagination should be used
          value: 'off'
          default: updateAParameterInEachRequest
          noDataExpression: true
          options:
          - name: 'Off'
            value: 'off'
            displayName: 'Off'
          - name: Update a Parameter in Each Request
            value: updateAParameterInEachRequest
            displayName: Update A Parameter In Each Request
          - name: Response Contains Next URL
            value: responseContainsNextURL
            displayName: Response Contains Next Url
          typeOptions: {}
        - displayName: Use the $response variables to access the data of the previous
            response. Refer to the <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/#pagination/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.httprequest"
            target="_blank">docs</a> for more info about pagination/
          name: webhookNotice
          type: notice
          default: ''
          displayOptions:
            hide:
              paginationMode:
              - 'off'
        - displayName: Next URL
          name: nextURL
          type: string
          description: Should evaluate to the URL of the next page. <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/#pagination"
            target="_blank">More info</a>.
          default: ''
          displayOptions:
            show:
              paginationMode:
              - responseContainsNextURL
        - displayName: Parameters
          name: parameters
          type: fixedCollection
          description: Where the parameter should be set
          placeholder: Add Parameter
          hint: Use expression mode and $response to access response data
          default: qs
          options:
          - name: parameters
            displayName: Parameter
            values:
            - displayName: Type
              name: type
              type: options
              description: Where the parameter should be set
              value: body
              default: qs
              options:
              - name: Body
                value: body
                displayName: Body
              - name: Header
                value: headers
                displayName: Header
              - name: Query
                value: qs
                displayName: Query
            - displayName: Name
              name: name
              type: string
              placeholder: e.g page
              default: ''
            - displayName: Value
              name: value
              type: string
              hint: Use expression mode and $response to access response data
              default: ''
          typeOptions:
            multipleValues: true
          displayOptions:
            show:
              paginationMode:
              - updateAParameterInEachRequest
        - displayName: Pagination Complete When
          name: paginationCompleteWhen
          type: options
          description: When should no further requests be made?
          value: responseIsEmpty
          default: responseIsEmpty
          noDataExpression: true
          options:
          - name: Response Is Empty
            value: responseIsEmpty
            displayName: Response Is Empty
          - name: Receive Specific Status Code(s)
            value: receiveSpecificStatusCodes
            displayName: Receive Specific Status Code(s)
          - name: Other
            value: other
            displayName: Other
          typeOptions: {}
          displayOptions:
            hide:
              paginationMode:
              - 'off'
        - displayName: Status Code(s) when Complete
          name: statusCodesWhenComplete
          type: string
          description: Accepts comma-separated values
          default: ''
          noDataExpression: true
          typeOptions: {}
          displayOptions:
            show:
              paginationCompleteWhen:
              - receiveSpecificStatusCodes
        - displayName: Complete Expression
          name: completeExpression
          type: string
          description: Should evaluate to true when pagination is complete. <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/#pagination"
            target="_blank">More info</a>.
          default: ''
          displayOptions:
            show:
              paginationCompleteWhen:
              - other
        - displayName: Limit Pages Fetched
          name: limitPagesFetched
          type: boolean
          description: Whether the number of requests should be limited
          default: false
          noDataExpression: true
          typeOptions: {}
          displayOptions:
            hide:
              paginationMode:
              - 'off'
        - displayName: Max Pages
          name: maxRequests
          type: number
          description: Maximum amount of request to be make
          default: 100
          noDataExpression: true
          typeOptions: {}
          displayOptions:
            show:
              limitPagesFetched:
              - true
        - displayName: Interval Between Requests (ms)
          name: requestInterval
          type: number
          description: Time in milliseconds to wait between requests
          hint: At 0 no delay will be added
          default: 0
          typeOptions:
            minValue: 0
          displayOptions:
            hide:
              paginationMode:
              - 'off'
      typeOptions:
        multipleValues: false
      displayOptions:
        hide:
          paginationMode:
          - 'off'
    - displayName: Proxy
      name: proxy
      type: string
      description: HTTP proxy to use
      placeholder: e.g. http://myproxy:3128
      default: ''
    - displayName: Timeout
      name: timeout
      type: number
      description: Time in ms to wait for the server to send response headers (and
        start the response body) before aborting the request
      default: 10000
      typeOptions:
        minValue: 1
- id: optimizeResponse
  name: Optimize Response
  type: boolean
  default: false
  required: false
  description: Whether the optimize the tool response to reduce amount of data passed
    to the LLM that could lead to better result and reduce cost
  validation:
    displayOptions:
      show:
        '@tool':
        - true
  typeInfo:
    type: boolean
    displayName: Optimize Response
    name: optimizeResponse
- id: responseType
  name: Expected Response Type
  type: options
  default: json
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        optimizeResponse:
        - true
        '@tool':
        - true
  typeInfo:
    type: options
    displayName: Expected Response Type
    name: responseType
    possibleValues:
    - value: json
      name: JSON
      description: ''
    - value: html
      name: HTML
      description: ''
    - value: text
      name: Text
      description: ''
- id: dataField
  name: Field Containing Data
  type: string
  default: ''
  required: false
  description: Specify the name of the field in the response containing the data
  hint: leave blank to use whole response
  placeholder: e.g. records
  validation:
    displayOptions:
      show:
        optimizeResponse:
        - true
        responseType:
        - json
        '@tool':
        - true
  typeInfo:
    type: string
    displayName: Field Containing Data
    name: dataField
- id: fieldsToInclude
  name: Include Fields
  type: options
  default: all
  required: false
  description: What fields response object should include
  validation:
    displayOptions:
      show:
        optimizeResponse:
        - true
        responseType:
        - json
        '@tool':
        - true
  typeInfo:
    type: options
    displayName: Include Fields
    name: fieldsToInclude
    possibleValues:
    - value: all
      name: All
      description: Include all fields
    - value: selected
      name: Selected
      description: Include only fields specified below
    - value: except
      name: Except
      description: Exclude fields specified below
- id: fields
  name: Fields
  type: string
  default: ''
  required: false
  description: Comma-separated list of the field names. Supports dot notation. You
    can drag the selected fields from the input panel.
  placeholder: e.g. field1,field2
  validation:
    displayOptions:
      show:
        optimizeResponse:
        - true
        responseType:
        - json
        '@tool':
        - true
      hide:
        fieldsToInclude:
        - all
  typeInfo:
    type: string
    displayName: Fields
    name: fields
- id: cssSelector
  name: Selector (CSS)
  type: string
  default: body
  required: false
  description: Select specific element(e.g. body) or multiple elements(e.g. div) of
    chosen type in the response HTML.
  placeholder: e.g. body
  validation:
    displayOptions:
      show:
        optimizeResponse:
        - true
        responseType:
        - html
        '@tool':
        - true
  typeInfo:
    type: string
    displayName: Selector (CSS)
    name: cssSelector
- id: onlyContent
  name: Return Only Content
  type: boolean
  default: false
  required: false
  description: Whether to return only content of html elements, stripping html tags
    and attributes
  hint: Uses less tokens and may be easier for model to understand
  validation:
    displayOptions:
      show:
        optimizeResponse:
        - true
        responseType:
        - html
        '@tool':
        - true
  typeInfo:
    type: boolean
    displayName: Return Only Content
    name: onlyContent
- id: elementsToOmit
  name: Elements To Omit
  type: string
  default: ''
  required: false
  description: Comma-separated list of selectors that would be excluded when extracting
    content
  placeholder: 'e.g. img, .className, #ItemId'
  validation:
    displayOptions:
      show:
        optimizeResponse:
        - true
        responseType:
        - html
        onlyContent:
        - true
        '@tool':
        - true
  typeInfo:
    type: string
    displayName: Elements To Omit
    name: elementsToOmit
- id: truncateResponse
  name: Truncate Response
  type: boolean
  default: false
  required: false
  description: ''
  hint: Helps save tokens
  validation:
    displayOptions:
      show:
        optimizeResponse:
        - true
        responseType:
        - text
        - html
        '@tool':
        - true
  typeInfo:
    type: boolean
    displayName: Truncate Response
    name: truncateResponse
- id: maxLength
  name: Max Response Characters
  type: number
  default: 1000
  required: false
  description: ''
  validation:
    displayOptions:
      show:
        optimizeResponse:
        - true
        responseType:
        - text
        - html
        truncateResponse:
        - true
        '@tool':
        - true
  typeInfo:
    type: number
    displayName: Max Response Characters
    name: maxLength
    typeOptions:
      minValue: 1
common_expressions:
- '={{$parameter["method"] + ": " + $parameter["url"]}}'
- ={{false}}
- '={{ Array.isArray($response.body) ? $response.body.length : !!$response.body }}'
ui_elements:
  notices:
  - name: googleApiWarning
    text: Make sure you have specified the scope(s) for the Service Account in the
      credential
    conditions:
      show:
        nodeCredentialType:
        - googleApi
  - name: provideSslCertificatesNotice
    text: Provide certificates in node's 'Credential for SSL Certificates' parameter
    conditions:
      show:
        provideSslCertificates:
        - true
  - name: infoMessage
    text: You can view the raw requests this node makes in your browser's developer
      console
    conditions: null
  tooltips: []
  placeholders:
  - field: url
    text: http://example.com/index.html
  - field: queryParameters
    text: Add Parameter
  - field: headerParameters
    text: Add Parameter
  - field: bodyParameters
    text: Add Parameter
  - field: bodyParameters
    text: Add Parameter
  - field: bodyParameters
    text: Add Parameter
  - field: body
    text: field1=value1&field2=value2
  - field: rawContentType
    text: text/html
  - field: options
    text: Add option
  - field: dataField
    text: e.g. records
  - field: fields
    text: e.g. field1,field2
  - field: cssSelector
    text: e.g. body
  - field: elementsToOmit
    text: 'e.g. img, .className, #ItemId'
  hints:
  - field: options
    text: Use expression mode and $response to access response data
  - field: dataField
    text: leave blank to use whole response
  - field: onlyContent
    text: Uses less tokens and may be easier for model to understand
  - field: truncateResponse
    text: Helps save tokens
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
  "$id": "https://n8n.io/schemas/nodes/HTTP Request.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HTTP Request Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "curlImport": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "method": {
          "description": "The request method to use",
          "type": "string",
          "enum": [
            "DELETE",
            "GET",
            "HEAD",
            "OPTIONS",
            "PATCH",
            "POST",
            "PUT"
          ],
          "default": "GET"
        },
        "url": {
          "description": "The URL to make the request to",
          "type": "string",
          "default": "",
          "format": "url",
          "examples": [
            "http://example.com/index.html"
          ]
        },
        "authentication": {
          "description": "We've already implemented auth for many services so that you don't have to set it up manually",
          "type": "string",
          "enum": [
            "none",
            "predefinedCredentialType",
            "genericCredentialType"
          ],
          "default": "none"
        },
        "nodeCredentialType": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "genericAuthType": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "provideSslCertificates": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "sslCertificate": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "sendQuery": {
          "description": "Whether the request has query params or not",
          "type": "boolean",
          "default": false
        },
        "specifyQuery": {
          "description": "",
          "type": "string",
          "enum": [
            "keypair",
            "json"
          ],
          "default": "keypair"
        },
        "queryParameters": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Add Parameter"
          ]
        },
        "jsonQuery": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "sendHeaders": {
          "description": "Whether the request has headers or not",
          "type": "boolean",
          "default": false
        },
        "specifyHeaders": {
          "description": "",
          "type": "string",
          "enum": [
            "keypair",
            "json"
          ],
          "default": "keypair"
        },
        "headerParameters": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "Add Parameter"
          ]
        },
        "jsonHeaders": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "sendBody": {
          "description": "Whether the request has a body or not",
          "type": "boolean",
          "default": false
        },
        "contentType": {
          "description": "Content-Type to use to send body parameters",
          "type": "string",
          "enum": [
            "form-urlencoded",
            "multipart-form-data",
            "json",
            "binaryData",
            "raw"
          ],
          "default": "json"
        },
        "specifyBody": {
          "description": "",
          "type": "string",
          "enum": [
            "keypair",
            "string"
          ],
          "default": "keypair"
        },
        "bodyParameters": {
          "description": "ID of the field to set. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": "",
          "examples": [
            "Add Parameter"
          ]
        },
        "jsonBody": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "body": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "inputDataFieldName": {
          "description": "The name of the incoming field containing the binary file data to be processed",
          "type": "string",
          "default": ""
        },
        "rawContentType": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "text/html"
          ]
        },
        "options": {
          "description": "Input will be split in batches to throttle requests. -1 for disabled. 0 will be treated as 1.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "optimizeResponse": {
          "description": "Whether the optimize the tool response to reduce amount of data passed to the LLM that could lead to better result and reduce cost",
          "type": "boolean",
          "default": false
        },
        "responseType": {
          "description": "",
          "type": "string",
          "enum": [
            "json",
            "html",
            "text"
          ],
          "default": "json"
        },
        "dataField": {
          "description": "Specify the name of the field in the response containing the data",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. records"
          ]
        },
        "fieldsToInclude": {
          "description": "What fields response object should include",
          "type": "string",
          "enum": [
            "all",
            "selected",
            "except"
          ],
          "default": "all"
        },
        "fields": {
          "description": "Comma-separated list of the field names. Supports dot notation. You can drag the selected fields from the input panel.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. field1,field2"
          ]
        },
        "cssSelector": {
          "description": "Select specific element(e.g. body) or multiple elements(e.g. div) of chosen type in the response HTML.",
          "type": "string",
          "default": "body",
          "examples": [
            "e.g. body"
          ]
        },
        "onlyContent": {
          "description": "Whether to return only content of html elements, stripping html tags and attributes",
          "type": "boolean",
          "default": false
        },
        "elementsToOmit": {
          "description": "Comma-separated list of selectors that would be excluded when extracting content",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. img, .className, #ItemId"
          ]
        },
        "truncateResponse": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "maxLength": {
          "description": "",
          "type": "number",
          "default": 1000
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
      "3",
      "4",
      "4.1",
      "4.2",
      "4.3"
    ]
  },
  "credentials": [
    {
      "name": "httpSslAuth",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['3', '4', '4.1', '4.2', '4.3'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
