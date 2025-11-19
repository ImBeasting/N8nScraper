---
title: "Node: WhatsApp Business Cloud"
slug: "node-whatsapp"
version: "['1', '1.1']"
updated: "2025-11-13"
summary: "Access WhatsApp API"
node_type: "regular"
group: "['output']"
---

# Node: WhatsApp Business Cloud

**Purpose.** Access WhatsApp API
**Subtitle.** ={{ $parameter["resource"] + ": " + $parameter["operation"] }}


---

## Node Details

- **Icon:** `file:whatsapp.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## API Patterns

**HTTP Methods:** POST

**Common Endpoints:**
- `https://graph.facebook.com/v19.0/oauth/access_token`
- `https://graph.facebook.com/v19.0{resource}`
- `{phoneNumberId}/messages`

**Headers Used:** content-type

---

## Operations

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send message |
| Send and Wait for Response | `` | Send message and wait for response |
| Send Template | `sendTemplate` | Send template |

### Media Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Upload | `mediaUpload` | Upload media |
| Download | `mediaUrlGet` | Download media |
| Delete | `mediaDelete` | Delete media |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✗ | Resource to operate on |  |

**Resource options:**

* **Message** (`message`)
* **Media** (`media`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | sendTemplate | ✗ | Operation to perform |  |

**Operation options:**

* **Send** (`send`) - Send message
* **Send and Wait for Response** (``) - Send message and wait for response
* **Send Template** (`sendTemplate`) - Send template

---

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| MessageType | `messageType` | options | text | ✗ | The type of the message |  |

**MessageType options:**

* **Audio** (`audio`)
* **Contacts** (`contacts`)
* **Document** (`document`)
* **Image** (`image`)
* **Location** (`location`)
* **Text** (`text`)
* **Video** (`video`)

| Name | `name` | fixedCollection | {} | ✓ | e.g. Add Parameter |  |

<details>
<summary><strong>Name sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `data` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | If omitted, the message will display an Invite to WhatsApp button instead of the standard buttons | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Addresses | `addresses` | fixedCollection | {} |  |
| Birthday | `birthday` | string |  |  |
| Emails | `emails` | fixedCollection | {} |  |
| Organization | `organization` | fixedCollection | {} |  |
| Phones | `phones` | fixedCollection | {} | If omitted, the message will display an Invite to WhatsApp button instead of the standard buttons |
| URLs | `urls` | fixedCollection | {} |  |

</details>

| Longitude | `longitude` | number |  | ✓ |  | min:∞, max:180 |
| Latitude | `latitude` | number |  | ✓ |  | min:∞, max:90 |
| Additional Fields | `additionalFields` | fixedCollection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name and Address | `nameAndAddress` |  |  |  |

</details>

| Text Body | `textBody` | string |  | ✓ | The body of the message (max 4096 characters) |  |
| Take Audio From | `mediaPath` | options | useMediaLink | ✗ | Use a link, an ID, or n8n to upload an audio file |  |

**Take Audio From options:**

* **Link** (`useMediaLink`) - WhatsApp will download the audio, saving you the step of uploading audio yourself
* **WhatsApp Media** (`useMediaId`) - If you have already uploaded the audio to WhatsApp
* **n8n** (`useMedian8n`) - Use binary data passed into this node

| Take Document From | `mediaPath` | options | useMediaLink | ✗ | Use a link, an ID, or n8n to upload a document |  |

**Take Document From options:**

* **Link** (`useMediaLink`) - When using a link, WhatsApp will download the document, saving you the step of uploading document yourself
* **WhatsApp Media** (`useMediaId`) - You can use an ID if you have already uploaded the document to WhatsApp
* **n8n** (`useMedian8n`) - Upload a binary file on the item being processed in n8n

| Take Image From | `mediaPath` | options | useMediaLink | ✗ | Use a link, an ID, or n8n to upload an image |  |

**Take Image From options:**

* **Link** (`useMediaLink`) - When using a link, WhatsApp will download the image, saving you the step of uploading image yourself
* **WhatsApp Media** (`useMediaId`) - You can use an ID if you have already uploaded the image to WhatsApp
* **n8n** (`useMedian8n`) - Upload a binary file on the item being processed in n8n

| Take Video From | `mediaPath` | options | useMediaLink | ✗ | Use a link, an ID, or n8n to upload a video |  |

**Take Video From options:**

* **Link** (`useMediaLink`) - When using a link, WhatsApp will download the video, saving you the step of uploading video yourself
* **WhatsApp Media** (`useMediaId`) - You can use an ID if you have already uploaded the video to WhatsApp
* **n8n** (`useMedian8n`) - Upload a binary file on the item being processed in n8n

| Link | `mediaLink` | string |  | ✗ | Link of the media to be sent |  |
| ID | `mediaId` | string |  | ✗ | ID of the media to be sent |  |
| Input Data Field Name | `mediaPropertyName` | string | data | ✓ | The name of the input field containing the binary file data to be uploaded |  |
| Filename | `mediaFilename` | string |  | ✓ | The name of the file (required when using a file ID) |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The name of the file | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filename | `mediaFilename` | string |  | The name of the file |
| Caption | `mediaCaption` | string |  | The caption of the media |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to display URL previews in text messages | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Show URL Previews | `previewUrl` | boolean | False | Whether to display URL previews in text messages |

</details>


### Send Template parameters (`sendTemplate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Template | `template` | options |  | ✓ | Name of the template |  |
| Language Code | `templateLanguageCode` | string | en_US | ✗ |  |  |
| Components | `components` | fixedCollection | {} | ✗ | Allows your customer to call a phone number and visit a website | e.g. Add Component |  |

<details>
<summary><strong>Components sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Component | `component` |  |  |  |

</details>


### Upload parameters (`mediaUpload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Sender Phone Number (or ID) | `phoneNumberId` | options |  | ✓ | The ID of the business account's phone number to store the media |  |
| Property Name | `mediaPropertyName` | string | data | ✓ | Name of the binary property which contains the data for the file to be uploaded |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The name to use for the file | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filename | `mediaFileName` | string |  | The name to use for the file |

</details>


### Download parameters (`mediaUrlGet`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Media ID | `mediaGetId` | string |  | ✓ | The ID of the media |  |

### Delete parameters (`mediaDelete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Media ID | `mediaDeleteId` | string |  | ✓ | The ID of the media |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter["resource"] + ": " + $parameter["operation"] }}`

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
* Categories: Communication, HITL

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: whatsApp
displayName: WhatsApp Business Cloud
description: Access WhatsApp API
version:
- '1'
- '1.1'
nodeType: regular
group:
- output
operations:
- id: send
  name: Send
  description: ''
  params:
  - id: messageType
    name: MessageType
    type: options
    default: text
    required: false
    description: The type of the message
    validation:
      displayOptions:
        show:
          resource:
          - message
          operation:
          - send
    typeInfo:
      type: options
      displayName: MessageType
      name: messageType
      possibleValues:
      - value: audio
        name: Audio
        description: ''
      - value: contacts
        name: Contacts
        description: ''
      - value: document
        name: Document
        description: ''
      - value: image
        name: Image
        description: ''
      - value: location
        name: Location
        description: ''
      - value: text
        name: Text
        description: ''
      - value: video
        name: Video
        description: ''
  - id: name
    name: Name
    type: fixedCollection
    default: {}
    required: true
    description: ''
    placeholder: Add Parameter
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - send
          messageType:
          - contacts
    typeInfo:
      type: fixedCollection
      displayName: Name
      name: name
      typeOptions:
        multipleValues: false
      subProperties:
      - name: data
        displayName: Name
        values:
        - displayName: Formatted Name
          name: formatted_name
          type: string
          default: ''
          required: true
          routing: "\n\t\t\t\t\t\t\tsend: {\n\t\t\t\t\t\t\t\ttype: 'body',\n\t\t\t\
            \t\t\t\t\tproperty: 'contacts[0].name.formatted_name',\n\t\t\t\t\t\t\t"
        - displayName: First Name
          name: first_name
          type: string
          default: ''
          routing: "\n\t\t\t\t\t\t\tsend: {\n\t\t\t\t\t\t\t\ttype: 'body',\n\t\t\t\
            \t\t\t\t\tproperty: 'contacts[0].name.first_name',\n\t\t\t\t\t\t\t"
        - displayName: Last Name
          name: last_name
          type: string
          default: ''
          routing: "\n\t\t\t\t\t\t\tsend: {\n\t\t\t\t\t\t\t\ttype: 'body',\n\t\t\t\
            \t\t\t\t\tproperty: 'contacts[0].name.last_name',\n\t\t\t\t\t\t\t"
        - displayName: Middle Name
          name: middle_name
          type: string
          default: ''
          routing: "\n\t\t\t\t\t\t\tsend: {\n\t\t\t\t\t\t\t\ttype: 'body',\n\t\t\t\
            \t\t\t\t\tproperty: 'contacts[0].name.middle_name',\n\t\t\t\t\t\t\t"
        - displayName: Suffix
          name: suffix
          type: string
          default: ''
          routing: "\n\t\t\t\t\t\t\tsend: {\n\t\t\t\t\t\t\t\ttype: 'body',\n\t\t\t\
            \t\t\t\t\tproperty: 'contacts[0].name.suffix',\n\t\t\t\t\t\t\t"
        - displayName: Prefix
          name: prefix
          type: string
          default: ''
          routing: "\n\t\t\t\t\t\t\tsend: {\n\t\t\t\t\t\t\t\ttype: 'body',\n\t\t\t\
            \t\t\t\t\tproperty: 'contacts[0].name.prefix',\n\t\t\t\t\t\t\t"
  - id: longitude
    name: Longitude
    type: number
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - send
          messageType:
          - location
    typeInfo:
      type: number
      displayName: Longitude
      name: longitude
      typeOptions:
        maxValue: 180
  - id: latitude
    name: Latitude
    type: number
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - send
          messageType:
          - location
    typeInfo:
      type: number
      displayName: Latitude
      name: latitude
      typeOptions:
        maxValue: 90
  - id: additionalFields
    name: Additional Fields
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Field
    validation:
      displayOptions:
        show:
          resource:
          - media
          operation:
          - mediaUpload
    typeInfo:
      type: collection
      displayName: Additional Fields
      name: additionalFields
      subProperties:
      - displayName: Filename
        name: mediaFileName
        type: string
        description: The name to use for the file
        default: ''
  - id: textBody
    name: Text Body
    type: string
    default: ''
    required: true
    description: The body of the message (max 4096 characters)
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - send
          messageType:
          - text
    typeInfo:
      type: string
      displayName: Text Body
      name: textBody
  - id: mediaPath
    name: Take Audio From
    type: options
    default: useMediaLink
    required: false
    description: Use a link, an ID, or n8n to upload an audio file
    validation: &id001
      displayOptions:
        show:
          operation:
          - send
          messageType:
          - video
    typeInfo: &id002
      type: options
      displayName: Take Video From
      name: mediaPath
      possibleValues:
      - value: useMediaLink
        name: Link
        description: When using a link, WhatsApp will download the video, saving you
          the step of uploading video yourself
      - value: useMediaId
        name: WhatsApp Media
        description: You can use an ID if you have already uploaded the video to WhatsApp
      - value: useMedian8n
        name: n8n
        description: Upload a binary file on the item being processed in n8n
  - id: mediaPath
    name: Take Document From
    type: options
    default: useMediaLink
    required: false
    description: Use a link, an ID, or n8n to upload a document
    validation: *id001
    typeInfo: *id002
  - id: mediaPath
    name: Take Image From
    type: options
    default: useMediaLink
    required: false
    description: Use a link, an ID, or n8n to upload an image
    validation: *id001
    typeInfo: *id002
  - id: mediaPath
    name: Take Video From
    type: options
    default: useMediaLink
    required: false
    description: Use a link, an ID, or n8n to upload a video
    validation: *id001
    typeInfo: *id002
  - id: mediaLink
    name: Link
    type: string
    default: ''
    required: false
    description: Link of the media to be sent
    validation:
      displayOptions:
        show:
          operation:
          - send
          mediaPath:
          - useMediaLink
    typeInfo:
      type: string
      displayName: Link
      name: mediaLink
  - id: mediaId
    name: ID
    type: string
    default: ''
    required: false
    description: ID of the media to be sent
    validation:
      displayOptions:
        show:
          operation:
          - send
          mediaPath:
          - useMediaId
    typeInfo:
      type: string
      displayName: ID
      name: mediaId
  - id: mediaPropertyName
    name: Input Data Field Name
    type: string
    default: data
    required: true
    description: The name of the input field containing the binary file data to be
      uploaded
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - mediaUpload
          resource:
          - media
    typeInfo: &id004
      type: string
      displayName: Property Name
      name: mediaPropertyName
  - id: mediaFilename
    name: Filename
    type: string
    default: ''
    required: true
    description: The name of the file (required when using a file ID)
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - send
          messageType:
          - document
          mediaPath:
          - useMediaId
    typeInfo:
      type: string
      displayName: Filename
      name: mediaFilename
- id: ''
  name: Send and Wait for Response
  description: ''
- id: sendTemplate
  name: Send Template
  description: ''
  params:
  - id: template
    name: Template
    type: options
    default: ''
    required: true
    description: Name of the template
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - sendTemplate
          resource:
          - message
    typeInfo:
      type: options
      displayName: Template
      name: template
      possibleValues: []
  - id: templateLanguageCode
    name: Language Code
    type: string
    default: en_US
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - sendTemplate
          resource:
          - message
    typeInfo:
      type: string
      displayName: Language Code
      name: templateLanguageCode
  - id: components
    name: Components
    type: fixedCollection
    default: {}
    required: false
    description: Allows your customer to call a phone number and visit a website
    placeholder: Add Component
    validation:
      displayOptions:
        show:
          operation:
          - sendTemplate
          resource:
          - message
    typeInfo:
      type: fixedCollection
      displayName: Components
      name: components
      typeOptions:
        multipleValues: true
      subProperties:
      - name: component
        displayName: Component
        values:
        - displayName: Type
          name: type
          type: options
          value: body
          default: body
          options:
          - name: Body
            value: body
            displayName: Body
          - name: Button
            value: button
            displayName: Button
          - name: Header
            value: header
            displayName: Header
        - displayName: Parameters
          name: bodyParameters
          type: fixedCollection
          placeholder: Add Parameter
          value: text
          default: {}
          options:
          - name: parameter
            displayName: Parameter
            values:
            - displayName: Type
              name: type
              type: options
              value: text
              default: text
              options:
              - name: Text
                value: text
                displayName: Text
              - name: Currency
                value: currency
                displayName: Currency
              - name: Date Time
                value: date_time
                displayName: Date Time
            - displayName: Text
              name: text
              type: string
              default: ''
              displayOptions:
                show:
                  type:
                  - text
            - displayName: Currency Code
              name: code
              type: options
              placeholder: USD
              default: ''
              displayOptions:
                show:
                  type:
                  - currency
            - displayName: Amount
              name: amount_1000
              type: number
              default: ''
              displayOptions:
                show:
                  type:
                  - currency
            - displayName: Date Time
              name: date_time
              type: dateTime
              default: ''
              displayOptions:
                show:
                  type:
                  - date_time
            - displayName: Fallback Value
              name: fallback_value
              type: string
              default: ''
              displayOptions:
                show:
                  type:
                  - currency
          typeOptions:
            multipleValues: true
          displayOptions:
            show:
              type:
              - body
        - displayName: Sub Type
          name: sub_type
          type: options
          description: Allows your customer to call a phone number and visit a website
          value: quick_reply
          default: quick_reply
          options:
          - name: Quick Reply
            description: Allows your customer to call a phone number and visit a website
            value: quick_reply
            displayName: Quick Reply
          - name: URL
            value: url
            displayName: Url
          displayOptions:
            show:
              type:
              - button
        - displayName: Index
          name: index
          type: number
          default: 0
          typeOptions:
            minValue: 0
            maxValue: 2
          displayOptions:
            show:
              type:
              - button
        - displayName: Parameters
          name: buttonParameters
          type: fixedCollection
          placeholder: Add Parameter
          value: payload
          default: {}
          options:
          - name: parameter
            displayName: Parameter
            values:
            - displayName: Type
              name: type
              type: options
              value: payload
              default: payload
              options:
              - name: Payload
                value: payload
                displayName: Payload
              - name: Text
                value: text
                displayName: Text
            - displayName: Payload
              name: payload
              type: string
              default: ''
              displayOptions:
                show:
                  type:
                  - payload
            - displayName: Text
              name: text
              type: string
              default: ''
              displayOptions:
                show:
                  type:
                  - text
          typeOptions:
            multipleValues: false
          displayOptions:
            show:
              type:
              - button
        - displayName: Parameters
          name: headerParameters
          type: fixedCollection
          placeholder: Add Parameter
          value: text
          default: {}
          options:
          - name: parameter
            displayName: Parameter
            values:
            - displayName: Type
              name: type
              type: options
              value: text
              default: text
              options:
              - name: Text
                value: text
                displayName: Text
              - name: Currency
                value: currency
                displayName: Currency
              - name: Date Time
                value: date_time
                displayName: Date Time
              - name: Image
                value: image
                displayName: Image
            - displayName: Text
              name: text
              type: string
              default: ''
              displayOptions:
                show:
                  type:
                  - text
            - displayName: Currency Code
              name: code
              type: options
              placeholder: USD
              default: ''
              displayOptions:
                show:
                  type:
                  - currency
            - displayName: Amount
              name: amount_1000
              type: number
              default: ''
              displayOptions:
                show:
                  type:
                  - currency
            - displayName: Date Time
              name: date_time
              type: dateTime
              default: ''
              displayOptions:
                show:
                  type:
                  - date_time
            - displayName: Image Link
              name: imageLink
              type: string
              default: ''
              displayOptions:
                show:
                  type:
                  - image
          typeOptions:
            multipleValues: true
          displayOptions:
            show:
              type:
              - header
- id: mediaUpload
  name: Upload
  description: ''
  params:
  - id: phoneNumberId
    name: Sender Phone Number (or ID)
    type: options
    default: ''
    required: true
    description: The ID of the business account's phone number to store the media
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - mediaUpload
          resource:
          - media
    typeInfo:
      type: options
      displayName: Sender Phone Number (or ID)
      name: phoneNumberId
      possibleValues: []
  - id: mediaPropertyName
    name: Property Name
    type: string
    default: data
    required: true
    description: Name of the binary property which contains the data for the file
      to be uploaded
    validation: *id003
    typeInfo: *id004
- id: mediaUrlGet
  name: Download
  description: ''
  params:
  - id: mediaGetId
    name: Media ID
    type: string
    default: ''
    required: true
    description: The ID of the media
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - mediaUrlGet
          resource:
          - media
    typeInfo:
      type: string
      displayName: Media ID
      name: mediaGetId
- id: mediaDelete
  name: Delete
  description: ''
  params:
  - id: mediaDeleteId
    name: Media ID
    type: string
    default: ''
    required: true
    description: The ID of the media
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - mediaDelete
          resource:
          - media
    typeInfo:
      type: string
      displayName: Media ID
      name: mediaDeleteId
common_expressions:
- '={{ $parameter["resource"] + ": " + $parameter["operation"] }}'
api_patterns:
  http_methods:
  - POST
  endpoints:
  - https://graph.facebook.com/v19.0/oauth/access_token
  - https://graph.facebook.com/v19.0{resource}
  - '{phoneNumberId}/messages'
  headers:
  - content-type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: name
    text: Add Parameter
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: components
    text: Add Component
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  hints:
  - field: recipientPhoneNumber
    text: When entering a phone number, make sure to include the country code
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
  "$id": "https://n8n.io/schemas/nodes/whatsApp.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "WhatsApp Business Cloud Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "send",
        "",
        "sendTemplate",
        "mediaUpload",
        "mediaUrlGet",
        "mediaDelete"
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
            "message",
            "media"
          ],
          "default": "message"
        },
        "operation": {
          "description": "The operation to perform on the media",
          "type": "string",
          "enum": [
            "mediaUpload",
            "mediaUrlGet",
            "mediaDelete"
          ],
          "default": "mediaUpload"
        },
        "messagingProduct": {
          "description": "",
          "type": "string",
          "default": "whatsapp"
        },
        "phoneNumberId": {
          "description": "The ID of the business account's phone number to store the media",
          "type": "string",
          "default": ""
        },
        "recipientPhoneNumber": {
          "description": "Phone number of the recipient of the message",
          "type": "string",
          "default": ""
        },
        "messageType": {
          "description": "The type of the message",
          "type": "string",
          "enum": [
            "audio",
            "contacts",
            "document",
            "image",
            "location",
            "text",
            "video"
          ],
          "default": "text"
        },
        "name": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Parameter"
          ]
        },
        "additionalFields": {
          "description": "The name to use for the file",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "longitude": {
          "description": "",
          "type": "number",
          "default": ""
        },
        "latitude": {
          "description": "",
          "type": "number",
          "default": ""
        },
        "textBody": {
          "description": "The body of the message (max 4096 characters)",
          "type": "string",
          "default": ""
        },
        "mediaPath": {
          "description": "Use a link, an ID, or n8n to upload a video",
          "type": "string",
          "enum": [
            "useMediaLink",
            "useMediaId",
            "useMedian8n"
          ],
          "default": "useMediaLink"
        },
        "mediaLink": {
          "description": "Link of the media to be sent",
          "type": "string",
          "default": ""
        },
        "mediaId": {
          "description": "ID of the media to be sent",
          "type": "string",
          "default": ""
        },
        "mediaPropertyName": {
          "description": "Name of the binary property which contains the data for the file to be uploaded",
          "type": "string",
          "default": "data"
        },
        "mediaFilename": {
          "description": "The name of the file (required when using a file ID)",
          "type": "string",
          "default": ""
        },
        "template": {
          "description": "Name of the template",
          "type": "string",
          "default": ""
        },
        "templateLanguageCode": {
          "description": "",
          "type": "string",
          "default": "en_US"
        },
        "components": {
          "description": "Allows your customer to call a phone number and visit a website",
          "type": "string",
          "default": {},
          "examples": [
            "Add Component"
          ]
        },
        "mediaGetId": {
          "description": "The ID of the media",
          "type": "string",
          "default": ""
        },
        "mediaDeleteId": {
          "description": "The ID of the media",
          "type": "string",
          "default": ""
        },
        "default": {
          "description": "",
          "type": "string"
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
