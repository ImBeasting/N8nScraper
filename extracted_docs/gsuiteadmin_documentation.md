---
title: "Node: Google Workspace Admin"
slug: "node-gsuiteadmin"
version: "1"
updated: "2025-11-13"
summary: "Consume Google Workspace Admin API"
node_type: "regular"
group: "['input']"
---

# Node: Google Workspace Admin

**Purpose.** Consume Google Workspace Admin API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:gSuiteAdmin.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **gSuiteAdminOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `gSuiteAdminOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Device Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a ChromeOS device |
| Get Many | `getAll` | Get many ChromeOS devices |
| Update | `update` | Update a ChromeOS device |
| Change Status | `changeStatus` | Change the status of a ChromeOS device |

### Group Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a group |
| Delete | `delete` | Delete a group |
| Get | `get` | Get a group |
| Get Many | `getAll` | Get many groups |
| Update | `update` | Update a group |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add to Group | `addToGroup` | Add an existing user to a group |
| Create | `create` | Create a user |
| Delete | `delete` | Delete a user |
| Get | `get` | Get a user |
| Get Many | `getAll` | Get many users |
| Remove From Group | `removeFromGroup` | Remove a user from a group |
| Update | `update` | Update a user |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | user | ✗ | Resource to operate on |  |

**Resource options:**

* **ChromeOS Device** (`device`)
* **Group** (`group`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Get a ChromeOS device |  |

**Operation options:**

* **Get** (`get`) - Get a ChromeOS device
* **Get Many** (`getAll`) - Get many ChromeOS devices
* **Update** (`update`) - Update a ChromeOS device
* **Change Status** (`changeStatus`) - Change the status of a ChromeOS device

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Device | `deviceId` | resourceLocator |  | ✓ | Select the device you want to retrieve | e.g. e.g. 123e4567-e89b-12d3-a456-426614174000 |  |
| Output | `projection` | options | basic | ✓ | Do not include any custom fields for the user |  |

**Output options:**

* **Basic** (`basic`) - Do not include any custom fields for the user
* **Full** (`full`) - Include all fields associated with this user

| Group | `groupId` | list |  | ✓ | Select the group to perform the operation on | e.g. e.g. 0123kx3o1habcdf |  |
| User | `userId` | resourceLocator |  | ✓ | Select the user to perform the operation on | e.g. e.g. sales@example.com |  |
| Output | `output` | options | simplified | ✓ | Only return specific fields: kind, ID, primaryEmail, name (with subfields), isAdmin, lastLoginTime, creationTime, and suspended |  |

**Output options:**

* **Simplified** (`simplified`) - Only return specific fields: kind, ID, primaryEmail, name (with subfields), isAdmin, lastLoginTime, creationTime, and suspended
* **Raw** (`raw`) - Return all fields from the API response
* **Select Included Fields** (`select`) - Choose specific fields to include

| Fields | `fields` | multiOptions | [] | ✗ | Fields to include in the response when "Select Included Fields" is chosen |  |

**Fields options:**

* **Creation Time** (`creationTime`)
* **Is Admin** (`isAdmin`)
* **Kind** (`kind`)
* **Last Login Time** (`lastLoginTime`)
* **Name** (`name`)
* **Primary Email** (`primaryEmail`)
* **Suspended** (`suspended`)

| Custom Fields | `projection` | options | basic | ✓ | Do not include any custom fields for the user |  |

**Custom Fields options:**

* **Don't Include** (`basic`) - Do not include any custom fields for the user
* **Custom** (`custom`) - Include custom fields from schemas requested in Custom Schema Names or IDs
* **Include All** (`full`) - Include all fields associated with this user

| Custom Schema Names or IDs | `customFieldMask` | multiOptions | [] | ✓ | A comma-separated list of schema names. All fields from these schemas are fetched. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Output | `projection` | options | basic | ✓ | Do not include any custom fields for the user |  |

**Output options:**

* **Basic** (`basic`) - Do not include any custom fields for the user
* **Full** (`full`) - Include all fields associated with this user

| Include Children | `includeChildOrgunits` | boolean | False | ✗ | Whether to include devices from organizational units below your specified organizational unit |  |
| Filter | `filter` | collection | {} | ✗ | Specify the organizational unit name or ID. Choose from the list or use an expression. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filter sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Organizational Unit Name or ID | `orgUnitPath` | options | [] | Specify the organizational unit name or ID. Choose from the list or use an expression. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Query | `query` | string |  | Use Google's querying syntax to filter results |

</details>

| Sort | `sort` | fixedCollection | {} | ✗ | Field to sort the results by | e.g. Add Sort Rule |  |

<details>
<summary><strong>Sort sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort Rules | `sortRules` |  |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Filter | `filter` | collection | {} | ✗ | The unique ID for the customer's Google Workspace account | e.g. Add Filter |  |

<details>
<summary><strong>Filter sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Customer | `customer` | string |  | The unique ID for the customer's Google Workspace account |
| Domain | `domain` | string |  | The domain name. Use this field to get groups from a specific domain. |
| Query | `query` | string |  | Query string to filter the results. Follow Google Admin SDK documentation. <a href="https://developers.google.com/admin-sdk/directory/v1/guides/search-groups#examples" target="_blank">More info</a>. |
| User ID | `userId` | string |  | Email or immutable ID of a user to list groups they are a member of |

</details>

| Sort | `sort` | fixedCollection | {} | ✗ | Field to sort the results by | e.g. Add Sort Rule |  |

<details>
<summary><strong>Sort sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort Rules | `sortRules` |  |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Output | `output` | options | simplified | ✓ | Only return specific fields: kind, ID, primaryEmail, name (with subfields), isAdmin, lastLoginTime, creationTime, and suspended |  |

**Output options:**

* **Simplified** (`simplified`) - Only return specific fields: kind, ID, primaryEmail, name (with subfields), isAdmin, lastLoginTime, creationTime, and suspended
* **Raw** (`raw`) - Return all fields from the API response
* **Select Included Fields** (`select`) - Choose specific fields to include

| Fields | `fields` | multiOptions | [] | ✗ | Fields to include in the response when "Select Included Fields" is chosen |  |

**Fields options:**

* **Creation Time** (`creationTime`)
* **Is Admin** (`isAdmin`)
* **Kind** (`kind`)
* **Last Login Time** (`lastLoginTime`)
* **Name** (`name`)
* **Primary Email** (`primaryEmail`)
* **Suspended** (`suspended`)

| Custom Fields | `projection` | options | basic | ✓ | Do not include any custom fields for the user |  |

**Custom Fields options:**

* **Don't Include** (`basic`) - Do not include any custom fields for the user
* **Custom** (`custom`) - Include custom fields from schemas requested in Custom Schema Names or IDs
* **Include All** (`full`) - Include all fields associated with this user

| Custom Schema Names or IDs | `customFieldMask` | multiOptions | [] | ✓ | A comma-separated list of schema names. All fields from these schemas are fetched. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Filter | `filter` | collection | {} | ✗ | The unique ID for the customer's Google Workspace account | e.g. Add Filter |  |

<details>
<summary><strong>Filter sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Customer | `customer` | string |  | The unique ID for the customer's Google Workspace account |
| Domain | `domain` | string |  | The domain name. Use this field to get groups from a specific domain. |
| Query | `query` | string |  | Query string to filter the results. Follow Google Admin SDK documentation. <a href="https://developers.google.com/admin-sdk/directory/v1/guides/search-users#examples" target="_blank">More info</a>. |
| Show Deleted | `showDeleted` | boolean | False | Whether retrieve the list of deleted users |

</details>

| Sort | `sort` | fixedCollection | {} | ✗ | Field to sort the results by | e.g. Add Sort Rule |  |

<details>
<summary><strong>Sort sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort Rules | `sortRules` |  |  |  |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Device | `deviceId` | resourceLocator |  | ✓ | Select the device you want to retrieve | e.g. e.g. 123e4567-e89b-12d3-a456-426614174000 |  |
| Update Fields | `updateOptions` | collection | {} | ✗ | The full path to the organizational unit. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Option |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Move to Organizational Unit Name or ID | `orgUnitPath` | options | [] | The full path to the organizational unit. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Annotated User | `annotatedUser` | string |  | The annotated user of the device |
| Annotated Location | `annotatedLocation` | string |  | The annotated location of the device |
| Annotated Asset ID | `annotatedAssetId` | string |  | The annotated asset ID of a device |
| Notes | `notes` | string |  | Add notes to a device |

</details>

| Group | `groupId` | list |  | ✓ | Select the group to perform the operation on | e.g. e.g. 0123kx3o1habcdf |  |
| Update Fields | `updateFields` | collection | {} | ✗ | An extended description to help users determine the purpose of a group. For example, you can include information about who should join the group, the types of messages to send to the group, links to FAQs about the group, or related groups. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | An extended description to help users determine the purpose of a group. For example, you can include information about who should join the group, the types of messages to send to the group, links to FAQs about the group, or related groups. |
| Email | `email` | string |  | The group's email address. If your account has multiple domains, select the appropriate domain for the email address. The email must be unique. |
| Name | `name` | string |  | The group's display name |

</details>

| User | `userId` | resourceLocator |  | ✓ | Select the user to perform the operation on | e.g. e.g. sales@example.com |  |
| Update Fields | `updateFields` | collection | {} | ✓ | Whether user is archived | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Archived | `archived` | boolean | False | Whether user is archived |
| Suspend | `suspendUi` | boolean | False | Whether to set the user as suspended. If set to OFF, the user will be reactivated. If not added, the status will remain unchanged. |
| Change Password at Next Login | `changePasswordAtNextLogin` | boolean | False | Whether the user is forced to change their password at next login |
| First Name | `firstName` | string |  |  |
| Last Name | `lastName` | string |  |  |
| Password | `password` | string |  | Stores the password for the user account. A minimum of 8 characters is required. The maximum length is 100 characters. |
| Phones | `phoneUi` | fixedCollection | {} | The type of phone number |
| Primary Email | `primaryEmail` | string |  | The user's primary email address. This property is required in a request to create a user account. The primaryEmail must be unique and cannot be an alias of another user. |
| Secondary Emails | `emailUi` | fixedCollection | {} | The type of the email account |
| Roles | `roles` | multiOptions | [] | Select the roles you want to assign to the user |
| Custom Fields | `customFields` | fixedCollection | {} | Allows editing and adding of custom fields |

</details>


### Change Status parameters (`changeStatus`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Device | `deviceId` | resourceLocator |  | ✓ | Select the device you want to retrieve | e.g. e.g. 123e4567-e89b-12d3-a456-426614174000 |  |
| Status | `action` | options | reenable | ✓ | Re-enable a disabled chromebook |  |

**Status options:**

* **Enabled** (`reenable`) - Re-enable a disabled chromebook
* **Disabled** (`disable`) - Disable a chromebook


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Group Name | `name` | string |  | ✗ | The group's display name | e.g. e.g. Sales |  |
| Group Email | `email` | string |  | ✓ | The group's email address. If your account has multiple domains, select the appropriate domain for the email address. The email must be unique | e.g. e.g. sales@example.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | An extended description to help users determine the purpose of a group. For example, you can include information about who should join the group, the types of messages to send to the group, links to FAQs about the group, or related groups. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | An extended description to help users determine the purpose of a group. For example, you can include information about who should join the group, the types of messages to send to the group, links to FAQs about the group, or related groups. |

</details>

| First Name | `firstName` | string |  | ✓ | e.g. e.g. Nathan |  |
| Last Name | `lastName` | string |  | ✓ | e.g. e.g. Smith |  |
| Password | `password` | string |  | ✓ | Stores the password for the user account. A minimum of 8 characters is required. The maximum length is 100 characters. |  |
| Username | `username` | string |  | ✗ | The username that will be set to the user. Example: If you domain is example.com and you set the username to n.smith then the user's final email address will be n.smith@example.com. | e.g. e.g. n.smith |  |
| Domain Name or ID | `domain` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✓ | Whether the user is forced to change their password at next login | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Change Password at Next Login | `changePasswordAtNextLogin` | boolean | False | Whether the user is forced to change their password at next login |
| Phones | `phoneUi` | fixedCollection | {} | The type of phone number |
| Secondary Emails | `emailUi` | fixedCollection | {} | The type of the email account |
| Roles | `roles` | multiOptions | [] | Select the roles you want to assign to the user |
| Custom Fields | `customFields` | fixedCollection | {} | Allows editing and adding of custom fields |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Group | `groupId` | list |  | ✓ | Select the group to perform the operation on | e.g. e.g. 0123kx3o1habcdf |  |
| User | `userId` | resourceLocator |  | ✓ | Select the user to perform the operation on | e.g. e.g. sales@example.com |  |

### Add to Group parameters (`addToGroup`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User | `userId` | resourceLocator |  | ✓ | Select the user to perform the operation on | e.g. e.g. sales@example.com |  |
| Group | `groupId` | resourceLocator |  | ✓ | Select the group to perform the operation on | e.g. e.g. 0123kx3o1habcdf |  |

### Remove From Group parameters (`removeFromGroup`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User | `userId` | resourceLocator |  | ✓ | Select the user to perform the operation on | e.g. e.g. sales@example.com |  |
| Group | `groupId` | resourceLocator |  | ✓ | Select the group to perform the operation on | e.g. e.g. 0123kx3o1habcdf |  |

---

## Load Options Methods

- `getDomains`
- `domainName`

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Get Many

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "group",
  "operation": "getAll",
  "returnAll": true,
  "filter": {}
}
```

