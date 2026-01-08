---
title: "Node: Pipedrive"
slug: "node-pipedrive"
version: "1"
updated: "2026-01-08"
summary: "Create and edit data in Pipedrive"
node_type: "regular"
group: "['transform']"
---

# Node: Pipedrive

**Purpose.** Create and edit data in Pipedrive
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:pipedrive.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **pipedriveApi**: N/A
- **pipedriveOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `pipedriveApi` | ✓ | {'show': {'authentication': ['apiToken']}} |
| `pipedriveOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Activity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an activity |
| Delete | `delete` | Delete an activity |
| Get | `get` | Get data of an activity |
| Get Many | `getAll` | Get data of many activities |
| Update | `update` | Update an activity |

### Deal Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a deal |
| Delete | `delete` | Delete a deal |
| Duplicate | `duplicate` | Duplicate a deal |
| Get | `get` | Get data of a deal |
| Get Many | `getAll` | Get data of many deals |
| Search | `search` | Search a deal |
| Update | `update` | Update a deal |

### Dealactivity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many activities of a deal |

### Dealproduct Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a product to a deal |
| Get Many | `getAll` | Get many products in a deal |
| Remove | `remove` | Remove a product from a deal |
| Update | `update` | Update a product in a deal |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a file |
| Delete | `delete` | Delete a file |
| Download | `download` | Download a file |
| Get | `get` | Get data of a file |
| Update | `update` | Update file details |
| Get All | `getAll` | Get data of all file |

### Lead Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a lead |
| Delete | `delete` | Delete a lead |
| Get | `get` | Get data of a lead |
| Get Many | `getAll` | Get data of many leads |
| Update | `update` | Update a lead |

### Note Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a note |
| Delete | `delete` | Delete a note |
| Get | `get` | Get data of a note |
| Get Many | `getAll` | Get data of many notes |
| Update | `update` | Update a note |

### Organization Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an organization |
| Delete | `delete` | Delete an organization |
| Get | `get` | Get data of an organization |
| Get Many | `getAll` | Get data of many organizations |
| Search | `search` | Search organizations |
| Update | `update` | Update an organization |

### Person Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a person |
| Delete | `delete` | Delete a person |
| Get | `get` | Get data of a person |
| Get Many | `getAll` | Get data of many persons |
| Search | `search` | Search all persons |
| Update | `update` | Update a person |

### Product Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get data of many products |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | deal | ✗ | Resource to operate on |  |

**Resource options:**

* **Activity** (`activity`)
* **Deal** (`deal`)
* **Deal Activity** (`dealActivity`)
* **Deal Product** (`dealProduct`)
* **File** (`file`)
* **Lead** (`lead`)
* **Note** (`note`)
* **Organization** (`organization`)
* **Person** (`person`)
* **Product** (`product`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create an activity |  |

**Operation options:**

* **Create** (`create`) - Create an activity
* **Delete** (`delete`) - Delete an activity
* **Get** (`get`) - Get data of an activity
* **Get Many** (`getAll`) - Get data of many activities
* **Update** (`update`) - Update an activity

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Subject | `subject` | string |  | ✓ | The subject of the activity to create |  |
| Done | `done` | options | 0 | ✗ | Whether the activity is done or not |  |

**Done options:**

* **Not Done** (`0`)
* **Done** (`1`)

| Type | `type` | string |  | ✓ | Type of the activity like "call", "meeting", etc | e.g. call |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the deal this activity will be associated with | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Deal ID | `deal_id` | number | 0 | ID of the deal this activity will be associated with |
| Due Date | `due_date` | dateTime |  | Due Date to activity be done YYYY-MM-DD |
| Note | `note` | string |  | Note of the activity (HTML format) |
| Organization Name or ID | `org_id` | options |  | ID of the organization this activity will be associated with. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Person ID | `person_id` | number | 0 | ID of the person this activity will be associated with |
| User Name or ID | `user_id` | options |  | ID of the active user whom the activity will be assigned to. If omitted, the activity will be assigned to the authorized user. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Custom Properties | `customProperties` | fixedCollection | {} | Adds a custom property to set also values which have not been predefined |

</details>

| Title | `title` | string |  | ✓ | The title of the deal to create |  |
| Associate With | `associateWith` | options | organization | ✓ | Type of entity to link to this deal |  |

**Associate With options:**

* **Organization** (`organization`)
* **Person** (`person`)

| Organization ID | `org_id` | number | 0 | ✓ | ID of the organization this deal will be associated with |  |
| Person ID | `person_id` | number | 0 | ✗ | ID of the person this deal will be associated with |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Currency of the deal. Accepts a 3-character currency code. Like EUR, USD, ... | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Currency | `currency` | string | USD | Currency of the deal. Accepts a 3-character currency code. Like EUR, USD, ... |
| Custom Properties | `customProperties` | fixedCollection | {} | Adds a custom property to set also values which have not been predefined |
| Label Name or ID | `label` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Lost Reason | `lost_reason` | string |  | Reason why the deal was lost |
| Organization ID | `org_id` | number | 0 | ID of the organization this deal will be associated with |
| Person ID | `person_id` | number | 0 | ID of the person this deal will be associated with |
| Probability | `probability` | number | 0 | Deal success probability percentage |
| Stage Name or ID | `stage_id` | options |  | ID of the stage this deal will be placed in a pipeline. If omitted, the deal will be placed in the first stage of the default pipeline. (PIPELINE > STAGE). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Status | `status` | options | open | The status of the deal. If not provided it will automatically be set to "open". |
| User Name or ID | `user_id` | options |  | ID of the active user whom the activity will be assigned to. If omitted, the activity will be assigned to the authorized user. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Value | `value` | number | 0 | Value of the deal. If not set it will automatically be set to 0. |
| Visible To | `visible_to` | options | 3 | Visibility of the deal. If omitted, visibility will be set to the default visibility setting of this item type for the authorized user. |

</details>

| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be written |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the activite this file will be associated with | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Activity ID | `activity_id` | number | 0 | ID of the activite this file will be associated with |
| Deal ID | `deal_id` | number | 0 | ID of the deal this file will be associated with |
| Organization Name or ID | `org_id` | options |  | ID of the organization this deal will be associated with. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Person ID | `person_id` | number | 0 | ID of the person this file will be associated with |
| Product ID | `product_id` | number | 0 | ID of the person this file will be associated with |

</details>

| Title | `title` | string |  | ✓ | Name of the lead to create |  |
| Associate With | `associateWith` | options | organization | ✓ | Type of entity to link to this lead |  |

**Associate With options:**

* **Organization** (`organization`)
* **Person** (`person`)

| Organization ID | `organization_id` | number | 0 | ✓ | ID of the organization to link to this lead |  |
| Person ID | `person_id` | number | 0 | ✓ | ID of the person to link to this lead |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Date when the lead’s deal is expected to be closed, in ISO-8601 format | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Expected Close Date | `expected_close_date` | dateTime |  | Date when the lead’s deal is expected to be closed, in ISO-8601 format |
| Label Names or IDs | `label_ids` | multiOptions | [] | ID of the labels to attach to the lead to create. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Organization ID | `organization_id` | number | 0 | ID of the organization to link to this lead |
| Owner Name or ID | `owner_id` | options |  | ID of the user who will own the lead to create. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Person ID | `person_id` | number | 0 | ID of the person to link to this lead |
| Value | `value` | fixedCollection | {} | Potential monetary value associated with the lead |

</details>

| Content | `content` | string |  | ✓ | The content of the note to create |  |
| Name | `name` | string |  | ✓ | The name of the organization to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Adds a custom property to set also values which have not been predefined | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Properties | `customProperties` | fixedCollection | {} | Adds a custom property to set also values which have not been predefined |
| Label Name or ID | `label` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Visible To | `visible_to` | options | 3 | Visibility of the person. If omitted, visibility will be set to the default visibility setting of this item type for the authorized user. |

</details>

| Name | `name` | string |  | ✓ | The name of the person to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Adds a custom property to set also values which have not been predefined | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Properties | `customProperties` | fixedCollection | {} | Adds a custom property to set also values which have not been predefined |
| Email | `email` | string |  | Email of the person |
| Label Name or ID | `label` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Marketing Status | `marketing_status` | options | subscribed | Please be aware that it is only allowed once to change the marketing status from an old status to a new one |
| Organization Name or ID | `org_id` | options |  | ID of the organization this deal will be associated with. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone | `phone` | string |  | Phone number of the person |
| Visible To | `visible_to` | options | 3 | Visibility of the person. If omitted, visibility will be set to the default visibility setting of this item type for the authorized user. |
| User Name or ID | `owner_id` | options |  | ID of the User this deal will be associated with. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the deal this note will be associated with | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Deal ID | `deal_id` | number | 0 | ID of the deal this note will be associated with |
| Lead ID | `lead_id` | number | 0 | ID of the lead this note will be associated with |
| Organization Name or ID | `org_id` | options |  | ID of the organization this deal will be associated with. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Person ID | `person_id` | number | 0 | ID of the person this note will be associated with |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Activity ID | `activityId` | number | 0 | ✓ | ID of the activity to delete |  |
| Deal ID | `dealId` | number | 0 | ✓ | ID of the deal to delete |  |
| File ID | `fileId` | number | 0 | ✓ | ID of the file to delete |  |
| Lead ID | `leadId` | string |  | ✓ | ID of the lead to delete |  |
| Note ID | `noteId` | number | 0 | ✓ | ID of the note to delete |  |
| Organization ID | `organizationId` | number | 0 | ✓ | ID of the organization to delete |  |
| Person ID | `personId` | number | 0 | ✓ | ID of the person to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Activity ID | `activityId` | number | 0 | ✓ | ID of the activity to get |  |
| Deal ID | `dealId` | number | 0 | ✓ | ID of the deal to get |  |
| File ID | `fileId` | number | 0 | ✓ | ID of the file to get |  |
| Lead ID | `leadId` | string |  | ✓ | ID of the lead to retrieve |  |
| Note ID | `noteId` | number | 0 | ✓ | ID of the note to get |  |
| Organization ID | `organizationId` | number | 0 | ✓ | ID of the organization to get |  |
| Person ID | `personId` | number | 0 | ✓ | ID of the person to get |  |
| Resolve Properties | `resolveProperties` | boolean | False | ✗ | By default do custom properties get returned only as ID instead of their actual name. Also option fields contain only the ID instead of their actual value. If this option gets set they get automatically resolved. |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Deal Name or ID | `dealId` | options |  | ✓ | The ID of the deal whose products to retrieve. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Resolve Properties | `resolveProperties` | boolean | False | ✗ | By default do custom properties get returned only as ID instead of their actual name. Also option fields contain only the ID instead of their actual value. If this option gets set they get automatically resolved. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Deal Name or ID | `dealId` | options |  | ✓ | The ID of the deal whose activity to retrieve. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether the activity is done or not | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Done | `done` | boolean | False | Whether the activity is done or not |
| Exclude Activity IDs | `exclude` | string |  | A comma-separated Activity IDs, to exclude from result. Ex. 4, 9, 11, ... |

</details>

| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Archived Status | `archived_status` | options | all |  |

</details>

| Filters | `filters` | collection | {} | ✗ | If supplied, only organizations whose name starts with the specified letter will be returned | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| First Char | `firstChar` | string |  | If supplied, only organizations whose name starts with the specified letter will be returned |
| Predefined Filter Name or ID | `filterId` | options |  | ID of the filter to use. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the filter to use. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Predefined Filter Name or ID | `filterId` | options |  | ID of the filter to use. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| First Char | `firstChar` | string |  | If supplied, only persons whose name starts with the specified letter will be returned |
| Sort | `sort` | string |  | The field names and sorting mode separated by a comma (field_name_1 ASC, field_name_2 DESC). Only first-level field keys are supported (no nested keys). |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the deal this note will be associated with | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Deal ID | `deal_id` | number | 0 | ID of the deal this note will be associated with |
| Lead ID | `lead_id` | number | 0 | ID of the lead this note will be associated with |
| Organization Name or ID | `org_id` | options |  | ID of the organization this deal will be associated with. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Person ID | `person_id` | number | 0 | ID of the person this note will be associated with |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether the Activity is done or not. 0 = Not done, 1 = Done. If omitted returns both Done and Not done activities. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Done | `done` | boolean | False | Whether the Activity is done or not. 0 = Not done, 1 = Done. If omitted returns both Done and Not done activities. |
| End Date | `end_date` | dateTime |  | Use the Activity due date where you wish to stop fetching Activities from. Insert due date in YYYY-MM-DD format. |
| Predefined Filter Name or ID | `filterId` | options |  | The ID of the Filter to use (will narrow down results if used together with user_id parameter). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Star Date | `start_date` | dateTime |  | Use the Activity due date where you wish to begin fetching Activities from. Insert due date in YYYY-MM-DD format. |
| Type Names or IDs | `type` | multiOptions | [] | Type of the Activity. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| User Name or ID | `user_id` | options |  | The ID of the User whose Activities will be fetched. If omitted, the User associated with the API token will be used. If 0, Activities for all company Users will be fetched based on the permission sets. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Filters | `filters` | collection | {} | ✗ | Predefined filter to apply to the deals to retrieve. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Predefined Filter Name or ID | `filter_id` | options |  | Predefined filter to apply to the deals to retrieve. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Stage Name or ID | `stage_id` | options |  | ID of the stage to filter deals by. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Status | `status` | options | all_not_deleted | Status to filter deals by. Defaults to <code>all_not_deleted</code> |
| User Name or ID | `user_id` | options |  | ID of the user to filter deals by. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Activity ID | `activityId` | number | 0 | ✓ | ID of the activity to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Whether the user is set to busy during the activity | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Busy Flag | `busy_flag` | boolean | False | Whether the user is set to busy during the activity |
| Deal ID | `deal_id` | number | 0 | ID of the deal this activity will be associated with |
| Due Date | `due_date` | dateTime |  | Due Date to activity be done YYYY-MM-DD |
| Done | `done` | options | 0 | Whether the activity is done or not |
| Note | `note` | string |  | Note of the activity (HTML format) |
| Organization Name or ID | `org_id` | options |  | ID of the organization this activity will be associated with. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Person ID | `person_id` | number | 0 | ID of the person this activity will be associated with |
| Public Description | `public_description` | string |  | Additional details about the activity that is synced to your external calendar |
| Subject | `subject` | string |  | The subject of the activity |
| Type | `type` | string |  | Type of the activity like "call", "meeting", etc |
| User Name or ID | `user_id` | options |  | ID of the active user whom the activity will be assigned to. If omitted, the activity will be assigned to the authorized user. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Custom Properties | `customProperties` | fixedCollection | {} | Adds a custom property to set also values which have not been predefined |

</details>

| Deal ID | `dealId` | number | 0 | ✓ | ID of the deal to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Currency of the deal. Accepts a 3-character currency code. Like EUR, USD, ... | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Currency | `currency` | string | USD | Currency of the deal. Accepts a 3-character currency code. Like EUR, USD, ... |
| Custom Properties | `customProperties` | fixedCollection | {} | Adds a custom property to set also values which have not been predefined |
| User Name or ID | `user_id` | options |  | ID of the active user whom the activity will be assigned to. If omitted, the activity will be assigned to the authorized user. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Label Name or ID | `label` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Lost Reason | `lost_reason` | string |  | Reason why the deal was lost |
| Organization Name or ID | `org_id` | options |  | ID of the organization this deal will be associated with. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Person ID | `person_id` | number | 0 | ID of the person this deal will be associated with |
| Probability | `probability` | number | 0 | Deal success probability percentage |
| Stage Name or ID | `stage_id` | options |  | ID of the stage this deal will be placed in a pipeline. If omitted, the deal will be placed in the first stage of the default pipeline. (PIPELINE > STAGE). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Status | `status` | options | open | The status of the deal. If not provided it will automatically be set to "open". |
| Title | `title` | string |  | The title of the deal |
| Value | `value` | number | 0 | Value of the deal. If not set it will automatically be set to 0. |
| Visible To | `visible_to` | options | 3 | Visibility of the deal. If omitted, visibility will be set to the default visibility setting of this item type for the authorized user. |

</details>

| Deal Name or ID | `dealId` | options |  | ✓ | The ID of the deal whose product to update. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Product Attachment Name or ID | `productAttachmentId` | options |  | ✓ | ID of the deal-product (the ID of the product attached to the deal). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Text to describe this product-deal attachment | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Comments | `comments` | string |  | Text to describe this product-deal attachment |
| Discount Percentage | `discount_percentage` | number | 0 | Percentage of discount to apply |
| Item Price | `item_price` | number | 0 | Price at which to add or update this product in a deal |
| Quantity | `quantity` | number | 1 | How many items of this product to add/update in a deal |
| Product Variation ID | `product_variation_id` | string |  | ID of the product variation to use |

</details>

| File ID | `fileId` | number | 0 | ✓ | ID of the file to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The updated visible name of the file | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | The updated visible name of the file |
| Description | `description` | string |  | The updated description of the file |

</details>

| Lead ID | `leadId` | string |  | ✓ | ID of the lead to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Name of the lead to update | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Title | `title` | string |  | Name of the lead to update |
| Owner Name or ID | `owner_id` | options |  | ID of the user who will own the lead to update. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Label Names or IDs | `label_ids` | multiOptions | [] | ID of the labels to attach to the lead to update. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Person Name or ID | `person_id` | options |  | ID of the person to link to this lead. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Value | `value` | fixedCollection | {} | Potential monetary value associated with the lead |
| Expected Close Date | `expected_close_date` | dateTime |  | Date when the lead’s deal is expected to be closed, in ISO-8601 format |

</details>

| Note ID | `noteId` | number | 0 | ✓ | ID of the note to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The content of the note | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content | `content` | string |  | The content of the note |
| Deal ID | `deal_id` | number | 0 | ID of the deal this note will be associated with |
| Lead ID | `lead_id` | number | 0 | ID of the lead this note will be associated with |
| Organization Name or ID | `org_id` | options |  | ID of the organization this deal will be associated with. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Person ID | `person_id` | number | 0 | ID of the person this note will be associated with |

</details>

| Organization ID | `organizationId` | number |  | ✓ | The ID of the organization to create |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Adds a custom property to set also values which have not been predefined | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Properties | `customProperties` | fixedCollection | {} | Adds a custom property to set also values which have not been predefined |
| Label Name or ID | `label` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Name | `name` | string |  | Organization name |
| Owner ID | `owner_id` | number | 0 | The ID of the user who will be marked as the owner of this Organization. When omitted, the authorized User ID will be used. |
| Visible To | `visible_to` | options | 3 | Visibility of the person. If omitted, visibility will be set to the default visibility setting of this item type for the authorized user. |

</details>

| Person ID | `personId` | number | 0 | ✓ | ID of the person to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The fields to update | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Properties | `customProperties` | fixedCollection | {} | Adds a custom property to set also values which have not been predefined |
| Email | `email` | string |  | Email of the person |
| Label Name or ID | `label` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Marketing Status | `marketing_status` | options | subscribed | Please be aware that it is only allowed once to change the marketing status from an old status to a new one |
| Name | `name` | string |  | The name of the person |
| Organization Name or ID | `org_id` | options |  | ID of the organization this deal will be associated with. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone | `phone` | string |  | Phone number of the person |
| User Name or ID | `owner_id` | options |  | ID of the User this person will be associated with. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Visible To | `visible_to` | options | 3 | Visibility of the deal. If omitted, visibility will be set to the default visibility setting of this item type for the authorized user. |

</details>

| Encode Properties | `encodeProperties` | boolean | False | ✗ | By default do custom properties have to be set as ID instead of their actual name. Also option fields have to be set as ID instead of their actual value. If this option gets set they get automatically encoded. |  |

### Duplicate parameters (`duplicate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Deal ID | `dealId` | number | 0 | ✓ | ID of the deal to duplicate |  |

### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Term | `term` | string |  | ✓ | The search term to look for. Minimum 2 characters (or 1 if using exact_match). |  |
| Exact Match | `exactMatch` | boolean | False | ✗ | Whether only full exact matches against the given term are returned. It is not case sensitive. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Supports including optional fields in the results which are not provided by default. Example: deal.cc_email. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Fields | `includeFields` | string |  | Supports including optional fields in the results which are not provided by default. Example: deal.cc_email. |
| Organization ID | `organizationId` | string |  | Will filter Deals by the provided Organization ID |
| Person ID | `personId` | string |  | Will filter Deals by the provided Person ID |
| Search Fields | `fields` | multiOptions |  | A comma-separated string array. The fields to perform the search from. Defaults to all of them. |
| Status | `status` | options | open | The status of the deal. If not provided it will automatically be set to "open". |

</details>

| Term | `term` | string |  | ✓ | The search term to look for. Minimum 2 characters (or 1 if using exact_match). |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether only full exact matches against the given term are returned. It is not case sensitive. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exact Match | `exactMatch` | boolean | False | Whether only full exact matches against the given term are returned. It is not case sensitive. |
| Fields | `fields` | multiOptions | [] | Fields to the search in. Defaults to all of them. |
| RAW Data | `rawData` | boolean | False | Whether to return the data exactly in the way it got received from the API |

