---
title: "Node: Box"
slug: "node-box"
version: "1"
updated: "2025-11-13"
summary: "Consume Box API"
node_type: "regular"
group: "['input']"
---

# Node: Box

**Purpose.** Consume Box API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:box.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **boxOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `boxOAuth2Api` | ✓ | - |

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
| Get | `get` | Get a file |
| Search | `search` | Search files |
| Share | `share` | Share a file |
| Upload | `upload` | Upload a file |

### Folder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a folder |
| Delete | `delete` | Delete a folder |
| Get | `get` | Get a folder |
| Search | `search` | Search files |
| Share | `share` | Share a folder |
| Update | `update` | Update folder |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | file | ✗ | Resource to operate on |  |

**Resource options:**

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
* **Get** (`get`) - Get a file
* **Search** (`search`) - Search files
* **Share** (`share`) - Share a file
* **Upload** (`upload`) - Upload a file

---

### Copy parameters (`copy`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File ID | `fileId` | string |  | ✓ |  |  |
| Parent ID | `parentId` | string |  | ✗ | The ID of folder to copy the file to. If not defined will be copied to the root folder. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. |
| Name | `name` | string |  | An optional new name for the copied file |
| Version | `version` | string |  | An optional ID of the specific file version to copy |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File ID | `fileId` | string |  | ✗ | Field ID |  |
| Folder ID | `folderId` | string |  | ✗ |  |  |
| Recursive | `recursive` | boolean | False | ✗ | Whether to delete a folder that is not empty by recursively deleting the folder and all of its content |  |

### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File ID | `fileId` | string |  | ✗ |  |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File ID | `fileId` | string |  | ✗ | Field ID |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. |

</details>

| Folder ID | `folderId` | string |  | ✗ |  |  |

### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Query | `query` | string |  | ✗ | The string to search for. This query is matched against item names, descriptions, text content of files, and various other fields of the different item types. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Limits search results to items with the given content types. Content types are defined as a comma-separated lists of Box recognized content types. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content Types | `contet_types` | string |  | Limits search results to items with the given content types. Content types are defined as a comma-separated lists of Box recognized content types. |
| Created At Range | `createdRangeUi` | fixedCollection | {} |  |
| Direction | `direction` | options |  | Defines the direction in which search results are ordered. Default value is DESC. |
| Fields | `fields` | string |  | A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. |
| File Extensions | `file_extensions` | string |  | Limits search results to a comma-separated list of file extensions |
| Folder IDs | `ancestor_folder_ids` | string |  | Limits search results to items within the given list of folders. Folders are defined as a comma-separated lists of folder IDs. |
| Scope | `scope` | options |  | Limits search results to a user scope |
| Size Range | `size_range` | string |  | Limits search results to items within a given file size range. File size ranges are defined as comma-separated byte sizes. |
| Sort | `sort` | options | relevance | Returns the results ordered in descending order by date at which the item was last modified |
| Trash Content | `trash_content` | options | non_trashed_only | Controls if search results include the trash |
| Update At Range | `updatedRangeUi` | fixedCollection | {} |  |
| User IDs | `owner_user_ids` | string |  | Limits search results to items owned by the given list of owners. Owners are defined as a comma-separated list of user IDs. |

</details>

| Query | `query` | string |  | ✗ | The string to search for. This query is matched against item names, descriptions, text content of files, and various other fields of the different item types. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Limits search results to items with the given content types. Content types are defined as a comma-separated lists of Box recognized content types. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content Types | `contet_types` | string |  | Limits search results to items with the given content types. Content types are defined as a comma-separated lists of Box recognized content types. |
| Created At Range | `createdRangeUi` | fixedCollection | {} |  |
| Direction | `direction` | options |  | Defines the direction in which search results are ordered. Default value is DESC. |
| Fields | `fields` | string |  | A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. |
| File Extensions | `file_extensions` | string |  | Limits search results to a comma-separated list of file extensions |
| Folder IDs | `ancestor_folder_ids` | string |  | Limits search results to items within the given list of folders. Folders are defined as a comma-separated lists of folder IDs. |
| Scope | `scope` | options |  | Limits search results to a user scope |
| Size Range | `size_range` | string |  | Limits search results to items within a given file size range. File size ranges are defined as comma-separated byte sizes. |
| Sort | `sort` | options | relevance | Returns the results ordered in descending order by date at which the item was last modified |
| Trash Content | `trash_content` | options | non_trashed_only | Controls if search results include the trash |
| Update At Range | `updatedRangeUi` | fixedCollection | {} |  |
| User IDs | `owner_user_ids` | string |  | Limits search results to items owned by the given list of owners. Owners are defined as a comma-separated list of user IDs. |