**Credentials:**
- gSuiteAdminOAuth2Api: `Google Workspace Admin account`

### Example 2: Delete Group

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "group",
  "operation": "delete",
  "groupId": {
    "__rl": true,
    "value": "01302m922pmp3e4",
    "mode": "list",
    "cachedResultName": "new2"
  }
}
```

**Credentials:**
- gSuiteAdminOAuth2Api: `Google Workspace Admin account`

### Example 3: Update Group

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "group",
  "operation": "update",
  "groupId": {
    "__rl": true,
    "value": "01302m922p525286",
    "mode": "list",
    "cachedResultName": "new"
  },
  "updateFields": {
    "description": "new1",
    "email": "new3@example.com",
    "name": "new2"
  }
}
```

**Credentials:**
- gSuiteAdminOAuth2Api: `Google Workspace Admin account`

### Example 4: Get Group

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "group",
  "operation": "get",
  "groupId": {
    "__rl": true,
    "value": "01302m922pmp3e4",
    "mode": "list",
    "cachedResultName": "new2"
  }
}
```

**Credentials:**
- gSuiteAdminOAuth2Api: `Google Workspace Admin account`

### Example 5: Create Group

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "group",
  "name": "Test",
  "email": "NewOnes22@example.com",
  "additionalFields": {
    "description": "test"
  }
}
```