</details>

| Term | `term` | string |  | ✓ | The search term to look for. Minimum 2 characters (or 1 if using exact_match). |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether only full exact matches against the given term are returned. It is not case sensitive. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exact Match | `exactMatch` | boolean | False | Whether only full exact matches against the given term are returned. It is not case sensitive. |
| Fields | `fields` | string |  | A comma-separated string array. The fields to perform the search from. Defaults to all of them. |
| Include Fields | `includeFields` | string |  | Supports including optional fields in the results which are not provided by default |
| Organization ID | `organizationId` | string |  | Will filter Deals by the provided Organization ID |
| RAW Data | `rawData` | boolean | False | Whether to return the data exactly in the way it got received from the API |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Deal Name or ID | `dealId` | options |  | ✓ | The ID of the deal to add a product to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Product Name or ID | `productId` | options |  | ✓ | The ID of the product to add to a deal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Item Price | `item_price` | number | 0 | ✓ | Price at which to add or update this product in a deal |  |
| Quantity | `quantity` | number | 1 | ✓ | How many items of this product to add/update in a deal | min:1, max:∞ |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Text to describe this product-deal attachment | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Comments | `comments` | string |  | Text to describe this product-deal attachment |
| Discount Percentage | `discount_percentage` | number | 0 | Percentage of discount to apply |
| Product Variation ID | `product_variation_id` | string |  | ID of the product variation to use |

