---
title: "Node: One Simple API"
slug: "node-onesimpleapi"
version: "1"
updated: "2026-01-08"
summary: "A toolbox of no-code utilities"
node_type: "regular"
group: "['transform']"
---

# Node: One Simple API

**Purpose.** A toolbox of no-code utilities


---

## Node Details

- **Icon:** `file:onesimpleapi.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **oneSimpleApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `oneSimpleApi` | ✓ | - |

---

## Operations

### Website Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Generate PDF | `pdf` | Generate a PDF from a webpage |
| Get SEO Data | `seo` | Get SEO information from website |
| Take Screenshot | `screenshot` | Create a screenshot from a webpage |

### Socialprofile Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Instagram | `instagramProfile` | Get details about an Instagram profile |
| Spotify | `spotifyArtistProfile` | Get details about a Spotify Artist |

### Information Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Exchange Rate | `exchangeRate` | Convert a value between currencies |
| Image Metadata | `imageMetadata` | Retrieve image metadata from a URL |

### Utility Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Expand URL | `expandURL` | Expand a shortened URL |
| Generate QR Code | `qrCode` | Generate a QR Code |
| Validate Email | `validateEmail` | Validate an email address |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | website | ✓ | Resource to operate on |  |

**Resource options:**

* **Information** (`information`)
* **Social Profile** (`socialProfile`)
* **Utility** (`utility`)
* **Website** (`website`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | pdf | ✗ | Generate a PDF from a webpage |  |

**Operation options:**

* **Generate PDF** (`pdf`) - Generate a PDF from a webpage
* **Get SEO Data** (`seo`) - Get SEO information from website
* **Take Screenshot** (`screenshot`) - Create a screenshot from a webpage

---

### Generate PDF parameters (`pdf`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Webpage URL | `link` | string |  | ✓ | Link to webpage to convert |  |
| Download PDF? | `download` | boolean | False | ✓ | Whether to download the PDF or return a link to it |  |
| Put Output In Field | `output` | string | data | ✓ | The name of the output field to put the binary file data in |  |
| Options | `options` | collection | {} | ✗ | Normally the API will reuse a previously taken screenshot of the URL to give a faster response. This option allows you to retake the screenshot at that exact time, for those times when it's necessary. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Page Size | `page` | options |  |  |
| Force Refresh | `force` | boolean | False | Normally the API will reuse a previously taken screenshot of the URL to give a faster response. This option allows you to retake the screenshot at that exact time, for those times when it's necessary. |

</details>


### Get SEO Data parameters (`seo`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Webpage URL | `link` | string |  | ✓ | Webpage to get SEO information for |  |
| Options | `options` | collection | {} | ✗ | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Headers? | `headers` | boolean | False |  |

</details>


### Take Screenshot parameters (`screenshot`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Webpage URL | `link` | string |  | ✓ | Link to webpage to convert |  |
| Download Screenshot? | `download` | boolean | False | ✓ | Whether to download the screenshot or return a link to it |  |
| Put Output In Field | `output` | string | data | ✓ | The name of the output field to put the binary file data in |  |
| Options | `options` | collection | {} | ✗ | Normally the API will reuse a previously taken screenshot of the URL to give a faster response. This option allows you to retake the screenshot at that exact time, for those times when it's necessary. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Screen Size | `screen` | options |  |  |
| Force Refresh | `force` | boolean | False | Normally the API will reuse a previously taken screenshot of the URL to give a faster response. This option allows you to retake the screenshot at that exact time, for those times when it's necessary. |
| Full Page | `fullpage` | boolean | False | The API takes a screenshot of the viewable area for the desired screen size. If you need a screenshot of the whole length of the page, use this option. |

</details>


### Instagram parameters (`instagramProfile`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Profile Name | `profileName` | string |  | ✓ | Profile name to get details of |  |

### Spotify parameters (`spotifyArtistProfile`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Artist Name | `artistName` | string |  | ✓ | Artist name to get details for |  |

### Exchange Rate parameters (`exchangeRate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Value | `value` | string |  | ✓ | Value to convert |  |
| From Currency | `fromCurrency` | string |  | ✓ | e.g. USD |  |
| To Currency | `toCurrency` | string |  | ✓ | e.g. EUR |  |

### Image Metadata parameters (`imageMetadata`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Link To Image | `link` | string |  | ✓ | Image to get metadata from |  |

### Expand URL parameters (`expandURL`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| URL | `link` | string |  | ✓ | URL to unshorten |  |

### Generate QR Code parameters (`qrCode`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| QR Content | `message` | string |  | ✓ | The text that should be turned into a QR code - like a website URL |  |
| Download Image? | `download` | boolean | False | ✓ | Whether to download the QR code or return a link to it |  |
| Put Output In Field | `output` | string | data | ✓ | The name of the output field to put the binary file data in |  |
| Options | `options` | collection | {} | ✗ | The QR Code size | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Size | `size` | options | Small | The QR Code size |
| Format | `format` | options | PNG | The QR Code format |

</details>


### Validate Email parameters (`validateEmail`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email Address | `emailAddress` | string |  | ✓ |  | email |

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
* Categories: Utility

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: oneSimpleApi
displayName: One Simple API
description: A toolbox of no-code utilities
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: oneSimpleApi
  required: true
operations:
- id: pdf
  name: Generate PDF
  description: Generate a PDF from a webpage
  params:
  - id: link
    name: Webpage URL
    type: string
    default: ''
    required: true
    description: Link to webpage to convert
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - expandURL
          resource:
          - utility
    typeInfo: &id002
      type: string
      displayName: URL
      name: link
  - id: download
    name: Download PDF?
    type: boolean
    default: false
    required: true
    description: Whether to download the PDF or return a link to it
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - screenshot
          resource:
          - website
    typeInfo: &id004
      type: boolean
      displayName: Download Screenshot?
      name: download
  - id: output
    name: Put Output In Field
    type: string
    default: data
    required: true
    description: The name of the output field to put the binary file data in
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - screenshot
          resource:
          - website
          download:
          - true
    typeInfo: &id006
      type: string
      displayName: Put Output In Field
      name: output