**Credentials:**
- gSuiteAdminOAuth2Api: `Google Workspace Admin account`


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
* Categories: Utility
* Aliases: Workspaces

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: gSuiteAdmin
displayName: Google Workspace Admin
description: Consume Google Workspace Admin API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: gSuiteAdminOAuth2Api
  required: true
operations:
- id: get
  name: Get
  description: Get a ChromeOS device
  params:
  - id: deviceId
    name: Device
    type: resourceLocator
    default: ''
    required: true
    description: Select the device you want to retrieve
    hint: Enter the device id
    placeholder: e.g. 123e4567-e89b-12d3-a456-426614174000
    validation: &id015
      required: true
      displayOptions:
        show:
          operation:
          - get
          - update
          - changeStatus
          resource:
          - device
    typeInfo: &id016
      type: resourceLocator
      displayName: Device
      name: deviceId
  - id: projection
    name: Output
    type: options
    default: basic
    required: true
    description: Do not include any custom fields for the user
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - user
    typeInfo: &id002
      type: options
      displayName: Custom Fields
      name: projection
      possibleValues:
      - value: basic
        name: Don't Include
        description: Do not include any custom fields for the user
      - value: custom
        name: Custom
        description: Include custom fields from schemas requested in Custom Schema
          Names or IDs
      - value: full
        name: Include All
        description: Include all fields associated with this user
  - id: groupId
    name: Group
    type: list
    default: ''
    required: true
    description: Select the group to perform the operation on
    placeholder: e.g. 0123kx3o1habcdf
    validation: &id017
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - addToGroup
          - removeFromGroup
    typeInfo: &id018
      type: resourceLocator
      displayName: Group
      name: groupId
  - id: userId
    name: User
    type: resourceLocator
    default: ''
    required: true
    description: Select the user to perform the operation on
    hint: Enter the user email
    placeholder: e.g. sales@example.com
    validation: &id019
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - addToGroup
          - delete
          - get
          - removeFromGroup
          - update
    typeInfo: &id020
      type: resourceLocator
      displayName: User
      name: userId
  - id: output
    name: Output
    type: options
    default: simplified
    required: true
    description: 'Only return specific fields: kind, ID, primaryEmail, name (with
      subfields), isAdmin, lastLoginTime, creationTime, and suspended'
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - user
    typeInfo: &id010
      type: options
      displayName: Output
      name: output
      possibleValues:
      - value: simplified
        name: Simplified
        description: 'Only return specific fields: kind, ID, primaryEmail, name (with
          subfields), isAdmin, lastLoginTime, creationTime, and suspended'
      - value: raw
        name: Raw
        description: Return all fields from the API response
      - value: select
        name: Select Included Fields
        description: Choose specific fields to include
  - id: fields
    name: Fields
    type: multiOptions
    default: []
    required: false
    description: Fields to include in the response when "Select Included Fields" is
      chosen
    validation: &id011
      displayOptions:
        show:
          output:
          - select
          operation:
          - getAll
          resource:
          - user
    typeInfo: &id012
      type: multiOptions
      displayName: Fields
      name: fields
      possibleValues:
      - value: creationTime
        name: Creation Time
        description: ''
      - value: isAdmin
        name: Is Admin
        description: ''
      - value: kind
        name: Kind
        description: ''
      - value: lastLoginTime
        name: Last Login Time
        description: ''
      - value: name
        name: Name
        description: ''
      - value: primaryEmail
        name: Primary Email
        description: ''
      - value: suspended
        name: Suspended
        description: ''
  - id: projection
    name: Custom Fields
    type: options
    default: basic
    required: true
    description: Do not include any custom fields for the user
    validation: *id001
    typeInfo: *id002
  - id: customFieldMask
    name: Custom Schema Names or IDs
    type: multiOptions
    default: []
    required: true
    description: A comma-separated list of schema names. All fields from these schemas
      are fetched. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id013
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - user
    typeInfo: &id014
      type: multiOptions
      displayName: Custom Schema Names or IDs
      name: customFieldMask
      typeOptions:
        loadOptionsMethod: getSchemas
      possibleValues: []