</details>


### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Deal Name or ID | `dealId` | options |  | ✓ | The ID of the deal whose product to remove. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Product Attachment Name or ID | `productAttachmentId` | options |  | ✓ | ID of the deal-product (the ID of the product attached to the deal). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File ID | `fileId` | number | 0 | ✓ | ID of the file to download |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |

---

## Load Options Methods

- `getActivityTypes`

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
* Categories: Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: pipedrive
displayName: Pipedrive
description: Create and edit data in Pipedrive
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: pipedriveApi
  required: true
- name: pipedriveOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create an activity
  params:
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: The subject of the activity to create
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - activity
    typeInfo:
      type: string
      displayName: Subject
      name: subject
  - id: done
    name: Done
    type: options
    default: '0'
    required: false
    description: Whether the activity is done or not
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - activity
    typeInfo:
      type: options
      displayName: Done
      name: done
      possibleValues:
      - value: '0'
        name: Not Done
        description: ''
      - value: '1'
        name: Done
        description: ''
  - id: type
    name: Type
    type: string
    default: ''
    required: true
    description: Type of the activity like "call", "meeting", etc
    placeholder: call
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - activity
    typeInfo:
      type: string
      displayName: Type
      name: type
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The title of the deal to create
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - create
    typeInfo: &id002
      type: string
      displayName: Title
      name: title
  - id: associateWith
    name: Associate With
    type: options
    default: organization
    required: true
    description: Type of entity to link to this deal
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - create
    typeInfo: &id004
      type: options
      displayName: Associate With
      name: associateWith
      possibleValues:
      - value: organization
        name: Organization
        description: ''
      - value: person
        name: Person
        description: ''
  - id: org_id
    name: Organization ID
    type: number
    default: 0
    required: true
    description: ID of the organization this deal will be associated with
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - deal
          associateWith:
          - organization
    typeInfo:
      type: number
      displayName: Organization ID
      name: org_id
  - id: person_id
    name: Person ID
    type: number
    default: 0
    required: false
    description: ID of the person this deal will be associated with
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - create
          associateWith:
          - person
    typeInfo: &id006
      type: number
      displayName: Person ID
      name: person_id
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be written
    validation: &id033
      required: true
      displayOptions:
        show:
          operation:
          - download
          resource:
          - file
    typeInfo: &id034
      type: string
      displayName: Put Output File in Field
      name: binaryPropertyName
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Name of the lead to create
    validation: *id001
    typeInfo: *id002
  - id: associateWith
    name: Associate With
    type: options
    default: organization
    required: true
    description: Type of entity to link to this lead
    validation: *id003
    typeInfo: *id004
  - id: organization_id
    name: Organization ID
    type: number
    default: 0
    required: true
    description: ID of the organization to link to this lead
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - create
          associateWith:
          - organization
    typeInfo:
      type: number
      displayName: Organization ID
      name: organization_id
  - id: person_id
    name: Person ID
    type: number
    default: 0
    required: true
    description: ID of the person to link to this lead
    validation: *id005
    typeInfo: *id006
  - id: content
    name: Content
    type: string
    default: ''
    required: true
    description: The content of the note to create
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - note
    typeInfo:
      type: string
      displayName: Content
      name: content
      typeOptions:
        rows: 5
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the organization to create
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - person
    typeInfo: &id008
      type: string
      displayName: Name
      name: name
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: The name of the person to create
    validation: *id007
    typeInfo: *id008
