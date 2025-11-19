---
title: "Node: Nextcloud"
slug: "node-nextcloud"
version: "1"
updated: "2025-11-13"
summary: "Access data on Nextcloud"
node_type: "regular"
group: "['input']"
---

# Node: Nextcloud

**Purpose.** Access data on Nextcloud
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:nextcloud.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **nextCloudApi**: N/A
- **nextCloudOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `nextCloudApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `nextCloudOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Copy | `copy` | Copy a file |
| Delete | `delete` | Delete a file |
| Download | `download` | Download a file |
| Move | `move` | Move a file |
| Share | `share` | Share a file |
| Upload | `upload` | Upload a file |

### Folder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Copy | `copy` | Copy a folder |
| Create | `create` | Create a folder |
| Delete | `delete` | Delete a folder |
| List | `list` | Return the contents of a given folder |
| Move | `move` | Move a folder |
| Share | `share` | Share a folder |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Invite a user to a NextCloud organization |
| Delete | `delete` | Delete a user |
| Get | `get` | Retrieve information about a single user |
| Get Many | `getAll` | Retrieve a list of users |
| Update | `update` | Edit attributes related to a user |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | file | ✗ | Resource to operate on |  |

**Resource options:**

* **File** (`file`)
* **Folder** (`folder`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | upload | ✗ | Copy a file |  |

**Operation options:**

* **Copy** (`copy`) - Copy a file
* **Delete** (`delete`) - Delete a file
* **Download** (`download`) - Download a file
* **Move** (`move`) - Move a file
* **Share** (`share`) - Share a file
* **Upload** (`upload`) - Upload a file

---

### Copy parameters (`copy`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From Path | `path` | string |  | ✓ | The path of file or folder to copy. The path should start with "/". | e.g. /invoices/original.txt |  |
| To Path | `toPath` | string |  | ✓ | The destination path of file or folder. The path should start with "/". | e.g. /invoices/copy.txt |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Delete Path | `path` | string |  | ✓ | The path to delete. Can be a single file or a whole folder. The path should start with "/". | e.g. /invoices/2019/invoice_1.pdf |  |
| Username | `userId` | string |  | ✓ | Username the user will have | e.g. john |  |

### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Path | `path` | string |  | ✓ | The file path of the file to download. Has to contain the full path. The path should start with "/". | e.g. /invoices/2019/invoice_1.pdf |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |

### Move parameters (`move`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From Path | `path` | string |  | ✓ | The path of file or folder to move. The path should start with "/". | e.g. /invoices/old_name.txt |  |
| To Path | `toPath` | string |  | ✓ | The new path of file or folder. The path should start with "/". | e.g. /invoices/new_name.txt |  |

### Share parameters (`share`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Path | `path` | string |  | ✓ | The file path of the file to share. Has to contain the full path. The path should start with "/". | e.g. /invoices/2019/invoice_1.pdf |  |
| Share Type | `shareType` | options | 0 | ✗ | The share permissions to set |  |

**Share Type options:**

* **Circle** (``)
* **Email** (``)
* **Group** (``)
* **Public Link** (``)
* **User** (``)

| Circle ID | `circleId` | string |  | ✗ | The ID of the circle to share with |  |
| Email | `email` | string |  | ✗ | The Email address to share with | e.g. name@email.com | email |
| Group ID | `groupId` | string |  | ✗ | The ID of the group to share with |  |
| User | `user` | string |  | ✗ | The user to share with |  |
| Options | `options` | collection | {} | ✗ | Optional search string | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Password | `password` | string |  | Optional search string |
| Permissions | `permissions` | options | 1 | The share permissions to set |

</details>


### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Path | `path` | string |  | ✓ | The absolute file path of the file to upload. Has to contain the full path. The parent folder has to exist. Existing files get overwritten. | e.g. /invoices/2019/invoice_1.pdf |  |
| Binary File | `binaryDataUpload` | boolean | False | ✓ |  |  |
| File Content | `fileContent` | string |  | ✗ | The text content of the file to upload |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Folder | `path` | string |  | ✓ | The folder to create. The parent folder has to exist. The path should start with "/". | e.g. /invoices/2019 |  |
| Username | `userId` | string |  | ✓ | Username the user will have | e.g. john |  |
| Email | `email` | string |  | ✓ | The email of the user to invite | e.g. john@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The display name of the user to invite | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Display Name | `displayName` | string |  | The display name of the user to invite |

</details>


### List parameters (`list`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Folder Path | `path` | string |  | ✗ | The path of which to list the content. The path should start with "/". | e.g. /invoices/2019/ |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Username | `userId` | string |  | ✓ | Username the user will have | e.g. john |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Optional search string | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Search | `search` | string |  | Optional search string |
| Offset | `offset` | number |  | Optional offset value |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Username | `userId` | string |  | ✓ | Username the user will have | e.g. john |  |
| Update Fields | `updateFields` | fixedCollection | {} | ✗ | The new address for the user | e.g. Add option |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `field` |  |  |  |

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
* Categories: Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: nextCloud
displayName: Nextcloud
description: Access data on Nextcloud
version: '1'
nodeType: regular
group:
- input
credentials:
- name: nextCloudApi
  required: true
- name: nextCloudOAuth2Api
  required: true
operations:
- id: copy
  name: Copy
  description: Copy a file
  params:
  - id: path
    name: From Path
    type: string
    default: ''
    required: true
    description: The path of file or folder to copy. The path should start with "/".
    placeholder: /invoices/original.txt
    validation: &id001
      displayOptions:
        show:
          operation:
          - list
          resource:
          - folder
    typeInfo: &id002
      type: string
      displayName: Folder Path
      name: path
  - id: toPath
    name: To Path
    type: string
    default: ''
    required: true
    description: The destination path of file or folder. The path should start with
      "/".
    placeholder: /invoices/copy.txt
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - move
          resource:
          - file
          - folder
    typeInfo: &id004
      type: string
      displayName: To Path
      name: toPath
- id: delete
  name: Delete
  description: Delete a file
  params:
  - id: path
    name: Delete Path
    type: string
    default: ''
    required: true
    description: The path to delete. Can be a single file or a whole folder. The path
      should start with "/".
    placeholder: /invoices/2019/invoice_1.pdf
    validation: *id001
    typeInfo: *id002
  - id: userId
    name: Username
    type: string
    default: ''
    required: true
    description: Username the user will have
    placeholder: john
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - delete
          - get
          - update
    typeInfo: &id008
      type: string
      displayName: Username
      name: userId
- id: download
  name: Download
  description: Download a file
  params:
  - id: path
    name: File Path
    type: string
    default: ''
    required: true
    description: The file path of the file to download. Has to contain the full path.
      The path should start with "/".
    placeholder: /invoices/2019/invoice_1.pdf
    validation: *id001
    typeInfo: *id002
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id005
      required: true
      displayOptions:
        show:
          binaryDataUpload:
          - true
          operation:
          - upload
          resource:
          - file
    typeInfo: &id006
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
- id: move
  name: Move
  description: Move a file
  params:
  - id: path
    name: From Path
    type: string
    default: ''
    required: true
    description: The path of file or folder to move. The path should start with "/".
    placeholder: /invoices/old_name.txt
    validation: *id001
    typeInfo: *id002
  - id: toPath
    name: To Path
    type: string
    default: ''
    required: true
    description: The new path of file or folder. The path should start with "/".
    placeholder: /invoices/new_name.txt
    validation: *id003
    typeInfo: *id004
- id: share
  name: Share
  description: Share a file
  params:
  - id: path
    name: File Path
    type: string
    default: ''
    required: true
    description: The file path of the file to share. Has to contain the full path.
      The path should start with "/".
    placeholder: /invoices/2019/invoice_1.pdf
    validation: *id001
    typeInfo: *id002
  - id: shareType
    name: Share Type
    type: options
    default: 0
    required: false
    description: The share permissions to set
    validation:
      displayOptions:
        show:
          operation:
          - share
          resource:
          - file
          - folder
    typeInfo:
      type: options
      displayName: Share Type
      name: shareType
      possibleValues:
      - value: Circle
        name: Circle
        description: ''
      - value: Email
        name: Email
        description: ''
      - value: Group
        name: Group
        description: ''
      - value: Public Link
        name: Public Link
        description: ''
      - value: User
        name: User
        description: ''
  - id: circleId
    name: Circle ID
    type: string
    default: ''
    required: false
    description: The ID of the circle to share with
    validation:
      displayOptions:
        show:
          resource:
          - file
          - folder
          operation:
          - share
          shareType:
          - 7
    typeInfo:
      type: string
      displayName: Circle ID
      name: circleId
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: The Email address to share with
    placeholder: name@email.com
    validation: &id009
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo: &id010
      type: string
      displayName: Email
      name: email
  - id: groupId
    name: Group ID
    type: string
    default: ''
    required: false
    description: The ID of the group to share with
    validation:
      displayOptions:
        show:
          resource:
          - file
          - folder
          operation:
          - share
          shareType:
          - 1
    typeInfo:
      type: string
      displayName: Group ID
      name: groupId
  - id: user
    name: User
    type: string
    default: ''
    required: false
    description: The user to share with
    validation:
      displayOptions:
        show:
          resource:
          - file
          - folder
          operation:
          - share
          shareType:
          - 0
    typeInfo:
      type: string
      displayName: User
      name: user
- id: upload
  name: Upload
  description: Upload a file
  params:
  - id: path
    name: File Path
    type: string
    default: ''
    required: true
    description: The absolute file path of the file to upload. Has to contain the
      full path. The parent folder has to exist. Existing files get overwritten.
    placeholder: /invoices/2019/invoice_1.pdf
    validation: *id001
    typeInfo: *id002
  - id: binaryDataUpload
    name: Binary File
    type: boolean
    default: false
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
    typeInfo:
      type: boolean
      displayName: Binary File
      name: binaryDataUpload
  - id: fileContent
    name: File Content
    type: string
    default: ''
    required: false
    description: The text content of the file to upload
    validation:
      displayOptions:
        show:
          binaryDataUpload:
          - false
          operation:
          - upload
          resource:
          - file
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
    validation: *id005
    typeInfo: *id006
- id: create
  name: Create
  description: Create a folder
  params:
  - id: path
    name: Folder
    type: string
    default: ''
    required: true
    description: The folder to create. The parent folder has to exist. The path should
      start with "/".
    placeholder: /invoices/2019
    validation: *id001
    typeInfo: *id002
  - id: userId
    name: Username
    type: string
    default: ''
    required: true
    description: Username the user will have
    placeholder: john
    validation: *id007
    typeInfo: *id008
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email of the user to invite
    placeholder: john@email.com
    validation: *id009
    typeInfo: *id010
- id: list
  name: List
  description: Return the contents of a given folder
  params:
  - id: path
    name: Folder Path
    type: string
    default: ''
    required: false
    description: The path of which to list the content. The path should start with
      "/".
    placeholder: /invoices/2019/
    validation: *id001
    typeInfo: *id002
- id: get
  name: Get
  description: Retrieve information about a single user
  params:
  - id: userId
    name: Username
    type: string
    default: ''
    required: true
    description: Username the user will have
    placeholder: john
    validation: *id007
    typeInfo: *id008
- id: getAll
  name: Get Many
  description: Retrieve a list of users
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          resource:
          - user
          operation:
          - getAll
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
- id: update
  name: Update
  description: Edit attributes related to a user
  params:
  - id: userId
    name: Username
    type: string
    default: ''
    required: true
    description: Username the user will have
    placeholder: john
    validation: *id007
    typeInfo: *id008
  - id: updateFields
    name: Update Fields
    type: fixedCollection
    default: {}
    required: false
    description: The new address for the user
    placeholder: Add option
    validation:
      displayOptions:
        show:
          resource:
          - user
          operation:
          - update
    typeInfo:
      type: fixedCollection
      displayName: Update Fields
      name: updateFields
      typeOptions:
        multipleValues: false
      subProperties:
      - name: field
        displayName: Fields
        values:
        - displayName: Key
          name: key
          type: options
          description: The new address for the user
          value: address
          default: email
          options:
          - name: Address
            description: The new address for the user
            value: address
            displayName: Address
          - name: Display Name
            description: The new display name for the user
            value: displayname
            displayName: Display Name
          - name: Email
            description: The new email for the user
            value: email
            displayName: Email
          - name: Password
            description: The new password for the user
            value: password
            displayName: Password
          - name: Twitter
            description: The new twitter handle for the user
            value: twitter
            displayName: Twitter
          - name: Website
            description: The new website for the user
            value: website
            displayName: Website
        - displayName: Value
          name: value
          type: string
          description: Value of the updated attribute
          default: ''
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: path
    text: /invoices/original.txt
  - field: toPath
    text: /invoices/copy.txt
  - field: path
    text: /invoices/2019/invoice_1.pdf
  - field: path
    text: /invoices/old_name.txt
  - field: toPath
    text: /invoices/new_name.txt
  - field: path
    text: /invoices/2019/invoice_1.pdf
  - field: path
    text: /invoices/2019/invoice_1.pdf
  - field: path
    text: /invoices/2019/invoice_1.pdf
  - field: email
    text: name@email.com
  - field: options
    text: Add option
  - field: path
    text: /invoices/2019
  - field: path
    text: /invoices/2019/
  - field: userId
    text: john
  - field: email
    text: john@email.com
  - field: additionalFields
    text: Add Field
  - field: userId
    text: john
  - field: options
    text: Add option
  - field: updateFields
    text: Add option
  hints:
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/nextCloud.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Nextcloud Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "copy",
        "delete",
        "download",
        "move",
        "share",
        "upload",
        "create",
        "list",
        "get",
        "getAll",
        "update"
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
            "accessToken",
            "oAuth2"
          ],
          "default": "accessToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "file",
            "folder",
            "user"
          ],
          "default": "file"
        },
        "operation": {
          "description": "Invite a user to a NextCloud organization",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "path": {
          "description": "The path of which to list the content. The path should start with \"/\".",
          "type": "string",
          "default": "",
          "examples": [
            "/invoices/2019/"
          ]
        },
        "toPath": {
          "description": "The new path of file or folder. The path should start with \"/\".",
          "type": "string",
          "default": "",
          "examples": [
            "/invoices/new_name.txt"
          ]
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "binaryDataUpload": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "fileContent": {
          "description": "The text content of the file to upload",
          "type": "string",
          "default": ""
        },
        "shareType": {
          "description": "The share permissions to set",
          "type": "string",
          "enum": [
            "Circle",
            "Email",
            "Group",
            "Public Link",
            "User"
          ],
          "default": 0
        },
        "circleId": {
          "description": "The ID of the circle to share with",
          "type": "string",
          "default": ""
        },
        "email": {
          "description": "The email of the user to invite",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "john@email.com"
          ]
        },
        "groupId": {
          "description": "The ID of the group to share with",
          "type": "string",
          "default": ""
        },
        "user": {
          "description": "The user to share with",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Optional search string",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "userId": {
          "description": "Username the user will have",
          "type": "string",
          "default": "",
          "examples": [
            "john"
          ]
        },
        "additionalFields": {
          "description": "The display name of the user to invite",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 50
        },
        "updateFields": {
          "description": "The new address for the user",
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
      "name": "nextCloudApi",
      "required": true
    },
    {
      "name": "nextCloudOAuth2Api",
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