- id: getAll
  name: Get Many
  description: Get many ChromeOS devices
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id003
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - user
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - user
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: projection
    name: Output
    type: options
    default: basic
    required: true
    description: Do not include any custom fields for the user
    validation: *id001
    typeInfo: *id002
  - id: includeChildOrgunits
    name: Include Children
    type: boolean
    default: false
    required: false
    description: Whether to include devices from organizational units below your specified
      organizational unit
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - device
    typeInfo:
      type: boolean
      displayName: Include Children
      name: includeChildOrgunits
  - id: sort
    name: Sort
    type: fixedCollection
    default: {}
    required: false
    description: Field to sort the results by
    placeholder: Add Sort Rule
    validation: &id007
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - user
    typeInfo: &id008
      type: fixedCollection
      displayName: Sort
      name: sort
      subProperties:
      - name: sortRules
        displayName: Sort Rules
        values:
        - displayName: Order By
          name: orderBy
          type: options
          description: Field to sort the results by
          value: email
          default: ''
          options:
          - name: Email
            value: email
            displayName: Email
          - name: Family Name
            value: familyName
            displayName: Family Name
          - name: Given Name
            value: givenName
            displayName: Given Name
        - displayName: Sort Order
          name: sortOrder
          type: options
          description: Sort order direction
          value: ASCENDING
          default: ASCENDING
          options:
          - name: Ascending
            value: ASCENDING
            displayName: Ascending
          - name: Descending
            value: DESCENDING
            displayName: Descending
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: sort
    name: Sort
    type: fixedCollection
    default: {}
    required: false
    description: Field to sort the results by
    placeholder: Add Sort Rule
    validation: *id007
    typeInfo: *id008
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: output
    name: Output
    type: options
    default: simplified
    required: true
    description: 'Only return specific fields: kind, ID, primaryEmail, name (with
      subfields), isAdmin, lastLoginTime, creationTime, and suspended'
    validation: *id009
    typeInfo: *id010
  - id: fields
    name: Fields
    type: multiOptions
    default: []
    required: false
    description: Fields to include in the response when "Select Included Fields" is
      chosen
    validation: *id011
    typeInfo: *id012
  - id: projection
    name: Custom Fields
    type: options
    default: basic
    required: true
    description: Do not include any custom fields for the user
    validation: *id001
    typeInfo: *id002
  - id: customFieldMask
    name: Custom Schema Names or IDs
    type: multiOptions
    default: []
    required: true
    description: A comma-separated list of schema names. All fields from these schemas
      are fetched. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id013
    typeInfo: *id014
  - id: sort
    name: Sort
    type: fixedCollection
    default: {}
    required: false
    description: Field to sort the results by
    placeholder: Add Sort Rule
    validation: *id007
    typeInfo: *id008