- id: delete
  name: Delete
  description: Delete an activity
  params:
  - id: activityId
    name: Activity ID
    type: number
    default: 0
    required: true
    description: ID of the activity to delete
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - activity
    typeInfo: &id010
      type: number
      displayName: Activity ID
      name: activityId
  - id: dealId
    name: Deal ID
    type: number
    default: 0
    required: true
    description: ID of the deal to delete
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - dealActivity
    typeInfo: &id012
      type: options
      displayName: Deal Name or ID
      name: dealId
      typeOptions:
        loadOptionsMethod: getDeals
      possibleValues: []
  - id: fileId
    name: File ID
    type: number
    default: 0
    required: true
    description: ID of the file to delete
    validation: &id013
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - file
    typeInfo: &id014
      type: number
      displayName: File ID
      name: fileId
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of the lead to delete
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - update
    typeInfo: &id016
      type: string
      displayName: Lead ID
      name: leadId
  - id: noteId
    name: Note ID
    type: number
    default: 0
    required: true
    description: ID of the note to delete
    validation: &id017
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - note
    typeInfo: &id018
      type: number
      displayName: Note ID
      name: noteId
  - id: organizationId
    name: Organization ID
    type: number
    default: 0
    required: true
    description: ID of the organization to delete
    validation: &id019
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - organization
    typeInfo: &id020
      type: number
      displayName: Organization ID
      name: organizationId
  - id: personId
    name: Person ID
    type: number
    default: 0
    required: true
    description: ID of the person to delete
    validation: &id021
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - person
    typeInfo: &id022
      type: number
      displayName: Person ID
      name: personId