</details>


### Share parameters (`share`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File ID | `fileId` | string |  | ✗ | The ID of the file to share |  |
| Accessible By | `accessibleBy` | options |  | ✗ | The type of object the file will be shared with |  |

**Accessible By options:**

* **Group** (`group`)
* **User** (`user`)

| Use Email | `useEmail` | boolean | True | ✗ | Whether identify the user by email or ID | email |
| Email | `email` | string |  | ✗ | The user's email address to share the file with | e.g. name@email.com | email |
| User ID | `userId` | string |  | ✗ | The user's ID to share the file with |  |
| Group ID | `groupId` | string |  | ✗ | The group's ID to share the file with |  |
| Role | `role` | options | editor | ✗ | A Co-owner has all of functional read/write access that an editor does |  |

**Role options:**

* **Co-Owner** (`coOwner`) - A Co-owner has all of functional read/write access that an editor does
* **Editor** (`editor`) - An editor has full read/write access to a folder or file
* **Previewer** (`previewer`) - A previewer has limited read access
* **Previewer Uploader** (`previewerUploader`) - This access level is a combination of Previewer and Uploader
* **Uploader** (`uploader`) - An uploader has limited write access
* **Viewer** (`viewer`) - A viewer has read access to a folder or file
* **Viewer Uploader** (`viewerUploader`) - This access level is a combination of Viewer and Uploader

| Options | `options` | collection | {} | ✗ | Whether the invited users can see the entire parent path to the associated folder. The user will not gain privileges in any parent folder and therefore cannot see content the user is not collaborated on. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Can View Path | `can_view_path` | boolean | False | Whether the invited users can see the entire parent path to the associated folder. The user will not gain privileges in any parent folder and therefore cannot see content the user is not collaborated on. |
| Expires At | `expires_at` | dateTime |  | Set the expiration date for the collaboration. At this date, the collaboration will be automatically removed from the item. |
| Fields | `fields` | string |  | A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. |
| Notify | `notify` | boolean | False | Whether if users should receive email notification for the action performed |

</details>

| Folder ID | `folderId` | string |  | ✗ | The ID of the folder to share |  |
| Accessible By | `accessibleBy` | options | user | ✗ | The type of object the file will be shared with |  |

**Accessible By options:**

* **User** (`user`)
* **Group** (`group`)

| Use Email | `useEmail` | boolean | True | ✗ | Whether identify the user by email or ID | email |
| Email | `email` | string |  | ✗ | The user's email address to share the folder with | e.g. name@email.com | email |
| User ID | `userId` | string |  | ✗ | The user's ID to share the folder with |  |
| Group ID | `groupId` | string |  | ✗ | The group's ID to share the folder with |  |
| Role | `role` | options | editor | ✗ | A Co-owner has all of functional read/write access that an editor does |  |

**Role options:**

* **Co-Owner** (`coOwner`) - A Co-owner has all of functional read/write access that an editor does
* **Editor** (`editor`) - An editor has full read/write access to a folder or file
* **Previewer** (`previewer`) - A previewer has limited read access
* **Previewer Uploader** (`previewerUploader`) - This access level is a combination of Previewer and Uploader
* **Uploader** (`uploader`) - An uploader has limited write access
* **Viewer** (`viewer`) - A viewer has read access to a folder or file
* **Viewer Uploader** (`viewerUploader`) - This access level is a combination of Viewer and Uploader