- id: update
  name: Update
  description: Update a ChromeOS device
  params:
  - id: deviceId
    name: Device
    type: resourceLocator
    default: ''
    required: true
    description: Select the device you want to retrieve
    hint: Enter the device id
    placeholder: e.g. 123e4567-e89b-12d3-a456-426614174000
    validation: *id015
    typeInfo: *id016
  - id: groupId
    name: Group
    type: list
    default: ''
    required: true
    description: Select the group to perform the operation on
    placeholder: e.g. 0123kx3o1habcdf
    validation: *id017
    typeInfo: *id018
  - id: userId
    name: User
    type: resourceLocator
    default: ''
    required: true
    description: Select the user to perform the operation on
    hint: Enter the user email
    placeholder: e.g. sales@example.com
    validation: *id019
    typeInfo: *id020
- id: changeStatus
  name: Change Status
  description: Change the status of a ChromeOS device
  params:
  - id: deviceId
    name: Device
    type: resourceLocator
    default: ''
    required: true
    description: Select the device you want to retrieve
    hint: Enter the device id
    placeholder: e.g. 123e4567-e89b-12d3-a456-426614174000
    validation: *id015
    typeInfo: *id016
  - id: action
    name: Status
    type: options
    default: reenable
    required: true
    description: Re-enable a disabled chromebook
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - changeStatus
          resource:
          - device
    typeInfo:
      type: options
      displayName: Status
      name: action
      possibleValues:
      - value: reenable
        name: Enabled
        description: Re-enable a disabled chromebook
      - value: disable
        name: Disabled
        description: Disable a chromebook