- id: get
  name: Get
  description: Get data of an activity
  params:
  - id: activityId
    name: Activity ID
    type: number
    default: 0
    required: true
    description: ID of the activity to get
    validation: *id009
    typeInfo: *id010
  - id: dealId
    name: Deal ID
    type: number
    default: 0
    required: true
    description: ID of the deal to get
    validation: *id011
    typeInfo: *id012
  - id: fileId
    name: File ID
    type: number
    default: 0
    required: true
    description: ID of the file to get
    validation: *id013
    typeInfo: *id014
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of the lead to retrieve
    validation: *id015
    typeInfo: *id016
  - id: noteId
    name: Note ID
    type: number
    default: 0
    required: true
    description: ID of the note to get
    validation: *id017
    typeInfo: *id018
  - id: organizationId
    name: Organization ID
    type: number
    default: 0
    required: true
    description: ID of the organization to get
    validation: *id019
    typeInfo: *id020
  - id: personId
    name: Person ID
    type: number
    default: 0
    required: true
    description: ID of the person to get
    validation: *id021
    typeInfo: *id022
  - id: resolveProperties
    name: Resolve Properties
    type: boolean
    default: false
    required: false
    description: By default do custom properties get returned only as ID instead of
      their actual name. Also option fields contain only the ID instead of their actual
      value. If this option gets set they get automatically resolved.
    validation: &id023
      displayOptions:
        show:
          resource:
          - activity
          - deal
          - organization
          - person
          - product
          operation:
          - get
          - getAll
    typeInfo: &id024
      type: boolean
      displayName: Resolve Properties
      name: resolveProperties