- id: seo
  name: Get SEO Data
  description: Get SEO information from website
  params:
  - id: link
    name: Webpage URL
    type: string
    default: ''
    required: true
    description: Webpage to get SEO information for
    validation: *id001
    typeInfo: *id002
- id: screenshot
  name: Take Screenshot
  description: Create a screenshot from a webpage
  params:
  - id: link
    name: Webpage URL
    type: string
    default: ''
    required: true
    description: Link to webpage to convert
    validation: *id001
    typeInfo: *id002
  - id: download
    name: Download Screenshot?
    type: boolean
    default: false
    required: true
    description: Whether to download the screenshot or return a link to it
    validation: *id003
    typeInfo: *id004
  - id: output
    name: Put Output In Field
    type: string
    default: data
    required: true
    description: The name of the output field to put the binary file data in
    validation: *id005
    typeInfo: *id006
- id: instagramProfile
  name: Instagram
  description: Get details about an Instagram profile
  params:
  - id: profileName
    name: Profile Name
    type: string
    default: ''
    required: true
    description: Profile name to get details of
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - instagramProfile
          resource:
          - socialProfile
    typeInfo:
      type: string
      displayName: Profile Name
      name: profileName
- id: spotifyArtistProfile
  name: Spotify
  description: Get details about a Spotify Artist
  params:
  - id: artistName
    name: Artist Name
    type: string
    default: ''
    required: true
    description: Artist name to get details for
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - spotifyArtistProfile
          resource:
          - socialProfile
    typeInfo:
      type: string
      displayName: Artist Name
      name: artistName
- id: exchangeRate
  name: Exchange Rate
  description: Convert a value between currencies
  params:
  - id: value
    name: Value
    type: string
    default: ''
    required: true
    description: Value to convert
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - exchangeRate
          resource:
          - information
    typeInfo:
      type: string
      displayName: Value
      name: value
  - id: fromCurrency
    name: From Currency
    type: string
    default: ''
    required: true
    description: ''
    placeholder: USD
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - exchangeRate
          resource:
          - information
    typeInfo:
      type: string
      displayName: From Currency
      name: fromCurrency
  - id: toCurrency
    name: To Currency
    type: string
    default: ''
    required: true
    description: ''
    placeholder: EUR
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - exchangeRate
          resource:
          - information
    typeInfo:
      type: string
      displayName: To Currency
      name: toCurrency
- id: imageMetadata
  name: Image Metadata
  description: Retrieve image metadata from a URL
  params:
  - id: link
    name: Link To Image
    type: string
    default: ''
    required: true
    description: Image to get metadata from
    validation: *id001
    typeInfo: *id002
- id: expandURL
  name: Expand URL
  description: Expand a shortened URL
  params:
  - id: link
    name: URL
    type: string
    default: ''
    required: true
    description: URL to unshorten
    validation: *id001
    typeInfo: *id002
- id: qrCode
  name: Generate QR Code
  description: Generate a QR Code
  params:
  - id: message
    name: QR Content
    type: string
    default: ''
    required: true
    description: The text that should be turned into a QR code - like a website URL
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - qrCode
          resource:
          - utility
    typeInfo:
      type: string
      displayName: QR Content
      name: message
  - id: download
    name: Download Image?
    type: boolean
    default: false
    required: true
    description: Whether to download the QR code or return a link to it
    validation: *id003
    typeInfo: *id004
  - id: output
    name: Put Output In Field
    type: string
    default: data
    required: true
    description: The name of the output field to put the binary file data in
    validation: *id005
    typeInfo: *id006
- id: validateEmail
  name: Validate Email
  description: Validate an email address
  params:
  - id: emailAddress
    name: Email Address
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - validateEmail
          resource:
          - utility
    typeInfo:
      type: string
      displayName: Email Address
      name: emailAddress
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
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: fromCurrency
    text: USD
  - field: toCurrency
    text: EUR
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
  "$id": "https://n8n.io/schemas/nodes/oneSimpleApi.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "One Simple API Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "pdf",
        "seo",
        "screenshot",
        "instagramProfile",
        "spotifyArtistProfile",
        "exchangeRate",
        "imageMetadata",
        "expandURL",
        "qrCode",
        "validateEmail"
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
            "information",
            "socialProfile",
            "utility",
            "website"
          ],
          "default": "website"
        },
        "operation": {
          "description": "Expand a shortened URL",
          "type": "string",
          "enum": [
            "expandURL",
            "qrCode",
            "validateEmail"
          ],
          "default": "validateEmail"
        },
        "link": {
          "description": "URL to unshorten",
          "type": "string",
          "default": ""
        },
        "download": {
          "description": "Whether to download the screenshot or return a link to it",
          "type": "boolean",
          "default": false
        },
        "output": {
          "description": "The name of the output field to put the binary file data in",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "message": {
          "description": "The text that should be turned into a QR code - like a website URL",
          "type": "string",
          "default": ""
        },
        "profileName": {
          "description": "Profile name to get details of",
          "type": "string",
          "default": ""
        },
        "artistName": {
          "description": "Artist name to get details for",
          "type": "string",
          "default": ""
        },
        "value": {
          "description": "Value to convert",
          "type": "string",
          "default": ""
        },
        "fromCurrency": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "USD"
          ]
        },
        "toCurrency": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "EUR"
          ]
        },
        "emailAddress": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "email"
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
      "name": "oneSimpleApi",
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