- id: create
  name: Create
  description: Create a group
  params:
  - id: name
    name: Group Name
    type: string
    default: ''
    required: false
    description: The group's display name
    placeholder: e.g. Sales
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - group
    typeInfo:
      type: string
      displayName: Group Name
      name: name
  - id: email
    name: Group Email
    type: string
    default: ''
    required: true
    description: The group's email address. If your account has multiple domains,
      select the appropriate domain for the email address. The email must be unique
    placeholder: e.g. sales@example.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - create
          resource:
          - group
    typeInfo:
      type: string
      displayName: Group Email
      name: email
  - id: firstName
    name: First Name
    type: string
    default: ''
    required: true
    description: ''
    placeholder: e.g. Nathan
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - user
    typeInfo:
      type: string
      displayName: First Name
      name: firstName
  - id: lastName
    name: Last Name
    type: string
    default: ''
    required: true
    description: ''
    placeholder: e.g. Smith
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - user
    typeInfo:
      type: string
      displayName: Last Name
      name: lastName
  - id: password
    name: Password
    type: string
    default: ''
    required: true
    description: Stores the password for the user account. A minimum of 8 characters
      is required. The maximum length is 100 characters.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - user
    typeInfo:
      type: string
      displayName: Password
      name: password
      typeOptions:
        password: true
  - id: username
    name: Username
    type: string
    default: ''
    required: false
    description: 'The username that will be set to the user. Example: If you domain
      is example.com and you set the username to n.smith then the user''s final email
      address will be n.smith@example.com.'
    placeholder: e.g. n.smith
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - user
    typeInfo:
      type: string
      displayName: Username
      name: username
  - id: domain
    name: Domain Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - user
    typeInfo:
      type: options
      displayName: Domain Name or ID
      name: domain
      typeOptions:
        loadOptionsMethod: getDomains
      possibleValues: []