- id: getAll
  name: Get Many
  description: Get data of many activities
  params:
  - id: dealId
    name: Deal Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the deal whose products to retrieve. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id011
    typeInfo: *id012
  - id: resolveProperties
    name: Resolve Properties
    type: boolean
    default: false
    required: false
    description: By default do custom properties get returned only as ID instead of
      their actual name. Also option fields contain only the ID instead of their actual
      value. If this option gets set they get automatically resolved.
    validation: *id023
    typeInfo: *id024
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id025
      displayOptions:
        show:
          operation:
          - getAll
    typeInfo: &id026
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id027
      displayOptions:
        show:
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id028
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: dealId
    name: Deal Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the deal whose activity to retrieve. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id011
    typeInfo: *id012
- id: update
  name: Update
  description: Update an activity
  params:
  - id: activityId
    name: Activity ID
    type: number
    default: 0
    required: true
    description: ID of the activity to update
    validation: *id009
    typeInfo: *id010
  - id: dealId
    name: Deal ID
    type: number
    default: 0
    required: true
    description: ID of the deal to update
    validation: *id011
    typeInfo: *id012
  - id: dealId
    name: Deal Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the deal whose product to update. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id011
    typeInfo: *id012
  - id: productAttachmentId
    name: Product Attachment Name or ID
    type: options
    default: ''
    required: true
    description: ID of the deal-product (the ID of the product attached to the deal).
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id031
      required: true
      displayOptions:
        show:
          operation:
          - remove
          resource:
          - dealProduct
    typeInfo: &id032
      type: options
      displayName: Product Attachment Name or ID
      name: productAttachmentId
      typeOptions:
        loadOptionsMethod: getProductsDeal
      possibleValues: []
  - id: fileId
    name: File ID
    type: number
    default: 0
    required: true
    description: ID of the file to update
    validation: *id013
    typeInfo: *id014
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of the lead to update
    validation: *id015
    typeInfo: *id016
  - id: noteId
    name: Note ID
    type: number
    default: 0
    required: true
    description: ID of the note to update
    validation: *id017
    typeInfo: *id018
  - id: organizationId
    name: Organization ID
    type: number
    default: ''
    required: true
    description: The ID of the organization to create
    validation: *id019
    typeInfo: *id020
  - id: personId
    name: Person ID
    type: number
    default: 0
    required: true
    description: ID of the person to update
    validation: *id021
    typeInfo: *id022
  - id: encodeProperties
    name: Encode Properties
    type: boolean
    default: false
    required: false
    description: By default do custom properties have to be set as ID instead of their
      actual name. Also option fields have to be set as ID instead of their actual
      value. If this option gets set they get automatically encoded.
    validation:
      displayOptions:
        show:
          resource:
          - activity
          - deal
          - organization
          - person
          - product
          operation:
          - update
    typeInfo:
      type: boolean
      displayName: Encode Properties
      name: encodeProperties
- id: duplicate
  name: Duplicate
  description: Duplicate a deal
  params:
  - id: dealId
    name: Deal ID
    type: number
    default: 0
    required: true
    description: ID of the deal to duplicate
    validation: *id011
    typeInfo: *id012
- id: search
  name: Search
  description: Search a deal
  params:
  - id: term
    name: Term
    type: string
    default: ''
    required: true
    description: The search term to look for. Minimum 2 characters (or 1 if using
      exact_match).
    validation: &id029
      required: true
      displayOptions:
        show:
          operation:
          - search
          resource:
          - person
    typeInfo: &id030
      type: string
      displayName: Term
      name: term
  - id: exactMatch
    name: Exact Match
    type: boolean
    default: false
    required: false
    description: Whether only full exact matches against the given term are returned.
      It is not case sensitive.
    validation:
      displayOptions:
        show:
          operation:
          - search
          resource:
          - deal
    typeInfo:
      type: boolean
      displayName: Exact Match
      name: exactMatch
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id025
    typeInfo: *id026
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id027
    typeInfo: *id028
  - id: term
    name: Term
    type: string
    default: ''
    required: true
    description: The search term to look for. Minimum 2 characters (or 1 if using
      exact_match).
    validation: *id029
    typeInfo: *id030
  - id: term
    name: Term
    type: string
    default: ''
    required: true
    description: The search term to look for. Minimum 2 characters (or 1 if using
      exact_match).
    validation: *id029
    typeInfo: *id030
- id: add
  name: Add
  description: Add a product to a deal
  params:
  - id: dealId
    name: Deal Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the deal to add a product to. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id011
    typeInfo: *id012
  - id: productId
    name: Product Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the product to add to a deal. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - add
          resource:
          - dealProduct
    typeInfo:
      type: options
      displayName: Product Name or ID
      name: productId
      typeOptions:
        loadOptionsMethod: getProducts
      possibleValues: []
  - id: item_price
    name: Item Price
    type: number
    default: 0
    required: true
    description: Price at which to add or update this product in a deal
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - add
          resource:
          - dealProduct
    typeInfo:
      type: number
      displayName: Item Price
      name: item_price
      typeOptions:
        numberPrecision: 2
  - id: quantity
    name: Quantity
    type: number
    default: 1
    required: true
    description: How many items of this product to add/update in a deal
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - add
          resource:
          - dealProduct
    typeInfo:
      type: number
      displayName: Quantity
      name: quantity
      typeOptions:
        minValue: 1
