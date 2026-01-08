---
title: "Node: Google Drive"
slug: "node-googledrive"
version: "['1', '2']"
updated: "2026-01-08"
summary: "Access data on Google Drive"
node_type: "regular"
group: "['input']"
---

# Node: Google Drive

**Purpose.** Access data on Google Drive
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:googleDrive.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleApi**: N/A
- **googleDriveOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleApi` | ✓ | {'show': {'authentication': ['serviceAccount']}} |
| `googleDriveOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Copy | `copy` | Copy a file |
| Delete | `delete` | Delete a file |
| Download | `download` | Download a file |
| List | `list` | List files and folders |
| Share | `share` | Share a file |
| Update | `update` | Update a file |
| Upload | `upload` | Upload a file |

### Folder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a folder |
| Delete | `delete` | Delete a folder |
| Share | `share` | Share a folder |

### Drive Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a drive |
| Delete | `delete` | Delete a drive |
| Get | `get` | Get a drive |
| List | `list` | List all drives |
| Update | `update` | Update a drive |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | file | ✗ | Resource to operate on |  |

**Resource options:**

* **Drive** (`drive`)
* **File** (`file`)
* **Folder** (`folder`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | upload | ✗ | Copy a file |  |

**Operation options:**

* **Copy** (`copy`) - Copy a file
* **Delete** (`delete`) - Delete a file
* **Download** (`download`) - Download a file
* **List** (`list`) - List files and folders
* **Share** (`share`) - Share a file
* **Update** (`update`) - Update a file
* **Upload** (`upload`) - Upload a file

---

### Copy parameters (`copy`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File | `fileId` | resourceLocator |  | ✓ | The ID of the file | e.g. Select a file... |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File | `fileId` | resourceLocator |  | ✓ | The ID of the file | e.g. Select a file... |  |
| Folder | `fileId` | resourceLocator |  | ✓ | The ID of the folder | e.g. Select a folder... |  |
| Drive | `driveId` | resourceLocator |  | ✓ | The ID of the drive | e.g. Drive |  |

### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File | `fileId` | resourceLocator |  | ✓ | The ID of the file | e.g. Select a file... |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| Options | `options` | collection | {} | ✗ | Format used to export when downloading Google Docs files | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Google File Conversion | `googleFileConversion` | fixedCollection | {} | Format used to export when downloading Google Docs files |
| File Name | `fileName` | string |  | File name. Ex: data.pdf. |

</details>


### List parameters (`list`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Use Query String | `useQueryString` | boolean | False | ✗ | Whether a query string should be used to filter results |  |
| Query String | `queryString` | string |  | ✗ | Query to use to return only specific files | e.g. name contains 'invoice' |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `queryFilters` | fixedCollection | {} | ✗ | Filters to use to return only specific files | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` |  |  |  |
| Mime Type | `mimeType` |  |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Options | `options` | collection | {} | ✗ | Query string for searching shared drives. See the <a href="https://developers.google.com/drive/api/v3/search-shareddrives">"Search for shared drives"</a> guide for supported syntax. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `q` | string |  | Query string for searching shared drives. See the <a href="https://developers.google.com/drive/api/v3/search-shareddrives">"Search for shared drives"</a> guide for supported syntax. |
| Use Domain Admin Access | `useDomainAdminAccess` | boolean | False | Whether to issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the shared drive belongs. (Default: false). |

</details>


### Share parameters (`share`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File | `fileId` | resourceLocator |  | ✓ | The ID of the file | e.g. Select a file... |  |
| Folder | `fileId` | resourceLocator |  | ✓ | The ID of the folder | e.g. Select a folder... |  |
| Permissions | `permissionsUi` | fixedCollection | {} | ✗ | Information about the different types can be found <a href="https://developers.google.com/drive/api/v3/ref-roles">here</a> | e.g. Add Permission |  |

<details>
<summary><strong>Permissions sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Permission | `permissionsValues` |  |  |  |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File | `fileId` | resourceLocator |  | ✓ | The ID of the file | e.g. Select a file... |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The name of the file | e.g. Add option |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Name | `fileName` | string |  | The name of the file |
| Keep Revision Forever | `keepRevisionForever` | boolean | False | Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions. |
| Move to Trash | `trashed` | boolean | False | Whether to move a file to the trash. Only the owner may trash a file. |
| OCR Language | `ocrLanguage` | string |  | A language hint for OCR processing during image import (ISO 639-1 code) |
| Parent ID | `parentId` | string |  | The ID of the parent to set |
| Use Content As Indexable Text | `useContentAsIndexableText` | boolean | False | Whether to use the uploaded content as indexable text |

</details>

| Options | `options` | collection | {} | ✗ | All fields | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | multiOptions | [] | All fields |

</details>

| Drive | `driveId` | resourceLocator |  | ✓ | The ID of the drive | e.g. Drive |  |
| Update Fields | `options` | collection | {} | ✗ | The color of this shared drive as an RGB hex string | e.g. Add option |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Color RGB | `colorRgb` | color |  | The color of this shared drive as an RGB hex string |
| Name | `name` | string |  | The name of this shared drive |
| Restrictions | `restrictions` | collection | {} | Whether the options to copy, print, or download files inside this shared drive, should be disabled for readers and commenters. When this restriction is set to true, it will override the similarly named field to true for any file inside this shared drive. |

</details>


### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Binary File | `binaryData` | boolean | False | ✗ | Whether the data to upload should be taken from binary field |  |
| File Content | `fileContent` | string |  | ✗ | The text content of the file to upload |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |
| File Name | `name` | string |  | ✓ | The name the file should be saved as | e.g. invoice_1.pdf |  |
| Resolve Data | `resolveData` | boolean | False | ✗ | By default the response only contain the ID of the file. If this option gets activated, it will resolve the data automatically. |  |
| Parents | `parents` | string | [] | ✗ | The IDs of the parent folders which contain the file |  |
| Options | `options` | collection | {} | ✗ | A collection of arbitrary key-value pairs which are private to the requesting app | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| APP Properties | `appPropertiesUi` | fixedCollection | {} | A collection of arbitrary key-value pairs which are private to the requesting app |
| Properties | `propertiesUi` | fixedCollection | {} | A collection of arbitrary key-value pairs which are visible to all apps |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Folder | `name` | string |  | ✓ | The name of folder to create | e.g. invoices |  |
| Name | `name` | string |  | ✗ | The name of this shared drive |  |
| Options | `options` | collection | {} | ✗ | Whether the current user can add children to folders in this shared drive | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Capabilities | `capabilities` | collection | {} | Whether the current user can add children to folders in this shared drive |
| Color RGB | `colorRgb` | color |  | The color of this shared drive as an RGB hex string |
| Created Time | `createdTime` | dateTime |  | The time at which the shared drive was created (RFC 3339 date-time) |
| Hidden | `hidden` | boolean | False | Whether the shared drive is hidden from default view |
| Restrictions | `restrictions` | collection | {} | Whether the options to copy, print, or download files inside this shared drive, should be disabled for readers and commenters. When this restriction is set to true, it will override the similarly named field to true for any file inside this shared drive. |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Drive | `driveId` | resourceLocator |  | ✓ | The ID of the drive | e.g. Drive |  |
| Options | `options` | collection | {} | ✗ | Whether to issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the shared drive belongs. (Default: false). | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Use Domain Admin Access | `useDomainAdminAccess` | boolean | False | Whether to issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the shared drive belongs. (Default: false). |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ": " + $parameter["resource"]}}`

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
node: googleDrive
displayName: Google Drive
description: Access data on Google Drive
version:
- '1'
- '2'
nodeType: regular
group:
- input
credentials:
- name: googleApi
  required: true
- name: googleDriveOAuth2Api
  required: true
operations:
- id: copy
  name: Copy
  description: Copy a file
  params:
  - id: fileId
    name: File
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the file
    placeholder: Select a file...
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - delete
          - share
          resource:
          - folder
    typeInfo: &id002
      type: resourceLocator
      displayName: Folder
      name: fileId
- id: delete
  name: Delete
  description: Delete a file
  params:
  - id: fileId
    name: File
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the file
    placeholder: Select a file...
    validation: *id001
    typeInfo: *id002
  - id: fileId
    name: Folder
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the folder
    placeholder: Select a folder...
    validation: *id001
    typeInfo: *id002
  - id: driveId
    name: Drive
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the drive
    hint: The Google Drive drive to operate on
    placeholder: Drive
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - delete
          - get
          - update
          resource:
          - drive
    typeInfo: &id006
      type: resourceLocator
      displayName: Drive
      name: driveId
- id: download
  name: Download
  description: Download a file
  params:
  - id: fileId
    name: File
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the file
    placeholder: Select a file...
    validation: *id001
    typeInfo: *id002
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
          binaryData:
          - true
    typeInfo: &id008
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
- id: list
  name: List
  description: List files and folders
  params:
  - id: useQueryString
    name: Use Query String
    type: boolean
    default: false
    required: false
    description: Whether a query string should be used to filter results
    validation:
      displayOptions:
        show:
          operation:
          - list
          resource:
          - file
    typeInfo:
      type: boolean
      displayName: Use Query String
      name: useQueryString
  - id: queryString
    name: Query String
    type: string
    default: ''
    required: false
    description: Query to use to return only specific files
    placeholder: name contains 'invoice'
    validation:
      displayOptions:
        show:
          operation:
          - list
          useQueryString:
          - true
          resource:
          - file
    typeInfo:
      type: string
      displayName: Query String
      name: queryString
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id003
      displayOptions:
        show:
          operation:
          - list
          resource:
          - drive
          returnAll:
          - false
    typeInfo: &id004
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 200
  - id: queryFilters
    name: Filters
    type: fixedCollection
    default: {}
    required: false
    description: Filters to use to return only specific files
    placeholder: Add Filter
    validation:
      displayOptions:
        show:
          operation:
          - list
          useQueryString:
          - false
          resource:
          - file
    typeInfo:
      type: fixedCollection
      displayName: Filters
      name: queryFilters
      typeOptions:
        multipleValues: true
      subProperties:
      - name: name
        displayName: Name
        values:
        - displayName: Operation
          name: operation
          type: options
          value: contains
          default: contains
          noDataExpression: true
          options:
          - name: Contains
            value: contains
            displayName: Contains
          - name: Is
            value: is
            displayName: Is
          - name: Is Not
            value: isNot
            displayName: Is Not
        - displayName: Value
          name: value
          type: string
          description: The value for operation
          default: ''
      - name: mimeType
        displayName: Mime Type
        values:
        - displayName: Mime Type
          name: mimeType
          type: options
          description: The Mime-Type of the files to return
          value: application/vnd.google-apps.drive-sdk
          default: application/vnd.google-apps.file
          options:
          - name: 3rd Party Shortcut
            value: application/vnd.google-apps.drive-sdk
            displayName: 3rd Party Shortcut
          - name: Audio
            value: application/vnd.google-apps.audio
            displayName: Audio
          - name: Custom Mime Type
            value: custom
            displayName: Custom Mime Type
          - name: Google Apps Scripts
            value: application/vnd.google-apps.script
            displayName: Google Apps Scripts
          - name: Google Docs
            value: application/vnd.google-apps.document
            displayName: Google Docs
          - name: Google Drawing
            value: application/vnd.google-apps.drawing
            displayName: Google Drawing
          - name: Google Drive File
            value: application/vnd.google-apps.file
            displayName: Google Drive File
          - name: Google Drive Folder
            value: application/vnd.google-apps.folder
            displayName: Google Drive Folder
          - name: Google Forms
            value: application/vnd.google-apps.form
            displayName: Google Forms
          - name: Google Fusion Tables
            value: application/vnd.google-apps.fusiontable
            displayName: Google Fusion Tables
          - name: Google My Maps
            value: application/vnd.google-apps.map
            displayName: Google My Maps
          - name: Google Sheets
            value: application/vnd.google-apps.spreadsheet
            displayName: Google Sheets
          - name: Google Sites
            value: application/vnd.google-apps.site
            displayName: Google Sites
          - name: Google Slides
            value: application/vnd.google-apps.presentation
            displayName: Google Slides
          - name: Photo
            value: application/vnd.google-apps.photo
            displayName: Photo
          - name: Unknown
            value: application/vnd.google-apps.unknown
            displayName: Unknown
          - name: Video
            value: application/vnd.google-apps.video
            displayName: Video
        - displayName: Custom Mime Type
          name: customMimeType
          type: string
          default: ''
          displayOptions:
            show:
              mimeType:
              - custom
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          operation:
          - list
          resource:
          - drive
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
- id: share
  name: Share
  description: Share a file
  params:
  - id: fileId
    name: File
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the file
    placeholder: Select a file...
    validation: *id001
    typeInfo: *id002
  - id: fileId
    name: Folder
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the folder
    placeholder: Select a folder...
    validation: *id001
    typeInfo: *id002
  - id: permissionsUi
    name: Permissions
    type: fixedCollection
    default: {}
    required: false
    description: Information about the different types can be found <a href="https://developers.google.com/drive/api/v3/ref-roles">here</a>
    placeholder: Add Permission
    validation:
      displayOptions:
        show:
          resource:
          - file
          - folder
          operation:
          - share
    typeInfo:
      type: fixedCollection
      displayName: Permissions
      name: permissionsUi
      typeOptions:
        multipleValues: false
      subProperties:
      - name: permissionsValues
        displayName: Permission
        values:
        - displayName: Role
          name: role
          type: options
          value: commenter
          default: ''
          options:
          - name: Commenter
            value: commenter
            displayName: Commenter
          - name: File Organizer
            value: fileOrganizer
            displayName: File Organizer
          - name: Organizer
            value: organizer
            displayName: Organizer
          - name: Owner
            value: owner
            displayName: Owner
          - name: Reader
            value: reader
            displayName: Reader
          - name: Writer
            value: writer
            displayName: Writer
        - displayName: Type
          name: type
          type: options
          description: Information about the different types can be found <a href="https://developers.google.com/drive/api/v3/ref-roles">here</a>
          value: user
          default: ''
          options:
          - name: User
            value: user
            displayName: User
          - name: Group
            value: group
            displayName: Group
          - name: Domain
            value: domain
            displayName: Domain
          - name: Anyone
            value: anyone
            displayName: Anyone
        - displayName: Email Address
          name: emailAddress
          type: string
          description: The email address of the user or group to which this permission
            refers
          default: ''
          displayOptions:
            show:
              type:
              - user
              - group
        - displayName: Domain
          name: domain
          type: string
          description: The domain to which this permission refers
          default: ''
          displayOptions:
            show:
              type:
              - domain
        - displayName: Allow File Discovery
          name: allowFileDiscovery
          type: boolean
          description: Whether the permission allows the file to be discovered through
            search
          default: false
          displayOptions:
            show:
              type:
              - domain
              - anyone
- id: update
  name: Update
  description: Update a file
  params:
  - id: fileId
    name: File
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the file
    placeholder: Select a file...
    validation: *id001
    typeInfo: *id002
  - id: driveId
    name: Drive
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the drive
    hint: The Google Drive drive to operate on
    placeholder: Drive
    validation: *id005
    typeInfo: *id006
- id: upload
  name: Upload
  description: Upload a file
  params:
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: false
    description: Whether the data to upload should be taken from binary field
    validation:
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
    typeInfo:
      type: boolean
      displayName: Binary File
      name: binaryData
  - id: fileContent
    name: File Content
    type: string
    default: ''
    required: false
    description: The text content of the file to upload
    validation:
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
          binaryData:
          - false
    typeInfo:
      type: string
      displayName: File Content
      name: fileContent
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be uploaded
    validation: *id007
    typeInfo: *id008
  - id: name
    name: File Name
    type: string
    default: ''
    required: true
    description: The name the file should be saved as
    placeholder: invoice_1.pdf
    validation: &id009
      displayOptions:
        show:
          operation:
          - create
          resource:
          - drive
    typeInfo: &id010
      type: string
      displayName: Name
      name: name
  - id: resolveData
    name: Resolve Data
    type: boolean
    default: false
    required: false
    description: By default the response only contain the ID of the file. If this
      option gets activated, it will resolve the data automatically.
    validation:
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
    typeInfo:
      type: boolean
      displayName: Resolve Data
      name: resolveData
  - id: parents
    name: Parents
    type: string
    default: []
    required: false
    description: The IDs of the parent folders which contain the file
    validation:
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
    typeInfo:
      type: string
      displayName: Parents
      name: parents
      typeOptions:
        multipleValues: true
- id: create
  name: Create
  description: Create a folder
  params:
  - id: name
    name: Folder
    type: string
    default: ''
    required: true
    description: The name of folder to create
    placeholder: invoices
    validation: *id009
    typeInfo: *id010
  - id: name
    name: Name
    type: string
    default: ''
    required: false
    description: The name of this shared drive
    validation: *id009
    typeInfo: *id010
- id: get
  name: Get
  description: Get a drive
  params:
  - id: driveId
    name: Drive
    type: resourceLocator
    default: ''
    required: true
    description: The ID of the drive
    hint: The Google Drive drive to operate on
    placeholder: Drive
    validation: *id005
    typeInfo: *id006
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: fileId
    text: Select a file...
  - field: fileId
    text: Select a folder...
  - field: options
    text: Add option
  - field: queryString
    text: name contains 'invoice'
  - field: queryFilters
    text: Add Filter
  - field: permissionsUi
    text: Add Permission
  - field: updateFields
    text: Add option
  - field: options
    text: Add option
  - field: name
    text: invoice_1.pdf
  - field: name
    text: invoices
  - field: options
    text: Add option
  - field: driveId
    text: Drive
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  hints:
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be uploaded
  - field: driveId
    text: The Google Drive drive to operate on
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
  "$id": "https://n8n.io/schemas/nodes/googleDrive.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Drive Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "copy",
        "delete",
        "download",
        "list",
        "share",
        "update",
        "upload",
        "create",
        "get"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "serviceAccount",
            "oAuth2"
          ],
          "default": "serviceAccount"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "drive",
            "file",
            "folder"
          ],
          "default": "file"
        },
        "operation": {
          "description": "Create a drive",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "list",
            "update"
          ],
          "default": "create"
        },
        "fileId": {
          "description": "The ID of the folder",
          "type": "string",
          "examples": [
            "Select a folder..."
          ]
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "A collection of arbitrary key-value pairs which are private to the requesting app",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "useQueryString": {
          "description": "Whether a query string should be used to filter results",
          "type": "boolean",
          "default": false
        },
        "queryString": {
          "description": "Query to use to return only specific files",
          "type": "string",
          "default": "",
          "examples": [
            "name contains 'invoice'"
          ]
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
        },
        "queryFilters": {
          "description": "Filters to use to return only specific files",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "permissionsUi": {
          "description": "Information about the different types can be found <a href=\"https://developers.google.com/drive/api/v3/ref-roles\">here</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Permission"
          ]
        },
        "binaryData": {
          "description": "Whether the data to upload should be taken from binary field",
          "type": "boolean",
          "default": false
        },
        "fileContent": {
          "description": "The text content of the file to upload",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "The name of the file",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "name": {
          "description": "The name of this shared drive",
          "type": "string",
          "default": ""
        },
        "resolveData": {
          "description": "By default the response only contain the ID of the file. If this option gets activated, it will resolve the data automatically.",
          "type": "boolean",
          "default": false
        },
        "parents": {
          "description": "The IDs of the parent folders which contain the file",
          "type": "string",
          "default": []
        },
        "driveId": {
          "description": "The ID of the drive",
          "type": "string",
          "examples": [
            "Drive"
          ]
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
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
      "2"
    ]
  },
  "credentials": [
    {
      "name": "googleApi",
      "required": true
    },
    {
      "name": "googleDriveOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