- id: delete
  name: Delete
  description: Delete a group
  params:
  - id: groupId
    name: Group
    type: list
    default: ''
    required: true
    description: Select the group to perform the operation on
    placeholder: e.g. 0123kx3o1habcdf
    validation: *id017
    typeInfo: *id018
  - id: userId
    name: User
    type: resourceLocator
    default: ''
    required: true
    description: Select the user to perform the operation on
    hint: Enter the user email
    placeholder: e.g. sales@example.com
    validation: *id019
    typeInfo: *id020
- id: addToGroup
  name: Add to Group
  description: Add an existing user to a group
  params:
  - id: userId
    name: User
    type: resourceLocator
    default: ''
    required: true
    description: Select the user to perform the operation on
    hint: Enter the user email
    placeholder: e.g. sales@example.com
    validation: *id019
    typeInfo: *id020
  - id: groupId
    name: Group
    type: resourceLocator
    default: ''
    required: true
    description: Select the group to perform the operation on
    placeholder: e.g. 0123kx3o1habcdf
    validation: *id017
    typeInfo: *id018
- id: removeFromGroup
  name: Remove From Group
  description: Remove a user from a group
  params:
  - id: userId
    name: User
    type: resourceLocator
    default: ''
    required: true
    description: Select the user to perform the operation on
    hint: Enter the user email
    placeholder: e.g. sales@example.com
    validation: *id019
    typeInfo: *id020
  - id: groupId
    name: Group
    type: resourceLocator
    default: ''
    required: true
    description: Select the group to perform the operation on
    placeholder: e.g. 0123kx3o1habcdf
    validation: *id017
    typeInfo: *id018
examples:
- name: Get Many
  parameters:
    resource: group
    operation: getAll
    returnAll: true
    filter: {}
  workflow: Unnamed workflow
- name: Delete Group
  parameters:
    resource: group
    operation: delete
    groupId:
      __rl: true
      value: 01302m922pmp3e4
      mode: list
      cachedResultName: new2
  workflow: Unnamed workflow