- id: remove
  name: Remove
  description: Remove a product from a deal
  params:
  - id: dealId
    name: Deal Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the deal whose product to remove. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id011
    typeInfo: *id012
  - id: productAttachmentId
    name: Product Attachment Name or ID
    type: options
    default: ''
    required: true
    description: ID of the deal-product (the ID of the product attached to the deal).
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id031
    typeInfo: *id032
- id: download
  name: Download
  description: Download a file
  params:
  - id: fileId
    name: File ID
    type: number
    default: 0
    required: true
    description: ID of the file to download
    validation: *id013
    typeInfo: *id014
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: *id033
    typeInfo: *id034
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
  - field: type
    text: call
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: filters
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be written
  - field: binaryPropertyName
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
  "$id": "https://n8n.io/schemas/nodes/pipedrive.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Pipedrive Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "get",
        "getAll",
        "update",
        "duplicate",
        "search",
        "add",
        "remove",
        "download"
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
            "apiToken",
            "oAuth2"
          ],
          "default": "apiToken"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "activity",
            "deal",
            "dealActivity",
            "dealProduct",
            "file",
            "lead",
            "note",
            "organization",
            "person",
            "product"
          ],
          "default": "deal"
        },
        "operation": {
          "description": "Get data of many products",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "getAll"
        },
        "subject": {
          "description": "The subject of the activity to create",
          "type": "string",
          "default": ""
        },
        "done": {
          "description": "Whether the activity is done or not",
          "type": "string",
          "enum": [
            "0",
            "1"
          ],
          "default": "0"
        },
        "type": {
          "description": "Type of the activity like \"call\", \"meeting\", etc",
          "type": "string",
          "default": "",
          "examples": [
            "call"
          ]
        },
        "additionalFields": {
          "description": "Whether the Activity is done or not. 0 = Not done, 1 = Done. If omitted returns both Done and Not done activities.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "activityId": {
          "description": "ID of the activity to update",
          "type": "number",
          "default": 0
        },
        "updateFields": {
          "description": "The fields to update",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "title": {
          "description": "Name of the lead to create",
          "type": "string",
          "default": ""
        },
        "associateWith": {
          "description": "Type of entity to link to this lead",
          "type": "string",
          "enum": [
            "organization",
            "person"
          ],
          "default": "organization"
        },
        "org_id": {
          "description": "ID of the organization this deal will be associated with",
          "type": "number",
          "default": 0
        },
        "person_id": {
          "description": "ID of the person to link to this lead",
          "type": "number",
          "default": 0
        },
        "dealId": {
          "description": "The ID of the deal whose activity to retrieve. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "productId": {
          "description": "The ID of the product to add to a deal. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "item_price": {
          "description": "Price at which to add or update this product in a deal",
          "type": "number",
          "default": 0
        },
        "quantity": {
          "description": "How many items of this product to add/update in a deal",
          "type": "number",
          "default": 1
        },
        "productAttachmentId": {
          "description": "ID of the deal-product (the ID of the product attached to the deal). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "term": {
          "description": "The search term to look for. Minimum 2 characters (or 1 if using exact_match).",
          "type": "string",
          "default": ""
        },
        "exactMatch": {
          "description": "Whether only full exact matches against the given term are returned. It is not case sensitive.",
          "type": "boolean",
          "default": false
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
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "fileId": {
          "description": "ID of the file to update",
          "type": "number",
          "default": 0
        },
        "organization_id": {
          "description": "ID of the organization to link to this lead",
          "type": "number",
          "default": 0
        },
        "leadId": {
          "description": "ID of the lead to update",
          "type": "string",
          "default": ""
        },
        "content": {
          "description": "The content of the note to create",
          "type": "string",
          "default": ""
        },
        "noteId": {
          "description": "ID of the note to update",
          "type": "number",
          "default": 0
        },
        "name": {
          "description": "The name of the person to create",
          "type": "string",
          "default": ""
        },
        "organizationId": {
          "description": "The ID of the organization to create",
          "type": "number",
          "default": ""
        },
        "personId": {
          "description": "ID of the person to update",
          "type": "number",
          "default": 0
        },
        "resolveProperties": {
          "description": "By default do custom properties get returned only as ID instead of their actual name. Also option fields contain only the ID instead of their actual value. If this option gets set they get automatically resolved.",
          "type": "boolean",
          "default": false
        },
        "encodeProperties": {
          "description": "By default do custom properties have to be set as ID instead of their actual name. Also option fields have to be set as ID instead of their actual value. If this option gets set they get automatically encoded.",
          "type": "boolean",
          "default": false
        },
        "filters": {
          "description": "Predefined filter to apply to the deals to retrieve. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
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
      "name": "pipedriveApi",
      "required": true
    },
    {
      "name": "pipedriveOAuth2Api",
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