| Options | `options` | collection | {} | ✗ | Whether the invited users can see the entire parent path to the associated folder. The user will not gain privileges in any parent folder and therefore cannot see content the user is not collaborated on. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Can View Path | `can_view_path` | boolean | False | Whether the invited users can see the entire parent path to the associated folder. The user will not gain privileges in any parent folder and therefore cannot see content the user is not collaborated on. |
| Expires At | `expires_at` | dateTime |  | Set the expiration date for the collaboration. At this date, the collaboration will be automatically removed from the item. |
| Fields | `fields` | string |  | A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. |
| Notify | `notify` | boolean | False | Whether if users should receive email notification for the action performed |

</details>


### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Name | `fileName` | string |  | ✗ | The name the file should be saved as | e.g. photo.png |  |
| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| File Content | `fileContent` | string |  | ✓ | The text content of the file |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |
| Parent ID | `parentId` | string |  | ✗ | ID of the parent folder that will contain the file. If not it will be uploaded to the root folder. |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Folder's name |  |
| Parent ID | `parentId` | string |  | ✗ | ID of the folder you want to create the new folder in. if not defined it will be created on the root folder. |  |
| Options | `options` | collection | {} | ✗ | Only emails from registered email addresses for collaborators will be accepted | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Access | `access` | options |  | Only emails from registered email addresses for collaborators will be accepted |
| Fields | `fields` | string |  | A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Folder ID | `folderId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Whether users who are not the owner of the folder can invite new collaborators to the folder | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Can Non-Owners Invite | `can_non_owners_invite` | boolean | False | Whether users who are not the owner of the folder can invite new collaborators to the folder |
| Can Non-Owners View Colaborators | `can_non_owners_view_collaborators` | boolean | False | Whether to restrict collaborators who are not the owner of this folder from viewing other collaborations on this folder |
| Description | `description` | string |  | The optional description of this folder |
| Fields | `fields` | string |  | A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response. |
| Is Collaboration Restricted To Enterprise | `is_collaboration_restricted_to_enterprise` | boolean | False | Whether new invites to this folder are restricted to users within the enterprise. This does not affect existing collaborations. |
| Name | `name` | string |  | The optional new name for this folder |
| Parent ID | `parentId` | string |  | The parent folder for this folder. Use this to move the folder or to restore it out of the trash. |
| Shared Link | `shared_link` | collection | {} | Share link information |

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
node: box
displayName: Box
description: Consume Box API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: boxOAuth2Api
  required: true
operations:
- id: copy
  name: Copy
  description: Copy a file
  params:
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      displayOptions:
        show:
          operation:
          - share
          resource:
          - file
    typeInfo: &id002
      type: string
      displayName: File ID
      name: fileId
  - id: parentId
    name: Parent ID
    type: string
    default: ''
    required: false
    description: The ID of folder to copy the file to. If not defined will be copied
      to the root folder.
    validation: &id025
      displayOptions:
        show:
          operation:
          - create
          resource:
          - folder
    typeInfo: &id026
      type: string
      displayName: Parent ID
      name: parentId
- id: delete
  name: Delete
  description: Delete a file
  params:
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: false
    description: Field ID
    validation: *id001
    typeInfo: *id002
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: false
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - folder
    typeInfo: &id004
      type: string
      displayName: Folder ID
      name: folderId
  - id: recursive
    name: Recursive
    type: boolean
    default: false
    required: false
    description: Whether to delete a folder that is not empty by recursively deleting
      the folder and all of its content
    validation:
      displayOptions:
        show:
          operation:
          - delete
          resource:
          - folder
    typeInfo:
      type: boolean
      displayName: Recursive
      name: recursive
- id: download
  name: Download
  description: Download a file
  params:
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id023
      required: true
      displayOptions:
        show:
          binaryData:
          - true
          operation:
          - upload
          resource:
          - file
    typeInfo: &id024
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
- id: get
  name: Get
  description: Get a file
  params:
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: false
    description: Field ID
    validation: *id001
    typeInfo: *id002
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: false
    description: ''
    validation: *id003
    typeInfo: *id004
- id: search
  name: Search
  description: Search files
  params:
  - id: query
    name: Query
    type: string
    default: ''
    required: false
    description: The string to search for. This query is matched against item names,
      descriptions, text content of files, and various other fields of the different
      item types.
    validation: &id005
      displayOptions:
        show:
          operation:
          - search
          resource:
          - folder
    typeInfo: &id006
      type: string
      displayName: Query
      name: query
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id007
      displayOptions:
        show:
          operation:
          - search
          resource:
          - folder
    typeInfo: &id008
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id009
      displayOptions:
        show:
          operation:
          - search
          resource:
          - folder
          returnAll:
          - false
    typeInfo: &id010
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: query
    name: Query
    type: string
    default: ''
    required: false
    description: The string to search for. This query is matched against item names,
      descriptions, text content of files, and various other fields of the different
      item types.
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id007
    typeInfo: *id008
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
- id: share
  name: Share
  description: Share a file
  params:
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: false
    description: The ID of the file to share
    validation: *id001
    typeInfo: *id002
  - id: accessibleBy
    name: Accessible By
    type: options
    default: ''
    required: false
    description: The type of object the file will be shared with
    validation: &id011
      displayOptions:
        show:
          operation:
          - share
          resource:
          - folder
    typeInfo: &id012
      type: options
      displayName: Accessible By
      name: accessibleBy
      possibleValues:
      - value: user
        name: User
        description: ''
      - value: group
        name: Group
        description: ''
  - id: useEmail
    name: Use Email
    type: boolean
    default: true
    required: false
    description: Whether identify the user by email or ID
    validation: &id013
      format: email
      displayOptions:
        show:
          operation:
          - share
          resource:
          - folder
          accessibleBy:
          - user
    typeInfo: &id014
      type: boolean
      displayName: Use Email
      name: useEmail
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: The user's email address to share the file with
    placeholder: name@email.com
    validation: &id015
      format: email
      displayOptions:
        show:
          operation:
          - share
          resource:
          - folder
          accessibleBy:
          - user
          useEmail:
          - true
    typeInfo: &id016
      type: string
      displayName: Email
      name: email
  - id: userId
    name: User ID
    type: string
    default: ''
    required: false
    description: The user's ID to share the file with
    validation: &id017
      displayOptions:
        show:
          operation:
          - share
          resource:
          - folder
          accessibleBy:
          - user
          useEmail:
          - false
    typeInfo: &id018
      type: string
      displayName: User ID
      name: userId
  - id: groupId
    name: Group ID
    type: string
    default: ''
    required: false
    description: The group's ID to share the file with
    validation: &id019
      displayOptions:
        show:
          operation:
          - share
          resource:
          - folder
          accessibleBy:
          - group
    typeInfo: &id020
      type: string
      displayName: Group ID
      name: groupId
  - id: role
    name: Role
    type: options
    default: editor
    required: false
    description: A Co-owner has all of functional read/write access that an editor
      does
    validation: &id021
      displayOptions:
        show:
          operation:
          - share
          resource:
          - folder
    typeInfo: &id022
      type: options
      displayName: Role
      name: role
      possibleValues:
      - value: coOwner
        name: Co-Owner
        description: A Co-owner has all of functional read/write access that an editor
          does
      - value: editor
        name: Editor
        description: An editor has full read/write access to a folder or file
      - value: previewer
        name: Previewer
        description: A previewer has limited read access
      - value: previewerUploader
        name: Previewer Uploader
        description: This access level is a combination of Previewer and Uploader
      - value: uploader
        name: Uploader
        description: An uploader has limited write access
      - value: viewer
        name: Viewer
        description: A viewer has read access to a folder or file
      - value: viewerUploader
        name: Viewer Uploader
        description: This access level is a combination of Viewer and Uploader
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: false
    description: The ID of the folder to share
    validation: *id003
    typeInfo: *id004
  - id: accessibleBy
    name: Accessible By
    type: options
    default: user
    required: false
    description: The type of object the file will be shared with
    validation: *id011
    typeInfo: *id012
  - id: useEmail
    name: Use Email
    type: boolean
    default: true
    required: false
    description: Whether identify the user by email or ID
    validation: *id013
    typeInfo: *id014
  - id: email
    name: Email
    type: string
    default: ''
    required: false
    description: The user's email address to share the folder with
    placeholder: name@email.com
    validation: *id015
    typeInfo: *id016
  - id: userId
    name: User ID
    type: string
    default: ''
    required: false
    description: The user's ID to share the folder with
    validation: *id017
    typeInfo: *id018
  - id: groupId
    name: Group ID
    type: string
    default: ''
    required: false
    description: The group's ID to share the folder with
    validation: *id019
    typeInfo: *id020
  - id: role
    name: Role
    type: options
    default: editor
    required: false
    description: A Co-owner has all of functional read/write access that an editor
      does
    validation: *id021
    typeInfo: *id022
- id: upload
  name: Upload
  description: Upload a file
  params:
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: false
    description: The name the file should be saved as
    placeholder: photo.png
    validation:
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
    typeInfo:
      type: string
      displayName: File Name
      name: fileName
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
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
      name: binaryData
  - id: fileContent
    name: File Content
    type: string
    default: ''
    required: true
    description: The text content of the file
    validation:
      required: true
      displayOptions:
        show:
          binaryData:
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
    validation: *id023
    typeInfo: *id024
  - id: parentId
    name: Parent ID
    type: string
    default: ''
    required: false
    description: ID of the parent folder that will contain the file. If not it will
      be uploaded to the root folder.
    validation: *id025
    typeInfo: *id026
- id: create
  name: Create
  description: Create a folder
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Folder's name
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - folder
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: parentId
    name: Parent ID
    type: string
    default: ''
    required: false
    description: ID of the folder you want to create the new folder in. if not defined
      it will be created on the root folder.
    validation: *id025
    typeInfo: *id026
- id: update
  name: Update
  description: Update folder
  params:
  - id: folderId
    name: Folder ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
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
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: options
    text: Add option
  - field: fileName
    text: photo.png
  - field: options
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: options
    text: Add option
  - field: updateFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/box.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Box Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "copy",
        "delete",
        "download",
        "get",
        "search",
        "share",
        "upload",
        "create",
        "update"
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
            "file",
            "folder"
          ],
          "default": "file"
        },
        "operation": {
          "description": "Create a folder",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "search",
            "share",
            "update"
          ],
          "default": "create"
        },
        "fileId": {
          "description": "The ID of the file to share",
          "type": "string",
          "default": ""
        },
        "parentId": {
          "description": "ID of the folder you want to create the new folder in. if not defined it will be created on the root folder.",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Limits search results to items with the given content types. Content types are defined as a comma-separated lists of Box recognized content types.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "query": {
          "description": "The string to search for. This query is matched against item names, descriptions, text content of files, and various other fields of the different item types.",
          "type": "string",
          "default": ""
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
        },
        "accessibleBy": {
          "description": "The type of object the file will be shared with",
          "type": "string",
          "enum": [
            "user",
            "group"
          ],
          "default": "user"
        },
        "useEmail": {
          "description": "Whether identify the user by email or ID",
          "type": "boolean",
          "default": true,
          "format": "email"
        },
        "email": {
          "description": "The user's email address to share the folder with",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "userId": {
          "description": "The user's ID to share the folder with",
          "type": "string",
          "default": ""
        },
        "groupId": {
          "description": "The group's ID to share the folder with",
          "type": "string",
          "default": ""
        },
        "role": {
          "description": "A Co-owner has all of functional read/write access that an editor does",
          "type": "string",
          "enum": [
            "coOwner",
            "editor",
            "previewer",
            "previewerUploader",
            "uploader",
            "viewer",
            "viewerUploader"
          ],
          "default": "editor"
        },
        "options": {
          "description": "Whether the invited users can see the entire parent path to the associated folder. The user will not gain privileges in any parent folder and therefore cannot see content the user is not collaborated on.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "fileName": {
          "description": "The name the file should be saved as",
          "type": "string",
          "default": "",
          "examples": [
            "photo.png"
          ]
        },
        "binaryData": {
          "description": "Whether the data to upload should be taken from binary field",
          "type": "boolean",
          "default": false
        },
        "fileContent": {
          "description": "The text content of the file",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "Folder's name",
          "type": "string",
          "default": ""
        },
        "folderId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "recursive": {
          "description": "Whether to delete a folder that is not empty by recursively deleting the folder and all of its content",
          "type": "boolean",
          "default": false
        },
        "updateFields": {
          "description": "Whether users who are not the owner of the folder can invite new collaborators to the folder",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
      "name": "boxOAuth2Api",
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