- name: Update Group
  parameters:
    resource: group
    operation: update
    groupId:
      __rl: true
      value: 01302m922p525286
      mode: list
      cachedResultName: new
    updateFields:
      description: new1
      email: new3@example.com
      name: new2
  workflow: Unnamed workflow
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
  - field: deviceId
    text: e.g. 123e4567-e89b-12d3-a456-426614174000
  - field: filter
    text: Add Filter
  - field: sort
    text: Add Sort Rule
  - field: updateOptions
    text: Add Option
  - field: groupId
    text: e.g. 0123kx3o1habcdf
  - field: name
    text: e.g. Sales
  - field: email
    text: e.g. sales@example.com
  - field: additionalFields
    text: Add Field
  - field: filter
    text: Add Filter
  - field: sort
    text: Add Sort Rule
  - field: updateFields
    text: Add Field
  - field: userId
    text: e.g. sales@example.com
  - field: groupId
    text: e.g. 0123kx3o1habcdf
  - field: firstName
    text: e.g. Nathan
  - field: lastName
    text: e.g. Smith
  - field: username
    text: e.g. n.smith
  - field: additionalFields
    text: Add Field
  - field: filter
    text: Add Filter
  - field: sort
    text: Add Sort Rule
  - field: updateFields
    text: Add Field
  hints:
  - field: deviceId
    text: Enter the device id
  - field: userId
    text: Enter the user email
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
  "$id": "https://n8n.io/schemas/nodes/gSuiteAdmin.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Workspace Admin Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll",
        "update",
        "changeStatus",
        "create",
        "delete",
        "addToGroup",
        "removeFromGroup"
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
            "device",
            "group",
            "user"
          ],
          "default": "user"
        },
        "operation": {
          "description": "Add an existing user to a group",
          "type": "string",
          "enum": [
            "addToGroup",
            "create",
            "delete",
            "get",
            "getAll",
            "removeFromGroup",
            "update"
          ],
          "default": "create"
        },
        "deviceId": {
          "description": "Select the device you want to retrieve",
          "type": "string",
          "examples": [
            "e.g. 123e4567-e89b-12d3-a456-426614174000"
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
          "default": 100
        },
        "projection": {
          "description": "Do not include any custom fields for the user",
          "type": "string",
          "enum": [
            "basic",
            "custom",
            "full"
          ],
          "default": "basic"
        },
        "includeChildOrgunits": {
          "description": "Whether to include devices from organizational units below your specified organizational unit",
          "type": "boolean",
          "default": false
        },
        "filter": {
          "description": "The unique ID for the customer's Google Workspace account",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "sort": {
          "description": "Field to sort the results by",
          "type": "string",
          "default": {},
          "examples": [
            "Add Sort Rule"
          ]
        },
        "updateOptions": {
          "description": "The full path to the organizational unit. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Option"
          ]
        },
        "action": {
          "description": "Re-enable a disabled chromebook",
          "type": "string",
          "enum": [
            "reenable",
            "disable"
          ],
          "default": "reenable"
        },
        "groupId": {
          "description": "Select the group to perform the operation on",
          "type": "string",
          "examples": [
            "e.g. 0123kx3o1habcdf"
          ]
        },
        "name": {
          "description": "The group's display name",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Sales"
          ]
        },
        "email": {
          "description": "The group's email address. If your account has multiple domains, select the appropriate domain for the email address. The email must be unique",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "e.g. sales@example.com"
          ]
        },
        "additionalFields": {
          "description": "Whether the user is forced to change their password at next login",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "Whether user is archived",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "userId": {
          "description": "Select the user to perform the operation on",
          "type": "string",
          "examples": [
            "e.g. sales@example.com"
          ]
        },
        "firstName": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Nathan"
          ]
        },
        "lastName": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Smith"
          ]
        },
        "password": {
          "description": "Stores the password for the user account. A minimum of 8 characters is required. The maximum length is 100 characters.",
          "type": "string",
          "default": ""
        },
        "username": {
          "description": "The username that will be set to the user. Example: If you domain is example.com and you set the username to n.smith then the user's final email address will be n.smith@example.com.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. n.smith"
          ]
        },
        "domain": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "output": {
          "description": "Only return specific fields: kind, ID, primaryEmail, name (with subfields), isAdmin, lastLoginTime, creationTime, and suspended",
          "type": "string",
          "enum": [
            "simplified",
            "raw",
            "select"
          ],
          "default": "simplified"
        },
        "fields": {
          "description": "Fields to include in the response when \"Select Included Fields\" is chosen",
          "type": "string",
          "default": []
        },
        "customFieldMask": {
          "description": "A comma-separated list of schema names. All fields from these schemas are fetched. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
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
      "name": "gSuiteAdminOAuth2Api",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Get Many",
      "value": {
        "resource": "group",
        "operation": "getAll",
        "returnAll": true,
        "filter": {}
      }
    },
    {
      "description": "Delete Group",
      "value": {
        "resource": "group",
        "operation": "delete",
        "groupId": {
          "__rl": true,
          "value": "01302m922pmp3e4",
          "mode": "list",
          "cachedResultName": "new2"
        }
      }
    },
    {
      "description": "Update Group",
      "value": {
        "resource": "group",
        "operation": "update",
        "groupId": {
          "__rl": true,
          "value": "01302m922p525286",
          "mode": "list",
          "cachedResultName": "new"
        },
        "updateFields": {
          "description": "new1",
          "email": "new3@example.com",
          "name": "new2"
        }
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
